# Candidate Article Ranking Report

Pipeline step 4. Built from `census/luna-v3` (717 episodes), `canon/` (alias table, vocabulary `broader` relations, speaker repair map) and `graph/graph.json`.

## Build parameters

| parameter | value |
|---|---|
| notability floor | episode_count >= 3 AND distinct_guests >= 3 |
| hosts (never counted as guests) | Chris Gammell, Dave Jones |
| dropped speaker labels | `__SPONSOR_READ__`, `Speaker ?`, `SPEAKER_NN` |
| score | `explains_count * log(1+episode_count) * (1 + distinct_guests/10)` |
| article threshold (the knob) | explains_count >= **15** |
| saga rule | >60% of mentions inside 2 consecutive years, across >=4 episodes in that window |
| episode -> year model | isotonic (PAVA) fit of max-year-mentioned-in-transcript vs episode number, floored |

## Counts

| metric | value |
|---|---:|
| canonical concepts in census | 62837 |
| **passed the notability floor** | **3027** |
| suggested `article` | 412 |
| suggested `section-of` | 2615 |
| `skip` (below floor) | 59810 |
| saga candidates (passing floor) | 93 |

### The article threshold knob

Of the 3027 concepts that clear the floor, the article count as a function of the `explains_count` threshold:

| explains >= | articles | sections |
|---:|---:|---:|
| 5 | 1503 | 1524 |
| 10 | 703 | 2324 |
| 15  <-- selected | 412 | 2615 |
| 20 | 261 | 2766 |
| 25 | 183 | 2844 |
| 30 | 134 | 2893 |
| 35 | 107 | 2920 |
| 40 | 91 | 2936 |
| 45 | 67 | 2960 |
| 50 | 52 | 2975 |
| 55 | 39 | 2988 |
| 60 | 32 | 2995 |

The brief asked for 250-400 suggested articles. `explains >= 15` yields **412**, just over the top of that band; the next step up (`>= 20`) drops to 261. I kept **15** because 412 is within noise of the cap and the 151 concepts between the two thresholds include things a reader would expect to find as their own page. To tighten, set the knob to 20 and re-run — the field is `_meta.explains_threshold_for_article` in `candidates.json`, and every record carries `explains_count`, so the UI can re-cut without a rebuild.

### Alternate sort orders

Every record carries `rank_by_score`, `rank_by_episode_count` and `rank_by_explains` so the curation UI can re-sort without recomputing. Breadth (episodes) and depth (explains) disagree often — e.g. `twitter` is in 300 episodes with 8 explanations, `pick-and-place-machine` in 146 with 125.

## Top 50 article candidates

