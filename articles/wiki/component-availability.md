---
title: Component Availability
concept: component-availability
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Component availability is the question of whether a chosen electronic part can actually be purchased in the quantity and timeframe a design requires. Whether an integrated part can be bought in production quantity, rather than its electrical merit, often decides whether it can be designed in: a distributor showing five units in stock is useless for a build of 10,000 when the factory lead time is 40 weeks.[1] Accepting an electrically sub-optimal component that is in stock is therefore often the correct engineering choice over a better part that has a questionable supplier or cannot be obtained.[145] Optimising a design involves simultaneous pressure from cost, power, package and availability, so part selection cannot be reduced to a single objective.[633]

## Availability as a design constraint

For a new analogue application many op amps typically meet the specification, so selection is decided by cost, availability and package type rather than by performance alone.[62] Locating an ideal component is only the first hurdle; the immediate follow-up checks are whether it can be bought at all and whether its price is acceptable, since an otherwise perfect part may be sold out worldwide.[524] Obtainability is likewise part of the definition of a jellybean component: a part that can no longer be bought ceases to qualify regardless of how standard its function is.[567] A part manufactured by many independent vendors is effectively immune to stock-out; the 555 timer, second-sourced by numerous manufacturers, can always be bought somewhere unless a designer insists on one specific brand's version.[16]

Substitution is rarely a local swap. Replacing a 10-cent chip that cannot be sourced with a 50-cent alternative forces changes to the surrounding circuitry and repeated bill-of-materials rework to recover cost.[1] Reusable modular PCB-level building blocks tend to break down in practice partly because they carry parts the reusing designer cannot obtain easily or cheaply, on top of form-factor, power and voltage mismatches.[25] Restricting a design to components anyone can buy on the open market in single quantities is what makes it self-buildable, a constraint that distinguishes hobbyist-reproducible hardware from designs relying on parts sold only under volume contracts.[97]

For products intended for sale rather than experimentation, off-the-shelf integrated parts that are already characterised over temperature win on time to market against discrete implementations, provided they can be bought in quantity.[366] Filter design tools expose the resistor and capacitor E-series as a selectable input because the chosen series directly determines how difficult the resulting component values will be to obtain.[392] Accepting weaker performance from an amplifier already held in inventory can be the right trade when the application's requirement is modest, since it avoids adding another part to stock.[392] Minimising distinct BOM line items is a design goal for kit and small-batch products, because every line item adds kitting labour and one more part that can become unobtainable.[229]

The economics of custom silicon are set against a distribution catalogue offering hundreds of thousands of characterised, tested parts at roughly a dollar each, which is why building a bespoke device rarely competes with buying a 50-cent microcontroller.[129] Semiconductor vendors also publish an aggressively priced headline part with minimal peripherals and charge steeply for the variant with the feature actually required, so a 25-cent 32-bit microcontroller can become a two-dollar part once a 12-bit rather than 10-bit ADC is needed.[98]

## Sourcing during design

Component selection commonly begins with a parametric search on distributor websites, restricting candidates to parts that can actually be purchased from Digi-Key or Mouser before any electrical evaluation.[95] Checking distributor stock as the first step of design is practised in large companies as well as small ones, because prototype schedules measured in weeks collapse if the chosen part cannot be delivered.[95] For niche production volumes in the thousands, one workable approach is to plan the whole project around parts confirmed in stock at several independent distributors, treating multi-distributor stock as a precondition for designing a part in.[197] Designing around the passives and transistors an assembly house already keeps loaded on its pick-and-place machines or in stock shortens build time and avoids sourcing risk, and is usually worth a small unit-cost penalty.[33]

Extended part-research phases can be self-defeating, because availability and pricing data go stale over the weeks spent gathering them and the selected parts may already be unobtainable by the time the search finishes.[16] Availability churns on a timescale of months, so a schematic revisited after a short interval typically requires re-selecting converter and charger ICs and re-running the whole BOM search for alternates on cost and stock.[128] Price and availability data captured at schematic entry are stale by the time a product ships, because a design cycle of around nine months is long enough for both to change completely.[545] Current distributor stock is a poor basis for a multi-year product, so sourcing decisions should be made against a forward risk profile rather than what happens to be listed at the moment of design.[451] A more durable sourcing signal than a stock snapshot is a supplier score built on historical on-time delivery performance, which survives the design cycle better than a spot availability figure.[545]

