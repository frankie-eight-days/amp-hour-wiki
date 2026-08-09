---
title: Pull-Up Resistor
concept: pull-up-resistor
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A pull-up resistor injects a controlled current from a supply rail into a node that would otherwise float once the driving device stops pulling it low; using a resistor rather than a direct connection to the rail is what makes the current controlled and allows the driver to overpower it.[274] An open-collector or open-drain output can only pull its node low, so it is inoperable without a pull-up somewhere on the net to establish the high level.[128] The component is therefore constitutive of open-drain buses: an I2C bus in its entirety is two wires and two pull-up resistors, one on the clock line and one on the data line.[396] Selecting its value is a trade between edge speed and standing current, and getting that trade wrong is one of the most common causes of marginal digital behaviour.[274]

## Electrical behaviour

Lowering the pull-up value increases the current available to charge the node, which shortens the rise time and reduces timing-marginal behaviour on the bus.[274] The reason higher values are used at all is power: a very low value injects a large current every time the line is held low, which either burns power directly or shortens battery life, which is why practical pull-ups cluster in the 2 kilohm to 10 kilohm range.[274]

A node brought high through a resistor approaches the rail asymptotically rather than in a straight edge, so an RC rise is unsuitable where a signal must reach a valid logic high within a tight timing budget.[222] The resulting edge asymmetry is visible on an open-collector bus: the falling edge is driven by a transistor and is nearly instantaneous, while the rising edge is produced only by the pull-up charging the line, so on an oscilloscope the two edges of the same signal have visibly different shapes.[274]

The level on a node is the resolution of everything attached to it rather than the intent of any one component, so where several pull-ups and pull-downs share a net their combined effect determines the resulting logic level.[599] Internal pull-ups on GPIO pins tied to the same node act in parallel, so enabling several at once produces an effective resistance of roughly a fifth of one pull-up and correspondingly faster edges and higher throughput.[697] An internal microcontroller pull-up is a weak resistor, on the order of 50 kilohms, and against the capacitance of a real node it limits data rates severely: reading a phototransistor through one held throughput below a thousand bits per second.[697]

## Choosing a value

The upper bound on a pull-up value is set by the input leakage current of the pin it holds: the resistor should be raised as far as power saving demands, but not so far that leakage develops a significant voltage across it.[10] The lower bound is set by the current the design can afford and the current the driving device must sink.[274]

For I2C, the Philips standard gives 2.2 kilohms as the nominal reference value, and longer lines, more devices and higher bus capacitance all push the appropriate value below that figure.[396] A working default of about 2 kilohms is common, and dropping to 1 kilohm is a legitimate diagnostic step when a bus is marginal.[274] The maximum speed of such a bus is itself set by an RC time constant: the roughly 2.2 kilohm pull-up charging the capacitance of the line fixes the slew rate of the rising edge, and that slew rate fixes the bus speed, so data rates far above the passive limit require an active pull-up rather than a resistor.[631]

Bus capacitance is what turns an oversized pull-up into a failure: the line takes too long to charge, the rising edge loses its sharpness, and receivers no longer see clean logic transitions.[396] Breadboard and flying-wire construction adds both stray capacitance and antenna-like pickup, so a prototype built that way needs a lower value than the same circuit would on a finished board.[274]

Where the net is fast, values fall dramatically. A 25 MHz clock line with substantial bus capacitance requires a pull-up as low as 100 ohms, which draws on the order of 33 milliamps.[482] Digital inputs also carry a maximum input transition-time specification, of the order of 500 nanoseconds for ordinary 74HC logic, and a resistor-driven edge slower than that voids the guarantee: the input may enter a metastable state and a clock input may oscillate.[482]

## Failure modes and diagnosis

If a pull-up is too weak for the leakage current present, the node is no longer held at a defined level and drifts, which is a slow and difficult fault to track down.[10] A high-impedance node held by a weak pull-up is also perturbed by the act of probing it, so the symptom can vanish as soon as an instrument or a finger is brought near the pin; that disappearance is itself evidence of an inadequately pulled-up input.[10] An input left without any defined pull-up returns whatever the surrounding environment imposes on it, so a read of a floating line yields ground, a high, or ambient radio-frequency pickup, and the result changes with the electromagnetic surroundings of the wiring.[222]

Under-strength pull-ups are hard to localise even for experienced hardware teams: on a server-class board it took multiple approaches to establish that the cause of the misbehaviour was simply a pull-up resistor that was not strong enough.[590] A large share of I2C bring-up failures likewise trace to the pull-up value rather than to the protocol or the addressing, with 10 kilohms and 5 kilohms common cases of a value too weak for the bus in question.[274] The standing first move when troubleshooting such a bus is therefore to check the pull-up resistors and, when in doubt, lower their value.[396]

On microcontroller inputs, the most frequent cause of a push button that fails to read correctly is that the internal pull-up was never enabled in firmware, leaving the pin floating; contact bounce is the other usual explanation.[599] A reset pin held only by the microcontroller's internal pull-up is similarly vulnerable to being disturbed by mains-frequency coupling and touch, and fitting an external pull-up of the order of 10 kilohms puts a far lower and better defined impedance on the pin.[288]

