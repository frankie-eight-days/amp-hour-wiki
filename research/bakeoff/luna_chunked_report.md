# Luna, chunked extraction (v3) — bake-off arm report

**Question.** Luna's whole-episode arm collapsed: 60 mentions across the two test
episodes and 0% of its snippets found verbatim anywhere in the body. Was that a
reasoning-effort problem or an attention/context-length problem? This arm splits
the episode into ~40-paragraph chunks and re-runs at the same low effort; a
separate control re-runs the whole episode at medium effort. The two together
separate the causes.

**Answer.** Chunking fixed it; effort alone did not. Chunked-low produced 613
mentions at 100% offset validity. Whole-episode-medium produced 76 — its
snippets are now verbatim, but it still reads only the first 60% of the
transcript and touches 38 of 246 paragraphs. Low effort was corrupting the
*snippets*; the whole-episode format was corrupting the *coverage*, and only
chunking addresses that.

## Configuration

| | chunked arm | control |
|---|---|---|
| prompt | `research/census_prompt_v3_chunk.md` (v2 minus `char_start`, chunk-scoped) | `research/census_prompt_v2.md`, unchanged |
| unit | 40 paragraphs, 1 paragraph overlap | whole episode |
| model / effort | gpt-5.6-luna, `low` | gpt-5.6-luna, `medium` |
| max output tokens | 16 000 per chunk | 64 000 |
| requests | 18 (11 for ep79, 7 for ep212) | 1 |
| output | `bakeoff/luna-chunked/` | `<scratch>/luna_medium_control_0212.json` (not a bake-off arm) |

`char_start` is not asked of the model. The pipeline computes it by searching for
`context_snippet` inside the span of the paragraph the mention names; a snippet
not found there is rejected. All 18 chunk requests returned HTTP 200, `completed`
(not truncated), and parsed as JSON on the first attempt. Reasoning burn was
97–516 tokens per chunk.

## Volume and the merge ledger

| | ep79 | ep212 | total |
|---|---:|---:|---:|
| raw mentions emitted by the model | 342 | 326 | 668 |
| dropped as overlap duplicates | 5 | 3 | 8 |
| **rejected — snippet not in its stated paragraph** | **20** | **27** | **47** |
| kept (published) | 317 | 296 | **613** |
| opus reference | 431 | 388 | 819 |

Per-chunk yield ran 21–42 on ep79 (median 30) and 22–72 on ep212 (median 46),
against the prompt's stated 10–25 anchor. Luna runs *above* the anchor rather
than below it, so the anchor is not what is holding the model back; no chunk came
back thin.

**Verbatim rate as emitted: 92.9%** (613 of 660 post-dedupe). That is the honest
number — the 100% figures below are 100% *by construction*, because the rejected
7.1% never reach the output file. The rejects are in
`<scratch>/luna_chunked_rejected_<stem>.json`; they are mentions whose snippet
was lightly paraphrased or stitched across a sentence boundary, not wild
hallucinations.

## Mechanical scores (published mentions, vs. the opus reference)

| metric | luna-chunked | luna (whole-episode, low) | opus |
|---|---:|---:|---:|
| mentions (2 episodes) | 613 | 60 | 819 |
| mentions / 1000 words | 22.3 | 2.2 | 29.8 |
| computed-offset validity | 100% | 0% | — |
| snippet verbatim in stated paragraph | 100% (92.9% pre-filter) | 0% | — |
| snippets over 100 chars | 7 (1.1%) | 0 | — |
| duplicate (concept, paragraph) pairs | 1 (0.2%) | 0 | — |
| paragraph coverage | 38.7% / 42.7% | 0% / 13.0% | 56.5% / 64.6% |
| max paragraph index reached | 411/416, 244/246 | none, 107/246 | — |
| invalid type / depth / concept format | 0 / 0 / 0 | 0 / 0 / 0 | — |
| speaker label accuracy | 99.7% | 65% | — |

Coverage is the honest gap: luna-chunked reaches the *end* of both episodes
(paragraph 411 of 416, 244 of 246 — the whole-episode arm never got past 107),
but within that span it still touches only ~40% of paragraphs against opus's
~60%. It is reading everything and extracting from less of it.

