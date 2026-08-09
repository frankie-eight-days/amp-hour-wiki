---
title: 3D Printing
concept: 3d-printing
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

3D printing is a family of additive manufacturing processes in which solid objects are built up layer by layer from a digital model. The term covers no coherent list of technologies: desktop extrusion machines sit alongside laser metal powder bed fusion, the process behind aerospace and medical components, and directed energy deposition, which builds large metal structures with robotic arms.[405] The technology's principal engineering roles are rapid prototyping, tooling-free production of one-off and low-volume parts, and the fabrication of geometries that other processes cannot produce; it has become a standard step in the product development process for consumer products generally, distinct from any role as a consumer manufacturing method in the home.[421]

## History

The desktop extrusion industry traces its technical foundations to the RepRap project, which was deliberately designed so that almost every part of the machine could be produced by the machine itself, making it self-replicating apart from the drive electronics.[30] The RepRap project had solved most of the hard technical problems of desktop extrusion printing before the commercial desktop industry began around 2009; the companies that followed took that technology, improved it incrementally and built businesses on it.[260]

Before affordable printing existed, prototype enclosures were hand-made from fiberglass and hand spray-painted; such cases looked finished but were fragile enough that a set could not be entrusted to a courier or a flight and had to be driven to the trade show.[623] The practical change printing brought to mechanical prototyping was replacing hot-glued sheet plastic and hobby-shop parts with drawing the part in CAD and having it in hand about an hour later.[424] Stereolithography machines fell from a couple of hundred thousand dollars to around ten thousand dollars during the 2010s, and a Chinese desktop machine at about two thousand four hundred dollars in 2012 was the entry point that made ownership plausible for an individual designer.[424] Low-cost Chinese machines later arrived calibrated well enough to print acceptably after roughly ten minutes of setup, removing the assembly-and-tuning stage earlier kits required.[458] In the early 2010s a good commercial machine ran to about fifteen thousand dollars fully equipped, filament cost around twenty dollars a kilogram on a spool, and commercial bureau printing was priced around five dollars per cubic inch.[78]

At least one printer vendor built a closed system that withheld user control of temperature and other print parameters in order to force purchases of its own material; the system was reverse engineered and an aftermarket temperature controller was sold for it.[424]

## Process physics

Fused-deposition print speed is bounded by the thermal properties of the plastic: each layer must harden just enough for the next layer to be laid on cleanly without smushing, a physical limit that cannot be engineered away.[105] Laser curing of a liquid resin is not subject to the same thermal constraint, so its physical limits are far less restrictive on speed.[105] Powder-based processes work by depositing a liquid binder onto a powder bed in the manner of an inkjet, producing a sludge that is subsequently baked.[105]

Additive fabrication is a raster process whose time scales as the area to be covered multiplied by the number of passes over it, set against the speed of the head; head speed is itself bounded by the accuracy that must be maintained, and that arithmetic is why the process does not suit production volumes.[172] The speed ceiling of a raster deposition process comes down to how fast the head can be physically moved while still holding the required process accuracy.[172] Individual prints still take hours — a detailed case takes on the order of three to four hours per part — and prints rarely finish in under an hour or two, which sets the throughput ceiling whenever printing is used beyond single units and makes utilisation and cost amortisation difficult for shared-access workshops charging per use.[415][550][368] A print therefore has to be started and collected around other work rather than watched.[550]

Frame rigidity governs dimensional accuracy: wood-framed machines flex, and a rigid-framed printer is the appropriate choice where accuracy matters.[189]

## Materials and mechanical constraints

Printable polymers are low-temperature and low-tensile-strength materials, which is the standing constraint on where printed parts can substitute for metal ones.[127] Printed plastic parts are weak enough that a mechanism built from them can fail under ordinary motor loads: printed carriages snapped in half when the motor was first energised, and the work moved to aluminium extrusion instead.[204] A resin machine left running overnight produces functional parts at roughly fifty-micron resolution with material properties adequate for function, though not equivalent to injection-moulded ABS.[480]

