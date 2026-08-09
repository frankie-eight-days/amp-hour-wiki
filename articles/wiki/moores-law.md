---
title: Moore's Law
concept: moores-law
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

Moore's Law is the observation that the density of integrated circuits — the amount of silicon function that fits in a given area at a given price — doubles on a regular cadence, commonly stated as every 18 months.[17][550] The statement concerns transistor density and cost, not processor speed, and the speed reading is a common misquotation.[17][550] The trend has functioned less as a physical law than as a self-fulfilling prophecy sustained by competitive pressure: each manufacturer invests to keep the doubling on schedule because a competitor otherwise will.[41][99] As scaling has slowed, the industry's response has shifted toward parallelism, die stacking, and chiplet-based heterogeneous integration.[297][499][704]

## Statement of the law

The trend is usually quoted as a doubling every 18 months, though formulations of 18 to 24 months also circulate; its author co-founded the company named for integrated electronics that produced the first single-chip microprocessor.[17][497] The underlying statement is about how much silicon function fits in the same area at the same price, not about how fast a chip runs.[17][550]

Two readings of the law are in common use: a lithographic reading, under which features shrink and transistor counts double, and a macro reading, under which memory halves in price and doubles in capacity every nine to eighteen months; whether the law is considered "over" depends on which definition is applied.[297] Under the density reading, the manufacturer chooses how to spend each generation's surplus: more speed, lower power consumption for battery life, or more dies per wafer delivering the same function.[550]

Plotting the transistor counts of released processors against the predicted doubling line shows the actual data oscillating ahead of and behind the trend rather than tracking it smoothly.[484]

## Historical development

Digital logic was built in bipolar technology until around 1980; bipolar was abandoned not because it stopped getting faster but because its power dissipation became intolerable, which drove the industry-wide switch to CMOS.[99] Companies that bet on gallium arsenide for speed lost out when CMOS became fast enough, a recurring pattern in which the incumbent process outruns an exotic alternative.[99]

Through the 1990s, clock frequency was the headline competitive axis in the megahertz and gigahertz races.[501] That axis ended well before density scaling did: desktop processors sat near three gigahertz for over a decade, and core count replaced frequency as the marketed specification.[61][501]

Using the chessboard-and-rice doubling parable as a yardstick, the counted generations of technology doubling passed the 32nd square around 2006, the point at which an exponential progression becomes visibly overwhelming.[195]

### Forecasts of the end

Predictions of the law's breakdown have a long history. One widely circulated forecast placed the breakdown of transistor scaling in the 2020 to 2030 window.[61] An IBM semiconductor research leader estimated on a Design Automation Conference panel that conventional semiconductor technology had about two more decades of runway.[99] Around eight-nanometer device dimensions, CMOS has been expected to require a fundamentally different approach — a boundary that had been predicted for roughly a decade without arriving.[228] GlobalFoundries' decision to halt seven-nanometer development was a single-company capability decision rather than an industry ceiling, since TSMC continued developing that node.[406]

Extrapolating exponential doubling to the physical limit of one bit per atom yields an absolute ceiling of roughly 600 years, beyond which all reachable matter would be consumed as storage.[23]

## Economic character

The doubling cadence is driven by commercial survival rather than technical enthusiasm. Fabs pursue each process generation under competitive pressure: if one company does not advance the node, a competitor will, which is why the whole industry marches in step.[41][564] The trend functions as a self-fulfilling prophecy in which each company invests to keep it on schedule because a rival otherwise will.[99] CMOS scaling continues because demand for storage, processing, and lower power funds it; without that economic pull, the technical progress would stop regardless of what physics permits.[228]

The industry has largely moved to a fabless-plus-foundry structure, with Intel the prime remaining example of a vertically integrated device manufacturer.[99] At the 28- and 20-nanometer generations, the process physics became severe enough that EDA tool selection could no longer be separated from the choice of foundry, forcing collaborative development and heavy mathematical modeling.[99]

