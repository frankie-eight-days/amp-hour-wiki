---
title: Calibration
concept: calibration
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Calibration is the process by which an instrument or product is referenced to known standards so that its readings can be trusted. It rests on a traceability chain in which instrument readings are compared back to national standards such as those held by NIST, so that widely separated instruments ultimately refer to the same small set of primary references.[72] A repeatable error can be calibrated out of a measurement, but uncertainty and drift cannot; they set the floor on how much confidence a measurement can carry.[94] In manufacturing, calibration is valuable because it lets a design correct nonlinearities and reach precision the raw hardware does not have, but it adds a fragile, labour-intensive stage to production.[182]

## Terminology

Two distinct activities are both called calibration. Instrument calibration verifies that an instrument meets all its published specifications and is what a calibration sticker certifies; open-short-load calibration is properly the error correction of a particular measurement setup.[533] The distinction has practical consequences: an instrument can be substantially out of its certified calibration and still yield a reasonable measurement once error correction is applied, because error correction references the measurement to known standards at the time of use.[533]

## Traceability

The impedance traceability chain begins with a precision airline whose impedance is derived from its physical dimensions at NIST; that airline calibrates a system, which in turn calibrates the loads and resistors used in ordinary laboratory calibration kits.[533] Guaranteeing a product's specification all the way back to a national standard carries real cost, because the manufacturer must own and maintain its own calibrated reference instruments in the chain.[554]

Standards-grade laboratories are scarce. Agilent's Melbourne facility is a standards-grade calibration laboratory that receives instruments from overseas, including from the United States, for calibration; few laboratories at that level remain worldwide.[132] Moving equipment at that level requires care, since freight shipping subjects calibrated equipment to heat cycling and shock, and high-accuracy standards are therefore moved by dedicated truck rather than by ordinary carriers.[132] Precision instrumentation destined for extreme field environments is fully insulated so that large swings in ambient temperature do not disturb the calibrated internals.[132] Ordinary shipping, by contrast, does not by itself invalidate an instrument's calibration; the temperature swings a package sees in transit are generally too small to shift a calibrated reading materially.[377] Calibrated instruments returned from a failed shipment nonetheless cannot simply be forwarded to customers, because the units require recalibration and that capability may not exist at the seller's own site.[377]

Rigour is tiered by the consequence of error. Aerospace and defence work keeps everything in calibration, runs daily calibrations and records every variation; cell-tower equipment is held to a looser standard, handsets looser still, and amateur radio work only as tight as the operator needs.[533] Recalibration is best folded into scheduled maintenance, since work such as replacing aged capacitors already requires opening the instrument and disturbs its existing calibration.[353]

## Calibration versus precision components

Specifying an expensive absolute-tolerance precision resistor instead of a cheap resistor plus a trimpot amounts to paying not to calibrate: the part price buys away the labour, time and error of a per-unit trim.[174] Small low-cost resistors also drift substantially over time, so a value set by trimming a cheap part does not hold, whereas a precision part keeps its absolute value.[174] The alternative to trimming each unit by hand is programmatic trim, which requires adding a DAC or programmable element plus all its supporting circuitry and firmware to an otherwise simple analogue product.[174] Older analogue high-current power modules are calibrated with trimmer potentiometers, while newer digital modules expose calibration through software menus, with DACs replacing the mechanical trimpots.[522]

The opposing approach accepts calibration and buys stability instead of absolute accuracy. A low-drift-plus-software-calibration design lets a product use inexpensive analogue parts, since a unit that must be calibrated anyway gains nothing from parts that are accurate straight out of manufacture; what matters is that the parts stay stable afterwards.[218] Building accuracy into the hardware instead is expensive at the component level: individual precision shunt resistors in a hand-held current-measurement instrument cost about five dollars each.[218] A precision current-measurement adapter reaches its published specification through parts rather than trimming, with a single resistor on the board costing about four dollars at volume against roughly twelve dollars at single-piece price, so the accuracy specification is effectively bought in the bill of materials.[554] A precision measurement product can be locked to specific parts in this way — 0.05 percent resistors, single-source op-amps, and a resistor costing around three dollars with no substitute — so that the usual contract-manufacturer practice of substituting equivalent parts is not available.[682] Open-source hardware built with lower-precision substitute components does not meet the original design's specification, and the original is separately guaranteed by custom-built test gear that checks every unit against spec.[554]

Specification setting is itself an economic exercise: loosening a published spec by a tenth of a percent can permit a part that costs an order of magnitude less, and pushing calibration onto the user is another way of relaxing what the factory must guarantee.[432]

## Calibration in production

