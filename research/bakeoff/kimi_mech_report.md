# Concept-Census Bake-off: Kimi K3 arm — mechanical report

**Corpus: 4 episodes (79, 0212, 0500, 0728), 56,098 words.** Episode 0650 is
excluded by decision; see §1.1 — its exclusion is itself the most important
finding in this report. Opus and sonnet were re-scored on the **same 4
episodes** so every recall and share below is apples-to-apples; none of the
numbers here are the previously circulated 5-episode figures.

Arm: `k3` via `https://api.kimi.com/coding/v1/messages` (Anthropic-compatible).
Payload: `research/census_prompt_v2.md` verbatim with the full transcript file
appended after the trailing `--- TRANSCRIPT ---` marker — identical to what the
opus and sonnet arms saw. Nothing was added to the prompt.

Extraction script: `<scratchpad>/kimi_extract.py`. Output:
`research/bakeoff/kimi/*.json`.

Instruments reused unmodified: `research/census_lib.py`,
`research/repair_validate.py` (self-test: **PASS**, 5 paragraphs, 12 planted
issues), and the scratchpad tooling `mech.py` / `align.py` / `inventory.py`.
The only changes to that tooling were two env switches in `common.py` —
`BAKEOFF_ARM_B` to select the challenger arm and `BAKEOFF_SKIP_STEMS` to drop an
episode from every arm at once. With both unset, `mech.py` reproduces the
previous `mech.json` **byte-identically**. Mention density per 1000 words is the
one metric none of the existing scripts computed; it is added in a separate
`density.py` rather than by editing them.

All figures are **raw, unrepaired** unless the section says otherwise.

---

## 1. Run log: tokens, thinking, wall time

| episode | HTTP | output tokens | thinking | wall | stop | parse | mentions |
|---|---|---|---|---|---|---|---|
| 0212 | 200 | 18,913 | 20,275 ch | 355 s | end_turn | ok | 188 |
| 0500 | 200 | 20,139 | 21,181 ch | 431 s | end_turn | ok | 213 |
| 79 | 200 | 51,908 | 132,095 ch | 934 s | end_turn | ok | 294 |
| 0728 attempt 1 | 200 | **64,000 (wasted)** | 225,233 ch | 1,156 s | **max_tokens** | **empty** | 0 |
| 0728 attempt 2 | 200 | 12,849 | 13,966 ch | +192 s | end_turn | ok | 167 |
| **4-episode total** | — | **167,809** (**103,809 productive**) | — | **~3,068 s** | — | — | **862** |
| *0650 attempt 1 (excluded)* | 200 | *64,000 (wasted)* | *171,548 ch* | *1,214 s* | *max_tokens* | *empty* | *0* |
| *0650 attempt 2 (excluded)* | 200 | *64,000 (wasted)* | *218,292 ch* | *915 s* | *max_tokens* | *empty* | *0* |

Every episode that produced text produced clean JSON with no markdown fence.

**Cost column reading.** Thinking dominates. On the four scored episodes kimi
burned 167,809 output tokens to deliver 862 mentions — 195 output tokens per
mention, and that is *after* excluding 0650. 64,000 of those tokens (38%) bought
nothing at all, spent entirely on 0728's failed first attempt. Wall time runs
355–1,348 s per episode; a 719-episode production run at this rate is on the
order of 150–250 hours of serial API time before any retries.

### 1.1 Episode 0650 and the silent budget-exhaustion failure

0650 is the reliability finding, and it generalises beyond one episode.

Twice, at `max_tokens=64000`, kimi consumed the **entire** output budget on
thinking (171,548 and 218,292 characters) and returned an **empty text block**
with `stop_reason: max_tokens`. Both responses were **HTTP 200**. There is no
error, no partial JSON, no signal at the transport layer that anything went
wrong — a naive pipeline records a successful call and an episode with zero
mentions. 0728 hit the identical failure and was only rescued by the scripted
retry.

So on this 5-episode sample the 64k cap silently destroyed **2 of 5 episodes
(40%)**, and one of them stayed destroyed across a retry. That is the number
that matters for a production run: the failure is invisible, it is not rare, and
it is not reliably fixed by retrying.

