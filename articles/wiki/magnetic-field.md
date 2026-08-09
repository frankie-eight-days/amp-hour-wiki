---
title: Magnetic Field
concept: magnetic-field
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A magnetic field is the field component that accompanies moving charge: around a current-carrying wire the electric field extends radially, at right angles to the wire, while the magnetic field forms circles around the wire whose direction follows the right-hand rule.[293] Because a changing electric field generates a changing magnetic field, which in turn regenerates the electric field, the pair is self-sustaining and propagates rather than appearing everywhere at once.[252][729] In practical electronics the magnetic field is what inductance quantifies, what near-field emissions consist of, and what produces the mechanical forces seen in high-current equipment.[252][385][472] Field and wave intuition of this kind is acquired mainly through years of hands-on experiment rather than study, and many engineers now designing 5 to 20 Gbit/s serial links have no working model of what a magnetic field is or how it affects their circuit.[77]

## Propagation and radiation

Signal propagation on an interconnect is self-sustaining. Applying a voltage between signal and return creates a changing electric field, which generates a changing magnetic field, which in turn regenerates the electric field, so the wave travels down the line.[252] Electromagnetic radiation has the same origin in time-varying currents: electrons oscillating back and forth generate a complementary magnetic field, and that changing magnetic field regenerates an electric field, producing a self-sustaining structure that propagates outward.[729]

## Inductance

Inductance is best defined as the efficiency with which a conductor generates rings of magnetic field lines, specifically the ratio of webers of field lines to amperes of current; doubling the current doubles the field lines but leaves the ratio unchanged.[252] Three physical properties set the inductance of an interconnect: width, length, and proximity to the return path. Spreading current over a wider conductor produces fewer rings of field lines, and a shorter conductor has fewer rings to count.[252]

Bringing the return path closer to the signal conductor lowers inductance because the return current circulates its field lines in the opposite direction and cancels those of the forward current.[252] Placing power and ground planes close together works on the same principle: the counter-propagating plane currents cancel each other's field lines, giving less total inductance and less voltage developed when the current changes.[252] Non-inductive wirewound resistors rely on the same cancellation, with the winding arranged so that adjacent turns carry current in opposing directions and their field contributions cancel.[252]

Driving an inductive load stores energy in a magnetic field and returns it later, offset in time rather than lost. On the electrical grid this circulating energy is reactive power measured in volt-amperes reactive, and reactive power controls voltage while real power determines frequency.[583] Grid loads are inductive in the overwhelming majority of cases, with capacitive loads confined to unusual industrial processes, so generation must be sized to supply the reactive component as well as the real power.[583]

### Limits of the lumped model

Lumped circuit modelling is valid only while structures are small compared with the wavelength; then energy stored electrostatically can be labelled a capacitor and energy stored in the magnetic field an inductor. When structure size approaches the wavelength the stored energy becomes distributed and those labels no longer separate.[459] Kirchhoff's current law is likewise a special-case derivation of Maxwell's equations and does not hold in the presence of a changing magnetic field, which is exactly what an inductor produces; in that situation the measured currents and voltages around a loop do not sum as the law predicts.[439]

Whether a voltage exists across a loop of wire linked by a changing magnetic field depends on the definition used. Treating voltage as available energy per unit charge means magnetic energy contributes voltage, whereas a strict path-integral definition denies it, so practising engineers and theoretical physicists can reach opposite conclusions about the same measurement.[562] In demonstrations where probe leads are moved around such a loop, the differing oscilloscope readings are real induced effects in the wire and coils; the disagreement is over whether those induced effects are called voltage, not over the measurement itself.[562] Circuit theory retains other abstractions that are physically inexact for similar reasons of convenience, such as conventional current direction and current flowing through a capacitor; in reality charge only accumulates on the plates, but treating the part as an impedance at frequency is easier to work with.[562]

## Near-field behaviour and EMC

In the near field, closer than a wavelength from the source, the magnetic and electric fields exist separately and require different probes; only at a distance on the order of a fraction of a wavelength do they combine into the familiar electromagnetic wave.[523] Close to a radiating product, especially where large currents flow, emissions are predominantly magnetic, so near-field probing uses an H-field probe — a small loop that can be built for a few dollars — held directly over the suspect component.[472]

Anything conductive placed within the near field of a radiator readily becomes part of the antenna and can dramatically alter its radiation pattern, an effect that is much weaker in the far field.[523] EMC chambers are intended to measure in the far field over a range typically running from 30 MHz to several gigahertz, but at the low-frequency end a small chamber is not physically large enough, so correction factors are applied instead.[523]

