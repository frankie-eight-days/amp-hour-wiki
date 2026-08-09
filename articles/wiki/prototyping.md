---
title: Prototyping
concept: prototyping
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Prototyping is the practice of building a partial or provisional version of a design in order to learn something that cannot be established on paper. Interaction design practice treats the prototype as the only reliable test of a design: build something people can actually operate, observe them using it, and iterate, because the quality of an interface is otherwise not knowable in advance.[726] The defining property of a prototype is that it can be changed easily, which is what distinguishes it from a committed design.[412] The governing priority in early work is to get a working artifact in hand, accepting that the first version will be slow and rough, with refinement deferred to later passes.[322]

## Purposes

Corporate research laboratories use prototyping as a de-risking function: building and investigating a technology establishes whether a design path is worth pursuing, and the negative result is fed back to the business unit before product development money is spent.[430] Integrated circuits built in such a group are generally aimed at becoming a product in roughly four to five years, so the prototype horizon sits far ahead of the current product line.[430]

The same logic protects a consulting practice at much smaller scale. Prototyping the single riskiest sub-block of a proposed job before accepting it means an unsolvable problem is discovered during the quote rather than after the contract is signed.[135]

Prototypes also verify parts. Front-page datasheet features can hide tolerances that break a design idea: a chip advertised with built-in current limiting may specify 15 percent tolerance on that limit over temperature, which rules out using it as a precision current source.[154] The recommended sequence for evaluating a promising part is therefore to read the full datasheet including the footnoted tolerances first, and then build a prototype to confirm the behaviour before designing around it.[154]

## Method

Prototyping can be run as the scientific method: state a hypothesis about how the thing works, run a defined experiment against it, evaluate whether the hypothesis held, and cycle back with a revised hypothesis if it did not.[373] A related technique for a concept that looks unworkable is to enumerate the specific reasons it should fail and then attempt each one, since many of the listed obstacles turn out to be individually solvable.[328]

What distinguishes highly effective prototypers is tenacity and method rather than special equipment: they keep trying variations systematically instead of abandoning an approach at the first failure.[373] They also suspend the demand for a finished-looking result and begin assembling immediately with expedient methods such as hot glue, treating the willingness to start as a learnable skill.[328]

Deliberate constraint is used as a forcing function. Working at a remote cabin with only a hauled-in oscilloscope, soldering station and a fixed parts stock and no internet forces completion with the resources on hand.[330] One mechanical design process starts by building physically from a bucket of standard parts on the desk and only afterwards designing the equivalent structure from scratch, removing the features the standard parts carried but the product does not need.[369]

Iteration counts are higher than the first result suggests. A concept demonstration built in a day proves only a limited case, and expanding that demonstration into something that works in every case is typically a further twenty or so iterations.[141] Front-end concept work on a small mechatronic build, covering sketches and a couple of schematics, can itself consume ten to twenty hours before any hardware is assembled.[284] Prototyping in an unfamiliar mechanical domain exposes constraints that cannot be predicted on paper; an enclosure sized to hold batteries and drivers can be found to obstruct movement only once the assembly is ridden or operated.[284]

Speed comes largely from keeping a standing library of known-good building blocks: a microcontroller always returned to, reusable code, and stock mechanical parts and subassemblies on the shelf.[416] A working mini electric motorbike was assembled in about three days entirely from parts already in the workshop, including eight-inch caster wheels, a spare motor and belt, T5 pulleys and a twist grip left over from an earlier project.[416] A one-person consultancy can likewise cover prototype-quantity parts from personal stock accumulated over thirty years, improvising or desoldering from an old board rather than ordering, because prototype quantities are small enough for that to work.[224] Such stock stays usable if leftovers are filtered out of the project box back into general stock as soon as each project finishes, so the inventory remains searchable from memory.[224]

## Building blocks

Modular, header-connected hardware is almost always the right choice for prototyping, because plugging known interfaces together is faster than fabricating an integrated board.[491] A top-down approach starts from off-the-shelf modules to prove the concept, since proving the concept is usually the hard part and custom hardware can follow.[383] Waiting on fabricated boards stretches the time before a team learns whether an idea is viable at all, which is the main argument for using modules already in hand during the earliest spins.[383] A first board should likewise use an integrated chip or a module rather than a discrete implementation, so the design gets finished and can then be revisited for cost optimisation, instead of never converging.[313] Early prototypes benefit from off-the-shelf choices in power and mechanics too: a coin cell is cheap and readily available as the initial power source, and a stock enclosure costs less and looks better than a printed case.[389]

