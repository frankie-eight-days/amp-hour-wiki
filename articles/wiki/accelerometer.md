---
title: Accelerometer
concept: accelerometer
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

An accelerometer is a transducer that measures acceleration and converts it into an electrical signal; in modern practice the sensing element is a capacitive micro-electromechanical structure fabricated in a CMOS process whose capacitance changes by amounts measured in zeptofarads, with that change converted to a voltage.[185] For a stationary device the reading is dominated by gravity, so the simplest demonstration of the sensor is one that shows which way is down.[256] The technology was a genuine discontinuity rather than an incremental improvement: before micro-electromechanical parts existed there was no practical way to make such measurements at all.[185] Its significance lies in the breadth of systems it enables, from orientation sensing and gesture input to vibration analysis, balancing machines, and clinical instrumentation.[204][246][549][560]

## Physical principles

The capacitive MEMS sensing element produces signals so small that Gaussian noise in the electronics sets a floor on how accurately mechanical motion can be resolved.[185] The unfamiliar part of the device for most engineers is the conversion itself: voltages and amplifiers are well understood, whereas turning gravity and tilt into an electrical number is not, and the understanding comes from having done it.[185]

Because the output of a stationary accelerometer is almost entirely the downward pull of gravity, the device is fundamentally an orientation sensor when at rest.[256] A gyroscope answers a different question: it responds to motion and gesture rather than orientation, and shows nothing while the device is still.[256]

## Fundamental limitations

### Double integration

Recovering position from acceleration requires integrating the signal twice, and any jitter in the acceleration reading is magnified enormously by that double integration, which is why dead reckoning from an accelerometer alone does not work.[147] The direction of the calculation matters: differentiation is a mathematically noisy operation and integration is not, so integrating an accelerometer toward velocity and position behaves better than differentiating a position measurement would.[334]

In practice this limit is decisive. An attempt to track how far a boat had drifted by integrating acceleration ended with the position unknown.[334] The same limit bounds fine position tracking on a person: double integration can be made to work only if the subject stays completely still, so anything mounted on a moving head defeats it.[660]

### Inference rather than measurement

Consumer activity metrics derived from accelerometers are inferences rather than measurements: an interrupt indicates movement, the change between successive readings is interpreted as a step, and filtering does the rest—accurate enough to be useful, but not the direct measurement it appears to be.[644]

## Sensor fusion and integration

Combining a three-axis accelerometer and a three-axis gyroscope into one digital part replaced two separate breakout boards, and the feature that mattered was the processor inside the part fusing the raw readings into orientation on the chip.[155] On-chip fusion matters most where the host is small: doing the orientation mathematics in the sensor saves processing time and power on a low-power microcontroller that should be asleep as much as possible.[155]

Documentation of these fusion processors has been a recurring problem. One vendor documented access to the raw accelerometer and gyroscope readings but published nothing about the fusion processor that was the part's main selling point, leaving the register map with no description of it at all.[155] The way in was the vendor's own evaluation kit: its companion board shipped with firmware that configured the processor correctly, so capturing the bus traffic between the two with a logic analyzer recovered the initialisation sequence.[155] The same pattern recurred on a nine-axis part combining gyroscope, magnetometer and accelerometer, where the interface to the motion processor had to be reverse engineered because the register map was withheld.[153]

A gyroscope costs roughly ten times the power of an accelerometer, so leaving it out is worth real battery life if the application can manage without it.[525] That trade can be tested rather than assumed: removing the gyroscope data from a gesture-classification problem left the accuracy unchanged, which eliminated a dollar part, its power draw, and potentially a move from six axes to three.[525]

## Hardware design practice

Two features decide whether a part is usable in a low-power design: an interrupt output, so a free-fall or motion event wakes the processor instead of being polled for, and lines such as shutdown and reset brought out so the device can be controlled and recovered.[602] Assembling the sensing hardware is the easy part of an inertial measurement project—the parts are catalogue items—and the point of getting the basics working quickly is to free the effort for the algorithms.[187]

## Software interfaces

Firmware should be written against a generic sensor interface rather than the specific part fitted, so that the code has as few dependencies on the rest of the system as possible.[556] Under Linux the sensor is presented as files: acceleration in each axis appears as a virtual file that is read when a value is wanted, through a subsystem built for this class of device.[378] The driver bridges the two worlds by translating the vendor's register map into that abstraction, so that reading a named file returns the value from a documented register address.[378] Once the driver probes correctly, the hardware work is finished and the sensor is reachable from ordinary application code in any language, which is what the separation between kernel and user space buys.[515]

