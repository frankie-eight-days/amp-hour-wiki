---
title: Digi-Key
concept: digi-key
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Digi-Key is a United States-based catalog distributor of electronic components, holding large physical inventories and selling in small quantities to design engineers, prototypers, and low-volume manufacturers.[7][699] Catalog distribution of this kind functions as a gate on component selection: a part that cannot be bought in prototype quantities from a major catalog distributor will not be designed into products, because prototype builds cannot be supplied.[44] Digi-Key is the largest of the catalog distributors, and unlike some competitors it does not sell placement in its search results.[546] Its catalogue listing has become a de facto test of whether a component exists at all, in that an announced device is treated as unreal until it can be ordered from a catalog distributor.[370]

## Position in the component supply chain

The distribution industry operates in tiers that perform different functions. Catalog distributors such as Digi-Key hold large physical inventories and sell in small quantities, whereas the large authorised distributors increasingly hold little or no stock and operate principally as financing intermediaries between manufacturer and customer.[699] Distribution is a thin-margin, high-churn business: an annual report showing a billion dollars of revenue against roughly fifty million dollars of profit implies a net margin around five percent, and the model depends on volume.[128]

For a semiconductor supplier, being listed by a catalog distributor is a negotiated relationship rather than a form submission. The courtship takes several months, during which the supplier must satisfy the distributor that it will be a viable line; the distributor buys reel quantities up front because its model depends on shipping from its own stock anywhere in the world within about forty-eight hours, which is defeated if it has to call the manufacturer for each order.[129] A semiconductor startup that launches without distributor listings forecloses its own design-ins regardless of the merits of the part.[44]

Listing also removes a procurement barrier unrelated to the product itself. Large customers hold blanket purchase orders with catalog distributors, so buying equipment through the distributor bypasses the customer's approved-vendor process entirely; for a small supplier, being listed is what makes the purchase possible at all.[527]

## Parametric search and part selection

Distributor parametric search is the ordinary first step in part selection for a design engineer, resolving the search about ninety-five percent of the time before manufacturers' own sites are consulted.[129] The tool has defined limits. Its filters cover catalogue attributes rather than application requirements, so a search for an unusual specification — such as a charger for a very low-capacity cell, outside the several-hundred-milliamp to several-amp band where most parts are made — has to be conducted on manufacturers' sites instead.[46] The sheer scale of the device space also defeats catalogue filtering on its own: one survey of analog-to-digital converters counted 2,412 devices from 24 manufacturers, roughly a hundred parts per manufacturer, which is why distributor filters cannot substitute for manufacturer selection guides.[191]

Parametric searches on both distributor and manufacturer sites silently omit parts that would have qualified, so a result set should be treated as a sample rather than an exhaustive list; an experienced colleague naming a part they have already used remains the faster route.[88] Faced with thousands of qualifying results, the common resolution is to sort by price and take the cheapest, a shortcut that reliably selects a poor part. Two heuristics reduce the field more usefully: pin count implies feature set, since a three-pin regulator physically cannot have a shutdown input, and filtering by manufacturer uses brand as a proxy for trust.[68]

A designer without corporate part-approval constraints can invert the selection process entirely and design only around parts currently in distributor stock, which removes obsolescence risk from the design and lets components and bare boards be ordered at the same moment. The same inversion at the level of cost — sorting a low-cost catalogue by price to find a one-cent regulator and a three-cent microcontroller — generates the product concept from the achievable bill-of-materials cost.[135] Processor selection for a cost-sensitive product can likewise be made directly from the listing by taking the cheapest part meeting the requirement, with the caveat that which device holds that position changes over time.[316]

## Pricing

Catalog distributor prices carry a premium that pays for holding stock and breaking bulk, so a part listed at ten dollars may be three or four dollars bought in volume direct. The premium collapses at reel quantities: a reel of five thousand parts costs about the same from a catalog distributor as from the manufacturer, and the gap only reopens at volumes on the order of a million.[5] Single-piece price curves are steeper for FPGAs than for other devices, with single-unit prices around a hundred and fifty dollars, because holding cost is high and single-quantity demand is low; some manufacturers additionally restrict volume distribution to one authorised distributor for export-compliance reasons, so the catalog listing exists for prototypes while production goes elsewhere.[466]

