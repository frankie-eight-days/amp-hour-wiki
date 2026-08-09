---
title: USB
concept: usb
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

USB (Universal Serial Bus) is a multi-drop serial bus that carries data and power between a host and peripheral devices over a standardised connector family.[595] It was released in 1996, with USB 1.0 running at 1.5 megabits per second and USB 1.1 at 12 megabits per second; USB 2 raised rates to 480 megabits per second, and later generations added gigabit-class signalling while remaining backwards compatible with the original two-wire interface.[595][467][668] The standard was developed by an international consortium rather than a single national body, which is why the same connector is found everywhere, in contrast to connector families that varied by country.[708] Beyond data, USB supplies power to attached devices, and convergence on USB as a common charging connector for mobile phones was achieved by legislation mandating it rather than by market pressure.[158][534]

## History

When USB was released in 1996, the interface chips were expensive and difficult for individuals to obtain, and using one meant adding a microcontroller and its software to a product; enumeration and the protocol stack are now built into commodity microcontrollers, some of which ship with a USB bootloader already programmed.[436] USB 1.0 ran at 1.5 megabits per second and USB 1.1 at 12 megabits per second; USB 2 raised this to rates comparable with FireWire.[595] Because USB is a multi-drop bus, the contemporaneous FireWire standard retained advantages in data synchronisation and sustained throughput even after USB matched it on headline rate.[595]

USB also displaced whole categories of equipment. Instruments whose content was a front end plus a converter, such as dynamic signal analysers, have largely been replaced by headless USB boxes, because the front panel, processor and display duplicate what the attached computer already provides.[168] Early USB-to-serial conversion was handled by fixed-function chips; development boards later replaced such chips with a microcontroller running an open-source USB stack, turning the interface into something reprogrammable through an on-board programming header at the cost of having to maintain firmware for it.[11]

Manufacturers formerly fitted proprietary connectors that combined USB with video and audio on a single shared interface; the practice has largely stopped, but it leaves equipment that cannot be connected without its original cable.[548]

## Signalling and protocol

A device's speed grade is signalled by pull-up and pull-down resistors on the data lines and is established when the host first sees the device, rather than being negotiated in software after defaulting to the slowest rate.[51] A low- or full-speed receiver decodes the differential pair into a small number of line states — the J and K states plus both-low, with both-high an error condition that should not occur — which is enough to implement the protocol without dedicated hardware.[467] High-speed USB at 480 megabits per second requires a true differential receiver and an external PHY, typically over a ULPI interface that deserialises the line into a parallel bus; it cannot be done on ordinary logic pins.[467] Implementing USB 3 requires gigabit serial transceivers with clock recovery, which is why at that speed dedicated hardware rather than fabric logic becomes necessary.[467] A USB 3 PHY that must also support USB 2 hosts carries the older ULPI interface alongside a 32-bit data bus, reaching seventy or eighty pins in total; backwards compatibility, not the new protocol, accounts for much of that pin count.[198]

Every layer of USB remains backwards compatible with the two-wire USB 2.0 signalling beneath it, with the additional capabilities negotiated at connection time; alternate modes and power delivery are layered on top of that base.[668] USB data pairs are routed to a differential impedance of about 90 ohms, distinct from the impedance targets of other high-speed interfaces on the same board.[668] USB signalling is pseudo-differential, swinging between zero and the supply rather than symmetrically about zero, so the crossover between the two lines is not exact; the resulting skew produces a common-mode spike at every transition, which is why common-mode chokes on USB pairs are an effective emissions measure.[645]

## Transfer model

USB offers four transfer types with different guarantees: control for basic device communication, interrupt for periodic small transfers such as a mouse, bulk for guaranteed delivery without guaranteed bandwidth as used by mass storage, and isochronous for dedicated bandwidth without retry.[527] Neither bulk nor isochronous gives both guaranteed bandwidth and guaranteed delivery, which is the combination a continuous instrument needs, and the bus was designed to move data cheaply and reliably, but not to move it reliably against a deadline.[527] Streaming over USB is workable in practice provided the design stays well below the bus's capacity and does not compete with other high-bandwidth devices on the same controller.[527]

## Power delivery

A USB 2 port supplies 500 milliamps, about two and a half watts, and ports on a machine typically share one controller, so a product that must work in any port has to be specified against that lowest common denominator rather than against a favourable case.[158] The original 500 milliamp limit was advisory rather than enforced: hosts supplied the current regardless, and requesting a smaller budget only mattered for leaving headroom for other devices; in practice designers wired devices to the 5 volt rail and ignored the negotiation, because policing it would have meant disconnecting devices.[340]

