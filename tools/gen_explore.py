#!/usr/bin/env python3
"""Generate site/explore.html from the graph-explorer template:
Amp Hour palette, site nav bar, and node-card links to published articles.
redeploy.sh copies it to public/explore.html (served via cleanUrls at /explore)."""
import pathlib, re, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = pathlib.Path("/private/tmp/claude-501/-Users-frankwalsh-Documents-vibecoding"
                   "-amp-hour-wiki/2439d3fc-e7b7-42c1-90da-27b1ddd5fa6c/scratchpad"
                   "/graph_explorer_pub.html")
OUT = ROOT / "site" / "explore.html"

s = SRC.read_text()

# ---- palette swap: neutral tokens -> Amp Hour tokens (light + dark) ----
LIGHT = {
    "--surface:#faf9f6": "--surface:#fbf7ee",
    "--ink:#191813": "--ink:#16140d",
    "--panel:#f1efe9": "--panel:#f3ecdc",
    "--rule:#dedbd2": "--rule:#d8cdb4",
    "--ink-dim:#191813a0": "--ink-dim:#16140da0",
    "--ink-faint:#19181366": "--ink-faint:#16140d66",
    "--panel-hi:#e7e4db": "--panel-hi:#efe7d5",
    "--accent:#7a3f12": "--accent:#c94628",
}
DARK = {
    "--surface:#171614": "--surface:#1d1a10",
    "--ink:#f0eee8": "--ink:#f0e9d8",
    "--panel:#201f1c": "--panel:#2e2310",
    "--rule:#35332d": "--rule:#4a3f28",
}
for k, v in {**LIGHT, **DARK}.items():
    s = s.replace(k, v)
# dark accent, if present in a dark block
s = re.sub(r"(--accent:)#[0-9a-fA-F]{6}(\s*}\s*/\*\s*dark)", r"\1#ef5d3c\2", s)

# ---- nav bar ----
NAV = (
    '<nav style="position:fixed; top:0; left:0; right:0; z-index:50;'
    ' display:flex; justify-content:space-between; align-items:center;'
    ' padding:10px 22px; border-bottom:3px solid #c94628;'
    ' background:var(--panel); font:bold 12px Verdana, sans-serif;'
    ' letter-spacing:.08em; text-transform:uppercase;">'
    '<a href="/" style="color:var(--ink); text-decoration:none;">'
    'The Amp Hour <span style="color:#c94628">Wiki</span></a>'
    '<span style="font-weight:normal; letter-spacing:.05em;">'
    '<a href="/topics" style="color:var(--ink); text-decoration:none;'
    ' margin-left:18px;">Topics</a>'
    '<a href="/all" style="color:var(--ink); text-decoration:none;'
    ' margin-left:18px;">All articles</a>'
    '<a href="/explore" style="color:#c94628; text-decoration:none;'
    ' margin-left:18px;">Graph</a></span></nav>'
    '<div style="height:44px"></div>'
)
s = re.sub(r"(<body[^>]*>)", r"\1" + NAV.replace("\\", "\\\\"), s, count=1)

# ---- published-article links on node cards ----
published = sorted(p.stem for p in (ROOT / "articles" / "wiki").glob("*.md"))
pubjs = f"const PUB=new Set({json.dumps(published)});"
s = s.replace("<script>", "<script>" + pubjs, 1)

card_anchor = '<div class="lbl">${esc(LBL[i])}</div>'
addition = (
    '${PUB.has(LBL[i].replace(/ /g,"-"))?`<a href="/${LBL[i].replace(/ /g,"-")}"'
    ' style="display:inline-block;margin:4px 0 2px;font-weight:bold;'
    'color:var(--accent);text-decoration:none;">Read the article &rarr;</a>`:""}'
)
if card_anchor in s:
    s = s.replace(card_anchor, card_anchor + addition, 1)
else:
    raise SystemExit("card anchor not found — template changed")

OUT.write_text(s)
print(f"explore written: {len(s):,} bytes, {len(published)} published slugs linked")
