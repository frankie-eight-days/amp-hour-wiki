---
title: CAN Bus
concept: can-bus
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**CAN bus** (Controller Area Network) is a differential, multi-drop serial bus developed by Bosch in 1985 as a multiplex network to replace the ever-growing bundles of individually wired signals in vehicles with a single twisted pair.[388][634] It became effectively universal in road vehicles only after being mandated at the diagnostic connector from around 2009.[388] Classic CAN tops out at about one megabit per second, with faster derivatives and companion buses extending the family where higher throughput is needed.[93][388] The bus is defined by arbitration and error handling built into its physical and data-link layers, giving it collision-free contention resolution and atomic frame delivery that higher-level systems come to depend on.[93][634]

## History

CAN was created at Bosch in 1985 to address the problem of the vehicle wiring harness growing without bound: as features multiplied, each new signal added discrete wires, and the design intent was a multiplex bus in which one twisted pair replaced bundles of PWM- or analogue-encoded signal lines.[634] The Bosch team began from a conventional RS-485-style multi-drop bus with an addressing scheme, and moved arbitration into hardware only after discovering that resolving contention in software consumed too much CPU time.[634]

Before CAN consolidated the market, the SAE automotive bus in the United States was an umbrella label covering incompatible manufacturer-specific implementations from Ford, General Motors and Chrysler that happened to share a bit rate but were not interoperable.[93] Those proprietary variants required standalone licensed interface chips implementing both the physical layer and the MAC, whereas CAN attracted broad support from silicon vendors, and that difference in chip economics drove CAN's displacement of the manufacturer buses through the mid-2000s.[93] Universal presence at the vehicle diagnostic connector arrived later still, through a mandate taking effect around 2009.[388]

The bandwidth ceiling of classic CAN motivated companion standards. FlexRay, at roughly ten megabits per second, and the optical MOST bus exist alongside CAN for applications its rate cannot serve.[93][388] At the low end, LIN emerged from a Volvo platform's need for something cheaper than CAN for trivial nodes such as button packs: a single wire, very low speed, bit-banged entirely in software on a microcontroller stripped down to the point of lacking even a UART.[634]

## Physical and data-link layer

CAN is a differential bus; the single-wire variant is the same protocol carried on one line of the pair with the other left unused.[388] Electrically, the bus behaves as a wired AND: transceivers float both lines to a common level for a recessive one, while any node transmitting a dominant zero pulls the pair together, so the medium itself resolves contention between simultaneous transmitters.[634]

### Arbitration

Arbitration is built into the physical layer rather than layered above it, so a multi-drop CAN bus has no collisions to recover from, in contrast to Ethernet, where collisions cost throughput.[93] Every node has a unique identifier; after the start bit, all waiting nodes begin transmitting in sync, each reading back what actually appears on the bus.[266][634] A node that reads back a value different from the one it sent knows a higher-priority frame is present, stops transmitting, and waits for the next frame; the node that survives to the end of the identifier field has won the bus, so the numerically lowest identifier always prevails while losers retry.[266][634]

The identifier field — eleven bits in the standard frame — does double duty as both the content identifier of the frame and its priority, and overloading one field with two meanings is a standing source of confusion for people learning the protocol.[634]

### Acknowledgement and error handling

CAN provides atomic delivery: a transmitted frame is valid only if at least one other node acknowledges it by pulling the acknowledgement bit dominant, a property most systems built on CAN rely on without realising it.[634] Error signalling exploits the protocol's bit-stuffing rule. Because six consecutive bits of the same polarity cannot occur in a valid frame, any node detecting an error asserts six dominant bits; every controller on the bus recognises the impossible pattern, all nodes discard the frame and resynchronise, and the sender retries.[634] Every node is additionally required to be able to take itself off the bus if it detects that it is transmitting continuously, so a single faulty module cannot destroy the network.[93]

## CAN FD

CAN FD retains the classic arbitration phase at conventional rates — commonly 250 or 500 kilobits per second — then switches to as much as eight megabits per second for the data field, with larger payloads.[388] The motivating application is flashing megabyte-sized ECU firmware images, a task that is painfully slow at classic rates; dealer software updates pushed through the diagnostic connector over a half-megabit link illustrate the problem, with four updates occupying four hours at a dealership in one instance.[388][524]

## Messaging model

From the programmer's side, CAN presents a publish-subscribe model rather than addressed messaging: a node broadcasts its sensor values, and any node that needs them picks them up and acts on them.[634][175] The protocol itself says nothing about message semantics, timing or identifier assignment; those decisions belong to whoever designs the network, and messaging may be periodic or event-driven, so a module cannot simply be dropped onto an existing bus and expected to work.[426]

