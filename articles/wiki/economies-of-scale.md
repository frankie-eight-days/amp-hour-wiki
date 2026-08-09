---
title: Economies of Scale
concept: economies-of-scale
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Economies of scale are the cost advantages that accrue to a producer as output increases, arising from the spreading of fixed costs such as tooling and engineering, from volume pricing on components and services, and from the negotiating leverage that large orders confer.[32][176][363] In electronics manufacturing the effect is pervasive but uneven: unit cost falls with volume along a stepped, product-specific curve rather than a smooth one, and the position of the steps must be discovered by negotiation with the manufacturer.[218] Because mass-market consumer hardware is amortised over volumes no small producer can reach, economies of scale shape not only what products cost but which products get made at all.[105][167]

## The shape of the volume–cost curve

The relationship between unit cost and volume is not linear and contains no threshold at which cost suddenly falls by an order of magnitude; moving from ten thousand to a hundred thousand units does not transform the base cost of a product.[152] The reductions available in the volume ranges most small producers occupy are modest: moving from a hundred units to a thousand yields something like ten percent rather than a halving, and the dramatic reductions associated with volume manufacturing require tens of thousands or a hundred thousand units, far beyond where most projects sit.[81] The common expectation that a fifty-dollar single board implies a five-dollar board at a thousand units is wrong; a representative assembly quotation runs roughly fifty-two dollars for one board, forty-five at ten, about thirty-five at a hundred and about twenty-three at a thousand.[243]

The curve is better understood as a step function with discontinuities whose positions vary by product and must be discovered by asking the contract manufacturer directly.[218] On the Mooshimeter, Van Wyk's team found that the difference between one thousand and five thousand units was enormous while the difference between five and ten thousand barely altered the production strategy, which is what makes locating the steps worth the effort.[218]

At genuine production volumes, the engineering effort justified by a unit-cost saving is large: a hundred thousand boards will support a hundred thousand dollars of labour to remove a dollar from each one.[32]

## Designing for volume

### Bill of materials consolidation

Volume economics drive component substitutions that would look absurd at small scale, such as fitting two of a cheaper resistance value in parallel to synthesise a more expensive one, saving a cent that becomes ten thousand dollars across a million units.[1] Optimisation also works by eliminating part numbers rather than by unit price: wiring one of an already-stocked transistor type as a diode avoids buying a whole reel of diodes for a single position.[1] The deeper reason is that each distinct part consumes a feeder position on the assembly machine, so a design with thirty part numbers requires a machine that can hold thirty reels to be built efficiently.[1]

### Enclosures, connectors and tooling

Designing around an off-the-shelf enclosure imports someone else's volume, which is why it is nearly always cheaper than commissioning a custom one; vendors will machine and punch a standard enclosure to order, which is not cheap in itself but becomes reasonable at high volume.[66] Where custom tooling is unavoidable, standardising an enclosure profile across successive versions of a product spreads the investment over several generations rather than charging it to one. The Bus Pirate project took this route, planning for versions four through seven to share one injection-mould profile so the tooling cost could be recovered over time.[125] Standardising a connector across a product family is likewise a deliberate route to volume, since consolidating on one part produces the quantity needed to bring its cost down.[277]

Tooling cost dominates a small hardware project's budget, with mould costs alone capable of consuming most of a substantial crowdfunding raise.[219] Conversely, recurring per-unit costs scale linearly with production: a modularity feature that is cheap at a hundred units becomes expensive enough at millions to justify hiring engineers purely to design it out.[565]

### Restricting variation

Restricting the options offered is how a manufacturing service reaches scale, with a single surface finish and one set of trace and space rules taking the place of a configurable order.[299] Reaching a price point can also require changing the process rather than negotiating the price: OSHstencils had a machine's loading system modified so that stencil material could be bought and cut in a form cheap enough to sell at the intended price.[320]

## Riding on others' scale

Component prices available to everyone are set by the volumes of the largest consumer products, which is why an inertial sensor costs a few dollars and a positioning module fifteen.[109] This relationship can be exploited deliberately by reading the parts list of a high-volume consumer product, on the reasoning that whatever a major manufacturer designs in will be widely available and cheap.[109] The same logic governs whole products: the first question before building any connected consumer device is whether custom hardware is needed at all, since a mass-produced tablet or phone costs less than anything achievable in small or medium quantities, with capable tablets selling for fifty dollars in one market and multi-function ones under twenty in another.[268]

Customer expectations are anchored to products amortised over volumes no small manufacturer can reach, so a device made in ten thousands is compared against a phone and judged expensive.[167] That anchoring imposes a price ceiling that can push a small producer deliberately toward inexpensive products, since a costly one invites comparison with mass-market hardware it cannot match.[167]

