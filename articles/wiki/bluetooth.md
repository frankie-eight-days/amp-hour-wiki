---
title: Bluetooth
concept: bluetooth
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Bluetooth is a short-range wireless communication standard operating in the unlicensed 2.4 GHz band, and alongside Wi-Fi and USB it is one of the practical options for moving data in and out of a small instrument.[142][155] The standard has two branches: classic Bluetooth, a connection-oriented link designed as a wireless serial cable replacement, and Bluetooth Low Energy (BLE), introduced in 2010 to address the power consumption of the original design.[354][442][664] Both branches occupy exactly the same spectrum and the same set of channels, BLE using a subset, and Bluetooth devices hop across 79 MHz of bandwidth with transmit power between 0 and 20 dBm.[155][161][728]

## Variants

### Classic Bluetooth

Classic Bluetooth was designed as a wireless serial cable replacement and supports serial port emulation that appears to the host operating system as a COM port at driver level.[354] Its design was centred on audio, with the serial port mode as a secondary feature, and it was power hungry relative to its successor.[442] It offers relatively high bandwidth at the cost of holding a connection open continuously.[145] Because a classic link is not deterministic, it is unsuitable for applications such as head tracking, where a dropped packet leaves the rendering engine with a stale head position and produces a visible error.[173]

### Bluetooth Low Energy

Bluetooth Low Energy was introduced in 2010 and brought the low-power and longer-range branches of the standard.[664] A BLE peripheral publishes a generic attribute table as part of its advertising data, so a host can discover what the device does without the PIN exchange and handshake that classic Bluetooth pairing requires.[144] BLE is low bandwidth, and its cable-replacement service does not present the same plug-and-play COM-port interface as classic Bluetooth.[145][354] BLE earns its place where a device must run for roughly two years from a single CR2032 coin cell.[354]

Classic profiles such as serial port and HID are defined by the Bluetooth SIG and handed to the implementer, whereas BLE requires the profile to be built by the developer unless the stack supplies one; this is more work but permits a very lightweight profile for a simple sensor.[155] The two branches share the same spectrum, so a dual-mode device cannot fully use both at once, and high-bandwidth serial data or high-quality audio consume most of the available spectrum for an active link.[155] The Bluetooth Smart branding is a compatibility mark rather than a protocol: it indicates a dual-mode device able to work with both classic Bluetooth and BLE.[285]

## History

Early Bluetooth silicon was a multi-chip solution: one company supplied the radio front end, another implemented the baseband in an FPGA or other digital logic, and a large software stack sat above both; present-day parts integrate all three.[338] The specification's long gestation meant its throughput was already inadequate for its original use case by the time silicon shipped: at around 700 kbit/s a four-megapixel image took about two and a half minutes to reach a printer, against 12 Mbit/s for contemporary USB.[169] For its first decade Bluetooth was in practice a wireless audio link plus a few simple gadgets, many of which used the ANT protocol instead, and the standard took close to a decade in the field before high-quality audio worked interoperably — a realistic timescale for a complex new interface standard to stabilise.[421][664]

Before BLE, an accessory that wanted to talk to Apple hardware needed an authentication chip; a BLE link bypassed that requirement, and even a slow serial channel was sufficient for many accessories.[168] Apple subsequently implemented BLE features that were not in the specification — for example allowing a phone application to scan for peripherals and to act as a peripheral itself, both at once — and the SIG later added them to the standard.[226] The low-power audio profiles were driven into the specification by the hearing aid industry and were then available to other industries to build on.[338]

Android hardware shipped with BLE capability before the operating system exposed it; official platform support arrived with API level 18, in Android 4.3.[155][226] Before that release a developer had to use each handset manufacturer's own stack, which is why small teams targeted iOS first.[226]

## Radio characteristics

