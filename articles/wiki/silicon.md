---
title: Silicon
concept: silicon
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**Silicon** is the semiconductor material on which the overwhelming majority of integrated circuits are built, valued in manufacture for an exceptionally low defect density—roughly a million times fewer defects than a typical perovskite film, a level at which a working device would otherwise be impossible because every charge carrier would be trapped.[433] Its band gap sits in the low single digits of electron volts, below the three-to-four electron volt range of the wide band gap materials silicon carbide and gallium nitride that now compete with it in power electronics.[534] Beyond conventional logic and memory, silicon serves as the substrate for photovoltaics, millimetre-wave transceivers, field emission devices, and quantum computing research, and the economics of fabricating it—dominated by thermal budget, die area, and yield—shape the structure of the entire electronics industry.[52][297][498]

## Physical and electrical properties

In silicon, electrons have higher mobility than holes, which is why N-channel MOSFETs are inherently better devices than P-channel ones; in organic semiconductors the ordering is often reversed, with holes the more mobile carrier.[390] Classical logic encodes information in the electrical state of a nanoscale transistor in silicon, with zeros and ones represented as low and high voltages; building a doped device starts from a silicon crystal into which dopants such as phosphorus, arsenic, or antimony are introduced.[498]

Silicon's band gap lies in the low single digits of electron volts, while the wide band gap materials silicon carbide and gallium nitride sit around three to four electron volts.[534] The practical consequence of a wider band gap is switching speed: wide band gap devices can be turned on and off faster, raising the switching frequency the whole downstream design can run at.[534] This matters because in a silicon switching converter it is the switching losses, not conduction losses, that set the ceiling on frequency.[61]

As an optical absorber, silicon is weak: a silicon photovoltaic cell needs on the order of two hundred micrometres of material to capture the incident light, whereas a perovskite film absorbs as strongly in a few hundred nanometres—roughly a four-hundredfold reduction in material thickness.[433] Under X-ray inspection silicon is largely transparent while metal is easy to see, so adjusting contrast changes which structures appear; bond wires are extremely fine, and gold shows differently from other materials, allowing the internal redistribution board inside a module to be traced separately from the die above it.[508]

At radio frequencies, millimetre wave is conventionally taken to start around thirty gigahertz, the point where free-space wavelength falls below roughly ten millimetres. Inside silicon the wavelength is shorter still because of the dielectric: at around ninety gigahertz it is about 1.6 millimetres with a dielectric constant near 4.2, and this sets the physical size of on-die passive structures.[228]

## Fabrication

### Thermal processing

The thermal steps are what make silicon processing uneconomic outside a factory. Running a furnace at around a thousand degrees Celsius for six hours consumes so much energy that a home-made solar cell will never generate back what it cost to make, even though the lithographic steps themselves are simple.[52] A production fab escapes that energy penalty by never letting the furnaces cool: temperature is held continuously and wafers are fed through without interruption, spreading the heating cost across an enormous number of parts and driving the energy cost per wafer down to fractions of a penny.[52]

### Doping and device formation

Device types differ sharply in how much furnace control they demand. Bipolar transistors require much tighter control than MOS devices, because the emitter and collector diffusions have to meet the base in the middle; the process is governed jointly by temperature and time, and overrunning it consumes the base entirely, leaving a device with no base left.[52] MOSFETs are the easier device to build with crude equipment because the critical step is growing a gate oxide, and oxide thickness can be judged directly from the interference colour of the grown film rather than from instrumented measurement.[52]

An implant or diffusion step never introduces only the intended species: while boron is being driven in, oxygen, nitrogen, helium, hydrogen and every other impurity present in the surrounding air go in with it, so the ambient atmosphere of the furnace is itself a process variable.[390] Deliberately controlling that ambient changes the electrical result—blowing chosen mixtures of nitrogen and oxygen through the furnace during the doping step dramatically alters the finished resistivity of the silicon.[390] Nitrogen is used as the furnace purge precisely because it is the least harmful thing to incorporate: nitrogen embedded in silicon is not electrically active and does not shift device behaviour much, so displacing other impurities with nitrogen is a favourable trade.[390]

When a die is thinned from the back for inspection, the material being removed is essentially pure silicon; the only doping at that depth is the wafer's own background doping and possibly some very deep implants, since the active structures sit far shallower.[303]

### Yield and failure

Yield across a wafer depends on keeping process variation low everywhere on it; where variation is not controlled the result is a bad die, and the area that die occupied is expensive silicon thrown away.[136] On a die holding billions of devices, yield is made acceptable by designing in redundancy, so that some fraction of the structures can fail without losing the part.[228]

