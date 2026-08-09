---
title: ASIC
concept: asic
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

An **application-specific integrated circuit** (ASIC) is an integrated circuit designed and fabricated for one fixed function, as distinct from a general-purpose processor or a field-programmable device. The economics that bound ASIC use are set by the fabrication process rather than by the devices themselves: as processes move to tighter geometries on larger wafers, the cost of a mask set rises, passing ten million dollars at the leading nodes, so an ASIC remains viable for an ever-shrinking set of applications.[103] Where one is warranted, dedicated silicon wins on efficiency by a large factor rather than a small one — implementing a fixed function as an ASIC rather than in an FPGA is worth something like twenty times, and possibly more.[254] Most of the effort in building an ASIC is verification rather than design, because a tape-out cannot be corrected once the masks are made.[547]

## Economics

The cost structure of an ASIC is almost entirely non-recurring: the first chip costs ten million dollars and the second costs ten million dollars and one dollar, which is what the question of required volume really asks.[503] The consequence is a volume threshold: the product has to ship in very high numbers before the mask set is recovered.[103] The break-even point has moved by orders of magnitude — around 1989 the dividing line was roughly a thousand pieces, and only in rare cases at that, whereas a thousand pieces is no longer anywhere near enough.[103]

Those figures assume an advanced node and an outside design team. Bringing an in-house design effort to an older process can put the cost well below ten thousand dollars, for a chip that has what is needed and very little else.[503] At the low-volume, high-price-per-chip end of the market, non-recurring engineering — the cost of the tools and of the team — dominates rather than the wafers, which is the case that open-source tooling addresses.[672]

Comparing an ASIC against a programmable part on price alone is a mistake: area, physical size and, most critically, power consumption also separate the two.[264]

### Gate arrays

Structured or metallised gate arrays sit between an FPGA and a full custom chip: the vendor has already fabricated an underlayer containing serialisers, memory blocks, multipliers and a sea of gates, and the customer buys only the metal layers that wire them together.[147] The economics of that middle route are proportionate: the non-recurring cost is nowhere near the half-million dollars of a 65-nanometre mask set, and the price paid is a higher cost per part — perhaps four dollars where a full ASIC would have been one.[147] On one product programme, Jeri Ellsworth's team needed the part under five dollars against a twenty-dollar FPGA doing the same work.[147]

## Comparison with programmable logic

ASICs always win on efficiency for a fixed function; the obstacle is not the technology but that few organisations can afford to spin one.[254] The requirement that follows is that the application be both large and stable: the device has to be formed exactly to one application, and if that application is not huge the money is never recovered.[254] A standard settling in a market removes the programmable option: once a video resolution and format are fixed, the volume manufacturers spin an ASIC for it.[254]

The dividing line also moves because programmable parts grow: an FPGA in the 85,000-logic-element class holds far more functionality than devices that were built as ASICs twenty years earlier.[423] Building a programmable device company requires three capabilities developed concurrently — the architecture, the software and the IC design — because working them sequentially yields a device two or three times larger than the best competing part; the software in question is the placement, routing and fitting algorithms, not the user interface.[535]

The conventional model is to prototype on an FPGA and then harden the whole design once, after which it stops changing. A more useful model would harden only the parts that have stopped evolving while the rest stays programmable — but FPGA vendors have no incentive to let a customer harden their PCI Express controller and stop buying their parts.[501]

## Justifications

Volume is not the only justification. Absolute lowest power consumption and a range of other parametric requirements keep ASICs in use where the unit count alone would not.[103] Moving a function from an FPGA into an ASIC is often driven by heat rather than by cost: an FPGA working hard on continuous data runs warm, and in a head-mounted product — such as the augmented-reality hardware Ellsworth's team developed — the thermal limit is the binding one.[173]

The absence of a suitable part is itself a reason to make one: a design needing a DC–DC converter that would start at 0.6 volts found that no manufacturer made one, and had to spin its own chip because nothing on the market was close enough.[389] A cryptographic mining algorithm is a good ASIC target precisely because it is simple: repeated bit operations that are easy to build in hardware and easy to run in parallel, which is where the advantage over a sequential processor comes from.[361] The same argument applies to inference: a fixed computation repeated over and over — object detection on a camera feed, say — is exactly what custom silicon is for, where an FPGA would cost more in silicon area, power and development time.[619]

