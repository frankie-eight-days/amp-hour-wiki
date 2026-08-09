---
title: Relay
concept: relay
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A **relay** is an electrically operated switch in which a magnetic coil physically moves a strip of metal into contact with another piece of metal to make or break a connection.[94] Because the control side and the switched side are separate, a relay provides galvanic isolation between the driving circuit and the load, and in one of its states a mechanical relay consumes no current at all.[93] Relays formed the basis of early computing and telephone switching and remain in use wherever contacts must carry large currents, exhibit near-zero leakage, or be driven from simple low-power control signals.[77][94][607]

## Construction and operation

A conventional electromechanical relay consists of a coil and a contact assembly: energising the coil generates a magnetic field that pulls an armature, closing (or opening) the contacts.[94] The coil and the switched contacts are electrically distinct, a point that practitioners identify as a common source of confusion: a university lab supervisor reports that students routinely cannot operate a relay because they do not realise a separately driven coil exists inside the package.[127] Unknown switch or relay terminals can be identified empirically by ringing them out with an ohmmeter rather than relying on pole-and-throw nomenclature.[127]

At extreme current levels the same principle scales up physically: switching 5,000 amps required a purpose-built pneumatic contactor in which a large ram forced one metal plate against another, the plates themselves forming the relay contact.[546]

The switching hardware in common use spans several distinct families with different terminal arrangements: miniature reed relays, solid-state relays, and conventional electromechanical relays in a range of sizes.[127]

### Reed relays

A reed switch on its own is a sealed glass tube containing two contacts, with no coil; only the coil-plus-switch assembly constitutes a reed relay.[88] Reed switches are a specialist product category with dedicated manufacturers, such as Mida, that build essentially nothing else, and the manufacturing process involves a surprising number of high-precision steps.[88]

Reed relays are the preferred choice for switching low-level signals, where contact quality and low leakage matter more than current-carrying capacity.[94] A good low-power reed relay needs only about five milliamps of coil drive current, which sets the benchmark any miniature relay alternative has to beat.[94]

### MEMS relays

MEMS relays exist as very small single-pole double-throw parts in LGA packages, offering mechanical contact behaviour at chip scale.[94]

## History

Early computing was built from relay logic, and engineers pushed relay technology to the upper limits of its speed capability before moving to vacuum tubes.[77] Relay-based machines were limited not only by speed but by heat dissipation and packaging problems, the same class of physical limits that later recurred with tubes, transistors and integrated circuits.[77]

Magnetically shielded ultra-miniature relays were developed for telephone switching exchanges, where thousands of lines had to be cross-connected in a small volume.[94]

Electromechanical pinball machines implemented scorekeeping, carry, reset and target logic entirely from relays, stepper units and solenoids, with no processor of any kind.[485] The programmable logic controller was later created to replace plant control panels that had been built from relays, switches and indicator lamps with a single reprogrammable box, and ladder logic was chosen as the PLC programming model specifically so that plant electricians and technicians could apply their existing relay-logic knowledge without learning a new discipline.[620]

## Failure modes

### Mechanical contact phenomena

The intrinsic speed limit of relay logic came from mechanical contact bounce: the moving levers ring rather than settling cleanly, which corrupts the switched signal.[77] Synchronously switching a large bank of relays couples mechanically through the chassis; the whole machine can vibrate hard enough to cause bit errors in unrelated parts of the system.[77]

Relay contacts wear mechanically from repeated impact, and any air inside the package allows the contact surfaces to oxidise over time.[94] Arcing at the contacts pits the metal and alters the surface material, so a worn relay can develop non-linear, rectifying behaviour instead of acting as a clean switch.[94] In fault diagnosis of switched drive systems, a permanently running load such as an ABS pump points to a shorted switching element — a shorted motor, a shorted drive transistor pair, or welded relay contacts, depending on which drive topology the unit uses.[664]

Where cycling is continuous, contact ratings dominate design: a domestic PIR alarm sensor uses a relay rated for ten million operations, because the contact cycles every time motion is detected, around the clock for years.[94]

### Magnetic interference

Because the contact armature is moved magnetically, a stray external magnetic field can pull the contacts together and close a relay that was never commanded on.[94] Packing relays tightly, as in a switching matrix, lets their coil magnetic fields couple into neighbouring relays and interfere with them; the fix is to specify magnetically shielded relays rather than trying to space ordinary parts apart.[94] High-specification shielded relays of this class cost on the order of ten dollars each even in volume.[94]

### Leakage in matrices

Off-state leakage adds in parallel across a matrix: an individual relay may offer about two gigaohms of open impedance, but a thousand of them in parallel behave like a much lower resistance and degrade signal integrity.[94]

## Driving relays

Relay coils are inductive loads and need a freewheeling, or flyback, diode across the coil to clamp the kickback transient generated when drive current is removed.[551] Inductive kickback transients are a credible cause of downstream damage: a Raspberry Pi CM4 already running near its voltage limit failed, with spikes from the upstream switching circuit the suspected trigger.[551] An open-drain output can sink current into relay coils and solenoids, but it cannot drive an H-bridge, which requires both high-side and low-side drive.[600]

## Relays versus solid-state switching

A latching or unenergised mechanical relay draws literally zero current in one of its states, which is why solid-state switches have not displaced relays despite vendors wanting to sell the replacement.[93] Mechanical relays remain attractive in precision analog signal paths because they have effectively zero leakage and very few parasitics, their main penalty being some added capacitance.[607]

