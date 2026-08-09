---
title: Switching Power Supply
concept: switching-power-supply
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A **switching power supply** (also *switched-mode power supply*, SMPS) is an electronic power converter that regulates its output by interrupting the input tens of thousands of times per second, with the ratio of on-time to off-time setting the output voltage.[361] The technique matters because operating the switch at high frequency allows the magnetics to be made very small — small enough that a mains charger can occupy a cubic inch rather than the brick-sized enclosure typical of 1980s equipment.[361] Switching conversion displaced the linear regulator in consumer products, early portable computers, and eventually most electronic equipment, on grounds of cost, heat, weight, and size.[222][684]

## Operating principle

The core principle is interruption: the input is switched on and off at rates from tens of kilohertz to several megahertz, and the duty ratio between the on and off intervals determines the output voltage.[361][61] Because energy is transferred in discrete packets at high frequency, the transformer or inductor that stores and transfers that energy can be physically small; at these frequencies a transformer tiny enough to fit inside a plug body suffices.[361]

Internally, the converter functions as a small control system rather than a passive power component. Output current is sensed across a resistor, the sensed value is fed back, and the controller uses it to adjust the drive and the pulse width.[62] Controllers also change strategy across the operating range, including skipping pulses entirely under light load.[62]

### Failure behaviour

The failure behaviour of a switching supply differs fundamentally from that of a linear supply, and this shapes how the surrounding system must be designed. A linear supply that is overloaded sags and carries on; a switching supply pushed past its limit shuts down.[222] In consumer computers this hard limit turned an accessory drawing six hundred milliamps into a supply-sizing problem for every unit shipped, and integrating the accessory's function — which required only a hundred milliamps — became the cheaper answer.[222]

## Frequency, magnetics, and switching devices

Switching frequency sets the size of the magnetics. At fifteen kilohertz the inductors are large components, often hand-wound, occupying a serious fraction of the board.[61] Commercial designs mostly operate between a few hundred kilohertz and a few megahertz, and at the top of that range the inductor shrinks to the point where a loop of copper trace on the board itself can serve as one.[61]

There is, however, a ceiling. As frequency rises, the parasitic capacitance and inductance of the layout and of the components themselves come to dominate, so the efficiency curve peaks and then falls — there is a sweet spot rather than a monotonic gain from ever-higher frequency.[61]

### Wide-bandgap semiconductors

Wide-bandgap devices — gallium nitride and silicon carbide — move that ceiling rather than removing it, switching fast enough (on the order of 100 volts per nanosecond) that the transistor spends essentially no time in its dissipative linear region.[61] Their significance lies in breaking the usual trade-off: raising a conventional transistor's breakdown voltage tends to make it slower, whereas these materials retain both high breakdown voltage and high speed.[553] Sharp switching edges combined with high breakdown produce very efficient DC–DC converters, and efficiency is what makes a supply physically small: higher efficiency means less waste heat, less waste heat means no large internal or external heatsink, and that chain is what allows sixty watts to be delivered from a plug-sized package.[553]

Power silicon in general does not follow the leading edge of process technology; such parts are built on mature nodes such as 90 or 45 nanometres rather than on the processes attracting fabrication investment.[582]

## Control

Control of a switching converter has traditionally been implemented by a dedicated analogue integrated circuit closing the feedback loop. The digital alternative reads the output voltage and current and adjusts the pulse-width-modulated duty cycle in software.[212]

The argument for digital control is iteration speed: an incorrect filter value in an analogue controller means recalculating the resistor and capacitor network, unsoldering parts, and possibly reordering them, whereas the digital equivalent is a coefficient change, a recompile, and a reflash.[212] The argument against is that a firmware image then has to be maintained, which is a poor trade against a fixed resistor and capacitor in a static application such as a plain 5 V to 3.3 V regulator.[212]

What makes digital control workable in practice is a hardware linkage between peripherals: the comparison events that shape the pulse width can also trigger the analogue-to-digital converter, so the measurement always lands at the same point in the switching cycle.[212] That determinism — the sampling instant relative to the switching edge — matters more than the raw speed of the converter.[212]

## Noise

The defining drawback of the topology is inherent rather than incidental: pushing pulses through a system is what a switching converter does, so electrical noise accompanies it, and a genuinely quiet system still requires a linear stage or a transformer somewhere in the chain.[9] Cascading two switching converters with no linear stage anywhere between them leaves nothing to attenuate the high-frequency content, and in such a chain the output capacitance is also what holds the loop stable when there is no load at all.[360]

The noise is not only electrical. Magnetics hum and vibrate, so a "quiet" supply may need to be quiet in the mechanical sense as well.[9] Audible noise has three distinct sources. First, an inductor wound loosely — a risk with hand-wound parts, as large power magnetics often are — vibrates under load.[127] Second, operating the supply outside its intended range can drive the controller into a very low duty-cycle mode that whines.[127] Third, multilayer ceramic capacitors are microphonic and audibly sing; because the effect is reciprocal, tapping the board makes them generate a voltage.[127]

