---
title: Sampling Rate
concept: sampling-rate
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Sampling rate is the frequency at which a continuous signal is measured and converted into discrete values, or at which discrete values are converted back into a continuous one. It is the parameter that determines whether distinct input frequencies remain distinguishable after conversion, since aliasing is the condition in which different frequencies appear identical once sampled.[185] The Nyquist criterion sets a floor of two times the highest frequency of interest, while the common instrument rule of thumb is roughly ten times the bandwidth in order to see waveform detail rather than merely avoid aliasing.[570] Sampling rate trades against resolution, power, data volume and cost throughout a signal chain, so the achievable rate is often set by the host interface, the acquisition memory or the converter's power budget rather than by the signal itself.[214][237][49]

## Aliasing

Aliasing is determined by the relationship between the frequency of interest and the sampling rate.[185] It can be demonstrated in the time domain by sampling three sine waves of different frequencies at one common rate: one cycle in ten samples, eleven cycles in the same ten slots, and twenty-one cycles in the same ten slots all produce identical sample values.[185] In the frequency domain, sliding the analog input frequency upward relative to a fixed sampling rate makes the alias images move downward, in the opposite direction.[185] Understanding data converters requires moving fluently between the two representations, because some converter behaviours are only visible in one of them.[185]

Presentation can obscure what a sample set contains. Sampled time-domain data is properly plotted as discrete points rather than as connected line segments, because connecting the dots invites the viewer to infer waveform detail that the samples do not contain.[185] Very cheap pocket oscilloscopes expose beginners to aliasing artefacts before they have the experience to recognise them, so a sub-par instrument makes early debugging harder rather than easier.[606]

Anti-aliasing filtering is tied to a specific rate. Reference designs supply only the minimum support circuitry needed for one assumed operating point, so an ADC front end copied unchanged will carry the wrong anti-aliasing filter as soon as the sample rate is altered.[301]

A related degenerate case arises in synthesis rather than acquisition: when a synthesised tone frequency falls at an exact order of the sampling frequency, the same phase point is sampled every period and the output collapses to a constant, transmitting nothing.[667] Conversely, choosing the sampling frequency for a one-bit synthesised carrier is an art of maximising the number of transitions in the output pattern, because the transmitted energy comes from the switching between on and off rather than from the sample values themselves.[667]

## Sample rate and bandwidth

Sample rate and rated bandwidth are distinct specifications, and the bandwidth figure is what determines what an instrument can actually resolve. A low-cost capture device specified at 12 megasamples per second across eight channels at 10 bits yields roughly 600 kHz of usable analog bandwidth.[193] On the output side, a video DAC clocked at 30 MHz yields a usable output analog bandwidth on the order of 5 MHz, since reconstruction filtering and sin(x)/x roll-off consume most of the nominal Nyquist span.[278]

Mid-range instruments conventionally run about five times their rated bandwidth, as in a handheld oscilloscope specified at 100 MHz analog bandwidth with 500 megasamples per second.[285] An instrument rated 100 megasamples per second but only 30 MHz of bandwidth runs at roughly three times oversampling where a factor of ten is the usual rule of thumb; such a ratio still avoids reporting an incorrect frequency but gives poor waveform fidelity.[339] Lower ratios are mathematically defensible when interpolation is applied: with sin(x)/x interpolation a sample rate of only about 2.4 times the bandwidth is sufficient to reconstruct the input waveform exactly, and for an oscilloscope with a Gaussian frequency response about 2.3 times the rated bandwidth guarantees no aliasing, so a 100 MHz instrument needs roughly 230 megasamples per second.[339][570] Some high-speed oscilloscopes from major vendors nonetheless ship with sample rates below twice their rated bandwidth, so the ratio is checked directly rather than assumed from the headline bandwidth figure.[570]

Channel count affects the available rate. Dedicating one acquisition ASIC per channel preserves 6.25 gigasamples per second on every channel simultaneously, whereas many instruments halve or quarter the sample rate as additional channels are switched on, and per-channel converters cannot be ganged to double the rate on one channel.[347] Bandwidth and sample rate are also frequently gated in firmware rather than hardware, and unlocking them can push a unit's sample rate above the maximum specified for any model in its product family, though the resulting acquisition is not necessarily calibrated.[339]

