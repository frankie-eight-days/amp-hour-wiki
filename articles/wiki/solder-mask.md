---
title: Solder Mask
concept: solder-mask
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Solder mask is the polymer layer applied over the copper of a printed circuit board, with openings cut where each pad sits and material left everywhere in between.[393] It serves several functions at once: it keeps moisture and surface contamination off the copper, which directly affects creepage and the withstanding voltage between adjacent traces; it steers solder and flux onto the pads during assembly; and it prevents bridging between closely spaced pads during reflow.[447][28][153] Because it is the inverse of a copper layer, its manufacturability is governed by a single rule — the minimum width of the strip of mask left between adjacent pads — and that rule in turn constrains how fine a component pitch a given fabrication house can build.[393][67]

## Function

The mask layer is the inverse image of the copper beneath it: an opening is cut over every pad, and mask is left everywhere else.[393] Its electrical function is insulation and protection. Creepage and voltage withstand between two traces depend on whether mask is present, because the layer keeps moisture and surface contamination off the copper; a proper board-spacing calculator takes its presence into account when giving a clearance for a given voltage.[447]

Its assembly function is equally central. Solder does not wet the mask, so during reflow, surface tension combined with the mask between the pins keeps solder confined to the pads.[259] Reflowing paste on a bare board without mask leaves only the flux to keep solder in place, with nothing to guide it back onto the pads.[233] This steering effect is a large part of what makes hand assembly on a fabricated board easy: flux and solder flow onto the pads rather than wandering across bare copper.[28][32]

The protection is not absolute. Salt-water contamination works its way under the mask and begins consuming the copper from underneath, a condition that is unrepairable rather than merely dirty.[312] Mask also cannot be relied on as an insulator for deliberate electrical isolation: counting on it to insulate a pad invites intermittent faults rather than a clean failure, and using it to blank off unwanted pads under a ball grid array has been considered and rejected because of the risk to the reflow process.[395]

## Design rules

A board house enforces exactly one rule on the solder mask layer: the minimum width of the strip of mask left between adjacent pads, which is the mirror image of the minimum trace width rule applied to copper.[393] Mask that does not survive between the pins is not doing the job it exists for, and being told by the fab that the mask is too narrow is one of the most common queries a designer will receive back on a job.[393]

Low-cost fabs carry a large minimum sliver rule that nearly every fine-pitch leadless footprint falls below, which is why boards routinely come back with no mask at all between the pins of packages such as QFNs.[162] Insisting on mask below the fab's minimum produces slivers that chip off in processing, and some board houses silently alter the layer rather than flagging the violation.[162]

Ball pitch drives board cost through mask and etch tolerance: tighter pitch demands tighter mask tolerances, which is why one open hardware design moved from 0.4 mm to 0.8 mm pitch parts so that builders could have their own versions manufactured.[67]

### Design verification

A rendered three-dimensional view of the bare board, with components hidden, is used to check mask expansion around pads and whether silkscreen is landing on top of them, both of which the flat layout view conceals.[34] Online board previews render mask expansion and silkscreen well but commonly ignore the drill file, so holes are missing from the picture being checked.[96]

## History

Mask is applied as a negative process because the early chemistry hardened under ultraviolet light: the exposed regions survived while the unexposed material was washed away, and the traditional green colour is an inheritance from that chemistry rather than a deliberate choice.[434] Early mask chemistry also shifted colour during processing, and fabs told customers nothing could be done about it until industry pressure produced chemistries that hold their colour; the problem is not encountered today.[170]

Modern boards apply mask directly over bare copper, whereas older boards applied it over roll-tinned copper, which is why boards from that era show wrinkled and peeling mask.[682] The roll-tinning step itself left small solder deposits that shorted closely spaced traces, and tracing down these "solder dags" was a routine and unpleasant part of bringing up a board.[682] Film-based exposure added another hazard: a speck of dust settling on the film was exposed into the board and appeared as a hairline short between adjacent tracks.[682] Every Gerber layer submitted to a fab becomes a photographic transparency — one per copper layer plus one per side for the mask — so a typical job consumes ten or a dozen of them.[414]

