---
title: Datasheet
concept: datasheet
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **datasheet** is the document published by a component's manufacturer that states how to use the part and what performance it guarantees; from a system designer's position, the internal process technology of a part is irrelevant compared with whether the part can be bought and whether its document states how to use it and what it guarantees.[230] The guarantees that bind a design are carried in the minimum and maximum columns of the specification tables rather than on the marketing summary page, and the difference between the two is routinely large.[53][97] Datasheets and their companion application notes are where current engineering practice is documented, whereas textbooks describe methods that remain correct but predate the parts in use.[15] Because the purchaser of a commodity chip has no visibility into what is inside and no proof that it behaves as described until it is on a board and running, buying the part is, in effect, "buying a data sheet".[650]

## Content and organisation

### Front page and feature lists

The first page of a datasheet is written by marketing and states the most favourable figures; the standard advice is "don't trust front page specs".[53] The feature list functions as a competitive checklist: customers compare two vendors' lists item by item, so features that a given customer will never use still have to be present for the part to survive the comparison.[103] A related-products box on the front page, listing parts of similar function with different feature sets or packages, allows a designer who has nearly the right part to navigate to the right one without a fresh search.[88]

Front-page figures are also aggregates rather than simultaneous capabilities: a part advertising four UARTs may not be able to run them at once because they share internal resources, a constraint not stated at the top of the document.[654] Pin-multiplexing restrictions, under which a peripheral is available only on particular pins, are likewise not stated prominently, even though assigning a peripheral to an unsupported pin invalidates the board.[375]

### Electrical characteristics: typical, minimum and maximum

What matters to a designer is the minimum and maximum columns rather than the typical ones, and those appear several pages in rather than on the summary page.[97] Worst-case figures are guaranteed by the manufacturer and usually stated at the temperature extremes, so they are what a power budget or a timing margin is built from; typical figures are appropriate only for estimates such as expected battery life, and adding up typical numbers produces a design that fails at the corners.[53] The rule of thumb is "never use typical figures from a data sheet": designing to them is done at the designer's risk, and any design that depends on the result should be measured rather than assumed.[36] The stated range exists because the parts vary across it; treating the typical value as the value the part will have discards the information the range was published to convey, which is why statistical process control and error budgets matter when performance is being relied on.[377]

On precision parts a good manufacturer publishes the distribution measured across thousands of devices, so the designer can see the production spread rather than a single number; commodity ("jellybean") parts do not carry that data because nobody needs it, and a well-known manufacturer's name is not a substitute for reading it.[578]

### Characteristic curves and application circuits

The characteristic curves in a datasheet accumulated historically: each was invented at some point to answer a particular customer's problem and then became a standard inclusion, so the document grows by accretion rather than by design.[348] Some manufacturers publish dozens of application schematics per part, showing the part used in many different configurations, and those circuits are a large part of the document's practical value.[315] A substantial proportion of published schematics in the wider literature are the manufacturer's application circuit reproduced with little change, so reading the datasheet for an unfamiliar part often explains an entire design that appeared original.[15]

### Registers and operational description

A complete register description is not sufficient to use a peripheral: what is missing is a worked example of the intended usage, and a generated list of register definitions does not supply it.[383] For decisions such as how many bypass capacitors a device needs, the datasheet's recommendation is the available answer from a blank sheet, since understanding why they are needed does not by itself determine the number.[329]

### Footnotes and buried restrictions

Critical caveats appear as footnotes in reduced type rather than in the specification tables, and a designer juggling thousands of parameters across a device has no reliable way to find them by inspection.[661] A feature listed on the front page may carry a tolerance in a footnote that changes what it can be used for: an integrated current limit with fifteen percent tolerance over temperature is adequate for crude overload protection and useless for a precision current-limited supply.[154] The decisive restriction is frequently a note beneath a diagram deep in the document stating that some feature does not work, which is read last if at all.[432]

## Production and maintenance

Which parameters appear as headline specifications is decided by a product definer who visits customers to learn which specifications their applications turn on; applications engineers then review the document, and vendors deliberately follow industry convention so that competing parts can be compared.[348] The theory-of-operation sections originate in the internal system specification written while the part is being defined, with the designers describing how a feature works as it is added; how much of that description survives into the published document is a deliberate decision, since competitors read it too.[270]

New datasheets are produced by copying the document for the nearest existing part and editing it, at a rate of hundreds of parts a year; errors survive that process as a matter of course, so a fresh datasheet for a new part is among the least reliable.[482] Datasheets are revised, and errata are added in later revisions, so working from a copy downloaded earlier means working from a document known to be wrong; long-established silicon carries less of this risk because the problems have been found.[482]

