---
title: SPI
concept: spi
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

SPI is a clocked serial interface whose transfers depend on the configured clock frequency, clock polarity, clock phase, and use of a slave-select signal.[348][461] Separate data lines carry information between a host and peripheral, while multiple peripherals can share one bus and be selected individually with chip-select lines.[201][203] Its directly driven electrical outputs distinguish it from I2C, although the resulting requirement for additional pins is a central design trade-off.[235][274] The abbreviation is pronounced either as three separate letters or as a single word.[274]

## Electrical characteristics

Every SPI line is a totem-pole output containing two transistors, one driving the line high and the other driving it low.[274] I2C instead uses an open-collector-style output in which the line returns high through a pull-up resistor.[274] SPI therefore does not require pull-up resistors and avoids the failure modes created by selecting an unsuitable pull-up value.[274]

The difference is visible on an oscilloscope: an I2C line falls almost immediately when a transistor pulls it low, while its rising edge is shaped by the pull-up resistor charging the line capacitance.[274] Breadboards and loose wiring introduce additional capacitance and act as antennas, forcing an I2C pull-up to charge that capacitance and sometimes requiring a lower-value resistor; a directly driven SPI line is not affected in the same way.[274]

SPI selects a peripheral with a dedicated line rather than through device-addressing transactions.[203][274] This removes the addressing-related failure class associated with I2C, but SPI requires more signal lines for an equivalent connection.[235][274] With supply voltage largely standardized, the substantive peripheral-interface decision is often between SPI and I2C, and the wider availability of I2C variants can determine the choice.[315]

## Configuration and failure modes

Before a transfer can operate correctly, the clock frequency, clock polarity and phase, and use of slave select must be established.[461] Incorrect polarity or phase is a characteristic bring-up failure because the bus can return plausible but meaningless data rather than an obvious error.[137] One such fault consumed three days of debugging before the operating mode was checked.[137]

A reversed clock-polarity setting can shift returned data by one bit, and the setting may not be reconsidered once initial communication appears possible.[645] In one project, that failure consumed two or three weeks before the polarity difference was identified.[645]

Transposing the MOSI and MISO data lines is another recurring board-layout error.[201] On one board, the error was corrected without cutting traces because every digital connection had been routed through solder-bridge jumpers.[201]

Bus variants can also share a footprint. An I2C real-time clock and an SPI real-time clock from the same family had identical pin assignments, allowing the wrong variant to pass footprint checks and assemble correctly before the system-level bus fault appeared.[652] The error originated when a component-library service returned the nearest available footprint together with a manufacturer part number, and that number was accepted without confirming that it represented the intended bus variant.[652]

An incorrect word length can fail silently: one SPI display did not operate because its peripheral remained configured for four-bit transfers.[479] More generally, an SPI peripheral cannot report that it expected a different mode or command state, so a system may produce no visible result until every setting is correct.[479]

Display controllers illustrate the scale of possible initialization work. One controller required approximately 400 commands over SPI and was documented by a 400-page data sheet, making adaptation of a known-good published driver more practical than developing the sequence solely from the data sheet.[479] Conversely, documentation that identifies the display pins, names the required library, and gives an operating procedure can be sufficient to bring up an unfamiliar SPI display without additional reference material.[330]

## Performance and signal integrity

Practical SPI clock rates commonly range from approximately 20 to 80 MHz.[463] During a read, the responding device has roughly half a clock cycle to prepare its result: the data must be available after the rising edge carrying the final address bit and present on the output by the following falling clock edge.[463]

Above approximately 10 MHz, capacitance, inductance, and edge rates must be considered because the connection can no longer be treated as a simple direct-current path.[252] A common hobbyist workaround for a bus that fails at 16 MHz is to reduce the clock to 2 MHz until communication works; this avoids the signal-integrity problem rather than diagnosing it.[252]

SPI cannot always replace a parallel interface. Reformatting parallel data arriving at 12.5 MHz into a single SPI stream would require a serial clock eight times as fast, a rate that was not achievable in one design.[412] Parallel interfaces driven by direct memory access also provide substantially more display bandwidth than SPI.[356]

A 2.8-inch colour TFT driven over SPI by a 16 MHz processor was sufficiently slow that it was moved to a parallel connection.[281] For larger or more frequently updated displays, the frame must be held in memory and then transmitted across the bus, and the resulting data rate can rule out the slow, low-power processor that a design might otherwise use.[702]

Memory-in-pixel displays are an exception to controller-based display architecture: the host communicates by SPI directly with the glass, supporting partial refreshes and a variable update rate ranging from once per second to approximately 25 or 30 frames per second.[175] SPI has also been used to stream video into an FPGA at 30 MHz, although that application required patches to an open-source synthesis toolchain to obtain finer control over logic merging; the patches were subsequently merged upstream.[423]

## Sharing buses and managing pins