Deliberate near-field coupling is used offensively in electromagnetic fault injection, which drives a powerful current pulse through a small inductor held over a target chip; because the induced field follows V = L di/dt, a large rate of current change is what produces a field strong enough to disturb the device.[552]

## Mechanical forces

Mains-frequency hum from a transformer is usually mechanical: laminations that are not bonded tightly enough vibrate under the alternating magnetic field and its coupling, and the whole transformer can also vibrate against the chassis.[127] At higher currents the forces become violent. High-speed imaging of a high-current power distribution test can show conductors physically flinging apart under the magnetic forces produced by the current they carry.[325]

Motor inrush current is large enough that the magnetic fields it produces make industrial bus bars physically rattle against one another.[385] Bus bar temperature is therefore monitored in industrial installations, because repeated rattling loosens joints, loose joints begin micro-arcing, and an arc to ground at tens of thousands of amps is destructive.[385]

Controlled force at much smaller scale is the basis of printed actuators. A PCB coil actuator can be built against an N52 neodymium magnet, the highest available grade, so that energising the flat coil generates a field strong enough to lift the coil and move light payloads such as a printed wing, a mirror or a ping pong ball.[663]

## Sensing and measurement

A very large transient current can in principle be measured without contact by placing a coil around the conductor and sensing the magnetic field it produces.[236] Magnetic storage read heads followed a related progression: early hard drives of roughly 100 GB capacity used inductive coils as both write element and read pickup, and later generations kept inductive writing but replaced the read pickup with magnetoresistive and then giant-magnetoresistive elements.[169] A GMR read head is externally interchangeable with a Hall effect sensor — current is driven through one axis and a voltage whose polarity follows the applied magnetic field is measured across the other — but the underlying physics is a quantum effect, unlike the Hall effect.[169]

Magnetic fields can also be sensed directly by the body. A magnet implanted in a fingertip gives a tactile sense of magnetic fields, because the magnet physically moves in response to surrounding fields and that movement stimulates the nerves already present in the fingertip.[123] The stray field from a hard disk drive is strong enough to be sensed at a hand's distance this way, making disk activity such as a machine going into swap directly perceptible.[123]

## Modelling and visualisation

Finite element analysis, adapted from civil engineering, was used to model the magnetic fields of disk drive actuators so that the force produced per unit coil current could be mapped as a function of angle, since that force response acts as a gain block inside the servo loop.[144] A modern PCB routing tool can publish a 3D field solution for an uploaded board so the E and B fields can be inspected interactively, which also serves as a check that the simulated curl of the magnetic field around a current follows the right-hand rule.[626]

Magnetic field results from professional solvers such as ANSYS, CST, FEMM and openEMS can be brought into Blender and rendered on top of the actual PCB geometry, but the pipeline requires substantial glue code because every solver stores and exports its data differently.[695] Open source solvers such as openEMS write results in the standard VTK format, which can be imported into Blender through its Python console; KiCad and openEMS also expose Python, so the whole chain from board design to field visualisation can be linked with scripts.[695] Field solvers written directly in Blender's Python environment, released as the electromagnodes add-on, are limited compared with professional tools but are adequate for quickly trying coil concepts before moving a settled design back to a full solver.[695] Interactive rendering of perpendicular electric and magnetic fields over real board geometry is a more effective teaching aid than the traditional chalkboard convention of drawing crosses and dots for field direction, because a change to the model updates the visible result immediately.[695]

Fields can be made visible physically as well. Light painting traces an electromagnetic field in space by moving an LED driven from a detector through the field of a microwave horn while a camera holds a long exposure, mapping out the phase of the wave as a sine wave.[120]

## Applications in physics and instrumentation

The spin of an electron is the fundamental microscopic magnetic dipole of elementary particles; placed in a magnetic field it takes two basis states, up and down, which can encode a quantum bit.[498] One tesla serves as a reference for a strong laboratory field: the Earth's magnetic field in Sydney is roughly 60 microtesla, while a strong neodymium magnet reaches about 1.3 tesla, which is why small arrays of permanent magnets can substitute for a superconducting magnet in spin qubit work.[498] An electron spin in a one tesla field has a spin-up to spin-down energy splitting equivalent to 1.3 kelvin, which sets a hard operating ceiling, since above that temperature thermal noise swamps the state distinction and dilution refrigerators become necessary.[498] The nitrogen vacancy centre in diamond avoids that requirement in part, carrying a spin whose energy splitting is created by the crystal field rather than an applied magnetic field, giving an intrinsic splitting of 2.7 GHz that an external field can then shift.[498]