Large corporations pipeline product development around the process cadence, so each year's product is far enough along that an individual builder cannot match it.[61] As the density curve flattened, a counterpart cost curve moved the opposite way, with semiconductor development cost rising as dimensions shrink.[553] Only about two or three companies worldwide can run five- and three-nanometer CMOS processes — TSMC and Samsung, with Intel potentially reaching them.[553] Proprietary process design kits carry legal overhead measured in 800-dollar-per-hour lawyer time, so only ideas a team is already confident in get explored; open PDKs lower the barrier to trying speculative architectures.[501]

Falling digital electronics cost also reset pricing in adjacent markets: an entry-level benchtop oscilloscope sat near 800 dollars for decades until Rigol halved the 1052E's price to 400 dollars in 2009.[293]

## Physical and design constraints

Below the wavelength limit of deep-ultraviolet lithography, a single layer is decomposed into several coarser patterns exposed on top of one another to reach the fine resolution, a technique called multiple patterning.[553] Multiple patterning removes layout freedom that older nodes allowed: gates can no longer be placed at arbitrary orientations, and everything on a layer must run in the same direction.[553]

Bond pads do not shrink at anything like the rate transistors do, so on advanced nodes a small die becomes pad-limited rather than transistor-limited.[272] Modern node names are marketing labels rather than feature sizes: a so-called two-nanometer node contains no two-nanometer features, and physics limits real dimensions to roughly ten or eleven nanometers.[704]

Power is a parallel constraint. Efficiency was historically bought by lowering supply rails alongside parallelization, but rail voltages have approached diode-drop levels, removing that lever.[704] Packing more transistors into a small area raises power density and makes heat extraction a serious limit, and adding cores only helps if memory bandwidth can feed them.[501] Current compute scaling is limited by power and by DRAM cost rather than by lithography alone, pushing gains toward efficiency instead of raw capability.[722]

High-speed RF parts are typically not built on leading-edge CMOS at all but on silicon-germanium BiCMOS, where SiGe bipolar devices provide higher breakdown voltage for power handling and the on-die CMOS is a far older node used as a helper.[553]

## Slowdown and its consequences

Transistor count per chip has kept roughly doubling, but what changed is how the transistors are usable: single-threaded performance hit a ceiling and core counts rose instead.[501] After roughly 40 years of hard scaling, present-day improvements come from more parallel processing rather than smaller transistors, and no successor technology with comparable breadth of application has emerged.[704]

System performance and transistor scaling are separable: architectural techniques such as parallelism can deliver performance gains that run ahead of the process-scaling schedule.[17] A common design habit, however, has been to accept slow compute-heavy tools on the assumption that future process generations will make them fast enough, deferring optimization work indefinitely.[19] The historical default answer to a performance shortfall was to wait roughly 18 months for faster silicon; when that stops working, the remaining lever is spending engineering time optimizing code or turning it into dedicated hardware.[317] ASIC design methodology has not been rethought at hundred-fold scale increments the way software practice has; chips are still designed with late-1990s methods because process scaling supplied the speed gains instead.[501]

If hardware performance stays flat for years, multi-year investments in optimizing compilers and hand-coded assembly start paying off because the gains are not erased by the next chip.[84] Physics makes the slowdown of transistor scaling essentially inevitable, and longer cycle times give architectural ideas more room to prove viability; under a fast cadence, by contrast, innovation is compressed into a window of months, because a full-stack idea must show a compelling improvement before the next node makes it irrelevant.[84] Backward compatibility combined with steady process gains makes incremental speedups the rational business choice, which suppresses architectural risk-taking such as moving the processor next to the memory.[84]

When scaling stops, memory capacity per generation stops multiplying, removing the yearly specification jump manufacturers had relied on for new product cycles.[61] A better strategy for a small hardware business than waiting for scaling to stall is to target niches large corporations serve badly.[61] Correspondingly, the end of easy gains in general-purpose computing opens more silicon niches, making specialized chip startups more viable than during the era of uniform scaling.[672]

### Stacking and chiplets

When a process node runs out of headroom, effort shifts to packaging improvements until packaging itself becomes the limiting factor and a new node jump is made.[84] Once density gains in the plane stall, the industry response is vertical stacking of die — the same move a densely populated area makes when land runs out.[297] Chiplet and heterogeneous system integration is positioned as the successor enabler for semiconductor innovation as monolithic scaling reaches its end.[499]