Several SPI devices commonly share one clock and pair of data lines, with chip-select signals identifying the active device.[203] Consecutive block reads allow the host to stream multiple bytes from each selected device at high rate.[203]

The same architecture generalizes to on-chip systems: independent blocks can share a tri-state bus when each has an active select line and presents high-impedance inputs and outputs while unselected.[616] That arrangement allows independent designs to be combined on one chip without all blocks driving the bus simultaneously.[616]

A hardware SPI peripheral shifts data from a register without processor intervention, whereas bit-banging requires software to generate the interface timing directly.[378] Programmable logic can extend this capability: a CPLD converted SPI packets from a microcontroller into the parallel shift-register interface required by an LED panel, allowing the panel to be driven by a DMA transfer while the processor performed other work.[340]

An SPI peripheral can also be repurposed as a timed bit generator. In one design, an infrared-remote waveform normally produced by manipulating pin states and delays was encoded as an SPI packet and clocked out by the peripheral, avoiding processor blocking and the timing variability of an interpreted language.[202]

The number of pins available on a module constrains which interfaces it can expose. An SD-card form factor limited one design to six input-output pins, while later soldered-down modules provided 12 and then 23 pins.[202] Some microcontroller families allow nearly any peripheral to be routed to nearly any pin, allowing pin functions to be shared and one peripheral to clock another.[224] Mike Harrison used this arrangement to clock LED-driver logic from an SPI port and, where four SPI ports were needed but never simultaneously, remapped a single port between pin pairs to drive each output in turn.[224]

The same routing flexibility permits a UART and an SPI device to share a pin by switching the pin between operating modes, although that practice is considered inadvisable.[378]

### FPGA connections

After an FPGA completes configuration, the pins used to read its SPI configuration flash can be transferred to the user design.[395] A straightforward reuse method is to place another SPI device on the same bus with its own chip select; the pins can also be shared with another bus or indicator outputs if no conflict occurs during boot.[395]

An FPGA containing a hard SPI peripheral can be controlled by an external microcontroller over that bus, dividing control and programmable-logic functions between the two devices.[395] Where a package is designed for high-density interconnect with filled and plated via-in-pad construction, SPI programming pins buried inside the footprint can be reached by routing across unused pads and covering them with solder mask, avoiding the prototype cost of the full process.[395]

## System applications

### Displays and addressable LEDs

SPI is commonly used for displays, but its bandwidth limits make parallel connections preferable where large frames must be transferred rapidly.[281][356] A memory-in-pixel panel can instead retain image data at the pixel and receive direct SPI updates, reducing the need for continuous full-frame refreshes.[175]

Among addressable-LED protocols, the two-wire SPI-controlled APA102 is easier to drive than a one-wire device and adds approximately five bits of global brightness control, although using that control slows the effective pulse-width modulation.[412] The APA102 is not constant-current, so reducing its supply from 4.5 to 4 volts changes its light output, a consideration when an entire installation is dimmed together.[412]

### Data conversion and storage

An extended interface marketed as multi-SPI adds two or four data lines and samples on both clock edges, forming a hybrid of serial and parallel transfer.[348] It reduces the clock rate needed to read a 20-bit successive-approximation converter at several megasamples per second.[348] Such extensions address the constraint that a precision converter may complete its conversion internally but still have to shift the result out serially; at 20 bits and megasample rates, that read-out becomes the limiting operation.[348]

SD cards support both the full SD input-output interface, which uses additional data lines, and a slower SPI mode.[356] In a layered software stack, the file system sits above the card interface, and the card is reached through four SPI pins; broad SPI support makes that layering portable across systems.[514]

### Networking and sensor systems

A module that terminates a network stack in hardware can reduce the host’s task to issuing SPI commands, with addressing, protocol processing, and even web-server functions handled on the module.[79] Network connectivity can also be routed through an SPI-attached interface on a single-board computer by changing one line of kernel configuration in place of the normal Ethernet device.[319]

The number of available buses is a practical criterion when selecting a single-board computer, and one widely used platform provides a single SPI bus.[235] Where several peripherals must be attached to that bus, an external CPLD can multiplex the signals.[225]

A vision module can expose results over SPI as a text stream at approximately 30 updates per second, allowing a small microcontroller to consume output produced by a much more capable processor.[517] In programmable signal generation, a microcontroller sends SPI commands to a direct-digital-synthesis device, which then generates frequencies from direct current up to its specified upper limit.[554]

The quality of a microcontroller’s SPI implementation can affect systems beyond ordinary bus communication. In one radio design, transmitting packets from a low-cost part produced poorly formed transmissions, while a higher-performance part in the same family achieved approximately 800 metres and more than one kilometre when overvolted.[667]

### Security

A secure controller can read an external SPI flash, validate its contents, and then emulate the flash to the protected system.[693] This closes a substitution attack in which a validated image is replaced after checking but before use.[693] The attack is possible when the validating system lacks enough memory to retain the complete image and must reload it from flash after validation.[693]

