---
title: USB-C
concept: usb-c
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

USB-C is a 24-pin reversible connector and interface standard that carries data at up to 10 gigabits per second per lane and delivers power at up to 100 watts (20 volts at 5 amps) through a single connection.[340][240] The connector achieves reversibility through radially symmetric power pins and hardware multiplexing of the high-speed data lines, with a dedicated configuration channel establishing plug orientation and power roles.[340][262] It is rated for 10,000 mating cycles, making it viable as a user-removable connection where internal board-to-board parts may be specified for ten or thirty cycles.[340] The same connector supports alternate modes such as video over the high-speed pins, so that one physical interface can carry display protocols, legacy USB, and negotiated power contracts simultaneously.[340][421]

## Connector architecture

The connector carries twenty-four pins where earlier USB connectors had four or five, with several pins duplicated for power and one dedicated configuration channel (the CC pins, CC1 and CC2) that establishes which way round the plug was inserted and which end is sourcing power.[340][640]

Reversibility is handled differently for different signal classes. The four power and four ground pins are placed radially symmetrically, so orientation does not matter for them, and the low-speed USB 2.0 data pair is slow enough that both candidate pin positions can simply be shorted together.[340] The high-speed pairs cannot be treated this way: shorting both positions at gigabit rates leaves a long unterminated stub on the line that destroys the signal, so orientation is resolved in hardware by multiplexing the lines so that the right signals reach the right pins whichever way the plug went in.[340][262] A related trap in pass-through designs is that the high-speed transmit and receive pairs are swapped inside the cable rather than at the ports.[293]

The connector is rated to 10 gigabits per second per lane depending on the specific part, with four lanes available, meaning in principle 40 gigabits per second of data and 100 watts of power can move through one connector at once.[340] The original USB 2.0 low-speed data pair remains present on the connector and is carried even by the newest specification; USB 4 runs two lanes in each direction for 40 gigabits per direction.[497] USB 4 originated when Intel opened up a proprietary high-speed interface, which was then adopted as the USB 4 specification using the same connector, so no further physical variant was introduced.[434]

### Durability and mechanical design

The published mating-cycle rating is 10,000 insertions.[340] Connectors below that grade fail much earlier: a locally sourced part substituted on cost grounds worked for roughly fifty insertions before the plating was scraped away and contact became unreliable, which justified paying for the higher-grade Japanese part despite it being among the more expensive items on the bill of materials.[450]

The connector can also outrun a factory's board process. A keyboard is otherwise a two-layer board with wide traces, and an assembler's usual fabricator preferred twelve-thousandths trace-and-space rules, which will not accommodate the connector's footprint; eight-thousandths rules are required.[450]

The plug overmold has a specified maximum envelope, on the order of 6.5 by 12 or 13 millimetres, which is the number to design an enclosure cutout against; cables in hand do not always respect the specification, so a recess sized to the specification can still fail to admit a particular heavier cable.[668]

## Power delivery

Role assignment begins as pure analogue: resistors on the two configuration pins set a voltage that indicates roughly whether an end is a source or a sink.[640] Above that sits a negotiation in which source and sink settle on a contract — one end advertising, for example, twenty volts at three amps alongside fifteen, nine and five volts — and either end can request a change of roles or contracts later.[640] The simplest implementations need nothing more than pull-ups, pull-downs and an analogue reading; swapping power or data roles on the fly requires the power delivery (PD) communication protocol, which despite the name governs far more than power.[340] That protocol is a single-wire, time-based scheme using biphase mark coding, which once had to be coaxed out of serial peripheral hardware; dedicated controller chips now translate it into a two-wire bus that ordinary firmware can drive.[340]

### Voltage rails and limits

The power brackets are a small set of fixed rails — five, nine, fifteen and twenty volts — and the top rail plausibly exists because laptop supplies had already settled around nineteen and a half to twenty volts.[421] The guaranteed ceiling is 100 watts, that figure being twenty volts at five amps; a laptop-and-dock pairing that charges at 130 watts is already outside what the standard guarantees.[421][240] Five amps is the ceiling because the copper cross-section is limited: several pins are assigned to power, but each is small.[640]

At forty-eight volts the contact geometry becomes a safety feature: the pin tips are shaped to steer where an arc forms, the configuration pins must break first, and the voltage must collapse quickly on unplugging under load, otherwise a direct-current arc sustains itself.[640] For that reason most connectors actually available are still rated only to twenty volts, whatever the standard permits.[640]

### Controllers and firmware practice

Anything above the default couple of watts requires a controller implementing the negotiation, placed on the port side of the isolation barrier in an isolated supply so that incoming power can be brokered before it crosses.[449] Because those controllers implement a common standard, poor documentation from one vendor can be worked around by taking a competing vendor's development material — in one case from Texas Instruments — and running it against the part, which worked.[449] Writing firmware against the standard rather than the part is what makes an obsolescence plan credible: if the chosen controller is discontinued five years into production, another power delivery controller should drop in with the code unchanged.[449]

Where a product only wants power, the full twenty-four-pin fine-pitch connector is a burden that must still be paid for, because the negotiation is mandatory even when no data will ever be sent.[496] A configurable sink addresses part of the resulting gap: a device that negotiates a contract and then presents whatever fixed output voltage and physical connector a legacy product expects, such as a barrel jack.[722]

## Alternate modes and port behaviour

Alternate mode runs a display protocol over the high-speed pins; even without leaving five volts, the power budget reaches fifteen watts, and this combination — detachable cable, video, and power — drove the connector's selection for at least one product needing a user-removable video connection.[340]

