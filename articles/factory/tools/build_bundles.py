#!/usr/bin/env python3
"""Build evidence bundles for every status=article concept (factory prep).

Generalises the altium-v4 cluster gather (scratchpad/cluster_gather.py) to all
412 article concepts.

Evidence scope for a concept C:
  core      = C + every alias that canonicalises to C
  children  = concepts whose candidates.json suggested.parent == C
  neighbors = graph cooccur edges touching C with weight >= NEIGHBOR_W whose
              own suggested.status is NOT 'article' (article-status neighbours
              get their own bundle, so their evidence is not pulled in here)

Core passages are taken unconditionally. Child/neighbour passages are kept only
when the +-1 paragraph window carries a lexical hit for C itself or one of its
aliases -- the mechanical form of "a hiring discussion that never mentions the
subject does not belong in the subject's article". If gating would leave a
bundle under RELAX_FLOOR passages the gate is dropped for that bundle and
gate_relaxed is recorded.

Usage:
  python3 build_bundles.py            # all 412
  python3 build_bundles.py altium ... # named concepts only (debug)
"""
import json, os, re, sys, time
from collections import defaultdict, Counter

ROOT = "/Users/frankwalsh/Documents/vibecoding/amp_hour_wiki"
CENSUS = os.path.join(ROOT, "census/union")
TRANS = os.path.join(ROOT, "transcripts")
OUTDIR = os.path.join(ROOT, "articles/factory/bundles")

CAP = 250
NEIGHBOR_W = 4
RELAX_FLOOR = 10          # below this, retry a bundle without the lexical gate
CTX_CHARS = 800           # chars of +-1 paragraph context kept
HOSTS = ("Dave Jones", "Chris Gammell")

ACRONYMS = {
    "3d", "ac", "adc", "ai", "am", "api", "arm", "asic", "atx", "awg", "bga",
    "ble", "bom", "can", "ccd", "cad", "cam", "cnc", "cpu", "crt", "css", "dac",
    "dc", "ddr", "dfm", "diy", "dmm", "dram", "dsl", "dsp", "dut", "dvd", "eda",
    "eeprom", "emc", "emf", "emi", "esd", "esr", "eu", "fcc", "fet", "ffc",
    "fpga", "fr4", "ftdi", "gnd", "gps", "gpu", "gsm", "gui", "hdl", "hdmi",
    "hf", "hp", "html", "http", "hvac", "i2c", "i2s", "ic", "ide", "ieee",
    "io", "iot", "ip", "ir", "isp", "jtag", "json", "kicad", "lcd", "led",
    "lidar", "lipo", "llc", "lna", "lora", "lte", "mcu", "mems", "mit", "mosfet",
    "mp3", "nasa", "nda", "nfc", "npn", "nvme", "oem", "opamp", "os", "ota",
    "pcb", "pcba", "pcie", "pdf", "pll", "pnp", "pob", "poe", "ppm", "psu",
    "pwm", "qfn", "rf", "rfid", "rgb", "rhs", "rma", "rms", "roi", "rohs",
    "rtos", "sata", "sdk", "sdr", "sem", "smd", "smps", "smt", "soc", "spi",
    "sram", "ssd", "svg", "swd", "tft", "tsmc", "tv", "uart", "ui", "url",
    "usa", "usb", "usd", "uv", "vco", "vhdl", "vna", "vr", "xyz",
}
LOWER_WORDS = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on",
               "or", "the", "to", "vs", "with"}

# Slugs whose conventional spelling no rule reproduces.
SPECIAL_NAMES = {
    "2-4-ghz-band": "2.4 GHz Band", "circuitpython": "CircuitPython",
    "cmos": "CMOS", "cpld": "CPLD", "dc-dc-converter": "DC-DC Converter",
    "digi-key": "Digi-Key", "dma": "DMA", "eagle": "EAGLE", "esp32": "ESP32",
    "esp8266": "ESP8266", "flip-flop": "Flip-Flop", "fr4": "FR-4",
    "freertos": "FreeRTOS", "gcc": "GCC", "gdb": "GDB", "github": "GitHub",
    "gpio": "GPIO", "hackrf": "HackRF", "ism-band": "ISM Band",
    "kicad": "KiCad", "lora": "LoRa", "lorawan": "LoRaWAN", "ltspice": "LTspice",
    "maxwell-equations": "Maxwell's Equations", "micropython": "MicroPython",
    "moores-law": "Moore's Law", "ohms-law": "Ohm's Law", "op-amp": "Op-Amp",
    "pull-up-resistor": "Pull-Up Resistor", "ram": "RAM", "risc-v": "RISC-V",
    "sd-card": "SD Card", "serdes": "SerDes", "sparkfun": "SparkFun",
    "spice": "SPICE", "usb-c": "USB-C", "wifi": "Wi-Fi", "youtube": "YouTube",
}