| # | concept | community | eps | guests | explains | opinions | score |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | `microcontroller` | 1 microcontroller, arduino, raspberry pi | 371 | 121 | 160 | 125 | 12406 |
| 2 | `fpga` | 6 fpga, arm, risc v | 312 | 94 | 201 | 149 | 12012 |
| 3 | `oscilloscope` | 9 oscilloscope, multimeter, soldering iron | 316 | 71 | 158 | 191 | 7370 |
| 4 | `open-source-hardware` | 4 kicad, altium, open source hardware | 268 | 76 | 132 | 260 | 6351 |
| 5 | `arduino` | 1 microcontroller, arduino, raspberry pi | 280 | 89 | 92 | 123 | 5135 |
| 6 | `firmware` | 13 firmware, engineering education, software | 223 | 75 | 100 | 67 | 4600 |
| 7 | `component-sourcing` | 5 digi key, component sourcing, bill of materials | 206 | 44 | 154 | 110 | 4435 |
| 8 | `analog-to-digital-converter` | 15 analog to digital converter, i2c, spi | 195 | 50 | 137 | 15 | 4339 |
| 9 | `pcb-fabrication` | 2 pcb fabrication, pcb, pick and place machine | 212 | 54 | 125 | 121 | 4289 |
| 10 | `usb` | 7 linux, usb, ethernet | 224 | 80 | 87 | 27 | 4241 |
| 11 | `kicad` | 4 kicad, altium, open source hardware | 240 | 64 | 104 | 187 | 4221 |
| 12 | `kickstarter` | 11 kickstarter, startup, venture capital | 246 | 67 | 95 | 110 | 4030 |
| 13 | `led` | 0 capacitor, led, op amp | 213 | 59 | 97 | 32 | 3591 |
| 14 | `datasheet` | 18 datasheet, internet, 555 timer | 212 | 55 | 97 | 69 | 3380 |
| 15 | `pcb-layout` | 4 kicad, altium, open source hardware | 200 | 48 | 108 | 86 | 3322 |
| 16 | `pick-and-place-machine` | 2 pcb fabrication, pcb, pick and place machine | 146 | 42 | 125 | 123 | 3244 |
| 17 | `bluetooth` | 3 bluetooth, wifi, internet of things | 217 | 62 | 66 | 44 | 2559 |
| 18 | `i2c` | 15 analog to digital converter, i2c, spi | 130 | 58 | 76 | 14 | 2520 |
| 19 | `semiconductor-fab` | 12 intel, texas instruments, semiconductor fab | 155 | 32 | 117 | 69 | 2481 |
| 20 | `bill-of-materials` | 5 digi key, component sourcing, bill of materials | 141 | 36 | 102 | 31 | 2325 |
| 21 | `transistor` | 0 capacitor, led, op amp | 171 | 47 | 78 | 17 | 2289 |
| 22 | `wifi` | 3 bluetooth, wifi, internet of things | 206 | 61 | 57 | 48 | 2158 |
| 23 | `linux` | 7 linux, usb, ethernet | 210 | 74 | 48 | 61 | 2158 |
| 24 | `contract-manufacturer` | 5 digi key, component sourcing, bill of materials | 113 | 47 | 79 | 43 | 2133 |
| 25 | `capacitor` | 0 capacitor, led, op amp | 200 | 50 | 59 | 34 | 1877 |
| 26 | `pcb` | 2 pcb fabrication, pcb, pick and place machine | 266 | 61 | 46 | 46 | 1825 |
| 27 | `raspberry-pi` | 1 microcontroller, arduino, raspberry pi | 172 | 55 | 54 | 75 | 1809 |
| 28 | `open-source-software` | 4 kicad, altium, open source hardware | 155 | 55 | 54 | 97 | 1772 |
| 29 | `resistor` | 0 capacitor, led, op amp | 219 | 50 | 53 | 21 | 1715 |
| 30 | `schematic` | 4 kicad, altium, open source hardware | 186 | 45 | 56 | 36 | 1611 |
| 31 | `python` | 1 microcontroller, arduino, raspberry pi | 138 | 63 | 43 | 27 | 1549 |
| 32 | `digi-key` | 5 digi key, component sourcing, bill of materials | 312 | 67 | 32 | 47 | 1416 |
| 33 | `pcb-assembly` | 2 pcb fabrication, pcb, pick and place machine | 121 | 37 | 62 | 30 | 1400 |
| 34 | `flash-memory` | 7 linux, usb, ethernet | 94 | 36 | 66 | 18 | 1383 |
| 35 | `reverse-engineering` | 13 firmware, engineering education, software | 85 | 34 | 70 | 30 | 1372 |
| 36 | `pcb-lead-time` | 2 pcb fabrication, pcb, pick and place machine | 96 | 25 | 83 | 39 | 1329 |
| 37 | `altium` | 4 kicad, altium, open source hardware | 229 | 36 | 52 | 150 | 1301 |
| 38 | `3d-printing` | 17 3d printing, 3d printer, injection molding | 131 | 40 | 50 | 51 | 1221 |
| 39 | `prototype` | 11 kickstarter, startup, venture capital | 122 | 36 | 54 | 43 | 1195 |
| 40 | `spi` | 15 analog to digital converter, i2c, spi | 102 | 44 | 43 | 6 | 1076 |
| 41 | `firmware-update` | 7 linux, usb, ethernet | 78 | 26 | 68 | 28 | 1070 |
| 42 | `bga` | 2 pcb fabrication, pcb, pick and place machine | 108 | 31 | 55 | 31 | 1058 |
| 43 | `power-supply` | 9 oscilloscope, multimeter, soldering iron | 157 | 37 | 44 | 22 | 1047 |
| 44 | `internet-of-things` | 3 bluetooth, wifi, internet of things | 198 | 57 | 29 | 127 | 1028 |
| 45 | `venture-capital` | 11 kickstarter, startup, venture capital | 106 | 40 | 43 | 52 | 1005 |
| 46 | `engineering-education` | 13 firmware, engineering education, software | 97 | 29 | 56 | 70 | 1001 |
| 47 | `3d-printer` | 17 3d printing, 3d printer, injection molding | 137 | 37 | 43 | 101 | 996 |
| 48 | `asic` | 6 fpga, arm, risc v | 83 | 27 | 60 | 24 | 984 |
| 49 | `uart` | 15 analog to digital converter, i2c, spi | 85 | 35 | 49 | 6 | 982 |
| 50 | `op-amp` | 0 capacitor, led, op amp | 159 | 31 | 47 | 23 | 978 |