Where mechanical strength is inadequate, workarounds exist. Filling the void in a printed shell with a curing compound such as RTV is a practical way to make a fragile printed prototype solid enough to handle.[175]

## Scope of the term

Laser metal powder bed fusion is the standard process for aerospace and medical metal components, and directed energy deposition is what allows very large metal structures to be built up.[405] Printed metal parts are difficult to edit once designed, which is why topology optimisation software exists and why the design method for them differs fundamentally from conventional modelling.[405] Four-dimensional printing refers to printing an object that changes shape after fabrication, unfolding into its final form when placed in water.[421] Full-colour printing only pays off if the part was designed for it and the colour routed through the geometry, rather than an existing model being sent to a colour machine.[689]

## Applications in electronics work

### Enclosures

The dominant electronics application is custom enclosures and shells, which are difficult to produce even with a good CNC milling machine.[75] Electronics engineers increasingly carry responsibility for packaging as well as circuits, and printing is what makes prototype packaging feasible without a mechanical department.[78] The competing practice is to design the product around an off-the-shelf enclosure, because such enclosures cost a dollar or two, are available in every country and require no design effort of their own.[75] In consulting work the recommended default is to take a suitable off-the-shelf case and design the board to fit it, because case design consumes hours that are difficult to bill and invites open-ended tweaking.[415] Designing an enclosure in house tends to produce a worse part than an enclosure vendor's, because the vendor's mechanical engineers design for draft angles and manufacturability at high volume in a way an electronics engineer does not.[665]

### Tooling, jigs and fixtures

The clearest justification for a printed part is one nobody would ever tool for: printed holders for pogo-pin test fixtures are a case where the need, rather than the schedule, makes printing the right process.[244] A printed jig matched to the board outline holds a small board flat and square during hand assembly and rework.[724] Printed pick-and-place feeders are used to escape the roughly thousand-dollar cost of commercial feeders, on the understanding that they will not match commercial pedigree.[411] One assembly-machine vendor publishes its strip feeder files so that owners print their own rather than buying them, selling the printed parts only as a convenience.[686] Printed feeders on a prototype machine are a prototype-only solution: a machine shipped in volume with printed feeders will need moulded tooling for them.[317] Printed parts are visually identifiable in product photographs, so extrusion layer lines in a vendor's images reveal that the unit shown is a prototype rather than a production build.[610]

### Mechanisms

Printed compliant mechanisms are a distinctive capability: an open-source microscope is printed as a single fourteen-hour part with flexures built into it, using lever-action gearing to scale a motor's motion down to tens of microns.[686] Where machining is not accessible, designers deliberately restrict themselves to printable geometry, and a printed capstan drive or gear reduction can be produced at a fraction of the cost of a machined metal gearbox with high precision.[712] Custom printed drivetrain components can be cheaper than buying a metal planetary gearbox while remaining precise enough for the application.[712] A humanoid robot programme moved from vacuum-formed shells to fully printed structural parts, with aluminium extrusion and steel brackets carrying load internally, and simulated the joints in CAD before printing.[416] Printing lowers the cost of mechanical prototyping enough that trial and error becomes the working method for someone without formal mechanical training.[416] Custom mechanism development is where printing earned its place in one machine-building practice, alongside existing CNC and laser capability, and throughput was raised by running several machines in parallel rather than by buying a faster one.[490]

### Casting patterns

Printed parts serve as the pattern for metal casting: a printed pattern used with lost-pattern sand casting produced an intake manifold, a curved and complex shape that would be impractical to machine and undesirable to split into a two-part assembly.[472] The limit on printed casting patterns is build volume: large patterns have to be made in multiple pieces, which leaves a seam in the finished metal part.[472]

## Prototyping practice

### Design workflow and file formats

