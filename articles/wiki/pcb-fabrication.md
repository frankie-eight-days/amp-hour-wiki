---
title: PCB Fabrication
concept: pcb-fabrication
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Printed circuit board (PCB) fabrication is the set of manufacturing processes that converts a layout design into a bare, unpopulated circuit board. A two-layer board passes through roughly fifteen distinct manufacturing steps, and a multi-layer board through substantially more; a full bare-board fabrication line runs to twenty-five or thirty steps, including cleanroom stages that must be re-entered in sequence.[140][414] The economics of the process have shifted by orders of magnitude: single boards that cost thousands of dollars and took weeks in the early 1990s are now available as five four-layer boards for about seven dollars from shared-panel services, a change that has restructured how hardware is designed and iterated.[79][137][652]

## Process sequence

Fabrication begins with drilling. The holes for vias and through-hole components are drilled into the raw copper-clad laminate before any plating, so that the hole barrels can subsequently be plated to form connections between layers; a mid-sized fab operates rooms of multi-spindle CNC drills in parallel.[121] Minimum via size is set by the mechanical drill: below the smallest available bit, holes must be laser-drilled, an additional process step that many fabs do not have on site, so such work is subcontracted or refused.[414] Drilling capacity also imposes a panel-level constraint — above roughly forty holes per square inch averaged over the panel, fabs object, because drilling time and bit wear dominate that part of the process.[149]

The imaging step transfers the layout to the copper layers through photographic masks. Traces are output as a positive image and copper planes as a negative one, so on the plane layers of a Gerber set the areas that appear blank are where copper remains; reading a plane layer as if it were positive inverts its meaning.[434] The negative convention is a legacy of manual layout, when only negative-photoresist board stock was available and a positive taped artwork had to be photographically converted to a negative on film before exposure, making board production a two-step photographic process.[434] One way to eliminate the conversion step was to lay the artwork out mirrored in the first place, trading a physical processing stage for a design-side inversion.[512]

Plating deposits copper in the drilled barrels and builds up trace cross-sections, and it is sensitive to the distribution of copper across the panel. Uneven copper coverage causes plating to run unevenly, producing breaks and shorts that the fab must hand-correct; a shared panel assembled from unrelated designs is especially prone to this, and fabs will refuse panels that force hundreds of manual fixes.[149] Processes differ between regions, not merely in price: environmental rules on etchant disposal shape the chemistry available, so in a United States fab any hole with a copper pad on both sides is plated and anything else is not, while Asian fabs use a different resist that permits a single pass where the US process needs multiple steps.[149]

### Multilayer and high-density construction

Multilayer boards are built up by repeated lamination. An any-layer stack-up, in which a laser via can connect any adjacent pair of layers, requires a lamination, plating and drilling cycle between each layer as the board is built up; an eight-layer any-layer board needs about five plating cycles, and that sequence, not the layer count alone, is what makes the board expensive.[681] Laser vias in such a build can be stacked directly on top of each other or staggered; stacking is harder on yield and some manufacturers will not accept it, so the choice belongs to the fab's capability rather than the designer's preference.[681]

A high-density module can be kept within standard PCB technology at 75-micron trace and space with 200-micron vias on an 81- to 85-micron drill; moving beyond that to substrate or interposer processes is a large step in price and closes the design to anyone without access to those processes.[681] Despite the process complexity, quantity amortises it: a ten-layer any-layer board small enough that 120 fit on an A4 sheet has been produced at about ten dollars each at that quantity.[681]

## Design rules and manufacturability

Design rules express a fab's process limits as minimum dimensions, and they determine where a board can be built. A six-thou (six-mil) trace-and-space design is within reach of essentially every fab, so choosing that rule set keeps a design orderable from the cheapest shops and reproducible by anyone.[375] A factory's habitual board house effectively sets the design rules available to a project: a keyboard manufacturer's usual fab preferred 12/12 rules where a design needed 8/8, because keyboards are historically two-layer boards with wide traces and that supply chain was not set up for USB Type-C or fine-pitch parts.[450] Fabs work in metric while many designers work in thousandths of an inch, and mixed conventions persist inside a single workflow — track and space in thou, drills and board outlines in millimetres — because manufacturing is carried out in metric whatever units the designer used; a quoting page that presents both can introduce a rounding error at the minimum-feature boundary, so a design that appears to pass the published rules is rejected or altered.[149][504]