Bluetooth hops across 79 MHz of bandwidth, and the minimum gap between packets is a little over 200 microseconds, which sets the hardware retune budget.[161] Frequency hopping imposes a hard requirement on the synthesiser: the PLL must acquire and lock a new frequency fast enough to be ready for each hop.[338] Where a hopping scheme spans more than the receiver's instantaneous bandwidth, the hopping must be implemented in the radio's own microcontroller, because adding USB latency to the host round trip pushes the retune well past the inter-packet gap.[161]

The 2.4 GHz band carries Wi-Fi, Bluetooth and assorted IoT protocols including Thread, and is congested; the mitigation available to product designers is band diversity, using 5 GHz or newer Wi-Fi generations where the application allows.[368][678] Wi-Fi and Bluetooth cannot both be transmitting at the same instant, so stacking several radios onto one product is dominated by battery life and coexistence questions even though modules exist for each.[167]

Practical range indoors is short and highly dependent on construction: a beacon may be readable across a small house while other Bluetooth devices fail to penetrate a single interior wall.[660] Outdoors, 2.4 GHz propagation degrades as humidity rises and the band is loaded by every phone in the vicinity, making Bluetooth a poor choice where distance matters.[453] Practical throughput is limited to about one megabit per second or less, which rules Bluetooth out for pushing display content or video to a device and forces such designs to Wi-Fi at an order-of-magnitude increase in power consumption; there is no satisfactory low-power personal-area network between the two, although video has been carried over Bluetooth by exploiting efficiencies in the specification.[638]

The prevailing mental model of Bluetooth as a very short-range link derives from its origin as a high-fidelity audio streaming standard; from a purely RF standpoint nothing in the physical layer restricts it to that use.[728]

## Discovery, profiles, and addressing

A true Bluetooth beacon transmits its data unsolicited and periodically for any listener to receive, which is distinct from advertising in preparation for pairing; asset trackers generally sit in beacon mode.[690] If a device continually publishes its readings in a standard GATT message, a listener can decode them without pairing; where pairing is required, the host must negotiate with each device before any data is available.[665] The SIG defines standard GATT profiles for common device classes such as a health thermometer or a heart rate monitor, so a generic host can decode those packets without device-specific code; the set reflects the applications anticipated early in the protocol's life and has grown since.[664]

Bluetooth device addresses, like USB vendor identifiers, are issued by a central authority, because guaranteeing a globally unique address requires one.[396] Bluetooth qualification through the SIG is a voluntary association rather than a government regulation: the 2.4 GHz band itself is unlicensed, and certification is only required if a product is to be presented as Bluetooth.[155]

## Platform support and the phone as gateway

Native BLE support in both Android and iOS makes the smartphone the default gateway for a sensor: the sensor connects to the phone, and the phone provides display and the path to the cloud.[232] Bluetooth devices marketed as internet-connected are in practice phone-connected: a Bluetooth peripheral has no publicly routable IP address, holds only a local address on the phone it is paired with, and the phone translates between the internet and the Bluetooth link.[202][587] By contrast, Thread nodes receive an IPv6 address through a border router and are addressable from the wider internet.[587]

Background Bluetooth operation is governed by the handset platform rather than by the Bluetooth specification: a national COVID contact-tracing application that relied on Bluetooth advertising in the background failed on Apple devices for this reason.[543] A single phone can hold simultaneous BLE connections to more than one peripheral, though the practical ceiling is imposed by the host implementation.[354] Host-side compatibility can be durable: on Eric Migicovsky's watch product, the Bluetooth connection continued to work with subsequent Android and iOS releases for eight years after the last unit was manufactured.[715]

## Power

Low-power Bluetooth systems meet their energy budget through an extremely small duty cycle — the RF circuits are live only briefly and off for well over 95 percent of the time, with a background digital controller running between bursts — together with optimisation of the power drawn by what remains.[704] A BLE device will run for about a year even from a small CR2032 cell, but classic Bluetooth is better on connection reliability; the choice turns on how often the device transmits and how quickly it must respond.[389] On a product already carrying four AA cells, Dave Jones judged that BLE's power advantage bought little and that classic Bluetooth would have been the sounder choice, noting that the module can in any case be powered down entirely between sessions.[354]

