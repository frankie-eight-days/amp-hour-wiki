---
title: RAM
concept: ram
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**Random-access memory** (RAM) is the working memory of a computing system, holding code and data for immediate access by a processor, in contrast to non-volatile program storage.[713] In embedded engineering it is treated as the resource that runs out first — ahead of program storage — and as the primary bottleneck when selecting a part.[224] Its cost historically shaped processor architecture itself, and its capacity continues to determine what class of software, graphics, and operating system a given machine can support.[241][359]

## Role in embedded system design

In embedded work, RAM is almost always the first resource exhausted and is the criterion on which parts are selected.[224] Memory ceilings rather than processing speed are what push designers from smaller processor cores to larger ones, since the smaller cores cannot address as much program storage or RAM; when a program outgrows its part, the choice is to pay for engineering effort to shrink the code or to move up to the larger device.[187] A representative selection case is a microcontroller chosen for its combination of 256 kilobytes of program storage and 64 kilobytes of RAM in a physically small package — available in through-hole, small-outline and leadless forms — rather than for its processor architecture, which was judged not to matter.[224]

A microcontroller is conventionally defined as a part carrying both its own RAM and its own program storage; a device with internal RAM alone does not strictly qualify, and starts with nothing to execute at power-up.[713]

### The constrained end of the range

Practitioners working in the deeply embedded range operate below about sixty megahertz, and treat half a megabyte of RAM as an unfamiliar abundance.[187] Very small parts remain in current use at the bottom of the range: a low-cost processor running at forty-eight megahertz with sixteen kilobytes of program storage and two kilobytes of RAM.[637] Platforms of that size force optimisation only when a design moves toward commercial production, since a two-kilobyte RAM budget cannot absorb general-purpose library code.[661]

At the extreme, a processor with roughly 256 bytes of RAM requires the memory to be partitioned deliberately and the code hand-optimised instruction by instruction, with cycle counts tracked individually.[212] A long-lived instrument design written in assembly on a twenty-year-old processor reached the point where roughly three bytes of RAM remained, and new features had to be built within whatever was left.[522]

## Managing scarcity

### Library overhead

The standard library is a major consumer of a small memory budget: using a formatted print routine even once forces the whole library to be linked in, adding a kilobyte or two — enough to justify writing a replacement routine by hand.[541] The cost is invisible at the call site, since a single added line pulls in layers of library code whose memory use the author never sees.[541] The same problem was familiar in earlier practice, where adding a print statement for debugging was impossible because the routine would have consumed more memory than the entire device had; the working maxim that follows is to write code as though RAM remains scarce, on the reasoning that program storage has become cheap while RAM has not.[490]

### Reserved and repurposed memory

A vendor's radio protocol stack supplied as a binary occupies a fixed region of both program storage and RAM that the application must reserve and must not touch, with the stack at the bottom of the address space and the bootloader at the top, both in protected regions.[516] Conversely, loading configuration or code into a peripheral's RAM at every wake-up, rather than maintaining firmware images in each device, is a deliberate architecture that removes the problem of keeping separate configurations correct.[667]

### Substitution under shortage

A component shortage that forced substitution to a variant with half the memory required the existing code base to be halved as well, achieved by disabling functionality rather than by redesign.[541]

## Memory-demanding workloads

### Graphics

Graphics is where memory demand grows fastest: holding a full frame buffer means every pixel occupies memory, which requires both substantial RAM and enough processing to move all those pixels.[467] The constraint still binds on contemporary microcontrollers — a part with 192 kilobytes of RAM, generous for its class, still cannot hold a complete frame buffer.[356] Historically, the transition from text and executables to bitmapped images, fonts and graphical elements is what caused memory requirements to explode, since a program made only of instructions is small by comparison; on early bitmapped workstations the display consumed roughly half the total memory, and programs would blank part of the screen to reclaim that RAM for their own use.[361]

### Security material and protocols

Security material carried over from mobile practice does not fit constrained devices: a certificate sized for a phone application can consume all the RAM available on an embedded target.[526] Protocols inherit the assumptions of what they were designed for, and the web protocols were never optimised for a limited memory budget or a small maximum packet size — the mismatch that motivated a constrained-device alternative modelled closely on them.[526]

### Interpreted languages