Component choice propagates directly into fabrication cost. BGA ball pitch tightens the tolerances required on etching and solder mask, so moving a design from 0.4- to 0.8-millimetre pitch parts is what makes a board reproducible by its users.[67] Choosing the larger-pitch package variant of a processor is a deliberate fabrication decision on a physically large board, keeping the whole board inside the ordinary prototype-shop process instead of forcing high-density-interconnect construction across its full area.[640] At the other extreme, a 0.35-millimetre-pitch wafer-level chip-scale package can be fabricated on a standard six-layer service with via-in-pad, but only by working exactly at the minimum 0.25-millimetre spacing and setting the design grid so every via lands on it; not all rows of the package can be escaped, and in one such design about 40 of 64 available pins were brought out.[692]

Designing below a fab's minimum track width does not necessarily produce a rejection; the boards may simply arrive with shorts between adjacent traces, recoverable only by cutting them apart by hand.[557] Stack-up definition carries a similar risk: design teams routinely define a layer order without dimensions and leave the dielectric thicknesses to the fabricator, effectively delegating the impedance calculation to whoever builds the board.[252] Because controlled impedance depends on a stack-up that belongs to one specific fab, boards ordered from a different house without a fab drawing have come back with impedance wrong by a factor of two, with days spent suspecting the measurement equipment before the stack-up was checked.[494]

### Standards, footprints and panelisation

The IPC standards define land patterns and pad dimensions for surface-mount components — IPC-7351 covers surface-mount design and land pattern standards — and following them is what makes soldering reliable at manufacture; a footprint that is oversized or undersized relative to the standard degrades yield rather than merely looking wrong.[531] A fabrication service can be operated without reading the IPC specifications, since they describe rather than police the process, but knowing them improves the product.[149] Where the manufacturer is known in advance, footprints and board features are sometimes designed for that specific fab and assembly machine rather than to a generic standard, which forecloses moving the design elsewhere without rework.[143]

Panelisation interacts with the board outline. Castellated edges and breakaway panel tabs compete for the same perimeter: edges that are castellated cannot carry tabs, and a connector that overhangs the board edge removes another side, so panelisation must be planned together with the outline.[395] Fabs work in large standard panels, commonly quoted in inches at sizes such as 18 by 24, which frequently exceed the rail capacity of a pick-and-place machine; a panel intended for assembly must be sized for the assembly equipment, not for the fab's efficiency.[415]

Layout skill alone does not produce a manufacturable board: a designer who does not know the specific limitations of the fab, the assembler and the equipment the board will pass through produces designs that cannot be built, however sound the layout.[195] Watching the process resolves design rules into physical causes — seeing a drill run explains why a via cannot shrink indefinitely, which no rule table conveys.[414]

## Economics

Turnaround time, not complexity, layer count, hole count or geography, is the dominant term in bare-board pricing: the same complex board is expensive tomorrow, moderate in a week, and very cheap if the delivery date does not matter.[163] Paying for expedited fabrication buys queue position — the fab bumps other jobs and starts within minutes of the order — and eight- to ten-layer boards have been turned in 24 hours this way at a cost of thousands of dollars for a prototype; some fabs instead hold a line in reserve for emergency work and describe expedited jobs as bumping other customers when in fact they are spinning up that reserve capacity.[502][654] Board fabrication differs sharply from semiconductor fabrication in this respect: a board can be expedited to hours because the queue is the constraint, while a chip with a 16- to 20-week process lead time cannot be, which is why distributors ask for months of forecast visibility rather than accepting expedite requests.[502]

At prototype quantities, pricing is dominated by setup rather than per-unit cost, so ordering twenty boards costs about the same as ordering one, and quotes for ten and for 250 boards can differ little enough that the larger quantity is the rational order.[121][395] Fabrication cost tracks the processing time of the panel rather than the material in it, which is why a small board on a shared panel is cheap and why board area matters less than the number of process passes.[412] Bare-board fabrication is a low-margin business, which is why assembly houses that consider bringing it in-house justify the move on turnaround time rather than on cost.[243]