Printers consume a solid model in STL form, so mechanical CAD output has to be converted, and conversion quality varies between tools.[211] Keeping a board as real solid-body geometry — a positive extrusion for the copper along the Z axis and a negative for the solder mask — is what makes downstream conversion reliable, because thermal finite-element analysis, milling CAM and printing each mesh the model differently and opportunistically.[471] An early electromechanical workflow was to export the board's 3D view into a free mechanical CAD package, design the case around it there and export a printable file through a plugin, putting a complete prototype within reach of about a hundred dollars; the board model is imported purely as a reference for the enclosure, since nothing further can be done to the board in that tool.[49]

Slicing software matured to the point where the operational skill could be acquired in a few hours, shifting the difficulty entirely onto the modelling side.[251] The capability that determines whether a printer is useful is 3D modelling rather than printing: without modelling skill, the machine only reproduces objects other people designed.[694] Once a machine is correctly set up it should not need further adjustment, so the skill worth acquiring is not the printing itself.[625] First-layer adhesion is the recurring troubleshooting problem for new users, with a glue stick on the build surface as the standard remedy; the transferable skill is understanding slicer configuration generically rather than following instructions for one machine.[675]

### Iteration

Printing is the iteration mechanism in an electrical and mechanical co-design workflow carried out by a single engineer with a single toolchain.[472] The iteration rate available in mechanical prototyping — three complete sets of prints inside two days — has no equivalent in electronics, where parts alone may not arrive in that time.[536] A rough print that is only good enough to reveal that a model is the wrong size is a legitimate use of the process, since the check costs a few hours and no tooling.[625] Printing a scale replica of a mechanism described in a paper is a way of understanding how it works, as was done with a nanometre-accuracy micro-positioning stage.[582] Print speed is fast enough to fit inside a one-week concept-to-finished-project cycle, which is why projects on that schedule are designed around printing rather than around machining.[550]

A printed model answers ergonomic and fit questions that cannot be settled from a drawing: printing a device mock-up so that people could carry it in a pocket established whether the electronics would fit the intended form factor.[550] A printed case prototype in clear resin communicates the look and feel of a product in a way images cannot, which is why manufacturers send them before tooling.[536] Printing the board itself is used as a physical check on the electromechanical design: a test fit for connectors, and confirmation that mounting holes are in the right place and that the screws intended for them actually pass through.[471] On the Pebble watch programme, the prototype shown for the campaign was one of three stereolithography prints, including a transparent printed lens that was painstakingly polished afterwards and cost about a thousand dollars each for the lens alone; the printed plastics were not strong enough to serve as a working case, so the display was crammed into the printed shell, the remaining volume filled with RTV to stiffen it, and the electronics tethered outside on a separate prototype board.[175]

Products that are custom by definition, such as orthopaedic insoles, are the natural application, because every item differs and there is no volume to amortise a tool against.[260] A general-purpose fabrication machine presents users with a blank-canvas problem: told that a machine will make anything, most people cannot say what they want made.[260] Printing a set of construction-toy-compatible beams — eight millimetres wide with holes eight millimetres centre to centre — gives a mechanical sketching medium that removes the blank-page problem at the start of a design, with the properly designed part following afterwards; a physical bucket of standard parts on the desk is a deliberate first step, with the from-scratch design done after the arrangement is understood.[369] Keeping a design printable also makes it reproducible locally from published files, which avoids international shipping and the customs costs that make exporting finished hardware to some countries impractical.[369]

## Design rules and failure modes

Printing is close to unconstrained in geometry apart from overhangs and the support material they require; machining carries real geometric limitations, and any moulded part needs draft or taper so that it will release from the mould, which CAD draft analysis tools check for.[379] Draft is a constraint printing does not impose, and it therefore has to be added deliberately when a printed design is moved to moulding.[379]

