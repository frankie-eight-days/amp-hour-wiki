---
title: Linux
concept: linux
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Linux is an open-source operating system kernel used in embedded systems as the general-purpose alternative to bare-metal firmware and real-time operating systems.[378] It is only the kernel, not the interface, and conflating the two misstates what a vendor supplies and what a product team must still build.[378] Its defining architectural requirement is a memory management unit, which is the dividing line between processors that can run the full kernel and microcontrollers that cannot, though cut-down variants exist for parts without one.[146] Its practical significance in embedded work is that it carries with it drivers, libraries and a network stack that would otherwise be a large undertaking to create, at the cost of memory, power, determinism and engineering complexity.[325][466][515]

## Hardware requirements

A full Linux kernel requires a memory management unit; this single architectural feature, together with the memory it implies, decides the boundary between processors that can run Linux and microcontrollers that cannot, and some microcontrollers now sit directly at that boundary.[146][653] The kernel also imposes a RAM floor: eight megabytes is the practical minimum and is cramped, an amount that is enormous by microcontroller standards, so memory cost is part of the decision to run it.[359] A die without sufficient on-chip memory cannot run Linux at all; a Linux-capable core on such a part must go off-chip for memory, at which point the input-output bandwidth to that memory becomes the limit.[616]

Sleep-mode power is where embedded Linux systems are weakest: a microcontroller running bare-metal code out of internal SRAM, with no external DRAM to keep alive, is orders of magnitude better.[515] A single-board Linux computer needs a mains supply or a large battery, and using one for a task a microcontroller could do wastes most of the power it draws; low-power Linux boards are quoted at around two watts.[565]

The crossover in silicon cost is narrow — roughly ten dollars for a Linux-capable system against five for a microprocessor system — so volume rather than capability often decides which side of the line a design falls.[515]

## Determinism and real-time behaviour

Linux is not deterministic, so timing-critical control cannot be placed in it; robotics work that must react within a bounded time has to keep that path off the general-purpose operating system.[97] Real-time motor control loops do not belong in Linux; the standard arrangement is a second processor or real-time core handling the loop while Linux handles everything above it, and the designer then has to account for buffer sizes and how often Linux services the interface.[466]

On Texas Instruments system-on-chips, programmable real-time units are used to synthesise peripherals the part has run out of — software UARTs, extra pulse-width-modulation outputs, and a fourth quadrature encoder where only three exist in hardware — all while Linux runs on the main cores.[378] Real-time firmware for those cores is deployed by placing the executable in the kernel's firmware directory and instructing the kernel to load it, after which it is reloaded automatically on every boot.[378]

Splitting a machine between Linux and microcontrollers is a live architecture in motion control: in one pick-and-place design the planner runs on Linux and sends timed packets over USB so that microcontrollers on the head and the base stay step-synchronised.[686]

## Device drivers and the device tree

Linux presents devices as files, so a driver's job is to map a part's register set onto virtual files that application code reads and writes; an accelerometer becomes files carrying the three axes.[378] The correct way to reach hardware under Linux is a kernel driver, with nothing in user space touching peripheral registers; memory-mapping a peripheral from user space is common because it requires less understanding of the system and reaches a timing goal sooner, not because the resulting code runs faster.[378]

The kernel already contains support for most classes of device, so bringing up a new part on a board is largely a matter of declaring its presence and address in the device tree rather than writing code.[378] Separating hardware description into a device tree rather than embedding it in application source is what makes a later change of chip affordable; where the pin mapping and controller specifics are woven into the code, unpicking them is expensive and produces corner-case defects.[711]

Custom logic in an FPGA is only half the work: once the fabric talks to the processor, someone still has to write the Linux driver, because the kernel has no knowledge of a block that did not exist before.[466]

## Boot process and board bring-up

On a system-on-chip combining ARM cores with FPGA fabric, the processor boots first and brings up the fabric rather than the other way round: JTAG reaches the ARM side, a debug UART is established, U-Boot is placed in boot flash and ported, and only then can a kernel be booted.[469] The bootloader reads the kernel image from an SD card or flash into RAM and sets the program counter to it; drivers are either compiled into that image or loaded afterwards as kernel object files, which means enough must be built in to reach the storage and its file system before any module can be loaded.[515]

Moving the console to a different UART is a multi-place change: the base address and pin multiplexing in the U-Boot source and device tree, and separately the kernel's own console setting passed as boot arguments; getting only the first half right produces a bootloader that prints and then a blank screen after the kernel starts.[515] The same change can be far more expensive on an unfamiliar tree: moving a console from one UART to another once took a month and a half because roughly ten places in the kernel source had to be found and altered.[325]

