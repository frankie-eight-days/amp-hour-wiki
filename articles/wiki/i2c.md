---
title: I2C
concept: i2c
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

I2C (inter-integrated circuit) is a two-wire synchronous serial bus for communication between integrated circuits on a board.[396] It was developed by Philips, originally to interconnect the many chips inside analogue television sets, and uses open-drain drivers with external pull-up resistors on its two lines, SDA and SCL.[631][319][274] Its combination of a two-pin footprint, multi-device addressing, and simple register-oriented peripherals has made it the standard interconnect for sensors and other low-speed devices in embedded systems.[202][315]

## History and licensing

Philips created I2C for its analogue television sets, in which it supplied a separate chip for each function — tuner, filter, CRT driver, on-screen display — and needed a standard protocol to join dozens of its own chips together in place of large multi-gang mechanical switches.[631] The bus was originally specified with an 8-bit address field on the assumption that 256 devices, all of them Philips parts, would be ample.[396] Once other manufacturers adopted the bus, the original address space was exhausted; a 10-bit addressing mode was added, that too ran short, and many parts on the market ended up sharing addresses.[396]

The I2C name and logo were trademarked by Philips: implementers had to submit a device for evaluation to be granted use of the logo, and licensing terms attached to the name.[396] Since 10 October 2006 no licensing fee is required to implement I2C, but a slave address allocated by NXP still is.[396] Vendors that do not want to use the trademarked name label an electrically identical interface as a two-wire interface, or TWI.[631]

I3C is the successor standard to I2C, developed under the MIPI Alliance rather than by a single vendor, and reaches 33 Mbit/s in its ternary signalling mode.[631] PMBus, used for power-management devices, is electrically and protocol-wise essentially I2C, and firmware can be pushed to power-management parts over it.[566]

## Electrical characteristics

I2C outputs are open-collector: devices can only pull the line low, and the line is returned high by an external pull-up resistor.[274] Ordinary digital outputs such as SPI use totem-pole drivers with one transistor pulling high and one pulling low, so they need no pull-up.[274] Because the low side is driven by a transistor and the high side only by a resistor, an I2C edge is asymmetric on an oscilloscope: the falling edge is nearly instantaneous while the rising edge follows an RC curve.[274]

### Pull-up sizing and bus capacitance

The Philips standard gives 2.2 kilohms as the nominal reference pull-up value.[396] A pair of 4.7-kilohm resistors on two adjacent lines is a recognisable signature of an I2C bus when inspecting an assembled board.[561] Longer lines and higher bus capacitance call for a lower pull-up value, because a lower resistance sources more current into the node and charges the line capacitance faster, restoring a sharp rising edge.[396] If bus capacitance is high enough that the pull-up cannot charge the line in time, the rising edge degrades and the bus stops working.[396] The speed limit of an I2C bus is set by the RC time constant formed by the pull-up resistor and the bus capacitance, which limits the slew rate of the rising edge.[631]

Breadboards and flying wires add capacitance and act as an antenna, which is unfavourable for an I2C line and argues for a lower pull-up value than a compact board would need.[274] A wrongly chosen pull-up value is a common root cause of I2C failures; values in the 5-to-10-kilohm range can be too high for a breadboarded bus.[274] For a short link across a board — updating a register in a real-time clock, or reading a temperature sensor at the other end — a pull-up at either end and, if the signal looks marginal, a reduced clock rate is sufficient.[631] At a few megahertz over a couple of inches on a board with a common ground, I2C is electrically undemanding; digital communication only turns into an analogue signal-corruption problem at high data rates and longer distances.[704]

The bus is easily disturbed, so sharing the SDA and SCL pins of a board with other functions invites failures; separating them onto dedicated lines is the fix.[396] Pull-ups are also a liability in low-power designs: a pull-up to VCC draws current whenever a device holds the line low or is powered down, and can back-power a powered-down section through the resistor, so an I2C bus in a low-power product has to be powered off entirely or left with every device in a low-power state.[527]

## Addressing and protocol

A slave acknowledges by pulling the data line low after its address is transmitted, signalling that the addressed device is present and ready for further bytes.[396] The classic I2C failure signature is a NACK: the master transmits an address and receives no acknowledge, then retries the same address indefinitely — a condition visible only once the bus is decoded, not from the shape of the waveform.[396]

Address collisions are a hard limit on how many identical parts can share one bus; where a part offers no address-strapping option, an I2C multiplexer or switch chip is required.[631] Wii Nunchuk peripherals, for example, communicate over plain I2C but are all hard-coded to the same address, because the Wiimote is the master and only one accessory can be plugged in at a time; reading several from one host requires a switch chip that selects between them.[167]

