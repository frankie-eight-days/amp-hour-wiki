---
title: Battery Life
concept: battery-life
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Battery life is the period for which a battery-powered device can operate before its cells are exhausted or require recharging, and it is governed by the ratio between the energy stored in the cells and the device's average power consumption over time.[10][49] It is frequently the governing constraint in portable and remote electronic design, determining a product's size, weight, price and feature set rather than merely following from them.[179][292][334] In remote telemetry it is also a commercial requirement, since a single field service visit can consume the margin on the serviced device and on several others.[427]

## Energy budgets and estimation

A first-order battery-life estimate comes from comparing cell capacity against load: a single AA alkaline cell holds roughly 2,800 mAh, so checking a product's advertised runtime against the capacity it carries is a quick test of whether the claim is plausible for the electronics inside.[10] At very low average currents the arithmetic yields striking figures — a load averaging around forty microamps runs roughly 70,000 hours from a pair of AA cells — but such figures approach a hard ceiling, because 70,000 hours is about eight years, roughly the shelf life of the cell itself.[49][191] Past that point self-discharge rather than circuit draw sets the limit, so reducing the average current further buys nothing.[191]

Estimates should be built on the correct datasheet figures. Typical supply currents are the right basis for a typical runtime estimate, while guaranteed maximum figures, usually quoted at temperature extremes, are what a power supply must be sized against; using worst-case numbers for runtime gives a needlessly pessimistic answer.[53] Budgets spanning several supply rails must be summed as power rather than current, because adding milliamps drawn at different voltages produces a meaningless total; working in current is only safe within a single fixed rail.[53]

## Duty cycling and sleep states

For most battery-powered devices the average consumption is set not by component ratings but by how much of the time each subsystem is powered. Achieved power consumption is dominated by firmware rather than by the schematic: a wearable board that runs four hours with everything powered up can reach days once the firmware sequences subsystems off.[175] A single instrument design can span three orders of magnitude of runtime on duty cycle alone — years of standby on two AA cells at an idle budget of about a hundred microwatts, falling to roughly ten days with every subsystem enabled and sampling continuously.[218]

Deep sleep currents set the floor of the achievable life before any activity energy is added. A deep sleep state of roughly a hundred nanoamps is achievable when only a real-time clock remains running, whereas a design carrying a cellular modem settles nearer half a milliamp asleep, a level that caps a set of AA cells at about 5,000 hours even if the device never transmits.[427][362] Between these extremes, a node sleeping at 1.8 microamps on two AA cells has a theoretical ceiling beyond ten years, against which the transmit energy is then subtracted.[557]

Peripheral autonomy extends the same principle inside the microcontroller. Transferring analogue-to-digital conversion results straight into memory by DMA, without waking the processor core, turns the part into a data logger that never runs code between reads; in workloads that fit the pattern this can cut energy consumption by around three orders of magnitude, and it saves nothing at all in workloads that do not.[95] Clock selection is a second lever: running a processor at a 32 kHz watch-crystal rate where the application demands no more throughput is the crudest and most effective control on average current, and is what allows a calculator-class wristwatch to target two years on a cell.[175] The converse failure is illustrated by a calculator redesign that emulated the original instruction set on a 30 MHz ARM part from a coin cell: the processor drew current in gulps the cell's internal resistance could not supply efficiently, and most of the original product's battery life was lost.[53]

Sleep-current failures in practice are usually sneak paths rather than device specifications: a shut-down subsystem back-powered through an input pin, a divider left partly turned on, or a pull-up left engaged.[527] Such leakage has to be traced by hand once an instrument shows it exists.[527]

## Circuit-level practices

### Indicator LEDs and resistors

Indicator LEDs are routinely driven far harder than a battery-powered product can afford. Raising the series resistor to run the part at a couple of milliamps, and specifying a higher-brightness die to recover the visibility, removes a continuous load from the energy budget.[10] Pulsing an indicator rather than driving it continuously delivers a perceived average brightness at a fraction of the average current, because the eye integrates the flashes; driven well below full brightness from a CR2032 coin cell, an LED can be kept continuously lit for about ten years.[10][465]