When selecting a processor for an embedded Linux design, the criterion is not merely that the kernel and bootloader support it but that a build system — Buildroot or Yocto — does, because that support decides how much work the board bring-up will be.[515] Across ten different embedded Linux boards, most parts took roughly three hours of software work to reach a prompt, so the barrier is knowing the process rather than the per-part effort.[515] Some processors are effectively plug and play: soldering the part down with a chunk of DDR memory and inserting an SD card was enough to boot one Allwinner device straight away, which is the property to look for when choosing silicon.[515]

Getting Linux running properly on a new board can exceed the effort of designing the hardware, and was the single largest drain on engineering resources for one FPGA module product.[466]

## Build systems and distributions

The working method with Buildroot is to configure a defconfig, build, write the resulting image to an SD card, boot it and then modify it incrementally, adding drivers and changes on a system that already runs.[515] Buildroot is simpler than Yocto at the price of doing more yourself, and Yocto's layered overlay system is what makes it heavier; a camera product built on a compute module used Buildroot to generate its distribution.[614]

Choosing a mainstream distribution over an embedded build system is a decision about who the customer is: Ubuntu gives software developers the package manager they expect, at the cost of maintaining a general-purpose distribution, with its releases every April and October, on an embedded platform.[466] A fielded Linux product needs its update path designed defensively: a power-on self test with fallback to the previous image means an update interrupted by loss of power does not brick the device, and that behaviour has to be tested deliberately.[614]

## Comparison with real-time operating systems and bare metal

A real-time operating system of the FreeRTOS type is a scheduling kernel with queues, semaphores and task notifications and nothing else, whereas Linux brings libraries and drivers with it; the RTOS earns its place by bounding operations in time, since every call takes a timeout and forces the designer to decide what happens when the deadline passes.[581] Zephyr was built as a distribution rather than a bare kernel, standing in the same relation to other real-time operating systems as a full Linux distribution does to the kernel alone, and it carries Linux conventions into the microcontroller world, including the device tree and a Linux-style configuration system.[653] The device tree idea carried over from Linux lets a driver be swapped without rewriting application code: the device is looked up by name and the code calls a generic interface, so replacing one real-time clock part with another is a driver plus a project-file change; the cost of that convenience is download size, with pulling every vendor software development kit into one tree running to tens of gigabytes.[509]

Bare metal remains the alternative for teams that want the system to work without rebuilding device trees, kernel modules and drivers against versions that stop being supported.[466] In regulated work the kernel's size counts against it: verification and validation of a system carrying millions of lines is a different undertaking from validating a few thousand lines running bare metal.[466] Where a system's function is confined to a real-time task, a small kernel that pulls in few third-party dependencies gives better provenance over what actually runs on the silicon, easier tracking when a security defect appears, and a smaller surface to certify.[653]

A price-based rule of thumb used in production test work puts devices under a hundred dollars in real-time operating system territory, where a temperature sensor has no business running a full kernel, and devices above about two hundred and fifty dollars in Linux territory.[544] Graphical user interface toolkits distort cost comparisons: the free options for bare-metal and real-time systems are poor, and a commercial toolkit licence runs to about ten thousand dollars, which on a low-volume product can justify moving to Linux and Qt instead.[515] The presence of a touchscreen is not by itself a reason to run Linux, since embedded graphics on microcontrollers is routine; the case for Linux is built on the whole set of subsystems a product needs.[515] On the firmware side, an experienced practitioner will strip a real-time operating system out of a design in favour of bare metal or a small scheduler and message passer, and reverses that position when the product needs a touchscreen interface, storage and networking at once.[187]

The character of the work differs from bare metal: bare-metal C is dominated by writing code and reading register maps, while embedded Linux work is dominated by reading other people's source.[515] Assembling a system from device tree files and existing programs rather than writing it produces fewer defects, because every line written is a line that can be wrong; the offsetting cost is that the first board support package is painful.[515] Linux projects are more complex than microcontroller projects in a way that shows up as team size: a single engineer can carry hardware, firmware and production for a small embedded product, while a Linux-based product of the same ambition needs more people to ship in a normal timeframe, or an engineer with a set of tools they have already used on previous systems.[614]

## Networking, portability and longevity

Networking is where Linux is hardest to argue against: the same network stack that runs servers is available, a sixty-cent SDIO Wi-Fi module can be wired to an MMC bus and enabled with an existing driver, and no proprietary TCP/IP stack with its list of unsupported features is involved.[515] Existing Linux drivers cover work that would otherwise be a large undertaking, which is why instruments that gained USB mass-storage and similar interfaces late did so once they moved to a general-purpose kernel.[325]

