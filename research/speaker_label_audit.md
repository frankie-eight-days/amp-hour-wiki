# Speaker Label Audit — Amp Hour Transcript Corpus

Audit of 719 transcript files in `transcripts/`. **No speaker labels were modified.** This
report is diagnostic only. (The frontmatter `episode:` backfill *was* applied — see §5.)

Corpus totals: **360 distinct speaker labels**, **244,496 labelled turns**.

---

## 1. How the labels went wrong

The transcripts were machine-diarized, and the pipeline named each diarized speaker by pulling a
**salient noun phrase out of that speaker's own speech** rather than by identifying the person.
That single mechanism explains nearly every bad label, and it produces three distinct failure
shapes:

**Named from a product, company, or place they talked about.** Chuck Peddle becomes `Atari`,
Luke Valenty becomes `FPGAs`, Andreas Olofsson becomes `Parallela`, Fabienne Serrière becomes
`Forbes`, Bunnie Huang becomes `Asia`. The guest's real name is almost always sitting in the
file's `title:` field, which makes these highly recoverable.

**Named from the episode title, when that speaker read the intro.** Chris Gammell opens most
post-2019 episodes with "This is The Amp Hour Podcast… Episode N. *<title>*." The pipeline
grabbed the title words. So episode 680 "Catching Rockets with Musk Sticks" labels Chris as
`Musk Sticks`, and episode 707 "Welding with an HDMI Cable" labels him `An Hdmi Cable`. **This
is the most consequential class**, because it silently attributes a *host's* words to a
nonexistent person — a census counting "who appeared" would invent guests.

**Phonetic mangling of a real name.** `Jeff Kaiser` for Jeff Keyzer, `Jerry Ellsworth` for Jeri
Ellsworth, `Alicia White` for Elecia White, `Simone Yach` for Simone Giertz. These are
lower-risk (a human reads them correctly) but they fragment identity across files, so any
per-person aggregation will undercount.

A useful diagnostic: the correct name often *also* appears in the same file with a tiny turn
count — `Andreas Olofsson`=4 alongside `Parallela`=94, `Samy Kamkar`=1 alongside `OpenGL`=109,
`Orkhan Amiraslanov`=1 alongside `LoRaWAN`=99. The diarizer split one person into two clusters
and named them independently.

---

## 2. Flagged suspects

Confidence key: **High** = title, self-introduction, and turn-count arithmetic all agree.
**Medium** = strong inference from two of those. **Low** = needs a human listen.

### 2a. Host mislabelled as a non-person (highest priority)

In every one of these the bogus label carries a *host's* turns. Evidence is arithmetic: the
other host's turn count is within a few of the bogus label's, and the real host's label is
absent or vestigial. Where the label speaks the "This is The Amp Hour Podcast… Episode N" intro,
attribution to Chris Gammell is certain — that line is his in every episode that has it.

| File | Bad label | Turns | Inferred correct | Evidence | Conf. |
|---|---|---:|---|---|---|
| `0680-catching-rockets-with-musk-sticks.md` | `Musk Sticks` | 215 | Chris Gammell | Speaks intro; next turn is "And I'm Chris Gammell of Contextual Electronics." Dave Jones=220, no Chris label | High |
| `0707-welding-with-an-hdmi-cable.md` | `An Hdmi Cable` | 169 | Chris Gammell | Speaks intro; self-IDs "And I'm Chris Gammell". Dave=165, no Chris label | High |
| `0674-turtles-as-a-service.md` | `Ethernet` | 198 | Chris Gammell | Speaks intro. Dave=199, no Chris label | High |
| `0589-mute-button-discipline.md` | `LTSpice` | 164 | Chris Gammell | Speaks intro; refers to Dave in 3rd person. Dave=165, no Chris label | High |
| `0576-a-literal-trainwreck.md` | `Missouri` | 179 | Chris Gammell | Speaks intro. Dave=180, Chris=5 residual | High |
| `0585-return-of-the-trade-show-jedi.md` | `Paul` | 156 | Chris Gammell | Speaks intro. Dave=149, Chris=21 residual | High |
| `0333-science-not-silence.md` | `Jeff` | 238 | Chris Gammell | Speaks intro. Dave=238, no Chris label | High |
| `the-amp-hour-45-nerdy-neuroelectronic-neurosis.md` | `Fat Man` | 258 | Chris Gammell | Speaks intro. Dave=257, no Chris label | High |
| `0555-timing-is-everything.md` | `Yankee` | 261 | Chris Gammell | Dave=260, Chris=13 residual; two-host live episode | High |
| `the-amp-hour-70-idiorhythmic-ipc-inconcinnity.md` | `Abraham` | 195 | Chris Gammell | Dave=199, no Chris label; two-host episode | High |
| `0412-3-cent-micros-and-1000s-of-leds.md` | `Mike Harrison` | 187 | Chris Gammell | Dave=184, Chris=3 residual. Mike Harrison is a real recurring guest, but here the label carries the host's turns | Medium |
| `the-amp-hour-61-gallimaufry-gan-gabble.md` | `Sydney` | 112 | Dave Jones (split) | Dave=114 *and* Chris=90 both present — one host was split into two clusters mid-file; "Sydney" points to Dave | Low |

### 2b. Guest mislabelled as a product, company, or place

