# Concept Census Extraction Prompt (v1)

This is the exact prompt a production pipeline sends once per episode, with the
full transcript appended after the `--- TRANSCRIPT ---` marker.

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

Paragraphs are indexed from 0, counting every non-empty paragraph after the
frontmatter, in order. `**Speaker ?:**` is a real speaker label used when
diarisation failed — treat it as the literal speaker string `Speaker ?`.

Speaker labels are unreliable in two known ways and you must not "fix" them:
a paragraph often contains both sides of an exchange merged under one label,
and a few episodes mislabel a guest (e.g. using a product name where a person's
name belongs). Always record the label exactly as it appears on the paragraph.

## Output format

Return **only** a JSON object, no prose, no markdown fence:

```json
{
  "episode": 212,
  "title": "An Interview with Trey German - Launchpad Laden Lodesman",
  "url": "https://theamphour.com/212-...",
  "file": "0212-an-interview-with-trey-german-....md",
  "mentions": [ ... ]
}
```

If frontmatter has no `episode` field, set `"episode": null`.

Each element of `mentions` is:

```json
{
  "concept": "solder-paste-stencil",
  "type": "tool-equipment",
  "speaker": "Chris Gammell",
  "paragraph_index": 363,
  "substantive": true,
  "context_snippet": "tutorial on KiCad and how to actually create your own laser cut stencils"
}
```

### Field rules

**`concept`** — a canonical-ish name for the thing being discussed.
- lowercase, hyphen-separated, ASCII only: `plated-through-hole`, `esp32-s2`,
  `field-oriented-control`.
- Must be a **self-contained noun phrase**. Never a pronoun, never a bare
  demonstrative, never a verb phrase. If the transcript says "these things
  work", "that chip", "one of those", resolve it from context to the actual
  noun (`pcb-mill`, `wiznet-module`) or drop the mention if it cannot be
  resolved with confidence.
- Prefer the standard industry name over the speaker's slang, but do not invent
  a name the passage does not support. `scope` and `oscilloscope` both become
  `oscilloscope`; `bomb consolidation` (a transcription error for "BOM") becomes
  `bom-consolidation`; `Kycat` / `key cat` becomes `kicad`. If you are guessing
  at what an ASR-garbled name is, keep your best reading and let the snippet
  carry the evidence.
- Do **not** merge distinct specificity levels. `msp430` and
  `msp430-launchpad` are separate concepts; `usb` and `usb-stack` are separate;
  `pcb-fabrication` and `pcb-milling` are separate.
- Singular, not plural: `stepper-motor`, not `stepper-motors`.
- Companies keep their own name even when only a product is discussed, and vice
  versa: `digi-key`, `analog-discovery`, `texas-instruments`, `c2000`.

**`type`** — exactly one of:

| type | covers |
|---|---|
| `component` | physical parts and silicon: resistor, ESP32-S2, WIZnet module, op-amp, CMOS image sensor |
| `technique` | something an engineer *does*: ground-pour, bit-banging, BOM consolidation, digital beamforming, hand soldering |
| `tool-equipment` | instruments, machines, fixtures: oscilloscope, LPKF mill, reflow oven, EUV scanner, Analog Discovery |
| `software` | tools, languages, stacks, OSes, services: KiCad, Verilog, Zephyr, FreeRTOS, LWIP, Verilator, CDN |
| `company-product` | companies, distributors, institutions, agencies, and their named commercial offerings: Digi-Key, TI, DARPA, Rose-Hulman, Hubble, Kickstarter |
| `standard-protocol` | CAN, USB, I²C, PMBus, Gerber, DIN 3105, Bluetooth, AMBA/AXI, 10GbE |
| `career-business` | jobs, hiring, business models, funding, pricing, market structure, engineering-org dynamics |
| `manufacturing` | fab, assembly, packaging, supply chain, logistics: solder mask, panelisation, tape-out, wafer fab, lead time |
| `community-event` | conferences, forums, meetups, movements: Maker Faire, DEF CON, Latch Up, TI E2E, open-source hardware |
| `media-resource` | books, app notes, videos, blogs, courses, datasheets, papers |
| `person` | named individuals discussed as subjects (authors, engineers, founders) — not the hosts introducing themselves |
| `concept-principle` | physical laws, phenomena, theory, rules of thumb: Ohm's law, fan-out, Miller plateau, Moore's law, path loss, angle of arrival |
| `material` | substances and substrates: Dibond, mylar, solder paste, silicon interposer, etchant |
| `other` | genuinely does not fit; use sparingly |

