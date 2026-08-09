# Amp Hour concept census — luna-v3 production run

Model `gpt-5.6-luna`, reasoning effort `low`, prompt `census_prompt_v3_chunk.md`, 40-paragraph chunks with 1-paragraph overlap.

## Totals

| metric | value |
|---|---|
| episodes | 717 |
| chunks | 6585 |
| mentions kept | 197424 |
| raw mentions returned | 218202 |
| rejected (snippet not found / bad index / malformed) | 17851 (8.18%) |
| overlap duplicates dropped | 2927 |
| distinct concepts | 67311 |
| failed chunks (no usable JSON) | 26 |
| suspect-sparse chunks | 4 |
| chunk retries | 537 |

Reject breakdown: 17845 snippet-not-found, 6 bad-paragraph-index, 0 malformed.

Every kept mention's `char_start` is computed by locating its snippet inside the paragraph it names, so offset validity is 100% by construction. 3418 kept mentions (1.73%) carry a `context_snippet` longer than the spec's 100-character limit — the merge keeps them, exactly as the bake-off did, but a downstream trim pass should shorten them.

## Cost and time

| metric | value |
|---|---|
| input tokens | 61,276,728 |
| output tokens | 12,665,024 (of which 2,053,028 reasoning) |
| cost at $0.20/M in, $1.20/M out | **$27.45** |
| wall time | 13.6 min |
| cost per episode | $0.0383 |

## Depth and type mix

Depth: `mention` 95428 (48.3%), `explains` 65900 (33.4%), `opinion` 36090 (18.3%), `asr_suspect` 2 (0.0%), `company-product` 1 (0.0%), `career` 1 (0.0%), `business-model` 1 (0.0%), `industry-economics` 1 (0.0%)

Type: `component` 39189 (19.9%), `company-product` 24917 (12.6%), `software` 18899 (9.6%), `technique` 18640 (9.4%), `manufacturing` 14705 (7.4%), `concept-principle` 13340 (6.8%), `tool-equipment` 12487 (6.3%), `business-model` 9266 (4.7%), `standard-protocol` 8729 (4.4%), `career` 7498 (3.8%), `media-resource` 6984 (3.5%), `community-event` 6270 (3.2%), `engineering-practice` 6003 (3.0%), `industry-economics` 5430 (2.8%), `person` 3599 (1.8%), `other` 1440 (0.7%), `logistics` 8 (0.0%), `technology` 4 (0.0%), `material` 3 (0.0%), `financial-instrument` 2 (0.0%), `failure-mode` 1 (0.0%), `security` 1 (0.0%), `legal` 1 (0.0%), `financial?` 1 (0.0%), `opinion` 1 (0.0%), `chemical` 1 (0.0%), `project` 1 (0.0%), `infrastructure` 1 (0.0%), `systems-integration` 1 (0.0%), `application` 1 (0.0%), `standards-protocol` 1 (0.0%)

## Mentions per 1000 words

Bake-off band was 10.8-21.6 mentions/1000 words.

| statistic | value |
|---|---|
| min | 3.6 |
| p10 | 12.1 |
| median | 18.6 |
| p90 | 23.9 |
| max | 33.3 |
| mean | 18.3 |
| in band | 501 / 717 (69.9%) |
| below band | 43 |
| above band | 173 |

Ten thinnest episodes (mentions/1000 words):

- `0317-a-decoupled-episode` — 3.6 (50 mentions, 13882 words)
- `0401-an-interview-with-brent-and-bryce-salmi` — 4.8 (128 mentions, 26653 words)
- `0420-an-interview-with-joe-long` — 5.0 (118 mentions, 23585 words)
- `0443-an-interview-with-jp-norair` — 5.1 (72 mentions, 14171 words)
- `0476-an-interview-with-kendall-castor-perry` — 5.3 (91 mentions, 17031 words)
- `0266-an-interview-with-ronald-sousa-of-hash-define-electronics` — 6.5 (125 mentions, 19294 words)
- `0402-an-interview-with-ben-einstein` — 6.6 (154 mentions, 23296 words)
- `0603-an-interview-with-ray-ozzie-blues-wireless` — 6.9 (92 mentions, 13365 words)
- `0699-circuithub-12-years-later-with-andrew-seddon` — 7.1 (125 mentions, 17629 words)
- `0452-an-interview-with-kieran-oleary` — 7.2 (125 mentions, 17334 words)