The figures in the document are backed by production test. Precision analog parts are tested individually rather than sampled statistically, at both die and packaged stages, and nearly every published parameter is measured on every device; that test time is a substantial part of why such a part can cost fifty dollars.[348] Digital parts can be functionally tested, but analog parts must be characterised against guaranteed limits and then sorted into grades, which is why the same silicon appears as several part numbers at several prices; designing the test fixtures for that characterisation and running it is a large and expensive part of bringing an analog part to market.[502]

## Use in circuit design

Part selection is conducted across dozens of simultaneously open documents, and the reasoning about why each candidate was accepted or rejected is frequently not recorded anywhere, so losing the set means repeating the comparison.[190]

A thorough part check assumes nothing: each pin on the schematic symbol is cross-referenced against the datasheet, then the footprint's pitch and pad sizes, then the mapping between symbol and footprint.[201] Package families whose names differ by a few characters are the common source of wrong footprints, because the designer recognises the general shape and skips the verification, and no fabricator can catch the error since the board is manufacturable either way.[505] Package drawings are frequently dimensioned from a mechanical draughtsman's perspective rather than from the origin a layout tool needs, so the numbers required to build a footprint have to be derived rather than read off.[536] The page-count economy that justified terse package drawings ended with printed data books, and the continued absence of additional views is a source of avoidable footprint errors.[370]

Parameters not stated directly can often be derived from those that are: a logic output's effective source resistance follows from the specified high-level output voltage at a given output current, which is how a design driving LEDs with no series resistors can be shown to be relying on the driver's output impedance.[598] For the lowest sleep currents each unused pin must be put in the state the manufacturer recommends, which is usually but not always an output driven low; the recommendation differs between parts and has to be read for each.[527]

Datasheets also support inference about the silicon itself. Where a family of parts once differed in forward voltage, capacitance and leakage, identical datasheets across the family suggest a single die is now sold under every number in the series, differentiated only by its voltage rating.[574] Datasheets for integrated parts can name the licensed peripheral blocks and their revisions, so tracking the document across years shows when a vendor changed the source of a peripheral—information which occasionally explains behaviour that changed with silicon revision.[652]

Some comparisons the designer wants are not published at all. Power figures quoted per megahertz are not comparable between microcontrollers, because parts differ in instructions per cycle and in whether the core is fed by a linear regulator or a switching converter; the comparable figure would be power per instruction, which datasheets do not publish, so the only reliable comparison is to build both boards and measure them running the same software.[629]

## Use in firmware and bring-up

Reading datasheets is part of firmware work at the level of power management, where understanding the device's modes and the trade-off between clock frequency and consumption is required; this is one reason the boundary between firmware and hardware skills is soft.[189] Hardware engineers necessarily work out register addresses and programming sequences while drawing the schematic, and when that work is not written down the firmware engineer repeats it; handing over a few expected values alongside the schematic also gives the firmware engineer a way to tell whether the result is right.[373]

Configuring a complex peripheral such as a serialiser from the datasheet alone, register by register, is a week of full-time work, and starting from the vendor's supplied default register set removes that week.[148] A workable method for a new peripheral is to start from vendor example code to get something compiling and producing output, then use the datasheet to correct the register values to what the application actually needs, rather than deriving the whole configuration from the document first.[617] Bringing up a modern microcontroller from the datasheet alone, without vendor configuration tools, is a project measured in months to a year, and the same is true of a peripheral such as a display controller documented in several hundred pages.[479]

Document length determines whether one person can hold a whole part in their head: at a thousand pages that is not feasible, while at three or four hundred pages a few weeks of reading gives an engineer a working understanding of how the chip fits together.[637] Length is not completeness, however; a single part has been documented in five thousand pages that still left questions answerable only by the vendor.[54]

A long bring-up reaches a point where the engineer cannot distinguish between having missed something in a document read repeatedly and having found a genuine defect, and note-taking becomes the substitute for a second person to check the reasoning.[474] When a peripheral that gives no visibility into its state refuses to respond and the small set of usual causes has been exhausted, systematically varying the inputs to see whether anything changes is a legitimate technique, and is the one that finds a bit documented incorrectly.[479] Unstructured trial and error can change the behaviour without revealing why, leaving a second fault masking the first; the recovery is to instrument the code, confirm what is actually happening, and re-read the reference manual with that observation in hand.[460]

