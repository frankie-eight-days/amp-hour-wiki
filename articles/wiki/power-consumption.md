---
title: Power Consumption
concept: power-consumption
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**Power consumption** is the rate at which an electronic circuit or system draws energy from its supply, and it is one of the primary constraints in electronic design, governing battery life, heat generation, mechanical design, and operating cost.[61][173][518] In digital circuits it decomposes into a dynamic component that scales with switching frequency and supply voltage, and a static component dominated by leakage, with the gap between active and off-state draw spanning several decades of current.[61][53] Because dissipated electrical power becomes heat, consumption is simultaneously an electrical and a thermal design problem, and in domains from medical implantables to satellites it can dominate the entire design effort.[704][501]

## Physical origins

Dynamic power in a digital process has a switching-frequency component and a supply-voltage component, which is why chip designers push core voltages as low as the process allows and avoid raising switching frequency beyond what the task requires.[61] Every logic transition charges a small capacitance — a trace, a bus line, a gate input — and therefore draws a pulse of current, so the instantaneous current on each clock edge scales with how many lines change state.[239][322] Slowing the slew rate reduces each impulse current, but only up to the point where the slower transition keeps the output devices in their linear region long enough to dissipate more than is saved.[322]

Process scaling reduces dynamic power superlinearly: halving the feature size roughly quarters power consumption while increasing speed, because the effect is quadratic, though the gains are paid for in wafer cost, yield, radiation performance, leakage, and progressively lower gate voltages.[347] Even within a fixed process, microarchitectural choices carry power costs; shortening a processor pipeline stage below its physical sweet spot requires making all the logic on the path faster, which consumes additional power and forces sacrifices elsewhere.[721]

Static consumption arises from leakage and bias currents. A low-power part may draw hundreds of microwatts in operation yet only nanoamps of leakage once switched off, and because leakage varies with temperature, the off-state figure cannot be assumed constant across the operating range.[53]

## Historical development

Power reduction has been a driver of semiconductor process and logic-family development since the early microcomputer era. Process work in the early 1980s, moving from roughly 1.6 micron toward one micron, was aimed not only at shrinking geometry but at making transistors turn off more completely so chips drew less power.[222] Earlier logic families illustrate the cost of static dissipation: an NMOS inverter is effectively a single transistor with a pull-up resistor, so it burns current continuously whenever its output is low, which is why NMOS logic dissipated far more than the CMOS that replaced it.[351] Integrated injection logic, promoted in the 1970s as a dense alternative to TTL, dissipated so much power in microprocessor implementations that ordinary ceramic packaging could not extract the heat and beryllium ceramic had to be substituted.[361] More recently, clock-frequency scaling has effectively stalled in favour of rising core counts, but packing more transistors into the same area raises the power dissipated in that area and makes heat extraction a limiting problem.[501] Design priorities also differ between otherwise similar parts: the RP2040 microcontroller was designed for low cost and deterministic behaviour with little attention to power, offering a deep sleep mode but remaining unsuited to micropower work, a gap addressed in its successor, the RP2350.[687]

## Figures of merit

The standard figure of merit for comparing processing platforms under a power budget is MIPS per watt — how much processing is obtained for a given consumption.[183] Active consumption of microcontrollers is conventionally quoted as current or power per megahertz; one low-power part, for example, is specified at 88 microwatts per megahertz in active processing mode.[629] This metric misstates efficiency when processors differ in instructions executed per clock, however: a part taking four cycles per instruction delivers a quarter of the work for the same current per megahertz, so power per MIPS is the sounder figure, and datasheets rarely provide it.[629]

Quoted figures must also be interpreted against the supply architecture. Whether a microcontroller's draw looks like constant current or constant power depends on its internal regulation: a core fed by an internal LDO draws constant current, so input power falls as battery voltage falls, whereas a DC-DC converter makes the draw constant power and the input current rises as the battery discharges.[629] For the same reason, battery-life arithmetic that divides capacity by load current must be performed in power rather than current whenever a boost converter sits between cell and load, because the converter draws more input current than the load current at the lower input voltage.[362] Headline ratings can likewise mislead outside electronics: an air conditioner's kilowatt figure is thermal output rather than electrical input, and because it is a heat pump with a coefficient of performance above one, a 3.5 kilowatt unit draws only about 800 watts electrically.[520]

