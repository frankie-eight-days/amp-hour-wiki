---
title: PCB Lead Time
concept: pcb-lead-time
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**PCB lead time** is the interval between the release of fabrication data for a printed circuit board and the delivery of the finished board, and it is the dominant commercial variable in prototype and small-volume circuit board procurement. For most circuit board fabrication the price-defining variable is turnaround time rather than board complexity, layer count, hole count or the geography of the fab: a board wanted tomorrow costs a great deal and the same board wanted in two months costs almost nothing.[163] For prototype boards the purchasing criteria are cost and lead time, with quality treated as almost secondary.[149] Lead time matters beyond price because it sets the hardware iteration cycle — the "compile time" of a board is measured in weeks depending on what is paid — and because it must be sequenced before assembly in any project schedule, since the board cannot be built until it physically exists.[170][16]

## Pricing structure

The relationship between price and turnaround in prototype fabrication is steep enough that the ordering interface is best framed as a price-versus-time slider rather than a specification: very complex boards can be obtained for almost no money if the buyer accepts a two-month wait.[163] The same four-layer board can be quoted at a twelve-day standard turn, an eight-day expedited turn, or a one-day turn costing on the order of a thousand dollars, making the turn selected the dominant term in the price.[16] Adding layers costs both money and schedule: moving from four to six layers adds an extra day or two, and on most projects the time is the more expensive of the two.[682]

Around 2011 a double-sided prototype board from a quick-turn fabricator ran about ninety dollars delivered in three or four days, and a two-layer prototype board at around ninety dollars on a claimed four-day turnaround was the going quick-turn offer from small regional fabricators in the early 2010s.[78][79] Pooled low-cost fabrication at that time was quoted at four to six cents per square inch plus roughly a hundred dollars of tooling, with a claimed three to four day turnaround, making the tooling charge rather than the board area the dominant cost on a prototype.[100] The cost and time of a prototype board subsequently fell from weeks and thousands of dollars in the late 2000s to under a week and about fifty dollars.[626]

Quoted manufacturing time is a ceiling rather than an estimate at some fabricators: a five-to-seven-day quote has been met in about two days before the shipping notice was issued.[468]

## Expediting

At the extreme of the price-versus-time curve, twenty-four-hour turns on multilayer boards have been bought at two to three thousand dollars apiece in commercial practice.[83] An eight-layer board turned in twenty-four hours sits at the edge of what is physically achievable, requiring every material step to go perfectly and leaving no margin for a materials problem.[83][227] Quick-turn prototype assembly quotes of five boards at twelve hundred dollars plus parts, shipping in three days, illustrate the going rate for compressing fabrication and assembly into a single short turn.[563]

Paying an expedite premium is justified only by a demonstrable downstream need for the board on that date; expediting because the work feels urgent produces the common outcome of having paid for speed that was never used.[145] The characteristic waste in expedited fabrication is discovering after delivery that the schedule would have tolerated the standard turn.[83] The mechanism behind the expedite premium is queue displacement: the expedited job is inserted ahead of other work already scheduled, and domestic quick-turn assembly houses charge a large premium — on the order of three thousand dollars above parts cost for a three-day job — because meeting the date requires displacing other customers' jobs on the line.[468]

Where engineering hours are expensive, buying fast board and mechanical prototype turns is the cheaper option overall, because the hours saved waiting exceed the expedite fee and clients optimising for time to market value it directly.[487] In an electronic design automation vendor's in-house hardware group, large eight-layer prototype boards costing thousands of dollars each were ordered freely and sometimes turned in twenty-four hours at double or triple the standard price, on the reasoning that a new concept could then be spun quickly.[652]

Paying for an expedited turn does not guarantee it: a high-specification board at four-mil trace and space with a BGA, bought at a three-to-four-day turn for around ten thousand dollars, arrived in four weeks, while a parallel low-cost order placed as a hedge arrived first and was used instead.[693]

## Batch and panel pooling

