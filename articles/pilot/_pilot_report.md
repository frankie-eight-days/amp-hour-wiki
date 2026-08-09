# Pilot article report — 5 concepts

Generated 2026-08-08 · model claude-opus-5 · pipeline steps 6-8 in miniature

Written in the encyclopedic register (Frank, 2026-08-08): Wikipedia-style lead, claims stated as knowledge with bracketed `[NNN]` episode citations, named attribution only where the who is the content, zero meta commentary, direct quotes rare.

Scripts in `/private/tmp/claude-501/-Users-frankwalsh-Documents-vibecoding-amp-hour-wiki/2439d3fc-e7b7-42c1-90da-27b1ddd5fa6c/scratchpad/`: `pilot_gather.py`, `mkpacket.py` + `packet_*.py`, `pilot_lint.py`, `epmeta.py`.
Working passage dumps: `scratchpad/pilot_pass/<concept>.txt` — every pinned passage with ±1 paragraph of context.

## Per-article summary

| Concept | Eps | Census mentions | Pins after dedupe | Capped | Examined → retained | Packet claims | Prose words |
|---|---|---|---|---|---|---|---|
| oscilloscope | 314 | 822 | 343 | yes → 150 | 150 → 105 | 54 | 1,396 |
| altium | 226 | 606 | 200 | yes → 150 | 150 → 103 | 59 | 1,429 |
| pick-and-place-machine | 146 | 426 | 245 | yes → 150 | 150 → 104 | 62 | 1,529 |
| soldering-iron | 109 | 147 | 42 | no | 42 → 26 | 39 | 1,047 |
| circuitpython | 24 | 48 | 29 | no | 29 → 23 | 31 | 1,035 |

Paragraph-level dedupe (collapsing multiple mentions landing in the same transcript paragraph) removes 40-60% of the raw explains+opinion count on dense topics, and is what made reading tractable.

### Re-graded depth vs census depth

| Concept | Census explains / opinion | Re-graded | Change |
|---|---|---|---|
| oscilloscope | 158 / 191 | 74 / 31 | explains −53%, opinion −84% |
| altium | 52 / 150 | 41 / 62 | explains −21%, opinion −59% |
| pick-and-place-machine | 125 / 123 | 68 / 36 | explains −46%, opinion −71% |
| soldering-iron | 17 / 25 | 12 / 14 | explains −29%, opinion −44% |
| circuitpython | 20 / 9 | 16 / 7 | explains −20%, opinion −22% |

Census grades are inflated, and the inflation scales with how common the word is. `oscilloscope` is the most frequent technical noun in the corpus and is graded "explains" whenever it appears as scenery — a film prop, a swap-meet purchase, a career origin story. `circuitpython` is rare and always discussed deliberately, so its grades were nearly correct. **Census depth is a usable signal for rare concepts and close to noise for common ones.**

The opinion grade is worse than the explains grade everywhere. Many "opinion" pins are questions, agreement noises, or mild enthusiasm — not positions anyone holds.

## Evidence packets

`articles/pilot/_packets/<concept>.json`, written **before** each article's prose so a writer model can work from the packet alone.

| Packet | Claims | rule-of-thumb / opinion / war-story / moment | Disagreement groups | capped |
|---|---|---|---|---|
| `circuitpython.json` | 31 | 16 / 9 / 3 / 3 | 2 | false |
| `soldering-iron.json` | 39 | 19 / 16 / 2 / 2 | 3 | false |
| `oscilloscope.json` | 54 | 22 / 17 / 7 / 8 | 5 | true |
| `pick-and-place-machine.json` | 62 | 26 / 17 / 12 / 7 | 2 | true |
| `altium.json` | 59 | 14 / 24 / 5 / 16 | 4 | true |

Each claim carries `claim_text`, `quote_verbatim`, `speaker`, `episode`, `episode_title`, `episode_url`, `depth_regraded`, `kind`, and an optional `disagreement_group` linking it to a `disagreements` entry (`id`, `question`, `positions[]`). Episode titles and URLs are resolved from the census at build time, so they cannot drift from the corpus.

`mkpacket.py` refuses to write a packet if any quote fails verbatim verification against its cited episode. **245 claims across five packets, all quotes verified.**

## Lint results

Two checks now run:

1. **Verbatim quotes** — every double-quoted phrase must be a substring of the cited episode's transcript (case- and whitespace-normalised, smart quotes folded, ellipsis-joined fragments checked per fragment). Citation parsing accepts both `[NNN]` and the older `(Speaker, #NNN)`.
2. **Claim support** — every episode cited in an article's prose must be backed by a verified claim in that concept's packet. This is the automatable half of "a claim must be supported by its cited episode".