## Implementation and software practice

Peripheral blocks can be instantiated from pre-built components in a custom-chip design flow, making the addition of two SPI modules a matter of minutes.[137] Software-defined peripherals remove the need to commit a chip to one fixed peripheral mix: a small processor attached to each input-output pin can implement I2C, SPI, or CAN according to the software loaded into it.[501]

A small processing block can also monitor an SPI or other serial bus for a selected pattern, raise an interrupt, and place results in memory for the main processor, moving real-time observation away from that processor.[501] Writing SPI driver calls against a real-time operating system’s abstraction allows protocol modules built on those calls to move into that operating system unchanged.[522]

Consistent peripheral behaviour within a single vendor’s microcontroller ecosystem reduces development time because experience with the interface transfers across that family, although the same knowledge does not necessarily transfer to another vendor.[383] A vendor library can reduce a transfer to sending a byte, but using such a library requires deciding how much of its operation to trust.[186]

## Bring-up and instrumentation

A host-controlled adapter can issue individual SPI commands and provide a bridge between a general-purpose computer and a device under test.[230] Such adapters allow scripts to operate SPI, I2C, or JTAG buses and are used to test protocols and commands against unfamiliar hardware quickly.[230][442]

A modern adapter can reduce bring-up to connecting the device, configuring frequency, polarity, phase, and slave select through a graphical interface, entering bytes in hexadecimal or decimal, and reading the returned data.[461] Exercising a new chip in this way produces command sequences and driver code already proven against the silicon, giving firmware development a working starting point.[110]

A working board from an earlier project can also drive a new device through the same interface after unnecessary code has been removed and only the bus driver retained.[110] The drawback of that approach is that reuse of an established platform can discourage migration to newer devices.[110]

Protocol analysers do not remove the need to configure the bus correctly: software timeout settings must be appropriate or captured data will not decode meaningfully.[391] High-rate instruments can stream samples to a host and perform analysis in software; a 100 MHz SPI bus can be recorded over USB 3.0, while software triggering is practical for a 10 MHz waveform sampled at approximately 100 megasamples per second.[237]

This design approach records the available traffic and searches it afterward, converting a real-time triggering problem into an offline search problem.[237] Instantiating separate UART, SPI, and I2C blocks for every pin of an FPGA-based protocol analyser consumes substantial programmable-logic area, although minimizing area is not necessarily the correct objective for someone learning hardware-description languages.[318]

The required depth of protocol knowledge depends on the work being performed: embedded engineering can require analysis of raw SPI or I2C signal traces, while constructing an installation from published libraries may not.[276] Chip vendors standardize demonstration hardware on common development platforms so that SPI-connected evaluation boards do not require a different demonstration system for every part.[230]

## References

| Episode | Title | URL | Date |
|---:|---|---|---|
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 110 | Armstrong, Camenzind & Museums - Outstanding Oneirophoros Obituaries | https://theamphour.com/the-amp-hour-110-outstanding-oneirophoros-obituaries/ | August 26, 2012 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 186 | Someone is watching...we think - Horme Hostility Hypochondriac | https://theamphour.com/186-someone-is-watching-we-think-horme-hostility-hypochondriac/ | February 25, 2014 |
| 201 | Cheap Respins And A Time Machine - Multiscience Mercenary Marketplace | https://theamphour.com/201-cheap-respins-and-a-time-machine-multiscience-mercenary-marketplace/ | June 2, 2014 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 203 | Tesla, Checklists and Bullies - Emerging External Eupsychics | https://theamphour.com/203-tesla-checklists-and-bullies-emerging-external-eupsychics/ | June 16, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 225 | Worktrips and Workspaces - Junket Jactation Jiltedness | https://theamphour.com/225-worktrips-and-workspaces-junket-jactation-jiltedness/ | November 25, 2014 |
| 230 | Prepping For Hoverboards - Gallionic GitHub Gabble | https://theamphour.com/230-prepping-for-hoverboards-gallionic-github-gabble/ | December 30, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 276 | Eating An Elephant | https://theamphour.com/276-eating-an-elephant/ | December 2, 2015 |
| 281 | Crossovers and Call-ins | https://theamphour.com/281-crossovers-and-call-ins/ | January 6, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ |  |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 423 | Open FPGA Toolchains at 35c3 | https://theamphour.com/423-open-fpga-toolchains-at-35c3/ | January 1, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ | October 6, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 479 | Why isn't this working? | https://theamphour.com/479-why-isnt-this-working/ | February 13, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 514 | Focus, Dammit | https://theamphour.com/514-focus-dammit/ | October 25, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 693 | Small Scale Electronics Manufacturing with Colin O'Flynn | https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/ | May 13, 2025 |
| 702 | Test Point Accupuncture | https://theamphour.com/702-test-point-accupuncture/ | September 14, 2025 |
