---
title: Risc V
concept: risc-v
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

RISC-V is an open instruction set architecture (ISA) rather than a processor: a core designed from scratch against the ISA remains entirely the designer's own silicon, and what conformance buys is that an existing compiler can already target it.[597] The base integer instruction set contains roughly 47 instructions, with standard and custom extensions layered on top, a small mandatory core that makes a compliant single-person implementation tractable.[644] Its significance lies in the shared software ecosystem: because GCC, Clang and LLVM target the ISA, cores of wildly different sizes can all be built against one actively maintained, stable compiler rather than each new processor forcing its toolchain to be built from scratch.[467][374]

## Instruction set versus implementation

RISC-V defines only the instruction set; it does not define a processor, and nothing outside the core is standardised, which is why groups of vendors have had to form separate consortia to agree reference architectures for interoperable parts.[642] An open ISA carries no guarantee that any particular implementation is open: a core described as RISC-V may be entirely proprietary, and the extensions it carries are equally unconstrained, so the openness of a CPU must be verified as a separate claim.[723] The licence does not flow down from the instruction set to the implementation — a company can take the ISA, design a core, and sell that core as proprietary soft IP or as hard silicon without publishing anything.[528]

The compactness of the mandatory base makes minimal implementations practical. A working RISC-V core has been published in on the order of a hundred lines of Verilog, fitting in about 1380 logic units on a small Lattice iCE40 part and running a real blinky demonstration.[644] Custom instruction-set extensions are open to anyone, and on a part that also carries embedded FPGA fabric those custom instructions can be implemented in the fabric itself, turning an extension into a hardware accelerator for operations such as convolution.[525]

## The shared-ecosystem rationale

A compiler is not finished when it first targets a processor; it needs a large user base inspecting generated code closely enough to write and contribute test cases, which a one-off private ISA never accumulates.[374] The economic argument for a shared ISA is that the ecosystem work — compiler, libraries, debugging support — is done once and reused by every subsequent processor, instead of being redone each time someone builds a new core.[374]

Before a common open ISA existed, a free core was typically either legally encumbered — usable until the product grew large enough to attract the IP holder's attention — or a one-person design whose GCC fork was never mainlined and had not been updated in years, leaving something antique like a Z80 or 8051 as the safe option.[467] What the shared ISA changed in practice is that cores of wildly different sizes can be dropped into a design and all of them share one actively maintained, stable compiler.[467] Because GCC absorbed the instruction set and its compilation down to those instructions is tested, retargeting a build to RISC-V is close to a compiler flag change rather than a port — the same property that applies to any other ISA the compiler supports.[528] For the engineer designing a custom processor, the common ISA removes the obligation to also build the language, the opcodes and the operating-system support; the translation layer already exists, which is what makes the exercise finishable for an individual.[721]

## Performance and implementation comparisons

Comparing one instruction set against another on performance is a category error; only implementations can be compared, and nothing in a clean modern ISA prevents building a high-performance processor from it.[374] x86 is fast because of the processors built around it, not because of its instruction set — a large fraction of the die area goes into instruction decode, which is exactly the overhead a reduced instruction set avoids, and the reason embedded parts went that way.[374]

For FPGA-hosted soft cores, the resource figures set the practical floor. A 32-bit RISC soft core fits in roughly half of a 5,000-logic-element FPGA, leaving the other half for custom peripherals.[423] A well-optimised open core such as VexRiscv places a multi-core Linux-capable SoC into an FPGA of about 35,000 LUTs or fewer, rather than requiring a large high-end device.[547] The same soft RISC-V core moved from an older 40 nm low-power FPGA family to a newer process went from about 100 MHz to about 400 MHz, a jump large enough that customers assumed a measurement error.[535] Once a soft core clocks at 400 to 500 MHz on the fabric, adding a hardwired processor subsystem to the die stops paying for itself — the logic area is better spent on more fabric, and the soft core can instead be offered as a modifiable SoC template.[535]