Per-line handling charges dominate small builds in a way unit prices conceal: a reeling charge of about seven dollars per part is unremarkable once, but a design with fifty unique parts adds several hundred dollars, and international shipping on a handful of modules can double their effective unit cost.[508] Published price breaks also stop well below production quantities, so a buyer needing one thousand to a hundred thousand pieces must request a quote by email and wait days, even though the pricing follows a formula the distributor could apply instantly against a logged-in account.[102]

Because catalog pricing is the conservative bound, the recommended costing method for a new product prices the bill of materials at catalog distributor rates and assumes local assembly, then applies the conventional three-to-four-times margin multiplier. Any saving obtained later by moving manufacture offshore is upside rather than a requirement, whereas a plan that assumes lowest-cost offshore manufacture from the outset leaves no options if that route becomes unavailable.[113] A standard-cost convention makes bill-of-materials estimates comparable: the thousand-piece distributor price is recorded as a field on each part in the design tool and used as the budgetary figure handed to a client, on the explicit understanding that it is not what will be paid and that shipping and other loadings sit on top.[542]

## Purchasing and inventory workflow

A bill of materials kept in a spreadsheet is obsolete the moment it is finished and cannot express the things that actually govern purchasing: multiple currencies across a multinational supply chain, minimum order quantities, order multiples, parts shared between projects that should be bought together, and approved substitutes. A database-backed tool defers the choice between substitutes to the moment of ordering, so the decision is made against what the market actually has that day.[542] The purchasing workflow that follows is a cart of several bills of materials multiplied by their build quantities, collapsed into a combined purchase list that still holds unresolved meta-parts; the offers available at that moment are then selected from, manually or by rules such as preferring one distributor and falling through to others on unavailability, and only then does the list become an order for specific part numbers.[542]

Component inventory management keys on distributor barcodes: scanning a bag recovers the manufacturer part number and, from modern two-dimensional codes, the quantity, but never the storage location, so a location scheme remains the operator's responsibility. Embedding order-specific identifiers in the purchase order closes the loop, because the labels printed on despatch then identify the line item and quantity on receipt.[542] The discipline that makes such a system work is that unrecorded parts are treated as lost, since they will not be found and will be bought again; after an initial indexing effort, maintaining it costs a few minutes per order.[542]

Loading a complete bill of materials into the distributor's own system turns reordering into a single operation that computes the correct quantities and reports live stock availability against every line before the order is placed, which is the practical argument for concentrating a build's purchasing with one supplier even at a higher unit price.[104] Because part numbers differ by packaging, two bills of materials are commonly maintained for the same design: a production version specifying reels and a short-run version specifying cut tape for hand assembly.[174]

## Stock data as market intelligence

Publicly visible distributor stock levels function as market intelligence. A stock figure that never moves is evidence that a product sold nothing, and scraping catalogue stock across vendors produces a picture of which manufacturers actually have supply.[306] During a shortage, however, aggregate catalogue stock figures are misleading, because sorting a manufacturer's parts by stock level surfaces exactly the lines that are well supplied rather than the ones that are short; a shortage has to be diagnosed part by part.[541]

Parts shown as on order are not reserved: another buyer can take the whole incoming quantity before it lands, so a promised arrival date carries no entitlement, and committing cash early to hold a position is a cash-flow problem rather than a guarantee. Stock that appears can also be gone within minutes of being noticed.[541] Distributors forward obsolescence notices to customers who have bought an affected part, but the more reliable practice is to re-quote the whole bill of materials every few months, since the quoting process itself surfaces parts that have become unbuyable.[382]

## Volume limits and lead times

Catalog distributor stock is not a production supply. A few thousand parts looks abundant to a designer but is consumed immediately once multiplied by parts per board and boards per run, and past a modest volume threshold the only route is buying reels directly from the manufacturer; quantities on the order of a million cannot be bought through distribution at all, with the partial exception of the cheapest passives.[645] Within a build, an assembly run cannot begin until every line on the bill of materials is in hand, so a single backordered passive stops the entire job regardless of the value of the part.[411]