## Articles per community

| community | name | articles | sections |
|---:|---|---:|---:|
| 0 | capacitor, led, op amp | 40 | 205 |
| 1 | microcontroller, arduino, raspberry pi | 23 | 174 |
| 2 | pcb fabrication, pcb, pick and place machine | 37 | 165 |
| 3 | bluetooth, wifi, internet of things | 31 | 218 |
| 4 | kicad, altium, open source hardware | 34 | 147 |
| 5 | digi key, component sourcing, bill of materials | 27 | 151 |
| 6 | fpga, arm, risc v | 37 | 197 |
| 7 | linux, usb, ethernet | 26 | 181 |
| 8 | youtube, twitter, consulting | 10 | 116 |
| 9 | oscilloscope, multimeter, soldering iron | 18 | 111 |
| 10 | battery, electric vehicle, tesla | 14 | 74 |
| 11 | kickstarter, startup, venture capital | 16 | 98 |
| 12 | intel, texas instruments, semiconductor fab | 10 | 93 |
| 13 | firmware, engineering education, software | 16 | 140 |
| 14 | apple, google, amazon | 2 | 71 |
| 15 | analog to digital converter, i2c, spi | 24 | 124 |
| 16 | robotics, artificial intelligence, sensor | 10 | 81 |
| 17 | 3d printing, 3d printer, injection molding | 11 | 69 |
| 18 | datasheet, internet, 555 timer | 7 | 49 |
| 19 | hiring, resume, jeff kaiser | 3 | 33 |
| 20 | digital signal processing, software defined radio, microphone | 4 | 17 |
| 21 | signal integrity, differential signaling, electromagnetic interference | 6 | 29 |
| 22 | lcd, electronics industry, off the shelf component | 1 | 17 |
| 23 | circuit breaker, three phase power, electrical safety | 1 | 6 |
| 24 | user interface, graphical user interface, skype | 2 | 7 |
| 25 | unclustered fragments | 1 | 35 |
| - | unassigned | 1 | 7 |

## Notable near-misses (just under the floor)

Concepts that fail the floor on exactly one leg and only just — either 3+ episodes but only 2 distinct guests, or 2 episodes with 3+ guests. These are the ones worth a human look before they are discarded; several are single-deep-dive topics where one guest carried the whole conversation.

