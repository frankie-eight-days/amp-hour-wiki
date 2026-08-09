---
title: UART
concept: uart
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **UART** (universal asynchronous receiver-transmitter) is a hardware peripheral that implements asynchronous serial communication between digital devices, and it is one of the most widely assumed capabilities in embedded computing.[137][24] Almost every serial link in practice uses the same framing — eight data bits, no parity, one stop bit — so the only settings a user normally has to get right are the baud rate and which port to open.[391] The dedicated serial interface chip is conventionally listed among the components that changed the electronics industry, alongside the first flash-programmable microcontroller and the first ARM processor.[24]

## Hardware availability and history

Hardware serial was not always assumed on a microcontroller: the cheapest parts historically had no serial peripheral at all, and designers bit-banged their own on general-purpose pins.[137] One major vendor was slow to put serial peripherals into its low-end parts, which pushed designers toward competing families that had one or two, and the gap persisted for years before it was closed.[524] At the very bottom of the market the peripheral still does not exist: a three-cent microcontroller has no hardware serial, so its output is bit-banged in software on an ordinary I/O pin.[493]

Peripherals can be wrong in silicon rather than in firmware: on one part the two serial ports were transposed — the pins as well as the registers — and the fact was added to the errata sheet months after release, after users had spent time debugging a port that could not work.[524]

### Pin assignment

Some microcontrollers carry an internal routing matrix, comparable to the routing inside an FPGA, so a serial peripheral can be assigned to almost any pin rather than to a fixed pair.[125] That flexibility is not usually a reason to choose a part, but it rescues layouts by removing the situation in which the required peripheral sits on a pin that cannot be escaped.[468] The board designer and the firmware engineer pull in opposite directions over which serial pins to use, because the convenient pin to escape from a ball grid array is rarely the default peripheral pin; deliberately using a different serial instance on a second board is a good way to learn where the configuration actually lives.[515]

Flexible peripheral blocks are allocated, not free: where a device offers four instances that can each be configured as SPI, I2C or serial, using all four as serial ports leaves nothing for the other two protocols.[654]

## Configuration and bring-up

The two ends of a serial link must share a ground reference; without it the transmit and receive lines carry nothing regardless of what the firmware is doing.[378] Swapping transmit and receive is the standard wiring error, and swapping it twice on the same board cancels out, which is how a link sometimes works by accident.[378]

When nothing comes back, the first move is to put an oscilloscope or other external instrument on the line and establish whether anything is being transmitted at all.[391] A protocol analyser is not self-explanatory: it decodes correctly only if it is set up correctly — the software timeout on an SPI capture, for instance — so it supplements knowing the protocol rather than replacing it.[391] Not every periodic signal on the expected pin is the expected signal: a waveform taken for serial output turned out to change its packet length as a hand approached the board, which identified it as something other than the UART.[493]

On a Linux single-board computer the pin has to be in serial mode before anything works: if the board table does not already list it as a serial port, a configuration tool must switch that pin's peripheral function.[378] Once the pin is in the right mode the port is reached through the device node, and any ordinary serial library will do, whatever the language.[378] The same pin can be switched between functions at run time — put into serial mode to talk to one device, then back to SPI to talk to another — which is possible and rarely advisable.[378]

## Performance and buffering

A well-implemented peripheral will run at baud rates up to a quarter of the peripheral clock, which puts 12 megabaud within reach on a conventional microcontroller — a rate at which a receive FIFO stops being optional.[224] The defect to check for in a FIFO implementation is a missing timeout interrupt: if the interrupt fires only at a fill threshold, a burst that ends short of it sits in the FIFO indefinitely, which shows up as the last few bytes of a large transfer never arriving; the workaround is a timer interrupt set a few microseconds after the last byte that drains whatever remains.[224]

Demand for serial ports on small boards exceeds what the parts provide, which is why bit-banging libraries exist for something as basic as a serial port; software serial on a small board tops out around 9600 baud and is not always reliable, particularly when it is also carrying debug output.[395]

## UARTs in programmable logic

Writing a transmitter and a receiver is the standard first exercise in a serial protocols course, with an LED toggled on receipt of a known character so the student can see it working before anything else is attempted.[318]