For completeness, and because it bounds the fix: 0650 *did* eventually succeed
when re-run at `max_tokens=200000`, emitting **73,613 output tokens** — above
the 64k cap, confirming the cap rather than the content was the cause. That
output exists at
`research/bakeoff/kimi/0650-accessible-asics-with-andreas-olofsson.json` (278
mentions) and is **excluded from every figure in this report** because it was
produced under a different token budget than the other four and is therefore not
comparable. It is retained on disk rather than deleted so the decision stays
reversible.

Operationally: any production use of this arm needs `max_tokens` near 200k, an
explicit `stop_reason == "max_tokens"` guard, and an empty-text assertion.
None of those are optional, and the cost implication of a 200k budget on an arm
that already averages 42k output tokens per episode is not small.

---

## 2. Mechanical validation, raw (4 episodes)

| episode | mentions | offsets valid | verbatim anywhere | verbatim in stated para | snippet >100 | dup (concept,para) | enum errors | coverage | max para | speaker | explains/opinion/mention |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0212 | 188 | 0/188 (0%) | 99.5% | 99.5% | 7 | 0 | 0 | 99/246 (40.2%) | 244/246 | 100% | .39 / .23 / .38 |
| 0500 | 213 | 0/213 (0%) | 100% | 17.8% | 13 | 1 | 1 | 136/385 (35.3%) | 343/385 | 55.9% | .31 / .37 / .32 |
| 0728 | 167 | 0/167 (0%) | 85.6% | 44.3% | 25 | 0 | 0 | 49/88 (55.7%) | 80/88 | 100% | .44 / .32 / .24 |
| 79 | 294 | 0/294 (0%) | 91.2% | 21.4% | 6 | 0 | 0 | 171/416 (41.1%) | 410/416 | 22.8% | .27 / .24 / .49 |
| **total** | **862** | **0/862 (0%)** | **94.1%** | **42.0%** | **51 (5.9%)** | **1** | **1** | — | — | **62.8%** | **.34 / .29 / .38** |

Enum validity is otherwise clean: **zero** invalid `type`, **zero** invalid
`depth`, **zero** malformed `concept` strings across all 862 mentions. The one
enum error is a single `asr_suspect` set to a non-`true` value in 0500.

### 2.1 The offsets are estimated, not shifted

Kimi scores 0% on offsets like opus does, but **for a completely different and
much worse reason**, and the two must not be conflated.

Opus's offsets are wrong by a **constant +1** with zero exceptions — a
defensible reading of an ambiguous sentence in the prompt, fully repairable by a
one-line convention change. Both alternative conventions were tested here:

| hypothesis | opus | kimi |
|---|---|---|
| `off_by_one_newline` (+1) | 1488 | **0** |
| `whole_file` (offset into raw file incl. frontmatter) | 0 | **0** |
| `paragraph_relative` | 0 | **0** |
| other / non-constant | 0 | **811** |
| unlocatable snippet | 0 | 51 |

Kimi matches **neither** the +1 convention nor the whole-file convention nor
paragraph-relative offsets. Deltas are non-constant with **141–255 distinct
values per episode**, ranging from −23,761 to +20,536. On 0212 the maximum
`char_start` is 96,880 against a body of 75,586 characters — an offset that
cannot correspond to any convention, because it points past the end of the text.

Pearson r between stated and true offset is nonetheless 0.987–0.9996. That
signature — strongly monotone but drifting by thousands of characters — is a
model *estimating* a plausible running character count as it walks the
transcript, not computing one. The offsets carry ordering information and no
positional precision. As a verifiable locator, which is the entire reason
`char_start` exists in the spec, they are unusable as emitted.

### 2.2 Paragraph indices drift on three of four episodes

The gap between `verbatim anywhere` (94.1%) and `verbatim in stated paragraph`
(42.0%) is the second defect. Snippets are overwhelmingly real text copied from
the transcript, but on 0500 (17.8%), 79 (21.4%) and 0728 (44.3%) they are
attributed to the wrong paragraph. Speaker accuracy tracks it exactly — 22.8% on
79 and 55.9% on 0500 versus 100% on 0212 and 0728 — confirming one underlying
fault (index drift) rather than two independent ones. Only 0212 holds both
indices and speakers essentially perfectly.