print("loading inputs...", file=sys.stderr)
ALIAS = json.load(open(os.path.join(ROOT, "canon/alias_table_v2.json")))
SPK = json.load(open(os.path.join(ROOT, "canon/speaker_map.json")))
SPKMAP = SPK["files"]
UNRELIABLE = {e["file"] for e in SPK["attribution_unreliable"]}
FUSED = {k for k in SPK["fused_turn_files"] if not k.startswith("_")}
GRAPH = json.load(open(os.path.join(ROOT, "graph/graph.json")))
CAND = json.load(open(os.path.join(ROOT, "articles/candidates.json")))["candidates"]

STATUS = {c["concept"]: c["suggested"]["status"] for c in CAND}
PARENT = {c["concept"]: c["suggested"].get("parent") for c in CAND}
CANDBY = {c["concept"]: c for c in CAND}
ARTICLES = [c["concept"] for c in
            sorted((c for c in CAND if c["suggested"]["status"] == "article"),
                   key=lambda c: -c.get("score", 0))]

ALIASES_OF = defaultdict(set)
for a, canon in ALIAS.items():
    ALIASES_OF[canon].add(a)

CHILDREN_OF = defaultdict(list)
for c, p in PARENT.items():
    if p:
        CHILDREN_OF[p].append(c)

NBRS_OF = defaultdict(dict)
for e in GRAPH["edges"]:
    if e.get("kind") != "cooccur":
        continue
    w = e.get("weight", 0)
    if w < NEIGHBOR_W:
        continue
    s, t = e["source"], e["target"]
    NBRS_OF[s][t] = max(NBRS_OF[s].get(t, 0), w)
    NBRS_OF[t][s] = max(NBRS_OF[t].get(s, 0), w)


def title_case(slug):
    if slug in SPECIAL_NAMES:
        return SPECIAL_NAMES[slug]
    out = []
    for i, w in enumerate(slug.split("-")):
        if w in ACRONYMS:
            out.append(w.upper())
        elif i and w in LOWER_WORDS:
            out.append(w)
        elif w and w[0].isdigit():
            out.append(w)
        else:
            out.append(w[:1].upper() + w[1:])
    return " ".join(out)


def core_regex(slugs):
    """Flexible word-level regex matching any of the concept's own surface forms."""
    pats = []
    for s in sorted(slugs, key=len, reverse=True):
        words = [w for w in re.split(r"[^a-z0-9]+", s.lower()) if w]
        if not words:
            continue
        if len(words) == 1 and len(words[0]) <= 2:
            continue                      # too short to gate on safely
        pats.append(r"[\s\-/]*".join(re.escape(w) for w in words))
    if not pats:
        return None
    return re.compile(r"\b(?:" + "|".join(pats) + r")\w{0,3}\b", re.I)


# ---------------------------------------------------------------- transcripts
_tcache = {}


def load_transcript(stem):
    if stem in _tcache:
        return _tcache[stem]
    path = os.path.join(TRANS, stem + ".md")
    if not os.path.exists(path):
        _tcache[stem] = ({}, [])
        return _tcache[stem]
    raw = open(path, encoding="utf-8").read()
    fm, body = {}, raw
    if raw.startswith("---"):
        try:
            end = raw.index("\n---", 3)
            for line in raw[3:end].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
            body = raw[end + 4:]
        except ValueError:
            pass
    paras = []
    for p in body.lstrip("\n").split("\n\n"):
        if not p.strip():
            continue
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", p.strip(), re.S)
        paras.append({"speaker_raw": m.group(1), "text": m.group(2)} if m
                     else {"speaker_raw": None, "text": p.strip()})
    _tcache[stem] = (fm, paras)
    return _tcache[stem]


def repair(stem, raw):
    ent = SPKMAP.get(stem, {}).get(raw)
    return ent["canonical_person"] if ent else raw


# ------------------------------------------------------------------- census
print("indexing census...", file=sys.stderr)
EPMETA = {}                                   # stem -> episode metadata
BY_CONCEPT = defaultdict(list)                # canonical concept -> [(stem, mention)]
for fn in sorted(os.listdir(CENSUS)):
    if fn.startswith("_") or not fn.endswith(".json"):
        continue
    stem = fn[:-5]
    d = json.load(open(os.path.join(CENSUS, fn)))
    EPMETA[stem] = {"episode": d.get("episode"), "title": d.get("title"),
                    "url": d.get("url"), "guest": d.get("guest_name")}
    for m in d.get("mentions", []):
        canon = ALIAS.get(m["concept"], m["concept"])
        BY_CONCEPT[canon].append((stem, m))
        if canon != m["concept"]:
            BY_CONCEPT[m["concept"]].append((stem, m))