Pricing has pockets. A service that constrains designs to two or four layers, one solder-mask colour and a 0.1-millimetre track and gap can quote a much lower price and a three-day turnaround, and over half the orders on such a service fall inside that envelope.[699] A prototype house's low price comes from running every job through one fixed process; supplying a fab drawing means specifying the process instead of accepting theirs, which is what makes non-standard work available and what makes it expensive.[415] Combined rigid-flex construction, for example, cannot be ordered by uploading Gerbers alone — it requires the mechanical and stack-up definition that the standard prototype flow deliberately does not accept.[415] Quick-turn prototype boards from a domestic fab still cost thousands of dollars, and engineers accustomed to low-cost overseas shared-panel pricing routinely mistake such a quote for an error.[646] A local fab willing to take artwork before late morning and ship the same day has charged no more than about £150 for a double-sided Eurocard in 24 hours, a price defensible on a client project and not on a hobby one.[224]

Where one component forces an expensive process across a whole board, fabricating that component's escape on a small dense module and joining it to a cheap motherboard by castellations or a board-to-board connector costs less than paying the advanced process across the full board area.[502] The falling cost and time of one hardware iteration — from weeks and thousands of dollars to under a week and tens of dollars — changes how many design spins a project can absorb.[626]

### Shared-panel services

The shared-panel prototype service began as a hobbyist group pooling designs onto one panel at a domestic fab, breaking the finished panel apart and distributing the boards, in response to month-long waits and poor yields from overseas orders.[149] The measured defect rate through the domestic fabs used by that service was about one board in 40,000, against roughly one in four — later about five per cent — from the low-cost overseas orders it replaced; the defects were shorts, solder-mask errors and annular ring breakouts.[149] A shared-panel service can only pool designs that share a solder-mask colour, so the default colour runs daily and any other colour waits for enough orders to fill a panel.[149] A shared panel also carries no room for special handling: with a hundred designs on the panel the fab will not adjust its process for one of them, whereas a customer paying for a full panel gets that attention.[504] At five dollars for five boards, such services are not profitable in themselves; they are run as loss leaders or as a route to higher-value work.[724]

## History

Professionally made boards were out of reach for individuals until around the mid to late 1990s, costing thousands of dollars for a single board.[79] Before online prototype services, a one-off commercial board cost of the order of a thousand dollars and took weeks, which made home etching and point-to-point construction rational choices rather than hobbies.[137] Inside companies in the early 1990s a board order meant eight hundred to a thousand dollars, a two-week wait and a triplicate purchase requisition, so an engineer who could etch a board in-house compressed a two-week loop into a day.[341]

By the early 2010s a fixed-price online service supplied ten double-sided, plated-through, solder-masked and silkscreened boards for twelve dollars including tooling — a specification that had been the mark of a high-end kit a decade earlier.[33] Large four-layer boards of about 30 by 30 centimetres, a size that had historically carried a large premium, were quoted at roughly 175 dollars for five delivered.[393] Four-layer prototype boards subsequently reached about seven dollars for five pieces at the low-cost Chinese shared-panel services, a change of roughly two orders of magnitude within a single career.[652]

Flexible circuit material is not a recent technology; it was common in consumer equipment by the 1970s. What is newer is rigid-flex construction, with the flex layers laminated inside the stack-up rather than attached beneath it.[468]

## The interface between designer and fabricator

Commercial fabs run an engineering review of incoming Gerbers before manufacture and query anything that looks wrong — a check the designer should expect and answer rather than a formality.[74] Online design-for-manufacture tools that digitise the checks a board house performs, and return the result with a visualiser, remove the sales conversation from quoting, and buyers select suppliers on that basis alone.[504] A fabricator quoting against a supplied specification, however, has no commercial interest in volunteering that a different stack-up or process would be cheaper; it will build what was asked for at the corresponding price, and learning which process the shop already runs is the designer's job.[718] The same asymmetry appears across fabrication trades: a shop will accept a job that forces its most expensive process rather than suggest the small design change that would allow a cheaper one.[379] Comparing fabricators' available stack-ups and prices at the start of a design, rather than at release, is what allows manufacturing constraints to shape the layout while changes are still cheap.[718]

