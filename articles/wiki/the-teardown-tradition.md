---
title: The Teardown Tradition
concept: the-teardown-tradition
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A teardown is the systematic disassembly and inspection of a finished product in order to recover how it was designed, built and costed.[353] The practice rests on the premise that nothing inside a manufactured product is inexplicable: every product opened is the output of a team of engineers working over a period of years, so each visible choice had a reason behind it that can in principle be recovered.[102] Taking gear apart and studying how it was designed and constructed is treated as part of an engineer's ordinary learning process rather than an optional curiosity, and has been formalised as university teaching material as well as practised informally.[353][116] Commercial teardown-analysis services such as iSuppli exist as an industry in their own right, selling structured breakdowns of competitors' products.[31]

## Method

### Opening the enclosure

Opening a clipped consumer enclosure is done incrementally with a knife, popping one clip at a time on the assumption that the process is still reversible; the commitment to a full teardown accumulates clip by clip rather than being decided at the start.[7] That assumption does not always hold. Enclosures closed by heat welding or ultrasonic welding make a teardown one-way, since the case cannot be reassembled afterwards, which is why densely integrated consumer devices are often left intact rather than opened.[301] Potted assemblies defeat the exercise entirely, since the compound cannot be removed without destroying what it encases, so potting is an effective barrier to inspection as well as to moisture.[482]

Electrostatic discharge discipline during a teardown is commonly reduced to an antistatic mat, with a wrist strap used only when a board is judged to warrant it, on the reasoning that ordinary careful handling of a finished product is itself a fair test of how robust that product is.[45]

### Reading the board

Part-number lookup is the bottleneck at the bench: without a datasheet-capable screen beside the work, the practitioner shuttles to a desk machine for each unknown part and loses the several specifications just memorised on the way back.[126] Visual inspection alone will not settle what a board contains, because parts and structures hidden under packages or inside the stack-up require X-ray to see.[460]

Some parts cannot be identified at all. Older instruments are commonly built around parts carrying a manufacturer's internal number rather than a catalogue number, so no datasheet exists to be found; in a teardown of a Tektronix TDS 220 the custom National Semiconductor part yielded at best a block diagram, and the practical ceiling on such investigation is identifying the standard part the custom device was derived from and working from that.[227] An unidentifiable part — a chip-on-board epoxy blob over bare silicon, or a device carrying a house label — can still be characterised without ever being named, by intercepting the serial traffic between it and the parts around it and then spoofing that traffic to exercise the function it controls.[178] The same approach serves reverse engineering without firmware extraction: tapping the bus between a microcontroller and a radio chip reveals the protocol, after which a substitute microcontroller can be connected to the same radio chip and made to drive it.[363]

A teardown can also be continued past the board to the die, since chemical decapsulation of a package yields die photographs, a level of detail below the board-level inspection at which most teardowns stop.[406]

### What counts as a result

How much there is to say about a board is set by how many separately partitioned functional blocks the design contains: a high-performance radio front end presented twenty-five distinct blocks to walk through, where an oscilloscope teardown offers nothing like that number.[304] A teardown that contains no surprises is still a valid result — confirming that a product holds exactly what its function implies, and no more, is an outcome rather than a failed investigation.[150] Conversely, the exercise regularly overturns expectations: a consumer tracking tag that appears functionally trivial proved to have a comparatively complex board and two separate printed circuit boards inside.[690]

A teardown teaches how an existing design was solved, but the subtle design considerations only become visible when the same thing is implemented, and that implementation stage routinely takes two to ten times longer than first estimated.[485]

## What construction reveals

Board count alone tells a reader where a product sits: finding more than one circuit board inside a toy is itself the signal that the design was pushed far beyond the norms of its category.[349] A promotional toy sold at three hundred dollars carried six motors, a miniature LCD behind the character's eyes and Bluetooth control throughout, which is the content that puts such a product outside the toy category on cost.[349]

Interconnect choices are equally legible. The connector-versus-hardwire decision is one of the oldest in product design: soldered-in cables save connector cost but force desoldering before boards can be separated for service or inspection, and a product that mixes proper board-to-board interconnect with hardwired links in the same assembly indicates the decision was not made consistently.[534] Smartphone internals are dominated by flexible circuits terminated in very low-profile board-to-board connectors that snap together, which is the interconnect style a teardown of any modern handset will encounter.[708]