**Depth calibration is the one clear miss.** Luna-chunked is 36.7% `explains` /
13.7% `opinion` / 49.6% `mention`, against opus's 23.2% / 34.7% / 42.1%. The
prompt's 25–33% `explains` anchor is exceeded, and `opinion` — the middle
category — is barely used: luna pushes judgements up into `explains` or down into
`mention`. Depth agreement on matched pairs is correspondingly the weakest of the
three fields (74.3%, against 86.4% for type and 90.9% for concept).

## Agreement with opus

| | ep79 | ep212 | total |
|---|---:|---:|---:|
| matched mentions | 165 | 166 | 331 |
| opus-only (missed) | 266 | 222 | 488 |
| luna-only | 152 | 130 | 282 |
| mention-level recall of opus | 38.3% | 42.8% | **40.4%** |
| of luna's mentions, matched | 52.1% | 56.1% | 54.0% |
| identical concept string, on matched | 89.7% | 92.2% | 90.9% |
| identical type, on matched | 84.8% | 88.0% | 86.4% |
| identical depth, on matched | 75.2% | 73.5% | 74.3% |

Concept-level (fuzzy inventory, deduped concept names):

| | ep79 | ep212 | total |
|---|---:|---:|---:|
| opus concepts | 226 | 226 | 452 |
| luna-chunked concepts | 243 | 241 | 484 |
| in both | 124 | 144 | 268 |
| **concept recall vs opus** | **54.9%** | **63.7%** | **59.3%** |
| luna-only concepts | 114 | 95 | 209 |

Read together: when luna and opus land on the same passage they agree on the
concept name 91% of the time, so the naming discipline is sound. The deficit is
recall — luna finds three-fifths of opus's concept inventory and 40% of its
individual mentions, while emitting a comparable *number* of distinct concepts
(484 vs 452). It is not extracting less; it is extracting a partly different set,
with 209 concepts opus never named. That arm-only pool is the thing to spot-check
before trusting this arm — it is either genuine additional recall or a
looser-splitting habit, and these counts cannot tell them apart.

## The effort control

Whole-episode 0212, v2 prompt verbatim, effort `medium`, 64k cap: **76 mentions**
(vs. 60 at low, 296 chunked, 388 for opus). Completed cleanly, 6016 output
tokens, 1237 reasoning tokens — nowhere near the cap, so it stopped because it
decided it was done, not because it ran out of room.

What medium effort did fix: all 76 snippets are verbatim and offset-valid, against
0 of 60 at low effort. Low effort was paraphrasing the evidence.

What it did not fix: the run stops at paragraph 149 of 246 and touches 38 distinct
paragraphs. Raising effort bought better *fidelity per mention* and almost no
additional *coverage*. Chunking, at the cheaper effort, bought coverage to the end
of the transcript and 4x the mentions.

## Verdict

Chunking fixes luna; effort does not. The failure was attention over a long input,
not insufficient reasoning — and the two symptoms have different causes, which
this pair of runs separates: low effort explains the mangled snippets, and the
whole-episode format explains the missing 60% of the transcript.

Luna-chunked is now a mechanically clean arm — 100% offset validity on published
mentions, 92.9% verbatim as emitted, 99.7% speaker accuracy, one duplicate pair
in 613, no enum violations — that recalls 59% of opus's concepts and 40% of its
mentions at 22 mentions per 1000 words against opus's 30. Two things stand
between it and production: paragraph coverage at ~40% versus opus's ~60%, and the
`opinion` band being collapsed into its neighbours. Both are prompt-level, not
format-level, and worth one more iteration before writing luna off or in.

## Reproduction

- prompt: `research/census_prompt_v3_chunk.md`
- chunker: `<scratch>/chunker.py` → `<scratch>/chunks/<stem>/<nn>.txt` (left in place)
- runner: `<scratch>/luna_chunked.py` (chunk requests, merge, control)
- scorer: `<scratch>/luna_chunked_score.py` → `<scratch>/luna_chunked_mech.json`
- run log: `<scratch>/luna_chunked_run_log.json`

`<scratch>` is
`/private/tmp/claude-501/-Users-frankwalsh-Documents-vibecoding-amp-hour-wiki/2439d3fc-e7b7-42c1-90da-27b1ddd5fa6c/scratchpad`.
Scoring reuses `mech.analyse`, `common.align_episode` and `inventory.best_match`
unchanged; `luna_chunked_score.py` differs from `openai_score.py` only in which
arms and stems it drives.
