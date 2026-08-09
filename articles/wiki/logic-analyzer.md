---
title: Logic Analyzer
concept: logic-analyzer
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A logic analyzer is an electronic test instrument that captures multiple digital signals simultaneously and displays them as timed waveforms or, with protocol decoders, as the data words carried on a bus.[436][165] It operates in two modes: timing analysis, in which the instrument samples from its own free-running clock, and state analysis, in which it samples in step with a clock taken from the system under test.[436][62] The instrument answers a narrow question reliably — which word was on the bus — and only when the signal is already clean, which places it alongside the oscilloscope rather than in place of it.[165][396]

## Operating modes

### Timing analysis

Timing analysis, the mode the instrument's name is generally taken to mean, works like an oscilloscope: it samples the input channels at a fixed rate from its own free-running clock and draws the result as square edges on a screen.[436] Resolving timing relationships demands a high oversample rate; sampling four times faster than the signal is not enough to make setup-and-hold relationships or metastability visible, and the differences between two signals only become apparent at much higher rates.[436] Because the instrument's clock and the device's clock are both free-running, they drift against each other, producing a characteristic false symptom in which the captured design looks correct for a minute and then appears to misbehave as the sampling instant slides relative to the product's clock.[436]

### State analysis

State analysis takes its clock from the system under test, so each sample corresponds to a clock edge in the circuit rather than to an arbitrary instant.[62] Because the instrument samples in step with the product's own clock, an input that changes on the same edge as the clock is visible as such, which is what allows setup and hold times to be examined directly rather than as artefacts of when the instrument happened to sample.[436] The specified maximum rate in state mode is lower than in timing mode, because the capability is spent on the synchronisation rather than on raw throughput.[62][436]

### Signal-integrity limits

The instrument reports which word was on the bus reliably only when the signal is already clean; everything happening between the logic levels is outside what it can show.[165] Correctly set logic thresholds are no guarantee of visibility: the real switching threshold moves with temperature and part grade, so a runt pulse that only just reaches the nominal level can be invisible to the instrument while being real in the circuit — a difference capable of costing weeks of debugging.[436]

## Triggering and storage

Triggering exists because storage does not scale to the problem: capturing an event that occurs somewhere within days at a resolution of a thousand samples per second produces more data than can be kept, so the buffer must discard what has been determined to be irrelevant.[510] Logic analyzers, like oscilloscopes, default to placing the trigger in the middle of the buffer — half pre-trigger and half post-trigger — because what happened immediately before the event is usually as informative as what happened after it.[510]

Configurable triggering is conventionally built as a trigger unit inside the instrument's FPGA, with the user's conditions loaded into it. In the context of open FPGA toolchains, this amounts to building "a reconfigurable architecture in a reconfigurable architecture" — an approach that wastes resources and is slower and less flexible than the underlying fabric.[374] The alternative she describes is to translate the trigger condition itself into a logic circuit and synthesise it when the user presses acquire; the vendor toolchains cannot support this because they are built for large designs and take minutes merely to start.[374]

## Architectures

### Streaming instruments

The streaming architecture puts almost nothing in the instrument. On the Saleae products, the hardware samples the pins and immediately sends the data over USB, while the desktop software holds the capture, provides the interface and performs the analysis — which, the Garrison brothers state, is where the value of the product actually sits.[237] In that architecture the sample buffer is host memory rather than instrument memory, and the trigger is implemented by searching the incoming stream in software, an approach that works well until the data rate approaches the limit of the link.[237] Software triggering does not match how experienced users of these instruments think: being told to capture everything and search it afterwards is not a substitute for triggering on the protocol event itself, such as a particular I²C packet.[237]

### Instrument-side memory

Instrument-side memory is the alternative architecture, and it is a cost decision. Static RAM is simple to interface but expensive enough to limit the buffer to tens or hundreds of megabytes, whereas the DDR memory that would remove the constraint needs a controller — a function that modern FPGAs now provide as hard blocks, taking most of that work away.[237]

### Software as the product

The underlying problem looks trivial from outside — record the state of eight pins and draw it on a screen — and the software is the reason such a product is worth anything at all.[237] In a crowded category, the price of the instrument buys the software development rather than the FPGA and converters inside it, and that software investment is what supports a vendor moving up-market over time.[554]

### Cloning

Hardware-level cloning is straightforward when the design is built around a standard USB interface chip: copies use the same part with the same EEPROM contents, so that they identify themselves as the original to the host software.[237] Saleae responded by detecting the copies from the host side and disabling them, writing nonsense into the EEPROM; it later probed how engaged the copiers were by changing the register map between software and FPGA in a beta release, and the copies were corrected to match within about forty-eight hours, establishing that the cloning operation was actively maintained rather than distributors reselling old work.[237] The distinction drawn around such cases is between modifying a product one has bought, which is legitimate, and reproducing it for resale under the original brand, which is not.[74]

