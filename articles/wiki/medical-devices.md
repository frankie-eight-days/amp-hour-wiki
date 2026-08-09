---
title: Medical Device Development
concept: medical-devices
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Medical device development is electronics and software engineering carried out under the supervision of a health regulator, principally the Food and Drug Administration in the United States and the Medicines and Healthcare products Regulatory Agency in the United Kingdom.[588][549] The regulator does not prescribe which components or technologies a device must use; it prescribes the diligence the manufacturer must perform and document to demonstrate that the device is safe, which makes regulated design resemble an audited quality process more than a technical rulebook.[588] The practical effect is that regulatory work, rather than design work, becomes the dominant consumer of an engineer's schedule, and the final portion of a programme — the approval and completion work rather than the innovation — determines whether the device can be used in a healthcare setting at all.[218][711]

## The regulatory mechanism

The FDA independently audits medical device and medical instrumentation companies, and the design process itself must be arranged so that it produces evidence of the diligence performed, not merely a working device.[588] Scrutiny is directed at the manufacturer's implementation rather than at component specifications: the questions asked are whether a part was implemented correctly, and whether it was used in the conditions under which its data sheet was characterised.[588] Most of the back-and-forth with a regulator comes from submitting against requirements that were never read carefully; establishing exactly what the submission must show before writing it removes those cycles.[549]

Regulatory burden attaches to the clinical claim rather than to the measurement technique. An instrument using an identical bio-impedance spectroscopy method escapes the approval process as long as it does not assert a diagnosis, and a wearable that monitors a patient without being invasive and without claiming to diagnose can reach market without FDA testing.[448][331] Turning the same measurement technique into an approved diagnostic requires clinical trial data and an algorithm built over that data to establish accuracy, followed by FDA clearance or a CE mark; the underlying technique is the small part of that work.[448] The applicable regulatory class is therefore itself a schedule variable: a UK exemption that removed most of the applicable regulations from a device materially shortened its development timeline.[549] Medical products aimed at consumers nonetheless remain FDA regulated, and the regulatory work stays a significant part of the business even when the device is not a clinical instrument.[402]

## Safety requirements

Failing safe means different things by industry. A test instrument may fail safe by carbonising inside its own case, but a medical device that fails must actively warn the user that care has been interrupted rather than simply stopping.[218] Class II medical devices are fail-safe devices: any single component in the circuit may be faulted in any way, and the requirement is not that care continues but that the device stops delivering care safely.[218] Safety qualification includes a dielectric withstand test of 5,400 volts AC RMS, roughly 7,600 volts peak, applied across the housing, in addition to the impulse tests used on measurement equipment.[218]

Safety-critical systems under FDA, FAA or space rules favour an external watchdog paired with a voltage supervisor over an on-chip one, because an external device cannot be disabled by the processor's own software and fires regardless of firmware state.[281] EMC competence does not transfer across industries: a medical device and a consumer device are governed by different regulations, different limits and different import and export rules, so EMC expertise is held in narrow per-sector niches rather than as a general skill.[229]

## Software and firmware

In medical devices the software and full stack are certified together, so a firmware update cannot be rolled out without recertification; that makes routine security patching impractical and forces the security design toward a locked, cryptographically verified bootloader established before certification.[318] Qualification, not development, sets the release cadence: a one-line code change requires the full qualification process, which on one large device took three months per release.[489] Certified medical software must have every line of code reviewed, and the industry rule of thumb prices that review at about one dollar per line, so ten thousand lines of code carries roughly ten thousand dollars of review cost.[486]

Medical device software must meet the applicable IEC and ISO safety standards along with coding standards such as MISRA-C. General mainline Linux carries none of that evidence, so a safety-critical Linux system must be built on a commercial distribution from a vendor such as Wind River that supplies the certification package.[515] The classification of source code also shapes hardware design entry: in regulated markets including medical, source code falls under stricter verification rules than schematics, so FPGA designs were entered as schematics that generate HDL in order to keep the design out of the source-code regime.[181]

Development process failures in this area are characteristic. A medical device programme that repeatedly failed and drew an FDA investigation was found to have no design phase at all: a domain expert wrote and adjusted code experimentally until behaviour looked right, and the result was then frozen. The underlying error is conflating research with development, which have different processes and different exit criteria.[489]

## Component selection and traceability