A soft core also permits the hardware to be rearranged to suit the software: gathering eight bits that live in eight different registers into one register turns roughly sixteen instructions of reads and XORs into a single read, an eight-fold speedup that makes a 20 MHz soft processor behave far better than its clock suggests.[703] More broadly, moving a function from software into dedicated hardware is often what removes the need for a fast processor at all, which reframes a slow soft core as a design starting point rather than a limitation.[703] Building a custom processor when a commodity one would do misreads what the open ISA enables, however; it opens a different application space rather than replacing the case for buying an off-the-shelf part.[721]

## Hardware interfaces and debug

On the 32-bit bus used by small RISC-V cores, sub-word writes are signalled rather than masked: the core always drives a full 32-bit value and uses the write strobes to indicate which bytes are meant, so a peripheral that ignores the strobes will corrupt neighbouring bytes.[467]

Debug interfaces vary widely across implementations. The CH32V debug interface avoids a complex protocol entirely: it exposes a small scratchpad, code is written into it, and a command halts the running program and executes that code on the core — so flashing and memory access are short RISC-V programs rather than protocol commands.[667] The RP2350 handles dual-architecture boot in the binary header: the mask ROM reads a flag saying whether the image is an ARM or a RISC-V binary and reboots the chip into the matching set of cores, so the architecture is chosen by the program rather than by a fuse or a part number.[687]

Debug readiness has historically been a gating issue for the ISA in product design. On the Raspberry Pi RP2040 programme, RISC-V was rejected because the debug specification was still in draft — the debug spec is not just JTAG but new control and status registers and an entire privileged mode, so core semantics were still subject to change while the chip had to be committed.[529] Debug capability is the deciding criterion in embedded architecture selection because there is no other way to see inside the running system, which is enough on its own to send a design to a mature architecture even when the engineer prefers the alternative; the engineer who made that call held the architecture itself in high regard and had RISC-V implementations of his own, and the decision turned on that one unfinished specification.[529]

## Silicon and SoC design practice

RISC-V cores have become structural components in open and modular silicon. On shared multi-project shuttle chips, a verified management core placed alongside the user area turns bring-up into software: it boots reliably, exposes virtual GPIO into the user design, and can enable, disable and probe blocks that may themselves be broken.[501] Pin count, not silicon area, is the binding constraint when several processors share a die; the answer is multiplexers on the IO so a user can select which design reaches the outside world.[501] On early open-source SoCs built before a RAM compiler was available, memory had to be built out of logic cells; a later revision keeps identical content but swaps in compiled RAM, the difference being visible on the die as a block rather than a spread of logic.[503] The first microcontroller built from a RISC-V core with a fully open-source tool set was assembled by splitting the work — an outside CPU author, a party with foundry access and analog IP, and a system integrator — and its value was demonstrating feasibility on real silicon rather than competitive performance.[503]

In modular chiplet systems, guaranteeing that one known processor is always present gives the software a fixed base to boot from, so the variable parts can then be discovered and configured automatically at runtime.[650] Core design itself is increasingly generated rather than fixed: describing hardware in a full programming language rather than plain Verilog lets a core be emitted from parameters — memory management unit, floating point, vector support — so one project produces a different CPU per configuration instead of shipping one design.[469] Ibex is the RISC-V core developed by lowRISC and also used in OpenTitan; CHERI is a separate set of extensions layered on it that add memory compartmentalisation, so the two names describe different layers of the same board.[693]

The absence of a licensing step changes schedules for small companies. For a fabless analog startup, putting a RISC-V style processor next to the analog section removes an ARM licensing negotiation from the schedule, one of several factors that make small chip companies viable again — the harder questions remaining whether the niche is real and how the work is funded.[579] During the worst of the component shortage, designing a custom SoC and having it fabricated would have been faster than waiting out lead times on a commodity microcontroller, an inversion that says more about supply conditions than about design effort.[616] Commodity parts have historically hidden idiosyncratic embedded controllers — SD cards have been found running an 8051 with 32-bit extensions — which are poor things to expose to large numbers of end users, and a common ISA with rapidly improving GCC, Clang and LLVM support is a better target for anything meant to be programmed.[423]

## Toolchains and architecture selection