Modules are designed for a prototype-then-respin workflow in which the module proves the concept and a custom board follows; using them as quasi-production hardware leaves in compromises such as permanently enabled pull-ups.[602] How much bring-up and debug infrastructure to break out on a module — the reset line, other debug pins, and individual per-module supplies allowing power sequencing — is a line drawn by application criticality rather than a universal rule, with wire count and bundle thickness the cost of that flexibility.[602]

Vendors have supported this workflow directly. Semiconductor suppliers have shipped Arduino-form-factor shields for their analogue parts, letting a hardware engineer read and write device registers and pull a data stream out of an ADC without writing low-level firmware first.[323] Radio modules serve the same role: a pair of XBee radios configured through the vendor GUI behaves as a transparent point-to-point serial link, though their cost means designs are expected to move to another radio for volume.[618]

Package choice follows prototyping needs as well. Through-hole microcontrollers survive because a DIP part can be pulled and replaced in seconds when a static discharge kills it, which is not true of a soldered SMD device.[3] Silicon vendors have continued to release modern cores in through-hole packages aimed at breadboard work, including a Cortex-M0 in a DIP package, a package choice justified by prototyping rather than by volume production.[68] Solderless breadboards and plug-in jumper wires are electrically adequate up to roughly 10 MHz, above which parasitics of the interconnect start to matter.[373] For most one-off circuit experiments, dead-bug construction, Manhattan-style pads, or a hand-cut board are faster and cheaper routes than buying dedicated prototyping hardware.[273] Hand prototyping is bounded by package technology overall: it stays feasible while parts remain hand-solderable, and BGA or fine-pitch TQFP devices push the work onto fabricated boards.[375]

Mechanical prototyping benefits from a comparable fixed grid. A Lego Technic-compatible beam system, 8 mm wide with holes on 8 mm centres, supplies the constraints that make early mechanical work tractable, since a blank mechanical design offers no starting point.[369] Lego itself is expensive as a bulk material: priced by weight, 3D printer filament came out roughly seven to ten times cheaper per pound, with extruding filament from raw pellets offering about another factor of ten.[369]

## Software for prototypes

Interpreted environments such as Lua virtual machines and Python are used to churn out prototypes and proofs of concept quickly, with the design reimplemented more rigorously once the product will be built in more than about five units.[295] When the objective is to get a prototype working quickly rather than to optimise it, C is a poor default and a higher-level embedded language removes friction from the first pass.[329] The concrete engineering argument for moving prototype firmware to CircuitPython is measured iteration speed rather than platform preference.[530]

Under a hard deadline such as a 24-hour hackathon, running interpreted code on an existing board displaces spinning a custom board and bringing it up bare metal, because only the former fits the time budget.[323] Scripting-language embedded platforms are aimed at that fast-iteration stage; a shipping product is usually handed to an embedded specialist to tighten up, unless the device is simple enough that no drop to low-level code is required.[323]

## Fabrication for prototype quantities

Manufacturability and prototypability are separate properties: a process can be viable in volume yet offer no way to make one-off samples, which blocks experimentation until someone brings the process down to prototype scale.[260] Inkjet-style conductive printing onto fabric illustrates the difficulty, because the substrate is floppy rather than flat and must be stretched taut to hold a controlled distance between print head and material.[260]

In-house forming and machining cannot match the throughput of a large stamping press and are therefore used only for prototype parts, not production runs.[156] Keeping fabrication in-house shortens the loop mainly by removing the outbound shipment and the retooling penalty, so a mistake costs another in-house run rather than a new tool and a new lead time.[156] Owning enough machining capability to make basic prototype parts in-house also pays off as a communication skill: the designer who has cut the part specifies it better and represents a more credible customer when the job is later sent to a machine shop.[379]

Desktop 3D printing is used for enclosure and packaging prototypes rather than volume parts, on the reasoning that a printed case need only be functional, not cosmetically finished, at that stage.[78] It is properly classified as a prototyping tool rather than a manufacturing process, and most projects do not require owning the equipment, since fabrication can be farmed out and a Dremel and a file cover a large fraction of early mechanical work.[353] Small mechanical parts such as miniature planetary gear sets can instead be prototyped by machining a positive mould, casting a silicone negative from it, and pouring urethane into the silicone, which yields multiple parts from one machining operation.[331] Injection moulding is deferred while a product is still effectively in prototyping, because continual design updates would invalidate the tooling investment.[369]

