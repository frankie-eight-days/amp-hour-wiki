---
title: Reverse Engineering
concept: reverse-engineering
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**Reverse engineering** is the reconstruction of a system's design, behaviour or protocol from the artifact itself, spanning board-level circuit recovery, silicon die analysis, firmware disassembly, bus and radio protocol capture, and fault injection.[725][25][346][634][582] It is a distinct skill set from circuit design, soldering or debugging, whose defining requirement is patience, since a problem is rarely solved in the first few minutes and the initial difficulty is often working out what one is even looking at.[178] The practice matters economically as well as technically: it underpins board-level repair, market entry against incumbent tooling, salvage of undocumented components, and the detection of deliberate deception in shipped firmware, while vendors deploy a corresponding range of countermeasures against it.[507][302][388][318][303]

## Character of the discipline

Practitioners divide the work by intent into exploratory and targeted reverse engineering. Exploratory work maps a system for its own sake and treats the process as the objective; targeted work aims at unlocking a specific capability, such as discovering that a receiver and its transceiver variant are physically identical and asking what prevents the extra function from being enabled.[450]

The skills transfer directly to debugging one's own product, because both activities consist of probing an unfamiliar system and forming hypotheses about how it works; the practice also exposes the engineer to other designers' decisions, elegant and otherwise.[363] The rigour applied in experimental biology—positive and negative controls on even routine steps, and explicit checks that the starting material is sound—sets a standard for reverse engineering, where the corresponding discipline is continually asking what assumptions are in play and whether a measurement is being thrown off.[336] The process is fundamentally one of trial and error rather than certain deduction.[614]

## Methods

### Board-level circuit recovery

Recovering a circuit from a board is tractable where the board is simple and not multi-layer, because the traces can be followed visually; for popular devices the reconstructed circuit is often already published, so the work becomes checking someone else's blueprint rather than starting from the copper.[725] Efficient work depends on tooling that links the schematic to the physical board: software that imports the schematic and overlays it on a board image, so that clicking a net highlights the trace across the board. Without a schematic and layout, troubleshooting degrades into removing components at random, since a measured voltage means nothing without knowing what the node does.[561]

### Silicon-level analysis

Silicon can be reverse engineered by decapsulating the die, photographing it at high resolution and tracing the devices. One such effort mapped all 3,500 transistors of an early microprocessor and produced a transistor-level simulation that was completely accurate without any debugging, and could execute real programs while displaying the state of the die.[25] Where more than one layer must be recovered, the die is etched from the top and worked downwards through the metal layers, with the circuit redrawn as the layers are removed; the process is straightforward in principle and extremely tedious in practice.[128] Die-level work is conducted in ordinary open-air laboratories with standard equipment, rather than in the cleanrooms that imagery of the field suggests.[303]

Old patents are a substantial documentary source, because they were written in a period when even trivial inventions were filed with pages of full schematics and listings of the code a chip executed; one calculator chip was reverse engineered from that material rather than from the silicon.[361]

### Firmware extraction and disassembly

Access to the debug port is the usual entry point on a system with a processor: with JTAG control the firmware can be dumped, and even without analysing the firmware, control of the input and output pins combined with reverse engineering the board establishes what each output actually drives.[346] What a dumped firmware image typically yields is not a subtle cryptographic weakness but hardcoded material: strings identifying an undocumented page that authenticates automatically and grants control, hardcoded root passwords, and private keys shipped into devices where only public keys were needed.[346]

Disassembly proceeds like a constraint puzzle rather than by reading code linearly. One known fact, such as the byte value of a documented command, is located by searching for where it is compared; that identifies the routine, whose cross-references identify the addresses it writes; those addresses acquire meaning from what wrote to them, and each element solved constrains the next.[450] An undocumented command disclosed for an unrelated purpose is a sufficient foothold: given a peek-and-poke command with a sixteen-bit address, sweeping the entire address space and disassembling whatever comes back reveals far more than the vendor exposed.[450]

