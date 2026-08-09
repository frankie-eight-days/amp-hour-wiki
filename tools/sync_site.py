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
    """Make [NNN] citations clickable and the References table a real link table."""
    parts = re.split(r"\n## References\s*\n", raw, maxsplit=1)
    prose, refs_md = parts[0], (parts[1] if len(parts) > 1 else "")

    def cite(m):
        nums = re.findall(r"\[(\d+)\]", m.group(0))
        return "".join(f'<sup><a href="#ref-{n}">[{n}]</a></sup>' for n in nums)

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

lines = [
    "---",
    "title: The Amp Hour Wiki",
    "---",
    "",
    "A topic-first distillation of the tribal engineering knowledge in "
    "**719 episodes of [The Amp Hour](https://theamphour.com)** — practices, "
    "rules of thumb, failure modes, and hard numbers, every claim cited to the "
    "episode it came from.",
    "",
    "Articles are AI-generated syntheses built from the show's official "
    "transcripts through a verified extraction pipeline; every bracketed "
    "citation traces to a verbatim transcript passage. A full *How this wiki "
    "was built* page documenting the pipeline, verification rules, and known "
    "limitations is coming with the complete build.",
    "",
    f"**Status: batch 1 of the article factory — {len(articles)} of {PLANNED} "
    "planned articles published so far. The factory is running; this page "
    "updates as articles land.**",
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