Binaries are portable across ARM Linux systems in a way firmware is not: a precompiled ARM executable copied onto the SD card of an unrelated board runs, because the program does not know which system-on-chip it is on.[515] Source-level longevity is a distinguishing property: a program built a decade ago can usually be rebuilt and run today, and an old distribution can be installed in a virtual machine to build code from twenty-five years ago, which is why open formats and open toolchains bear directly on long-term data access.[463] That longevity contrasts with closed tools: a widely used FPGA suite segmentation-faulted during synthesis on current Linux distributions for years with no recourse available to users, whereas an open toolchain leaves the option of inspecting and fixing it.[423]

## Development workflow

Case sensitivity in file names is a real portability failure: a library that includes a header with the wrong capitalisation compiles on Windows and fails on Linux, and the fault appears to be in the build environment rather than the code.[599] Cross-platform compilation does not follow automatically from writing portable source; a project planned as cross-platform from the first day still met substantial work to build for Linux.[368]

Continuous integration for embedded work depends on being able to build from the command line rather than only inside an IDE, because only a command-line build is repeatable on a machine nobody is watching.[556] Command-line builds on Windows were historically painful enough to tie developers to IDEs, and the Windows Subsystem for Linux is what made that workflow practical on Windows machines.[556] Embedded development remains predominantly hosted on Windows, with over sixty percent of attendees at one practitioner training reporting it as their operating system.[612]

Storing the toolchain alongside the code protects a project from its own build environment ageing, and is lighter than archiving a virtual machine image, which drags a whole operating system and its interface along with the compiler.[612] Embedded toolchains do not install equally on every host: one Zephyr toolchain took a full day on Windows without success and installed on Linux immediately, so the documented host for a framework is a practical constraint on the developer's machine.[511] A vendor's own tools are expected to install and build without assembly: where the supplied development software does not simply work, that is itself evidence against choosing the silicon.[470] Pinning a build machine to an old kernel version has physical consequences: one team's build system could not accept wireless cards at all and had to be given a wired connection.[475]

## Hardware integration

### Modules and systems-in-package

A compute module packages the processor, RAM and flash on a single connector so a product can carry Linux without the designer solving memory routing; a hackable camera product was built this way with a full single-board computer inside every unit.[235] A system-in-package takes that further by integrating over a hundred components into one wide-pitch BGA, removing the memory layout and controlled-impedance work from the customer's board at a price premium over the equivalent development board.[362] The appeal of that approach for industrial work is that it puts Linux on a board with one part soldered down, and it is the answer where the processor itself cannot be bought as a loose chip.[482]

Where such a module is open source, the customer can read its bill of materials and ask for a part that is holding up delivery to be depopulated, or change it themselves, which is the argument for the user of a central building block owning that block.[681] The hardware abstraction Linux provides is what makes a module upgrade path real: if a later, faster module keeps the same footprint and pinout, the same base board can carry it after retesting.[681] Building a Linux computer from a system-in-package is within reach of an engineer who has made microcontroller boards, provided they understand signal integrity and matched trace lengths; those are the skills that should decide the attempt, not the software.[378]

### Single-board computers

Single-board Linux computers combine a desktop environment reached over HDMI, USB and audio with direct access to the input-output pins, and are provisioned by writing a distribution image to an SD card.[59] An SD card as the root file system is a wear item: a product built on that arrangement failed through card death in the field, and the experience argued for a microcontroller with a wireless module in place of a board that requires managing an operating system and software stack.[189]

Development-board design frequently obstructs the intended use: on one Linux-capable microcontroller board the display pins were routed to an HDMI transmitter so a parallel LCD could not be attached at all, only a subset of the input-output reached any pin, and boards loaded with transceivers and terminal blocks for every bus reach several hundred dollars.[515]

Devices sold as simple serial peripherals are frequently full Linux systems inside; marketing a module as a serial-to-wireless converter limits the support obligation to documenting the serial interface, while the knowledgeable user can replace the firmware with OpenWRT and run a web server on it.[359]

### Linux in FPGAs and custom silicon

A soft RISC-V core can put a multi-core Linux-capable system inside a modest FPGA, on the order of thirty-five thousand lookup tables or fewer, which contradicts the assumption that Linux in fabric requires a very large device.[547] A Linux-capable system-on-chip has been taped out on a shared 130-nanometre shuttle by one part-time developer with no prior chip design experience, and it boots an unmodified upstream kernel with no board support package.[703]

## Security and fleet maintenance

Cheap silicon capable of carrying a Linux stack does not mean a product should carry one: the network stack arrives but the hardening does not, and default credentials persist because a device needs some reset path, with no password amounting to the same exposure as a shared default.[321] Once a device holds an IP address on a Linux stack, its attack surface is larger than a comparable microcontroller product, because network reachability, common open-source components and shipped defaults all widen the ways in.[698]