USB-C power negotiation begins with the source holding pull-ups on both CC lines; a voltage drop on one of them indicates both that a plug is present and which orientation it is in, after which 5 volts appears on VBUS, and a capable source then broadcasts its available voltage and current combinations, which the sink requests by index and the source grants.[340] A multi-port source must track its total input power against everything it has already promised, since granting every port its full allocation would require a supply many times the size of any single port's rating.[340] Drawing more than the default current from a USB-C source does not require a power delivery controller: a pull-down on the CC pin and a reading of that pin's voltage with an ordinary microcontroller analog input distinguishes the 500 milliamp, 1.5 amp and 3 amp advertisements, with full power delivery messaging needed only beyond that.[340]

Galvanic isolation is straightforward on USB-A, where the cable carries only ground, VBUS and the two data lines and VBUS is always present, and much harder on USB-C, where an ideal source holds VBUS at zero until a 5.1 kilohm pull-down on a CC pin signals an attached device and then superimposes digital messaging on that same line.[640] A digital isolator in the USB path, commonly a capacitive rather than optical part, is standard practice when debugging equipment at elevated potential, because otherwise the host computer's ground becomes the reference for whatever the equipment is connected to.[485] Connecting a mains-earthed USB host to equipment running from a floating supply creates a ground path through the USB cable, and the resulting problems appear even though the interface itself carries little power.[288]

### Power-related failure modes

Bulk decoupling capacitance downstream of a USB protection device draws an inrush at insertion that can trip the protection into overcurrent shutdown; the same fault has been observed with nothing plugged in, correlating with several hundred millivolts of noise on the 5 volt rail, indicating the protection chip can be triggered by supply noise as well as by real overcurrent.[408] A single-board computer's downstream USB ports may not supply enough current for two power-hungry peripherals such as Wi-Fi adapters, with the symptom appearing as unreliable operation rather than as an explicit power fault.[308] Development board conventions commonly bring USB 5 volts to the header through a series protection diode so that an attached board cannot back-power the host port; the consequences are that the nominal 5 volt pin sits nearer 4.4 volts and that the board cannot be powered from that pin.[600] A battery-powered design that works while plugged in and fails on battery may be depending on the host-supplied 5 volt rail for a peripheral, with the failure appearing as a firmware hang waiting for that peripheral rather than as a power fault.[623]

The USB core is a significant contributor to a system-on-module's idle power, enough that on one compute module it is left disabled in the default device tree and must be deliberately enabled.[548] An instrument powered only from a USB port and lacking a step-up converter is limited by the burden voltage drops in its own signal path: from a 5 volt input, the maximum usable output in its highest accuracy mode was 3.75 volts.[640] Powering a teaching platform entirely from a laptop's USB port removes the need for bench power and mains distribution, which is what allows laboratory work to leave the timetabled laboratory slot.[497] Commodity USB hubs omit per-port power monitoring and the ability to power-cycle or disconnect a downstream device, because a dollar of monitoring silicon is not viable in a five-dollar bill of materials; adding it lets a system identify the port whose current has jumped and disable it before the whole bus is brought down.[425]

## Hardware implementation

USB imposes a clock accuracy requirement that a free-running internal oscillator does not meet; some microcontrollers close the gap by trimming their internal oscillator against the synchronisation packets on the bus, an option not available on FPGAs, which therefore need an external crystal for a USB interface.[395] Handling USB communication is awkward on an FPGA and routine on a microcontroller with a built-in PHY, so designs that need both custom logic and a host connection commonly carry an FPGA and a microcontroller together.[588] The assumption that USB requires dedicated silicon, licensed as a hard core with its own PHY, is not absolute: on its device with an embedded FPGA but no USB hard core, QuickLogic drove the USB connector directly from FPGA fabric pins using a soft core.[525]

Low-speed USB can be bit-banged in software on a microcontroller with no USB peripheral by timing bus samples against the core clock, in one case reading or writing a bit every 53.3 cycles at 160 MHz.[637] A bit-banged implementation that computes the CRC and classifies the packet type inline as bits arrive can answer a host request with data immediately, where common stacks first send a negative acknowledgement, hand off to user code and reply on a later transaction.[637] The cost is that the processor is fully occupied during every frame it sends or receives, so the technique suits parts where a second core or a hardware peripheral is not available at the price.[637] Software USB on a ten-cent microcontroller changes what is worth building, since the alternatives with hardware USB were parts at roughly 70 cents to a dollar forty; the same vendor later offered a variant with hardware USB at around four times the price of the base part.[637]

