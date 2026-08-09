---
title: Op-Amp
concept: op-amp
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

An operational amplifier (op amp) is an analog amplifier whose name records its original purpose: operational amplifiers performed mathematical operations on analog voltages, the function from which analog computers were built.[296] The classical set of operations omits multiplication, which is supplied by a dedicated analog multiplier and which extends the applications into modulation and demodulation.[46] Real devices depart substantially from the idealized description used in teaching, and much of the practice of analog design consists of selecting parts for, and working around, their imperfections.[480][45]

## Ideal versus real behavior

Instruction on operational amplifiers conventionally begins with the ideal amplifier, a starting point that obscures more than it reveals; the more tractable model is that the output is the difference between the two inputs multiplied by a gain.[609] The ideal model persists because it allows a course to reach circuit analysis immediately, but reading the supposed specifications of the ideal device shows how unrealistic each property is.[609] At the opposite extreme of instruction, being asked to measure twenty parameters of a real part without being told what any of them mean is a corresponding failure.[609]

Real devices behave very little like the undergraduate description, and the substance of the discipline is working around their limitations; were a perfect amplifier to exist, much of the work would disappear, since every circuit would simply be an analog computer.[480] The gap between reading the description and building the circuit is where beginners come unstuck: the account of how the device works reads as complete, and the implementation then fails on imperfections the account did not mention.[480] Individual facts taught early — that no current flows into either input, for instance — carry no weight until the learner has met them repeatedly in real circuits, which is why teaching purely through the mathematics leaves so little behind.[127]

## Internal structure

The classic general-purpose part is not complicated internally — around two dozen transistors — which is why it can be rebuilt from discrete components as a teaching object.[609] The internal structure of such parts has not changed, so seeing it laid out in discrete components is a way to learn what the simplified symbol stands for.[213] Reading a transistor-level schematic is a matter of recognising structures rather than following every device: the differential pair, the current mirror, and the current source, of which the symbol most engineers work with is a compression.[574]

## Derived circuits

### Instrumentation and differential amplifiers

The classic instrumentation amplifier is three amplifiers and four resistors — two followers feeding a difference stage — and its performance depends entirely on how precisely those resistors are matched.[34] That dependence is why the discrete version is usually skipped in favour of an integrated part, in which the resistors are laser trimmed, thermally matched, and share the same drift and temperature coefficient.[34] The reason for the topology is common-mode rejection: it recovers a small differential signal riding on a large common-mode voltage, which makes it the front end for measurements taken from electrodes on the skin.[34] The specialised amplifiers sold as complete parts decompose into the same elements: a difference or instrumentation amplifier is three amplifiers and some precision resistors, packaged as a system.[15] Likewise, a differential amplifier built from discrete amplifiers and resistors has its accuracy set entirely by the matching of the feedback resistors, which determines whether the finished instrument meets its specification.[491]

### Transimpedance and charge amplifiers

A transimpedance amplifier is an amplifier with a resistor in its feedback path: current driven into the input develops a voltage across that resistor, which becomes the output.[579] The photodiode front end is the standard instance, with the diode on the input and a megohm-class resistor in the feedback loop.[579] The performance available from that arrangement is set by the amplifier's input characteristics: a JFET-input part with very low noise and very low input current, at around fifty dollars, has supported tens of picoamps of resolution with about half a picoamp of noise.[245]

A charge amplifier substitutes a capacitor for the feedback resistor so that the stage integrates charge rather than converting current; it needs a very high impedance input and works at very low frequencies.[570] The historical constraint on that circuit was the feedback capacitor: low frequencies want as much capacitance as possible, and the ultra-stable NP0 ceramics needed for the job did not exceed a nanofarad at the time.[570]

### Precision rectifiers and composite amplifiers

Placing an ordinary diode inside the feedback loop removes its forward drop, producing the ideal-diode behaviour used in precision peak detectors; the same objective in a switching converter is what integrated ideal-diode parts address, by cutting the loss in the switching diode.[98] Cascading two amplifiers in series buys bandwidth or drive capability, but a composite amplifier is different: the second amplifier is placed inside the first's feedback loop, which lets a very low-noise, low-offset input stage be combined with a high-current line driver.[660] The point of the composite arrangement is that at the edge of the specification no single device meets every requirement at once, since amplifier parameters always trade off against one another.[660]