At the top of the range, instruments running at 40 gigasamples per second per channel depend on sampling clocks that are both very high frequency and very low jitter, pushing the oscillator design into exotic materials and physics.[104] The highest real-time bandwidth oscilloscope available in the mid-2010s was a 100 GHz instrument sampling at 240 gigasamples per second with 8-bit resolution, from the Teledyne LeCroy line.[252] The Keysight UXR series reaches a true 110 GHz of real-time bandwidth on all channels at roughly 256 gigasamples per second, using an indium phosphide front end rather than silicon.[404] The LeCroy HDO8000A series, released in 2017, offered eight 12-bit channels at 10 gigasamples per second plus an external trigger and a separate 16-channel logic analyzer, driving an external ultra-HD monitor so that all channels could be displayed at once.[347]

## Rate against resolution

Resolution and sample rate trade against each other inside a single acquisition system: a 12-bit oscilloscope front end may sustain full resolution only up to about 3 gigasamples per second while reaching higher rates at reduced bit depth.[347] High converter resolution is straightforward to obtain if the rate is allowed to drop, since a 24-bit ADC can be placed in an oscilloscope provided the acquisition is slowed down, so the engineering difficulty lies in holding resolution at speed.[677] USB oscilloscopes have long offered 12-bit and even 16-bit converters because bit depth is cheap at modest speeds; the scarce quantity is bandwidth, meaning resolution sustained at a high sample rate.[677]

The same trade appears within one converter's own specifications. Effective number of bits falls as sample rate rises: one measurement chain delivers about 18 effective bits at 8 kSa/s but recovers to over 19 bits at around 100 samples per second.[218] Converter precision degrades generally as conversion rate increases, which is why precision and high-speed converters are developed as distinct product lines rather than as points on one continuum.[348] A precision analog-to-digital converter is accordingly defined by its accuracy at DC rather than by its speed, and headline gigasample-per-second parts sit at the opposite end of the design space and may not measure a static volt accurately.[65] Successive-approximation converters built for precision applications typically top out around five megasamples per second, with faster conversion handled by separate high-speed product families.[348]

Averaging converts surplus rate into resolution. Boxcar averaging is a rolling-average filter applied to samples immediately after the ADC stage, before display processing, which raises the effective number of bits, so that an oscilloscope with only an 8-bit converter can present 9, 10, 11 or 12 bits of resolution.[455] The cost is rate: the instrument's effective sample rate drops in proportion to the number of samples combined per displayed point.[455] Oscilloscope high-resolution mode implements the same idea, averaging groups of adjacent samples on the fly, typically four or ten, and is appropriate only when the signal under test does not need the instrument's full sample rate.[117]

Sigma-delta conversion inverts the relationship deliberately. Such a converter samples in a very small window and continuously compares the input against its running estimate, using a one-bit DAC fed back through an integrator and summing junction; the resulting average is highly accurate, which is why sigma-delta sampling frequencies sit orders of magnitude above the signal band.[474]

## Data volume, interfaces and memory

The achievable rate in a memoryless streaming front end is set by the host interface rather than by the converters, so the maximum throughput of high-speed USB becomes the governing constraint for the whole signal chain.[214] Pairs of 8-bit quadrature samples delivered 20 million times per second essentially saturate high-speed USB, fixing the instantaneous bandwidth of such a receiver at about 20 MHz.[214] A 20 megasample-per-second design point also sits at a favourable cost break, because analog and digital signal-chain components rated meaningfully faster become substantially more expensive.[214]

Continuous streaming and buffered capture are the two architectures. A front end that streams 20 megasamples per second continuously over USB makes a poor oscilloscope but a serviceable data-acquisition instrument, because the value of continuous streaming is uninterrupted record length rather than peak timing resolution.[198] The alternative is to sample far faster than the host link can carry, apply triggering and local storage, and then read the captured record out slowly over the interface.[198]

Storage bounds record length in both architectures. Streaming analog capture at 50 megasamples per second consumes host RAM so quickly that even a machine with 8 to 16 GB is limited to roughly 20 to 30 seconds of continuous recording, whereas compressed digital channels can be recorded for days.[237] A high headline sample rate says nothing about usable record length: the Tektronix TBS1000 series pairs a one gigasample-per-second acquisition rate with only about 20 kilopoints of sample memory.[646] Between the roughly $400 and $800 tiers of four-channel oscilloscopes the incremental purchase is a larger touchscreen, higher sample rates and more acquisition memory, though for general bench use a $400 four-channel instrument remains adequate indefinitely.[606]