The characteristic failure of designing an enclosure only against a printer is that the printed prototype cannot be manufactured by the production process it is later handed to.[682] A prototype optimised for hand assembly and printing is effectively a different design from the manufacturable version, so schedule and iteration have to be budgeted for design for manufacture and for trial runs with the real suppliers.[437] Mechanical design for manufacture cannot be done in isolation from the supplier: it is a sustained exchange about what the supplier can and cannot do and what its mould flow analysis shows, and on a complex product that exchange can run for months before a part is released.[437] A part that is painful to print — full of undercuts and thin walls — may be trivial by another process such as heat-folding sheet plastic over a nichrome wire, so a designer needs a mental library of manufacturing methods kept in sync with what the chosen supplier actually owns.[437] Knowing the vocabulary of standard mechanical parts and methods is what prevents wasted printing: not knowing the name of the right component leads to spending weeks printing a jig for a problem that had a standard solution.[611]

A first print typically fails on build-plate adhesion rather than on geometry: a simple part printed correctly but could not be separated from its raft, and printing without a raft only worked once the build-surface tape had been cleaned.[94] Build-surface preparation is the undocumented step that decides whether raftless printing succeeds, and the knowledge circulates through forums rather than through documentation.[94] Filament degrades in storage: three-year-old material broke repeatedly inside the printer until it was replaced.[705] Resin prints require a cleaning step in isopropyl alcohol after printing, which makes the process dependent on a consumable that is not always available.[536] An early stereolithography print collapsed under its own geometry, a reminder that a shape that slices successfully is not necessarily one the process can hold.[665] Printers emit fumes strong enough to be a siting constraint; one production printing effort was run outdoors on a balcony because the smell was intolerable indoors.[189]

### Process-specific design techniques

A six-millimetre hole in polylactic acid takes a quarter-inch camera-mount screw driven directly into the plastic, the coarse threads gripping without an insert, which opens up a large ecosystem of tripod and clamp hardware.[528] Captive nuts should be designed as a slot open at the top so that the nut drops in as the part prints; pausing the print to insert a nut horizontally and printing over it does not work.[559] Wall thickness at a connector opening has to be sized from the mating cable's overmould rather than the connector alone: a thick-walled printed case blocked a USB-C cable whose overmould is specified at roughly six and a half by thirteen and a half millimetres maximum, requiring a recess.[668] Printing onto fabric is done by printing a base layer, pausing to lay the fabric down and letting the heat of the next layer fuse the fabric between layers, embedding a rigid insert directly into textile.[415]

### Verification of printed mechanisms

A printed mechanism that must operate repeatedly needs cycle testing rather than a single successful demonstration: a printer tool changer facing three hundred changes in a single multi-material part was cycle tested overnight, with a camera used to capture where it broke around the two hundred and fiftieth cycle.[611] Filming a repeated test is what makes an intermittent mechanical failure diagnosable, since the failure is otherwise discovered only after the fact.[611]

## Printed electronics

A proposed route to printed electronics was to deposit a conductive layer within a powder-sintering process so that vias could be built up from the bottom layer to the top.[35] The same idea extends to printing pockets for surface-mount components, halting the process midway to drop parts in and then continuing to build over them.[35] The obstacle to embedding components during printing is thermal: the printed polymer would have to survive soldering temperatures, or the board disintegrates when the joints are made.[35] A printed circuit-board process is not a substitute for a fabricated board; the industry it addresses is large companies that need to keep design work in house for intellectual-property reasons.[406] A related route to a three-dimensional object without a printer is to laser-cut each layer from thin sheet material and stack the layers.[45]

## Economics

### Materials, tooling and small-batch work

The economics of one-off and small-batch work have inverted: material cost used to rival the non-recurring engineering cost at quantities of one or ten, whereas material is now cheap and engineering time remains expensive.[422] Tooling cost has effectively disappeared for low-run prototypes, so a one-person operation can produce hundreds of well-finished units without amortising a tool.[665] A proof of concept assembled from an off-the-shelf development board, a custom sensor board on its standard pinout and a printed case cost perhaps ten to twenty times the eventual unit cost but was delivered on the schedule the client needed.[422] Bulk feedstock is cheap relative to bureau pricing: about twenty dollars for a kilogram of ABS on a spool.[78] Stereolithography consumables are the limiting cost at small production volumes: a kilogram bottle of resin at around a hundred and fifty dollars yields roughly twenty prints.[415]