## Measurement and characterisation

Because datasheet figures are unreliable for comparison, the only dependable way to compare two microcontrollers for power is to build a board around each, run the same firmware on both, and exercise every peripheral and sleep mode while measuring.[629] Consumption should also be re-measured over the full operating temperature range — for example by placing the assembled unit in a thermal chamber and repeating the measurement at 0 °C and 70 °C — because leakage and bias currents vary with temperature.[53]

Characterisation continues after a product ships. On the Pebble smartwatch programme, Andrew Witte's team used current probes to determine exactly where power was going on the board, driving the firmware into each of its modes in turn to attribute consumption.[175] Attribution is intrinsically difficult because a single firmware routine typically enables a radio, subsystem clocking, and further peripherals at once, so the observed current cannot be assigned to any one action.[527] Ordinary bench meters cannot resolve current across the full span from sleep to active, so dedicated energy analysers with wide dynamic range, such as the Joulescope, are used for troubleshooting.[661] Firmware continuous-integration practice includes measuring baseline power consumption on real hardware for every build, so that a change which doubles the current drawn in a given power state is caught when introduced rather than immediately before shipping.[556]

## Low-power design practice

### Energy budgeting

A low-power design starts from the battery: chemistry and capacity are chosen first, because without a fixed energy source there is nothing against which to budget the rest of the design.[389] Some loads can be omitted from the budget entirely; a real-time clock draws so little that it is usually insignificant next to the rest of the system — such parts are said to run "on the sniff of an oily rag".[389] Average consumption, not peak, determines battery life, so duty cycling is the central technique: the device wakes, connects, sends its data, and returns to sleep quickly, keeping joules per cycle small even when peak power is high.[202] The update rate is therefore a requirements question before it is an engineering one. On a solar-powered soil-sensing project, Luke Iseman's team optimised around an assumed one-reading-per-minute rate, but users were satisfied with four readings a day — a duty cycle requiring roughly a thousandth of the power — and establishing the real requirement first would have avoided hundreds of hours of optimisation.[268] Industrial wireless sensors typically report every six minutes or every hour; the interval can be scheduled below a second, but doing so directly increases consumption and shortens battery life.[458]

Sleep modes have entry and exit costs that bound their usefulness. Entering a Wi-Fi power-save mode can take up to about 300 milliseconds, so there is no benefit in dropping to the next power-save level unless the device will remain online longer than that.[202]

### Power gating and component-level practice

Functional blocks that are not in use are switched off entirely. Integrating blocks onto a single die facilitates this, since unused sections of the die can simply be powered down.[97] Analog front-end and boost-converter sections are switched off when idle because their linear elements would otherwise draw substantial current continuously.[218] Peripherals left initialised but unused are a common source of unexplained current: an idle UART block can draw more than 200 microamps, and de-initialising and powering down the block recovers it.[661] Bus pull-up resistors are a continuous drain whenever the line is held low, so low values such as tens of ohms are avoided on battery-powered designs in favour of values in the 2K to 10K range, trading edge speed for current.[274] Where a capacitive touch input serves as a wake-from-off power button, a dedicated external touch controller that holds the microcontroller unpowered until a touch is detected costs less current than the microcontroller's built-in touch peripheral.[477] Firmware-level optimisation resembles earlier code-size and speed work, and includes running the core at a different clock speed to trade throughput for a small reduction in consumption.[187]

### Radio and communications

Radio design is often the dominant power decision in a connected device. Choosing a very low data rate permits a very sensitive receiver because more processing gain is available per bit, which keeps both cost and transmit power down; a utility meter, for instance, needs only about one bit per hour.[109] Where antenna size is unconstrained, a lower carrier frequency is preferable: semiconductors are cheaper, gain is easier to obtain, propagation is better, and consumption is lower.[109] Payload format is likewise a power decision: replacing a 200-byte JSON packet with a 16-byte binary message cut hundreds of microamps of average consumption in one deployment by shortening radio-on time.[661]

