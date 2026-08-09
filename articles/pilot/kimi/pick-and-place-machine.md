---
title: Pick-and-Place Machine
concept: pick-and-place-machine
generated: 2026-08-08
model: kimi-k3
writer-bakeoff: true
---

A **pick-and-place machine** is an automated machine used in electronics manufacturing to place surface-mount components onto printed circuit boards.[411] It sits at the centre of a surface-mount assembly line, taking components from tape feeders and depositing them onto boards prepared with solder paste before reflow soldering.[646][411] The machine's feeders, rather than its motion system, are regarded as its defining and costliest subsystem.[224][317][319] Once restricted to half-million-dollar industrial equipment, machines became available at desktop price points over the following decade, creating an ongoing debate over whether small companies and individual engineers should own one.[6][63][412]

## Role in the assembly line

A surface-mount assembly line is physically a line: a stencil printer, one or more pick-and-place machines, a reflow oven, automated optical inspection and bed-of-nails test equipment, connected by conveyors.[646][50] Solder paste is applied before placement because its tackiness retains the placed parts until reflow.[411] The machine transports panels through itself on tooling strips carrying sprocket holes along the panel edge.[494]

Professional machines place dozens of devices per second, completing a board in an hour or two.[218] Placement capability alone does not define throughput, however: a machine may achieve fine-pitch placement only at a large time penalty per board, on the order of 80 percent additional cycle time.[237]

## Feeders

Feeders are the defining subsystem of the machine. Without tape feeders that dispense components continuously, a pick-and-place machine is not functionally a pick-and-place machine but a gantry, since jelly-bean parts must be dispensed indefinitely without operator intervention.[224][319] Anyone designing a machine is advised to design the feeder first, the motion system being comparatively straightforward: XY motors, a camera, software and a vacuum head.[319]

Feeders dominate machine cost at roughly 500 dollars each and are the subsystem an owner most wants more of.[317] They also carry part identity and configuration, completing the machine in the way a cartridge completes a game console.[411] Feeding mechanisms are the principal reason machines cost what they do.[49]

Feeder slot count is a hard constraint on the bill of materials: exceeding the machine's loader count forces a second setup pass and a second setup cost, and the same threshold effect applies at 60 feeders versus 61 distinct parts, which is the practical argument for BOM consolidation.[216][508] Integrated components are bought partly for this convenience, occupying one feeder slot where discrete equivalents would occupy four.[580]

## Process constraints

### Component packages

Every machine handles 0603 packages as a minimum; 0402 is a capability step that not all machines clear, requiring different nozzles and costing yield, so smaller packages should not be specified without need.[104] Package size filters the available supplier list rather than merely raising cost: 0402 is placeable by roughly 65 percent of machines and 0201 by roughly 30 percent.[502]

### Panels

Panel dimensions must be agreed with the assembler, not only the fabricator: PCB houses quote large panels that will not fit a pick-and-place machine, a mismatch companies discover after the boards are made.[415] A large V-scored panel supported only at its guide rails will fail mechanically under placement head pressure.[415]

### Setup and operation

A machine cannot detect that the wrong reel was loaded into a slot; it assumes the correct part is in the correct slot, and the error surfaces only at automated optical inspection after assembly.[554] Assemblers require excess components beyond the board count because parts are consumed during reel loading and setup, and cut-tape reels with leader tape do not solve the problem since the machine wastes a large fraction of a short reel.[24][410] Most machines are natively metric and convert from imperial input, which introduces cascading rounding errors in placement data.[299] Pickup is tuned per component: nozzle dwell time, vacuum level and release timing are all adjustable and all need setting.[419]

Operating a machine changes design practice, because nozzle changes and part handling become visible constraints at schematic and layout time.[153] A mature in-house process aligns CAD library part orientation with feeder tape orientation, so that placement rotation needs no per-job checking.[412]

## History and cost trajectory

In 2010, falling machine prices were predicted to put in-house placement, reflow and paste dispensing within hobbyist reach within a decade, marking the shift from half-million-dollar to ten-thousand-dollar machines.[6] At that time an open-source machine was described as the outstanding unsolved problem in open hardware, defeated by mechanical complexity, with feeding mechanisms named as the reason for the cost.[49]

By late 2013, Chinese desktop machines were available at around 5,000 dollars and reported to work acceptably.[178] Secondhand professional machines from the mid-1990s were available in good condition at around 10,000 dollars.[153] By late 2022, a desktop machine with 40 integrated feeders was available under 3,000 dollars.[610] Desktop machines target low to medium volume and in-house prototype batches rather than production.[686]

