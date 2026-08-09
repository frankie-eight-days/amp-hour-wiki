#!/usr/bin/env python3
"""Sync articles/wiki/*.md into site/content/ and regenerate index pages.

Site v2: per-article infobox (sparkline, stats, top speakers, related topics),
provenance line, related-articles footer, community-sectioned homepage, /all
A-Z page, citation tooltips. Re-runnable at any time; the factory writes
articles concurrently and this copies whatever exists when it runs.
"""
import pathlib, re, json, datetime, html as html_mod

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "articles" / "wiki"
DST = ROOT / "site" / "content"
PLANNED = 412

DST.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- corpus data
cand = {c["concept"]: c
        for c in json.load(open(ROOT / "articles" / "candidates.json"))["candidates"]}
graph = json.load(open(ROOT / "graph" / "graph.json"))
# adjacency with edge weights (cooccurrence only)
adj = {}
for e in graph.get("edges", graph.get("links", [])):
    if e.get("kind") == "hierarchy":
        continue
    a, b, w = e.get("source"), e.get("target"), e.get("weight", 1)
    adj.setdefault(a, []).append((b, w))
    adj.setdefault(b, []).append((a, w))

published = {p.stem for p in SRC.glob("*.md")}


def sparkline(mentions_by_year, width=178, height=34):
    """Inline SVG sparkline of mentions 2010-2026."""
    years = list(range(2010, 2027))
    vals = [mentions_by_year.get(str(y), mentions_by_year.get(y, 0)) or 0
            for y in years]
    top = max(vals) or 1
    step = width / (len(years) - 1)
    pts = " ".join(f"{i*step:.1f},{height - 3 - (v/top)*(height-8):.1f}"
                   for i, v in enumerate(vals))
    area = f"0,{height} " + pts + f" {width},{height}"
    return (
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'preserveAspectRatio="none" role="img" aria-label="mentions per year">'
        f'<polygon points="{area}" fill="var(--tertiary)" opacity="0.25"/>'
        f'<polyline points="{pts}" fill="none" stroke="var(--secondary)" '
        'stroke-width="1.6"/></svg>')


def infobox(slug, n_refs):
    c = cand.get(slug)
    if not c:
        return ""
    esc = html_mod.escape
    HOSTS = {"Chris Gammell", "Dave Jones"}
    pool = c.get("top_guests") or [
        sp for sp in (c.get("top_speakers") or [])
        if (sp.get("name") if isinstance(sp, dict) else sp) not in HOSTS]
    speakers = [sp.get("name") if isinstance(sp, dict) else
                (sp[0] if isinstance(sp, (list, tuple)) else sp)
                for sp in pool[:3]]
    neighbors = sorted(adj.get(slug, []), key=lambda t: -t[1])
    related = [n for n, _ in neighbors if n in published and n != slug][:5]
    rows = [
        ("Episodes", f'{c["episode_count"]}'),
        ("Mentions", f'{c["mention_count"]:,}'),
        ("Cited here", f"{n_refs}"),
        ("First — last", f'#{c["first_episode"]} — #{c["last_episode"]}'),
    ]
    rows_html = "".join(
        f'<tr><td class="ibk">{k}</td><td class="ibv">{v}</td></tr>'
        for k, v in rows)
    speakers_html = ""
    if speakers:
        speakers_html = ('<tr><td class="ibk">Top guests</td><td class="ibv">'
                         + ", ".join(esc(s) for s in speakers) + "</td></tr>")
    related_html = ""
    if related:
        links = " · ".join(
            f'<a href="./{n}">{esc(cand.get(n, {}).get("concept", n)).replace("-", " ")}</a>'
            for n in related)
        related_html = (f'<tr><td class="ibk">Related</td>'
                        f'<td class="ibv">{links}</td></tr>')
    return (
        '<div class="amp-infobox">'
        f'<div class="ib-spark">{sparkline(c.get("mentions_by_year") or {})}'
        '<div class="ib-sparklabel">mentions 2010–2026</div></div>'
        f'<table>{rows_html}{speakers_html}{related_html}</table>'
        "</div>")


PROVENANCE = ('<div class="amp-provenance">Synthesized from {n} episodes of '
              '<a href="https://theamphour.com">The Amp Hour</a> · AI-generated, '
              "every claim cited to a verbatim transcript passage</div>")

INFOBOX_CSS = """
<style>
.amp-infobox { float: right; width: 210px; margin: 0 0 1rem 1.4rem;
  background: var(--lightgray); border: 1px solid var(--lightgray);
  padding: 10px 12px; font-size: 0.78rem; border-radius: 4px; }
.amp-infobox table { width: 100%; margin: 0; border-collapse: collapse; }
.amp-infobox td { padding: 2px 0; border: none; vertical-align: top; }
.amp-infobox .ibk { color: var(--darkgray); padding-right: 8px;
  white-space: nowrap; }
.amp-infobox .ibv { text-align: right; }
.ib-sparklabel { text-align: center; color: var(--darkgray);
  font-size: 0.68rem; margin-bottom: 6px; }
.amp-provenance { color: var(--darkgray); font-size: 0.8rem;
  margin: -0.4rem 0 1.1rem; }
@media (max-width: 800px) { .amp-infobox { float: none; width: 100%;
  margin: 0 0 1rem; } }
</style>
"""