For a purely digital design at an older process node there is little reason to make a chip at all — a microcontroller does the job. The distinctive case for a low-volume custom ASIC is analog and mixed signal: high-performance analog combined with a radio or a processor core on one die is something no other route produces.[672]

Obsolescence is a distinct justification: an old board whose parts no longer exist can be re-implemented as a chip, weighed against a last-time buy of ten years of stock. The design files then belong to the owner, who can rebuild the part for as long as some fab will run it.[503]

The question of whether a system needs an ASIC is hard for the people who would benefit, because the knowledge of how an ASIC trades off against a two-chip or multi-chip solution sits on the ASIC side of the industry; the system designer dismisses the option on cost before evaluating it.[503]

## Design flow

### Description and synthesis

Hardware description languages are among the genuinely portable standards: careful RTL that avoids vendor-specific IP blocks runs across different FPGA vendors' devices and can be taken into an ASIC without change, even though the languages are harder to work in than a modern software language.[650] Logic synthesis is the step that bridges a description to an architecture: the same adder written in HDL becomes a dedicated adder primitive, a chain of carry cells in an FPGA, or NAND and NOR gates for an ASIC, depending on what the target offers — the analogue of compiling a program to machine code.[374]

Portability has to be designed for: inferring a memory by declaring an array in Verilog is hazardous because it binds the design to one vendor's primitives, so memories are wrapped behind a generic interface that can be re-implemented on a gate array, a full ASIC or another vendor's FPGA.[173] Those wrappers must be explicit about polarity: an ASIC vendor supplied an I/O whose enable had the opposite polarity to the others, which nearly rendered a chip unusable and was recovered only in software.[173]

### Prototyping and verification

Prototyping on an FPGA transfers safely in proportion to how close the prototype is to the RTL that will be used in the ASIC.[147] The nine-month wait for silicon shapes the whole development flow: after simulating the RTL against a test bench, the same design is ported to an FPGA with wrappers mapping the I/O to the device's pins, so the host microcontroller's firmware and the interface between them can be brought up and debugged long before the chip exists.[721] Hardening is the last step and not a single one: throughout the process the design is repeatedly checked against whether it can actually be implemented — whether it meets the target frequency and fits the area — rather than only at the end.[721]

Most of the effort in building an ASIC is verification rather than design, because a tape-out cannot be corrected; the universal verification methodology is the established framework for it, and its SystemVerilog basis is the gap in open tooling.[547] Simulation is layered by cost: a behavioural simulator runs the known parts of the system fast, while the peripheral or block under development is simulated in HDL alongside it much more slowly, and because only part of the system is slow the overall result remains usable.[519] Above simulation sits emulation in hardware: EDA vendors sell boxes containing grids of high-end FPGAs whose purpose is to run an ASIC design before it is committed.[176]

The specific failure that makes verification unavoidable is a state machine that can reach a state from which it cannot be unblocked, since there is no recovery short of a new mask at the cost of the original one — which is why formal methods are used where failure cannot be tolerated.[467] A chip cannot be bodged, so observability has to be designed in: internal sensors and current measurement in the support harness let a designer find out why something failed and improve it, rather than treating a tape-out as final.[501]

ASIC place and route is not a clean compilation step: the design that comes out at the end typically carries a couple of thousand errors that have to be fixed by hand, in the way a board design rule check does.[501]

### Designing for fixedness

Because a respin is the only way to change fixed logic, flexibility is designed in deliberately: putting a small processor core on the die to handle low-level behaviour during idle periods means those functions are not hard-coded, and unused serialisers are left in place to be enabled if a later display needs them.[147]

### Physical realities

The mental model transferred from FPGAs misleads. An FPGA gives a flip-flop with every logic tile; an ASIC is a blank slate on which everything is placed, and a flip-flop turns out to be six to eight times larger than an inverter.[616] Component ranges on a die bear no relation to board level. Board designs use resistors from about one ohm to ten megohms and capacitors from a picofarad to ten thousand microfarads; on-chip capacitors run from femtofarads to picofarads.[672] Absolute values on a die cannot be relied on: components can be matched to about one percent to each other on the same die but vary by around thirty percent from wafer to wafer, which is why analog design on silicon is done in ratios rather than absolute numbers.[672]