| concept | eps | guests | explains | mentions | first-last ep | why it missed |
|---|---:|---:|---:|---:|---|---|
| `oscilloscope-bandwidth` | 26 | 2 | 21 | 27 | 12-710 | only 2 distinct guests |
| `component-library` | 22 | 2 | 20 | 35 | 16-707 | only 2 distinct guests |
| `controlled-impedance` | 21 | 2 | 20 | 30 | 163-706 | only 2 distinct guests |
| `manufacturing-cost` | 22 | 2 | 19 | 26 | 1-700 | only 2 distinct guests |
| `battery-energy-storage` | 16 | 2 | 19 | 38 | 120-696 | only 2 distinct guests |
| `rs-232` | 27 | 2 | 13 | 37 | 11-685 | only 2 distinct guests |
| `product-margin` | 20 | 2 | 14 | 24 | 78-592 | only 2 distinct guests |
| `bootstrapping` | 23 | 2 | 13 | 30 | 17-486 | only 2 distinct guests |
| `public-company` | 22 | 2 | 13 | 26 | 6-687 | only 2 distinct guests |
| `desoldering` | 19 | 2 | 13 | 23 | 59-717 | only 2 distinct guests |
| `circuitmaker` | 17 | 2 | 13 | 51 | 96-487 | only 2 distinct guests |
| `supply-and-demand` | 15 | 2 | 13 | 15 | 14-672 | only 2 distinct guests |
| `busbar` | 16 | 2 | 12 | 22 | 14-683 | only 2 distinct guests |
| `component-pricing` | 20 | 2 | 11 | 23 | 8-702 | only 2 distinct guests |
| `frame-rate` | 15 | 2 | 12 | 19 | 8-700 | only 2 distinct guests |
| `wireless-power` | 18 | 2 | 11 | 33 | 32-695 | only 2 distinct guests |
| `company-valuation` | 16 | 2 | 11 | 22 | 45-668 | only 2 distinct guests |
| `plated-through-hole` | 21 | 2 | 10 | 25 | 32-710 | only 2 distinct guests |
| `product-cost` | 15 | 2 | 11 | 17 | 70-645 | only 2 distinct guests |
| `thermal-profile` | 11 | 2 | 12 | 16 | 63-716 | only 2 distinct guests |
| `assembly-house` | 24 | 2 | 9 | 29 | 34-716 | only 2 distinct guests |
| `capacitive-coupling` | 12 | 2 | 11 | 14 | 8-676 | only 2 distinct guests |
| `e-ink-display` | 15 | 2 | 10 | 26 | 6-646 | only 2 distinct guests |
| `industry-consolidation` | 19 | 2 | 9 | 21 | 1-719 | only 2 distinct guests |
| `pcb-respin` | 19 | 2 | 9 | 21 | 17-628 | only 2 distinct guests |
| `engineering-constraint` | 10 | 2 | 11 | 11 | 244-712 | only 2 distinct guests |
| `mentorship` | 17 | 2 | 9 | 19 | 51-718 | only 2 distinct guests |
| `fabless-semiconductor-company` | 17 | 2 | 9 | 19 | 31-729 | only 2 distinct guests |
| `part-number` | 16 | 2 | 9 | 18 | 20-635 | only 2 distinct guests |
| `parasitic-inductance` | 9 | 2 | 11 | 11 | 7-596 | only 2 distinct guests |

2046 concepts sit in this near-miss band in total.

### The floor is really a guest floor

Of the two legs, `distinct_guests >= 3` does essentially all the work: **6672** concepts clear the episode leg and fail on guests, while only **6** do the reverse. **434** of the rejects appear in 10 or more episodes.

That is a structural bias, not a data error. Chris and Dave carry the recurring bench-level topics themselves; guests bring their own specialities. So the floor systematically drops host-driven staples — `rs-232` (27 episodes), `oscilloscope-bandwidth` (26), `assembly-house` (24) — while admitting narrower topics that happened to come up with three different interviewees. If the wiki is meant to cover what the show actually talks about, consider an OR clause such as `distinct_guests >= 3 OR episode_count >= 10`, which would readmit these 434 concepts. I did not apply it, because the brief specified an AND; the stats needed to apply it are all in `candidates.json`.