## Practice

Companies have acquired in-house placement for reasons beyond unit cost. 3D Robotics bought a line because batching a thousand outsourced boards froze the design until the stock sold, whereas in-house placement permitted roughly thirty board revisions in a year.[105] A 40,000-dollar secondhand Juki bought around 2000 for an in-house line repaid its cost within four months, given continuous internal demand, a dedicated operator and prior subcontractor spending.[169]

Machines require sustained attention to commission and to keep running, and placement alone is insufficient without reflow and stencil equipment.[250] In one documented exercise, a repeated-part panel ran without difficulty while the mixed-component side required per-part calibration and differing pick heights; roughly 95 percent placement accuracy was achieved without extensive setup across 1,200 LEDs, the characteristic failure being parts standing on edge that vision accepted because the lens distorted the outline.[403][419] The conclusion drawn was that panelising boards should be the default regardless of assembly method.[403]

One in-house placement effort was later characterised as a mistake made against a co-founder's objection. The root cause was a design decision to minimise board size, which forced 0201 placement; the selected machine was specified for that package size but had no customer running it that way in production.[237] The recommendation drawn from the experience is to have the actual board built on the exact machine before purchase, and to select machines that contract manufacturers run daily.[237]

Machines occasionally change hands informally: one was acquired on indefinite loan after the hackspace that owned it was evicted and its equipment needed storage.[697] During the 2021–22 component shortage, at least one owner mothballed a working machine for lack of parts and space, raising the unresolved question of whether an idle machine must be exercised periodically.[587]

## Reception and debate

### Whether to own a machine

Dave Jones has argued that the window in which a self-operated machine beats outsourced assembly on combined time and money is very narrow, estimating that roughly nine in ten people who believe they need a machine do not.[63][412] He sets the volume threshold at around a hundred boards—below that, manual assembly is faster overall—and argues on opportunity-cost grounds that the purchase price of a low-cost machine buys a large quantity of professional assembly.[195][178]

Mike Harrison agrees with the 90 percent estimate but holds that falling entry cost is shifting it, and that high-mix, low-volume work with fast turnaround is now a genuine case for ownership. He characterises the difficulty as many small problems rather than one large one, which is why it is underestimated before ownership: "It's lots and lots and lots and lots of tiny, tiny issues. And little ones that will kill you."[412] Chris Gammell has argued that falling cost and rising accessibility have made ownership defensible where sufficient recurring demand exists, though he also frames the real cost as a change of profession: an owner becomes a process engineer concerned with paste thickness and placement statistics rather than an electrical engineer.[403][232]

Dafydd Roche proposes a usage test—a machine used less than weekly represents money better spent elsewhere—and identifies learning rather than profit as the honest motive for most owners.[270] Ian Johnston declines ownership at batch sizes around fifty on the grounds of learning time rather than purchase price.[643] Jeff Keyzer rejects the premise outright: "I don't really need a pick and place machine. I am a pick and place machine."[613]

### Low-cost and crowdfunded machines

Jones has argued that headline prices for crowdfunded machines exclude the options needed to make them usable, at which point commercial machines are already available, and has rejected one crowdfunded machine's one-touch setup claim while crediting its custom feeder design.[221][317] Harrison frames the test for a low-cost machine as whether the entry price buys something expandable into a working machine or a fixed toy.[224] Jonathan Hirschman has argued that the industry optimises the wrong specifications, and that a genuinely working sub-5,000-dollar machine would lack the structure to carry full reels.[299] Stephen Hawes, who built a desktop machine, attributes poor industrial machine software to switching costs: a buyer locked into a 50,000-dollar machine will tolerate any interface.[686]

Separately, standardising on a common parts library and permanently loading many machines has been found to fail on combinatorics; workable high-mix assembly treats placement as one step among many, with material handling as the dominant problem.[699]

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
|---|---|---|
| 6 | Open Hardware and The Creative Economy | https://theamphour.com/the-amp-hour-6-open-hardware-and-the-creative-economy/ |
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ |
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
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ |
| 643 | Calibration & Repair with Ian Johnston | https://theamphour.com/643-calibration-repair-with-ian-johnston/ |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ |
| 697 | LEDs Everywhere with Tim from Mitxela | https://theamphour.com/697-leds-everywhere-with-tim-from-mitxela/ |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ |
