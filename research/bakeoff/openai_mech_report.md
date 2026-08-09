# OpenAI arms (gpt-5.6-luna, gpt-5.6-sol) — mechanical report

Concept-census extraction over the five bake-off episodes, scored raw and
unrepaired against the same instruments used for the opus/sonnet arms
(`census_lib.py`, `repair_validate.py`, and the scratchpad `common.py` /
`mech.py` / `align.py` / `inventory.py`). `repair_validate.py --selftest` passes
(5 paragraphs, 12 planted issues).

**Headline: both arms failed at the tested configuration, and one failure is
structural.** Luna produced 182 mentions across five episodes and Sol produced
10, against Sonnet's 479 and Opus's 1,847. No semantic adjudication is needed to
disqualify them — they fail on mechanics.

Two of those failures have different causes, and §4 separates them. The **yield
collapse is an artifact of `effort: "low"`** and reverses at higher effort (Sol
reaches 305 mentions on a single episode at medium). The **offset failure does
not**: `char_start` is invalid for 100% of mentions from both models at every
effort level tested, so no mention either arm produces can be anchored to its
evidence. That is the disqualifying finding.

## 1. Run configuration

Both arms saw byte-identical input to the other arms: `census_prompt_v2.md`
verbatim with the transcript appended after the trailing `--- TRANSCRIPT ---`
marker, nothing added. Responses API, `reasoning.effort: "low"`,
`max_output_tokens: 64000`, streamed.

All 10 requests returned HTTP 200 with `status: "completed"` and parsed as valid
JSON on the first attempt. **No request was truncated and no retry fired.** The
low yields are what the models chose to emit, not a transport or parsing
artifact.

Driver: `<scratchpad>/openai_extract.py`. Scoring: `<scratchpad>/openai_score.py`
→ `<scratchpad>/openai_mech.json`. Raw run log: `<scratchpad>/openai_run.log`.

### Token usage (reported by the API, for cost comparison)

| arm | input | output | of which reasoning | requests |
|---|---|---|---|---|
| luna | 121,141 | 9,726 | 1,490 | 5 |
| sol | 121,141 | 6,233 | 5,179 | 5 |

Input is identical by construction. Sol spent 83% of its output budget on
reasoning tokens and emitted almost nothing. Per-episode wall time was 7–14s
(luna) and 15–40s (sol) — one to two orders of magnitude below what a
150–300-mention extraction takes.

## 2. Comparison table

Sonnet's numbers are the known values from the prior run; Opus is the reference
arm. Luna and Sol are this run.

| metric | luna | sol | sonnet | opus (ref) |
|---|---|---|---|---|
| mentions (5 eps) | 182 | 10 | 479 | 1,847 |
| mentions / 1,000 words | 2.6 | 0.14 | 6.9 | 26.6 |
| spec band (10.8–21.6) | 4.1× below floor | 75× below floor | 1.6× below floor | 1.2× above ceiling |
| offset validity (spec convention) | 0.0% | 0.0% | 100% | 0.0% |
| verbatim snippet (anywhere in body) | 40.1% | 100% | — | — |
| verbatim in *stated* paragraph | 2.2% | 70% | — | — |
| snippets > 100 chars | 3 (1.6%) | 0 | 130 (27.1%) | 0 |
| duplicate (concept, paragraph) pairs | 0 | 0 | 10 | 0 |
| enum validity (type/depth/concept/asr) | 100% | 100% | 100% | 100% |
| coverage (paragraphs touched) | 0–23% | 0–2.3% | 21–44% | 56–74% |
| max paragraph_index reached | 107/246 … 0/416 | 1/246 … 22/416 | — | — |
| `explains` share (anchor 25–33%) | 65.4% | 50% | 30.1% | 25.2% |
| speaker label correct | 52.2% | 70% | 100% | 100% |
| concept recall vs opus | 14.6% | 0.9% | 21.4% | — |
| matched / arm-only / opus-only | 22 / 160 / 1,825 | 6 / 4 / 1,841 | 279 / 200 / 1,568 | — |
| identical concept name (of matched) | 77.3% | 100% | 85.7% | — |

