---
title: Inductor
concept: inductor
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

An **inductor** is the circuit element to which energy stored in a magnetic field is assigned, in the same way that a capacitor is the element assigned energy stored electrostatically.[459] The relation V = L di/dt serves as the working mental model for inductive behaviour: interrupting a current flowing in an inductor produces a voltage spike, the mechanism behind both boost-converter operation and relay-coil kickback.[276] Inductors are central to switching power conversion, filtering and sensing, but their size, cost, losses and integration limits make them a frequent design constraint, and faster switching devices matter in large part because they permit smaller inductors, which are among the heaviest and most expensive parts in a converter as well as its main source of stray magnetic field.[443]

## Lumped and distributed behaviour

The lumped identification of a component as an inductor, capacitor or resistor is valid only while the physical object is small compared with the wavelength of the signals passing through it.[459] Once structures approach the size of a wavelength, energy can no longer be localised as purely magnetic in one place and purely electrostatic in another, and the circuit must be treated as distributed rather than as separate inductors and capacitors.[459]

Kirchhoff's current law is itself a special-case derivation of Maxwell's equations and does not hold in the presence of a changing magnetic field, which is what an inductor produces; measured currents around such a loop do not sum to zero.[439]

## Ratings and the inductance–current trade-off

Within a single inductor series at a fixed physical size, current rating falls sharply as inductance rises: a 1 microhenry part rated at 1.8 amps may sit in the same series as a 100 microhenry part rated at roughly 100 milliamps.[488] The trade-off is mechanical: more inductance requires more turns of finer wire, so obtaining both high inductance and high current requires a physically larger part.[488] A requirement of around 2.3 amps in a small surface-mount inductor is demanding enough that general-purpose inductor sample kits will not contain a suitable part.[488]

Height is a first-order constraint. A height-constrained inductor can exhibit very low DC resistance, on the order of a milliohm or less, and still perform poorly because its core losses dominate; allowing a taller part lowers core loss and improves the overall result.[566] Mechanical z-height limits set by the product, rather than electrical requirements, frequently decide which inductor a power converter can use, so the strictness of a stated height limit is worth interrogating early in a design.[566]

## Failure modes

### Core saturation

When the magnetic core of an inductor or transformer saturates, the part stops behaving as an inductor and presents little more than the DC resistance of its winding, so current is limited only by the copper.[419] In a switching supply, saturation shows up as a primary-side meltdown with the secondary side intact and the input fuse blown, while the unit may still briefly power up and drive its display before failing.[419]

### Converter misbehaviour

An audibly singing inductor in a switching converter is a symptom of a badly compensated control loop rather than a defect in the inductor; a converter designed before high-value ceramic output capacitors were available can be destabilised by them and by its load.[188] Powering a boost converter from a source-measure unit into an active load can likewise cause the control loop to lose regulation, driving the output voltage too high and destroying the switching transistor, while the same board works normally from an ordinary bench supply.[623]

### Assembly and substitution errors

Because chip inductors and chip capacitors share the same passive packages, an assembly error in which inductors are populated in place of decoupling capacitors presents at power-up as an apparent short across the supply rail, the parts being indistinguishable by inspection.[239] Inductor orientation can also matter. Surface-mount air-core inductors differ between manufacturers in the axis of their winding — some wound with the coil cylinder lying flat on the board, others with it standing vertically — and in a differential LC filter two closely spaced horizontal-axis parts couple enough to act as a common-mode transformer, giving good common-mode rejection; substituting vertical-axis parts of identical value destroys that rejection.[169] In the diagnostic case described by Vincent Himpe, a qualified LC filter that failed on a customer board while simulation predicted correct behaviour was investigated by sweeping the filter, measuring the inductors in circuit, then desoldering them and measuring value, Q factor, drift and tolerance; when all of those came back within specification, the fault was localised to the physical arrangement rather than the components, a distinction that took days to isolate.[169] A vendor hardware design guide that must specify the orientation in which a switching-regulator inductor is installed indicates a marginal part choice; a larger inductor and different layout would remove the sensitivity instead of pushing the constraint onto assembly.[676]

## Use in power conversion

A push-pull controller alternately switches a high-side and a low-side transistor to drive a transformer or inductor, transferring power that is then stepped up or down and rectified on the far side.[9] A boost converter works by driving current through an inductor and abruptly interrupting it, so that the resulting voltage spike is rectified through a diode into an output capacitor; a complete implementation can consist of an inductor, a diode, two capacitors and a four-pin switching IC.[623] A transformer can be regarded as an inductor with a second inductor coupled to it, so a standard buck converter can drive a transformer winding rather than a plain inductor, and coupling a second winding onto a buck inductor gives the converter flyback-like behaviour in addition to its buck action.[108][210]

