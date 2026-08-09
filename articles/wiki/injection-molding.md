---
title: Injection Molding
concept: injection-molding
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Injection molding is a manufacturing process in which plastic pellets are melted, driven forward by a reciprocating screw, and forced into a precision-machined mold under hundreds of tons of clamping pressure.[379] The process dominates the production of high-volume plastic parts because its economics invert those of most fabrication methods: the tooling carries nearly all of the cost, while the marginal cost of each additional part approaches zero.[130][405] That cost structure, together with geometric constraints imposed by the need to extract a solidified part from a steel tool, shapes a distinct body of design rules, failure modes, and production practices.[153][218]

## Process

In a molding machine, plastic pellets are heated and pushed through a screw, which transfers torque to drive the material forward, and the melt is then injected into a mold held closed under multi-hundred-ton clamping force.[379] The mold itself is machined to very tight precision or cut by electrical discharge machining.[379] Die casting is the analogous process for metal: material is injected at high pressure, typically one to two hundred degrees above its melting point, so that it reaches every crevice of the cavity before solidifying.[325]

A spectrum of molding processes exists below full high-pressure injection molding, usable for test parts or short production runs without the multi-hundred-ton machine.[379] At quantities around a thousand parts, work is generally done on bench presses, by machining, by printing, or by low-pressure molding rather than on a true injection molding line.[379]

## Design constraints

### Draft and ejection

A molded wall cannot be perpendicular to the direction of draw: without a taper, or draft angle, the part tears against the tool as it is pulled free, so a nominally square feature emerges slightly trapezoidal.[153] The interlocking plastic brick is a rare molded product whose outer walls really are square and perpendicular, achieved by placing all of the draft on the inside surface of the part.[379] Because a part's shape carries the evidence of how it was made — a face angled purely so the part will release reliably from the tool — teardown analysis of commercial parts is a recognized way of learning mold design.[485] When an experienced practitioner critiques a model, the first finding is typically missing draft on a face that would never release.[665]

### Geometry and complexity

Pushing complexity into the tool is generally the favorable trade: features such as a battery retention detail require slides and draws that make the mold more expensive, while the extra plastic consumed per shot costs essentially nothing.[277] However, each variant of a design requires its own tool, so an engineer's time spent modifying a model is trivial next to the cost of the mold the modification implies.[374] A geometry that a 3D printer will readily produce can be impossible to mold, and proving a feature on a printed prototype says nothing about whether it can be manufactured in volume.[127] For this reason, custom mechanical parts are designed so that a prototype can be machined or printed even when production will be die cast or molded, rather than discovering at the end of development that the production geometry cannot be prototyped.[436]

### Gates and flow

Gate placement — the position of the injection points in the tool — is a classic first-product failure, surfacing only once parts emerge from the mold.[715] The effective mold designer works alongside the manufacturing engineer, understanding how the machine and the flow of the plastic constrain what the tool can be, and feeds those constraints back into the design.[712]

## Tooling

### Cost and geography

Tooling cost is the defining economic fact of the process. A production tool for a part as small as a plastic brick has been estimated at tens of thousands to a couple of hundred thousand dollars in the United States.[379] A single small proprietary connector plug carried a tooling cost of roughly eighteen thousand dollars.[167] Quotes vary by orders of magnitude with where the tool is cut; non-recurring engineering for a molded part in China has been quoted at around five hundred dollars.[379] Tooling can consume a crowdfunding raise outright: in one campaign, mold costs alone would have absorbed most of the roughly $170,000 raised.[219]

### Hard and soft tooling

Soft tooling costs far less than hardened production tooling and wears out much sooner, but yields fully functional parts of reasonable quality — sufficient for regulated products that need a certifiable unit long before mass tooling exists, and good enough to pass regulatory testing while looking like the real product.[159] At a build of well under two thousand units, a custom hard tool for an enclosure is not the right call, with a soft mold the sensible alternative.[161] The threshold is not absolute: Michael Ossmann ran one product with an injection-molded case while manufacturing it in batches of a thousand at a time.[161]

### Tool life and correction

