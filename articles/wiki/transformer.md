---
title: Transformer
concept: transformer
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **transformer** is a passive electrical device that transfers energy between circuits through magnetic coupling between two or more windings, allowing alternating-current voltage to be raised or lowered while providing galvanic isolation. The transformer's ability to change voltage levels cheaply and efficiently is the fundamental reason alternating current was adopted for power distribution; nearly every other aspect of AC operation, reactive power in particular, is harder than the DC equivalent.[583] Conventional power transformers run at roughly 99 percent efficiency with extreme reliability,[717] and because every transformer is inherently bidirectional, the same device can step voltage up or down depending on which winding is driven.[671][14] Beyond power distribution, transformers underpin isolated power conversion, signal isolation, measurement, and a wide range of unconventional applications from medical stimulation to through-window power transfer.

## Efficiency and thermal limits

Large power transformers must operate far above 99 percent efficiency, and this can be established by argument rather than looked up: if a large unit were only 95 percent efficient, the resulting dissipation inside the device would destroy it, so real units cannot be anywhere near that figure.[583] Transformer losses appear as heat inside the windings, and an efficiency shortfall of even a few percent in a multi-megawatt unit melts the wire insulation and shorts the winding; the loss figure is therefore a survival limit rather than a running cost.[639]

This efficiency benchmark defines the bar for proposed replacements. Solid-state transformers suggested for existing distribution infrastructure typically achieve around 96 percent efficiency, which gives back several percent as heat across every megawatt passing through, compared against conventional units running near 99 percent and already extremely reliable.[717]

## Role in power transmission and distribution

### AC versus DC transmission

Alternating current was adopted for distribution because transformers make raising and lowering voltage easy.[583] High-voltage DC transmission must convert at both ends and accept the conversion losses, whereas AC transmission at 500 kV between major plants uses transformers that are already extremely efficient on generation that is already alternating; the case for DC therefore has to be won on distance rather than on efficiency alone.[205] The trade is explicit: conversion losses at each end are accepted in exchange for lower losses over the distance in between, making HVDC a length-dependent decision rather than a general improvement over the transformers on a distribution pole.[717]

### Distribution hierarchy

Distribution networks step voltage down in stages. A zone substation serving a suburb takes 66 kV down to 11 kV onto a bus, distribution breakers hanging off that bus feed the streets, and pole-mounted or pad-mounted transformers produce the final low voltage.[641] Line voltage can be estimated from the hardware: counting the skirts on an insulator gives a rough kilovolt scale, six skirts suggesting 66 kV and three suggesting 33 kV.[641]

### Measurement and protection

Substation measurement runs entirely on instrument transformers. A voltage transformer scales the bus voltage down to about a hundred volts, and a current transformer provides a proportional current at ratios such as 200 to 5 or 800 to 5.[641] Protection commissioning uses a programmable source capable of a thousand volts at any frequency and current, with logic inputs to observe the result: wrapping its output through a current transformer several times multiplies the injected current, and the instrument times the breaker's contacts opening in milliseconds so trip curves can be verified rather than assumed.[641] Substations are built with standby capacity and bus-tie breakers, so that a transformer locking out causes a tie breaker to close, either bringing in the spare transformer or transferring the load onto the remaining units.[641]

### System-level constraints

Power-line communication signals do not pass through a distribution transformer, so the network a given scheme can reach is bounded by the transformer rather than by the wiring; the approach consequently suits regions with large low-voltage networks per transformer.[583] Similarly, the distribution transformer, not the individual inverter, sets how much a group of connected houses can export, which is the physical reason coordinating rooftop generation has to happen above the level of the individual house.[583]

Large transformers have become genuinely difficult to source, so a failure is a schedule problem measured in months rather than a simple purchase; the usual fallback of buying from a large overseas supplier competes against that supplier's own domestic demand.[724] Grid infrastructure is also physically vulnerable in ways rarely designed for: a 2013 attack deliberately destroyed seventeen large transformers at a single substation by targeting the mechanics rather than firing at random.[612]

## Failure modes and protection

Mains hum from a transformer is mechanical: the laminations vibrate under the magnetic field when they are not bonded tightly enough or have lost their bonding, and the whole assembly can also vibrate against the chassis it is bolted to.[127]