Architecture-level choices follow from link budgets. Battery-powered sensor nodes are commonly given a low-power proprietary RF link to a mains-powered gateway that bridges to Wi-Fi, rather than putting Wi-Fi on every node — a decision driven mainly by power and secondarily by cost.[272] For wearable personal-area links, Bluetooth Low Energy is the low-power option but cannot carry video; moving to Wi-Fi for the higher data rate brings an order-of-magnitude jump in consumption, with no satisfying low-power link in between.[638] For low-rate sensor telemetry, 2G bandwidth is entirely adequate, and the objection to it is the power required at the device; in Europe the 2G and 3G networks have in any case been switched off.[678] Keeping a GNSS receiver listening for signals around −120 dBm is power hungry, which is why combined cellular-and-GPS front ends alternate between the two functions rather than running both continuously.[600]

### Offloading

Moving computation off a power-constrained device is a recurring architectural lever. Doing heavy processing locally on a wrist-worn device is the main reason its battery life is short; treating the watch as a terminal for a nearby phone moves the consumption elsewhere.[233] The saving is a system-level reallocation rather than an absolute reduction, because the transmitting device consumes extra power to carry the offloaded data.[638]

## Platform selection

Power consumption is one of the parametric reasons a design is taken to an ASIC rather than an FPGA, alongside die area, physical size, IP protection, and business considerations; FPGAs are rarely selected when power is the governing constraint.[103][264] The difference is felt directly in product design: on Jeri Ellsworth's head-mounted display project, performing head-tracking and video processing in an FPGA dissipated enough power that the glasses became noticeably warm to the wearer, driving a move to an ASIC to cut both consumption and heat.[173] Consumption in programmable logic is also easy to create accidentally: a single line of behavioural HDL can instantiate several thousand gates and add on the order of 100 milliwatts, a consequence that stays invisible until the design no longer fits the part or fails timing.[302] FPGAs additionally impose packaging constraints: a high-capacity device cannot be offered in a very small pin count, because with only a handful of pins a single power pin carries too much inductance to supply the surge current the device needs at turn-on.[567]

An analogous trade-off exists between microcontrollers and microprocessors. The Pebble watch platform was built on a microcontroller rather than an ARM Cortex-A class microprocessor, accepting reduced application headroom in exchange for lower consumption, and power was treated as a primary criterion in both part selection and software design, with features dropped when they would cost too much battery life.[175] Engineers controlling power and timing tightly may also resist larger ARM parts because they force reliance on manufacturer peripheral libraries whose internal behaviour and timing are opaque.[403] A Linux single-board computer used for a task a microcontroller could do wastes most of the power it draws, and even low-power variants still require a mains supply or a large battery with solar charging.[565] A Raspberry Pi, with a supply requirement of 5 volts at up to 2.5 amps, is unsuitable as a default for embedded applications on power grounds.[428] Within a product line, consumption can differentiate variants: the Raspberry Pi Model A cost about $10 less than the Model B, dropped one USB port and the Ethernet interface, and consumed substantially less power because a large share of the Model B's consumption went to the Ethernet controller.[97] Board-level figures must be quoted with their assumptions: the BeagleBoard consumed roughly 2 watts at maximum clock while decoding video, plus whatever peripherals drew from the USB host ports.[59] Conversely, older hardware can be surprisingly frugal: an early 386SX-class industrial PC drew about two watts idling, low enough that no heatsink was required.[362]

Where line power is available, the delivery standard sets the budget: Power over Ethernet supplies on the order of 10 watts to a device, and designs intended to be safely within that budget are targeted at less than half the maximum.[318]

## Application profiles

### Wearables and body-worn devices