Integrating everything onto one monolithic die remains the performance-optimal answer, providing roughly 13 metal layers, hundred-nanometer wire pitches, and the best energy efficiency, cost, and bandwidth; the trade is that monolithic integration abandons modularity entirely, producing a statically compiled blob with no reuse, whereas chiplets give hardware the equivalent of software libraries and linking.[650]

### Custom and reconfigurable logic

Process headroom running out revived interest in programmable logic, restoring the long-standing tradeoff between FPGA custom logic and brute-force parallel processors.[296] Slowing process gains likewise increased interest in open-source FPGA toolchains, because optimizing custom logic becomes worthwhile when free performance no longer arrives.[421] FPGAs offer software-style deployment timescales — worldwide in minutes rather than years — but pay a substantial silicon cost for that configurability.[501]

Commodity ARM cores driven by smartphone volume became powerful enough that custom hardware such as FPGAs stopped being necessary for many embedded control applications.[105] Analog preprocessing before conversion retains real niches at low power, low amplitude, and low sensitivity, but analog will not match digital scaling for integration, complexity, and processing throughput.[119]

The long-run trend in the cost of compute is downward toward zero, now driven by GPUs, TPUs, and algorithmic efficiency rather than transistor scaling alone, letting models that once needed a cluster run on local machines.[626] Very large scale integration also remains the enabling substrate in its own right: modern phased arrays are practical because integration supplies the many data converters and wide data pipes that mechanically scanned radar could not.[729]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 17 | EE Movies, Part Rants and SPICE. | https://theamphour.com/the-amp-hour-17-ee-movies-part-rants-and-spice/ |  |
| 19 | CAD programs, Systems Design and Renewable Energy | https://theamphour.com/the-amp-hour-19-cad-programs-systems-design-and-renewable-energy/ |  |
| 23 | The Innovation Speculation | https://theamphour.com/the-amp-hour-23-the-innovation-speculation/ |  |
| 41 | Contests, Ham Radio & TWIT.tv - Ham, Spam, Thank You Ma'am | https://theamphour.com/ham-spam-thank-you-maam/ | May 4, 2011 |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ |  |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 99 | An Interview with Steve Leibson - Impavid Ideopraxist Insider | https://theamphour.com/the-amp-hour-99-impavid-ideopraxist-insider/ | June 10, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 119 | An Interview with Dr. Kent Lundberg - Luculent Linear Legacy | https://theamphour.com/the-amp-hour-119-luculent-linear-legacy/ | October 28, 2012 |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ | April 21, 2014 |
| 228 | An Interview with Shahriar from The Signal Path - Quisquous Quivering Quadripole | https://theamphour.com/228-an-interview-with-shahriar-from-the-signal-path-quisquous-quivering-quadripole/ | December 16, 2014 |
| 272 | An Interview With Luke Beno of Analog.io | https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/ | October 21, 2015 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 297 | An Interview with Jake Baker | https://theamphour.com/297-an-interview-with-jake-baker/ | May 4, 2016 |
| 317 | A Decoupled Episode | https://theamphour.com/317-a-decoupled-episode/ | September 28, 2016 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 484 | Man Behind The Curtain | https://theamphour.com/484-man-behind-the-curtain/ | March 16, 2020 |
| 497 | An Interview with Brock LaMeres | https://theamphour.com/497-an-interview-with-brock-lameres/ | June 21, 2020 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ | July 18, 2021 |
| 553 | Debunking with Shahriar | https://theamphour.com/553-debunking-with-shahriar/ | August 10, 2021 |
| 564 | Pavlovian Cheapskates | https://theamphour.com/564-pavlovian-cheapskates/ | October 31, 2021 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 650 | Accessible ASICs with Andreas Olofsson | https://theamphour.com/650-accessible-asics-with-andreas-olofsson/ | November 12, 2023 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 722 | AI Tooling with Matt Liberty and Luke Beno | https://theamphour.com/722-ai-tooling-with-matt-liberty-and-luke-beno/ | April 22, 2026 |
| 729 | The Terahertz Frontier with Greg Charvat of Teradar | https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/ | July 22, 2026 |