Lead time on a needed part is often identical at the distributor and at the manufacturer, and no volume commitment buys priority; the answer given to a customer asking to be moved up the queue is to plan further ahead next time.[389] The floor on semiconductor lead time is structural rather than commercial: roughly thirty days of wafer processing, then shipment to another country for packaging, then further test, then distribution, which makes six weeks an optimistic minimum even before material for the wafer starts is considered. A demand surge propagates through that chain the way a traffic jam clears, in stop-start waves rather than smoothly.[502]

Semiconductors developed to one large customer's requirement were historically released into general distribution afterwards, so the repair trade could buy them; increasingly they are not, leaving no legitimate supply at all, and the resulting practice in the repair trade of buying new assemblies purely to remove one chip and discard the rest is the cost of that closure.[507] At the other end of the lifecycle, semiconductor manufacturers keep decades-old parts in production because a design that specified one twenty or thirty years ago still needs supply, and the continued catalogue listing of long-obsolete devices is the visible result of that obligation.[520] Catalogue searches also settle questions about package obsolescence empirically: filtering the distributor's chip listings by through-hole packages returns tens of thousands of parts, a figure that has declined only slightly over a decade, which is evidence against the recurring prediction that such packages are about to disappear.[274]

## Counterfeit risk and authorised supply

Buying through authorised distribution is the practical defence against counterfeit and re-marked components, since grey-market supply carries a substantial chance of receiving a package correctly marked on the outside with a different die inside, which for an analog part means the wrong function entirely.[366] The risk from an unverified source scales with how hard the part is to validate on receipt: an LED is tested by turning it on, whereas a microcontroller cannot be qualified by inspection, so the same supply route is acceptable for one and not the other.[79]

Authorised supply does not eliminate part-identity errors. A batch ordered as 0.1 percent tolerance resistors arrived as one percent parts under the correct part number, reached assembled boards and shipped before the discrepancy was found during testing of the following batch, with the fault traced towards the component manufacturer rather than the distributor.[22] The failure that damages a distributor's usefulness most directly is a stock listing that proves wrong on ordering, because the whole reason for using a distributor is the assurance that a part shown as in stock will actually arrive.[545] Marketplace listings, in which third-party sellers offer stock inside a distributor's catalogue, undercut that same guarantee: a search returning a seller's own warehouse rather than distributor-held stock is not what the buyer went there for, and distinguishing the two in the interface becomes a requirement rather than a preference.[600]

The Chinese catalog distributor that Western engineers encounter occupies the same tier of trust as the established catalog distributors for sourcing purposes, because it is an official supplier for the brands it lists and does not substitute; the difference is the brand mix, which includes Asian manufacturers unfamiliar elsewhere, whereas marketplace platforms carry no such guarantee.[674] A Chinese catalog distributor tied to a board fabricator also exposes parts available only in that market, which is where an equivalent part number for an unfamiliar Asian-marked component can be found; the LCSC catalogue serves this lookup role.[580]

## International ordering, export control and tariffs

Late-evening order cut-offs with next-morning delivery change how prototyping is scheduled, since a part discovered missing at seven on a Friday evening can be on the bench the following morning. The assumption fails completely outside the served region: shipping to South America took a week at best, three dollars of cable attracted two hundred and fifty dollars of freight plus customs duty, and the working response is to plan ahead rather than to order reactively.[248] International shipping charges from large distributors are high because their fulfilment is built entirely around couriers, with no path for ordinary postal dispatch; smaller vendors shipping the same item by post charge a fraction of the amount but take far longer.[38] Within the served region, expedited shipping is cheap measured against the cost of not having parts, and the rate a distributor passes on is below what an individual can negotiate because of courier volume: overnight delivery at around thirty dollars, against roughly a hundred for first-thing-in-the-morning service.[623]