Decoy structures are placed on chips deliberately: circuits that do nothing, included so that someone x-raying the die spends months working out that they are not part of the design.[110]

### Team scale

Small teams can produce large chips because the work is at the level of top-level code: at Adapteva, Andreas Olofsson's chips were each done by fewer than three designers, and a 28-nanometre part of 200 million transistors was completed in twelve weeks by three engineers.[254]

## Industry structure and access

Data does not flow in the ASIC industry because of how the agreements are structured: with several proprietary parties involved, obtaining the information needed for a design can require a three- or four-way non-disclosure agreement negotiated between organisations with different priorities and lawyers charging eight hundred dollars an hour.[501] The same agreements block reproducibility: research cannot be replicated if the raw data requires agreements with three separate companies to obtain, which suppresses the ability to demonstrate that one approach to a circuit is better than another.[501]

Access to processor IP has loosened under competitive pressure: the HDL for two ARM cores was put on the web for download under a licence that forbids using it in an actual ASIC, in what reads as a response to RISC-V.[374]

An open process design kit at 130 nanometres, with shuttle runs sponsored by Google through SkyWater, made tape-out accessible on the condition that the submitted designs be open source.[541] A multi-project wafer slot is small but not trivial: roughly 3.3 by 2.8 millimetres, about ten square millimetres, which was enough to hold a set of a designer's FPGA-scale projects at once, and enough that nine separate designs shared one slot.[616] Bringing up a returned chip from such a run can require more instrumentation than the chip itself: one recovery used an FPGA to emulate the memory the on-die RISC-V core executed from, counted the instructions retired while sweeping the core voltage, and found an undervolted operating point at which enough instructions ran to configure the GPIOs.[616]

There is a graded path into the field: draw a few standard cells in a browser-based tool and run the automated flow to get a chip made; then build fundamental digital blocks — a full adder, a register, a linear feedback shift register — and test them; then learn a hardware description language.[672] The groups that benefit from cheap tape-out are small companies, universities and research institutions, and projects that would otherwise be stuck with an FPGA when what they need is a chip.[390]

### Chiplets

Chiplets apply the modular approach at silicon level: an existing die layout is reused and joined to others over a standardised interconnect, so a device can be assembled from off-the-shelf blocks and the design time cut.[639] Several competing interconnect standards exist — UCIe, which is serial and named by analogy with PCI Express, alongside Bunch of Wires and OpenHBI — with UCIe agreed among the major vendors and released in March 2022.[639]

One commercial expression of that model lets a customer select from a portfolio of chiplets in a browser and have the assembled device built for them, which makes the resulting part specific to that customer without a custom design effort.[650] The evaluation loop can be closed without silicon: selecting blocks emits the corresponding RTL, which is sent to cloud FPGA instances, loaded as bitstreams, and returned as a terminal session against the configured device within minutes.[650] The market for such a service is neither end of the spectrum: designers well served by existing microcontrollers and FPGAs do not need it, and organisations with effectively unlimited budgets already run thousand-person design centres. It is the middle — specialised requirements, real constraints on size, weight and power, and limited engineering budget, as in aerospace and defence.[650]

## Use in test and measurement equipment

Bringing the signal chain into a custom chip is what enabled a low-cost instrument line to be designed and built in-house rather than rebadged: once the development is paid for, the chip itself costs a few dollars to produce, and it delivers performance the competition cannot reach.[30] That chip put the performance of an oscilloscope into a single device, and it was developed over several years by essentially one engineer.[31]

Features are decided at chip design time and cannot be added later, which is why niche capabilities are excluded: independent time bases per input channel would have raised the complexity of the design substantially for a rare need, so the answer offered to a customer who needs it is a second instrument.[145] Dedicating one converter chip per channel removes a compromise built into shared designs: 6.25 gigasamples per second per channel that does not halve or quarter when further channels are enabled.[347] Where a function is implemented decides whether it costs anything to use: with serial decoding, FFTs and measurements built into the chip, turning them on does not slow the instrument, whereas a single measurement left in software dropped the waveform update rate from a million per second to under a thousand.[619] A custom front-end amplifier chip is amortised across an entire product line, appearing in the flagship and in models an order of magnitude cheaper, with the lower models deliberately limited in firmware.[654]