| Concept | Quotes | Cited episodes | Unbacked citations |
|---|---|---|---|
| circuitpython | 2 / 2 pass | 14 | none |
| soldering-iron | 2 / 2 pass | 21 | none |
| oscilloscope | 1 / 1 pass | 37 | none |
| pick-and-place-machine | 1 / 1 pass | 41 | none |
| altium | 1 / 1 pass | 38 | none |
| **Total** | **7 / 7 pass** | **151** | **none** |

The claim-support check earned its place immediately: on its first run it caught a citation in `circuitpython.md` ([578], ESP32-S2 support) with no packet claim behind it. The fix was to extract and verify the missing claim, not to drop the citation.

A third check runs as a grep tripwire: a banned-pattern scan for meta commentary (`the corpus`, `the archive`, `the show`, `this page`, `the reader`, and similar). Currently zero hits across all five articles. Worth wiring into the lint proper for the full run.

Quote counts fell from 378 to 7 with the register change. The evidence packets are now where quotes live.

## Further reading (pipeline-owned)

Harvested by `further_reading.py` from the show notes of every episode an article cites. Each episode page is fetched once and cached to `scratchpad/shownotes/<ep>.html` (141 pages cached, shared across concepts). Extraction is confined to the page's single `<div class=show-notes>` block; the site emits unquoted HTML attributes, so the anchor regex accepts quoted and unquoted `href`.

Dropped mechanically: the show's own domain, podcast platforms and feeds, social, Patreon/PayPal, anything carrying `utm_`/`tag=`, `/subscribe`, `/sponsor`, `/donate`, and Amazon `amzn.to` affiliate shortlinks. URLs are canonicalised (scheme, `www.`, trailing slash) before dedupe — an early version missed a duplicate because it normalised host but not scheme.

Relevance was applied by hand against the rule: on an interview episode about the concept keep generously, on a grab-bag episode keep only concept-relevant links.

| Concept | Cited episodes | Raw candidates | Kept | Keep rate |
|---|---|---|---|---|
| circuitpython | 14 | 207 | 22 | 11% |
| soldering-iron | 21 | 282 | 5 | 2% |
| oscilloscope | 37 | 465 | 17 | 4% |
| pick-and-place-machine | 41 | 513 | 16 | 3% |
| altium | 38 | 481 | 18 | 4% |

Persisted to `_packets/<concept>.further_reading.json` as `[{title, url, episode}]` and appended to each article as `## Further reading` before `## References`, formatted `- [Title](url) — via #NNN`.

Two notes for the full run. **The keep rate is low by nature** — a grab-bag episode's show notes cover everything discussed that week, so most links are unrelated to any one concept. `soldering-iron` keeping 5 of 282 is not a filter failure; the hosts simply never linked iron material, which is consistent with it being a thin concept. **Link titles are raw show-note text** and frequently contain quotation marks and parentheses, so the writer percent-encodes parens (bare parens break markdown link parsing) and the lint now excludes the Further reading section from quote verification — those titles are harvested data, not authored claims.

## Wall notes: what was hard

### 1. Speaker labels are wrong far more often than the pipeline assumes

Still the finding that should gate the full run. `canon/speaker_map.json` repairs label *spelling* ("Adam Wolfe" → "Adam Wolf") but not label *assignment*. Three defect classes:

**(a) Host/guest swap — 144 of 719 episodes (20%).** The show-open boilerplate ("This is The Amp Hour Podcast, recorded <date>. Episode NNN…") is always read by a host, but in these files it carries the guest's label. Ep 383's turn labelled `**Scott Shawcroft:**` reads the intro; the turn labelled `**Chris Gammell:**` gives Scott's bio. Every CircuitPython design-authority claim there is currently credited to the wrong person. File list: `scratchpad/suspect_swap.json`.

**(b) Host-to-host swap — invisible to that detector.** Ep 555 is a Dave+Chris episode, so the boilerplate probe passes, but the labels swap mid-exchange: the pro-Altium argument is labelled Chris Gammell and the reply labelled Dave Jones says *"Dave's working from old knowledge"*. Caught only by reading. No cheap detector exists for this class.

**(c) A host's name applied to someone not on the episode.** Ep 697 has exactly two labels, "Chris Gammell" and "Dave Jones" — but Dave is not on it; the guest is Tim from Mitxela. Eps 472 and 523 label their guest's turns "Chris Gammell", but the speaker describes working at Valve on the Steam Controller and selling a Geiger counter kit: Jeff Keyzer. Ep 59 labels "Chris Gammell" saying he was laid off when Altium moved to China: Dave Jones.