Overloading an output transistor produces a failure that spreads laterally through the die rather than staying local: the heat released at the device starts to break bonds, ions migrate under that heat, and the damage propagates across the silicon layer.[351] Silicon also offers no equivalent of a bodge wire—a board can be corrected after fabrication with a cut trace and a jumper, but an error committed to a die cannot be patched.[279]

## Scaling and integration

The long climb in serial link speeds has been driven chiefly by the transceiver silicon rather than by cables or connectors: as transistors shrink they switch faster, so shrinking is straightforwardly good for that application.[77] Devices have reached hundreds of gigahertz through scaling alone—as geometries shrank, the intrinsic parasitic capacitances and other unwanted elements of the transistor shrank with them, to the point where building a transistor that generates signals in the hundreds of gigahertz became routine on a state-of-the-art process.[228]

A modern CMOS transistor is barely a silicon device any more: germanium is added, the channel is strained, and a variety of other elements appear in the structure, so the physics of a 22-nanometre device is far more involved than that of an older 0.35-micron transistor.[228]

Function has steadily migrated from the board down into the package and then into the die itself, by way of multi-chip modules, hybrid modules and flip-chip assemblies, ending with everything on a single die; the direction of travel is steadily larger-scale integration.[165] High-integration mobile processors obtain their large memory by stacking: a DRAM die sits physically on top of the processor die and the two are packaged together as one component, which is why the part count on a phone board stays low while the memory does not.[54] When a process node stops yielding gains for analogue parts, innovation shifts into the package, and packaging then becomes the limiting factor until the next process jump arrives; the constraint moves rather than disappearing.[84]

A silicon interposer offers an alternative form of integration that avoids per-customer custom silicon: the underlying transistors in the interposer are identical for every customer, and only the connectivity is configured—the customer's schematic is burned into the interposer as a switch configuration that wires the chiplets together the required way.[499]

## Economics

### Cost structure

Memory is what makes a microcontroller expensive, not the processor core: the same part with 128k of memory instead of 32k costs substantially more because that memory occupies a large fraction of the die area, and die area is what is being sold.[676] Embedded flash is a distinct process technology, so building it into a die raises the cost of the whole wafer; leaving flash off the die and buying it from a dedicated flash maker is a real cost-optimisation lever, at the price of needing a second component.[713] Package size and die size are only loosely related—a part such as an ATmega328 in a DIP package is a very small piece of silicon inside a large moulded body, so the outline of a component says little about how much silicon has been bought.[726]

Silicon cost can dominate a product outright. One development board retailed at twenty-five thousand dollars because the chip on it cost so much, with sixteen thousand dollars of that being the cost to populate the board, making a build of a hundred units a serious financial commitment.[302]

### Entry costs and low-volume access

Entering silicon as a business is a hundred-million-dollar undertaking, and companies that fail at it typically end by selling off their design portfolio as assets rather than being bought as going concerns.[223] Against that, shared-wafer services such as MOSIS have long let a small organisation buy a custom chip outright for roughly ten to twenty thousand dollars of up-front non-recurring engineering, so a fully custom part has never been strictly out of reach for a determined small company; what is in question is whether the result earns that money back.[14]

A ten-thousand-dollar tape-out is inexpensive by the standards of a small or medium company, which makes low-cost shuttle runs a way to prove a concept before committing; once something works and has been characterised, the same company typically signs an NDA with a larger foundry for a finer process and licenses the commercial tools.[616] A ten-thousand-dollar shuttle run historically returned somewhere between one hundred and fifty and two hundred packaged chips, a prototyping quantity rather than a production one.[703] Raising the return to a thousand chips changes the category of the service: enough parts remain after two prototype board revisions of a hundred units each to ship five hundred units of product, so the run functions as low-volume production rather than as prototyping.[703] The cost arithmetic that makes a low-volume custom part viable runs through the usual three-times bill-of-materials rule: at seven dollars a chip inside a thirty-to-forty-dollar bill of materials, the product retails near a hundred dollars and the custom silicon is affordable within it.[703]

Turnaround on a shared shuttle run is around nine months from design submission to receiving parts, and the parts come back packaged rather than as bare die.[674] More generally, chip lead times cannot be compressed below roughly eight weeks, because the material starts as sand and every process step is fixed in duration; that figure belongs in a schedule as a hard dependency with everything downstream moved out behind it.[298]

