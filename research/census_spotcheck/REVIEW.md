# Concept census — 5-episode spot check review

Prompt under test: `research/census_prompt.md` (v1).
Extractions: five `*.json` files in this directory.
Extraction was performed by the same model that wrote the prompt, applying it to
the full transcript of each episode.

## 1. Counts

| episode | words | paragraphs | mentions | substantive | % subst | unique concepts |
|---|---:|---:|---:|---:|---:|---:|
| 79 — Ludibrious Luxating Layout (2012, hosts only) | 13,757 | 416 | 279 | 260 | 93% | 250 |
| 212 — Trey German / TI (2014, interview) | 13,740 | 246 | 217 | 205 | 94% | 211 |
| 500 — Two and a Half Orders of Magnitude (2020, hosts only) | 15,976 | 385 | 188 | 184 | 98% | 183 |
| 650 — Andreas Olofsson / Zero ASIC (2023, interview) | 13,394 | 197 | 188 | 181 | 96% | 182 |
| 728 — Alex Haro / Hubble (2026, interview) | 12,676 | 88 | 172 | 166 | 97% | 169 |
| **total** | 69,543 | 1,332 | **1,044** | **996** | **95%** | 956 distinct |

Yield is roughly 13–20 mentions per 1,000 words. The hosts-only episodes are the
densest because the two of them cover eight or ten unrelated topics in an hour,
while an interview stays on one subject for forty minutes and re-mentions the
same six concepts.

## 2. The `substantive` flag is broken

**This is the most serious finding and it is a calibration failure, not a
transcript problem.** 95% of mentions came back `substantive: true`, which makes
the flag almost useless — it does not discriminate. The prompt says "when
genuinely ambiguous, prefer false", and that instruction plainly did not bind.

The cause is that on this show almost every sentence *does* carry some engineering
content, so "is there knowledge here?" answers yes nearly always. The question
that actually needs answering downstream is different: **would this passage be
worth quoting in a wiki article about this concept?** By that standard, my own
spot check suggests the honest rate is somewhere around 40–55%. Passages like
"they've got much better quality sensors in them" (episode 79, paragraph 178) got
`true` and should not have.

Recommended fix before the 719-episode run — replace the boolean with a
three-way `depth` field, which forces a discrimination the boolean does not:

- `"explains"` — the passage teaches the concept: a mechanism, a number, a
  trade-off with its reason, a procedure. (`fan-out`, episode 500 paragraph 49.)
- `"opinion"` — a judgement or war story about the concept without a full
  explanation. (`pcb-lead-time`, episode 79 paragraph 23.)
- `"mention"` — named only.

Keep `substantive` as a derived field (`depth != "mention"`) if downstream code
already wants a boolean, but make the model commit to the three-way choice. Add a
soft target to the prompt — "on a typical episode, expect roughly a quarter to a
third of mentions to be `explains`" — because an unanchored model will not
self-calibrate.

## 3. Canonicalization, as actually observed

Every one of these clusters appeared in the five transcripts. They are grouped by
what causes them, because each cause needs a different fix.

**ASR corruption of proper nouns** — the single largest source. The speech-to-text
pass mangles names it does not know, and there is no way to recover them from the
prompt alone:

| written in transcript | actual concept | episode |
|---|---|---|
| "Kycat", "key cat" | KiCad | 500, 650 |
| "bomb consolidation", "bomb optimization" | BOM | 500 |
| "I penalized my board" | panelized | 79 |
| "Vigilant", "Digilant" | Digilent | 500, 212 |
| "Laura" (throughout) | LoRa | 728 |
| "hyper" | Hiber | 728 |
| "Sam's aloof", "Sam's the roof" | Sam Zeloof | 500, 650 |
| "Hans Kammensund" | Hans Camenzind | 79 |
| "Bob Weidler" | Bob Widlar | 79 |
| "Adeptiva" | Adapteva | 650 |
| "InstaSpend" | InstaSpin | 212 |
| "Axie" | AXI | 650 |
| "certes", "a 30s PCI express 30s" | SerDes | 650 |
| "USB 32 didn't have that" | ESP32 | 500 |
| "2.4 megahertz band" | 2.4 GHz band | 728 |
| "IT Studios" / "IT Studio" | ITEAD Studio | 79 |
| "my PCB card is shut down" | PCBCart | 79 |
| "Deutsch Institute for Normung" | Deutsches Institut für Normung | 500 |

"SerDes" → "30s" is the worst case: the string carries no recoverable signal at
all, and I only resolved it because the surrounding sentence was about PCI
Express PHY design. A production run will silently drop or mis-canonicalize
concepts like this.

