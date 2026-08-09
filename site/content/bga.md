---
title: BGA
concept: bga
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A ball grid array (BGA) is a surface-mount integrated circuit package in which the connections to the printed circuit board are made through an array of solder balls on the underside of the package rather than through leads around its periphery.[362][469] Ball grid array and chip-scale packages are cheaper to manufacture than leaded packages because each ball connects directly to the substrate and no bond wires are required; wire bonding is itself the throughput constraint, since each wire is placed individually, and a second per part can be the difference between ten thousand and a hundred thousand chips a day.[16] The defining engineering parameter of the package is its ball pitch, which determines the difficulty of routing signals out of the part, the cost of the board beneath it, and whether the part can be assembled or reworked outside a high-volume production line.[362][520] The packages are designed for high-volume production, where the setup cost of getting the process right is amortised, which is what makes them awkward for anyone building in small quantities.[3]

## Construction and variants

The basic ball grid array carries solder balls on the underside of the package substrate; a chip-scale package (CSP) is named for being essentially no larger than the bare die, with the balls landing on the top layer of the die's own metallisation once it is flipped over.[502] A land grid array (LGA) is the same arrangement without the balls, using flat pads, which suits height-constrained applications because the ball's contribution to the vertical dimension is removed.[499] Wafer-level chip-scale packages (WLCSP) are small ball grid arrays produced directly at wafer level; taping out into one requires additional information about the packaging and how the balls are bonded, which an intermediary service can absorb on the designer's behalf.[616]

Fine pitch appears even on very small parts: a three-by-three millimetre programmable device carries forty-nine balls at 0.4 millimetre pitch with thirty-three usable signals, and a wafer chip-scale part measuring 1.6 by 1.6 millimetres has carried a three-by-three matrix of pads with the centre position omitted because the sensing element occupied that area.[535][53]

A system-in-package integrates processor, memory and support components into a wide-pitch ball grid array, so that a complete Linux system becomes one part soldered down with no memory routing or controlled-impedance work required, at a price close to that of a whole single-board computer.[482] Cross-sections of such packages show stacked dies, tiny internal boards and package-on-package memory forming a three-dimensional structure; packaging is where the visible innovation now sits rather than in board technology.[609] On the BeagleBoard programme, stacked package-on-package memory combined with fine ball pitch gave the board its reputation for being difficult to assemble.[59]

## Pitch and escape routing

Ball pitch is the parameter that determines everything downstream: a pitch of 1.27 millimetres is generously wide, most contemporary parts sit at 0.8 millimetres or below, and 0.4 millimetres is genuinely difficult.[362] Parts at 0.25 and 0.4 millimetre pitch cannot be escaped on an inexpensive standard prototype board process at all.[520] Ball count alone does not determine difficulty: a 676-ball part at one millimetre pitch is straightforward, while a much smaller part at fine pitch is not.[469]

Escape routing, not soldering, is the property that decides whether a package is usable on an ordinary board: a three-row 256-ball part at 1.27 millimetre pitch can have every pin escaped on the top layer with six-thousandth-of-an-inch trace and space, which puts a complete Linux-capable device on a four-layer board.[362] The significance of that property is routinely underestimated by designers evaluating a part.[362]

### Fabrication limits

A pooled prototype fabrication service could handle a one-millimetre-pitch part without difficulty, with anything finer described as pushing the process; to let customers place 0.8 millimetre pitch parts, that service raised its four-layer design rules to five-thousandths-of-an-inch trace and space with a ten-thousandth drill and a four-thousandth annular ring, which is just enough to squeak through.[149] Published design rules of that kind are the fabricator's guaranteed values rather than enforced limits, so designs violating them are sometimes submitted and built by accident.[149] A service offering an eight-thousandth minimum drill and five-thousandth annular ring is respectable for general work but not adequate for small ball grid arrays.[299] Drill size and annular ring are what drive fabrication price sharply upward on a small four-layer board carrying a 0.5 millimetre pitch part, to the point that low-cost fabricators quote thousands for the tightest values.[557]

Fine pitch also raises board cost directly, because the tolerances on solder mask registration and etching all tighten with the pitch.[67] Where only one part on a board requires fine-pitch capability, the entire board area is manufactured to that tolerance and the rest of the design carries the cost of that single chip.[502]