### The transition to production

Because a new mould is expensive, injection moulding penalises design variation, whereas printing makes cheap one-offs; that asymmetry is what makes parametric modelling valuable, since engineer time spent generating variants is the cheap part.[374] Between printing and injection moulding sit low-pressure moulding processes that avoid the multi-hundred-ton clamping pressure of injection moulding and serve both testing and small-run production.[379] An alternative prototype route for small mechanical parts is to machine a positive master, cast a silicone negative from it and pour urethane into that, a route used to prototype miniature planetary gear sets.[331] Mould making has itself become cheap enough to compete: a five-axis machine can cut a soft-metal or steel mould for hundreds of dollars, and cast-off moulds can be bought second hand and modified by welding on a new gate.[702]

Printing production enclosures does not scale. On the Ninja Block programme, printing the cases for a funded hardware product meant running several machines continuously to produce hundreds and eventually close to a thousand parts, covering the main case and every accessory enclosure; the second version of the product moved to injection moulding, which brought its own problems but was decisively better than printing at that volume.[189] Printed cases are a reasonable production choice only at volumes of roughly ten units or fewer.[189] Printed production parts also disappoint on finish quality, which together with the machine-tending burden is why the practitioners who have done it describe it as not to be repeated.[415]

### Outsourcing and machine ownership

Service bureaus give access to machines an individual could not justify: the owner of a five-hundred-dollar desktop machine can send a job to a hundred-thousand-dollar machine and pay only for material and time.[313] Distributed printing marketplaces differ from bureaus in owning no machines: they locate the nearest privately owned printer, list its capabilities and price, and act purely as a transaction layer.[313][244] The buy-versus-outsource arithmetic favours outsourcing for most users: a good desktop machine at about two thousand dollars buys roughly forty bureau prints at around fifty dollars each, more than most people order in a year unless they are iterating heavily.[312] Bureau pricing carries a large premium over material cost: a tennis-ball-sized part cost about a hundred and fifty dollars rush-printed at a commercial bureau against roughly twenty dollars at a shared workspace charging material only, but the shared machine ran just once a week, so the trade between the two is a schedule one.[473] Low-cost board fabricators added printing services at prices low enough to weaken the case for owning a machine at all.[619] Most people working in this space do not need to own the equipment: the work can be sent out, and a great deal can still be accomplished with a Dremel and a file.[353]

### Equipment selection

The selection criterion that matters for a working machine is the size of its user community and depth of support rather than headline specifications, so that any problem encountered has already been solved and documented by someone else.[610] Deliberately staying on well-supported, slightly older equipment means never running out of forum threads when a problem appears.[610] A vendor that supplies filament tuned to its own machines removes a variable from the workflow, so that a user who stays on the supported path does not have to think about material parameters at all.[627]

