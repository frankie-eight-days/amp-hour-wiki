---
title: Resistor
concept: resistor
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A resistor is a passive electronic component that presents a defined resistance to current flow, used for current limiting, voltage division, current sensing and signal termination across virtually every class of circuit.[598][133] Discrete resistors are specified by value, tolerance, temperature coefficient, power rating and package, and in volume production they are treated as commodity parts ordered by generic description rather than by manufacturer part number.[216][17] Resistors are also one of the three primitives of analog integrated-circuit design, alongside MOSFETs and capacitors, where their behaviour under process variation dictates ratio-based design techniques.[672]

## Characteristics and specification

### Tolerance and temperature coefficient

Precision resistors specified at 0.1% tolerance with temperature coefficients on the order of 25 ppm or better are relied upon to be in specification as delivered, because verifying each part's tolerance and drift would require stepping it through temperature.[22] At the top of the precision range, the binding specification is temperature coefficient rather than initial tolerance: bulk-metal foil resistors reach 0.05 ppm per degree Celsius, while 0.01% tolerance is unremarkable and 0.005% parts are obtainable for about twenty dollars.[174]

In practice, ten percent tolerance is adequate for most designs, and where a tighter part would help, adding another component is often a better trade than tightening the tolerance specification.[157] Specifying resistors more tightly than the circuit requires is considered a design error with downstream cost: choosing E96 values or paying for 0.01% parts where the accuracy has no effect on the result degrades sourcing and raises cost, and one open-source design has carried sixty different resistor values on its bill of materials.[500]

### Matching

In a two-op-amp differential amplifier, the resistor dividers on the two inputs must match rather than merely be accurate: 1% resistors may leave gain error acceptable while badly degrading common-mode rejection ratio, because the rejection depends on the divider ratios being equal. High-voltage differential probes are therefore built with trimmer resistors and trimmer capacitors adjusted at the factory.[528]

### Noise

A resistor's intrinsic Johnson noise rises with its resistance value, which sets a floor on attenuator and signal-path design at low noise levels.[558]

### Power rating

Power rating constrains design independently of value. A bench holding every E96 value in quarter-watt parts still cannot build a ten-ohm load capable of dissipating the power of a battery discharge test, which requires one-watt parts or on the order of a hundred quarter-watt resistors in parallel.[488] Contact resistance in switches is evaluated as a power-dissipation problem in the same terms: three volts across roughly an ohm is nine watts by V²/R, dissipated inside a small mechanical switch before wiring resistance is counted.[447]

## Preferred values

Where an exact value is needed from a coarse preferred series, a computational search across the E24 range finds pairs of resistors that combine to the target, and the same tooling shows how much the error falls if the design moves to the finer E96 series.[348] Rules of thumb for resistor selection originated in the era before cheap calculation, when working out a value with a slide rule was expensive enough that engineers instead picked a value from the bench, observed the behaviour and adjusted in the direction indicated.[47]

## Resistors in integrated circuits

Analog integrated-circuit layout is drawn from three primitives — MOSFETs, resistors and capacitors — and the governing constraint is that absolute values do not repeat between wafers while neighbouring matched devices do. A process variation of a few microns in a layer's thickness can move device values by around ten percent on the next wafer, so circuits are designed as ratios of like components: a divider of three identically sized resistors gives the same output voltages regardless of their absolute value.[672]

Resistors occupy a large area on a die. This is cited as a reason why TTL logic, which depends on on-chip resistors, scaled poorly and was displaced by CMOS, where an inverter is two transistors and no resistance is required.[361] Analog front-end modules increasingly place their dividers inside the package as laser-trimmed resistors, which are better than the discrete parts a designer would buy externally and remove the parasitics of separate packages, the pin inductance of each device, and the risk of two external resistors drifting in opposite directions and stacking their tolerances.[166]

### Trimming

On-chip resistors are laser-trimmed during wafer and package test to raise the accuracy of the finished part; the step is performed after wafer fabrication and before dicing, with the part tested again in package form.[348] Wafers also carry dedicated test sites — typically one at the centre and several on the periphery — populated with test transistors and resistors so the fab can confirm the process ran correctly; a comprehensive post-fabrication measurement on these sites decides whether the wafers are used at all, and an entire wafer lot can be scrapped on that result.[348]

