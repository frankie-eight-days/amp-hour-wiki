---
title: Reference Design
concept: reference-design
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A **reference design** is a complete, published circuit or system design, typically produced by a component vendor, that is intended to be copied directly into a customer's product.[41][216] Reference designs are free to use and carry no attribution requirement, a legal position distinct from most published engineering work.[41] They function simultaneously as technical documentation, as a sales mechanism for the vendor's entire catalogue, and as an informal standard around which whole product categories form.[216][231]

## Legal and licensing status

Reference designs are published specifically to be copied verbatim, without fees or attribution requirements.[41] Application notes and application circuits have been effectively open for as long as the semiconductor industry has existed; their entire function is to be lifted into someone else's design, and this practice predates any formal open licensing framework.[216]

The terminology itself carries legal weight. Calling a design a "reference design" implies that it was validated for a purpose, which creates liability exposure if a customer copies it exactly and it fails in their application.[723] On the BeagleBoard programme, Jason Kridner addressed this by stating explicitly that the published design was not validated for any purpose whatsoever, while still releasing the full documentation so that users could validate it for their own purposes; the material remains just as useful with the guarantee removed.[723]

## Vendor economics

The vendor's motive for encouraging verbatim copying is that the circuit is built entirely from its own catalogue — the regulator, the switching circuit, and the discrete devices — so a copied design sells the whole bill of materials rather than a single part.[216] Inside semiconductor vendors, applications engineers are frequently the people actually performing the design work that becomes the published reference, and a large share of the industry's circuit design happens in that function rather than at the customer.[231] Vendor support can be granular: in robotics, a supplier may offer a device and a matching reference design for every individual joint of a robot, each with an available demonstration board.[719]

Because vendors give reference designs away, a paid marketplace for reusable design blocks cannot compete; attaching even a small transactional cost stops engineers from using a block at all.[163] Reference status can also be a commercial lever in the other direction: on Adapteva's open-source board, Andreas Olofsson found that once the board functioned as a reference design for the chips on it, the suppliers of those chips had a reason to improve their pricing that had not existed before.[254]

## Prevalence in product development

Reliance on reference designs in consumer products is extensive. A widely quoted figure holds that sixty to eighty percent of mobile phone designs are essentially unmodified vendor reference designs, though the figure is flagged as unverified even by those citing it; it matches what practitioners observe.[216] The same pattern holds in consumer networking, where products are largely the networking chip's reference circuit repackaged, with the vendor absorbing the research and development cost and the product company contributing the enclosure and the brand.[363] An entire product category can amount to one part plus its reference design: a common Bluetooth speaker is built on a roughly one-dollar part carrying microphone input, converters in both directions, signal processing, battery charging, and the radio, so that the product is effectively the reference design itself.[351] When a platform owner gives away the software for a device category, the barrier to entry collapses further — anyone can obtain a reference design and build the product with near-zero startup cost, and margins across the category fall accordingly.[327]

Reference designs also shape part selection well beyond their own circuit. Components are specified into unrelated products simply because that is what the reference design used, which is one mechanism by which a particular interface chip becomes ubiquitous.[587]

## Use in engineering practice

Reference designs matter most in two cases: parts that require firmware to be written for them, and very high-performance parts where layout dominates the result; elsewhere a datasheet may be sufficient.[270] When a customer reports poor performance, the vendor's first diagnostic question is whether the reference design was followed, in the same reflexive way that computer support asks whether a machine has been switched off and on.[270] The reference board also allocates responsibility: it demonstrates the performance the part is capable of, and establishes that departing from the published layout is the customer's own decision, with the resulting performance the customer's own problem.[270]

The numbers behind layout sensitivity explain why a reference layout is not advisory. An audio system with 115 to 130 dB of dynamic range at one volt RMS output has a noise floor in the low nanovolts, so routing an amplifier's ground current past the converter lifts the ground reference and can consume the entire noise budget.[270]

When a proven reference circuit fails to work in a new design, the default assumption is that the implementer did something wrong rather than that the published geometry needs adjusting; a design that has worked repeatedly is evidence about the board, not about the design.[631] The checklist that follows is specific: wrong dielectric, other components placed too close, or the wrong impedance on the feeding trace — each a deviation from the reference conditions rather than a flaw in the reference.[631]

For an unfamiliar integrated circuit, the standard first step is to read the reference schematics and work through them part by part, considering how each piece would be realised in one's own design.[573] The learning argument for this approach parallels music: the existing forms are learned before they are modified, and following the example through to the end, including the parts that go wrong, is where the understanding comes from.[573] Choosing among reference designs is itself a design decision, since a datasheet frequently contains six or seven distinct ones rather than a single circuit.[360]

Vendor layout guidance can also be consumed by tooling: a recommended layout for a sensitive block such as a switching regulator can be copied into a design as a fixed region, marked untouchable so that automated routing tools work around it rather than through it.[626]

## Limitations and failure modes

The fundamental limitation of any reference design is scope: it shows how to make one device work well, but what distinguishes the strongest designers is global knowledge of the whole signal chain — asking in turn how every other part of the system interferes with each circuit until the whole board has been considered.[270]

A well-supported reference library measurably changes outcomes, and the standard it should be judged against is customers reaching mass production on their first board spin, including designs carrying wireless.[202] The counterweight is that a good reference kit is persuasive in a way that has nothing to do with whether the part is the right long-term choice; Dave Jones recounted being taken in by a good reference kit, a failure recognised among experienced engineers rather than only beginners.[271]

