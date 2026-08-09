---
title: Analog To Digital Converter
concept: analog-to-digital-converter
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

An **analog-to-digital converter** (ADC, or A/D converter) is an electronic device that converts a continuous analog signal into a discrete digital representation, and it sits at the boundary between physical sensors and digital processing in almost every electronic system.[274][119] The nominal bit count of a converter does not equal its usable resolution: a 24-bit part in a handheld power-measurement instrument returned roughly 18 effective bits at its highest sample rate and little more than 19 when slowed down.[218] Converter selection and the surrounding signal-chain design, rather than the part's headline specification, determine the performance actually delivered, and a common outcome on real boards is that a 20-bit converter yields 12-bit performance, the missing bits having been lost to the surrounding design rather than to the part itself.[492]

## Resolution and effective number of bits

The number of bits printed on a converter's part number is not the number of usable bits, because noise and non-idealities in the converter and its environment consume the lowest-order bits.[218] The shortfall varies with the converter's context: a 12-bit converter embedded in an FPGA may deliver only about eight effective bits because the digital process the part is built on constrains analog performance, and the 12-bit converter inside a Bluetooth Low Energy system-on-chip was measured at three effective bits, adequate only for confirming whether a load is on.[219][218]

Effective resolution can be recovered or improved by system-level techniques. Most oscilloscopes use an 8-bit converter and recover extra resolution in a high-resolution mode that averages adjacent samples, producing an effective 10 to 12 bits from 8-bit hardware.[106] High-resolution mode is a boxcar, or rolling-average, filter applied after the sampling stage and before processing, and some instruments expose it as a menu choice of 8, 9, 10, 11 or 12 bits from converter hardware that is only 8 bits wide.[455] An instrument revision that moved from a 14-bit converter with 12.1 effective bits to a 16-bit converter with 15.1 effective bits—an improvement of about eight times—achieved the gain through changes to amplification, filtering and supply noise alongside the converter change, not by changing the converter alone.[607]

A simple relation ties the jitter of a converter's sampling clock to the maximum effective number of bits achievable, so clock jitter sets a hard floor on a sampling system's resolution regardless of the converter itself.[228]

## Dynamic range

Dynamic range in decibels is approximately six times the number of bits, so the 16-bit compact disc standard corresponds to about 96 dB.[270] Even the best 24-bit converters restricted to about 2 kHz of bandwidth reach only around a −130 dB noise floor, meaning the full 24 bits are never available in practice; at that level the thermal noise of the surrounding resistors becomes the limit.[270]

A single signal path cannot deliver 32 bits of dynamic range however heavily a delta-sigma converter is oversampled, because amplifying a very quiet signal amplifies the front-end noise with it; recorders claiming such range use two amplification paths and stitch the results together, in the manner of a multi-range meter.[658] Covering five orders of magnitude of current without range switching requires a 24-bit converter, a low-noise environment, and wider supply rails, because the fixed-gain amplifier on the sense shunt can only swing within its rails; moving from a few volts to plus-and-minus-fifteen-volt rails buys a corresponding increase in usable dynamic range.[301]

## Sampling, aliasing and reconstruction

Anti-aliasing filtering ahead of the converter is mandatory rather than optional: content beyond the Nyquist frequency folds into the band of interest at sampling and cannot be removed afterwards.[392] A reference design's front end is valid only for the sample rate it was drawn for; changing the sample rate changes the required anti-aliasing filter, so copying the recommended circuit at a different rate silently invalidates it.[301]

Nyquist governs aliasing, but faithful waveform reconstruction is a separate requirement: about 2.3 times oversampling with sin(x)/x interpolation guarantees the displayed sine wave is legitimate on a Gaussian-response instrument, and a non-Gaussian roll-off changes the figure.[570] High-speed real-time oscilloscopes used for HDMI and DisplayPort compliance work oversample by little more than two times, which is adequate for mask testing but glosses over fine detail that a general-purpose measurement would need.[570] Resolution and sample rate trade against each other in an oscilloscope front end: high bit counts are readily available at low speed, and the engineering difficulty is achieving them at high sample rates.[677]