**Genuine synonymy in speech** — the same object under several names in one
episode. Episode 79 alone calls the same machine a *board cutter*, *board mill*,
*circuit board mill*, *PCB mill*, *LPKF*, and (via ASR) *"piece of bee mill"*.
Episode 500 has *scope* / *travel scope* / *analog discovery* pointing at
overlapping-but-not-identical things. Episode 650 uses *chiplet*, *die*, *brick*,
and *e-brick* for the same physical object within four paragraphs.

**Specificity collisions I created myself** — the prompt tells the model not to
merge across specificity levels, and the result is neighbouring concepts that a
merge pass will have to reconcile: `pcb-mill` (tool-equipment) vs `pcb-milling`
(technique) vs `board-cutter` (tool-equipment) are three canonical names for one
wiki article. Same for `chinese-new-year-shutdown` vs
`chinese-pcb-manufacturing`, and `ip-licensing-cost` vs `ip-outsourcing`.

**Conclusion:** canonicalization cannot be solved inside the per-episode prompt.
It needs a second stage. The practical shape is a growing controlled vocabulary:
run the census, cluster the ~150k raw concept strings the full corpus will
produce, hand-curate the top few thousand into canonical entries with aliases,
then re-run the census with that vocabulary injected as a "prefer these names"
list. Budget for two passes over the corpus, not one.

## 4. Sponsor reads and small talk

**No sponsor read appears in any of the five episodes.** The prompt's
sponsor-skipping rule was therefore never exercised and remains untested. What
does appear is house promotion — EEVblog kits, Contextual Electronics, listener
donations, the LibSyn hosting migration, a $1.99 podcast app. The prompt already
distinguishes these correctly and the extraction handled them as intended
(`listener-donations`, `podcast-app-monetization`, both retained, mostly
`substantive: false`). Before the production run, someone should grep the corpus
for sponsor-read markers ("brought to you by", "use code", "/amphour") to find out
whether later episodes carry them at all; if they do not, that section of the
prompt is dead weight.

Small-talk filtering worked well. Yield-zero digressions correctly produced no
mentions:

- Texas barbecue and brisket (212, paragraphs 10–11)
- the Halloween cross-dressing extra-credit story (212, paragraph 23)
- gym classes and motivation (500, paragraph 77)
- bad Amazon Prime sci-fi films (500, paragraphs 62–71)
- science stock photography (79, paragraphs 343–360)
- the Corgi-identified-as-a-dingo joke (650, paragraphs 166–167) — though this
  one legitimately yielded `model-vs-hardware-error`, which is a real distinction
  worth a wiki line

The rule that saved the extraction is rule 3 — "extract from small talk when it
carries engineering content". Under a naive small-talk filter, episode 79 would
have lost its entire Chinese New Year supply-chain discussion and episode 500
would have lost the PhD-precarity and textbook-pricing material, both of which are
exactly the kind of industry knowledge this wiki should carry. Keep that rule.

## 5. Type distribution

| type | count | share |
|---|---:|---:|
| career-business | 207 | 19.8% |
| technique | 142 | 13.6% |
| company-product | 136 | 13.0% |
| component | 130 | 12.5% |
| concept-principle | 86 | 8.2% |
| manufacturing | 81 | 7.8% |
| software | 78 | 7.5% |
| standard-protocol | 56 | 5.4% |
| tool-equipment | 35 | 3.4% |
| community-event | 34 | 3.3% |
| person | 30 | 2.9% |
| media-resource | 21 | 2.0% |
| material | 8 | 0.8% |
| other | 0 | 0% |

Read this as a description of the show more than of the schema: The Amp Hour is a
business-and-career podcast with electronics in it, not a component-reference
podcast. That is a real editorial signal for the wiki's structure.

### Schema changes I made, and why

Four types were added to the list in the brief:

- **`concept-principle`** (8.2%) — the original list had no home for physical laws
  and phenomena. Fan-out, the Miller plateau, path loss, angle of arrival, flux
  vectors, price elasticity and Moore's law are not techniques (nobody *does* a
  Miller plateau) and not components. This is the single most valuable addition;
  these entries are the show's most durable teaching content.
- **`media-resource`** (2.0%) — books, app notes, blogs, datasheets, training
  series. Episode 79 is half a book-recommendation show; the Linear Technology app
  notes, *Analog Secrets*, the Navy NEETS series and *Eccentric Orbits* have no
  other home and are exactly what a wiki reader wants linked.
- **`person`** (2.9%) — Jim Williams, Bob Widlar, Sergio Franco, Andrew Kahng,
  Ben Wild. These recur across episodes and deserve their own nodes; filing them
  under `company-product` would have destroyed that.