A transformer imposes no current limit of its own, and a fuse in the circuit does not make the secondary safe to touch; enough current passes before the fuse clears to be lethal, which is what makes salvaged microwave oven transformers dangerous.[88] Failures can also propagate backwards through the device: in one case a secondary-side fuse clearing reflected back to the primary and pushed it into thermal runaway, an argument for protecting the primary rather than trusting secondary-side protection alone.[419] A transformer manufacturer will build a thermal fuse in line with the winding on request, set high enough that ordinary use and small surges never reach it; the trade is that it is a one-time device and the transformer is scrap once it operates.[419]

High-frequency noise passes straight through a mains transformer via the interwinding capacitance, so a linear supply is not automatically quiet at high frequency merely because it contains no switching stage.[462]

## Design and construction

Designing a transformer for a specific application—trading efficiency, cost, and size simultaneously—is genuinely specialised knowledge that most electronics engineers do not have and rarely need, because off-the-shelf parts and complete converter modules cover the normal cases.[5] Custom magnetics are a common point where a nearly finished power product stalls: missing an efficiency target can force a redesign of both the converter and its custom transformer, with that cost landing on top of a bill of materials that may already be too high for the market.[682]

In a linear power supply, the transformer and the enclosure carry most of the cost—a good 80-watt transformer is a substantial piece of iron—so cost reduction on such a product almost always targets the magnetics first.[122] A planar transformer can require several revisions with the manufacturer to meet specification, but ends up cheaper than a comparable quality custom-wound part as well as lighter.[432] Inductors, transformers, and antennas can also be formed directly from printed circuit board traces, costing nothing beyond the area they occupy because the copper is being etched anyway.[76]

A mains-frequency transformer can be operated at other frequencies and voltages if it is derated appropriately, which makes a stock 50 or 60 Hz part usable well outside its nameplate conditions.[88]

## Use in power conversion

### Switching topologies

Switching tens of thousands of times per second is what shrank the transformer, and with it the whole supply: the power that required a wall-wart in the 1980s now fits in a phone charger the size of a cubic inch.[361] The basic pattern behind most isolated converters is the push-pull arrangement, which alternates two transistors to drive a transformer or inductor from a DC rail, with rectification on the far side giving a stepped-up or stepped-down output; dedicated controller chips are available to drive the discrete devices.[9]

Treating a transformer as an inductor with a second winding coupled to it means an ordinary buck converter can drive one directly, opening up isolated and multiple-output topologies without a dedicated controller.[108] Replacing a buck converter's inductor with a coupled inductor yields a second output for very little: the primary still functions as the buck inductor while a secondary tapped off it behaves like a flyback, giving two rails from one magnetic component.[210] In a half bridge, the primary's midpoint ties between two DC-link capacitors so the winding sees half the link voltage, where a full bridge would apply all of it; the half bridge therefore trades higher primary current for lower switch voltage stress.[522]

A high-voltage supply can be built from a 10-to-1 transformer in a package a few millimetres across by treating one winding as a plain inductor: the winding is clamped to ground while it charges from the low rail, then released, and the secondary delivers ten times the flyback voltage through a diode into a capacitor.[637]

Efficiency and spectral cleanliness trade directly against each other in power conversion: driving a clean sinusoid through a transformer with transistors held in their linear region can leave the converter around twenty percent efficient, while hard switching recovers the efficiency at the cost of harmonics that must then be dealt with.[151]

### Regulation and measurement

Isolated converters can regulate either through an optocoupler carrying feedback across the barrier or by primary-side sensing, where what the primary winding sees during the flyback interval is enough to drive the control loop, removing the optocoupler and its aging characteristics from the design.[210] Measuring a converter's loop response rigorously means injecting a swept signal into the feedback divider through a small transformer and reading the result on a network analyser, which turns loop stability from an assumption into a measurement.[377]

### Isolation as the limiting constraint

Multi-channel mains dimming needs an independent floating reference per channel, and neither answer scales: one DC-DC converter per channel becomes absurd at sixteen channels, and a custom switch-mode supply with one secondary winding per channel hits the same wall from the transformer side.[524] At data-centre power levels the transformer, not the semiconductor, sets the topology: an 800-volt bus could in principle be switched down to 12 volts with a 1200-volt silicon carbide device, but only through a transformer too large to fit on the board, which is what forces a multi-stage conversion architecture instead.[719]

A converter described as transformerless usually means only its main conversion path: a hybrid inverter still carries a transformer for the battery side, and every transformer is inherently bidirectional whether or not the datasheet says so.[671]

## Signal isolation

Digital isolators work by placing two coils between two dies inside a single package—a transformer small enough to be part of the packaging—which is how isolated USB and similar interfaces are built without an optocoupler.[94] A classic application-note thermocouple circuit sends data across an isolation barrier by driving one side of a transformer with logic gates, and it remains electrically sound, but with integrated parts now matching or beating that performance, reproducing it from discretes is hard to justify on a commercial design however instructive it is.[573]

