---
title: Reflow Oven
concept: reflow-oven
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A reflow oven is the machine that heats a pasted and populated circuit board through a controlled temperature sequence until the solder melts and forms joints. It occupies a fixed position in the surface-mount sequence, taking boards from the stencil printer and pick and place and melting the solder at a very tightly controlled rate so that neither board nor components are damaged.[411] Machines range from converted domestic toaster ovens through inexpensive imported benchtop units to fourteen-foot multi-zone conveyor ovens, with vapor phase machines and bare hot plates as alternatives built on different heating principles.[344][458][608][613] Because reflow is the immediate next stop after fabrication, a bare board that cannot survive a pass through the oven is unusable in production, and a reflow oven is one of the machines that must be present before boards can be produced in house at all.[250][544]

## Machine types

### Converted domestic ovens

A toaster oven can be converted into a reflow machine without internal modification: conversion kits control the oven's existing heating element externally from the mains and add a temperature probe.[344] The controller must switch AC mains power, because the oven's heating elements draw on the order of hundreds of watts.[5] Standalone PID controller boxes for this purpose include a learn function, in which a temperature sensor is placed inside any oven and the controller characterises that oven's thermal response before profiles are run.[176] Building such a setup serves as an intermediate step between hand soldering and production equipment, even though off-the-shelf controllers already exist.[221] A controller with a graphical screen showing the current stage is preferable to bare status LEDs, since with LEDs the operator has to watch a wristwatch to know how far through ramp-up or soak a run has progressed.[221]

### Low-cost benchtop ovens

By the early 2010s small infrared reflow ovens were available on eBay for around 200 dollars, or about 250 dollars delivered to Australia, cheap enough that the hot-plate method no longer had a cost advantage.[63] Such ovens allow a programmed temperature profile including a preheat stage, a capability a bare hot plate does not provide.[63] Inexpensive imported units selling for around 300 dollars, with front-panel buttons and an LCD that draws a profile graph, are internally the same arrangement of a couple of heater elements as a converted toaster oven and suffer the same hot spots.[176]

These machines are commonly modified rather than used as delivered. The first modification made to low-cost imported ovens is replacing the thermocouple interface, because the operational amplifier front ends fitted on the stock control board are very inaccurate.[454] An identified gap in the market is a pre-modified, dialled-in unit: cheap T962-class ovens bought in quantity, reworked and resold, letting a buyer pay roughly double rather than spend time modifying an oven personally.[558] At the upper end of the benchtop range, a Mancorp machine in the five to seven thousand dollar bracket was mechanically robust and well vented but was hampered by an Android tablet interface and by profiles that were never quite right.[558]

### Batch and inline production ovens

Batch reflow ovens use a pneumatic clamshell that opens for the operator to load boards and closes on a button press, in contrast to inline ovens where boards enter on a conveyor.[411] A production conveyor machine carries boards from the pick and place through an oven that usually has five heating stages, so timing through the profile is fixed by belt speed rather than by an operator placing and removing the board as with a hot plate.[636] A used industrial oven of the kind found on a small line is around fourteen feet long with seven temperature zones top and bottom, each individually PLC controlled.[458] One widely sold industrial oven was designed largely around Apple's requirements, and Apple's bulk ordering of the same units pushed lead times for other customers out to 50 weeks.[411]

### Vapor phase

Vapor phase machines heat by immersion rather than by air. The oven boils a fluid called Galden, which boils at exactly 230 degrees and produces a vapour heavier than air, so the assembly sits in vapour fixed at that temperature and components such as BGAs and FPGAs cannot be overheated.[608] Some small manufacturers use vapor phase instead of a traditional convection oven; a limitation of lower-end machines is weak profiling, where the operator programs how much heat is applied for how many seconds rather than specifying a true thermal profile.[237] An open-source vapor phase oven aimed at small hardware offices was priced at 5,000 euros against roughly 10,000 euros for other vapor phase machines; the original design target had been around 1,500 dollars for makers and hobbyists, but required features in the system made that price unattainable.[608]

### Alternatives to an oven

Several routes reach reflow temperature without an oven. Hand assembly can approximate oven reflow by preheating the board to follow a thermal profile and applying generous flux rather than relying on the iron alone.[154] No-lead packages such as QFNs can be soldered by preheating the board, flooding the area with flux, and applying a hot air pencil so the part seats itself on the pads, and QFNs can be assembled with only a hot air gun, which gives a designer a fallback route when no oven or technician is available.[158][183] Boards with substantial copper area should sit on a benchtop preheater for a minute or two to reach roughly 200 degrees before hot-air work, because the copper otherwise sinks heat away from the joint; such preheaters cost around 200 dollars.[158]

