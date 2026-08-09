# Contributing to The Amp Hour Wiki

All contributions land by pull request and get reviewed by a human
(@frankie-eight-days). CI runs the same checks the factory uses, so if the
lint passes, review is about substance, not mechanics.

## The one rule

**Every claim traces to a verbatim transcript quote.** The whole pipeline
exists to enforce this. If you remember Dave saying something but can't find
the passage, it doesn't go in. If the transcript garbled it (they're
machine-generated), quote the garble or leave it out — never "fix" a quote.

## Lane 1 — Improve an article (easiest)

Articles live in `articles/wiki/*.md`. Good PRs here:

- Fix awkward phrasing, structure, or flow — **without changing what's claimed**.
- Tighten a section that repeats itself.
- Fix a claim that misreads its own citation (check the packet in
  `articles/factory/packets/<concept>.json` — the quote is right there).

Keep the citation markers (`[^N]` style runs and the References table) intact;
the site build turns them into hover-cards and anchor links. Run the lint
before pushing:

```bash
python3 articles/factory/tools/lint.py \
  --article articles/wiki/<concept>.md \
  --packet articles/factory/packets/<concept>.json
```

## Lane 2 — Extract a packet / write a new article

~200 ranked concepts don't have articles yet. The full procedure is in
[`articles/factory/tools/EXTRACTION_SPEC.md`](articles/factory/tools/EXTRACTION_SPEC.md) —
read it first, it's the real spec. Short version:

1. **Pick a concept** from `articles/candidates.json` that has no file in
   `articles/wiki/` and no open PR. Open a draft PR early to claim it.
2. **Get the bundle.** Most already exist in `articles/factory/bundles/`;
   rebuild one with `python3 articles/factory/tools/build_bundles.py <concept>`.
3. **Extract the packet**: read every passage in the bundle and produce
   `articles/factory/packets/<concept>.json` — structured claims, each with a
   `kind` (from the ten-term vocabulary in the spec), a verbatim `quote`
   sliced from a passage's `text` field, and its episode. Slice quotes
   programmatically, not by retyping — retyped quotes fail verification.
4. **Verify**: `python3 articles/factory/tools/verify_packet.py <concept>`
   must pass — it byte-compares every quote against the bundle.
5. **Write the article** from the packet only (an LLM or your own hands, but
   don't peek back at raw transcripts — the packet is the contract).
6. **Lint** (command above) and open the PR with both files.

A packet-only PR (steps 1–4, no article) is also welcome — packets are the
hard part and someone else can write it up.

## Lane 3 — The site

- Static site: Quartz 5 under `site/`, custom styles in
  `site/quartz/styles/custom.scss`.
- Build/publish tooling: `tools/sync_site.py` (markdown → site content,
  infoboxes, citations), `tools/gen_landing.py`, `tools/gen_explore.py`,
  `tools/inject_nav.py`, orchestrated by `tools/redeploy.sh`.
- Build locally: `cd site && npx quartz build` after
  `python3 tools/sync_site.py`. Deploys are maintainer-only, so include a
  screenshot in site PRs.

## Reporting errors without a PR

Use the **Report** button on the site (highlight text first), or open an
issue directly. "The extraction misunderstood what was said" is exactly the
kind of report we want — include the article, the sentence, and the citation
number if you can.

## What CI checks

Every PR touching `articles/` runs `lint.py` on each changed article/packet
pair and `verify_packet.py` on each changed packet. Red CI means fix and
push again; nobody reviews mechanics by hand.
