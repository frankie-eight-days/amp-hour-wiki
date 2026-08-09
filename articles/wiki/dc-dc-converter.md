---
title: DC-DC Converter
concept: dc-dc-converter
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A DC-DC converter is an electronic circuit that converts direct-current electrical power from one voltage to another, either stepping down — as when a nine-volt battery is reduced to a five-volt rail — or stepping up, as when two AA cells must supply a higher voltage than they provide.[32] Modern converters accomplish this through high-frequency semiconductor switching with magnetic energy storage, and conversion work that once filled equipment racks is now performed by a small switcher chip and a small inductor.[88] The devices are pervasive in digital systems, where a single design routinely requires half a dozen separate rails — 3.3 volts for I/O, a 1.2-volt core, a 1.5-volt PLL supply and more — making the power budget a set of interacting converters rather than a single calculation.[53] Switching converters are also among the largest sources of conducted noise in a product, placing them at the centre of most electromagnetic compliance problems.[165]

## Efficiency

A quoted converter efficiency figure describes a single operating point — a particular load current at a particular output voltage — and says nothing about the rest of the efficiency curve, so the headline number on a datasheet is not the figure a given design will achieve.[53] A product with several operating modes draws a different current in each mode and therefore sits at a different point on the efficiency curve in each, which is what undermines a power budget calculated from a single figure.[53] Consequently, converter efficiency must be built up and measured rather than computed from the datasheet, and the measured figure can come back at seventy percent where the quoted figure said ninety-five.[53] Rigorous measurement requires capturing input voltage, input current, output voltage and output current simultaneously — four instruments — because taking the readings in sequence lets the operating point drift between them.[18]

Very high efficiencies are attainable but characteristically over a narrow load range; a converter rated at ninety-eight percent typically holds that figure only within a restricted span of loads, so any headline claim should be read together with the range across which it holds.[112] The final percent of efficiency costs disproportionately more work than the first ninety, and the variables involved — interwinding capacitance among them — make extracting it a specialist skill rather than a matter of following design equations.[5]

Where a circuit's current draw is essentially static, the supply can be sized close to that draw with roughly twenty percent as a minimum margin; designing the supply also to survive fault conditions is a separate requirement and usually not worth paying for.[53]

## Switching frequency and semiconductor technology

A switching frequency of one megahertz counts as high for a converter, and ten megahertz is extreme; raising the frequency shrinks the magnetics dramatically but moves the losses into the switching devices, which is what bounds the trade-off.[304] Switching frequencies reaching into the tens of megahertz are what permit converters to be pulled onto the same die or into the same package as the load, because the magnetics shrink with frequency even as leakage and loss problems become harder.[156]

Device physics sets further limits. Raising a transistor's breakdown voltage normally costs switching speed, and the contribution of gallium nitride and other wide-bandgap devices is to break that link, holding off high voltages while still switching fast; because high efficiency means little waste heat, and little waste heat removes heatsinks, these devices enable very small supplies.[553] Step-down conversion nonetheless runs into a semiconductor ceiling somewhere around five to eight hundred volts input, above which there is no efficient way to convert down directly — one reason very-high-voltage distribution is not simply converted at the point of use.[353]

A synchronous converter is any standard topology with the rectifying diode replaced by an actively switched device, eliminating the diode's forward conduction loss; the diode's compensating advantages were that it is cheap and requires no timing or control.[565] A standard converter architecture can serve even unusual supply requirements provided the switching device is chosen for a controllable analog region rather than being driven hard into saturation.[290]

## Electromagnetic compatibility

Switching converters produce substantial conducted noise and therefore sit at the centre of most electromagnetic compliance problems rather than at their periphery.[165] Mitigation strategies target the noise at its source. Converters exist that move their switching frequency to track a radio receiver's tuning, keeping the switching fundamental and its harmonics a fixed distance from whatever station is being received — solving the interference problem by moving the aggressor rather than filtering it.[165] Choosing a switching frequency of two megahertz places the fundamental clear of the AM broadcast band, and deliberately spreading the switching frequency lowers the peak noise at any single frequency; both are decisions made to pass compliance testing rather than to improve the converter itself.[635]

## Power sources and battery operation

The choice of battery determines whether a converter is needed at all: a nine-volt cell is easily reduced to five volts, while two AA cells force a boost stage and its cost into the design.[32] A single lithium cell runs from about 4.2 volts at full charge down to about 3 volts at cut-off, crossing a 3.3-volt rail from above and then from below; a buck converter alone cannot follow that excursion, so extracting the cell's full capacity into a 3.3-volt circuit calls for a SEPIC topology, at some cost in efficiency against a converter that only steps one way.[62] Without a converter holding the rail up, a device captures only the portion of the discharge curve above its chip's minimum operating voltage — enough, in one instance, to turn a nominal eight-year battery life into roughly three months of usable service.[49] Lithium primary cells present the opposite hazard: they sit at a higher terminal voltage than the alkalines they replace, around 1.75 volts per cell, so a converter wired directly across a series stack can be pushed past its maximum input voltage by what appears to be a like-for-like battery swap.[690]

