---
title: Hardware Description Language
concept: hardware-description-language
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A **hardware description language** (HDL) is a notation in which a designer states in abstract terms what a circuit should do, leaving the tools to derive the physical implementation, lay out the chip and perform the detailed work that would otherwise be done by hand.[34] Its defining capability is that it nonetheless reaches down to the structural level, so the designer creates registers and other structures directly in logic, which is the reason to use programmable logic at all rather than a processor.[150] Portability across vendors is the stated design intent of such languages, and is the practical reason a designer can select a programmable logic vendor on price rather than on toolchain commitment.[303] Although the languages were intended to be higher-level than structural entry they remain difficult in practice, which is why engineers keep writing compilers that translate an easier language down into HDL.[301]

## Concurrency

The asymmetry between software and hardware description is exact and worth stating as a rule: software written for a processor is sequential by default and the programmer works to make it parallel, while a hardware description is parallel by default and the designer works to make it synchronous and sequential.[450] Moving between the two is difficult in both directions; an engineer fluent in describing logic where everything happens at once and is instantiated in hardware struggles to return to step-by-step processing on an eight-bit microcontroller, just as microcontroller programmers struggle with concurrency.[127]

The characteristic beginner error is reading top-to-bottom position on the screen as order of execution, a trap made worse because ordinary editors give no visual cue distinguishing statements that execute concurrently from those that are ordered; syntax highlighting that showed which statements run at the same time would address it directly.[450]

Concurrency is only half the barrier. The second obstacle is independent of the language entirely: even starting from someone else's working source, the design must still be run through synthesis, place and route and the rest of the flow, and that toolchain is a second body of knowledge to acquire.[567]

## Synthesis

Logic synthesis is the step that bridges a description of a logic function to an architecture that can implement it: a program consumes a description, usually written in a hardware description language, and generates a logic circuit made of gates, lookup tables or other primitives. An adder written once in the source becomes a dedicated adder primitive under coarse-grain synthesis, a chain of carry cells for an FPGA, and NAND and NOR gates for an ASIC.[374] Synthesis is the same class of operation as compilation: both take a higher-level description in one format and perform a sequence of transformations to produce an equivalent representation in a format that can actually be worked with, so a compiler or assembler can reasonably be called a program synthesiser.[374]

Place and route for such a design is compute-intensive enough that vendors added the ability to dispatch the job to a compute cluster for faster turnaround, because the tool must evaluate many alternative placements and timing paths.[626]

Sign-off in an HDL flow rests on the tool reports rather than on physical inspection: if the timing report passes and the other checks pass, the compiled design can be treated as working, with failures outside that envelope rare enough that an experienced engineer may never encounter one. Board-level design has no comparable closed check.[626]

## Synchronous design discipline

Before hardware description languages, gate-count limits pushed designers toward asynchronous techniques, feeding combinational logic into set-reset latches, JK latches or latches built from combinational logic, which produced a large class of timing hazards and made designs very hard to get right.[609] A principal benefit of hardware-description-based design is that it enforces a synchronous template of combinational logic feeding D flip-flops in cascaded stages, which removes those ad hoc hazards and makes the design tractable to automated timing analysis tools.[609]

## Relation to schematic entry

Vendor documentation, rather than the languages themselves, decided how a generation of engineers entered designs. One vendor's manuals were written entirely around a hardware description language flow, with schematic drawing relegated to an appendix noting that it was possible but not how the work was done.[374] The competing vendor's documentation was inverted, presenting the schematic tools as the main flow and confining the language to an appendix that described it as very complicated; comparing the two vendors' documentation was itself sufficient grounds for choosing a vendor, because the documentation determined which design method would be supported in practice.[374]

Regulatory classification also drove design-entry choice in military electronics. Because a design written in a hardware description language was deemed to be source code, it fell under rules requiring every line to be verified, at a nominal cost on the order of a hundred dollars per line, so teams used schematic capture instead to keep the design out of the source-code category.[181] The workaround was to enter the design as a schematic, present the schematic as evidence that the product was not programmed, and then regenerate the hardware description language from that schematic for implementation; the resulting schematics are unreadable at review because they consist of very large numbers of individual gates.[181]

Schematic capture survives alongside the language flow for a specific job: consolidating a handful of discrete shift registers and flip-flops of glue logic into one small FPGA, where the design is simple enough that learning and writing a hardware description language is not worth the effort.[567] It also remains useful as a teaching route, precisely because it is graphical: drawing the design as a network of joined components makes it evident that everything runs in parallel and that separate instantiated devices are being wired together, whereas a text description invites a programmer to read it as an executable program for a CPU. A schematic tool with an export to a hardware description language over a small standard cell library lets a beginner take that route and still reach the normal flow.[672]

## Verification

Hardware description language work supports a purely software-side role: some practitioners in the VHDL domain never touch a physical device and spend their time writing test benches and algorithms, which makes verification a career path separate from board and device bring-up.[83]

