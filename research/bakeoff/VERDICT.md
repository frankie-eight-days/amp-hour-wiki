# Concept-Census Bake-off: Sonnet 5 vs Opus — Verdict

Judged against `research/census_prompt_v2.md`, using `research/census_lib.py` /
`research/repair_validate.py` (self-test: PASS, 5 paragraphs, 12 planted issues
verified). All validation below is on **raw, unrepaired** output unless stated.

Corpus: 5 episodes, 69,545 words total (mean 13,909/episode).
Sonnet 479 mentions; Opus 1,847 mentions.

---

## 1. Mechanical validation (raw, unrepaired)

### Sonnet 5

| episode | mentions | offsets valid | snippet >100 | dup (concept,para) | enum errors | coverage | max para | explains/opinion/mention |
|---|---|---|---|---|---|---|---|---|
| 0212 | 97 | 97/97 (100%) | 35 | 1 | 0 | 75/246 (30.5%) | 240/246 | .35 / .23 / .42 |
| 0500 | 94 | 94/94 (100%) | 20 | 3 | 0 | 82/385 (21.3%) | 366/385 | .29 / .37 / .34 |
| 0650 | 86 | 86/86 (100%) | 27 | 2 | 0 | 68/197 (34.5%) | 192/197 | .29 / .33 / .38 |
| 0728 | 72 | 72/72 (100%) | 40 | 4 | 0 | 39/88 (44.3%) | 82/88 | .28 / .40 / .32 |
| 79 | 130 | 130/130 (100%) | 8 | 0 | 1 | 107/416 (25.7%) | 406/416 | .29 / .29 / .42 |
| **total** | **479** | **479/479 (100%)** | **130 (27.1%)** | **10** | **1** | — | — | — |

### Opus

| episode | mentions | offsets valid | snippet >100 | dup (concept,para) | enum errors | coverage | max para | explains/opinion/mention |
|---|---|---|---|---|---|---|---|---|
| 0212 | 388 | 0/388 (0%) | 0 | 0 | 0 | 159/246 (64.6%) | 244/246 | .24 / .32 / .44 |
| 0500 | 390 | 0/390 (0%) | 0 | 0 | 0 | 221/385 (57.4%) | 376/385 | .26 / .35 / .39 |
| 0650 | 359 | 0/359 (0%) | 0 | 0 | 0 | 142/197 (72.1%) | 193/197 | .25 / .34 / .42 |
| 0728 | 279 | 0/279 (0%) | 0 | 0 | 0 | 65/88 (73.9%) | 84/88 | .31 / .41 / .28 |
| 79 | 431 | 0/431 (0%) | 0 | 0 | 0 | 235/416 (56.5%) | 411/416 | .22 / .37 / .41 |
| **total** | **1847** | **0/1847 (0%)** | **0** | **0** | **0** | — | — | — |

### The Opus 0% offset score is an artifact, not a defect

This is the single most important mechanical finding, and it inverts the
headline number. For **all 1,847 Opus mentions across all five episodes**:

```
body[char_start + 1 : char_start + 1 + len(snippet)] == snippet
```

The delta between true and stated offset is **exactly +1, constant, with zero
exceptions**; Pearson r between stated and true offset is 1.0000; every span
lands inside its stated paragraph. `repair()` fixed 100% of them with the single
strategy `exact-in-stated-paragraph`, leaving Opus with **zero** validation
errors of any kind.

Opus computed genuinely correct character offsets and resolved an ambiguity in
the prompt the other way. Prompt line 32–34 says the body is "everything after
the closing `---` of the frontmatter, with the single newline that follows it
stripped." After `---` the file contains `\n\n**Chris`. `census_lib` reads
"the single newline" as the one terminating the `---` line, leaving `\n**Chris`.
Opus read it as leaving `**Chris`. Both readings are natural. **The prompt is
ambiguous and the spec sentence is the bug, not the model.**

Sonnet resolved the same ambiguity the way `census_lib` does and scored 100%.
This is a coin-flip, not a capability difference — both models can count
characters into a 200 KB body essentially perfectly.

### Other mechanical facts

- **Verbatim snippets: 100% in both arms** (479/479 and 1847/1847), located
  verbatim *within the stated paragraph* in every case.
- **Snippet length:** Opus median 65, max exactly 100, **0 violations**. Sonnet
  median 77, p90 132, max 198, **130/479 = 27.1% over the hard cap**. These are
  auto-rejected downstream, so Sonnet's *effective* yield is 349, not 479.