Orders shipped from the United States require an end-use declaration covering military, government surveillance and nuclear or chemical weapons applications, and a declaration of personal use can still trigger a follow-up request for details of the project, even for an order of passive components.[7] The same export-control regime restricts specific technologies to specific destinations, and some components cannot be bought at all without signing an export control agreement, which can defeat a purchase entirely.[204] Tariffs are itemised on distributor invoices and applied to imported components; where duty falls on raw components but not on finished goods, the structure penalises domestic assembly directly, since importing parts to build locally attracts the charge while importing the completed product does not.[458]

Local component markets also carry information that catalogues do not. A catalogue lists every part but does not distinguish which parts are commonly used and available at manufacturing scale in a given region; a part list drawn purely from Western catalogue numbers came back from a Chinese assembler as unbuildable in the normal way, with cheaper and more available local equivalents substituted. The information can be approximated remotely by translating the part category and searching a Chinese marketplace sorted by popularity.[121]

## Design-tool integration

Design tools embed distributor catalogues so that a part can be pulled into a schematic by parametric search or by part number, complete with symbol and footprint. Coverage is the limiting factor: early implementations were missing footprints for less common parts such as connectors, and a distributor-published open-source library covered on the order of a thousand parts because it was produced by hand.[145] Distributor-derived libraries are necessarily atomic, binding one footprint, one symbol and one 3D model to a single orderable part number, because two orderable variants of the same device can carry entirely different packages and must therefore be separate entries in both schematic and layout.[508]

Cross-distributor aggregators exist to search stock and pricing across vendors at once, and design tools consume a mixture of aggregator APIs, direct feeds from distributors including Digi-Key, Arrow, Newark and Mouser, and data taken directly from semiconductor manufacturers, because no single source is complete or reliable enough on its own.[163] Distributor APIs give reliable access to catalogue data but uneven access to ordering, with the level of integration depending on the account, so a workable compromise is generating a purchase order locally and uploading it; anti-scraping countermeasures intended to distinguish humans from bulk scrapers also block legitimate automated tooling, since the two are hard to tell apart.[722]

## Packaging and warehouse operations

The dominant catalog distributor's location was chosen by accident of origin rather than logistics, being far from a major airport or transport infrastructure, which forces it to operate its own inbound courier arrangements and to bus in several thousand employees from surrounding towns.[184] The warehousing itself is physically unglamorous and largely manual: rows of steel shelving holding cardboard trays with barcodes on the front, walked by pickers who pull the tray, take the parts and replace it, with temporary as well as permanent labour on the line.[598]

At the packaging level, the distributor prints the part number and values onto the back of cut tape, replacing the practice of hand-marking each strip with a permanent marker, which is the step that made small-quantity tape orders identifiable on the bench.[536] Earlier thermally printed component bag labels faded to blank over time, destroying the identification of anything stored in its original packaging; the defect was acknowledged and corrected in later labels.[58] Some oscillator parts are programmed to order by the distributor rather than stocked at every frequency, which resolves an inventory-breadth problem that would otherwise require carrying every value in the range along with its packaging variants.[524]

Repackaging components from bulk into forms suited to short runs is a recognised gap in the supply chain: cut-tape services address part of it, and automated de-reeling into trays would address more, but the process carries real cost with no guaranteed demand.[299] Part availability also propagates into physical assembly problems invisible at selection time: constrained to whichever LEDs the distributor held in quantity, one build found the carrier tape so thin that parts were ejected as the feeder advanced.[412]

## Education and publishing

Catalog distributors fund technical education directly, commissioning and hosting full course series on their own channels — produced under contract by outside educators — and publishing an industry magazine written by outside contributors, a marketing channel that operates as a component of the design ecosystem rather than as advertising.[675]

## Catalogue breadth as an industry benchmark