### Layer counts and pin assignment

High ball counts force layer counts: a thousand-pin part needs on the order of eight layers purely to route the signals out, and a six-hundred-pin part likewise dictated an eight-layer board with no possibility of fewer.[19][325] A designer constrained to four layers finds that searching for new silicon in leaded packages returns almost nothing, and the parts that remain are ball grid arrays needing six or eight layers to fan out.[116] The pin count required by a device can be wildly out of proportion to the pins actually used: a design needing only serial in and serial out was forced onto a twelve-hundred-pin part, with a twelve-layer board to route it, and the pins are where the cost sits.[181]

Careful pin assignment can keep a large part on a modest board. On the XESS FPGA boards, Vandenbout routed a 256-ball package on four layers with memory on the opposite side of the board, with two of those layers given over to power and ground; pin assignment is where the difficulty concentrates in such a design, because the requirement is to get a specific pin to a specific destination through the available layers.[181] Signal escape from the package limits how many general-purpose pins a low-technology board can expose, and was the constraint cited for not bringing more out on the Raspberry Pi, which used a deliberately low-tech PCB.[97] An image sensor in a package designed for mobile telephones forced a design that would otherwise have fitted on two layers onto a four-layer service, purely because the two-layer process could not hold the fine trace and space needed to route the part out.[502] Dual-row packages with a large central thermal pad present the same escape problem, with the vendor's suggested layout calling for blind and buried vias that raise board cost substantially.[502]

### Via strategies and pad design

At 0.4 millimetre pitch, a part with three rows of balls can still be escaped and manufactured cheaply; beyond three rows the design requires laser-drilled vias, on the order of a 0.15 to 0.2 millimetre drill.[59] An 81-ball part at 0.4 millimetre pitch is specified for a high-density interconnect process using via-in-pad with roughly 0.2 millimetre vias on a 0.1 millimetre drill, filled and plated, which is prohibitively expensive at prototype quantities.[395] On his own fine-pitch FPGA design, where that process was unaffordable, Valenty routed over unused pads and covered them with solder mask to reach buried signals, placed a via in the centre of two-by-two groups of pads, and narrowed the outer row of pads to 0.1 millimetre while elongating them to 0.35 millimetre, preserving roughly the same surface area for the ball to wick to while opening a gap for traces to pass.[395] The pill-shaped pad gains no area over the original circle; the gain is entirely in the reduced width, which is what allows a track to escape between pads.[502] Valenty's own recommendation after doing it was that others should not repeat it: a larger package, and specifically 0.8 millimetre pitch, is dramatically easier and escapes by conventional means on four layers.[395] Yield is a further consequence of fine pitch: his small board built around the package had a low enough assembly yield that its maker would only produce more in bulk quantities.[395]

Solder mask can be pulled slightly over the pad edge to help align the ball and to help the solder fill correctly, a technique used where via-in-pad is unavoidable because of density.[393] The ball's specified size is its widest dimension, while the actual contact area on the pad is smaller because the ball is a sphere that necks down where it meets the pad.[393] Whether pads are defined by the solder mask opening or by the copper is a genuine choice, and one worth testing empirically before committing a design; Grover's in-house prototyping work treated it as an open question to be tested.[454]

Where the array is fully populated, giving up top-layer routing costs roughly one and a half pin rows of escape; the preferred remedy is blind and buried vias rather than simply adding layers, because through vias consume routing space on every layer they pass.[439] Substituting a switching regulator can cascade into a package change from a leaded part to a ball grid array or wafer-level package, which in turn forces blind and buried vias and a much larger qualification effort.[601]

### Routing effort and tools

The manual effort scales with ball count: a thousand-pin part with every pin in use means roughly a thousand traces and a thousand vias to place, multiplied by however many times the routing is torn up and redone.[316] That effort is what makes autorouting economically interesting for these parts, with a topological router that lays traces as a person would rather than on a grid able to route a package in hours where manual work takes days.[46] Dense multi-package boards have been laid out successfully in hobbyist-tier tools, but time spent compensating for a tool's limitations is time not spent designing, which is the argument against pushing a tool past its comfortable range.[162]