## Coupling, bidirectionality, and unconventional applications

Wireless power transfer is inefficient for a structural reason rather than an engineering shortfall: the two coils are loosely coupled where a transformer's windings are tightly coupled, and the efficiency follows the coupling.[172] Inductive coupling through a barrier is nonetheless usable at surprising distances—a through-window power link designed by an RF engineer works across about thirty centimetres of glass, far more than the millimetre-scale gaps usually associated with the technique.[664]

Because transformers work in both directions, bidirectionality is exploitable: a salvaged distribution transformer run backwards steps a wall outlet up to very high voltage, and with a voltage multiplier behind it this is how improvised high-voltage supplies are built.[14] Transcranial magnetic stimulation is built as one half of a transformer with the body as the other: a current rising at roughly five thousand amps per second produces a field change fast enough to induce current locally in tissue.[75] An induction motor can be modelled as a set of transformers whose secondary sweeps past the primary, coupling energy magnetically as it goes—which also explains why the same machine recovers energy during regenerative braking without separate hardware.[168]

A commodity ATX supply is a cheap source of raw power for bench work: the 5-volt rail carries twenty to thirty amps, and boosting or push-pulling that through a transformer produces a bipolar rail at high current for a fraction of the cost of a laboratory supply.[199]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ | |
| 9 | From Boston In Boxers? | https://theamphour.com/the-amp-hour-9-from-boston-in-boxers/ | |
| 14 | China, Entrepreneurs and Blue Collar Reality | https://theamphour.com/the-amp-hour-14-china-entrepreneurs-and-blue-collar-reality/ | |
| 75 | An Interview with Ben Krasnow - Sprauncy Saccadic Spintherism | https://theamphour.com/the-amp-hour-75-sprauncy-saccadic-spintherism/ | |
| 76 | Fremescent Floccose Fortification | https://theamphour.com/the-amp-hour-76-fremescent-floccose-fortification/ | January 2, 2012 |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 94 | Gnomic Gazumping Gobemouche | https://theamphour.com/the-amp-hour-94-gnomic-gazumping-gobemouche/ | May 6, 2012 |
| 108 | Mars, Makerbot & Power Outages - Reprobate Replicator Replication | https://theamphour.com/the-amp-hour-108-reprobate-replicator-replication/ | August 12, 2012 |
| 122 | Processors, CEOs & Soldering irons - Plentiful Perfunctory Programs | https://theamphour.com/the-amp-hour-122-plentiful-perfunctory-programs/ | November 19, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 151 | Google Glass, Lean Startup and VotC - Initializing Instructed Interviews | https://theamphour.com/the-amp-hour-151-initializing-instructed-interviews/ | June 24, 2013 |
| 168 | Specialized and/or Open Source Test Gear and Dev Boards - Vacation Videography Vorboten | https://theamphour.com/168-specialized-and-open-source-test-gear-and-dev-boards-vacation-videography-vorboten/ | October 21, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 199 | The 2014 Maker Faire Show - Traveling Technology Trangam | https://theamphour.com/199-the-2014-maker-faire-show-traveling-technology-trangam/ | May 19, 2014 |
| 205 | Solar Factories and HVDC Lines - Pollent Power Pushing | https://theamphour.com/205-solar-factories-and-hvdc-lines-pollent-power-pushing/ | June 30, 2014 |
| 210 | Risky Components and Hardware Innovation - Slipshod Shack Shutdown | https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/ | August 5, 2014 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 419 | Feels over reals | https://theamphour.com/419-feels-over-reals/ | December 9, 2018 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 583 | The Smart Grid with Paul Zawada | https://theamphour.com/583-the-smart-grid-with-paul-zawada/ | March 27, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 639 | Daaaamn We're Duuuummmb | https://theamphour.com/639-daaaamn-were-duuuummmb/ | July 17, 2023 |
| 641 | Power Transmission with Toby Robb | https://theamphour.com/641-power-transmission-with-toby-robb/ | July 31, 2023 |
| 664 | Simulating doors falling off | https://theamphour.com/664-simulating-doors-falling-off/ | April 3, 2024 |
| 671 | NDA Sideshow | https://theamphour.com/671-nda-sideshow/ | June 19, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
| 719 | Inventing the Power MOSFET with Alex Lidow | https://theamphour.com/719-inventing-the-power-mosfet-with-alex-lidow/ | March 20, 2026 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
