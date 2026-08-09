---
title: PCB Milling
concept: pcb-milling
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**PCB milling** is the fabrication of printed circuit boards by mechanically removing copper from copper-clad laminate with a small rotating bit, rather than dissolving it chemically, and therefore requires no wet chemistry.[111] The process is a form of isolation routing: the bit cuts only an outline around each conductor, leaving the unused copper in place rather than etching it away.[345][275] Its principal value is turnaround speed—small designs can go from layout to an assembled board in a single evening, and simple boards in as little as twenty minutes to two hours—which has made it a standard rapid-prototyping method in fab labs and engineering workshops despite its inability to reproduce plated through holes, solder mask, or multilayer construction.[166][176][454][208]

## Process

In PCB milling, copper is cut mechanically from the clad stock by a spinning routing or drill bit.[111] Because the bit only outlines each conductor, a milled board retains a "sea" of surrounding copper; this leaves the board easy to short accidentally during assembly but also means the uncut area can serve as a continuous ground plane.[345][106] A dedicated desktop board mill is essentially a miniaturised metal-working CNC mill fitted with a much faster spindle, suited to shallow cuts in soft substrate.[462]

The recurring setup difficulty is establishing Z height and ensuring the stock is genuinely flat, because depth of cut must be held consistently across the whole panel.[345] The mechanical figures of merit for a board-cutting machine are frame rigidity and bed flatness, both of which govern that depth consistency.[251] Software polish does not alter the underlying constraint: a spinning bit is being driven into copper, with all the tooling and depth limits that implies.[367]

### Operation sequence

Holes must be drilled before the isolation routing pass; routing the annular ring first leaves a thin unsupported pad that the drill tears off the substrate.[111] Once routing is done, the hardest remaining operations are registering the drill hits to the routed pattern and forming vias by hand.[345] Vias on a double-sided milled board can be formed manually by threading enamel wire through the drilled hole and melting solder on both faces.[686]

Solder mask can be added to a milled board by coating the finished copper and then milling the mask away over the pads, producing mask openings without photoimaging.[434] Milling the mask rather than photoimaging it keeps the whole process dry, which is the rationale for choosing milling over etching in the first place.[434] Solder mask is typically the first capability added after the mill itself, because it provides insulation between a component and the surrounding copper.[434]

## Toolchain and data formats

The toolchain runs Gerber output from the CAD package through a converter that emits G-code, and the G-code is what actually drives the router's XY motion.[223] G-code is the low-level command language positioning the milling bit in three-dimensional space; the toolchain's job is decomposing the Gerber geometry into those moves.[462] Curved traces have no native representation in the generated tool path and are approximated by thousands of tiny straight segments.[462]

The Gerber format's apertures are a survival of photoplotters that exposed film through physical wheels of differently sized holes on an XY bed, which historically limited designers to the trace widths a wheel provided.[462] The tool path must be generated for the exact bit geometry in the spindle: running a path computed for a 50-degree V-bit with a 20-degree bit in place ruins the board.[462] Producing good milled boards requires adapting the CAD layout to suit the process—tweaking the CAD output to be mill-friendly—and getting the stock genuinely flat and dialled in, rather than running the default flow.[462]

For outlines and routing data handed to a board house, clean Excellon milling paths are the industry-standard interchange format, and requests to supply outlines in proprietary formats are discouraged.[299] Some lower-end CAD packages cannot emit a proper milling path and instead fall back on a deprecated encoding that expresses the cut as a dense sequence of drill hits.[299] Some CAD tools have no native slotted-hole primitive; the standard workaround is to define the slot on the milling layer for the fab to route.[531] For board outlines and internal cutouts, drawing the feature as a single wide trace rather than tracing its perimeter is easier to edit and naturally yields the rounded internal corners a router bit produces.[162] Because fabs interpret outline data inconsistently, a common convention is to draw the inside dimension as the routing line and to state that convention explicitly in the fab notes.[162]

## Equipment

Before prototype board services existed, a commercially fabricated board cost eight hundred to a thousand dollars and took two weeks, which was the environment in which in-house fabrication could turn a board around in a single day.[341] Professional-grade LPKF board plotters occupy the established high end of the market at roughly forty thousand dollars, which created the demand for low-cost machines.[111] Purpose-built desktop PCB mills such as the Other Mill emerged as a distinct product category from general CNC routers, designed to cut boards and nothing else.[145] A turnkey PCB mill removes the setup burden of a generic CNC machine, which must be assembled, trammed, and aligned before it will cut accurately.[145]