## Vibration measurement and test practice

Cable movement generates its own charge: insulation moving against the conductor produces a charge on the cable, and since a typical vibration accelerometer is itself a charge-output device, a test jig whose cabling flexes injects error directly into the measurement.[215] Calibrated equipment does not rescue a badly built test: a calibrated accelerometer, charge amplifier and shaker will still produce meaningless vibration results if the fixture is wrong, and the check that reveals it is the coherence measurement.[570] Coherence is not taught as part of a normal course, which is why the failure is common: engineers reach vibration testing without the concept and read the resulting garbage as a fault in the apparatus.[570]

The physical method for board-level vibration work is to glue a miniature accelerometer directly to the assembly, usually in several places and orientations, and to mount the board in different configurations across successive shakes.[631] The instrument for this work is a dynamic signal analyser rather than a network analyser: designed for audio-band measurement, it takes accelerometer inputs and produces the vibration and seismic spectra.[25] Some quantities are settled empirically rather than derived: fitting accelerometers and observing what happens is the engineering answer where calculation would be the scientific one.[614]

A sensor can also be improvised from an unrelated part: on Julia Truchsess's work replacing condenser microphones that suffered crosstalk and feedback, an electret microphone potted in epoxy inside a machined housing screwed directly to the instrument became, in effect, a purpose-built accelerometer.[424]

## Applications

### Audio and automotive

Active noise cancellation in a car takes its reference from accelerometers mounted on the suspension, which pick up the vibration that will later become audible after travelling through the chassis into the cabin.[560] The cancellation depends on estimating the acoustic transfer function from the noise source to the listener's position, passing the measured noise through that estimate and inverting it, so the quality of the result follows directly from the quality of the estimate.[560] In a security application the sensor's job is to qualify an event rather than to measure motion—confirming that a vehicle is stationary before anything is triggered.[614]

### Head-mounted and wearable devices

Head-mounted displays need a fast sensor specifically because of latency: if the image does not follow a quick head movement, the mismatch makes the wearer motion sick.[164] A wearable camera used the sensor for a control gesture rather than for measurement: placing the device face down was detected as an orientation and used to switch it off.[301] The signal carries more identity than expected: machine learning applied to accelerometer data alone can identify which person is wearing the sensor from their walking pattern, without a camera being involved.[557]

### Control and interlock

A sensor fitted for one purpose often supplies a second: on Mike Harrison's work, the accelerometer detecting that a laser had been moved also sensed its angle, so tilting the unit downward switched the laser off—a safety interlock with no extra hardware.[135] Free-fall detection is a standard use of the interrupt output: on Brandon Harris's reference design, a device thrown into the air woke, connected to the network and returned to sleep before it was caught again.[202] The same reference design taped to a garage door and wired to a messaging service produced a notification whenever the door stayed open more than five minutes—a real problem solved in a couple of hours with parts already to hand.[202]

Balancing machines combine the sensor with the mechanics: a body sitting on rollers above a ball, driven by high-torque motors, balances using the accelerometer for its attitude reference.[246] Not every balancing product contains one, however: a self-balancing board that appears to sense lean turned out to use a switch, which is a simpler control problem than the two-wheeled vehicle it resembles.[305]

### Data recording and display

Orientation can be used as a data source rather than a control input: on Noah Feehan's project, sampling the three axes once a minute and mapping them linearly to colour produced a continuous record of what position a device—and by extension its owner—had been in through the day.[204] A levelling instrument can be built entirely from the sensor and indicators: an outer ring of twelve LEDs for coarse level and an inner ring of four around the sensor for fine, with all sixteen lit once the device is level.[727]

### Clinical and research instrumentation

Clinical problems often reduce to adding a few standard sensors to an instrument already in use: on Shrouk El-Attar's work, assessing how steady a surgeon's hands are meant adding galvanic skin response, an accelerometer and time recording to the existing probe.[549] Cheapness produces uses the part was never intended for: a researcher measuring balance for Parkinson's work used off-the-shelf consumer hardware rather than instrumentation.[249]

## History and cost structure

