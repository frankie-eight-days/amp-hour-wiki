---
title: Operating System
concept: operating-system
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

An operating system is the software layer that absorbs hardware variation, so that software written at a sufficiently high level need not care which target it is compiled for.[387] Its presence brings with it a large body of code the project neither writes nor maintains, which is the substantive case for putting one under an embedded product.[581] It also costs boot time, storage, maintenance obligation and attack surface, so the decision to include one is a design decision rather than a default.[334][464][521] The definitive technical boundary between a Linux-class system and a bare embedded one is the memory management unit: task scheduling and interrupting on inputs are the same idea at either scale, but the memory management hardware is what separates the two, whatever the core count on either side.[589]

## What an operating system provides

Because the operating system carries every hardware variant beneath the application, a vendor that controls its own hardware and tolerates no clones supports a far smaller variant matrix than one whose system must run on arbitrary machines.[387] The same distribution can be built for unrelated instruction sets — x86 and AMD parts as well as the ARM processors used on boards such as the BeagleBone and the Raspberry Pi — which is what makes the choice of application software largely independent of the processor underneath it.[387]

Loading files off a disk into memory and executing them is the mechanism from which modern operating systems are assembled, but building a product on an embedded Linux part does not require knowing it; the abstraction holds well enough that a designer can select an application processor and work above the boot path without understanding it.[515] The functionality that arrives with the system is mostly other people's code, providing capability the project does not have to create directly.[581]

## Deciding whether to include one

Devices divide into two classes by their storage budget and what that permits: a low-level embedded part with tens of kilobytes of flash, or a machine with hundreds of gigabytes running a high-level operating system. The storage available is a reliable indicator of which side of that line a design sits on.[464]

Availability immediately after the power button is pressed is a requirement that excludes a large operating system, because boot time is the price paid for one; where a device must be running the moment it is switched on, an operating system is included only if something else in the specification demands it.[521] A low-power display product likewise cannot host a higher-order operating system and so has no font infrastructure to install typefaces into; the substitute is a dedicated font ROM holding the glyph table plus a small routine in the microcontroller that reads glyph data out of it and transfers it straight to the LCD.[700]

Shipping a Linux-based connected product carries recurring costs of its own: SD cards that fail in the field, and the standing obligation to manage an operating system and a software stack. Where the function permits it, a microcontroller with a wireless module carries neither.[189] Bringing up an embedded Linux system-on-module into a fully networked configuration with Yocto took six months of work, which is the counterweight to the ready-made functionality an operating system brings with it.[581] On a self-designed laptop-class computer the board work is the bounded part of the effort — roughly a month of schematics followed by layout, BGA packages included — while the software is where the project stalls, and attempting the operating system as well is the point at which a one-person effort hits a wall.[126]

Arguing the other way, the size of the available engineering labour pool is itself a reason to put an operating system under a product. A rule that everything is written in C on bare metal restricts development to a small population of engineers, and a product intended to grow an ecosystem of third-party devices will exhaust that supply before the performance advantage pays for itself; raising the abstraction level also lets contributors program against generic interfaces rather than hardware-specific calls.[487]

## Working without one

A language runtime intended to run on bare metal cannot call on the system services a Linux-class operating system supplies, so anything it would ordinarily borrow from the kernel — memory management above all — has to be implemented inside the runtime itself.[323] Where application code runs under an interpreted runtime rather than on bare metal, software timing loops become unreliable and blocking the processor for the length of a bit-banged transmission is unacceptable; the work is moved into a hardware peripheral instead, with an infrared remote packet assembled in memory and clocked out by the SPI peripheral at the required frequency.[202]

Portability without an operating system is obtained through layered drivers. A two-tier model separates a hardware presentation layer, whose job is to expose every register of a given chip so that nothing the part can do is hidden, from a hardware abstraction layer above it that reduces a peripheral to a single call such as reading an ADC; application code written against the upper layer moves to a different processor by rewriting only the lower one.[581]