An interpreted language on a microcontroller stores its compiled bytecode in RAM rather than in program storage, so the memory budget must accommodate the program itself and not only its data.[383] Source comments carry a runtime cost in such an environment, because the file is loaded into RAM in its entirety, so the memory has to hold the comments as well as the code.[323]

## Operating systems and boot

An operating system's memory appetite decides which class of processor can run it: a full general-purpose kernel needs megabytes and is cramped at eight, so a device with half a megabyte of RAM runs a real-time operating system instead.[359] Running the general-purpose kernel on such a device requires cutting it back to the point that it is barely the same system; eight megabytes is simultaneously enormous by microcontroller standards and tight by kernel standards.[359]

The boot sequence on a memory-managed system reads the kernel image from storage into RAM at some address and sets the program counter to that address, after which loadable driver modules are read from a file system into RAM and initialised.[515] That arrangement creates a bootstrapping order problem, since enough drivers must be compiled into the kernel image for it to reach the storage device and file system that hold the remaining modules.[515]

## Physical integration and board design

Large memory in mobile processors is achieved by stacking a second die carrying the memory on top of the processor die inside one package rather than by placing separate parts on the board.[54] That integration is what makes such a processor a complete system rather than a bare core: display drivers and memory are built in, whereas a plain processor requires everything to be added around it to become useful.[58] Adding memory to a processor complicates timing closure, because more memory means more routing to carry addresses from the processors and more concurrent accesses to arbitrate on the bus.[687]

At the board level, memory that is soldered directly to the circuit board rather than socketed cannot be upgraded without desoldering, and a machine built to a custom memory specification is assembled to order rather than drawn from stock.[408]

## High-speed memory systems

In a high-speed board design the memory interface, not the display interface, is the signal-integrity problem: a display link is a terminated differential pair and straightforward, while the memory bus is multi-drop and running fast.[325] On one camera design built around a newly chosen programmable logic device, getting the memory interface working was the riskiest element, with a fallback to the previous device planned if it had not worked within weeks of the deadline.[325]

Memory bandwidth rather than capacity set the resolution limit on that design, which consumed more than sixty percent of a theoretical 4.8 gigabytes per second.[325] First-in first-out buffers are required in front of shared memory because the memory must be time-shared between the incoming data, the readout for display and its own refresh cycles, so writes have to be pausable; true dual-port memory would remove the need for them.[325] The resulting data path fills a buffer from the incoming stream, trips logic at a fill level that drains it into main memory, and has separate logic read back out at the display rate through a second buffer while applying gain, offset and colour processing.[325]

Capacity translates directly into capability in a capture instrument, where record time scales with installed memory: doubling to thirty-two gigabytes would extend recording to about sixteen seconds.[325] The limit on installing more was the memory controller rather than the board — signal integrity would have supported a second module, but the controller as implemented supported only one.[325] Capture instruments that instead stream to the host shift the constraint onto the host's memory, where analogue data sampled at fifty megasamples per second exhausts even a sixteen-gigabyte machine within tens of seconds.[237]

## Host and fleet memory

Host memory shows a threshold effect in compilation and toolpath generation: exceeding available RAM sends the process into paging and lengthens run time sharply, while crossing back above the requirement can cut the time by an order of magnitude; the improvement past the threshold is abrupt rather than gradual, with run time dropping to roughly a tenth.[138][438] One generation job was brought down to six hours only by raising the host machine to thirty-two gigabytes of RAM.[438] A machine controller with limited RAM cannot hold an entire job, so the toolpath is streamed to it one move at a time and buffered; a part with more memory allows a deeper planner queue until the depth stops being the limiting factor.[438]

In server fleets memory is frequently stranded, with capacity sitting unused on a machine whose processing is idle and no mechanism to lend it to another machine that needs it.[357]

## History

Memory technology preceding random-access parts was recirculating shift-register memory, a single-input single-output device that behaved as a first-in first-out buffer rather than allowing arbitrary access.[684] Some early programmable machines had no addressable memory at all, offering only a stack a few entries deep.[35]

The cost of memory shaped early processor architecture directly: an eight-bit external bus variant of a sixteen-bit processor was insisted upon, and became the version widely adopted, because memory was expensive enough to justify halving the number of parts.[241] Historically significant machines ran in what would now be trivial amounts of memory, including a fully discrete guidance computer with four kilobytes and a working sprinkler controller written in machine code within two kilobytes of RAM.[709] Development before erasable storage was mediated by emulators: a device that presented itself as memory to the machine under development while appearing as writable storage to the host, which avoided repeatedly erasing parts under ultraviolet light.[247]