The habitual 10 kΩ pull-up wastes current continuously whenever the line is held low, so in a battery design the resistor should be raised toward the largest value the input's leakage current still allows.[10] The technique has its own failure mode: a pull-up raised too far leaves the pin floating, producing an intermittent fault that vanishes when a probe is touched to the pin, because the probe itself changes the node impedance.[10] In designs targeting multi-year life the rule is stricter still — any pull-up left active during sleep rules out years of battery life on its own, so low-power systems place pull-ups on a switchable rail that firmware can collapse along with the rest of the sleeping hardware.[527]

### Bulk capacitance

A bulk electrolytic capacitor across the cell supplies the short current pulses that the cell's own output impedance cannot, and measurably extends battery life in pulsed designs such as periodic radio transmitters.[202] The gain is largest with alkaline cells, whose output impedance is high and rises as they discharge, and much smaller with nickel–metal-hydride or lithium primary cells, whose output impedance is low and roughly constant across the discharge.[202]

### Sensor selection

In a battery sensor node the sensor rather than the radio frequently dominates the sleep budget: a passive infrared motion detector drawing 50 to 60 microamps continuously swamps a microcontroller and radio that together sit below 7 microamps asleep, of which the watchdog timer alone accounts for roughly 4 microamps.[398] Passive infrared sensors drawing about 2 microamps exist but cost on the order of thirty dollars apiece, so a twenty-five-fold reduction in the dominant sleep current is bought with an order-of-magnitude increase in component cost.[398] Similarly, a gyroscope draws on the order of ten times the current of an accelerometer, so testing whether a sensor actually contributes to the required result can remove both its cost and its power — one gesture classifier lost no accuracy when gyroscope data was withheld, eliminating a dollar of bill of materials and its current draw together.[525] Optimisation effort belongs where the return is largest: confirming that every sensor and peripheral actually enters its sleep state returns far more than selecting a marginally lower-power radio variant.[398]

## Radio and communications

Radio choice sets the floor of a connected product's energy budget. Wi-Fi is generally excluded from battery-powered designs, Bluetooth Low Energy trades bandwidth away for energy, and a classic Bluetooth link that must stay connected continuously costs far more than either.[145] Sub-gigahertz links around 900 MHz penetrate obstacles better than 2.4 GHz and need substantially less transmit power for the same reach, which is why battery-powered sensor nodes gravitate to the lower band.[398]

Report interval is normally the dominant term in a telemetry device's energy budget: moving from six transmissions an hour to one an hour is what takes such a device to five years or more on its cells.[334] Once sleep current is low enough, transmissions become the entire budget — adding a single 20-to-25-byte packet an hour to a node sleeping at microamps brings expected life down from over ten years to three to five.[557] A long-range low-power radio running at roughly 600 bits per second in its lowest-power mode and sending once an hour or once a day supports ten-year lifetimes, trading throughput for both range and energy.[422] The wake, connect, transmit and return-to-sleep cycle therefore dominates the budget, and how quickly a stack completes that sequence matters more to runtime than its steady-state currents.[359] Payload format matters on the same grounds: verbose text formats such as JSON are convenient on the phone side of a link, but every additional byte costs transmit energy, so devices targeting ten-year lifetimes encode compactly.[661]

The energy budget of an event-driven wireless device follows from four questions: how often the event occurs, how often the device must poll or announce itself, how quickly it must respond, and whether messages can be stored and forwarded instead of sent immediately.[389] Architecture can shift the burden further. Battery-powered always-listening devices run keyword detection on a small always-on coprocessor and keep the main processor and network link asleep, since streaming audio continuously would be prohibitive.[335] Computing an endpoint's position from angle of arrival at a receiving satellite lets a tag drop both its GPS receiver and its cellular modem and carry only a Bluetooth radio, removing the two largest energy consumers; with the signal-processing burden pushed onto the receiving infrastructure, a tag reporting once an hour can last multiple years on a single coin cell.[728] Offloading computation to a companion device moves the energy rather than removing it — the wearable's saving is partly paid out of the phone's battery.[638]