## Assembly

The package is self-aligning during reflow: surface tension pulls the part into position over the pads, which makes placement accuracy less critical than it appears.[291] Self-alignment weakens as the package grows: a ball grid array is heavy enough that surface tension helps less, whereas a wafer-level chip-scale part is so small and light that it behaves more like soldering a resistor.[501] Where paste can be screened through a decent stencil, the package is among the easier components to solder precisely because of that surface tension.[471]

### Stencils and paste application

Laser-cut polyimide stencils have a floor of about five thousandths of an inch in every direction, below which the plastic melts back over the opening instead of cutting through, though people routinely use that limit for fine-pitch parts; a laser-cut polyimide stencil can nonetheless be produced for essentially any package including ball and land grid arrays, with high pin count leaded packages presenting more difficulty than the arrays.[320][153] Stainless steel stencils are the better choice for the same work: they are flatter, dimensionally consistent, align more precisely and release paste better, producing fewer bridges and stray solder balls than film.[320] The economic case for the better stencil is rework avoided: a single bridged joint costs hours, and a bridge hidden underneath the package is worse still.[320]

The single most important variable in hand-pasting is using too little rather than too much: a small amount of paste is enough to make a connection, whereas excess causes shorts beneath the package that cannot be found visually, and shorts under the part are the characteristic failure of over-pasting.[291] Paste application is the process step that limits assembly quality, and hand stencilling is inconsistent enough that pressure variation leaves individual pads without paste to reflow.[458] On one fine-pitch design assembled by hand, three boards were built and one worked.[692]

A stencil ordered alongside a board can be cut from an earlier revision than the one finally fabricated, so the stencil no longer matches the board it was bought for.[692]

### Placement and reflow

A modern automated printer with an under-stencil wipe improves paste quality enough to make consistently smaller parts feasible, and a contemporary placement machine handling thirteen thousand placements an hour will place very fine ball grid arrays.[458] Benchtop assembly machines aimed at prototype work cover 0402 passives and 0.4 millimetre pitch leaded parts, with users reporting good results placing 0.5 millimetre pitch ball grid arrays; on the LumenPnP project, such placements were the reported experience of users of the machine.[686] Vapour phase reflow includes a hold at around a hundred and twenty degrees Celsius to vaporise residual fluid off the board and out from underneath components, so no droplets are left between the balls.[608]

A ball grid array in the assembly is one of the standard reasons a designer outsources a board rather than building it themselves.[243] Prototyping methods that stop short of a professionally fabricated board are ruled out by the packages in current use, since a ball grid array has to be reflowed and cannot be worked by hand-etched means.[260] Milling a board in house can reach these packages: on Grover's prototyping work, a spring-mounted engraving tip with a very small point allowed leadless parts and light ball grid array work, including four and six ball parts at around 0.35 millimetre pitch.[454] Soldering to an individual pad of a one-millimetre-pitch package by hand is achievable, and is in fact easier than doing the same on a 0.5 millimetre pitch quad flat pack.[120]

## Inspection and test

X-ray inspection is useful for the obvious defects such as a short between adjacent balls, but is not effective at finding an intermittent or merely poor connection.[237] A small operation without x-ray equipment instead controls the paste process, budgets for a failure rate on the order of one in ten thousand and discards or reflows the failures rather than diagnosing them.[237] Boundary scan through the debug interface verifies that every ball on a large package is connected and not shorted to its neighbours, which substitutes for x-ray equipment where none is available.[482]

Mounting the package on a flexible circuit with no stiffener allows the joints to be inspected through the translucent film from the back, showing every ball directly; Allen used this technique in his Shenzhen hardware work, and holds that without inspection equipment full verification is impractical, but electrical test is frequently sufficient in practice, and the package is not inherently difficult to work with.[414]

Computed-tomography inspection reconstructs the assembly in three dimensions and re-slices through it, revealing detail such as voiding inside the solder joints.[631] The part has to be held at a deliberately non-orthogonal angle during such a scan, because viewing straight along a row of balls means the nearest ball blocks the path to the ones behind it.[508]

Custom test sockets for these packages run to thousands of dollars, must align perfectly across every contact, and degrade measured performance, so a distortion figure taken through a socket may look poor for reasons that have nothing to do with the device.[452]