General-purpose CNC machines produce usable copper-clad boards only at the high end of their specification range; a low-end machine will not do the job reliably.[120] The common inexpensive Chinese CNC engravers sold as the 3020 and 3040 differ mainly in bed size, the 3040 being roughly A3.[224] A machine sold as an engraver may have only about 15 mm of vertical travel, which rules out tall stock but is irrelevant for cutting PCB outlines, a task at which such machines perform very well.[224] Small CNC router tables generally have Z travel on the order of one or two inches, which suits them to wide, flat, planar work such as copper-clad board.[199] At the bottom of the price range, board milling has been demonstrated on machines costing around 150 dollars.[673] The used market lowers entry cost substantially: a four- or five-year-old desktop board mill has changed hands for about nine hundred dollars, against roughly two thousand dollars for current models.[454]

A desktop mill's practical envelope is small—roughly four by five inches—and the machine is justified when the work fits that envelope and speed matters more than board quality.[145] A shared board mill also needs an assigned operator, a staffing cost justified only at higher utilization such as a busy school makerspace.[345]

## Materials and design rules

Desktop board mills typically use FR-1 substrate rather than FR-4, because the glass-fibre reinforcement in FR-4 is abrasive enough to destroy cutting bits.[345] An enclosed mill with vacuum extraction is the health-relevant configuration when cutting FR-4, which liberates glass dust that must not be inhaled.[454] Desktop milling is generally restricted to soft FR-1, whereas additive board-printing processes can work directly on FR-4 and G10.[260]

Design rules for milled boards are coarse by fabrication standards. Designing to 8 mil trace and 8 mil space leaves enough margin for roughly a 90 to 95 percent first-pass success rate.[245] The Other Mill's practical feature size was around a 10 mil limit, and claims of 7 mil on comparable machines were treated as unproven until demonstrated.[275] Later-generation desktop mills were marketed as accepting Gerber files directly and producing double-sided boards at six-thou trace and space, but current desktop machines cannot hold five-mil trace and five-mil space, though they remain capable across a wide range of coarser designs.[345][382] Because package footprints keep shrinking rather than growing, a mill limited to coarse geometry forces every new fine-pitch part onto a breakout board first.[275]

A mill can also machine isolated circular pads out of bare copper-clad stock, producing the solderable islands used in Manhattan construction, while the surrounding uncut copper continues to serve as a ground plane for dead-bug builds.[106]

## Limitations and failure modes

A milled board lacks the features that make a fabricated board convenient: it has no plated through holes, no solder mask, and no silkscreen, so it cannot substitute for a finished board requiring controlled impedance, fine spacing, or four to six layers.[176][345] Milled prototypes can also mislead on RF designs, because the substrate and geometry give different impedances than the fabricated board that will follow.[345]

The process trades chemical mess for particulate mess, throwing fiberglass and copper dust around the machine and the room, and the machines are slower than expected, messy, and loud enough to be unpleasant in a shared workspace.[111][275] Consumables are a recurring failure point: running a job without the correct milling bits on hand ends the job early, because the wrong bits break during the cut.[223]

## Comparison with other in-house methods

Home board fabrication divides into two families: wet chemical etching, and mechanical copper routing on a milling machine, the latter avoiding chemical handling entirely.[49] Laser-based board prototyping machines substitute a focused beam for the spinning routing bit, ablating copper and cutting the FR-4 outline instead of mechanically removing it.[28] Laser ablation of copper-clad board is complicated by heat conduction, however: copper spreads the incident energy across the plane instead of confining it to the spot being burned away.[26] A milling machine also covers a wider range of materials than a laser cutter, since only a small handful of materials can be laser-cut without producing dangerous fumes.[224] Cheap laser cutters have failed not on the optics but on the motion control, with a parallel-port 8051 controller stalling mid-job and leaving the beam burning the workpiece.[224]

Against additive processes, subtractive milling cannot deposit a solder mask layer as a final step, which an inkjet-style additive process can in principle do.[275] Across milling, additive printing, and acid etching, the practical differentiator between home fabrication systems is the software tool flow rather than the physical mechanism.[251] Narrowed to the single purpose of turning out fast prototype boards, a milling machine working FR-4 remains a defensible choice against the other in-house methods.[236]

## Applications and economics

