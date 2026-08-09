---
title: Spectrum Analyzer
concept: spectrum-analyzer
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **spectrum analyzer** is a test instrument that measures and displays signal power as a function of frequency, sweeping over a selected frequency range and reporting how much power is present at each frequency within it.[376][465] It is one of the principal instruments of radio-frequency (RF) work: a serious RF bench is defined by a network analyzer and a spectrum analyzer, with a tracking generator if the budget allows, and for microwave design specifically the principal instruments are a power meter and a spectrum analyzer, with a frequency counter as a possible third.[73][107] A wideband RF spectrum analyzer is also typically one of the last big-ticket instruments a general electronics bench acquires, with new units starting at roughly $1,500 to $2,000 and prices climbing steeply from there.[73]

## Operating principle

What a spectrum analyzer physically does is sweep through frequencies one at a time and report the power present at each; everything else attributed to the instrument is a consequence of that single measurement.[376][465] This is the same mechanism a network analyzer uses when it injects a swept stimulus and observes how a circuit responds across a band.[376] A swept analyzer visibly updates the display point by point as it moves across the band, which is itself diagnostic information: the operator can see where in the sweep the instrument currently is, whereas instruments that compute an entire screen at once behave differently and cannot be read the same way.[209]

### Swept versus FFT architectures

Not all analyzers sweep continuously. Older FFT-based instruments acquire a chunk of data, run Fourier transforms on it, and display the result before acquiring the next chunk, so events occurring between chunks are invisible; real-time spectrum analyzers close that gap, which matters for intermittent or bursty signals.[178] Modern dedicated analyzers achieve update rates that make the display feel live, on the order of 50,000 FFTs per second, achieved with dedicated silicon rather than general-purpose processing.[619]

Resolution bandwidth and span together set the processing load on the instrument. A span of 0 to 2 MHz with a 300 Hz resolution bandwidth filter is a reasonable request that nonetheless forces the instrument to process gigabytes of data, and long update times should be expected whenever the ratio of span to resolution bandwidth is large.[209] A well-designed analyzer remains interactive while a slow sweep runs, letting the operator stop the sweep, move cursors over data already on screen, or change settings; locking the user interface during a long acquisition is a design fault rather than an unavoidable consequence of the processing load.[209]

## Instrument classes and related instruments

Audio spectrum analyzers and wideband RF spectrum analyzers are separate instrument classes with separate price structures; a lab can accumulate several audio-band instruments and still have no RF capability.[73] A dynamic signal analyzer is an FFT instrument aimed at low frequencies, typically the audio band; it occupies the frequency domain like a spectrum analyzer but with a range and resolution tuned to a different problem, so the two are not interchangeable.[570] A modulation domain analyzer occupies a third axis pairing, plotting frequency against time where an oscilloscope plots voltage against time and a spectrum analyzer plots amplitude against frequency; this pairing is what allows an operator to watch a frequency source settle, seeing it commanded to a new frequency, go out of lock, and drift back in.[613]

### Oscilloscope integration

Modern oscilloscopes commonly offer an FFT function, which is the usual fallback for an engineer without analyzer training; it gives some visibility into frequency content but is a partial substitute rather than an equivalent.[165] The real discriminator between a scope's FFT function and a dedicated analyzer is the number of frequency bins: scope FFTs are mediocre because the bucket count is low, so fine structure in the spectrum is simply not resolved.[619]

A spectrum analyzer built into an oscilloscope may also be capped by the scope's bandwidth licence rather than by its own hardware: the 100 MHz model of a range may have its analyzer function limited to 100 MHz in software even though the front end can do more, so the purchaser must check what bounds the analyzer function before treating it as a substitute instrument.[184] A bandwidth-limited built-in analyzer is still useful for switch-mode power supply work, where the interesting content sits well below 100 MHz, though that use case is occasional rather than routine.[184]

Putting real spectrum analyzer hardware into every oscilloscope in a product range raises the bill of materials enough to lift an entry-level 100 MHz dual-channel model to around $3,300, which puts it out of competition against instruments that omit the feature; bundling an expensive subsystem across a whole product line taxes the customers who do not need it.[186] The vendor rationale for doing so was market research showing that around 40 percent of new designs contain wireless.[186] The value of a true mixed-domain oscilloscope is the hardware that time-correlates the time domain and the frequency domain, allowing a digital event to be tied to the RF emission it caused; stripping that hardware out to save cost leaves a spectrum analyzer merely sharing a box with a scope.[186]

### Convergence with network analyzers