Two further hazards: some files carry **one label for every turn** (ep 651: 190 turns all "Jeff Geerling"; ep 699: 129 turns all "Andrew Seddo"), and turns are frequently **fused**, so one paragraph holds both speakers and the label is right only for its opening sentence. One packet claim (`soldering-iron`, ep 288) is deliberately marked `unattributed (transcript fuses both hosts)` rather than guessed.

All of this was handled by attributing from content and documenting each reassignment in the article's production-notes comment. That works at five articles; it will not scale to 400.

**A cheap check I validated but did not build out:** 39 episodes contain a speaker self-identifying at the start of a turn ("I'm Dave Jones from the EEV blog"). All 39 agreed with their label — 0 mismatches. That probe, plus affiliation matching ("when I was at X" against the guest's known employer), would give per-file label confidence before a writer sees a passage.

### 2. Two file-index bugs that fail silently

- **Transcript filenames are inconsistent.** Only 550 of 719 use the `NNNN-` prefix; the rest are `the-amp-hour-550-…`, `show-345-…`, or bare slugs. The first lint globbed by number prefix and silently scored every unmatched episode as FAIL. Resolve episode → file through the census, never by filename pattern.
- **The census `file` field is stale for 19 episodes** — it names a transcript that does not exist. The census JSON's own filename stem is correct. Worth fixing at source.
- **Four episodes have no episode number** (`chips-and-fabs-and-garages`, `ham-spam-thank-you-maam`, `quassating-quadcopter-quantophrenia`, `the-chinese-clairvoyancy`) and so cannot be cited under a `[NNN]` scheme. Two good passages were dropped: a SparkFun soldering-iron-kit chicken-and-egg joke, and Altium's 2011 Shanghai move told first-hand.

### 3. ASR spellings

The transcripts misspell exactly the proper nouns these articles are about: Hakko as "Heiko"/"HAKO"/"HACO", baud as "board", Limor Fried as "Lamore", LeCroy as "LaCroix", Jeff Keyzer as "Jeff Kaiser", Elecia White as "Alicia White", KiCad as "KeyCAD"/"Kaikad"/"KECAD", Altium as "Autium". Under the previous quote-heavy register this forced bracketed glosses in the prose. **The encyclopedic register largely dissolves this problem** — claims are paraphrased, so corrected spellings appear in the article while raw forms stay in the packet's `quote_verbatim`. This is an unplanned benefit of the voice change and a reason to prefer it at scale. A known-ASR-error map is still worth building for the packets.

### 4. Length: resolved by the register

Under the quote-heavy register the three large concepts ran 2,900-3,500 words against a 800-2000 target, and could not be cut further without discarding verified claims. In the encyclopedic register all five land inside the target (1,035-1,529 words) while carrying **more** claims, because a claim now costs a clause rather than a block quote plus attribution scaffolding. A flat word budget is workable after all; density per word roughly doubled.

### 5. Things the census missed

Re-grading is not only subtractive. Reading ep 383 with full context surfaced paragraph 87 — the `code.py` naming rationale and the deliberate decision to run slower than MicroPython — which the census had not pinned at all, and which is the strongest claim in that article. **A gather that only surfaces pinned paragraphs will miss the best material in an interview episode.** For interview-heavy concepts, pulling the contiguous run around a cluster of pins beats ±1 paragraph around each.

## What I'd change before the 400-article run

1. **Fix speaker assignment first (step 2.6).** Extend `speaker_map.json` from spelling repair to assignment repair: the boilerplate probe for the 144 host/guest swaps, self-ID phrases for confidence scoring, and flags on single-label and placeholder-label files. Without it, roughly one citation in five is a coin flip in exactly the sections where attribution matters.
2. **Fix the two index bugs** (transcript filename resolution via census; stale `file` field). Both fail silently.
3. **Keep packet-before-prose.** Writing the packet first forced every claim to be stated and verified before any sentence was composed, and it is what makes the claim-support lint possible at all.
4. **Keep both lint checks, and promote the meta-commentary grep into the lint.**
5. **Down-weight census depth grades for high-frequency concepts** — normalise the explains rate against raw mention count; a concept whose explains rate approaches its mention rate is being graded on keyword proximity.
6. **Give the gather contiguous runs, not ±1 paragraph,** where pins cluster.
7. **Add an unnumbered-episode citation fallback.**
8. **Build the ASR correction map** for packet quotes.