def linkify(raw: str, slug: str) -> str:
    """Citations -> tooltip links; references -> link table; inject infobox,
    provenance, and related-articles footer."""
    parts = re.split(r"\n## References\s*\n", raw, maxsplit=1)
    prose, refs_md = parts[0], (parts[1] if len(parts) > 1 else "")

    ref_meta = {}
    for line in refs_md.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].isdigit():
            tip = f"Ep {cells[0]}: {cells[1]}"
            if len(cells) > 3 and cells[3]:
                tip += f" ({cells[3]})"
            ref_meta[cells[0]] = tip.replace('"', "&quot;")

    def cite(m):
        nums = re.findall(r"\[(\d+)\]", m.group(0))
        return "".join(
            f'<sup><a href="#ref-{n}" data-tip="{ref_meta.get(n, "")}" '
            f'title="{ref_meta.get(n, "")}">[{n}]</a></sup>'
            for n in nums)

    prose = re.sub(r"(?:\[\d+\]){1,}", cite, prose)

    # inject provenance + infobox after frontmatter
    fm_end = prose.find("\n---", 3)
    if prose.startswith("---") and fm_end != -1:
        head = prose[: fm_end + 4]
        body = prose[fm_end + 4:]
    else:
        head, body = "", prose
    n_eps = cand.get(slug, {}).get("episode_count", "?")
    inject = (INFOBOX_CSS + PROVENANCE.format(n=n_eps)
              + infobox(slug, len(ref_meta)))
    prose = head + "\n" + inject + "\n" + body

    rows = []
    for line in refs_md.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].isdigit():
            n, title, url = cells[0], cells[1], cells[2]
            date = cells[3] if len(cells) > 3 else ""
            rows.append(
                f'<tr id="ref-{n}"><td>{n}</td>'
                f'<td><a href="{url}" target="_blank" rel="noopener">{title}</a></td>'
                f"<td>{date}</td></tr>")
    out = prose
    if rows:
        table = ("<table><thead><tr><th>Episode</th><th>Title</th><th>Date</th>"
                 "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>")
        out = prose + "\n## References\n\n" + table + "\n"
    elif refs_md:
        out = prose + "\n## References\n\n" + refs_md
    return out


# ------------------------------------------------------------------- sync
articles = []
for md in sorted(SRC.glob("*.md")):
    raw = md.read_text()
    m = re.search(r"^title:\s*(.+)$", raw, re.M)
    title = m.group(1).strip() if m else md.stem
    articles.append((md.stem, title))
    (DST / md.name).write_text(linkify(raw, md.stem))

present = {a[0] for a in articles}
KEEP = {"topics", "all", "explore", "contribute", "how-this-was-built"}
for md in DST.glob("*.md"):
    if md.stem not in KEEP and md.stem not in present:
        md.unlink()

total_refs = 0
for md in SRC.glob("*.md"):
    total_refs += len(re.findall(r"^\| \d+ \|", md.read_text(), re.M))

# ------------------------------------------------------------- homepage
by_comm = {}
for slug, title in articles:
    comm = cand.get(slug, {}).get("community_name") or "other topics"
    by_comm.setdefault(comm, []).append((slug, title))

hero = [
    "---",
    "title: Browse the wiki",
    "---",
    "",
    '<div style="text-align:center; padding: 1.2rem 0 0.4rem;">',
    '<h1 style="font-size: 2.1rem; margin-bottom: 0.4rem; border: none;">'
    "Sixteen years of electronics oral tradition&nbsp;&mdash; indexed.</h1>",
    '<p style="font-size: 1.05rem; max-width: 34rem; margin: 0 auto;">'
    "The tribal knowledge in <strong>719 episodes of "
    '<a href="https://theamphour.com">The Amp Hour</a></strong> &mdash; the '
    "practices, rules of thumb, failure modes, and hard numbers that "
    "engineers only say out loud &mdash; distilled into cited, browsable "
    "articles.</p>",
    "</div>",
    "",
    '<div style="display:flex; justify-content:center; gap:2.2rem; '
    'flex-wrap:wrap; text-align:center; margin: 1rem 0 1.4rem; '
    'font-variant-numeric: tabular-nums;">'
    f'<div><strong style="font-size:1.5rem;">{len(articles)}</strong><br>'
    "articles live</div>"
    f'<div><strong style="font-size:1.5rem;">{total_refs:,}</strong><br>'
    "episode citations</div>"
    '<div><strong style="font-size:1.5rem;">719</strong><br>'
    "episodes indexed</div>"
    f'<div><strong style="font-size:1.5rem;">{PLANNED}</strong><br>'
    "articles planned</div>"
    "</div>",
    "",
    '<p style="text-align:center;">'
    '<strong><a href="./explore">Explore the concept graph &rarr;</a></strong>'
    ' &nbsp;·&nbsp; <a href="./all">All articles A&ndash;Z</a>'
    ' &nbsp;·&nbsp; search with <kbd>⌘K</kbd></p>',
    "",
    "Every claim carries a bracketed citation tracing to a verbatim passage "
    "in the show's official transcripts. Articles are AI-generated syntheses "
    "built by a verified extraction pipeline — read "
    "[how this wiki was built](./how-this-was-built), or "
    "[contribute](./contribute).",
    "",
    "## Topics",
    "",
]
hero.append('<div class="amp-commgrid">')
for comm in sorted(by_comm, key=lambda c: -len(by_comm[c])):
    items = sorted(by_comm[comm], key=lambda a: a[1].lower())
    links = "".join(f'<a href="./{sl}">{ti}</a> ' for sl, ti in items)
    hero.append(
        f'<div class="amp-commcard"><h3>{comm.title()}</h3>'
        f'<div class="amp-commcount">{len(items)} articles</div>'
        f'<div class="amp-commlinks">{links}</div></div>')
