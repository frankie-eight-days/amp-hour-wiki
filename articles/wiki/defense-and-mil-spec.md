---
title: Defense and Mil-Spec Work
concept: defense-and-mil-spec
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Defence and mil-spec work is electronics design carried out under military procurement rules, where the binding constraints are contractual service life, documentation and export control rather than unit cost or schedule.[1][322][186] A defence programme typically obliges the supplier to support the product for ten to fifteen years, which converts component selection from an engineering decision into a compliance decision and creates a permanent secondary market in obsolete parts.[1][322][567] The regulatory load is comparable to that of medical device work and extends to test engineering as much as to design.[288] Cost is not a design variable in the usual sense: the engineer's obligation is to meet the stated performance whatever the bill of materials costs.[211][255]

## Product life and component supply

Military contracts commonly require a supplier to support a product for ten to fifteen years, which forces the designer to obtain written statements from component vendors committing to supply the part over that horizon; such statements are difficult to extract.[1][7] Where a customer demands five to ten years of product support, parts with uncertain supply lifetimes are simply unavailable regardless of their technical merit, and a contractual ten to twenty year service life means a designer is not permitted to specify a component whose supply cannot be guaranteed across that period.[264][322] Because vendor assurances are difficult to obtain and cannot be fully trusted — a commitment can be withdrawn or misstated later — long-life designs are protected by specifying second-source parts, or parts whose family shares a common footprint, so a substitute can be dropped in without a board respin.[7]

The residual risk is absorbed by a specialist aftermarket. Obsolete-part houses such as Rochester Electronics operate their own wafer fab and approach the original chip designer when a part is going obsolete, buying the mask set rather than the schematics so that the vendor's intellectual property concerns are avoided.[169] They sell long-term sourcing service contracts, undertaking to supply a part for ten years to customers such as government and defence programmes whose original vendor will not commit to that horizon.[567] These re-manufacturers select which chips to keep alive by end market, concentrating on parts saleable to military customers, so a commercial designer whose part is discontinued cannot assume the aftermarket will cover it.[169] Specialist manufacturers keep long-obsolete processors in production for defence and space programmes, producing runs as small as ten units at prices on the order of ten thousand dollars per chip.[20]

The demand for those parts follows from deployment lag. Military hardware is typically about ten years behind current technology by the time it is fielded, so a maintenance cycle ten years later requires sourcing twenty-year-old chips.[80] Obsolete processors survive in defence equipment because maintaining a legacy design costs less than requalifying a redesign, not because the part is technically preferred.[81] The lag has narrowed over time: fielded military electronics trailed commercial technology by roughly twenty years around 2000 and by only five to ten years two decades later, meaning defence deployment cycles accelerated faster than the commercial industry over that period.[77]

## Development cycle and documentation

A defence product development cycle runs on the order of five years, after which the design is frozen and manufactured essentially unchanged for twenty years; industrial products by comparison run eighteen to twenty-four month cycles.[256] Programmes routinely build a total quantity of one unit, which removes the usual economic basis for cost optimisation.[64] The qualification and documentation load can make selecting a single mechanical fastener a six-month exercise.[288]

Documentation rules shape design entry itself. In military programmes HDL is classified as source code and therefore falls under software verification rules requiring every line to be verified, at a rule-of-thumb cost of around one hundred dollars per line; design teams avoided the rule by entering FPGA designs as schematic capture instead of HDL.[181] As recently as the early to mid 2000s, large defence contractors maintained design documentation on numbered A3 graph sheets, with computer-drawn circuits printed out and glued onto the sheets, because the controlled record was the paper sheet rather than the CAD file.[506]

Some conventions run the other way. Marine and underwater equipment, both military and civil, historically had no EMC or emissions standard to design to outside territorial waters, and the industry had no in-house standards either; the only acceptance test was whether the equipment did its job.[445] Handling requirements can still be severe: underwater military sonar equipment used high-energy lithium batteries carrying enough stored energy to explode on a short circuit, and shipping those assemblies required substantial dangerous-goods paperwork.[29] Equipment for industrial and military racks is still built to be repaired and serviced, because enclosure volume is not a binding constraint in rack-mounted applications and space can be spent on serviceability.[455]

## Prices and market structure

Connector prices of around two hundred US dollars per unit are routine in defence electronics, and a connector specified by a military customer can be sole-sourced to a single manufacturer at around nine hundred dollars a unit — being sole-sourced does not guarantee quality.[491] Sorting a distributor catalogue by descending price surfaces military parts at the top; the most expensive single chip found in such a search was around $128,000.[567] Very expensive military signal-processing parts are justified by workloads such as adaptive-bandwidth phased-array radar, which requires processing on the order of a thousand simultaneous channels at one gigasample per second in real time.[710] Component brokers who accumulate stock and resell it at multiples of the original price are viable because military and aerospace buyers can absorb those prices; commercial and hobbyist buyers are not the intended customer for that channel.[309]