Part choices in large organisations are frequently made outside engineering, with purchasing departments overriding selections on the basis of component availability or supplier relationships.[137] A design handed to a contract manufacturer should already have its part availability resolved, including any equivalent-part substitutions, because post-handoff changes are where the contract manufacturer earns its margin.[255] A distributor's review of a BOM validates sourceability, shipping times and lead-time normality, and should not be mistaken for validation that the circuit works.[300]

## Distribution structure

Volume buyers concentrate purchasing on distributors that actually hold stock, since guaranteed availability outweighs catalogue breadth for parts needed in thousands.[5] Distributor selection during a shortage turns on stock position rather than brand: a distributor with no parts wins no business regardless of its name, and buyers will accept a higher unit price from whoever can actually ship.[12] When components are in short supply the purchasing decision inverts, with unit price becoming secondary to whether the part can be obtained at all.[12]

No distributor stocks the whole component universe; catalogue depth is tiered, with Digi-Key deeper than regional distributors and the Shenzhen component markets deeper still on price and sometimes on availability.[80] Distributors outside the largest markets hold progressively less local stock and ship from regional hubs, so an Australian buyer ordering from Farnell may wait for goods routed from Singapore even when the part shows as available.[80] Distributor choice for small orders is driven by delivery speed as well as price and stock; Mouser ships from a warehouse near Dallas, so US customers using even the cheapest ground option often receive orders the following day.[38] Local component availability can also be a function of trade access rather than technology: designers in Yugoslavia in the 1980s travelled roughly 1,000 kilometres to Munich to buy parts that are now sold domestically.[247]

A part listed by a distributor is not necessarily promptly deliverable; catalogue presence and lead time are separate questions, and a part orderable at the push of a button may still be weeks away.[277] Distributor listings showing a few hundred units shippable immediately typically carry a substantial price premium relative to normal supply.[362] A specialised variant of an otherwise common part, such as a microcontroller with an integrated LCD driver supporting an unusual segment count, may be absent from distribution simply because distributors decline to stock low-turnover variants rather than because it is discontinued.[360] Distributor search tools also do not let a user rank the whole catalogue by stock quantity; availability sorting works only within a product category, so finding the most-stocked part overall requires category-by-category inspection.[642]

Component library download counts follow a strong Pareto distribution, with roughly 20 percent of parts accounting for about 80 percent of downloads, which makes download frequency a usable proxy for identifying the jellybean part in a category.[531]

## Failure modes

A part can become unbuildable without being discontinued, because another buyer clears out distributor and factory stock, leaving the designer stranded on a current production part.[88] House stock at an assembly service behaves the same way: it is a live figure that another customer can exhaust in a single order, so a part shown as available while a design is in progress can disappear before the build is submitted.[700]

Distributor in-stock indicators are not reliable, with parts advertised as available proving not to be once an order is placed, so the flag should be treated as a claim to be confirmed rather than a guarantee.[545] Distributors will accept orders and payment for parts they cannot actually deliver, refunding the money later, so an accepted order is not evidence that stock exists.[600] A quoted lead time is likewise only an estimate until goods are physically received, since natural disasters and other disruptions can extend delivery after an order is accepted.[367] Buying on lowest price alone from unfamiliar sources is a risk many engineers only learn to weigh after being burned, which is why filtering distributor search results to in-stock parts from known suppliers has become routine.[564] Sourcing low-cost parts from consumer marketplaces carries a stock reliability penalty as well as a quality one: listings frequently cannot be fulfilled, and lots of a hundred warrant incoming inspection.[408]

The worst point at which to discover a supply problem is mid-build, when the assembly house reports it has run out of a part that is no longer in stock and carries a 16-week lead time.[197] Deferring component purchase until manufacturing begins is a common failure for low-volume projects, since parts that were listed at design time can be entirely unavailable, even in quantities of ten or a hundred, by the time the build is scheduled.[231] Poor part selection can strand a programme after prototypes are built: a military sonar project reached a multi-million-dollar prototype PCB whose components could no longer be sourced, leaving the team to patch hardware together purely to pass a customer milestone.[116] A board respin also cannot be executed on a 24-hour timescale unless the components are already on hand, making local parts inventory the limiting factor in emergency rework.[484]