Batch or panel-pooling fabrication services place a submitted design into whatever spare space the next scheduled panel has, so the quoted turnaround is not a firm commitment but a function of when that panel runs.[33] A pooled-panel service has placed boards on a panel the same day they were submitted and delivered in about two weeks typically; sitting on the most commonly ordered panel option, such as the standard two-layer board share, moves an order through faster than an unusual specification.[337] Low-cost Chinese fabricators also pool customer designs onto shared panels, but do so silently, quoting a board price rather than disclosing the board share.[337]

A pooled-panel service operating from United States fabs, run by Laen, reported an average order-to-shipment time of eight days, putting boards in a domestic customer's hands in roughly ten days with priority shipping.[149] That service chose domestic fabs over Chinese ones on speed and quality: Chinese fabrication at the time meant waiting a month or more, with roughly one board in four failing.[149] Matching a seven-day domestic delivery through a Chinese fab requires buying a three-day turn and overnight shipping, which erodes the nominal cost advantage of offshore fabrication.[149]

A fabrication service whose demand outgrows its capacity begins to miss its own published turnaround: an eight-day standard turn that had been met reliably slipped as volume grew, and prices were raised to bring demand back into balance with capacity.[79]

## Quoting conventions

Turnaround should be quoted in calendar days rather than business days, because business-day definitions are renegotiated once an order is running late; one fabrication service, PCB:NG under Jonathan Hirschman, adopted a twelve calendar day turn for that reason.[299] A business-day turn placed just before a weekend absorbs the non-working days as well, so a three-day turn ordered on a Saturday delivers no sooner than one ordered on the following Monday.[391]

A fabricator's upload preview that renders only top and bottom copper regardless of the stack-up will not flag missing inner-layer files, so the omission surfaces a day later as an email from the fab and costs a further day or two across time zones.[434] Any query raised during fabrication adds about two days to delivery, because the exchange crosses time zones and each round trip costs most of a working day at each end.[428]

## Assembly lead times

Fabrication lead time and delivery must be sequenced before assembly in a project schedule; arranging a contract manufacturer alone takes five to ten days, which can rule out outsourcing on a short deadline and force an in-house build.[16] On a build with roughly ten days available, the schedule was met by fabricating bare boards overnight in Taiwan because no local fabricator was fast enough, and by hand-building twenty assemblies in house.[16]

A contract assembler's low-cost service ran fifteen business days, with a five-day service priced higher because both the bare boards and the components have to be expedited to hold that date.[243] An integrated quote-and-build service delivered a board three days from the completion of design, which is unattainable through a traditional contract manufacturer because a conventional CM cannot return a quote within an hour.[411] One quick-turn assembly service shipped about eighty-one percent of orders placed on its fastest lead time within roughly three days of file upload, covering fabrication, assembly and everything required to get the order out of the door.[699]

Conventional electronics manufacturing services carry two to three month order lead times, and complex programmable parts have been seen at six to twelve month delivery because the distributor places the order with the semiconductor fab only on demand; meanwhile the rest of the bill of materials accumulates at the assembler as tied-up cash.[699] A single missing component halts an entire assembled board, making a stalled order a visible physical manifestation of trapped cash on the production line.[699]

A hand-assembly house returned a populated box of boards in under two weeks from the point at which parts were drop-shipped and inspected boards sent, including weather disruption; hand-placing 0402 parts under a microscope carries a large surcharge over machine placement.[87]

## Logistics

With low-cost offshore fabrication the dominant term in delivered lead time is shipping rather than fabrication, with express shipping available as the lever; two-dollar boards have arrived in five days.[462] A nominal four-day fabrication turn from a Chinese board house amounts to a solid two weeks once shipping is counted, and a re-spin adds another two weeks to that cycle.[541]

Customs clearance is an unpredictable component of delivered lead time that cannot be committed to a customer: the same importer saw shipments cleared in seven days on some occasions and seven weeks on others.[661] A change in customs inspection policy can add delay to an established route without any change at the fabricator; a batch service that shipped three days after order took about a week in transit from Hong Kong, extended by newly increased inspection of packages from that origin.[33]