## History

The category was transformed by the host connection: where the instrument once meant a large dedicated box, small devices attached to a computer now do a serviceable job.[144] The earlier generation was correspondingly heavyweight — an early instrument was a large unit, from vendors such as Hewlett-Packard, that effectively arrived with its own support engineer.[373]

Cheap programmable logic is what first put the instrument within reach of a magazine project: in 1995 two designers independently picked the same new low-cost programmable logic device and set out to build an analyser with it.[504] Their designs converged almost exactly, because the part choice constrained everything downstream: the pin count fixed the channels per device, which made a separate control device and trigger device the obvious division, and the trigger implementations ended up essentially identical.[504]

## Use alongside the oscilloscope

The governing rule is to look at the analogue waveform first and reach for the digital view second, rather than starting from the decoded picture.[396] The complementary error is stopping at the waveform: a signal can look exactly like the signal it is supposed to be while carrying the wrong content, and only decoding it reveals that a device is repeatedly retrying the same address without ever being acknowledged.[396]

On a misbehaving two-wire bus, the order that works is to scope the lines first for pull-up value and edge quality, then confirm the device is being addressed and enabled, and only then question the protocol and whether the library driving it has ever been proven.[274] Connecting the instrument can itself change the behaviour of a marginal bus: in one case a device that failed to respond with the analyser attached answered about eighty percent of the time once it was disconnected.[274] Setting up a protocol decoder is a skill in its own right, and getting it wrong manufactures a fault that is not there — the wrong baud rate, parity or inversion produces garbage on the screen and sends the engineer looking for a defect in a design that is working.[391]

## Instrument selection

Before buying oscilloscope bandwidth to chase a fast microcontroller, the question worth asking is whether the analogue waveform is needed at all or whether a digital capture answers the question.[606] Logic capture cannot be retrofitted to an oscilloscope that lacks it, but it can be supplemented with a separate USB instrument, which is the trade against paying more for a mixed-signal model at purchase.[606] A constrained instrument covers most of the people who will ever use one — roughly eighty percent — and the expensive instrument is bought at the point where the need is real rather than in anticipation of it.[199]

For asynchronous timing problems the channel count is what matters: a two-channel oscilloscope is better than nothing but not adequate, while a sixteen-channel instrument makes the relationships visible. Eric Schlaepfer, whose work involves reverse-engineering and analysing classic hardware, names the Saleae Logic Pro 16 as his most frequently used tool for that purpose.[609] Channel count also separates a useful instrument from a cheap one: an eight-channel unit gives little more than a protocol capture would, because the value lies in the relative timing between many signals at once.[412] Sixteen-channel units cost several times what the eight-channel ones do, while remaining an order of magnitude cheaper than the high-end oscilloscope that would otherwise be needed.[412]

Simplicity also determines whether an instrument gets used at all: more capable equipment ends up sitting in the lab while a simple instrument stays on the desk, and measurements that are naturally scripted suit a computer-attached instrument, where the tactile control of an oscilloscope suits the bench.[527] For work on programmable logic and radio, Matt Ettus — founder of the USRP software-defined radio line — places the logic analyzer in a set of three instruments alongside the spectrum analyser and signal generator, with the oscilloscope useful mainly for power supplies.[101]

## Applications

### Embedded system integration

The productive habit during system integration is to instrument the processor permanently rather than for one measurement: bring out everything significant on spare pins and leave the analyser connected for the duration.[581] Left connected, the display becomes a status readout for the system — "the pulse of the system" — in which periodic accesses appear as regular activity, and toggling a spare pin at the entry and exit of an interrupt routine gives a high-resolution picture of when it actually runs.[581]

A debug probe answers a different question. Toggling a pin to observe behaviour is inference from outside; attaching a debugger stops the processor's clock and steps one instruction at a time while showing the contents of variables, which is how an off-by-one is found rather than guessed at.[356] Capture and stimulus are complementary in an automated setup: one instrument puts the embedded system into a given state or provides the stimulus, and the analyser records how it responds.[461] The instrument also serves as a profiler, with the cycle timing of hand-optimised signal-processing code measured by watching it run rather than by reasoning about it.[513]

A recurring beginner trap is connecting the instrument after the system has booted: an embedded target emits its traffic at start-up and then idles, so the screen stays empty until the reset button is pressed.[318]

### Protocol decoding and reverse engineering

