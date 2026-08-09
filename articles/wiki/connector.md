---
title: Connector
concept: connector
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A connector is the mating interface through which power and signals pass between separable parts of an electronic system, and its selection governs reliability, cost and serviceability to a degree out of proportion to its apparent simplicity. Connector proliferation is a consequence of physics rather than poor standardisation: no single connector can both carry vehicle-charging currents and present the constant impedance and high-frequency response an antenna feed requires.[708] A modular product depends on the quality of its connection points for reliability, and even where there is no discrete connector the mating contact surfaces still require deliberate mechanical design.[170] Obsolescence is among the largest long-term risks a connector introduces into a design, since the mating part and harness are locked to it and no electrical substitute exists.[425]

## Electrical limits

The power budget of a compact interface is set by contact and conductor cross-section rather than by protocol, and a hundred watts cannot be pushed through a handful of thin twisted pairs in a small connector shell.[240] High-power delivery over a small connector is therefore achieved by raising the voltage rather than the current, because contact and conductor resistance make the equivalent power impossible to pass at five volts.[240] Five amps through a connector of small consumer size sits at the edge of what the contact geometry can support, leaving little margin for contact resistance growth.[240] The same principle applies on a board: feeding a board at 24 volts and stepping down to 5 volts with an on-board buck converter keeps the current through the input connector low enough that the housing does not melt.[340] At the high-power extreme, delivering 350 kilowatts to a single vehicle at 800 volts and 450 amps requires a purpose-designed connector, because at those currents every micro-ohm of contact resistance turns into significant dissipation.[353]

At high signalling rates the interconnect becomes the limiting element. Once gigabit speeds are reached the cable and connector are more critical than they are at USB 2.0 speeds, and a kink in the cable raises the bit error rate enough to drop the link entirely.[50] Current-carrying capacity and mating life are also not independent: a connector rated for 10,000 mating cycles is not necessarily rated to carry its full current after those cycles, because plating wear raises contact resistance as the gold rubs away.[240]

ESD protection belongs physically close to the connector it defends and must be rated for the working voltages of that interface.[573] Choosing such a device depends on the bus or signal speed, the frequencies of interest and the operating voltages, so a part suitable for one connector interface may load or distort another.[573] Where a keyed connector can physically be mated reversed, one orientation may apply supply directly to a data input and destroy the first device in a chain, and a series protection resistor on that input is a cheap defence.[412]

## Mating cycles and wear

Connectors are sold in different grades of gold plating, with contact coatings specified in thicknesses such as 5, 10 and 20 microns, and thicker plating buys mating-cycle life at higher unit cost.[141] Rated cycle counts vary enormously by intended use. Some HDMI cable assemblies are rated for as few as 20 mating cycles, a figure far below what a user would assume from experience with consumer charging cables.[50] Connectors used for permanent internal wiring are often rated for only ten to thirty mating cycles, which is acceptable while two devices are hardwired but not once the user is given a removable cable.[340]

A rated cycle count also assumes correct insertion technique, since a low-cycle connector can be destroyed within ten to twenty insertions if it is mated at the wrong angle or with the wrong amount of force.[50] Because real-world reliability depends on repeated insertions rather than on a single bench trial, a custom connector justifies building a dedicated rig that mates the part automatically.[380] Contact corrosion is another common way connector knowledge is learned the hard way, as submerging a cable assembly or leaving it exposed in a high-humidity environment degrades the contact interface.[708]

## Cost and the supply base

Connector cost frequently dominates silicon cost on a board: a 16-channel data acquisition chip can cost around three dollars while a bulky plastic connector on the same design costs seven.[170] In some industries a connector price of around $200 per unit is routine, so interconnect can be a first-order line item in the bill of materials rather than a rounding error.[491] Connectors qualified for military and emergency-services equipment can cost hundreds of dollars each, with prices around $900 per connector reported for such programmes, and unit prices of around $2,000 occur on specialised products, driven by low production volumes together with the testing and certification burden rather than by material content.[227] Navy-specified connectors are typically sole-source, all-metal parts made by a single approved manufacturer, which is a large part of why their unit price reaches hundreds of dollars.[491] A very expensive military connector is not automatically the highest-quality part available, since its price often reflects a long custom specification document written for one application rather than superior contact design.[491] Letting purchasing chase a tenfold price reduction on such a part is a route to grey-market or counterfeit components, with the consequences surfacing only after the units are built.[491]