The meaning of frames in a production vehicle is manufacturer-specific and is changed freely between models and model years, so a third party supporting a range of vehicles is maintaining a separate decoding effort per vehicle.[388] Manufacturers keep their message definitions private and sometimes split a single value across several frames under a private transport layer of their own, so receiving every frame on the bus is trivial while knowing what any byte means is the hard part.[568]

A consequence of the identifier-priority duality is that bus bandwidth is easy to exhaust by accident: a node with a low-numbered identifier transmitting on a short period wins arbitration every time and starves the rest of the network.[266] On the Hash Define Electronics sensor network, Ronald Sousa's first polled design — a controller broadcasting every 500 milliseconds with each sensor answering within that window — behaved well, while a later redesign in which every node fired its own one-second interrupt and gave up when it could not transmit produced permanent starvation of the higher-numbered nodes.[266]

## Vehicle network architecture

A car is partitioned into several buses rather than one. A high-speed one-megabit powertrain bus carries the engine and transmission controllers and reaches the rest of the vehicle through a gateway at the instrument cluster; a complex vehicle may contain as many as a hundred modules.[93] At roughly fifty cents in volume for a transceiver, minor modules are pushed onto cheaper UART-based sub-buses to keep both cost and CAN node count down.[93] LIN serves the same role below CAN, running on the UART peripheral any microcontroller already has and using a single wire instead of a pair.[518][634]

A 500-kilobit bus carries roughly 4,700 messages per second, which is the practical ceiling on how much vehicle data can be published.[388] Autonomous-driving sensing exceeds that ceiling by orders of magnitude: a LiDAR reporting distances thousands of times a second, or camera video, requires FlexRay or Ethernet, while CAN remains as the command-and-control path telling those sensors what to do.[388]

Safety-critical actuation is designed not to depend on the network: the airbag charge fires autonomously, and the bus connection exists so the module can report status for the warning lamp.[93] The corollary of distributed architecture is graceful degradation — any module can fail and the rest keeps operating — a property exploited outside road vehicles, where, for example, a ground station can still reach a battery module after the onboard computer dies, provided the command radio acts only as a packet router.[518]

Because modern ECUs are no longer islands, engine transplants between makes have become difficult: the ECU waits on messages from other modules — a traction control module instructing it to cap torque during wheel slip, for example — and those messages do not exist in a different manufacturer's car.[388]

Modern motorcycles carry the same architecture in a far smaller space: an ECU handling fuelling and ignition talks over CAN to a fly-by-wire throttle, an ABS module and an active suspension module.[426]

## Diagnostics and aftermarket access

The onboard diagnostics (OBD) connector is a standardised, deliberately accessible drop onto the vehicle's CAN bus, with a fixed pinout and a defined set of messages, which is why an inexpensive generic code reader works across makes.[93] The port sits on the vehicle bus, but access to full traffic is gated: a command or passphrase must be sent before the connector yields everything.[318] Because the connector is standardised, tuning tools reach the engine control module through it to remap fuel tables, alter boost pressure on turbocharged engines and change spark timing.[212] Dealer firmware updates are likewise pushed through the diagnostic connector over the CAN link.[524]

The standardised port also supports a market in aftermarket plug-in devices, some of which have been found on teardown not to be connected to the bus at all — a blinking light in a plastic case.[538]

## Security

Vehicle internal networks are effectively open once entered: the bus carries no meaningful access control, so going from control of a single device to control of many on the same bus takes very little.[265] The attack surface is every microcontroller attached to the bus, and a modern car has hundreds of them, down to sensors nobody thinks of as computers.[265]

Published automotive security research has followed this structure. The early published Toyota work required physical access to the bus to take control of the vehicle; follow-up research deliberately reproduced the same degree of control remotely to answer the objection that physical access made the result uninteresting.[265] Tyre-pressure monitors turned out not to be a route onto the vehicle bus precisely because their radio packets are a short fixed-format frame into a simple receiver rather than a complete CAN frame; had they carried full frames, the exposure would have been severe.[265]

Manufacturers segment vehicle buses so that critical systems are not on a user-accessible network, but segmentation always requires a gateway node that speaks on both sides, and that gateway is the weak point; the published Jeep work entered through the radio and crossed to the important bus through such a gateway.[388] The same weakness underlies a commercial vehicle-theft tool built into a Bluetooth speaker, with its apparent charging cable actually carrying the twisted pair: the bus is reached through wiring exposed behind a headlight, the legitimate nodes are first prevented from transmitting, and an unlock message is then asserted.[634][633] Teardown of that device found roughly ten dollars of parts — a PIC18F with an on-chip CAN controller, a transceiver and a small add-on circuit — potted in resin and sold for thousands of dollars.[634]

