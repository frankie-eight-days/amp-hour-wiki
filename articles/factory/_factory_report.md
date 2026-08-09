# Factory prep report — evidence bundles

Generated 2026-08-08 from `census/union` (717 episodes) for the 412 `status=article` concepts in `articles/candidates.json`.

## Method

For each article concept the evidence cluster is: the concept plus every alias that canonicalises to it (core); every concept whose suggested parent is it (children); and every graph co-occurrence neighbour with edge weight ≥ 4 whose own status is not `article` (neighbours). Core passages are kept unconditionally; child and neighbour passages are kept only when the ±1 paragraph window carries a lexical hit for the concept itself, so borrowed material has to actually be about the subject. Passages are `explains` or `opinion` depth only, deduplicated per (episode, paragraph), capped at 250 with all `explains` first and `opinion` filled in by speaker diversity then recency.

## Totals

| Metric | Value |
| --- | --- |
| bundles | 412 |
| passages total | 30109 |
| passages available pre cap | 32575 |
| passages median | 49.0 |
| passages mean | 73.1 |
| passages min | 16 |
| passages max | 250 |
| capped bundles | 17 |
| thin risk bundles | 0 |
| gate relaxed bundles | 0 |
| episodes covered union | 709 |
| passages with unreliable attribution | 3054 |
| bundle bytes total | 89553466 |

## Bundle size distribution (passages)

| Passages | Bundles |
| --- | --- |
| 0-9 | 0 |
| 10-24 | 22 |
| 25-49 | 185 |
| 50-99 | 122 |
| 100-149 | 38 |
| 150-199 | 18 |
| 200-249 | 10 |
| 250+ | 17 |

## Biggest 15 (by evidence available before the cap)

| Concept | Passages kept | Available | Episodes | Children | Neighbours |
| --- | --- | --- | --- | --- | --- |
| fpga | 250 | 690 | 327 | 59 | 19 |
| open-source-hardware | 250 | 572 | 312 | 23 | 22 |
| microcontroller | 250 | 494 | 413 | 48 | 32 |
| oscilloscope | 250 | 486 | 330 | 36 | 18 |
| arduino | 250 | 448 | 316 | 64 | 25 |
| kicad | 250 | 434 | 242 | 22 | 31 |
| altium | 250 | 410 | 240 | 33 | 24 |
| kickstarter | 250 | 403 | 261 | 44 | 20 |
| component-sourcing | 250 | 397 | 263 | 17 | 10 |
| pcb-fabrication | 250 | 367 | 266 | 20 | 9 |
| pick-and-place-machine | 250 | 348 | 152 | 20 | 11 |
| firmware | 250 | 325 | 278 | 31 | 7 |
| usb | 250 | 279 | 271 | 23 | 9 |
| pcb-layout | 250 | 279 | 229 | 11 | 6 |
| semiconductor-fab | 250 | 270 | 176 | 27 | 9 |

## Smallest 15

| Concept | Passages | Episodes | Explains | Opinions |
| --- | --- | --- | --- | --- |
| standard-cell | 16 | 10 | 15 | 1 |
| multiplexer | 18 | 20 | 18 | 0 |
| crosstalk | 18 | 11 | 16 | 2 |
| netlist | 19 | 19 | 18 | 1 |
| differential-signaling | 19 | 20 | 19 | 1 |
| bond-wire | 19 | 20 | 18 | 1 |
| flip-flop | 20 | 39 | 18 | 2 |
| current-source | 20 | 25 | 20 | 2 |
| ohms-law | 21 | 37 | 17 | 4 |
| bitstream | 21 | 21 | 20 | 1 |
| beamforming | 21 | 19 | 21 | 0 |
| ism-band | 21 | 19 | 19 | 2 |
| programmable-logic-controller | 21 | 15 | 19 | 2 |
| lookup-table | 22 | 27 | 21 | 1 |
| pll | 23 | 35 | 21 | 3 |

## Capped bundles (17)

| Concept | Kept | Available | Discarded |
| --- | --- | --- | --- |
| fpga | 250 | 690 | 440 |
| open-source-hardware | 250 | 572 | 322 |
| microcontroller | 250 | 494 | 244 |
| oscilloscope | 250 | 486 | 236 |
| arduino | 250 | 448 | 198 |
| kicad | 250 | 434 | 184 |
| altium | 250 | 410 | 160 |
| kickstarter | 250 | 403 | 153 |
| component-sourcing | 250 | 397 | 147 |
| pcb-fabrication | 250 | 367 | 117 |
| pick-and-place-machine | 250 | 348 | 98 |
| firmware | 250 | 325 | 75 |
| usb | 250 | 279 | 29 |
| pcb-layout | 250 | 279 | 29 |
| semiconductor-fab | 250 | 270 | 20 |
| datasheet | 250 | 262 | 12 |
| internet-of-things | 250 | 252 | 2 |

## Thin-risk bundles (< 10 passages)

None — every bundle carries at least 16 passages.

## Lean bundles (10–19 passages, 6)

standard-cell (16), multiplexer (18), crosstalk (18), netlist (19), differential-signaling (19), bond-wire (19)