Processor core rails are supplied by the ordinary buck topology, taking anything from about 5 volts to 22 volts down to roughly a volt; at any appreciable power the single buck is replicated into a multi-phase buck of parallel switch-and-inductor sets sharing common input and output capacitors.[566] Paralleling N buck phases gives an effective inductance of L/N, so the converter can slew output current far faster and needs less output capacitance than a single phase attempting to supply 150 to 200 amps; the input and output ripple cancellation this yields depends on the quality of the layout.[566]

### Switching frequency

Switch-mode power supplies of the early 2010s typically topped out around 500 kilohertz, with a physically substantial inductor carrying on the order of an amp.[61] Motor-control PWM typically runs in the 10 to 30 kilohertz range, while digital power conversion runs at 100 kilohertz and above; the higher frequency is what allows digital-power inductors to be physically smaller.[212] Raising switching frequency reduces inductor size but eventually runs into a wall where parasitic capacitance and parasitic inductance in the layout and components dominate; the efficiency curve peaks and then falls, defining a sweet spot for the operating frequency.[61] At sufficiently high frequencies the required inductance becomes small enough that a loop of PCB trace can serve as the converter inductor in place of a discrete wound part.[61]

The penalty for low frequency is board area and cost. A device requiring several separately regulated high-current rails needs a switching regulator and inductor per rail, and the resulting inductors can occupy more board area than the FPGA or system-on-chip they supply.[156]

### Design procedure and alternatives

Designing a switching converter from a controller data sheet is a long calculation sequence, on the order of thirty equations, in which the inductor peak current is computed first, an inductor is selected against it, and that part's DC resistance is fed back into the loss calculation.[273] For production runs of only a handful of units, an off-the-shelf power module is usually cheaper than a discrete switching design, because the engineering time spent selecting the MOSFET and inductor, working the calculations and chasing possible oscillation dominates the component cost.[604]

Cleaning up a switching supply's output can be done either with a large output LC filter or with a tracking linear post-regulator; the tracking regulator costs efficiency, but a low-dropout part need only sit a few hundred millivolts above the output.[360] Output noise must be characterised across the whole load range rather than at one operating point, because output-capacitor effectiveness falls with rising current and interacts with the inductor and with a switching frequency that may itself vary with load.[360]

### High-current and integrated implementations

In a high-current isolated supply, the rectified transformer output is a square wave, so a large inductance follows the secondary diodes to smooth it.[522] Complete DC-DC converter modules are built as a small PCB with the inductor mounted on top and the controller die embedded inside the board, in an SO-8 sized footprint and costing under fifteen cents in quantity; higher-current variants up to about six amps use the same die with a larger inductor.[412] The Raspberry Pi RP2350 integrates a switching regulator that takes a 3.3 volt input and generates the core supplies, but still requires an external inductor and external capacitors.[676]

### High-voltage and LED drive

A 200 volt Nixie supply can be built as a flyback by treating one winding of a small 10:1 transformer as a plain inductor: the winding is clamped to ground to charge from a 5 volt rail and then released, and the ten-times voltage appearing on the secondary is dumped through a diode into a capacitor; in CNLohr's CH32V003-based implementation, a microcontroller GPIO with 50 milliamps of drive capability switched the flyback MOSFET directly, without a separate gate driver, with a second GPIO used for feedback.[637]

An LED can be driven from an inductor's flyback rather than from a series resistor: a short PWM-triggered current pulse energises the inductor and the LED sits across it as the flyback element, with brightness set by the current and duration of the energising pulse.[465] Ted Yapo's work on low-power indicators used this technique on the basis that an LED has one specific drive current, set by die size and device physics, at which it converts electrical energy to light most efficiently; efficiency falls above that current through droop and also falls at very low currents, so pulsing at the efficient current beats a large series resistor for a long-lived dim indicator.[465]

## Use in filtering and audio

Active filters built around amplifiers run out of usefulness above roughly five megahertz, so signal-conditioning filters at higher frequencies are built from real inductors instead.[392]

A class D amplifier needs a physically large output inductor, and the finite resistance of its winding dissipates enough heat at maximum volume to make thermal headroom a layout and packaging constraint alongside the space constraint.[474] A class D output stage uses two second-order LC filters whose inductors and capacitors must be arranged so that the fluxes cancel and the impedances at each end are balanced; an imbalance produces an audible click or pop at start-up and shows up on radiated-emission scans.[474] The efficiency for which class D amplifiers are known applies at high output levels; at normal low listening levels the loss in the output filter inductors dominates, and Jørgen Jakobsen reported that addressing that region cut power consumption there by a factor of ten.[338]