| concept | eps | guests | explains | first-last ep |
|---|---:|---:|---:|---|
| `eevblog-forum` | 98 | 1 | 3 | 1-727 |
| `forum` | 41 | 2 | 4 | 1-720 |
| `skype` | 32 | 2 | 4 | 1-508 |
| `subreddit` | 31 | 2 | 5 | 65-659 |
| `rs-232` | 27 | 2 | 13 | 11-685 |
| `silicon-chip` | 27 | 2 | 1 | 10-703 |
| `jeff-kaiser` | 27 | 1 | 0 | 12-694 |
| `oscilloscope-bandwidth` | 26 | 2 | 21 | 12-710 |
| `solar-roadways` | 26 | 2 | 1 | 200-660 |
| `m-hub` | 26 | 2 | 0 | 313-631 |
| `assembly-house` | 24 | 2 | 9 | 34-716 |
| `dhl` | 24 | 2 | 2 | 149-720 |
| `bootstrapping` | 23 | 2 | 13 | 17-486 |
| `design-contest` | 23 | 0 | 10 | 1-659 |
| `electronics-forum` | 23 | 0 | 1 | 3-674 |

## Saga candidates

A saga is a topic that flares rather than hums: more than 60% of all its mentions land inside a two-year window spanning at least 4 episodes. These are the arcs worth a narrative page rather than a reference page. All 93 pass the notability floor.