On-chip trimming turns a twenty percent process spread into roughly one percent accuracy: the resistor is laid out as a chain of smaller chunks, a reference value is measured at production test, and links are fused to select the combination.[338] Self-trimming structures built into the silicon are the alternative to trimming at the wafer tester, and are chosen to avoid spending tester or boot-up time on the operation.[338]

## Applications

### Current limiting

The general rule is that any LED driven from a voltage source needs a series resistor; a seven-segment display driven from logic outputs is properly designed with an individual dropper resistor per segment so the current through each is defined by calculation.[598] Dedicated LED driver chips are difficult to design out precisely because the alternative — driving each LED from a microcontroller pin — requires an external series resistor per LED and cannot reproduce the driver's current control.[546] Indicator LED brightness is nonetheless normally set empirically: a nominal series resistor such as 1K is fitted, the assembled product is judged by eye, and the value is changed on the bill of materials afterwards if it is wrong.[724]

### Voltage division and instrumentation

Resistor divider networks for precision instruments are negotiated against three coupled parameters — cost, initial tolerance and drift — so that loosening initial tolerance to 0.03% can buy a 10 ppm drift specification; one network vendor modified the serpentine patterns of its thick-film elements to reduce stray capacitance. The overall accuracy specification of a digital multimeter is then the root-sum-square of the individual component contributions.[180]

### Current sensing

Current sensing with a small series resistor, on the order of 0.1 ohm, is the standard method borrowed from voltage-regulator short-circuit protection, and adding half an ohm in series with a coil that already has ohms of resistance is an acceptable perturbation.[133] Measuring current by putting a resistor in line and reading the drop with an oscilloscope is limited by what the measurement is referenced to: touching the probe ground to one side ties the measurement to the instrument's earth ground and introduces errors, so a genuine differential probe is required for a correct reading.[607]

### Voltage regulation

A class of low-dropout regulator sets its output voltage with one resistor to ground instead of a feedback divider, by driving an internal constant current source of about ten microamps through it to develop the reference. Because that current is small, the internal source can be overridden by driving a voltage directly onto the set pin, converting the part into a programmable supply.[44] The same single-resistor scaling principle is extended in later regulators to auxiliary outputs: a current monitor and a die-temperature output each have their range set by one external resistor, so the full-scale voltage can be matched to whatever analog-to-digital converter input range is available without external op amps or dividers.[154]

### Signalling and identification

The minimum hardware change to replace a USB 2.0 port with a USB-C connector is to tie the two positions provided for the data pair together, wire them into the device as before, and add a pull-down resistor on the CC lines.[340] Electric-vehicle charging on the Type 2 connector signals with two pins and no data protocol: one carries a one-kilohertz square wave, and a resistor of a defined value inside the vehicle encodes the current level it can accept.[510] Board revision can similarly be encoded in a set of resistors read by firmware at boot, avoiding separate builds or preprocessor branches per revision; the associated firmware discipline is to confine revision handling to a single board-support or hardware-abstraction file.[556]

A minimal USB human-interface-device implant reduces to three resistors, two zener diodes and an ATtiny microcontroller, a circuit arrived at by cannibalising existing development boards to find the smallest design that retains the function.[454]

### Resistors as heat sources

A resistor can be used as a controlled heat source rather than a circuit element: passing current through a resistor taped inside the flotation bag of a marine instrument burns a hole in the bag on command and scuttles the equipment.[190] Burn-wire release mechanisms use the same principle in spacecraft: a meltable wire is wrapped around a resistor to hold a spring-loaded latch, and heating the resistor releases deployable solar panels and antenna elements on small satellites.[679] A load resistor absorbing the output of a high-current power module glows visibly, and colour is used as the working temperature indicator during test, with orange acceptable and white the point at which the test is stopped.[522]

### Printed resistors

Resistors can be printed directly onto a board as conductive graphite by fabricators offering the process, with the required value specified as a design parameter rather than fitted as a component.[260]

## Manufacturing and assembly

### Soldering behaviour

Tombstoning occurs when solder on one land pad reflows before the other and its surface tension lifts a chip component upright off the second pad. A production board has been found under a stereo microscope with a resistor tombstoned so that one terminal made no contact at all, yet the board still functioned.[11] Conversely, solder surface tension self-aligns small chip components during reflow, so a resistor placed approximately in position is drawn into place; the hard case is a package with a large central ground pad, which is difficult to heat sufficiently and will tilt the part if too much solder is applied there.[501] Workmanship standards allow far more placement error than intuition suggests: a chip resistor sitting roughly a third off its pads remains mechanically robust.[183]