## Reliability and failure modes

The limiting conditions that make a part unsuitable are buried, not summarised, so avoiding them means reading the whole document; schedule pressure means engineers routinely accept that risk instead, choosing the part without having read every page.[186]

Working at register level against a datasheet that is simply wrong is a recognised failure mode encountered repeatedly over a career, and it is the case in which methodical reading cannot converge.[470] A board laid out correctly from a published pinout can still be wrong because the pinout itself was documented incorrectly against the silicon—the correction appearing as errata in a later revision— as in a case where two UART pins were swapped in the document.[468] A parameter can depend on an operating condition the datasheet does not relate it to: an amplifier's offset voltage varying with supply rail was found by experiment after the fault was mistakenly attributed to board layout, with the published histograms at two supply voltages giving no hint of the dependence.[146] An application circuit printed in the datasheet has been found to drive the part beyond its own specified limits; once that trust is broken, a vendor's assurance and a corrected document do not restore it, because a field failure later cannot be laid at the vendor's door on the strength of a document since revised.[140] Protection structures may be absent or far weaker than implied: in one case a high-voltage driver specified with clamping diodes destroyed parts under inductive kickback because the diodes could not carry the stated conditions.[480]

A blanket footnote reserving the right to change any specification undercuts the document's contractual force, and it has been invoked by suppliers declining to guarantee the performance a customer designed around.[290] Silicon can also be redesigned without a part number change and with the new limitation stated only deep in a revised datasheet: an amplifier used in the front end of many oscilloscopes lost the input offset range it had been designed around, and instruments were damaged before the change was traced.[727] Successor parts advertised as improvements are frequently better on one axis and worse on another—higher bandwidth but lower slew rate, for example—so a substitution presented as an upgrade must be checked against every parameter the design depends on.[727]

Parts frequently perform far better than their specification, and designs quietly come to depend on the observed behaviour rather than the guaranteed one; when a process change moves the part back towards its published limit, the manufacturer is within its rights and the design is broken.[36] Measurement sometimes confirms the document rather than beating it: a widely used regulator's dropout voltage matched its published load graph almost exactly, so the margin a designer hoped to find was not there.[36]

An unspecified parameter is not a favourable one. A part five times cheaper than its established equivalent may omit a parameter that determines whether it is safe in the application, such as a switch's on-resistance.[663] A datasheet found by searching an exact part number may also describe a different device: the same number has appeared on a six-pin package and an eight-pin one with different internal architecture, so the correspondence between marking and document cannot be assumed.[462] Some component documentation is deliberately thin because the manufacturer expects its real customers to be supported by an applications engineer; for anyone without that relationship, undocumented behaviour—such as a clock divider that must also be set before a mode change takes effect—has to be discovered experimentally.[473]

Substituting an equivalent part is not free even where the specifications appear to match: the substitute must be revalidated against the datasheet in the application, which is why specifying manufacturer and part number exactly is the norm for silicon in production.[175]

## Simulation and machine readability

A simulation model cannot in general be constructed from a datasheet, because the document does not contain the characteristics the model needs; for bipolar transistors the quasi-saturation region is never documented well enough and the attempt is hopeless.[196] A MOSFET model good enough for switching supplies can be built by fitting model parameters until the simulated output characteristics, on-resistance against gate voltage and gate charge reproduce the published curves, a process that is laborious even for an expert, taking of the order of an hour.[196] Different curves in the same datasheet are frequently measured on different physical devices, so no single set of model parameters can reproduce them all: the gate-charge and output-characteristic curves may come from parts with different threshold voltages, and no transistor exists that behaves like the composite document.[196] Simulators of embedded hardware are likewise built from datasheets and inherit their errors, so the practical validation is whether real software behaves correctly on the model rather than whether the model matches the document.[519]

Publishing datasheets as PDFs means the characteristic curves are pictures: a designer operating between two published supply voltages cannot interpolate, cannot read values off a curve, and has no access to the underlying numbers; vendors are hesitant about interpolation because the part is characterised only under the conditions shown.[392] A single machine-readable format for component data, rather than millions of PDFs, would make symbols, footprints, models and parameters usable by tools directly; the obstacle is inertia rather than difficulty, and each part carries hundreds or thousands of attributes that resist simple structuring.[163]