The reporting interval can dominate a power budget by orders of magnitude: on Luke Iseman's connected-sensor programme, a sensor assumed to need a reading every minute in fact satisfied its users at four readings a day, a roughly thousandfold reduction in energy.[268] Partitioning a low-power design so the radio module maintains the connection while the application microcontroller sleeps lets an infrequent-transmission product keep a live link without keeping the processor awake; on Colin Karpfinger's design the module held the connection to the phone while the main processor slept.[226] Power characterisation is done against a budget rather than by open-ended measurement: the current in each system state, such as modem transmitting, modem sleeping and the Bluetooth microcontroller idle, is estimated at design time, and measurement then checks each state against the estimate.[527] Some IoT standards for house-wide mesh networks mandate a minimum battery life of one or two years, because replacing cells in dozens of nodes at short intervals is not acceptable to the user.[704]

As an example of the low end, the nRF52810 pairs a Cortex-M4 with an integrated Bluetooth radio, runs at about 32 microamps per megahertz with roughly two microamps per megahertz more when executing from flash rather than RAM, and works down to 1.7 volts; the part with a coin cell is cheap enough to appear in single-use disposable products.[551][636]

## Modules, silicon, and manufacturing

A pre-built radio module stops being the efficient choice at production volumes of roughly one hundred thousand units a year, above which integrating the equivalent circuit onto the product's own board becomes worthwhile.[155] On the Pebble watch, Migicovsky's team used a bare CSR Bluetooth chip instead of a module to save roughly eight dollars a unit — a module costing about ten dollars against one to two dollars for the chip — at the price of about eight months porting an open-source Bluetooth stack to it.[715] His rule of thumb was that the early-stage bill of materials should be optimised for the least hassle in shipping a first product rather than for mass-production cost, because the purpose of the first units is to establish that the product is worth building at all.[715] Jeff Keyzer's corresponding judgment is that Bluetooth is a commodity function, so a custom Bluetooth chip is only justified by a specific need such as a required level of integration, a deliberate deviation from the specification, or an unusual power or battery architecture.[365]

Inheriting a module's FCC modular certification is conditional on using one of the antennas the module manufacturer had approved, typically a small set of ceramic chip antennas.[175] A radio module cannot be changed late in a programme because the design is already at the test house undergoing FCC compliance testing; the radio choice is effectively frozen at that point.[354] Compliance failures can also arise from classification error rather than technical fault: in one case a laboratory employee assessed a Bluetooth module against Wi-Fi transmitter criteria.[226]

On Andrew Witte's early smartwatch project, radio performance was verified per unit rather than per design: after the antenna was assembled the complete watch went into an RF test chamber and its output power was measured, alongside a pressure test of the waterproofing.[175] The same project later replaced the certified module with the equivalent circuit laid out directly on the product's own board, delivering a substantial cost saving at the price of certifying the radio afresh, and the respin occupied the electrical engineering team for a long period.[175] Its open-source Bluetooth stack had originally been written as a user-mode stack for jailbroken iPhones, illustrating how thin the supply of usable third-party stacks was at the time.[175]

The ESP32 places two 240 MHz 32-bit cores running FreeRTOS alongside classic Bluetooth, BLE and Wi-Fi on a single low-cost chip; at launch its Bluetooth side was effectively undocumented and had to be worked out from forum sample code.[330] The nRF52810 is the low end of Nordic's nRF52 family and the nRF52840 the high end.[551] Cloning a combined Wi-Fi and Bluetooth system-on-chip is impractical because a clone would have to implement the radio protocols from scratch; complex clone parts are behavioural simulators with an entirely different internal architecture, not copies of the silicon.[359]