Toolchain maturity dominates architecture selection: the chains for established parts are well proven and long-lived, and engineers who have to ship a product are rationally conservative about working with unknown tools.[489] Mainstream microcontrollers and their heavily used compilers still surface bugs, so an architecture with a small user base should be assumed to hide proportionally more undiscovered problems — a real risk to weigh when starting a product on one.[432] For a commercial SoC the incumbent architecture wins on availability, verification, documentation and the existence of genuinely high-performance cores; the maturity gap runs x86 first, ARM second and RISC-V some distance behind, and software tooling maturity follows the same order.[648]

Hand-written low-level work on the architecture carries its own learning cost: fluency in ARM, x86 and AVR assembly does not transfer cleanly, and an engineer experienced in all three found working in RISC-V assembly a genuine struggle.[637] The low-cost WCH CH32V line — where CH marks the Chinese semiconductor maker WCH and the V marks RISC-V — ships with MounRiver, the vendor's proprietary Eclipse-based development environment.[637] A published teardown analysis of the ten-cent CH32V003 microcontroller concluded it is not the best cheap part available, noting that a comparable 48 MHz Cortex-M0 from a memory manufacturer meets the same brief.[619]

Cores themselves are the abundant part and the least valuable: a CPU is not usable without GPIO drivers, programmable IO, PWM, converters, timers and interrupts, the forty-peripheral surround that a mature vendor microcontroller supplies and a bare core does not.[672] This shapes how established vendors use the architecture: a large microcontroller vendor deploys RISC-V where it is invisible to the customer — inside an FPGA or a data-centre part — rather than as the advertised core, on ecosystem grounds.[632] Competitive pressure from the open ISA has nonetheless improved terms on the incumbent: the licensing processes for getting hold of ARM IP became easier, which benefits designers who never intend to switch architectures.[648] In a further convergence, MIPS — the architecture famously chosen over ARM for the PIC32 line — announced that its next-generation architecture would be based on RISC-V rather than developed further on its own instruction set.[534]

## Use as an educational vehicle

The RP2350 added RISC-V cores alongside its ARM cores in a mainstream microcontroller; the added cores were small enough to fit the existing socket without growing the die, and were justified mainly as an education vehicle — both for users and for the design team learning to implement a new architecture in a conventional system.[687]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 423 | Open FPGA Toolchains at 35c3 | https://theamphour.com/423-open-fpga-toolchains-at-35c3/ | January 1, 2019 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 489 | An Interview with Jack Ganssle (2nd) | https://theamphour.com/489-an-interview-with-jack-ganssle-2nd/ | April 19, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ | January 31, 2021 |
| 529 | Embedded Hardware with the Raspberry Pi Team | https://theamphour.com/529-embedded-hardware-with-the-raspberry-pi-team/ | February 7, 2021 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 535 | Efinix FPGAs with Sammy Cheung | https://theamphour.com/535-efinix-fpgas-with-sammy-cheung/ | March 21, 2021 |
| 547 | Open Source Mindset with Michael Gielda | https://theamphour.com/547-open-source-mindset-with-michael-gielda/ | June 28, 2021 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 597 | Wow, Dave REALLY likes Top Gun | https://theamphour.com/597-wow-dave-really-likes-top-gun/ | July 24, 2022 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 632 | Steve Sanghi - Microchip CEO for 31 Years! | https://theamphour.com/632-steve-sanghi-microchip-ceo-for-31-years/ | May 15, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 642 | Sad Violins for Superconductors | https://theamphour.com/642-sad-violins-for-superconductors/ | August 13, 2023 |
| 644 | Garbage Ninjas | https://theamphour.com/644-garbage-ninjas/ | August 28, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 650 | Accessible ASICs with Andreas Olofsson | https://theamphour.com/650-accessible-asics-with-andreas-olofsson/ | November 12, 2023 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 693 | Small Scale Electronics Manufacturing with Colin O'Flynn | https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/ | May 13, 2025 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
| 721 | Chip Design for Fun (and Waffles) with Julia Desmazes | https://theamphour.com/721-chip-design-for-fun-and-waffles-with-julia-desmazes/ | April 8, 2026 |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ | May 7, 2026 |