## Top 50 concepts by raw frequency

| # | concept | mentions | episodes |
|---|---|---|---|
| 1 | `oscilloscope` | 822 | 316 |
| 2 | `kickstarter` | 700 | 246 |
| 3 | `microcontroller` | 684 | 369 |
| 4 | `kicad` | 679 | 241 |
| 5 | `fpga` | 661 | 278 |
| 6 | `arduino` | 652 | 280 |
| 7 | `altium` | 604 | 229 |
| 8 | `open-source-hardware` | 540 | 261 |
| 9 | `twitter` | 526 | 300 |
| 10 | `youtube` | 471 | 262 |
| 11 | `pick-and-place-machine` | 425 | 145 |
| 12 | `firmware` | 382 | 223 |
| 13 | `digi-key` | 378 | 233 |
| 14 | `texas-instruments` | 377 | 219 |
| 15 | `raspberry-pi` | 374 | 172 |
| 16 | `usb` | 372 | 224 |
| 17 | `linux` | 369 | 210 |
| 18 | `bluetooth` | 364 | 217 |
| 19 | `multimeter` | 356 | 183 |
| 20 | `internet-of-things` | 325 | 175 |
| 21 | `resistor` | 324 | 219 |
| 22 | `led` | 322 | 207 |
| 23 | `datasheet` | 320 | 210 |
| 24 | `component-sourcing` | 310 | 204 |
| 25 | `pcb-layout` | 307 | 197 |
| 26 | `maker-faire` | 299 | 119 |
| 27 | `intel` | 278 | 170 |
| 28 | `eagle` | 274 | 129 |
| 29 | `3d-printer` | 272 | 129 |
| 30 | `capacitor` | 270 | 200 |
| 31 | `transistor` | 260 | 172 |
| 32 | `apple` | 254 | 162 |
| 33 | `pcb-fabrication` | 254 | 152 |
| 34 | `google` | 245 | 156 |
| 35 | `op-amp` | 242 | 159 |
| 36 | `python` | 240 | 138 |
| 37 | `risc-v` | 230 | 86 |
| 38 | `schematic` | 228 | 179 |
| 39 | `power-supply` | 225 | 157 |
| 40 | `open-source-software` | 225 | 154 |
| 41 | `ebay` | 222 | 142 |
| 42 | `digikey` | 221 | 146 |
| 43 | `analog-to-digital-converter` | 216 | 146 |
| 44 | `sparkfun` | 214 | 125 |
| 45 | `adafruit` | 212 | 139 |
| 46 | `i2c` | 212 | 130 |
| 47 | `3d-printing` | 205 | 118 |
| 48 | `arm` | 203 | 125 |
| 49 | `github` | 202 | 125 |
| 50 | `amazon` | 201 | 134 |

## Top 50 concepts by episode spread