Network analyzers since around 2012 have absorbed spectrum analysis, modulated-signal measurement, and complicated noise figure measurement, moving well beyond swept sine and continuous-wave measurement, and the boundary between instrument categories has been dissolving from the vector network analyzer side.[533] Microwave test previously meant building a rack—a spectrum analyzer, a signal generator, and a noise figure meter behind a switch matrix—whereas the demand is now for one instrument that tests everything at once, because switching between boxes costs process efficiency on the production floor.[533]

## Tracking generator and scalar network analysis

A tracking generator outputs a sine wave locked to wherever the analyzer is currently sweeping: when the receiver is looking at 100 MHz the generator is producing 100 MHz, and that synchronisation turns a passive receiver into a stimulus-response instrument.[465] To measure a filter, the tracking generator is connected to one side of the filter and the analyzer input to the other; the operator then reads off how much energy passes at each frequency across the sweep, producing a response plot showing whether the stopband is down 10 dB or 50 dB and whether the wanted signal still passes.[465]

A tracking generator plus a spectrum analyzer constitutes a scalar network analyzer: it measures amplitude only, not phase.[465] That limitation means no Smith charts and genuine ambiguity when measuring purely reactive components, which is where a vector instrument becomes necessary.[465]

## Software-defined radio as analyzer

A software-defined radio with a display add-on can function as a standalone handheld analyzer. The HackRF with a PortaPack tunes anywhere across six gigahertz, running about a thousand FFTs per second over a 20 MHz instantaneous span; the tuning range and the instantaneous span are separate numbers, and confusing them overstates the instrument.[161] The HackRF, developed by Michael Ossmann, was deliberately built without an FPGA on the reasoning that laptop DSP capability had become strong enough that the board only needed to move samples in and out of high-speed USB at the maximum rate; pushing signal processing to the host is what kept the cost down.[161]

At a lower price point, a twenty-dollar USB digital television dongle repurposed as a receiver gives a usable spectrum display, including spectrum over time, which is enough to confirm whether a band is genuinely empty or a local station is at fault; it turns an unfalsifiable suspicion into a measurement.[145] A consumer toy containing a radio has been reverse engineered into a working 900 MHz spectrum analyzer by Ben Krasnow, an exercise that serves as both a cheap route to an instrument and a substantial engineering undertaking.[75]

The first step with a new software-defined radio is typically to route the source block into a frequency sink to obtain a spectrum plot and waterfall, then tune to a known band such as 433 MHz or 2.4 GHz; within minutes this reveals that domestic thermostats and car tyre pressure monitors are transmitting continuously, each with a unique identifier.[381] Modulation type is readable directly from a waterfall display: a chirp-spread system draws slopes sweeping up and down as frequency changes, while a frequency-shift-keyed link sits static at its centre frequency with a bandwidth set by the modulation parameters, and identifying an unknown signal often starts with this visual distinction.[398]

## Applications

### Electromagnetic interference and pre-compliance

Direct probing frequently fails to reveal what is radiating from a board. The technique that works is to wand near-field probes over the board while watching a spectrum analyzer, building a map of where energy is coming from.[117] Near-field probes come in two forms, E-field and H-field, physically a stub or a loop, designed to respond to near-field rather than far-field radiation; making loop antennas by hand to fit into tight spaces on a board is standard practice when a commercial probe will not reach.[117] Alan Wolke described this probing practice with both homemade and purchased probes as routine in EMI diagnosis.[117]

The economics of compliance testing make bench measurement valuable: failing EMC compliance costs roughly $2,000 per retest with about three weeks between attempts, so blind iteration is financially ruinous, and that economics is what makes pre-compliance measurement on a bench analyzer worth the instrument's price.[183] In one instance related by consultant Scott Driscoll, an experienced test-house technician fixed a failing board by finding long traces that looked noisy on a spectrum analyzer, cutting them, and adding two ferrites; the pattern generalises to localising the radiating structure first, then applying the smallest mechanical change that kills it.[183]

The analyzer also quantifies layout decisions. Cutting a ground plane to route a signal across it costs roughly seven decibels of extra radiated emission, measurable on a spectrum analyzer; the fix is to patch the signal through a discrete wire, lay a copper patch over the break, and restore a solid plane, and the before-and-after measurement is what teaches the lesson.[704] A slot cut in a ground plane behaves as a slot antenna, and naming the mechanism makes the emission predictable rather than mysterious; closing the slot removes the radiator.[704]