The central application is rapid iteration. An on-site board plotter collapses the design loop to a single evening, letting a small design be laid out, cut, and assembled in one session.[166] For simple single-sided analog work such as an op-amp circuit, a milled board can go from layout to finished part in about two hours.[176] A desktop mill turns a KiCad layout into a tested board in about twenty minutes single-sided or roughly an hour double-sided, against a week or two for an outside shop.[454] The engineering value lies in the number of failed boards the process permits: cheap wrong boards surface grounding and shorting mistakes that a single yearly fabricated board never would.[454] Fab labs standardise on milling for circuit boards because the process is fast, accepting that it cannot produce complex boards.[208] In the fab lab context, the commercial circuit board mill sold into the labs was judged by Nadya Peek's group to be the most expensive machine in the lab per unit of output, a judgement that motivated the group's work on modular replacement machines.[208]

A common division of labour is to mill boards only for evaluating unfamiliar ICs and developing drivers, then order fabricated boards once the design is understood; at Freaklabs, Akiba describes this as the main role of milling in his workflow.[245] RF circuits are among the hardest to synthesize with confidence, so the value of an in-house rapid board process is empirically testing whether a design behaves as predicted.[260] RF boards are also the clearest remaining case for milling specifically, since they are often mostly ground plane and therefore need very little copper removed.[406] In-house board fabrication additionally persists at firms whose contracts forbid sending Gerbers out, because outsourcing exposes the design to reverse engineering.[406] Beyond boards, a small CNC pays for itself on jigs and fixtures: drilling twenty holes at an exact pitch is nearly impossible by hand but takes minutes on the machine.[224]

The buy-versus-outsource decision reduces to a crossover calculation: divide the machine price by the price of an overnight fabricated board and ask how long it takes to accumulate that many urgent jobs.[341] With desktop mills costing around two thousand dollars against overnight fabricated turns under two hundred dollars, the crossover requires a substantial volume of urgent work.[345] The market context has shifted steadily against home fabrication: once cheap offshore fabs offered week-turnaround double-sided boards with plated through holes and solder mask for around sixteen dollars, the economic case for making boards at home largely disappeared, and two-day delivery of fabricated boards for a few dollars has since compressed it further.[33][673] Cheap fabricated boards still carry their own trade-off—a batch can arrive with defects such as a short between two tracks, shifting verification onto the buyer.[33] The desktop-mill market has been characterised as drawing engineers from software backgrounds who seek to import an iterate-fast working style into hardware development.[373]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 26 | The Ben & Jeri Show | https://theamphour.com/the-amp-hour-26-the-ben-jeri-show/ | |
| 28 | Bowie and The Brown Note | https://theamphour.com/the-amp-hour-28-bowie-and-the-brown-noise/ | February 1, 2011 |
| 33 | Bob Widlar, Electronic Design, FIRST Robotics - Monday, Meta Monday | https://theamphour.com/the-amp-hour-33-monday-meta-monday/ | |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 111 | DIP projects, OSHW & Trade Booths - Demonstrative DIP Dacrygelosis | https://theamphour.com/the-amp-hour-111-demonstrative-dip-dacrygelosis/ | |
| 120 | Prototyping, Machining & Accelerators- Mugwumps Mulling Milling | https://theamphour.com/the-amp-hour-120-mugwumps-mulling-milling/ | November 4, 2012 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 166 | Prior Art, Wafer Fabs and Guns - Whimsical Wafer Waffling | https://theamphour.com/166-prior-art-wafer-fabs-and-guns-whimsical-wafer-waffling/ | October 7, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 199 | The 2014 Maker Faire Show - Traveling Technology Trangam | https://theamphour.com/199-the-2014-maker-faire-show-traveling-technology-trangam/ | May 19, 2014 |
| 208 | An Interview With Nadya Peek - Gallant Gcode Gerontology | https://theamphour.com/208-an-interview-with-nadya-peek-gallant-gcode-gerontology/ | July 21, 2014 |
| 223 | Space Difficulties and Lost Heroes - Wanzing Workshop Whemmle | https://theamphour.com/223-space-difficulties-and-lost-heroes-wanzing-workshop-whemmle/ | November 4, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 275 | No One Even Missed Us? | https://theamphour.com/275-no-one-even-missed-us/ | November 19, 2015 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 341 | All the way with DLJ | https://theamphour.com/341-all-the-way-with-dlj/ | |
| 345 | Milling About | https://theamphour.com/show-345-milling-about/ | May 30, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 382 | The Toggle Boggle | https://theamphour.com/382-the-toggle-boggle/ | March 4, 2018 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 673 | Lifelong Learning with Bitluni | https://theamphour.com/673-lifelong-learning-with-bitluni/ | July 15, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