### Voltage regulators

An adjustable low-dropout regulator can be little more than an amplifier and an internal current source: the output voltage is set by one resistor to ground rather than by a divider, because the current source drives a fixed current through it to make the reference.[44] Because that internal source is only about ten microamps, it can be overridden by driving the set pin directly, which turns the regulator into a programmable supply.[44] A switching regulator and a linear one share almost the whole circuit — the amplifier, the feedback element, the pass transistor and the reference; what differs is that the amplifier's output driving the pass transistor is switched rather than continuous.[574]

### Larger analog systems

An analog audio dynamics processor is built from the same parts in combination: four amplifiers, RMS converters and voltage-controlled amplifiers, arranged to make a compressor, a limiter, automatic gain control or a de-esser.[563] A power operational amplifier intended for audio can serve as the output stage of a supply: a device rated at roughly 120 watts, paralleled and reconfigured, has reached about 700 watts of output.[315] Modular instrument systems have included an amplifier as a plug-in module with terminals on the front panel, so that external resistors or a small board turn it into an integrator, a differentiator or a summing stage.[655]

## Device selection

Selection is driven by which imperfection matters in the application: low offset voltage for sensing small voltages, low input bias current for a photodiode front end, low noise and low offset drift where the measurement is slow.[45] Where the requirements are not demanding, the choice hardly matters and a general-purpose part from the drawer will do, which is the right answer for a beginner who cannot yet name what they need.[45] A modest application may have no meaningful selection problem at all: for an ultrasonic transducer amplifier used to measure distance, on the order of a hundred parts on the market would serve, because no noise floor or precision requirement has been stated.[141]

The vendor application note is a legitimate shortcut: for a given transducer there is usually a published circuit in which the amplifier has already been chosen, and it works.[141] Those notes exist because they sell chips, which does not make them less useful; a design known to work is worth more than the exercise of deriving it.[141]

Replacing a part in a characterised system is a different problem from choosing one for a new design: a nearly-equivalent device with slightly different phase margin can make the circuit oscillate, and the working rule is that "the right op amp is the op amp you already have".[62] That is what makes an approximate cross-reference dangerous: close is not exact, and the difference lands in a parameter the original design depended on without recording it.[62]

Sorting a distributor listing by price is a reasonable way to choose among twenty parts that all meet the requirement; the caveat is that an unusually low price may reflect stock the distributor is clearing rather than the part's standing price.[211] Second sourcing is easier for a part in a standard small-outline package than for a converter, and a second source need not be a different manufacturer: a higher-performance part from the same vendor costs more but is available immediately, which is what gets a design out of a lead-time problem.[104]

Designing an expensive part out has to clear the arithmetic: at a hundred units a year, halving the cost of a fifty-dollar amplifier saves about two and a half thousand dollars, so more than about twenty-five hours of engineering turns the change into a loss.[64] The unit price also bounds the product: a fifty-dollar amplifier cannot go into something intended to sell for forty dollars, so the part choice and the price point have to be settled together.[245] In precision instruments the parts are not substitutable at all: 0.05 percent resistors and specific amplifiers are single-sourced with no equivalent, which is simultaneously a supply risk and a barrier protecting the product.[682]

A design tool can carry the selection: entering the filter requirement and an optimisation preference for power or noise makes the tool choose the components and the amplifiers, with an expert mode in which the user picks a part they already stock and is shown the resulting performance instead.[392] Such a tool also selects component series by availability, since the resistor and capacitor series determine how hard the parts are to obtain; a design that looks poor against a general standard is correct if the application only needs twenty decibels of rejection and it avoids stocking another amplifier.[392]

## Data sheets, testing, and simulation