The disassembly tools divide sharply on cost and approachability. One open-source tool is powerful but low-level, with a command-line interface, a steep learning curve, and architecture support the user may have to repair; a later free tool with a graphical interface decompiles assembly into pseudo-C and is considerably more approachable; the commercial standard costs on the order of a thousand dollars once obscure targets are needed.[450]

A simulator turns static analysis into an experiment. Running the binary under simulation shows which functions write which registers, and recording every call in the simulated binary produces a trace that can be walked backwards from a breakpoint to recover the path that led there, which static disassembly alone cannot give.[599] Large language models are useful on the volume-limited parts of the problem, sorting through packet captures too large for a person to read in order to recover a proprietary over-the-wire protocol, and matching values visible in a graphical interface against a proprietary binary file to decode its format; the residual risk is that the technique is pattern matching without understanding, so a plausible answer can be subtly wrong in ways that are not caught.[722] Decompilers also guess at intent, and existing static analysis already recognises library signatures such as a formatted print routine or a system call; the realistic value is in that pattern recognition rather than in explanation, and misplaced trust in a wrong answer is harder to catch in code one did not write.[614]

### Bus and protocol analysis

Where firmware is inaccessible, the communication between a processor and a peripheral can be tapped instead. Recording the traffic between a microcontroller and its radio chip, then connecting a different microcontroller to the same radio, reproduces the function without ever extracting the original code.[363] The same approach recovers undocumented component protocols: a proprietary addressable LED string was decoded by putting a logic analyser on the data line, identifying the stream and reproducing it from a development board, which was the only route to controlling the parts at all.[308]

Reverse engineering a vehicle bus starts from an undifferentiated stream of frames at ten, twenty and fifty millisecond intervals, from which a specific identifier and then a specific bit position within its payload must be isolated. Tools narrow the field by ranking candidate fields on how fast their bits change, since the least significant bits of a slowly varying signal change fastest, and the remainder is correlation: actuate a function and see which field moves.[634] Frames on such a bus can also be attributed to the physical device that sent them, because impedance mismatches produce reflections whose effect on rise and fall times is deterministic given a transmitter's position; measuring those times precisely enough allows a map of which module transmits which frames to be built before any payload is decoded.[634] Bus traffic being visible is not the same as being understood: the protocols carried over a vehicle bus are proprietary, so the ones and zeros can be read without their meaning being recoverable except through sustained effort or by obtaining design specifications.[212]

Bluetooth Low Energy is unusually easy to survey because service enumeration is built into the protocol: any phone application can list the services a nearby device advertises, and each service carries properties that function as permissions to read, write or subscribe to notifications. Manufacturers commonly tunnel an existing custom binary serial protocol over that transport, using the write characteristic to send and the notify characteristic to receive, because the protocol offers no native asynchronous channel; the reverse engineering task therefore reduces to recovering that binary protocol from sniffed exchanges and determining whether the same messages can be sent from an unauthorised client.[698]

### Radio-frequency capture and replay

Capture and replay is the standard first attack on consumer remote controls, over infrared and over radio. In the unlicensed bands most consumer equipment sits at 433 MHz or, depending on the country, 315 MHz, covering garage door openers, mains remote controls and wireless weather stations, and a receiver shield producing the raw waveform is enough to start.[349] Recurring work justifies purpose-built tooling: a board carrying a wireless microcontroller and a switching supply at one end, with the remaining half left as blank prototyping area, lets a remote control be stuck down and wired in directly, replacing the jumper-wire setup that made each such job unattractive.[349]

### Fault injection

Fault injection extends reverse engineering to devices that will not give up their firmware: side-channel measurement and voltage glitching are used to extract an image, which is then analysed statically with a decompiler.[582] Whether such work counts as reverse engineering is contested, on the argument that recovering behaviour from an already open design is a different activity from reconstructing an unknown one; the counter-argument is that a product contains more than its published source and board files, so establishing something subtle that was not in the original design is reconstruction of a kind.[576]

## Historical practice