Conditions at the extreme end of this regime are severe. An experimental atomic-level storage scheme that manipulated nuclear spin required a magnetic field of 8.5 tesla, cryogenic temperatures near zero kelvin, and terahertz drive frequencies, and still held state for only a few hundred nanoseconds.[23]

Magnetic deflection is also used to separate matter by mass. Uranium-235 makes up about 0.7 percent of mined uranium, and separating it from uranium-238 is difficult because the two isotopes are chemically identical.[365] Calutrons, a form of cyclotron used at Oak Ridge for isotope separation, work by ionising uranium and bending the ion beam in a magnetic field; because the two isotopes differ in mass they follow different radii and land in separate collection buckets.[365]

Microwave tunable resonators exploit the field in a different way, built as a small sphere of an exotic magnetic material that behaves like a tiny tuning fork, with its resonant frequency set by an applied magnetic field.[107]

In a Hall effect thruster a heated cathode boils off electrons that become trapped in an applied magnetic field, creating a region of high electron density; neutral propellant gas flowing through that region is ionised by collision and the resulting positive ions are repelled out of the thruster by a nearby positively charged plate.[701] The cathodes are thermionic emitters descended from vacuum tube practice, using barium oxide in many designs and lanthanum hexaboride in others.[701]

## Magnetic stimulation of tissue

Transcranial magnetic stimulation can be improvised from an air coil of heavy wire held against the skull: current is built up in the coil and then abruptly interrupted, and the collapsing magnetic field induces current in the motor cortex that produces a visible muscle twitch.[75] The coupling of such a coil into tissue falls off with the square of distance, so the coil must be held essentially against the skull for the induced field to be effective.[75] A setup of this kind passes a large impulse current through the coil to target the motor cortex and produce an arm twitch, but its spatial selectivity is very coarse compared with targeted neural interfaces.[582]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 23 | The Innovation Speculation | https://theamphour.com/the-amp-hour-23-the-innovation-speculation/ |  |
| 75 | An Interview with Ben Krasnow - Sprauncy Saccadic Spintherism | https://theamphour.com/the-amp-hour-75-sprauncy-saccadic-spintherism/ |  |
| 77 | An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry | https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/ | January 9, 2012 |
| 107 | An interview with Tony Long - Millimeter Microwave Magician | https://theamphour.com/the-amp-hour-107-millimeter-microwave-magician/ | August 5, 2012 |
| 120 | Prototyping, Machining & Accelerators- Mugwumps Mulling Milling | https://theamphour.com/the-amp-hour-120-mugwumps-mulling-milling/ | November 4, 2012 |
| 123 | An Interview with Jon Oxer - Innoxious Implant Innovator | https://theamphour.com/the-amp-hour-123-innoxious-implant-innovator/ | November 26, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 144 | An Interview with Bob Davidson - Hoodied HP Hijinks | https://theamphour.com/the-amp-hour-144-hoodied-hp-hijinks/ | May 7, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 365 | Wait, why is Jeff glowing? | https://theamphour.com/365-wait-why-is-jeff-glowing/ | October 30, 2017 |
| 385 | An Interview with John Davis | https://theamphour.com/385-an-interview-with-john-davis/ | March 25, 2018 |
| 439 | Grow A Superbrain | https://theamphour.com/the-amp-hour-439-grow-a-superbrain/ | April 21, 2019 |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 498 | Quantum Computing with Andrea Morello | https://theamphour.com/498-quantum-computing-with-andrea-morello/ | June 28, 2020 |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ | December 27, 2020 |
| 552 | Shouting at chips with Colin O'Flynn | https://theamphour.com/552-shouting-at-chips-with-colin-oflynn/ | August 1, 2021 |
| 562 | Electroboom! | https://theamphour.com/562-electroboom/ | October 19, 2021 |
| 582 | The Same Wavelength | https://theamphour.com/582-the-same-wavelength/ | March 20, 2022 |
| 583 | The Smart Grid with Paul Zawada | https://theamphour.com/583-the-smart-grid-with-paul-zawada/ | March 27, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 663 | Motors on PCBs with Carl Bugeja | https://theamphour.com/663-motors-on-pcbs-with-carl-bugeja/ | March 25, 2024 |
| 695 | Making The Invisible, Visible with Sam Aldhaher | https://theamphour.com/695-making-the-invisible-visible-with-sam-aldahar/ | June 3, 2025 |
| 701 | Electric Propulsion with Todd Bailey | https://theamphour.com/701-electric-propulsion-with-todd-bailey/ | August 21, 2025 |
| 729 | The Terahertz Frontier with Greg Charvat of Teradar | https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/ | July 22, 2026 |