- **Speaker labels:** Opus 100% correct. Both arms correctly preserved the
  corrupted `Parallela` label on episode 650 and named the guest Andreas
  Olofsson.
- **Enum/format validity:** both arms clean, except Sonnet's one
  `asr_suspect: false` on episode 79 (the field must be present only when true).
- **Header blocks:** both arms match frontmatter on title/url/file, carry 3
  `main_topics`, and every main topic appears in `mentions`. One error: **Sonnet
  set `episode: null` on episode 79, whose frontmatter contains `episode: 79`**
  — it applied the legacy-episode rule to a file that has the field. Opus got it
  right.
- **`notes`:** Opus flagged broken diarisation on all five episodes; Sonnet
  flagged only episode 650. Diarisation is visibly merged/mislabelled on all
  five, so Sonnet under-reports a field downstream consumers depend on.

### Both arms miss the prompt's own yield band

The prompt asks for 150–300 mentions per hour-long episode (≈10.8–21.6 per 1,000
words on this corpus).

| | mentions/1000 words | vs spec band |
|---|---|---|
| Sonnet | 6.9 | **2.3× below the floor**; 0/5 episodes in band |
| spec band | 10.8 – 21.6 | — |
| Opus | 26.6 | **1.2× above the ceiling**; 1/5 episodes in band |

Neither arm is the ground truth. Opus is closer, but it overshoots the spec's
own anchor, and the depth band confirms it: Opus's `explains` share is in the
25–33% band on 2/5 episodes (dipping to .22), Sonnet's on 4/5.

---

## 2. The density gap — who is right?

Mentions were aligned across arms (paragraph delta ≤1, concept identical or
fuzzy-matched). Result: **279 matched pairs, 1,568 Opus-only, 200 Sonnet-only.**

I read the transcript passage for every sampled mention and judged it against
the prompt's mechanical emission rule (§Coverage rule 2), its sponsor/small-talk
exclusions (rules 3–5), and its type/depth definitions. Three verdicts were
needed rather than two, because a large share of "misses" turned out to be
alignment failures where Sonnet *did* cover the material under a different name:

- **genuine-miss** — concept named (or unambiguously pronoun-referenced) in the
  paragraph, census-worthy, and absent from Sonnet's output for that paragraph.
- **over-emission** — violates the emission rule (not named, referent not
  resolvable from that paragraph or the one before) or falls inside an exclusion.
- **artifact** — the other arm covered the same material under a different
  canonical name; the matcher, not the model, failed.

### 2a. Forty Opus-only mentions (stratified by episode and depth)