A switching converter and a linear regulator load a battery differently: the linear part draws constant current while the converter draws constant power, so as the battery discharges the linear regulator's drain holds steady while the converter's current rises with falling voltage.[629] Related measurement cautions apply to the loads themselves: power figures on microcontroller datasheets are not comparable between parts — microamps per megahertz ignores instructions per cycle, and power per instruction, the honest metric, is not published — so a genuine comparison requires building both boards and running identical software with identical peripherals and sleep modes.[629]

An instrument powered solely from a USB port with no boost stage cannot output more than the bus voltage minus its internal drops; in one case this capped a nominal five-volt output at 3.75 volts in the instrument's highest-accuracy mode.[640]

### Battery charging

A battery wants to be charged from a current source early in the cycle and from a voltage source as it approaches capacity, with the crossover point depending on cell chemistry, which makes charging a control problem rather than a matter of applying a fixed voltage.[41] A charge controller can drive an ordinary converter's compensation pin as its control input, turning any DC-DC converter into a battery charger without the converter containing any battery-specific logic.[41] That construction only pays at high power or in unusual cell configurations: it carries no internal switching devices, requiring external FETs plus a separate converter chip costing several dollars, where an integrated charger for a standard cell topology costs around fifty cents.[41]

## Control loop and stability

The compensation network of a converter is a resistor and capacitor setting the time constants of the feedback loop, and getting the values wrong is what makes a supply oscillate; because the correct values depend on the load, the calculation belongs in each design rather than being copied from elsewhere.[41] Measuring loop response rigorously means coupling a swept signal into the feedback divider through a small transformer and reading the result on a network analyser, turning stability from something assumed into something measured.[377] A datasheet's example circuit is sized for the datasheet's example conditions, so reusing its component values at a different target current leaves efficiency far from the quoted figure; the suggested inductor part numbers are a starting point, and verification of efficiency, noise and layout remains the designer's responsibility.[301]

## Packaging and integration

Converters are available with the inductor co-packaged on top of the controller, giving a small footprint at good efficiency — convenient enough to be used throughout a board for several different rails rather than designing each supply separately.[638] Some converter modules in an SO-8 outline are in fact small circuit boards with the inductor on top and the controller die embedded inside the board itself, which is why such a package appears to contain only passives when opened.[412] Bare-die and wafer-scale converter packages are photosensitive: a xenon camera flash delivered enough photons to an exposed converter on a well-known single-board computer to lock it up, a failure mode that appears nowhere in the electrical specification.[270]

For test equipment or any low-volume build, buying a converter module at thirty to fifty dollars beats designing one even though the chip, inductor, switching device and diode together cost about five dollars, because the design time is the expensive part and buys nothing the module does not already provide.[273] Placing a converter on a daughterboard isolates the main design from it, so a supply change — a part going obsolete or a specification moving — becomes a small board respin instead of a revision of the whole product.[565]

## Applications

### Automotive

A vehicle's 12-volt line carries enough transient energy that an ordinary converter is likely to fail eventually, so automotive-rated parts are bought for survival rather than for paperwork.[568] A converter rated for 125 amps continuous into a vehicle's 12-volt system represents roughly a kilowatt of conversion capability — far more than accessory loads justify, and a strong indication in one examined vehicle that the capability was fitted for a vehicle-to-grid feature not yet enabled in software.[692]

### LED lighting

An LED lamp's service life is now set by its converter rather than by the light-emitting device, so reliability work on such products is work on the power supply.[71] Leakage through switch capacitance, combined with how little power a modern lamp needs, can supply enough current to raise the converter's start-up threshold and make a switched-off bulb glow faintly.[491]

### Capacitor-bank charging

A converter charging a capacitor bank faces the widest possible load swing within a single cycle of operation: a discharged capacitor looks like a short circuit and one charged to nine hundred volts looks like an open circuit, which is what makes the magnetics design difficult.[481] Giving the converter the maximum available time to complete a charge is what makes it efficient, and monitoring the rate of rise of the capacitor voltage doubles as a safety check — a bank that is not rising as expected is shorted, and continuing to drive it starts a fire.[481]

### Photovoltaic systems

A solar panel's substantial source impedance — around thirty ohms in one satellite design — means that drawing more current pulls the panel voltage down, and that relationship is what lets a converter regulate its own input voltage rather than its output.[401] Where a five-year orbital mission makes radiation-induced bit flips likely and reprogramming impossible, a maximum power point tracker was built as an analog computer around an op-amp instead of a microcontroller, computing the panel's peak-power voltage directly and feeding it forward to control the converter's input.[401]

### Isolation

Parts exist that carry both isolated data and an isolated supply across the same barrier, and the common mistake made with them is connecting the two grounds back together downstream, which defeats the isolation the part was bought for.[341]

## DC distribution

