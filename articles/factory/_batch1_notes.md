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
  batch 3 and consider a rebuild pass for affected bundles.
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