Through-hole components are held in their bandolier tape with glue, and leads pulled from the strip carry a residue that acts as an insulator; the leads must be trimmed before the part is inserted into a breadboard or contact may not be made.[236]

### Placement

Placement accuracy on a machine without vision is limited by parts moving inside their tape pockets, so the part must be aligned after pickup. Two alignment methods exist, camera vision and laser measurement; a laser line rotating the part measures its angular and X-Y offset from the nozzle centre so the machine can correct both at placement.[153] Pick-and-place assembly also consumes more parts than the board count implies, because components are lost when the reel is wound onto the machine, so excess must be supplied — ten or twenty spare parts is typical for cheap passives. Expensive components should be identified to the assembler so they are handled and loaded with care rather than wasted at the same rate.[24]

A one-off value needed at a single position, such as the feedback reference resistor of a switching regulator, is hand-soldered after assembly rather than given a feeder on the placement machine.[224] In hand assembly, every part is deliberately rotated to a common orientation so values can be read in one pass during inspection; a larger package such as 1210 may be chosen deliberately over 0603 so that signals can be routed underneath the part.[561] Hand-placing the first boards of a design is regarded as the most direct design-for-manufacture feedback available, because the designer experiences the consequences of choices such as an unnecessarily small resistor package while placing them.[612] Locating design work next to manufacturing surfaces problems that do not appear on paper, such as a component position where the part consistently falls off the board during assembly.[124]

### Bills of materials and purchasing practice

Commodity passives are ordinarily specified on the bill of materials by package, tolerance and value rather than by manufacturer part number, because the assembler will supply standard stock and the brand is immaterial.[216] Contract manufacturers hold house parts for common passive values and run a matching step that maps a generic line such as a 1K 0805 to their own stock; the economics work against the customer specifying only generic values, since a board built entirely from house parts may leave the assembler no margin, so naming a part number is considered the better practice.[243] Assembly houses stock common resistor values across the standard chip sizes — 0805, 0603 and 0402 — so a small build need not buy full reels, but a generic house part may not carry a specification the design depends on, such as a particular temperature coefficient or power rating.[17]

Bill-of-materials optimisation trades component count against line-item count: two 10K resistors in parallel substitute for a more expensive 5K part and save a cent per unit, and a spare transistor wired as a diode avoids buying a reel of diodes. The deciding constraint is often feeder slots, since a design with thirty distinct parts requires an assembly machine that can hold thirty reels.[366] Line-item count is a recurring labour cost for anyone kitting a product by hand and is considered a design parameter worth minimising up front, though in practice the redesign is rarely undertaken until a component goes obsolete and forces the design open again.[229]

A company component database multiplies variants of an apparently trivial part: a 10K resistor branches by schematic-symbol style, then by tolerance grade at one percent, half a percent and 0.1 percent, then by temperature coefficient at 50, 15 or 10 ppm, and finally by the three IPC land-pattern density classes, so twenty entries for a 10K resistor accumulate and the wrong one gets picked. Raising a new part request — with specification, data sheet, an approved manufacturer part number and the required footprint variant — can consume half a working day.[445]

### Kits and hand assembly

Surface-mount parts are poorly suited to kits because each value must be cut from its carrier strip individually and then bagged and labelled, and chip capacitors carry no marking, so the builder must measure them. Through-hole parts carry printed values or colour codes, which makes them sortable, packageable and identifiable by the person assembling them.[143] Mislabelled or mixed component bags are caught during hand assembly by measuring the parts with a meter; a strip of 40.2K parts found in a bag marked 100K would otherwise have been fitted into a regulator feedback network, where the wrong divider value shows up as an output stuck well below its intended voltage.[561]

## Supply chain and cost

A single critical precision resistor can carry a two-month lead time at both the distributor and the manufacturer, which makes the reorder point for a product with such a part a supply-chain decision rather than a stock-level one.[210] Passive-component shortages propagate across resistors, capacitors and low-complexity discretes together rather than affecting one part type, and have produced distributor reel prices doubling within a few months.[377] Over-the-counter component supply persists in a small number of distributors, where a staffed counter takes a spoken specification such as a quarter-watt one-kilohm resistor and fetches the part, but the model is disappearing.[284]