Carrier disruption is a schedule risk independent of the distributor or fabricator, and there is no practical recourse: a two-day distributor delivery ran to six days through a courier failure, and a weather event at a courier hub cost a week beyond the one day announced.[693] Unannounced carrier delays break every downstream schedule that was built on the promised transit time.[619]

Collecting boards in person from a nearby fabricator saves a business day, and in a startup schedule one business day can translate into three real days of delivered outcome.[305]

## Failure modes and hedging

Boards that arrive after the design has already moved on are wasted: a five-week delivery arrived after the design had been revised, so the boards were never built up.[79] A two-week wait has a cost beyond the schedule: motivation for the project decays across the gap and the work is deferred in favour of whatever is currently in front of the engineer.[234] Even a perfectly sequenced prototype cycle carries about a two-week wait unless hundreds of dollars in rush charges are paid, because the logistics of ordering parts, fabricating and shipping cannot be compressed further at standard rates.[234]

Where a hard date depends on an expedited board, placing a low-cost order in parallel provides a fallback that costs little relative to the expedite fee.[693] Receiving and validating components in hand before releasing the board to assembly costs about two days up front and avoids losing two weeks at the back end, which is what a re-spin costs when the assembler discovers a part was never in the kit.[541]

Specifying an exact calculated component value rather than a range can force a part with a twenty-week lead time; a quoting system that suggests in-range substitutes where no specific part number is mandated removes that self-inflicted delay.[243]

## Component lead times

### Stock dynamics

The classic forty-week semiconductor lead time reflects a build that starts from bare wafers rather than from stock.[367] Before online distribution, local distributors carried no stock and quoted lead times as long as forty weeks for ordinary parts.[231] A vendor whose parts sample freely but ship on forty-week lead times becomes a design-in hazard, and several large companies responded with a blanket internal rule against using that manufacturer's parts.[44] Restarting a semiconductor fab after a shutdown takes long enough that part lead times ran thirty to forty weeks afterwards, which is why high-volume design requires parts with second and third sources rather than parts that are merely available today.[5]

Distributor stock is not reserved: a part checked as in stock can be gone between the check and the order, converting an off-the-shelf part into a twelve-week lead time.[287] Quantities should be quoted early, because crossing the distributor's stock threshold moves the order to the manufacturer and brings manufacturer lead times and minimum order quantities with it.[367] A part that is cheap and in stock may be cheap because stock is being cleared ahead of end of life; manufacturers schedule production from demand trends, so a part on a declining trend is precisely the one that later returns a twelve-week lead time.[210] Build-to-order finished goods carry reorder lead times of about two months because the supplier holds no stock, so stock-out planning has to run two months ahead of demand.[287] Distributors began shipping partial quantities against orders — a hundred delivered against five hundred ordered, with the balance uncertain — so component tracking has to model split shipments and revised delivery estimates rather than a single receipt.[542]

### Shortage conditions

Just-in-time supply is sound only while lead times stay bounded; the model fails outright when lead times stretch towards a year.[408] A small manufacturer ordering an eclectic mix of parts through distributors encountered lead times as long as sixty-two weeks during the shortage period.[429] During the 2021 shortage even basic through-hole components such as standard indicator light-emitting diodes took three to four months to obtain.[570] Parts in specialised footprints have no substitution path when they become unavailable, so the only remaining response is to redesign them out of the board.[530] Component vendors whose minimum interesting order is around a million units quote both high prices and long lead times — eighteen weeks in one case — for ten-thousand-unit orders, so ordering in small batches to control cash makes the pricing worse.[517]

Genuine second sourcing has become harder because packaging and footprints differ between manufacturers and are themselves protected; where no pin-compatible alternative exists, the available escape is often a higher-performance part from the same manufacturer, bought at a higher price to avoid a three-month wait.[104]

### Design-in practice

