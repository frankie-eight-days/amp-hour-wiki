---
title: How to contribute
---

The wiki is an open project: the transcripts, the extraction pipeline, the
articles, and the site all live in one public repo —
[github.com/frankie-eight-days/amp-hour-wiki](https://github.com/frankie-eight-days/amp-hour-wiki). Anyone can improve it; every change lands by
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
quotes. The <a href="https://github.com/frankie-eight-days/amp-hour-wiki/blob/main/articles/factory/tools/EXTRACTION_SPEC.md">extraction
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
[CONTRIBUTING.md](https://github.com/frankie-eight-days/amp-hour-wiki/blob/main/CONTRIBUTING.md).

*Curious how the pipeline works end-to-end? Read
[How this wiki was built](./how-this-was-built).*