| # | concept | episodes | mentions |
|---|---|---|---|
| 1 | `microcontroller` | 369 | 684 |
| 2 | `oscilloscope` | 316 | 822 |
| 3 | `twitter` | 300 | 526 |
| 4 | `arduino` | 280 | 652 |
| 5 | `fpga` | 278 | 661 |
| 6 | `youtube` | 262 | 471 |
| 7 | `open-source-hardware` | 261 | 540 |
| 8 | `kickstarter` | 246 | 700 |
| 9 | `kicad` | 241 | 679 |
| 10 | `digi-key` | 233 | 378 |
| 11 | `altium` | 229 | 604 |
| 12 | `usb` | 224 | 372 |
| 13 | `firmware` | 223 | 382 |
| 14 | `texas-instruments` | 219 | 377 |
| 15 | `resistor` | 219 | 324 |
| 16 | `bluetooth` | 217 | 364 |
| 17 | `datasheet` | 210 | 320 |
| 18 | `linux` | 210 | 369 |
| 19 | `led` | 207 | 322 |
| 20 | `component-sourcing` | 204 | 310 |
| 21 | `capacitor` | 200 | 270 |
| 22 | `pcb-layout` | 197 | 307 |
| 23 | `multimeter` | 183 | 356 |
| 24 | `schematic` | 179 | 228 |
| 25 | `internet-of-things` | 175 | 325 |
| 26 | `transistor` | 172 | 260 |
| 27 | `raspberry-pi` | 172 | 374 |
| 28 | `intel` | 170 | 278 |
| 29 | `apple` | 162 | 254 |
| 30 | `op-amp` | 159 | 242 |
| 31 | `power-supply` | 157 | 225 |
| 32 | `google` | 156 | 245 |
| 33 | `pcb` | 154 | 198 |
| 34 | `open-source-software` | 154 | 225 |
| 35 | `pcb-fabrication` | 152 | 254 |
| 36 | `printed-circuit-board` | 147 | 185 |
| 37 | `digikey` | 146 | 221 |
| 38 | `analog-to-digital-converter` | 146 | 216 |
| 39 | `soldering` | 145 | 200 |
| 40 | `pick-and-place-machine` | 145 | 425 |
| 41 | `ebay` | 142 | 222 |
| 42 | `software` | 140 | 177 |
| 43 | `adafruit` | 139 | 212 |
| 44 | `python` | 138 | 240 |
| 45 | `battery` | 137 | 200 |
| 46 | `contextual-electronics` | 135 | 185 |
| 47 | `amazon` | 134 | 201 |
| 48 | `sensor` | 131 | 160 |
| 49 | `i2c` | 130 | 212 |
| 50 | `eagle` | 129 | 274 |

## Long tail

- 67311 distinct concepts total
- 46578 (69.2%) appear exactly once in the whole corpus
- 2059 appear in 10 or more episodes
- median distinct concepts per episode: 220

## Failures and suspect chunks

Episodes with chunks that never returned usable JSON:

- `0174-motors-and-upgrading-sinclairs` — chunks [6]
- `0193-were-sorry-but-apple-aint-remorseless-ram-racketeering` — chunks [4]
- `0224-meracious-mike-manuduction` — chunks [4]
- `0244-the-art-of-staying-interested-in-electronics-exponible-electronics-ennui` — chunks [1]
- `0266-an-interview-with-ronald-sousa-of-hash-define-electronics` — chunks [3]
- `0269-be-tidy` — chunks [8]
- `0298-dont-turn-it-on-dont-take-it-apart` — chunks [7]
- `0320-an-interview-with-brent-of-oshstencils` — chunks [2]
- `0344-back-into-the-swing-of-things` — chunks [0]
- `0382-the-toggle-boggle` — chunks [5]
- `0420-an-interview-with-joe-long` — chunks [1]
- `0453-vertically-integrated-design-engineering` — chunks [4]
- `0520-inductance-and-stuff` — chunks [6]
- `0527-measuring-current-with-matt-liberty` — chunks [4]
- `0531-footprints-and-symbols-with-natasha-baker` — chunks [4]
- `0546-thousands-of-dependencies` — chunks [5]
- `0558-toasted-marshmallow-connectors` — chunks [4]
- `0591-olive-a-the-world` — chunks [0]
- `0623-artisanal-crystals` — chunks [5]
- `0624-design-manufacturing-consulting-with-scott-williams-from-xentronics` — chunks [0]
- `0706-leading-edge-analog-with-joren-vaes` — chunks [0]
- `the-amp-hour-124-urging-unemployment-ullagone` — chunks [7]
- `the-amp-hour-132-vacuuous-vortex-verification` — chunks [6]
- `the-amp-hour-445-ludicrously-high-frequency-interference` — chunks [5]
- `the-amp-hour-9-from-boston-in-boxers` — chunks [4]
- `theamphour-82-vecordious-vacation-variorum` — chunks [4]

Suspect-sparse chunks (returned zero mentions twice over a >10-paragraph span):

- `0253-consolidate-all-the-things-zonked-zelotic-zaitech` — chunks [11]
- `0312-aussie-bound` — chunks [9]
- `the-amp-hour-30-funding-fusion-is-not-futile` — chunks [9]
- `the-amp-hour-51-vafrous-video-vaniloquence` — chunks [10]