An alternative iteration technique keeps hands inside the circuit: the analyzer identifies which peaks are failing, then an ordinary radio receiver is tuned to that frequency and the work proceeds by ear, poking components and hearing the spurious content attenuate, freeing the operator from watching a screen while probing. Jeri Ellsworth described using this method, listening to the result over a ham radio.[173]

### Field verification

Interference disputes can be settled by measurement rather than assertion. When Akiba of Freaklabs was told that a wireless system would interfere with a venue's radio microphones, the operators put both on a spectrum analyzer and showed the microphones at 850 MHz against a transmitter at 920 MHz; carrying the instrument turns a policy argument into a fact.[245]

### Production use

Production tuning can be automated by reading the analyzer over GPIB while stepper motors adjust inductors, driving the low end and high end of a tuner into specification without an operator; the instrument becomes a sensor in a closed loop rather than a display for a human. Vincent Himpe employed this arrangement in tuner production.[169] Conversely, a spectrum analyzer built into a dedicated production tester is scoped to one application, such as testing mobile phones, and is useless outside it despite impressive headline coverage; instruments sold in quantities of tens or hundreds are designed to one customer's test plan.[168]

### Measurement verification

A small two-layer demonstration board connected to a scope or analyzer makes an abstract specification concrete: it can show that a nominally 20-bit ADC is delivering 12-bit performance and where the missing eight bits went; a board ten centimetres a side and two layers is enough hardware to make that point.[492] A capital-starved startup can substitute a spectrum analyzer for a dedicated phase noise meter, taking the data down by hand; the measurement is available and only the convenience is missing.[101]

### Education

Cheap SDR hardware has a documented pedagogical role. Seeing filtering as narrowing onto the darker part of a spectrum display produces a mental shift that mathematics alone does not, and the hardware is now cheap enough that cost is no longer the obstacle to placing it in every signals course.[162] The standard pedagogical failure is three weeks of Fourier mathematics followed, at the end, by a frequency chart on an analyzer that makes the whole idea obvious in seconds; showing the measurement first supplies the motivation that carries a student through the theory.[725] Having a spectrum analyzer physically in front of a student while learning Fourier transforms supplies the reference point that abstract instruction lacks, and the general pattern is alternating hands-on work and theory rather than front-loading either.[444]

The skills gap is real in industry: most engineers cannot use a spectrum analyzer because electrical engineering education teaches the oscilloscope and the voltmeter and stops there, and the instrument is conceptually a different beast; the gap shows up exactly when EMI work begins.[165]

## The RF and microwave lab

For RF and FPGA development the three instruments that matter are the signal generator, the spectrum analyzer, and the logic analyzer; oscilloscopes remain useful for power supplies but are cheap enough not to drive the equipment budget.[101] Very fast oscilloscopes get little use in microwave work because the signals are sinusoids and nobody is chasing sharp rise times—the waveform shape carries no information there, so the spectrum analyzer displaces the scope as the primary instrument.[107]

Microwave work at very low power budgets can rely on unusual sources. A microcontroller PLL that tops out near 270 MHz, with substantial part-to-part variation between about 250 and 290 MHz, may expose only a quarter of that on an output pin because of the clock tree; transmitting at 900 MHz from such a part means generating around 69.5 MHz as a square wave and using its harmonic content, which is weak but real and visible to an analyzer.[667]

The physical lab must accommodate the instruments. Standard lab benches are too shallow for RF instruments; custom double-depth benches let a full-depth spectrum analyzer sit at the back while leaving a working area in front, which is a cheap fix compared with the equipment it holds.[169] For timing-critical work such as DSL development, a single reference clock—in one case a GPS-disciplined 10 MHz—can be distributed to every instrument in the lab over matched-length coaxial cable, where matching the cable lengths keeps the instruments phase aligned as well as time aligned; Himpe's lab used this arrangement.[169]

## Selection and ownership

### Frequency coverage

The analyzer's frequency ceiling should be chosen from the fifth harmonic of the highest signal to be measured, not from the fundamental: a bench working at a few hundred megahertz still needs gigahertz coverage to see the harmonic content that causes emissions problems.[73] Analyzer frequency ceilings are commonly software options over identical hardware—a unit sold at 2.1 GHz may have a front end capable of 3.2 GHz, unlocked by licence—so the hardware limit rather than the model number should be checked when planning headroom.[304] The RF front end of an analyzer lives inside a milled aluminium block, an islanded section isolated from the rest of the instrument, and that physical partitioning is what the price of the instrument largely buys.[304]

### Cost structure

