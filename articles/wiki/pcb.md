---
title: PCB
concept: pcb
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A printed circuit board (PCB) is the laminated substrate of copper traces, planes and dielectric on which electronic components are mounted and interconnected; its function is to execute the schematic faithfully, such that the ideal board would have traces of zero length with no resistance, inductance or capacitance, and every real board is an approximation measured by how close it gets to that ideal.[626] The board occupies one stage of a size hierarchy spanning roughly six orders of magnitude, from a 14-nanometre transistor through a 70-micron die pad, a package trace and a half-millimetre BGA pitch up to an eight-mil board trace.[469] Because every electronic design requires a board, PCB fabrication became the first custom-manufacturing market organised around online upload-and-checkout ordering, and low-cost pooling services removed cost as a reason to build circuits any other way, leaving only the turnaround time of a week or two as the counter-argument.[400][110]

## Fabrication services

The commercial model for prototype and low-volume boards shifted from emailing Gerber files, waiting for a quotation and paying manually to uploading files and checking out online; the market formed around boards rather than other custom mechanical parts because every design needs one.[400] The low prices of pooling services derive from sharing a fabrication panel among many customers, a practice low-cost factories typically perform without disclosing it; a service that shares panels openly allows a design built on the most common stack-up to move through the queue faster.[337]

Board fabrication is specified rather than selected from a fixed menu: material, impedance and dielectric constant can all be stated and the fabricator will attempt whatever is asked, though there are few settled standards and the manufacturer understands its own process better than an occasional customer does.[387] Keeping a board to a standard size makes vendor pricing directly comparable so that the cost effect of each option is visible; a finish such as ENIG buys flatness and quality but can triple the price, while solder mask colour is usually free.[457] For small boards, cost is dominated by tooling rather than area: a hundred small flexible boards have been quoted at seventy-seven dollars, with no saving in ordering ten instead of a hundred.[468]

A fabricator's panel option generally means the fabricator decides the panel layout, which is usually not what the customer wants, since control over how boards are arranged and separated belongs with the designer.[176] Fabricators also modify customer files as part of their process, adding rails and tooling features, and that editing step can corrupt data: in one case a via lost information and was placed on the wrong layer, producing a short the designer never drew.[682]

### In-house fabrication

Bare boards are a commodity purchase, which is why in-house fabrication is now rare. Milling only isolates traces from the surrounding sea of copper, leaving large copper areas that short easily, and aligning drills and forming vias remains the hard part of the process.[345] Etching boards at home additionally imposes a chemical disposal problem — the spent etchant contains dissolved copper — that a paid service absorbs, which is a practical argument against home processing independent of quality.[66]

### Output generation and transfer faults

Scripted manufacturing-output generation can fail silently: a four-layer board was exported with only two layers because the output job was misconfigured, and the fault surfaced only when the fabricator's upload preview disagreed with the design.[434] Fabricator preview tools also reject some legitimate output; inner plane layers exported as negative images did not render, a class of problem discovered at upload rather than at design time.[434]

## Layout practice

Layout quality is judged by how faithfully the physical board realises the schematic, since every trace adds parasitic resistance, inductance and capacitance absent from the ideal circuit.[626] An automated layout tool carries an obligation to know and state its own limits, warning the user when a design exceeds what the tool has been proven to handle rather than silently producing a result.[626]

Layer count multiplies board cost, so a twelve-layer design forces the team to conserve area and drives the board as small as possible.[316] Where a design contains an FPGA, swapping pin assignments so signals emerge near their destinations is what keeps layer count down; without that freedom a high-layer-count board becomes the realistic option.[181]

Fine-pitch packages arrive with an assumed fabrication process: a package specified for high-density interconnect carries an official recommendation of via-in-pad with 0.2-millimetre vias on a 0.1-millimetre drill, filled and plated, which puts prototype cost into the thousands and forces designers to work around the recommendation when the package is the only one that fits the form factor.[395] Where a package's important pins sit deep inside the footprint, one workaround routes over the unused pads and covers them with solder mask, trading unused input-output for access to the pins that matter.[395]

Board design remains a craft learned by accumulating examples rather than from a single authority: there is no one correct layout and no definitive text, so practitioners build a mental library of patterns from reviewing other people's boards.[494]

## Board construction and materials

Standard board thickness is 1.6 millimetres, which is why card guides and separators are made to that width.[555] A standard process gives the designer roughly five visual materials to work with — bare substrate, copper, solder mask, silkscreen and the surface finish — which constitutes the entire palette available for decorative work.[587]

Standard epoxy-glass laminate has reached its frequency ceiling, ending a long period in which ordinary board material served ever-faster designs.[165] Printed conductive traces on fabric and other flexible substrates have resistance measured in ohms per inch, restricting them to sensing and low-current signals rather than power, and printing rigid boards with the same technology is not worthwhile.[172] Printing circuits onto contoured plastic competes with simply ordering a flexible board, which is already copper on plastic, so the case for the printed process rests on geometry rather than on the conductor.[415] Machines that deposit circuit traces produce a real board but not a replacement for a fabricated one.[406]

## The board as a component

