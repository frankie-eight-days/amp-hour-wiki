# Speaker Repair Map — Report

Companion to `canon/speaker_map.json` (pipeline step 2.5). Built from
`research/speaker_label_audit.md`, with every uncertain case re-checked against the transcript
itself. **No transcript or census file was modified.**

Corpus: 719 files, 360 distinct raw labels, 244,496 labelled turns.

---

## 1. Mapping counts

| | Count |
|---|---:|
| Files carrying at least one mapping | 159 |
| Label-in-file mappings emitted | 175 |
| — high confidence | 172 |
| — medium confidence | 3 |
| — low confidence | 0 (see §4 — everything that would have been "low" is in `unresolvable` instead) |
| Distinct `raw_label → canonical_person` pairs | 142 |
| Raw labels collapsed away by the map | 56 (360 → 304 surviving keys) |
| Distinct real people after repair | 293 |

The map has two layers. **Global rules** (110 pairs) apply to every file where the label occurs —
phonetic manglings, casing/punctuation splits, and affiliation text fused into the label.
**Per-file rules** (32 files) cover cases where the same string means different things in
different episodes, such as `Jeff`, `FPGAs`, `Arduino(s)`, `Atari`, and `David`.

Three entries are medium, and each says why in its `evidence` field:
`Sydney`→Jeff Keyzer (the-amp-hour-61), `Ed McMahon`→Jeff Keyzer (the-amp-hour-59), and
`Bluetooth Low Energy`→Bob Davidson (ep 232).

One entry maps to the sentinel `__SPONSOR_READ__` rather than a person: `Screaming Circuits`
(3 turns in `0482-shine-a-light`) is sponsor ad copy, not a participant. Drop it from person
counts instead of resolving it to a human.

---

## 2. Corrections to the audit

Six audit conclusions did not survive spot-checking. These are the entries most worth a second
pair of eyes, because in each case the map now disagrees with the document it was built from.

