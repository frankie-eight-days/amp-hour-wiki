#!/usr/bin/env python3
"""Post-build: inject the site-wide top nav bar into every Quartz page.

Runs against site/public after `quartz build`. Skips index.html (the landing
has its own nav) and explore.html (gen_explore injects its own). Idempotent.
"""
import pathlib, re, sys

PUB = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "site/public")

NAV = """<nav class="amp-topbar"><a class="amp-brand" href="/">The Amp Hour <span>Wiki</span></a><span class="amp-links"><a href="/topics">Topics</a><a href="/all">All articles</a><a href="/explore">Graph</a><a href="/how-this-was-built">How it was built</a><a href="/contribute">Contribute</a></span></nav>
<style>
:root { --amp-nav: 43px; }
.amp-topbar { position: sticky; top: 0; z-index: 100; display: flex;
  justify-content: space-between; align-items: center; padding: 0 22px;
  height: var(--amp-nav); box-sizing: border-box;
  border-bottom: 3px solid #c94628; background: var(--light);
  font-family: Verdana, sans-serif; font-size: 12px; letter-spacing: .08em;
  text-transform: uppercase; }
/* Quartz's rails are sticky at top:0, which parks them under this bar and
   clips their headings. The left rail stays sticky on mobile too, so the
   offset must apply at EVERY width — only the height clamp is desktop-only. */
#quartz-body > .sidebar { top: var(--amp-nav) !important; }
@media (min-width: 800px) {
  #quartz-body > .sidebar { height: calc(100vh - var(--amp-nav)) !important; }
}
html { scroll-padding-top: calc(var(--amp-nav) + 12px); }
.amp-brand { font-weight: bold; color: var(--dark) !important;
  text-decoration: none !important; }
.amp-brand span { color: #c94628; }
.amp-links a { color: var(--dark) !important; text-decoration: none !important;
  margin-left: 18px; font-weight: normal; }
.amp-links a:hover { color: #c94628 !important; }
/* On a phone the brand + four links exceed the viewport, which widens the
   whole document and clips every page. Wrap to two centred rows instead. */
@media (max-width: 799px) {
  /* the bar wraps to two rows here, so it is taller than the desktop 43px;
     the JS below measures it and corrects --amp-nav for any width */
  :root { --amp-nav: 54px; }
  .amp-topbar { height: auto; min-height: var(--amp-nav); flex-wrap: wrap;
    gap: 3px 0; justify-content: center; padding: 6px 10px; font-size: 10px;
    letter-spacing: .04em; }
  .amp-brand { flex: 1 0 100%; text-align: center; }
  .amp-links { display: flex; flex-wrap: wrap; justify-content: center;
    gap: 0 14px; }
  .amp-links a { margin-left: 0; }
}
#amp-report { position: absolute; z-index: 200; display: none;
  background: #16140d; color: #fbf7ee; border: none; border-radius: 4px;
  padding: 6px 12px; font: bold 11px Verdana, sans-serif; letter-spacing: .06em;
  text-transform: uppercase; cursor: pointer; box-shadow: 0 2px 8px rgba(22,20,13,.35); }
#amp-report:hover { background: #c94628; }
</style>
<script>
(function () {
  // Keep --amp-nav equal to the bar's REAL height. It wraps to two rows on
  // narrow screens, so a hardcoded value leaves everything that offsets for
  // the bar (sticky rails, scroll-padding, the trace page's pinned sentence)
  // short by the difference, and content tucks under the banner.
  function ampNavHeight() {
    var bar = document.querySelector(".amp-topbar");
    if (!bar) return;
    var h = Math.round(bar.getBoundingClientRect().height);
    if (h > 0) document.documentElement.style.setProperty("--amp-nav", h + "px");
  }
  document.addEventListener("DOMContentLoaded", ampNavHeight);
  window.addEventListener("load", ampNavHeight);
  window.addEventListener("resize", ampNavHeight);
  if (window.ResizeObserver) {
    document.addEventListener("DOMContentLoaded", function () {
      var bar = document.querySelector(".amp-topbar");
      if (bar) new ResizeObserver(ampNavHeight).observe(bar);
    });
  }
})();
(function () {
  var REPO = "https://github.com/frankie-eight-days/amp-hour-wiki";
  var lastText = "";

  // Quartz is an SPA: its router swaps document.body on every internal
  // navigation, which detaches a button appended once at load and leaves any
  // saved reference pointing at a dead node. So look the button up (and
  // recreate it) on demand, and delegate clicks off document, which survives.
  function reportButton() {
    var b = document.getElementById("amp-report");
    if (!b || !document.body.contains(b)) {
      b = document.createElement("button");
      b.id = "amp-report";
      b.type = "button";
      b.textContent = "\\u26a0 Report an issue";
      document.body.appendChild(b);
    }
    return b;
  }

  function hide() {
    var b = document.getElementById("amp-report");
    if (b) b.style.display = "none";
  }

  function onSelect() {
    var sel = window.getSelection();
    var text = sel ? sel.toString().trim() : "";
    if (!sel || sel.rangeCount === 0 || text.length < 8 || text.length > 1200) {
      return hide();
    }
    // only offer it for article prose, not nav/sidebar/UI text
    var node = sel.anchorNode;
    node = node && node.nodeType === 3 ? node.parentElement : node;
    if (!node || !node.closest || !node.closest("article, .center, .hb")) {
      return hide();
    }
    var rect = sel.getRangeAt(0).getBoundingClientRect();
    if (!rect || (rect.width === 0 && rect.height === 0)) return hide();
    lastText = text;
    var b = reportButton();
    b.style.display = "block";
    var left = Math.min(rect.left + window.scrollX,
                        window.scrollX + document.documentElement.clientWidth
                        - b.offsetWidth - 10);
    b.style.left = Math.max(8, left) + "px";
    b.style.top = (rect.bottom + window.scrollY + 8) + "px";
  }

  document.addEventListener("mouseup", function () { setTimeout(onSelect, 10); });
  document.addEventListener("keyup", function (e) {
    if (e.shiftKey || e.key === "Shift") setTimeout(onSelect, 10);
  });

  document.addEventListener("mousedown", function (e) {
    var b = e.target && e.target.closest && e.target.closest("#amp-report");
    if (!b) return;
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
    hide();
  }, true);
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
