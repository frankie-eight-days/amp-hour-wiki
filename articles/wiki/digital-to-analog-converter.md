---
title: Digital To Analog Converter
concept: digital-to-analog-converter
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **digital-to-analogue converter** (DAC) is a device that converts a digital code into a corresponding analogue voltage or current, forming the output half of the boundary between digital processing and the physical world.[573][381] In system terms it appears wherever a processed or stored digital value must drive something real: waveform generators reconstructing stored samples, programmable power supplies setting their rails, software radios returning processed signals to a front end, and audio chains feeding speakers.[278][689][315][381] The converter itself is rarely the whole problem; in nearly every application it is surrounded by analogue circuitry — filters, buffers, amplifiers, references and gain stages — whose design is the substantive engineering work.[573][278]

## Role in waveform generation

An arbitrary waveform generator is fundamentally a fast converter playing samples out of memory: the waveform, even a plain sine, is stored as an explicit sequence of values and read back repeatedly.[278] The engineering difficulty in such an instrument is not the conversion but the memory architecture — one stored cycle must be repeated at any requested frequency, which requires segmenting the sample memory and controlling how it is read, or else preloading a large memory with many cycles of the waveform.[278]

Converter resolution constrains where amplitude control can live. With an eight-bit converter, scaling the output down in the stored data is not practical — a full-scale ten-millivolt output would leave about two bits of resolution — so the amplitude control must be analogue and must sit after the converter.[278] This is why an instrument described as purely digital still contains a substantial analogue output section: DC offset, attenuators, amplifiers and filters all sit between the converter and the output connector.[278] The immediate stage after the converter is typically a reconstruction (anti-aliasing) filter followed by a buffer, because the converter itself will not drive the load it is asked to feed.[278] Wide, fast output swings force a discrete output stage: obtaining plus and minus twenty volts at speed from an operational amplifier is difficult, and any real output current makes it harder again.[278]

Sample rate is not output bandwidth: a converter rated for thirty megasamples intended for video gives usable analogue bandwidth in the region of five megahertz.[278] Instruments also do not necessarily filter their output to a clean sine; the waveform from expensive equipment is often a visible staircase, because the steps are removed by the sampling and filtering that follow rather than at the source.[570] A development order that avoids compounding problems is to start with an eight-bit converter, get the system working end to end, and only then move to twelve or sixteen bits once the behaviour is understood.[278]

## Accuracy, linearity and resolution selection

The headline linearity figure and the guaranteed figure for a converter are different numbers: a part advertising integral non-linearity of about plus or minus two counts may specify plus or minus twelve over temperature.[80] Measuring several parts settles the question that data sheets leave open — three samples of one converter showed the spread between devices directly.[80] Choosing fewer bits from the same family can improve real accuracy, because the parts come from one die that is sorted in manufacture: the ten-bit version can be tighter within its range than the twelve-bit version is within its own.[80]

The converter is often the weakest element in an otherwise precise chain: surrounding an ordinary converter with 0.1 percent resistors and a 0.25 percent voltage reference concentrates the error in the cheap part.[80] Published specifications also routinely exceed the requirement; audio converters are offered at twenty-four bits and sample rates near two hundred kilohertz, and the engineering task is tying the selection back to what the application actually needs — which makes converter selection a cost optimisation, whether a two-dollar part can be made to perform rather than whether a thirty-dollar part meets a number.[573]

## Characterisation pitfalls

Sweeping the codes of a converter and measuring the output with a bench meter is the obvious characterisation method, and auto-ranging invalidates it: the meter changes accuracy at each range boundary, producing steps in the plot that read as converter defects.[169] Turning auto-ranging off does not end the problem — a precision meter built around a multi-slope integrating converter has behaviour of its own that appears as step-to-step error scattered across the linearity plot, which again belongs to the instrument rather than the part under test.[169] When output values are implausible, the reference is worth checking before the code: one converter producing wrong values was traced to a slightly incorrect reference, caused by an analogue ground connected to three capacitors and nothing else.[474]

Testing a converter can be a larger problem than building it. Developing a sixteen-bit converter clocked around seventeen megahertz in 1995 required building a programmable pattern generator to feed the device, because the data arrived on a time-interleaved four-bit bus carrying both samples and opcodes.[169]

## Integration versus discrete parts

The asymmetry inside a microcontroller is consistent: a usable analogue-to-digital converter is not hard to integrate, and a good digital-to-analogue converter is.[87] Reasons to fit an external converter rather than use one inside a microcontroller include lower noise and flexibility — an external part can be substituted for a better one without changing the rest of the design.[80]

Discrete converters carry a price premium, and there is no commodity part at the bottom of the market.[80] On microcontrollers the peripheral does not appear at all below a certain price: an inexpensive part will have an analogue input and a comparator but no output converter.[610] Integration is also bounded by process: putting a converter alongside higher-power circuitry forces one semiconductor process to serve both, so a die optimised for the converter will not also give low-resistance switches, and the published specifications narrow accordingly.[216] The same compromise shows in reconfigurable mixed-signal parts, where the converters top out around twelve bits and the analogue blocks are adequate rather than good.[12]

Integration has a performance ceiling as well. On the USRP software-defined radio family, a single package containing both dual converters made for a very sparse board, but no higher-rate, higher-precision version of that part existed, so the next generation used separate converters — one chip became six.[101] The change propagated into the system architecture: the separate high-end converters brought so many more pins that two channels no longer fitted on one board, and multiple-antenna operation became a matter of tying boards together.[101]