A correction that adds material to the part is cheap, because it requires only cutting more steel out of the tool; designing so that fixes run in that direction keeps changes quick.[218] Worn tools reveal themselves as flash — a rim of excess material around the parting line where the mold halves no longer close cleanly.[586] Across tens of thousands of shots the tool wears and the plastic sags, so prototype shots that look acceptable are not evidence that a part is production-ready, and cosmetic standards shift once finished product is being judged.[287]

### Tooling lead time

Tooling lead time has historically set the iteration rate of entire industries: appliance models appeared on cycles of five to seven years because design plus tooling took that long, and process rules were built around that pace even for products that would sell in the thousands.[159] On the Bus Pirate programme, Ian Lesnet fixed the board outline across successive product versions so that one enclosure tool could be amortized over several generations rather than remaining a single-product cost.[125]

### The toolmaking skill

The scarce skill in a molded product is the toolmaker rather than the part designer: early units can be machined from solid aluminium at any cost, but production without a senior mold designer produces exactly the ejection failures that stop a line. Jeri Ellsworth, who brought a molded consumer product to production, described the necessary person as a "unicorn" who knows how to make the tools.[173]

## Economics and production volumes

Past the tooling cost, the marginal cost of molded plastic is close to nothing: on an inexpensive vacuum cleaner the copper motor windings are the expensive content, while the entire plastic body costs around a dollar on a million-shot tool.[130] Ordinary molded consumer goods cost fractions of a penny per part.[405] Toy companies employ dedicated costing engineers who estimate a part by weighing the plastic, pricing the raw resin, and adding the molding cycle time for that specific geometry.[424]

The rough crossover where prototype-style processes stop being the cheaper route and tooling begins to pay sits around five thousand units, though the type of mold still matters below the high-volume threshold.[218] Design-for-manufacture guidance is correspondingly tiered by tooling budget: cheap tools come with one set of draft-angle and wall-thickness rules, expensive tools relax them, and the highest tier represents capability effectively unavailable to anyone else.[218]

No additive process competes with molding on throughput, because the cycle is simply heating plastic and shooting it into a tool.[172] One crowdfunded product that printed all of its enclosures ended up running a room of printers continuously to keep up — a choice its maker afterwards called a mistake.[172] Additive manufacturing is considered unlikely to displace molding at the commodity end of the market.[405] The process is, however, unforgiving of late commitment: crowdfunding publishes an idea before the team has any way to build it, and campaigns are routinely run by people with no route to a molded part or a manufacturable board who then cannot afford the engineers to get one.[336]

Defence and consumer molding operate at incompatible scales, so a supplier tooled for military volumes cannot simply take commercial work to stay busy between contracts.[705] Choosing among thousands of molders resists rating systems, because a buyer who had a good project leaves five stars while a buyer who had a bad one simply walks away rather than damage a relationship they may need again.[405]

## Process variation and failure modes

A part almost never ejects cleanly from a new tool on the first attempt; on one design the part jammed so hard that the ejector pins sheared off before the plastic gave way.[173] Parts leave the tool carrying enough electrostatic charge to bounce back out of the collection bin, striking the side to discharge before they will settle.[218]

The same tool does not give the same part. Shot speed and melt temperature are all adjustable, so pre-production and production runs can differ, and a defect affecting a small percentage of parts is invisible in a fifty-unit build and obvious at five hundred or a thousand.[377] A field failure in a mechanical switch was traced to dimensional variation in the molded parts despite two years of prototypes on what was nominally the same tool never showing it.[377]

Plastic shrinks as it leaves the tool, so the drawing carries a shrinkage allowance rather than the measured dimension. Re-baselining the drawing to the shrunk parts, as a factory may request, would cause the next tool to be cut to the shrunk size and shrink again from there, ratcheting the part smaller with every generation.[564]

Colour contamination from an incompletely purged machine carries the previous run into the next; one thousand-unit order of light-coloured knobs arrived flecked with black, blue, and red, forcing hand inspection of every piece.[586]

## Design for manufacture practice

