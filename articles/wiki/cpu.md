---
title: CPU
concept: cpu
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A central processing unit is general-purpose hardware defined by the obligation to execute anyone's code reasonably well, which is a different design problem from executing one known workload as fast as possible.[721] Its basic organisation has not changed since the earliest devices: data is moved from one register to the next along a pipeline of transistor stages, and what modern parts add is depth and breadth, running several pipelines in parallel rather than a single one.[238] A simple processor is not a separate category of design from the building blocks beneath it, since once a full adder and a state machine have been built, the datapath and the control that sequences it are most of what a rudimentary processor is.[672] Over roughly the last decade the general-purpose processor has ceased to be the default engine for demanding workloads, with the pattern shifting toward application-specific hardware, GPUs and ASICs that cost more to build but are faster and more energy-efficient at the task they were designed for.[498]

## Architecture and design constraints

The cache hierarchy exists to minimise the cost of moving data, and it works because general-purpose code has strong spatial and temporal locality: data used in a computation is very likely to be used again shortly within the same program context, so keeping it close pays for itself.[721] Load-to-use latency is one of the strongest single predictors of processor performance, since the number of cycles taken to return a value from the L1 cache to the core is highly correlated with delivered performance, and the difference between a three-cycle and a four-cycle L1 is substantial.[721]

Embedded cores are designed against two hard constraints beyond performance: a power envelope set by the battery life of the end device, and core area, because die area translates directly into manufacturing cost and therefore into the price of the chip and the product.[721] An architecture licence adds a third, functioning as a conformance contract rather than a starting point, since a core declared to implement a given revision of the ARM architecture must implement the features that revision specifies and perform acceptably on them, which bounds how far an implementer can specialise.[721]

The accumulator register found in processor architectures descends from mechanical calculators, where adding a separate mechanical register holding a running result, instead of operating directly on the input mechanism, is what first made multiplication and division possible.[725]

## Specialisation and offload

The trade for abandoning general-purpose design is stark: a specialised chip built for one known use case, with no obligation to legacy or even to general code, can be made very fast, but it is expensive to build, full of custom parts, hard for anyone else to program, and useless outside its target task.[721] Machine-learning accelerators additionally break the assumption the cache hierarchy is built on, because weights are reused and can be held in place while incoming activation data is consumed once and discarded, so there is little reuse to exploit and the memory design has to be reasoned about differently.[721] The hardware that happens to be available in turn shapes which algorithms are pursued, since the network architectures treated as state of the art in machine learning were selected in part because they run well on existing hardware rather than because they are the best available approach.[721]

Not every workload needs full arithmetic precision. Image compression, video playback and streaming tolerate small computational errors invisibly, so full-width floating-point precision spends processor energy on accuracy the output cannot show, whereas scientific simulation is precision-critical.[344]

Offload is not automatically a win. For a particular video codec, source format and driver stack, an overclocked desktop processor running at around three and a half gigahertz beat the discrete graphics card, and the OpenCL and CUDA paths behave as different systems rather than interchangeable ones.[230] Where hardware acceleration does apply, however, falling back to the processor is not a marginal penalty: encoding at 50 to 60 frames per second on the processor alone ran roughly six times slower than the accelerated path.[230] In the other direction, the signal-processing throughput of a general-purpose desktop processor is high enough that a software-defined radio can stream samples to a host PC and omit an FPGA entirely, trading board complexity and FPGA development time for dependence on the host's compute.[214]

### Graphics as a historical case

Early machines without a dedicated display processor generated video from the processor itself, taking an interrupt on every scan line to pull pixels out of memory and push them to the display, which could consume roughly half of the machine's total throughput before any application work was done.[361] Console-era graphics hardware existed for the same reason: a Super Nintendo ran a 16-bit processor at only a few megahertz, and a naive frame buffer where every byte of memory maps to a pixel demands both a large amount of RAM and enough processor throughput to write every pixel every frame.[467] A two-dimensional accelerator removes that blitting work by consuming a command list already in memory, with the processor writing a list of draw operations carrying position and transparency while the hardware walks the list, fetches the source data and writes the frame buffer, operating on eight pixels per step instead of one.[469]

## System integration

A processor paired with an FPGA typically talks to it over two separate paths: wide streaming links carrying the payload, in one case two 24-bit RGB streams, and a narrow general-purpose parallel memory bus, there a 16-bit GPMC, that exists only so the processor can read and write control registers inside the FPGA.[325] Repurposing a high-volume tablet applications processor for an embedded task inherits both the compute and the analogue plumbing, since a part built for tablets already carries audio input and output alongside an ARM Cortex-A8 core, and the tablet volumes keep it low-power and inexpensive.[258]

A standardised compute-module footprint decouples the processor from the carrier board, so an industrial design can drop in a faster module years later against the same pinout and the same operating system layer, retesting rather than redesigning; the cost of the modularity is paying for interfaces the product does not use.[681]

