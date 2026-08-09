---
title: Ethernet
concept: ethernet
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

**Ethernet** is a family of wired networking standards whose classical form is a shared medium with contention-based access: a station transmits whenever it likes, collisions are detected and signalled, and the transmitter retries after a randomised delay, which is what makes unswitched Ethernet non-deterministic.[631] Higher data rates over an unchanged physical medium are obtained by adding levels to the transmitted signal rather than raising the symbol rate indefinitely, which is why gigabit Ethernet over ordinary Category 5 unshielded twisted pair uses a five-level signal.[77] On a circuit board an Ethernet port is normally partitioned into a MAC/PHY device plus an analogue front end between the PHY and the connector, so a design that already has a MAC may still need a separate PHY added to it.[150] Beyond general-purpose networking, Ethernet has become the backbone of industrial control cabinets, vehicle and avionics architectures, and networked audio, in each case competing against simpler buses on grounds of bandwidth, determinism and installation cost.[385][584][560]

## Media access and switching

Contention on classical Ethernet is resolved above the wire, by detecting a collision and retrying, which distinguishes it from buses that resolve contention in the physical layer itself. CAN is a multi-drop bus whose arbitration is built into the physical layer, so contention is settled deterministically as frames are transmitted.[93]

A modern Ethernet switch changes the picture: each ingress port has its own queue, and internal logic forwards packets from those queues to the correct egress port, so the collision behaviour of shared-medium Ethernet largely does not arise on a switched network. What replaces it is queueing delay.[584] A desktop user can treat the switch as a black box, but a control system cannot; designing with Ethernet in a real-time role requires knowing the jitter and latency the switch contributes and being able to bound them.[584] Some transports impose further requirements on the switch itself: AVB requires precision time protocol support implemented at the switch level, so the switch silicon has to be chosen for it, whereas transports that ride on UDP tolerate occasional lost packets and place no such demand on the infrastructure.[560]

Determinism, not raw bandwidth, is usually the binding constraint when streaming instrument data. Where delivery timing has to be bounded, TCP is unsuitable because its retransmission behaviour makes arrival times unpredictable.[209]

## Silicon and board-level implementation

Early bus interface silicon for vehicles was sold as standalone chips that carried both the physical layer and the MAC, and the protocols were licensed, which made the parts expensive relative to the function they provided.[93] Ethernet followed a different path in embedded designs, where several levels of integration coexist. Self-contained Ethernet modules integrate the MAC and the protocol stack behind a serial or SPI interface, so a microcontroller design gains a network port without the host having to implement TCP/IP; such modules were available for around twenty dollars.[79] The Microchip ENC28J60 is an Ethernet controller with an SPI host interface, which lets a board with no Ethernet MAC of its own gain a wired network port over a few existing pins.[319] Where several single-board computers plug into a common baseboard, distributing Ethernet to each slot over the SPI signals already present on the expansion header avoids a bundle of external cables and separate connectors.[319]

At the other extreme, the programmable I/O blocks on a low-cost microcontroller have been used to bit-bang 10 Mbit/s Ethernet directly, needing only a resistor network in place of a PHY, and the same blocks have been driven at the RMII interface level to talk to a real PHY.[687] Some application processors aimed at industrial equipment integrate two gigabit Ethernet MACs and an Ethernet switch on chip, alongside real-time coprocessor units capable of running fieldbus protocols such as EtherCAT, which is what makes them worth using in that role.[515]

Plugging a ready-made module into a product is economical only at low volume; once quantities reach the thousands the module's cost and assembly overhead justify designing the same function directly into the board.[349] Within one maker-oriented board vendor's range of roughly sixty to seventy products, the Ethernet-based boards accounted for the largest sales volume, with Power over Ethernet modules and PoE-equipped boards prominent among them.[349]

Requiring both an Ethernet port and high-speed USB on one microcontroller can eliminate whole vendor families, because some parts do not offer the two peripherals in the same silicon; in a 2019 Cortex-M7 selection this constraint cut the candidate list to two devices.[640] Errata are part of the same selection: a candidate carrying about twenty pages of errata was set aside in favour of a part with a cleaner document, even though both met the peripheral requirements.[640]

Because many microcontrollers integrate Ethernet MAC hardware, that hardware can be used as a fast point-to-point serial link by sending raw Ethernet frames and omitting TCP/IP entirely; a unidirectional link of this kind also removes collisions because the transmitter shares its segment with nothing else.[294]

## Power, isolation and cabling

An Ethernet port is galvanically isolated at the magnetics, which makes a sealed, weatherproof outdoor interface practical, and Power over Ethernet can carry supply current on the same cable so no separate power entry is needed.[548] The same property converts peripherals into instruments: replacing a USB host interface with gigabit Ethernet plus Power over Ethernet turns a computer peripheral into a standalone networked device, since one cable then supplies both the data path and the power.[265]

