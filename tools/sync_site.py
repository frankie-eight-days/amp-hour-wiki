#!/usr/bin/env python3
"""Sync articles/wiki/*.md into site/content/ and regenerate the index page.

Re-runnable at any time; the factory writes articles concurrently and this
copies whatever exists when it runs.
"""
import pathlib, re, shutil, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "articles" / "wiki"
DST = ROOT / "site" / "content"
PLANNED = 412

DST.mkdir(parents=True, exist_ok=True)

def linkify(raw: str) -> str:
    """Make [NNN] citations clickable (with hover tooltips) and the References
    table a real link table."""
    parts = re.split(r"\n## References\s*\n", raw, maxsplit=1)
    prose, refs_md = parts[0], (parts[1] if len(parts) > 1 else "")

    # parse references first so citations can carry tooltips
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
            f'<sup><a href="#ref-{n}" title="{ref_meta.get(n, "")}">[{n}]</a></sup>'
            for n in nums)

    prose = re.sub(r"(?:\[\d+\]){1,}", cite, prose)

    rows = []
    for line in refs_md.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].isdigit():
            n, title, url = cells[0], cells[1], cells[2]
            date = cells[3] if len(cells) > 3 else ""
            rows.append(
                f'<tr id="ref-{n}"><td>{n}</td>'
                f'<td><a href="{url}" target="_blank" rel="noopener">{title}</a></td>'
                f"<td>{date}</td></tr>"
            )
    if rows:
        table = (
            "<table><thead><tr><th>Episode</th><th>Title</th><th>Date</th></tr></thead>"
            "<tbody>" + "".join(rows) + "</tbody></table>"
        )
        return prose + "\n## References\n\n" + table + "\n"
    return raw if not refs_md else prose + "\n## References\n\n" + refs_md


articles = []
for md in sorted(SRC.glob("*.md")):
    raw = md.read_text()
    m = re.search(r"^title:\s*(.+)$", raw, re.M)
    title = m.group(1).strip() if m else md.stem
    articles.append((md.stem, title))
    (DST / md.name).write_text(linkify(raw))

# prune articles removed upstream (never prune index.md)
present = {a[0] for a in articles}
for md in DST.glob("*.md"):
    if md.stem != "index" and md.stem not in present:
        md.unlink()

by_letter = {}
for slug, title in sorted(articles, key=lambda a: a[1].lower()):
    by_letter.setdefault(title[0].upper(), []).append((slug, title))

# total citations across the wiki (rows in References tables)
total_refs = 0
for md in SRC.glob("*.md"):
    total_refs += len(re.findall(r"^\| \d+ \|", md.read_text(), re.M))

lines = [
    "---",
    "title: The Amp Hour Wiki",
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
    "Every claim carries a bracketed citation that traces to a verbatim "
    "passage in the show's official transcripts, through a verified "
    "extraction pipeline. Articles are AI-generated syntheses; a full "
    "*How this wiki was built* page is coming with the complete build.",
    "",
    "**[Explore the concept graph &rarr;](./explore)**",
    "",
    "## Articles",
    "",
]
for letter in sorted(by_letter):
    lines.append(f"### {letter}")
    lines.append("")
    for slug, title in by_letter[letter]:
        lines.append(f"- [[{slug}|{title}]]")
    lines.append("")

lines.append(
    f"*Last synced {datetime.date.today().isoformat()} · "
    "[source corpus and pipeline](https://github.com/frankie-eight-days/amp-hour-wiki)*"
)
(DST / "index.md").write_text("\n".join(lines) + "\n")
print(f"synced {len(articles)} articles -> {DST}")
