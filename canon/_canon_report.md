# Canonicalization report — Amp Hour concept census

Source: `census/luna-v3` (717 episodes, 197424 mentions). This layer is additive; no census file was modified.

## Headline

| metric | value |
|---|---|
| raw distinct concept strings | 67311 |
| canonical concepts | 62837 |
| compression | 6.6% fewer entries |
| total mentions (unchanged) | 197424 |
| singleton canonical concepts (1 mention, no alias) | 42937 |
| canonical concepts in >=10 episodes | 2169 |
| `broader` (parent-child) relations recorded | 7112 |

## Pipeline stages

| stage | method | merges |
|---|---|---|
| 1. hygiene | junk `type` values remapped to the canonical 16; leaked `depth` values reset to `mention` | 34 field fixes |
| 2. normalization | case / punctuation / whitespace / unicode fold | folded into stage 3 |
| 3. plural + hyphen variants | deterministic, only when both surface forms observed | 214 plural, 576 hyphen/spacing |
| 4. embedding recall | `text-embedding-3-small`, cosine >= 0.80, all 66,467 x 66,467 pairs | 45387 candidate pairs |
| 5. rule auto-merge | identical stemmed token sequence + compatible type | 343 pairs |
| 6. rule reject | differing digit signature (part numbers) or both-singleton below 0.86 | 11323 pairs |
| 7. acronym recall | deterministic: initials of a multi-word concept matching a 2-6 letter string (embeddings cannot see `pcb` = `printed-circuit-board`) | 4368 extra pairs |
| 8. adjudication | `gpt-5.6-luna`, effort low, 60 pairs/request | 33721 pairs |

An acronym is allowed exactly one expansion: the highest-mention expansion plus any co-expansion that already
clusters with it or is a spelling variant of it. 13 homonym expansions were rejected this way
(`ul` kept `underwriters-laboratories` and rejected `ultraviolet-laser`; `dsp` kept `digital-signal-processor`
and rejected `dual-sided-pcb`; `ac` kept `alternating-current` and rejected four others).

### Data hygiene fixes (all 34)

Junk `type` values (28 mentions) remapped by nearest sensible match:

| junk type | mapped to | mentions |
|---|---|---|
| `logistics` | `industry-economics` | 8 |
| `technology` | `concept-principle` | 4 |
| `material` | `component` | 3 |
| `financial-instrument` | `business-model` | 2 |
| `failure-mode` | `concept-principle` | 1 |
| `legal` | `industry-economics` | 1 |
| `security` | `concept-principle` | 1 |
| `financial?` | `business-model` | 1 |
| `opinion` | `concept-principle` | 1 |
| `chemical` | `component` | 1 |
| `project` | `media-resource` | 1 |
| `infrastructure` | `other` | 1 |
| `systems-integration` | `engineering-practice` | 1 |
| `application` | `concept-principle` | 1 |
| `standards-protocol` | `standard-protocol` | 1 |

Field-leakage in `depth` (6 mentions, all reset to `mention`): `asr_suspect` x2, `company-product` x1, `career` x1, `business-model` x1, `industry-economics` x1

Full per-mention log: `_hygiene_fixes.json`.

## Adjudication

| metric | value |
|---|---|
| pairs sent | 33721 |
| requests | 453 (plus 6573 pairs reused from an earlier round) |
| SAME | 3513 (10%) |
| BROADER (parent-child, not merged) | 7657 (23%) |
| DISTINCT | 22551 (67%) |
| input / output tokens | 1,611,374 / 449,382 |
| cost at $0.20/M in, $1.20/M out | **$0.86** |
| mutual parent-child edges resolved as merges | 5 |
| embedding cost (66,467 strings) | ~$0.01 |

## 50 biggest merge clusters

Eyeball check: each row is one canonical entry and the raw strings folded into it.

