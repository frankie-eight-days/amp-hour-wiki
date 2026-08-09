---
title: Pwm
concept: pwm
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**Pulse-width modulation** (**PWM**) is a technique for encoding an analog quantity as the duty cycle of a square wave: the output switches between a fixed voltage and zero, and the proportion of each period spent high carries the information. Three parameters must be specified independently — the switching voltage, the frequency, and the duty cycle — and conflating them produces circuits that are correct in only one of the three.[329] The technique spans switching frequencies from one cycle per sixty seconds up to hundreds of kilohertz, and its two largest application families sit an order of magnitude apart: motor control typically runs in the 10–30 kHz range while digital power supplies run at 100 kHz and above.[202][212] Because a PWM output needs only a single digital pin and a timer, it substitutes for dedicated hardware across an unusual range of functions, from digital-to-analog conversion and programmable power supplies to LED dimming, audio amplification, and signalling.[281][44][285][612]

## Characteristics

A PWM waveform is fully described by its switching voltage, its frequency, and its duty cycle, and these are independent choices.[329] The waveform is not equivalent to the DC voltage its RMS value suggests: a load may respond to the peaks of the switching waveform in ways it would not respond to the same average applied as a steady voltage, so a signal with an RMS value of 0.8 volts can drive behaviour that 0.8 volts DC cannot.[329]

Available frequency ranges depend on the platform. On high-level platforms a pin can be configured as a modulated output in a single line of code, with the slowest available period reaching one cycle per sixty seconds — a range covering indicator blinking as readily as motor drive.[202] At the other extreme, dropping below the convenient PWM abstraction trades a specified period for counter frequencies, count totals, and bookkeeping that the developer then owns; that trade is justified when the higher-level approach can be articulated as the limiting factor, not before.[711]

## Analog voltage generation

### DAC substitution

A PWM output through a resistor–capacitor filter substitutes for a digital-to-analog converter on parts that do not have one: varying the duty cycle from zero to one hundred percent and low-pass filtering the result recovers a proportional analog voltage.[281] The filtered output is a voltage reference rather than a drive; an op-amp after the filter both scales it — output nought to 2.5 volts and multiply by four, for example — and supplies the current the processor pin cannot.[281]

Some loads need no filter at all. An analog panel meter driven directly with PWM settles at an intermediate position through the movement's own inertia, which is why meter-face clocks are electrically trivial and require no converter.[725]

### Programmable regulators and control loops

Buffering a PWM output into the set pin of an adjustable regulator turns a fixed supply into a digitally programmable one, giving a microcontroller a controllable voltage or current source out of a part that was never advertised as programmable.[44]

Closing a power-supply loop in software rather than around an analog control IC changes the cost of being wrong: a miscalculated filter value becomes a recompile and reflash in five minutes instead of recalculating a resistor–capacitor network, desoldering parts, and possibly reordering components.[212] Deterministic sampling in such loops comes from linking the peripherals in silicon: PWM compare events both drive the output pin and trigger the analog-to-digital conversion, so the feedback point is always sampled at the same instant within the switching cycle rather than whenever software gets round to it.[212]

For a high-current supply that must limit on voltage and current simultaneously, two PID regulators can be run in parallel — one on each quantity — with whichever demands the narrower pulse winning; this keeps the supply stable when the load resistance changes underneath it, as happens when parts enter and leave a plating bath.[522] Because the control loop responds on the next pulse, the entire sense, calculate, and regulate sequence has to fit inside one switching period — on the order of twenty-odd microseconds at a switching frequency of 47 kHz.[522]

## Rail generation from a pin

A PWM pin plus a couple of diodes makes a charge-pump voltage doubler good enough to run an LCD bias rail, removing a dedicated doubler part and its cost from the bill of materials.[9] The trick has two hidden costs: efficiency is poor compared with a purpose-built converter, and the processor can no longer enter its low-power modes because it has to keep switching.[175]

## Motor control

Motor-control PWM typically runs in the 10–30 kHz range.[212] Bidirectional drive from a signed command is handled by taking the absolute value for the duty cycle and using the sign to select which of two pins the modulation comes out of — a two-line idea sufficient for real robot drive.[416]