Because switching behaviour, output-capacitor effectiveness, and sometimes the switching frequency itself all change with load, noise must be characterised across the load range rather than at a single operating point.[360]

### Electromagnetic compliance

Including a switching converter in a product commits the design to electromagnetic-compatibility work, because the switching action is a deliberate source of emissions.[184] One practical response in noise-sensitive analogue products is to buy the problem rather than design it: an off-the-shelf external brick with switching content in the tens of kilohertz (roughly 30–50 kHz) is straightforward to filter and has small leakage currents.[513] The same choice keeps mains wiring out of the product entirely.[513]

## Design practice

### Layout dependence

Switching converters are heavily layout-dependent, so a component substitution is not a like-for-like swap the way replacing a linear regulator is.[601] The cost cascades: new passives must be selected, qualification effort grows, and a replacement part in a smaller package can force the board into blind and buried vias.[601] All of this can be triggered by an unremarkable part making an unremarkable rail, which is why a switcher is a poor place to carry sourcing risk.[601]

### Controller selection and sourcing risk

Implementing the control loop on a general-purpose microcontroller using its own timers and converters is considered the wrong instinct; a dedicated controller chip is known to work.[88] Dependence on a specific vendor part, however, creates supply exposure: an end-of-life notice or an allocation problem leaves the design stranded.[88] When such a part becomes scarce, the decision is binary — pay as much as a hundred times the original price or design the part out — and there is no honest probability to attach to either branch.[601]

### Modelling and simulation

Device modelling for switching-converter simulation is difficult. For bipolar transistors it is essentially impossible to build a model from a datasheet, because the quasi-saturation region is never documented well enough.[196] For field-effect devices it is possible and adequate for the application, but laborious: test fixtures are built that curve-trace the device to reproduce the datasheet characteristics — output curves, on-resistance against gate voltage, gate charge — and the model parameters are adjusted until they match.[196] Even then, a trap remains: often no single physical transistor matches the whole datasheet, because different curves were extracted from different devices, so no model can fit all of them at once.[196] Beginner-oriented browser-based simulators are likewise unsuited to the problem, since convergence on a switching supply is exactly the case they are not designed to handle.[210]

### Modules and bought-in converters

At small production volumes the calculation favours bought-in conversion: for a run of ten units, an off-the-shelf module avoids selecting the transistor and inductor, working through the calculations, and discovering afterwards that the loop oscillates.[604] Complete modules go further, packaging the converter with a panel interface and control knob so that a bench supply is only an enclosure and an input source away.[408] That reusability once underpinned a broader claim — that since every product contains a converter and the layout had been done many times, nobody would lay out a converter board from scratch again — but the claim did not survive contact with practice.[565] At the low end of the market a gap remains: adjustable modules are widely available and noisy, whereas much of the time a fixed, properly regulated output with no adjustment is what is wanted.[406]

### Organisation and review

In organisations that treat converter design seriously, the work is partitioned to a specialist: one designer takes the converter half of the board and another takes the digital and analogue remainder, with the two merged at the end.[230] The converter is also a classic subject for a design review to catch, and the feedback loop in particular is where an inexperienced designer is found out — Dave Jones has described being caught out on exactly this point early in his career.[138] A development circuit of any kind should expose its intermediate signals deliberately, because that access is exactly what disappears once the function is integrated into production hardware.[309]

## Applications

### Bench and laboratory supplies

Laboratory instruments are not exempt from the trade-offs. A bench supply can be switch-mode internally, with a quasi-linear post-regulator and substantial filtering behind it, and still be noisier than a classic linear design.[169] Above a certain current there is no choice: a linear supply delivering forty amps would be unmanageably heavy, so high-current bench supplies are switch-mode by necessity.[277]

### Commodity and consumer supplies

A commodity computer supply is a cheap source of serious current — a few hundred watts for around twenty dollars — and quieter than its reputation suggests, because low-cost manufacturers have adopted better offline switching techniques.[199] Its low-voltage rail carries tens of amps (a 5 V rail can supply on the order of 35 A), making it a practical starting point for generating other rails by boosting rather than by building a supply from scratch.[198] Converters built to modern efficiency standards draw around a tenth of a watt in standby.[5] Universal input — the ability of a switching front end to accept any regional mains voltage — is what allows a single stock item to be sold across regions with interchangeable plug pins, though the saving in overhead is pushed onto the buyer as a drawer of unused adapters.[523]

### Front-panel switching and standby behaviour

A front-panel power switch is often not a mains switch at all but a logic input to the converter's enable pin. This is a legitimate design, and it is also the reason an instrument can draw six and a half watts while apparently switched off.[39]

### Mains-side failure behaviour

A mains-side failure inside a switching supply can put current to earth and trip a residual-current breaker while leaving no visible damage and no equipment that has stopped working, which makes the fault very hard to localise afterwards.[81]

### Interaction with dimmers