In a sampling oscilloscope the bandwidth is set entirely by the front-end sample-and-hold, which captures the signal in a picosecond-scale window and then holds it; conversion can then be done arbitrarily slowly, so a 10 GHz-bandwidth instrument can use the converter inside a 30-cent microcontroller.[178] Such a sampling front end has no attenuator and only a 50-ohm input, so probing a high-impedance source requires an active probe that can cost many times the instrument.[178]

## Architectures

### Successive approximation

A successive-approximation register (SAR) converter presents a switched capacitor of roughly 20 to 30 picofarads at its input on every sample, and that capacitance must settle within the sample period.[392] SAR converters have moved into resolutions of 18 to 20 bits that were formerly delta-sigma territory, and have absorbed the integration that characterised delta-sigma parts: internal references and reference buffers, programmable gain amplifiers and excitation current sources, with size and power falling in parallel.[348] A 20-bit SAR converter running at 500 kilosamples per second is an unusual combination of resolution and speed and is priced above twenty dollars, placing it outside all but precision-market designs.[150]

### Delta-sigma

Delta-sigma converters need very little front-end filtering; the residual case is a very wideband front end producing noise high enough in frequency that even the converter's oversampling folds it back into the baseband, and a small RC network suffices to remove it rather than a brick-wall filter.[476] The latency of a delta-sigma converter is high but constant and predictable because the conversion is largely digital, so it can be planned around wherever synchronisation is not required; the architecture suits low-bandwidth work such as DC to 20 kHz audio, and oversampling ratios of 64 or 256 times are ordinary.[474] For low-frequency measurement work, resolution rather than speed is usually the binding requirement, and a delta-sigma converter integrates high-frequency noise away as part of its operation.[199] Audio-grade delta-sigma parts reach total harmonic distortion around −110 dB, equivalent to roughly three microvolts RMS across the audio bandwidth.[474]

### Historical context

Before delta-sigma converters became routine, data acquisition systems built on sampling converters needed a front end of gain, transducer interfacing and steep anti-aliasing filtering, and that requirement supported a market for purpose-built analog filters supplied in thousands or tens of thousands of channels at a time.[476] Converter research is mature enough that new architectures rarely have a unique application to justify them, so results are argued on energy per conversion or on speed rather than on capability no other part offers.[579]

## Front-end and signal-chain design

Filtering discards information, so filtering in the analog domain before conversion lowers the sample rate and dynamic range the converter must provide, often permitting a 12-bit part in place of a more expensive one, and it reduces the processing load on the FPGA or microcontroller behind it.[392] A sensor with 10 to 50 kilohms of source impedance cannot settle a SAR converter's input capacitance to 16-bit accuracy, which is why a driving amplifier is required.[392] The RC network between the driving amplifier and the converter input has a two-sided constraint: too much series resistance increases converter distortion, too little and the amplifier cannot drive the load.[392] Datasheet performance figures are quoted with the best available driving amplifier, which can consume as much power as the converter or more; where the application does not need every specification, a driver of a quarter the capability may be the better system choice.[392]

The standing rule is to convert as close to the sensor as possible, so that the signal spends the shortest possible path in the analog domain where it can pick up noise.[274] System designers push the conversion point ever closer to the sensor or antenna, and that pressure is what forces converter performance upward; the analog front end between the real-world interface and the first converter remains a distinct engineering discipline.[119]

In an ultra-high-performance converter signal chain the AC-coupling and sampling capacitors are selected for their analog behaviour, not their tolerance, because dielectric performance rather than value error sets the achievable distortion.[502] An instrument input left open in a high-impedance mode accumulates charge on the front-end input capacitance, so a converter reads a drifting or implausible voltage with nothing connected.[293]

### Grounding and return currents

The older prescription of separate analog and digital ground planes joined at a single point beneath the converter has been superseded by the discipline of tracing where return currents actually flow and partitioning the board accordingly, keeping sensitive analog away from switching circuitry.[270] At 115 to 130 dB of system dynamic range, a 1 V RMS signal implies a noise budget in the low nanovolts, so routing a power amplifier's ground return past the converter modulates its ground reference and destroys the dynamic range the converter was bought for.[270] Application notes and reference designs show how to make one device perform well in isolation; system performance instead requires asking, for each part of the circuit in turn, how everything else in the system can interfere with it, including switching supply rates beating against converter and PWM rates.[270] Placing a digital isolator immediately after the converter guarantees that no return current from downstream digital circuitry can flow through the analog front end, an alternative to controlling that current by layout alone.[185]