### Board layout

High-speed USB and HDMI can be routed successfully on a two-layer board provided the connector is placed close to the controller; the short controlled length matters more than layer count.[219] USB 3 will refuse to negotiate a link if the signal pairs are broken out to test pads or branched at all, so the debugging convenience of accessible test points is unavailable at super-speed.[293] Inserting any instrument in series with a super-speed bus degrades the signalling unless the interposer includes a repeater.[527] A product operating at the limit of its link budget fails intermittently once an adapter and an internal ribbon cable are added in series, and works when connected directly; the fault is cumulative margin loss, not any single defective element.[597]

## Software stacks

Porting an existing USB stack to a new architecture is generally preferred over writing one, both because supporting the full set of device and host classes is a large undertaking and because a shared implementation means bug fixes flow in both directions between the teams using it.[212] Implementing USB properly in a small commercial product consumed months of engineering, working through device classes, descriptors, string descriptors and composite devices before any of the product's own functionality was exercised.[453] A vendor USB stack supplied under a licence that forbids redistributing the source forces an open project to strip that code out before publishing, breaking a one-click build for anyone trying to learn from the project; a community-contributed open stack replaced it and additionally offered features, such as double buffering, that the vendor library lacked.[125]

Microcontroller USB stacks are mature on the device side and thin on the host side: a common open stack handles keyboards, mice and some audio devices as a host, and supporting anything further means porting the equivalent Linux driver, which is why most microcontroller designs act as devices.[529] Programmable IO blocks that handle bit-level serial protocols reach their limit with USB, because the protocol's response deadlines leave no room for the software half of the split between hardware bit-banging and firmware processing.[529]

### Host interaction

A host assigns a new virtual serial port number to each newly seen USB device and the numbering increments and eventually wraps; in a manufacturing setting where many devices are plugged in successively, this behaviour is easy to bypass during test development and to be bitten by in production.[215] Host-side chipset defects have made whole classes of motherboards periodically reset every USB port, disconnecting and re-enumerating attached devices for seconds at a time, so a peripheral that appears to misbehave may be reacting to this.[546] Running a vendor toolchain inside a virtual machine and passing the USB device through to it is the common way to reconcile a toolchain that only supports one operating system with a host running another; the passthrough itself is reliable, and per-project virtual machines also preserve a working environment against later host changes.[510] Compatibility layers that run a Linux userspace inside another operating system generally handle files and terminals but historically could not reach the USB device, which is precisely what embedded work requires.[576] Browser-hosted development environments can compile and simulate but cannot reach a USB device on the user's desk, which is the boundary that keeps embedded work off fully cloud-hosted toolchains.[604]

## Device classes and applications

Unless a product needs the data rate, presenting it as a serial port over a USB-to-serial bridge is the better engineering choice, because a native USB device requires custom host software while a virtual serial port can be driven from any terminal program the customer already has.[551] Any microcontroller with a USB peripheral can be made into a USB-to-serial bridge in firmware, which sets a ceiling on what a dedicated bridge chip can be worth.[587] Some fixed-function USB-to-serial parts are ordinary microcontrollers from the same vendor's catalogue shipped with firmware programmed in, sold as a separate product with its own datasheet and support.[30]

Presenting a development board as a mass-storage device removes the toolchain from the edit-run loop entirely: the file is edited in any text editor and saved, and the board runs it.[383] Firmware update over USB has standard classes to build on — DFU for low-level updates and mass storage for file-level access — so a device can be updated without any host-side software specific to it.[467] A USB bootloader serves as the recovery path when a firmware update leaves a device unbootable, provided the bootloader itself is not what was overwritten.[250]

Emulating an Ethernet interface over USB lets a single cable supply power and a network connection to an embedded Linux board, which the host sees as a virtual network adapter it can address over the network stack it already has.[142] Presenting the board as a network device and serving a web page on it removes the need for terminal software or drivers on the host, at the cost of the connection being unfamiliar to users expecting a serial port.[378] Reading a device's console on a phone or tablet over a single USB-C cable requires the target to implement serial-over-USB itself; the convenience is a property of the target's firmware, not of the cable.[713]

## Use in instrumentation and test

A whole class of USB-connected instruments, including logic analysers and current measurement instruments, follows the architecture of shipping raw data to the host and doing all analysis there, in place of the embedded computer a traditional bench instrument contains.[527] The value of a host-connected instrument lies entirely in the conversion hardware between the physical signal and the bus; the bus itself contributes only a standard, universally available transport.[101]