The origin of the technology was aviation, which is some distance from where the parts are now used.[249] Before MEMS parts, the measurement was bulky: an accelerometer meant an electromechanical assembly and a compass meant coils, with the mathematics left to the designer and no libraries to draw on.[221] Where inertial parts were unavailable, designers substituted a different physical principle entirely: on Bruce Simson's flight controller, infrared thermopiles on each wingtip and the nose inferred bank and pitch from the sky being a different temperature to the ground, which still worked at night with the temperature relationship reversed.[538]

The cost collapse is what changed the design space: measuring ten accelerometers at once became routine, and parts are cheap enough that using several is unremarkable.[246] The same balancing machine would have needed a ten-thousand-dollar sensor a decade earlier, which is why the applications rather than the technique are what is new.[246]

Production test can depend on the platform the sensor was designed for: on Colin Karpfinger's motion-sensing controller, which was intended to be played with a phone, the test application had to run on those devices, which meant supplying iPod Touches to everyone on the factory line.[226]

## Education

As a teaching device the sensor works better shared out than explained: in Charlie Larrabee's instruction, each student takes one sensor from a board, researches what it does and why it would be used, and presents that to the others rather than sitting through an exhaustive account of how it works.[572] Gesture interfaces built on these sensors are easy to propose and mostly do not survive contact with use: shaking or flicking a device to trigger an action is a neat concept that is rarely practical.[3]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 3 | HP, IEEE, and Human Interface | https://theamphour.com/3-hp-ieee-and-human-interface/ | |
| 25 | NASA, WOTW & Modular Design - The NASA Nostalgia | https://theamphour.com/the-amp-hour-25-the-nasa-nostagia/ | |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 147 | An interview with Jeri Ellsworth - Absorptive Augmented Actuality | https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/ | May 27, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 155 | An Interview with Jeff Rowberg - Mini Module Master | https://theamphour.com/the-amp-hour-155-mini-module-master/ | July 22, 2013 |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ | September 23, 2013 |
| 185 | An Interview with Hank Zumbahlen - Zoppa Zumbahlen Zateticism | https://theamphour.com/185-an-interview-with-hank-zumbahlen-zoppa-zumbahlen-zateticism/ | February 17, 2014 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 204 | An Interview with Noah Feehan - Biloquistic Blinking Blush | https://theamphour.com/204-an-interview-with-noah-feehan-biloquistic-blinking-blush/ | June 23, 2014 |
| 215 | Wrong Hardware, Wrong Software - Fugacious Fan Funding | https://theamphour.com/215-wrong-hardware-wrong-software-fugacious-fan-funding/ | September 7, 2014 |
| 221 | Warming Up To IoT - Tendentious Thermal Tools | https://theamphour.com/221-warming-up-to-iot-tendentious-thermal-tools/ | |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 246 | Robots are coming - Ominous Operational Overhaul | https://theamphour.com/246-robots-are-coming-ominous-operational-overhaul/ | April 21, 2015 |
| 249 | Wearables Might Have Limited Fashion Options - Lachrymogenic Lane Language | https://theamphour.com/249-wearables-might-have-limited-fashion-options-lachrymogenic-lane-language/ | May 12, 2015 |
| 256 | Is This A Show? | https://theamphour.com/256-is-this-a-show/ | July 1, 2015 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 305 | An Interview With Dave Young | https://theamphour.com/305-an-interview-with-dave-young/ | June 29, 2016 |
| 334 | An Interview with Gerry Roston | https://theamphour.com/334-an-interview-with-gerry-roston/ | February 1, 2017 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 538 | Missle Man with Bruce Simson | https://theamphour.com/538-missle-man-with-bruce-simson/ | April 12, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ | |
| 560 | High End Audio with Remco Stoutjesdijk | https://theamphour.com/the-amp-hour-560-high-end-audio-with-remco-stoutjesdijk/ | October 3, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 572 | Technology Instruction with Charlie Larrabee | https://theamphour.com/572-technology-instruction-with-charlie-larrabee/ | January 9, 2022 |
| 602 | Rigorous engineering stuff may be out the window | https://theamphour.com/602-rigorous-engineering-stuff-may-be-out-the-window/ | September 11, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 644 | Garbage Ninjas | https://theamphour.com/644-garbage-ninjas/ | August 28, 2023 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1, 2026 |