A distributor shipping the wrong tolerance under a correct-looking part number is a live failure mode for precision analog work: a batch supplied as 0.1% parts was actually 1%, the parts were assembled onto boards and shipped, and the error surfaced as a roughly fifty percent test failure rate — a five percent failure rate might be written off, but fifty percent is noticed.[182] Reels of precision resistors are now commonly shipped directly from the distributor to the assembler rather than double-handled through the designer, a change from the earlier practice of taking delivery first specifically to verify that the right part arrived.[342]

The cost structure of a precision instrument is dominated by a few parts and by verification: a single resistor at four dollars in volume can cost around twelve dollars at single-piece pricing, so low-volume builds absorb the difference directly out of margin, and the specification is backed by NIST-traceable calibration and purpose-built test gear that measures every unit. Copies of an open-source precision design built with lower-precision parts do not meet the original specification.[554] A design whose performance rests on a precision part should not be sent to an assembler who is free to substitute, because a four-dollar resistor will be replaced with a four-cent one and the substitution destroys the specification the product is sold on.[239]

At the other extreme, unit-cost constraints in toy design change the design process qualitatively: a resistor costing a hundredth of a cent cannot simply be added, and cost reduction is the rewarded outcome, in contrast to industries where time to market dominates.[35] Cost-optimised consumer products are consequently poor material for learning circuit theory but good material for learning manufacturing improvisation, containing expedients such as a resistor soldered on edge purely as a mechanical brace for a potentiometer.[276] The marginal cost of an additional passive on a board is negligible while the first one is not: getting a single resistor onto a board carries the design time, the board fabrication, the distributor order and the waiting, so the cost curve is dominated by fixed setup.[434]

## Testing and debugging

Debugging by voltage stack-up follows current through known resistances: one amp through a ten-ohm resistor must produce ten volts across it, and a smaller reading means the current is going somewhere else. The method holds for DC analog circuits and breaks down at high frequency, where capacitance shunts current away from the path being reasoned about.[160] A quick health check on a working board is that series and pull-up resistors should show negligible voltage across them, since voltage across a resistor is dissipated power; bypass capacitors, by contrast, are expected to hold voltage. Where a drop is present, the resistance value converts it directly into a current figure.[527]

Measuring a component in circuit can give a confidently wrong answer: a MOSFET read as 0.6 volts because of surrounding components and was taken for a bipolar transistor, and had to be removed and put on a component tester to identify. Once identified, the two 4.7-megohm resistors and the lower-value one below them made sense as a divider limiting the gate voltage to a level the MOSFET could survive.[539] Multimeters that warn when the probe is in the wrong jack detect the condition with a split current jack and a high-value resistor of around five megohms feeding a high-impedance threshold detector; because the sensing node is high impedance, dirt, grime or moisture inside the jack produces the warning with nothing plugged in, and cleaning the jacks with alcohol restores correct behaviour.[688]

Component swaps made during debugging should be recorded as they are made, with the hypothesis attached, because the alternative is a tray of desoldered resistors of unknown value and no record of which change produced which result.[460] Where a design's resistors are within tolerance and its amplifiers are within their input-bias specification, the remaining functional test adds little, so sample testing at one board in a hundred plus absorbing the cost of returns is a defensible production strategy for a low-value product.[182]

In simulation, SPICE unit suffixes are a standing trap: M denotes milli and Meg denotes mega, so a resistor entered as one M is a thousand times smaller than intended and the simulation result is wrong rather than obviously broken.[76]

## In education and prototyping