Reusing an open-source core is not automatically cheaper than writing one: a core emulating a full 16C550 with multiple baud rates and framing options occupied more area than the CPU next to it, where the actual requirement — 9600 baud in each direction — fits in twenty or thirty flip-flops written directly.[101] Cores from public repositories vary widely in quality and are often aimed at a different problem, so the practical filters are who wrote it and how recently it was updated.[101] Hardening a serial port into an FPGA is a poor use of silicon: it is a small block of logic running slowly, and the vendor cannot predict how many a given customer wants or which features they need.[103]

The soft system-on-chip inverts the selection problem: instead of hunting for a microcontroller with exactly the right number of serial ports, an existing core is taken and the one missing peripheral is added, which turns firmware that would have relied on DMA tricks and bit-banging into something simple.[423] A controller needing thirty-two serial outputs from one unit is far easier to build by driving data into an FPGA and splitting it than by finding a microcontroller with thirty-two ports.[423] The same requirement is one of the standing arguments for custom silicon: a part with sixteen serial ports is hard to buy off the shelf but straightforward to specify if the chip is being made.[503] Where soft cores are used at scale, a small number of well-supported blocks become de facto standards even for something as simple as a serial port, so the same peripheral appears regardless of which processor is chosen — though the software still talks to it through a driver rather than by writing registers directly.[395]

### Programmable I/O blocks

A programmable I/O block takes a third position between hardware and bit-banging: small stripped-down processors that are very good at deterministic high-speed bit-banging and poor at everything else. The timing-critical part of a software peripheral is pushed onto them and then accessed through FIFOs and DMA as if it were a hardware block, so the resource can be committed to extra serial ports — or to protocols nobody would commit to silicon.[687] An addressable LED protocol has been driven with zero processor overhead by feeding a state machine over DMA, which is not something a chip vendor would build a dedicated peripheral for.[687]

A peripheral can also be repurposed directly when the one needed is absent: a codec requiring I2S on a part with no I2S support was driven by pressing the serial peripheral into service for the I2S bus and bit-banging the remaining pins, with about eight instructions of timing margin to work in.[375]

## Firmware architecture

Serial input is a good argument for interrupts over polling: an interrupt from the peripheral can deliver a meaningful block of data and then signal a task to wake, rather than a task spending cycles checking at some interval; systems built that way scale better, respond faster and use less power, since an event-driven design lets the processor stay asleep.[581] A reliable sign that a long-running computation should become its own task is finding oneself adding a check on the serial port every hundred iterations of a loop to avoid a buffer overflow and dropped characters.[581]

Adding a second serial port breaks the habitual output path: the standard print function targets one port, so a second requires a function that takes the port as an argument or otherwise selects between them.[478] Moving the console from one serial instance to another on an embedded Linux system was not a configuration change: register values had to be found and changed in about ten separate places in the kernel source tree, and the exercise took over a month for someone new to it.[325]

A serial console is a useful skeleton to start a project from: it needs the serial peripheral, and once it exists the other drivers can each be exercised from it, so the system is built up from working pieces rather than from a blank page.[373] The case for including a shell over the serial port in an embedded project is not obvious until testing is considered, at which point it becomes the thing that unlocks automation; lightweight shell implementations are widely available.[537]

### Hardware description and simulation

Describing hardware separately from code is what makes a board change cheap: a device tree records that a serial port exists at a given address in a particular chip's memory map, and swapping a sensor or a board becomes a different overlay file rather than a change to the C.[622] That uniform description is machine-readable at ecosystem scale: with hundreds of platforms all describing which chip has how many serial ports and where they sit on the bus, simulation configurations can be generated automatically for all of them rather than written by hand.[691] From the software's point of view one serial peripheral is much like another — the registers and memory map differ but the behaviour does not — which is the argument for choosing hardware by what the application needs rather than mapping the application onto whatever was available.[547] A simulator can stand in for the board during development: the binary runs, the console output appears, and an interactive terminal is available, along with a log of every peripheral access.[519]

## Power consumption

An initialised but unused serial block is a real power cost: one design was drawing over 200 microamps through a peripheral that was not being used, recovered by de-initialising the block and removing its power.[661] Payload size on the link is a power decision too: replacing a 200-byte JSON packet with a 16-byte encoding cut hundreds of microamps from the same product.[661]