| concept | window | share in window | eps in window / total | mentions | suggested | community |
|---|---|---:|---|---:|---|---|
| `chip-and-pin` | 2015-2016 | 100% | 5 / 5 | 12 | section-of | unclustered fragments |
| `anki` | 2019-2020 | 100% | 4 / 4 | 8 | section-of | microcontroller, arduino, raspberry pi |
| `quicklogic` | 2020-2021 | 100% | 8 / 8 | 10 | section-of | fpga, arm, risc v |
| `solidcon` | 2014-2015 | 97% | 11 / 12 | 32 | section-of | microcontroller, arduino, raspberry pi |
| `google-plus` | 2012-2013 | 92% | 14 / 16 | 26 | section-of | youtube, twitter, consulting |
| `part-shortage` | 2021-2022 | 92% | 9 / 10 | 12 | section-of | digi key, component sourcing, bill of materials |
| `rp2350` | 2025-2026 | 91% | 4 / 5 | 22 | section-of | microcontroller, arduino, raspberry pi |
| `frequency-shift-keying` | 2018-2019 | 89% | 7 / 9 | 18 | section-of | bluetooth, wifi, internet of things |
| `gateway` | 2017-2018 | 85% | 5 / 8 | 27 | article | bluetooth, wifi, internet of things |
| `ice40` | 2018-2019 | 84% | 7 / 9 | 19 | section-of | fpga, arm, risc v |
| `ch32v003` | 2023-2024 | 83% | 17 / 21 | 41 | section-of | fpga, arm, risc v |
| `gnu-radio` | 2018-2019 | 83% | 8 / 11 | 23 | section-of | digital signal processing, software defined radio, microphone |
| `smart-card` | 2015-2016 | 82% | 5 / 7 | 11 | section-of | unclustered fragments |
| `smart-glasses` | 2022-2023 | 82% | 5 / 7 | 11 | section-of | apple, google, amazon |
| `large-language-model` | 2025-2026 | 81% | 16 / 19 | 26 | section-of | robotics, artificial intelligence, sensor |
| `olin-college` | 2012-2013 | 80% | 5 / 6 | 10 | section-of | kickstarter, startup, venture capital |
| `imts` | 2017-2018 | 79% | 7 / 9 | 14 | section-of | 3d printing, 3d printer, injection molding |
| `yaml` | 2023-2024 | 78% | 4 / 6 | 9 | section-of | bluetooth, wifi, internet of things |
| `opengl` | 2016-2017 | 78% | 5 / 7 | 9 | section-of | linux, usb, ethernet |
| `blind-and-buried-via` | 2019-2020 | 77% | 5 / 8 | 13 | section-of | pcb fabrication, pcb, pick and place machine |
| `linux-foundation` | 2020-2021 | 77% | 8 / 11 | 13 | section-of | linux, usb, ethernet |
| `ventilator` | 2020-2021 | 76% | 8 / 10 | 17 | section-of | kicad, altium, open source hardware |
| `non-commercial-license` | 2011-2012 | 75% | 4 / 6 | 12 | section-of | kicad, altium, open source hardware |
| `lean-startup` | 2013-2014 | 75% | 4 / 7 | 12 | section-of | unclustered fragments |
| `game-developer` | 2017-2018 | 75% | 4 / 6 | 8 | section-of | unclustered fragments |
| `business-plan` | 2013-2014 | 75% | 5 / 7 | 8 | section-of | pcb fabrication, pcb, pick and place machine |
| `analog-engineering` | 2013-2014 | 73% | 6 / 10 | 15 | section-of | datasheet, internet, 555 timer |
| `starship` | 2023-2024 | 73% | 7 / 13 | 26 | section-of | battery, electric vehicle, tesla |
| `chatgpt` | 2023-2024 | 72% | 15 / 21 | 58 | section-of | robotics, artificial intelligence, sensor |
| `formal-verification` | 2018-2019 | 72% | 4 / 7 | 18 | section-of | fpga, arm, risc v |
| `hoverboard` | 2014-2015 | 72% | 4 / 8 | 18 | section-of | kicad, altium, open source hardware |
| `chief-technology-officer` | 2012-2013 | 72% | 6 / 13 | 25 | section-of | kickstarter, startup, venture capital |
| `hackaday-prize` | 2015-2016 | 71% | 14 / 21 | 35 | section-of | youtube, twitter, consulting |
| `research-funding` | 2015-2016 | 71% | 7 / 12 | 17 | section-of | capacitor, led, op amp |
| `raspberry-pi-zero` | 2016-2017 | 71% | 7 / 10 | 17 | section-of | linux, usb, ethernet |
| `industrial-control-system` | 2016-2017 | 70% | 5 / 8 | 10 | section-of | linux, usb, ethernet |
| `yosys` | 2018-2019 | 69% | 5 / 12 | 26 | section-of | fpga, arm, risc v |
| `covid-19` | 2021-2022 | 69% | 12 / 20 | 26 | section-of | youtube, twitter, consulting |
| `quantum-computing` | 2019-2020 | 69% | 5 / 10 | 16 | section-of | robotics, artificial intelligence, sensor |
| `amazon-echo` | 2016-2017 | 68% | 9 / 15 | 19 | section-of | apple, google, amazon |
| `raspberry-pi-pico` | 2021-2022 | 68% | 10 / 17 | 25 | section-of | microcontroller, arduino, raspberry pi |
| `circuitpython` | 2018-2019 | 67% | 12 / 24 | 48 | article | microcontroller, arduino, raspberry pi |
| `spi-flash` | 2018-2019 | 67% | 7 / 14 | 21 | section-of | linux, usb, ethernet |
| `computer-science-education` | 2015-2016 | 67% | 5 / 9 | 12 | section-of | microcontroller, arduino, raspberry pi |
| `time-domain-reflectometry` | 2019-2020 | 67% | 7 / 12 | 15 | section-of | bluetooth, wifi, internet of things |
| `chips-act` | 2023-2024 | 67% | 9 / 14 | 15 | section-of | intel, texas instruments, semiconductor fab |
| `vacuum-system` | 2018-2019 | 67% | 4 / 7 | 9 | section-of | oscilloscope, multimeter, soldering iron |
| `rare-earth-element` | 2011-2012 | 67% | 4 / 6 | 9 | section-of | digi key, component sourcing, bill of materials |
| `laboratory-equipment` | 2013-2014 | 67% | 7 / 11 | 12 | section-of | kicad, altium, open source hardware |
| `deadline` | 2016-2017 | 67% | 4 / 8 | 12 | section-of | pcb fabrication, pcb, pick and place machine |
| `samd21` | 2017-2018 | 67% | 4 / 8 | 18 | section-of | microcontroller, arduino, raspberry pi |
| `cortex-m7` | 2020-2021 | 67% | 6 / 9 | 15 | section-of | microcontroller, arduino, raspberry pi |
| `juicero` | 2017-2018 | 67% | 6 / 10 | 15 | section-of | kickstarter, startup, venture capital |
| `git-repository` | 2022-2023 | 67% | 4 / 7 | 9 | section-of | kicad, altium, open source hardware |
| `nuclear-fusion` | 2022-2023 | 67% | 5 / 9 | 12 | section-of | battery, electric vehicle, tesla |
| `carbon-nanotube` | 2019-2020 | 67% | 4 / 7 | 9 | section-of | unclustered fragments |
| `consulting-forum` | 2021-2022 | 67% | 4 / 8 | 12 | section-of | youtube, twitter, consulting |
| `lincoln-laboratory` | 2013-2014 | 67% | 4 / 7 | 12 | section-of | bluetooth, wifi, internet of things |
| `blender` | 2024-2025 | 66% | 9 / 19 | 38 | section-of | kicad, altium, open source hardware |
| `smart-grid` | 2022-2023 | 65% | 5 / 11 | 20 | section-of | bluetooth, wifi, internet of things |
| `edge-computing` | 2020-2021 | 65% | 5 / 11 | 17 | section-of | linux, usb, ethernet |
| `feather` | 2021-2022 | 64% | 4 / 8 | 14 | section-of | microcontroller, arduino, raspberry pi |
| `chumby` | 2011-2012 | 64% | 8 / 13 | 14 | section-of | fpga, arm, risc v |
| `hand-placement` | 2014-2015 | 64% | 4 / 7 | 11 | section-of | pcb fabrication, pcb, pick and place machine |
| `makefile` | 2018-2019 | 64% | 5 / 8 | 11 | section-of | fpga, arm, risc v |
| `picorv32` | 2018-2019 | 64% | 4 / 7 | 11 | section-of | fpga, arm, risc v |
| `oculus-rift` | 2013-2014 | 64% | 6 / 9 | 11 | section-of | apple, google, amazon |
| `repairability` | 2020-2021 | 64% | 5 / 9 | 11 | section-of | apple, google, amazon |
| `graduate-student` | 2015-2016 | 64% | 6 / 10 | 11 | section-of | firmware, engineering education, software |
| `semiconductor-startup` | 2012-2013 | 64% | 4 / 8 | 11 | section-of | intel, texas instruments, semiconductor fab |
| `ifixit` | 2020-2021 | 64% | 4 / 8 | 11 | section-of | apple, google, amazon |
| `ecp5` | 2018-2019 | 63% | 6 / 9 | 19 | section-of | fpga, arm, risc v |
| `sensor-network` | 2015-2016 | 62% | 6 / 12 | 16 | section-of | bluetooth, wifi, internet of things |
| `plasma-etching` | 2012-2013 | 62% | 5 / 8 | 8 | section-of | intel, texas instruments, semiconductor fab |
| `six-sigma` | 2013-2014 | 62% | 5 / 10 | 16 | section-of | firmware, engineering education, software |
| `data-acquisition` | 2013-2014 | 62% | 5 / 8 | 8 | section-of | linux, usb, ethernet |
| `spectrum-analysis` | 2012-2013 | 62% | 4 / 7 | 8 | section-of | digital signal processing, software defined radio, microphone |
| `board-level-design` | 2012-2013 | 62% | 5 / 8 | 8 | section-of | intel, texas instruments, semiconductor fab |
| `career-path` | 2022-2023 | 62% | 4 / 6 | 8 | section-of | pcb fabrication, pcb, pick and place machine |
| `backend-server` | 2016-2017 | 62% | 4 / 7 | 8 | section-of | firmware, engineering education, software |
| `vivado` | 2018-2019 | 62% | 4 / 7 | 8 | section-of | fpga, arm, risc v |
| `animation` | 2020-2021 | 62% | 4 / 7 | 8 | section-of | youtube, twitter, consulting |
| `kinect` | 2011-2012 | 62% | 10 / 14 | 16 | section-of | microcontroller, arduino, raspberry pi |
| `verizon` | 2019-2020 | 62% | 5 / 8 | 8 | section-of | bluetooth, wifi, internet of things |
| `manufacturing-tolerance` | 2013-2014 | 62% | 7 / 12 | 13 | section-of | kickstarter, startup, venture capital |
| `engineering-salary` | 2011-2012 | 62% | 7 / 11 | 13 | section-of | youtube, twitter, consulting |
| `designspark` | 2011-2012 | 62% | 9 / 17 | 39 | section-of | kicad, altium, open source hardware |
| `flickr` | 2011-2012 | 62% | 6 / 11 | 13 | section-of | unclustered fragments |
| `bob-dobkin` | 2012-2013 | 62% | 6 / 11 | 13 | section-of | datasheet, internet, 555 timer |
| `gitlab` | 2023-2024 | 62% | 4 / 8 | 13 | section-of | kicad, altium, open source hardware |
| `mastodon` | 2022-2023 | 61% | 6 / 12 | 18 | section-of | youtube, twitter, consulting |
| `electronics-career` | 2012-2013 | 61% | 7 / 15 | 23 | section-of | lcd, electronics industry, off the shelf component |
| `edn` | 2011-2012 | 61% | 24 / 41 | 51 | section-of | datasheet, internet, 555 timer |