Medical design is deliberately conservative in component selection: the newest part is usually not the chosen part, because the evidence burden favours devices with established behaviour.[588] Because every revision, down to changes in code, requires approval and extensive documentation, technology fielded in regulated medical products lags the state of the art considerably.[151] Since every change reopens the approval burden, companies change nothing unless forced to, and the practical consequence is that engineers on mature medical products spend their time on obsolescence management — six months of work to qualify a replacement for a single discontinued transistor.[486]

This conservatism supports a distinct segment of the semiconductor industry. Some makers run a deliberate business model of not advancing process nodes, serving medical and automotive customers from older equipment and 8-inch rather than 12-inch wafers, because those parts do not need billions of transistors and their customers value continuity.[297]

Component lot control and build traceability, optional elsewhere, are a legal requirement when building medical devices, so the build system must record which specific ordered lot supplied each part in each unit.[542] For a US medical startup those obligations begin at the start of design rather than at market entry, because the first prototype may itself be tested or form part of the FDA evaluation; startups that discover this late must reconstruct the paperwork retrospectively.[542]

## Programme structure and testing

A regulated hardware startup must stand up product lifecycle management and a quality management system alongside external design review and compliance testing, infrastructure that unregulated startups never build.[295] Where a device can kill its user, the prototype being developed is not the product that ships: several rounds of external design review and full regulatory approval sit between them, and that gap has to be planned into the schedule.[295] Medical clients commonly route documentation, integration testing and design records through a specialist regulatory firm that reviews and returns them until the format matches what the FDA submission requires.[492]

Debugging on such a programme is usually driven by the regulatory test house's report rather than by discovery at the bench: the compliance failures become the lab data the team works from, and board turns are planned as remedial actions against that report.[704] Design for test therefore has to account for regulatory testing itself — burying an antenna on the far side of the PCB left no way to attach a BNC for compliance measurement without physically drilling into the finished product.[549]

## Industry structure

Medical device volumes span a wide range and include electronic products built at a million units a year, so medical work is not inherently low volume.[330] Minneapolis is a concentration point for the industry, hosting Medtronic, St. Jude Medical and Boston Scientific, and local contract manufacturers are correspondingly oriented toward medical work.[330]

Work also occurs deliberately outside the regulated path. Jean Rintoul, after more than a decade in biosensor wearables, judged the regulatory path — though necessary — to be the binding constraint on bioelectronics innovation, and built an open-source research instrument outside that path rather than through it.[448] Reworking an established clinical instrument for low-resource settings meant adding two constraints to a known design: cost, and the removal of the trained specialist from the interpretation step, which was solved by moving classification to a machine learning model running on a phone fed over Bluetooth.[711]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 151 | Google Glass, Lean Startup and VotC - Initializing Instructed Interviews | https://theamphour.com/the-amp-hour-151-initializing-instructed-interviews/ | June 24, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ | |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 281 | Crossovers and Call-ins | https://theamphour.com/281-crossovers-and-call-ins/ | January 6, 2016 |
| 295 | An Interview with Omer Kilic | https://theamphour.com/295-an-interview-with-omer-kilic/ | April 20, 2016 |
| 297 | An Interview with Jake Baker | https://theamphour.com/297-an-interview-with-jake-baker/ | May 4, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 331 | An Interview with Simone Giertz | https://theamphour.com/331-an-interview-with-simone-giertz/ | January 11, 2017 |
| 402 | An Interview with Ben Einstein | https://theamphour.com/402-an-interview-with-ben-einstein/ | August 6, 2018 |
| 448 | An Interview with Jean Rintoul | https://theamphour.com/448-an-interview-with-jean-rintoul/ | June 23, 2019 |
| 486 | Medical Kits, They're The Future | https://theamphour.com/486-medical-kits-theyre-the-future/ | March 29, 2020 |
| 489 | An Interview with Jack Ganssle (2nd) | https://theamphour.com/489-an-interview-with-jack-ganssle-2nd/ | April 19, 2020 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 542 | Component Management with Jan Rychter | https://theamphour.com/542-component-management-with-jan-rychter/ | May 17, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 588 | Siloed Engineering with Leigh Brady | https://theamphour.com/588-siloed-engineering-with-leigh-brady/ | May 8, 2022 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 711 | Medical Electronics Education with Mark Palmeri | https://theamphour.com/711-medical-electronics-education-with-mark-palmeri/ | December 21, 2025 |