A hot plate can be controlled to within about a degree by inching the setpoint up, and permits a microscope to be positioned over the board to watch joints reflow, which an oven's small door window does not allow.[613] It also avoids the air currents present inside a convection oven, one reason it is easier to control for single-sided boards.[613] Hot plates lose their advantage on large or complicated boards and on assemblies carrying tall components, where vertical temperature gradients develop across the parts, while ordinary low-profile assemblies reflow well.[613] Double-sided assembly is not a prerequisite for choosing a reflow process at all; ordinary single-sided surface-mount work already justifies one.[613] Some component packages tolerate hot air rework poorly and must be soldered in an oven or drag-soldered instead, which removes the alternatives from consideration for those parts.[645]

## Thermal control

Air circulation distinguishes a professional-grade machine from a radiant one. A radiant oven that does not circulate its hot air produces hot spots across the board, which is why such ovens are not considered professional-grade reflow equipment.[176] Even in a controlled machine the temperature is not flat across a board, with the centre differing from the edges, so a critical component sitting in a cooler region may fail to reflow properly even when the nominal profile is correct.[558]

Control architecture governs how closely the profile is actually followed. A conveyor oven controlled only by independent PID zones, typically two bottom and three top controllers plus conveyor speed, gives weak control of the real profile, and an uncalibrated setpoint of 280 degrees may not correspond to 280 degrees at the board.[558] The same discrepancy appears at the low end: a cheap reflow station set to a nominal 220 to 240 degrees blackened FR-4 substrate on several runs, showing that the delivered temperature exceeded the setpoint.[454] Calibrating an oven for a new paste or board is therefore empirical and normally consumes a few sacrificial boards before the profile is trusted.[558]

Profile management in routine use is lighter than the calibration effort suggests. Reflow controllers commonly ship with preset profiles for distinct alloy families — two leaded formulations, several unleaded ones, and a very low-temperature bismuth alloy — because each melts at a different temperature.[558] A contract manufacturer running mixed low-volume work checks datasheet temperature limits only for unusual parts, then lowers the oven temperature for heat-sensitive components or raises it for BGA packages, selecting from a small library of already-characterised profiles rather than reprofiling each job.[243] In routine assembly the profile only needs changing when copper weight changes, such as moving to two-ounce copper, because the extra copper alters the thermal mass of the board.[716]

The payoff from profile optimisation is bounded. For roughly 90 percent of boards a perfect profile is worth only about the difference between a 0.3 and a 0.5 percent process error rate.[243] On one-off builds, visually inspecting and reworking defects is cheaper than developing a custom profile to prevent tombstoning of a single part.[243]

## Cost and ownership

Capital cost spans several orders of magnitude, from a couple of hundred dollars for a converted or imported benchtop unit to industrial lines bought second hand.[63][176] A complete used SMT line consisting of a 1996-vintage pick and place with 80 feeders, a seven-zone reflow oven and a manual stencil printer was bought and delivered for 25,000 dollars.[458] Industrial machines are engineered for high-volume production and long service life, with 20 to 25 years of service not uncommon, which is what makes second-hand equipment viable for a small manufacturer.[458] Within such a line, feeders rather than ovens dominate the placement machine's cost: a 30,000 dollar machine with feeders at 500 dollars each reaches roughly 50,000 dollars before any other equipment is bought.[458] Second-hand placement and reflow equipment demands continuous attention, since getting a machine working the first time takes a long time and keeping it working takes more.[250]

Energy is a raw input to assembly, and simply energising the heating coils is a significant recurring cost adder on top of the equipment itself.[289] Electricity cost should therefore be calculated before purchase; some units that appeared to be good deals worked out at up to 10,000 dollars a month in energy at 20 shifts a month.[299] Scrap forms the other side of the economic case: a 300 dollar cheap oven can destroy enough prototypes that the loss quickly exceeds the price gap to a controlled machine, particularly for high-end boards that would otherwise be sent to an assembly house.[608]

Surrounding automation is a separate purchase from the oven itself. Well-run assembly shops buy the automation around a machine rather than the machine alone, deciding in advance how it will be fed, loaded and unloaded on the floor.[411] Board buffers and unloaders sized to a small batch, on the order of fifteen boards, are worth installing even at low volume, since machine capital is cheap relative to the labour of manual handling.[411] This is uncommon in practice: across more than a hundred contract manufacturers and OEMs visited over one career, only about 15 to 20 had anything other than a table or a cardboard ramp catching boards as they left the oven.[411] The equipment feeding the oven has its own limits, since a manual stencil printer, where the operator holds the squeegee blades and draws them across the stencil after aligning the board by hand, is repeatable only to the extent the operator is.[411]