The reference rail matters as much as the value. A pull-up must be referenced to a rail whose voltage is actually known: pulling a microcontroller input up to USB VBUS on the assumption that VBUS is always five volts destroys the pin once power delivery negotiates VBUS up to twenty volts.[340]

Confirming that every open-collector net carries a pull-up is a standard item on a pre-fabrication PCB checklist, on the principle that routine mechanical verification catches omissions the designer already understands perfectly well.[428] A design review of a safety-relevant board also explicitly checks that every strapping pin is bootstrapped correctly by its pull-up resistors, so that the hardware lands in a safe configuration even if the wrong firmware is loaded and no output is set early in the code.[584]

## Power consumption

A pull-up draws current continuously whenever the line it holds is pulled low, so the habitual 10 kilohm pull-up is a permanent drain that a genuinely low-power design cannot afford.[7] A design targeting battery life measured in years cannot leave any pull-up energised during sleep, because the standing current through even one such resistor dominates the sleep budget.[527]

Topology can remove the drain. Wiring buttons to the positive rail against pull-down resistors, rather than to ground against pull-ups, means the resistors carry current only while a button is actually pressed.[403] That choice can be forced by the silicon, since AVR parts provide internal pull-ups only, whereas ARM parts typically offer internal pull-downs as well, so a pull-down scheme on an AVR requires external resistors.[403]

## Shared and open-drain buses

Because every device on an open-drain bus can only output a zero against a shared pull-up, any node on an I2C bus can force bits low at will; this wired-AND behaviour means a single misbehaving or hostile device can corrupt an address on the wire and impersonate a peripheral.[318] The same passive high level makes I2C less robust than SPI, since its high is produced by a resistor working against the capacitance of the bus and an incorrectly chosen pull-up leaves the line vulnerable to interference, whereas an SPI line is driven high and low by a totem-pole output and needs no pull-up at all.[274]

## Configuration and signalling uses

Configuration options that once required external logic to load into a device are now commonly set by strapping resistors: the chip pulls the pin internally and reads the level established by an external resistor at start-up.[128] USB applies the same idea to speed grades, signalling them with static pull-up and pull-down resistors on the data lines rather than with a software negotiation, so the host learns the speed grade from which data line carries a pull-up before any protocol exchange occurs.[51]

A pull-up of a known value working against another known resistance produces a predictable intermediate voltage rather than a logic level, and a 3.3 kilohm pull-up that yields roughly half the rail can be exploited to distinguish several inputs on a single pin by the voltage each one produces.[343] Pull-ups and pull-downs of differing values can likewise encode which of several buttons is pressed onto a single conductor, allowing more signals to be carried than there are wires; the same line can then be time-shared with another function such as LED data when the buttons are not being sampled.[689]

Toggling an internal pull-up on and off distinguishes a node that is genuinely driven low from one that is merely tri-stated or floating: a truly grounded pin stays low with the pull-up enabled, whereas a floating pin follows the pull-up.[689]

## Relation to logic families

An NMOS inverter is a single switching transistor working against a pull-up rather than a complementary totem-pole pair, so it draws current continuously whenever its output is held low and burns more power than the equivalent CMOS stage.[351] An NMOS pass device has a related limitation, able to pull its output up only to roughly a gate threshold below its supply — around four volts from a five volt rail — after which the gate turns off and the device behaves as a weak, poorly defined pull-up rather than an active driver.[222]

CMOS logic scaled where TTL could not because CMOS gates are built only from transistors and require no on-die pull-up resistors, and resistors occupy a physically large area of die compared with a transistor.[361]

A totem-pole CMOS output carries no pull-up because it relies on its upper transistor to drive the node high, so degradation of that transistor leaves the output able to pull low but not high, and the part fails progressively rather than all at once.[482] An external pull-up can rescue such a failed output, and the Intel C2000 clock-output degradation, which affected every manufacturer that had designed the processor in, was remedied across those products by exactly that external pull-up on the affected clock line rather than by a silicon replacement.[482]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 7 | Love Robots and Pantyhose Screens | https://theamphour.com/the-amp-hour-7-love-robots-and-pantyhose-screens/ |  |
| 10 | Open Hardware and Self Publishing | https://theamphour.com/the-amp-hour-10-open-hardware-and-self-publishing/ |  |
| 51 | Vafrous Video Vaniloquence | https://theamphour.com/the-amp-hour-51-vafrous-video-vaniloquence/ |  |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ | February 24, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 343 | Road trip to the deep space network | https://theamphour.com/343-road-trip-to-the-deep-space-network/ | April 17, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 396 | The Synergy Bus | https://theamphour.com/396-the-synergy-bus/ | June 10, 2018 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 584 | Software for Rockets with Charles Aylward | https://theamphour.com/584-software-for-rockets-with-charles-aylward/ | April 3, 2022 |
| 590 | Finding Hardware Flaws with Laura Abbott | https://theamphour.com/590-finding-hardware-flaws-with-laura-abbott/ | May 22, 2022 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
| 697 | LEDs Everywhere with Tim from Mitxela | https://theamphour.com/697-leds-everywhere-with-tim-from-mitxela/ | July 8, 2025 |