| File | Bad label | Turns | Inferred correct | Evidence | Conf. |
|---|---|---:|---|---|---|
| `0650-accessible-asics-with-andreas-olofsson.md` | `Parallela` | 94 | Andreas Olofsson | Title; `Andreas Olofsson`=4 in same file | High |
| `0241-an-interview-with-chuck-peddle-*.md` (2 files) | `Atari` | 251 ea. | Chuck Peddle | Title; label self-IDs "My name is Chuck Petal" | High |
| `0395-an-interview-with-luke-valenty.md` | `FPGAs` | 172 | Luke Valenty | Title; sole guest | High |
| `0525-open-fpga-toolchains-...-brian-faith-of-quicklogic.md` | `FPGAs` | 90 | Brian Faith | Title; sole guest | High |
| `0390-an-interview-with-sam-zeloof.md` | `Arduinos` | 170 | Sam Zeloof | Title; sole guest, discusses "making chips in the garage" | High |
| `0235-an-interview-with-matt-richardson-...` | `Arduino` | 113 | Matt Richardson | Title; sole guest | High |
| `0376-an-interview-with-richard-ginus.md` | `IoT` | 226 | Richard Ginus | Title; sole guest | High |
| `0518-satellites-and-evs-with-joris-aerts.md` | `Starlink` | 184 | Joris Aerts | Title; sole guest | High |
| `0257-an-interview-with-fabienne-serriere-of-knityak.md` | `Forbes` | 232 | Fabienne Serrière | Title; `Fabienne Of Knityak`=7 in same file | High |
| `0308-an-interview-with-samy-kamkar.md` | `OpenGL` | 109 | Samy Kamkar | Title; `Samy Kamkar`=1 in same file | High |
| `0557-generic-nodes-with-orkhan-amiraslanov.md` | `LoRaWAN` | 99 | Orkhan Amiraslanov | Title; `Orkhan Amiraslanov`=1 in same file | High |
| `0323-an-interview-with-tony-dicola.md` | `MicroPython` | 80 | Tony DiCola | Title; sole guest | High |
| `0640-software-defined-power-supplies-with-werner-johansson.md` | `Bluetooth` | 110 | Werner Johansson | Title; `Werner`=105 is the other cluster of the same person | High |
| `0232-impedance-matching-with-davidson-and-vandenbout-...` | `Bluetooth Low Energy` | 97 | Bob Davidson | Title names Davidson and Vandenbout; Vandenbout has his own (mangled) label | Medium |
| `0473-an-interview-with-greg-davill.md` | `Icebreaker FPGA` | 100 | Greg Davill | Title; sole guest; only two labels in file | High |
| `0529-embedded-hardware-with-the-raspberry-pi-team.md` | `Raspberry Pi` | 88 | James Adams (likely) | Team episode; `Liam Fraser`/`Luke Renn` labelled separately; matches `James Adams` role in eps 648/687 | Medium |
| `0266-an-interview-with-ronald-sousa-...` | `London` | 103 | Ronald Sousa | Title; `Ronald Sousa Of Hash Defi`=1 in same file | High |
| `the-amp-hour-336-an-interview-with-bunnie-huang-2nd.md` | `Asia` | 103 | Bunnie Huang | Title; label says "I'm located in Singapore" | High |
| `0175-an-interview-with-andrew-witte-...` | `Engadget` | 180 | Andrew Witte | Title; label describes working at Pebble | High |
| `0204-an-interview-with-noah-feehan-...` | `Kotki` | 112 | Noah Feehan | Title; `Noah Fian`=67 is the other cluster of same person | High |
| `0169-an-interview-with-vincent-himpe-...` | `Free Electron` | 219 | Vincent Himpe | Label self-IDs "this is Free Electron, or as I'm known in the real world, Vincent Hempey" | High |
| `0268-an-interview-with-luke-iseman-of-ycombinator.md` | `Y Combinator` | 73 | Luke Iseman | Title; `Luke Iseman Of Ycombinato`=1 in same file | High |
| `0467-stories-from-supercon-2019.md` | `Super Nintendo` | 70 | Jeroen Domburg / Sprite_tm (likely) | Supercon badge-FPGA discussion matches Sprite_tm's 2019 badge work | Low |
| `0365-wait-why-is-jeff-glowing.md` | `Mighty Home` | 94 | Jeff Keyzer | "MightyOhm" is Keyzer's handle; title is "Wait, why is Jeff glowing?" | High |
| `the-amp-hour-454-mike-grover.md` | `AT-Tinny's` | 69 | Mike Grover | `Mike Grover Mg`=79 is the other cluster of same person | High |
| `0482-shine-a-light.md` | `Screaming Circuits` | 3 | *(sponsor ad voiceover)* | Ad copy for the episode sponsor, not a show participant — see §4 | High |
| `the-amp-hour-59-bonafide-beagleboard-bionomics.md` | `Ed McMahon` | 75 | Jason Kridner | Title names Keyzer and Kridner; Keyzer has own label. "Ed McMahon" is a running joke *in* the episode | Medium |

### 2c. Single-word labels that are a real person's first name or handle

Not wrong so much as **non-canonical** — they will fragment a per-person census.

| File | Label | Turns | Canonical name | Conf. |
|---|---|---:|---|---|
| `the-amp-hour-149-purple-pcb-philosophy.md` | `Lane` | 338 | Laen (OSH Park) | High |
| `0354-a-meeting-of-the-davids.md` | `David` | 338 | the guest "other David" | Medium |
| `0562-electroboom.md` | `Mehdi` | 190 | Mehdi Sadaghdar | High |
| `the-amp-hour-84-bunnies-bibelot-bonification.md` | `Bunny` | 124 | Bunnie Huang | High |
| `0614-reunion-impedance-matching-...` | `Alvaro` | 119 | Alvaro Prieto | High |
| `0448-an-interview-with-jean-rintoul.md` | `Gene` | 98 | Jean Rintoul | High |
| `0409-electronics-consultant-impedance-matching.md` | `Peter` | 67 | Piotr Esden-Tempski (1BitSquared) | High |
| `0461-an-interview-with-jonathan-georgino.md` | `Bino` | 70 | Jonathan Georgino | High |
| `0355-the-internet-of-septage-with-akiba.md` | `Akiba` | 152 | Akiba (Christopher Wang) | High |
| `0501-discussing-the-open-source-pdk-with-tim-ansell.md` | `Sean` | 145 | Tim Ansell | Medium |
| `0640-...-werner-johansson.md` | `Werner` | 105 | Werner Johansson | High |
| `0228`, `0430` | `Shariar` | 306 | Shahriar Shahramian | High |
| `0288-call-in-show-3.md` | `Mahesh` | 47 | caller self-IDs as "Sebastian from Germany" | Medium |

`0501` deserves a note: `Tim Ans`=145 and `Sean`=145 are an exact tie, the signature of one
speaker duplicated into two clusters. Both are Tim Ansell.

### 2d. Phonetic manglings of real names (identity fragmentation)

Highest-volume error first. All High confidence — the title carries the correct spelling in each
case.

| Bad label | Turns | Files | Correct name |
|---|---:|---:|---|
| `Jeff Kaiser` | 2079 | 19 | **Jeff Keyzer** — spelled correctly as `Jeff Keyzer` (107 turns) in `theamphour-82-...`, confirming the same person |
| `Jerry Ellsworth` | 943 | 5 | Jeri Ellsworth |
| `Alicia White` (656) + `Eliseo White` (232) | 888 | 5 | Elecia White |
| `Clifford Wolf` | 577 | 2 | **Claire Wolf** — title reads "Claire (née 'Clifford') Wolf"; use the current name |
| `Gregory Charvat` (352) + `Greg Charvat` (585) | 937 | 6 | Greg Charvat (pick one form) |
| `Simone Yach` (267) + `Simone Yetsch` (114) | 381 | 2 | Simone Giertz |
| `Scott Williams From` | 333 | 1 | Scott Williams (Xentronics) |
| `Piotr Ezdintensky` (244) + `Pietro Ezrin-Temsky` (40) + `Piotr Esden-Tempski` (16) | 300 | 3 | Piotr Esden-Tempski |
| `Bruce Simpson` | 274 | 1 | Bruce Simson |
| `Charlie Larrabe` | 202 | 1 | Charlie Larrabee |
| `Vic Apria` | 185 | 1 | Vic Aprea |
| `Ron Demko` | 183 | 1 | Ron Demcko |
| `Nadia Peek` | 182 | 1 | Nadya Peek |
| `Marcus Schaffe` | 172 | 1 | Marcus Schappi |
| `Ben Heckendorn` | 166 | 1 | Ben Heck (Heckendorn) — arguably correct, listed for completeness |
| `Davith Roche` | 161 | 1 | Dafydd Roche |
| `Kevin Cappucio` | 152 | 1 | Kevin Cappuccio |
| `Michael G` (149) + `Michael Gieldo` (66) | 215 | 2 | Michael Gielda |
| `Mike Stisch` | 145 | 1 | Mike Szczys |
| `Amitabh Shriv` | 134 | 1 | Amitabh Shrivastava |
| `Evin Yanbu` (131) + `Oyvian Yanbu` (3) | 134 | 1 | Øyvind Janbu |
| `Jack Gansel` | 129 | 1 | Jack Ganssle (`Jack Ganssle`=95 also present) |
| `Andrew Seddo` | 129 | 1 | Andrew Seddon |
| `Ron Kwan` | 127 | 1 | Ron Quan |
| `Dmitry Netospazov` | 121 | 1 | Dmitry Nedospasov |
| `Eric Bogutin` | 117 | 1 | Eric Bogatin |
| `Carrie Sharpglass` | 115 | 1 | Kerry Scharfglass |
| `Frederick Kinsander` | 115 | 1 | Fredrik Kensander |
| `Tom Laments` | 109 | 1 | Tom LeMense |
| `Dave Vandenbaum` | 108 | 1 | Dave Vandenbout |
| `Michael Osman` (106) + `Michael Ossman` (83) | 189 | 2 | Michael Ossmann |
| `Hank Zumbelan` | 100 | 1 | Hank Zumbahlen |
| `Brandon Gillis` | 99 | 1 | Brandon Gilles |
| `Mike Englehart` | 94 | 2 | Mike Engelhardt |
| `Akbar Dinaliwala` | 92 | 1 | Akbar Dhanaliwala |
| `Zach Ferdinand` | 87 | 1 | Zach Fredin |
| `Sam Aldah` | 84 | 1 | Sam Aldhaher |
| `Zach Hoken` | 82 | 1 | Zach Hoeken (Smith) |
| `Steve Senge` | 82 | 1 | Steve Sanghi |
| `Philip Johnston` | 81 | 1 | Phillip Johnston |
| `Pete Bevelaqua` | 76 | 1 | Pete Bevelacqua |
| `Colin Kidder` | 71 | 1 | Collin Kidder |
| `Benjamin Kabe` | 69 | 1 | Benjamin Cabé |
| `Noah Fian` | 67 | 1 | Noah Feehan |
| `Michael Zalewski` | 60 | 1 | Michał Zalewski (lcamtuf) |
| `Eric Schlepfer` | 58 | 1 | Eric Schlaepfer |
| `Wendell Aske` | 51 | 1 | Windell Oskay |
| `Mark Palmieri` | 49 | 1 | Mark Palmeri |
| `Adam Wolfe` | 142 | 1 | Adam Wolf |
| `Bill Hurd` | 43 | 1 | Bil Herd |
| `Voya Antinich` | 1 | 1 | Voja Antonić |
| `Sean Meehan` | 1 | 1 | Shaun Meehan |