For body-worn devices, heat generation is a design constraint in its own right alongside battery life, so processing is moved off general-purpose logic specifically to stop the product running warm.[173] The battery itself is usually the binding limit: a smartwatch achieving about seven days of life was calculated to be drawing only around 600 microamps, with the small cell that fits the case — not the current draw — being the constraint.[238] Wearable wireless modules show the characteristic pulse profile of such devices, specified at 200 to 300 milliamps peak and under one milliwatt in standby.[249] Not every microcontroller can serve: the CH32V003 proved unsuitable for a coin-cell-powered LED earring because its consumption is high for the application and its brown-out detector cannot be disabled, so the part simply stops below about three volts rather than running the cell down.[697] Display choice follows the same logic: a reflective segmented LCD gives high contrast for almost zero power and needs no backlight, suiting a battery-powered instrument whose clock keeps the display live continuously, though it cannot show arbitrary content; dot-matrix panels are chosen when flexibility matters, and transflective dot-matrix panels that work without a backlight are difficult to source.[700]

Hearing-device-class products impose still tighter budgets: total consumption below one milliamp, of which only a small portion is available for the analog and wireless sections, forcing extensive measures in the control stack to pull consumption down.[338] In medical implantables, driving consumption down to virtually nothing is the system bottleneck and can absorb around 90 percent of total design effort, leaving the remaining functionality comparatively straightforward.[704]

### Battery-powered Wi-Fi devices

In a battery-powered Wi-Fi device, most of the energy is burned in high load transients rather than in steady-state online operation, and alkaline, nickel-metal-hydride, and lithium primary chemistries behave differently under those transients.[202] A representative device drew roughly one to two milliamps powered up with the radio off, five to six milliamps with Wi-Fi on in power-save mode, and about 100 milliamps with everything running.[202]

### Remote and satellite telemetry

Sealed field sensors are designed against multi-year battery targets: one sensor puck programme was governed by a requirement of five years on the internal battery, making consumption the overriding system constraint.[179] A battery security camera built around a custom low-power imaging chip ran about two years on two AA lithium cells while capturing continuous low-frame-rate video, an achievement attributable to the custom silicon.[382] Satellite links impose their own arithmetic: Iridium Short Burst Data messages carry 340 bytes uplink and 240 bytes downlink per message, transmitting a single message draws over a watt for several seconds, and attempts often have to be repeated, so the energy per successful message is a multiple of the nominal figure.[614] On the spacecraft itself, lower consumption directly extends economically useful life because the solar panels degrade over time, while the companion limit is heat rejection, since large heatsinks are not an option.[518]

### Large-channel-count systems

In towed marine seismic streamers up to about 10 kilometres long, ADC power consumption dominated the system design because it was multiplied across roughly 10,000 channels, so every microwatt per channel mattered.[65] The budget trades directly against mechanical design: higher consumption demands heavier copper conductors to carry the power, which in turn demands more buoyancy material.[228]

### Audio

Class D amplifier efficiency is high only at high output levels; at normal listening levels the losses in the output filter inductors dominate, and an amplifier optimised for that region can cut consumption there by a factor of ten.[338] Output quality can be tuned upward at the direct expense of higher consumption, making it an explicit product-level trade-off rather than a fixed specification.[338] At the opposite extreme of the field, a large valve audio amplifier used about 23 tubes with roughly 16 to 20 amps of filament current and a 535-volt DC plate supply, drawing on the order of one kilowatt in total.[115]

### LED systems

Perceived LED brightness follows roughly a square law, so doubling apparent brightness requires about four times the power; gamma correction applies the inverse of the eye's response.[412] Applying gamma correction to an LED array therefore both makes brightness look correct and reduces overall consumption, because the corrected colours are skewed darker.[450] Installations are sized to worst case but run well below it: one large array was designed to a maximum draw of about 500 watts but in practice ran nearer 100 to 200 watts, because only part of the array was illuminated at any moment.[450]

### Data conversion and processing

