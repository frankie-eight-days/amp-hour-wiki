---
title: Failures, Fires, and Recalls
concept: failures-and-recalls
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Failures, fires and recalls in electronics concern the mechanisms by which a defect escapes design and production test, reaches the field, and then has to be corrected across an installed population. The characteristic property of such failures is that the cost is set by the accessibility of the fault rather than by the value of the part at fault: a component as trivial as a rubber band has caused a recall costing on the order of 20 million dollars.[532] The same asymmetry drives component sourcing, because the true cost of a counterfeit component is the field service call it eventually causes, not the price of the part and its assembly.[366] Many field failures attributed to defective silicon are instead system design problems — inadequate brownout protection, unprotected data leaving a board, or a firmware timing path treated as a feature rather than as a safety function.[485][704]

## Counterfeit and substituted components

The dangerous class of counterfeit power semiconductor is not the empty package but the underspecified one. Parts sold as capable of dissipating around 50 W have contained genuine dies rated for about 5 W, so assemblies passed test, worked for a week and then failed once in service.[366] A counterfeit transistor with no die at all inside a TO-220 package behaves differently again, presenting as an open circuit or a fire risk rather than as a degraded part — a more abrupt failure mode than an undersized die.[1] Because the eventual field service call rather than the unit price dominates the cost, gray-market sourcing is avoided even on low-volume products where unit cost is not the binding constraint.[366]

Substitution also occurs legitimately and without notice. A silicon vendor redesigned the LMH6518 variable-gain amplifier used in the front end of most modern oscilloscopes and reduced its tolerance of the 400 millivolt input offset the original part supported, without changing the part number and with the change buried in the datasheet; there are documented cases of instruments being bricked by front-end DC offset as a result.[727]

Supply continuity for digital parts no longer relies on dual sourcing. Splitting a chip across two foundries has largely been abandoned because it is too costly and the processes are not compatible enough to port between, so continuity now rests on the fact that a large foundry operates several fabs able to run the same process.[95]

## Field failure mechanisms

### Brownout and memory corruption

The most common cause of microcontrollers bricking themselves in the field after months of service is inadequate brownout protection. A large holding capacitor keeps the rail at around 1.2 to 1.5 volts, well below the minimum operating voltage but high enough for the part to keep executing code, and when power returns the device does not reliably reset before writing to flash or EEPROM and corrupts it.[485] Corrupted flash or EEPROM reported as a silicon defect is therefore very often a system design problem instead, fully preventable with a proper brownout or supervisor circuit; failures of this kind recur frequently in returns analysis without being defects in the part.[485]

### Thermal and firmware-mediated fire risk

Solenoid drive is a firmware safety problem as much as a hardware one. A coil energised and not turned off within its rated duty will overheat, smoke and can catch fire, so the timing that limits on-time is a safety function rather than a feature.[485] Electromechanical game driver boards illustrate the scale of the exposure: they were built around arrays of Darlington transistors in the TIP102 class, rated 60 to 100 V and five to fifteen amps, fed from a four-bit latched data bus with separate latch assertion lines, with roughly a quarter of the outputs driving high-current solenoids and the rest incandescent lamps.[485]

Direct current sustains arcs that alternating current does not. A DC arc has no current zero crossing to extinguish it, so a fault in a high-voltage DC isolator sustains the arc until something burns. This is why rooftop solar DC isolators at around 460 volts have been a recurring fire source, and why microinverter architectures, which keep the array wiring at low voltage and combine at AC, are inherently safer.[532]

### Environmental robustness

Medical device regulatory testing requires the system to keep functioning through applied EMI, ESD and magnetic field disturbance rather than merely to survive them, so a reset or a crash on an ESD pulse is a failure of the test and not an acceptable recovery.[704] A recurring pattern in devices that fail regulatory EMC testing is a digital-led design with no ESD protection and single-ended, ground-referenced data leaving the board on cables, with no error detection and no common-mode rejection; each of those omissions is individually survivable on a bench and collectively fatal in a hostile environment.[704]

Component modelling contributes to the same class of problem. Treating a marked component value as the actual value is a common source of unexplained behaviour, since a nominal 0.1 microfarad capacitor's real capacitance depends heavily on the dielectric and the applied conditions, and academic training rarely covers the non-ideal behaviour of basic passives.[704]

Architectural choices can remove failure classes outright. Whether a product must be battery powered is worth challenging explicitly, because removing the battery removes a whole class of reliability and service failures; wireless and battery operation are frequently product expectations rather than requirements.[704]

## Board-level reliability

Power should never be carried through a single via, because the resistance of an individual via is not well controlled and a via can crack under mechanical or thermal stress; multiple vias in parallel provide both lower resistance and redundancy against one of them failing.[170] Solder-filling power vias serves reliability as well as resistance, reducing the current density in the plating and removing the barrel as a single mechanical failure point; via resistance is essentially irrelevant on signal traces, so this applies only to power nets.[170] Power vias should accordingly be left untented if the board will see a wave solder process, because the wave will then fill them, giving lower resistance and better reliability at no additional cost.[170]

In a modular product the connection points are where reliability is won or lost, and this remains true when there is no discrete connector and only mating contact surfaces, so the mechanical quality of the interface has to be designed deliberately.[170]