Manufacturability is treated as part of the design rather than a downstream check, on the principle that a part that cannot be made is not a design at all.[712] A mold designer gives the same kind of free design feedback a contract manufacturer gives on a circuit board — thin walls, missing slope, and unbuildable geometry, all identified before any steel is cut.[350] The recurring pattern is that a factory reviewing a finished design finds savings that could have been designed in from the start, which is the argument for pulling manufacturing knowledge earlier into the process.[451]

Published design-for-manufacture curricula cover molding alongside die casting, rotational molding, factory selection, managing cost against quality and schedule, and waterproofing, with the molding module alone running to fifty or sixty slides.[451] Hands-on manufacturing courses have taken students from solid modelling through having tooling cut, treating surface finish and resin choice between ABS and polycarbonate as decisions the designer makes, alongside techniques such as in-mold lamination.[280] Toy-industry practice is to be physically present whenever a tool is opened, with trips batched around the run-up to the holiday season.[414] Taking a molded product to volume calls for a mechanical engineer with tooling experience in both molding and die casting, comfortable with tolerances and with working directly with contract manufacturers — a distinct hire from the board designer.[517]

### Alternatives to custom tooling

An off-the-shelf enclosure is frequently good enough for the look and feel of a product, and going fully custom adds certification work on top of tooling.[287] Zach Dunham chose a stock container as the enclosure for a first product, removing the need to produce any enclosure at all and treating the constraint as deliberate rather than a compromise.[350] Where standard chip encapsulation could not be adapted to leave a window for a display, Marcus Schappi's product instead used a molded enclosure over the assembled board to obtain the desired shape.[189] Jason Huggins held his product on printed parts while the design was still changing, treating assembly capacity — the maximum number of units that could be put together in a month regardless of demand — as the signal for when to move to tooling.[369]

Custom tooling buys freedom at volume, including parts such as bespoke battery form factors that cannot be bought from a catalogue, but it also removes every fallback: with a custom molded part there is no equivalent of buying a project box when the tool fails, and the designer becomes the supply chain with no backup.[365]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 130 | Boeing, PCBs & Startups - Awful Airplane Aeration | https://theamphour.com/the-amp-hour-130-awful-airplane-aeration/ | January 28, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 159 | Interview with Eric Ries - Transorted Testing Tachydidaxy | https://theamphour.com/the-amp-hour-159-transorted-testing-tachydidaxy/ | |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25, 2013 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 280 | New Year Education | https://theamphour.com/280-new-year-education/ | |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 336 | An Interview with Bunnie Huang (2nd) | https://theamphour.com/the-amp-hour-336-an-interview-with-bunnie-huang-2nd/ | |
| 350 | An Interview with Zach Dunham | https://theamphour.com/350-an-interview-with-zach-dunham/ | July 3, 2017 |
| 365 | Wait, why is Jeff glowing? | https://theamphour.com/365-wait-why-is-jeff-glowing/ | October 30, 2017 |
| 369 | An Interview with Jason Huggins | https://theamphour.com/369-an-interview-with-jason-huggins/ | November 26, 2017 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 379 | An Interview with John Saunders | https://theamphour.com/379-an-interview-with-john-saunders/ | February 11, 2018 |
| 405 | An Interview with Spencer Wright | https://theamphour.com/405-an-interview-with-spencer-wright/ | September 3, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 451 | An Interview with Scott Miller (2nd) | https://theamphour.com/451-an-interview-with-scott-miller-2nd/ | July 21, 2019 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 564 | Pavlovian Cheapskates | https://theamphour.com/564-pavlovian-cheapskates/ | October 31, 2021 |
| 586 | Fran Blanche Version 3 | https://theamphour.com/586-fran-blanche-version-3/ | |
| 665 | Really long needle nose pliers | https://theamphour.com/665-really-long-needle-nose-pliers/ | April 24, 2024 |
| 705 | Psst...Hey buddy, wanna buy an Octopus? | https://theamphour.com/705-psst-hey-buddy-wanna-buy-an-octopus/ | October 8, 2025 |
| 712 | Robots Everywhere with Aaed Musa | https://theamphour.com/712-robots-everywhere-with-aaed-musa/ | January 19, 2025 |
| 715 | Shiny New Pebble with Eric Migicovsky | https://theamphour.com/715-shiny-new-pebble-with-eric-migicovsky/ | February 9, 2026 |