Wired Ethernet is also chosen for installation reasons. A deployed monitoring product was specified with a wired Ethernet connection rather than Wi-Fi so that installation is a matter of plugging in a cable at a customer site, with a cellular modem recommended as a fallback where the site's own internet connection is unreliable and the data volume is small.[544]

RJ45 connectors and Category cabling are frequently reused for interfaces that are not Ethernet, because the connector is standard and cheap, pre-terminated assemblies can be bought off the shelf, and the cable's electrical behaviour is characterised.[337] RS-485 and RS-422 signalling will run roughly a hundred metres over ordinary Ethernet cable, which covers most installation distances without any Ethernet protocol being involved.[337] Designing a product around standard off-the-shelf cable assemblies rather than a custom cable is a strong default, because custom cables carry engineering, tooling and supply effort that almost never repays itself.[337] The reuse has a cost: an RJ45 jack carrying a non-Ethernet interface invites a user to plug a network cable into it, which at best fails silently and at worst applies the wrong signals, the connector having become strongly associated with Ethernet even though it did not begin that way.[636]

## Selection against simpler buses

For short cable runs and modest data rates RS-485 is often preferred over Ethernet because it has no protocol stack, can be probed directly with an oscilloscope during debugging, and needs no switching infrastructure.[294] Ethernet carries an infrastructure cost that simpler buses do not: a general network needs hubs or switches and the cabling that goes with them, which grows the bill of materials and the physical complexity of an installation.[294] The practical trigger for moving an installation from RS-485 to Ethernet is bandwidth: once the required data rate makes the simpler differential bus struggle, the extra stack and infrastructure become worth paying for.[412]

The same threshold appears in vehicles. Sensors used for autonomous driving, such as lidar, generate data faster than a standard CAN bus can carry, which pushes vehicle architectures towards higher-rate buses including FlexRay and Ethernet.[388] Legacy industrial interfaces such as 24 V discrete inputs and 4-20 mA current loops persist alongside networked control because they tolerate long cable runs and can be diagnosed with simple instruments, which an Ethernet-based control network cannot match on those terms.[385]

Bandwidth also decides where a network sits in a system architecture. Software-defined radio platforms are partitioned by their host interface: one variant streams samples to an external computer over gigabit Ethernet, while an embedded variant puts a Linux host processor inside the box so the sample stream never has to be squeezed through an external link at all.[101] A host board with only 10/100 Ethernet is a bandwidth downgrade relative to USB 2.0 for streaming sampled data off a platform, so an embedded carrier board is only a good host when the processing stays on board rather than being exported over the network.[265]

## Industrial and avionics networks

Modern industrial control cabinets are wired with ordinary Ethernet switches and Category 5, 6 or 7 cable, and the switches are interchangeable commodity parts rather than special industrial silicon, because the control protocols sit on top of the standard networking stack.[385] Choosing Ethernet as a vehicle's internal network makes the Ethernet switch a first-class part-selection problem alongside the processor, with cost and component availability among the deciding factors.[584]

A network link budget can be worked out on paper before any hardware exists: starting from the Ethernet frame payload size and the preamble and header overheads, then subtracting a TCP or UDP header, gives the bytes left for sensor data and therefore how many sensor channels the link can carry at a given rate.[584] That paper budget is what lets an avionics team answer sensor-count requests from other disciplines with a number rather than an opinion, early enough that the request can still be renegotiated.[584]

Keeping a vehicle's avionics on a single major network, rather than bridging several, keeps the number of hops between a command and an actuator small and the timing behaviour analysable.[584] When a control subsystem runs out of I/O, the scalable answer on an Ethernet architecture is to duplicate the controller board and add it as another addressable node rather than hanging sub-processors beneath the existing one; this keeps the topology hub-and-spoke, where adding a spoke changes nothing else, instead of a tree that must be rebalanced against bandwidth limits.[584]

Ethernet also serves as a transport where the alternative cannot span the distance. In a lecture-theatre video capture rig the camera and presenter feeds are converted to Ethernet and trunked to a software mixer, because HDMI runs are limited to roughly ten metres and cannot cross the room.[375]

## Networked audio

Networked audio over Ethernet has no open standard, so vendors implement proprietary transports; one leading transport originally required buying the silicon from its owner and later moved to licensed FPGA code, leaving the ecosystem fragmented across incompatible implementations.[560]

## Ethernet over USB

A Linux single-board computer can present itself over USB as Ethernet, first enumerating as mass storage to deliver drivers and then switching to an Ethernet peripheral; because the same cable supplies power, development needs only one connection to the host.[142] Such a board may expose two Ethernet-over-USB interfaces at once because the host operating systems support different gadget protocols: macOS binds to one and Windows to the other, while Linux enumerates both.[378] The board handles address assignment by DHCP so the interface comes up automatically in the large majority of cases; what remains for the user is changing the routing and gateway on the host if the board is to reach the wider network.[378]