## Electromagnetic interference

Inductor values in shipping designs are routinely altered late and empirically to pass radiated-emissions testing; a documented case is a 20 microhenry change made for FCC compliance.[319] EMI reduction rests on understanding why low inductance and small loop area matter, so an EMI reference document that lists techniques without their underlying reasoning is a lookup aid rather than a substitute for the physics.[322]

## Construction and fabrication

Inductors and transformers are among the few components an engineer can practically fabricate by hand, which is why they remain accessible in through-hole construction.[76] Inductors, transformers and antennas can all be formed directly from PCB copper; because the board is being etched anyway, such structures cost nothing but the board area they occupy.[76] An extremely low-profile inductor can be built by winding the coil through the layers of a twelve- to sixteen-layer board and fitting a ferrite core through a hole drilled in the centre of the winding.[76] Salvage is also practical: the deflection yoke coil from a CRT television can be reused directly as an inductor of about 3 millihenries.[127]

Large inductors are not amenable to silicon integration or wafer-level assembly, so even a highly integrated single-chip or chiplet solution must place them on the package substrate or on the board.[499] Tuned circuits resonating at around 100 megahertz require inductors too large to integrate on a chip; Tom Lee's thesis work built an FM radio entirely in CMOS with no inductors by using gyrators, which synthesise an inductance from a capacitor and add electrical tunability at the cost of poor quality.[459] In an earlier era of precision passive filter manufacture, before tight component tolerances were available, production depended on in-house winding of inductors on dedicated machines and on individually measuring each capacitor and marking its actual value on the body, a practice Kendall Castor-Perry described from his own company's history.[476]

## Sensing and instrumentation

An inductance-to-digital converter senses metal in proximity by monitoring a resonant coil inductor, which is the operating principle of a stud finder.[329] Electromagnetic fault injection, as practised by Colin O'Flynn, uses an inductor as the probe tip and dumps a large, fast current pulse into it, since by V = L di/dt a strong localised magnetic field requires a large rate of change of current.[552]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 9 | From Boston In Boxers? | https://theamphour.com/the-amp-hour-9-from-boston-in-boxers/ | |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ | |
| 76 | Fremescent Floccose Fortification | https://theamphour.com/the-amp-hour-76-fremescent-floccose-fortification/ | January 2, 2012 |
| 108 | Mars, Makerbot & Power Outages - Reprobate Replicator Replication | https://theamphour.com/the-amp-hour-108-reprobate-replicator-replication/ | August 12, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 156 | Tesla, FPGAs and DigiKey - Zesty Zippy Zynq | https://theamphour.com/the-amp-hour-156-zesty-zippy-zynq/ | July 29, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 188 | Capacitors, Simulation and Closures - Deonerated Design Dealmaking | https://theamphour.com/188-capacitors-simulation-and-closures-deonerated-design-dealmaking/ | March 10, 2014 |
| 210 | Risky Components and Hardware Innovation - Slipshod Shack Shutdown | https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/ | August 5, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 273 | Part Choice Triathlon | https://theamphour.com/273-part-choice-triathlon/ | October 28, 2015 |
| 276 | Eating An Elephant | https://theamphour.com/276-eating-an-elephant/ | December 2, 2015 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 322 | World Trade Futurity (WTF) | https://theamphour.com/322-world-trade-futurity-wtf/ | November 9, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ | |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 360 | A Total 360 | https://theamphour.com/360-a-total-360/ | September 18, 2017 |
| 392 | An Interview with Matt Duff | https://theamphour.com/392-an-interview-with-matt-duff/ | May 13, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 419 | Feels over reals | https://theamphour.com/419-feels-over-reals/ | December 9, 2018 |
| 439 | Grow A Superbrain | https://theamphour.com/the-amp-hour-439-grow-a-superbrain/ | April 21, 2019 |
| 443 | An Interview with JP Norair | https://theamphour.com/443-an-interview-with-jp-norair/ | May 19, 2019 |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ | January 26, 2020 |
| 488 | Sowing Discord | https://theamphour.com/488-sowing-discord/ | April 12, 2020 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 552 | Shouting at chips with Colin O'Flynn | https://theamphour.com/552-shouting-at-chips-with-colin-oflynn/ | August 1, 2021 |
| 566 | Switching Converter Engineering with Carmen Parisi | https://theamphour.com/566-switching-converter-engineering-with-carmen-parisi/ | November 14, 2021 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 623 | Artisanal Crystals | https://theamphour.com/623-artisanal-crystals/ | March 12, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 676 | Moving House (And Lab) | https://theamphour.com/676-moving-house-and-lab/ | September 2, 2024 |