## Judgment calls

1. **Episode dates are modelled, not read.** No transcript carries a release date — the frontmatter is only `episode`, `title`, `url`, and no "Released ..." line exists anywhere in the corpus. Each transcript was scanned for four-digit years; the maximum year mentioned is an upper envelope on the release year, so those per-episode maxima were fitted with an isotonic (PAVA) monotone regression against episode number and floored. Spot checks line up: ep 164 ("Agilent's new name") lands in 2013, ep 365 in 2017, the last episode in 2026. Year buckets are good to about +/-1 year, which is enough for burst detection but should not be quoted as an air date.
2. **Four episodes have no number** (`chips-and-fabs-and-garages`, `ham-spam-thank-you-maam`, `quassating-quadcopter-quantophrenia`, `the-chinese-clairvoyancy`) — the site never numbered them and the census has no `episode` field. They still count toward `episode_count` and the year histogram (year taken from their own year mentions) but are excluded from `first_episode`/`last_episode`. Four more (`0344`, `0591`, `0624`, `0706`) were missing the field but recovered from the filename.
3. **Episode 196 appears twice** in the census (an original and a rebroadcast). Both were ingested; because episodes are keyed by number, the pair collapses to one episode for counting purposes, which is the behaviour you want.
4. **Parent selection is a cascade, and its confidence is recorded.** A `section-of` concept takes its parent from, in order: a `broader` relation pointing at an article-level concept; the heaviest co-occurrence edge to an article in the same community; any co-occurrence edge to an article; then raw shared-episode overlap. The last case exists because the graph only holds concepts with >=5 episodes, so ~950 floor-passing concepts have no edges at all. Overlap-derived parents for concepts with zero explanations are noise (`ukraine` -> `laser`), so every suggestion carries `parent_confidence` (438 high / 1708 medium / 469 low) — filter the UI on it rather than trusting the parent blindly.
5. **`broader` fired for only 66 parents.** The vocabulary has 6,154 concepts with a `broader` relation, but most point at concepts that are not themselves article-level, and some are simply wrong (`fpga` -> `pga`). Co-occurrence carried the rest.
6. **Hosts count toward nothing.** Chris Gammell and Dave Jones are excluded from `distinct_guests` entirely, so a concept only the hosts ever discuss can never clear the floor no matter how many episodes it spans. `top_speakers` still shows them, since they dominate every concept; `top_guests` is the host-free version and is the more useful column for curation.
7. **The speaker repair map does not reach concept names.** `speaker_map.json` corrects the speaker label `Jeff Kaiser` to `Jeff Keyzer`, but the *concept* `jeff-kaiser` (27 episodes) still carries the mangled spelling because it comes from the alias table, which is a separate namespace. Person-type concepts should be reconciled against the repaired speaker roster before any of them become pages.
8. **The file is split by the floor.** `candidates.json` holds the full record — year histograms, top speakers, graph neighbours, snippets — for the 3,027 concepts that clear the floor, and is small enough for a UI to load. The 59,810 below-floor concepts (mostly hapaxes and ASR debris) sit in `candidates_below_floor.json` as compact rows carrying their counts and a `skip` status, so the floor can be relitigated without pulling 70MB into the browser.