Converter performance in an instrument is bounded by clock jitter, which relates directly to the maximum effective number of bits achievable; the rapid improvement in instrument specifications came from 5-to-10-gigasample CMOS converters, where dense calibration algorithms can be built alongside the converter.[228] Above about 110 gigahertz the connector rather than the silicon becomes the limit: a one-millimetre connector is no longer 50 ohms at that frequency, so measurement moves to digitising in frequency bands or down-converting instead.[228]

Very low-cost consumer instruments are built around a chip and almost nothing else: an epoxy blob with a few supporting passives is what makes a five-dollar multimeter possible.[87]

## Lifecycle and obsolescence

An ASIC can outlive the process that made it: when a fab retires a node the customer places a final order — perhaps a million parts — and ships product from that stock for years afterwards, which is why date codes on chips inside current instruments run years behind.[646] Eventually that runs out. A calculator ASIC designed in the 1980s could no longer be manufactured because nobody runs a 20-micron process any more, ending a product with a stable market.[53]

Semi-custom parts are available to customers with sufficient volume: a large buyer can have an analog vendor spin a variant of an existing device. For everyone else, given time-to-market pressure, assembling the function from standard parts is faster than waiting for a perfect chip.[53]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 30 | Agilent, Analog, Cold Fusion - Funding Fusion Is Not Futile | https://theamphour.com/the-amp-hour-30-funding-fusion-is-not-futile/ | |
| 31 | Freescale, Hackerspaces, Printable Electronics - Publish Popular Parts Please! | https://theamphour.com/the-amp-hour-31-publish-popular-parts-please/ | |
| 53 | Biarchy Birthday Bavardage | https://theamphour.com/the-amp-hour-53-biarchy-birthday-bavardage/ | |
| 87 | An Interview with Ian Daniher - Nascent Nonolith Numquid | https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/ | |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 110 | Armstrong, Camenzind & Museums - Outstanding Oneirophoros Obituaries | https://theamphour.com/the-amp-hour-110-outstanding-oneirophoros-obituaries/ | August 26, 2012 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 147 | An interview with Jeri Ellsworth - Absorptive Augmented Actuality | https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/ | May 27, 2013 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 228 | An Interview with Shahriar from The Signal Path - Quisquous Quivering Quadripole | https://theamphour.com/228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole/ | December 16, 2014 |
| 254 | An Interview with Andreas Olofsson - Adapteva's Ampliative Abacus | https://theamphour.com/254-an-interview-with-andreas-olofsson-adaptevas-ampliative-abacus/ | June 16, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ | April 29, 2018 |
| 423 | Open FPGA Toolchains at 35c3 | https://theamphour.com/423-open-fpga-toolchains-at-35c3/ | January 1, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 519 | Simulating Embedded Hardware with Michael Gielda | https://theamphour.com/519-simulating-embedded-hardware-with-michael-gielda/ | November 29, 2020 |
| 535 | Efinix FPGAs with Sammy Cheung | https://theamphour.com/535-efinix-fpgas-with-sammy-cheung/ | March 21, 2021 |
| 541 | Chip Shortage Denier | https://theamphour.com/541-chip-shortage-denier/ | May 10, 2021 |
| 547 | Open Source Mindset with Michael Gielda | https://theamphour.com/547-open-source-mindset-with-michael-gielda/ | June 28, 2021 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 639 | Daaaamn We're Duuuummmb | https://theamphour.com/639-daaaamn-were-duuuummmb/ | July 17, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 650 | Accessible ASICs with Andreas Olofsson | https://theamphour.com/650-accessible-asics-with-andreas-olofsson/ | November 12, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 721 | Chip Design for Fun (and Waffles) with Julia Desmazes | https://theamphour.com/721-chip-design-for-fun-and-waffles-with-julia-desmazes/ | April 8, 2026 |