Programmable logic retains a substantial defence market, and defence customers form a sizeable part of the business of smaller FPGA vendors.[525] MIT Lincoln Laboratory works primarily on US military programmes together with FAA and NASA work, on a budget approaching a billion dollars a year and with well over three thousand employees.[115] The commercial and military logic families diverged from the start: the 5400 series released in 1964 was a military-grade part, with the commercial 7400 series following roughly two years later.[207]

The supply base is contracting. Consolidation among qualified defence board houses interacts badly with procurement rules: when only about three shops can meet the requirements but every job must attract two or three bids, the same work is repeatedly bid to the same suppliers and price competition disappears.[567] A large share of US defence assembly is done by small family-run shops whose owners are retiring without successors, leaving no replacement capacity for the specific parts they have been making for decades.[705] Onshoring a defence supply chain fails when the sole historic supplier of a part has already gone out of business, because the capability cannot be recreated by placing an order.[705]

## Export control

Export control regimes such as ITAR are enforced at the point of transaction: semiconductor vendors gate software downloads and parts orders behind end-use declarations that the buyer must affirm.[186] Distributors require an end-use declaration before an order can be completed, asking whether the parts will be used in military, government surveillance, nuclear or chemical weapons applications, regardless of how ordinary the parts are, and a declaration of personal use can trigger follow-up questioning demanding further project detail even on an order consisting only of LEDs, resistors and op-amps.[7] Export-controlled products cannot be sold into certain countries, with the controlled list weighted toward items with nuclear proliferation relevance; liability for a false end-use declaration falls on the party who ticked the box.[186]

The reach of these rules is wider than the nationality of the parties suggests. A buyer was flagged on a US government watch list for purchasing non-US parts from a UK company out of stock already held in Australia.[186] Ordinary catalogue components can carry the obligation: a forty-dollar thermal sensor array could not be bought from a distributor without first signing an export control agreement, and two attempts to order it failed.[204] The burden propagates to anyone reselling a board that contains such a part, which is enough on its own to stop a small designer from offering an otherwise open design for sale.[204] Software-defined radio hardware sold at retail can carry export control restrictions that delay shipment outside the United States, and radio hardware also faces import restrictions, so a shipment can clear the seller's export rules and still be blocked by the destination government.[265]

### Sourcing and location as compliance decisions

Silicon for US government customers must come from a certified domestic process and cannot leave the country, which rules out offshore foundries irrespective of cost or capability.[228] Space systems classified as defence dual-use force the entire manufacturing chain in-country: neither bills of materials nor circuit assemblies can be sent overseas without an export control approval, so design, layout and assembly are all kept local.[679] The same logic applies to tooling suppliers. US defence customers dropped an EDA vendor after it moved research and development to China, because US regulations restrict which products a defence contractor may buy from a company effectively based there; where engineering work is performed is therefore a market-access decision, not only a cost decision.[197] A public portfolio of personal projects, generally an asset when job hunting, can count against a candidate seeking classified defence work.[151]

### Performance thresholds and materials

Export control is frequently written as a performance threshold rather than a product category. Sanctions imposed after the invasion of Ukraine barred Russia and Belarus from buying Taiwanese CPUs rated above 25 MHz, a threshold set on clock rate rather than on part type.[594] Restrictions on advanced compute hardware to China apply to specified performance levels of a vendor's range rather than to the vendor's whole product line.[602] The approach is long-established: a PlayStation console was export controlled because its GPU crossed a supercomputing threshold that made it usable for simulating weapon implosions.[602] High-bandwidth oscilloscopes and low-current instrumentation carried export restrictions because, until the mid to late 1990s, the applications needing that performance were nuclear instrumentation, and the restrictions persisted after commercial communications work moved into the same frequency range.[119] Even reference literature has been controlled: the MIT Radiation Laboratory series, the standard collection on radar circuits, antennas, klystrons and microwave instrumentation, was itself export restricted.[119] The pairing of state funding with sales conditions is older still — US Atomic Energy Commission funding of technology development came with a restriction limiting the resulting products to American buyers.[119]

Materials are controlled by the same mechanism from the other direction. China imposed export controls on germanium and gallium, both inputs with no immediate drop-in substitute for compound-semiconductor and optoelectronic supply chains, at a time when it accounted for roughly 60 percent of world germanium output and about 80 percent of gallium output.[652]