- **`material`** (0.8%) — Dibond, mylar, silicon interposers, etchant, organic
  substrate. Marginal at under 1%; **I would fold this into `manufacturing`
  before the production run.** It does not pay for its own complexity.

`company-product` was widened to cover institutions and agencies (DARPA,
Rose-Hulman, the Cleveland Foundation) rather than adding an `organization` type,
because the boundary between "company" and "institution" generates more coin-flips
than it resolves.

**`career-business` is now a dumping ground at 20%** and should be split before
the full run. It currently holds at least four distinct things: hiring and
careers, business models and pricing, funding and economics, and
engineering-organization dynamics (design-by-committee, the benevolent-dictator
model, self-review limits). Those last ones are arguably the wiki's best content
and they are invisible inside a bucket this large. Suggested split:
`career`, `business-model`, `industry-economics`, `engineering-practice`.

## 6. Concepts that obviously merge across these five episodes

Exact canonical-name matches across two or more of the five:

| concept | episodes |
|---|---|
| contextual-electronics | 212, 500, 650, 728 |
| open-source-hardware | 79, 212, 500, 650 |
| texas-instruments | 79, 212, 728 |
| usb | 79, 212, 650 |
| kickstarter | 79, 212, 650 |
| kicad | 79, 500, 650 |
| arduino | 79, 650, 728 |
| chiplet | 500, 650 |
| zglue | 500, 650 |
| sam-zeloof | 500, 650 |
| google-open-mpw-shuttle | 500, 650 |
| risc-v | 500, 650 |
| digi-key, mouser | 79, 650 |
| bluetooth | 212, 728 |
| raspberry-pi | 650, 728 |
| build-vs-buy | 212, 650 |
| bom-cost | 212, 728 |
| component-sourcing, hand-assembly, resistor-tolerance | 79, 500 |

Beyond exact matches, several thematic clusters plainly want to be one wiki
article each and are currently spread across differently-named entries:

- **Accessible custom silicon** — `skywater-pdk`, `open-pdk`, `process-design-kit`,
  `130nm-process-node`, `tiny-tapeout`, `multi-project-wafer`, `efabless`,
  `openroad`, `silicon-compiler`, `homemade-chip-fab`, `photolithography`,
  `desktop-chip-printer`. This is a through-line from episode 500 to episode 650
  and is arguably the show's biggest recurring story.
- **Build-versus-buy for IP and modules** — `make-vs-buy` (79),
  `build-vs-buy` (212, 650), `ip-licensing-cost` (650), `ip-outsourcing` (650),
  `module-cost` (79). Same argument, five names, four episodes.
- **Getting a low-cost board made** — the entire episode-79 PCB vendor cluster
  (`pcb-cart`, `circuit-labs`, `itead-studio`, `pcbzone`, `pcb-turnaround-time`,
  `pcb-lead-time`, `pcb-pricing`, `historic-pcb-cost`) plus episode 500's
  `pcb-assembly-turnaround`.
- **Standards get made by one company or two people in a room** —
  `standards-committee-process` (79, 650), `de-facto-standard` (650),
  `network-effect` (650), `10-gigabit-ethernet` (79), `amba` (650).
- **Motor control** — `field-oriented-control`, `clarke-transform`,
  `park-transform`, `sensorless-commutation`, `instaspin`, `three-phase-motor`,
  `ac-induction-motor` (all 212). Self-contained to one episode here, but this is
  clearly a recurring show topic.

## 7. Schema and prompt weaknesses to fix before 719 episodes

**7.1 `paragraph_index` is a poor locator on modern episodes.** Episode 728 has 88
paragraphs for 12,676 words — guest turns run past 900 words each. Paragraph 5
alone carries 13 distinct mentions and is a full page of text. Paragraph 20 has
another 13. The index is fine for episode 79 (416 short paragraphs) and useless
for episode 728. **Fix:** add `char_start`, the character offset of the
`context_snippet` within the transcript body, verifiable by exact string search.
That gives precise anchoring, and it also gives a free integrity check — if the
snippet is not found at that offset, the model paraphrased and the mention can be
rejected automatically.

