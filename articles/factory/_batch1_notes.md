# Batch 1 — operational and content notes

## Content gaps found by extractors (candidates for a later enrichment pass)

- **i2c**: bundle contains NO clock-stretching, stuck-slave/nine-clock-pulse
  recovery, speed-grade (standard/fast/fast-plus/high-speed), or
  level-translation material in its 122 passages, despite being core I2C
  topics. Extractor correctly declined to invent them; evidence would have to
  come from another bundle or a targeted transcript search.

- **semiconductor-fab**: three passages from the "Chips And Fabs And Garages"
  episode carry `episode: null` in the bundle and are uncitable (dry etch /
  SF6 content was covered from eps 134/120 instead). Multiple other bundles
  also showed a single null-episode passage 0. Check the bundle builder for
  the null-episode hole before batch 2.
- **ROOT CAUSE FOUND (transistor extractor)**: the null-episode passages come
  from transcript stem `0706-leading-edge-analog-with-joren-vaes` — episode
  706's episode/title/URL join fails in the bundle builder, so EVERY bundle
  drawing on ep 706 silently loses those passages (they had good material:
  foundry PDK models with hundreds of parameters, parasitic extraction
  inflating a 30-device schematic to 2–3M devices). Fix the join before
  batch 3 and consider a rebuild pass for affected bundles. Second broken
  stem found by the inductor extractor: `0591-olive-a-the-world` (ep 591) —
  same null-episode/null-URL join failure.
- **attribution_reliable: true is not trustworthy** (worst cases: ep 18
  hosts flatly transposed; ep 542 Dave Jones credited on an episode he isn't
  on; battery-life bundle would have credited Dave Jones with 11 claims that
  are four different guests' own product measurements). Consider a
  speaker-repair v2 pass before batch 3.

## Kimi API behavior (learned 2026-08-08 night)

- Kimi returns **403 permission_error with "billing cycle" quota text for
  transient rolling-window trips**. Two short outages (~22:15, ~22:27 PDT) each
  recovered within ~2 minutes. The error text is misleading — do not treat a
  403 as a dead key.
- Retry policy that works: on 403, wait 120 s, rerun kimi_write unchanged;
  first-attempt success every time it was tried. Report as blocked only after
  a second failed wait-and-retry cycle; the packet stays complete and the
  write is merely pending.
- `kimi_write.py` writes `<concept>.md.prompt.txt` BEFORE calling the API — a
  prompt file with no matching `.md` means "call in flight or interrupted",
  NOT "failed permanently".

## Timing instrument traps

- Deriving `t_extract_s` from a prompt-file mtime breaks when a retry
  overwrites the prompt file; stale duplicate lines can appear in
  `_timing.jsonl` (summarize() takes last-non-null, so final values win).
- Article word counts appear twice per concept (kimi raw vs post-lint); use
  the lint entry.

## Bundle field gotchas (for any hand-rolled verifier)

- Verify quotes against the bundle passage `text` field, NOT `paragraph_text`
  (the latter caused 23 false failures on pcb-layout).
- `attribution_reliable` under-reports speaker swaps badly (multiple episodes
  flagged reliable had systematically swapped labels: 338, 396, 631, 135,
  411, 403, 412, 101, 138...). Content-attribute when unambiguous, else
  speaker: null; record every judgment in attribution_notes.
- Passages with `episode: null` are uncitable — drop them.
- Lint's reception-language regex bans the bare word "divided"; phrase
  numeric claims as "0.35 over the rise time", not "divided by".
- **Scratchpad collisions**: extractor agents share one scratchpad; two agents
  overwrote each other's `build.py` mid-run (harmless this time — packet was
  already written). Batch-3 briefs should mandate per-concept script names
  (`build_<concept>.py`).
- **Bundle dedup**: ep 196 appears twice under different episode_title strings
  (one "(Re-broadcast)") — downstream dedup must key on episode number.
- **Lint fix pattern (no API call needed)**: Kimi sometimes opens a bullet list
  with an uncited lead-in sentence ("Several failure modes are characteristic
  of X:"). Deleting the lead-in by hand fixes lint in seconds — do not spend a
  rewrite call on it.

## From g2's final lane verification (add to lint.py before batch 3)

- **Assert packet has `name`**: when missing, kimi_write title-cases the slug
  ("Pcb Layout", "I2c", "Lora"). Hit two articles; fixed by hand.
- **Assert `kind` ∈ ten-term vocabulary**: `explains` (a depth value) leaked
  into `kind` on two packets (17 claims total).
- **State prompt-file semantics in briefs**: kimi_write writes
  `<concept>.md.prompt.txt` BEFORE the API call; prompt-without-md means
  "in flight or interrupted", never "key dead".
- **Delegate watcher pattern**: parent groups never receive delegate
  completion notifications (they route to the lead). Fix that worked: arm a
  background `until [ -f <artifact> ]` watcher with ABSOLUTE paths right
  after launching each delegate (relative paths silently fail — cwd resets
  between bash calls). Event-driven, costs nothing idle. Mandate in batch-3
  briefs.
- **Bundle join FIXED (2026-08-09 morning)**: 120 null-episode passages
  backfilled across 79 bundles from transcript frontmatter (eps 706, 591, et
  al.); ham-spam-thank-you-maam resolved to ep 41 from the live page. Three
  early episodes remain unnumbered anywhere (chips-and-fabs-and-garages,
  quassating-quadcopter-quantophrenia, the-chinese-clairvoyancy) — their
  passages stay uncitable; extractors drop them correctly.
- **Canonical kind mapping (2026-08-09, fleet-agreed)**: principle→mechanism,
  judgment→practitioner-judgment, case→history, comparison→tradeoff,
  number→numbers, rule-of-thumb→practice, rationale→mechanism,
  explains→mechanism, design→practice, spec→numbers, sourcing→market-structure,
  threshold→numbers, definition→mechanism, trade-off→tradeoff,
  vendor-history→history, cost→numbers, reference→history. Applied centrally
  to 923 claims in 42 packets; batch-3+ extractors emit the ten-term set
  directly.
- **Enrichment lead**: chips-and-fabs-and-garages published 2010-10-22 (ep 1 =
  2010-08-07, weekly cadence → likely episode ~11-13, unconfirmed). Resolving
  it would unlock 7+ passages of semiconductor-process material for wafer /
  semiconductor-fab. Site page and sitemap carry no number; needs archive.org
  or RSS-history confirmation.