### Digital interfaces and termination

Wide parallel buses out of video converters—where three 12-bit colour channels plus clock and sync can total 36 or more signals—are ruined by misplaced termination: a series or source termination belongs at the driver, an end termination at the far end of the line, and an unterminated line reflects until its energy dissipates, corrupting clock edges and causing sampling at the wrong instant, an error that cannot be corrected after layout.[452] A small series resistor and capacitor to ground is a legitimate way to bandwidth-limit energy leaving a board on a cable, but designers who confuse that filter with a termination resistor and fit a 27 or 33 ohm part alongside a large capacitor roll off the bandwidth the signal actually needs.[452] Moving data out of converters running at hundreds of megasamples per second drove a dedicated multi-gigabit serial standard, JESD204, and the FPGA primitives to receive it; modern high-speed converters use such serial links in place of wide parallel buses.[103]

## Integration

### Process constraints

Integrating a usable analog-to-digital converter into a microcontroller is comparatively easy; integrating a good digital-to-analog converter on the same die is hard, and the difficulty rises as the microcontroller's cost falls.[87] Converters embedded in FPGAs and processors are generally modest 12-bit delta-sigma designs because the leading-edge digital process the die uses tolerates that and no more; reaching 24-bit performance requires a different process or external devices.[156] Integrating an excitation circuit, converter and power stage on one die forces a single process choice, so highly integrated sensor front ends carry limited specifications—a process optimised for converters will not also give low-resistance power FETs—and precision work still needs the discrete excitation and normalisation circuitry the integrated part replaces.[216] Twelve bits is the routine specification for a converter integrated on a microcontroller, but linearity and performance near the bottom of the range are typically poor, which is what distinguishes it from a standalone converter of the same nominal resolution.[264]

### Microcontroller peripherals

Some microcontrollers can run the converter as an autonomous peripheral: a timer triggers a conversion, the result is stored, and the processor core is woken only when the result FIFO fills, which removes the core's power draw from the sampling loop entirely.[187] A direct-memory-access path from the converter to RAM that runs without powering up the processor core makes a complete data logger out of the peripherals alone.[95] In real-time control the sampling instant matters as much as the sample: linking the PWM compare events to the conversion trigger fixes the sample at the same point in every switching cycle, making the control loop deterministic, and converters in this class of part run to about 12 bits and several megasamples per second across several channels.[212]

The ESP8266 was designed as a Wi-Fi chip for cheap tablets with standalone operation added as an afterthought, which is why it has so few peripherals and only a single converter channel; its successor was designed for connected devices first.[359] The internal comparators of an FPGA can be operated as a converter, removing a separate part from the bill of materials where the required performance is modest.[549]

### Integrated measurement devices

An integrated power monitor measures bus voltage and shunt current through an input switch and computes power internally from a programmed shunt value, returning voltage, current or power over I2C.[88] Comparing such a part against discrete equivalents must include the parts the converter implies: a one-dollar power-monitor device combining a programmable gain amplifier, a 12-bit converter, shunt and calibration registers and an I2C interface, with 10 microvolts typical and 40 microvolts maximum offset, is difficult to beat on cost or board area once the external reference and amplifier are counted.[88] Consolidation has left essentially two suppliers for precision analog building blocks such as instrumentation amplifiers, and the surviving vendors increasingly package the amplifier, converter and microcontroller as one application-specific measurement device rather than selling the blocks separately.[601]

Nearly every handheld multimeter below the highest price tier is built on a dedicated multimeter chipset that integrates the converters, range switching, auto-ranging and the capacitance, diode, continuity, resistance, voltage and current modes, because implementing that switching and timing from scratch is a substantial design in itself.[370] Building a multimeter from a microcontroller's converter and discrete range-switching transistors instead is possible but transfers the whole burden of switching, timing and mode handling to the designer, and instruments have been shipped that got it wrong.[455] Displaying 10,000 counts at one microvolt resolution requires the noise to be held to half a count, which no processor-integrated converter achieved; separating the processor from the delta-sigma converter reached roughly 19 flicker-free bits.[180]