Inductors, transformers and antennas can be formed from copper traces on the board itself, and because the copper is being etched anyway they cost nothing but area.[76] A heating element can be implemented as an inner-layer copper trace routed as a zigzag and brought out to high-current tabs, with resistance and target temperature calculated in advance so the board is not delaminated by its own heater.[617] Internal layers can also serve as the windings of a magnetic component, with a ferrite passing through the board and the coils formed in copper, yielding a very low-profile part.[432]

Exposed-copper artwork can be made electrically useful by placing a via into each exposed area and relieving the solder mask only on the opposite side, turning a decorative pattern into a grid of contact points.[275] Backlighting through the board is done by clearing copper through the whole stack so a rear-mounted LED shines through the substrate, while a thin ring of copper is left around the shape and plated so the illuminated icon has a defined edge; the appearance differs between ENIG and hot-air-levelled finishes.[622] A board can also be designed as a prototyping substrate rather than a product, carrying a repeating grid of vias so that placement equipment has something to build onto without a project-specific layout.[710]

## Mechanical integration

An electronics designer left to define the mechanics will produce a rectangular board with sharp corners, convenient dimensions and generous spacing; in consumer products the industrial design is fixed first and the board shaped to it, a different discipline from optimising for layout.[447] Mechanical modelling has accordingly become part of the electronics job, because a three-dimensional model of the board is what proves it fits the enclosure; parametric modelling makes the relationship formulaic, linking board dimensions to other components rather than fixing them by hand.[379] The two quantities that electrical and mechanical design tools have historically had to keep synchronised are the board outline and the component positions.[471]

## Prototyping and production

### Sequencing and prototyping strategy

The sequencing rule for a new product is to get the board working on its own before it is put into a case, just as a constrained build gets the minimum path working before anything is bolted on.[287] Prototype discipline varies widely: some designers will not build anything short of a final-quality board and bill of materials even for a one-off, and there is a real step in rigour between a first prototype and a run of a hundred.[291]

During a component shortage the working rule became not to order boards until the parts for them are physically in hand, because availability at design time is no guarantee of availability at assembly.[570]

### Scaling to volume

A design that works at a hundred units may fail at a hundred thousand, because a small build draws all its components from one reel while a large build spans many: parameters such as transistor threshold voltage shift across reels and across second sources, and a good design is insensitive to that spread while a marginal one stops working when an unlucky reel arrives.[279] In volume production a defect compounds by the hour, because the line keeps producing the same fault while the fix is being worked out, which is why responsiveness matters more than at prototype scale.[279]

Hardware economics differ from software in shape: an initial tooling investment is followed by a substantial per-unit cost of parts and board, which fixes the margin regardless of how many units are sold.[152] Making the placement cost of each part visible changes design decisions: at three dollars thirty to place a forty-four-pin package, a designer can knowingly trade extra board area against assembly cost, and a house part that is cheaper at low volume may be dearer than a specified part at a thousand units.[243] Designing to a cost target can be run backwards from distributor pricing: choosing a one-cent regulator, a one-cent amplifier and a three-cent microcontroller leaves the remainder of a one-dollar budget for the board itself.[625]

### Test fixtures and latent defects

Test fixtures impose mechanical load: each pogo pin exerts tens to hundreds of grams of force, so a fixture with a couple of hundred pins presses hard enough to crack the board or micro-crack multilayer ceramic capacitors if the jig is not designed to support it.[585] Such fixtures can be bought cheaply without a formal data package: a shop making pogo-pin fixtures will build one from the physical board with the required holes marked in red pen, asking for no Gerbers.[355]

Tin whiskers grow out of a perfect solder joint over time and bend across to the adjacent pin, producing shorts that are not a workmanship defect and cannot be inspected out at build time.[578]

## System partitioning and modularity

Splitting a system across several boards joined by connectors is often driven by schedule rather than engineering: a front-end board can be finished and demonstrated at a design review while the rest is still in progress, and only sometimes is the split forced by maximum board size.[277] Once a prototype assembled from development boards must be built in quantity, putting everything on one board and resolving the connectors is far easier than replicating a stack of modules and cabling for every unit.[524] A middle path keeps off-the-shelf sensor breakouts but replaces point-to-point wiring between them with a simple custom board carrying only headers, so that a five-board order is the entire production run for a demonstration unit.[604] Products are frequently the evaluation boards condensed onto one custom board, and the decision to design a part in directly rather than buy a module turns on volume and on wanting to omit what the module includes, such as its own microcontroller between radio and host.[614]

A design-tool vendor once pursued a vision in which nobody would lay out a custom board again, with pre-laid-out functional modules dropped into a design; the flagship development board was sold at four thousand dollars with the FPGA and software tooling bundled and the board layout tool deliberately excluded.[555] The argument for modular electronics is that a switching power supply has been laid out a million times and should be reused as a block rather than redrawn; the argument against is that a real product's constraints rarely let a fixed module drop in unchanged.[565]

## Boards and advanced packaging