Lead-time management cannot be delegated to a turnkey assembler; availability has to be considered while the product is being designed.[197] Whether a part can be bought in production quantity, not whether a few are in stock, decides if it can be designed in: five units at a distributor are no help against a build of ten thousand facing a forty-week lead time.[366] A known eight-week minimum lead time is useful precisely because it is a hard constraint that resource planning cannot negotiate away.[298] At volume the lead time has to be designed in from the start: fifty light-emitting diodes on fifty thousand units cannot be sourced casually, carries at least a twenty-week lead time, and once half a million parts are committed the part can no longer be changed, so thermal and other qualification has to be complete before the order is placed.[502]

Key long-lead components are bought before the money for the build arrives when a campaign or order is pending, because parts costed at design time can be taken by another buyer in the interval, leaving the project holding a design it cannot build for twelve weeks.[176] Pre-purchasing every long-lead part is possible with enough planning horizon, and remains necessary because alternatives exist for most parts but a single unobtainable one stops the build.[372] Manufacturer advisories are a usable early warning: one letter advised customers to expect lead times stretching from a familiar two to four weeks out to six to eight weeks or more and to place orders immediately, and orders placed that week were quoted delivery two months out.[135] A component ordering rule can be automated only once it is stated explicitly — a reorder threshold set so that the replenishment arrives before stock runs out given the lead time — whereas the rule most commonly applied in practice remains an unstated judgement.[435] After a successful demonstration, the honest answer to when another unit can be built is the component lead time plus the debug time on the boards already made, which is why prototypes assembled from parts scavenged off other products create an interval in which the product cannot be reproduced.[328]

## Lead time and the design iteration cycle

Hardware iteration cycles run to weeks or months to get a board back, worse where shipping distances are long, and almost no automated checking is done before committing to fabrication; schematic checks run at commit time would be the hardware counterpart to software unit tests.[375] Remote manufacturing lengthens the feedback loop on subtle board faults such as a trace changing capacitance or resistance, because the lead time governs how long it takes for such errors to return to the designer.[132]

Iteration speed differs by roughly two orders of magnitude between board work and packaging work: a packaging house takes about three months to return parts where a board fabricator returns boards in about three days.[703] Custom silicon schedules slip against fixed external dates in a way board schedules do not: one design returned in mid-October to November against an August expectation, which matters when the deliverable is tied to a conference or a graduation date.[579] Long lead times shape the process a designer chooses, not just the schedule: overseas on-demand machining at a couple of weeks biases work towards parts that can be printed in house.[712] In regions without local supply the constraint on experimental work is planning horizon rather than money, since a needed item may be a month away and inspiration-driven work cannot wait that long.[248] On space hardware lead times are usually not the binding constraint, because parts are selected for suitability regardless of unit cost and are consequently already stocked at distributors.[349]

### In-house fabrication

Milling boards in house turned a single-sided board around in about twenty minutes and a double-sided board in about an hour, against a week or two from a fabrication shop; on Mike Grover's projects the value taken from it was the number of design iterations attempted, not the boards themselves.[454] The decision rule for in-house board fabrication is a learning-rate one: the machine earns its place when it compresses months of iteration into days, not when it beats the per-board price.[454] The financial form of the same decision is a crossover calculation: divide the cost of the machine by the cost of the expedited boards it would displace and establish how soon the crossover occurs before buying.[341] A vendor of benchtop assembly equipment published a return-on-investment calculator for that crossover, with the qualifying question being how much pain a ten-day wait for boards causes rather than the headline machine price.[686]

In-house milling is justified in narrow cases — largely ground-plane RF boards, in-house rapid prototypes, or runs of about ten boards — because commercially fabricated boards are cheap and fast enough to win elsewhere.[406] An in-house etching setup is worth having only if it is kept permanently ready, since the difference between tanks standing by and equipment that has to be unpacked decides whether it gets used; in practice it serves simple boards such as breakouts, with a local fabricator covering anything else in two to four days.[412] Same-day in-house board production earns its place where hands-on user-experience testing is needed, since that testing cannot begin until a physical board exists; at Cartesian Co the case was stronger when quick-batch boards in Australia cost around a hundred dollars rather than twenty.[260] The common requirement is a fully featured four-layer board with solder mask, silkscreen and plated-through holes within about a week; sub-day in-house turnaround answers a narrow set of needs rather than a general one.[710]

