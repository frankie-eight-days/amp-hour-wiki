---
title: Pick-and-place machine
concept: pick-and-place-machine
generated: 2026-08-08
model: kimi-k3
spec: knowledge-only-v3
---

A pick-and-place machine is an automated assembly machine that picks surface-mount components from tape reels mounted on feeders and places them onto a printed circuit board previously coated with solder paste, whose tack retains the parts until reflow soldering fixes them permanently.[411] The machine's motion system — XY motors, a camera, control software, and a vacuum pickup head — is the comparatively straightforward part of its design; the feeder subsystem, which dispenses components continuously from tape, is what distinguishes a working machine from a bare gantry.[319][224] Professional machines place dozens of devices per second and can complete a board in an hour or two.[218] In production the machine sits physically in a conveyor-linked line: stencil printer, pick-and-place, reflow oven, automated optical inspection, and bed-of-nails test.[646][50]

## Feeders

Without tape feeders a pick-and-place machine is not functionally a pick-and-place machine; it is a gantry, because components must be dispensed continuously rather than reloaded every hundred parts.[319][224] Anyone designing a machine is advised to design the feeder first, the motion system being comparatively straightforward.[319] Feeders dominate machine cost at roughly $500 each, and are the subsystem an owner most wants more of.[317]

Feeder slot count is a hard constraint on the bill of materials: exceeding the machine's loader count forces a second setup pass and a second setup cost.[216] The same threshold effect applies at 60 feeders and 61 distinct parts, which is the practical argument for BOM consolidation.[508] Integrated parts are bought partly for this reason, occupying one feeder slot where discrete equivalents would occupy four.[580]

## Panel design and transport

Panel dimensions must be agreed with the assembler, not only the fabricator: PCB houses quote large panels that will not fit a pick-and-place machine, a mismatch companies discover after the boards are made.[415] A large V-scored panel supported only at its guide rails will fail mechanically under placement head pressure — the board snaps as soon as the head hits it.[415] Tooling strips carrying sprocket holes along the panel edge are what allow a board to be transported through the machine.[494]

Panelisation pays off in operation: a repeated-part panel ran without difficulty while the mixed-component side required per-part calibration and differing pick heights, leading one operator to conclude that panelising boards should be the default regardless of assembly method.[403]

## Package size and machine capability

Every machine handles 0603; 0402 is a capability step that not all machines clear, requiring different nozzles and costing yield, so smaller packages should not be specified without need.[104] Package size filters the supplier list rather than merely raising cost: 0402 is placeable by roughly 65 percent of machines and 0201 by roughly 30 percent.[502] A decision to minimise board size that forced 0201 placement was traced as the root cause of one troubled machine deployment.[237]

Placement capability alone is an insufficient specification: a machine may achieve fine-pitch placement only at a large throughput penalty, such as 80 percent more time per board.[237] One machine specified for the required package size turned out to have no customer running it that way in production.[237] The recommended procurement test is to have the actual board built on the actual machine before purchase, and to select machines that contract manufacturers run daily in that configuration.[237]

## Operation, setup, and failure modes

A machine cannot detect that the wrong reel was loaded into a slot; it assumes the correct part is in the correct slot, and the error surfaces only at automated optical inspection after assembly.[554] Most machines are natively metric and convert from imperial input, which introduces cascading rounding errors in placement data.[299]

Pickup is tuned per component: nozzle dwell time, vacuum level, and release timing are all adjustable and all need setting.[419] Across a run of 1,200 LEDs, roughly 95 percent placement accuracy was achieved without extensive setup; the characteristic failure was parts standing on edge that the vision system accepted because the lens distorted the outline.[419] A mature in-house process aligns CAD library part orientation with feeder tape orientation, so that placement rotation needs no per-job checking.[412]

Assemblers require excess components beyond the board count, because parts are consumed during reel loading and setup; a reel of 100 resistors will not populate 100 boards.[24] Cut-tape reels with leader tape do not solve the problem, since the machine consumes a large fraction of a short reel.[410]

Machines require sustained attention to commission and to keep running, and placement alone is insufficient without reflow and stencil equipment.[250] The difficulty is characterised by experienced owners as many small problems rather than one large one, which is why it is underestimated before ownership — "lots and lots and lots and lots of tiny, tiny issues. And little ones that will kill you."[412]

## High-mix operation

Standardising on a common parts library and permanently loading many machines fails on combinatorics; workable high-mix assembly treats placement as one step among many, with material handling as the dominant problem.[699]

