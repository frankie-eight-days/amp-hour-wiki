# Concept Census Extraction Prompt (v2)

This is the exact prompt a production pipeline sends once per episode, with the
full transcript appended after the `--- TRANSCRIPT ---` marker.

Changes from v1, all driven by the five-episode spot check
(`census_spotcheck/REVIEW.md`): the `substantive` boolean is replaced by a
three-way `depth` field, `char_start` is added as a verifiable locator,
`career-business` is split into four types, `material` is folded into
`manufacturing`, ASR corruption is handled explicitly, the mention-emission rule
is stated mechanically, and each episode now carries a small header block.

---

You are building a concept census for a wiki derived from *The Amp Hour*, a
long-running electronics-engineering podcast. Your job on this episode is
**exhaustive inventory, not curation**. Downstream stages handle merging,
ranking and article writing. You only find and label.

## Input format

The transcript is markdown with YAML frontmatter (`episode`, `title`, `url`;
some legacy episodes are missing `episode`) followed by blank-line-separated,
speaker-labelled paragraphs:

```
**Chris Gammell:** ...text...

**Dave Jones:** ...text...
```

The **body** is everything after the closing `---` of the frontmatter, with the
single newline that follows it stripped. Character offsets are measured into the
body, not into the whole file.

Paragraphs are indexed from 0, counting every non-empty paragraph in the body, in
order. `**Speaker ?:**` is a real speaker label used when diarisation failed —
treat it as the literal speaker string `Speaker ?`.

Speaker labels are unreliable in three known ways and you must not "fix" them:
a paragraph often contains both sides of an exchange merged under one label; some
episodes mislabel a guest with a product name (episode 650 labels Andreas
Olofsson as `Parallela` on nearly every turn); and a stray label sometimes lands
on the wrong paragraph. Always record the label exactly as it appears on the
paragraph, and use the `notes` field to flag an episode whose labels are visibly
broken.

## Output format

Return **only** a JSON object, no prose, no markdown fence:

```json
{
  "episode": 212,
  "title": "An Interview with Trey German - Launchpad Laden Lodesman",
  "url": "https://theamphour.com/212-...",
  "file": "0212-an-interview-with-trey-german-....md",
  "main_topics": ["c2000", "field-oriented-control", "msp430-launchpad"],
  "guest_name": "Trey German",
  "guest_affiliation": "Texas Instruments",
  "notes": null,
  "mentions": [ ... ]
}
```

### Header fields

**`episode`** — from frontmatter. If frontmatter has no `episode` field, set
`null`; do not infer it from the filename or the cold open.

**`main_topics`** — 2 to 3 canonical concept names identifying what the episode
is *about*, as opposed to what it merely mentions. Each must also appear as a
`concept` in `mentions`. For an interview this is usually the guest's subject
matter; for a hosts-only episode it is the two or three threads that occupy the
most airtime. Rank by airtime and depth, not by mention count — a concept named
forty times in passing is not a main topic.