The countervailing limitation is speed. For current-measurement range switching there are three options — relays, N-channel MOSFETs, or a mix — and relays, while clean, are far too slow for fast automatic ranging.[293] The audible clicking of a bench multimeter changing ranges is relay actuation, and it is a direct indicator of how slow relay-based range switching is compared with FET switching.[607] Replacing relay range switching with MOSFETs allows the range decision to be made in under a microsecond using dedicated comparators and a separate analog channel feeding an FPGA, though the solid-state switches must be driven fast but with a controlled edge, because uncontrolled MOSFET gate drive injects charge into the measured signal.[607] Integrated parts with "current shunt" in the name are designed for power monitoring, not low-current measurement, making them a poor starting point for a microamp-capable instrument.[293]

Digital isolator chips provide an alternative to relays for galvanic isolation by placing two dies in one package with a pair of coils between them, forming an on-package transformer; the same technique now supports isolated DC-to-DC conversion as well as isolated data links such as USB.[94]

In power electronics, automotive ABS pump drive moved from a relay in older designs to a totem-pole MOSFET pair in newer ones.[664]

## Applications

In industrial equipment the standby current budget is dominated not by the processor but by sensors, actuators and relays.[93] Industrial carrier boards offer relay modules as a standard option so a compute module can drive conventional 24-volt DC machine interfaces alongside opto-isolated IO and serial links.[608]

Switching the output of a rotary phase converter into a step-up transformer required a relay rated at 14 kVA, deliberately oversized from a calculated requirement of roughly four to four and a half kVA to add margin; the start-up sequence matters, because the transformer must be switched in only after the converter is already spinning, otherwise energising it can destroy the converter.[220] A safety interlock on delivery trucks uses a relay driven by one controller to signal a second controller that it is safe to release the handbrake, preventing rollaway while the engine idles to run the delivery pump.[266]

A Wi-Fi-connected garden controller switched AC outlets for pumps and lights through Omron relays, driven by temperature, humidity, light and soil-conductivity readings.[268] Off-the-shelf home automation relay boards are commonly specified around four channels rated for 240 volts at 20 amps.[683] A relay can also serve as a hard power kill for a networked appliance, physically cutting mains to a smart speaker so it cannot listen regardless of its firmware state.[335] Grid-tied solar inverters curtail output by simply opening relay contacts inside the box to disconnect from the grid, rather than by any sophisticated regulation.[702]

In a home-built transcranial magnetic stimulation rig, a relay is used to abruptly interrupt the current in a heavy-gauge air-core stimulating coil; the collapsing field induces current in nearby tissue, producing a visible muscle twitch. Because field strength falls off with the square of distance, the coil must be held essentially against the target to be effective.[75]

## Design and practice

Breadboard prototyping remains acceptable provided the builder respects its limits, and slow loads such as relay circuits fall comfortably inside those limits.[551] In a layered automation system, the firmware that actually closes the relay should be kept trivially simple and stable — listen for a signal, flip the relay — with changeable scheduling and priority logic pushed up to a higher-level interface.[654]

Distributor parametric search will not surface a part from qualitative requirements such as small and cheap; finding the right relay can mean guessing the one technology keyword under which the vendor indexes it.[94]

Debugging relay logic is a schematic-tracing exercise rather than a software one: the technician follows the circuit through each relay contact in turn, probing with clip leads and indicators to localise the fault.[485] The relay has been identified alongside the BJT and the SCR as a core device an electrical engineer must understand, with the observation that formal courses skip connections between them, such as treating an SCR as a solid-state relay.[109]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 75 | An Interview with Ben Krasnow - Sprauncy Saccadic Spintherism | https://theamphour.com/the-amp-hour-75-sprauncy-saccadic-spintherism/ | |
| 77 | An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry | https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/ | January 9, 2012 |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 93 | An Interview with Tom LeMense - Cacaesthestic Chronometric Carriwitchet | https://theamphour.com/the-amp-hour-93-cacaesthestic-chronometric-carriwitchet/ | April 29, 2012 |
| 94 | Gnomic Gazumping Gobemouche | https://theamphour.com/the-amp-hour-94-gnomic-gazumping-gobemouche/ | May 6, 2012 |
| 109 | An Interview with Larry Sears - Hexagram Hardware Holism | https://theamphour.com/the-amp-hour-109-hexagram-hardware-holism/ | August 19, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 220 | An Interview with Shaun Meehan - Doctiloquent Dove Deployer | https://theamphour.com/220-an-interview-with-shaun-meehan-doctiloquent-dove-deployer/ | October 13, 2014 |
| 266 | An Interview with Ronald Sousa of Hash Define Electronics | https://theamphour.com/266-an-interview-with-ronald-sousa-of-hash-define-electronics/ | September 8, 2015 |
| 268 | An Interview with Luke Iseman of yCombinator | https://theamphour.com/268-an-interview-with-luke-iseman-of-ycombinator/ | September 22, 2015 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 335 | When the TV watches you | https://theamphour.com/335-when-the-tv-watches-you/ | February 8, 2017 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 608 | Vapor Phase with Saber Kaygusuz | https://theamphour.com/608-vapor-phase-with-saber-kaygusuz/ | November 7, 2022 |
| 620 | Engineering Education with Dr Don Wilcher | https://theamphour.com/620-engineering-education-with-dr-don-wilcher/ | February 20, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 664 | Simulating doors falling off | https://theamphour.com/664-simulating-doors-falling-off/ | April 3, 2024 |
| 683 | Troubleshooting is the skill | https://theamphour.com/683-troubleshooting-is-the-skill/ | November 20, 2024 |
| 702 | Test Point Accupuncture | https://theamphour.com/702-test-point-accupuncture/ | September 14, 2025 |