Calibrating analogue components is straightforward for a handful of units but becomes a major manufacturing constraint at volume, since the per-unit time and equipment do not shrink with scale.[363] Hand-assembly steps such as bonding optical parts with adhesive introduce unit-to-unit dimensional variation, which forces a per-unit calibration step that a dimensionally stable production design could avoid.[147] Manual alignment procedures historically depended on tacit operator skill, with individual technicians known for knowing exactly how far to turn each adjustment, which makes such processes hard to transfer or scale.[146]

Production test on a low-cost precision product can be reduced from a full calibration to an automated pass-fail verification at a spot value, confirming each unit meets spec without characterising it over the full range.[182] High-volume consumer products typically ship with a built-in self test rather than a full calibration, whereas a test-and-measurement manufacturer devotes a large share of its production engineering to the calibration setup itself.[369] A sensor bought pre-calibrated to a guaranteed specification and read out over a digital bus such as I2C can remove the need for a functional or calibration test on the line altogether, whereas testing an uncalibrated sensor in-line would require stimulus hardware such as a pressure chamber.[544] Production line test tooling is scoped for fast, precise verification of each unit with live feedback, not for design validation work such as thermal vacuum or shake-and-bake testing at a certification laboratory.[544]

### Statistics and stand-to-stand agreement

Production calibration is a heavily statistical activity: gauge repeatability and reproducibility studies are run on test stands, stands are recalibrated on a schedule, and all results are tied back to a single traceable reference so that a stand going out of calibration can be detected.[236] Statistical process control on a calibration line tracks each test stand against the others, because two stands calibrating the same 10 mV range to the same nominal accuracy can sit offset from one another by a fraction of a percent.[377] Because production test enforces a hard pass-fail limit, a unit sitting marginally outside the limit on one rig can pass on another rig whose offset runs the other way, which is why stand-to-stand agreement must be monitored rather than assumed.[377]

Using previous-generation instruments to calibrate the next generation risks generational degradation, in which each batch inherits and compounds the error of the units that calibrated it; the fix is to keep a traceable calibrated multimeter in series in the test fixture so every generation is referenced to the same external standard.[640]

Component tolerance errors surface directly in calibration yield. A shipment of resistors supplied at 1 percent tolerance in place of the specified 0.1 percent produced roughly a 50 percent failure rate in production test; a tolerance error large enough to move yield that far is obvious, whereas a 5 percent shift could be written off as noise.[182]

### Contract manufacturing

Calibration and functional test of a precision instrument require expensive equipment that a normal contract manufacturer does not have, so the instrument maker must supply the test stand and the contractor is chosen partly for its willingness to host it.[607] A precision instrument whose factory test flow includes touchy calibration stages likewise constrains contractor selection, favouring a nearby shop with a consistently skilled operator over a cheaper or more distant one.[527] Established instrument manufacturers instead run calibration in a temperature-controlled room staffed by dedicated calibration technicians who put each unit through its full cycle, an environment that is not normally available at a contract manufacturer.[527] In test and measurement generally, the barriers protecting incumbents are bespoke supply chains for precision components and test methodologies that competitors are unwilling or unable to reproduce, including the ability to calibrate to a recognised standard.[682]

## Radio-frequency and microwave calibration

A vector network analyser calibration works by measuring artifacts whose true values are known and correcting the readings to match; resolving impedance requires three known standards, conventionally an open, a short and a load.[533] Practical open and short standards are physically offset from the reference plane, so an uncorrected trace traces an arc rather than collapsing to a point; naming them simply open and short rather than offset open and offset short has been a lasting source of user confusion.[533] Where a component's behaviour is not repeatable, it is characterised over temperature so the correct correction factor can be selected for the temperature at which the measurement is made.[533] Test cables stretch and shrink as they heat and cool, and because the measurement depends on propagation time, that dimensional change moves the measured phase; calibration removes the error as long as the cable state stays constant afterwards.[533]

Connector handling is part of the calibration. High-frequency RF connectors must be tightened with a torque wrench, because an incorrectly torqued connector invalidates the calibration and can shift the measurement by a decibel or two.[496] Standard SMA connectors are unsuitable for measurements at 10 GHz and above, and specialised precision connectors are used instead.[496]

Calibrating is not the first step in a network analyser measurement, despite being the answer most users give; modern analysers have been pre-calibrated at the factory well enough that useful first measurements can be made before any user calibration.[533] The recommended sequence is to connect the device and take the measurement uncalibrated first, sanity-check the result for obvious errors such as a part hooked up backwards, adjust cables, connectors and adapters and wiggle the part to confirm stability, and only then spend time calibrating.[533]

At scale the procedure is automated. Testing a 64-element base-station antenna array requires 64 cables to blind-mate connectors and 64 separate calibrations performed at the end of each cable, which is handled by a robot that attaches the open, short and load standards in turn.[533]