The reason a precision part costs fifty dollars is test: every die is tested, every packaged device is tested, and almost every parameter printed in the data sheet is measured on each unit rather than established statistically.[348] A data sheet for a precision part will report the production spread from thousands of tested devices; a commodity part gets no such treatment, so the presence or absence of that data — not the manufacturer's name — is what indicates what is being bought.[578] Some behaviour is not in the data sheet at all: an input offset voltage that varies with the supply rail, arising inside the part, is the kind of dependence found by varying the rails during debugging rather than by reading.[146] The working definition of input offset voltage is the operational one — short the inputs and observe what the output does; the formally correct definition, the voltage that would have to be applied to bring the output to zero, describes the same quantity from the other direction.[148]

Noise is specified in nanovolts per root hertz, and measuring it is difficult in its own right because every instrument used to make the measurement contributes noise of its own.[384] Counterfeit and rebadged parts turn up in this category: a quad amplifier marked as one general-purpose type has turned out to be a different device entirely — an LM324 rebadged as a TL074-class part — and the two behave quite differently.[625] Simulation rarely needs the exact device: vendors integrate their own part models to push their catalogues, but for most work a generic model of the amplifier is what is actually being simulated.[28]

## Practical design considerations

Quiescent current is what the device draws while doing nothing: an amplifier that is not amplifying still burns current simply by being powered.[10] That is a real fault in a low-power design: a power budget expected to be tens of microamps has come out at tens of milliamps, with one contributor an amplifier left enabled and idle on a plug-in board.[534] In precision analog the amplifier gets its own supply: a low-noise linear regulator dedicated to that part at the point of use, rather than a general-purpose regulator shared with the rest of the board, because the supply noise appears in the measurement.[168]

Driving a coaxial cable is a stability question rather than a power one: some power amplifiers lose stability into a capacitive 50-ohm load, so an output buffer has to be selected for that specific ability.[278] Capacitive loading in general is a design criterion in its own right and a common way to destroy the stability of an otherwise sound circuit.[141] Ceramic capacitor value is specified at zero volts of DC bias, and no working circuit runs there: a one-microfarad 25-volt X7R operated at three volts might retain 0.9 microfarad if it is a good one and a small fraction of that if it is not — which matters directly when the capacitor is compensating an amplifier.[169]

A supply fault propagates through a board's analog section: a rail that went high voltage has killed roughly half the amplifiers on a board at once, which is usually the point at which repair stops being economic.[643] Schematic edits carry their own risk: two pins on an amplifier were transposed while a drawing was being reformatted, a mistake that would otherwise have surfaced as a circuit that failed to regulate.[80]

## Applications

In audio the front end decides the product: gain with low noise is what determines quality, and that stage is analog — a low-noise bipolar amplifier — after which the work can move to digital signal processing.[513] Moving the subsequent stages into DSP avoids the accumulated noise of a chain of analog stages, and avoids the potentiometers used in traditional preamplifiers, which are high impedance, go scratchy and act as noise magnets.[513]

Direct-conversion receivers move the amplification problem down in frequency: converting straight from radio frequency to a very low intermediate frequency means the amplifiers are ordinary off-the-shelf parts working in the kilohertz range and the filtering becomes resistors and capacitors.[52]

Long-duration space hardware can be a reason to choose analog over a processor: a microcontroller in low Earth orbit accumulates radiation-induced bit flips, which is acceptable over a six-month mission but not over five years with no way to reprogram.[401] In one such design a maximum power point tracker was built as an analog computer, using an amplifier to evaluate a straight-line relationship for the panel's optimum voltage.[401] That design used commercial off-the-shelf parts selected for existing radiation test data to at least thirty thousand rad, and closed its loop by exploiting the panel's source impedance: drawing more current drops the voltage, which is what makes feed-forward control of the input voltage possible.[401]