`repair_validate.py` needed its `resync-paragraph` strategy on **449 of 862
mentions (52%)**.

### 2.3 Snippet length

51 snippets (5.9%) exceed the 100-character hard limit, maximum 149. Better than
sonnet's 103 (26.2%) and worse than opus's 0. Violations concentrate in 0728
(25) and 0500 (13).

### 2.4 Header blocks

`episode`, `title` and `url` are correct on all four episodes. `main_topics` is
3 entries on every episode and **every topic appears in `mentions`** on all
four. Guest name and affiliation are correct throughout. The one header defect
is the `file` field, wrong on **2 of 4** episodes (0728 and 79).

### 2.5 What repair recovers

Not part of the raw score, recorded because it changes how this arm would be
operated. `repair_validate.py` on the 4-episode subset:

```
files=4  mentions=862  offsets 0 -> 811  unresolvable=51  errors 1238 -> 130
repairs: exact-in-stated-paragraph=362, exact-in-same-speaker-paragraph=449,
         resync-paragraph=449, unresolvable=51
remaining: offset-mismatch=51, snippet-too-long=51, speaker-mismatch=23,
           header-file-mismatch=2, duplicate-concept-paragraph=2, asr-suspect-value=1
```

94.1% of offsets are recoverable because the snippets are genuine, but **51
mentions (5.9%) are permanently unresolvable** — their snippet text does not
occur in the body at all, so they are either paraphrased or fabricated. Opus
left zero unresolvable; sonnet left zero. This is the residue no repair pass can
fix, and the number to weigh against kimi's higher yield.

---

## 3. Density and depth against the spec (4 episodes)

### Mentions per 1000 words (spec band 10.8–21.6)

| episode | words | opus | sonnet | kimi |
|---|---|---|---|---|
| 0212 | 13,724 | 28.3 | 7.1 | **13.7** |
| 0500 | 15,962 | 24.4 | 5.9 | **13.3** |
| 0728 | 12,663 | 22.0 | 5.7 | **13.2** |
| 79 | 13,749 | 31.3 | 9.5 | **21.4** |
| **corpus** | 56,098 | 26.5 | 7.0 | **15.4** |

**Kimi is the only arm inside the spec band, and it is inside on all four
episodes.** Opus is above the band on all four; sonnet is far below at 7.0,
roughly two-thirds of the way under the floor. Against the prompt's own stated
expectation of 150–300 mentions per episode, kimi lands at 167–294 — squarely
inside — while sonnet returns 72–130 and opus 279–431.

### Depth distribution against the 25–33% `explains` anchor

Corpus-wide kimi sits at **33.8% `explains`**, marginally *above* the anchor's
ceiling (opus 25.3%, sonnet 30.3% — both inside). Per episode kimi is far more
volatile than either arm: 0728 at 43.7% and 0212 at 38.8% are both well outside,
0500 (31.0%) and 79 (26.9%) inside. The prompt warns specifically that an
`explains` share drifting above a third means assertions are being counted as
explanations; on half these episodes kimi is doing exactly that.

---

## 4. Alignment against the opus reference arm (same 4 episodes)

### Mention-level

| episode | opus | kimi | matched | opus-only | kimi-only | identical name |
|---|---|---|---|---|---|---|
| 0212 | 388 | 188 | 114 | 274 | 74 | 77.2% |
| 0500 | 390 | 213 | 56 | 334 | 157 | 89.3% |
| 0728 | 279 | 167 | 59 | 220 | 108 | 91.5% |
| 79 | 431 | 294 | 191 | 240 | 103 | 86.4% |
| **total** | **1488** | **862** | **420** | **1068** | **442** | **85.0%** |

Of the 420 matched pairs: 85.0% identical concept name, 83.3% identical `type`,
71.4% identical `depth`. Sonnet on the same 4 episodes: 231 matched, 83.5% /
82.7% / 55.8% — kimi agrees with opus on depth markedly more often.

Caveat: `align_episode` only pairs mentions within a paragraph delta of 1, so
kimi's index drift (§2.2) mechanically suppresses its match rate on exactly the
episodes where indices are broken — 0500 (56 matched) and 0728 (59) are the two
worst, and both are index-drift episodes. The concept-level figures below are
paragraph-independent and are the fairer read.

