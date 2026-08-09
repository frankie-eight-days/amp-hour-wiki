#!/usr/bin/env python3
"""Post-build: inject the site-wide top nav bar into every Quartz page.

Runs against site/public after `quartz build`. Skips index.html (the landing
has its own nav) and explore.html (gen_explore injects its own). Idempotent.
"""
import pathlib, re, sys

PUB = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "site/public")

NAV = """<nav class="amp-topbar"><a class="amp-brand" href="/">The Amp Hour <span>Wiki</span></a><span class="amp-links"><a href="/topics">Topics</a><a href="/all">All articles</a><a href="/explore">Graph</a><a href="/contribute">Contribute</a></span></nav>
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
#amp-report { position: absolute; z-index: 200; display: none;
  background: #16140d; color: #fbf7ee; border: none; border-radius: 4px;
  padding: 6px 12px; font: bold 11px Verdana, sans-serif; letter-spacing: .06em;
  text-transform: uppercase; cursor: pointer; box-shadow: 0 2px 8px rgba(22,20,13,.35); }
#amp-report:hover { background: #c94628; }
</style>
<script>
(function () {
  var REPO = "https://github.com/frankie-eight-days/amp-hour-wiki";
  var btn = document.createElement("button");
  btn.id = "amp-report";
  btn.textContent = "\\u26a0 Report an issue";
  document.addEventListener("DOMContentLoaded", function () {
    document.body.appendChild(btn);
  });
  var lastText = "";
  document.addEventListener("mouseup", function () {
    setTimeout(function () {
      var sel = window.getSelection();
      var text = sel ? sel.toString().trim() : "";
      if (text.length < 8 || text.length > 1200 ||
          !document.querySelector("article, .center")) {
        btn.style.display = "none"; return;
      }
      var rect = sel.getRangeAt(0).getBoundingClientRect();
      lastText = text;
      btn.style.left = Math.max(8, rect.left + window.scrollX) + "px";
      btn.style.top = (rect.bottom + window.scrollY + 8) + "px";
      btn.style.display = "block";
    }, 10);
  });
  btn.addEventListener("mousedown", function (e) {
    e.preventDefault(); e.stopPropagation();
    var slug = location.pathname.replace(/^\\/|\\/$/g, "") || "index";
    var title = "[report] " + slug + ": \\u201c" +
      lastText.slice(0, 60).replace(/\\s+/g, " ") +
      (lastText.length > 60 ? "\\u2026" : "") + "\\u201d";
    var body = "**Page:** " + location.href +
      "\\n\\n**Highlighted text:**\\n\\n> " +
      lastText.replace(/\\n/g, "\\n> ") +
      "\\n\\n**What's wrong?** (a claim can be wrong even when its quote is real \\u2014 " +
      "e.g. the extraction misunderstood the speaker. Say what you think was meant.)\\n\\n";
    window.open(REPO + "/issues/new?labels=report&title=" +
      encodeURIComponent(title) + "&body=" + encodeURIComponent(body), "_blank");
    btn.style.display = "none";
  });
})();
</script>"""

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