An intermediate arrangement is a vendor-supplied device operating system. Running on an STM32F2 alongside a cellular or wireless module, it lets the customer supply only Arduino-like application code, which is compiled and run on top of it, while the vendor's own background tasks handle network statistics, monitoring and firmware update. Delivering over-the-air update reliably — getting the right data across and checking it — is substantial firmware work the customer is thereby spared.[477]

## Updates, longevity and support

A remotely updatable device should be built so that no update can leave it in a state the owner cannot recover from by changing the code and re-issuing it. Without that property an update is capable of wiping the operating system, at which point the device is broken and no further remote action is possible.[202] A system that cannot be physically reached once deployed is given an operating system selected for robustness against the commands sent to it, so that no remotely issued command can leave the machine unrecoverable.[343]

At the other extreme, a long-lived build or instrument machine is kept alive by pairing an old operating system that does very little with isolation from the network. Once such a machine is on a network, newer machines attempt to talk to it and the system attempts to fetch updates, and both are routes for it to be disturbed.[137]

When the supplier of a device operating system ends support, deployed units keep running and the code remains available for the product owner to develop further, but the update channel closes. The maintenance obligation transfers to the customer rather than disappearing, which makes an announced end-of-update date a scheduling problem for everyone shipping on that platform.[477]

Holding a device's operating system image on a removable SD card rather than in soldered on-chip flash is a deliberate design change, motivated by either cost saving or field flexibility; a side effect is that the complete image can be read out of the product by anyone who removes the card.[646]

## Portability and platform commitment

A desktop operating system carries assumptions about the instruction-set architecture it was built for, so a vendor moving its machines to a different architecture faces an operating-system problem rather than only a silicon one.[387] Engineering tooling concentrates on whichever operating system dominates the desktop, and the concentration is self-reinforcing because the available programming talent follows it; the practical consequence is that changing operating system breaks a substantial part of an established toolchain irrespective of the merits of the alternative.[298] A platform choice that was sound when a product was started is not reopened lightly two decades later, since moving a long-lived codebase onto whichever operating system or language is currently in favour costs more than living with the original decision.[298]

Tools compiled for every operating system rather than one widen who can use them, and that accessibility is paid for by the maintainers, who carry the per-platform build and support burden — a cost open-source EDA projects report directly.[612] Rehosting an application from a native toolkit onto a server-and-browser model generalises it across operating systems and removes the per-platform packaging problem, but direct hardware access does not generalise with it: Bluetooth in particular remains operating-system specific and stays hard to get around.[448]

Instrument and research software frequently builds only against one exact operating-system version, one exact driver and one exact compiler build; shipping the environment as a container image is the practical escape, because it distributes the dependency set itself rather than a description of it.[448] The same problem appears in training, where material must not assume that attendees arrive with a freshly installed operating system on their own machines — that assumption fails in practice, and supplying remote machines that already carry the environment is the reliable alternative.[639] A complete operating system with the toolchain already installed can be delivered inside a browser tab, so that a user opens a terminal and compiles immediately with nothing installed on the local machine.[604]

Portability between similar targets is not automatic either. Substituting one Linux single-board computer for another is not a port in the software sense, because the operating system layer is unchanged; the work reappears at the board level, where pinouts and peripherals differ and previously documented projects no longer match the hardware, which is why the substitution is costly in engineer time despite the identical software stack.[628]

## Security surface

A device built on custom hardware with no operating system presents a very small attack surface: an intruder would need the schematics and the data formats before there is anything to attack, and would then still have to work out how to reprogram the part.[334] Conversely, generating a secret on a general-purpose operating system means trusting the entire machine — a fresh install from scratch, disconnected from any network, and verified free of key loggers and malware. That requirement conflicts with the network access the same application needs afterwards, which is the argument for generating the secret on an isolated microcontroller with its own display instead.[353]