## 3. Anomalies

These are the findings that decide the bake-off, in descending severity. Items
marked *(effort-conditional)* reverse at higher reasoning effort — see §4.

### 3.1 Sol regurgitates the prompt's few-shot examples (critical, *effort-conditional*)

**7 of Sol's 10 mentions are verbatim copies of the worked examples in
`census_prompt_v2.md`**, carrying the prompt's own illustrative `char_start`
values — which the prompt explicitly labels as illustrative:

| copied from | concept | char_start | landed in |
|---|---|---|---|
| Example 1 | `bom-consolidation` | 12044 | ep 500 |
| Example 1 | `component-sourcing` | 12232 | ep 500 |
| Example 1 | `contract-assembly-house` | 12362 | ep 500 |
| Example 5 | `phd-student-precarity` | 44120 | ep 500 |
| Example 2 | `trace-width-and-spacing` | 9903 | ep 79 |
| Example 2 | `trace-width-and-spacing` | 9975 | ep 79 |
| Example 2 | `drill-hole-size` | 10022 | ep 79 |

Only 3 mentions across all five episodes are Sol's own work
(`texas-instruments`, `hubble`, `bluetooth` — all `depth: "mention"`, all from
the first two paragraphs of their episodes).

This poisons Sol's every favourable-looking statistic. Its 100% verbatim-snippet
rate, 100% identical-concept-name rate and 100% type/depth agreement with Opus
are all measuring the prompt's examples, not extraction. Sol's true concept
recall against Opus is 0.9%.

### 3.2 Luna emits mentions with no evidence at all (critical)

On episodes 212 and 500 — **90 of Luna's 182 mentions, 49%** — every mention
carries `"context_snippet": ""` and `"char_start": 0`. The concept, type,
speaker, paragraph_index and depth fields are populated and schema-valid, but
there is no snippet to verify and no offset to verify it at. These mentions are
unfalsifiable by construction and would be rejected wholesale by the downstream
validator.

### 3.3 Offsets are non-functional in both arms under every convention

The brief asked whether the arms used a different offset convention. They did
not use any. I tested four:

| convention | luna hits | sol hits |
|---|---|---|
| body-relative (the spec) | 0 / 92 | 0 / 10 |
| body + 1 (leading-newline off-by-one) | 0 | 0 |
| whole-file (offsets include frontmatter) | 0 | 0 |
| paragraph-relative | 1 | 0 |

Luna's failure is not a constant shift that repair could undo: on ep 728 all 44
`char_start` values are literally `0` while the snippets themselves are real
(84% locatable), and on ep 650 the deltas take 35 distinct values from 1 to
18,655. **134 of Luna's 182 mentions (74%) have `char_start == 0`** — the field
is filler, not a measurement.

Context: Opus also scores 0% on offset validity, so this alone does not separate
Luna and Sol from the reference. Sonnet remains the only arm that anchors
evidence correctly (100%).

### 3.4 Luna dropped an entire episode (*effort-conditional*)

Luna returned **0 mentions for episode 79** — a well-formed header with
`main_topics: []` and a correct diarisation note, and an empty `mentions` array.
Sol returned 0 mentions for episode 650 the same way. Both models read the
episodes (Sol correctly identified Andreas Olofsson and his affiliation *Zero
ASIC*, and flagged the `Parallela` mislabelling), then emitted nothing.

### 3.5 Coverage collapses in the back half of every episode (*effort-conditional*)

Both arms stop early rather than sampling thinly throughout. Luna's highest
paragraph index is 107 of 246 (ep 212), 170 of 385 (ep 500), 99 of 197 (ep 650),
49 of 88 (ep 728). The pattern is a truncated pass over the front of the
transcript, not a uniform under-extraction — which matters, because it means the
missing mentions are not a random sample and no density correction would recover
them.

### 3.6 Depth calibration is badly skewed (luna)

Luna marks **65.4% of mentions `explains`** against the prompt's 25–33% anchor,
reaching 77% on ep 728. This is the same failure mode the prompt was rewritten in
v2 to fix (v1 marked 95% knowledge-bearing). Sonnet (30.1%) and Opus (25.2%) both
sit in or at the band. Sol's 50% is on a base of 10 and not meaningful.