Automated PCB design services have been offered as prototyping services at around $3,000 for a 24-hour turnaround, bounded by limits such as fewer than 50 components, 20 unique components, under 3 amps, under 500 MHz, and under 20 watts total.[412]

## Schedule and supply

The realistic answer to how soon another prototype build can be made is the component lead time plus debug time, roughly twelve weeks plus however long it takes to bring up the batch of ten boards.[328] A twelve-week lead time also desynchronises prototyping from procurement: by the time the ordered part arrives and is fitted and tested, the board may already be three or four revisions further on, leaving several live versions of the design to track.[176]

Board fabrication lead time is not dead time in a spin, because firmware can be written while the PCB is in fab, which is part of why compressing fab turnaround alone buys less than it appears.[412] Prototype builds are nonetheless often placed with domestic assembly houses purely for turnaround speed, with the move to lower-cost offshore manufacture deferred until quantities rise.[229]

Salvage shortens some loops and closes others. Laser diodes pulled out of old CD and DVD players supplied the emitters for early laser-scanning tracking experiments.[326] Harvesting parts out of finished consumer products creates a trap, however: the demonstration works but the product cannot be built, because the salvaged item, such as an LCD, is only sold against a minimum order of panels.[328] Custom display suppliers rarely support prototype quantities from small unknown customers, and the low-volume route that does exist, used for military LCDs, runs on the order of a thousand dollars per screen.[328]

Changes keep arriving late. A nominally locked-down hardware design still accumulates prototype changes, because engineers keep trying new variants and correcting mistakes after the freeze.[176] Even after a production panel has been ordered and passes quality inspection, small mechanical corrections keep surfacing, such as enlarging a hole by 0.2 mm because a connector lacks margin and a switch wobbles, or nudging silkscreen a couple of millimetres.[176] During safety and EMC compliance testing a design change costs no extra test fee but pauses the certification schedule until a corrected unit is delivered, which makes the change expensive in calendar time.[218] Compliance testing therefore compresses the turn time a team is used to, so that a two-week prototype turn becomes a same-day emergency build.[218]

## Economics

Prototyping deliberately trades unit economics for information: single-piece and low-quantity versions cost more per unit, and that premium buys knowledge of what is actually needed before committing to volume.[313] The same logic applies to capital equipment for a prototyping shop, where using shared or outsourced services first establishes which machines are genuinely needed, whereas buying up front on assumption leaves advanced equipment unused.[313] For a build of only about three units, assembling from off-the-shelf components is cheaper and faster than a custom design, because custom engineering cost can only be amortised over a thousand or more units.[635]

Designing a switching DC-DC converter from scratch rather than using an off-the-shelf regulator adds a prototyping cycle, which is one reason cost-sensitive designs step voltages up or down with standard parts instead.[32] Modular construction is usually wrong for production, because connectors add cost, the stacked form factor is inefficient, and power consumption is not optimised for the application; the exception is a high-margin niche product where the module cost is immaterial.[491]

Engineers trained in prototyping-only organisations learn to design against functional requirements with cost as a secondary concern, a habit that has to be unlearned when moving to volume manufacturing.[577] At volume the arithmetic of part selection changes sharply: saving ten cents of bill-of-materials cost across a million units returns one hundred thousand dollars, roughly the cost of another engineer.[577]

Prototype work performed for a prospective client is billable engineering time rather than a free sales activity, and treating it as free is a recognised failure mode of design consulting.[592]

## Limits of what a prototype demonstrates

Prototypes built on general-purpose platforms do not scale: an installation demonstrated with about 200 LEDs behaves differently at 20,000, where power management fails first and data bandwidth second.[524] Customers who bring in a production-focused designer earlier, rather than after a prototype has been proven on hobbyist hardware, avoid re-engineering work because the scaling constraints are understood before the architecture is fixed.[524] Low-power wide-area networks show the same pattern: a configuration that works in a small prototype degrades as node count rises, because the available channels are few and slow and packet collisions increase, making network capacity rather than link range the limiting factor.[618]

A manufacturable product differs from the original dev-board prototype by essentially every measure, so converting a proven prototype into a producible design is a distinct project rather than a cleanup pass.[628]

Appearance is a particularly weak proxy. A convincing crowdfunding demonstration can be a purely cosmetic prototype, for example a cast acrylic model with no electronics, firmware, or software inside.[314] A crowdfunded hardware programme can conversely be launched from an early proof of concept plus a user-interface mock-up and a render of a pre-beta board, with the design then carried through a production run of a couple of hundred units.[87] Functionality that does not exist yet can also be faked by a human during a demonstration, a Mechanical Turk approach exemplified by an engineer behind a trade-fair booth manually switching an LED that the product is supposed to control.[235]