### Silicon defects and verification

Silicon defects in integrated converters are documented deep in errata rather than in the datasheet body, so a part can be selected on its headline specification and only later found not to deliver it.[432] Converter non-linearity that a vendor's own testing never provoked was found by a customer stressing the part harder; the results were reproduced with the designers, traced in simulation, fixed in a silicon revision that became a new part suffix, and published as errata against the old one.[485] Medical and defence practice treats a converter's datasheet specification as a claim to be verified on the finished board with recorded analysis, where a startup selects a part that meets the specification on paper and proceeds.[588]

Characterising a converter by sweeping it and reading the result with a bench multimeter produces artefacts from the measuring instrument: auto-ranging introduces a step in the INL and DNL plot at each range change because accuracy differs per range, and the meter's own multi-slope conversion adds further structure, so the defect appears to be in the device under test and is not.[169]

## Market structure and selection

A survey of the converter market counted 2,412 devices from 24 manufacturers, averaging about a hundred parts per manufacturer, with some vendors offering more than 500 and several offering only one or two.[49] Distributor parametric search is inadequate for selecting a converter; the manufacturers' own parametric tools carry the parameters that decide the choice.[49] A workable selection method across thousands of candidate parts is to pull the field into a spreadsheet and eliminate whole manufacturers and families at a time rather than compare parts individually.[191]

Low-power 16-bit converters are readily available at a few hundred samples per second, and only a handful of the thousands of parts on the market combine low power with kilohertz-rate sampling; the part selected in one such search consumed 108 microwatts at an 8 kHz sample rate and delivered 18 bits.[191] Pricing of integrated converters is not proportional to their performance: a microcontroller with a 12-bit converter on board can cost less than half the price of a standalone converter of similar specification.[87]

At the top of the performance range the supply is a duopoly: for a world-leading 24-bit converter behind a charge amplifier front end there were two viable parts, one holding about 90 percent of the market, and independent design teams therefore converge on the same front end because they select the same converter and then follow its application notes.[36] Leading-edge low-data-rate 24-bit converters were made by about three companies worldwide and cost a couple of hundred US dollars each.[335] Converters at the extreme of performance can be designed for a single industry: one part was made for underwater seismic survey work with perhaps five customers worldwide and no distributor listing.[567] Converter capability that once had to be designed in-house at a test and measurement company is now bought as a twenty-dollar catalogue part in small quantities, though a high-performance converter still gives poor results behind poor cabling.[601]

## Applications

### Oscilloscopes and instrumentation

Oscilloscope practice centres on recovering resolution from fast 8-bit converters by averaging, on reconstruction rules tied to the instrument's roll-off, and on sampling front ends that separate capture from conversion.[106][455][570][178]

### Current and power measurement

Measuring the current of a modern device means covering an active current in milliamps or amps and a sleep current in microamps in the same record, a span that exceeds what a single affordable converter can resolve.[527] Burden voltage across the sense resistor sets the limit on how wide a current range a single shunt can cover; twenty millivolts of burden voltage over a million-to-one range leaves only tens of nanovolts at the bottom, which is why range switching is unavoidable.[607] Most auto-ranging instruments stop measuring during a range change, for milliseconds or longer, while the analog path resets, and continue to display a reading throughout; measuring continuously across a range change requires a second converter channel held permanently at the widest range so the switched channel can be reconstructed.[607] When a target device's current jumps from microamps to an amp in under a hundred microseconds, a slow range change causes a burden-voltage drop large enough to brown out the device under test; sub-microsecond auto-ranging avoids it, and an FPGA rather than a microcontroller is used to hold two converters in sync and meet that deadline, with one instrument auto-ranging in less than 1.2 microseconds.[527] Converter resolution cannot rescue a shunt chosen for the wrong range: a 0.1 ohm shunt sized for 10 amps leaves microamp currents below the noise regardless of whether a 12-bit or 16-bit converter follows it.[623]