Partial automation exists. Optical character recognition applied to a datasheet's pin table can extract the pin list and classify pins as inputs, outputs or power, generating a schematic symbol from the document rather than from manual transcription.[531] Building library data from a datasheet remains skilled work rather than a task for a junior: electromechanical parts require interpreting plated and non-plated holes, slotted features and the density level the footprint should follow, and the standards do not define everything, leaving pin-one markers and silkscreen widths to preference.[531] Older parts survive only as scans of photocopies, skewed on the page and beyond the reach of text recognition, so their contents cannot be searched or extracted.[273]

## Access, distribution and preservation

Before the internet the printed data book was the only source of component information, so which manufacturer's books an engineer happened to own determined which parts they designed with; companies that gave books away freely, or sold them through retail, acquired designers by that route.[52] The data book model broke on volume: at hundreds of new parts a year and twenty or thirty pages each, the annual book could not keep growing, which forced the move to other distribution.[326] Between printed books and the web, datasheets were distributed as a rented service: a supplied computer with several hundred floppy disks of scanned documents, searched through an index disk that then directed the user to insert a particular numbered disk.[326] Giving away expensive documentation to win future component sales is an old pattern in the industry rather than a recent one, predating the software businesses now identified with it.[366]

Access is not always open. Requiring a non-disclosure agreement to obtain a datasheet removes the part from consideration for a significant group of engineers regardless of its price or capability, though a consumer product's buyers are indifferent and a company competing on cost may accept the terms.[84] Processors at the heart of widely used boards have shipped with the datasheet available only under agreement, which blocks bare-metal programming of the part by anyone outside that arrangement.[235] Datasheet secrecy is a company policy rather than a technical necessity: an acquirer has released the whole documentation set of an acquired company that had kept it under agreement.[324] A manufacturer may simply decline to sell a part or supply its documentation to a given customer, which forecloses the design regardless of how well the part fits.[588] Some ecosystems gate the datasheet behind a legal and commercial admission process, so obtaining the document is a business negotiation rather than a download; the vendor's justification is control over the quality of what carries its interface.[628]

Language and part-marking add further friction. Very low-cost parts are frequently documented only in Chinese and in a family of single-letter variants whose differences are unexplained, so the effective cost of the part includes the work of decoding its documentation.[587]

Repair work is largely conducted without documentation: with no datasheet and no schematic, the relationship between signals must be reconstructed by measuring which are present on working and failed boards, and a diagnosis that takes fifteen minutes to state may represent many hours of that reconstruction.[311]

Preservation is its own problem. Practice divides between keeping local copies and re-fetching documents from the web on demand: the argument for local copies is that documents move or disappear, and the argument against is the effort of managing them.[219] Datasheets are withdrawn from manufacturers' sites, so relying on a search engine as the repository means the reference for a part in production may cease to exist; verifying that documentation before release is part of the designer's job.[322] At the bench, a printed page is often preferred to a screen because it can be annotated and left in place while both hands are occupied; the same need drives the recurring interest in a tablet or e-reader at the bench, whose usefulness depends on rendering a page-sized PDF properly.[126]

## Role in engineering practice

Reading a datasheet is a teachable skill rather than an obvious one, involving organising what the device does well enough to explain it to someone else, and it sits alongside system architecture as a distinct topic in embedded practice.[187] It sits in the same set of core competences as laying out boards, managing a bill of materials, choosing alternative parts and cost optimisation; it is not separable from doing the work.[251] The application circuits in datasheets are a teaching resource in their own right, sufficient to learn a large part of practical electronics from.[44]

