#!/usr/bin/env python3
"""Lint a generated article against the packet it was written from.

  python3 lint.py --article articles/factory/articles/altium.md \
                  --packet  articles/factory/packets/altium-v4.json [--json]

Checks
  1. every [NNN] citation in the body traces to a packet claim's episode
  2. cited episodes and References-table rows agree in both directions
  3. every quoted string of 12+ chars is verbatim inside some quote_verbatim
  4. reception-language tripwire (spec forbids reception material anywhere)
  5. meta-commentary tripwire (podcast / hosts / this article / the archive)
  6. every prose line carries at least one citation
  7. References table is well formed: 4 columns, no invented dates, ordered
  8. frontmatter present with title/concept, concept matching the packet

Exit 0 on pass, 1 on fail.
"""
import argparse, json, os, re, sys, time

RECEPTION = re.compile(
    r"\bcame around\b|\badoption\b|\bdismissed\b|\bhosts disagreed\b|\breception\b|"
    r"\bdivided\b|\bwidely praised\b|\bcriticis|\bcriticiz|\bwas well received\b|"
    r"\bwarmly received\b|\bfan favourite\b|\bfan favorite\b", re.I)
META = re.compile(
    r"\bpodcast\b|\bthe archive\b|\bthe show\b|\bthis article\b|\bthe hosts\b|"
    r"\bepisode \d+ (?:covers|discusses)\b|\bthe reader\b|\bthe takeaway\b|"
    r"\bthis page\b|\bthe episode\b|\bin conversation\b", re.I)
DATE_OK = re.compile(
    r"^(?:January|February|March|April|May|June|July|August|September|October|"
    r"November|December) \d{1,2}, \d{4}$")

norm = lambda s: re.sub(r"\s+", " ", s).strip()


def lint(article_path, packet_path):
    t0 = time.monotonic()
    art = open(article_path, encoding="utf-8").read()
    pkt = json.load(open(packet_path))
    claims = pkt["claims"]
    pkt_eps = {c["episode"] for c in claims}
    quotes = [c.get("quote_verbatim") or "" for c in claims]

    fail, warn = [], []
    body = art.split("## References")[0]
    ref = art.split("## References", 1)[1] if "## References" in art else ""

    # 8. frontmatter
    if not art.startswith("---"):
        fail.append("no YAML frontmatter")
    else:
        fm = art[3:art.index("\n---", 3)] if "\n---" in art[3:] else ""
        for k in ("title:", "concept:"):
            if k not in fm:
                fail.append(f"frontmatter missing {k}")
        m = re.search(r"^concept:\s*(\S+)", fm, re.M)
        if m and m.group(1) != pkt["concept"]:
            fail.append(f"frontmatter concept {m.group(1)!r} != packet "
                        f"{pkt['concept']!r}")

    # 1-2. citations
    cited = {int(n) for n in re.findall(r"\[(\d{1,3})\]", body)}
    unknown = sorted(cited - pkt_eps)
    if unknown:
        fail.append(f"citations with no packet claim: {unknown}")
    if not ref:
        fail.append("no '## References' section")
    ref_eps = [int(m.group(1)) for m in re.finditer(r"^\|\s*(\d{1,3})\s*\|", ref, re.M)]
    ref_set = set(ref_eps)
    if cited - ref_set:
        fail.append(f"cited but missing from References: {sorted(cited - ref_set)}")
    if ref_set - cited:
        fail.append(f"in References but never cited: {sorted(ref_set - cited)}")
    if ref_eps != sorted(ref_eps):
        fail.append("References table not ordered by episode number")
    if len(ref_eps) != len(ref_set):
        fail.append("duplicate rows in References table")

    # 7. references rows well formed
    for line in ref.splitlines():
        if not re.match(r"^\|\s*\d{1,3}\s*\|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            fail.append(f"References row has {len(cells)} columns: {line.strip()}")
            continue
        if cells[3] and not DATE_OK.match(cells[3]):
            fail.append(f"malformed date in References: {cells[3]!r}")
        if cells[2] and not cells[2].startswith("http"):
            fail.append(f"non-URL in References URL column: {cells[2]!r}")

    # 3. verbatim quotes
    prose = body.split("## Further reading")[0]
    bad_q = [q for q in re.findall(r'"([^"\n]{12,})"', prose)
             if not any(norm(q) in norm(v) or norm(v) in norm(q) for v in quotes if v)]
    if bad_q:
        fail.append(f"quotes not verbatim in packet: {bad_q}")

    # 4-5. tripwires
    for label, pat in (("reception language", RECEPTION), ("meta commentary", META)):
        hits = [m.group(0) for m in pat.finditer(body)]
        if hits:
            fail.append(f"{label} tripwire: {sorted(set(hits))}")

    # 6. uncited prose
    uncited = [ln for ln in body.splitlines()
               if ln.strip()
               and not ln.startswith(("#", "-", "*", "|", "---", ">"))
               and not re.match(r"^\w+:\s", ln)
               and not re.search(r"\[\d{1,3}\]", ln)]
    if uncited:
        fail.append(f"prose lines with no citation: {uncited}")

    unused = sorted(pkt_eps - cited)
    if len(unused) > len(pkt_eps) * 0.4:
        warn.append(f"{len(unused)}/{len(pkt_eps)} packet episodes unused: {unused}")

    return {
        "article": article_path, "packet": packet_path,
        "concept": pkt["concept"], "words": len(body.split()),
        "claims_in_packet": len(claims),
        "episodes_cited": len(cited), "episodes_in_packet": len(pkt_eps),
        "episodes_unused": unused, "fail": fail, "warn": warn,
        "pass": not fail, "t_lint_s": round(time.monotonic() - t0, 3),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--article", required=True)
    ap.add_argument("--packet", required=True)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--record-timing", action="store_true",
                    help="append t_lint_s and article_words to _timing.jsonl")
    a = ap.parse_args()
    r = lint(a.article, a.packet)
    if a.record_timing:
        try:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from timing import append_timing
            append_timing(r["concept"], {"t_lint_s": r["t_lint_s"],
                                         "article_words": r["words"]})
        except Exception as exc:
            print(f" ! timing not recorded: {exc}", file=sys.stderr)
    if a.json:
        print(json.dumps(r, indent=1))
    else:
        print(f"article words: {r['words']}  (lint {r['t_lint_s']}s)")
        print(f"episodes cited: {r['episodes_cited']} / packet episodes: "
              f"{r['episodes_in_packet']} (unused: {r['episodes_unused']})")
        print(f"claims in packet: {r['claims_in_packet']}")
        for w in r["warn"]:
            print(" ! ", w)
        if r["fail"]:
            print("\nLINT FAIL")
            for f in r["fail"]:
                print(" -", f)
        else:
            print("\nLINT PASS")
    sys.exit(0 if r["pass"] else 1)


if __name__ == "__main__":
    main()