### Compressed cadences

A weekly prototype cadence was run by Vincent Himpe by pairing a three-day board turn with same-week parts and stencil supply: Gerber data out Friday evening to United States fabs that work weekends, parts ordered Monday for overnight delivery, a locally cut stencil in hours, and the pick-and-place programmed Tuesday morning so five to ten populated boards existed by Tuesday evening.[169] Fabricators that work through the weekend are what make a Friday-to-Tuesday prototype cycle possible.[169]

Bob Davidson maintained two routes deliberately in parallel: a pooled low-cost service at one to two weeks for hobby and low-priority work, and a domestic fab at five to seven hundred dollars for overnight or two-day turnaround on high-priority work, with the choice made per job rather than per shop.[232]

## Historical development

In 1980 a sub-eight-hour turn on a two-layer board of about three by two inches cost around fifteen hundred dollars, equivalent to roughly six thousand dollars later.[222] Before prototype fabrication services existed, a board cost eight hundred to a thousand dollars and took two weeks, on top of an internal paper purchase requisition process, which is why in-house etching that produced a board the same day was treated as a revolution inside companies.[341]

Cheap fast fabrication changed what a failed board costs: submitting a design once meant waiting months and paying hundreds or thousands before discovering an error, whereas affordable failure is what makes exploratory design viable.[673] The cost and time of a prototype board fell from weeks and thousands of dollars in the late 2000s to under a week and about fifty dollars, but hardware still has no zero-marginal-cost retry in the way software does.[626] Cheap fast iteration carries an unpriced externality in electronic waste, which is part of the argument for spending simulation effort instead of respins where high-speed or high-reliability requirements already justify the solver cost.[626]

## Seasonal and regional disruption

Chinese fabricators and component suppliers close for roughly two weeks over Chinese New Year, and the shutdown routinely catches projects that resumed on schedule after the western new year.[79] Western board houses shut for a couple of weeks over Christmas and the new year; on an offshore order the same shutdown is absorbed into an already long lead time and is less visible.[127] A job that would ordinarily take about a month cannot be planned as a month when it spans both the western holidays and Chinese New Year, because suppliers on both sides are absent for part of the window.[654]

Regional supply disruption recovers unevenly between fabricators rather than uniformly across a country, so capacity has to be checked per vendor: during one disruption some houses were delivering normally while others quoted eight weeks, and a four-to-five-day service moved out to ten days.[482] Board shipments continued out of a locked-down manufacturing region with roughly one to two weeks of added delay rather than stopping altogether.[587] When a disruption is announced after an order has already gone out, the decision to make immediately is what the real in-house deadline for the boards is and what cost tolerance exists for working around it; the alternative is to accept delivery whenever it comes.[587]

## Planning practice

Consulting practice is to obtain client approval before spending client money on expedited turnaround, telling them in advance what the acceleration will cost so the expense can be authorised rather than discovered; Dave Young states this as a personal rule.[409] A client's choice of the low-cost assembly route commits the consultant to roughly a month before boards return, which has to be sequenced against other clients' work rather than treated as idle time.[409]

The schedule risk in project work often sits before the work starts rather than in the build: the interval between a proposal and the decision to proceed consumes the slack, and the accumulated urgency is then paid for in one-week board turns and couriers.[135] Early-stage companies routinely underestimate manufacturing intervals, and an eight-week lead time discovered late is enough to undo a plan built without one.[130]