Clocking matters at the system level: clocking converters from an external source rather than from a microcontroller's own clock generator keeps the sampling instants free of the jitter that generator would add.[265] A small programmable logic device is often present purely as interface glue between the converters and the processor, doing no processing of its own.[161]

## In other converters

A successive-approximation analogue-to-digital converter contains a digital-to-analogue converter: the input is captured on a sample-and-hold capacitor, and the internal DAC is stepped through voltages that a comparator weighs against that stored value, with the sequence of comparisons forming the result.[348] The constraint that follows is at the input — the front-end switch must stay closed long enough for the internal capacitor to charge through its own series resistance, which is what makes driving that input the hard part.[348]

## Applications

### Audio

In audio, the converter is usually not the limiting element: a loudspeaker runs at something between half a percent and one percent distortion, and room acoustics contribute more error than even a poor speaker.[270] An audio codec packages the converter pair together with what is needed around them — a good converter in each direction plus enough to drive a microphone and headphones from one chip.[167] Purpose-built parts reach considerable density: four channels of conversion together with two channels of audio amplification reaching seventy watts in a nine-by-nine-millimetre package.[338] A practical digital audio processing chain places an adjustable gain stage ahead of the input converter so the signal lands in that converter's usable range, then returns the processed result through the output converter.[513]

Where audio quality is the entire point, the converter can be avoided altogether: rather than fitting an input and output converter for each of hundreds of console channels, a motor drives the physical fader so the signal path stays analogue throughout.[27]

### Radio and millimetre-wave

In software radio the converters are indifferent to what produced the signal, so the same hardware serves ultrasound research as readily as radio, and the architecture reduces to a front end, an input converter, processing, and an output converter back to a front end.[381] At millimetre-wave frequencies the radio is not what limits usable bandwidth — the converters are: wide spectrum is of no use if only a fifty-megahertz slice can be digitised.[483] The limit holds for reasons of power rather than ingenuity: converting and processing at those rates costs on the order of a watt, which a handheld device cannot spend without becoming uncomfortable to hold.[483]

### Video

Video can be generated from a microcontroller with a resistor-ladder converter of only a few bits, because a monochrome signal has no colour burst to reproduce.[469] Colour video needs both the converter and the clock: one microcontroller drove a parallel output into an R-2R resistor ladder to produce the signal, and generating it at the correct rate depended on a phase-locked clock source that later revisions of the part removed along with its built-in converters.[673]

### Instrumentation and power

A programmable supply can be built from an inexpensive serial-bus converter producing zero to about five volts, with a power operational amplifier scaling and shifting that to the required rails while supplying the current.[689] The converter can also be the source in a measurement: driving a known voltage through a current sensor and measuring the drop turns the same hardware into a resistance meter.[689] A programmable bench supply used two sixteen-bit converters to set positive and negative rails independently across a wide range, with sixteen-bit current measurement returning the output current.[315] Adding a converter for programmable calibration brings the whole support structure with it, which is the argument for parts accurate enough that no per-unit trimming is needed.[174]

## Configuration trends and alternatives

Peripheral count drives part selection directly: microcontrollers have been chosen specifically because they offered four output converters that an application required.[564] The direction of travel is toward making that irrelevant, with newer parts offering many general-purpose pins each of which can be configured as an input or output converter.[564] Configurable mixed-signal parts already make the converter a routing choice, offering several converters that can be switched to any pin alongside the digital logic.[352]

The converter itself belongs to a choice of approach rather than being obligatory: comparing a voltage and acting on the result can be done with a comparator directly, or by digitising it, comparing in software and driving an output converter — and which one an engineer reaches for tends to follow what they were trained on.[2] Either way, the analogue circuitry around a converter has to be designed, and that boundary between the two domains is the mixed-signal skill worth acquiring.[573]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 2 | Critical Mass | https://theamphour.com/show-2-critical-mass/ | |
| 12 | Dave Is Back And Blogging! | https://theamphour.com/the-amp-hour-12-dave-is-back-and-blogging/ | |
| 27 | 555 Contest, Computer Museum, Octopart - The Green Pen Hornswoggle | https://theamphour.com/the-amp-hour-27-the-green-pen-hornswoggle/ | |
| 80 | Otiose Ontocyclic Opiniasters | https://theamphour.com/the-amp-hour-80-otiose-ontocyclic-opiniasters/ | January 29, 2012 |
| 87 | An Interview with Ian Daniher - Nascent Nonolith Numquid | https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/ | |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15, 2014 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 278 | Our Second Callin Show(ish) | https://theamphour.com/278-our-second-callin-showish/ | December 16, 2015 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 352 | Conning with Michael Ossmann | https://theamphour.com/352-conning-with-michael-ossmann/ | July 17, 2017 |
| 381 | An Interview with Derek Kozel | https://theamphour.com/381-interview-with-derek-kozel/ | February 25, 2018 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 483 | An Interview with Adrian Tang | https://theamphour.com/483-an-interview-with-adrian-tang/ | |
| 513 | Audio DSP with Shannon Parks | https://theamphour.com/513-audio-dsp-with-shannon-parks/ | October 18, 2020 |
| 564 | Pavlovian Cheapskates | https://theamphour.com/564-pavlovian-cheapskates/ | October 31, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ | November 20, 2022 |
| 673 | Lifelong Learning with Bitluni | https://theamphour.com/673-lifelong-learning-with-bitluni/ | July 15, 2024 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