## Programmable logic practice

Portability between programmable logic vendors requires memory blocks to be isolated in their own wrapper, because vendors' memory primitives differ and one vendor's memory may need two clock cycles to complete a read where another needs one.[147] The design should therefore be written to tolerate differing clock counts rather than assuming a fixed access latency.[147]

## Instrumentation, security, and failure modes

A trace peripheral can be pointed at an address in RAM to record program flow in a buffer the designer allocates; at eight bytes per recorded branch, a 256-byte buffer holds about thirty-two branches.[383] Executing from RAM rather than from program storage changes power consumption measurably, with one low-power part quoted at thirty-two microamps per megahertz and roughly two microamps per megahertz of difference between the two execution sources.[636]

Memory contents are a target in hardware security work, since sensitive material copied into RAM at power-up for speed becomes readable if the chip's protection can be downgraded to allow debug access.[575] One published attack chain reduced a device's readout protection from its maximum level to a level that grants debug access limited to RAM, which was sufficient because the private material was resident there during a firmware update.[575]

Memory faults present as system-wide erratic behaviour rather than as a clean failure: one instrument ran correctly for about thirty minutes before every relay and driver began operating at random as the controller emitted garbage onto its data lines — a failure traced to the RAM.[431]

## Scaling trends

The generational memory increases that characterised earlier computing have slowed, with one console generation moving from eight to sixteen gigabytes, described as the smallest such increment on record where a doubling or more had been normal.[490] Where memory scaling slows, manufacturers differentiate products on other axes such as power consumption and storage technology rather than on capacity alone.[61] One consequence of the capacity-versus-speed trade is baking a model into read-only memory instead of holding it in RAM, which allows it to be accessed far faster and entirely on chip, at the cost of fixing its contents at manufacture.[722]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 35 | An Interview with Jeri Ellsworth - The Ternary Tussle | https://theamphour.com/the-amp-hour-35-the-ternary-tussle/ | |
| 54 | An Interview with Jack Ganssle - Embedded Elchee Epexegesis | https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/ | |
| 58 | Multicopter, DIY drones & Tektronix - Zappy Zendik Zoilism | https://theamphour.com/the-amp-hour-58-zappy-zendik-zoilism/ | |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ | |
| 138 | An Interview with Ryan Brown - Effortless Equipment Extensibility | https://theamphour.com/the-amp-hour-138-effortless-equipment-extensibility/ | March 25, 2013 |
| 147 | An interview with Jeri Ellsworth - Absorptive Augmented Actuality | https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/ | May 27, 2013 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 241 | An Interview With Chuck Peddle - Charismatic Chipmaking Coryphaeus | https://theamphour.com/241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus/ | March 18, 2015 |
| 247 | An Interview with Voja Antonic - Gerontogenous Galaksija Genesis | https://theamphour.com/247-an-interview-with-voja-antonic-gerontogenous-galaksija-genesis/ | April 29, 2015 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 357 | An Interview with Rick Altherr | https://theamphour.com/357-an-interview-with-rick-altherr/ | August 28, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 431 | An Interview with Adam McCombs | https://theamphour.com/431-an-interview-with-adam-mccombs/ | February 24, 2019 |
| 438 | An Interview with Bart Dring | https://theamphour.com/438-an-interview-with-bart-dring/ | April 14, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 526 | Why IoT Is Difficult with Jonathan Beri | https://theamphour.com/526-why-iot-is-difficult-with-jonathan-beri/ | January 18, 2021 |
| 541 | Chip Shortage Denier | https://theamphour.com/541-chip-shortage-denier/ | May 10, 2021 |
| 575 | New Life Skills with Joe Grand | https://theamphour.com/575-new-life-skills-with-joe-grand/ | January 30, 2022 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ | |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 709 | Nobel Prize Winner Dr Barry Marshall | https://theamphour.com/709-nobel-prize-winner-dr-barry-marshall/ | November 10, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
| 722 | AI Tooling with Matt Liberty and Luke Beno | https://theamphour.com/722-ai-tooling-with-matt-liberty-and-luke-beno/ | April 22, 2026 |