## Identification and secrecy

Defence contractors sometimes remark every integrated circuit on a board with their own part numbers, so the underlying devices cannot be identified from the assembly.[106]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 1 | What's In A Name? | https://theamphour.com/1-whats-in-a-name/ | |
| 7 | Love Robots and Pantyhose Screens | https://theamphour.com/the-amp-hour-7-love-robots-and-pantyhose-screens/ | |
| 20 | Military Electronics and The Free Eagle (Freagle) Campaign | https://theamphour.com/the-amp-hour-20-military-electronics-and-our-first-wotws/ | |
| 29 | DJ and Jazzy Jeff | https://theamphour.com/the-amp-hour-29-dj-and-jazzy-jeff/ | |
| 64 | OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster | https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/ | |
| 77 | An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry | https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/ | January 9, 2012 |
| 80 | Otiose Ontocyclic Opiniasters | https://theamphour.com/the-amp-hour-80-otiose-ontocyclic-opiniasters/ | January 29, 2012 |
| 81 | Jersey Jeff Jactitation | https://theamphour.com/the-amp-hour-81-jersey-jeff-jactitation/ | February 6, 2012 |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 115 | An Interview with Dr Greg Charvat - Watcher of Wraithlike Walls | https://theamphour.com/the-amp-hour-115-watcher-of-wraithlike-walls/ | September 30, 2012 |
| 119 | An Interview with Dr. Kent Lundberg - Luculent Linear Legacy | https://theamphour.com/the-amp-hour-119-luculent-linear-legacy/ | October 28, 2012 |
| 151 | Google Glass, Lean Startup and VotC - Initializing Instructed Interviews | https://theamphour.com/the-amp-hour-151-initializing-instructed-interviews/ | June 24, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ | |
| 186 | Someone is watching...we think - Horme Hostility Hypochondriac | https://theamphour.com/186-someone-is-watching-we-think-horme-hostility-hypochondriac/ | February 25, 2014 |
| 197 | Spacing Out On Space - Dave's Dongle Designing | https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/ | May 5, 2014 |
| 204 | An Interview with Noah Feehan - Biloquistic Blinking Blush | https://theamphour.com/204-an-interview-with-noah-feehan-biloquistic-blinking-blush/ | June 23, 2014 |
| 207 | B Plus Boards and D Minus Cities - Uneath Urban Ubication | https://theamphour.com/207-b-plus-boards-and-d-minus-cities-uneath-urban-ubication/ | July 14, 2014 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 228 | An Interview with Shahriar from The Signal Path - Quisquous Quivering Quadripole | https://theamphour.com/228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole/ | December 16, 2014 |
| 255 | Inspirations and Aspirations - Recanting Rocket Rationale | https://theamphour.com/255-inspirations-and-aspirations-recanting-rocket-rationale/ | June 24, 2015 |
| 256 | Is This A Show? | https://theamphour.com/256-is-this-a-show/ | July 1, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ | February 24, 2016 |
| 309 | An Interview with Stefan Dzisiewski-Smith | https://theamphour.com/309-an-interview-with-stefan-dzisiewski-smith/ | July 27, 2016 |
| 322 | World Trade Futurity (WTF) | https://theamphour.com/322-world-trade-futurity-wtf/ | November 9, 2016 |
| 445 | Ludicrously High Frequency Interference | https://theamphour.com/the-amp-hour-445-ludicrously-high-frequency-interference/ | June 2, 2019 |
| 455 | Bill and Dave's Excellent Equipment | https://theamphour.com/455-bill-and-daves-excellent-equipment/ | August 19, 2019 |
| 491 | The Almighty Dollarydoo | https://theamphour.com/491-the-almighty-dollarydoo/ | May 3, 2020 |
| 506 | Hipster Fodder | https://theamphour.com/506-hipster-fodder/ | August 24, 2020 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 594 | AI aren't sentient yet...right? | https://theamphour.com/594-ai-arent-sentient-yet-right/ | June 18, 2022 |
| 602 | Rigorous engineering stuff may be out the window | https://theamphour.com/602-rigorous-engineering-stuff-may-be-out-the-window/ | September 11, 2022 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 679 | Satellite Design Engineering with Dan Esparon | https://theamphour.com/679-satellite-design-engineering-with-dan-esparon/ | October 11, 2024 |
| 705 | Psst...Hey buddy, wanna buy an Octopus? | https://theamphour.com/705-psst-hey-buddy-wanna-buy-an-octopus/ | October 8, 2025 |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ | December 6, 2025 |