**7.2 Speaker attribution is unreliable and the prompt only warns about it.**
Transcript paragraphs routinely merge both sides of an exchange under one label.
Episode 79 paragraph 20 is labelled Dave Jones but contains Chris asking "What's
that? Alibaba." and Dave answering. Roughly a fifth of the substantial paragraphs
in the hosts-only episodes have this problem. Every `speaker` value in this
spot-check inherits that error. **Fix:** either run a diarisation-repair pass
before extraction, or add a `speaker_confidence` field, or drop `speaker` from the
schema until the transcripts are cleaned. Do not build wiki attribution ("Dave
Jones argues that…") on the current data.

**7.3 Episode 650's speaker labels are corrupted at the file level.** The guest,
Andreas Olofsson, is labelled `**Parallela:**` — a product name — on essentially
every one of his turns, and `**Andreas Olofsson:**` appears on four stray
paragraphs including paragraph 0, which is actually Chris reading the cold open.
I recorded labels verbatim as the prompt requires and flagged it in the file's
`notes`. **Someone should scan all 719 transcripts for speaker labels that are not
plausible person names before the census runs**, because these produce
confidently wrong attribution rather than obviously missing attribution.

**7.4 Legacy frontmatter has no `episode` field.** The one legacy-named file in
this sample (`the-amp-hour-79-...`) has only `title` and `url`; the number is
recoverable from the filename, the URL, and the cold-open line, but not from the
frontmatter the prompt reads. There are other legacy-named files in
`transcripts/`. Backfill the field before the run rather than handling it in the
prompt.

**7.5 The `context_snippet` rules do not survive contact with generation.**
My own output violated them badly: 174 of 1,044 snippets exceeded 100 characters
and 185 contained mid-string `...` elisions, i.e. they were not verbatim
substrings. Both are explicitly forbidden by the prompt. I repaired them
mechanically after the fact. **The lesson is that this constraint must be enforced
by a validator in the pipeline, not by prompt text** — reject-and-retry on
`len > 100` or "snippet not found in paragraph". Cheap to implement, and it also
catches hallucinated quotes.

**7.6 The "one mention per paragraph in which it is carried forward" rule is
underspecified.** I applied it inconsistently: `pcb-fabrication`-adjacent concepts
in episode 79 got a mention in most paragraphs of a run, while `chiplet` in
episode 650 got one mention per *topic shift* rather than per paragraph. This
directly distorts frequency ranking, which is presumably how the wiki decides what
gets an article. **Fix:** state the rule as mechanical — emit a mention iff the
concept is named, or unambiguously referenced by pronoun, in that paragraph — and
give a counter-example in the few-shot set.

**7.7 No episode-level output.** Each file is a flat mention list. A production
census would benefit from a small header block: the two or three concepts the
episode is actually *about* (as opposed to merely mentions), and the guest's
identity and affiliation. That is cheap to add to the same call and saves a
separate pass later.

## 8. Token estimate for the production pass

Measured on this corpus (719 transcripts, 11.0M words total; median 14,586 words
per episode, mean 15,279, p90 18,917).

Per episode:

| | tokens |
|---|---:|
| static prompt (`census_prompt.md`) | ~3,400 |
| transcript, median episode | ~19,500 |
| transcript, p90 episode | ~25,300 |
| **input, typical** | **~23,000** |
| output, at ~200 mentions × ~45 tokens (compact JSON) | ~9,000 |
| output, dense hosts-only episode (280 mentions) | ~13,000 |

Full corpus, single pass: roughly **16.5M input tokens and 6.5M output tokens**.
On Claude Sonnet 5 at list pricing ($3/MTok in, $15/MTok out) that is about $50 in
and $98 out — call it **$150 per full pass**, plus a comparable amount for the
second pass that the canonicalization problem in section 3 requires. Sonnet 5 is
running introductory pricing of $2/$10 per MTok through 2026-08-31, which puts a
pass nearer $100 if the run happens before then.

Three notes on cost control:

- **Batch processing is the biggest lever** and applies cleanly, since these 719
  calls are independent, order-insensitive and not latency-sensitive. The Batches
  API is a flat 50% discount, halving the figures above to roughly $75 per pass at
  list pricing, or $50 at the introductory rate.
- **Prompt caching buys little here.** The cacheable prefix is only the ~3,400-token
  prompt, against a ~19,500-token per-episode transcript that cannot be cached
  across calls. At Sonnet 5's 1024-token minimum the prompt does clear the bar, but
  the expected saving is under 10% and cache writes cost 1.25x, so it barely pays
  for itself.
- **Test Haiku 4.5 before committing to Sonnet.** At $1/$5 per MTok it is a third
  the price, and this task is closer to dense extraction than open-ended reasoning.
  Run it against these five episodes and compare against the JSON here before
  spending on a full Sonnet pass. Note Haiku 4.5's 200K context, which is ample for
  a 25K-token episode.

Two limits to check before launching. The largest episode in the corpus should be
checked against the output token limit — a 280-mention episode already produces
~13k output tokens and the densest hosts-only episodes will run higher, so set
`max_tokens` generously and stream rather than letting a long episode truncate
mid-JSON. And Batches allows up to 100,000 requests or 256 MB per batch; 719
transcripts at ~90KB each is about 65 MB, so the whole corpus fits in one batch.