The mobile phones of the early analogue era were built as an eight-bit microcontroller with an external read-only memory and a serial electrically erasable memory holding the identity number, which was stored in a standard bit-packed format of country, manufacturer, model and serial fields; reading that memory out therefore often showed the number directly in the dump.[294] The efficient way into that code was to disassemble the entire read-only memory, of thirty-two to sixty-four kilobytes, and search for any access to the input-output pin the serial memory was wired to, which located the read and write routines immediately; the calls to those routines then located everything that used them. Since every manufacturer used a different processor, this meant writing a disassembler per architecture.[294] The objective was to reprogram the device without opening it, which meant recovering the factory test protocol available on the external connector; those protocols were generally simple serial protocols, since they existed only for production and dealer use.[294]

One manufacturer defended the stored identity by routing part of the address bus through a custom chip that blocked processor access to that location, so no code running on the device could write it. The defeat was physical rather than logical: lifting one address pin and tying it changed the mapping so that a writable address landed on the protected location, and epoxy over the chips followed as the next countermeasure.[294] The general principle drawn from that work is to attack the layer the designer did not defend—modifying the hardware rather than fighting the software—on the reasoning that engineers secure a system in the domain they built it in.[294]

## Countermeasures and defensive design

Custom part marking removes the starting point a reverse engineer relies on: manufacturers will print any part number or company logo requested at moderate order quantities, sometimes free above a threshold, so a device can be built entirely from standard parts that carry no identifiable markings.[15]

The countermeasures used on high-security silicon go beyond obscurity. A pay television operator will take the vendor's register-transfer source and synthesise the part itself so that proprietary cryptography is never documented back to the chip vendor, and metal layers are changed between production years purely to invalidate work already done on the previous version.[303] The security level of a smart card tracks the compensating controls around it rather than the apparent sensitivity of the application: a SIM card is the cheapest and least protected because the network operator can detect fraud by other means; a banking card is not much stronger because daily withdrawal and transaction limits bound the loss; an electronic passport sits above those; and pay television cards sit an order of magnitude higher again, because there is no other mechanism to fall back on.[303]

Advanced packaging is used as a deliberate obstacle to copying: integrating several dies onto a silicon interposer with programmable interconnect whose configuration is protected by one-time programmable security bits makes the subsystem substantially harder to reverse engineer. Nothing is made impossible; the objective is to make the effort not worth the copier's time.[499]

Protecting a tool that talks to hardware over an observable link is harder than protecting the software itself, since the protocol can be recovered by sniffing the bus. Two mitigations have been used together: a hardware dongle containing a microcontroller that performs the final transformation, so the source of the software can be given away without revealing the method; and burying the few real command bytes inside thirty seconds of functionless commands, some carrying fragments of the target serial number as decoys, with the position of the real ones randomised as a function of that number.[294] The recommended protection for the part of a product that can actually be protected treats software as the asset: the device carries a bootloader whose encryption is programmed at a secure facility with no network access, and the programmed integrated circuits are then consigned to the factory, which both keeps the image out of the factory's hands and caps production, since a factory given a known number of programmed parts cannot run an unauthorised extra shift.[113] Because a vehicle bus itself carries no encryption, the practical defence against payload recovery is encrypting the data the bus carries.[212]

## Economics and applications

Whether to reverse engineer a device before repairing it is an economic calculation rather than a technical one. Repair without a schematic is possible where the layout of an adjacent model year is known and the common faults are familiar. For a device that will be seen thousands of times, paying someone to spend months measuring every node on a working board is worth it; for a device that will be seen once, at a repair price of a few tens of dollars, open-ended troubleshooting is not viable at any level below tens of thousands of dollars of value.[507]

Keeping a design closed does not protect it: a schematic can be reconstructed from a product in about a day by anyone competent to do a teardown, so the decision to publish costs a designer very little of what closed distribution was supposed to preserve.[298] What a competitor gains by copying is rarely the part that took the time; the circuit on a straightforward product can be reproduced almost immediately, whereas the manufacturing, the documentation and the support material are where the real investment sits.[458] The three subsystems of a product are unequally exposed: mechanical design is the easiest to copy, requiring little more than a scanner and material identification; electrical design takes more work but yields to component identification, circuit reconstruction and x-ray of the assembly; software is simultaneously the easiest to protect and the most complete loss once it is gone.[113]