High-performance motor control imposes hard architectural constraints. Centre-aligned PWM with the converter sampling motor current mid-pulse for field-oriented control at twenty kilohertz leaves no room for an operating system or a network stack to steal the processor; that class of loop rules out the architecture rather than merely straining it.[515]

In bridge topologies, dead time between complementary switch pulses is the difference between a working bridge and a destroyed one: it should be configured in the timer block and then verified on an oscilloscope at maximum duty cycle rather than trusted from configuration alone.[522] Measuring switch timing on a high-voltage bridge requires high-voltage probes plus either isolated probes or an isolation transformer on the instrument, because the reference point on the switching node is not ground.[522]

## LED dimming

### Efficiency

An LED has one current at which it converts electricity into light most efficiently, set by die size and device physics; above it efficiency falls away as droop, and efficiency also collapses at very low currents.[465] The obvious way to build a long-life dim indicator — a large series resistor from a battery — wastes most of the energy because it parks the LED far below its efficient operating current; pulsing at the efficient current and letting the eye average is the efficient equivalent.[465] In Ted Yapo's low-power indicator work, a very low duty-cycle driver was built from an eight-pin microcontroller asleep most of the time: its PWM peripheral fires a one-shot, the short current pulse energises an inductor, and the LED sits across the inductor running off the flyback kick — the same energy a catch diode would otherwise absorb — with brightness set by how long the inductor is energised.[465]

A related sizing practice holds that an indicator LED's series resistor should err on the bright side, with brightness dimmed back by PWM in firmware, because the modulation is free to change later while the resistor value is not.[724]

### Multiplexed and addressable arrays

Colour mixing and brightness control are separate mechanisms stacked on one another: without PWM an RGB module gives only the fixed mixtures its three channels produce, and graded intensity means running multiplexing and modulation simultaneously.[16] Multiplexed brightness need not cost continuous processor time: precalculate each LED's on-time, fire them all at the start of the frame, and let each turn off at its own moment; with 0201 parts the whole frame's duty cycles fit inside a few microseconds.[697] Frame timing can come from the watchdog timer at its maximum prescaler, which wakes the processor every 16 milliseconds — 60 times a second, exactly a video frame rate — so the processor sleeps between frames and contributes essentially nothing to the power budget.[697]

Smart LEDs impose their own constraints. Eight bits per colour leaves no headroom for global dimming, since dimming the whole array means giving up the low end of every channel's range at once.[412] The two-wire smart LED is easier to drive over SPI and adds several bits of global control, but using that control slows its PWM, and the part is not constant-current — intensity falls as the supply sags from 4.5 to 4 volts, which shows up immediately across a large installation.[412]

### Simulated LEDs

A physical LED has effectively unlimited refresh rate while a display refreshes at 60 to 200 hertz, so mapping a PWM-driven LED straight to a pixel reproduces the switching as flicker rather than as brightness.[599] Rendering a simulated LED correctly means integrating rather than sampling: take a moving average of on-time over each display frame, then apply gamma before setting the drawn opacity, so thirty percent duty appears at roughly seventy percent opacity — the same perceptual correction the eye applies to real hardware.[599]

### Lighting distribution

On low-voltage DC lighting distribution, dimming becomes a modulation problem rather than a mains-waveform problem; traditional phase-angle dimmers are electrically nasty and are what makes modern electronic lamps flicker and misbehave on legacy dimmer circuits.[539]

## Audio amplification

A class D amplifier is pulse-width modulation applied to audio: the input is compared against a sawtooth to produce a modulated square wave, the output stage is switched with it, and the load and filter recover the waveform — which is why these amplifiers are efficient rather than linear.[285] The output stage only ever presents the supply rail or zero volts, and the analog waveform at the speaker exists only as the average of that switching, so the modulation scheme, not the output devices, sets the achievable fidelity.[338]

## Signalling

Electric-vehicle charging negotiates current over a PWM signal: the vehicle sets its charge rate from the duty cycle the supply equipment presents, and the resulting control loop settles over a couple of seconds, which matters when the setpoint is being driven by fluctuating surplus solar generation.[612]

Driving a probe tip with PWM turns a logic probe into a node-impedance test: a point held high through a wire swallows the modulation, while a floating node follows it, distinguishing two states a passive probe reads identically.[689] A passive bug can carry no transmitter at all: a square wave is modulated onto a passive element, the device is illuminated with an external radar, and the information is read off the modulated return.[182]