Unit prices at the commodity end track the gold price directly, because the plating on the contacts is a real material cost, and a rise in bullion prices moves a one-dollar part to roughly a dollar twenty.[141] That end of the market is heavily contested, with very large numbers of Shenzhen manufacturers building the same low-end part and each aiming to work its way up into higher-margin niches.[164] Consolidation has also touched the top of the industry: Molex, among the largest connector manufacturers in the world, was bought by the Koch business interests, bringing a major share of the interconnect supply base under a new owner.[164]

Connector manufacturers build many of their parts to order from large permutation spaces of pin counts, orientations and platings, which is why their catalogues contain vastly more part numbers than are ever stocked.[531] Certain families are chronically scarce regardless: fifty-mil-pitch 100-pin board-to-board connectors used for daughterboard modules are expensive and hard to source, and a design needing a mating pair of them carries that supply risk twice over.[628] Where an assembly house is out of stock of a connector, one workable response is to omit it from the assembly order and hand-solder the part later rather than delay the whole build.[700]

### Second sourcing

Connectors are harder to second-source than passives because compatibility is physical rather than electrical: a resistor can be moved from 0603 to 0805 with little consequence, while a connector change propagates into the mating part and the harness.[178] A second-source connector is never an exact duplicate of the original and must be fully re-characterised; purpose-built automated insertion jigs mate the part a thousand times at varying angles to measure gold wear and expected life.[178] Once a local shop has been paid to tool a connector it becomes the sole source and can raise prices, because re-tooling elsewhere means paying for tooling a second time and repeating the qualification work.[178]

Substitution can also defeat the safety features of the original part. Third-party housings with slightly undersized keys allowed a two-by-two power connector to be forced in reversed, which was not possible with the genuine part.[412] Field failures traced back to connectors are often multi-factor in this way: subcontracted cable assembly, a slightly different production housing, remote installation and untrained assemblers each looked harmless alone but combined to produce a repeatable dead-input failure.[412]

## Keying and mis-mating

The Molex Micro-Fit is a 3 mm pitch two-by-two power connector that latches and is keyed so that it cannot be mated the wrong way round, which is why it is chosen where board space is tight and reverse mating would be destructive.[412] Effective keying works partly through tactile feedback: on a correctly toleranced housing an attempted reverse insertion feels obviously wrong, and the latch also sits in the wrong place, which stops an assembler before damage occurs.[412] Military and aerospace equipment consolidates many links into one multi-way circular connector specifically so that a technician reconnecting a system after maintenance cannot plug the wrong cable into the wrong place.[496] Conversely, reusing a standard housing for a non-standard interface, such as an RJ45 that is not Ethernet, invites a user to plug in a genuine cable and creates a mis-mating hazard that no marking fully removes.[636]

## Layout and mechanical integration

Connector manufacturer drawings are rarely dimensioned from the part centre, which makes placing the footprint origin awkward and forces the designer to derive pin positions from edge dimensions.[620] Dual-row plastic header bodies frequently measure wider than the manufacturer's published dimension, so mechanical clearances around them should be checked against physical samples rather than the datasheet alone.[378] Double-row pin headers are generally at least five millimetres wide while single-row equivalents can be found under two and a half millimetres, which constrains board edge space on small modules.[378] Mixed imperial and metric dimensioning causes stack-up errors of the same kind, since enclosures built to 19-inch rack standards force fractional-inch standoff heights that do not line up with metric connector stack heights.[518]

Placement errors are easy to miss. A connector footprint can be placed with the component rotated exactly 180 degrees while still appearing perfectly aligned on the board, a layout error that no automated design check catches.[682] Even a first revision with no electrical mistakes usually needs a respin, because manufacturability and access in deployment reveal that some connectors should be placed differently once the design is viewed from the user's side.[661] Panel and board cutouts around connectors are routinely adjusted by fractions of a millimetre after first production, for example enlarging a hole by 0.2 mm where there is insufficient margin and a mounted part wobbles.[176] Where a design is built around an off-the-shelf enclosure, the specification may instead be cut to fit the case, for example dropping from four front-panel connectors to three rather than commissioning custom tooling.[50]

Process temperature is a further mechanical limit: connector housings can be melted by an over-hot reflow or rework profile, so the temperature rating of the plastic body constrains the process window as much as the solder alloy does.[558] Removing a through-hole connector without damaging the board is done by breaking away the plastic housing first and then desoldering the individual pins one at a time, which leaves the pads reusable.[493]

## Architectural consequences