hero.append("</div>")
hero.append("")
hero.append(
    f"*Last synced {datetime.date.today().isoformat()} · "
    "[source corpus and pipeline]"
    "(https://github.com/frankie-eight-days/amp-hour-wiki)*")
(DST / "topics.md").write_text("\n".join(hero) + "\n")

# ---------------------------------------------------------------- /all page
by_letter = {}
for slug, title in sorted(articles, key=lambda a: a[1].lower()):
    by_letter.setdefault(title[0].upper(), []).append((slug, title))
allpage = ["---", "title: All articles", "---", ""]
for letter in sorted(by_letter):
    allpage.append(f"### {letter}")
    allpage.append("")
    for slug, title in by_letter[letter]:
        allpage.append(f"- [[{slug}|{title}]]")
    allpage.append("")
(DST / "all.md").write_text("\n".join(allpage) + "\n")

# --------------------------------------------------------- /contribute page
REPO = "https://github.com/frankie-eight-days/amp-hour-wiki"
contrib = f"""---
title: How to contribute
---

The wiki is an open project: the transcripts, the extraction pipeline, the
articles, and the site all live in one public repo —
[{REPO.split('//')[1]}]({REPO}). Anyone can improve it; every change lands by
pull request and gets human review.

**The one rule:** every claim traces to a verbatim transcript quote. CI
byte-compares every quote against the transcripts, so a PR either has real
evidence or it doesn't build.

## Three ways in

<div class="amp-commgrid">
<div class="amp-commcard"><h3>Fix an article</h3>
<div class="amp-commcount">easiest — just markdown</div>
<div style="font-size:0.9rem; line-height:1.55;">Awkward phrasing, a section
that repeats itself, a claim that misreads its own citation. Edit the file in
<code>articles/wiki/</code>, keep the citation markers intact, open a PR.
The lint runs automatically.</div></div>
<div class="amp-commcard"><h3>Extract a new article</h3>
<div class="amp-commcount">the real work — ~200 concepts left</div>
<div style="font-size:0.9rem; line-height:1.55;">Pick an unwritten concept,
read its evidence bundle, and produce a packet of claims with verbatim
quotes. The <a href="{REPO}/blob/main/articles/factory/tools/EXTRACTION_SPEC.md">extraction
spec</a> is the full procedure; a packet-only PR is welcome even without the
written article.</div></div>
<div class="amp-commcard"><h3>Hack on the site</h3>
<div class="amp-commcount">quartz 5 + python tooling</div>
<div style="font-size:0.9rem; line-height:1.55;">The static site, the graph
explorer, the landing page, infoboxes — all in the repo under
<code>site/</code> and <code>tools/</code>. Include a screenshot with site
PRs.</div></div>
</div>

## Spotted an error?

You don't need a PR. **Highlight the offending text on any article and hit
the "Report" button that appears** — it opens a prefilled GitHub issue with
the article, the exact text, and the page link already filled in. This is
especially useful when an extraction misunderstood what a speaker meant:
the quote is real but the claim built on it is wrong. Those are the hardest
errors for the pipeline to catch itself and the most valuable to report.

No GitHub account? Open one — it takes a minute and the issue queue is the
project's memory. All reports are public and you can watch yours get fixed.

## What review looks like

CI runs the same checks the article factory uses: `verify_packet.py`
byte-compares quotes, `lint.py` checks that every paragraph is cited, every
citation resolves, and nothing editorializes beyond the evidence. Green CI
means review is about substance only. Full details in
[CONTRIBUTING.md]({REPO}/blob/main/CONTRIBUTING.md).

*Curious how the pipeline works end-to-end? Read
[How this wiki was built](./how-this-was-built).*
"""
(DST / "contribute.md").write_text(contrib)

# ------------------------------------------- /how-this-was-built (authored)
meta_src = ROOT / "articles" / "meta" / "how-this-was-built.md"
if meta_src.exists():
    (DST / "how-this-was-built.md").write_text(meta_src.read_text())

print(f"synced {len(articles)} articles -> {DST} "
      f"({len(by_comm)} communities, {total_refs:,} citations)")
