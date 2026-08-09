#!/usr/bin/env python3
"""Build evidence bundles for THEME articles (articles/factory/_themes.json).

Theme articles are editorially curated experiential topics the frequency
ranking is structurally blind to: the census grades a mention `explains` only
when the concept itself is explained, so story-shaped knowledge (Shenzhen 62
episodes / 6 explains, teardown 67 / 11) never clears the topic lane's floor.

Two differences from the topic lane (see DESIGN.md):

1. DEPTH-RELAXED. `mention`-depth passages are gathered too, because the
   narratives live there. The knowledge-only rule is not dropped, it moves to
   the claim level during extraction: anchored experience is the standard
   ("bring cash to Huaqiangbei" survives, "China was wild" dies).

2. TWO GATHERING MODES.
   - concept-union: every passage touching any member concept.
   - guest-episode: every passage from a domain-guest's episodes, then
     relevance-filtered, for themes carried by who was talking rather than by
     any concept (Mike Harrison installations, Bil Herd retrocomputing).

Reuses the topic bundler's census index, transcript loader and speaker repair,
so passage shape — crucially `text`, the field quotes are verified against —
is identical to a topic bundle and verify_packet.py works unchanged.

  python3 build_theme_bundles.py            # every ungated theme
  python3 build_theme_bundles.py <slug> ... # named themes only
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_bundles as bb           # noqa: E402  (module-level census index)

ROOT = bb.ROOT
THEMES = os.path.join(ROOT, "articles/factory/_themes.json")
OUTDIR = os.path.join(ROOT, "articles/factory/bundles")
CAP = 300                            # themes run wider than topics (250)

# Guests who carry a tier-3 theme. The manifest names the theme, not the
# people; these are the domain guests whose episodes ARE the evidence.
THEME_GUESTS = {
    "broadcast-and-big-installs": ["Mike Harrison"],
    "retrocomputing": ["Bil Herd", "Fran Blanche"],
    "failures-and-recalls": [],       # no single guest; concept seed + filter
    "debugging-war-stories": [],
}

# Relevance filter for guest-episode mode: a guest's episode ranges over
# everything, so passages must touch the theme's subject to be gathered.
THEME_FILTER = {
    # Word-bounded and case-sensitive where it matters: under re.I a bare
    # "LED" also matches the verb "led", and "show" matches "the show" in
    # every episode of a podcast, which drags in the entire corpus.
    "broadcast-and-big-installs": r"""
        \binstallation|\binstalls?\b|stage light|lighting rig|broadcast|
        projector|projection|theatre|theater|museum|exhibit|\bvenue|arena|
        billboard|display wall|rigging|\btruss|dimmer|\bDMX\b|
        pixel|nixie|\bneon\b|high.voltage|\bLEDs\b|LED (?:strip|panel|wall|
        matrix|driver|display)""",
    "retrocomputing": r"""
        \bretro|vintage|Commodore|\bC64\b|\bVIC\b|Amiga|8.bit|\bROM\b|
        EPROM|cassette|floppy|restorat|refurb|museum|archaeolog|emulat|
        old (?:computer|machine|gear|scope|board)|core memory|
        \bCRT\b|tube|reverse.engineer""",
    "failures-and-recalls": r"""
        \brecall|caught fire|\bfire\b|burned? (?:up|out|down)|blew up|
        exploded|field failure|failure in the field|\bRMA\b|warranty|
        bricked|dead on arrival|\bDOA\b|lawsuit|liability|\bdefect|
        scrapped|safety (?:issue|recall|certif)""",
    "debugging-war-stories": r"""
        \bdebug|\bbugs?\b|intermittent|root cause|tracked it down|
        three days|two weeks|turned out (?:to be|it)|finally found|
        chasing|\brepro\b|glitch|heisenbug""",
}


def load_themes():
    d = json.load(open(THEMES))
    return {t["slug"]: t for t in d["themes"]}


def citable(stem):
    """Three transcripts carry no episode number; a claim from them could
    never be cited, so they are dropped rather than gathered."""
    return bb.EPMETA.get(stem, {}).get("episode") is not None


def passage(stem, pi, paras, depth, concept, src):
    """Same shape as a topic-bundle passage (bb.collect)."""
    spk_raw = paras[pi]["speaker_raw"]
    spk = bb.repair(stem, spk_raw) if spk_raw else None
    text = paras[pi]["text"]
    before = paras[pi - 1]["text"] if pi - 1 >= 0 else ""
    after = paras[pi + 1]["text"] if pi + 1 < len(paras) else ""
    meta = bb.EPMETA[stem]
    return {
        "episode": meta["episode"],
        "episode_title": meta["title"],
        "episode_url": meta["url"],
        "guest": meta["guest"],
        "stem": stem,
        "paragraph_index": pi,
        "depth": depth,
        "speaker_raw": spk_raw,
        "speaker_repaired": spk,
        "attribution_reliable": stem not in bb.UNRELIABLE,
        "fused_turns": stem in bb.FUSED,
        "concept_source": src,
        "concepts": [concept] if concept else [],
        "paragraph_text": text,
        "context_before": before[-bb.CTX_CHARS:],
        "context_after": after[:bb.CTX_CHARS],
        "context_before_speaker": (
            bb.repair(stem, paras[pi - 1]["speaker_raw"])
            if pi - 1 >= 0 and paras[pi - 1]["speaker_raw"] else None),
        "context_after_speaker": (
            bb.repair(stem, paras[pi + 1]["speaker_raw"])
            if pi + 1 < len(paras) and paras[pi + 1]["speaker_raw"] else None),
        "text": " ".join(x for x in (before[-bb.CTX_CHARS:], text,
                                     after[:bb.CTX_CHARS]) if x),
    }


def gather_concept_union(theme):
    """Every passage touching any member concept, all depths kept."""
    seen, depth_counts, episodes = {}, Counter(), set()
    for concept in theme.get("concepts", []):
        for stem, m in bb.BY_CONCEPT.get(concept, ()):
            pi = m.get("paragraph_index")
            if pi is None:
                continue
            if not citable(stem):
                continue
            _fm, paras = bb.load_transcript(stem)
            if not (0 <= pi < len(paras)):
                continue
            spk_raw = paras[pi]["speaker_raw"] or m.get("speaker")
            if spk_raw and bb.repair(stem, spk_raw) == "__SPONSOR_READ__":
                continue
            depth = m.get("depth") or "mention"
            key = (stem, pi)
            if key in seen:
                if concept not in seen[key]["concepts"]:
                    seen[key]["concepts"].append(concept)
                if depth == "explains":
                    seen[key]["depth"] = "explains"
                continue
            depth_counts[depth] += 1
            episodes.add(bb.EPMETA[stem]["episode"])
            seen[key] = passage(stem, pi, paras, depth, concept,
                                f"theme-concept:{concept}")
    return list(seen.values()), depth_counts, episodes


def gather_guest_episode(theme):
    """Every passage from the theme guests' episodes, relevance-filtered.

    Seed concepts are also swept so a theme with a thin guest list still finds
    its material; the filter applies to both.
    """
    slug = theme["slug"]
    guests = THEME_GUESTS.get(slug, [])
    pat = re.compile(THEME_FILTER[slug], re.I | re.X)
    seen, depth_counts, episodes = {}, Counter(), set()

    stems = [s for s, meta in bb.EPMETA.items()
             if meta.get("guest") in guests] if guests else []

    # depth by (stem, paragraph) from the census, for whatever it graded
    graded = defaultdict(str)
    for concept in theme.get("concepts", []):
        for stem, m in bb.BY_CONCEPT.get(concept, ()):
            if m.get("paragraph_index") is not None:
                graded[(stem, m["paragraph_index"])] = m.get("depth") or "mention"
            if stem not in stems:
                stems.append(stem)

    for stem in stems:
        if not citable(stem):
            continue
        _fm, paras = bb.load_transcript(stem)
        for pi, para in enumerate(paras):
            # match the passage's OWN paragraph, not its neighbours: matching
            # the context window drags in whatever was said either side of a
            # single on-topic word, which is mostly banter
            if not pat.search(para["text"]):
                continue
            spk_raw = para["speaker_raw"]
            if spk_raw and bb.repair(stem, spk_raw) == "__SPONSOR_READ__":
                continue
            if len(para["text"]) < 60:          # skip back-channel turns
                continue
            depth = graded.get((stem, pi), "mention")
            depth_counts[depth] += 1
            episodes.add(bb.EPMETA[stem]["episode"])
            seen[(stem, pi)] = passage(stem, pi, paras, depth, None,
                                       "theme-guest")
    return list(seen.values()), depth_counts, episodes


def cap(passages):
    """explains first, then opinion, then mention — each spread over episodes."""
    if len(passages) <= CAP:
        return passages, False
    order = {"explains": 0, "opinion": 1}
    tiers = defaultdict(list)
    for p in passages:
        tiers[order.get(p["depth"], 2)].append(p)
    out = []
    for t in sorted(tiers):
        byep = defaultdict(list)
        for p in tiers[t]:
            byep[p["episode"]].append(p)
        # round-robin across episodes so one episode cannot dominate
        while byep and len(out) < CAP:
            for ep in sorted(byep):
                if byep[ep]:
                    out.append(byep[ep].pop(0))
                if len(out) >= CAP:
                    break
            byep = {e: v for e, v in byep.items() if v}
        if len(out) >= CAP:
            break
    out.sort(key=lambda p: (p["episode"], p["paragraph_index"]))
    return out, True


def build(theme):
    slug = theme["slug"]
    mode = theme["gathering"]
    if mode == "concept-union":
        passages, depths, episodes = gather_concept_union(theme)
    else:
        passages, depths, episodes = gather_guest_episode(theme)
    total = len(passages)
    passages, capped = cap(passages)
    out = {
        "concept": slug,
        "name": theme["title"],
        "lane": "theme",
        "tier": theme.get("tier"),
        "scope": theme.get("scope"),
        "gathering": mode,
        "cluster": {"core": theme.get("concepts", []), "children": [],
                    "neighbors": []},
        "guests": THEME_GUESTS.get(slug, []),
        "stats": {
            "episodes": len(episodes),
            "mentions": total,
            "explains": depths["explains"],
            "opinions": depths["opinion"],
            "mentions_depth": depths["mention"],
            "passages_by_depth": dict(Counter(p["depth"] for p in passages)),
        },
        "capped": capped,
        "total_available": total,
        "passages": passages,
    }
    path = os.path.join(OUTDIR, slug + ".json")
    json.dump(out, open(path, "w"), indent=1)
    return out


def main():
    themes = load_themes()
    want = sys.argv[1:]
    if want:
        sel = [themes[s] for s in want]
    else:
        sel = [t for t in themes.values() if not t.get("gate")]
        skipped = [t["slug"] for t in themes.values() if t.get("gate")]
        if skipped:
            print(f"gated, not built: {', '.join(skipped)}", file=sys.stderr)
    for t in sel:
        b = build(t)
        s = b["stats"]
        print(f"{b['concept']:36} {b['gathering']:15} "
              f"eps={s['episodes']:4} passages={len(b['passages']):4} "
              f"(of {b['total_available']:5}) "
              f"explains={s['explains']:4} op={s['opinions']:4} "
              f"ment={s['mentions_depth']:5}")


if __name__ == "__main__":
    main()
