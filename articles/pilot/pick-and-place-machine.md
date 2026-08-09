---
title: Pick-and-place machine
concept: pick-and-place-machine
episodes: 146
guests: 42
explains: 68
opinion: 36
generated: 2026-08-08
model: claude-opus-5 (pilot batch, pipeline steps 6-8)
---

<!--
PRODUCTION NOTES (not for readers)
Gather: 426 census mentions across 146 episodes -> 245 pinned explains/opinion
passages after paragraph-level dedupe, CAPPED at 150 (all explains kept; opinion
selected by recency + speaker diversity, non-host speakers first).
Re-grade: of the 150 examined, 104 retained as substantive (68 explains, 36
opinion) and 46 discarded - placeholder-speaker turns, passing asides, and long
passages the census pinned because the phrase appeared inside a discussion of
something else entirely (IoT lifespan, YouTube thumbnails, multimeter teardowns).
Evidence packet: _packets/pick-and-place-machine.json (62 claims, 2 disagreement
groups).
ATTRIBUTION: ep 697 is labelled "Chris Gammell" / "Dave Jones" but Dave is not on
that episode at all - the guest is Tim from Mitxela, and the diarizer gave him a
host's name. Ep 699 carries a single label for all 129 turns. Eps 126 and 125 use
placeholder labels (SPEAKER_00/01/02). Everything from those files was attributed
by content or dropped. See _pilot_report.md.
-->

A pick-and-place machine positions surface-mount components onto solder paste under vacuum, forming one stage of an assembly line between the [[stencil]] printer and the [[reflow-oven]].[646][411] Its defining subsystem is the tape feeder rather than the motion system: without feeders the machine is a gantry, and feeders dominate both cost and setup effort.[319][224][317] Feeder slot count and minimum package size act as hard constraints on board design, determining both bill-of-materials consolidation and which assemblers can build a given board.[216][502] Whether an individual or small company should own one is persistently disputed, with a widely repeated estimate that around nine in ten prospective buyers do not need one,[412] set against a fall in entry price from roughly half a million dollars to under three thousand across sixteen years.[6][610]

## Feeders

Without tape feeders a machine is not functionally a pick-and-place machine but a gantry, a point made in near-identical terms by owners and non-owners alike.[319][224] The requirement is continuous dispensing: jelly-bean parts must feed indefinitely rather than be reloaded every hundred placements.[224] Anyone designing a machine is advised to design the feeder first, the motion system being comparatively straightforward — XY motors, a camera, software and a vacuum head.[319]

Feeders also dominate cost, at roughly 500 dollars each, and are the subsystem an owner most wants more of.[317] They carry part identity and configuration rather than being passive holders, completing the machine in the way a cartridge completes a console.[411]

## Design constraints imposed on the board

**Feeder slot count constrains the bill of materials.** Exceeding a machine's loader count forces a second setup pass and a second setup cost, whether the threshold is 40 slots and 41 parts or 60 and 61.[216][508] This is the practical argument for BOM consolidation, and it explains purchasing decisions that appear irrational in isolation: an integrated part occupies one feeder slot where discrete equivalents occupy four.[580]

**Package size filters the supplier list, not just the price.** Every machine handles 0603, while 0402 is a capability step that not all machines clear, requiring different nozzles and costing yield, so smaller packages should not be specified without need.[104] Quantitatively, 0402 is placeable by roughly 65 percent of machines and 0201 by roughly 30 percent.[502]

**Panel dimensions must be agreed with the assembler rather than the fabricator.** PCB houses quote large panels that will not fit a machine, a mismatch typically discovered after the boards have been made.[415] A large V-scored panel supported only at its guide rails will additionally fail mechanically under placement head pressure.[415] Tooling strips carrying sprocket holes along the panel edge are what allow a board to be transported through the machine at all.[494]

## Process and limitations

The machine occupies one position in a physical line: stencil printer, placement, reflow oven, automated optical inspection and bed-of-nails test, connected by conveyor.[646][50] [[solder-paste]] is applied before placement because its tack retains components until reflow.[411]

Placement is not self-verifying. A machine cannot detect that the wrong reel has been loaded into a slot; the error surfaces only at optical inspection after assembly.[554] Component consumption is also higher than board count implies, since parts are lost during reel loading and setup, which is why assemblers require excess stock.[24] Short cut-tape reels with leader tape do not solve this, as the machine consumes a large fraction of a short reel.[410]