On the HackRF One software-defined radio, Michael Ossmann designed around the maximum rate of high-speed USB as the instrument's primary limitation: a pair of eight-bit quadrature samples 20 million times per second saturates the link, giving 20 MHz of instantaneous bandwidth.[214] That ceiling proved a well-matched design point, because analog and digital parts capable of substantially more than 20 megasamples per second rise steeply in price, while the resulting bandwidth is many times what a low-cost tuner dongle provides.[214] With the host connection as the bottleneck, on-board signal processing could be omitted entirely: a small CPLD for glue logic and a microcontroller with a built-in high-speed USB interface are enough to get samples in and out, leaving the processing to the host.[214]

Commercial USB protocol analysers cost thousands of dollars and come with correspondingly complex software, and analysing USB 3 is substantially harder than USB 2, so most such instruments cover only up to high speed.[551] USB traffic can instead be captured with the operating system's own monitoring facilities and written out as a packet capture, including for a guest operating system running in a virtual machine, which avoids the cost of a hardware analyser.[318] An in-line analyser sits between host and device, passing traffic through while reading it, and a device that can also modify packets in transit becomes a fault-injection tool rather than only an observer.[551]

A USB port added for low-latency, interference-free communication also becomes the debugging and manufacturing-test interface, because it is the one connection every test computer already has and many units can be attached at once without contending for a shared channel.[279] Automated test racks that must exercise many target boards route each board's USB connection to a backplane and switch it through a matrix, so a single host can address any target under software control.[518]

## Security

The standard USB attack presents the device as a keyboard, or another human interface device, and types a stored script, so it requires no vulnerability at all: the host is behaving exactly as specified.[454] On his cable-implant work, Mike Grover fits the assembled boards inside the moulding of a USB-A plug on a sacrificed cable, so the visual inspection that distinguishes a suspect thumb drive from a normal one does not apply to cables.[454] A device that charges capacitors to a couple of hundred volts from the port's own 5 volt supply and discharges them into the data lines destroys the host, which argues against exposing USB ports on unattended public-facing equipment and for fast transient suppression on those that must exist.[315] Removable USB storage is the standard mechanism by which malware crosses an air gap into networks that have no external connection.[20]

Firmware that sends back a buffer over USB is a memory disclosure path: corrupting the length field can make the device continue reading past the buffer and return the firmware itself if the address map places it adjacently.[552] Emulating a hub and making devices appear and disappear at controlled moments is an established technique against host USB implementations, and its practicality depends on having development tools that allow the sequence to be iterated quickly.[442] A board with a USB device interface on each end, one facing a controlling computer and one facing a target host, allows the target's USB stack to be probed with arbitrary device behaviour; the technique has produced a large number of USB stack defects.[318]

## Connectors and cables

USB-A contacts slide past one another rather than being pins and sockets, so the connectors have no gender in the contact sense; nor does plug and receptacle distinguish them, since extension cables exist — what distinguishes them is shrouding.[708] USB-A persists in equipment such as label printers and older instruments precisely because its four-contact construction is mechanically robust and functionally sufficient.[554]

Physically identical USB-C cables differ in whether ground is bonded to the shield, whether they meet USB 2 or USB 3.2 signalling, and what identification resistor or marker chip they contain, so cable capability cannot be inferred from the connector and is worth testing.[668] Converging USB and Thunderbolt onto one connector was intended to reduce the number of cables in circulation but produced a set of visually indistinguishable variants supporting different combinations of USB, DisplayPort and Thunderbolt.[346] USB has accumulated capability rather than replacing it: a current design must support the ubiquitous legacy USB 2 behaviour, the newer high-speed modes, and the additional dimension that USB-C and its alternate modes introduce, and choosing wrongly among those options constrains or kills a product.[421] Some USB-C multiplexer and charging controllers are not sold through distribution at all and the manufacturer will not supply them to third parties, so the parts that select between USB 2, USB 3, DisplayPort and charging on a given port cannot be obtained for repair.[507]

A single universal connector is impossible rather than merely unachieved: current-carrying capacity rules USB out for vehicle charging and its lack of controlled high-frequency impedance rules it out for antenna connections, so multiple connector families remain necessary.[708]

## Application domains

USB is a poor choice for sensor connections on mobile robots, where connector retention, sealing and cable robustness matter; power over Ethernet is preferred there, while USB remains well suited to automated test of embedded electronics.[425] Modules intended for robotics are offered in variants that replace the USB host connection with self-booting from on-board flash or with power over Ethernet, because the mechanical and serviceability properties of the interface, not its bandwidth, decide the choice.[517]