Pick the type by *what the passage is about*, not by the word's dictionary
category. "They ran out of 1.02K resistors at 2am" is `manufacturing`
(a sourcing story), not `component`.

**`speaker`** — the paragraph's label verbatim, without the asterisks or colon.

**`paragraph_index`** — 0-based index of the paragraph the mention occurs in.
If a concept is discussed across five consecutive paragraphs, emit one mention
per paragraph in which it is actually named or clearly carried forward. Do not
emit one mention for the whole run, and do not emit a mention for a paragraph
that is only "Yeah." / "Right."

**`substantive`** — `true` when the passage carries transferable knowledge about
the concept: an opinion with a reason, a heuristic, a number, an explanation, a
war story, a trade-off, a recommendation. `false` for a passing name-drop, a
joke, a segue, a scheduling remark, or agreement noise.

Calibration:
- `true` — "waited over a month for those, like five weeks... I'd already
  figured, oh no, I want to change things" (about `pcb-lead-time`).
- `true` — "if it's an LED, your test is, does it turn on?" (about
  `counterfeit-components`; it's a heuristic even though it's phrased as a joke).
- `false` — "Yeah, that's what Freak Labs posted on Twitter the other day."
- `false` — "I've got a jet engine in my spare bedroom."

When genuinely ambiguous, prefer `false`. Precision on `substantive` matters
more than recall; every mention is retained either way.

**`context_snippet`** — a verbatim substring of the paragraph, ≤100 characters,
that shows why you tagged it. Trim to the informative part. Do not paraphrase,
do not add ellipses at both ends, do not include the speaker label.

## Coverage rules

1. **Extract every mention, not the interesting ones.** A passing reference to
   Digi-Key is a mention. Ten mentions of `pcb-fabrication` in one segment are
   ten mentions. Expect 80–250 mentions for a typical hour-long episode.