Also note `Colin O'Flynn` (284, 2 files) vs `Colin Oflynn` (122, 1 file), and `Matt Venn` (136)
vs `Matthew Venn` (139), and `Adam McCombs` (100) vs `Adam Mccombs` (101) — same people, split
by punctuation and casing.

### 2e. Labels contaminated with trailing affiliation text

Cosmetic, but they break exact-match aggregation: `Alan Wolke Rebroadcast`, `Jonathan Hirschman
Of Pcb`, `Clint Cole Of Digilent`, `Zach Barth Of Zachtronics`, `Ariel Of Cartesian Co`,
`Florin Of Voltlo` / `Florin Of Voltlog` (same person, same file, two spellings), `Uri Shaked
Wokwicom`, `Ray Ozzie Blues Wireless`, `Jeroen Domburg Sprite Tm`, `Mike Grover Mg`, `Ben
Krasnow 8 Years On`, `Scott Miller 2nd`, `David Kronstein Tesla500`, `Stefan Dzisiewski Smith`,
`Tim Mithro Ansell`, `Luke Iseman Of Ycombinato`, `Ronald Sousa Of Hash Defi`, `Brent Of
Oshstencils`, `Saberkite Use Us`, `Phil's Lab` (= Philip Salmony), `Fabienne Of Knityak`,
`Craig J Bishop`, `Remco Stardustite`.

The **multi-person** labels are a different problem — `Jason Kridner And Robert`, `Brent And
Bryce Salmi`, `Joshua And Za`, `Alvaro And Jen From The Ure` each contain **two people's speech
merged into one cluster**, so they cannot be fixed by renaming.

### 2f. Diarization placeholders (not names)

| Label | Turns | Files |
|---|---:|---:|
| `Speaker ?` | 3460 | 678 |
| `SPEAKER_01` | 958 | 27 |
| `SPEAKER_00` | 397 | 22 |
| `SPEAKER_02` | 285 | 13 |
| `SPEAKER_03` | 120 | 2 |
| `Caller` | 26 | 1 |
| `Narrator` | 8 | 3 |
| `Intro Voice` | 4 | 1 |
| `Music` | 3 | 1 |
| `Unknown` | 2 | 1 |

`Speaker ?` appears in 678 of 719 files — the pipeline's catch-all for short interjections.
`Caller` in `0307-call-in-show-5.md` is arguably correct usage (an unnamed listener), though the
caller self-IDs as "Alexander from Toronto" in his first turn.

---

## 3. A caveat that affects any downstream census

Independently of the labels, **the diarization frequently merges several speakers into a single
paragraph**. In `0001-whats-in-a-name.md` the paragraph labelled `**Dave Jones:**` carries
Chris's replies inline; the same is visible in most files flagged above. Turn boundaries are lost
mid-paragraph.

So a per-speaker word-count census over this corpus will be materially wrong regardless of how
the labels are fixed. Label correction addresses *who is named*; it does not address *where each
turn begins and ends*.

---

## 4. Sponsor reads (scan results)

Grepping the full marker set (`brought to you by`, `sponsored by`, `use code`, `promo code`,
`/amphour`, `this episode is supported`) returns **107 files**, but most are **incidental
conversation** — hosts joking about sponsorship, or a guest saying their research was "sponsored
by" someone. Filtering to genuine ad-read syntax gives **31 episodes (4% of the corpus)**:

- **15 files** with `This episode of the Amp Hour is brought to you by ContextualElectronics.com`
  — Chris Gammell's own course. Clustered in eps **128–177**, plus **291, 355, 466, 488**.
- **16 files** with an intro-line sponsor tag, `Episode N, sponsored by X` — all in eps
  **480–729**: Screaming Circuits (480, 482, 484, 489), Roden (483), Keysight (497),
  Mouser/"Mauser" (498, 508, 526, 544, 568, 583), InspectAR (548), "Maser" (558), Blues (707),
  Siemens (729).
- **1 file** (`0729`) uses explicit `(sponsored segment)` speaker labels — 11 turns.

`/amphour` and `this episode is supported` return **zero** hits; those two markers can be dropped
from any detection rule.

**The reads live inside the transcript body, not in show-note text.** They carry ordinary speaker
labels and sit in the paragraph stream like any other turn. Three examples:

> `**Lane:** This episode of the Amp Hour is brought to you by ContextualElectronics.com. Are you
> an advanced Arduino user? Perhaps you're a hardware engineer who's still a student or just
> getting started. Maybe you're a software person who's being asked to design the products you
> normally just program. Contextual Electronics is a hands-on course taught remotely. You'll
> learn all about how to design your own PCBs from scratch using KiCad and get timely instruction
> about the nuances of working with electronics.`
>
> — `the-amp-hour-149-purple-pcb-philosophy.md`. The read is attributed to **`Lane`**, the
> guest's label, which is wrong twice over: it is Chris reading, and "Lane" is itself a
> mis-transcription of the guest's name "Laen".

> `**An Hdmi Cable:** This is the Amp Hour Podcast. Release October 26th, 2025. Episode 707,
> sponsored by Blues. Welding with an HDMI cable.`
>
> — `0707-welding-with-an-hdmi-cable.md`. The sponsor tag is fused into the standard episode
> intro line, and the speaker label is itself derived from that same line (see §2a).

> `**Chris Gammell (sponsored segment):** We know the feeling — you spent years mastering your
> current CAD tool. You know every quirk, workaround and menu. Switching feels like changing a
> religion, but what if the friction you're used to isn't required? We talked to past guests of
> the show, Shrouk El Attar from episode 549, about her experience…`
>
> — `0729-the-terahertz-frontier-greg-charvat-teradar.md`, the only file with dedicated
> sponsored-segment labels (`Chris Gammell (sponsored segment)`=6, `Shrouk El Attar (sponsored
> segment)`=5).

