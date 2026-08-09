---
title: Vector Network Analyzer
concept: vector-network-analyzer
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A vector network analyzer (VNA) characterizes electrical circuits by reporting gain and impedance as complex numbers, giving magnitude and phase together; every network other than a pure DC network has a complex impedance, so reactance appears in the measurement as a phase angle change.[533] Network analyzers come in scalar and vector forms, and the vector instrument is the one that recovers phase as well as magnitude.[347] Instruments lacking vector capability run into trouble specifically with purely reactive components, cannot present results on a Smith chart, and are harder to calibrate.[465] An oscilloscope can display the sine waves involved but makes it awkward to extract magnitude and phase, which is the practical reason to reach for a VNA when complex impedance is the quantity of interest.[533]

## Principle of operation

In operation a VNA emits a sine wave stepped across frequency and observes how much of it comes back, the same reflection physics that governs a PCB trace or any other impedance-matched structure.[496] Measuring impedance at RF reduces to measuring the reflected wave, because reflection coefficient and impedance are related by a fixed equation: on a 50 ohm line terminated in 60 ohms, the reflection is fully determined.[446] A vector network analyzer and a radar are architecturally the same class of device, both transmitting a stimulus and analysing the returned signal, which is why the same hardware platform can plausibly serve as both.[214]

Separating the returning wave from the outgoing one on a single line requires a bidirectional coupler, which siphons off part of the reflected energy; getting that coupler accurate over a wide bandwidth is the hard engineering problem and a large part of what a good instrument costs money for.[446] Beyond the coupler an instrument needs amplifiers and a frequency synthesizer, and off-the-shelf synthesizer parts covering roughly 10 MHz to 6 GHz can be programmed by a microcontroller to emit a commanded frequency, so an instrument can step to the band of interest and then read the reflected wave there.[446] Beyond one port, useful measurement means multi-port setups and the S-parameter formalism, in which transmission and reflection between every pair of ports is expressed.[496]

## Calibration

Calibration means measuring artifacts whose true values are known and then correcting subsequent readings toward those true values; solving for impedance on a vector instrument requires three known standards, conventionally an open, a short and a load.[533] Because a vector instrument captures both amplitude and phase, a phase error anywhere in the measurement path can be calibrated out, which a scalar instrument that only sees magnitude cannot do.[465] Running the supplied calibration kit standards through a fixture — the through plus the short, open and load — yields a sophisticated model of what the test jig contributes to every measurement, which is what lets the fixture be removed from the result.[465] When adapters and converters are used to reach a different connector family, the working approach is to accept them as part of the measurement setup and calibrate with the adapters already in place rather than calibrating bare and adding them afterwards.[533]

### Standards and connectors

Commercial calibration opens and shorts are physically offset from the connector reference plane, so on a Smith chart they trace an arc rather than collapsing to a single point.[533] This produces a recurring beginner complaint that connecting the calibration short does not produce a single dot on the display; the explanation is the physical offset, which the instrument makers' naming choice from the early 1970s onward hid by calling the parts plainly open and short rather than offset open and offset short.[533] Dunsmore, who worked on these standards, judged the naming an industry mistake.[533]

Gendered RF connectors leave a small air gap when a calibration load is mated, because the pin seats into the socket with slight clearance; that gap behaves like a small series inductance, which the instrument's error correction measures and subtracts.[533] The APC7 connector is sexless, with a collet and spring giving a mating junction of zero offset, so its shorts are true shorts, its opens are close to ideal and its load has no mating discontinuity — a property that mattered enormously before error correction became routine, after which instruments kept the connector out of inertia rather than necessity.[533]

### Verifying a calibration

A calibration will always appear to succeed. Applying the open, short and 50 ohm load lets the instrument compute correction coefficients that make the open trace flat and the load land at the centre of the Smith chart regardless of whether the calibration was actually valid, so a beginner has no built-in reference for whether the result is trustworthy.[496] The available sanity check on a suspect measurement is physical plausibility rather than the instrument itself: a passive part cannot plot outside the boundary of the Smith chart, so a trace that leaves the chart indicates a bad calibration or setup rather than a device radiating energy.[496]

## Antenna measurement

Before measuring a phone antenna, the antenna is cabled out — a cable is attached at the antenna feed and its shield grounded to the PCB, so the cable itself does not perturb the measurement — and only then is the assembly connected to a VNA to read impedance.[446] A sweep gives VSWR against frequency, where a VSWR of one means a perfect match, so the plot shows where the antenna is tuned and which direction it needs to move.[446]