## Ownership economics

Practitioners place the window in which a self-operated machine beats outsourced assembly on combined time and money as very narrow.[63] Below roughly a hundred boards, manual assembly is judged faster overall; at batch sizes around fifty, one practitioner declined ownership on the grounds of learning time rather than purchase price.[195][643] The purchase price of a low-cost machine buys a large quantity of professional assembly time, an opportunity-cost argument against ownership.[178] A proposed usage test is that a machine used less than weekly represents money better spent elsewhere.[270] The real cost is framed as a change of profession: an owner becomes a process engineer concerned with paste thickness and placement statistics rather than an electrical engineer.[232] Conversely, operating a machine has been reported to change design practice for the better, because nozzle changes and part handling become visible constraints at schematic and layout time.[153]

The counter-example is sustained internal demand: a $40,000 secondhand Juki bought around 2000 for an in-house line repaid its cost within four months, given continuous internal demand, a dedicated operator, and prior subcontractor spending.[169] 3D Robotics bought a line because batching a thousand boards froze the design until the stock sold, whereas in-house placement permitted roughly thirty board revisions in a year.[105] Desktop machines target low-to-medium volume and in-house prototype batches rather than production.[686]

## Low-cost machines

Headline prices for crowdfunded machines exclude the options needed to make them usable; a machine advertised from $300 reaches $3,000 with options, at which point commercial machines are already available.[221] The test for a low-cost machine is whether the entry price buys something expandable into a working machine or a fixed toy.[224] The industry optimises the wrong specifications: a genuinely working sub-$5,000 machine would lack the structure to carry full reels.[299]

The price of entry fell over the following decade: by late 2013 Chinese desktop machines were available at around $5,000 and reported to work acceptably; secondhand professional machines from the mid-1990s were available in good condition at around $10,000; by late 2022 a desktop machine with 40 integrated feeders was available under $3,000.[178][153][610]

## Further reading

- [Sparkfun has a new "grab bag" program for all their pick and place cast off parts](http://www.sparkfun.com/news/516) — via #24
- [redFrog](http://buildyourcnc.com/PickandPlaceMachineTheredFrog.aspx) — via #63
- [the hotplate method of reflowing boards](http://www.sparkfun.com/tutorials/59) — via #63
- [Limor from adafruit did a tutorial using info from Ryan](http://learn.adafruit.com/laser-cut-pcb-stencils/overview) — via #153
- [Sparkfun tutorial about paste/stencils](https://www.sparkfun.com/tutorials/58) — via #153
- [Quad PnP](http://ohararp.com/quad-pick-and-place/) — via #153
- [CircuitHub](http://circuithub.com) — via #216
- [Mancorp](https://www.manncorp.com/component-placement-and-handling/pick-and-place) — via #237
- [vapor phase](https://en.wikipedia.org/wiki/Reflow_oven#Vapour_phase_oven) — via #237
- [Jonathan Hirschman of PCB:NG](http://pcb.ng/) — via #299
- [Pieco paste press](https://www.tindie.com/products/Pieco/paste-press/) — via #299
- [NeoDen4](http://www.neodentech.eu/contents/en-uk/d8_NEODEN4.html) — via #419
- [OpenPNP](https://openpnp.org/) — via #686
- [Compare the Lumen to other methods](https://compare.opulo.io/) — via #686
- [Worthington Assembly](https://www.worthingtonassembly.com/) — via #699
- [See the CircuitHub capabilities](https://www.circuithub.com/capabilities/design-rules) — via #699

## References

| Episode | Title | URL |
|---------|-------|-----|
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ |
| 50 | Callow Cough Coverups | https://theamphour.com/the-amp-hour-50-callow-cough-coverups/ |
| 63 | Shop bots, 450 mm fabs & redFrog - Pick and Place Palillogy | https://theamphour.com/the-amp-hour-63-pick-and-place-palillogy/ |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ |
| 221 | Warming Up To IoT - Tendentious Thermal Tools | https://theamphour.com/221-warming-up-to-iot-tendentious-thermal-tools/ |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ |
| 317 | A Decoupled Episode | https://theamphour.com/317-a-decoupled-episode/ |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ |
| 419 | Feels over reals | https://theamphour.com/419-feels-over-reals/ |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ |
| 643 | Calibration & Repair with Ian Johnston | https://theamphour.com/643-calibration-repair-with-ian-johnston/ |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ |
