---
title: Mosfet
concept: mosfet
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

The metal–oxide–semiconductor field-effect transistor (MOSFET) is a voltage-driven semiconductor switching and amplifying device, in contrast to the current-driven bipolar junction transistor.[589] The power variant of the device was developed at International Rectifier in the late 1970s, and the basic patents, held exclusively, returned close to a billion dollars in royalties before expiring.[719] Over the commercial life of the power device, on-resistance for a given die area has fallen from ohms to micro-ohms, a span of roughly six orders of magnitude.[719] The MOSFET is the transistor most commonly encountered in day-to-day design practice, ahead of the bipolar device.[725]

## History

The power MOSFET was developed at International Rectifier in the late 1970s by a very small group. Alex Lidow, working with graduate-school colleague Tom Herman, described his first challenge there as building a better transistor, the result being "something that's now called the Power MOSFET".[719] At the time, bipolar transistors dominated power work despite three compounding weaknesses: limited switching speed, a safe operating area problem that made them fragile, and limited gain.[719]

The HexFET structure followed from injecting extra charge into a region of the device that was too narrow, so that the region presented itself as wider to the electrons; the second attempt at building the device went from 2 ohms to 0.7 ohms of on-resistance.[719]

In the later 1980s the insulated-gate bipolar transistor (IGBT) emerged as a structural variant of the FET, trading the low-resistance N-plus substrate for a P substrate. This made the device behave partly like a bipolar and gave it lower effective on-resistance specifically at high voltages, which is why high-voltage work moved to IGBTs while superjunction devices such as CoolMOS answered from the other direction.[719]

As gate lengths have shrunk in integrated processes, device geometry has gone vertical to recover gate surface area within the same die footprint; the FinFET names this shape rather than a new device type.[106]

## Wide-bandgap successors

Silicon is cheap fundamentally because the bond between its atoms is weak, so little energy is needed to form the crystal. Silicon carbide's strong bond is exactly what makes it a wide-bandgap material, and also what makes it permanently more expensive: no process change can make a silicon carbide crystal as cheap as silicon.[719]

Growing gallium nitride as a micron-thin layer on standard silicon, demonstrated by Japanese researchers in 1999, sidesteps the compound-semiconductor cost problem by delivering the wide bandgap without paying to grow the expensive crystal.[719] Gallium nitride wins on three independent counts: higher electron mobility; a wide bandgap that lets high-voltage terminals sit closer together without breaking down, so the device can be physically smaller; and a two-dimensional electron gas running along the surface that supports very efficient lateral devices, theoretically thousands of times more efficient than a vertical silicon structure.[719]

## Device structure and behaviour

A power MOSFET's channel is roughly half a micron long and on the order of ten metres wide — an older device perhaps five — folded up inside a package small enough to hold. This is the physical consequence of the design goal of a channel as wide and as short as possible.[196]

A power MOSFET's gate-drain capacitance depends on whether the device is conducting, because the channel lies between gate and drain and its state changes the effective separation. In a lateral integrated MOSFET, where gate and drain sit side by side above the channel, the capacitance barely moves, which is why the two device types require different charge models.[196] The gate-drain capacitance is the Miller capacitance and it determines switching behaviour.[196]

The Miller plateau — the gate charge levelling off at a particular gate-source voltage rather than continuing to ramp — is mostly a concern in high-current driver and motor work, and gate series resistance is the usual lever for managing what happens through it.[500]

Because the bipolar transistor is a current-driven device and the field-effect device is voltage-driven, parameter names that carry over between the two families usually mean something else: beta, for example, is a bipolar parameter meaning current gain and has no standard meaning for a MOSFET.[589]

## Integrated devices

Devices drawn close together on a die match each other extremely well, but their absolute values move roughly ten percent from wafer to wafer, because a few microns' difference anywhere in the stack-up changes how every device on that wafer performs.[672] Integrated design therefore works in ratios rather than absolute values: a divider made from three identically drawn resistors still produces the same output fractions on the next wafer even though every resistor's absolute value has shifted.[672]

A CMOS inverter is two complementary MOSFETs in a totem pole, with their gates tied together as the input and their outputs tied together; the signal drives both gates at once.[351]

## Modelling and simulation

Building a simulation model from a datasheet alone is essentially impossible for a bipolar transistor because the quasi-saturation region is never documented well enough. For a MOSFET it is achievable and good enough for switching power supply work, but only by bringing assumptions the datasheet does not supply.[196] The workable procedure is to build test fixtures that reproduce the datasheet's own curves — output characteristics, on-resistance against gate voltage, and gate charge — then adjust model parameters until the simulated curves match. Even done expertly this takes around 45 minutes per device.[196]

Frequently no physical device matches its own datasheet, because different curves were extracted from different sample transistors: the gate-charge plot may come from a part with a different threshold voltage than the one used for the output characteristics, so no single model can satisfy both.[196] An alternative to modelling an unmodelled part is to sort the simulator's existing device library by gate charge and then by on-resistance, find an entry matching both, and simulate with that; the sourcing decision is then independent of which model was simulated.[196]

Expecting a model from the manufacturer misreads the skill involved: simulation plays no part in designing a power MOSFET, so the people who build the best devices have no particular reason to be able to model them.[196] A model without a state-dependent charge model does not merely lose accuracy — it does not behave like a power MOSFET at all, which is why simulated waveforms failed to resemble bench measurements until a dedicated model was written.[196]

A simulator's default beta parameter for a MOSFET is sized for a small-signal device; at an amp of current through a power device it produces an inexplicable voltage drop across the part until the value is raised to something like eighty or calculated properly.[589]

## Applications and design practice

### Power conversion

A synchronous converter is any conventional topology with the rectifying diode replaced by an actively switched FET, which removes the diode's forward conduction loss at the cost of needing timing and control that a diode requires none of.[565] Converters that must start from nothing keep an ordinary diode for the initial bootstrap and then switch to a synchronous rectifier placed in parallel with it once the internal circuitry has power, taking the efficiency penalty only during start-up.[217]

For a buck converter, the two switching devices can be bought as one package with the source of one already tied to the drain of the other and separate high and low gate pins, which simplifies layout and cuts the losses that the interconnection between two separate parts would add.[340]

A gate driver is not always required: a microcontroller pin rated for 50 milliamps of drive can switch a MOSFET directly in a low-power high-voltage supply, with one further pin taken back as feedback.[637] A high-voltage flyback supply can be built by treating one winding of a small step-up transformer as a plain inductor: clamp it to ground while the other side charges from the low-voltage rail, release it, and the secondary presents ten times the flyback voltage into a diode and capacitor.[637]

In an electric drivetrain the loss budget is dominated by conduction drops at every element: the inverter's switch drops account for about two percent at full power and the battery's internal impedance about three percent, which makes low impedance everywhere a system-level requirement rather than a component preference.[112]

### Mains switching and dimming

Trailing-edge dimming needs a bidirectional switch built as two N-channel MOSFETs in inverse series with their sources tied together. Those joined sources are the drive reference and they swing with the mains, so every channel needs its own completely floating gate supply — a problem that multiplies with channel count.[524] Mains dimmers are hard to protect against short circuits because fault currents rise so fast that the semiconductor fails before the fuse does.[524] The answer is to detect the fault within the half cycle rather than to fuse it: an isolated Hall-effect sensor in an SO8 with an internal half-milliohm shunt reports plus or minus ten amps as zero to 3.3 volts centred at 1.65 volts, and cutting the drive as the current climbs from the zero crossing saves the device even when switched into a dead short.[524] Because the sensed current is bipolar around a mid-rail reference, a windowed analog-to-digital converter that flags when the signal leaves a band between two limits does in one peripheral what would otherwise need a comparator whose polarity is flipped every half cycle.[524]

### Switching and protection roles

When a module's own low-power modes will not meet the current budget its datasheet implies, cutting its supply entirely with a low-side N-channel switch is the reliable fallback; the firmware then has to take on measuring the available energy and adapting its measurement and upload rates to it.[603]

Switching resistors in and out with MOSFETs under plain digital control is enough to make a regulator's set point or a load's current programmable, with no analog output anywhere in the design.[607] A design can dispense with dropper resistors entirely by relying on the on-resistance of a logic chip's high-side output devices, and that effective output resistance is derivable from the datasheet's output-high voltage drop at a stated output current.[598]

Driving anything outside the board from a single-board computer should go through a FET on a separate power domain, so a fault destroys the transistor or blows the domain's fuse rather than the processor.[339]

Supply glitching for fault injection needs no more than a MOSFET used as a crowbar for a few nanoseconds: it drains the bypass capacitance, the rail droops while the capacitor recharges, and that droop is the attack.[239] The simplest possible backscatter retroreflector is a MOSFET with an antenna on it, shorting the antenna under gate control; more elaborate modulation at the reflector is possible but the minimal version needs no more parts than that.[214]

### Automotive

An automotive high-side switch is a MOSFET with protection built in — against transients, over-temperature and over-current — driven from a plain logic level, so the designer gets the protection behaviour without designing any of it.[568] A vehicle's 12-volt line carries enough transient energy that an ordinary DC-DC converter is likely to fail in service, so the automotive-rated part is a reliability requirement rather than a certification formality.[568]

### Comparison with relays

Where a low-impedance path has to hold its value against time and temperature, a MOSFET is a poor substitute for a relay: on-resistance moves with temperature, and the device's own dissipation heats it, so there is no guaranteed constant value without adding thermal control around it.[94] The trade runs the other way on lifetime: a relay is a physical mechanism with a rated life that changes as it wears, while a semiconductor switch kept inside its thermal ratings has no wear mechanism and can be operated indefinitely.[94]

## Failure modes and constraints

Discrete MOSFETs do not carry ESD protection by default. Protection requires a specific suffixed variant, only a small number of parts offer it, and many of those are dual or quad devices intended for logic-level input protection rather than general switching. Once a design has established that it needs the protected variant somewhere, consolidating onto it across the whole board is usually right: the parts differ by a few cents, and mixing two nearly identical devices leaves the reasoning invisible to whoever repairs the board later.[580]

A shorted switch does not only stop the circuit working: one holding a load permanently connected deep-discharged the battery pack to zero volts, destroying cells that could not afterwards be recovered by any slow-charge revival attempt.[580]

Package size and safe operating area move together: larger power devices give more margin, and shrinking the package quickly runs the designer out of available parts. Intermediate surface-mount packages such as the D2PAK — essentially a TO-220 with the tab folded for reflow — exist to fill the gap.[61]

Some MOSFETs are export-controlled and cannot be bought outside the United States, because devices fast enough for certain switching applications fall under weapons-related restrictions — a sourcing constraint that has nothing to do with the electrical specification.[602]

Totem-pole CMOS outputs can degrade asymmetrically: when the upper device weakens the pin can no longer pull high, and because a totem pole has no pull-up resistor the failure is total. Adding an external pull-up recovers it, but at 25 MHz into a capacitive bus that means a hundred ohms and tens of milliamps.[482] Logic inputs carry a maximum input slew rate — on the order of 500 nanoseconds for common HC-family parts — and a signal slower than that voids the guarantee: the input can enter a metastable state, and a clock line doing so will oscillate unpredictably rather than simply run slow.[482]

Slowing an edge cuts the impulse current delivered into the trace capacitance and so lowers average power, but the same slow edge burns power in a MOSFET crossing its transition region and can push non-Schmitt logic inputs into instability; the optimum is a balance rather than a direction.[322]

A single shared dropper resistor for a multi-segment display makes brightness depend on how many segments are lit, because the available current is shared among whatever is on, visible as digits that dim as more of them illuminate.[598]

At a build quantity of ten, selecting the switching device and inductor, running the calculations and then debugging oscillation costs more than an off-the-shelf converter module; the design effort only pays back at volume.[604] Comparative part selection work — buying a spread of candidate devices, testing them against each other, plotting the results and writing it up — happens constantly inside companies and essentially never gets published, so the same characterisation is repeated privately many times over.[477]

## Fabrication

MOSFETs are the easier device to fabricate outside a fab: a bipolar transistor needs a very accurate furnace because the emitter and collector diffusions must meet the base without overrunning it, a process controlled by temperature and time together, whereas a MOSFET needs an oxide grown to a thickness that can be judged by its colour.[52]

## Extreme-scale devices

A single-electron readout device used in quantum computing is a deliberately non-linear MOSFET around 50 by 100 nanometres: at nanometre distances, moving one electron nearby shifts the bias point by the equivalent of some tens of millivolts, which is enough to switch the device from off to on when the whole system is held near absolute zero.[498]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 52 | An Interview with Jeri Ellsworth - Carnassial Chip Chemicals | https://theamphour.com/the-amp-hour-52-carnassial-chip-chemicals/ | |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ | |
| 94 | Gnomic Gazumping Gobemouche | https://theamphour.com/the-amp-hour-94-gnomic-gazumping-gobemouche/ | May 6, 2012 |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 112 | An Interview with Bob Simpson - Ardent Automotive Artisan | https://theamphour.com/the-amp-hour-112-ardent-automotive-artisan/ | September 9, 2012 |
| 196 | An Interview with Mike Engelhardt (Re-broadcast) | https://theamphour.com/196-an-interview-with-mike-engelhardt-re-broadcast/ | April 28, 2014 |
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 217 | 3D Printed Shark Jumps - Edifying Edison's Energy | https://theamphour.com/217-3d-printed-shark-jumps-edifying-edisons-energy/ | September 22, 2014 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 322 | World Trade Futurity (WTF) | https://theamphour.com/322-world-trade-futurity-wtf/ | November 9, 2016 |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ | March 12, 2017 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 498 | Quantum Computing with Andrea Morello | https://theamphour.com/498-quantum-computing-with-andrea-morello/ | June 28, 2020 |
| 500 | Two and a Half Orders of Magnitude | https://theamphour.com/500-two-and-a-half-orders-of-magnitude/ | July 12, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 568 | YouTube to Consulting with Florin of Voltlog | https://theamphour.com/568-youtube-to-consulting-with-florin-of-voltlog/ | November 28, 2021 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6, 2022 |
| 589 | Mute Button Discipline | https://theamphour.com/589-mute-button-discipline/ | May 15, 2022 |
| 598 | Best way to find a leak | https://theamphour.com/598-best-way-to-find-a-leak/ | August 7, 2022 |
| 602 | Rigorous engineering stuff may be out the window | https://theamphour.com/602-rigorous-engineering-stuff-may-be-out-the-window/ | September 11, 2022 |
| 603 | An Interview with Ray Ozzie (Blues Wireless) | https://theamphour.com/603-an-interview-with-ray-ozzie-blues-wireless/ | September 25, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 719 | Inventing the Power MOSFET with Alex Lidow | https://theamphour.com/719-inventing-the-power-mosfet-with-alex-lidow/ | March 20, 2026 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