A silicon vendor's evaluation hardware is typically a ladder rather than one board: a coin-cell-sized form-factor demonstrator, a broken-out reference design, and a full development kit that supports current measurement.[452] Internal characterisation boards spend money and area on supply quality that a customer board would not, because the point is to measure the performance of the silicon rather than the performance of the board.[452]

## Software stacks

Nordic's SoftDevice is a precompiled binary with a fixed API that occupies a reserved region at the bottom of flash and a portion of RAM, with the bootloader placed at the top of memory; the application must be linked around both.[516] Zephyr is a real-time operating system that originated at Wind River and passed to the Linux Foundation; its attraction for connected devices is that Bluetooth arrives as an included subsystem rather than as low-level calls into an opaque vendor API.[510] Choosing a silicon vendor whose part is natively supported by Zephyr supplies a maintained Bluetooth stack with the kernel; the alternative is keeping the existing RTOS and integrating a separate open-source stack, and the cost of each path is hard to forecast in advance.[715] Keeping a radio module and a swappable application coprocessor as separate parts lets prototype firmware move onto a production board of any shape: the same module and protocol are retained while the coprocessor is chosen for cost.[226]

Working at a very low layer of the Bluetooth protocol, L2CAP, allowed Witte's watch to communicate with BlackBerry applications, but the same approach gave limited support on Android and none on iOS.[175] The classic HID profile is a common starting point for a wireless input device because it gives very wide compatibility with existing hosts without a custom driver.[155]

## Firmware update

Over-the-air update requires a second image region: the new image is downloaded, checksummed and stored separately, verified by running it, and only then copied over the previous one, leaving the old slot free for the next update.[364] Implementing update over Bluetooth forces the entire Bluetooth stack into the bootloader, which is what makes the feature expensive on a part with a small bootloader region; on one of Dave Jones's instrument projects the feature was estimated as disproportionate work and abandoned in favour of an SD card, in part because the link is not reliable enough to be depended on for a whole image transfer.[364]

An nRF52840 carrying a bootloader alongside the SoftDevice can accept a new firmware image over the air from a phone application, so a sealed enclosure never has to be opened to update it.[510] Both the Bluetooth stack and the bootloader must sit in protected memory so that a failed update can still be recovered over the Bluetooth link, and some microcontrollers provide too little protected memory to hold a Bluetooth stack, ruling out recoverable update on those parts.[516] On Elecia White's account, the nRF52 firmware update mechanism is a sound and reasonably secure design, but per-device keying makes fleet updates awkward, and the correct direction of trust is for the device to authenticate the image it receives rather than the reverse.[422] Firmware update over Bluetooth changes the support economics of a product: an image can be sent to a user and loaded from a phone application without any cable or disassembly.[516]

## Security

Placing a Bluetooth device in non-discoverable mode does not prevent an observer from finding it or monitoring its transmissions, and monitoring a single Bluetooth channel yields enough information to derive the frequency-hopping sequence and then follow the link across the band.[161] Research tooling that requires a two-thousand-dollar instrument plus a hardware modification is rarely reproduced; Michael Ossmann started the Ubertooth project to replace that approach with a low-cost dedicated receiver that monitors one channel and passes the bits to a computer over USB.[161] Early Bluetooth car kits carried vulnerabilities that allowed an unauthenticated party to connect to them.[352] An attacker need not extract a cryptographic key from a token: adding a Bluetooth radio to the device and reading and broadcasting the displayed code achieves the same result.[346]

Consumer BLE appliances commonly broadcast their state with no key exchange, so any receiver in range can decode the activity; a mains toothbrush was found to advertise its usage openly and be readable by a generic home-automation integration.[660] In CVSS risk scoring the attack vector is ranked remote, then local, then adjacent, then physical; attacks over a radio protocol such as Bluetooth or Wi-Fi fall in the adjacent category, which scores lower than a network-reachable Linux device with an IP address.[698]

## Interoperability and failure modes