Most machines are natively metric and convert from imperial input, introducing cascading rounding errors in placement data.[299] Pickup itself is tuned per component, with nozzle dwell time, vacuum level and release timing all adjustable and all requiring setting.[419]

Ownership changes design practice, because nozzle changes and part handling become visible constraints at schematic and layout time.[153] A mature in-house process aligns CAD library part orientation with feeder tape orientation, so that placement rotation requires no per-job checking.[412]

## Ownership debate

The question of whether to own a machine has been argued continuously since 2012 without converging. Dave Jones has held the negative position throughout: the window in which a self-operated machine beats outsourced assembly on combined time and money is very narrow,[63] roughly nine in ten people who believe they need one do not,[412] the volume threshold is around a hundred boards,[195] and on opportunity cost the purchase price buys a great deal of professional assembly.[178]

Mike Harrison, who runs a machine commercially, accepts the ninety-percent estimate while arguing that falling entry cost is shifting it, and that high-mix low-volume work needing fast turnaround is now a genuine case for ownership.[412] His characterisation of the difficulty is that it consists of many small problems rather than one large one, which is why it is underestimated before purchase.[412] Chris Gammell moved toward conditional support, holding that accessibility has made ownership defensible where recurring demand exists,[403] while separately supplying the strongest argument against it: ownership converts an electrical engineer into a process engineer concerned with paste thickness and placement statistics.[232]

Guests generally decline. Dafydd Roche proposes a usage test — a machine used less than weekly represents money better spent elsewhere — and identifies learning rather than profit as the honest motive for most owners.[270] Ian Johnston declines at batch sizes around fifty on grounds of learning time rather than price.[643] Jeff Keyzer rejects the premise outright: "I don't really need a pick and place machine. I am a pick and place machine."[613]

Low-cost and crowdfunded machines attract a separate scepticism. Headline prices exclude the options needed to make a machine usable, at which point commercial machines are already available at the resulting figure,[221] and specific claims such as one-touch setup were rejected while custom feeder designs were credited.[317] Mike Harrison states the test neutrally: an entry price is acceptable if it buys something expandable into a working machine, not if it buys a fixed toy.[224] Jonathan Hirschman argues the industry optimises the wrong specifications altogether, and doubts a genuinely working sub-5,000-dollar machine could carry full reels structurally.[299] Stephen Hawes, who builds an open-source desktop machine, attributes poor incumbent software to switching costs: a buyer locked into a 50,000-dollar machine will tolerate any interface.[686]

Andrew Seddon reports that the obvious high-mix strategy does not survive contact with reality: standardising on a common parts library and permanently loading twenty-five to thirty machines fails on combinatorics, and workable systems treat placement as one step among many, with material handling as the dominant problem.[699]

## Reported outcomes

A 40,000-dollar secondhand Juki bought around 2000 for an in-house line repaid its cost within four months, under conditions worth noting: continuous internal demand, a dedicated operator, and prior spending on subcontractors.[169]

The opposing case is documented in equal detail. Joe Garrison describes an in-house placement decision as a mistake made against a co-founder's objection, traces the root cause to a design choice to minimise board size that forced 0201 placement, and reports that the selected machine was specified for the package but had no customer running it that way in production.[237] His resulting advice is to have the actual board built on the actual machine before purchase, and to select machines that contract manufacturers run daily.[237] Capability alone is insufficient, since a machine may achieve fine-pitch placement only at a large throughput penalty.[237] Vic Aprea similarly reports that machines require sustained attention both to commission and to keep running, and that placement equipment alone is insufficient without reflow and stencil equipment.[250]

A documented learning exercise found that a repeated-part panel ran without difficulty while the mixed-component side required per-part calibration and differing pick heights,[403] reaching roughly 95 percent placement accuracy without extensive setup across 1,200 LEDs, the characteristic failure being parts standing on edge that the vision system accepted because the lens distorted the outline.[419] The durable conclusion concerned design rather than the machine: panelising boards should be the default regardless of assembly method.[403]

Two other outcomes are recorded: a machine acquired on indefinite loan after the hackspace that owned it was evicted and its equipment needed storage,[697] and a working machine mothballed during the 2021-22 component shortage for lack of parts and space, raising the unresolved question of whether an idle machine must be exercised periodically.[587]

## Price history