**Implication for the census prompt.** The sponsor-skipping rule is worth keeping but is a
narrow concern. An unskipped read attributes vendor marketing copy to whoever's label it landed
under — and in `0482` it would invent a speaker literally named `Screaming Circuits`. However, a
rule keyed on the bare strings `brought to you by` / `sponsored by` would fire on the other 76
files where those phrases are ordinary conversation. Key the rule on the read-opener forms
(`This episode ... is brought to you by`, `Episode N, sponsored by`, `(sponsored segment)`)
rather than the bare phrases.

---

## 5. Frontmatter backfill (applied)

169 files lacked an `episode:` field. Numbers were derived from the filename stem, the URL slug,
and the spoken intro line (`…Episode N.`), accepting a value only where the available sources
agreed.

- **165 files backfilled.** All legacy-named (`the-amp-hour-N-*.md`, `theamphour-N-*.md`,
  `show-N-*.md`, plus one slug-only file resolved from its intro line). **715 of 719** files now
  carry `episode:`.
- **4 files left untouched** — no episode number appears in filename, URL, title, or body:
  - `chips-and-fabs-and-garages.md`
  - `ham-spam-thank-you-maam.md`
  - `quassating-quadcopter-quantophrenia.md`
  - `the-chinese-clairvoyancy.md`

Two **duplicate-content pairs** surfaced during the backfill (one episode, two files):

- Ep **117** — `0117-an-interview-with-alan-wolke-re-broadcast.md` and
  `theamphour-117-undulating-utensil-utility.md`. Both transcribe the 2021 rebroadcast and both
  bodies say "Episode 117".
- Ep **241** — `0241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus.md` and
  `0241-an-interview-with-chuck-peddle-re-air.md`. Identical label counts
  (`Dave Jones`=263, `Atari`=251, `Speaker ?`=12) confirm duplicate text.

These will double-count in any corpus-wide aggregate.

---

## 6. Full label inventory

All 360 distinct labels, by turn count. The Files column lists file stems where a label appears
in four or fewer files.