In a distributed sensor company, the systems integration site handles over-the-air and chip test, calibration and basic performance characterisation against spherical and canonical radar targets and first-principles physics, while a separate software site tests the same hardware against customer-facing performance metrics.[729]

## Self-calibration in the field

CMOS used in space is not radiation hard, so spacecraft systems-on-chip embed sensors that monitor bias, voltage and current conditions and detect when radiation has shifted the circuit away from its characterised operating point.[483] A space-grade RF synthesiser can carry hundreds of adjustment knobs — clock phase, bias conditions, clock and VCO tuning, output stage trim and output match — plus an integrated subprocessor that runs a calibration routine whenever a monitored parameter leaves its allowed corridor.[483] Extreme temperature excursions shift the operating point of spacecraft electronics in the same way radiation does, so on-board calibration must cover the thermal range as well as radiation-induced drift.[483]

Bench instruments are specified with a warm-up time before their accuracy claims hold, an assumption that fails for field instruments, which are used at arbitrary times and temperatures and must therefore tolerate a wider range of operating conditions.[218] Where field units receive firmware updates that affect their behaviour, over-the-air updates to a large fleet are staged rather than pushed at once, typically seeding roughly 0.1 percent of units first, then 1 percent, then 10 percent, so that a bad image is caught before it reaches the whole population.[363]

## Calibration of machines and positioning

A pick-and-place machine needs a machine-specific component library and calibration data for each component type, not just X-Y placement coordinates, because the head is a robot whose pick and placement behaviour depends on the part geometry.[411] Introducing a component the assembly line has not run before remains a manual step, requiring an engineer to look up the datasheet and determine the part's physical dimensions before the machine can handle it.[411] Even with the nozzle position calibrated exactly, reliable picking from tape depends on separately tuned parameters — how long the nozzle lingers on the part, how much suction is applied, and when vacuum is released — and these must be dialled in for each component type.[419] An open-source pick-and-place ships with as much machine configuration as possible baked into the firmware at boot, leaving the user a guided calibration walkthrough supported by video tutorials, because the number of adjustable settings on such a machine is otherwise overwhelming.[686]

Positioning stages have their own calibration discipline. When a table has mechanical slop, every move must approach the target from the same side in X and Y so that backlash contributes a constant rather than a variable error; the amount of slop can be measured at different points of travel and compensated.[390] In a home-built lithography stepper, focus is calibrated by pre-scoring the wafers with a laser cutter to give true indexing edges, focusing at each side of the wafer, and fitting the focus variation as a line in three-dimensional space that the computer then applies across the wafer.[390]

## Calibration gaps in application

A common class of reported field failure is not a defective part but a calibration gap in the application: the device shows an offset or gain error of a few least-significant bits that is inside its published specification, while the customer's calibration scheme does not compensate for it.[485] The most common cause of returned parts reported as defective is crystal oscillator startup failure traced to incorrect load capacitors on the crystal, which is a board design error rather than a silicon fault.[485]

Interface choices can add unrelated burdens to an instrument programme. USB 3.0 host implementations proved far less uniform across computers than USB 2.0, so instrument products relying on USB 3.0 face host-compatibility work in addition to their own analogue and calibration software problems.[237]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 72 | Kismetic Keithley Katowse | https://theamphour.com/the-amp-hour-72-kismetic-keithley-katowse/ |  |
| 94 | Gnomic Gazumping Gobemouche | https://theamphour.com/the-amp-hour-94-gnomic-gazumping-gobemouche/ | May 6, 2012 |
| 132 | Melbourne, Hackerspace & Calibration - Vacuuous Vortex Verification | https://theamphour.com/the-amp-hour-132-vacuuous-vortex-verification/ | February 11, 2013 |
| 146 | Hamvention, Arduino and Intel - Burdensome Background Battology | https://theamphour.com/the-amp-hour-146-burdensome-background-battology/ | May 21, 2013 |
| 147 | An interview with Jeri Ellsworth - Absorptive Augmented Actuality | https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/ | May 27, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 182 | Manufacturing By Wire And Skipping Testing - Calefacient Cuculine Cash | https://theamphour.com/182-manufacturing-by-wire-and-skipping-testing-calefacient-cuculine-cash/ | January 27, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 369 | An Interview with Jason Huggins | https://theamphour.com/369-an-interview-with-jason-huggins/ | November 26, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ | April 29, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 419 | Feels over reals | https://theamphour.com/419-feels-over-reals/ | December 9, 2018 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 483 | An Interview with Adrian Tang | https://theamphour.com/483-an-interview-with-adrian-tang/ |  |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 496 | Drab Olive | https://theamphour.com/496-drab-olive/ | June 14, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 533 | Microwave measurement with Joel Dunsmore | https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/ | March 7, 2021 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 729 | The Terahertz Frontier with Greg Charvat of Teradar | https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/ | July 22, 2026 |