An isolated Hall-effect current sensor centred at half its supply, combined with a converter offering programmable upper and lower thresholds, flags an out-of-range current on either half cycle of an AC waveform without firmware in the loop, allowing the drive to be cut before a MOSFET is destroyed, where a comparator alternative would require switching polarity every half cycle.[524]

### Control and power conversion

A software-controlled switching power supply was built around a microcontroller chosen specifically for a 2-megasample-per-second 12-bit successive-approximation converter, because a short lag between sampling and the regulation decision is what makes closed-loop control in firmware viable.[640] Raising a measurement instrument's sample rate from about 4 kilosamples per second to 250 kilosamples per second was done with two four-channel simultaneous-sampling converters rather than one multiplexed part, so that all eight channels represent the same instant.[640] Maximum power point tracking is implemented by measuring panel voltage and current with the charger's internal converter, stepping the presented input impedance, and repeating until the power peak is passed, then re-running as illumination changes; a part advertised as supporting the technique may only document it as an application note requiring an external microcontroller rather than performing it internally.[512]

### Audio

Audio product specifications routinely exceed what the application needs, with 24-bit converters running near 200 kHz sample rates where much lower figures are sufficient; matching converter and driver cost to the specification actually required is the design problem.[573] The noise floor of built-in PC and laptop audio chipsets is poor enough to make them unusable for quality capture; putting the preamplifier and converter together in a shielded, separately regulated box at the microphone, and sending the result over USB, removes the analog run through the noisy computer entirely.[27]

### Radio and radar

A through-wall radar was architected to convert to a 10.7 MHz intermediate frequency so an off-the-shelf crystal filter could be used, with the local oscillator set so the wall return fell into the noise and the targets passed; the signal was then brought to baseband and digitised with a 200-kilosample-per-second 16-bit converter, a deliberately low-bandwidth converter being how large dynamic range is obtained cheaply.[115] Wide-bandwidth radio astronomy instruments must down-convert because no converter covers the bandwidth directly; the received band is heterodyned to an intermediate frequency and digitised a few gigahertz at a time, then windowed and processed with an FFT, with thousands of spectra averaged to bring signals out of the noise.[483] At millimetre-wave frequencies the converters, not the radio, set the usable bandwidth, and the power cost of high conversion rates is what rules them out of mobile equipment rather than any radio limitation.[483]

A software radio's first generation used a single analog device combining dual converters in each direction, giving a very sparse board; higher sample rates and precision were only available as separate parts, so the later generation used six chips with far more pins, and the pin count is why the newer boards carry one antenna each with multiple-antenna operation done by tying boards together.[101] A VGA capture dongle is three high-speed converters, one per colour channel, which is why such devices can be repurposed as multi-channel software radio front ends.[391]

### Imaging

CMOS image sensors are made on standard semiconductor processes and allow the control logic and converters to be integrated on the sensor die, which CCD processes do not.[325] High-speed image sensor readout multiplexes columns down to a fixed bank of converters—in one case sixteen converters at 90 MHz fed by multiplexers selecting groups of sixteen of the 1280 column lines—and frame rate is traded against window height because that bank is the bottleneck.[325]

### Seismic acquisition

A seismic acquisition system ran to 10,000 channels with the converter alone costing about one hundred dollars per channel, so converter selection at that scale is a system cost decision rather than a component one.[65] Underwater seismic streamers 100 metres long carry some of the quietest converters made, with noise floors around −136 dB, and a rise of a fraction of that figure is enough to ruin the survey data.[532]

### Security and test

A digital sensor is only as trustworthy as its converter, so an attack against the conversion step generalises across every sensor type built on the same approach rather than being specific to one device.[352] Power-analysis measurement uses a low-noise amplifier ahead of a 10-bit converter at about 105 megasamples per second; the quantity of interest is a fluctuation of the order of ten millivolts across a small series resistor, and the required sample rate follows the clock frequency of the device under test because the interesting events occur at clock edges.[239] Feeding an analog sensor into the converter of a wireless microcontroller couples transmitter energy into the measurement, and the function built on it stops working while transmitting; additional decoupling and a pi filter improved the result substantially but did not remove the disturbance during active transmission.[657]