Peripheral combinations, not headline performance, often decide microcontroller selection: requiring Ethernet and high-speed USB on the same die eliminated most of the available high-end Cortex-M7 parts, leaving a choice between one part with extensive errata and one other family.[640] Single-board computers have used one hub part with an internal port tied to an on-die Ethernet controller to provide both networking and multiple external USB ports; depopulating that part and linking the processor's USB straight to a single connector produces a cheaper, lower-power variant of the same board from the same bare PCB.[97]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 11 | Ardui...no Dave This Week? | https://theamphour.com/the-amp-hour-11-ardui-no-dave-this-week/ | |
| 20 | Military Electronics and The Free Eagle (Freagle) Campaign | https://theamphour.com/the-amp-hour-20-military-electronics-and-our-first-wotws/ | |
| 30 | Agilent, Analog, Cold Fusion - Funding Fusion Is Not Futile | https://theamphour.com/the-amp-hour-30-funding-fusion-is-not-futile/ | |
| 51 | Vafrous Video Vaniloquence | https://theamphour.com/the-amp-hour-51-vafrous-video-vaniloquence/ | |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ | |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 142 | Kickstarter, IndieGoGo & Ignite - Jasperated Jimswinger Jobbery | https://theamphour.com/the-amp-hour-142-jasperated-jimswinger-jobbery/ | April 22, 2013 |
| 158 | Hyperloop, Upverter and Soldering - Unbelievable USB Ustulater | https://theamphour.com/the-amp-hour-158-unbelievable-usb-ustulater/ | August 12, 2013 |
| 168 | Specialized and/or Open Source Test Gear and Dev Boards - Vacation Videography Vorboten | https://theamphour.com/168-specialized-and-open-source-test-gear-and-dev-boards-vacation-videography-vorboten/ | October 21, 2013 |
| 198 | Mike Ossmann Returns! - Planetic Portalab Packaging | https://theamphour.com/198-mike-ossmann-returns-planetic-portalab-packaging/ | May 12, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 215 | Wrong Hardware, Wrong Software - Fugacious Fan Funding | https://theamphour.com/215-wrong-hardware-wrong-software-fugacious-fan-funding/ | September 7, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20, 2015 |
| 279 | Merry Keyzermas! | https://theamphour.com/279-merry-keyzermas/ | December 22, 2015 |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ | February 24, 2016 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 383 | An Interview with Scott Shawcroft | https://theamphour.com/383-an-interview-with-scott-shawcroft/ | March 11, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 425 | An Interview with Chris Osterwood | https://theamphour.com/425-an-interview-with-chris-osterwood/ | January 13, 2019 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 453 | Vertically Integrated Design Engineering | https://theamphour.com/453-vertically-integrated-design-engineering/ | August 4, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 497 | An Interview with Brock LaMeres | https://theamphour.com/497-an-interview-with-brock-lameres/ | June 21, 2020 |
| 507 | Right To Repair with Louis Rossmann | https://theamphour.com/the-amp-hour-507-right-to-repair-with-louis-rossmann/ | |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 529 | Embedded Hardware with the Raspberry Pi Team | https://theamphour.com/529-embedded-hardware-with-the-raspberry-pi-team/ | February 7, 2021 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 548 | The Last Line of Defense | https://theamphour.com/548-the-last-line-of-defense/ | July 5, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 552 | Shouting at chips with Colin O'Flynn | https://theamphour.com/552-shouting-at-chips-with-colin-oflynn/ | August 1, 2021 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 576 | A literal trainwreck | https://theamphour.com/576-a-literal-trainwreck/ | February 6, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 588 | Siloed Engineering with Leigh Brady | https://theamphour.com/588-siloed-engineering-with-leigh-brady/ | May 8, 2022 |
| 595 | Trade Show or Conference? | https://theamphour.com/595-trade-show-or-conference/ | July 10, 2022 |
| 597 | Wow, Dave REALLY likes Top Gun | https://theamphour.com/597-wow-dave-really-likes-top-gun/ | July 24, 2022 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 623 | Artisanal Crystals | https://theamphour.com/623-artisanal-crystals/ | March 12, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 668 | 50.0000 Ohms | https://theamphour.com/668-50-0000-ohms/ | May 30, 2024 |
| 708 | All the Connectors with Davide Andrea | https://theamphour.com/708-all-the-connectors-with-davide-andrea/ | November 1, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