Tying an open hardware platform to a single silicon vendor exposes every downstream design to that vendor's supply position; the Arduino's dependence on Atmel microcontrollers left derivative products unable to source parts until the software was ported to other microcontroller families.[43] Low-cost assembly services that fit their own stocked components force the BOM to be reworked for each build, because the same part numbers cannot be relied on to be in the house catalogue months later.[700]

A supplier's delivery record persists as a design constraint long after the underlying problem is addressed, because engineers who have designed in a part and then been unable to buy it carry the professional consequences and avoid that supplier on later projects.[129] Releasing new part numbers faster than a fab and test operation can support them produces chronic supply failure: Maxim introduced around 500 new devices a year in the 1990s and could not ship many of them.[326] Quoted lead times of around 50 weeks were reported for parts from suppliers with severe supply problems, a delay long enough to make a designed-in part effectively unavailable for a product cycle.[326]

## Managing supply risk

A BOM health risk assessment screens every line against component databases to flag parts that are not recommended for new designs, approaching end of life, single-sourced, or carrying long lead times, so those decisions can be corrected before they are locked in.[451] Global available quantity is a graded criterion in such scoring: a manufacturer part number with only a handful of units in worldwide inventory is materially riskier than one with millions, independent of its lifecycle status.[451] The recommended point for a supply risk review is roughly 80 percent through development, once the prototype functions, because early sourcing decisions cast long shadows but the BOM must exist before it can be graded.[451]

Identifying footprint-compatible cross-references and listing them as an approved vendor list gives the factory permitted drop-in substitutes, removing the sole-source dependency that arises when only one manufacturer part number is specified.[451] Defence work commonly required three qualified parts from three different vendors for a given BOM position, so that any of them could be substituted into production without requalification.[574] Where a device family spans graded variants, such as the 1N4004 through 1N4007 rectifiers differing only in voltage rating, listing every acceptable member against one BOM line lets any of them be fitted interchangeably.[574] Package and packaging suffixes on a shared base part number are treated by buyers as the same item, but a change of base part number is not, so an acceptable alternate with a different base number must be explicitly called out on the BOM as a valid replacement.[574]

Designing around genuinely multi-sourced components, or failing that around parts stocked by several distributors, is the standard defence against supply interruption, though simultaneous clearance of stock across every distributor can still defeat it.[455] Even at build volumes in the tens of units, consultants work backup alternatives into the design phase, since a single hard-to-get component can stop the boards being built at all.[568] Laying out several alternative footprints for op amps and memory devices on the same board, so that whichever device is obtainable can be fitted, is a design-for-availability technique that pandemic-era shortages made relevant again.[661] Deliberate second-sourcing of another vendor's catalogue is itself a commercial strategy built on that vendor's delivery failures, offering customers an alternate supply for parts they cannot reliably obtain from the original manufacturer.[129]

## Purchasing and inventory

Loading a complete BOM into a distributor account lets a repeat build be re-ordered in minutes at the correct quantities and part numbers, which for small production runs can justify buying everything from one, more expensive, distributor.[104] A stored distributor BOM also reports live stock against every line before the order is placed, surfacing shortages at the point of ordering rather than after the money is committed.[104] An export plugin for the EDA tool that formats the BOM to the assembler's specification and checks each line against the assembler's parts database moves the availability check into the design environment.[700]

Buying long-lead components up front, before contracts with a manufacturing partner are finalised, pre-empts the delay introduced by the partner's own purchasing cycle, by which time the parts may have gone out of stock.[197] Paying several times the normal unit price to a distributor that has stock is rational for a small manufacturer, because the premium is small against the cost of a stalled build and a missed delivery commitment.[197] Buying full reels ahead of demand nevertheless ties up substantial working capital, with a single reel of resistors costing on the order of 4,000 dollars and reels of 2,500 ICs bought at a time, and even that buffer is eventually consumed without warning.[231] Some components are not sold in one-off quantities at all, so incremental demand forces the purchase of a whole reel; an extra 1,000-piece reel at four dollars per part can be required to satisfy a single additional unit of demand.[177]

Low-volume turnkey assemblers restrict designs to their own stocked catalogue and waive the placement fee for in-house passives, while charging a placement fee for any component the customer supplies from outside.[236] Hands-off quick-turn assembly services in the United States can deliver assembled boards in under a week at a substantial price premium, but only if the components on the BOM are themselves available.[587]