Each BLE implementation differs in practice — in the words of one discussion, "Each BLE implementation is a special snowflake" — so a product must be validated against individual host implementations rather than against the specification alone.[354] A wireless standard functions as a suggestion rather than a contract, and large vendors implement variants; conformance to the specification is what maximises the number of devices a product will interoperate with.[468] Devices operating at the edge of the specification interoperate with each other but not necessarily with everything else; the practical remedy is to control and define both ends of the link.[376]

Streaming continuous data over a Bluetooth link, which the protocol was not designed for, is easily interrupted on the congested band and shows up as corrupt packets.[368] A Bluetooth data-logging link on one of Jones's meters produced a failure worse than a dropout: a fixed one-volt reading was reported as ten volts, a value outside the range the meter was set to, so corruption in the link was indistinguishable from a real measurement, whereas a dropout reported as a null value would have been benign.[694] Diagnosing intermittent corruption over a Bluetooth link means isolating each element of the chain in turn: the instrument, the firmware in the Bluetooth module, the Bluetooth driver on the receiving handset, and the handset operating system version.[694] Debugging a device over its own Bluetooth link is of limited use when the defects under investigation are in the Bluetooth stack itself; the technique suits application developers whose code sits above the stack.[175]

## Applications and system architectures

A Bluetooth asset tag keeps per-device cost and power low by only broadcasting a beacon identifier; the location fix comes from passing phones that report the sighting with their own GPS, so utility depends on how many phones pass the tag.[543] Jean Rintoul's measurement instrument uses a Bluetooth link to remove the wired connection so it can run from a lithium-ion cell, a low-noise supply compared with mains-derived power, with the data arriving as a serial port on the computer.[448] Andrea Longobardi's air-quality sensor was given two data paths — BLE for live retrieval by a phone during exercise, and NFC so the data could be downloaded by touch afterwards without carrying the phone — in a package measuring 18 by 18 by 8 millimetres and weighing about five grams, with the battery carried separately in the garment.[635] On Aedan Cullen's AR headset programme, Bluetooth's throughput ceiling ruled it out for display content and forced the design to Wi-Fi.[638]

Thread is a mesh arrangement built on the 802.15.4 radio protocol at 2.4 GHz, which lets the same class of low-power node used for Bluetooth carry routed traffic instead of a point-to-point link; an nRF52840 is nominally a Bluetooth part but its radio can carry other 2.4 GHz protocols, which is what allows the same silicon to be used for Thread meshing.[587] A point-to-point Bluetooth radio is the wrong primitive for a gateway that must collect from many low-power sensors and backhaul over cellular; a mesh layer is what makes that platform work.[587] A commercial 802.15.4 Thread mesh built on nRF52840 nodes was withdrawn after about a year of development because the networks proved too difficult to set up reliably, leaving radio-only node hardware without a mesh to join.[477] A long-range mesh node design splits the two radios by role: an ESP32 presents a Bluetooth interface to the phone application while a Semtech LoRa transceiver carries the long-distance link, with the mesh forwarding up to three hops.[677]

For a simple one-way broadcast application a plain 2.4 GHz transceiver is preferable to a full protocol such as Bluetooth or ANT, because the nodes never need to transmit back.[453] A proprietary link with a unique 128-bit encryption key programmed into each unit at the factory removes channel setup entirely and eliminates the pairing step.[636] Before committing to a connected consumer device at all, Iseman's design question is whether the product is really a sensor connecting over Bluetooth or Wi-Fi to a phone or tablet the buyer already owns, which avoids the cost of a custom screen and enclosure at low volume.[268]