Reproducible builds are the supply-chain answer at distribution level: Debian's move to full reproducibility means the artefacts can be rebuilt identically at every level, and because Debian sits upstream of Ubuntu the property propagates downstream.[724] Fielded fleets can be kept current with an immutable Linux image aimed at single-board computers, where updates are pushed as packages to machines already deployed rather than reflashed by hand.[720] A remote shell and the ability to run a container on the target are why remotely managed assets are built on Linux, whereas over-the-air update mechanisms for microcontrollers remain awkward by comparison; power consumption is what pulls the decision back the other way.[723]

## Product and staffing considerations

Choosing Android on top of the same hardware is a staffing decision as much as a technical one: it supplies an interface users recognise and lets the work be done by developers who write Java applications rather than by scarce low-level C engineers.[167] The same argument constrains ecosystem design: insisting that everything be bare-metal C limits a product line to the number of engineers who can work that way, and raising the abstraction level widens the pool that can build on it.[487] Putting a whole Linux computer into a device that only toggles three outputs and turns on a light is defensible where the organisation's engineers write Python and JavaScript, and where the vehicle's battery makes the extra draw a small fraction of the total; on a scooter design the argument was made on team skills rather than power.[487]

## Commercial structure

Software given away without warranty or complete documentation creates the opening for a business selling support and end-to-end service around it, which is how Red Hat and IBM built on the kernel and is the model open hardware inherits.[105] The commercial value of a free tool sits in services rather than licences, and the same route is expected for open-source design tools, where the expensive part for a company switching is the manpower to rebuild libraries rather than the software itself.[441] Paying for software buys someone to hold to an agreement; that accountability is the thing a free project cannot supply, and it is a legitimate input to a tooling decision independent of technical merit.[489] Nearly all users of an open-source system consume a finished, supported distribution rather than building from source, so the packaged product and its support are what determine whether the underlying project reaches users at all.[22]

Linux appearing in progressively cheaper products changed production test equipment: programming fixtures aimed at 32-bit microcontrollers had to be extended to program Linux devices over USB.[544]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 22 | The Hard Work Hypothesis | https://theamphour.com/the-amp-hour-22-the-hard-work-hypothesis/ | December 21, 2010 |
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ | |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ | |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 146 | Hamvention, Arduino and Intel - Burdensome Background Battology | https://theamphour.com/the-amp-hour-146-burdensome-background-battology/ | May 21, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 321 | Monster Scale Production | https://theamphour.com/321-monster-scale-production/ | October 27, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 368 | The EEVblog Sparkgap Generator | https://theamphour.com/368-the-eevblog-sparkgap-generator/ | November 19, 2017 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 423 | Open FPGA Toolchains at 35c3 | https://theamphour.com/423-open-fpga-toolchains-at-35c3/ | January 1, 2019 |
| 441 | Motivational Speaker | https://theamphour.com/441-motivational-speaker/ | May 5, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 466 | An Interview with Ryan Cousins | https://theamphour.com/466-an-interview-with-ryan-cousins/ | November 10, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 470 | Just Add Salt | https://theamphour.com/470-just-add-salt/ | December 8, 2019 |
| 475 | An Interview with Christina Cyr | https://theamphour.com/475-an-interview-with-christina-cyr/ | January 19, 2020 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 489 | An Interview with Jack Ganssle (2nd) | https://theamphour.com/489-an-interview-with-jack-ganssle-2nd/ | April 19, 2020 |
| 509 | Cellular IoT with Jared Wolff | https://theamphour.com/509-cellular-iot-with-jared-wolff/ | September 20, 2020 |
| 511 | Brewing Electronics with Eli Hughes | https://theamphour.com/511-brewing-electronics-with-eli-hughes/ | October 4, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 547 | Open Source Mindset with Michael Gielda | https://theamphour.com/547-open-source-mindset-with-michael-gielda/ | June 28, 2021 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 581 | Real Time Operating Systems with Brian Amos | https://theamphour.com/581-real-time-operating-systems-with-brian-amos/ | March 13, 2022 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 653 | Benjamin Cabé Nose Zephyr | https://theamphour.com/653-benjamin-cabe-nose-zephyr/ | December 11, 2023 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
| 711 | Medical Electronics Education with Mark Palmeri | https://theamphour.com/711-medical-electronics-education-with-mark-palmeri/ | December 21, 2025 |
| 720 | Hyper Growth and OpenClaw Interns | https://theamphour.com/720-hyper-growth-and-openclaw-interns/ | March 31, 2026 |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ | May 7, 2026 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