print(f"  {len(EPMETA)} episodes, {len(BY_CONCEPT)} concept keys", file=sys.stderr)


def build_cluster(target):
    aliases = set(ALIASES_OF.get(target, ())) | {target}
    children = sorted(set(CHILDREN_OF.get(target, ())) - aliases)
    nbrw = {o: w for o, w in NBRS_OF.get(target, {}).items()
            if STATUS.get(o) != "article"}
    neighbors = sorted(set(nbrw) - set(children) - aliases)
    return aliases, children, neighbors, nbrw


def collect(target, aliases, children, neighbors, gate_re, gated):
    """Walk every mention in scope; return (passages, stats-counters)."""
    role = {}
    for a in aliases:
        role[a] = ("core", None)
    for c in children:
        role.setdefault(c, ("child", c))
    for n in neighbors:
        role.setdefault(n, ("neighbor", n))

    seen_pass, episodes, seen_mentions = {}, set(), set()
    n_mentions = 0
    depth_counts = Counter()
    gated_out = Counter()

    for concept, (r, src_name) in role.items():
        for stem, m in BY_CONCEPT.get(concept, ()):
            pi = m.get("paragraph_index")
            if pi is None:
                continue
            mid = (stem, pi, m.get("char_start"), m["concept"])
            if mid in seen_mentions:      # same mention reachable via alias + canon key
                continue
            seen_mentions.add(mid)
            fm, paras = load_transcript(stem)
            if not (0 <= pi < len(paras)):
                continue
            spk_raw = paras[pi]["speaker_raw"] or m.get("speaker")
            spk = repair(stem, spk_raw) if spk_raw else None
            if spk == "__SPONSOR_READ__":
                continue
            text = paras[pi]["text"]
            before = paras[pi - 1]["text"] if pi - 1 >= 0 else ""
            after = paras[pi + 1]["text"] if pi + 1 < len(paras) else ""

            if r != "core" and gated and gate_re is not None:
                if not gate_re.search(" ".join((before, text, after))):
                    gated_out[concept] += 1
                    continue

            ep = EPMETA[stem]["episode"]
            episodes.add(ep)
            n_mentions += 1
            depth = m.get("depth")
            depth_counts[depth] += 1
            if depth not in ("explains", "opinion"):
                continue

            src = "core" if r == "core" else f"{r}:{src_name}"
            key = (stem, pi)
            cur = seen_pass.get(key)
            if cur is None:
                seen_pass[key] = {
                    "episode": ep,
                    "episode_title": EPMETA[stem]["title"],
                    "episode_url": EPMETA[stem]["url"],
                    "guest": EPMETA[stem]["guest"],
                    "stem": stem,
                    "paragraph_index": pi,
                    "depth": depth,
                    "speaker_raw": spk_raw,
                    "speaker_repaired": spk,
                    "attribution_reliable": stem not in UNRELIABLE,
                    "fused_turns": stem in FUSED,
                    "concept_source": src,
                    "concept_sources": [src],
                    "concepts": [concept],
                    "paragraph_text": text,
                    "context_before": before[-CTX_CHARS:],
                    "context_after": after[:CTX_CHARS],
                    "context_before_speaker": (
                        repair(stem, paras[pi - 1]["speaker_raw"])
                        if pi - 1 >= 0 and paras[pi - 1]["speaker_raw"] else None),
                    "context_after_speaker": (
                        repair(stem, paras[pi + 1]["speaker_raw"])
                        if pi + 1 < len(paras) and paras[pi + 1]["speaker_raw"] else None),
                }
            else:
                if src not in cur["concept_sources"]:
                    cur["concept_sources"].append(src)
                if concept not in cur["concepts"]:
                    cur["concepts"].append(concept)
                if depth == "explains":
                    cur["depth"] = "explains"
                rank = {"core": 0, "child": 1, "neighbor": 2}
                if rank[src.split(":")[0]] < rank[cur["concept_source"].split(":")[0]]:
                    cur["concept_source"] = src

    passages = list(seen_pass.values())
    for p in passages:
        p["concept_sources"].sort()
        p["concepts"].sort()
        p["text"] = " ".join(x for x in (p["context_before"], p["paragraph_text"],
                                         p["context_after"]) if x)
    return passages, {
        "episodes": len(episodes),
        "mentions": n_mentions,
        "explains": depth_counts["explains"],
        "opinions": depth_counts["opinion"],
        "gated_out": sum(gated_out.values()),
        "gated_out_by_concept": gated_out.most_common(15),
    }


