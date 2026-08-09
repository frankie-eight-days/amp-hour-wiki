# Sonnet, chunked extraction (v3) — bake-off arm report

Sonnet re-run over the same 18 chunks the luna arm used (40 paragraphs, 1
paragraph overlap, `research/census_prompt_v3_chunk.md`), merged and scored by
identical code — `luna_chunked.merge` is imported, not reimplemented, so the two
chunked arms differ only in the model that produced the chunk JSONs.

**Headline.** Chunking helps sonnet more than it helps luna, in the metric that
matters: mention-level recall of opus goes from 17.5% whole-episode to 39.2%
chunked, and raw volume from 227 to 539. But sonnet-chunked lands *behind*
luna-chunked on concept inventory (49.1% vs 59.3% recall, 336 vs 484 distinct
concepts) despite touching **more** paragraphs, and its depth calibration is the
worst of any arm: 44.5% `explains` against the prompt's 25–33% anchor and opus's
23.2%.

## Merge ledger

| | ep79 | ep212 | total |
|---|---:|---:|---:|
| raw mentions emitted | 350 | 223 | 573 |
| dropped as overlap duplicates | 10 | 11 | 21 |
| **rejected — snippet not in stated paragraph** | **11** | **2** | **13** |
| bad / out-of-range paragraph index | 0 | 0 | 0 |
| kept (published) | 329 | 210 | **539** |

All 18 chunks present and parsed; no failed chunks, no malformed mentions, and no
header block leaked onto a later chunk. **Verbatim rate as emitted: 97.6%** (539
of 552 post-dedupe), against luna-chunked's 92.9%. Rejects are saved to
`<scratch>/sonnet_chunked_rejected_<stem>.json`.

Sonnet dropped more overlap duplicates than luna (21 vs 8) — it is more
consistent about re-finding the same concept in a shared boundary paragraph,
which is a mild positive signal about determinism.

## Mechanical scores (published mentions)

| metric | sonnet-chunked | luna-chunked | sonnet-whole | opus |
|---|---:|---:|---:|---:|
| mentions | 539 | 613 | 227 | 819 |
| mentions / 1000 words | 19.6 | 22.3 | 8.3 | 29.8 |
| computed-offset validity | 100% | 100% | 100%¹ | see anomaly |
| verbatim in stated paragraph | 100% (97.6% pre-filter) | 100% (92.9%) | 100% | 100% |
| snippets over 100 chars | 25 (4.6%) | 7 (1.1%) | 43 (18.9%) | 0 |
| duplicate (concept, paragraph) pairs | 0 | 1 | 1 | 0 |
| paragraph coverage (ep79 / ep212) | 56.7% / 45.5% | 38.7% / 42.7% | 25.7% / 30.5% | 56.5% / 64.6% |
| speaker accuracy | 99.8% | 99.7% | 100% | 100% |
| invalid type / depth / concept format | 0 | 0 | 0 | 0 |

¹ sonnet-whole wrote its own `char_start` and got the body convention right; the
chunked arms have no `char_start` to get wrong, since the pipeline computes it.

**Paragraph coverage is the interesting inversion.** Sonnet-chunked matches opus
on ep79 (56.7% vs 56.5%) and beats luna-chunked on both episodes, yet emits fewer
mentions and far fewer distinct concepts. Sonnet is visiting more of the
transcript and getting less out of each visit: 539 mentions over 336 distinct
concepts (1.6 mentions per concept) against luna's 613 over 484 (1.3). It is
re-naming the same handful of concepts across paragraphs rather than finding new
ones.

**Depth calibration is the clear failure.**

| arm | explains | opinion | mention |
|---|---:|---:|---:|
| opus | 23.2% | 34.7% | 42.1% |
| prompt anchor | 25–33% | ~45% | balance |
| sonnet-chunked | **44.5%** | **11.3%** | 44.2% |
| luna-chunked | 36.7% | 13.7% | 49.6% |
| sonnet-whole | 31.7% | 26.4% | 41.9% |

Both chunked arms collapse the `opinion` band into its neighbours, and sonnet
does it harder — 11.3% opinion, with nearly half of everything called
`explains`. This is exactly the failure mode the v2 prompt's calibration anchor
was written to prevent (v1 marked 95% knowledge-bearing), and it is *worse under
chunking than whole-episode*: sonnet-whole sat at a defensible 31.7/26.4. A
40-paragraph window seems to remove the sense of proportion the anchor depends
on — the model cannot see that a passage is a passing opinion relative to the
episode's overall register when it only has forty paragraphs of register to
judge against. Depth agreement on matched pairs is correspondingly weakest:
70.4%, against 74.3% for luna-chunked.

## Agreement with opus