Antenna quality is a non-obvious but large term in the budget: a poorly matched or detuned antenna can waste half the transmitted RF power, which must be recovered either as lost range or as increased transmit power drawn straight from the battery.[435] At 2.4 GHz and above a millimetre of mechanical movement is enough to shift antenna performance, so an antenna etched into or onto the housing gives a far more stable match than one that can flex relative to the enclosure.[435]

Peak current capability also shapes radio design. A coin cell's internal resistance can be too high to supply the pulse a transmission demands, which is why long-life sensor nodes move up to pen-light cells even when the average current would suit a coin cell.[376] A satellite uplink burst radiating around 1.5 W draws roughly 3 W — close to an amp of peak current once power-amplifier efficiency is counted — so the design needs a dedicated power path or a supercapacitor to keep that peak from collapsing cells that otherwise see only nanoamps.[427]

## Displays, processors and software

Display technology determines how runtime scales with use. An electrophoretic display holds its image without power and consumes energy only when the image changes, so an e-reader's runtime scales with page turns rather than with the time the screen is visible.[301] OLED power scales with lit content because unlit pixels draw nothing, so a sparse interface on a dark screen costs a small fraction of a fully white display; runtime for such a device depends on what is shown, not merely on how long it is on.[638] Optical efficiency can carry the whole power design: a retroreflective projection surface returns almost all emitted light to the viewer's eye, allowing a wearable projector to operate at roughly one lumen rather than the hundreds a conventional projector needs, with the saving carrying both the battery and the thermal design.[340]

Processor class sets a hard floor. An application-class processor with external DDR memory running Linux consumes more than an all-day wearable budget allows even before the display and radio are counted, pushing such designs back onto microcontroller-class parts.[638] Battery-sensitive devices need explicit shutdown and low-power states under direct firmware control; placing a general-purpose operating system on every class of device forfeits that control and with it the achievable runtime.[253] A defensible wearable architecture spends its energy only on functions the user perceives — the display and the data link — and drives local processing toward zero, since computation delivers nothing the user can see.[638]

With cell sizes fixed, there are only three levers on a portable device's runtime: reduce the energy per operation through a smaller process node, turn more of the silicon off more of the time, or write software that does less work.[269] Mainstream phone cells top out around 3,500 mAh, so improvements have to be found in the load rather than in more stored energy.[269]

## Cells and capacity

Cell selection is as much about internal resistance, self-discharge and form factor as about nameplate capacity. Lithium thionyl chloride primary cells are the usual choice where a decade of field life is required, selected for very low self-discharge rather than for capacity alone.[376] At the small end, a Bluetooth Low Energy button device on a single CR2032 coin cell reaches about a year of service; moving to a thicker coin cell of the same diameter class multiplies the available capacity by about four, the simplest route from roughly one year to five years in a low-duty-cycle radio device.[389] Where no prototype measurements exist, a design proceeds from requirements: fix the physical size, fit the largest cell it will take, then drive the average resting current down through sleep modes until the required runtime falls out of the arithmetic.[389]

Form factor is frequently the binding constraint rather than current consumption. A smartwatch drawing on the order of 600 microamps average is not a heavy load by any absolute standard; its week-long runtime is set by the small cell the case permits.[238] Cell sourcing determines product life independently of the electronics: unbranded lithium cells in cheap wearables have been found to give four hours when new and to lose the ability to take a charge at all within about a week of use.[175]

Cell capacity also varies with temperature and from unit to unit, so a runtime characterised on one sample can be days out on another; cold conditions such as immersion in sea water reduce available capacity further, making deployed endurance a distribution rather than a number.[190] For devices specified at ten years of service, the cell rather than the electronics ends the product's life, and the design question becomes matching the cell's own shelf life rather than reducing current further.[557]

## Rechargeable pack longevity