## Rework

In hot-air rework the temperature is controlled by hand through nozzle distance and angle rather than by the setting on the station, with a quarter of an inch of nozzle movement worth roughly thirty degrees at the board.[311] The variables that actually determine the outcome are the element temperature, the airflow setting, the nozzle size and angle, the surrounding components and how well the board sinks heat.[311] In Rossmann's repair practice, a thermocouple placed on the part is used when replacing a very large package of several hundred balls, and is not practical for smaller work where hand control suffices; large processors and graphics parts require a preheater under the board with hot air above, or a professional rework station, while a ninety-ball part or one with 0.25 millimetre balls is achievable with ordinary hand rework equipment.[311] Replacing a very large package is uneconomic even where it is possible, because replacement parts of that class come only from doubtful sources and a forty-minute operation that fails leaves nothing to show for it.[311] Rossmann's experience is that becoming comfortable with a microscope is what removes the difficulty, since tilting the board reveals the balls underneath the package and makes the joint quality directly visible, and that rework skill decays without regular use, to the point that an engineer who has not used hot air for several months practises before attempting a real part.[311] The corresponding advice is to build soldering skill on low-risk work rather than on the board that has to work tomorrow, because running a bodge wire out from under a package is a high-risk operation to attempt for the first time under pressure.[473]

A design-review service can flag layout hazards specific to the package, such as a ball grid array placed close enough to a capacitor to cause thermal shadowing during reflow.[545]

## Design strategies

Where a single fine-pitch part would otherwise set the tolerance for a whole board, the remedy is to isolate the difficult part on a small module with castellated edges or a board-to-board connector, since a one-inch square high-specification board plus interconnects is cheaper than manufacturing a large board to the same tolerance.[502] A commercially bought module carries the same benefit with the tight tolerances and often the regulatory certification already paid for, at the cost of the module's price premium.[502] Escaping a package on four layers rather than six, and at a coarser trace-and-space class, opens the job to cheaper fabricators and is worth designing for deliberately.[502]

The module approach has driven specific products. O'Flynn's ChipWhisperer used an FPGA module carrying the ball grid array FPGA so that customers building the board themselves never had to solder it; moving to a single hand-assembled board required switching to a leaded FPGA and dropping the features that the larger part had supported.[239] Henkel's compact high-speed module was deliberately specified at 0.8 millimetre pitch and chosen for ease of routing, so that no expensive stack-up or dense via structure is needed to break the package out, and the underlying processor can be substituted behind a fixed footprint.[681] An open hardware platform deliberately moved from 0.4 to 0.8 millimetre ball pitch so that users could fabricate and build their own variants, since a fine-pitch part makes that impossible.[67]

Designers who intend to assemble and rework their own boards select parts accordingly. On the USRP, Ettus chose the largest FPGA available in a non-ball-grid package to preserve hand rework, accepting the loss of hardware multipliers and compensating with different signal-processing algorithms.[101] Ossmann keeps his designs assemblable with a soldering iron as a stated constraint, choosing a large leaded package where one exists and accepting its physical size, resorting to a ball grid array only where no alternative is available.[265] A leaded package with configurable peripheral routing is preferable to a fine-pitch ball grid array where the design does not actually need a large number of pins.[521] Redesigning to escape the package is a legitimate outcome: one board was reworked to move from a ball grid array footprint to a leaded package specifically so it could be soldered and desoldered reliably by hand, after a previous version yielded one working board out of five.[717]

The contrary view is that a wide-pitch ball grid array is preferable to a very fine pitch leaded package, since a 0.8 millimetre pitch array is easier to work with than a 0.4 millimetre pitch quad flat pack carrying a large number of pins.[515] Higher-performance application processors sit at 0.5 or 0.65 millimetre pitch, which places them in a different category of layout difficulty from the parts a hobbyist would normally attempt.[515] The reservation held against the package by designers who avoid it is visibility: a fault cannot be diagnosed without removing the whole part.[515]

At the extreme of fine pitch, a 0.35 millimetre pitch wafer-level part was placed on a six-layer service with via-in-pad by working at exactly the process minimum of 0.25 millimetres, which requires the layout grid to be constructed to match or the fabricator's checks reject it; at that pitch not all rows of the array can be used, and on that design roughly forty of the sixty-four available signals were brought out.[692]