## Implementation

### Hardware versus software generation

A part without a hardware PWM peripheral has to bit-bang the waveform, and the resulting LED flicker is plainly visible against a hardware-driven channel side by side; on Keith Burzinski's home-automation lighting work this was reason enough to lay out a custom controller rather than accept an off-the-shelf module built on the cheaper part.[657] Channel count, not processing power, is what typically exhausts a small microcontroller: needing eight modulated outputs for RGB indicators exceeded the hardware channels available and forced the modulation into software.[330] Bit-banging sixteen modulated channels on a mid-range microcontroller costs roughly fifty percent interrupt loading — acceptable when the part has no other job, which is a legitimate design position rather than a failure to specify properly.[524]

### Offloading and peripheral extension

Once microcontrollers cost a few cents, dedicating a whole part to generating one modulated output is cheaper than contorting the main processor's peripheral allocation to produce it.[412] Programmable real-time units fill in the peripherals a system-on-chip ran out of: on the BeagleBone Blue, firmware for the PRUs provides additional outputs that behave like hardware PWM, a fourth quadrature encoder where the silicon has three, and software UARTs where an earlier design had too few — the same trick that let the Lego Mindstorms EV3 talk to all its sensors.[378] Programmable IO blocks are tiny deterministic processors good only at high-speed bit banging: the timing-critical part of a software peripheral is pushed onto them, and the host talks to them through DMA and FIFOs exactly as if they were a fixed peripheral, which buys interfaces nobody would commit to silicon — such as driving WS2812 LEDs with their pulse-width-coded serial protocol at zero processor overhead.[687]

A part list that shows no PWM peripheral is not the end of the question: an advanced timer can usually be configured to produce it, so the timer complement rather than the feature bullet is what determines whether a cheap part can do the job.[610] Microcontroller line proliferation traces directly to lost designs over exactly this kind of gap — one PWM channel short, or the right peripheral set on the wrong pin count — and the obvious remedy of one part carrying everything fails too, because loading a die with unused peripherals loses the design on cost instead.[632]

## Failure modes

A PWM waveform can produce effects its average value does not predict: loads respond to switching peaks, and a device may act on a waveform whose RMS is 0.8 volts while ignoring 0.8 volts DC.[329]

Switching frequencies in the audible range announce themselves mechanically. A switching supply operated outside its intended load range drops into very low duty-cycle behaviour and can start whining audibly, with a loosely wound inductor's ferrite the usual mechanical source and ceramic capacitor microphonics a further one.[127] Ceramic capacitors sing audibly when the current through them is pulse-width modulated, which is why LED dimming circuits buzz; the low-ESR electrolytics that avoid it cost several dollars each rather than pennies.[224]

Generating a supply rail from a microcontroller pin forfeits efficiency relative to a purpose-built converter and blocks the processor's low-power modes, since it must keep switching.[175]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 9 | From Boston In Boxers? | https://theamphour.com/the-amp-hour-9-from-boston-in-boxers/ | |
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ | |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 182 | Manufacturing By Wire And Skipping Testing - Calefacient Cuculine Cash | https://theamphour.com/182-manufacturing-by-wire-and-skipping-testing-calefacient-cuculine-cash/ | January 27, 2014 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 281 | Crossovers and Call-ins | https://theamphour.com/281-crossovers-and-call-ins/ | January 6, 2016 |
| 285 | Something's Serially Wrong Here | https://theamphour.com/285-somethings-serially-wrong-here/ | February 3, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ | |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 416 | An Interview with James Bruton | https://theamphour.com/416-an-interview-with-james-bruton/ | November 18, 2018 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 539 | The King of Trash with Big Clive | https://theamphour.com/the-amp-hour-539-the-king-of-trash-with-big-clive/ | April 26, 2021 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ | November 20, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 632 | Steve Sanghi - Microchip CEO for 31 Years! | https://theamphour.com/632-steve-sanghi-microchip-ceo-for-31-years/ | May 15, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
| 697 | LEDs Everywhere with Tim from Mitxela | https://theamphour.com/697-leds-everywhere-with-tim-from-mitxela/ | July 8, 2025 |
| 711 | Medical Electronics Education with Mark Palmeri | https://theamphour.com/711-medical-electronics-education-with-mark-palmeri/ | December 21, 2025 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