Before mask over bare copper became standard, designers deliberately left mask off a thermal pad so the wave-solder process would plate tin onto it, adding thermal mass and improving the heat transfer path — the same reason pads are deliberately solder-coated today.[436]

The availability of mask has tracked the economics of fabrication. Within living memory a tinned single-sided board counted as a high-quality kit and a double-sided board was unheard of, while masked, screened, plated-through double-sided boards are now the baseline.[143] The prototype board houses of two and three decades ago supplied double-sided tin-plated boards with no mask at all, and that was what a designer expected to work with.[494] Fixed-price prototype services later reached the point of offering ten double-sided plated-through boards with mask and silkscreen on both sides for twelve dollars including tooling, which removed most of the reason to make boards at home.[33]

## Assembly

Hand-pasting a fine-pitch package does not require dabbing each pad: a single line of paste drawn across all the pins reflows correctly because surface tension, together with the mask between the pins, keeps the solder on the pads, and the usual mistake is applying too much paste.[259] Bridging remains a real possibility whenever paste is applied through a stencil, and what prevents it is the mask between pads combined with getting the paste volume right.[153] Solder balls lodged under the mask are the visible sign that a paste application went wrong and needs to be wiped off and repeated.[473]

Reflow failures interact with the same surface-tension physics. Tombstoning is a reflow failure in which surface tension on one land pulls a component upright off the other, and a mass-produced board with a resistor in that state can still function, which is what makes the defect easy to ship.[11] Large thermal pads are broken into segments rather than left as one mask-and-paste opening so that the component does not float on molten solder; one production practice places a cross of mask and paste through the middle of the component.[531]

Guard traces are a recurring point of failure in the other direction: covering a guard trace over with mask removes the reason the guard was added in the first place, yet the error recurs in designs.[180]

### Fine-pitch escape

On one design, the route taken for power and ground escape under a ball grid array was to gang four adjacent pads around a single large via placed between them, with the annular ring touching all four pads and enough mask remaining between each pad and the via barrel.[395]

### Boards without mask

Milled boards lack plating, mask and silkscreen entirely, so a board made that way still has to be remade properly, and the machine time is only justified when the design genuinely cannot wait.[345] The case where milling does pay is simple single-sided analog work, where a board can be turned around in about two hours.[176] Printed silver-ink boards survive without mask because silver forms a sulphide tarnish rather than rusting, and that tarnish is self-limiting so it never penetrates the conductor — but the protection is only cosmetic in engineering terms, since the surface becomes unsolderable after a couple of months, giving an unmasked printed board a shelf life for assembly.[260]

## Home application and removal

The home process for mask is a UV-curable compound spread over the board and exposed through a printed transparency carrying the inverse image, after which the uncured material over the pads is washed off with alcohol and the rest fully cured; the process works but is messy, and alignment is the hard part.[454] Cure time depends on colour, with black slow because it absorbs the curing light and white also poor because it is far from transparent.[454]

Milling cured mask off a board demands vertical resolution around a hundredth of a millimetre, but a board is never flat to that degree and the copper is only half an ounce to an ounce thick, so a fixed depth setting exposes copper in one region and not another.[454] The workaround is a spring-loaded drag tip fitted with very light springs so that depth becomes pressure rather than position: the mask is soft enough that the tip cuts straight through it and then rides on the copper, restoring a usable margin for error.[454] A fibre laser can ablate copper directly to produce a single-sided board in about ten minutes of unattended time, with mask adding roughly five minutes of hands-on work and twenty minutes of processing, at the cost of giving up controlled impedance and fine geometry.[686]

Stripping cured mask off a finished board to expose the copper underneath is possible, but only with aggressive chemistry.[68]

## Thermal and environmental limits

Using a board as its own reflow heater is not reusable: after around five cycles at the roughly 200 °C needed to melt solder, the damage shows in the mask.[663]

## Colour and aesthetics

Colour choice remains constrained to a handful of stock options rather than an arbitrary specification, even though the palette is far wider than it once was.[434] A non-standard mask colour is not something fabs stock: when the OSH Park pooled service added redundant board houses, its operator had to buy the purple ink in for the ones that did not carry it and absorb that cost.[149] More than one mask colour can be printed on a single panel, but it requires an entirely separate set of screens and adds roughly fifty percent to the panel price.[149] The same pooled service, running through United States fabs, measured a failure rate of about one board in forty thousand, the failures being annular ring breakout, shorts and mask that was not quite right.[149]