Because independent verification of every specification is beyond the resources of most designers, at some point the document is trusted; the practical question is which parameters the design actually depends on and therefore which are worth measuring.[671] Medical and defence practice verifies the published specification on the finished board rather than accepting it, which is a cultural difference from environments where a part meeting its datasheet on paper is treated as settled.[588] On the production side, Zach Fredin's rule for scaling a design beyond tinkering is to never use a part that lacks a datasheet he can rely on, since a part without one carries liability a product cannot absorb.[330] For electromagnetic compatibility specifically, layout consultant Zachariah Peterson avoids semiconductor application notes and datasheets as sources, preferring specialist publications and practitioners.[718]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 15 | Analog Components, First Person Flying and Idea Ownership | https://theamphour.com/the-amp-hour-15-analog-components-first-person-flying-and-idea-ownership/ | |
| 36 | Big Business Buffoonery | https://theamphour.com/the-amp-hour-36-big-business-buffoonery/ | |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 52 | An Interview with Jeri Ellsworth - Carnassial Chip Chemicals | https://theamphour.com/the-amp-hour-52-carnassial-chip-chemicals/ | |
| 53 | Biarchy Birthday Bavardage | https://theamphour.com/the-amp-hour-53-biarchy-birthday-bavardage/ | |
| 54 | An Interview with Jack Ganssle - Embedded Elchee Epexegesis | https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/ | |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ | |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 126 | eReaders, datasheets & board assembly - Yearly Yeasty Yapping | https://theamphour.com/the-amp-hour-126-yearly-yeasty-yapping/ | December 17, 2012 |
| 140 | Project Management, Lasers & Robots - Staunch Specialty Sanctanimity | https://theamphour.com/the-amp-hour-140-staunch-specialty-sanctanimity/ | April 8, 2013 |
| 146 | Hamvention, Arduino and Intel - Burdensome Background Battology | https://theamphour.com/the-amp-hour-146-burdensome-background-battology/ | May 21, 2013 |
| 148 | Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood | https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/ | June 3, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 186 | Someone is watching...we think - Horme Hostility Hypochondriac | https://theamphour.com/186-someone-is-watching-we-think-horme-hostility-hypochondriac/ | February 25, 2014 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 190 | Let's Hear It For The Buoys - Vanishing Vessel Vexation | https://theamphour.com/190-lets-hear-it-for-the-buoys-vanishing-vessel-vexation/ | March 24, 2014 |
| 196 | An Interview with Mike Engelhardt - SPICE Simulator Synteresis | https://theamphour.com/196-an-interview-with-mike-engelhardt-spice-simulator-synteresis/ | April 28, 2014 |
| 201 | Cheap Respins And A Time Machine - Multiscience Mercenary Marketplace | https://theamphour.com/201-cheap-respins-and-a-time-machine-multiscience-mercenary-marketplace/ | June 2, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 230 | Prepping For Hoverboards - Gallionic GitHub Gabble | https://theamphour.com/230-prepping-for-hoverboards-gallionic-github-gabble/ | December 30, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 273 | Part Choice Triathlon | https://theamphour.com/273-part-choice-triathlon/ | October 28, 2015 |
| 290 | An Interview with Mark Morin of Nufern | https://theamphour.com/290-an-interview-with-mark-morin-of-nufern/ | March 9, 2016 |
| 311 | An Interview with Louis Rossmann | https://theamphour.com/311-an-interview-with-louis-rossmann/ | August 10, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 322 | World Trade Futurity (WTF) | https://theamphour.com/322-world-trade-futurity-wtf/ | November 9, 2016 |
| 324 | Mapping Out Nerdery | https://theamphour.com/324-mapping-out-nerdery/ | November 23, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ | |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 392 | An Interview with Matt Duff | https://theamphour.com/392-an-interview-with-matt-duff/ | May 13, 2018 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 460 | Rubber Ducking | https://theamphour.com/460-rubber-ducking/ | September 29, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 470 | Just Add Salt | https://theamphour.com/470-just-add-salt/ | December 8, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 479 | Why isn't this working? | https://theamphour.com/479-why-isnt-this-working/ | February 13, 2020 |
| 480 | An Interview with Ben Krasnow, 8 years on | https://theamphour.com/480-an-interview-with-ben-krasnow-8-years-on/ | February 16, 2020 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ | August 16, 2020 |
| 519 | Simulating Embedded Hardware with Michael Gielda | https://theamphour.com/519-simulating-embedded-hardware-with-michael-gielda/ | November 29, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ | March 28, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 578 | Histogrammic or Histomagraphical | https://theamphour.com/578-histogrammic-or-histomagraphical/ | February 20, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 588 | Siloed Engineering with Leigh Brady | https://theamphour.com/588-siloed-engineering-with-leigh-brady/ | May 8, 2022 |
| 598 | Best way to find a leak | https://theamphour.com/598-best-way-to-find-a-leak/ | August 7, 2022 |
| 617 | Conference Room Innovation | https://theamphour.com/617-conference-room-innovation/ | January 29, 2023 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 629 | At least my house isn't haunted | https://theamphour.com/629-at-least-my-house-isnt-haunted/ | April 23, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 650 | Accessible ASICs with Andreas Olofsson | https://theamphour.com/650-accessible-asics-with-andreas-olofsson/ | November 12, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 663 | Motors on PCBs with Carl Bugeja | https://theamphour.com/663-motors-on-pcbs-with-carl-bugeja/ | March 25, 2024 |
| 671 | NDA Sideshow | https://theamphour.com/671-nda-sideshow/ | June 19, 2024 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1, 2026 |