| canonical | type | eps | mentions | aliases merged | sample aliases |
|---|---|---|---|---|---|
| `pcb-assembly` | manufacturing | 121 | 158 | 8 | `pcba`, `assembled-pcb`, `pcba-assembly`, `assembled-board`, `preassembled-pcb`, `circuit-board-assembly` |
| `quick-turn-pcb-fabrication` | manufacturing | 16 | 19 | 8 | `fast-turn-pcb`, `quick-turn-pcb`, `rapid-pcb-fabrication`, `rapid-turn-prototype-pcb`, `expedited-pcb-fabrication`, `fast-turn-pcb-fabrication` |
| `design-for-manufacturing` | manufacturing | 80 | 108 | 7 | `dfm`, `design-for-manufacture`, `design-for-manufacturability`, `design-for-manufacturing-assembly`, `design-for-manufacture-and-assembly`, `manufacturing-design-for-production` |
| `evil-mad-scientist` | company-product | 21 | 25 | 7 | `emsl`, `evil-mad-science`, `evil-mad-science-labs`, `evil-mad-scientist-labs`, `evil-man-scientist-labs`, `evil-mad-science-laboratories` |
| `pcb-fabrication` | manufacturing | 212 | 386 | 6 | `pcb-fab`, `pcb-production`, `pcb-manufacturer`, `pcb-manufacturing`, `circuit-board-manufacturing`, `printed-circuit-board-manufacturing` |
| `semiconductor-fab` | manufacturing | 155 | 308 | 6 | `semiconductor-factory`, `semiconductor-production`, `semiconductor-fabrication`, `semiconductor-manufacturing`, `semiconductor-fabrication-plant`, `semiconductor-fabrication-facility` |
| `pcb-design-software` | software | 43 | 55 | 6 | `pcb-cad`, `pcb-design-tool`, `pcb-layout-tool`, `pcb-cad-software`, `pcb-layout-software`, `printed-circuit-board-design-software` |
| `flex-pcb` | component | 33 | 64 | 6 | `fpc`, `flex-circuit`, `flexible-pcb`, `flexible-circuit`, `flexible-circuit-board`, `flexible-printed-circuit` |
| `small-batch-manufacturing` | manufacturing | 28 | 31 | 6 | `micro-manufacturing`, `small-production-run`, `small-run-production`, `small-batch-production`, `small-scale-production`, `small-scale-manufacturing` |
| `fpga-board` | technique | 21 | 35 | 6 | `fpga-prototype`, `fpga-development`, `fpga-programming`, `fpga-prototyping`, `fpga-configuration`, `fpga-development-system` |
| `usb-to-serial-converter` | component | 10 | 11 | 6 | `usb-serial-adapter`, `usb-to-serial-chip`, `usb-serial-converter`, `serial-to-usb-adapter`, `usb-to-serial-adapter`, `usb-to-uart-converter` |
| `pcb-lead-time` | manufacturing | 96 | 131 | 5 | `pcb-order-lead-time`, `pcb-turnaround-time`, `pcb-fabrication-lead-time`, `pcb-fabrication-turnaround`, `pcb-manufacturing-lead-time` |
| `home-battery` | component | 18 | 30 | 5 | `house-battery`, `home-energy-storage`, `home-battery-storage`, `home-storage-battery`, `home-energy-storage-battery` |
| `smart-light-bulb` | component | 11 | 12 | 5 | `smart-bulb`, `connected-light-bulb`, `web-connected-light-bulb`, `internet-connected-led-bulb`, `internet-connected-light-bulb` |
| `wlcsp` | manufacturing | 10 | 17 | 5 | `wcsp`, `wl-csp`, `wlcsp-package`, `wafer-chip-scale-package`, `wafer-level-chip-scale-package` |
| `xilinx-tools` | software | 7 | 7 | 5 | `xilinx-tool`, `xilinx-fpga-tool`, `xilinx-fpga-tools`, `xilinx-tool-suite`, `xilinx-design-tools` |
| `eevblog-forum` | community-event | 98 | 131 | 4 | `eev-forum`, `evblog-forum`, `eavblog-forum`, `eevblog-forums` |
| `firmware-update` | software | 78 | 118 | 4 | `dfu`, `firmware-upgrade`, `device-firmware-update`, `device-firmware-upgrade` |
| `open-hardware-summit` | community-event | 50 | 83 | 4 | `open-hardware-convention`, `open-source-hardware-summit`, `open-source-hardware-conference`, `open-source-hardware-convention` |
| `heat-sink` | component | 41 | 61 | 4 | `heatsink`, `custom-heatsink`, `custom-heat-sink`, `heat-sink-component` |
| `soic` | component | 40 | 44 | 4 | `soic8`, `soic-8`, `soic-package`, `soic-8-package` |
| `build-vs-buy` | business-model | 33 | 36 | 4 | `buy-vs-make`, `make-or-buy`, `make-vs-buy`, `build-versus-buy` |
| `double-sided-pcb` | manufacturing | 25 | 30 | 4 | `two-sided-pcb`, `dual-sided-pcb`, `double-sided-assembly`, `double-sided-pcb-assembly` |
| `counterfeit-component` | manufacturing | 23 | 27 | 4 | `counterfeit-parts`, `component-counterfeit`, `component-counterfeiting`, `counterfeit-electronic-component` |
| `oreilly` | company-product | 19 | 23 | 4 | `O'Reilly`, `o-reilly`, `oreilly-media`, `o-reilly-media` |
| `silicon-fabrication` | manufacturing | 19 | 20 | 4 | `silicon-fab`, `silicon-process`, `silicon-processing`, `silicon-manufacturing` |
| `bare-pcb` | manufacturing | 19 | 19 | 4 | `bareboard`, `blank-pcb`, `bare-board`, `bareboard-pcb` |
| `home-lab` | tool-equipment | 17 | 22 | 4 | `homelab`, `home-based-lab`, `home-laboratory`, `home-based-laboratory` |
| `blinky` | technique | 17 | 18 | 4 | `blinkies`, `blinky-led`, `blinking-led`, `flashing-led` |
| `firmware-programming` | technique | 17 | 17 | 4 | `firmware-upload`, `firmware-flashing`, `firmware-reflashing`, `firmware-reprogramming` |
| `capital-investment` | industry-economics | 16 | 17 | 4 | `capital-funding`, `investor-funding`, `investment-capital`, `investment-funding` |
| `swd` | standard-protocol | 15 | 23 | 4 | `swD`, `serial-wire-debug`, `single-wire-debug`, `one-wire-debug-protocol` |
| `obd2` | standard-protocol | 12 | 19 | 4 | `obd`, `obd-ii`, `onboard-diagnostics`, `on-board-diagnostics` |
| `employee-hiring` | career | 11 | 13 | 4 | `staff-hiring`, `company-recruiting`, `employee-recruiting`, `employee-recruitment` |
| `rebranding` | business-model | 10 | 19 | 4 | `brand-rebranding`, `company-rebranding`, `product-rebranding`, `corporate-rebranding` |
| `electric-bike` | component | 10 | 11 | 4 | `e-bike`, `electronic-bike`, `electric-bicycle`, `electronic-bicycle` |
| `phone-camera` | component | 9 | 12 | 4 | `camera-phone`, `mobile-camera`, `cell-phone-camera`, `mobile-phone-camera` |
| `audio-mixer` | tool-equipment | 7 | 8 | 4 | `audio-console`, `mixing-console`, `audio-mixing-board`, `audio-mixing-console` |
| `pcb-warping` | manufacturing | 7 | 7 | 4 | `pcb-warp`, `pcb-warpage`, `board-warpage`, `board-warping` |
| `sensor-chip` | component | 6 | 7 | 4 | `sensing-chip`, `on-chip-sensor`, `sensor-on-chip`, `sensor-as-a-chip` |
| `zach-smith` | person | 6 | 7 | 4 | `zach-hoken`, `zach-hocken`, `zach-hokensmith`, `zach-hoken-smith` |
| `electronics-retail-store` | company-product | 6 | 6 | 4 | `electronic-store`, `electronics-shop`, `electronics-store`, `retail-electronics-store` |
| `seven-nanometer-process` | manufacturing | 6 | 6 | 4 | `seven-nanometer`, `7-nanometer-process`, `7-nanometer-process-node`, `seven-nanometer-process-node` |
| `wifi-hotspot` | standard-protocol | 6 | 6 | 4 | `wi-fi-hotspot`, `mobile-hotspot`, `wireless-hotspot`, `mobile-internet-hotspot` |
| `analog-fab` | manufacturing | 5 | 5 | 4 | `analog-fabrication`, `analog-semiconductor-fab`, `analog-device-fabrication`, `analog-semiconductor-fabrication` |
| `schematic` | media-resource | 186 | 236 | 3 | `circuit-diagram`, `circuit-schematic`, `schematic-diagram` |
| `bga` | component | 108 | 187 | 3 | `bga-package`, `ball-grid-array`, `ball-grid-array-package` |
| `cad` | software | 77 | 92 | 3 | `computer-aided-design`, `computer-aided-design-tool`, `computer-aided-design-software` |
| `battery-life` | concept-principle | 69 | 99 | 3 | `battery-runtime`, `battery-lifespan`, `battery-longevity` |
| `hewlett-packard` | company-product | 68 | 95 | 3 | `hp`, `hectlett-packard`, `he तेwlett-packard` |