A commercial clone of an instrument was produced without any physical access to the design, by observing the product's behaviour with a logic analyser until the function of its programmable logic could be reimplemented. Every part was reproduced except the intellectual-property protection module, and the vendor's own software was then patched at the binary level to load the clone's bitstream in place of the original, the one component that could not be reimplemented.[237]

Reverse engineering has served as a deliberate market entry route. On Digilent's low-cost development boards, the team reverse engineered the Xilinx programming cable and integrated it onto the boards, because a seventy-nine-dollar board could not be sold alongside a three-hundred-dollar programming cable; equivalent cables of Digilent's own design followed.[302]

Repair-driven reverse engineering supports viable small businesses. An instrument display that fails systematically and is no longer obtainable was addressed by recovering its protocol and building an adapter board around a microcontroller that accepts the meter's original signalling and drives a currently available display, which sells in the hundreds because the failure is that common.[646] Recovering an interface can be worth more than recovering a whole product, because it makes an existing assembly reusable: reverse engineering the flat-flex interface of a display module gave its pin-out and its shift-register-based drive scheme, so a new driver board could be designed to plug into a display that already fits its enclosure and gasket.[598] Salvage of components from wrecked or discontinued electric vehicles depends on reverse engineering, since the interfaces of original-equipment traction and control modules are undocumented and must be recovered before the parts can be reused in another vehicle.[388] In one case, Julia Truchsess reverse engineered the control system of a closed 3D printer to expose the process parameters the manufacturer withheld, and the resulting temperature controller sustained a small manufacturing business for several years.[424]

The activity is not confined to outsiders: engineers inside a manufacturer routinely reverse engineer their own systems because documentation for an interface between subsystems is missing, and companies hire contractors to reverse engineer boards they themselves produced, which is common rather than exceptional.[716] Bringing up a fabricated chip that barely works can itself require reverse engineering apparatus: an FPGA was used to emulate the memory that the processor on the chip executed from, counting executed instructions while sweeping the core voltage, so that a histogram of instructions completed against voltage identified an undervolted operating point at which enough instructions ran to configure the outputs.[616]

Community efforts can reconstruct an entire toolchain around an undocumented part: for a microcontroller costing a few cents, support was added to an existing C compiler and the vendor's programming protocol was reverse engineered into an open-source programmer board, making the part usable without the vendor's tools.[453] The same pattern applies to consumer radios, where the encryption on a manufacturer's firmware update images was broken, the firmware reverse engineered, and a patched firmware is maintained that runs on the unmodified commercial hardware.[442] Pervasive reverse engineering can function as de facto openness: in the Chinese electronics ecosystem, parts nominally closed at the register level are effectively documented, not by policy but because everything has been taken apart.[245]

Firmware analysis has been used to demonstrate deliberate deception: a curve found in engine control software, with defined upper and lower bounds, matched the certification test cycle so exactly, with equal margins on both sides, that its purpose was unambiguous once the two were overlaid.[318] Commercial teardown analysis is a paid service that reverse engineers products on behalf of clients, and its conclusions can contradict the prevailing explanation: one such analysis of a battery fire attributed the cause to insufficient physical margin in the mechanical design of the cell rather than to an internal manufacturing short.[326]

## Education and preservation

A structured teaching exercise runs reverse engineering forward into a clean-room rebuild: students strip a simple product such as a guitar pedal, recover the schematic and every component value, simulate it, and write a documentation package that fully describes the circuit and its interfaces. Packages are then exchanged between teams, each builds from the other's document, and the rebuilt object is compared against the original to expose what the documentation missed; a harder variant withholds what the device does and blacks out the board markings.[119] The teaching case for teardown is that no other engineering discipline expects designs to be produced without examining existing ones, and that pulling products apart shows component selection, layout and the trade-offs actually made, which first-principles instruction does not.[119]

The activity has been simulated as a teaching game with a deliberately faithful instrument set: a voltage probe, a pulse generator, a register read-and-write interface analogous to a debug port, and a serial port, applied to test points on simulated boards whose function must be worked out and then subverted.[332] Introductory hardware hacking instruction reliably takes non-specialists from unfamiliarity to working results within a couple of days, moving through soldering, logic analysis, monitoring signals and cutting traces; the value claimed is not expertise but the removal of the barrier to attempting it at all.[575]