Manufacturers edit incoming board files to add panel rails and fiducials, and that edit can corrupt the design: on one four-layer board a via lost its layer assignment during such an edit and was fabricated on the wrong layer, a fault that is neither a design error nor a process defect.[682] Incoming inspection of bare boards exists to verify that the supplier built what was specified, and is a distinct activity from testing the design.[663] A stencil ordered alongside a board is cut from whichever revision was current when the order was placed, and the fab will not necessarily flag that later board revisions have moved parts; the mismatch appears at paste application.[692]

### The cost of errors

The cost of an error is asymmetric between hardware and software because a fabricated and populated batch cannot be patched: ten thousand boards must be scrapped or reworked, and both are expensive.[546] A symbol or footprint error that survives to fabrication costs the board run plus the days spent debugging a board that cannot work, which is why library errors are disproportionately expensive relative to their apparent triviality.[131] A defined checking procedure covering schematic, layout and footprints before release exists because the same defects cost far more once boards are in production than they do to catch on screen.[316] A design that fails electromagnetic compliance typically consumes several board spins — a first failure, a speculative modification, another spin, pre-compliance retesting and a further formal test — reaching tens of thousands of dollars in board runs and test fees before salaries are counted.[718]

Board construction also feeds back into assembly: taking a proven design to a much thicker board with heavier copper changed its thermal mass enough that every 0402 component tombstoned in a reflow profile that had been dialled in for the thinner version.[610]

## Specialised capabilities

Fabs will perform controlled-depth routing, embed components inside the board, and print multiple silkscreen colours, if the requirement is explained and paid for; these capabilities sit outside the standard quoting flow rather than outside the industry.[286] Some fabricators can print resistors directly onto the board from conductive ink, supplying a specified resistance as part of the board rather than as a placed component.[260] Solder mask, silkscreen and selective omission of layers give the board process a range of visual and mechanical effects, and boards can be stacked as structural layers to build an enclosure or front panel out of PCB material alone.[145] Board dimensions outside the ordinary range, such as a board a metre long, restrict the design to the few fabs whose equipment can physically handle it.[508]

Electronics fabrication capability is closer to binary than mechanical fabrication: a shop either can place an 0105 package or cannot, and blind and buried vias have become common where they once were not, whereas mechanical suppliers vary continuously in equipment, engineering skill and quality control even when nominally able to make a part.[437]

## Home and in-house fabrication

Home fabrication schemes cannot change the economics while ten four-layer boards with solder mask and silkscreen cost about five dollars; the remaining case for making boards at home is turnaround measured in hours, not cost.[710] Home etching also carries a chemical disposal obligation that outsourced fabrication does not, which for many practitioners settles the question independently of cost or quality.[66]

Where home fabrication is practised, the details are settled empirically. For laser-printed artwork, tracing paper of 90 gsm or heavier is the better transparency medium: lighter paper crinkles passing through the printer's fuser and drafting film distorts, and two sheets stapled into an envelope register the two sides of a double-sided board.[224] Whether the capability is used at all turns on setup friction: with tanks left standing and heating started at the beginning of a layout session, a simple breakout board is finished within the same session, whereas equipment stored away is never worth retrieving against a two- or three-day commercial turnaround.[412] Home fabrication reaches a double-sided board on proper FR4 with drilled holes in about an hour, but not plated-through holes, which is the capability boundary that sends all but the simplest work to a fab.[251]

A milled prototype is not a fabrication-ready design: the layout must respect the mill's minimum feature and clearance, and a larger design is generally redrawn for the fab because the choices made for milling would not be made otherwise.[454] Prototypes are often deliberately kept in the two-layer, standard-thickness envelope so that the prototype resembles the production board; thickness below the default 1.6 millimetres, at 0.6 or 0.8, is a routine order, but layer count is where cost rises.[454]

## Industry structure

Geographic sourcing involves trade-offs beyond unit price. Overseas fabs can deliver the highest quality, but at a price that eliminates the cost advantage; normalised for turnaround and quality, top-tier domestic fabs are comparable, and matching a seven-day domestic delivery means paying for three-day service plus overnight shipping.[149] Choosing overseas manufacture by default ignores hidden costs; where a product's test procedure is technical and needs iteration to get right, a local facility at comparable pricing is the better choice, and pricing at good domestic shops can be close enough that proximity decides.[60] For low volumes, working the total through — shipping, delay and quality risk included — can make local fabrication cheaper as well as less troublesome than an overseas order.[239]