| Label | Turns | Files | Episodes (file stems) |
|---|---:|---:|---|
| `Chris Gammell` | 96030 | 639 | _639 files_ |
| `Dave Jones` | 90849 | 558 | _558 files_ |
| `Speaker ?` | 3460 | 678 | _678 files_ |
| `Jeff Kaiser` | 2079 | 19 | _19 files_ |
| `SPEAKER_01` | 958 | 27 | _27 files_ |
| `Jerry Ellsworth` | 943 | 5 | _5 files_ |
| `Fran Blanche` | 739 | 3 | 0263-an-interview-with-fran-blanch, 0540-the-space-time-continuum-with, 0647-dave-hanging-with-fran-blanch |
| `Alicia White` | 656 | 4 | 0187-an-interview-with-elecia-whit, 0256-is-this-a-show, 0281-crossovers-and-call-ins, 0422-stick-em-on-whales |
| `Dave Young` | 591 | 4 | 0305-an-interview-with-dave-young, 0409-electronics-consultant-impeda, 0601-rebuilding-projects-with-dave, 0628-two-dads-puzzlin-things-out |
| `Greg Charvat` | 585 | 3 | 0179-greg-charvat-returns-with-a-b, 0729-the-terahertz-frontier-greg-c, the-amp-hour-115-watcher-of-wraith |
| `Clifford Wolf` | 577 | 2 | 0374-an-interview-with-claire-nee-, 0423-open-fpga-toolchains-at-35c3 |
| `Mike Harrison` | 557 | 4 | 0224-meracious-mike-manuduction, 0294-live-from-serbia-with-mike-ha, 0412-3-cent-micros-and-1000s-of-le, 0524-leds-and-evs-with-mike-harris |
| `Atari` | 502 | 2 | 0241-an-interview-with-chuck-peddl, 0241-an-interview-with-chuck-peddl |
| `Travis Goodspeed` | 454 | 1 | 0442-an-interview-with-travis-good |
| `SPEAKER_00` | 397 | 22 | _22 files_ |
| `Andrea Morello` | 381 | 1 | 0498-quantum-computing-with-andrea |
| `David` | 375 | 2 | 0354-a-meeting-of-the-davids, show-345-milling-about |
| `Akiba` | 366 | 2 | 0245-an-interview-with-akiba-from-, 0355-the-internet-of-septage-with- |
| `Gregory Charvat` | 352 | 2 | 0214-impedance-matching-with-charv, 0407-gregory-charvat-and-three-new |
| `Big Clive` | 340 | 1 | the-amp-hour-539-the-king-of-trash |
| `Jason Huggins` | 340 | 1 | 0369-an-interview-with-jason-huggi |
| `Lane` | 338 | 1 | the-amp-hour-149-purple-pcb-philos |
| `James Bruton` | 337 | 1 | 0416-an-interview-with-james-bruto |
| `Scott Williams From` | 333 | 1 | 0624-design-manufacturing-consulti |
| `Jay Carlson` | 331 | 1 | 0515-embedded-linux-with-jay-carls |
| `Henry Ott` | 329 | 1 | 0165-an-interview-with-henry-ott-f |
| `Ari Gerstman` | 325 | 1 | 0630-renewable-energy-policy-with- |
| `Adrian Tang` | 323 | 1 | 0483-an-interview-with-adrian-tang |
| `Charles Aylward` | 317 | 1 | 0584-software-for-rockets-with-cha |
| `Matt Liberty` | 306 | 3 | 0527-measuring-current-with-matt-l, 0607-the-joulescope-upgrade-with-m, 0722-ai-tooling-with-matt-liberty- |
| `Shariar` | 306 | 2 | 0228-an-interview-with-shahriar-fr, 0430-shahriar-discusses-5g |
| `Joel Dunsmore` | 291 | 1 | 0533-microwave-measurement-with-jo |
| `Davide Andrea` | 289 | 1 | 0708-all-the-connectors-with-david |
| `SPEAKER_02` | 285 | 13 | _13 files_ |
| `Colin O'Flynn` | 284 | 2 | 0239-an-interview-with-colin-oflyn, 0693-small-scale-electronics-manuf |
| `Alan Wolke Rebroadcast` | 282 | 2 | 0117-an-interview-with-alan-wolke-, theamphour-117-undulating-utensil- |
| `Bart Dring` | 277 | 1 | 0438-an-interview-with-bart-dring |
| `Zach Dunham` | 276 | 1 | 0350-an-interview-with-zach-dunham |
| `Natasha Baker` | 275 | 1 | 0531-footprints-and-symbols-with-n |
| `Bruce Simpson` | 274 | 1 | 0538-missle-man-with-bruce-simson |
| `Martin Lorton` | 273 | 1 | 0206-an-interview-with-martin-lort |
| `Omer Kilic` | 269 | 1 | 0295-an-interview-with-omer-kilic |
| `Simone Yach` | 267 | 1 | 0331-an-interview-with-simone-gier |
| `John Saunders` | 263 | 1 | 0379-an-interview-with-john-saunde |
| `FPGAs` | 262 | 2 | 0395-an-interview-with-luke-valent, 0525-open-fpga-toolchains-and-mach |
| `Jeff` | 262 | 2 | 0333-science-not-silence, the-amp-hour-30-funding-fusion-is- |
| `Todd Bailey` | 261 | 2 | 0194-an-interview-with-todd-bailey, 0701-electric-propulsion-with-todd |
| `Yankee` | 261 | 1 | 0555-timing-is-everything |
| `Fat Man` | 258 | 1 | the-amp-hour-45-nerdy-neuroelectro |
| `Paul Zawada` | 253 | 1 | 0583-the-smart-grid-with-paul-zawa |
| `Joe Bamberg` | 251 | 1 | 0371-an-interview-with-joe-bamberg |
| `Stephen Craig` | 251 | 3 | 0315-mashuppery-with-mep, 0564-pavlovian-cheapskates, 0670-engineering-careers-with-circ |
| `Ian Danaher` | 248 | 1 | the-amp-hour-87-nascent-nonolith-n |
| `Piotr Ezdintensky` | 244 | 1 | 0356-an-interview-with-piotr-esden |
| `Ted Yapo` | 240 | 1 | 0465-an-interview-with-ted-yapo |
| `Michael Osman` | 235 | 2 | 0214-impedance-matching-with-charv, the-amp-hour-161-gifted-grimgribbe |
| `Arduinos` | 233 | 3 | 0278-our-second-callin-showish, 0293-call-in-show-4, 0390-an-interview-with-sam-zeloof |
| `Eliseo White` | 232 | 1 | 0329-work-on-it-for-10-years |
| `Forbes` | 232 | 1 | 0257-an-interview-with-fabienne-se |
| `Ken Burns` | 230 | 1 | 0458-an-interview-with-ken-burns |
| `Larry Sears` | 228 | 1 | the-amp-hour-109-hexagram-hardware |
| `IoT` | 226 | 1 | 0376-an-interview-with-richard-gin |
| `David Ray` | 224 | 1 | 0716-electronics-manufacturing-his |
| `Forrest Mims` | 223 | 1 | 0171-an-interview-with-forrest-mim |
| `Eric Van Wyk` | 222 | 1 | 0218-an-interview-with-eric-vanwyk |
| `David Kronstein Tesla500` | 219 | 1 | the-amp-hour-325-an-interview-with |
| `Free Electron` | 219 | 1 | 0169-an-interview-with-vincent-him |
| `Musk Sticks` | 215 | 1 | 0680-catching-rockets-with-musk-st |
| `Scotty Allen` | 213 | 1 | 0414-an-interview-with-scotty-alle |
| `Joe Fitzpatrick` | 212 | 1 | 0346-an-interview-with-joe-fitzpat |
| `Michael` | 212 | 2 | 0276-eating-an-elephant, 0577-product-lifecycle-management- |
| `Chris Osterwood` | 209 | 1 | 0425-an-interview-with-chris-oster |
| `Jørgen Jakobsen` | 208 | 1 | 0338-an-interview-with-jorgen-jako |
| `Jonathan Ellis` | 206 | 1 | 0283-an-interview-with-jonathan-el |
| `Matt Berggren` | 206 | 1 | 0471-an-interview-with-matt-berggr |
| `Luke Beno` | 204 | 2 | 0272-an-interview-with-luke-beno-o, 0722-ai-tooling-with-matt-liberty- |
| `Charlie Larrabe` | 202 | 1 | 0572-technology-instruction-with-c |
| `Joe Grand` | 201 | 2 | 0575-new-life-skills-with-joe-gran, the-amp-hour-60-pancyclopaedic-pro |
| `Ethernet` | 198 | 1 | 0674-turtles-as-a-service |
| `Ben Jordan` | 197 | 1 | 0593-publicly-traded-hobby-with-be |
| `Jon Oxer` | 197 | 1 | 0349-another-interview-with-jon-ox |
| `Philip Frieden` | 197 | 1 | the-amp-hour-103-xenodochial-xilin |
| `Daryl Tewksbury` | 196 | 1 | 0521-outdoor-laser-projection-obje |
| `Abraham` | 195 | 1 | the-amp-hour-70-idiorhythmic-ipc-i |
| `Rick Altherr` | 194 | 1 | 0357-an-interview-with-rick-alther |
| `Jeff Geerling` | 190 | 1 | 0651-learning-computing-with-jeff- |
| `Mehdi` | 190 | 1 | 0562-electroboom |
| `Mike Englehart` | 188 | 2 | 0196-an-interview-with-mike-engelh, 0196-an-interview-with-mike-engelh |
| `Scott Shawcroft` | 186 | 1 | 0383-an-interview-with-scott-shawc |
| `Chrissy Meyer` | 185 | 1 | 0437-an-interview-with-chrissy-mey |
| `Vic Apria` | 185 | 1 | 0250-an-interview-with-vic-aprea-f |
| `Starlink` | 184 | 1 | 0518-satellites-and-evs-with-joris |
| `Zach Fredin` | 184 | 1 | 0330-an-interview-with-zach-fredin |
| `Eric Klein` | 183 | 1 | 0495-an-interview-with-eric-klein |
| `Ron Demko` | 183 | 1 | 0596-capacitor-schoopage-with-ron- |
| `Ahmed` | 182 | 1 | 0267-standing-with-ahmed |
| `Carmen` | 182 | 1 | 0566-switching-converter-engineeri |
| `Lee Felsenstein` | 182 | 1 | 0684-lee-felsenstein-the-computer- |
| `Nadia Peek` | 182 | 1 | 0208-an-interview-with-nadya-peek- |
| `Chris White` | 181 | 3 | 0256-is-this-a-show, 0281-crossovers-and-call-ins, 0329-work-on-it-for-10-years |
| `Engadget` | 180 | 1 | 0175-an-interview-with-andrew-witt |
| `Pete Staples` | 180 | 1 | 0544-standardizing-manufacturing-w |
| `Missouri` | 179 | 1 | 0576-a-literal-trainwreck |
| `James Adams` | 178 | 2 | 0648-the-rp1-and-beyond-with-the-r, 0687-the-rp2350-with-the-raspberry |
| `John Day` | 178 | 1 | 0485-an-interview-with-john-day |
| `Mark Morin` | 176 | 1 | 0290-an-interview-with-mark-morin- |
| `Ben Einstein` | 173 | 1 | 0402-an-interview-with-ben-einstei |
| `Chris Church` | 172 | 1 | 0243-an-interview-with-macrofab-ma |
| `Louis Rossmann` | 172 | 2 | 0311-an-interview-with-louis-rossm, the-amp-hour-507-right-to-repair-w |
| `Marcus Schaffe` | 172 | 1 | 0189-an-interview-with-marcus-scha |
| `Trammell Hudson` | 172 | 1 | 0463-an-interview-with-trammell-hu |
| `Dave Taylor` | 171 | 1 | 0180-an-interview-with-dave-taylor |
| `An Hdmi Cable` | 169 | 1 | 0707-welding-with-an-hdmi-cable |
| `Scott Driscoll` | 169 | 1 | 0183-an-interview-with-scott-drisc |
| `Ben Heckendorn` | 166 | 1 | 0490-an-interview-with-ben-heckend |
| `Gerry Roston` | 166 | 1 | 0334-an-interview-with-gerry-rosto |
| `Jason Cerundolo` | 165 | 1 | 0340-an-interview-with-jason-cerun |
| `Bob Davidson` | 164 | 1 | the-amp-hour-144-hoodied-hp-hijink |
| `LTSpice` | 164 | 1 | 0589-mute-button-discipline |
| `Arduino` | 163 | 2 | 0235-an-interview-with-matt-richar, the-amp-hour-43-audacious-arduino- |
| `Jonathan Hirschman Of Pcb` | 163 | 1 | 0299-an-interview-with-jonathan-hi |
| `Davith Roche` | 161 | 1 | 0270-an-interview-with-dafydd-roch |
| `Matt Duff` | 161 | 1 | 0392-an-interview-with-matt-duff |
| `Julia Truchsess` | 160 | 1 | 0424-an-interview-with-julia-truch |
| `Shrouk El Attar` | 160 | 1 | 0549-creative-engineering-with-shr |
| `Barry Marshall` | 159 | 1 | 0709-nobel-prize-winner-dr-barry-m |
| `Colin` | 159 | 1 | 0226-an-interview-with-colin-karpf |
| `Ming Zhang` | 157 | 1 | 0499-discussing-chiplets-with-ming |
| `Dan Esparon` | 156 | 1 | 0679-satellite-design-engineering- |
| `Paul` | 156 | 1 | 0585-return-of-the-trade-show-jedi |
| `Robert Feranec` | 156 | 1 | 0316-an-interview-with-robert-fera |
| `Joe Long` | 153 | 1 | 0420-an-interview-with-joe-long |
| `Kevin Cappucio` | 152 | 1 | 0689-a-jumperless-breadboard-with- |
| `Florin Of Voltlo` | 150 | 1 | 0568-youtube-to-consulting-with-fl |
| `Paul Thompson` | 150 | 1 | 0481-an-interview-with-paul-thomps |
| `Howard Johnson` | 149 | 1 | the-amp-hour-77-winsome-waveform-w |
| `Michael G` | 149 | 1 | 0519-simulating-embedded-hardware- |
| `Ken Shirriff` | 148 | 1 | 0361-an-interview-with-ken-shirrif |
| `Florin Of Voltlog` | 147 | 1 | 0568-youtube-to-consulting-with-fl |
| `Pallav Aggarwal` | 146 | 1 | 0661-blogging-electronics-with-pal |
| `Mike Stisch` | 145 | 1 | 0403-an-interview-with-mike-szczys |
| `Sean` | 145 | 1 | 0501-discussing-the-open-source-pd |
| `Tim Ans` | 145 | 1 | 0501-discussing-the-open-source-pd |
| `Dave Vandenbout` | 143 | 1 | 0181-an-interview-with-dave-vanden |
| `Zach Barth Of Zachtronics` | 143 | 1 | 0332-an-interview-with-zach-barth- |
| `Adam Wolfe` | 142 | 1 | 0167-an-interview-with-adam-wolf-b |
| `Kyle Dumont` | 141 | 1 | 0505-hardware-revision-control-wit |
| `Ben Eater` | 140 | 1 | 0444-an-interview-with-ben-eater |
| `Ben Krasnow 8 Years On` | 139 | 1 | 0480-an-interview-with-ben-krasnow |
| `John Davis` | 139 | 1 | 0385-an-interview-with-john-davis |
| `Matthew Venn` | 139 | 1 | 0616-open-source-tapeout-with-matt |
| `Ryan O'Hara` | 139 | 1 | the-amp-hour-153-keyed-kerfed-kapt |
| `Tim Mithro Ansell` | 138 | 1 | 0375-an-interview-with-tim-mithro- |
| `Joshua And Za` | 137 | 1 | 0611-grad-school-time-capsule-with |
| `Jason Kridner` | 136 | 1 | 0723-beagleboards-back-with-jason- |
| `Matt Venn` | 136 | 1 | 0672-silicon-revolution-with-matt- |
| `Stephen Hawes` | 136 | 1 | 0686-a-benchtop-pick-and-place-wit |
| `Amitabh Shriv` | 134 | 1 | 0618-refrigerators-and-robots-with |
| `Ben Krasnow` | 134 | 1 | the-amp-hour-75-sprauncy-saccadic- |
| `Spencer Wright` | 134 | 1 | 0405-an-interview-with-spencer-wri |
| `Brandon Harris` | 133 | 1 | 0202-an-interview-with-brandon-har |
| `Evin Yanbu` | 131 | 1 | the-amp-hour-95-feracious-fabless- |
| `Steve Liebson` | 131 | 1 | the-amp-hour-99-impavid-ideopraxis |
| `Kent Lundberg` | 130 | 1 | the-amp-hour-119-luculent-linear-l |
| `Andrew Seddo` | 129 | 1 | 0699-circuithub-12-years-later-wit |
| `Jack Gansel` | 129 | 1 | the-amp-hour-54-embedded-elchee-ep |
| `Ron Kwan` | 127 | 1 | the-amp-hour-133-tenacious-transis |
| `Brian Amos` | 125 | 1 | 0581-real-time-operating-systems-w |
| `Bunny` | 124 | 1 | the-amp-hour-84-bunnies-bibelot-bo |
| `Chris Denney` | 124 | 1 | 0411-an-interview-with-chris-denne |
| `Jared Wolff` | 123 | 1 | 0509-cellular-iot-with-jared-wolff |
| `Colin Oflynn` | 122 | 1 | 0552-shouting-at-chips-with-colin- |
| `Charles Alexanian` | 121 | 1 | 0429-an-interview-with-charles-ale |
| `Dmitry Nedospasov` | 121 | 1 | 0303-an-interview-with-dmitry-nedo |
| `Dmitry Netospazov` | 121 | 1 | 0318-impedance-matching-with-micha |
| `Jonathan Beri` | 121 | 1 | 0526-why-iot-is-difficult-with-jon |
| `Matt Brown` | 121 | 1 | 0698-hardware-security-with-matt-b |
| `Timothy Lamb` | 121 | 1 | 0292-an-interview-with-timothy-lam |
| `Trey German` | 121 | 1 | 0212-an-interview-with-trey-german |
| `Anthony Wall` | 120 | 1 | 0579-adc-chip-design-with-anthony- |
| `SPEAKER_03` | 120 | 2 | 0175-an-interview-with-andrew-witt, the-amp-hour-163-ramiform-reciproc |
| `Alvaro` | 119 | 1 | 0614-reunion-impedance-matching-an |
| `Phil's Lab` | 119 | 1 | 0573-mixed-signal-education-with-p |
| `Andrew Seddon` | 117 | 1 | the-amp-hour-131-necessary-network |
| `Eric Bogutin` | 117 | 1 | 0252-an-interview-with-eric-bogati |
| `Josh Datko` | 117 | 1 | 0418-an-interview-with-josh-datko |
| `Leigh Brady` | 117 | 1 | 0588-siloed-engineering-with-leigh |
| `Eric Ries` | 116 | 1 | the-amp-hour-159-transorted-testin |
| `Carrie Sharpglass` | 115 | 1 | 0487-an-interview-with-kerry-schar |
| `Chris Anderson` | 115 | 1 | the-amp-hour-105-deambulatory-daed |
| `Frederick Kinsander` | 115 | 1 | 0522-high-power-supplies-with-fred |
| `Simone Yetsch` | 114 | 1 | 0592-product-design-with-simone-gi |
| `Ian Johnston` | 112 | 1 | 0643-calibration-repair-with-ian-j |
| `Jonathan Oxer` | 112 | 1 | the-amp-hour-123-innoxious-implant |
| `Kotki` | 112 | 1 | 0204-an-interview-with-noah-feehan |
| `Saar Drimer` | 112 | 1 | 0286-an-interview-with-saar-drimer |
| `Sydney` | 112 | 1 | the-amp-hour-61-gallimaufry-gan-ga |
| `Nash Reilly` | 111 | 1 | 0474-an-interview-with-nash-reilly |
| `Alvaro Prieto` | 110 | 1 | 0363-an-interview-with-alvaro-and- |
| `Bluetooth` | 110 | 1 | 0640-software-defined-power-suppli |
| `Brett Fox` | 110 | 1 | the-amp-hour-129-device-doubling-d |
| `Eli Hughes` | 109 | 1 | 0511-brewing-electronics-with-eli- |
| `OpenGL` | 109 | 1 | 0308-an-interview-with-samy-kamkar |
| `Tom Laments` | 109 | 1 | the-amp-hour-93-cacaesthestic-chro |
| `Dave Vandenbaum` | 108 | 1 | 0232-impedance-matching-with-david |
| `Christina Cyr` | 107 | 1 | 0475-an-interview-with-christina-c |
| `Jeff Keyzer` | 107 | 1 | theamphour-82-vecordious-vacation- |
| `Tim Ansell` | 107 | 1 | 0703-building-wafer-space-with-tim |
| `Art Kay` | 106 | 1 | 0348-an-interview-with-art-kay |
| `Michael Ossman` | 106 | 1 | 0198-mike-ossmann-returns-planetic |
| `Werner` | 105 | 1 | 0640-software-defined-power-suppli |
| `Christopher White` | 104 | 1 | 0479-why-isnt-this-working |
| `Asia` | 103 | 1 | the-amp-hour-336-an-interview-with |
| `London` | 103 | 1 | 0266-an-interview-with-ronald-sous |
| `Mohamed Kassem` | 103 | 1 | 0503-fabless-chip-design-with-moha |
| `Jan Rychter` | 102 | 1 | 0542-component-management-with-jan |
| `Adam Mccombs` | 101 | 1 | 0431-an-interview-with-adam-mccomb |
| `Clint Cole Of Digilent` | 101 | 1 | 0302-an-interview-with-clint-cole- |
| `Derek Kozel` | 101 | 1 | 0381-interview-with-derek-kozel |
| `Adam McCombs` | 100 | 1 | 0431-an-interview-with-adam-mccomb |
| `Hank Zumbelan` | 100 | 1 | 0185-an-interview-with-hank-zumbah |
| `Icebreaker FPGA` | 100 | 1 | 0473-an-interview-with-greg-davill |
| `Joe Garrison` | 100 | 1 | 0237-an-interview-with-joe-and-mar |
| `Brandon Gillis` | 99 | 1 | 0517-depth-and-ai-with-brandon-gil |
| `LoRaWAN` | 99 | 1 | 0557-generic-nodes-with-orkhan-ami |
| `Andreas Olofsson` | 98 | 2 | 0254-an-interview-with-andreas-olo, 0650-accessible-asics-with-andreas |
| `Gene` | 98 | 1 | 0448-an-interview-with-jean-rintou |
| `Julia Desmazes` | 98 | 1 | 0721-chip-design-for-fun-and-waffl |
| `Parker Dolman` | 98 | 1 | 0564-pavlovian-cheapskates |
| `Alvaro And Jen From The Ure` | 97 | 1 | 0363-an-interview-with-alvaro-and- |
| `Bluetooth Low Energy` | 97 | 1 | 0232-impedance-matching-with-david |
| `Bob Simpson` | 97 | 1 | the-amp-hour-112-ardent-automotive |
| `Michael Gielda` | 96 | 1 | 0547-open-source-mindset-with-mich |
| `Sergiy Nesterenko` | 96 | 1 | 0626-intelligent-routing-with-serg |
| `Jack Ganssle` | 95 | 1 | 0489-an-interview-with-jack-ganssl |
| `Cnlohr A` | 94 | 1 | 0667-long-distance-with-cnlohr-a |
| `Dean Pick` | 94 | 1 | 0426-an-interview-with-dean-pick |
| `Mighty Home` | 94 | 1 | 0365-wait-why-is-jeff-glowing |
| `Parallela` | 94 | 1 | 0650-accessible-asics-with-andreas |
| `Avidan Ross` | 93 | 1 | 0327-an-interview-with-avidan-ross |
| `Akbar Dinaliwala` | 92 | 1 | 0537-firmware-deployment-and-troub |
| `Joshua Vasquez` | 92 | 1 | 0611-grad-school-time-capsule-with |
| `Katerina Galitskaya` | 92 | 1 | 0678-all-about-antennas-with-kater |
| `Petr Dvorak` | 91 | 1 | 0669-freelance-pcb-design-with-pet |
| `Alex Lidow` | 90 | 1 | 0719-inventing-the-power-mosfet-wi |
| `Laura Abbott` | 90 | 1 | 0590-finding-hardware-flaws-with-l |
| `Raspberry Pi` | 88 | 1 | 0529-embedded-hardware-with-the-ra |
| `Jake Baker` | 87 | 1 | 0297-an-interview-with-jake-baker |
| `Sam Stranks` | 87 | 1 | 0433-an-interview-with-sam-stranks |
| `Stefan Dzisiewski Smith` | 87 | 1 | 0309-an-interview-with-stefan-dzis |
| `Zach Ferdinand` | 87 | 1 | 0611-grad-school-time-capsule-with |
| `Chris Taylor` | 86 | 1 | the-amp-hour-157-efficacious-engin |
| `Jason Kridner And Robert` | 86 | 1 | 0378-an-interview-with-jason-kridn |
| `Andrea Longobardi` | 85 | 1 | 0635-low-power-connected-devices-w |
| `Martin Rowe` | 85 | 1 | 0714-the-measurement-blues-with-ma |
| `Parker Doman` | 85 | 1 | 0243-an-interview-with-macrofab-ma |
| `Brent And Bryce Salmi` | 84 | 1 | 0401-an-interview-with-brent-and-b |
| `Sam Aldah` | 84 | 1 | 0695-making-the-invisible-visible- |
| `Scott Williams` | 84 | 1 | 0645-moving-down-the-stack-with-sc |
| `Michael Ossmann` | 83 | 1 | 0265-a-security-update-with-michae |
| `Tom Lee` | 83 | 1 | 0459-an-interview-with-tom-lee |
| `Uri Shaked Wokwicom` | 83 | 1 | 0599-an-interview-with-uri-shaked- |
| `Sammy Cheung` | 82 | 1 | 0535-efinix-fpgas-with-sammy-cheun |
| `Steve Senge` | 82 | 1 | 0632-steve-sanghi-microchip-ceo-fo |
| `Zach Hoken` | 82 | 1 | the-amp-hour-121-creative-china-co |
| `Philip Johnston` | 81 | 1 | 0556-firmware-for-hardware-enginee |
| `MicroPython` | 80 | 1 | 0323-an-interview-with-tony-dicola |
| `Mitch Altman` | 80 | 1 | the-amp-hour-38-comical-keyzer-com |
| `Ariel Of Cartesian Co` | 79 | 1 | 0260-an-interview-with-ariel-brine |
| `Mike Grover Mg` | 79 | 1 | the-amp-hour-454-mike-grover |
| `Zachariah Peterson` | 77 | 1 | 0718-layout-review-with-zachariah |
| `Pete Bevelaqua` | 76 | 1 | 0446-an-interview-with-pete-bevela |
| `Shawn Hymel` | 76 | 1 | 0675-changing-course-with-shawn-hy |
| `Ed McMahon` | 75 | 1 | the-amp-hour-59-bonafide-beagleboa |
| `Ryan Cousins` | 75 | 1 | 0466-an-interview-with-ryan-cousin |
| `Mark Garrison` | 74 | 1 | 0237-an-interview-with-joe-and-mar |
| `Aedan Cullen` | 73 | 1 | 0638-building-ar-headsets-with-aed |
| `Lukas Henkel` | 73 | 1 | 0681-compact-high-speed-design-wit |
| `Y Combinator` | 73 | 1 | 0268-an-interview-with-luke-iseman |
| `Alan Yates` | 72 | 1 | the-amp-hour-57-recondite-radiatio |
| `Josh Lifton` | 72 | 1 | 0314-an-interview-with-josh-lifton |
| `Colin Kidder` | 71 | 1 | 0388-an-interview-with-earl-sharpe |
| `Bertrand` | 70 | 1 | 0258-an-interview-with-bertrand-an |
| `Bino` | 70 | 1 | 0461-an-interview-with-jonathan-ge |
| `Jeff Roberg` | 70 | 1 | the-amp-hour-155-mini-module-maste |
| `Keith Burzinski` | 70 | 1 | 0657-automating-the-home-with-keit |
| `Super Nintendo` | 70 | 1 | 0467-stories-from-supercon-2019 |
| `AT-Tinny's` | 69 | 1 | the-amp-hour-454-mike-grover |
| `Benjamin Kabe` | 69 | 1 | 0653-benjamin-cabe-nose-zephyr |
| `Bitluni` | 69 | 1 | 0673-lifelong-learning-with-bitlun |
| `Matt Eddis` | 69 | 1 | the-amp-hour-101-quality-quadratur |
| `Shahriar` | 69 | 1 | 0553-debunking-with-shahriar |
| `Parker Dillman` | 68 | 1 | 0315-mashuppery-with-mep |
| `Noah Fian` | 67 | 1 | 0204-an-interview-with-noah-feehan |
| `Peter` | 67 | 1 | 0409-electronics-consultant-impeda |
| `Michael Gieldo` | 66 | 1 | 0691-system-designer-lets-you-try- |
| `Saber Kaygusuz` | 64 | 1 | 0608-vapor-phase-with-saber-kaygus |
| `Gerald Friedland` | 60 | 1 | 0258-an-interview-with-bertrand-an |
| `Michael Zalewski` | 60 | 1 | 0725-the-secret-life-of-circuits-w |
| `Eric Schlepfer` | 58 | 1 | 0609-open-circuits-with-eric-schla |
| `Brock Lameres` | 57 | 1 | 0497-an-interview-with-brock-lamer |
| `Massimo Banzi` | 57 | 1 | the-amp-hour-726-arduinos-invisibl |
| `Aaed Musa` | 56 | 1 | 0712-robots-everywhere-with-aaed-m |
| `Jeroen Domburg Sprite Tm` | 55 | 1 | 0359-an-interview-with-jeroen-domb |
| `Tony Kloppenstein` | 54 | 1 | the-amp-hour-157-efficacious-engin |
| `Eric Migicovsky` | 53 | 1 | 0715-shiny-new-pebble-with-eric-mi |
| `Eric Thompson` | 51 | 1 | 0409-electronics-consultant-impeda |
| `James Lewis` | 51 | 1 | 0670-engineering-careers-with-circ |
| `Wendell Aske` | 51 | 1 | 0609-open-circuits-with-eric-schla |
| `Mark Palmieri` | 49 | 1 | 0711-medical-electronics-education |
| `Liam Fraser` | 48 | 3 | 0529-embedded-hardware-with-the-ra, 0648-the-rp1-and-beyond-with-the-r, 0687-the-rp2350-with-the-raspberry |
| `Scott Miller 2nd` | 48 | 1 | 0451-an-interview-with-scott-mille |
| `Mahesh` | 47 | 1 | 0288-call-in-show-3 |
| `Greg Gage` | 45 | 1 | 0248-an-interview-with-greg-and-ti |
| `Ariel Briner` | 43 | 1 | 0614-reunion-impedance-matching-an |
| `Bill Hurd` | 43 | 1 | 0222-an-interview-with-bil-herd-za |
| `Kieran Oleary` | 43 | 1 | 0452-an-interview-with-kieran-olea |
| `Ray Ozzie Blues Wireless` | 43 | 1 | 0603-an-interview-with-ray-ozzie-b |
| `Alex Haro` | 42 | 1 | 0728-space-age-bluetooth-with-alex |
| `Luke Renn` | 42 | 1 | 0529-embedded-hardware-with-the-ra |
| `Kieran O'Leary` | 41 | 1 | 0492-more-electronics-consultant-i |
| `Paul Stevenson` | 40 | 1 | the-amp-hour-76-fremescent-floccos |
| `Pietro Ezrin-Temsky` | 40 | 1 | 0423-open-fpga-toolchains-at-35c3 |
| `Alex Klimai` | 33 | 1 | 0492-more-electronics-consultant-i |
| `Jesse Vincent` | 33 | 1 | 0450-stories-from-teardown-2019 |
| `Caller` | 26 | 1 | 0307-call-in-show-5 |
| `David Shah` | 26 | 1 | 0423-open-fpga-toolchains-at-35c3 |
| `Jeremiah Gillis` | 26 | 1 | 0492-more-electronics-consultant-i |
| `Chris Boris` | 23 | 1 | 0687-the-rp2350-with-the-raspberry |
| `Zach Archer` | 23 | 1 | 0450-stories-from-teardown-2019 |
| `Piotr Esden-Tempski` | 16 | 1 | 0450-stories-from-teardown-2019 |
| `Andy` | 9 | 1 | the-amp-hour-alteritous-andys-absq |
| `Narrator` | 8 | 3 | 0279-merry-keyzermas, 0368-the-eevblog-sparkgap-generato, 0384-a-will-buy-again |
| `Fabienne Of Knityak` | 7 | 1 | 0257-an-interview-with-fabienne-se |
| `Chris Gammell (sponsored segment)` | 6 | 1 | 0729-the-terahertz-frontier-greg-c |
| `Shannon Parks` | 6 | 1 | 0513-audio-dsp-with-shannon-parks |
| `Bilal` | 5 | 1 | 0514-focus-dammit |
| `Dlj` | 5 | 1 | 0341-all-the-way-with-dlj |
| `Shrouk El Attar (sponsored segment)` | 5 | 1 | 0729-the-terahertz-frontier-greg-c |
| `Intro Voice` | 4 | 1 | 0636-discovering-cursed-connectors |
| `Kendall Castor Perry` | 3 | 1 | 0476-an-interview-with-kendall-cas |
| `Mike` | 3 | 1 | 0367-not-reely-an-issue |
| `Music` | 3 | 1 | the-amp-hour-74-younker-youtube-ya |
| `Oyvian Yanbu` | 3 | 1 | the-amp-hour-95-feracious-fabless- |
| `Screaming Circuits` | 3 | 1 | 0482-shine-a-light |
| `Carl Bugeja` | 2 | 1 | 0663-motors-on-pcbs-with-carl-buge |
| `Philip Salmony` | 2 | 1 | 0573-mixed-signal-education-with-p |
| `Unknown` | 2 | 1 | 0564-pavlovian-cheapskates |
| `Bill` | 1 | 1 | 0455-bill-and-daves-excellent-equi |
| `Brent Of Oshstencils` | 1 | 1 | 0320-an-interview-with-brent-of-os |
| `CNLohr` | 1 | 1 | 0637-ch32v003-fun-with-cnlohr |
| `Craig J Bishop` | 1 | 1 | 0469-an-interview-with-craig-j-bis |
| `Luke Iseman Of Ycombinato` | 1 | 1 | 0268-an-interview-with-luke-iseman |
| `Orkhan Amiraslanov` | 1 | 1 | 0557-generic-nodes-with-orkhan-ami |
| `Remco Stardustite` | 1 | 1 | the-amp-hour-560-high-end-audio-wi |
| `Ronald Sousa Of Hash Defi` | 1 | 1 | 0266-an-interview-with-ronald-sous |
| `Saberkite Use Us` | 1 | 1 | 0608-vapor-phase-with-saber-kaygus |
| `Samy Kamkar` | 1 | 1 | 0308-an-interview-with-samy-kamkar |
| `Sean Meehan` | 1 | 1 | 0220-an-interview-with-shaun-meeha |
| `Voya Antinich` | 1 | 1 | 0247-an-interview-with-voja-antoni |