| # | episode | concept | depth | verdict | note |
|---|---|---|---|---|---|
| 1 | 212 | `can-bus` | mention | genuine-miss | "So I made some, like, CAN adapters" — named. Sonnet took 1 of 6 named concepts in p33 |
| 2 | 212 | `firmware-update` | explains | genuine-miss | bootloader-based update mechanism spelled out |
| 3 | 212 | `maker-community` | opinion | genuine-miss | "de facto standard for the maker community" — named |
| 4 | 212 | `assembly-language` | opinion | genuine-miss | "you mentioned like assembly" — named; Sonnet emitted nothing in p128 |
| 5 | 212 | `mips` | opinion | **over-emission** | MIPS never named; "use up every last little resource" is inferred, not named |
| 6 | 212 | `sensorless-control` | explains | genuine-miss | "we don't have a hall sensor… we measure the currents and voltages" |
| 7 | 212 | `power-stage` | mention | genuine-miss | "more efficiency out of your power stage" — named |
| 8 | 212 | `c28x` | mention | artifact | Sonnet has `c28x-core` in the same paragraph |
| 9 | 500 | `breadboard` | mention | genuine-miss | named; Sonnet emitted nothing in p47, also losing `fan-out:explains` |
| 10 | 500 | `motor-driver` | mention | genuine-miss | "like motor drivers and stuff like that" — named |
| 11 | 500 | `netflix` | mention | **over-emission** | streaming-catalogue small talk; no engineering content (rule 4) |
| 12 | 500 | `self-directed-learning` | opinion | genuine-miss | "do amazing things at home and on their own"; `career` covers "how people learn" |
| 13 | 500 | `din-connector` | explains | genuine-miss | "a DIN connector is your traditional circular plug" — a definition |
| 14 | 500 | `open-hardware-license-icon` | opinion | **over-emission** | the icon is never named; passage states the problem only |
| 15 | 500 | `esp32` | explains | genuine-miss | ESP32 explicitly contrasted with ESP32-S2; distinct specificity levels |
| 16 | 500 | `cargo-cult-engineering` | opinion | artifact | Sonnet has `cargo-cult-electronics` |
| 17 | 500 | `chiplet` | explains | artifact | Sonnet merged into `z-glue-chiplets` (a spec violation, but covered) |
| 18 | 650 | `zero-asic` | mention | genuine-miss | named; Sonnet emitted nothing in p21 despite 5 named concepts |
| 19 | 650 | `tape-out` | explains | genuine-miss | "if the tape out is $20 million" — number with actionable context |
| 20 | 650 | `multi-project-wafer` | explains | genuine-miss | "MPW type things" named; Opus's `explains` is inflated here |
| 21 | 650 | `code-reuse` | opinion | genuine-miss | "it has zero reuse factor" — named |
| 22 | 650 | `cpu` | opinion | genuine-miss | "the CPU is just not going to be good enough"; low value but legal |
| 23 | 650 | `chiplet` | opinion | genuine-miss | "an infinite number of chiplets" — named |
| 24 | 650 | `mouser` | mention | genuine-miss | "You go up to DigiKey or Mouser" — named |
| 25 | 650 | `product-tiering` | explains | genuine-miss | "small, medium, large, and extra large… the bigger, the more expensive" |
| 26 | 650 | `chiplet-interface-standard` | mention | genuine-miss | "that standard" resolvable within the paragraph |
| 27 | 728 | `2-4-ghz-band` | explains | genuine-miss | named + explained; Sonnet took 6 of 15 from a 3,841-char paragraph |
| 28 | 728 | `spread-spectrum` | opinion | genuine-miss | "the sped spectrum nature" — recoverable ASR garble |
| 29 | 728 | `wch` | mention | genuine-miss | company named; spec says companies keep their own name |
| 30 | 728 | `mark-rober` | mention | genuine-miss | named person in a use-case discussion |
| 31 | 728 | `network-as-a-service` | opinion | genuine-miss | "they kind of rent that hard part from you" |
| 32 | 728 | `space-hardware-reliability` | explains | genuine-miss | failure modes with the reason you can't fix them |
| 33 | 79 | `pcb-cart` | opinion | **over-emission** | "they" — p75 never names PCBCart; referent not resolvable (verified) |
| 34 | 79 | `pcb-milling` | mention | genuine-miss | "a board mill is in there as well" — named |
| 35 | 79 | `3d-printer` | mention | genuine-miss | "It's a 3D printer" — named |
| 36 | 79 | `motion-detection` | explains | genuine-miss | "does motion sensing" named; Opus's `explains` is inflated |
| 37 | 79 | `consumer-electronics-commoditisation` | opinion | **over-emission** | "they" carried across p238 = "Yeah." — the exact carry-forward the spec forbids |
| 38 | 79 | `ucsf` | mention | genuine-miss | named institution; Sonnet collapsed p288 into one concept, losing 5 |
| 39 | 79 | `svg` | opinion | genuine-miss | "outputting in an SVG" — named |
| 40 | 79 | `pcb-pricing` | explains | artifact | Sonnet has `cheap-pcb-fabrication-history` |

**Totals (a): genuine-miss 31/40 (77.5%), over-emission-by-Opus 5/40 (12.5%),
alignment artifact 4/40 (10%).**

