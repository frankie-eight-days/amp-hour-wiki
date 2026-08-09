#!/usr/bin/env python3
"""Post-build: inject the site-wide top nav bar into every Quartz page.

Runs against site/public after `quartz build`. Skips index.html (the landing
has its own nav) and explore.html (gen_explore injects its own). Idempotent.
"""
import pathlib, re, sys

PUB = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "site/public")

NAV = """<nav class="amp-topbar"><a class="amp-brand" href="/">The Amp Hour <span>Wiki</span></a><span class="amp-links"><a href="/topics">Topics</a><a href="/all">All articles</a><a href="/explore">Graph</a></span></nav>
<style>
.amp-topbar { position: sticky; top: 0; z-index: 100; display: flex;
  justify-content: space-between; align-items: center; padding: 9px 22px;
  border-bottom: 3px solid #c94628; background: var(--light);
  font-family: Verdana, sans-serif; font-size: 12px; letter-spacing: .08em;
  text-transform: uppercase; }
.amp-brand { font-weight: bold; color: var(--dark) !important;
  text-decoration: none !important; }
.amp-brand span { color: #c94628; }
.amp-links a { color: var(--dark) !important; text-decoration: none !important;
  margin-left: 18px; font-weight: normal; }
.amp-links a:hover { color: #c94628 !important; }
</style>"""

SKIP = {"index.html", "explore.html", "404.html"}
count = 0
for f in PUB.rglob("*.html"):
    if f.name in SKIP:
        continue
    html = f.read_text()
    if "amp-topbar" in html:
        continue
    new = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + NAV, html, count=1)
    if new != html:
        f.write_text(new)
        count += 1
print(f"nav injected into {count} pages")