Variants within a sensor family commonly differ only in their I2C bus speed or device address, differences that a hardware abstraction layer can hide until they cause a silent failure.[330] On microcontrollers with more than one I2C peripheral, the alternate instance is mapped to different pins, so selecting I2C1 versus I2C2 in firmware changes which physical pins the bus appears on — a configuration error that presents as a dead bus.[623] Because the bus is open-drain and any device may pull a line low, an attacker with bus access can corrupt the address phase and impersonate a peripheral, after which the genuine peripheral no longer replies.[318]

## Comparison with SPI

SPI is the more robust of the two buses: its totem-pole drivers avoid the pull-up sizing, line-capacitance and interference problems that afflict I2C.[274] Where SPI is faster, I2C is the more widely available interface across parts, which in practice decides the choice for many designs.[315] I2C has more to go wrong than SPI, but the slave side of an I2C device is simple — essentially a set of registers hanging off the bus.[396] Because the interfaces are often offered as siblings in the same footprint, ordering by footprint alone can substitute an SPI part for its I2C counterpart: the board assembles, and the error only appears when the device fails to enumerate on the I2C bus.[652]

## Implementation

Bit-banging an I2C master in software is straightforward; implementing an I2C slave in software is substantially harder.[524] Before microcontrollers carried hardware I2C peripherals, designers wrote their own I2C libraries in software.[396] An implementation does not have to cover every mode in the specification; a minimal implementation sufficient to talk to the specific chip is far less work than a general-purpose reusable one.[137]

A typical I2C sensor contains no processor: a state machine listens for its address, fetches the requested value from memory and places it on the bus.[622] Presenting a subsystem as an I2C peripheral — a display module that accepts a register-and-payload command set exactly as a sensor would — makes it usable unchanged from any host framework and conserves pins on the controller.[622]

Some parts impose quirks. The RP2040's Pico SDK I2C driver responds to only one address in device mode; supporting multiple addresses requires a PIO implementation, using the chip's programmable state machines to listen on the bus — a task for which the PIO blocks are well matched, since the state machine can continuously service incoming messages while the processor handles only decoded commands.[622][648] A microcontroller may implement I2C in software even when the peripheral pins appear fixed, so the same bus can be instantiated on other pins; this has been observed on the ESP32.[396] The Intel Galileo used I2C to emulate Arduino I/O behind its x86 core, and the resulting I/O was very slow.[490]

In driver frameworks, I2C devices are described declaratively: hardware description languages such as Zephyr's devicetree record a device's bus instance, address and driver, so swapping a sensor for a different part on the same bus becomes an overlay-file change with no alteration to application code.[622] In Linux, a peripheral fails silently when the driver is not bound to the right I2C address, and diagnosing it means reading kernel source rather than writing code.[515] Even inside a driver framework, a raw I2C read or write remains available as an escape hatch for working around a subsystem abstraction, while still benefiting from the framework's power management.[653]

## Failure modes and diagnosis

A single mis-wired pin takes down the whole bus and every sensor on it, producing error messages that do not point at the wiring.[657] Noise on the lines caused by a poor soldering job can present as intermittent protocol misbehaviour — stray stops and restarts — and prompt elaborate firmware workarounds that turn out to be unnecessary once the joint is fixed; checking the soldering is worth doing before redesigning the protocol.[622]

The recommended order for diagnosing a dead I2C link is: probe the lines with a scope to confirm the pull-up behaviour and clean edges; then check that the device is being addressed and enabled; then question the protocol layer and the provenance of the library.[274] Confirming on a scope that a waveform looks like valid I2C traffic does not confirm the transaction succeeded; only decoding the bus with a logic analyser shows whether the slave acknowledged.[396] A logic analyser or scope with an I2C protocol decoder converts the waveform directly into addresses and bytes and is the fastest route to a bus fault.[274] On a multi-microcontroller bus, such a protocol analyser can resolve a communication fault in minutes where inspection had failed over a longer period.[54] Deep-memory logic analysers sidestep the need to trigger on a specific I2C packet: record continuously for as long as needed to guarantee capture, then search the recording for the packet in software, converting a real-time trigger problem into an offline search problem.[237]

Combining a captured I2C trace with the target's register map reconstructs each transaction as a named read or write to a named register with decoded bit fields, turning a binary stream into a readable account of the device's behaviour, and lets the sequence be replayed from another host.[155] Vendors have shipped I2C sensors without publishing a register map, leaving integrators to determine the register set experimentally.[155]