Volume allocation in a flagship phone is a fixed pattern. The device is built as a screen layer and a single layer of everything else, and within that layer the battery accounts for roughly sixty percent of the volume, the dominant constraint on what else can be fitted.[367] Of the remainder, roughly thirty percent is circuit board and roughly ten percent is camera modules carried on flexible boards, with rigid-flex construction used where a single part must be partly board and partly flex.[367] Opening a phone also shows how much of it is custom in the mechanical domain rather than the electrical one: custom plastics and tooling are comparatively accessible, whereas taking a chip custom means going the whole way through the semiconductor process, which is why bespoke mechanics appear long before bespoke silicon does.[502]

A teardown can expose an omitted process step rather than a bad part: one product was found to have no conformal coating at all, and an owner hardened his own unit by applying conformal coating inside it after seeing the bare boards.[362] Vendor concentration is revealed directly — an Agilent U1272A handheld meter was found to use a large number of Maxim parts, showing which supplier had won the analogue content of the design.[44]

Across products opened week after week, nothing fundamental about how electronics is made has changed: boards are still laid out on fibreglass laminate, components are still soldered to them, catalogue parts are still bought through distributors, and only the size and capability of the parts have moved.[240]

## Cost analysis

A cost-driven teardown proceeds chip by chip across the board with the cost of each part added up, and the exercise is informative precisely because a precision instrument is obliged to use precision parts to meet its published specifications.[460] A retail price far below what the visible content should cost is itself a reason to open a product: an e-book reader sold boxed at retail for thirty Australian dollars carried a seven-inch colour TFT screen.[100]

Published cost estimates have known limits. They account only for the major chips and give no reliable figure for what a product costs to make; a real cost requires assembly, transportation, warehousing and the rest of the vertically integrated manufacturing chain to be added.[502] Third-party analysis put the bill of materials of a 199 US dollar Kindle at around 203 dollars, implying the hardware was sold below cost.[70] Such estimates systematically understate a large buyer's position, because a manufacturer forecasting sales of eight million units within four months commits to and pays for that volume of parts up front, at prices a per-unit teardown estimate cannot see.[70]

Where the low price comes from is sometimes a matter of silicon economics rather than corner-cutting. What separates a low-cost oscilloscope built by a large instrument maker from one built by a smaller competitor is custom ASIC development: the smaller firms lack the research budget to develop such chips, and once the development cost has been paid the chip itself costs only a few dollars per unit, which is what enables the low selling price.[30] Agilent's low-end oscilloscopes were formerly rebadged Rigol instruments before the company brought design and manufacture of that range back in house.[30]

## Judging cost-down and claims

The specific test applied when judging cost-cutting is derated headroom rather than brand: capacitors rated 200 volts on a 300-volt bus are a legitimate fault to call out, whereas 600-volt parts in sufficient number on the same bus are sound engineering even when the brand is unfamiliar.[671] Marketing claims about component quality are checkable by this method and do not always survive it: one inverter shipped with a glossy brochure devoting a full page to its use of named premium components, including Nippon Chemi-Con capacitors and Panasonic relays, and none of those parts were present in the unit.[671]

Anonymity is sometimes deliberate. An instrument bought for 8.70 US dollars with free shipping met its published specifications and looked acceptable inside, but carried no manufacturer name at all: the name and model number had been physically abraded off the product.[460]

Publishing a debunking teardown carries legal exposure. A forum member who bought a fuel-saver device, reverse-engineered its schematic and showed that it could not work was threatened with a lawsuit by the company selling it, with demands for damages and removal of the material, though nothing came of the threat.[55]

## Related uses

Withholding a schematic protects very little when the part numbers on the board are legible, because the schematic can be reverse-engineered from the physical product in about a day; this is the argument for publishing the schematic while keeping the firmware source closed.[298] Regulatory compliance filings are a further public source of internal photographs, since a radio product must be submitted for certification before it can be sold, and the filings routinely include device and internal views that amount to a teardown published ahead of launch.[391]