Triggering exists because capturing every event at the rate needed to resolve millisecond-scale phenomena over days produces unmanageable data volumes; the trigger provides the rule for discarding irrelevant samples once the acquisition buffer fills.[510] Oscilloscopes and logic analyzers default to 50 percent pre-trigger and 50 percent post-trigger capture so that the record shows the conditions leading up to the trigger event as well as its aftermath.[510]

Downstream processing carries the same constraint. In GNU Radio the core signal-processing blocks are written in C++ with only a Python interface layer on top, because high-end and commercial systems run at sample rates that demand direct access to the machine architecture for optimisation.[381] A low-cost FPGA such as the Tang Nano 9K is only marginally fast enough to accept 50 to 100 megasamples per second from an external ADC and simultaneously drive a parallel TFT display, making sample-rate throughput the binding constraint in a hobby oscilloscope build.[673] An open-source oscilloscope front end built around the HMCAD1511 four-channel ADC achieves about one gigasample per second with roughly 350 MHz of analog bandwidth, with proper shielding cans in the front end.[627]

## Power and part selection

Converter power efficiency is usefully normalised as energy per sample rather than as bulk supply current: a part drawing about 100 microwatts at 8 kSa/s works out to roughly 0.1 picojoule per sample, or about 40 microamps from a 2.5 V rail.[49] Around 2011 the ultra-low-power 16-bit converter segment held only about half a dozen usable parts, where ultra-low-power meant roughly 100 microwatts at an 8 kHz sample rate.[49] Low-power 16-bit converters are plentiful at very low speeds, with many topping out near 300 samples per second, so pushing the same power budget to kilohertz rates sharply narrows the field.[49] The Analog Devices AD7691 draws about 108 microwatts at an 8 kHz sample rate and delivers 18 bits rather than the 16 bits its class implies, making it a benchmark low-power converter for kilohertz-rate acquisition.[191]

Measurement requirements are also right-sized against their cost, since instruments capable of picoamp resolution are priced for semiconductor work rather than board-level electronics design.[640]

## Applications

### Audio

In an I2S audio system the master clock must be an integer multiple of the sampling frequency and a much higher one; a 50 MHz sampling bandwidth oversampled 64 times would demand a 3.2 GHz clock, comparable to a high-end processor core clock and prohibitive on power grounds.[474] At audio sample rates of 44.1 or 48 kHz, one sample period leaves room for on the order of a thousand processing operations on a fast DSP, so feed-forward loudspeaker correction is straightforward, while closing a loop from the loudspeaker output back to the amplifier input demands latency low enough to require custom silicon instead.[560]

Audio converter product definition often reduces to whether basic functions such as switching between 44.1 kHz and 48 kHz sample rates are exposed on hardware pins or over a serial bus, and many hardware customers insist on a pin they can pull low even when I2C or SPI control would unlock more features.[270] Marketing pushes 24-bit converters running at nearly 200 kHz when far lower specifications are adequate, so the engineering task is to trace the requirement back to what is actually audible, since the difference between a $30 and a $2 DAC is often inaudible in the finished product.[573] General-purpose microcontrollers increasingly carry digital audio interfaces: the ESP32 provides two channels of I2S output capable of 24-bit data at sample rates beyond hi-fi requirements, enough for one device to drive several audio channels.[338]

In filter design work the rate is an explicit parameter of the analysis. MATLAB's FVTool plots a digital filter's response from DC to Nyquist and requires the sampling rate to be entered, since the frequency axis of any discrete-time filter is meaningful only relative to that rate.[513]

### Logic analysis

A logic analyzer in timing analysis mode behaves like an oscilloscope with a comparator front end, sampling asynchronously at a fixed rate such as 50 or 100 megasamples per second and rendering the result as blocky square transitions.[436] Sampling a 50 MHz design with a 200 megasample-per-second analyzer gives only four times oversampling, which is enough to capture the states but not enough time granularity to resolve setup and hold relationships between signals, so a much higher oversample rate is needed for timing debug.[436]

Because the analyzer's sampling clock and the design under test are not synchronised, the two drift relative to each other over minutes, so a circuit can appear to work and then suddenly show nonsense as edges drift out of the sampling window, an artefact easily mistaken for a real intermittent fault.[436] When a digital capture shows an anomaly, the first question is whether it is genuine circuit behaviour, noise, or an artefact of undersampling; correctly configured logic thresholds do not eliminate the risk, because real switching levels shift with temperature and part grade and a runt pulse that barely reaches the threshold can cost weeks of troubleshooting.[436]

