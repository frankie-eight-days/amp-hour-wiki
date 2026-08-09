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

articles = []
for md in sorted(SRC.glob("*.md")):
    raw = md.read_text()
    m = re.search(r"^title:\s*(.+)$", raw, re.M)
    title = m.group(1).strip() if m else md.stem
    articles.append((md.stem, title))
    shutil.copy2(md, DST / md.name)

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