Alex Haro's satellite programme treats a Bluetooth chip simply as a source of 2.4 GHz sine waves, driving it to emit a custom waveform rather than run the Bluetooth stack, which makes a satellite uplink a software-only change to an existing device.[728] Because Bluetooth chips transmit at between zero and 20 dBm, a link over hundreds of kilometres has to be closed at the receiver: lowering the bit rate puts more energy into each bit, and thousands of antennas performing digital beamforming on the satellite form narrow spot beams that isolate one weak transmitter from the rest.[728] Bluetooth was preferred over LoRa as the device-side radio because Bluetooth is already embedded in nearly every electronic product, whereas LoRa silicon is available only from Semtech.[728] Two waveforms can share one chip because an advertising device is idle most of the time — a tag advertising every two seconds transmits for under a hundred milliseconds and leaves about 1.9 seconds free — but a chip can only emit one waveform at a time, so continuous audio streaming has to be paused for the second transmission.[728]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 142 | Kickstarter, IndieGoGo & Ignite - Jasperated Jimswinger Jobbery | https://theamphour.com/the-amp-hour-142-jasperated-jimswinger-jobbery/ | April 22, 2013 |
| 144 | An Interview with Bob Davidson - Hoodied HP Hijinks | https://theamphour.com/the-amp-hour-144-hoodied-hp-hijinks/ | May 7, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 155 | An Interview with Jeff Rowberg - Mini Module Master | https://theamphour.com/the-amp-hour-155-mini-module-master/ | July 22, 2013 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 168 | Specialized and/or Open Source Test Gear and Dev Boards - Vacation Videography Vorboten | https://theamphour.com/168-specialized-and-open-source-test-gear-and-dev-boards-vacation-videography-vorboten/ | October 21, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 268 | An Interview with Luke Iseman of yCombinator | https://theamphour.com/268-an-interview-with-luke-iseman-of-ycombinator/ | September 22, 2015 |
| 285 | Something's Serially Wrong Here | https://theamphour.com/285-somethings-serially-wrong-here/ | February 3, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 352 | Conning with Michael Ossmann | https://theamphour.com/352-conning-with-michael-ossmann/ | July 17, 2017 |
| 354 | A Meeting Of The Davids | https://theamphour.com/354-a-meeting-of-the-davids/ | August 7, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 365 | Wait, why is Jeff glowing? | https://theamphour.com/365-wait-why-is-jeff-glowing/ | October 30, 2017 |
| 368 | The EEVblog Sparkgap Generator | https://theamphour.com/368-the-eevblog-sparkgap-generator/ | November 19, 2017 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 396 | The Synergy Bus | https://theamphour.com/396-the-synergy-bus/ | June 10, 2018 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 448 | An Interview with Jean Rintoul | https://theamphour.com/448-an-interview-with-jean-rintoul/ | June 23, 2019 |
| 452 | An Interview with Kieran O'Leary | https://theamphour.com/452-an-interview-with-kieran-oleary/ | July 28, 2019 |
| 453 | Vertically Integrated Design Engineering | https://theamphour.com/453-vertically-integrated-design-engineering/ | August 4, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 543 | Cassette decks have browsers? | https://theamphour.com/543-cassette-decks-have-browsers/ | May 23, 2020 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 635 | Low Power Connected Devices with Andrea Longobardi | https://theamphour.com/635-low-power-connected-devices-with-andrea-longobardi/ | June 4, 2023 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 664 | Simulating doors falling off | https://theamphour.com/664-simulating-doors-falling-off/ | April 3, 2024 |
| 665 | Really long needle nose pliers | https://theamphour.com/665-really-long-needle-nose-pliers/ | April 24, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
| 678 | All About Antennas with Katerina Galitskaya | https://theamphour.com/678-all-about-antennas-with-katerina-galitskaya/ | September 30, 2024 |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11, 2025 |
| 694 | Voltage, Vibes, and VOCs | https://theamphour.com/694-voltage-vibes-and-vocs/ | May 21, 2025 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 715 | Shiny New Pebble with Eric Migicovsky | https://theamphour.com/715-shiny-new-pebble-with-eric-migicovsky/ | February 9, 2026 |
| 728 | Space Age Bluetooth with Alex Haro | https://theamphour.com/728-space-age-bluetooth-with-alex-haro/ | July 9, 2026 |