Breadboards that insert protective series resistance keep beginners from destroying LEDs but conceal the need for a current-limiting resistor, so parts fail as soon as the circuit is transferred to a real board.[689] A resistor, an LED and a battery are sufficient material for a genuine sense of discovery in electronics, and a design practice can be built on presenting circuits that way rather than on a single-board computer running an operating system.[286]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 11 | Ardui...no Dave This Week? | https://theamphour.com/the-amp-hour-11-ardui-no-dave-this-week/ | |
| 17 | EE Movies, Part Rants and SPICE. | https://theamphour.com/the-amp-hour-17-ee-movies-part-rants-and-spice/ | |
| 22 | The Hard Work Hypothesis | https://theamphour.com/the-amp-hour-22-the-hard-work-hypothesis/ | December 21, 2010 |
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ | |
| 35 | An Interview with Jeri Ellsworth - The Ternary Tussle | https://theamphour.com/the-amp-hour-35-the-ternary-tussle/ | |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 47 | Apple HQ and Vintage Arcade Games - The Mothership Manifesto | https://theamphour.com/theamphour47-the-mothership-manifesto/ | June 15, 2011 |
| 76 | Fremescent Floccose Fortification | https://theamphour.com/the-amp-hour-76-fremescent-floccose-fortification/ | January 2, 2012 |
| 124 | SpaceX, Enclosures & Startups - Urging Unemployment Ullagone | https://theamphour.com/the-amp-hour-124-urging-unemployment-ullagone/ | December 3, 2012 |
| 133 | An Interview with Ron Quan - Tenacious Transistor Teacher | https://theamphour.com/the-amp-hour-133-tenacious-transistor-teacher/ | February 18, 2013 |
| 143 | PCBs, Tektronix & Ham Radio - Habitual Handicraft Hangups | https://theamphour.com/the-amp-hour-143-habitual-handicraft-hangups/ | April 29, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 157 | An Interview with the SparkFun Team - Efficacious Engineering Ensemble | https://theamphour.com/the-amp-hour-157-efficacious-engineering-ensemble/ | August 5, 2013 |
| 160 | Troubleshooting, PCBs and LEDs - Quaintized Quich Quelling | https://theamphour.com/the-amp-hour-160-quaintized-quich-quelling/ | August 26, 2013 |
| 166 | Prior Art, Wafer Fabs and Guns - Whimsical Wafer Waffling | https://theamphour.com/166-prior-art-wafer-fabs-and-guns-whimsical-wafer-waffling/ | October 7, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 180 | An Interview with Dave Taylor - Multi-talented Meter Maker | https://theamphour.com/180-an-interview-with-dave-taylor-multi-talented-meter-maker/ | January 13, 2014 |
| 182 | Manufacturing By Wire And Skipping Testing - Calefacient Cuculine Cash | https://theamphour.com/182-manufacturing-by-wire-and-skipping-testing-calefacient-cuculine-cash/ | January 27, 2014 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 190 | Let's Hear It For The Buoys - Vanishing Vessel Vexation | https://theamphour.com/190-lets-hear-it-for-the-buoys-vanishing-vessel-vexation/ | March 24, 2014 |
| 210 | Risky Components and Hardware Innovation - Slipshod Shack Shutdown | https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/ | August 5, 2014 |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 276 | Eating An Elephant | https://theamphour.com/276-eating-an-elephant/ | December 2, 2015 |
| 284 | An Interview with Great Scott | https://theamphour.com/284-an-interview-with-great-scott/ | January 27, 2016 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 445 | Ludicrously High Frequency Interference | https://theamphour.com/the-amp-hour-445-ludicrously-high-frequency-interference/ | June 2, 2019 |
| 447 | Voltnuts for Flashlights | https://theamphour.com/447-voltnuts-for-flashlights/ | June 16, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 460 | Rubber Ducking | https://theamphour.com/460-rubber-ducking/ | September 29, 2019 |
| 488 | Sowing Discord | https://theamphour.com/488-sowing-discord/ | April 12, 2020 |
| 500 | Two and a Half Orders of Magnitude | https://theamphour.com/500-two-and-a-half-orders-of-magnitude/ | July 12, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ | January 31, 2021 |
| 539 | The King of Trash with Big Clive | https://theamphour.com/the-amp-hour-539-the-king-of-trash-with-big-clive/ | April 26, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 558 | Toasted Marshmallow Connectors | https://theamphour.com/558-toasted-marshmallow-connectors/ | September 19, 2021 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 598 | Best way to find a leak | https://theamphour.com/598-best-way-to-find-a-leak/ | August 7, 2022 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 679 | Satellite Design Engineering with Dan Esparon | https://theamphour.com/679-satellite-design-engineering-with-dan-esparon/ | October 11, 2024 |
| 688 | The Tandy Train | https://theamphour.com/688-the-tandy-train/ | February 11, 2025 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