For rechargeable systems, service life is managed through the state-of-charge window and charge regime. Restricting a lithium cell to roughly the 30-to-80-percent window, avoiding both full charge and deep discharge, extends its useful health by years at the cost of the capacity held in reserve at each end.[38] Hybrid-vehicle manufacturers apply the same principle to nickel–metal-hydride packs, holding them within plus-or-minus twenty percent around a fifty-percent state of charge, which yields hundreds of thousands of cycles; the same cells cycled to full depth deliver far fewer.[112] Home storage installations are likewise commonly configured to use only about eighty percent of nameplate capacity to extend pack life, so the usable energy a system is sized around is lower than the capacity printed on it.[677]

The first generation of energy-dense lithium cells was rated at only about 300 to 400 cycles, having been built for consumer goods replaced every year or two where cycle longevity was not a requirement.[112] An electric-vehicle pack is treated as having reached the end of its first life when it has lost twenty percent of original capacity, with the remaining eighty percent still serviceable in less demanding second-life applications; whether a pack reaches that point in five years or ten is determined by cell stress, operating temperature and management strategy rather than by chemistry alone.[112] Repeated high-rate DC charging is the largest single determinant of vehicle pack degradation, which is why manufacturers implement step-based charging algorithms and warn against habitual fast charging.[512]

Cells can be charged well beyond their rated C-rate — a cell rated for 5C will accept 10C — so passing a stress test proves less than it appears to, the cost being the cell's service life.[717] A twenty-degree-Celsius temperature rise during a charge test indicates internal losses that shorten life, making temperature rise a more informative result than whether the cell survived.[717] Battery management is accordingly a large part of what a packaged storage system buys: a self-assembled pack of comparable cells can work initially and be unusable within three or four years because nothing controls how the cells are charged and balanced.[358]

Chemistry transitions carry their own penalties. Moving hearing aids from primary cells to rechargeable chemistry lowered the available energy density substantially, turning a single day of continuous operation into the hard design target and forcing high-efficiency switching conversion into the signal chain.[338] Aftermarket battery-extender products exploit a different margin: they are boost converters drawing on the gap between a product's cut-off voltage and the cell's true end of discharge, and the energy recoverable that way is modest.[328]

## Measurement and verification

The current drawn by a modern battery device spans an enormous dynamic range, from nanoamps or microamps asleep to milliamps or amps while sensing and transmitting, and capturing both ends accurately in one measurement is the central difficulty in characterising an energy budget.[607] Because a spot current reading cannot answer how long a duty-cycled device will run, energy-measuring instruments integrate current and voltage into power, energy and accumulated charge over time — the quantity that maps onto battery life.[607]

The term "low power" itself spans several orders of magnitude, from a Linux-class system regarded as frugal at 150 milliamps to a coin-cell sensor measured in microamps, so a power target is meaningless without the current figure attached.[527] Characterisation conditions matter as well: portable audio runtime should be measured at the medium and low listening levels customers actually use rather than at full output, because realistic sound pressure needs only a small fraction of an amplifier's peak power.[338]

Per-subsystem measurement generally requires deliberate hardware: an internal development variant with every rail broken out to test points and current-sense shunts is what makes such measurement possible, since the production board rarely permits it.[175] Consumption should be measured on a regular cadence throughout development rather than at the end; discovering near release that battery life is a quarter of the specification leaves only a schedule slip or shipping spare cells as remedies.[556]

## System-level constraints

Required runtime is a specification to be fixed before design begins, alongside range and physical size; it determines price, size, weight and schedule, and revising it afterwards is a change order rather than a tweak.[292] Feature scope and runtime are the same decision: adding media playback to a wearable whose central requirement is multi-day operation forfeits that requirement, so the runtime specification must be settled before the feature list.[175] The gap this creates between device classes is large — a processor-based smartwatch of the mid-2010s reached about a week between charges against three years or more for a quartz analogue watch, a gap of two orders of magnitude coming from the display, radio and processor rather than from the cell.[175] The ordering of constraints has also shifted with time: for portable recording devices the binding limit moved from storage capacity to energy, as memory became cheap enough that what a device can capture is limited by what it can afford to power.[233]