| | ep79 | ep212 | total |
|---|---:|---:|---:|
| matched mentions | 171 | 150 | 321 |
| opus-only (missed) | 260 | 238 | 498 |
| sonnet-only | 158 | 60 | 218 |
| **mention-level recall of opus** | 39.7% | 38.7% | **39.2%** |
| identical concept string, on matched | — | — | 86.6% |
| identical type, on matched | — | — | 81.9% |
| identical depth, on matched | — | — | 70.4% |

Concept-level (fuzzy inventory):

| | ep79 | ep212 | total |
|---|---:|---:|---:|
| opus concepts | 226 | 226 | 452 |
| sonnet-chunked concepts | 178 | 158 | 336 |
| **concept recall vs opus** | 48.2% | 50.0% | **49.1%** |
| sonnet-only concepts | — | — | 113 |

Mention-level recall is a near-tie with luna-chunked (39.2% vs 40.4%), but
concept-level recall is ten points behind (49.1% vs 59.3%), and sonnet agrees
with opus on the exact concept string less often when they do match (86.6% vs
90.9%). On this evidence luna-chunked is the stronger chunked arm, and the gap is
in inventory breadth and naming discipline rather than in raw hit rate.

## The chunking lift, both models

| | sonnet whole → chunked | luna whole → chunked |
|---|---|---|
| mentions | 227 → 539 (2.4x) | 60 → 613 (10x) |
| mention recall of opus | 17.5% → 39.2% | ~0% → 40.4% |
| concept recall of opus | 26.1% → 49.1% | 11.5% → 59.3% |
| snippets over 100 chars | 18.9% → 4.6% | 0% → 1.1% |
| depth calibration | 31.7% explains → 44.5% | — → 36.7% |

Chunking is a large, consistent win on coverage for both models, and it also
fixed sonnet's snippet-length indiscipline (18.9% over-length whole-episode, 4.6%
chunked). Its one consistent cost is depth calibration, which degrades for both.

## Anomalies

**1. The opus reference's `char_start` is uniformly off by one — instrument
issue, not a data-quality issue.** All 819 opus mentions across both episodes
fail the spec's `body[cs:cs+len]==snippet` check and all 819 validate at
`cs+1`. `mech.analyse` diagnoses this correctly (`delta_constant: true`,
`delta_median: 1`, `off_by_one_newline: 388/388`). Opus measured offsets into a
body with the leading newline stripped — the exact convention error
`census_lib.parse_transcript` carries a warning about. It is uniform and
losslessly correctable with `+1`; every opus snippet is verbatim in its stated
paragraph, so nothing about the reference's content is in doubt, and no
comparison in this report is affected (alignment is by concept and paragraph
index, not by offset). But the reference should be corrected before anything
downstream consumes those offsets.

**2. The scorer's `body_plus_one` probe has the sign backwards and hides the
above.** `alt_offset_conventions` in `openai_score.py` tests
`body[cs-1 : cs-1+L]`, which finds offsets that are one too *high*; the observed
error is one too *low*, needing `cs+1`. So the probe reports 0 hits under every
convention for opus, which reads as "unlocatable" when the truth is "off by one
in the other direction". Worth a one-character fix if that probe is kept.

**3. Sonnet-chunked's over-length snippets are concentrated in one episode:** 22
of 25 are in ep79, against 3 in ep212. Not spread evenly, so it looks like a
register effect on the hosts-only episode rather than a general habit.

**4. Coverage up, inventory down.** Flagged above and worth repeating as the
finding most likely to mislead: sonnet-chunked's paragraph coverage matches opus
on ep79, which would normally read as a strong arm. Its concept recall is 48%.
Paragraph coverage is not a proxy for extraction quality here, and any dashboard
that leads with it will rank sonnet-chunked above luna-chunked incorrectly.

## Reproduction

- merge: `<scratch>/sonnet_chunked_merge.py` (imports `luna_chunked.merge`) → `bakeoff/sonnet-chunked/`
- scorer: `<scratch>/chunked_bakeoff_score.py` → `<scratch>/chunked_bakeoff_mech.json`, `<scratch>/chunked_bakeoff_score.txt`
- merge log: `<scratch>/sonnet_chunked_merge_log.json`
- rejects: `<scratch>/sonnet_chunked_rejected_<stem>.json`

`<scratch>` is
`/private/tmp/claude-501/-Users-frankwalsh-Documents-vibecoding-amp-hour-wiki/2439d3fc-e7b7-42c1-90da-27b1ddd5fa6c/scratchpad`.
The scorer drives four arms (sonnet-chunked, luna-chunked, sonnet, opus) over the
two test episodes; opus scored against itself is the 100% row and is there only
to put the reference's own mechanics in the same table.