A modular architecture always requires many connectors, and high-density parts such as an 80-pin Hirose board-to-board series push the unit cost of a modular system well above an equivalent monolithic board.[383] Building a product around an off-the-shelf single-board computer transfers cost into the interconnect in the same way, since extra circuitry has to be plugged in through additional connectors, producing an awkward stacked form factor that is hard to mount.[282] The trade can also run the other way: splitting one large board into smaller boards joined by high-density board-to-board connectors can be cheaper overall than a single oversized bare PCB, even at a couple of dollars per connector against a hundred-dollar panel.[502] High-density interconnect at the fine end uses parts such as a 100-position Hirose series at 0.4 mm pitch, arranged as 50 contacts per side and requiring a mating pair on each board.[563]

On small boards the interconnect can be the dominant constraint. On a daisy-chained modular board the connectors, rather than the firmware, were the hardest design problem, because the interconnect must not dominate the board outline.[330] Fitting seven four-position connectors onto a 30 by 60 millimetre board while carrying close to one amp per link constrained the choice to parts compatible with 26 AWG wire, since the chain had to power a servo at its far end.[330] At the opposite extreme, a development board can be built with no connectors at all, with programming and sensor access carried over Bluetooth Low Energy so the module is entirely wireless and cannot be plugged into anything.[226]

Whether to use connectors throughout or hardwire cables is a long-standing product-design decision: hardwiring saves unit cost, but soldered-in cables must be desoldered before boards can be separated for service or analysis.[534] For test fixtures where peripherals are connected and disconnected repeatedly, a pluggable connector gives a more reliable joint than a ribbon cable that has been hand-soldered and desoldered several times.[534] Debug interfaces show the same trade in pin count, since a 20-pin header exposes full trace information while a five-pin JTAG or two-to-three-pin SWD footprint still yields useful but reduced access.[373]

## Finding and specifying parts

Experienced engineers commonly recognise a connector on sight while being unable to recall its name, which makes visual catalogues and image-based searching more useful than text search for interconnect parts.[208] Some parts have no accepted generic name at all: the insulation-displacement connector crimped onto the end of a ribbon cable is one, which is part of why interconnect is hard to search for by description.[708] The existing literature does not close the gap, being written by connector designers rather than connector users, leaving no single reference covering the full range of interconnect from the specifying engineer's point of view.[708]

Image search is therefore a practical route, typing the closest description such as the interface family and scrolling the results visually.[154] The method works better with more descriptive attributes assembled first, such as orientation, pitch and mounting style for a right-angle two-millimetre-pitch edge connector.[294] Another approach is to find any vendor making something similar, learn the family term they use for it, such as mezzanine connector, and search on that term to reach the correct product category.[294] Where the mating part is already known, searching on that part's own name together with the word connector and reading a published schematic is faster than working down a classification tree.[708] Keeping a mental library of connectors encountered in teardowns and catalogues pays off later, since knowing that a suitable part exists avoids designing a custom connector or settling for a worse solution.[294] Handling physical samples conveys scale, latch feel and mating action in a way distributor listings cannot, which is why sample cases carried by manufacturers' representatives remain a useful selection aid.[585]

The availability of cheap ready-made cable assemblies is itself a reason to specify a particular connector, since five-centimetre jumper leads sold five to a pack for under a dollar remove all in-house harness work.[277] Keeping pin headers, both straight and right-angle, in dedicated standing lab drawers rather than in per-project bags keeps interconnect stock available across projects instead of being consumed by one build.[606] Fitting a mating two-pin pluggable pair to battery and switch leads, rather than soldering them directly, keeps the joint serviceable, and pre-crimped wires inserted into two-pin housings are the stock item that makes this practical.[606]

## Harnesses and documentation

An automotive wiring harness drawing documents the connectors and the diameter and length of each branch bundle rather than individual wires, with separate prints giving the pinouts of each connector.[620] Automotive harness contacts are retained by small barbs, so removing or replacing a pin requires the manufacturer's dedicated extraction tool rather than improvised pulling.[620] Large vehicle manufacturers historically sourced their harness connectors from a single key in-house supplier, which later branched out to serve other automotive makers and held all the connector prints and pinouts.[620] Insulation-displacement ribbon-cable termination depends on a proprietary hand tool costing around $150, of which a workshop typically owns exactly one, making the tool a bottleneck for harness work.[708]