Wired Ethernet ports on single-board computers carry their own architectural constraints. On early Raspberry Pi boards the Ethernet controller hangs off the same internal USB bus as the external USB ports, so disk traffic and network traffic contend for one link and total throughput is limited.[235] Removing the Ethernet port and three of the four USB host ports yields a smaller, lighter and lower-cost variant of the same board, which suits embedded projects that do not need wired networking.[235]

## Bring-up, debugging and failure modes

Bringing an Ethernet interface up on an early single-board Linux computer was not a plug-and-play exercise: the port did not work out of the box and required extended work at the operating-system level before a link and stack were usable.[26] A bare-metal or RTOS networking bring-up characteristically demonstrates well and then fails hours later, with the PHY, MAC and DHCP all coming up and passing packets before transmission stops and the processor sits in a hard fault; an operating system that isolates and restarts a failed process contains that class of bug far better.[515] An embedded product that accumulates USB host support, a file system and an Ethernet stack acquires several long-running background tasks that spend most of their time blocked, and that combination is the point at which a real-time operating system starts to earn its complexity.[511]

An Ethernet link that drops on an exact, repeating period is a lease-expiry symptom rather than a physical-layer fault: the DHCP lease reaches its end and the interface resets while the address is renegotiated.[674]

Physical-layer observation is difficult. 100 Mbit/s Ethernet cannot usefully be probed by putting an oscilloscope on the pair, because the line coding makes the waveform look like noise and it is not even possible to tell by eye when the link is transmitting.[412] Capturing gigabit Ethernet on an oscilloscope is memory-bound: a hundred megasamples at one terasample per second is only about a hundred microseconds of record, enough to hold roughly one to three UDP packets, which is why differential probing of the pairs is a last resort rather than a routine method.[600] The workable approach is to decode rather than to probe: an Ethernet PHY recovers the received data together with a data-valid indication, and a small FPGA parallelises that stream into a mixed-signal oscilloscope's parallel bus input so the logic analyser can decode packets.[412]

Prototyping tolerances are looser than they appear. Application-processor interfaces including 100 Mbit Ethernet will run well enough over 0.1 inch headers and jumper wires for prototyping, because the resulting packet errors are absorbed by the CRC checks and retransmission already built into TCP/IP, so a breadboarded link still proves the design out.[515]

## Historical incompatibility

The Ethernet on the Xerox Alto ran at 3 Mbit/s over coaxial cable and is electrically and logically incompatible with modern twisted-pair Ethernet, so connecting such a machine to a current network requires a purpose-built gateway; an FPGA-based bridge was built to do exactly this.[361]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 26 | The Ben & Jeri Show | https://theamphour.com/the-amp-hour-26-the-ben-jeri-show/ |  |
| 77 | An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry | https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/ | January 9, 2012 |
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 93 | An Interview with Tom LeMense - Cacaesthestic Chronometric Carriwitchet | https://theamphour.com/the-amp-hour-93-cacaesthestic-chronometric-carriwitchet/ | April 29, 2012 |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 142 | Kickstarter, IndieGoGo & Ignite - Jasperated Jimswinger Jobbery | https://theamphour.com/the-amp-hour-142-jasperated-jimswinger-jobbery/ | April 22, 2013 |
| 150 | Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness | https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/ | June 17, 2013 |
| 209 | Headless Units and Baseless Batteries - KiCad Kickoff Kopophobia | https://theamphour.com/209-headless-units-and-baseless-batteries-kicad-kickoff-kopophobia/ | July 28, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 294 | Live from Serbia with Mike Harrison | https://theamphour.com/294-live-from-serbia-with-mike-harrison/ | April 13, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 349 | An(other) Interview with Jon Oxer | https://theamphour.com/349-another-interview-with-jon-oxer/ | June 25, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 385 | An Interview with John Davis | https://theamphour.com/385-an-interview-with-john-davis/ | March 25, 2018 |
| 388 | An Interview with Earl Sharpe and Collin Kidder | https://theamphour.com/388-an-interview-with-earl-sharpe-and-collin-kidder/ | April 15, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 511 | Brewing Electronics with Eli Hughes | https://theamphour.com/511-brewing-electronics-with-eli-hughes/ | October 4, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 548 | The Last Line of Defense | https://theamphour.com/548-the-last-line-of-defense/ | July 5, 2021 |
| 560 | High End Audio with Remco Stoutjesdijk | https://theamphour.com/the-amp-hour-560-high-end-audio-with-remco-stoutjesdijk/ | October 3, 2021 |
| 584 | Software for Rockets with Charles Aylward | https://theamphour.com/584-software-for-rockets-with-charles-aylward/ | April 3, 2022 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 674 | Turtles as a Service | https://theamphour.com/674-turtles-as-a-service/ | July 25, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