**`0501` — the audit had both clusters as one person; they are two different people.**
The audit read `Tim Ans`=145 and `Sean`=145 as an exact tie and concluded both were Tim Ansell.
The tie is real but means the opposite: it is a clean two-speaker alternation. `Tim Ans` speaks
the episode intro *including* "I'm Chris Gammell of Contextual Electronics" and asks every
interviewer question ("So your fourth time on…", "Past guest of The Amp Hour"). `Sean` gives the
guest answers ("the first time I was here…", "I'm quite happy with stuff that I can do on my
computer"). So `Tim Ans`→**Chris Gammell** and `Sean`→**Tim Ansell**. Taking the audit at face
value would have credited 145 host turns to a guest.

**`0529` — the two labels are swapped.** The audit proposed `Raspberry Pi`=88 → James Adams.
In fact `Raspberry Pi` is the host: it asks "what is Raspberry Pi Trading?", says "I'm very
excited to have you guys here", and delivers the outro and the patron-thanks read. Meanwhile the
label literally reading `Chris Gammell`=53 carries James Adams's speech — "we are basically a
subsidiary of the charity", "Who's going to answer that one? Perhaps that one's for me", and his
own Twitter handle, "At James Adams 314". Both directions are mapped.

**`0467` — a second, unflagged error in the same file.** `Super Nintendo` is confirmed as Jeroen
Domburg and upgraded from low to high: Chris opens the block with "I'm talking to Sprite" and
closes it with "Well, Sprite, thank you for this great badge", and the label spans lines 9–285
contiguously. Separately, and *not* flagged by the audit, the label `Dave Jones`=52 in this file
is not Dave Jones — he was not at Supercon 2019. It spans lines 289–493, the segment Chris opens
with "And I'm here with…", where the label answers "Sylvain Minot" and self-IDs again a few turns
later. Mapped to **Sylvain Minot**.

**`0412` — not an error at all.** The audit flagged `Mike Harrison`=187 as a host's turns wearing
a guest's name. The label self-IDs "And I'm Mike Harrison from Mike's Electric Stuff". `Chris
Gammell`=3 is genuine: Chris reads the intro and then leaves, which Dave notes on air ("he's
skiving off"). This is a Dave + Mike Harrison episode. Recorded as an identity row so a later
pass does not "repair" a correct label.

**`the-amp-hour-59` — `Ed McMahon` is probably Keyzer, not Kridner.** The audit assigned it to
Jason Kridner. The label asks BeagleBoard questions from the outside ("where did the name
BeagleBoard come from?", "for the benefit of me and also our listeners…"), never speaks in the
first person about TI or BeagleBoard, and addresses Kridner in the second person ("We've met
before, Jason, right?"). "Ed McMahon" is the show's running nickname for Keyzer — confirmed in
ep 61, where Chris says "Ed McMahon's in the house" immediately after introducing Jeff Kaiser.
Best reading: a second cluster of Keyzer split from `Jeff Kaiser`=111, with Kridner's speech
merged into other labels. Graded **medium**; this one is worth a human listen.

**`the-amp-hour-61` — `Sydney` is the third chair, not a Dave split.** The audit guessed Dave
Jones on the strength of the word "Sydney". But Dave=114 and Chris=90 are both already labelled,
and the guest Jeff Keyzer has no label anywhere in the file despite being introduced by name.
`Sydney`=112 is that missing third speaker. Mapped to **Jeff Keyzer**, medium.

Two smaller upgrades: `0354`'s `David` is **David Ledger** (high, not medium — the label self-IDs
"it's on the website. David Ledger" and Dave confirms "his real name is David Ledger"), and
`0409`'s `Peter` is **Piotr Esden-Tempski** (self-IDs "I own OneBitSquared").

---

## 3. Top 20 people by repaired turn count

Placeholders and the sponsor sentinel are excluded. The last column shows what the person's own
correctly-spelled label was worth before repair, so the size of each rescue is visible.

| # | Person | Repaired turns | Was, under the canonical spelling |
|---:|---|---:|---|
| 1 | Chris Gammell | 98,249 | 96,030 (+2,219) |
| 2 | Dave Jones | 90,797 | 90,849 (−52) |
| 3 | Jeff Keyzer | 2,467 | 107 (+2,360) |
| 4 | Jeri Ellsworth | 943 | 0 (+943) |
| 5 | Greg Charvat | 937 | 585 (+352) |
| 6 | Elecia White | 888 | 0 (+888) |
| 7 | Fran Blanche | 739 | 739 |
| 8 | Dave Young | 591 | 591 |
| 9 | Claire Wolf | 577 | 0 (+577) |
| 10 | Mike Harrison | 557 | 557 |
| 11 | Chuck Peddle | 502 | 0 (+502) |
| 12 | Travis Goodspeed | 454 | 454 |
| 13 | Michael Ossmann | 424 | 83 (+341) |
| 14 | Scott Williams | 417 | 84 (+333) |
| 15 | Colin O'Flynn | 406 | 284 (+122) |
| 16 | Tim Ansell | 390 | 107 (+283) |
| 17 | Simone Giertz | 381 | 0 (+381) |
| 18 | Andrea Morello | 381 | 381 |
| 19 | Shahriar Shahramian | 375 | 0 (+375) |
| 20 | Piotr Esden-Tempski | 367 | 16 (+351) |

Seven of the top twenty scored **zero** under their correct spelling before repair — Ellsworth,
White, Wolf, Peddle, Giertz, Shahramian, and (at 16 turns) Esden-Tempski. Any per-person
aggregation run against the raw labels would have missed them entirely.

Dave Jones goes **down** by 52. That is the `0467` correction: 52 turns that were labelled
`Dave Jones` actually belong to Sylvain Minot. He is the only person in the corpus whose count
falls after repair, which makes it a useful canary — if a downstream census shows Dave gaining
turns, the map was not applied.

---

## 4. Unresolvable

Listed in the `unresolvable` block of the JSON rather than mapped. Nothing here was guessed.

**Diarization placeholders** — no identity to recover without listening:

| Label | Turns | Files |
|---|---:|---:|
| `Speaker ?` | 3,460 | 678 |
| `SPEAKER_01` | 958 | 27 |
| `SPEAKER_00` | 397 | 22 |
| `SPEAKER_02` | 285 | 13 |
| `SPEAKER_03` | 120 | 2 |
| `Narrator` | 8 | 3 |
| `Intro Voice` | 4 | 1 |
| `Music` | 3 | 1 |
| `Unknown` | 2 | 1 |

That is **5,237 turns (2.1% of the corpus)** left deliberately unattributed.

**Multi-person merges** — two or more people share one cluster, so renaming cannot fix them
(451 turns): `Joshua And Za` (137), `Alvaro And Jen From The Ure` (97), `Jason Kridner And
Robert` (86), `Brent And Bryce Salmi` (84), and `Mahesh` (47).

`Mahesh` is a new finding and does not match the audit's description. The audit called it a
mis-transcribed name with the caller self-IDing as "Sebastian from Germany". Both names are in
the file: an early caller says "My name is Mahesh, and I'm from India", and a later turn under
the *same* label says "I'm Sebastian from Germany". It is a merge of at least two callers in a
call-in show, so it belongs here rather than in the phonetic-mangling table.

**Genuinely ambiguous** — evidence exists but is not sufficient:

- `Jeff` in `the-amp-hour-30` (24 turns) — short interjections only. No self-ID, and the strings
  "Jeff" and "MightyOhm" appear nowhere in the file body. Plausibly Keyzer given the era, but
  there is nothing in the transcript to stand on. Note this is a *different* speaker from the
  `Jeff`=238 in `0333`, which is mapped to Chris Gammell with high confidence.
- `David` in `show-345-milling-about` (37 turns) — distinct from ep 354's David. Chris=255 and
  Dave=252 are both present, so this is an unidentified third speaker.
- `Remco Stardustite`, `Brent Of Oshstencils`, `Florin Of Voltlo` / `Florin Of Voltlog` — first
  name is reliable, surname never appears in the transcript. (The two Florin spellings are the
  same person in the same file, but there is no surname to canonicalise onto.)
- `Caller` in `0307-call-in-show-5` (26 turns) — self-IDs as "Alexander from Toronto", but the
  label may cover more than one caller, so it is left alone.

---

## 5. Remaining risk

### 5.1 Merged paragraphs — the dominant residual error, and relabelling cannot touch it

The diarizer regularly fuses several speakers into one paragraph, so a single labelled turn can
contain two people's words. Relabelling fixes *who is named*; it cannot fix *where a turn begins
and ends*. Two measurements bound the damage:

**Tight lower bound: 87 turns in 87 files** contain *both* host self-introductions fused into one
paragraph — a turn labelled with one host that opens "I'm Dave Jones from the EEV blog" and
continues "And I'm Chris Gammell of…". That is 12% of the corpus with a provably merged opening
turn, and it is exactly the pattern visible in `0001-whats-in-a-name.md`, where the paragraph
labelled `**Dave Jones:**` carries Chris's replies inline.

**Loose upper bound: 6,974 turns across 718 of 719 files** contain two or more distinct
multi-word self-introductions in a single paragraph. This regex proxy over-counts (a host can
legitimately name a guest while introducing them), so treat it as a ceiling rather than an
estimate. The real figure sits between the two, and even the floor is an order of magnitude
larger than the 451 turns lost to multi-person labels.

**Consequence.** Per-speaker *word* counts over this corpus will be materially wrong no matter
how good the label map is, and the error runs in a consistent direction: whoever holds the label
on a merged paragraph absorbs the other speaker's words. Since the hosts hold most labels, host
word-counts are inflated and guest word-counts are deflated. Turn *counts* — what §3 reports —
are the more defensible metric, and even they undercount interjections swallowed mid-paragraph.
Any census that reports words per speaker should carry this caveat explicitly.

### 5.2 Duplicate transcripts double-count

Two episodes exist as two files each, and both copies survive in the map:

- Ep **117** — `0117-an-interview-with-alan-wolke-re-broadcast` and
  `theamphour-117-undulating-utensil-utility`, 291 turns each.
- Ep **241** — `0241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus` and
  `0241-an-interview-with-chuck-peddle-re-air`, 526 turns each.

**817 turns of duplication.** Chuck Peddle's 502 repaired turns are really 251 — his rank in §3
is inflated by exactly one episode. Deduplicate by episode number before publishing per-person
totals.

### 5.3 Residual clusters left in place

Where the audit found a small correct-name cluster beside a large mangled one (`Andreas
Olofsson`=4 next to `Parallela`=94, `Samy Kamkar`=1 next to `OpenGL`=109), the map sends the
mangled label to the correct name, so the two merge automatically. But the reverse case —
one person split into two clusters that are *both* plausibly named — is only handled where the
audit or a spot-check caught it. Files with an unexplained turn-count near-tie between two named
labels are the place to look for the ones still hiding.

### 5.4 Sponsor reads

31 episodes (4%) contain genuine ad reads inside the transcript body, carrying ordinary speaker
labels. Only `0729` uses explicit `(sponsored segment)` labels, which the map normalises to the
underlying people. Everywhere else the read is attributed to whichever label it landed under, and
the map cannot distinguish it. If the census is meant to skip ads, key the rule on the read-opener
forms — `This episode … is brought to you by`, `Episode N, sponsored by`, `(sponsored segment)` —
not the bare phrases `brought to you by` / `sponsored by`, which fire on 76 files of ordinary
conversation.


---

## 6. Step 2.6 — host/guest label swaps

A later pilot-articles pass flagged 144 interview episodes where the show-open boilerplate
("This is The Amp Hour Podcast… Episode NNN") sits on the *guest's* label, and proposed that
host and guest labels are swapped throughout. I re-derived the verdict for each file
independently. **The swap is real in 26 files, false in 30, and unresolvable in 83.** The
headline number does not survive: a label-level swap is the minority explanation.

Note that the suspect list arrived keyed by **canonical** names rather than raw labels — its
`Noah Feehan`=179, for example, is this map's merge of raw `Kotki`=112 and `Noah Fian`=67. The
detector had been run against a post-repair view, so every entry was translated back to raw
labels before anything was written.

### 6.1 Method

Three independent signals, in order of authority:

1. **Intro-line rule.** The boilerplate is host speech. Measured against the 431 clean
   (non-suspect) files that contain it, Chris Gammell reads it **86%** of the time (363/431) and
   Dave Jones 8%, consistently across all three eras. So a guest label holding that line is
   always wrong — but that alone does not say whether the *whole file* is swapped or just that
   one turn.
2. **Speech-role statistics.** Hosts ask and guests answer. Calibrated on 43 clean single-guest
   interview episodes: the host label runs a median **38 words/turn at 0.66 questions/turn**, the
   guest label **76 words/turn at 0.29** — a clean 2x separation in both directions. A file is a
   genuine swap only when the intro-bearing label is host-shaped *and* the `Chris Gammell` label
   is guest-shaped.
3. **Hand verification** of the content, for every medium call and a sample of the rest.

A swap is only emitted when both clusters are substantive (n ≥ 20). Where the `Chris Gammell`
cluster is vestigial, the file is a two-speakers-in-one-cluster collapse, not a recoverable swap,
and it goes to `attribution_unreliable` instead.

I also tried a "who addresses the guest by first name" signal and **discarded it** — name-hit
rates came out under 0.06 on both sides in most files, because fused paragraphs put both
speakers' name usage under one label. It could not separate host from guest.

### 6.2 Results

| Outcome | Files |
|---|---:|
| Swap confirmed, reassignments emitted | **26** (52 label entries: 20 high / 6 medium, of which 8 hand-verified and upgraded to high) |
| Intro-boilerplate label reassigned to Chris Gammell | **12** (medium) |
| Swap hypothesis **false** — labels already correct | **30** |
| `attribution_unreliable` | **83** |
| `fused_turn_files` | **143** of the 144 |

`attribution_unreliable` breaks down as 33 single-cluster files (every turn under one named
label), 30 where role statistics do not separate cleanly, 7 where the guest label holds only the
boilerplate and no other cluster is substantive, 7 with no usable intro anchor, 3 with no host
label, and 3 demoted from SWAP because the `Chris Gammell` cluster was vestigial. Those 83 files
hold **22,105 turns, 9.0% of the corpus** — content-based attribution has real work to do there.

### 6.3 The 26 confirmed swaps

In every case the exchange is between the guest-named label and `Chris Gammell`; where `Dave
Jones` is present he is unaffected.

| Episode file | Intro-bearing label → | `Chris Gammell` label → |
|---|---|---|
| `0260-an-interview-with-ariel-briner-of-cartesian-co` | `Ariel Of Cartesian Co` → Chris Gammell | `Chris Gammell` → Ariel Briner |
| `0297-an-interview-with-jake-baker` | `Jake Baker` → Chris Gammell | `Chris Gammell` → Jake Baker |
| `0302-an-interview-with-clint-cole-of-digilent` | `Clint Cole Of Digilent` → Chris Gammell | `Chris Gammell` → Clint Cole |
| `0305-an-interview-with-dave-young` | `Dave Young` → Chris Gammell | `Chris Gammell` → Dave Young |
| `0314-an-interview-with-josh-lifton` | `Josh Lifton` → Chris Gammell | `Chris Gammell` → Josh Lifton |
| `0359-an-interview-with-jeroen-domburg-sprite_tm` | `Jeroen Domburg Sprite Tm` → Chris Gammell | `Chris Gammell` → Jeroen Domburg |
| `0383-an-interview-with-scott-shawcroft` | `Scott Shawcroft` → Chris Gammell | `Chris Gammell` → Scott Shawcroft |
| `0385-an-interview-with-john-davis` | `John Davis` → Chris Gammell | `Chris Gammell` → John Davis |
| `0426-an-interview-with-dean-pick` | `Dean Pick` → Chris Gammell | `Chris Gammell` → Dean Pick |
| `0429-an-interview-with-charles-alexanian` | `Charles Alexanian` → Chris Gammell | `Chris Gammell` → Charles Alexanian |
| `0433-an-interview-with-sam-stranks` | `Sam Stranks` → Chris Gammell | `Chris Gammell` → Sam Stranks |
| `0452-an-interview-with-kieran-oleary` | `Kieran Oleary` → Chris Gammell | `Chris Gammell` → Kieran O'Leary |
| `0472-keyzermas-vacation` | `Jeff Kaiser` → Chris Gammell | `Chris Gammell` → Jeff Keyzer |
| `0511-brewing-electronics-with-eli-hughes` | `Eli Hughes` → Chris Gammell | `Chris Gammell` → Eli Hughes |
| `0517-depth-and-ai-with-brandon-gilles-and-brian-weinstein` | `Brandon Gillis` → Chris Gammell | `Chris Gammell` → Brandon Gilles |
| `0518-satellites-and-evs-with-joris-aerts` | `Starlink` → Chris Gammell | `Chris Gammell` → Joris Aerts |
| `0522-high-power-supplies-with-fredrik-kensander` | `Frederick Kinsander` → Chris Gammell | `Chris Gammell` → Fredrik Kensander |
| `0524-leds-and-evs-with-mike-harrison` | `Mike Harrison` → Chris Gammell | `Chris Gammell` → Mike Harrison |
| `0588-siloed-engineering-with-leigh-brady` | `Leigh Brady` → Chris Gammell | `Chris Gammell` → Leigh Brady |
| `0601-rebuilding-projects-with-dave-young` | `Dave Young` → Chris Gammell | `Chris Gammell` → Dave Young |
| `0616-open-source-tapeout-with-matthew-venn` | `Matthew Venn` → Chris Gammell | `Chris Gammell` → Matt Venn |
| `0618-refrigerators-and-robots-with-amitabh-shrivastava` | `Amitabh Shriv` → Chris Gammell | `Chris Gammell` → Amitabh Shrivastava |
| `0657-automating-the-home-with-keith-burzinski` | `Keith Burzinski` → Chris Gammell | `Chris Gammell` → Keith Burzinski |
| `0667-long-distance-with-cnlohr-a` | `Cnlohr A` → Chris Gammell | `Chris Gammell` → CNLohr |
| `0695-making-the-invisible-visible-with-sam-aldahar` | `Sam Aldah` → Chris Gammell | `Chris Gammell` → Sam Aldhaher |
| `the-amp-hour-155-mini-module-master` | `Jeff Roberg` → Chris Gammell | `Chris Gammell` → Jeff Roberg |

### 6.4 Spot-check evidence (5 examples)

**`0518-satellites-and-evs-with-joris-aerts`** — the `Starlink` label explains the guest's own
employer to the audience: *"if people don't remember, Hyber is a IoT-centric kind of satellite
company… Is that a good characterization?"* That is host speech. The `Chris Gammell` label
carries the fused self-intro *"Hi, my name is Yoris, and I currently work at Hyber"* and all of
Joris's answers. **This overrides a step-2.5 entry** that had read `Starlink` as Joris Aerts on
the audit's "title names the sole guest" reasoning.

**`0314-an-interview-with-josh-lifton`** — the `Chris Gammell` label speaks as Crowd Supply:
*"there's the vetting and then there's what we do to actually help you once we do work with
you"*, and *"our creators"*. That is Josh Lifton. Conversely the `Josh Lifton` label refers to
Dave in the third person: *"Dave is in the throes of this right now."*

**`0297-an-interview-with-jake-baker`** — the `Chris Gammell` label says *"I'm a professor here in
the U.S., and I've been a professor at University of Nevada, Las Vegas, where I am right now."*
That is Jake Baker. The `Jake Baker` label carries the fused *"And I'm Chris Gammell of Contextual
Electronics… So, Jake, what is your main profession?"*

**`0588-siloed-engineering-with-leigh-brady`** — the `Leigh Brady` label asks *"But what kind of
industry is there? Where are you floating around in industry right now?"* and the `Chris Gammell`
label answers *"It's an interesting place to be an electrical engineer. You're absolutely correct
that Disney parks, Universal, SeaWorld… are here."* The questioner is the host.

**`0601-rebuilding-projects-with-dave-young`** — the `Dave Young` label says *"You are a guest of
the show in the past… 305 and 409, which of course we will link into the show notes."* Only the
host refers to his own show notes.

### 6.5 Where the swap hypothesis was FALSE (30 files)

In these the guest label is genuinely the guest — long, answer-shaped turns — and both host
labels behave like hosts. The only defect is that the single boilerplate turn landed on the
guest's cluster, which **a label-level map cannot express**: the label is correct for its other
hundreds of turns. Two hand-checks:

- `0165-an-interview-with-henry-ott-forced-fcc-filtering` — the `Henry Ott` label self-IDs *"And
  I'm Henry Ott of Henry Ott Consultants"* and later *"I spent 30 years there [Bell Labs]"*. It is
  Henry Ott. (Chris has no label at all here; his speech is fused into `Dave Jones`, whose opening
  turn reads *"I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics."*)
- `0189-an-interview-with-marcus-schappi-kit-ketch-kenophobia` — the `Marcus Schaffe` label
  self-IDs *"And I'm Marcus Schaffe from Micreview"* and talks first-person about Ninja Blocks.
  Both hosts are correctly labelled.

The full list:

- `0165-an-interview-with-henry-ott-forced-fcc-filtering`
- `0171-an-interview-with-forrest-mims-snell-solisequious-scientist`
- `0189-an-interview-with-marcus-schappi-kit-ketch-kenophobia`
- `0228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole`
- `0254-an-interview-with-andreas-olofsson-adaptevas-ampliative-abacus`
- `0263-an-interview-with-fran-blanche`
- `0290-an-interview-with-mark-morin-of-nufern`
- `0299-an-interview-with-jonathan-hirschman-of-pcbng`
- `0311-an-interview-with-louis-rossmann`
- `0316-an-interview-with-robert-feranec`
- `0330-an-interview-with-zach-fredin`
- `0332-an-interview-with-zach-barth-of-zachtronics`
- `0334-an-interview-with-gerry-roston`
- `0338-an-interview-with-jorgen-jakobsen`
- `0379-an-interview-with-john-saunders`
- `0416-an-interview-with-james-bruton`
- `0481-an-interview-with-paul-thompson`
- `0490-an-interview-with-ben-heckendorn`
- `0503-fabless-chip-design-with-mohammed-kassem`
- `0521-outdoor-laser-projection-object-mapping-with-daryl-tewksbury`
- `0553-debunking-with-shahriar`
- `0583-the-smart-grid-with-paul-zawada`
- `0590-finding-hardware-flaws-with-laura-abbott`
- `0661-blogging-electronics-with-pallav-aggarwal`
- `0672-silicon-revolution-with-matt-venn`
- `0689-a-jumperless-breadboard-with-kevin-cappuccio`
- `0701-electric-propulsion-with-todd-bailey`
- `0716-electronics-manufacturing-history-with-david-ray`
- `the-amp-hour-133-tenacious-transistor-teacher`
- `the-amp-hour-87-nascent-nonolith-numquid`

These 30 carry a one-turn error each (~30 turns corpus-wide, 0.01%). Not worth chasing; recorded
so a future pass does not re-flag them.

### 6.6 Fused paragraphs

`fused_turn_files` lists **143 of the 144** suspect files, **1,873 fused turns**. A paragraph
counts as fused when it carries two or more distinct multi-word self-introductions, or asks a
question and answers it in the first person twice, or asks a question and then runs past 80 words.
Corpus-wide the same test finds **10,321 fused turns (4.2%) across 713 of 719 files** — a sharper
figure than the loose bound in §5.1, and it confirms that direction: the floor is 87 provable
host-intro fusions, the realistic figure is around 4% of all turns, and the regex ceiling of ~6,974
multi-self-ID turns was an over-count.

Fusion is why the swap looked more widespread than it is. The standard opening splits as:

```
**<Guest label>:** This is The Amp Hour Podcast… Episode N. <title>. Welcome to the Amp Hour.
**Chris Gammell:** I'm Chris Gammell of Contextual Electronics. And I'm <Guest>, who does <bio>.
```

The second line is one paragraph holding **both** speakers, so the guest's bio genuinely does sit
under the `Chris Gammell` label — in swapped and unswapped files alike. That is a fusion artifact,
not proof of a swap, and it is what a detector keyed on bio content will trip over. Only the
whole-file role statistics separate the two cases.

### 6.7 Effect on the counts

Chris Gammell drops **368 turns** net (97,881), because the guest-shaped `Chris Gammell` clusters
he loses in the 26 swapped files outweigh the host-shaped intro clusters he gains. Mike Harrison
gains 71 (628). Dave Jones is unchanged. No other top-20 position moves by more than one turn —
the swap repair is concentrated, not corpus-wide.