Formal verification of a hardware design is assembled from a synthesis front end and general-purpose solvers: the front end converts the design into a form the constraint solvers can consume, and the solvers then discharge or refute the stated properties.[374] The difficult part of a formal flow is not the solving but the reporting. A raw solver result states that a numbered property failed with a numbered signal high in a given cycle, which means nothing to the designer; the tool must map that counter-example back onto the source design as an artefact the engineer can read, such as a waveform trace.[374] The share of HDL code emitted by other tools rather than written by hand is increasing, which compounds the problem, since a message referring to a signal or property by number is harder still to trace when no human wrote the signal in the first place.[374]

Languages of this kind are also used internally for behavioural modelling rather than synthesis. A SPICE vendor maintained a private, primitive description language in which controller models were written; the simulator parses and compiles that language into executable data structures rather than into object code, and then executes them in the manner of a standard hardware description language such as Verilog or VHDL.[196]

## Higher-level layers and generated code

Hand-coding at register level does not scale to mathematics-heavy work, so for DSP-type functions inside an FPGA, libraries hosted in a general-purpose language act as a compiler from that language to hardware, in the same way that C-to-hardware compilers do.[150] An algorithm prototyped in a numerical environment such as MATLAB is likewise not the deliverable for a cost-sensitive part: a separate engineer may spend of the order of twelve months converting that routine into a hardware description language so that it implements efficiently in an ASIC.[39]

Not every layer hosted in a general-purpose language is a translator. Some are templating layers, emitting a parameterised instance of a block such as an SPI controller without the user having to work through the internals, which makes them accessible at a high level while leaving the underlying hardware description unchanged in kind.[375] Graphical block-integration tools inside a vendor IDE achieve a similar assembly of pre-built blocks by dragging and connecting them, but with a lock-in cost the scripted equivalents do not carry: the user is given no source code for what the tool produced.[375]

A family of newer languages is built as domain-specific languages hosted inside a strongly typed general-purpose language. SpinalHDL began as a fork of Chisel, and both are built on Scala running on the Java virtual machine; hosting in a strongly typed language means a connection between two buses of mismatched width is rejected as an error rather than silently accepted.[469] MyHDL, LiteX and MiGen form a comparable group that starts in Python and emits a conventional hardware description language, so the new layer sits above the existing flow rather than replacing any part of it.[469] Amaranth is a newer entrant that is a hardware description language rather than a high-level synthesis tool, meaning the designer still describes hardware directly rather than having it inferred from an algorithm; it is under active development driven by community requests for comment.[672]

A generated-code flow can become an end-to-end black box for the engineer operating it: an algorithm entered in MATLAB generated code the engineer never inspected, which was pushed into an FPGA whose behaviour was equally unexamined, leaving a single LED as the only observable and a six-hour turnaround on each iteration.[374]

## Sources of reusable code

Access to processor IP at the hardware description language level was historically gated by contract: obtaining the source for a small ARM core required long negotiations, and the code was released only at the end of them. That changed when the vendor published the M0 and M3 sources for download under a click-through licence that permits experimentation and integration but forbids use in an actual ASIC.[374]

Public repositories of donated cores are of uneven provenance and are best treated as reference rather than as drop-in modules. A usable pattern is to take only the fragment that answers a specific structural question, such as how to implement an AES S-box purely in logic, and to write the remainder oneself.[318]

## Use in instrumentation

Building instrumentation in a hardware description language is justified when commercial equipment refuses to emit invalid stimulus. Security analysis of a proprietary or uncommon protocol requires sending deliberately malformed packets, for example with a byte count that does not match the packet contents, and commercial protocol analysers rarely permit that, whereas a custom FPGA peripheral will.[318]

Resource efficiency is the wrong objective while learning. A naive protocol analyser instantiates a separate UART, SPI and I2C module, each with its own internal counter for baud-rate division, on every pin being observed, which wastes a great deal of the FPGA; that waste is acceptable because area should not constrain someone still learning to build in the language.[318]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 34 | AD620, DesignSpark, Instrumentation Amplifier - The Rant Rhetorical | https://theamphour.com/the-amp-hour-34-the-rant-rhetorical/ | March 14, 2011 |
| 39 | Dan Pink, Dual Core, level translators - Mumble Mumbo Jumbo | https://theamphour.com/the-amp-hour-39-mumble-mumbo-jumbo/ |  |
| 83 | Aggravating Agersia Agiotage | https://theamphour.com/the-amp-hour-83-aggravating-agersia-agiotage/ | February 19, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 150 | Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness | https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/ | June 17, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ |  |
| 196 | An Interview with Mike Engelhardt (Re-broadcast) | https://theamphour.com/196-an-interview-with-mike-engelhardt-re-broadcast/ | April 28, 2014 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 303 | An Interview with Dmitry Nedospasov | https://theamphour.com/303-an-interview-with-dmitry-nedospasov/ | June 14, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
