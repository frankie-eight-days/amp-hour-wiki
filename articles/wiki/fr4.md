---
title: FR-4
concept: fr4
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

FR-4 is the designation in universal use for the standard printed circuit board substrate: a woven fibreglass fabric impregnated with epoxy resin, clad with copper foil.[345][428] The name itself denotes a flammability rating rather than a specific material, so two boards both described as FR-4 can differ substantially in their electrical properties.[345] The material dominates electronics manufacture because it combines mechanical rigidity, low cost, and adequate electrical performance across most applications; predictions that it would be displaced by optical interconnect have been made for decades without materialising.[165] Its limits — lossy dielectric, poor thermal conductivity, and loose tolerance on dielectric constant — define the boundaries at which designers move to metal-core, PTFE, or ceramic substrates.[63][107]

## Name and composition

FR-4 names a flammability rating rather than a material; what the industry means by the term is a particular class of woven fibreglass and epoxy mix.[345] The board itself is a glass fabric woven in both directions and encased in epoxy: the glass provides rigidity, strength, dimensional stability, and resistance to warping, while the epoxy acts as the glue holding the structure together.[428]

The older term "phenolic" originally described plastics made with phenol resins, such as Bakelite, and technically covers a whole class of composites that includes modern board laminate — which is why the same word can describe both a cheap single-sided board and, strictly, the glass-epoxy material universally called FR-4.[609]

## Electrical properties

### Dielectric constant and signal velocity

The dielectric constant quoted for standard laminate is nominal, around 4.3, and carries a tolerance that reflects the price of the material; tight, repeatable dielectric properties are a premium that a standard board does not include.[468] A signal propagates through the laminate at the speed of light in the material rather than in air, slowed by the square root of the dielectric constant — with a dielectric constant near four, a factor of two — which converts every trace length into a calculable delay.[252] Light covers a foot per nanosecond in air and about six inches per nanosecond in standard laminate, giving the rule of thumb that a nanosecond corresponds to roughly fifteen centimetres of trace, enough for mental timing arithmetic at a whiteboard.[252]

### Glass-weave effect

Cheaper board grades use a loose weave with visible gaps between the glass bundles, producing a checkerboard of glass and bare resin.[428] A controlled-impedance trace running over glass sees a different dielectric constant from one running over a gap, so its impedance depends on where it happens to sit relative to the weave — an effect measurable with a time-domain reflectometer.[428]

### Loss mechanisms

Two independent loss mechanisms bound a high-speed channel: conductor size sets the skin-effect loss, and the dielectric sets the dielectric loss.[77] Large conductors in an excellent dielectric carry signals remarkably fast at corresponding cost, while small traces on ordinary laminate are what limit how fast and how far a signal can travel.[77] The practical bound is a speed–distance product: a gigabit across ten inches works on any reasonable board material; ten gigabits across the same ten inches forces a conversation about materials; a hundred gigabits is a serious problem whose eventual escape is optical rather than better laminate.[77]

Copper foil is deliberately roughened where it meets the laminate to develop peel strength, and at very high data rates the loss depends acutely on that roughness — a surface that is too rough can double the loss.[476] Materials made for these speeds use smoother foil and sacrifice adhesion, to the point that traces can nearly lift off if handled carelessly.[476] A link between two entirely digital chips becomes an analog channel once it leaves the package: what matters is the frequency and time response of copper on laminate, and equalising for it is filter theory applied to a signal whose contents are irrelevant to the person designing the path.[476]

### Frequency limits and alternatives

Ordinary laminate can carry a 10 GHz radio and the radio will work; what it will not deliver is an excellent noise figure below about half a decibel, which is the point at which a design must move to a higher-performance substrate.[107] An 800 MHz instrument front end is achievable on standard laminate with disciplined, tight routing, but multiple gigahertz is where controlled-impedance materials become unavoidable — so the board technology, rather than the silicon, sets the price floor for a cheap fast instrument.[654]

High-frequency substrates built on PTFE or ceramics offer low loss tangent, different dielectric constants, and far better repeatability, but they take the board out of the commodity supply chain: the plating and etching chemistry differs, the softer material moves during processing, and multilayer construction becomes difficult, so most low-cost vendors will not quote them at all.[107]

### Parasitic capacitance

Where the laminate itself contributes the capacitance limiting a high-impedance divider, one remedy is to remove it: cutting the material away around the divider takes the dielectric out of the circuit rather than attempting to compensate for it.[180]