## Strategies for small producers

A small producer building fifty or a hundred units instead of a thousand accepts a substantially higher unit price in exchange for a much smaller cash outlay and correspondingly lower risk.[38] A workable strategy for a first production run is to break even deliberately, building it the expensive way to validate the market and treating the efficiencies not yet taken as the margin available once volume arrives; because low-volume quotations are erratic, the price to the customer has to be set with that variability already built in.[314] Industrial and low-volume products are freed from the pressure to optimise every component, since a slightly more expensive part across five thousand units does not materially affect the business, and the same total revenue can arrive as few expensive units or many cheap ones, with the two demanding radically different unit costs — the volume assumption determines what the product can be.[363]

A niche product escapes the mass-market comparison entirely, since buyers accept a premium where nothing else is available and scale is therefore not required to have a viable business; working in a niche is also what allows manufacturing to stay in a high-cost country, because the premium covers the absence of volume.[64][57] A company competing against inevitable low-cost copies can stay a generation ahead rather than defending the current product, treating the arrival of cheap equivalents as expected.[112]

## Scale in industrial structure

Fabrication plants become cheaper to run the longer they operate, since a facility paid off many times over keeps producing at declining cost, and a supporting cluster of chemical and service suppliers grows around it.[176] At the leading edge the direction reverses: semiconductor manufacturing consolidates because advanced capacity has become too expensive for any but the largest to fund, with individual plants costing billions.[249] Where a technology is new, cost reduction waits on whichever variant reaches sufficient volume first, and several variants may persist because different applications need different characteristics.[23]

Distributors operate on high turnover and thin margins rather than large mark-ups, with one distributor's published figures showing around five percent profit on a billion dollars of revenue.[128] Buyers with sufficient reserves commit to enormous quantities up front rather than ordering a trial batch, and that commitment is part of what secures the price; at the extreme, securing supply can mean buying out an entire plant's output, a straightforward decision for a company holding large cash reserves that earn nothing.[70][289]

Scale within a large company also works through order aggregation, since one product line's requirement is treated as part of a much larger order and priced accordingly.[628] Acquisition by a larger company is pursued for the same buying power, with the expectation that the parent's volume advantage will lower the cost of manufacturing a small company's products.[101] Vertical integration requires enough demand and money behind it to be worth doing, which is why it is available to very large companies and not to small ones.[518]

The same principle operates cooperatively: a subscription or aggregation model can exist partly to obtain buying power on behalf of individuals who would otherwise buy the same items singly, and a shared-cost fabrication service becomes cheaper for everyone as participation rises, making growth in users the route to lowering its price.[420][703]

## Risks and limits

Ordering an assembled batch large enough to obtain a volume price removes the ability to change the design until the whole batch is sold, a direct cost in inflexibility.[105] Owning the assembly line resolves that tension by allowing small on-demand batches: Chris Anderson's company produced around thirty versions of a board in a year, each cheaper or more reliable than the last, without accumulating obsolete inventory.[105] Large manufacturers dominate through scale to the extent that products aimed at narrow audiences are simply not made, because neither the manufacturer nor the retailer wants to operate at that volume; what efficient small-batch manufacturing and internet distribution change is not the existence of mass production but its monopoly, allowing a long tail of products to exist alongside it.[105]

Concentrating production for efficiency creates a single point of failure, so that one plant going down removes a large share of available parts at once, an exposure realised during the COVID-era chip shortage.[628] Consolidation compounds the exposure because a merged company's product lines share the same manufacturing route, whereas separate suppliers with their own plants had genuinely different vulnerabilities and lead times.[628] Concentrating manufacturing capacity on one industry similarly risks that capacity sitting idle if the industry contracts, whereas making a component sold into many industries spreads the exposure.[518] Deliberate inefficiency therefore has value as insurance against concentration, though the argument is difficult to make while the efficient arrangement is working, and the shortage that matters in practice is of the ordinary parts used in vehicles and appliances rather than the newest process nodes.[532]

Volume pricing also tempts the small producer: buying ten thousand of a component at a tenth the unit price is attractive precisely when demand is least predictable, and demand arriving suddenly through a new distribution channel is hard for a one-person operation to absorb, since a distributor whose sales go well moves from nothing to full rate very quickly.[421] Establishing what users actually need before optimising can eliminate the requirement entirely; one design being optimised for readings every minute turned out to satisfy its users at four readings a day, a thousandfold reduction in the power budget.[268]

## Scale as strategy and as moat