Clock gating and power gating are not the same option: the clock to a serial peripheral can be disabled to save dynamic power, but the block cannot be individually powered down, because defining a separate power region per peripheral costs placement density that would otherwise hold logic.[687] Coarser power modes exist around the peripheral: a mode that stops the clocks to everything except the serial port, and a dormant mode that stops all clocks until a pin changes, from which software resumes exactly where it stopped as though no time had passed.[687]

## System-level uses and failure modes

A 115,200 baud link is a small pipe, and forcing both operational data and debug data through it means one has to be sacrificed, usually the debugging.[584] The design response is not to widen the debug channel but to remove the distinction: rather than attaching JTAG and dumping data over serial during bring-up — acceptable for a product that will end up in a case on a shelf — the information is carried in the data stream the system already produces, because a launch vehicle cannot be probed in flight.[584]

Input validation on a serial stream can create the fault it was meant to prevent: a driver that discarded any byte above 127 as line noise crashed deployed units in one country, because the cell tower name being reported contained an accented character encoded above that threshold.[614]

### Bridging to other subsystems

A module carrying the whole protocol stack on board removes a porting problem: a small microcontroller with tens of kilobytes of flash cannot host a Bluetooth host stack, so a module that exposes the finished service over a serial link and takes data in and out is what makes the design possible at all.[155] The same pattern applies to adding connectivity generally: a second chip is placed alongside the main processor and spoken to over a serial link, which keeps the main firmware small and the vendor's stack at arm's length.[403]

## Test, debug and instrumentation

Serial is the production test interface: a jig at the end of the line sends a command, takes a measurement, sends another and takes another, producing a per-unit test report alongside programming and voltage checks.[544] The boot console is the standard entry point for examining a device that was not meant to be examined: connecting to a couple of pins and reading what the bootloader prints establishes what the system is.[536] That entry point has been closing: over about five years vendors stopped marking JTAG and serial test points, disabled the consoles and disabled JTAG, and the longer-term trajectory is a board with one or two pieces of silicon and no test points at all, where anything short of an attack on the silicon becomes very difficult.[346]

Debug access on a finished product is a physical operation: wires soldered to the JTAG header and to the serial pins, which break, leaving the engineer unsure whether they are debugging their code or their soldering.[537] A phone can serve as the console: a terminal application with a serial option, connected to the board over USB, gives an interactive shell for reading sensor output and issuing commands without a laptop, provided the target supports serial over its USB connection.[713] Instrument automation converges on the same interface: a parser that consumes serial output can drive any instrument whose interface ultimately resolves to a serial port, whatever the physical connection.[694]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ | |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 155 | An Interview with Jeff Rowberg - Mini Module Master | https://theamphour.com/the-amp-hour-155-mini-module-master/ | July 22, 2013 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 423 | Open FPGA Toolchains at 35c3 | https://theamphour.com/423-open-fpga-toolchains-at-35c3/ | January 1, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 478 | Optimization Beast | https://theamphour.com/478-optimization-beast/ | February 9, 2020 |
| 493 | PITA Package | https://theamphour.com/493-pita-package/ | May 17, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 519 | Simulating Embedded Hardware with Michael Gielda | https://theamphour.com/519-simulating-embedded-hardware-with-michael-gielda/ | November 29, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ | March 28, 2021 |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ | April 5, 2021 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 547 | Open Source Mindset with Michael Gielda | https://theamphour.com/547-open-source-mindset-with-michael-gielda/ | June 28, 2021 |
| 581 | Real Time Operating Systems with Brian Amos | https://theamphour.com/581-real-time-operating-systems-with-brian-amos/ | March 13, 2022 |
| 584 | Software for Rockets with Charles Aylward | https://theamphour.com/584-software-for-rockets-with-charles-aylward/ | April 3, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 622 | Building Firmware and Hardware for Trade Shows with Mike Szczys | https://theamphour.com/622-building-firmware-and-hardware-for-trade-shows-with-mike-szczys/ | March 5, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 691 | System Designer Lets You Try Every Part with Michael Gielda | https://theamphour.com/691-system-designer-lets-you-try-everything-with-michael-gielda/ | March 23, 2025 |
| 694 | Voltage, Vibes, and VOCs | https://theamphour.com/694-voltage-vibes-and-vocs/ | May 21, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