Availability can also govern when a vendor adopts a new device generation. A small board vendor moving to a newer FPGA generation waits not only for density and price to be right but for supply to be loose enough that much larger customers are not consuming the entire allocation.[181] High-churn consumer product lines such as PC motherboards, which turn over roughly every six months, set their next design around whichever chips can be obtained at what price that week rather than around a fixed architecture.[126] Application processors aimed at low-cost consumer tablets turn over fast enough that a chipset can be unbuyable roughly two years after launch, forcing single-board computer vendors to maintain several hardware generations around successive chipsets.[389]

## Shortage cycles

Reports that a major distributor is out of an entire component category are usually overstated; ceramic capacitor shortages appeared as gaps at particular case size and voltage combinations rather than across the whole catalogue.[391] During a passive component shortage prices rise noticeably and designers searching on specific part numbers should expect to re-evaluate the requirement and select a different part rather than wait for the original.[391] Multilayer ceramic capacitors reached lead times of roughly 72 weeks, long enough that designing one in without checking supply could make a product milestone unreachable.[451]

Supply is uneven between vendors. Scraping distributor stock and grouping it by manufacturer during a shortage showed Microchip holding by a wide margin the most parts in stock,[587] while supply during the 2020s shortage was concentrated to the point that some manufacturers' catalogues were effectively absent from distribution for years at a time.[600] When a mainstream part such as the CP2102 USB bridge is stripped from distributor stock, clone versions from Asian suppliers remain obtainable at low prices, which trades supply certainty against unverified provenance.[587] The RP2040 remained purchasable in quantities of 500 through the shortage, which made availability itself a selection argument for the part.[607]

During the 2021 shortage, parts ordered for a production run could fail to arrive for over a year; an instrument build stalled on an NXP device and an STM32F0 ordered in March or April 2021 that had still not been delivered, exhausting the product's supply.[607] One response to extreme lead times is to order components for a product roughly a year ahead of production, before the design is even finalised, committing cash to inventory against a prototype that is still changing.[607]

Disruption extends beyond semiconductors. ESD foam sold through a distributor rose from about 20 dollars to about 57 dollars per sheet with shipping cost roughly doubling, a per-kit increase large enough to threaten a small kit business.[613] The parts that endanger a small hardware business during a shortage are often not the microcontrollers or passives but overlooked items such as packaging materials and specialist components like Geiger tubes that depend on a single import channel.[613] Component sourcing also consumes a growing share of a small manufacturer's operating time during a shortage, adding a labour cost on top of the higher component prices themselves.[613]

Fab capacity announced during a shortage takes roughly two to three years to come online, so publicly funded expansion offers no relief to a current sourcing crunch and may arrive into an oversupplied market.[598] New leading-edge fabs also do not relieve shortages of the commodity analogue and power parts most designs depend on, because those fabs are not built to produce simple devices such as voltage regulators.[598] Defensive pre-buying inflates the demand signal semiconductor vendors see, so order books overstate real consumption and the correction arrives as oversupply and cancelled forecasts once buyers' inventories are filled.[652] The semiconductor supply cycle duly reversed after the shortage, moving from scarcity to oversupply within a few years, with some component categories still constrained while the market overall loosened.[652]

## Long-lived products and repair

For a long-lived low-volume product, the loss of a component is usually what forces a redesign, since no other pressure is strong enough to justify reopening a design that still sells.[229] Relaunching a discontinued product line built on older analogue ICs such as the 8038 function generator and bucket-brigade delay devices requires partial redesign, because the surviving catalogue dictates what compromises are possible.[263]