In 2010 the prediction was that falling prices would bring in-house placement, reflow and paste dispensing within hobbyist reach inside a decade, the marker being a shift from half-million-dollar machines to ten-thousand-dollar ones.[6] An open-source machine was at that point the outstanding unsolved problem in open hardware, defeated by mechanical complexity, with feeding mechanisms named as the reason machines cost what they do.[49]

By late 2013 Chinese desktop machines were available around 5,000 dollars and reported to work acceptably,[178] while secondhand professional machines from the mid-1990s could be had in good condition around 10,000 dollars.[153] By late 2022 a desktop machine with 40 integrated feeders was available under 3,000 dollars,[610] and an open-source desktop machine aimed at in-house prototype batches had reached its fourth revision by 2025.[686]

Two commercial rationales recur independently of price. 3D Robotics bought a line because batching a thousand boards froze the design until the stock sold, whereas in-house placement permitted roughly thirty board revisions in a year.[105] And at the other extreme, professional machines place dozens of devices per second, completing a board in an hour or two.[218]

## Further reading

- [Sparkfun has a new "grab bag" program for all their pick and place cast off parts](http://www.sparkfun.com/news/516) — via #24
- [redFrog](http://buildyourcnc.com/PickandPlaceMachineTheredFrog.aspx) — via #63
- [the hotplate method of reflowing boards](http://www.sparkfun.com/tutorials/59) — via #63
- [Limor from adafruit did a tutorial using info from Ryan](http://learn.adafruit.com/laser-cut-pcb-stencils/overview) — via #153
- [Quad PnP](http://ohararp.com/quad-pick-and-place/) — via #153
- [Sparkfun tutorial about paste/stencils](https://www.sparkfun.com/tutorials/58) — via #153
- [CircuitHub](http://circuithub.com) — via #216
- [Mancorp](https://www.manncorp.com/component-placement-and-handling/pick-and-place) — via #237
- [vapor phase](https://en.wikipedia.org/wiki/Reflow_oven#Vapour_phase_oven) — via #237
- [Jonathan Hirschman of PCB:NG](http://pcb.ng/) — via #299
- [Pieco paste press](https://www.tindie.com/products/Pieco/paste-press/) — via #299
- [NeoDen4](http://www.neodentech.eu/contents/en-uk/d8_NEODEN4.html) — via #419
- [Compare the Lumen to other methods](https://compare.opulo.io/) — via #686
- [OpenPNP](https://openpnp.org/) — via #686
- [See the CircuitHub capabilities](https://www.circuithub.com/capabilities/design-rules) — via #699
- [Worthington Assembly](https://www.worthingtonassembly.com/) — via #699

## References

| Ep | Title | URL | Date |
|---|---|---|---|
| 6 | Open Hardware and The Creative Economy | https://theamphour.com/the-amp-hour-6-open-hardware-and-the-creative-economy/ | - |
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ | - |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | - |
| 50 | Callow Cough Coverups | https://theamphour.com/the-amp-hour-50-callow-cough-coverups/ | - |
| 63 | Shop bots, 450 mm fabs & redFrog - Pick and Place Palillogy | https://theamphour.com/the-amp-hour-63-pick-and-place-palillogy/ | - |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15th, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23rd, 2012 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8th, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28th, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30th, 2013 |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ | April 21st, 2014 |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15th, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29th, 2014 |
| 221 | Warming Up To IoT - Tendentious Thermal Tools | https://theamphour.com/221-warming-up-to-iot-tendentious-thermal-tools/ | 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12th, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | 2015 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17th, 2015 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20th, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7th, 2015 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18th, 2016 |
| 317 | A Decoupled Episode | https://theamphour.com/317-a-decoupled-episode/ | September 28th, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12th, 2016 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12th, 2018 |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ | October 7th, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 419 | Feels over reals | https://theamphour.com/419-feels-over-reals/ | December 9th, 2018 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31st, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26th, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13th, 2020 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15th, 2021 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6th, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | - |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ | November 20th, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18th, 2022 |
| 643 | Calibration & Repair with Ian Johnston | https://theamphour.com/643-calibration-repair-with-ian-johnston/ | August 22nd, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11th, 2023 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21st, 2025 |
| 697 | LEDs Everywhere with Tim from Mitxela | https://theamphour.com/697-leds-everywhere-with-tim-from-mitxela/ | July 8th, 2025 |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ | July 31st, 2025 |