Bench bring-up can be done without target firmware. Linux board bring-up can validate an I2C bus from the command line with utilities that probe the bus, and GPIO through sysfs, before any driver code is written.[378] Zephyr provides shell commands for bus-level work, including an I2C scan and direct sensor access, compiled in behind a build symbol and reachable over UART or RTT.[696] A USB host adapter for I2C and SPI reduces bench bring-up of a bus device to configuring the clock frequency, entering the slave address and payload, and reading back the response.[461]

## Ecosystem and applications

Because I2C needs only two lines, it fits a microcontroller whose pins are otherwise fully allocated, where a directly driven parallel LCD would not.[74] A shared bus lets a dozen sensors hang off two pins, making it the standard answer for pin-starved devices, and an I2C I/O expander extends the same trick to general-purpose I/O.[202] Buses of several dozen microcontrollers on a single segment are built in practice; one system carried around 45 microcontrollers communicating over I2C.[54]

Bringing the I2C bus out to a header is a cheap design allowance that lets external sensors be added later without a board respin.[232] Peripherals connected off-board through ordinary 0.1-inch headers are workable precisely because interfaces such as I2C run far below the tens-of-megahertz region where connector parasitics start to matter.[181] Small four-pin I2C-only cabled sensor connector systems exist, of which Qwiic is one; Grove uses a similar connector but carries interfaces other than I2C on it.[458] Four-pin sensor-cable standards omit the interrupt pin that many of the sensors provide, so interrupt-driven features are unreachable; using them fully needs a five- or six-conductor cable for which no standard exists.[602] The Def Con badge add-on convention standardises on a four-pin header carrying power, ground, SDA and SCL, so arbitrary add-on boards can be plugged into arbitrary badges.[396] Development-board form factors such as Adafruit's Feather fix the I2C signals to specific header pins regardless of which microcontroller is fitted, so add-on boards remain interchangeable across processors.[396]

I2C also appears inside larger systems. The VGA connector on a standard x86 server carries EDID, which is an I2C bus, plus power — an exposed, externally accessible I2C attack surface into the machine.[418] Because a single physical connector can carry both a PCIe lane and an I2C bus, management firmware needs an explicit description of that mapping to know which sensors and devices sit behind which connector when tracing faults to a component.[357] A parallel-output image sensor typically splits its interfaces: pixel data leaves on a clocked parallel bus with line-valid and frame-valid strobes, while all configuration — crop, output bit width, timings — is written over a separate I2C interface.[473] An I2C DAC producing 0 to 4.96 volts, followed by a high-current op-amp that scales and shifts the output to plus and minus eight volts, forms a compact programmable supply channel.[689]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 54 | An Interview with Jack Ganssle - Embedded Elchee Epexegesis | https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/ | |
| 74 | Younker Youtube Yarling | https://theamphour.com/the-amp-hour-74-younker-youtube-yarling/ | |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 155 | An Interview with Jeff Rowberg - Mini Module Master | https://theamphour.com/the-amp-hour-155-mini-module-master/ | July 22, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ | |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 357 | An Interview with Rick Altherr | https://theamphour.com/357-an-interview-with-rick-altherr/ | August 28, 2017 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 396 | The Synergy Bus | https://theamphour.com/396-the-synergy-bus/ | June 10, 2018 |
| 418 | An Interview with Josh Datko | https://theamphour.com/418-an-interview-with-josh-datko/ | December 2, 2018 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ | October 6, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 566 | Switching Converter Engineering with Carmen Parisi | https://theamphour.com/566-switching-converter-engineering-with-carmen-parisi/ | November 14, 2021 |
| 602 | Rigorous engineering stuff may be out the window | https://theamphour.com/602-rigorous-engineering-stuff-may-be-out-the-window/ | September 11, 2022 |
| 622 | Building Firmware and Hardware for Trade Shows with Mike Szczys | https://theamphour.com/622-building-firmware-and-hardware-for-trade-shows-with-mike-szczys/ | March 5, 2023 |
| 623 | Artisanal Crystals | https://theamphour.com/623-artisanal-crystals/ | March 12, 2023 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 653 | Benjamin Cabé Nose Zephyr | https://theamphour.com/653-benjamin-cabe-nose-zephyr/ | December 11, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
| 696 | It Works With Option Number 5 | https://theamphour.com/696-it-works-with-option-number-5/ | June 18, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