### Industry structure

The largest fabless companies employ their own process technology engineers, who work directly with the foundry to develop process variants; the developing company then gets exclusive access to that process for something like a year before anyone else can use it.[103] Some silicon is developed for only a handful of customers: where an industry has half a dozen major players who each ship millions of units, a chip company will create a part for that tiny customer list, because unit volume rather than customer count is what pays for it.[139]

Academic computer architecture stalled as a build-it field because process advantage outran design advantage: a research chip taking four years to realise would be overtaken by a commercial part several times faster before it shipped.[84] Restarting mothballed wafer capacity is far harder than it appears, because fabs that shut down had their capital equipment sold off rather than left idle; what remains is an empty building and the restart is effectively from scratch.[541]

## Alternatives and complements to custom silicon

A widely used alternative to spinning a custom part is to press an existing microcontroller into the role, since a general-purpose micro already carries the USB and UART blocks a job needs and is flexible enough to be reprogrammed; the counter-argument for a product team is that a pre-programmed, pre-tested off-the-shelf chip removes the work of programming and verifying the part oneself.[30] A fixed inference workload is likewise a poor match for programmable logic: implementing it in an FPGA is costly in die area, in power, and in programming effort, whereas committing the same repeated computation to dedicated silicon removes all three costs.[619] A spacecraft instrument power budget of around fifty watts leaves only one to two watts for the digital back end, which rules out an FPGA and forces dedicated silicon for a signal-processing chain running four-thousand-to-eight-thousand-point transforms behind a six-gigasample-per-second converter.[483]

Choosing a deliberately old process is a legitimate cost strategy. A field emission display programme was built in five-micron NMOS specifically so that depreciated older equipment could be used, keeping costs low on a structure that did not need fine geometry.[297] The device worked by etching an emitter tip down into the silicon wafer, then laying glass and phosphor over the top with a metal grid positioned directly above the tip; the grid extracts electrons off the tip and they strike the phosphor to produce colour.[297] An old process node also changes what is worth making: on a twenty-year-old process development kit there is no sensible reason to build a purely digital chip, because an off-the-shelf microcontroller will beat it; what such a node still offers is analogue and mixed-signal capability.[672]

In photovoltaics, production capacity rather than efficiency is the binding constraint on silicon at global scale: running existing silicon panel manufacturing flat out would take forty to fifty years to reach world-scale deployment, which is the argument for thin-film alternatives that can be produced far faster.[433]

A satellite connectivity business that requires its customers to design a new silicon modem into their own products faces an untenable go-to-market: each customer must commit to as much as eighteen months of prototyping and deployment on the promise that the network will exist when they finish.[728]

## Design and bring-up practice

One of the few things that genuinely justifies putting a function on its own die is radio-frequency performance: integrating an RF signal chain onto a single piece of silicon beats assembling the same function from discrete components on a board, because the parasitics of the board interconnect are removed.[14] Owning the silicon in an instrument is a durable competitive position, since a rival cannot simply produce a cheaper version of the same architecture; the counterweight is that a competitor building from off-the-shelf parts can still reach a comparable specification at a low price.[347] Designing for volume means pulling as much as possible onto a small number of chips—one sensor unit carrying all the inertial measurement, one processor, drivers pushed out to the motors, and almost nothing else on the board.[130]

Partitioning a system across two dies can be the right answer when the two halves want different things: the large processor die stays generic while the medium-speed mixed-signal interfaces such as USB and GPIO move into a second, separately controlled chip that the system owner can specify exactly.[648] Owning the silicon also lets the pinout be co-designed with the board—every chip on the board can have its pins placed so the wires leave in exactly the right direction, and on a multi-lane PCI Express link between two chips, differential pairs that had to cross over would otherwise force a more expensive board technology.[648]

Because silicon cannot be patched after fabrication, an off-the-shelf part is easier for a small team working to an aggressive schedule.[279] On a compressed schedule the pinout of a new chip may still be unfixed while the die is already in fabrication, because bond-out is decided later than the die itself; a board team designing to a provisional pinout is accepting real risk and does it only when the timeline leaves no choice.[452] Boards come back faster than chips do, so schematic capture and layout for the target board should begin as the silicon goes to fabrication or even before, with normal schematic and layout reviews still applied.[452]