A finished board's appearance is three independent choices stacked — the plating finish, the mask colour and the silkscreen colour — and each additional silkscreen colour means another pass through the process and another charge.[587] Combining mask, silkscreen and deliberately exposed copper gives a wide range of colours, textures and translucency from an entirely standard fabrication process, controlled purely by what is placed on each Gerber layer.[145] Mask colour can itself be chosen as the artwork, with a white mask supplying the base image and component colours picked to complete it.[403]

A front panel can be made from a board by flooding the area with copper and opening the legend through the mask layer, so the lettering appears in the plating finish against the mask colour.[149] For a cosmetically uniform top surface, vias are tented with mask and then covered again with silkscreen so they disappear into the artwork.[600] Leaving mask off a region lets light pass through the laminate itself, so the board substrate can be made to glow rather than needing a separate diffuser.[642] Mask relief can also be applied asymmetrically to a via, so that the same connection is exposed for contact on one face of the board and covered on the other.[275]

The mask surface is also what defeats photorealistic board rendering: at the right angle it reflects enough light to read as white while the plated pads still show as gold, so material models can only get so close.[473]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 11 | Ardui...no Dave This Week? | https://theamphour.com/the-amp-hour-11-ardui-no-dave-this-week/ | |
| 28 | Bowie and The Brown Note | https://theamphour.com/the-amp-hour-28-bowie-and-the-brown-noise/ | February 1, 2011 |
| 32 | Cores, Digikey, Electronic Design - The Commercial Competitor Commencement | https://theamphour.com/the-amp-hour-32-the-commercial-competition-commencement/ | |
| 33 | Bob Widlar, Electronic Design, FIRST Robotics - Monday, Meta Monday | https://theamphour.com/the-amp-hour-33-monday-meta-monday/ | |
| 34 | AD620, DesignSpark, Instrumentation Amplifier - The Rant Rhetorical | https://theamphour.com/the-amp-hour-34-the-rant-rhetorical/ | March 14, 2011 |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ | |
| 68 | Radiation Chips & Old Package Types - Technocratic Toilet Troubleshooting | https://theamphour.com/the-amp-hour-68-technocratic-toilet-troubleshooting/ | |
| 96 | Senseless Saccadic Shemozzle | https://theamphour.com/the-amp-hour-96-senseless-saccadic-shemozzle/ | |
| 143 | PCBs, Tektronix & Ham Radio - Habitual Handicraft Hangups | https://theamphour.com/the-amp-hour-143-habitual-handicraft-hangups/ | April 29, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 180 | An Interview with Dave Taylor - Multi-talented Meter Maker | https://theamphour.com/180-an-interview-with-dave-taylor-multi-talented-meter-maker/ | January 13, 2014 |
| 233 | Glass and Gongkai GSM - Unzymotic Ursidae Upbuilding | https://theamphour.com/233-glass-and-gongkai-gsm-unzymotic-ursidae-upbuilding/ | January 20, 2015 |
| 259 | No More Naming | https://theamphour.com/259-no-more-names/ | |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 275 | No One Even Missed Us? | https://theamphour.com/275-no-one-even-missed-us/ | November 19, 2015 |
| 312 | Aussie Bound! | https://theamphour.com/312-aussie-bound/ | August 17, 2016 |
| 345 | Milling About | https://theamphour.com/show-345-milling-about/ | May 30, 2017 |
| 393 | I've bitten myself | https://theamphour.com/393-ive-bitten-myself/ | May 20, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 447 | Voltnuts for Flashlights | https://theamphour.com/447-voltnuts-for-flashlights/ | June 16, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 642 | Sad Violins for Superconductors | https://theamphour.com/642-sad-violins-for-superconductors/ | August 13, 2023 |
| 663 | Motors on PCBs with Carl Bugeja | https://theamphour.com/663-motors-on-pcbs-with-carl-bugeja/ | March 25, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