## Use outside passenger cars

CAN appears wherever there is a motor controller and a battery, not only in cars: mobile industrial equipment, robots and aircraft all carry the bus.[631] Hobby autopilots adopted CAN for dependable communication between subsystems years before standardised UAV bus specifications existed.[356] In robotics, moving a multi-axis machine from several microcontrollers strung together on serial links to a single controller on CAN became practical once the motor drives themselves gained CAN support.[416] In electric-vehicle conversions, every subsystem sits on CAN, with battery packs daisy-chained through small latching four-wire connectors and only the high-current cables running separately; the bus delivers a torque command and direction to the inverter, so regenerative braking is the same command with a sign change rather than a separate subsystem.[112]

Of the two DC fast-charging standards, one carries the volts-and-amps negotiation over CAN with dedicated pins for dedicated functions and supports exporting power from the vehicle, while the other layers the same negotiation on a power-line-communication protocol with heavy modulation and encryption.[524]

## Engineering practice

Hardware interfacing is straightforward: a microcontroller with an integrated CAN controller still needs an external transceiver to drive the bus at the correct line voltages, and the transceiver costs on the order of fifty cents in volume.[568][93] Bit-banging CAN on programmable I/O is harder than it appears, because the controller is not a shift register but a state machine with many distinct paths through its flow.[687] Boards intended to live in a vehicle need automotive-grade DC-DC converters and protected high-side switches, because the 12-volt line carries transients that will eventually kill a typical converter.[568]

For exploration, the recommended starting point is passive: an inexpensive Arduino-class adapter running SavvyCAN to watch traffic before transmitting anything.[388] Reverse-engineering a donor vehicle is a matter of tapping the bus, capturing traffic, identifying which value moves with which gauge, then transmitting on that same address.[112] Where wiring has been replaced by messages, validation becomes a matter of reading the bus: with an oscilloscope on the pair, pressing a switch shows the expected bit changing at its known position in the frame.[620]

A common safety rule for bus-based systems is to make every message globally unique, so that a command frame intended for one actuator has no effect if it arrives at any other node.[584] A subtler hazard appears when systems are ported off CAN: because the protocol's atomic acknowledgement is invisible while it is working, systems moved to a faster bus without it break in ways that look inexplicable, surfacing as race conditions that were never possible before.[634]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 93 | An Interview with Tom LeMense - Cacaesthestic Chronometric Carriwitchet | https://theamphour.com/the-amp-hour-93-cacaesthestic-chronometric-carriwitchet/ | April 29, 2012 |
| 112 | An Interview with Bob Simpson - Ardent Automotive Artisan | https://theamphour.com/the-amp-hour-112-ardent-automotive-artisan/ | September 9, 2012 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 266 | An Interview with Ronald Sousa of Hash Define Electronics | https://theamphour.com/266-an-interview-with-ronald-sousa-of-hash-define-electronics/ | September 8, 2015 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 388 | An Interview with Earl Sharpe and Collin Kidder | https://theamphour.com/388-an-interview-with-earl-sharpe-and-collin-kidder/ | April 15, 2018 |
| 416 | An Interview with James Bruton | https://theamphour.com/416-an-interview-with-james-bruton/ | November 18, 2018 |
| 426 | An Interview with Dean Pick | https://theamphour.com/426-an-interview-with-dean-pick/ | January 20, 2019 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 538 | Missle Man with Bruce Simson | https://theamphour.com/538-missle-man-with-bruce-simson/ | April 12, 2021 |
| 568 | YouTube to Consulting with Florin of Voltlog | https://theamphour.com/568-youtube-to-consulting-with-florin-of-voltlog/ | November 28, 2021 |
| 584 | Software for Rockets with Charles Aylward | https://theamphour.com/584-software-for-rockets-with-charles-aylward/ | April 3, 2022 |
| 620 | Engineering Education with Dr Don Wilcher | https://theamphour.com/620-engineering-education-with-dr-don-wilcher/ | February 20, 2023 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 633 | Engineering Optimization | https://theamphour.com/633-engineering-optimization/ | May 22, 2023 |
| 634 | The CAN bus can! with Dr Ken Tindell | https://theamphour.com/634-the-can-bus-can-with-dr-ken-tindell/ | May 30, 2023 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