**`guest_name`** / **`guest_affiliation`** — the interviewee and the company or
institution they are introduced as representing. Both `null` on hosts-only
episodes. If a guest gives no affiliation, set `guest_affiliation` to `null`
rather than guessing. Use the person's real name even when the speaker label is
corrupted (episode 650's guest is `Andreas Olofsson`, not `Parallela`).

**`notes`** — `null` normally. A one-sentence string when something about the
file itself would mislead a downstream consumer: broken speaker labels, missing
frontmatter, an unusually coarse paragraph structure, a truncated transcript.

### Mention objects

```json
{
  "concept": "solder-paste-stencil",
  "type": "tool-equipment",
  "speaker": "Chris Gammell",
  "paragraph_index": 363,
  "char_start": 208871,
  "depth": "explains",
  "context_snippet": "tutorial on KiCad and how to actually create your own laser cut stencils"
}
```

`asr_suspect` is a fourth optional field, present only when `true` (see below).

## Field rules

### `concept`

A canonical-ish name for the thing being discussed.

- lowercase, hyphen-separated, ASCII only: `plated-through-hole`, `esp32-s2`,
  `field-oriented-control`.
- Must be a **self-contained noun phrase**. Never a pronoun, never a bare
  demonstrative, never a verb phrase.
- Singular, not plural: `stepper-motor`, not `stepper-motors`.
- Prefer the standard industry name over the speaker's slang. `scope` and
  `oscilloscope` both become `oscilloscope`.
- Do **not** merge distinct specificity levels. `msp430` and `msp430-launchpad`
  are separate concepts; `usb` and `usb-stack` are separate; `pcb-fabrication`
  and `pcb-milling` are separate.
- Companies keep their own name even when only a product is discussed, and vice
  versa: `digi-key`, `analog-discovery`, `texas-instruments`, `c2000`.

### `asr_suspect` and ASR corruption

These transcripts come from automatic speech recognition, which reliably mangles
proper nouns it does not know. This is the single largest source of bad canonical
names, so handle it explicitly:

- **If you can confidently recover the intended name from context**, canonicalise
  to the real name and let the `context_snippet` carry the verbatim garbled
  string as evidence. Do not set `asr_suspect`. Examples seen in this corpus:
  "Kycat" → `kicad`, "bomb consolidation" → `bom-consolidation`, "I penalized my
  board" → `panelization`, "Laura" → `lora`, "Sam's the roof" → `sam-zeloof`,
  "Vigilant" → `digilent`, "Adeptiva" → `adapteva`, "2.4 megahertz band" →
  `2-4-ghz-band`.
- **If the string is clearly a mangled proper noun but you cannot recover it with
  confidence**, keep the verbatim string as the concept (lowercased and
  hyphenated) and set `"asr_suspect": true`. A downstream pass will cluster these.
- **Never guess a plausible-sounding name you cannot support from context.** A
  wrong canonical name is worse than a flagged unknown one, because it merges
  silently into the wrong wiki article.

"Confidently recover" means the surrounding sentences pin the referent. "a 30s
PCI express 30s" is recoverable as `serdes` because the passage is explicitly
about PHY design effort; the bare token "30s" elsewhere would not be.

### `type`

Exactly one of the following sixteen.

| type | covers |
|---|---|
| `component` | physical parts and silicon: resistor, ESP32-S2, WIZnet module, op-amp, CMOS image sensor |
| `technique` | something an engineer *does to a design*: ground-pour, bit-banging, digital beamforming, hand soldering, current sensing |
| `tool-equipment` | instruments, machines, fixtures: oscilloscope, LPKF mill, reflow oven, EUV scanner, Analog Discovery |
| `software` | tools, languages, stacks, OSes, services: KiCad, Verilog, Zephyr, FreeRTOS, LWIP, Verilator, CDN |
| `company-product` | companies, distributors, institutions, agencies, and their named commercial offerings: Digi-Key, TI, DARPA, Rose-Hulman, Hubble, Kickstarter |
| `standard-protocol` | CAN, USB, I²C, PMBus, Gerber, DIN 3105, Bluetooth, AMBA/AXI, 10GbE |
| `manufacturing` | fab, assembly, packaging, supply chain, logistics, **and materials**: solder mask, panelisation, tape-out, wafer fab, lead time, Dibond, mylar, silicon interposer |
| `career` | the individual working life: jobs, hiring, interviews, titles, education, resumes, burnout, how people learn |
| `business-model` | how a company makes money: pricing, margins, licensing, monetisation, make-vs-buy, feature gating, product strategy |
| `industry-economics` | market-level forces: supply and demand, trade policy, the funding landscape, commoditisation, market sizing, capital barriers to entry |
| `engineering-practice` | how engineering *organisations* work: design-by-committee, the benevolent-dictator model, systems engineering process, code review culture, schedule slip, the limits of self-review |
| `community-event` | conferences, forums, meetups, movements: Maker Faire, DEF CON, Latch Up, TI E2E, open-source hardware |
| `media-resource` | books, app notes, videos, blogs, courses, datasheets, papers |
| `person` | named individuals discussed as subjects (authors, engineers, founders) — not the hosts introducing themselves |
| `concept-principle` | physical laws, phenomena, theory, rules of thumb: Ohm's law, fan-out, Miller plateau, Moore's law, path loss, angle of arrival, price elasticity |
| `other` | genuinely does not fit; use sparingly |

Pick the type by *what the passage is about*, not by the word's dictionary
category. "They ran out of 1.02K resistors at 2am" is `manufacturing` (a sourcing
story), not `component`.

Three boundaries that generate most of the coin-flips:

- **`technique` vs `engineering-practice`** — `technique` is what one engineer
  does to a circuit or a board; `engineering-practice` is how a team organises
  the work. Partitioning a schematic across pages is `technique`; deciding that
  one architect owns every decision is `engineering-practice`.
- **`business-model` vs `industry-economics`** — `business-model` is one
  company's choice; `industry-economics` is the environment every company faces.
  Charging a premium for ROM-resident IP is `business-model`; mask sets costing
  $20M is `industry-economics`.
- **`career` vs `engineering-practice`** — `career` follows a person;
  `engineering-practice` follows a process. "I spend 20 hours a week on the
  forums" is `career`; "you can't check your own stuff" is
  `engineering-practice`.

### `speaker`

The paragraph's label verbatim, without the asterisks or colon.

### `paragraph_index`

0-based index of the paragraph the mention occurs in.

### `char_start`

The 0-based character offset of `context_snippet` within the **body** (as defined
under Input format). It must satisfy exactly:

```
body[char_start : char_start + len(context_snippet)] == context_snippet
```

Paragraph indices are a coarse locator on modern episodes — some carry 900-word
speaker turns with a dozen distinct mentions — so `char_start` is what actually
anchors a mention to its evidence. It also serves as an integrity check: if the
snippet is not found at the stated offset, the mention is rejected automatically.

### `depth`

How much the passage actually teaches about the concept. Three values, in
descending order:

- **`explains`** — a reader who did not know the concept would learn something
  usable: a mechanism, a procedure, a trade-off *with its reason*, or a number
  with the context that makes it actionable.
- **`opinion`** — a judgement, preference, war story, or assertion about the
  concept, without the mechanism or reasoning that would let a reader apply it.
- **`mention`** — the concept is named and nothing more: a passing reference, a
  segue, a joke, an aside.

Worked calibration, taken from real extractions:

| passage | concept | depth | why |
|---|---|---|---|
| "chips have a certain drive capability. They can drive a certain amount of current whilst keeping a, the minimum low and high threshold levels required" | `fan-out` | `explains` | states the mechanism |
| "normally, you think of a byte as 8-bits. Well, actually, on our architecture, a byte is 16-bits" plus the struct-alignment consequence | `16-bit-byte-addressing` | `explains` | mechanism plus its downstream effect |
| "the magic figure is like $300. Once a product gets below the $300 threshold, it becomes an impulse buy" | `impulse-buy-price-threshold` | `explains` | a number with the context that makes it actionable |
| "I waited over a month for those, like five weeks... I'd already figured, oh no, I want to change things" | `pcb-lead-time` | `opinion` | a war story with a number, but no transferable rule |
| "Somebody has to run it and make all the decisions and be the dictator on the project" | `benevolent-dictator-model` | `opinion` | a strong position, no reasoning offered |
| "they've got much better quality sensors in them" | `image-sensor-quality` | `opinion` | bare assertion; borderline, and `opinion` is the right call |
| "that's what Freak Labs posted on Twitter the other day" | `freaklabs` | `mention` | named only |
| "you had your Google Glass on" | `google-glass` | `mention` | aside |

**Calibration anchor — this matters, do not skip it.** On a typical episode
expect roughly **a quarter to a third of mentions to be `explains`**, a little
under half `opinion`, and the balance `mention`. A v1 run of this prompt marked
95% of mentions as knowledge-bearing, which made the field useless as a
discriminator. If your `explains` share is drifting far above a third, you are
counting assertions as explanations — re-read the definition and tighten. If it
is far below a quarter on a technical interview, you are being too strict.

The share varies by episode: a deep single-subject interview runs at the high end
of the `explains` band, and a link-roundup episode runs at the low end. Do not
force the ratio on any individual episode — use it to check yourself.

### `context_snippet`

A verbatim substring of the paragraph, at most 100 characters, showing why you
tagged the mention. Trim to the informative part. Do not paraphrase, do not
insert `...` elisions, do not add the speaker label.

> Pipeline note: both constraints are enforced downstream — a mention is rejected
> if `context_snippet` is longer than 100 characters or is not found verbatim at
> `char_start`. The rules are stated here so you produce valid output, not
> because the validator is optional.

## Coverage rules

### 1. Extract every mention, not the interesting ones

A passing reference to Digi-Key is a mention. Expect 150–300 mentions for a
typical hour-long episode; hosts-only episodes run denser than interviews because
they cover more unrelated topics.

### 2. The mention-emission rule is mechanical

Emit exactly one mention for a concept in a paragraph **if and only if** that
paragraph either:

- **names** the concept (in any surface form, including an ASR-mangled one), or
- refers to it by a pronoun or demonstrative whose referent is **unambiguously**
  the concept and is resolvable from that paragraph or the one immediately before
  it.

Otherwise emit nothing for that concept in that paragraph — even when the
paragraph is plainly part of the same conversational thread. Do not "carry
forward" a concept across a run of paragraphs because the topic has not changed,
and do not collapse a run into a single mention. Both distortions corrupt the
frequency ranking that decides which concepts get wiki articles.

Two consequences worth internalising: one dense paragraph can legitimately yield
fifteen mentions, and a paragraph that is only "Yeah." or "Right." yields none no
matter what it is agreeing with.

### 3. Skip sponsor-read segments entirely

A contiguous block of ad copy in marketing register, usually announced ("this
episode is brought to you by…", "our sponsor…") and closing with a discount code
or URL. Skip everything inside it, including the advertised product.

The hosts also promote their **own** businesses — EEVblog kits, Contextual
Electronics, listener donations, the show's hosting and app. That is **not** a
sponsor read. Extract it normally, usually as `business-model` and usually
`depth: "mention"`.

### 4. Do extract from small talk when it carries engineering content

Barbecue, gym classes and bad sci-fi films yield nothing. But a digression about
Chinese New Year factory shutdowns, university funding, PhD-student precarity, or
textbook pricing is real domain knowledge for this audience — extract it. This
rule is load-bearing: a naive small-talk filter would strip some of the corpus's
best `industry-economics` and `career` material.

### 5. Ignore the show's own furniture

The cold open, "welcome to the Amp Hour", episode numbering, "we'll link it in
the show notes", sign-offs. These produce no mentions.

### 6. Skip the unrecoverable

If a concept appears only inside a garbled ASR run you cannot resolve *and* the
mangled string is not even clearly a proper noun, skip it rather than emit
nonsense. Use `asr_suspect` for the recoverable-but-uncertain middle ground.

## Few-shot examples

Character offsets below are illustrative; compute real ones against the body.

---

**Example 1 — one dense paragraph, mixed depth.**

Input paragraph 21 (episode 500):

> **Dave Jones:** Lowering the cost of assembly and lowering the cost, lowering
> the risk as well of sourcing parts and stuff like that. Because, you know,
> like you can just risk goofing it up if you can't get these. You're purchasing
> departments going around like crazy, trying to purchase 60 different reels of
> resistors. And, you know, oh, they ran out. You know, so you get a phone call
> at 2 a.m. in the morning from your assembly house because they're urgent, you
> know, in China.

Output:

```json
[
  {"concept": "bom-consolidation", "type": "technique", "speaker": "Dave Jones", "paragraph_index": 21, "char_start": 12044, "depth": "explains", "context_snippet": "Lowering the cost of assembly and lowering the cost, lowering the risk as well of sourcing parts"},
  {"concept": "component-sourcing", "type": "manufacturing", "speaker": "Dave Jones", "paragraph_index": 21, "char_start": 12232, "depth": "explains", "context_snippet": "purchasing departments going around like crazy, trying to purchase 60 different reels of resistors"},
  {"concept": "contract-assembly-house", "type": "manufacturing", "speaker": "Dave Jones", "paragraph_index": 21, "char_start": 12362, "depth": "opinion", "context_snippet": "you get a phone call at 2 a.m. in the morning from your assembly house because they're urgent"}
]
```

Three mentions from one paragraph. `resistor` is **not** emitted separately — the
passage is about sourcing reels, not about resistors. The first two `explains`
because they give the reason a consolidated BOM lowers cost and risk; the third
is `opinion` because the 2am phone call is a war story, not a rule.

---

**Example 2 — the mechanical rule, including a paragraph that yields nothing.**

Input paragraphs 21–23 (episode 79):

> **Chris Gammell:** What about the limits? Is it 6-6? Six-line, six-space?
>
> **Dave Jones:** Yeah, it might be 6-6 or 5-5 or something like that.
> 0.3-millimeter hole, something like that. You know, fairly generic type stuff.
>
> **Chris Gammell:** Okay.

Output:

```json
[
  {"concept": "trace-width-and-spacing", "type": "manufacturing", "speaker": "Chris Gammell", "paragraph_index": 21, "char_start": 9903, "depth": "opinion", "context_snippet": "What about the limits? Is it 6-6? Six-line, six-space?"},
  {"concept": "trace-width-and-spacing", "type": "manufacturing", "speaker": "Dave Jones", "paragraph_index": 22, "char_start": 9975, "depth": "explains", "context_snippet": "it might be 6-6 or 5-5 or something like that"},
  {"concept": "drill-hole-size", "type": "manufacturing", "speaker": "Dave Jones", "paragraph_index": 22, "char_start": 10022, "depth": "explains", "context_snippet": "0.3-millimeter hole, something like that. You know, fairly generic type stuff"}
]
```

Two things to take from this. `trace-width-and-spacing` is emitted **twice**,
once per paragraph that names it — the run is not collapsed into a single
mention. And paragraph 23 emits **nothing**: "Okay." is unmistakably part of the
same exchange about PCB specs, but it neither names a concept nor contains a
resolvable pronoun, so the thread is not carried forward.

---

**Example 3 — ASR corruption, both branches.**

Input paragraph 74 (episode 650):

> **Parallela:** if you say build versus buy, if I were to, uh, go out and
> design a 30s PCI express 30s, I would have to probably hire 10 people and, uh,
> you know, spend two years doing it. So if you look at us salaries, you know,
> say $200,000 per engineer times 10 times two, you're you're, you know, it takes
> you two years, you lost, lost time, and then you don't come out ahead in terms
> of cost.

Output:

```json
[
  {"concept": "build-vs-buy", "type": "business-model", "speaker": "Parallela", "paragraph_index": 74, "char_start": 41207, "depth": "explains", "context_snippet": "say $200,000 per engineer times 10 times two, you're you're, you know, it takes you two years"},
  {"concept": "serdes", "type": "component", "speaker": "Parallela", "paragraph_index": 74, "char_start": 41093, "depth": "explains", "context_snippet": "go out and design a 30s PCI express 30s, I would have to probably hire 10 people"},
  {"concept": "pci-express", "type": "standard-protocol", "speaker": "Parallela", "paragraph_index": 74, "char_start": 41093, "depth": "opinion", "context_snippet": "go out and design a 30s PCI express 30s, I would have to probably hire 10 people"}
]
```

"30s" is ASR corruption of "SerDes", recoverable because the passage is
explicitly about the effort to design a PCI Express PHY — so it canonicalises to
`serdes` with **no** `asr_suspect` flag, and the snippet preserves the verbatim
garble as evidence. The speaker label `Parallela` is recorded verbatim even
though it is a product name, and the episode's `notes` field flags that.

Contrast a case where recovery is not confident:

```json
{"concept": "hans-kammensund", "type": "person", "speaker": "Chris Gammell", "paragraph_index": 216, "char_start": 121455, "depth": "mention", "asr_suspect": true, "context_snippet": "Hans Kammensund, the 555 guy, he actually did one"}
```

Here "the 555 guy" strongly suggests Hans Camenzind, but the surname is mangled
past confident reconstruction, so the verbatim string is kept and flagged.

---

**Example 4 — a paragraph that yields nothing at all.**

Input paragraph 205 (episode 500):

> **Chris Gammell:** Here's where Dave gets his PhD. This is where Dave goes back
> and he gets his PhD in this thing. Whatever it is. And he just, he just goes to
> conferences and argues with people for the rest of his frigging life. Dr.
> Jones. Yeah.

Output:

```json
[]
```

A running joke about the co-host. `phd` is not a concept mention here — the
passage is not about doctoral study, it is about Dave.

---

**Example 5 — the small-talk rule earning its place.**

Input paragraph 79 (episode 500):

> **Dave Jones:** Almost half of Australian PhD students considering disengaging
> from studies due to the pandemic. Wow. This is like, yeah. They, they reckon 5%
> of PhD students in Australia are currently or about to experience homelessness
> and 11% are skipping meals.

Output:

```json
[
  {"concept": "phd-student-precarity", "type": "career", "speaker": "Dave Jones", "paragraph_index": 79, "char_start": 44120, "depth": "explains", "context_snippet": "5% of PhD students in Australia are currently or about to experience homelessness"}
]
```

Off-topic by a naive filter, but this is exactly the industry-and-career material
the wiki should carry, and the numbers make it `explains`.

---

--- TRANSCRIPT ---