Building for high volume at low margin is a coherent strategy distinct from pursuing high margins, sustained by selling in quantity rather than by pricing power — the model on which the MOS Technology 6502-era chip business operated.[241] Setting a headline price first and designing the product and its supply chain to meet it inverts the usual sequence, and works with margins that are sustainable but lower than the industry norm.[529] On the Raspberry Pi programme, that strategy proved self-reinforcing: a lower price sells more units, more units buy better component pricing and justify automation, and the higher volume also improves measured defect rates because the same product is built millions of times.[529] Scaling production is likewise what allows a module's price to fall, chiefly through the component pricing that volume unlocks.[427]

Because a competitive advantage frequently rests on manufacturing efficiency and volume rather than on the design itself, publishing the design can cost very little.[203] Cloning a product without technical improvement is defended on the ground that reaching a lower price point and the volume behind it is itself a contribution, and disputed on the ground that it is not sufficient contribution.[123] Small-scale and personal fabrication adopts a deliberately different objective from mass manufacturing, aimed at making things that do not exist rather than reproducing what a mature industry already supplies cheaply.[208]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 1 | What's In A Name? | https://theamphour.com/1-whats-in-a-name/ |  |
| 23 | The Innovation Speculation | https://theamphour.com/the-amp-hour-23-the-innovation-speculation/ |  |
| 32 | Cores, Digikey, Electronic Design - The Commercial Competitor Commencement | https://theamphour.com/the-amp-hour-32-the-commercial-competition-commencement/ |  |
| 38 | An Interview with Jeff Keyzer - Comical Keyzer Comes a-Callin' | https://theamphour.com/the-amp-hour-38-comical-keyzer-comes-a-callin/ |  |
| 57 | An Interview with Alan Yates - Recondite Radiation Raconteur | https://theamphour.com/the-amp-hour-57-recondite-radiation-raconteur/ |  |
| 64 | OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster | https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/ |  |
| 66 | Magnets, China & IEEE - Xenomorphic Xerox Xebec | https://theamphour.com/the-amp-hour-66-xenomorphic-xerox-xebec/ |  |
| 70 | Idiorhythmic IPC Inconcinnity | https://theamphour.com/the-amp-hour-70-idiorhythmic-ipc-inconcinnity/ |  |
| 81 | Jersey Jeff Jactitation | https://theamphour.com/the-amp-hour-81-jersey-jeff-jactitation/ | February 6, 2012 |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 109 | An Interview with Larry Sears - Hexagram Hardware Holism | https://theamphour.com/the-amp-hour-109-hexagram-hardware-holism/ | August 19, 2012 |
| 112 | An Interview with Bob Simpson - Ardent Automotive Artisan | https://theamphour.com/the-amp-hour-112-ardent-automotive-artisan/ | September 9, 2012 |
| 123 | An Interview with Jon Oxer - Innoxious Implant Innovator | https://theamphour.com/the-amp-hour-123-innoxious-implant-innovator/ | November 26, 2012 |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 203 | Tesla, Checklists and Bullies - Emerging External Eupsychics | https://theamphour.com/203-tesla-checklists-and-bullies-emerging-external-eupsychics/ | June 16, 2014 |
| 208 | An Interview With Nadya Peek - Gallant Gcode Gerontology | https://theamphour.com/208-an-interview-with-nadya-peek-gallant-gcode-gerontology/ | July 21, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 241 | An Interview With Chuck Peddle - Charismatic Chipmaking Coryphaeus | https://theamphour.com/241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus/ | March 18, 2015 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 249 | Wearables Might Have Limited Fashion Options - Lachrymogenic Lane Language | https://theamphour.com/249-wearables-might-have-limited-fashion-options-lachrymogenic-lane-language/ | May 12, 2015 |
| 268 | An Interview with Luke Iseman of yCombinator | https://theamphour.com/268-an-interview-with-luke-iseman-of-ycombinator/ | September 22, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ | March 2, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 314 | An Interview with Josh Lifton | https://theamphour.com/314-an-interview-with-josh-lifton/ | September 7, 2016 |
| 320 | An Interview with Brent of OSHstencils | https://theamphour.com/320-an-interview-with-brent-of-oshstencils/ | October 20, 2016 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 420 | An Interview with Joe Long | https://theamphour.com/420-an-interview-with-joe-long/ | December 16, 2018 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 427 | An Interview with Maarten Engelen | https://theamphour.com/427-an-interview-with-maarten-engelen/ | January 27, 2019 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 529 | Embedded Hardware with the Raspberry Pi Team | https://theamphour.com/529-embedded-hardware-with-the-raspberry-pi-team/ | February 7, 2021 |
| 532 | Recalling Recalls | https://theamphour.com/532-recalling-recalls/ | February 28, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