## Top 100 canonical concepts by episode count

| # | canonical | type | episodes | mentions | aliases |
|---|---|---|---|---|---|
| 1 | `microcontroller` | component | 371 | 687 | 2 |
| 2 | `oscilloscope` | tool-equipment | 316 | 822 | 0 |
| 3 | `fpga` | component | 312 | 767 | 1 |
| 4 | `digi-key` | company-product | 312 | 599 | 1 |
| 5 | `twitter` | software | 300 | 526 | 0 |
| 6 | `arduino` | component | 280 | 653 | 1 |
| 7 | `open-source-hardware` | community-event | 268 | 595 | 1 |
| 8 | `pcb` | component | 266 | 387 | 2 |
| 9 | `youtube` | media-resource | 262 | 471 | 0 |
| 10 | `kickstarter` | company-product | 246 | 701 | 1 |
| 11 | `kicad` | software | 241 | 679 | 0 |
| 12 | `altium` | software | 229 | 606 | 1 |
| 13 | `texas-instruments` | company-product | 225 | 386 | 1 |
| 14 | `usb` | standard-protocol | 224 | 372 | 0 |
| 15 | `firmware` | software | 223 | 383 | 1 |
| 16 | `resistor` | component | 219 | 324 | 0 |
| 17 | `bluetooth` | standard-protocol | 217 | 365 | 1 |
| 18 | `led` | component | 213 | 338 | 1 |
| 19 | `datasheet` | media-resource | 213 | 331 | 1 |
| 20 | `pcb-fabrication` | manufacturing | 212 | 386 | 6 |
| 21 | `linux` | software | 210 | 369 | 0 |
| 22 | `wifi` | standard-protocol | 206 | 351 | 1 |
| 23 | `component-sourcing` | manufacturing | 206 | 314 | 2 |
| 24 | `pcb-layout` | technique | 200 | 313 | 2 |
| 25 | `capacitor` | component | 200 | 270 | 0 |
| 26 | `internet-of-things` | concept-principle | 198 | 384 | 1 |
| 27 | `analog-to-digital-converter` | component | 195 | 315 | 2 |
| 28 | `schematic` | media-resource | 186 | 236 | 3 |
| 29 | `multimeter` | tool-equipment | 183 | 356 | 0 |
| 30 | `raspberry-pi` | component | 172 | 374 | 0 |
| 31 | `transistor` | component | 172 | 260 | 0 |
| 32 | `intel` | company-product | 170 | 278 | 0 |
| 33 | `apple` | company-product | 162 | 254 | 0 |
| 34 | `op-amp` | component | 159 | 242 | 0 |
| 35 | `power-supply` | component | 157 | 225 | 0 |
| 36 | `google` | company-product | 156 | 245 | 0 |
| 37 | `semiconductor-fab` | manufacturing | 155 | 308 | 6 |
| 38 | `open-source-software` | software | 155 | 226 | 1 |
| 39 | `pick-and-place-machine` | tool-equipment | 146 | 426 | 1 |
| 40 | `soldering` | technique | 145 | 200 | 0 |
| 41 | `ebay` | company-product | 144 | 228 | 2 |
| 42 | `bill-of-materials` | manufacturing | 141 | 215 | 1 |
| 43 | `software` | software | 140 | 177 | 0 |
| 44 | `adafruit` | company-product | 139 | 212 | 0 |
| 45 | `python` | software | 138 | 240 | 0 |
| 46 | `3d-printer` | tool-equipment | 137 | 291 | 2 |
| 47 | `battery` | component | 137 | 200 | 0 |
| 48 | `contextual-electronics` | company-product | 135 | 186 | 1 |
| 49 | `amazon` | company-product | 134 | 201 | 0 |
| 50 | `3d-printing` | manufacturing | 131 | 227 | 1 |
| 51 | `sensor` | component | 131 | 160 | 0 |
| 52 | `i2c` | standard-protocol | 130 | 213 | 1 |
| 53 | `radio-frequency` | concept-principle | 130 | 176 | 1 |
| 54 | `eagle` | software | 129 | 275 | 1 |
| 55 | `sparkfun` | company-product | 125 | 215 | 1 |
| 56 | `arm` | component | 125 | 203 | 0 |
| 57 | `github` | software | 125 | 202 | 0 |
| 58 | `startup` | business-model | 124 | 192 | 1 |
| 59 | `test-equipment` | tool-equipment | 122 | 188 | 1 |
| 60 | `prototype` | manufacturing | 122 | 160 | 0 |
| 61 | `microchip` | company-product | 121 | 202 | 2 |
| 62 | `mouser` | company-product | 121 | 168 | 1 |
| 63 | `pcb-assembly` | manufacturing | 121 | 158 | 8 |
| 64 | `maker-faire` | community-event | 119 | 299 | 0 |
| 65 | `hackaday` | media-resource | 116 | 159 | 1 |
| 66 | `contract-manufacturer` | manufacturing | 113 | 197 | 2 |
| 67 | `soldering-iron` | tool-equipment | 110 | 147 | 0 |
| 68 | `ethernet` | standard-protocol | 109 | 148 | 0 |
| 69 | `bga` | component | 108 | 187 | 3 |
| 70 | `internet` | standard-protocol | 108 | 126 | 0 |
| 71 | `venture-capital` | industry-economics | 106 | 181 | 0 |
| 72 | `development-board` | component | 106 | 147 | 2 |
| 73 | `embedded-system` | component | 104 | 159 | 1 |
| 74 | `reddit` | community-event | 103 | 148 | 0 |
| 75 | `tesla` | company-product | 102 | 182 | 1 |
| 76 | `spi` | standard-protocol | 102 | 150 | 1 |
| 77 | `integrated-circuit` | component | 102 | 137 | 1 |
| 78 | `pcb-design` | technique | 102 | 134 | 0 |
| 79 | `analog-devices` | company-product | 101 | 160 | 1 |
| 80 | `iphone` | component | 99 | 139 | 0 |
| 81 | `eevblog-forum` | community-event | 98 | 131 | 4 |
| 82 | `artificial-intelligence` | software | 97 | 201 | 1 |
| 83 | `engineering-education` | career | 97 | 139 | 0 |
| 84 | `crowdfunding` | business-model | 96 | 170 | 1 |
| 85 | `pcb-lead-time` | manufacturing | 96 | 131 | 5 |
| 86 | `eevblog` | company-product | 95 | 118 | 0 |
| 87 | `flash-memory` | component | 94 | 160 | 0 |
| 88 | `patent` | company-product | 94 | 150 | 0 |
| 89 | `gerber` | standard-protocol | 94 | 144 | 1 |
| 90 | `camera` | component | 94 | 131 | 0 |
| 91 | `silicon` | component | 93 | 105 | 0 |
| 92 | `robotics` | technique | 92 | 148 | 0 |
| 93 | `antenna` | component | 91 | 135 | 0 |
| 94 | `samsung` | company-product | 90 | 116 | 0 |
| 95 | `smartphone` | component | 89 | 123 | 0 |
| 96 | `facebook` | company-product | 88 | 107 | 0 |
| 97 | `windows` | software | 87 | 137 | 0 |
| 98 | `risc-v` | component | 86 | 230 | 0 |
| 99 | `android` | software | 86 | 127 | 0 |
| 100 | `tsmc` | company-product | 86 | 120 | 2 |

