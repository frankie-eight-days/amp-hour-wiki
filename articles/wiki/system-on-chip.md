---
title: System on Chip
concept: system-on-chip
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A system on chip (SoC) is an integrated circuit that absorbs most of an electronic system onto a single piece of silicon, combining a processor core with memory, peripherals and often analogue or radio blocks that would otherwise occupy separate packages on a board.[152][118] The approach displaced designs built from large amounts of non-specialised discrete circuitry: first-generation DVD players, built before SoC parts existed for the application, filled a single board of roughly 10 by 12 inches and retailed for over a thousand early-1990s dollars.[704] Integration lowers component count and board area but trades away the designer's ability to swap an individual function out, and chip design remains far less accessible than board design.[469] Designing an SoC of any reasonable size costs on the order of 50 to 100 million dollars even when a large proportion of the design is assembled from pre-built IP blocks.[469]

## What is integrated

The defining move is to place functions that were previously separate packages onto one die. A Bluetooth system-on-chip of the early 2010s carried an ARM core, SRAM, baseband processing, encoding and the radio circuitry together, so a sensor node needed little beyond the chip itself; such a part drew about 3.8 milliamps in both receive and transmit.[152] Application processors follow the same pattern at larger scale, integrating memory, graphics processing and DSP blocks into a single-chip solution.[118]

Putting a co-processor and its accelerators on one die is favourable for power, because unused blocks can be shut off, and it also allows an existing platform to be extended by dropping a co-processor alongside the main application processor rather than redesigning around a new one.[97] The consequence at board level is that a design becomes a handful of large processor, FPGA or system-on-chip packages joined by modular blocks rather than the hundreds of small logic packages that once made autorouting useful.[134]

### Multi-die packages

Not everything that ships as one chip is one die. Multi-die packaging lets a vendor sell what looks like a single part: dies that cannot be built on one piece of silicon, such as a large flash array alongside a processor, are stacked or flipped together inside one package, removing the external memory chip from the bill of materials.[12] In application processors the memory die is commonly packaged on top of the processor die rather than placed separately on the board.[118] The distinction matters when a product line evolves — a system-in-package may keep the microcontroller and the radio transceiver as separate dies in one package, while the succeeding part licenses the transceiver design and combines everything onto a single die, giving more integration and a smaller footprint.[557]

Packaging the same die with integrated DDR2 memory produces a variant part that removes the external memory and its high-speed routing from the board, which is what makes a miniaturised design both low cost and straightforward to lay out.[638] Pushing further runs into process limits: stacking bare memory and storage dice on top of the system-on-chip requires interposer-level design rules of roughly 10 to 20 microns line and space, which conventional PCB processes cannot achieve.[681] An eMCP package combining 4 GB of LPDDR4X with 64 GB of eMMC is dominated by the memory dice themselves, with the moulding accounting for perhaps 10 to 20 percent of the package volume, so the only remaining path to a smaller module is stacking the memory onto the SoC.[681] Advanced integration steps of this kind — embedded components, stacked bare dice — are technically available but only rational at volume, since the non-recurring engineering and time investment have to be recovered across a common enough use case.[681]

Chiplet integration is offered as an alternative to a monolithic system-on-chip built on one process node, with time to market as the claimed advantage: production samples in months rather than the quarters or years a monolithic part requires.[499]

## Processor plus programmable logic

A distinct branch of the category pairs hard processor cores with FPGA fabric on one die. The Xilinx Zynq combined a dual-core 1 GHz ARM Cortex-A9 processor with FPGA fabric, and higher models added hard-logic DDR2 and DDR3 memory controllers and high-speed serial transceivers.[156] The pairing suits systems where a very high-bandwidth data path must be managed by logic that does not itself need high bandwidth, such as a telecoms base station routing packet transactions; the cost of the processor is absorbed into the fabric rather than paid separately.[452] Integration on FPGA-based parts extended to RF as well: Xilinx released an RF SoC with multiple RF DACs and ADCs integrated onto the die, allowing a software-defined radio or radar system, including its DSP, to be built on one chip.[452]

When cores and fabric sit on the same die, communication bandwidth between them is not a design constraint, because the link is internal rather than a serialised off-chip interface.[466] Latency is a separate matter. A signal path that runs from a custom peripheral in the fabric to a bare-metal core and up to a Linux core and back still consumes significant time, so buffer sizes and how often the operating system services the interface have to be sized for the case where the call is late or never arrives.[466]

Fabric can also host a soft SoC. In such a design the number of CPU cores can be a single Verilog parameter, but beyond a certain count added cores stop helping, because the shared memory bus becomes the constraint and the CPUs wait on each other.[467] A multi-core Linux-capable RISC-V system-on-chip can be fitted into an FPGA of roughly 35,000 LUTs or fewer, rather than requiring a top-end device.[547]

## Licensed IP and configurability

Many blocks inside a system-on-chip are designed by companies other than the chip maker and licensed in, so the display controller or similar subsystem in one vendor's SoC may be the same IP family found in another's.[638] Teams take the IP cores bundled with a vendor tool chain because building the equivalent from scratch is about twice the work, so open alternatives only displace vendor IP where they are already good enough to use in practice.[547] An individual licensed block can carry documentation on the scale of a printed phone book, because every configurable register of the block is exposed to the integrator.[117]