Designing for self-test means reserving converter channels and spare pins to measure the voltages and logic levels that the test needs to check; choosing a microcontroller with more pins than the function requires, and connecting the spares to points of interest, allows tests to be added in firmware later instead of by modifying boards.[125] Because an integrated circuit cannot be probed or modified with bodge wires after fabrication, on-die converters for internal voltage and current measurement are the equivalent of test points, letting a designer establish why a design failed and iterate rather than treating a tape-out as final.[501]

### Other measurement techniques

Impedance can be measured by taking the forward and reflected waves into a detector chip that outputs one voltage proportional to magnitude and another proportional to phase, digitising both, and computing the complex reflection coefficient from which impedance follows directly.[446]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 27 | 555 Contest, Computer Museum, Octopart - The Green Pen Hornswoggle | https://theamphour.com/the-amp-hour-27-the-green-pen-hornswoggle/ | |
| 36 | Big Business Buffoonery | https://theamphour.com/the-amp-hour-36-big-business-buffoonery/ | |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | |
| 65 | Silego, ADCs & Seismic Detection - Dave's Dingo Dystocia | https://theamphour.com/the-amp-hour-65-daves-dingo-dystocia/ | |
| 87 | An Interview with Ian Daniher - Nascent Nonolith Numquid | https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/ | |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 95 | An Interview with Øyvind Janbu - Feracious Fabless Facilitator | https://theamphour.com/the-amp-hour-95-feracious-fabless-facilitator/ | |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 115 | An Interview with Dr Greg Charvat - Watcher of Wraithlike Walls | https://theamphour.com/the-amp-hour-115-watcher-of-wraithlike-walls/ | September 30, 2012 |
| 119 | An Interview with Dr. Kent Lundberg - Luculent Linear Legacy | https://theamphour.com/the-amp-hour-119-luculent-linear-legacy/ | October 28, 2012 |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 150 | Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness | https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/ | June 17, 2013 |
| 156 | Tesla, FPGAs and DigiKey - Zesty Zippy Zynq | https://theamphour.com/the-amp-hour-156-zesty-zippy-zynq/ | July 29, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 180 | An Interview with Dave Taylor - Multi-talented Meter Maker | https://theamphour.com/180-an-interview-with-dave-taylor-multi-talented-meter-maker/ | January 13, 2014 |
| 185 | An Interview with Hank Zumbahlen - Zoppa Zumbahlen Zateticism | https://theamphour.com/185-an-interview-with-hank-zumbahlen-zoppa-zumbahlen-zateticism/ | February 17, 2014 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 199 | The 2014 Maker Faire Show - Traveling Technology Trangam | https://theamphour.com/199-the-2014-maker-faire-show-traveling-technology-trangam/ | May 19, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 228 | An Interview with Shahriar from The Signal Path - Quisquous Quivering Quadripole | https://theamphour.com/228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole/ | December 16, 2014 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 335 | When the TV watches you | https://theamphour.com/335-when-the-tv-watches-you/ | February 8, 2017 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 352 | Conning with Michael Ossmann | https://theamphour.com/352-conning-with-michael-ossmann/ | July 17, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 392 | An Interview with Matt Duff | https://theamphour.com/392-an-interview-with-matt-duff/ | May 13, 2018 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 446 | An Interview with Pete Bevelacqua | https://theamphour.com/446-an-interview-with-pete-bevelacqua/ | June 9, 2019 |
| 452 | An Interview with Kieran O'Leary | https://theamphour.com/452-an-interview-with-kieran-oleary/ | July 28, 2019 |
| 455 | Bill and Dave's Excellent Equipment | https://theamphour.com/455-bill-and-daves-excellent-equipment/ | August 19, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ | January 26, 2020 |
| 483 | An Interview with Adrian Tang | https://theamphour.com/483-an-interview-with-adrian-tang/ | |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 532 | Recalling Recalls | https://theamphour.com/532-recalling-recalls/ | February 28, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 588 | Siloed Engineering with Leigh Brady | https://theamphour.com/588-siloed-engineering-with-leigh-brady/ | May 8, 2022 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 623 | Artisanal Crystals | https://theamphour.com/623-artisanal-crystals/ | March 12, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
| 658 | Uncle Al's Eating Garbage Again | https://theamphour.com/658-uncle-als-eating-garbage-again/ | February 12, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