## Thermal behaviour

The laminate is a poor conductor of heat. Heating a board from below relies on conduction through the laminate, and where heat genuinely has to move through the board — high-power lighting being the common case — a metal core rather than glass and epoxy is the appropriate construction.[63]

Thermal mass, not just peak temperature, determines what survives a reflow profile: plastic connectors survive reflow because they are surrounded by air rather than in contact with anything that stores heat, while a connector resting against the laminate, which does retain heat, can melt.[436] Blackening of the laminate during reflow is evidence that the oven is misreporting its temperature rather than that the profile is aggressive: a station set to 220 or 240 °C may actually deliver considerably more, a common failing of cheap thermocouple front ends.[454]

Material choice also has consequences at end of life in aerospace applications. A small satellite built from aluminium, ordinary laminate, and standard solder burns up completely on re-entry and remains in the upper atmosphere as particles; a denser material such as tungsten would reach the ground, which is why the approval process treats material selection as a safety question.[497]

## Fabrication and machining

Milling standard laminate aerosolises fibreglass — glass shards small enough to be inhaled or to enter the eyes — which is why desktop milling machines typically use a softer prototyping material and why cutting real glass-epoxy demands extraction rather than an after-the-fact workshop vacuum.[345] Where laminate is to be milled, the enclosure and vacuum extraction are not accessories: the dust is the hazard, and a cheaper open machine can be made acceptable by adding extraction.[454] Reasons for milling genuine laminate rather than the softer prototyping material include thicknesses below the usual 1.6 mm, ordinary availability from bulk suppliers, better heat resistance, and a more robust copper bond — and the resulting prototype more closely resembles the production board it is meant to predict.[454]

Laser ablation works on the softer phenolic material but not on glass-epoxy laminate, for a specific reason: carbonising the epoxy leaves a residue that conducts, so a process that removes copper cleanly from one substrate leaves conductive tracks across the other.[686]

The economics of fabrication weigh against in-house board making. A properly made double-sided board costs a few dollars, leaving time rather than money as the justification for the machine: the only real argument is needing a board within the hour, and anything beyond a one-off is sent out anyway.[251] Boards as thin as 0.1 mm are available and are not exotic; the material is the same pre-preg stock that multilayer fabs already hold for inner layers, so obtaining them is a matter of finding a willing vendor rather than sourcing a special material.[412]

## Non-electrical uses and characterisation techniques

The laminate is a versatile mechanical material in its own right: scrap board stock, copper-clad or blank, makes excellent structural fibreglass and has been used, in one case, for high-strength rocket fins.[70] At the other extreme of density, a modern phone board is noticeably heavy in the hand because it is mostly copper with very little laminate — the substrate reduced to just enough to separate the layers, since anything more is volume that could have been conductor.[414]

Removing the solder mask over an area lets light pass through the laminate itself, which glows and diffuses, allowing an illuminated indicator to be built into the board with no additional parts beyond the emitter behind it.[642] In design tools, hiding the substrate in a three-dimensional board viewer and examining only the copper and vias is an effective way to learn layout, because it forces the mental jump from lines on a screen to a stack of connected conductors.[512]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 63 | Shop bots, 450 mm fabs & redFrog - Pick and Place Palillogy | https://theamphour.com/the-amp-hour-63-pick-and-place-palillogy/ | |
| 70 | Idiorhythmic IPC Inconcinnity | https://theamphour.com/the-amp-hour-70-idiorhythmic-ipc-inconcinnity/ | |
| 77 | An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry | https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/ | January 9, 2012 |
| 107 | An interview with Tony Long - Millimeter Microwave Magician | https://theamphour.com/the-amp-hour-107-millimeter-microwave-magician/ | August 5, 2012 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 180 | An Interview with Dave Taylor - Multi-talented Meter Maker | https://theamphour.com/180-an-interview-with-dave-taylor-multi-talented-meter-maker/ | January 13, 2014 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 345 | Milling About | https://theamphour.com/show-345-milling-about/ | May 30, 2017 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ | January 26, 2020 |
| 497 | An Interview with Brock LaMeres | https://theamphour.com/497-an-interview-with-brock-lameres/ | June 21, 2020 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 642 | Sad Violins for Superconductors | https://theamphour.com/642-sad-violins-for-superconductors/ | August 13, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