Configurability is aimed at the system designer rather than the chip designer: a vendor's configuration interface lets the buyer specify how much RAM and how many converters are wanted, which yields far more combinations than the fixed option table of a microcontroller family.[503] With RISC-V the instruction set architecture is fixed by a ratified specification, but the microarchitecture, the number of cores, how those cores communicate and what I/O goes on the chip are all left to the implementer, so implementations of the same ISA vary widely.[547]

## Board-level consequences

Adopting an SoC reshapes the board around it. Supplying the part can dominate physically: with a separate inductor required per rail, the power supply occupies more area than the processor, and the inductors alone can be larger than the FPGA they feed, while adding cost and efficiency loss.[156] The rails are typically variable-voltage rather than fixed, because the supply voltage is lowered together with the clock frequency to obtain the best power efficiency, so the external supply has to be a variable source.[325]

Moving from a single-board computer to a design with the SoC mounted directly on one's own board is a large discontinuity in skill, which is why vendors offer compute modules as an intermediate step; the alternative is going straight to a high-speed DDR3 layout.[235] Evaluation modules and tooling quality are decisive for parts that require firmware work, and for high-performance parts the vendor must publish example layouts showing how the board is to be laid out.[270] A hard requirement such as a large FPGA with hard processor cores narrows the choice to one or two devices, and the vendor tool chain then comes with the device; replacing a tool chain is not something a project takes on against a deadline.[547]

Selection is not always driven by compute. One head-mounted design chose its part because it offered both MIPI DSI and LVDS outputs matching the display in use, alongside on-chip H.264 and H.265 encode and decode.[638]

## Economics and supply

Yield falls as die area grows, because a fixed density of wafer defects removes a larger fraction of big dies; this is why cost-down revisions shrink the die, which lowers price and raises yield at once.[469] Price expectations can outrun what silicon allows: a chip vendor's own assessment in the mid-2010s was that a one-gigahertz system-on-chip selling for one dollar was not achievable at the time, whatever a board price built on that assumption implied.[253] Cost can also arrive from an adjacent market. The Broadcom part at the centre of the early Raspberry Pi was designed as a multimedia co-processor to sit alongside a phone's main SoC; an ARM core was grafted onto it, which turned it into a small system-on-chip capable of running Linux, and it was inexpensive because phone makers do not pay much for silicon.[529]

For application-specific parts serving a narrow end product, only two or three manufacturers may make the part, and the firmware is commonly written by the chip manufacturer to a settings list supplied by the equipment maker rather than by the equipment maker itself.[270] Supply conditions can invert the usual build-versus-buy calculation: during the semiconductor shortage the lead time on commodity microcontrollers was long enough that designing a custom RISC-V system-on-chip and having it fabricated would have been quicker than waiting for STM32 parts to arrive.[616]

## Custom silicon

The case for a custom chip is normally a system-on-chip case rather than a processor case. Outside a learning exercise there is little reason to design a new processor core when off-the-shelf RISC-V cores are available; the motivation is custom peripherals, a particular feature set or a custom instruction.[616] On-chip SRAM is the practical limit on how much a small custom die can do, and it is what separates a microcontroller from a microprocessor design, since memory has to be placed off chip once the on-die SRAM runs out.[703] The scale of what a small effort can reach is not trivial: a Linux-capable system-on-chip has been taped out on a 130 nm shuttle by a single part-time developer with no prior chip design experience, booting an unmodified upstream Linux kernel with no board support package required.[703]

## Security

Assumptions about physical security are lost along the supply chain. A silicon vendor may reasonably assume that anyone with physical access to the chip can reprogram it, but that assumption is not passed on to the board maker, the OEM that badges the board, or the software vendor above them.[346]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 12 | Dave Is Back And Blogging! | https://theamphour.com/the-amp-hour-12-dave-is-back-and-blogging/ | |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ | |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ | August 23, 2021 |
| 118 | Kickstarter, Open Source RC & Modelsource - Facinorous Financial Foulness | https://theamphour.com/the-amp-hour-118-facinorous-financial-foulness/ | October 21, 2012 |
| 134 | Intel, EPA & Brown Field - Google's Ground Gurgitation | https://theamphour.com/the-amp-hour-134-googles-ground-gurgitation/ | February 25, 2013 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 156 | Tesla, FPGAs and DigiKey - Zesty Zippy Zynq | https://theamphour.com/the-amp-hour-156-zesty-zippy-zynq/ | July 29, 2013 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 253 | Consolidate All The Things - Zonked Zelotic Zaitech | https://theamphour.com/253-consolidate-all-the-things-zonked-zelotic-zaitech/ | June 9, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 452 | An Interview with Kieran O'Leary | https://theamphour.com/452-an-interview-with-kieran-oleary/ | July 28, 2019 |
| 466 | An Interview with Ryan Cousins | https://theamphour.com/466-an-interview-with-ryan-cousins/ | November 10, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 529 | Embedded Hardware with the Raspberry Pi Team | https://theamphour.com/529-embedded-hardware-with-the-raspberry-pi-team/ | February 7, 2021 |
| 547 | Open Source Mindset with Michael Gielda | https://theamphour.com/547-open-source-mindset-with-michael-gielda/ | June 28, 2021 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ | |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