Designing around one chip also pulls in the vendor's other parts: the engineer ends up sourcing each surrounding reference design, dropping it into the schematic, and tweaking it, becoming the designer of all of them rather than only the one originally wanted.[163] The proposed remedy is to place a whole reference design into a schematic the way a chip is placed, treating it as a reusable block.[163] The claim for such reuse has to be stated carefully: what it delivers is a prototype to work with sooner, not a finished product out the door sooner, and conflating the two oversells it.[163]

Security is a recurring failure mode in software-heavy reference material. Vendor example code carries explicit warnings against production use because security features are disabled to keep the example simple, yet it is copied into shipping products anyway.[363] The situation is often worse than a disabled feature: vendor-supplied software can be unstable and carry its own defects, and product schedules are tight enough that those defects may never be found before the device ships.[363]

## Economics of reuse

For low-volume products, a reference design can justify expensive parts: paying a few hundred dollars for a device usable straight from the published circuit beats spending engineering time optimising toward a cheaper part when the volume will never repay the effort.[64] Buying a proven module is effectively buying somebody else's reference design together with the community around it; memory training between a processor and its memory is very hard to debug without the right tools, and avoiding that class of problem is what the module premium purchases.[681] For anyone without the budget for full custom silicon, the sensible route is to start from an existing reference design and customise the ordinary functions around the chip or the firmware on top of it, gaining real flexibility without a custom tape-out.[499]

## Reference designs outside the semiconductor vendor

The reference-design model extends beyond chip vendors. For consultants, client work cannot be reused, so the hours produce no reusable asset; a self-funded reference design both attracts clients and becomes the basis for later work.[470] Stated as a business strategy, the mechanism is to put projects into the world so that someone eventually arrives asking for something that looks like one of them, at which point the answer is that this is exactly what the consultant does.[492] A concrete version of the strategy is to develop and properly test the hardware and firmware, ship a standard version to the general market, and take customisation work from customers who need a different size or feature set.[492] The failure mode of a portfolio reference design is leaving the system context for later: one board showcased the hardware competently but was unfinished as a product because the software and networking topology were deferred, and the radio chosen never suited the intended architecture.[587]

Open projects can be conceived as references from the start. Publishing everything — schematics, board files, bill of materials, and the software development kit — lets a general-purpose design serve as a reference for the specific variants others build from it, which is the point of a generic node rather than a side effect.[557] The Jubilee motion platform was conceived from the outset as a reference rather than a product, capturing current best practices for precision motion so that anyone who wants the capability can build one without designing it themselves.[611] Publishing a reference design for a difficult board has effects nobody plans for: on the BeagleBoard project, Jeff Keyzer observed assembly houses downloading the artwork and building the board themselves, which levelled the field between them and produced uses of the design that were never anticipated.[59]

The number of reference designs a platform blesses is a strategic decision rather than a technical one: a single common reference design produces a coherent ecosystem, while several incompatible ones sharing only a software interface fragment it.[43]

## Automated generation and derivative uses

Two approaches to generating schematics automatically trade generality against assurance. Parsing datasheets can generate almost anything but risks interpretation errors; assembling predefined manufacturer blocks known to work can only generate specific things but moves the remaining risk to how the blocks are connected.[718] Existing board designs also find unexpected uses, for instance as the starting point for learning visualisation: importing a real project gives the learner something concrete to work with immediately rather than modelling an object from nothing.[695]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 41 | Contests, Ham Radio & TWIT.tv - Ham, Spam, Thank You Ma'am | https://theamphour.com/ham-spam-thank-you-maam/ | May 4, 2011 |
| 43 | An Interview with Jeff Keyzer and Jeremy Blum - Audacious Arduino Arguments | https://theamphour.com/the-amp-hour-43-audacious-arduino-arguments/ | |
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ | |
| 64 | OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster | https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/ | |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15, 2014 |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ | January 6, 2015 |
| 254 | An Interview with Andreas Olofsson - Adapteva's Ampliative Abacus | https://theamphour.com/254-an-interview-with-andreas-olofsson-adaptevas-ampliative-abacus/ | June 16, 2015 |
| 270 | An Interview With Dafydd Roche | https://theamphour.com/270-an-interview-with-dafydd-roche/ | October 7, 2015 |
| 271 | Amazon Moves In, Dave Says Run | https://theamphour.com/271-amazon-moves-in-dave-says-run/ | October 14, 2015 |
| 327 | An Interview with Avidan Ross | https://theamphour.com/327-an-interview-with-avidan-ross/ | December 14, 2016 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 360 | A Total 360 | https://theamphour.com/360-a-total-360/ | September 18, 2017 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 470 | Just Add Salt | https://theamphour.com/470-just-add-salt/ | December 8, 2019 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ | |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 611 | Grad School Time Capsule with Joshua and Zach | https://theamphour.com/611-grad-school-time-capsule-with-joshua-and-zach/ | December 4, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 695 | Making The Invisible, Visible with Sam Aldhaher | https://theamphour.com/695-making-the-invisible-visible-with-sam-aldahar/ | June 3, 2025 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
| 719 | Inventing the Power MOSFET with Alex Lidow | https://theamphour.com/719-inventing-the-power-mosfet-with-alex-lidow/ | March 20, 2026 |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ | May 7, 2026 |