### Current and power measurement

A current-measurement instrument sampling at only 4 kilosamples per second, with a range from one microamp to five amps, cannot capture the fast current slugs that dominate battery-powered radio designs, where a device sleeps most of the time and a LoRa transmit burst alone draws 20 milliamps or more.[432] At the other extreme, an instrument sampling two million times per second resolves firmware changes of a few milliseconds in a power waveform, letting a developer quantify the energy saved by shortening a routine.[527]

Requirements vary sharply with the measurement. Sleep-current measurement needs only hundreds of samples per second, or even one per second, and the practical architecture keeps a slow default rate and switches to a high-speed mode only when an event of interest occurs.[640] One instrument samples internally at 250 kilosamples per second but presents at most 50 kilosamples per second to the user, averaging five by five, because the extra rate is not needed for most measurements.[640] The circuit under test can also limit what any rate would reveal: a bulk capacitor sitting where a battery connects to a board forms a low-pass filter in the current path, so the current waveform reaching the instrument is already smoothed regardless of how fast it samples.[640]

A digital multimeter samples at a fixed interval and shows only the converted value, so rapidly changing circuit values fall between samples and are never displayed; bar-graph secondary displays exist to restore that dynamic feel, with a 105-step graph giving one percent resolution at about ten updates per second.[561]

Metering hardware shows the same divide. Conventional smart-meter chips built around fixed-function DSP blocks are limited to roughly three to six kilohertz of measurement bandwidth, whereas a software-defined metering front end can sample up to a megasample per second and resolve far more harmonic content.[371]

### Radar

In chirp radar the sample rate purchases unambiguous range extent: a coffee-can radar limited to a roughly 15 kHz audio input reaches only about 100 to 150 metres, whereas raising the sample rate extends detection of car-sized 10 dBsm targets out to about a kilometre.[214]

## Development practice

A recommended development sequence for a high-speed output stage is to prove the system with an 8-bit DAC first, confirming how fast the whole chain runs, and only then move to a 12-bit or 16-bit part.[278]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ |  |
| 65 | Silego, ADCs & Seismic Detection - Dave's Dingo Dystocia | https://theamphour.com/the-amp-hour-65-daves-dingo-dystocia/ |  |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ | August 23, 2021 |
| 185 | An Interview with Hank Zumbahlen - Zoppa Zumbahlen Zateticism | https://theamphour.com/185-an-interview-with-hank-zumbahlen-zoppa-zumbahlen-zateticism/ | February 17, 2014 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 193 | We're Sorry! But Apple Ain't! - Remorseless RAM Racketeering | https://theamphour.com/193-were-sorry-but-apple-aint-remorseless-ram-racketeering/ | April 7, 2014 |
| 198 | Mike Ossmann Returns! - Planetic Portalab Packaging | https://theamphour.com/198-mike-ossmann-returns-planetic-portalab-packaging/ | May 12, 2014 |
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 278 | Our Second Callin Show(ish) | https://theamphour.com/278-our-second-callin-showish/ | December 16, 2015 |
| 285 | Something's Serially Wrong Here | https://theamphour.com/285-somethings-serially-wrong-here/ | February 3, 2016 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ | March 12, 2017 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 371 | An Interview With Joe Bamberg | https://theamphour.com/371-an-interview-with-joe-bamberg/ | December 10, 2017 |
| 381 | An Interview with Derek Kozel | https://theamphour.com/381-interview-with-derek-kozel/ | February 25, 2018 |
| 404 | Proof Of Blink | https://theamphour.com/404-proof-of-blink/ | August 26, 2018 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 455 | Bill and Dave's Excellent Equipment | https://theamphour.com/455-bill-and-daves-excellent-equipment/ | August 19, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 513 | Audio DSP with Shannon Parks | https://theamphour.com/513-audio-dsp-with-shannon-parks/ | October 18, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 560 | High End Audio with Remco Stoutjesdijk | https://theamphour.com/the-amp-hour-560-high-end-audio-with-remco-stoutjesdijk/ | October 3, 2021 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23, 2022 |
| 627 | Works on my machine | https://theamphour.com/627-works-on-my-machine/ | April 9, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 673 | Lifelong Learning with Bitluni | https://theamphour.com/673-lifelong-learning-with-bitluni/ | July 15, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