Not all intervention improves reliability. Reworking a solder joint purely because it looks cosmetically poor usually reduces its long-term reliability rather than improving it, because the additional thermal cycle grows the intermetallic layer; appearance is not on its own a reason to touch a working joint.[183]

## Root cause analysis

Silicon defects that survive production test are usually narrow boundary conditions, and the way to get them acknowledged is to capture the exact bus transaction with a logic analyser and hand the vendor's test engineers a reproducible address boundary and timing; in one case this exposed a defect in the part's address decoder.[485] Automotive customers work to a zero parts-per-million target, which in practice means any field failure is returned to the supplier and the supplier is expected to establish root cause and put a corrective action in place rather than treat it as within tolerance.[485]

Attribution frequently runs the other way. A confidently argued warranty claim that the design is at fault often turns out to be an assembly error by the claimant — in one case a five-volt regulator fitted backwards — which is an argument for checking supply rails methodically before accepting a design fault.[176]

Investigation carries its own hazards. A convenient-looking metal surface such as a fat heatsink inside a UPS may sit at 400 volts DC with no fuse in the path, so the ground reference for a scope probe must be established from the schematic rather than assumed from what looks like chassis metal.[485]

## Recalls

Multiple brands of solar DC isolator have been subject to safety recalls after field failures, which makes the isolator, rather than the panels or the inverter, a component worth checking on an installed array.[532]

The scale of a recall is governed by the population and the injury profile rather than by the complexity of the part. The Takata airbag inflator recall covered roughly 67 million units, with about 17 deaths and 200 injuries attributed to inflators firing incorrectly, and 130,000 cars recalled in Australia alone, from a single component supplier of about 50,000 employees.[532]

Design life can itself become the subject of a recall. A recall of failing touchscreen units in 135,000 Tesla cars was defended on the grounds that the units had only ever been expected to last five to six years, which in a vehicle where the touchscreen carries essentially all controls makes the design life of a single subsystem the design life of the product.[532]

Where the fault is in a control law rather than in hardware, the remedy can be delivered without touching the product. A 2020 model electric vehicle was recalled worldwide for a fault that could short the traction battery and cause a fire, and the remedy delivered was a software update to the battery management behaviour rather than replacement of the cells.[727]

## Repair and warranty economics

Reliability effort is a function of who bears the consequences. A commodity consumer product built to a monthly schedule prices warranty returns in and ships whatever the design state is at the deadline, whereas an industrial or test-and-measurement product takes eighteen months and slips further, because the manufacturer's reputation rather than the unit is what is at risk.[170]

Return rates vary by orders of magnitude with mechanical content. Products with substantial mechanical content carry warranty return rates that swamp their electronics: for a 3D printer class machine, replacement of something like one unit in twenty to thirty would not be surprising, which has to be priced in before the product ships.[243]

Warranty terms can also be used as an instrument rather than a liability. When a low-volume product uses a part whose field reliability is genuinely unknown, offering an unconditional free replacement is a deliberate way to buy failure data, because the exposure is bounded by the small unit count and the returns identify which part to change in the next revision.[369] At the other end, administrative cost can make a valid claim not worth filing: for a reseller of moderate-value instruments, the cost of claiming an individual unit against the factory warranty exceeded the value of the claim, so failures were absorbed instead, and the calculation only flips once the failure rate rises far enough that returns accumulate into a batch.[646]

Repair sometimes has to be invented after the fact. A manufacturing defect in the OLED module used in a family of Agilent and Keysight handheld meters caused a high enough failure rate, with the original display no longer purchasable, that a third party reverse-engineered the display protocol and built an STM32-based translator board to drive a currently available OLED in its place.[646] Repairing a fault sealed inside a hundred-metre marine seismic streamer likewise required developing a surgical procedure from scratch: cutting the outer sheath open with a scalpel, then building purpose-made tools to grip and retract the sheath because it could not be pulled back by hand.[532]

## Liability and contractual exposure

Professional liability cover for an independent embedded design consultant is genuinely hard to obtain. A four-month search through local agents, online providers and a professional body's insurance partner produced quotes only through Lloyd's of London, at an astronomically high premium.[492] The difficulty is structural rather than a judgement about risk level: insurers price from actuarial tables, and there is no table for embedded design work, so the more precisely the work is described the further outside a priced category the applicant falls.[492]

Pricing a work warranty into a consulting engagement up front means small post-delivery changes can be absorbed without a fresh negotiation at the moment the client is least willing to pay, and functions as a credible quality signal rather than as pure cost.[492]

Supply contracts offer less protection than their delivery dates imply. Force majeure clauses present in most supply contracts release a supplier from the contracted delivery date, and during supply disruption they are invoked broadly enough that the contracted date stops being a planning input at all.[492]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 1 | What's In A Name? | https://theamphour.com/1-whats-in-a-name/ |  |
| 95 | An Interview with Øyvind Janbu - Feracious Fabless Facilitator | https://theamphour.com/the-amp-hour-95-feracious-fabless-facilitator/ |  |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 369 | An Interview with Jason Huggins | https://theamphour.com/369-an-interview-with-jason-huggins/ | November 26, 2017 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 532 | Recalling Recalls | https://theamphour.com/532-recalling-recalls/ | February 28, 2021 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1, 2026 |