Oversampling imposes a clock-rate cost that becomes a power problem: a 50 MHz signal bandwidth oversampled 64 times demands a 3.2 GHz clock, comparable to the fastest desktop processors and precisely the regime designers avoid on power grounds.[474] At the largest scales, converting an existing data centre to AI workloads has required roughly an order of magnitude more incoming power for the same server floor area, with new building volume added purely for transformers, cooling, and standby generators.[724]

## Failure modes

Power-related faults are frequently subtle. An on-chip back-bias generator — a capacitive voltage doubler driving the substrate — in one early home-computer chip drifted in voltage during intervals when the chip was not being addressed and corrupted the display; grounding the substrate through the package's pin-one slot restored correct operation.[222] An underpowered charger can present the correct voltage and assert charging status while supplying almost no current, so the machine's own consumption exceeds the charge current and the battery discharges despite the operating system reporting that it is charging.[702] Idle but initialised peripherals, brown-out detectors that cannot be disabled, and battery chemistries mismatched to load transients are further recurring sources of designs that miss their consumption or lifetime targets.[661][697][202]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 53 | Biarchy Birthday Bavardage | https://theamphour.com/the-amp-hour-53-biarchy-birthday-bavardage/ | |
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ | |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ | |
| 65 | Silego, ADCs & Seismic Detection - Dave's Dingo Dystocia | https://theamphour.com/the-amp-hour-65-daves-dingo-dystocia/ | |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ | |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 109 | An Interview with Larry Sears - Hexagram Hardware Holism | https://theamphour.com/the-amp-hour-109-hexagram-hardware-holism/ | August 19, 2012 |
| 115 | An Interview with Dr Greg Charvat - Watcher of Wraithlike Walls | https://theamphour.com/the-amp-hour-115-watcher-of-wraithlike-walls/ | September 30, 2012 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 179 | Greg Charvat Returns With A Book! - Laboratory Literature Laureate | https://theamphour.com/179-greg-charvat-returns-with-a-book-laboratory-literature-laureate/ | January 6, 2014 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 228 | An Interview with Shahriar from The Signal Path - Quisquous Quivering Quadripole | https://theamphour.com/228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole/ | December 16, 2014 |
| 233 | Glass and Gongkai GSM - Unzymotic Ursidae Upbuilding | https://theamphour.com/233-glass-and-gongkai-gsm-unzymotic-ursidae-upbuilding/ | January 20, 2015 |
| 238 | Old Books, New Tricks - Iterant Inscription Irrationality | https://theamphour.com/238-old-books-new-tricks-iterant-inscription-irrationality/ | February 25, 2015 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 249 | Wearables Might Have Limited Fashion Options - Lachrymogenic Lane Language | https://theamphour.com/249-wearables-might-have-limited-fashion-options-lachrymogenic-lane-language/ | May 12, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 268 | An Interview with Luke Iseman of yCombinator | https://theamphour.com/268-an-interview-with-luke-iseman-of-ycombinator/ | September 22, 2015 |
| 272 | An Interview With Luke Beno of Analog.io | https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/ | October 21, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 322 | World Trade Futurity (WTF) | https://theamphour.com/322-world-trade-futurity-wtf/ | November 9, 2016 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 361 | An Interview with Ken Shirriff | https://theamphour.com/361-an-interview-with-ken-shirriff/ | September 25, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 382 | The Toggle Boggle | https://theamphour.com/382-the-toggle-boggle/ | March 4, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 629 | At least my house isn't haunted | https://theamphour.com/629-at-least-my-house-isnt-haunted/ | April 23, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 678 | All About Antennas with Katerina Galitskaya | https://theamphour.com/678-all-about-antennas-with-katerina-galitskaya/ | September 30, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 697 | LEDs Everywhere with Tim from Mitxela | https://theamphour.com/697-leds-everywhere-with-tim-from-mitxela/ | July 8, 2025 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
| 702 | Test Point Accupuncture | https://theamphour.com/702-test-point-accupuncture/ | September 14, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 721 | Chip Design for Fun (and Waffles) with Julia Desmazes | https://theamphour.com/721-chip-design-for-fun-and-waffles-with-julia-desmazes/ | April 8, 2026 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