Chiplet integration and board integration solve the same problem at different scales: a board glues silicon to silicon through packages, bond wires and layers of laminate with all the associated capacitance and inductance, and the primary advantage of doing it in a package instead is miniaturisation.[499] Packaging several dies into one module removes intermediate steps in the size hierarchy, and the direction of travel is towards connecting dies to each other directly rather than through balls, packages and board traces; the offsetting loss is the ability to swap parts, since chip design remains far less accessible than board design.[469] Used silicon reaches the market as fragments of board: sellers cut chunks out of scrapped equipment with the expensive chip still attached, leaving the buyer to remove and reball it.[469]

## Open hardware and copying

Open source hardware requires releasing the board and schematic files, not only the software; publishing code alone does not meet the definition.[55] For an openly published design the only real protection is a trademark on the name, because the board itself, and everything on it, can be copied lawfully.[6] A bare board is far easier to clone at high quality than a complete product with its plastics and custom connectors, so mechanical complexity is a practical deterrent to copying where legal protection is not.[298]

Electronics magazines once printed the copper artwork at one-to-one so readers could etch their own boards, and some authors deliberately withheld it to remain the sole source of the board or the programmed part — an old form of the same decision open hardware makes today.[713] Taking a published open hardware project from its repository through fabrication, assembly, testing and driver installation is a substantial exercise in its own right, and the failures encountered along the way are where most of the learning is.[493] Prototype boards at the technology level of a previous-generation mobile phone now cost a couple of hundred dollars delivered, and the low-cost pooling services that opened that ecosystem were followed by competitors who priced it lower still.[501]

## Security and reverse engineering

Consumer boards have become progressively harder to attack physically: vendors stopped marking debug test points, then disabled the interfaces, and the direction is towards boards carrying one or two highly integrated devices with no accessible test points, which pushes hardware attacks down to the silicon.[346] Reverse engineering from the board itself works only while the board is simple: a single-layer or two-layer board can be traced by eye, and a multilayer board cannot, which is why published reverse-engineered schematics of popular devices are valuable.[725]

## Visualisation

Renders of boards read as artificial precisely because the model is too perfect; adding surface imperfections such as smudges, dust and scratches, and placing the board against a dark background, is what makes an image look like a real object.[695] Assembly animations of components falling into place on a board are scripted rather than posed by hand, which makes them repeatable when the design changes.[695]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 6 | Open Hardware and The Creative Economy | https://theamphour.com/the-amp-hour-6-open-hardware-and-the-creative-economy/ | |
| 55 | Shonky Stiver Stultiloquence | https://theamphour.com/the-amp-hour-55-shonky-stiver-stultiloquence/ | |
| 66 | Magnets, China & IEEE - Xenomorphic Xerox Xebec | https://theamphour.com/the-amp-hour-66-xenomorphic-xerox-xebec/ | |
| 76 | Fremescent Floccose Fortification | https://theamphour.com/the-amp-hour-76-fremescent-floccose-fortification/ | January 2, 2012 |
| 110 | Armstrong, Camenzind & Museums - Outstanding Oneirophoros Obituaries | https://theamphour.com/the-amp-hour-110-outstanding-oneirophoros-obituaries/ | August 26, 2012 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ | |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 275 | No One Even Missed Us? | https://theamphour.com/275-no-one-even-missed-us/ | November 19, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 279 | Merry Keyzermas! | https://theamphour.com/279-merry-keyzermas/ | December 22, 2015 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 291 | Artificially Intelligent Party Platform | https://theamphour.com/291-artificially-intelligent-party-platform/ | March 16, 2016 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 345 | Milling About | https://theamphour.com/show-345-milling-about/ | May 30, 2017 |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 355 | The Internet of Septage (with Akiba) | https://theamphour.com/355-the-internet-of-septage-with-akiba/ | August 13, 2017 |
| 379 | An Interview with John Saunders | https://theamphour.com/379-an-interview-with-john-saunders/ | February 11, 2018 |
| 387 | Microfichery | https://theamphour.com/387-microfichery/ | April 8, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ | |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 447 | Voltnuts for Flashlights | https://theamphour.com/447-voltnuts-for-flashlights/ | June 16, 2019 |
| 457 | Dotty Ernest Annty Frost | https://theamphour.com/457-dotty-ernest-annty-frost/ | September 8, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 493 | PITA Package | https://theamphour.com/493-pita-package/ | May 17, 2020 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ | August 30, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 578 | Histogrammic or Histomagraphical | https://theamphour.com/578-histogrammic-or-histomagraphical/ | February 20, 2022 |
| 585 | Return of the Trade Show Jedi | https://theamphour.com/585-return-of-the-trade-show-jedi/ | April 10, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 617 | Conference Room Innovation | https://theamphour.com/617-conference-room-innovation/ | January 29, 2023 |
| 622 | Building Firmware and Hardware for Trade Shows with Mike Szczys | https://theamphour.com/622-building-firmware-and-hardware-for-trade-shows-with-mike-szczys/ | March 5, 2023 |
| 625 | Gremlins in the machine | https://theamphour.com/625-gremlins-in-the-machine/ | March 26, 2023 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 695 | Making The Invisible, Visible with Sam Aldhaher | https://theamphour.com/695-making-the-invisible-visible-with-sam-aldahar/ | June 3, 2025 |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ | December 6, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