In routine use the instrument is a protocol decoder more than a timing tool, covering the two-wire bus, the vehicle bus, the industrial serial standards and the synchronous serial bus from a single capture.[661] Undocumented protocols are recovered by capture: Samy Kamkar drove a proprietary addressable light string with no published interface from a microcontroller after recording and decoding its data stream with a borrowed instrument.[308] In his hardware-security teaching, Dmitry Nedospasov hands students a logic analyzer with a target board and no stated assignment, so the exercise is to find the signals, work out how to interface to them, and then meet a timing requirement a microcontroller could not; the legal position he states for such work is that producing a device which emits the same signal is emulation rather than copying, since no source code has been taken.[303]

Reverse engineering a vehicle bus starts by narrowing to one identifier and one bit position within the payload, helped by tools that infer which bits are least significant from how quickly they change.[634] Ken Tindell's work on CAN shows that a decoder with enough timing resolution can go further and identify which physical node sent a frame: impedance mismatches produce reflections that shift rise and fall times by an amount determined by position on the bus, so measuring bit duration precisely maps frames to the units transmitting them.[634]

A secure element's bus traffic is fully visible to an instrument, and that visibility is not itself a vulnerability: the private key is generated on the chip and never leaves it, so what can be observed is the challenge and response rather than the secret.[698]

### Failure analysis

In failure analysis of customer returns that test good at the factory, John Day's method is to bring in the engineers who wrote the code that talks to the failing part, write test code that exercises it the way the application does, and attach an instrument with a deep enough buffer to catch the event.[485]

### Simulation and verification

Recording real hardware once turns a slow manual test into a fast automated one. Uri Shaked, developer of the Wokwi simulator, captured forty test cases — each taking two to three minutes to run by hand — from hardware with the instrument and replayed them against the simulator, compressing a half-day feedback cycle to about five seconds.[599] The approach also exposes where the model and the world disagree: the simulator and the instrument agreed on the timing of the real part, and the discrepancy turned out to be physical devices tolerating timings outside their published specification, which meant the simulation had to be loosened rather than corrected.[599] A generic decoder is likewise enough to verify software against a device the simulator does not model: watching the expected sequence of register writes and read-backs on the simulated bus confirms the driver without a model of that specific sensor.[599] In the browser-based simulator itself, the instrument attaches to the simulated wires in the same way as to real ones, recording the protocol traffic passing between the simulated parts.[599]

The simulation equivalent of a capture is a value change dump loaded into a waveform viewer, which presents the same picture the instrument would; formal verification tools produce very short traces that run from a working state directly to the failing one.[467]

## FPGA-based and embedded implementations

A capture engine can be instantiated inside the device under test. On a large FPGA an internal logic analyzer is a reasonable way to see internal signals; on a small one it consumes a significant share of the resources, whereas simulation costs nothing and exposes every signal at every instant.[467]

The instrument can also be built from a general-purpose board's peripherals: one project implements a fourteen-channel, hundred-megasample-per-second capture on the real-time units of an application processor using software DMA, with open-source software performing the analysis.[378] A programmable I/O block does the same job on a microcontroller, sampling whatever pins are configured and streaming the data over USB into standard analysis software.[648]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 62 | Op amps, Microchips & Mergers - Narquois Nerd Nescience - Narquois Nerd Nescience | https://theamphour.com/the-amp-hour-62-narquois-nerd-nescience/ | |
| 74 | Younker Youtube Yarling | https://theamphour.com/the-amp-hour-74-younker-youtube-yarling/ | |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 144 | An Interview with Bob Davidson - Hoodied HP Hijinks | https://theamphour.com/the-amp-hour-144-hoodied-hp-hijinks/ | May 7, 2013 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 199 | The 2014 Maker Faire Show - Traveling Technology Trangam | https://theamphour.com/199-the-2014-maker-faire-show-traveling-technology-trangam/ | May 19, 2014 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 303 | An Interview with Dmitry Nedospasov | https://theamphour.com/303-an-interview-with-dmitry-nedospasov/ | June 14, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 396 | The Synergy Bus | https://theamphour.com/396-the-synergy-bus/ | June 10, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ | October 6, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 504 | This Is Just A Tribute | https://theamphour.com/504-this-is-just-a-tribute/ | August 9, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 513 | Audio DSP with Shannon Parks | https://theamphour.com/513-audio-dsp-with-shannon-parks/ | October 18, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 581 | Real Time Operating Systems with Brian Amos | https://theamphour.com/581-real-time-operating-systems-with-brian-amos/ | March 13, 2022 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23, 2022 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 634 | The CAN bus can! with Dr Ken Tindell | https://theamphour.com/634-the-can-bus-can-with-dr-ken-tindell/ | May 30, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