Some applications make runtime non-negotiable. In-pavement parking sensors are hermetically sealed pucks that must last five years on internal cells because they cannot be serviced once glued into the road surface.[179] Fixed industrial gas monitors are specified in some applications for ten years without a battery change, making power consumption a headline requirement rather than an optimisation.[635] A pendant-format personal tracker specified at six months on a single charge, with the cell constrained by the form factor, forces aggressive duty cycling of the satellite receiver rather than continuous position fixing.[661] Energy-harvesting designs are dimensioned against the worst case of the source rather than its average: a solar-recharged sensor node uploading over 3G once an hour was sized to carry two to three weeks without sun.[355]

The rational low-power target is the servicing interval rather than the lowest current physically achievable; a node whose battery outlasts the interval at which it will be visited anyway gains nothing from further optimisation.[398] Even the structure of the charging interval affects usability: a runtime slightly longer than a day is worse in use than exactly one day, because daily charging attaches to an existing nightly habit whereas a two- or three-day interval breaks the routine and the device goes flat unexpectedly.[301]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 10 | Open Hardware and Self Publishing | https://theamphour.com/the-amp-hour-10-open-hardware-and-self-publishing/ | |
| 38 | An Interview with Jeff Keyzer - Comical Keyzer Comes a-Callin' | https://theamphour.com/the-amp-hour-38-comical-keyzer-comes-a-callin/ | |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | |
| 53 | Biarchy Birthday Bavardage | https://theamphour.com/the-amp-hour-53-biarchy-birthday-bavardage/ | |
| 95 | An Interview with Øyvind Janbu - Feracious Fabless Facilitator | https://theamphour.com/the-amp-hour-95-feracious-fabless-facilitator/ | |
| 112 | An Interview with Bob Simpson - Ardent Automotive Artisan | https://theamphour.com/the-amp-hour-112-ardent-automotive-artisan/ | September 9, 2012 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 179 | Greg Charvat Returns With A Book! - Laboratory Literature Laureate | https://theamphour.com/179-greg-charvat-returns-with-a-book-laboratory-literature-laureate/ | January 6, 2014 |
| 190 | Let's Hear It For The Buoys - Vanishing Vessel Vexation | https://theamphour.com/190-lets-hear-it-for-the-buoys-vanishing-vessel-vexation/ | March 24, 2014 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 233 | Glass and Gongkai GSM - Unzymotic Ursidae Upbuilding | https://theamphour.com/233-glass-and-gongkai-gsm-unzymotic-ursidae-upbuilding/ | January 20, 2015 |
| 238 | Old Books, New Tricks - Iterant Inscription Irrationality | https://theamphour.com/238-old-books-new-tricks-iterant-inscription-irrationality/ | February 25, 2015 |
| 253 | Consolidate All The Things - Zonked Zelotic Zaitech | https://theamphour.com/253-consolidate-all-the-things-zonked-zelotic-zaitech/ | June 9, 2015 |
| 269 | Be Tidy | https://theamphour.com/269-be-tidy/ | September 30, 2015 |
| 292 | An Interview with Timothy Lamb | https://theamphour.com/292-an-interview-with-timothy-lamb/ | March 23, 2016 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 328 | The Ghost of Keyzermas Past | https://theamphour.com/328-the-ghost-of-keyzermas-past/ | December 21, 2016 |
| 334 | An Interview with Gerry Roston | https://theamphour.com/334-an-interview-with-gerry-roston/ | February 1, 2017 |
| 335 | When the TV watches you | https://theamphour.com/335-when-the-tv-watches-you/ | February 8, 2017 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 355 | The Internet of Septage (with Akiba) | https://theamphour.com/355-the-internet-of-septage-with-akiba/ | August 13, 2017 |
| 358 | Mergers and People Acquisitions | https://theamphour.com/358-mergers-and-people-acquisitions/ | September 4, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 427 | An Interview with Maarten Engelen | https://theamphour.com/427-an-interview-with-maarten-engelen/ | January 27, 2019 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ | |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 635 | Low Power Connected Devices with Andrea Longobardi | https://theamphour.com/635-low-power-connected-devices-with-andrea-longobardi/ | June 4, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
| 728 | Space Age Bluetooth with Alex Haro | https://theamphour.com/728-space-age-bluetooth-with-alex-haro/ | July 9, 2026 |