### 3.7 Luna's speaker labels are wrong half the time

52.2% of Luna's mentions carry a `speaker` that does not match the label on the
paragraph it cites, against 100% for both Sonnet and Opus. Combined with §3.3
this means Luna's `paragraph_index` and `speaker` frequently disagree with each
other — the mention cannot be placed in the transcript by any field it provides.

### 3.8 What both arms did get right

Enum discipline is perfect in both: zero invalid `type`, `depth` or `concept`
format violations, zero malformed `asr_suspect`, zero duplicate
(concept, paragraph) pairs, zero out-of-range paragraph indices. Header blocks
match frontmatter on title and URL in all 10 files, and both arms correctly named
Andreas Olofsson and flagged episode 650's broken diarisation. Both arms also
respected the 100-character snippet limit far better than Sonnet (1.6% and 0%
over, vs Sonnet's 27.1%).

The failure is not format compliance. It is that neither arm did the extraction.

## 4. Is this an artifact of `effort: "low"`?

Partly, and the distinction matters for how these results should be read. Before
reporting a 10-mention arm I re-ran the **identical payload** at higher reasoning
effort on episode 212 only, writing outside the arm directories so the bake-off
outputs stay at the tested config (`<scratchpad>/diag_*.json`).

| arm / effort | mentions | offset valid | verbatim anywhere | in stated para | coverage | explains% | few-shot copies |
|---|---|---|---|---|---|---|---|
| luna / low | 60 | 0.0% | 0% | 0.0% | 13.0% | 61.7% | 0 |
| luna / medium | 102 | 0.0% | 89.2% | 2.0% | 21.1% | 44.1% | 0 |
| luna / high | 221 | 0.0% | 85.1% | 0.9% | 37.4% | 46.2% | 0 |
| sol / low | 1 | 0.0% | 100% | 100% | 0.4% | 0% | 0 |
| sol / medium | 305 | 0.0% | 0% | 0.0% | 44.7% | 43.0% | 0 |
| sol / high | 288 | 0.0% | 97.6% | 12.2% | 40.2% | 42.0% | 0 |

Two conclusions, and they point in opposite directions.

**The yield collapse is an artifact of `effort: "low"`.** Sol goes from 1 mention
to 305 on the same episode, at 44.7% coverage — in the same range as Opus's
56–74% and above Sonnet's 21–44%. The few-shot regurgitation of §3.1 also
disappears entirely at higher effort. So §3.1, §3.4 and §3.5 are findings about
the *tested configuration*, not about the models' ceiling. If the production
config can afford medium effort, both models deserve a re-run before being
written off on yield.

**The evidence-anchoring failure is structural and effort-independent.** Offset
validity is **0.0% at every effort level for both models** — including
`luna/high` and `sol/high`, which emit plausible non-zero `char_start` values
(227, 255, …) that simply do not point at their snippets. Verbatim-in-stated-
paragraph never exceeds 12%. And the empty-snippet failure of §3.2 recurs
unpredictably: `sol/medium` emitted all 305 mentions with `context_snippet: ""`,
and `luna/medium` emitted all 102 with `char_start: 0`.

That is the disqualifying result. More effort buys more mentions, but not
mentions you can verify — and `char_start` is the field the pipeline uses to
reject a mention whose snippet is not where it claims. Neither model can count
characters into an 80,000-character body, and the failure is not a constant
offset that a repair pass could correct.

Caveat on scope: this diagnostic is one episode and one sample per cell, so treat
the mention counts as indicative rather than measured. The 0% offset validity is
not sample-limited — it holds across all 6 cells and all 1,059 diagnostic
mentions.

## 5. Reproduction

```
python3 <scratchpad>/openai_extract.py            # both arms, all 5 episodes
python3 <scratchpad>/openai_score.py              # -> openai_mech.json + summary
```

Arm outputs: `research/bakeoff/luna/*.json`, `research/bakeoff/sol/*.json`.