First silicon typically arrives untested, because a test engineer needs physical samples to validate the test program before it can be deployed to the assembly site; the parts and the means of testing them are not ready at the same moment.[452] Bringing up untested parts often needs a custom socket, and those sockets run into thousands of dollars each, particularly for fine-pitch ball grid array packages where alignment must be exact.[452] A chip that does not start up correctly may be a design fault or a part fault, and the questions that settle it are often not answerable from the datasheet—whether particular pins must be tied a certain way, or whether they carry internal pull-ups.[279] Manufacturing in China gives a design team a support channel that has no equivalent elsewhere: almost any component problem can be resolved within a day or two by bringing a local manufacturer's representative in to provide support in person.[279]

For a first custom part, a sensible split is to keep it digital: high-precision analogue such as a chopper-stabilised amplifier is the wrong thing to attempt on a low-cost shuttle process, whereas a small custom processor block is a reasonable target.[607] For teaching device structure, building a three-dimensional model of the process layers—with each layer labelled and independently hideable—works far better than the conventional top-down and cross-section drawings, because it supplies the view between the two that textbook figures never give.[215]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 14 | China, Entrepreneurs and Blue Collar Reality | https://theamphour.com/the-amp-hour-14-china-entrepreneurs-and-blue-collar-reality/ | |
| 30 | Agilent, Analog, Cold Fusion - Funding Fusion Is Not Futile | https://theamphour.com/the-amp-hour-30-funding-fusion-is-not-futile/ | |
| 52 | An Interview with Jeri Ellsworth - Carnassial Chip Chemicals | https://theamphour.com/the-amp-hour-52-carnassial-chip-chemicals/ | |
| 54 | An Interview with Jack Ganssle - Embedded Elchee Epexegesis | https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/ | |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ | |
| 77 | An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry | https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/ | January 9, 2012 |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 130 | Boeing, PCBs & Startups - Awful Airplane Aeration | https://theamphour.com/the-amp-hour-130-awful-airplane-aeration/ | January 28, 2013 |
| 136 | Hardware, Surveys and Giveaways - Radular Rental Ranting | https://theamphour.com/the-amp-hour-136-radular-rental-ranting/ | March 12, 2013 |
| 139 | Google Glass & Adafruit - Obtaining Ostentatious Oculiforms | https://theamphour.com/the-amp-hour-139-obtaining-ostentatious-oculiforms/ | April 2, 2013 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 215 | Wrong Hardware, Wrong Software - Fugacious Fan Funding | https://theamphour.com/215-wrong-hardware-wrong-software-fugacious-fan-funding/ | September 7, 2014 |
| 223 | Space Difficulties and Lost Heroes - Wanzing Workshop Whemmle | https://theamphour.com/223-space-difficulties-and-lost-heroes-wanzing-workshop-whemmle/ | November 4, 2014 |
| 228 | An Interview with Shahriar from The Signal Path - Quisquous Quivering Quadripole | https://theamphour.com/228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole/ | December 16, 2014 |
| 279 | Merry Keyzermas! | https://theamphour.com/279-merry-keyzermas/ | December 22, 2015 |
| 297 | An Interview with Jake Baker | https://theamphour.com/297-an-interview-with-jake-baker/ | May 4, 2016 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11, 2016 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 303 | An Interview with Dmitry Nedospasov | https://theamphour.com/303-an-interview-with-dmitry-nedospasov/ | June 14, 2016 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ | April 29, 2018 |
| 433 | An Interview with Sam Stranks | https://theamphour.com/433-an-interview-with-sam-stranks/ | March 10, 2019 |
| 452 | An Interview with Kieran O'Leary | https://theamphour.com/452-an-interview-with-kieran-oleary/ | July 28, 2019 |
| 483 | An Interview with Adrian Tang | https://theamphour.com/483-an-interview-with-adrian-tang/ | |
| 498 | Quantum Computing with Andrea Morello | https://theamphour.com/498-quantum-computing-with-andrea-morello/ | June 28, 2020 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 541 | Chip Shortage Denier | https://theamphour.com/541-chip-shortage-denier/ | May 10, 2021 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 674 | Turtles as a Service | https://theamphour.com/674-turtles-as-a-service/ | July 25, 2024 |
| 676 | Moving House (And Lab) | https://theamphour.com/676-moving-house-and-lab/ | September 2, 2024 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
| 726 | Arduino's Invisible Touch with Massimo Banzi | https://theamphour.com/the-amp-hour-726-arduinos-invisible-touch-with-massimo-banzi/ | June 17, 2026 |
| 728 | Space Age Bluetooth with Alex Haro | https://theamphour.com/728-space-age-bluetooth-with-alex-haro/ | July 9, 2026 |