The accumulated complexity is structural: USB 2.0 is ubiquitous enough that it must still be supported, the faster generation is wanted on top of that, and the connector adds a further dimension of alternate modes.[421] The greatest hazard of a connector that can do anything is that a given port usually cannot: one port on a machine may be the only one that charges, another the only one that drives a display, and the plug gives no clue.[340] Dedicating one of a small number of ports to charging quietly removes it from the pool, which is a real cost when the machine has only four.[565]

The remedies are weak. Markings can be printed on the case and will mostly be ignored, and a billboard device class exists to deliver a human-readable string over USB explaining why the thing the user just plugged in is not working.[340] Making every port equivalent is the right answer for the user and expensive for the builder, because it means duplicating the internal hardware behind each port — switches and multiplexers, already needed to handle the cable flip — while keeping power and signal integrity intact across them. This is the general pattern of the standard: ease for the user, paid for by the engineer.[340]

A modular port scheme exploits the same generality in the other direction: every slot is the same connector into the mainboard, and each removable module converts it out to a display protocol, a network connection or a legacy port while passing through the full charging power.[717] Because the interface is documented, third parties can design their own modules for such a machine.[600]

## Cables

Convergence on one connector did not converge the cables: differently specified cables that look identical support different combinations of features, and some carry identification chips to declare what they are.[346] Every cable or adapter that does anything beyond basic USB contains a microcontroller, which changes what a cable is from a passive object to a computer of unknown provenance.[346]

Cables are a common root cause of faults. Trying a different cable belongs near the top of the list when a board will not enumerate, ahead of hours of investigation.[470] A cable can produce a signal-integrity problem that looks like a board problem: added bypass capacitors helped a little in one case, but the actual fault was an out-of-specification cable without the shielding it should have had.[450]

## Security characteristics

The embedded electronics in cables and adapters create an attack surface. Opening one adapter revealed a display-protocol conversion chip, a power delivery chip and a microcontroller with direct firmware update left enabled, so its firmware could be read out and replaced.[346] The consequence is that a single plug can enumerate as a display, a charger, a network adapter, a keyboard and a mass storage device at once, connecting every standard input and output path of the computer to hardware whose contents are unknown until it is plugged in.[346]

## Design practice and failure modes

The most useful thing to know starting out is how little is needed for the common case: to replace an older USB port with this connector, tie the two candidate positions for the data lines together, wire them in as before, and add a pull-down resistor on the configuration lines.[340] For a device that only wants the new connector at legacy speeds, that compatibility is the whole story — changing connector needs very little else.[421] Some products adopt the connector purely for its mechanical robustness and power handling while running data at serial-port speeds that the first USB generation could have carried.[434] Whether the layout is demanding depends entirely on speed: at low rates the connector is undemanding, but moving gigabits per second across it is not a first layout.[421] During a migration it is worth carrying both connectors on a prototype with a switch between them, both to prove the new one works and to find out what users actually think of having the choice.[475]

- A pull-up tied to the bus voltage on the assumption that it is always five volts will destroy microcontroller input pins the moment the rail negotiates up to twenty.[340]
- Protocol violations are enforced in firmware in a way they were not on the older bus: a device that misbehaves is hard-reset and has its bus voltage cut rather than tolerated, which makes a protocol analyser close to mandatory because otherwise the only visible symptom is a link that keeps resetting for no stated reason.[340]
- A device operating near the top of the link's data rate can be tipped over the edge by the path rather than the device: an adapter to the older connector plus the internal ribbon run to the motherboard lost enough margin that the device failed well below its maximum resolution, and plugging the same device straight into a port on the back of the machine fixed it. The general lesson is that a marginal high-speed link should be tested on the shortest, most direct path before anything else is suspected.[597]
- A product that supports only one proprietary fast-charge scheme inherits a compatibility problem that can be fatal to it: the overwhelming majority of battery packs already owned will not implement that scheme, and there is no fallback at lower power.[421]

A phone can serve as a debug terminal: connecting a development board port-to-port and opening a serial session in a phone terminal application gives shell access and log output without a laptop, provided the board's firmware presents a serial device over USB.[713]

## Cost considerations

The connector costs about twice what the older micro-USB connector does, which is not negligible on a product engineered down to a few dollars where the fixed costs of test and assembly already dominate.[648] Going the other way, fitting a second legacy connector costs about as much as including a small adapter in the box, so a single modern connector plus an adapter bought in bulk is the cheaper way to satisfy everyone.[434]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 240 | Compare and Contrast Tech Entitlement - Worldly Working Wonks | https://theamphour.com/240-compare-and-contrast-tech-entitlement-worldly-working-wonks/ | March 10, 2015 |
| 262 | Jobs For Weirdos | https://theamphour.com/262-jobs-for-weirdos/ | August 12, 2015 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ | June 30, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 470 | Just Add Salt | https://theamphour.com/470-just-add-salt/ | December 8, 2019 |
| 475 | An Interview with Christina Cyr | https://theamphour.com/475-an-interview-with-christina-cyr/ | January 19, 2020 |
| 496 | Drab Olive | https://theamphour.com/496-drab-olive/ | June 14, 2020 |
| 497 | An Interview with Brock LaMeres | https://theamphour.com/497-an-interview-with-brock-lameres/ | June 21, 2020 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 597 | Wow, Dave REALLY likes Top Gun | https://theamphour.com/597-wow-dave-really-likes-top-gun/ | July 24, 2022 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 668 | 50.0000 Ohms | https://theamphour.com/668-50-0000-ohms/ | May 30, 2024 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
| 722 | AI Tooling with Matt Liberty and Luke Beno | https://theamphour.com/722-ai-tooling-with-matt-liberty-and-luke-beno/ | April 22, 2026 |