2. **Skip sponsor-read segments entirely** — contiguous ad copy delivered in
   marketing register, usually announced ("this episode is brought to you
   by…", "our sponsor…") and ending with a discount code or URL. Skip everything
   inside it including the product being advertised. Note that the hosts also
   promote their *own* businesses (EEVblog kits, Contextual Electronics,
   listener donations, the show's hosting). That is **not** a sponsor read —
   extract it normally, typically as `career-business` and typically
   `substantive: false`.
3. **Do extract from small talk when it carries engineering content.** Barbecue,
   gym classes and bad sci-fi films yield nothing. But a digression about
   university funding, Chinese New Year factory shutdowns, or textbook pricing
   is real domain knowledge for this audience — extract it.
4. **Ignore the show's own furniture**: the cold open, "welcome to the Amp
   Hour", episode numbering, "we'll link it in the show notes", sign-offs. These
   produce no mentions.
5. If a concept appears only inside an obviously garbled ASR run that you cannot
   resolve, skip it rather than emit a nonsense canonical name.

## Few-shot examples

**Input paragraph 21 (episode 500):**

> **Dave Jones:** Lowering the cost of assembly and lowering the cost, lowering
> the risk as well of sourcing parts and stuff like that. Because, you know,
> like you can just risk goofing it up if you can't get these. You're purchasing
> departments going around like crazy, trying to purchase 60 different reels of
> resistors. And, you know, oh, they ran out. You know, so you get a phone call
> at 2 a.m. in the morning from your assembly house because they're urgent, you
> know, in China.

**Output:**

```json
[
  {"concept": "bom-consolidation", "type": "technique", "speaker": "Dave Jones", "paragraph_index": 21, "substantive": true, "context_snippet": "Lowering the cost of assembly and lowering the cost, lowering the risk as well of sourcing parts"},
  {"concept": "component-sourcing", "type": "manufacturing", "speaker": "Dave Jones", "paragraph_index": 21, "substantive": true, "context_snippet": "purchasing departments going around like crazy, trying to purchase 60 different reels of resistors"},
  {"concept": "contract-assembly-house", "type": "manufacturing", "speaker": "Dave Jones", "paragraph_index": 21, "substantive": true, "context_snippet": "you get a phone call at 2 a.m. in the morning from your assembly house because they're urgent"}
]
```

Note: three mentions from one paragraph; `resistor` is *not* emitted separately
because the passage is about sourcing reels, not about resistors.

---

**Input paragraph 49 (episode 500):**

> **Dave Jones:** ...If people don't know what fan out is, it's chips have a
> certain drive capability. They can drive a certain amount of current whilst
> keeping a, the minimum low and high threshold levels required. There's high
> drive and there's low drive from the totem pole output... And this isn't a
> problem on CMOS. It only becomes a problem on CMOS when you have actually
> capacitance on the line...

**Output:**

```json
[
  {"concept": "fan-out", "type": "concept-principle", "speaker": "Dave Jones", "paragraph_index": 49, "substantive": true, "context_snippet": "chips have a certain drive capability. They can drive a certain amount of current"},
  {"concept": "totem-pole-output", "type": "concept-principle", "speaker": "Dave Jones", "paragraph_index": 49, "substantive": true, "context_snippet": "There's high drive and there's low drive from the totem pole output"},
  {"concept": "cmos-logic", "type": "component", "speaker": "Dave Jones", "paragraph_index": 49, "substantive": true, "context_snippet": "isn't a problem on CMOS. It only becomes a problem on CMOS when you have actually capacitance"},
  {"concept": "input-capacitance", "type": "concept-principle", "speaker": "Dave Jones", "paragraph_index": 49, "substantive": true, "context_snippet": "all the input gates have X amount of capacitance"}
]
```

---

**Input paragraph 205 (episode 500):**

> **Chris Gammell:** Here's where Dave gets his PhD. This is where Dave goes back
> and he gets his PhD in this thing. Whatever it is. And he just, he just goes to
> conferences and argues with people for the rest of his frigging life. Dr.
> Jones. Yeah.

**Output:**

```json
[]
```

Nothing here is a concept mention — it is a running joke about the co-host.

---

**Input paragraph 9 (episode 728):**

> **Alex Haro:** ...he's the inventor of the Amazon Sidewalk Wireless Network...
> part of the reason we went with Bluetooth is Bluetooth is already embedded into
> every chip... Where LoRa, you know, you can only get your chip from Semtech.
> And, you know, on top of that, the bands are discontinuous... because it's a
> lower frequency, it's in the 900 megahertz range... it's a longer wavelength.
> And so your antenna array actually has to be significantly bigger...

**Output:**

```json
[
  {"concept": "amazon-sidewalk", "type": "company-product", "speaker": "Alex Haro", "paragraph_index": 9, "substantive": false, "context_snippet": "he's the inventor of the Amazon Sidewalk Wireless Network"},
  {"concept": "bluetooth", "type": "standard-protocol", "speaker": "Alex Haro", "paragraph_index": 9, "substantive": true, "context_snippet": "Bluetooth is already embedded into every chip, but pretty much every electronics device out there"},
  {"concept": "lora", "type": "standard-protocol", "speaker": "Alex Haro", "paragraph_index": 9, "substantive": true, "context_snippet": "with LoRa, you know, you can only get your chip from Semtech"},
  {"concept": "semtech", "type": "company-product", "speaker": "Alex Haro", "paragraph_index": 9, "substantive": true, "context_snippet": "you can only get your chip from Semtech"},
  {"concept": "ism-band-fragmentation", "type": "standard-protocol", "speaker": "Alex Haro", "paragraph_index": 9, "substantive": true, "context_snippet": "the bands are discontinuous. So the frequency bands here in the U.S. versus Europe are different"},
  {"concept": "antenna-array", "type": "component", "speaker": "Alex Haro", "paragraph_index": 9, "substantive": true, "context_snippet": "it's a longer wavelength. And so your antenna array actually has to be significantly bigger"},
  {"concept": "2-4-ghz-band", "type": "standard-protocol", "speaker": "Alex Haro", "paragraph_index": 9, "substantive": true, "context_snippet": "a band that's unlicensed everywhere in the world"}
]
```

Note the mix of `substantive` values inside a single dense paragraph, and that
the mis-transcribed "2.4 megahertz band" is canonicalised to `2-4-ghz-band`
because the passage clearly means the 2.4 GHz ISM band.

---

--- TRANSCRIPT ---