Schedules are bounded by the fabrication step, which cannot begin until layout is finished and cannot be compressed below the fab's turnaround plus shipping; contract assembly carries an arrangement lead time of five to ten days before anything is built, so a schedule of days rather than weeks forces in-house hand assembly regardless of volume, and in one ten-day build a board manufactured overnight in Taiwan and flown in was the only way the schedule survived.[16]

Domestic capacity in some countries has contracted severely. Australia was reduced to a single bare-board manufacturer, which survived on government contracts at prototype pricing of the order of a thousand dollars a board; defence and in-country sourcing requirements, rather than commercial demand, are what keep such a fab alive.[567] Domestic capacity can also return by acquisition rather than new investment: a New Zealand fab relocating to Australia restored a general-purpose bare-board option alongside the single remaining high-layer-count specialist.[555] As designs grow more demanding, the set of board houses qualified to build them shrinks, and procurement rules requiring two or three competitive bids then route every job back to the same few suppliers, so the formal competition becomes nominal.[567] Losing domestic prototype fabrication costs iteration speed, not just supply security: much product innovation originates on the manufacturing side, so a team that hands the design over a wall gives up the feedback from watching it be built.[699]

Ownership of the remaining Western fabrication and assembly shops rests largely with proprietors approaching retirement, which has driven a wave of private-equity roll-ups in board fabrication and assembly.[699] Vertical integration at scale has reappeared domestically as well: a satellite terminal producer runs bare-board fabrication, surface-mount assembly, functional test, injection moulding and box build on one site, shipping of the order of a thousand finished units a day.[720]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ | |
| 33 | Bob Widlar, Electronic Design, FIRST Robotics - Monday, Meta Monday | https://theamphour.com/the-amp-hour-33-monday-meta-monday/ | |
| 60 | An Interview with Joe Grand - Pancyclopaedic Prototyping Polymath | https://theamphour.com/the-amp-hour-60-pancyclopaedic-prototyping-polymath/ | |
| 66 | Magnets, China & IEEE - Xenomorphic Xerox Xebec | https://theamphour.com/the-amp-hour-66-xenomorphic-xerox-xebec/ | |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ | |
| 74 | Younker Youtube Yarling | https://theamphour.com/the-amp-hour-74-younker-youtube-yarling/ | |
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 121 | An Interview with Zach Hoeken Smith - Creative China Commorant | https://theamphour.com/the-amp-hour-121-creative-china-commorant/ | November 11, 2012 |
| 131 | An Interview with Andrew Seddon - Necessary Networked Novelty | https://theamphour.com/the-amp-hour-131-necessary-networked-novelty/ | February 4, 2013 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 140 | Project Management, Lasers & Robots - Staunch Specialty Sanctanimity | https://theamphour.com/the-amp-hour-140-staunch-specialty-sanctanimity/ | April 8, 2013 |
| 143 | PCBs, Tektronix & Ham Radio - Habitual Handicraft Hangups | https://theamphour.com/the-amp-hour-143-habitual-handicraft-hangups/ | April 29, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ | April 21, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 341 | All the way with DLJ | https://theamphour.com/341-all-the-way-with-dlj/ | |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 379 | An Interview with John Saunders | https://theamphour.com/379-an-interview-with-john-saunders/ | February 11, 2018 |
| 393 | I've bitten myself | https://theamphour.com/393-ive-bitten-myself/ | May 20, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 437 | An Interview with Chrissy Meyer | https://theamphour.com/437-an-interview-with-chrissy-meyer/ | April 7, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 504 | This Is Just A Tribute | https://theamphour.com/504-this-is-just-a-tribute/ | August 9, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 555 | Timing is Everything | https://theamphour.com/555-timing-is-everything/ | August 30, 2021 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ | |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ | November 20, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 663 | Motors on PCBs with Carl Bugeja | https://theamphour.com/663-motors-on-pcbs-with-carl-bugeja/ | March 25, 2024 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 692 | Like a steam engine in your house | https://theamphour.com/692-like-a-steam-engine-in-your-house/ | April 15, 2025 |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ | July 31, 2025 |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ | December 6, 2025 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
| 720 | Hyper Growth and OpenClaw Interns | https://theamphour.com/720-hyper-growth-and-openclaw-interns/ | March 31, 2026 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