Teardown is also a route to reviving obsolete capital equipment rather than only to inspecting it: a Phantom V4 high-speed camera dating from the early 2000s was torn down and returned to working order.[325] Large end-of-life office equipment such as a colour laser printer is torn down as a parts-harvesting exercise as much as an inspection one, the object being to establish which mechanisms and assemblies inside are worth salvaging.[490] Harvested parts accumulate into a specific storage problem: items too large or too low in value to sell individually but plainly useful to someone, which practitioners clear in bulk at swap meets rather than piece by piece.[412]

Systematically opening consumer products is a route into identifying which silicon platforms serve ultra-low-cost designs, and pairs with keeping public written notes, because the knowledge is otherwise held only in the practitioner's head.[661]

## Teaching

Teardown has been used as formal teaching material rather than only as informal practice: Kent Lundberg ran a class built on tearing down products such as guitar pedals.[328] It has also been run as the spine of an electrical engineering prototyping course, on the reasoning that one would not design a bridge without first studying how bridges are built.[116]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 7 | Love Robots and Pantyhose Screens | https://theamphour.com/the-amp-hour-7-love-robots-and-pantyhose-screens/ | |
| 30 | Agilent, Analog, Cold Fusion - Funding Fusion Is Not Futile | https://theamphour.com/the-amp-hour-30-funding-fusion-is-not-futile/ | |
| 31 | Freescale, Hackerspaces, Printable Electronics - Publish Popular Parts Please! | https://theamphour.com/the-amp-hour-31-publish-popular-parts-please/ | |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 45 | Texas Instruments, OPA & Chevy Volt - Nerdy Neuroelectronic Neurosis | https://theamphour.com/the-amp-hour-45-nerdy-neuroelectronic-neurosis/ | May 30, 2011 |
| 55 | Shonky Stiver Stultiloquence | https://theamphour.com/the-amp-hour-55-shonky-stiver-stultiloquence/ | |
| 70 | Idiorhythmic IPC Inconcinnity | https://theamphour.com/the-amp-hour-70-idiorhythmic-ipc-inconcinnity/ | |
| 100 | Bonkers Birthday Badinage | https://theamphour.com/the-amp-hour-100-bonkers-birthday-badinage/ | June 17, 2012 |
| 102 | Gouging Green Gardyloo | https://theamphour.com/the-amp-hour-102-gouging-green-gardyloo/ | July 1, 2012 |
| 116 | Distribution, Wozniak & Robots - Early Eight-bit Endgame | https://theamphour.com/the-amp-hour-116-early-eight-bit-endgame/ | October 7, 2012 |
| 126 | eReaders, datasheets & board assembly - Yearly Yeasty Yapping | https://theamphour.com/the-amp-hour-126-yearly-yeasty-yapping/ | December 17, 2012 |
| 150 | Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness | https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/ | June 17, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 227 | Space Bound, Again - Xtreme Xtraplanetary Xenonosocomiophobia | https://theamphour.com/227-space-bound-again-xtreme-xtraplanetary-xenonosocomiophobia/ | December 8, 2014 |
| 240 | Compare and Contrast Tech Entitlement - Worldly Working Wonks | https://theamphour.com/240-compare-and-contrast-tech-entitlement-worldly-working-wonks/ | March 10, 2015 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11, 2016 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 304 | Alexa joins the fray | https://theamphour.com/304-alexa-joins-the-fray/ | June 22, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 328 | The Ghost of Keyzermas Past | https://theamphour.com/328-the-ghost-of-keyzermas-past/ | December 21, 2016 |
| 349 | An(other) Interview with Jon Oxer | https://theamphour.com/349-another-interview-with-jon-oxer/ | June 25, 2017 |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 460 | Rubber Ducking | https://theamphour.com/460-rubber-ducking/ | September 29, 2019 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 671 | NDA Sideshow | https://theamphour.com/671-nda-sideshow/ | June 19, 2024 |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11, 2025 |
| 708 | All the Connectors with Davide Andrea | https://theamphour.com/708-all-the-connectors-with-davide-andrea/ | November 1, 2025 |