The technology's real effect has been argued to resemble precision casting rather than the semiconductor: a genuinely important process whose consequences reach consumers only indirectly, and which does not threaten commodity injection moulding of items costing fractions of a penny.[405]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 30 | Agilent, Analog, Cold Fusion - Funding Fusion Is Not Futile | https://theamphour.com/the-amp-hour-30-funding-fusion-is-not-futile/ | |
| 35 | An Interview with Jeri Ellsworth - The Ternary Tussle | https://theamphour.com/the-amp-hour-35-the-ternary-tussle/ | |
| 45 | Texas Instruments, OPA & Chevy Volt - Nerdy Neuroelectronic Neurosis | https://theamphour.com/the-amp-hour-45-nerdy-neuroelectronic-neurosis/ | May 30, 2011 |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | |
| 75 | An Interview with Ben Krasnow - Sprauncy Saccadic Spintherism | https://theamphour.com/the-amp-hour-75-sprauncy-saccadic-spintherism/ | |
| 78 | Alteritous Andy's Absquatulation | https://theamphour.com/the-amp-hour-alteritous-andys-absquatulation/ | January 16, 2012 |
| 94 | Gnomic Gazumping Gobemouche | https://theamphour.com/the-amp-hour-94-gnomic-gazumping-gobemouche/ | May 6, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 204 | An Interview with Noah Feehan - Biloquistic Blinking Blush | https://theamphour.com/204-an-interview-with-noah-feehan-biloquistic-blinking-blush/ | June 23, 2014 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 244 | The Art Of Staying Interested In Electronics - Exponible Electronics Ennui | https://theamphour.com/244-the-art-of-staying-interested-in-electronics-exponible-electronics-ennui/ | April 7, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 312 | Aussie Bound! | https://theamphour.com/312-aussie-bound/ | August 17, 2016 |
| 313 | My Kind of Town | https://theamphour.com/313-my-kind-of-town/ | August 31, 2016 |
| 317 | A Decoupled Episode | https://theamphour.com/317-a-decoupled-episode/ | September 28, 2016 |
| 331 | An Interview with Simone Giertz | https://theamphour.com/331-an-interview-with-simone-giertz/ | January 11, 2017 |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 368 | The EEVblog Sparkgap Generator | https://theamphour.com/368-the-eevblog-sparkgap-generator/ | November 19, 2017 |
| 369 | An Interview with Jason Huggins | https://theamphour.com/369-an-interview-with-jason-huggins/ | November 26, 2017 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 379 | An Interview with John Saunders | https://theamphour.com/379-an-interview-with-john-saunders/ | February 11, 2018 |
| 405 | An Interview with Spencer Wright | https://theamphour.com/405-an-interview-with-spencer-wright/ | September 3, 2018 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 416 | An Interview with James Bruton | https://theamphour.com/416-an-interview-with-james-bruton/ | November 18, 2018 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 437 | An Interview with Chrissy Meyer | https://theamphour.com/437-an-interview-with-chrissy-meyer/ | April 7, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 480 | An Interview with Ben Krasnow, 8 years on | https://theamphour.com/480-an-interview-with-ben-krasnow-8-years-on/ | February 16, 2020 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ | January 31, 2021 |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ | March 28, 2021 |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ | July 18, 2021 |
| 559 | Occam's Engineering Razor | https://theamphour.com/559-occams-engineering-razor/ | September 26, 2021 |
| 582 | The Same Wavelength | https://theamphour.com/582-the-same-wavelength/ | March 20, 2022 |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ | November 20, 2022 |
| 611 | Grad School Time Capsule with Joshua and Zach | https://theamphour.com/611-grad-school-time-capsule-with-joshua-and-zach/ | December 4, 2022 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 623 | Artisanal Crystals | https://theamphour.com/623-artisanal-crystals/ | March 12, 2023 |
| 625 | Gremlins in the machine | https://theamphour.com/625-gremlins-in-the-machine/ | March 26, 2023 |
| 627 | Works on my machine | https://theamphour.com/627-works-on-my-machine/ | April 9, 2023 |
| 665 | Really long needle nose pliers | https://theamphour.com/665-really-long-needle-nose-pliers/ | April 24, 2024 |
| 668 | 50.0000 Ohms | https://theamphour.com/668-50-0000-ohms/ | May 30, 2024 |
| 675 | Changing Course with Shawn Hymel | https://theamphour.com/675-changing-course-with-shawn-hymel/ | August 8, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
| 694 | Voltage, Vibes, and VOCs | https://theamphour.com/694-voltage-vibes-and-vocs/ | May 21, 2025 |
| 702 | Test Point Accupuncture | https://theamphour.com/702-test-point-accupuncture/ | September 14, 2025 |
| 705 | Psst...Hey buddy, wanna buy an Octopus? | https://theamphour.com/705-psst-hey-buddy-wanna-buy-an-octopus/ | October 8, 2025 |
| 712 | Robots Everywhere with Aaed Musa | https://theamphour.com/712-robots-everywhere-with-aaed-musa/ | January 19, 2025 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