A solid-state transformer is a conversion chain rather than a magnetic device — rectify to a DC bus, convert, then invert back to AC — and the reason it does not simply replace distribution transformers is the number of devices that would have to be stacked in series to stand off hundreds of kilovolts.[717] A whole-house DC distribution scheme fed from one central converter founders on the wiring rather than the electronics: every run must be sized for the highest current any outlet might draw, and the copper that requires is prohibitively expensive.[25]

## Design, substitution and procurement

Converters churn in and out of availability fast enough that a schematic revision can turn into two days of parametric searching for a substitute, and a part unavailable two months earlier may be back in stock.[128] When a converter goes to a year's lead time, the practical search is by footprint first: working down the list of datasheets looking for a part that drops into the existing land pattern is faster than redesigning the supply around a better part.[637] Two days spent finding a replacement converter is sometimes two days spent solving the wrong problem, since a change elsewhere in the schematic can remove the need for the rail entirely — a possibility worth checking before the substitution search begins.[128]

Component substitutions in production range from a paper qualification, where reading the datasheet is genuinely sufficient for something like a resistor, up to changes requiring a sample build and real testing; a converter swap sits at the expensive end and takes the design back to first principles.[279] Design documentation should record why each value was chosen, not merely what it is: the reason a supply uses a 4.7-microfarad capacitor rather than a 10 — acoustic behaviour, for example — is exactly what has been forgotten by the time a part goes obsolete and the circuit must be revisited.[279] Where no catalogue part meets the requirement, custom silicon remains the last resort: when no existing converter could meet a start-up requirement of 0.6 volts, one company canvassed every manufacturer and then designed its own integrated circuit, illustrating that for a sufficiently unusual specification the only remaining option is silicon of one's own.[389]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ |  |
| 18 | Transistor Types and Where To Get Electronic Gear | https://theamphour.com/the-amp-hour-18-transistor-types-and-where-to-get-electronic-gear/ |  |
| 25 | NASA, WOTW & Modular Design - The NASA Nostalgia | https://theamphour.com/the-amp-hour-25-the-nasa-nostagia/ |  |
| 32 | Cores, Digikey, Electronic Design - The Commercial Competitor Commencement | https://theamphour.com/the-amp-hour-32-the-commercial-competition-commencement/ |  |
| 41 | Contests, Ham Radio & TWIT.tv - Ham, Spam, Thank You Ma'am | https://theamphour.com/ham-spam-thank-you-maam/ | May 4, 2011 |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ |  |
| 53 | Biarchy Birthday Bavardage | https://theamphour.com/the-amp-hour-53-biarchy-birthday-bavardage/ |  |
| 62 | Op amps, Microchips & Mergers - Narquois Nerd Nescience - Narquois Nerd Nescience | https://theamphour.com/the-amp-hour-62-narquois-nerd-nescience/ |  |
| 71 | An Interview with John Edmond - Luciferous LED Lucubrator | https://theamphour.com/the-amp-hour-71-luciferous-led-lucubrator/ |  |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 112 | An Interview with Bob Simpson - Ardent Automotive Artisan | https://theamphour.com/the-amp-hour-112-ardent-automotive-artisan/ | September 9, 2012 |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 156 | Tesla, FPGAs and DigiKey - Zesty Zippy Zynq | https://theamphour.com/the-amp-hour-156-zesty-zippy-zynq/ | July 29, 2013 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 273 | Part Choice Triathlon | https://theamphour.com/273-part-choice-triathlon/ | October 28, 2015 |
| 279 | Merry Keyzermas! | https://theamphour.com/279-merry-keyzermas/ | December 22, 2015 |
| 290 | An Interview with Mark Morin of Nufern | https://theamphour.com/290-an-interview-with-mark-morin-of-nufern/ | March 9, 2016 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 304 | Alexa joins the fray | https://theamphour.com/304-alexa-joins-the-fray/ | June 22, 2016 |
| 341 | All the way with DLJ | https://theamphour.com/341-all-the-way-with-dlj/ |  |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 401 | An Interview with Brent and Bryce Salmi | https://theamphour.com/401-an-interview-with-brent-and-bryce-salmi/ | July 29, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 481 | An Interview with Paul Thompson | https://theamphour.com/481-an-interview-with-paul-thompson/ | February 24, 2020 |
| 491 | The Almighty Dollarydoo | https://theamphour.com/491-the-almighty-dollarydoo/ | May 3, 2020 |
| 553 | Debunking with Shahriar | https://theamphour.com/553-debunking-with-shahriar/ | August 10, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 568 | YouTube to Consulting with Florin of Voltlog | https://theamphour.com/568-youtube-to-consulting-with-florin-of-voltlog/ | November 28, 2021 |
| 629 | At least my house isn't haunted | https://theamphour.com/629-at-least-my-house-isnt-haunted/ | April 23, 2023 |
| 635 | Low Power Connected Devices with Andrea Longobardi | https://theamphour.com/635-low-power-connected-devices-with-andrea-longobardi/ | June 4, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11, 2025 |
| 692 | Like a steam engine in your house | https://theamphour.com/692-like-a-steam-engine-in-your-house/ | April 15, 2025 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