Fidelity should be matched to the question being asked. Prototypes intended for user testing should represent what test participants expect the experience to be rather than a technically accurate simulation; in one case a hastily assembled mock built from televised race footage tested better than a physically accurate model.[550]

A common procedural error is moving into PCB layout too early, when bodging with existing hardware, wire-wrap, a dev board wired to a sensor breakout, or duct-taped assemblies would answer the open questions before any board is committed.[373] Committing early also carries a long tail, since the first PCB CAD package a beginner learns tends to be the one they keep using for years.[373]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 3 | HP, IEEE, and Human Interface | https://theamphour.com/3-hp-ieee-and-human-interface/ |  |
| 32 | Cores, Digikey, Electronic Design - The Commercial Competitor Commencement | https://theamphour.com/the-amp-hour-32-the-commercial-competition-commencement/ |  |
| 68 | Radiation Chips & Old Package Types - Technocratic Toilet Troubleshooting | https://theamphour.com/the-amp-hour-68-technocratic-toilet-troubleshooting/ |  |
| 78 | Alteritous Andy's Absquatulation | https://theamphour.com/the-amp-hour-alteritous-andys-absquatulation/ | January 16, 2012 |
| 87 | An Interview with Ian Daniher - Nascent Nonolith Numquid | https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/ |  |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 141 | FPGAs, Robots & Thermocouples - Wampum's Wavering Worth | https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/ | April 15, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 156 | Tesla, FPGAs and DigiKey - Zesty Zippy Zynq | https://theamphour.com/the-amp-hour-156-zesty-zippy-zynq/ | July 29, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 273 | Part Choice Triathlon | https://theamphour.com/273-part-choice-triathlon/ | October 28, 2015 |
| 284 | An Interview with Great Scott | https://theamphour.com/284-an-interview-with-great-scott/ | January 27, 2016 |
| 295 | An Interview with Omer Kilic | https://theamphour.com/295-an-interview-with-omer-kilic/ | April 20, 2016 |
| 313 | My Kind of Town | https://theamphour.com/313-my-kind-of-town/ | August 31, 2016 |
| 314 | An Interview with Josh Lifton | https://theamphour.com/314-an-interview-with-josh-lifton/ | September 7, 2016 |
| 322 | World Trade Futurity (WTF) | https://theamphour.com/322-world-trade-futurity-wtf/ | November 9, 2016 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 328 | The Ghost of Keyzermas Past | https://theamphour.com/328-the-ghost-of-keyzermas-past/ | December 21, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ |  |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 331 | An Interview with Simone Giertz | https://theamphour.com/331-an-interview-with-simone-giertz/ | January 11, 2017 |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 369 | An Interview with Jason Huggins | https://theamphour.com/369-an-interview-with-jason-huggins/ | November 26, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 379 | An Interview with John Saunders | https://theamphour.com/379-an-interview-with-john-saunders/ | February 11, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 416 | An Interview with James Bruton | https://theamphour.com/416-an-interview-with-james-bruton/ | November 18, 2018 |
| 430 | Shahriar Discusses 5G | https://theamphour.com/430-shahriar-discusses-5g/ | February 17, 2019 |
| 491 | The Almighty Dollarydoo | https://theamphour.com/491-the-almighty-dollarydoo/ | May 3, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15, 2021 |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ | July 18, 2021 |
| 577 | Product Lifecycle Management with Michael Corr | https://theamphour.com/577-product-lifecycle-management-with-michael-corr/ | February 13, 2022 |
| 592 | Product Design with Simone Giertz | https://theamphour.com/592-product-design-with-simone-giertz/ | June 6, 2022 |
| 602 | Rigorous engineering stuff may be out the window | https://theamphour.com/602-rigorous-engineering-stuff-may-be-out-the-window/ | September 11, 2022 |
| 618 | Refrigerators and Robots with Amitabh Shrivastava | https://theamphour.com/618-refrigerators-and-robots-with-amitabh-shrivastava/ | February 5, 2023 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 635 | Low Power Connected Devices with Andrea Longobardi | https://theamphour.com/635-low-power-connected-devices-with-andrea-longobardi/ | June 4, 2023 |
| 726 | Arduino's Invisible Touch with Massimo Banzi | https://theamphour.com/the-amp-hour-726-arduinos-invisible-touch-with-massimo-banzi/ | June 17, 2026 |