Firmware dependency creates a bootstrapping problem at the socket. A processor newer than the motherboard firmware that has to start it will not boot, and the board's diagnostic indicators can point at the wrong subsystem, with a DRAM error LED lit while the actual fault was an unsupported processor.[546] Because a board cannot flash the firmware that would support a new processor without first booting on some processor, AMD runs a loan programme that ships an older compatible part to the customer, who fits it, updates the firmware, and returns the loaner.[546]

## Software and toolchains

Time-critical signal-processing routines are sometimes hand-written in assembly rather than a high-level language, because the compiler's code generation is not predictable enough at the cycle level and the author needs direct control over what the processor executes.[169] Optimising numerical code close to the processor can be framed as an energy problem rather than a timing one: given the input data and the required output bit pattern, the goal is the instruction sequence that moves the least charge through the processor to reach that pattern.[196]

A shared instruction set is what makes small custom silicon affordable to build, since with a common ISA the designer inherits the compiler, the opcodes and the operating system layer instead of writing a language and toolchain alongside the hardware, which frees effort for unusual accelerators built beside the core.[721] The hidden cost of building around a one-off instruction set is correspondingly toolchain maintenance rather than the core itself: a well-written core from a single author typically comes with a compiler fork that was never merged upstream and has not been updated in years, which is why designers otherwise fell back on antique architectures such as the Z80 or 8051 whose toolchains are already maintained.[467]

## Licensing and open cores

RISC stands for reduced instruction set computer, a term dating from the 1980s, and an open processor project of this kind is distributed not as silicon but as a complete design in a hardware description language such as VHDL or Verilog, which anyone can synthesise.[78] The practical value of RISC-V is legal rather than technical: cores were downloadable from repositories such as opencores.org long before it existed, but using one in a product that grew large exposed the user to claims from the architecture's owner, whereas an open instruction set carries no such encumbrance.[467] Writing hardware description in a general-purpose programming language further turns a core into a generator, and a parameterised RISC-V implementation such as VexRiscv exposes options for a memory management unit, floating point or vector support, emitting a different processor depending on which are selected.[469]

Historically, Intel's architectures were cloned far more widely than any other vendor's because Intel treated them as standard products it did not defend once they reached end of life: the 8080 begat the Z80, the PC line was reimplemented by AMD, Cyrix and IBM, and the 8051 and 8048 were second-sourced by hundreds of companies, while microcontroller vendors took the opposite line, so there is no knockoff 6809, PIC or AVR.[169] A vendor whose business rests on a single proprietary core will not license it for a compatible clone at any price, and the licensing conversation ends with questions about who the customer is, because a second source would compete directly with the only product the vendor sells.[169]

## Commercial context

Processor selection for a consumer product is normally a commercial decision rather than a technical one: the chumby used a Marvell applications processor originally built for smart photo frames and media tablets because the cost-performance and the price were right and the feature set was adequate.[84] Marvell does not sell its processors as an open-market catalogue part, working vertical by vertical and pursuing named design wins directly rather than serving general distribution.[84] The common belief that FPGAs are priced far above other silicon does not hold at the level of vendor economics either, since FPGA and processor makers price on substantially the same model and the gross margins of Xilinx and Intel sit within a few percent of each other.[103]

## Security exposure

An exposed debug header is a control interface, not just a diagnostic one. A ten-pin ARM JTAG connector reachable through an expansion-module opening on an industrial controller allowed a small microcontroller board, powered from the connector itself, to halt the processor and write a GPIO to change an output within seconds of being plugged in.[346] Buying one sample of a target controller establishes the processor and base firmware for every unit of that model, so someone who gains JTAG control and reverse-engineers which GPIOs drive which outputs can manipulate the machine without ever extracting or analysing the firmware.[346]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 78 | Alteritous Andy's Absquatulation | https://theamphour.com/the-amp-hour-alteritous-andys-absquatulation/ | January 16, 2012 |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 196 | An Interview with Mike Engelhardt (Re-broadcast) | https://theamphour.com/196-an-interview-with-mike-engelhardt-re-broadcast/ | April 28, 2014 |
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 230 | Prepping For Hoverboards - Gallionic GitHub Gabble | https://theamphour.com/230-prepping-for-hoverboards-gallionic-github-gabble/ | December 30, 2014 |
| 238 | Old Books, New Tricks - Iterant Inscription Irrationality | https://theamphour.com/238-old-books-new-tricks-iterant-inscription-irrationality/ | February 25, 2015 |
| 258 | An Interview with Bertrand Irrisou and Gerald Friedland of Audeme | https://theamphour.com/258-an-interview-with-bertrand-and-gerald-of-audeme/ | July 14, 2015 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 344 | Back Into The Swing Of Things | https://theamphour.com/344-back-into-the-swing-of-things/ |  |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 498 | Quantum Computing with Andrea Morello | https://theamphour.com/498-quantum-computing-with-andrea-morello/ | June 28, 2020 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 721 | Chip Design for Fun (and Waffles) with Julia Desmazes | https://theamphour.com/721-chip-design-for-fun-and-waffles-with-julia-desmazes/ | April 8, 2026 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