A fabricator can be asked to split a production run against a hard date: on Zach Fredin's builds one supplier accepted a customer-supplied partial reel, ran a hundred and twenty of five hundred boards immediately to meet a delivery commitment, and completed the balance on standard lead time without charging for the split.[330] Where lead times will not meet a committed date, saying so explicitly to the supplier is what opens the possibility of a partial run.[330]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ | |
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ | |
| 33 | Bob Widlar, Electronic Design, FIRST Robotics - Monday, Meta Monday | https://theamphour.com/the-amp-hour-33-monday-meta-monday/ | |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 78 | Alteritous Andy's Absquatulation | https://theamphour.com/the-amp-hour-alteritous-andys-absquatulation/ | January 16, 2012 |
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 83 | Aggravating Agersia Agiotage | https://theamphour.com/the-amp-hour-83-aggravating-agersia-agiotage/ | February 19, 2012 |
| 87 | An Interview with Ian Daniher - Nascent Nonolith Numquid | https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/ | |
| 100 | Bonkers Birthday Badinage | https://theamphour.com/the-amp-hour-100-bonkers-birthday-badinage/ | June 17, 2012 |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 130 | Boeing, PCBs & Startups - Awful Airplane Aeration | https://theamphour.com/the-amp-hour-130-awful-airplane-aeration/ | January 28, 2013 |
| 132 | Melbourne, Hackerspace & Calibration - Vacuuous Vortex Verification | https://theamphour.com/the-amp-hour-132-vacuuous-vortex-verification/ | February 11, 2013 |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 197 | Spacing Out On Space - Dave's Dongle Designing | https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/ | May 5, 2014 |
| 210 | Risky Components and Hardware Innovation - Slipshod Shack Shutdown | https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/ | August 5, 2014 |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 227 | Space Bound, Again - Xtreme Xtraplanetary Xenonosocomiophobia | https://theamphour.com/227-space-bound-again-xtreme-xtraplanetary-xenonosocomiophobia/ | December 8, 2014 |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ | January 6, 2015 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 234 | We'll Believe It When We See It - Hiring Hypercatalectic Helpelp | https://theamphour.com/234-well-believe-it-when-we-see-it-hiring-hypercatalectic-helpelp/ | January 27, 2015 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 248 | An interview with Greg and Tim of Backyard Brains - Boethetic Bug Brainwaves | https://theamphour.com/248-an-interview-with-greg-and-tim-of-backyard-brains-boethetic-bug-brainwaves/ | May 5, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 298 | Don't Turn It On, Don't Take It Apart | https://theamphour.com/298-dont-turn-it-on-dont-take-it-apart/ | May 11, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 305 | An Interview With Dave Young | https://theamphour.com/305-an-interview-with-dave-young/ | June 29, 2016 |
| 328 | The Ghost of Keyzermas Past | https://theamphour.com/328-the-ghost-of-keyzermas-past/ | December 21, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 341 | All the way with DLJ | https://theamphour.com/341-all-the-way-with-dlj/ | |
| 349 | An(other) Interview with Jon Oxer | https://theamphour.com/349-another-interview-with-jon-oxer/ | June 25, 2017 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 372 | Year End, 2017 | https://theamphour.com/372-year-end-2017/ | December 17, 2017 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 409 | Electronics Consultant Impedance Matching | https://theamphour.com/409-electronics-consultant-impedance-matching/ | September 30, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 429 | An Interview with Charles Alexanian | https://theamphour.com/429-an-interview-with-charles-alexanian/ | February 10, 2019 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15, 2021 |
| 541 | Chip Shortage Denier | https://theamphour.com/541-chip-shortage-denier/ | May 10, 2021 |
| 542 | Component Management with Jan Rychter | https://theamphour.com/542-component-management-with-jan-rychter/ | May 17, 2021 |
| 563 | Grumpy Collaboration | https://theamphour.com/563-grumpy-collaboration/ | October 24, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 673 | Lifelong Learning with Bitluni | https://theamphour.com/673-lifelong-learning-with-bitluni/ | July 15, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 693 | Small Scale Electronics Manufacturing with Colin O'Flynn | https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/ | May 13, 2025 |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ | July 31, 2025 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ | December 6, 2025 |
| 712 | Robots Everywhere with Aaed Musa | https://theamphour.com/712-robots-everywhere-with-aaed-musa/ | January 19, 2025 |