## Facilities and safety

Reflow ovens emit strong fumes and require extraction, so they cannot be operated in a commercial office space with no ventilation provision.[195] The air-conditioning load imposed by a production oven comes mostly from its exhaust rather than radiated heat: the oven itself is well insulated, but it pulls roughly a thousand cfm of conditioned air out through the roof.[315] Boards emerging from the machine, even after the cool-down section, remain hot enough to burn on contact and should not be picked up bare-handed.[486]

## Operational constraints

The oven's presence in the line constrains what may be built. Through-hole connectors are frequently not rated to pass through an oven and melt outright when they do, so connector temperature ratings must be checked before including them in a reflowed assembly.[558] Plastic connectors survive repeated cycles only because they contact air alone; placed in contact with a heat-retaining material such as FR4 the same plastic melts quickly, so scrap connectors must not be used as board standoffs inside the oven.[436] Printed silver-ink conductors tolerate only about 140 degrees, so a board using them cannot pass through an oven at all, which limits the technology to prototype work.[406]

Timing constrains the material as well. Once solder paste has been printed onto a board it has a limited working life and must reach the oven within about four hours, because the volatile components in the paste evaporate; pasted boards with parts on them cannot be left standing for days.[337] Low-quality or dried-out paste passes through the machine without ever properly reflowing, leaving crusty joints that resemble cold solder joints because the flux and paste have effectively gone.[716] Once paste has dried out the joint cannot be rescued by another oven pass and must be reworked with a hot plate and fresh flux.[716]

Moisture is the corresponding hazard for components. Moisture absorbed into a plastic-packaged part turns to steam as the part passes through the oven, expanding and cracking the package, with LEDs particularly susceptible.[243] Moisture-sensitive surface-mount components are therefore supplied in a hermetically sealed moisture barrier package with a desiccant bag, and the seal should not be broken until the day the parts go into the placement machine.[558] Components on paper carrier tape stored at around 60 percent humidity eventually stick to the cover tape, so the tape will not peel cleanly and the feeder jams; dry storage protects the tape as well as the parts.[243] A controlled oven is also used to bake moisture out of components before assembly, though using a reflow oven for unrelated drying tasks such as 3D printer filament risks contaminating a machine that must stay clean.[558]

## Use in repair

Putting an entire assembled board back through an oven is a last-resort repair for a suspected bad BGA joint, with a low and unpredictable chance of fixing the fault.[203] Reflowing a failed BGA in a toaster oven does not permanently repair the joint; at best it restores function temporarily, and an overlong dwell will destroy the board outright.[311]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ |  |
| 63 | Shop bots, 450 mm fabs & redFrog - Pick and Place Palillogy | https://theamphour.com/the-amp-hour-63-pick-and-place-palillogy/ |  |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 158 | Hyperloop, Upverter and Soldering - Unbelievable USB Ustulater | https://theamphour.com/the-amp-hour-158-unbelievable-usb-ustulater/ | August 12, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ | April 21, 2014 |
| 203 | Tesla, Checklists and Bullies - Emerging External Eupsychics | https://theamphour.com/203-tesla-checklists-and-bullies-emerging-external-eupsychics/ | June 16, 2014 |
| 221 | Warming Up To IoT - Tendentious Thermal Tools | https://theamphour.com/221-warming-up-to-iot-tendentious-thermal-tools/ |  |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20, 2015 |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ | March 2, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 311 | An Interview with Louis Rossmann | https://theamphour.com/311-an-interview-with-louis-rossmann/ | August 10, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ |  |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 344 | Back Into The Swing Of Things | https://theamphour.com/344-back-into-the-swing-of-things/ |  |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 486 | Medical Kits, They're The Future | https://theamphour.com/486-medical-kits-theyre-the-future/ | March 29, 2020 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 558 | Toasted Marshmallow Connectors | https://theamphour.com/558-toasted-marshmallow-connectors/ | September 19, 2021 |
| 608 | Vapor Phase with Saber Kaygusuz | https://theamphour.com/608-vapor-phase-with-saber-kaygusuz/ | November 7, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 716 | Electronics Manufacturing History with David Ray | https://theamphour.com/716-electronics-manufacturing-history-with-david-ray/ | February 25, 2026 |