Multi-way military connectors carrying hundreds of individual pins require a wiring drawing that documents every pin, since unlike a structured interface such as Ethernet there is no implicit pairing to fall back on.[496] Hand-terminating one such connector takes on the order of one to two hours, a labour cost that dominates the harness build.[496]

## Test and measurement

Calibrating a test fixture models the leakage, attenuation and phase shift of its wiring and connectors up to the measurement plane, so the fixture's contribution can be backed out and only the device response remains.[465] The recommended sequence for a network measurement is to connect and measure first with no calibration, sanity-check the result, then adjust cables, connectors and adapters and wiggle the part to confirm stability, and only then calibrate.[533] That uncalibrated first look catches gross errors: an amplifier connected backwards shows up immediately as gain and isolation swapping sign, for example minus 30 dB of gain with plus 30 dB of isolation.[533] Cheap online-sourced RF cables vary enough in quality to corrupt measurements, so a common bench practice is to physically segregate characterised good cables from unverified ones.[465]

Connectors also feature in improvised test tooling. A low-cost equivalent of a spring-pin programming connector can be made by soldering pogo pins to a connector body and moulding hot glue around the joint to form a handle.[454] Making a breakout board for every component used, fanning out to 2.5 mm pin headers, allows fine-pitch parts such as sub-millimetre BGAs to be exercised on a breadboard before committing to a layout.[454] In repair work, instruments returned as faulty are sometimes found to have nothing more than an internal connector deliberately unplugged, which is why reseating internal connectors is a first step before deeper investigation.[643]

## History

The S-100 bus took its name from the 100-pin connector used in the MITS Altair; because the machine was an open design, other manufacturers standardised on that same connector and called the result the S-100 slot.[27]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 27 | 555 Contest, Computer Museum, Octopart - The Green Pen Hornswoggle | https://theamphour.com/the-amp-hour-27-the-green-pen-hornswoggle/ |  |
| 50 | Callow Cough Coverups | https://theamphour.com/the-amp-hour-50-callow-cough-coverups/ |  |
| 141 | FPGAs, Robots & Thermocouples - Wampum's Wavering Worth | https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/ | April 15, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ | September 23, 2013 |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 208 | An Interview With Nadya Peek - Gallant Gcode Gerontology | https://theamphour.com/208-an-interview-with-nadya-peek-gallant-gcode-gerontology/ | July 21, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 227 | Space Bound, Again - Xtreme Xtraplanetary Xenonosocomiophobia | https://theamphour.com/227-space-bound-again-xtreme-xtraplanetary-xenonosocomiophobia/ | December 8, 2014 |
| 240 | Compare and Contrast Tech Entitlement - Worldly Working Wonks | https://theamphour.com/240-compare-and-contrast-tech-entitlement-worldly-working-wonks/ | March 10, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 282 | 3D Product Logistics | https://theamphour.com/282-3d-product-logistics/ | January 13, 2016 |
| 294 | Live from Serbia with Mike Harrison | https://theamphour.com/294-live-from-serbia-with-mike-harrison/ | April 13, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 380 | Just Terrestrial and Space Things | https://theamphour.com/380-just-terrestrial-and-space-things/ | February 18, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 425 | An Interview with Chris Osterwood | https://theamphour.com/425-an-interview-with-chris-osterwood/ | January 13, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 491 | The Almighty Dollarydoo | https://theamphour.com/491-the-almighty-dollarydoo/ | May 3, 2020 |
| 493 | PITA Package | https://theamphour.com/493-pita-package/ | May 17, 2020 |
| 496 | Drab Olive | https://theamphour.com/496-drab-olive/ | June 14, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 533 | Microwave measurement with Joel Dunsmore | https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/ | March 7, 2021 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 558 | Toasted Marshmallow Connectors | https://theamphour.com/558-toasted-marshmallow-connectors/ | September 19, 2021 |
| 563 | Grumpy Collaboration | https://theamphour.com/563-grumpy-collaboration/ | October 24, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 585 | Return of the Trade Show Jedi | https://theamphour.com/585-return-of-the-trade-show-jedi/ | April 10, 2022 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23, 2022 |
| 620 | Engineering Education with Dr Don Wilcher | https://theamphour.com/620-engineering-education-with-dr-don-wilcher/ | February 20, 2023 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
| 643 | Calibration & Repair with Ian Johnston | https://theamphour.com/643-calibration-repair-with-ian-johnston/ | August 22, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
| 708 | All the Connectors with Davide Andrea | https://theamphour.com/708-all-the-connectors-with-davide-andrea/ | November 1, 2025 |