## Parent-child (`broader`) relations

7112 relations recorded on 6154 concepts. These are deliberately NOT merged; they feed the graph layer.

| narrower | broader |
|---|---|
| `fpga` | `pga` |
| `pcb-layout` | `circuit-board-design`, `circuit-layout`, `pcb-design` |
| `open-source-software` | `open-source`, `open-source-product` |
| `pick-and-place-machine` | `pick-and-place` |
| `microchip` | `microcontroller` |
| `pcb-assembly` | `pcb-fabrication` |
| `pcb-design` | `pcb-engineering` |
| `pcb-lead-time` | `hardware-lead-time`, `manufacturing-lead-time` |
| `robotics` | `robotic-automation` |
| `tsmc` | `taiwan-manufacturing` |
| `hand-soldering` | `solder-process`, `soldering`, `soldering-technique` |
| `asic` | `specialized-integrated-circuit` |
| `design-for-manufacturing` | `design-for-production` |
| `pic-microcontroller` | `microchip`, `microcontroller`, `single-chip-microcontroller` |
| `solar-panel` | `photovoltaic` |
| `battery-life` | `battery-performance` |
| `dc-dc-converter` | `dc-converter` |
| `switching-power-supply` | `switching-converter` |
| `mobile-phone` | `cellular-device`, `mobile-device` |
| `user-interface` | `software-interface` |
| `online-forum` | `public-forum` |
| `component-obsolescence` | `product-obsolescence` |
| `startup-funding` | `business-financing` |
| `analog-electronics` | `analog-technology` |
| `profit-margin` | `business-margin` |
| `reflow-soldering` | `solder-melting`, `solder-paste-application` |
| `open-hardware-summit` | `embedded-open-source-summit`, `open-source-conference` |
| `cnc-machine` | `cnc` |
| `quadcopter` | `multicopter` |
| `pcb-routing` | `pcb-layout` |

## Long tail

| mentions | canonical concepts |
|---|---|
| 1 | 42937 |
| 2-4 | 13395 |
| 5-19 | 5261 |
| 20-99 | 1090 |
| 100+ | 154 |

Singletons are kept as-is and carry `low_confidence: true`. Concepts whose mentions came from ASR-suspect
strings carry `asr_suspect_mentions > 0` (292 concepts).

## Sanity checks

- every one of the 67311 raw strings appears as a key in `alias_table.json`: PASS
- no alias chains (every value maps to itself): PASS
- no `broader` cycles or dangling targets: PASS
- mention totals preserved (197424 in, 197424 out): PASS
- every alias target exists in `vocabulary.json`: PASS