Opus's over-emissions are not random noise — they are a coherent, narrow failure
mode. Two of the five (#33, #37) are the *same* violation: carrying a concept
forward through a paragraph whose only pronoun has no resolvable referent, which
the prompt explicitly prohibits and illustrates with a worked example. Two more
(#5, #14) are concepts inferred from a passage rather than named in it. One (#11)
is small talk. Extrapolated, roughly **12% of Opus's 1,568 extra mentions (~190)
are rule violations** — real, but far short of explaining a 4× density gap.

### 2b. Fifteen Sonnet-only mentions

| # | episode | concept | depth | verdict | note |
|---|---|---|---|---|---|
| 1 | 212 | `can-bus-security` | explains | artifact | Opus split the same passage into 5 finer concepts |
| 2 | 212 | `dynamic-load-response` | opinion | artifact | Opus has `dynamic-load` |
| 3 | 212 | `sparkfun-autonomous-vehicle-competition` | mention | **miss-by-Opus** | Opus emitted only `sparkfun`; the competition is a separate concept (but Sonnet's expansion of ASR "ABC" is an unsupported guess) |
| 4 | 500 | `skywater-pdk` | mention | **over-emission** | passage says "Google is the new open source PDK" — SkyWater never named; guessed |
| 5 | 500 | `open-source-chip-fabbing` | explains | artifact | Opus has `open-source-silicon` |
| 6 | 500 | `magic-layout-tool` | opinion | **over-emission** | speaker says he can't recall the name; the Java tool described is Electric, **not** Magic — a wrong canonical name, which the spec calls worse than a flagged unknown |
| 7 | 650 | `darpa-commute` | mention | **over-emission** | DARPA not named in p50; p49 is "Yeah. Yeah. Yeah. Yeah." |
| 8 | 650 | `aerospace-defense-market` | opinion | artifact | Opus has `aerospace-and-defence` |
| 9 | 650 | `open-source-contribution-scarcity` | explains | artifact | Opus has `open-source-contribution`; Sonnet also emitted it twice in one paragraph |
| 10 | 728 | `digital-beamforming` | explains | **miss-by-Opus** | "the beam forming is actually a lot harder to do" — named in p9; Opus emitted 13 concepts there but not this one |
| 11 | 728 | `crowdsourced-gateway-network` | opinion | **over-emission** | nothing crowdsourced in the passage; Opus's `terrestrial-gateway-network` is correct |
| 12 | 728 | `iridium-constellation` | mention | artifact | Opus has `iridium` |
| 13 | 79 | `make-vs-buy-pcb` | explains | artifact | Opus has `make-vs-buy` — the spec's own vocabulary |
| 14 | 79 | `prototype-to-production-timeline` | opinion | **miss-by-Opus** | Opus framed the passage as `systems-engineering`; Sonnet's concept fits better |
| 15 | 79 | `spi-bus` | mention | artifact | Opus has `spi`, the canonical industry name |

**Totals (b): alignment artifact 8/15 (53%), over-emission-by-Sonnet 4/15 (27%),
genuine-miss-by-Opus 3/15 (20%).**

Two conclusions. First, Opus is **not** a strict superset — it misses real
material (#3, #10, #14), so ~20% of Sonnet's 200 unique mentions (~40) are
genuine additions. Second, and more serious: **27% of Sonnet's unique mentions
break the emission rule**, and two of the four (#4 `skywater-pdk`,
#6 `magic-layout-tool`) are confidently-asserted wrong canonical names — exactly
the failure the spec singles out as "worse than a flagged unknown one, because it
merges silently into the wrong wiki article." Sonnet used `asr_suspect` zero
times across all five episodes; Opus used it four times. Sonnet is not being
conservative, it is being confidently wrong in the places the spec warns about.

### 2c. Recall for `explains`-depth material — the wiki-value number

Opus emitted 465 `explains` mentions: 117 matched to a Sonnet mention, 348 with
no counterpart. Twelve of the 40 adjudicated mentions were `explains`, and they
split **10 genuine-miss / 2 artifact / 0 over-emission** — the over-emission rate
in the `explains` stratum is zero, meaning Opus's extra *teaching* material is
essentially all legitimate. Applying the 16.7% artifact rate to the 348:

| quantity | value |
|---|---|
| Opus `explains` total | 465 |
| …matched to any Sonnet mention | 117 |
| …Opus-only but covered by Sonnet under another name (16.7% of 348) | ≈58 |
| …genuinely missed by Sonnet (83.3% of 348) | ≈290 |
| **Sonnet recall of Opus `explains` material (any depth)** | **175/465 ≈ 38%** |
| **…recall that also preserves `depth: explains`** | **≈84/465 ≈ 18%** |

**Judge-sampled estimate: Sonnet recovers roughly 35–40% of the explains-depth
material Opus finds, and preserves the `explains` label on roughly 18%.**

*Confidence caveat.* This rests on 12 adjudicated `explains` items. The 95%
interval on the 2-of-12 artifact rate is roughly 5–41%, which propagates to a
recall interval of **≈29–56%**. The point estimate is stable in the sense that
even its optimistic end leaves Sonnet losing about half the teaching material.
Two further caveats push in opposite directions: Opus's `explains` label is
itself inflated on some items (#20, #36 above), which shrinks the true
denominator; and Sonnet's 27% over-length snippets are auto-rejected downstream,
which shrinks its true numerator. I did not attempt to quantify either.

<!-- SECTION3 -->

---

*Sections 1–2c above were written by the judging agent, which was repeatedly
killed by API connection drops before it could finish. Sections 3–5 below were
written by the session lead from the judge's completed adjudication data and the
tooling agent's mechanical report. No new adjudication was performed.*

## 3. Concept-name agreement

From the alignment pass (matched pairs, n=279): **85.7% identical canonical
names**; the rest are mostly specificity/compounding variants (`spi` vs
`spi-bus`, `make-vs-buy` vs `make-vs-buy-pcb`, `iridium` vs
`iridium-constellation`), with Sonnet biased toward longer compound names. At
the concept-inventory level, 44.5% of "absent" Opus concepts share a content
token with some Sonnet concept — a naming difference, not a coverage
difference. Consequences: (a) canonicalization must fuzzy-merge on head tokens,
which was already planned; (b) raw inventory-overlap numbers understate
Sonnet's true coverage, which is why the adjudicated sample, not the inventory
diff, is the recall estimate of record.

## 4. Verdict

**Neither arm, as configured, is the production system.**

- **Sonnet 5 + v2 prompt is not acceptable.** Adjudicated recall on
  `explains`-depth material — the wiki's entire reason to exist — is ≈35–40%
  (CI 29–56%). Even the optimistic end loses half the teaching content, and
  the loss mechanism (whole concepts absent, 79% of the gap) cannot be
  repaired downstream: what was never extracted can't be ranked, cited, or
  synthesized. Compounding it, Sonnet's unique output runs a 27% over-emission
  rate including confidently-wrong canonical names (`skywater-pdk`,
  `magic-layout-tool` for what is actually Electric) with `asr_suspect` used
  zero times — the exact silent-merge poison the spec warns about.
- **Opus + v2 prompt is the quality reference but not affordable at census
  scale** (≈5× Sonnet's price across ~23M tokens/pass × 2 passes). Its 12%
  over-emission rate is a narrow, mechanically-lintable failure mode
  (pronoun carry-forward), and its `explains` stratum sampled at 0%
  over-emission — its extra teaching material is essentially all real.
- The offset "failure" was a prompt ambiguity, not a model failure. Both
  models quoted 100% verbatim and located 100% of snippets in the stated
  paragraph. Conclusion confirmed: **drop `char_start` from model output**;
  the pipeline computes offsets by exact string search of the (validated)
  snippet within the stated paragraph. This deletes the ambiguity, the
  arithmetic burden, and a whole class of validation failures at once.

**Root cause of Sonnet's undersweep** is attention budget, not capability:
coverage tracks paragraph count (21–44% of paragraphs touched vs Opus's
56–74%), and quality-per-mention is fine when it does emit. It sweeps too
coarsely on a 14k-word input; it does not misunderstand the task.

## 5. Prescription — prompt/pipeline v3

1. **Drop `char_start` from the model schema.** Pipeline computes it
   (string-search in stated paragraph); "snippet not found" = auto-reject.
   Also fixes the ambiguous body-definition sentence by making it moot.
2. **Chunked extraction.** Feed each episode in ~3,000-word chunks (with
   one-paragraph overlap and running paragraph numbering) instead of one
   14k-word slab. This attacks the attention-budget root cause directly and
   is the change most likely to close the recall gap. Cost: prompt repeated
   ~5× per episode → roughly $60–70 per full pass on Sonnet with Batch API
   (vs ~$50), still ≈4× cheaper than an Opus pass.
3. **Per-paragraph sweep instruction + yield anchor**: "for each paragraph,
   enumerate every named concept before moving on"; state the expected yield
   (10–22 mentions per 1,000 words) as a per-chunk anchor, and flip the
   ambiguity bias to "when in doubt whether a named concept is worth a
   mention-depth record, emit it."
4. **Snippet cap moves to the validator** (reject >100 chars, reject
   non-verbatim, reject duplicate (concept, paragraph) pairs) with
   reject-and-retry per chunk — Sonnet's 27% cap violations and 10 dups all
   become retries instead of data loss.
5. **`asr_suspect` becomes mandatory-when-expanding**: any canonical name not
   appearing verbatim (or near-verbatim) in the snippet's paragraph must
   carry `asr_suspect: true`. Kills the confidently-wrong-name failure.
6. **Re-test before the full run**: Sonnet + v3 on 2 of the 5 bake-off
   episodes, scored with the same alignment tooling against the frozen Opus
   reference. Gate: explains-recall ≥70% and wrong-name rate ≈0 in a
   20-item sample. If Sonnet+v3 clears it, run the census on Sonnet; if it
   narrowly misses, consider Sonnet for sweep + Opus for a second
   explains-only pass on flagged-dense paragraphs before paying full Opus
   rates.

## 6. Recommendation

Chunked Sonnet 5 with the v3 prompt and validator-enforced schema, gated on
the 2-episode re-test against the Opus reference. Do not launch the 719-episode
run until the re-test clears.