Wiping a commodity machine and reinstalling removes everything above the firmware, because the hardware itself carries no behaviour and merely waits for an operating system to be loaded onto it. What a reinstall does not touch is the boot firmware, a separate layer requiring separate scrutiny: whether the vendor wrote its own or shipped an off-the-shelf BIOS, and whether that code was ever vetted.[335] Boot firmware has grown from the original 64 kilobyte BIOS chips into images containing an entire operating system of their own, so a modern machine runs a complete software stack underneath the operating system its owner installed.[463]

## Market structure

Outside the United States the mobile operating-system split is heavily one-sided: roughly 84 percent of the world's users are on Android against about 14 percent on Apple's platform, which also determines where an application must be published to reach them.[475] An open-source licence on a mobile operating system lets a manufacturer cut off from the original vendor fork the system and ship its own version, with nothing legally in the way. What does not transfer is the proprietary application store layered above it: every application has to be republished to the new store by its own author, so the licence removes the legal obstacle without removing the ecosystem one.[445]

## Historical development

On the earliest machines the read-only memory was constructed physically out of diodes, so reprogramming the operating system was a soldering operation, with the diodes encoding the old code removed and replaced.[578]

The 6502 was designed for distributed processing: one processor to do a single job well and cheaply, with a second processor added for a second job rather than more work loaded onto the first. Against that model, the operating systems needed to support many processors inside one machine are enormous and impose a slowdown of their own.[241]

Connected consumer devices of an earlier generation, built when processing power was more limited, ran a custom Linux assembled with OpenEmbedded and later Yocto; as compute became inexpensive the same class of product moved toward stock mobile-operating-system images rather than bespoke builds.[487] Wholly in-house stacks persist in places. A teardown of a product built on a five-core application processor costing several hundred dollars — a part of the class that would normally run Linux — found the manufacturer's own operating system, its own MPEG codecs and its own USB drivers.[536]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 126 | eReaders, datasheets & board assembly - Yearly Yeasty Yapping | https://theamphour.com/the-amp-hour-126-yearly-yeasty-yapping/ | December 17, 2012 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 241 | An Interview With Chuck Peddle - Charismatic Chipmaking Coryphaeus | https://theamphour.com/241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus/ | March 18, 2015 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11, 2016 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 334 | An Interview with Gerry Roston | https://theamphour.com/334-an-interview-with-gerry-roston/ | February 1, 2017 |
| 335 | When the TV watches you | https://theamphour.com/335-when-the-tv-watches-you/ | February 8, 2017 |
| 343 | Road trip to the deep space network | https://theamphour.com/343-road-trip-to-the-deep-space-network/ | April 17, 2017 |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 387 | Microfichery | https://theamphour.com/387-microfichery/ | April 8, 2018 |
| 445 | Ludicrously High Frequency Interference | https://theamphour.com/the-amp-hour-445-ludicrously-high-frequency-interference/ | June 2, 2019 |
| 448 | An Interview with Jean Rintoul | https://theamphour.com/448-an-interview-with-jean-rintoul/ | June 23, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 464 | KonnectorPanik | https://theamphour.com/464-konnectorpanik/ | October 27, 2019 |
| 475 | An Interview with Christina Cyr | https://theamphour.com/475-an-interview-with-christina-cyr/ | January 19, 2020 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 521 | Outdoor Laser Projection & Object Mapping with Daryl Tewksbury | https://theamphour.com/521-outdoor-laser-projection-object-mapping-with-daryl-tewksbury/ | December 13, 2020 |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ | March 28, 2021 |
| 578 | Histogrammic or Histomagraphical | https://theamphour.com/578-histogrammic-or-histomagraphical/ | February 20, 2022 |
| 581 | Real Time Operating Systems with Brian Amos | https://theamphour.com/581-real-time-operating-systems-with-brian-amos/ | March 13, 2022 |
| 589 | Mute Button Discipline | https://theamphour.com/589-mute-button-discipline/ | May 15, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 639 | Daaaamn We're Duuuummmb | https://theamphour.com/639-daaaamn-were-duuuummmb/ | July 17, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