The existence of hundreds of thousands of fully characterised, tested and qualified parts in multiple packages at prices of cents each is the benchmark any on-demand chip fabrication method has to clear, and it is the packaging, test and qualification rather than the patterning that constitutes the difficulty.[234] The same breadth cuts the other way for product strategy: wholly off-the-shelf sourcing is itself a competitive exposure, because a product built entirely from parts anyone can order carries no supply-chain position and nothing that cannot be reproduced by a competitor who takes it apart, so differentiation has to come from somewhere other than the parts list.[259]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ | |
| 7 | Love Robots and Pantyhose Screens | https://theamphour.com/the-amp-hour-7-love-robots-and-pantyhose-screens/ | |
| 22 | The Hard Work Hypothesis | https://theamphour.com/the-amp-hour-22-the-hard-work-hypothesis/ | December 21, 2010 |
| 38 | An Interview with Jeff Keyzer - Comical Keyzer Comes a-Callin' | https://theamphour.com/the-amp-hour-38-comical-keyzer-comes-a-callin/ | |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ | |
| 58 | Multicopter, DIY drones & Tektronix - Zappy Zendik Zoilism | https://theamphour.com/the-amp-hour-58-zappy-zendik-zoilism/ | |
| 68 | Radiation Chips & Old Package Types - Technocratic Toilet Troubleshooting | https://theamphour.com/the-amp-hour-68-technocratic-toilet-troubleshooting/ | |
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 88 | Yonderly Yodeling Yobbos | https://theamphour.com/the-amp-hour-88-yonderly-yodeling-yobbos/ | March 25, 2012 |
| 102 | Gouging Green Gardyloo | https://theamphour.com/the-amp-hour-102-gouging-green-gardyloo/ | July 1, 2012 |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 113 | An Interview with Scott Miller - Sudden SinoAmerican Synthesis | https://theamphour.com/the-amp-hour-113-sudden-sinoamerican-synthesis/ | September 16, 2012 |
| 121 | An Interview with Zach Hoeken Smith - Creative China Commorant | https://theamphour.com/the-amp-hour-121-creative-china-commorant/ | November 11, 2012 |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 129 | An Interview with Brett Fox and Dr Jeroen Fonderie - Device Doubling Decretum | https://theamphour.com/the-amp-hour-129-device-doubling-decretum/ | January 21, 2013 |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 204 | An Interview with Noah Feehan - Biloquistic Blinking Blush | https://theamphour.com/204-an-interview-with-noah-feehan-biloquistic-blinking-blush/ | June 23, 2014 |
| 234 | We'll Believe It When We See It - Hiring Hypercatalectic Helpelp | https://theamphour.com/234-well-believe-it-when-we-see-it-hiring-hypercatalectic-helpelp/ | January 27, 2015 |
| 248 | An interview with Greg and Tim of Backyard Brains - Boethetic Bug Brainwaves | https://theamphour.com/248-an-interview-with-greg-and-tim-of-backyard-brains-boethetic-bug-brainwaves/ | May 5, 2015 |
| 259 | No More Naming | https://theamphour.com/259-no-more-names/ | July 21, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ | July 6, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 382 | The Toggle Boggle | https://theamphour.com/382-the-toggle-boggle/ | March 4, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 466 | An Interview with Ryan Cousins | https://theamphour.com/466-an-interview-with-ryan-cousins/ | November 10, 2019 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 507 | Right To Repair with Louis Rossmann | https://theamphour.com/the-amp-hour-507-right-to-repair-with-louis-rossmann/ | |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ | March 28, 2021 |
| 541 | Chip Shortage Denier | https://theamphour.com/541-chip-shortage-denier/ | May 10, 2021 |
| 542 | Component Management with Jan Rychter | https://theamphour.com/542-component-management-with-jan-rychter/ | May 17, 2021 |
| 545 | Fear of Banjos | https://theamphour.com/545-fear-of-banjos/ | June 6, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6, 2022 |
| 598 | Best way to find a leak | https://theamphour.com/598-best-way-to-find-a-leak/ | August 7, 2022 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 623 | Artisanal Crystals | https://theamphour.com/623-artisanal-crystals/ | March 12, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 674 | Turtles as a Service | https://theamphour.com/674-turtles-as-a-service/ | July 25, 2024 |
| 675 | Changing Course with Shawn Hymel | https://theamphour.com/675-changing-course-with-shawn-hymel/ | August 8, 2024 |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ | July 31, 2025 |
| 722 | AI Tooling with Matt Liberty and Luke Beno | https://theamphour.com/722-ai-tooling-with-matt-liberty-and-luke-beno/ | April 22, 2026 |