That result is necessarily partial. A working antenna needs two independent things, a structure that supports radiation and a match to 50 ohms, and a plain 50 ohm resistor terminating a VNA port reads as a perfect match while radiating nothing — the standard demonstration that a good match is not evidence of a working antenna.[446] Once impedance is matched, the next measurement is radiation efficiency, taken in an anechoic chamber that integrates radiated power over all directions, and an antenna programme iterates on the pair of measurements, impedance against frequency and efficiency against frequency.[446] Antenna qualification normally consists of passive VNA measurements plus over-the-air measurements in an anechoic chamber, and that pair is sufficient for the overwhelming majority of cases; active measurements with the radio actually transmitting and receiving are reserved for cellular antennas and are rare, since roughly 99 percent of verification is achievable passively.[678]

Faults surface quickly on the instrument. Putting a suspect antenna module on a VNA revealed two independent problems at once: the radiator was the wrong physical size and therefore resonant at the wrong frequency, and the ground plane it was mounted on was too small to support it.[464] A fractal antenna gets its electrical length by folding the conductor back on itself so a long radiator fits a small area, which is what made compact phone antennas practical, but it still requires a ground plane of comparable size to work.[464] Structures not intended as RF parts are legitimate subjects too: a metal block heatsink bolted to chassis ground and sitting close to an antenna feed trace can usefully be put on a VNA, because what matters is its actual impedance at frequency rather than its intended thermal role.[520]

## Signal integrity and board work

A vector network analyzer is used in signal integrity work in both frequency and time domain, unlike RF practice where the time domain response often matters less; in signal integrity the concern is fast edges reflecting off impedance discontinuities along a transmission line, which is inherently a time domain picture.[421] Time domain results can be obtained two ways: directly with a time domain reflectometer, or by sweeping reflection and transmission against frequency on a VNA and applying a transform to convert the frequency domain data into a time domain response.[421]

Fabricated trace impedance varies within a manufacturing tolerance band, so a nominal 50 ohm trace may arrive at 45 or 55 ohms and the only way to know is to measure.[494] Test coupons therefore carry deliberately laid out controlled impedance traces with an SMA connector footprint at each end, so the trace can be connected to a VNA or a TDR and its characteristics measured; large companies with impedance-critical products staff an incoming inspection function whose job is measuring returned boards continuously.[494] One controlled impedance failure traced through two days of debugging turned out to be an unannounced change of board house with a completely different stack-up, leaving the measured trace impedance off by a factor of two, reading about 25 ohms where 50 was designed, and the conclusion drawn was to send an explicit stack-up drawing rather than trusting a verbal description.[494] The delay came from the natural first assumption that a measurement disagreeing with expectation is operator error with an unfamiliar instrument; eliminating every other explanation is what eventually forced attention back to the stack-up.[494]

Measuring the capacitance of ground plane pairs in a four-layer board requires sweeping well past the 50 MHz limit of a low-frequency network analyzer, because the interesting behaviour only begins around 50 to 100 MHz.[710]

## Simulation as a substitute

If S-parameters for a board can be computed, essentially every electromagnetic question about that board is answerable, which is why a field solver aims to reproduce what connecting the physical board to a vector network analyzer would measure.[626] A three-dimensional Maxwell solver can stand in for the instrument by letting a designer place virtual input and output ports on an imported board and sweep S-parameters across frequency, which allows signal integrity and isolation to be compared between candidate routings before fabrication.[626]

## Instruments and the market

The two specifications that determine whether a given instrument is usable for a job are frequency range and dynamic range. Small handheld units offer roughly 40 dB up to a gigahertz or about 70 dB at 500 MHz, whereas an older bench instrument from the classic vendors delivers on the order of 80 to 100 dB.[449] A modest low-cost instrument is adequate for impedance matching, transmission line work and antenna tuning, but not for full component characterization, which is where the dynamic range and accuracy of a large bench instrument are needed.[449] A buyer therefore faces two distinct paths, a new low-end instrument or the used equipment market, and the choice is shaped by the frequency range actually needed, since covering to three gigahertz is a different problem from covering tens of megahertz.[449]

Prices span several orders of magnitude. Around the mid-2010s the entry price for a new instrument sat near three thousand dollars, so the used market on auction sites was the realistic route for a small lab, and even secondhand units were expensive.[347] Decades-old bench analyzers with floppy disk drives still commanded around six thousand dollars secondhand, which sets the reference price against which any new low-cost instrument is judged.[462] New instruments from the value-oriented Chinese vendors started around three and a half thousand US dollars before software option upgrades.[462] At the top, a 40 GHz instrument ran roughly forty thousand dollars and a 68 GHz instrument around half a million, placing high-frequency measurement capability inside institutional rather than individual budgets.[472] Instruments reaching 60 GHz can cost over half a million dollars, more than a house in many US cities, and serve a very small worldwide population of users, a price structure that follows directly from how few organizations need microwave measurement at that frequency.[479]