Price scales with frequency range rather than with any other specification.[73] At the top of the range the cost is extreme: a 50 GHz instrument costs as much as a supercar, and the vendors in that space are Agilent, Rohde & Schwarz, and Anritsu, which is why microwave startups build their labs from second-hand equipment.[107] A complete general-purpose lab can be equipped for under $10,000, including a couple-of-thousand-dollar scope and a couple-of-thousand-dollar spectrum analyzer; RF is the discipline that breaks that budget.[567]

The accessories are not a rounding error: one engineer spent $3,000 on cables to accompany a $3,000 second-hand instrument, and interconnect should be budgeted at the same order as the instrument itself.[567] Input protection is a related practical concern: measuring a 50-watt amplifier without destroying the analyzer front end requires a specific block diagram of attenuation and coupling ahead of the input, a routine hazard in power measurement and the reason published example setups exist.[533]

### Used market and price history

Secondhand analyzers are the affordable route but are physically enormous, and freight can cost more than a new instrument for anyone outside the major markets; the purchase price is not the whole cost of ownership.[25] Very old analyzers remain usable for real work: a microwave engineer starting a company on a small budget ran a 12.4 GHz instrument built in 1968 that cost $100, then upgraded to a mid-1980s unit; age matters far less than coverage and calibration for this class of instrument.[107] Serious coverage is reachable on the used market—26 GHz laboratory analyzers such as the E4407B turn up at auction—and watching corporate liquidations is a viable acquisition strategy for instruments that are unaffordable new.[312]

The entry-level price collapsed rapidly. A 1.5 GHz analyzer with a tracking generator arrived at $1,500, a configuration that had been out of reach for an individual shortly before; the same capability had cost around $12,000 a year earlier, and before that the only route for an individual was a second-hand boat-anchor instrument from an auction site.[144] Bob Davidson, who worked at HP through the transition, described the same collapse from the vendor side: an analyzer that had been well north of $10,000 not long before became available for $1,000 to $1,500 from newer entrants.[144][232] Davidson also argued, from decades inside a test-equipment maker that once built its own front panels and silkscreens, that inspiration for the next design comes from being around manufacturing, so a company that outsources production keeps climbing the value pyramid until nothing is left—an argument about design capability rather than cost.[232]

At the bottom of the market, sub-$1,000 direct-from-China one-gigahertz analyzers advertised with a tracking generator should be treated as suspect: the specification is implausible for the price, and some of these designs still ship with a CRT rather than an LCD, which is itself a signal about the vintage of the design.[73]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 25 | NASA, WOTW & Modular Design - The NASA Nostalgia | https://theamphour.com/the-amp-hour-25-the-nasa-nostagia/ | |
| 73 | Horrisonous Holiday Habromania | https://theamphour.com/the-amp-hour-73-horrisonous-holiday-habromania/ | |
| 75 | An Interview with Ben Krasnow - Sprauncy Saccadic Spintherism | https://theamphour.com/the-amp-hour-75-sprauncy-saccadic-spintherism/ | |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 107 | An interview with Tony Long - Millimeter Microwave Magician | https://theamphour.com/the-amp-hour-107-millimeter-microwave-magician/ | August 5, 2012 |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ | August 23, 2021 |
| 144 | An Interview with Bob Davidson - Hoodied HP Hijinks | https://theamphour.com/the-amp-hour-144-hoodied-hp-hijinks/ | May 7, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 168 | Specialized and/or Open Source Test Gear and Dev Boards - Vacation Videography Vorboten | https://theamphour.com/168-specialized-and-open-source-test-gear-and-dev-boards-vacation-videography-vorboten/ | October 21, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 186 | Someone is watching...we think - Horme Hostility Hypochondriac | https://theamphour.com/186-someone-is-watching-we-think-horme-hostility-hypochondriac/ | February 25, 2014 |
| 209 | Headless Units and Baseless Batteries - KiCad Kickoff Kopophobia | https://theamphour.com/209-headless-units-and-baseless-batteries-kicad-kickoff-kopophobia/ | July 28, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 304 | Alexa joins the fray | https://theamphour.com/304-alexa-joins-the-fray/ | June 22, 2016 |
| 312 | Aussie Bound! | https://theamphour.com/312-aussie-bound/ | August 17, 2016 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 381 | An Interview with Derek Kozel | https://theamphour.com/381-interview-with-derek-kozel/ | February 25, 2018 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 444 | An Interview with Ben Eater | https://theamphour.com/444-an-interview-with-ben-eater/ | May 27, 2019 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 533 | Microwave measurement with Joel Dunsmore | https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/ | March 7, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