def apply_cap(passages):
    """All explains first, then opinion by speaker diversity + recency."""
    if len(passages) <= CAP:
        return passages, False
    ex = [p for p in passages if p["depth"] == "explains"]
    op = [p for p in passages if p["depth"] != "explains"]
    byspk = defaultdict(list)
    for p in sorted(op, key=lambda x: -(x["episode"] or 0)):
        byspk[p["speaker_repaired"]].append(p)
    order = sorted(byspk, key=lambda s: (s in HOSTS, -len(byspk[s]), str(s)))
    picked, i = [], 0
    while len(ex) + len(picked) < CAP:
        added = False
        for s in order:
            if i < len(byspk[s]):
                picked.append(byspk[s][i])
                added = True
                if len(ex) + len(picked) >= CAP:
                    break
        if not added:
            break
        i += 1
    return ex[:CAP] + picked, True


def build(target):
    aliases, children, neighbors, nbrw = build_cluster(target)
    gate_re = core_regex(aliases)
    passages, stats = collect(target, aliases, children, neighbors, gate_re, True)
    gate_relaxed = False
    if len(passages) < RELAX_FLOOR and (children or neighbors) and gate_re is not None:
        p2, s2 = collect(target, aliases, children, neighbors, gate_re, False)
        if len(p2) > len(passages):
            passages, stats, gate_relaxed = p2, s2, True

    total_available = len(passages)
    passages, capped = apply_cap(passages)
    passages.sort(key=lambda p: (p["episode"] or 0, p["paragraph_index"]))

    cand = CANDBY[target]
    bundle = {
        "concept": target,
        "name": title_case(target),
        "type": cand.get("type"),
        "score": cand.get("score"),
        "rank_by_score": cand.get("rank_by_score"),
        "cluster": {
            "core": sorted(aliases),
            "children": children,
            "neighbors": [{"concept": n, "weight": nbrw[n]} for n in
                          sorted(neighbors, key=lambda n: (-nbrw[n], n))],
        },
        "stats": {
            "episodes": stats["episodes"],
            "mentions": stats["mentions"],
            "explains": stats["explains"],
            "opinions": stats["opinions"],
            "candidate_episode_count": cand.get("episode_count"),
            "candidate_mention_count": cand.get("mention_count"),
            "gated_out": stats["gated_out"],
            "gated_out_by_concept": stats["gated_out_by_concept"],
            "gate_relaxed": gate_relaxed,
            "unreliable_attribution_passages": sum(
                1 for p in passages if not p["attribution_reliable"]),
            "speakers": Counter(p["speaker_repaired"] for p in passages).most_common(20),
            "passages_by_source_role": dict(Counter(
                p["concept_source"].split(":")[0] for p in passages)),
            "passages_by_depth": dict(Counter(p["depth"] for p in passages)),
        },
        "cap": CAP,
        "capped": capped,
        "total_available": total_available,
        "passages": passages,
    }
    return bundle


def main():
    targets = sys.argv[1:] or ARTICLES
    os.makedirs(OUTDIR, exist_ok=True)
    manifest, t0 = [], time.time()
    for i, t in enumerate(targets, 1):
        b = build(t)
        path = os.path.join(OUTDIR, t + ".json")
        json.dump(b, open(path, "w"), indent=1)
        manifest.append({
            "concept": t, "name": b["name"], "rank_by_score": b["rank_by_score"],
            "bundle": os.path.relpath(path, ROOT),
            "bundle_bytes": os.path.getsize(path),
            "passages": len(b["passages"]), "total_available": b["total_available"],
            "capped": b["capped"], "episodes": b["stats"]["episodes"],
            "mentions": b["stats"]["mentions"], "explains": b["stats"]["explains"],
            "opinions": b["stats"]["opinions"],
            "children": len(b["cluster"]["children"]),
            "neighbors": len(b["cluster"]["neighbors"]),
            "gate_relaxed": b["stats"]["gate_relaxed"],
            "gated_out": b["stats"]["gated_out"],
            "unreliable_attribution_passages":
                b["stats"]["unreliable_attribution_passages"],
            "thin_risk": len(b["passages"]) < RELAX_FLOOR,
        })
        if i % 25 == 0 or i == len(targets):
            print(f"  [{i}/{len(targets)}] {t}  {len(b['passages'])} passages"
                  f"  ({time.time()-t0:.0f}s)", file=sys.stderr)
    json.dump(manifest, open(os.path.join(
        os.path.dirname(OUTDIR), "_manifest_rows.json"), "w"), indent=1)
    print(json.dumps({"bundles": len(manifest),
                      "passages": sum(m["passages"] for m in manifest),
                      "capped": sum(1 for m in manifest if m["capped"]),
                      "thin": sum(1 for m in manifest if m["thin_risk"]),
                      "seconds": round(time.time() - t0, 1)}, indent=1))


if __name__ == "__main__":
    main()