High-voltage, high-speed requirements are where the catalogue runs out: driving plus and minus fifteen volts at twenty megahertz into loads of a few hundred ohms to a kilohm, from sixty-volt rails, leaves very few parts to choose from.[194] At the other extreme, reducing the amplifier count is what makes some form factors possible: a handheld instrument depended on not having many amplifiers scattered through it, and on CMOS, to run from batteries for a useful time.[180]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 10 | Open Hardware and Self Publishing | https://theamphour.com/the-amp-hour-10-open-hardware-and-self-publishing/ | |
| 15 | Analog Components, First Person Flying and Idea Ownership | https://theamphour.com/the-amp-hour-15-analog-components-first-person-flying-and-idea-ownership/ | |
| 28 | Bowie and The Brown Note | https://theamphour.com/the-amp-hour-28-bowie-and-the-brown-noise/ | February 1, 2011 |
| 34 | AD620, DesignSpark, Instrumentation Amplifier - The Rant Rhetorical | https://theamphour.com/the-amp-hour-34-the-rant-rhetorical/ | March 14, 2011 |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 45 | Texas Instruments, OPA & Chevy Volt - Nerdy Neuroelectronic Neurosis | https://theamphour.com/the-amp-hour-45-nerdy-neuroelectronic-neurosis/ | May 30, 2011 |
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ | |
| 52 | An Interview with Jeri Ellsworth - Carnassial Chip Chemicals | https://theamphour.com/the-amp-hour-52-carnassial-chip-chemicals/ | |
| 62 | Op amps, Microchips & Mergers - Narquois Nerd Nescience - Narquois Nerd Nescience | https://theamphour.com/the-amp-hour-62-narquois-nerd-nescience/ | |
| 64 | OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster | https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/ | |
| 80 | Otiose Ontocyclic Opiniasters | https://theamphour.com/the-amp-hour-80-otiose-ontocyclic-opiniasters/ | January 29, 2012 |
| 98 | Proemial Passive Poiesis | https://theamphour.com/the-amp-hour-98-proemial-passive-poiesis/ | June 3, 2012 |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 141 | FPGAs, Robots & Thermocouples - Wampum's Wavering Worth | https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/ | April 15, 2013 |
| 146 | Hamvention, Arduino and Intel - Burdensome Background Battology | https://theamphour.com/the-amp-hour-146-burdensome-background-battology/ | May 21, 2013 |
| 148 | Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood | https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/ | June 3, 2013 |
| 168 | Specialized and/or Open Source Test Gear and Dev Boards - Vacation Videography Vorboten | https://theamphour.com/168-specialized-and-open-source-test-gear-and-dev-boards-vacation-videography-vorboten/ | October 21, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 180 | An Interview with Dave Taylor - Multi-talented Meter Maker | https://theamphour.com/180-an-interview-with-dave-taylor-multi-talented-meter-maker/ | January 13, 2014 |
| 194 | An Interview With Todd Bailey - Embedded Embrasure Engineering | https://theamphour.com/194-an-interview-with-todd-bailey-embedded-embrasure-engineering/ | April 14, 2014 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ | |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 278 | Our Second Callin Show(ish) | https://theamphour.com/278-our-second-callin-showish/ | December 16, 2015 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 384 | A++++++ Will Buy Again | https://theamphour.com/384-a-will-buy-again/ | March 18, 2018 |
| 392 | An Interview with Matt Duff | https://theamphour.com/392-an-interview-with-matt-duff/ | May 13, 2018 |
| 401 | An Interview with Brent and Bryce Salmi | https://theamphour.com/401-an-interview-with-brent-and-bryce-salmi/ | July 29, 2018 |
| 480 | An Interview with Ben Krasnow, 8 years on | https://theamphour.com/480-an-interview-with-ben-krasnow-8-years-on/ | February 16, 2020 |
| 491 | The Almighty Dollarydoo | https://theamphour.com/491-the-almighty-dollarydoo/ | May 3, 2020 |
| 513 | Audio DSP with Shannon Parks | https://theamphour.com/513-audio-dsp-with-shannon-parks/ | October 18, 2020 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 563 | Grumpy Collaboration | https://theamphour.com/563-grumpy-collaboration/ | October 24, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 578 | Histogrammic or Histomagraphical | https://theamphour.com/578-histogrammic-or-histomagraphical/ | February 20, 2022 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 625 | Gremlins in the machine | https://theamphour.com/625-gremlins-in-the-machine/ | March 26, 2023 |
| 643 | Calibration & Repair with Ian Johnston | https://theamphour.com/643-calibration-repair-with-ian-johnston/ | August 22, 2023 |
| 655 | The Twelfth Day of Keyzermas | https://theamphour.com/655-the-twelfth-day-of-keyzermas/ | January 8, 2024 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