Cost has consequences for how work is organised. Expensive shared measurement equipment constrains how distributed a hardware team can be: a fifty thousand dollar instrument is not something an engineer takes home, both because of company policy and because coworkers need access to the same unit.[514] Conversely, having a 40 GHz instrument permanently available changes how an engineer works, because the marginal cost of measuring one more thing is zero and everything gets put on the instrument; losing that access after leaving a well-stocked RF lab is a real loss of capability.[472]

### The HP 8753

The HP 8753 is a vector network analyzer dating from the late 1980s and early 1990s that remained a live reference point decades later, used as the side-by-side comparison against which newer instruments were judged.[613] Joel Dunsmore developed much of its RF front end, remained at the successor company, and wrote books both on the development of that instrument and on using a VNA effectively.[532] The 8753ES variant bundles an internal test set with the analyzer, meaning the RF relay switching needed to route the stimulus is built in, so full S-parameter measurements can be made without assembling external switching hardware.[462]

Old instruments remain serviceable. Keyzer rebuilt the step attenuator on a secondhand 8753 and put it into working service in a home lab, arguing for it on fluency — it was the analyzer he used in college and in his first two RF jobs, so he can operate it almost without looking, which outweighs its very large bench footprint.[655] Newer alternatives include headless instruments that have no front panel and are driven entirely from a host computer, which is how the size problem of the older boxes gets solved.[655]

## Low-cost and self-built instruments

The scarcity and cost of vector network analyzers motivated at least one antenna designer to build his own, on the reasoning that the instrument is among the most critical tools for measuring RF and antennas.[446] Bevilacqua found the bidirectional coupler took many iterations, working between cheap catalogue couplers from a distributor and printed couplers etched directly on the circuit board, which achieve roughly the same function.[446] The resulting two-port instrument covering 400 MHz to 2.7 GHz handles Bluetooth and low- and high-band cellular work, and its advantage over professional bench instruments is size and weight, being roughly the bulk of a large phone.[446] Sold as a low-cost two-port instrument with a calibration kit built in, it was aimed specifically at characterizing antennas and was designed by an antenna engineer who had not previously done PCB layout and iterated through many revisions.[347] A lower frequency limit of 400 MHz excludes work below the RF bands, and an engineer working mostly at lower frequencies would want coverage extending down toward kilohertz.[347]

Another homebuilt instrument covering 30 MHz to 6 GHz was implemented on an ordinary low-cost prototyping-service PCB using simulated stripline structures, laid out in KiCad, with the software built on an existing open source SDR codebase.[312]

One argument against a portable instrument with a built-in screen is that a USB-connected unit driven from a PC gives a far better interface for the analysis work than six buttons and a small display, though most instruments of this class are bench units with their own screens.[347]

## Operating skill

An engineer with decades of instrument experience judged that a VNA is not a device he could pick up and use without a refresher course, in contrast with a dynamic signal analyzer, which is essentially a network analyzer for audio circuits where twenty kilohertz counts as high frequency.[496] Knowing when the instrument is genuinely required is itself a skill; for most non-antenna work an engineer concluded he did not need one, and that what he actually wanted for inspecting circuit board behaviour was closer to a TDR.[710]

Technique matters at the probe as well. When landing an RF probe on a chip, the probe is connected to a VNA and the S11 reflected energy watched as contact is made, since that drop is the indication of correct landing; judging contact by pressure instead risks destroying the probe, because at high frequencies the probe is the fragile element and the discontinuity that ruins the measurement.[729]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 312 | Aussie Bound! | https://theamphour.com/312-aussie-bound/ | August 17, 2016 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 446 | An Interview with Pete Bevelacqua | https://theamphour.com/446-an-interview-with-pete-bevelacqua/ | June 9, 2019 |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ | June 30, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 464 | KonnectorPanik | https://theamphour.com/464-konnectorpanik/ | October 27, 2019 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 479 | Why isn't this working? | https://theamphour.com/479-why-isnt-this-working/ | February 13, 2020 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 496 | Drab Olive | https://theamphour.com/496-drab-olive/ | June 14, 2020 |
| 514 | Focus, Dammit | https://theamphour.com/514-focus-dammit/ | October 25, 2020 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 532 | Recalling Recalls | https://theamphour.com/532-recalling-recalls/ | February 28, 2021 |
| 533 | Microwave measurement with Joel Dunsmore | https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/ | March 7, 2021 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 655 | The Twelfth Day of Keyzermas | https://theamphour.com/655-the-twelfth-day-of-keyzermas/ | January 8, 2024 |
| 678 | All About Antennas with Katerina Galitskaya | https://theamphour.com/678-all-about-antennas-with-katerina-galitskaya/ | September 30, 2024 |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ | December 6, 2025 |
| 729 | The Terahertz Frontier with Greg Charvat of Teradar | https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/ | July 22, 2026 |