## Reliability and standards

Differing thermal expansion coefficients between the board, the silicon and the overmould leave the solder balls carrying the resulting stress as the assembly heats, which is why reliability analysis asks why a ball at a particular position fails and uses heat-transfer and finite-element modelling to answer it.[399] The package was not approved for use in flight hardware until the late two thousands.[471]

## Significance for system architecture

The escape problem is also an architectural constraint on silicon: with a one-millimetre-pitch package only so many traces can leave the part, whereas an on-chip wire may be a tenth of a micron wide and thousands can run in parallel, which is why a larger single die gives a super-linear gain over many small chips.[254] Connecting two packaged chips means stepping a signal up from a transistor of a few tens of nanometres, through a die pad of tens of microns, a package trace, a half-millimetre ball, and an eight-thousandth board trace, then back down the same ladder — a change of roughly a millionfold in each direction, which is the argument for integrating dies into one package.[469]

Newly released parts are increasingly available only in packages too fine to use on an ordinary process, and the direction of travel across the industry is towards chip-scale packages, so declining to learn them progressively locks a designer out of current silicon.[502] The same constraint applied a decade earlier: specialised parts available only in micro ball grid array made small production runs impractical.[3]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 3 | HP, IEEE, and Human Interface | https://theamphour.com/3-hp-ieee-and-human-interface/ |  |
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ |  |
| 19 | CAD programs, Systems Design and Renewable Energy | https://theamphour.com/the-amp-hour-19-cad-programs-systems-design-and-renewable-energy/ |  |
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ |  |
| 53 | Biarchy Birthday Bavardage | https://theamphour.com/the-amp-hour-53-biarchy-birthday-bavardage/ |  |
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ |  |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ |  |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ |  |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 116 | Distribution, Wozniak & Robots - Early Eight-bit Endgame | https://theamphour.com/the-amp-hour-116-early-eight-bit-endgame/ | October 7, 2012 |
| 120 | Prototyping, Machining & Accelerators- Mugwumps Mulling Milling | https://theamphour.com/the-amp-hour-120-mugwumps-mulling-milling/ | November 4, 2012 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ |  |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 254 | An Interview with Andreas Olofsson - Adapteva's Ampliative Abacus | https://theamphour.com/254-an-interview-with-andreas-olofsson-adaptevas-ampliative-abacus/ | June 16, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 291 | Artificially Intelligent Party Platform | https://theamphour.com/291-artificially-intelligent-party-platform/ | March 16, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 311 | An Interview with Louis Rossmann | https://theamphour.com/311-an-interview-with-louis-rossmann/ | August 10, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 320 | An Interview with Brent of OSHstencils | https://theamphour.com/320-an-interview-with-brent-of-oshstencils/ | October 20, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 393 | I've bitten myself | https://theamphour.com/393-ive-bitten-myself/ | May 20, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 399 | An Interview with Steve Kreuzer | https://theamphour.com/399-an-interview-with-steve-kreuzer/ | July 15, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 439 | Grow A Superbrain | https://theamphour.com/the-amp-hour-439-grow-a-superbrain/ | April 21, 2019 |
| 452 | An Interview with Kieran O'Leary | https://theamphour.com/452-an-interview-with-kieran-oleary/ | July 28, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 521 | Outdoor Laser Projection & Object Mapping with Daryl Tewksbury | https://theamphour.com/521-outdoor-laser-projection-object-mapping-with-daryl-tewksbury/ | December 13, 2020 |
| 535 | Efinix FPGAs with Sammy Cheung | https://theamphour.com/535-efinix-fpgas-with-sammy-cheung/ | March 21, 2021 |
| 545 | Fear of Banjos | https://theamphour.com/545-fear-of-banjos/ | June 6, 2021 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ |  |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 608 | Vapor Phase with Saber Kaygusuz | https://theamphour.com/608-vapor-phase-with-saber-kaygusuz/ | November 7, 2022 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 692 | Like a steam engine in your house | https://theamphour.com/692-like-a-steam-engine-in-your-house/ | April 15, 2025 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