### Concept-level (fuzzy inventory intersection)

| episode | opus concepts | kimi concepts | intersection | kimi recall vs opus | kimi-only concepts |
|---|---|---|---|---|---|
| 0212 | 226 | 181 | 110 | 48.7% | 70 |
| 0500 | 235 | 206 | 129 | 54.9% | 81 |
| 0728 | 179 | 160 | 95 | 53.1% | 63 |
| 79 | 226 | 235 | 153 | 67.7% | 80 |
| **total** | **866** | **782** | **487** | **56.2%** | **294** |

**Kimi recovers 56.2% of opus's concept inventory against sonnet's 22.1% on the
identical 4 episodes — a 2.5x improvement**, and contributes 294 concepts opus
did not name (sonnet: 120). On episode 79 kimi proposes more distinct concepts
than opus (235 vs 226).

Of the 1,068 opus mentions kimi did not match, 49.3% are concepts kimi *did*
name elsewhere in the episode (a frequency-counting difference) and 50.7% are
concepts kimi never named at all. Sonnet's equivalent split is 19.9% / 80.1%,
i.e. sonnet's misses are overwhelmingly genuine absences while kimi's are
roughly half bookkeeping.

---

## 5. Summary against the other arms (all 4-episode figures)

| metric | sonnet | opus | **kimi** |
|---|---|---|---|
| mentions | 393 | 1488 | **862** |
| mentions / 1000 words | 7.0 | 26.5 | **15.4** (only arm in the 10.8–21.6 band) |
| offsets valid (raw) | 100% | 0% | **0%** |
| offset error structure | n/a | constant +1, repairable | **non-constant, estimated** |
| offsets repairable | n/a | 100% | **94.1%; 51 unresolvable** |
| verbatim in stated paragraph | 100% | 100% | **42.0%** |
| snippets >100 ch | 103 (26.2%) | 0 | **51 (5.9%)** |
| dup (concept,para) pairs | 8 | 0 | **1** |
| enum errors | 1 | 0 | **1** |
| speaker accuracy | 100% | 100% | **62.8%** |
| coverage range | 21–44% | 57–74% | **35–56%** |
| explains share | 30.3% | 25.3% | **33.8%** (just above anchor) |
| concept recall vs opus | 22.1% | — | **56.2%** |
| identical name on matched | 83.5% | — | **85.0%** |
| identical depth on matched | 55.8% | — | **71.4%** |
| episodes lost to silent API failure | 0 | 0 | **2 of 5 at 64k budget** |

---

## 6. Anomalies

1. **Silent budget exhaustion cost 2 of 5 episodes** (§1.1). HTTP 200, empty
   text block, `stop_reason: max_tokens`. This is a production blocker in its
   current form, not a tuning detail — the failure is invisible at the transport
   layer and survived a retry on 0650.
2. **`char_start` is estimated, not computed** (§2.1). Unlike the opus +1
   artifact this is a real capability gap, and it means the spec's integrity
   check cannot be run on kimi output without a repair pass first.
3. **Paragraph-index drift on 3 of 4 episodes** (§2.2), dragging speaker
   accuracy to 22.8% on episode 79 and requiring `resync-paragraph` on 52% of
   all mentions.
4. **51 snippets (5.9%) do not occur in the transcript at all** — the only
   evidence of outright fabricated evidence strings among the three arms.
5. **Usage reporting is unreliable on retries.** Retry requests reported
   `input_tokens` of 123 and 243 against a ~16k–27k-token payload. The 0728
   retry output is demonstrably genuine (correct title, correct guest
   `Alex Haro` / `Hubble`, 143/167 snippets verbatim from the body), so this is
   a gateway accounting artifact and not a truncated request — but token-based
   cost tracking on this endpoint cannot be trusted across retries, which
   matters given §1's cost column.
6. **Thinking overhead is the dominant cost.** 195 output tokens per delivered
   mention across the four scored episodes, 38% of output tokens bought nothing,
   and the two longest-thinking episodes (0728 at 225k characters, 0650 at 218k)
   are exactly the two that failed.

Semantic adjudication of sampled mentions is deliberately not attempted here;
that is the later judging step.