Availability is also a lever in the repair market. Withholding service parts forces replacement purchases: independent repair firms handling equipment such as endoscopes found spare components no longer supplied, obliging hospitals to buy new units.[507] Publishing schematics does not by itself make a product repairable if the components in them cannot be purchased or are serialised to the original unit.[534]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 1 | What's In A Name? | https://theamphour.com/1-whats-in-a-name/ |  |
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ |  |
| 12 | Dave Is Back And Blogging! | https://theamphour.com/the-amp-hour-12-dave-is-back-and-blogging/ |  |
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ |  |
| 25 | NASA, WOTW & Modular Design - The NASA Nostalgia | https://theamphour.com/the-amp-hour-25-the-nasa-nostagia/ |  |
| 33 | Bob Widlar, Electronic Design, FIRST Robotics - Monday, Meta Monday | https://theamphour.com/the-amp-hour-33-monday-meta-monday/ |  |
| 38 | An Interview with Jeff Keyzer - Comical Keyzer Comes a-Callin' | https://theamphour.com/the-amp-hour-38-comical-keyzer-comes-a-callin/ |  |
| 43 | An Interview with Jeff Keyzer and Jeremy Blum - Audacious Arduino Arguments | https://theamphour.com/the-amp-hour-43-audacious-arduino-arguments/ |  |
| 62 | Op amps, Microchips & Mergers - Narquois Nerd Nescience - Narquois Nerd Nescience | https://theamphour.com/the-amp-hour-62-narquois-nerd-nescience/ |  |
| 80 | Otiose Ontocyclic Opiniasters | https://theamphour.com/the-amp-hour-80-otiose-ontocyclic-opiniasters/ | January 29, 2012 |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 95 | An Interview with Øyvind Janbu - Feracious Fabless Facilitator | https://theamphour.com/the-amp-hour-95-feracious-fabless-facilitator/ |  |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ |  |
| 98 | Proemial Passive Poiesis | https://theamphour.com/the-amp-hour-98-proemial-passive-poiesis/ | June 3, 2012 |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 116 | Distribution, Wozniak & Robots - Early Eight-bit Endgame | https://theamphour.com/the-amp-hour-116-early-eight-bit-endgame/ | October 7, 2012 |
| 126 | eReaders, datasheets & board assembly - Yearly Yeasty Yapping | https://theamphour.com/the-amp-hour-126-yearly-yeasty-yapping/ | December 17, 2012 |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 129 | An Interview with Brett Fox and Dr Jeroen Fonderie - Device Doubling Decretum | https://theamphour.com/the-amp-hour-129-device-doubling-decretum/ | January 21, 2013 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 177 | Discussing Innovation and the Future with Mike Ossmann - Fiesty Festivus Futurology | https://theamphour.com/177-discussing-innovation-and-the-future-with-mike-ossmann-fiesty-festivus-futurology/ |  |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ |  |
| 197 | Spacing Out On Space - Dave's Dongle Designing | https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/ | May 5, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 231 | Supply Chain Woes And Wares - Nonplussed Neotechnic Nithing | https://theamphour.com/231-supply-chain-woes-and-wares-nonplussed-neotechnic-nithing/ | January 6, 2015 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 247 | An Interview with Voja Antonic - Gerontogenous Galaksija Genesis | https://theamphour.com/247-an-interview-with-voja-antonic-gerontogenous-galaksija-genesis/ | April 29, 2015 |
| 255 | Inspirations and Aspirations - Recanting Rocket Rationale | https://theamphour.com/255-inspirations-and-aspirations-recanting-rocket-rationale/ | June 24, 2015 |
| 263 | An Interview with Fran Blanche | https://theamphour.com/263-an-interview-with-fran-blanche/ | August 19, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 300 | Three Hundred Down, Three Hundred To Go | https://theamphour.com/300-three-hundred-down-three-hundred-to-go/ | May 25, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 360 | A Total 360 | https://theamphour.com/360-a-total-360/ | September 18, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 392 | An Interview with Matt Duff | https://theamphour.com/392-an-interview-with-matt-duff/ | May 13, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 451 | An Interview with Scott Miller (2nd) | https://theamphour.com/451-an-interview-with-scott-miller-2nd/ | July 21, 2019 |
| 455 | Bill and Dave's Excellent Equipment | https://theamphour.com/455-bill-and-daves-excellent-equipment/ | August 19, 2019 |
| 484 | Man Behind The Curtain | https://theamphour.com/484-man-behind-the-curtain/ | March 16, 2020 |
| 507 | Right To Repair with Louis Rossmann | https://theamphour.com/the-amp-hour-507-right-to-repair-with-louis-rossmann/ |  |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 545 | Fear of Banjos | https://theamphour.com/545-fear-of-banjos/ | June 6, 2021 |
| 564 | Pavlovian Cheapskates | https://theamphour.com/564-pavlovian-cheapskates/ | October 31, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 568 | YouTube to Consulting with Florin of Voltlog | https://theamphour.com/568-youtube-to-consulting-with-florin-of-voltlog/ | November 28, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 598 | Best way to find a leak | https://theamphour.com/598-best-way-to-find-a-leak/ | August 7, 2022 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 633 | Engineering Optimization | https://theamphour.com/633-engineering-optimization/ | May 22, 2023 |
| 642 | Sad Violins for Superconductors | https://theamphour.com/642-sad-violins-for-superconductors/ | August 13, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