Lamp dimming interacts with switching supplies in specific ways. A conventional (leading-edge) dimmer waits past the mains zero crossing, then triggers a latching device that stays on until the current falls to zero at the end of the half cycle.[524] Modern lamps, whose front end is a rectifier feeding an electrolytic capacitor, prefer the opposite arrangement, because switching the rectifier-capacitor input on partway up the waveform draws a large current surge — the reason conventional dimmers contain a sizeable choke to slow the edge.[524] Switching off late in the cycle has its own hazard: interrupting several amps drawn through the inductance of a transformer secondary can generate a spike on the order of 800 V, sufficient to destroy a small internal mains supply while leaving the output devices under test unharmed.[524] The remedies are to avoid the transformer or to place a few microfarads of capacitance across its output; the diagnosis requires putting an oscilloscope on the incoming mains rather than on the suspected circuit.[524]

### High-voltage and industrial converters

At extreme voltage the topology is unchanged but everything around it is different. A converter taking mains in and producing ten kilovolts out means creepage and clearance distances measured in inches and circuit boards floating at the full output voltage.[438] Potting the assembly solves the insulation problem and creates a thermal one, because the heat — up to a kilowatt of it — then has to cross the potting compound to escape.[438] The way out is materials that conduct heat without conducting electricity, such as alumina and other technical ceramics, supplemented by heat pipes spreading the thermal load to several points.[438]

Industrial rectifiers are the same topology at scale: despite a name that suggests four diodes, they are switch-mode supplies built for high current and high voltage.[522] The same logic appears in power distribution. Running low-voltage direct current over any distance loses too much to I²R resistive drops, so the converter belongs local to the load rather than centralised.[25] The grid-scale version of the idea, a solid-state transformer operating at several kilovolts (for example 7.2 kV), is essentially the switching-supply topology scaled up.[583]

## History

The transition from linear to switching supplies in consumer products was driven by cost alone.[222] In early portable computers the attraction was that the topology addressed three constraints at once — heat, weight, and size — rather than any one of them.[684] The transition also raised system complexity: instruments from the 1980s are markedly harder to service than those from the 1970s, and the switching supply is among the components responsible for the increase.[655]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ |  |
| 9 | From Boston In Boxers? | https://theamphour.com/the-amp-hour-9-from-boston-in-boxers/ |  |
| 25 | NASA, WOTW & Modular Design - The NASA Nostalgia | https://theamphour.com/the-amp-hour-25-the-nasa-nostagia/ |  |
| 39 | Dan Pink, Dual Core, level translators - Mumble Mumbo Jumbo | https://theamphour.com/the-amp-hour-39-mumble-mumbo-jumbo/ |  |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ |  |
| 62 | Op amps, Microchips & Mergers - Narquois Nerd Nescience - Narquois Nerd Nescience | https://theamphour.com/the-amp-hour-62-narquois-nerd-nescience/ |  |
| 81 | Jersey Jeff Jactitation | https://theamphour.com/the-amp-hour-81-jersey-jeff-jactitation/ | February 6, 2012 |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 138 | An Interview with Ryan Brown - Effortless Equipment Extensibility | https://theamphour.com/the-amp-hour-138-effortless-equipment-extensibility/ | March 25, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 196 | An Interview with Mike Engelhardt (Re-broadcast) | https://theamphour.com/196-an-interview-with-mike-engelhardt-re-broadcast/ | April 28, 2014 |
| 198 | Mike Ossmann Returns! - Planetic Portalab Packaging | https://theamphour.com/198-mike-ossmann-returns-planetic-portalab-packaging/ | May 12, 2014 |
| 199 | The 2014 Maker Faire Show - Traveling Technology Trangam | https://theamphour.com/199-the-2014-maker-faire-show-traveling-technology-trangam/ | May 19, 2014 |
| 210 | Risky Components and Hardware Innovation - Slipshod Shack Shutdown | https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/ | August 5, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 230 | Prepping For Hoverboards - Gallionic GitHub Gabble | https://theamphour.com/230-prepping-for-hoverboards-gallionic-github-gabble/ | December 30, 2014 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 309 | An Interview with Stefan Dzisiewski-Smith | https://theamphour.com/309-an-interview-with-stefan-dzisiewski-smith/ | July 27, 2016 |
| 360 | A Total 360 | https://theamphour.com/360-a-total-360/ | September 18, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 438 | An Interview with Bart Dring | https://theamphour.com/438-an-interview-with-bart-dring/ | April 14, 2019 |
| 513 | Audio DSP with Shannon Parks | https://theamphour.com/513-audio-dsp-with-shannon-parks/ | October 18, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ | December 27, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 553 | Debunking with Shahriar | https://theamphour.com/553-debunking-with-shahriar/ | August 10, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 582 | The Same Wavelength | https://theamphour.com/582-the-same-wavelength/ | March 20, 2022 |
| 583 | The Smart Grid with Paul Zawada | https://theamphour.com/583-the-smart-grid-with-paul-zawada/ | March 27, 2022 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 655 | The Twelfth Day of Keyzermas | https://theamphour.com/655-the-twelfth-day-of-keyzermas/ | January 8, 2024 |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ |  |