Older data formats and hardware are easier to recover because the constraints of the era—limited code space and slow processors—forced representations that remain legible; decoding a simple bitmap is qualitatively easier than decoding a transform-coded image, which is why documenting old formats before the knowledge is lost is treated as a preservation problem.[463]

## Disclosure and legal response

Disclosure of a defect found in hardware differs from software because the vendor frequently cannot deploy a fix to devices already in the field, which weakens the usual argument for private notification; the countervailing concern is that a vendor given quiet notice has an institutional incentive to do nothing, so the leverage to obtain a response is the credible prospect of publication.[274] A legal demand is a routine rather than exceptional response to disclosure, with conference talks withdrawn after vendors issue notices, and an independent teardown that debunked a product's claims drawing a demand for thousands of dollars in damages together with removal of the analysis.[55]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 15 | Analog Components, First Person Flying and Idea Ownership | https://theamphour.com/the-amp-hour-15-analog-components-first-person-flying-and-idea-ownership/ | |
| 25 | NASA, WOTW & Modular Design - The NASA Nostalgia | https://theamphour.com/the-amp-hour-25-the-nasa-nostagia/ | |
| 55 | Shonky Stiver Stultiloquence | https://theamphour.com/the-amp-hour-55-shonky-stiver-stultiloquence/ | |
| 113 | An Interview with Scott Miller - Sudden SinoAmerican Synthesis | https://theamphour.com/the-amp-hour-113-sudden-sinoamerican-synthesis/ | September 16, 2012 |
| 119 | An Interview with Dr. Kent Lundberg - Luculent Linear Legacy | https://theamphour.com/the-amp-hour-119-luculent-linear-legacy/ | October 28, 2012 |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 294 | Live from Serbia with Mike Harrison | https://theamphour.com/294-live-from-serbia-with-mike-harrison/ | April 13, 2016 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11, 2016 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 303 | An Interview with Dmitry Nedospasov | https://theamphour.com/303-an-interview-with-dmitry-nedospasov/ | June 14, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 332 | An Interview with Zach Barth of Zachtronics | https://theamphour.com/332-an-interview-with-zach-barth-of-zachtronics/ | January 18, 2017 |
| 336 | An Interview with Bunnie Huang (2nd) | https://theamphour.com/the-amp-hour-336-an-interview-with-bunnie-huang-2nd/ | |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 349 | An(other) Interview with Jon Oxer | https://theamphour.com/349-another-interview-with-jon-oxer/ | June 25, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 388 | An Interview with Earl Sharpe and Collin Kidder | https://theamphour.com/388-an-interview-with-earl-sharpe-and-collin-kidder/ | April 15, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 453 | Vertically Integrated Design Engineering | https://theamphour.com/453-vertically-integrated-design-engineering/ | August 4, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 507 | Right To Repair with Louis Rossmann | https://theamphour.com/the-amp-hour-507-right-to-repair-with-louis-rossmann/ | |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 575 | New Life Skills with Joe Grand | https://theamphour.com/575-new-life-skills-with-joe-grand/ | January 30, 2022 |
| 576 | A literal trainwreck | https://theamphour.com/576-a-literal-trainwreck/ | February 6, 2022 |
| 582 | The Same Wavelength | https://theamphour.com/582-the-same-wavelength/ | March 20, 2022 |
| 598 | Best way to find a leak | https://theamphour.com/598-best-way-to-find-a-leak/ | August 7, 2022 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 634 | The CAN bus can! with Dr Ken Tindell | https://theamphour.com/634-the-can-bus-can-with-dr-ken-tindell/ | May 30, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
| 716 | Electronics Manufacturing History with David Ray | https://theamphour.com/716-electronics-manufacturing-history-with-david-ray/ | February 25, 2026 |
| 722 | AI Tooling with Matt Liberty and Luke Beno | https://theamphour.com/722-ai-tooling-with-matt-liberty-and-luke-beno/ | April 22, 2026 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
