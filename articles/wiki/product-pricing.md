---
title: Product Pricing
concept: product-pricing
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

Product pricing is the process of setting the sale price of a physical product, and in electronics hardware it is dominated by the relationship between the bill of materials, distribution margins, and the production volume the seller can realistically achieve.[105][143][201] Common practice builds the retail figure from a cost multiplier — typically 2.4 to 4 times hardware cost — while the price a market will bear is bounded by psychological thresholds, volume economics, and the margin demands of distributors.[215][114][646] Underpricing is the characteristic failure mode of small and crowdfunded hardware ventures, because a price that cannot cover production, fulfillment, and support guarantees failure regardless of demand.[215][58]

## Cost-plus pricing and margin multipliers

The dominant method of pricing small-run electronics is cost-plus: a retail price derived by multiplying the bill of materials (BOM) by a factor that absorbs distribution and retail margins. On 3D Robotics' open-hardware products, Chris Anderson's practice was a transparent retail price of 2.6 times the BOM, a figure derived from stacking two 40 percent margins — one for the manufacturer acting as wholesaler and one for the retailer.[105] The same structure appears from the retailer's side: a retail price is built from parts cost, then the distributor's roughly 40 percent margin, then the maker's own margin on top, and the resulting number is what the product must sell for.[143]

Other formulations converge on similar figures. The cost figure fed into the multiplier should absorb every foreseeable expense, including returns, and is then multiplied by about 2.5; because a distributor typically takes around 60 percent margin, a 2.5-times multiplier makes the maker's per-unit earnings equal the distributor's, and pricing below it means the distributor earns more per unit than the person who designed the product.[201] For a one-person hardware business, the minimum defensible price is BOM times 2.4, with BOM times 3 the safer figure; pricing lower does customers no favors because the seller cannot deliver and support the product.[215] A multiplier of roughly 4 times hardware cost is used as a starting guideline, with the actual price then moved until revenue against unit volume is maximized — an optimum that shifts with market conditions such as a recession.[646]

Deliberate deviation below the multiplier is a recognized strategy. Digilent's normal multiplier was 1.35, yet an early FPGA board with a BOM of $55 to $59 was retailed at $79, with the shortfall treated as a marketing expense to seed university users.[302]

A multiplier is only as good as the cost basis fed into it, and that basis extends well beyond the parts list: packaging, firmware programming, engineering time, and supply-chain work all carry real cost even when they add no visible hardware.[259] Contract design introduces a related hazard: a design house's first proposal can come back over-engineered, with unrequested features at double the target price, requiring the customer to re-specify parts downward to hit the price point.[282]

## Cost floors and hidden costs

Several cost structures resist reduction regardless of design effort. Machines built from many feeders, vision systems, and precision motion have a hard cost floor set by their mechanical content, so their price cannot be pushed arbitrarily low.[221] At small production volumes, a large share of a product's price tracks its shipping weight rather than its electronics content.[167]

Fixed and contingent costs must be priced in from the outset. Tooling such as injection molds must be amortized into the price from the beginning; without a committed volume or purchase orders, selling piece by piece leaves the real per-unit cost unknown.[441] Minimum order quantities on custom components such as LCD panels can block production entirely: the prototype works and customers want the product, but the panel cannot be bought below the vendor's minimum panel count.[328] Margins must also absorb yield loss — a margin as low as 20 percent leaves no room for it, and an 80 percent manufacturing yield can wipe out the profit entirely.[487]

Prices also drift upward during development. A manufacturing partner raises the agreed unit price each time the specification changes, so late feature changes push a product past its intended cost.[362] A product aimed at a $200 retail class can drift out of its bracket entirely as component sourcing and specification costs creep up.[368] The same risk runs in reverse for early announcements: declaring a price before the silicon and manufacturing are proven is risky, because failed respins or unexpected costs may force the price up later — Jeri Ellsworth's standing rule on her early hardware ventures was that no one should commit the project to a price point prematurely.[147]

## Price points and market structure

Certain price levels carry structural significance. For consumer accessories, roughly $100 acts as a psychological ceiling below which a large addressable market will buy on impulse.[114] There is also a dead band in electronics pricing where a product is too expensive to be an impulse buy and too cheap to be a considered professional purchase, roughly around the $150 to $180 mark; Pete Staples' rule of thumb is that electronics products simply should not occupy that bracket.[544]

Vendor pricing frequently reflects which segments a vendor wants to serve rather than cost. A vendor whose business is not hobbyist supply can hold a development board at a high price — $400 in one instance — simply because the hobbyist segment is not a market it cares to serve.[43] Semiconductor vendors targeting million-unit sockets deliberately set single-unit pricing high to price small buyers out rather than support them.[150] The inverse strategy also exists: Matt Richardson described Raspberry Pi's refusal of volume price breaks as keeping the board at one low price for everyone, which serves education and small production runs but rules out very high volume commercial use.[235]

Historical cases show price as a strategic lever in both directions. Early bright LEDs were priced at around a dollar into indicator applications even though the incumbent market had been paying roughly $70 per part — a deliberate choice to open a volume segment rather than harvest the old price.[71] A mass-market children's toy can carry a roughly ten-to-one gap between manufacturing cost and retail price, with a few dollars of parts sold for tens of dollars.[50] Price level alone can determine viability: a technically excellent FPGA system priced at $4,000 failed to sell, while a later $300 version of the same idea sold in far greater numbers.[593] Competitive positioning can also define a price point: a vapor-phase soldering machine was positioned at 5,000 euros against roughly 10,000 euros for existing machines, after the original $1,500 hobbyist target was abandoned because the required features would not fit that price.[608]

## Willingness to pay and price testing

Value-based pricing departs from cost entirely. Alan Wolke's practitioner judgment is that customers pay a premium over a cheaper equivalent when the price also buys someone who will diagnose and remove their specific pain, which is why understanding the customer's application matters more than knowing one's own equipment.[117] A simple test board costing about a dollar to make can sustain a $40 price because the price reflects the value of the measurement, not the hardware content.[551] Engineers systematically underprice by reasoning from parts cost, when the correct question is what a buyer will actually pay for the finished object; a kit with about three dollars of parts sold fine at twenty dollars.[646]

Willingness to pay can be measured experimentally rather than assumed. Eric Ries' procedure uses a mocked-up, non-functional replica of a hardware product placed in a realistic customer environment to run a purchase-decision experiment, varying the offered price point from customer to customer.[159] The same approach measures whether customers will actually pay a premium for an expensive feature such as full robotic automation, allowing engineering scope to be cut from the specification before engineers are committed to it.[159]

## Crowdfunding pricing

Crowdfunding imposes its own pricing dynamics, most of them hazardous. Crowdfunded hardware has a viability curve below which the campaign price cannot cover production; a project priced under that line goes bankrupt before delivering, even if the founders pay themselves nothing.[215] The pressure is structural: crowdfunding pushes creators toward a price low enough to attract a crowd and generate momentum, which conflicts with the price needed to cover production.[394] First-time creators systematically underprice, and Zach Dunham's standing advice to new campaign runners is to double whatever price they first arrived at.[350]

A campaign's price can itself be read as a diagnostic. A pledge tier that includes both a finished electromechanical product and shipping for about twenty dollars signals that the campaign's unit economics do not close.[58] Likewise, when a crowdfunded product's claimed feature set — electronics, HD video capture, recording, battery — cannot physically be built into the stated volume at the stated price, the price itself is the tell that it will not ship.[87]

Established campaign practices mitigate these risks. David Kronstein's approach splits rewards into a limited early-bird tier and a higher-priced later tier, which both rewards early backers and leaves a small quantity buffer to absorb production failures.[325] Capping the number of units offered in a campaign bounds the production commitment a solo engineer takes on, and pairs with charging enough per unit.[358] Where the initial price proves wrong, correction is possible: after one campaign and its fulfillment run, Vic Aprea's product price was raised from $100 to about $185 per unit to reflect real costs.[250] Cash flow also constrains order strategy: for a premium product selling at $365, even a hundred-unit order ties up significant cash up front, which is why Simone Giertz's operation stepped order sizes up only as confidence in the manufacturer grew.[592]

## Launch sequencing and portfolio strategy

Price strategy interacts with production volume over a product line's lifetime. Jeri Ellsworth's first-generation product was priced at conventional consumer retail margins rather than at a high low-volume price, to test whether the product was viable in the form it would eventually reach the mass market — at the cost of near-zero profit on the first run.[173] The same logic generalizes: a workable launch pattern is to break even on the first expensive low-volume batch to validate the market, then capture the volume efficiencies that were skipped as margin on later runs.[314] One sensor node's price ladder illustrates the progression: a 100-unit first run that was largely given away, then about $70 per unit at 500 pieces, and a planned MSRP near $40 at 5,000 to 10,000 units.[557]

Entry-level pricing serves ecosystem goals. Matt Ettus' practice at Ettus Research was to keep at least one product in a price range a self-funded hobbyist can afford, even as the higher-end line climbed, because low-priced offerings bring new users into the ecosystem and its surrounding software.[101] Adam Wolf's kits were built down to the lowest possible price and sold as multi-packs, removing beginners' fear of destroying an expensive board and lowering the barrier to trying surface-mount soldering.[167] Charging $20 to $30 for a development kit rather than giving it away filters out people who sign up for anything free and leaves the genuinely interested users.[164] At the portfolio level, a product line spanning roughly $100 to $10,000 lets one company — Colin O'Flynn's, in the case described — serve students, researchers, and professional security evaluators from the same catalog.[693]

Scope decisions are pricing decisions. Trying to build one product that covers every use case drives cost past what any reasonable price can support; Piotr Esden-Tempski's autopilot work treated narrowing scope as a pricing decision for that reason.[356] Chasing the last fraction of a percent of demanding customers can double a product's price, a poor trade against serving the mainstream buyer.[415] Variant strategy follows the same arithmetic: offering two board variants only makes sense if the cheaper part yields a meaningful price gap, and when Luke Valenty's lower-capacity device saved only about $3, the second SKU was dropped.[395]

## Competition, copying, and margin defense

Price structure determines vulnerability to copyists. Pricing at a bare BOM multiplier with no intellectual-property loading caps how far a copyist can undercut the original: they can strip out roughly one of the stacked 40 percent margins and no more.[105] Reselling commodity parts is the opposite position — margin is hostage to supplier pricing and to anyone who can start the same business from a laptop, which was Marcus Schappi's argument for developing own-brand products.[189] At the premium end, pricing into a very high margin bracket attracts knockoffs and outright counterfeits, a downside of positioning a product like fashion or design goods.[592]

## Price changes over time

Prices are not set once. Hardware sellers should raise prices on a regular cadence, though the do-it-yourself culture resists this, and sellers with thin margins do not survive long enough to keep supplying the community.[564] When component costs such as memory are rising, Jason Kridner's commitment at BeagleBoard has been to limit price revisions to no more than once per quarter, keeping pricing predictable for customers.[723] Matt Venn's experience illustrates tiered correction of chronic underpricing, which he attributes to costing only the parts and ignoring the labor: a service originally priced at a hundred dollars was later tiered at $150 for the first hundred individual customers and $300 for institutional buyers or later orders.[672] Venn's related naming rule is that embedding a price point in a company or product name removes the ability to raise the price later, so the name should be kept independent of the number.[672]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 43 | An Interview with Jeff Keyzer and Jeremy Blum - Audacious Arduino Arguments | https://theamphour.com/the-amp-hour-43-audacious-arduino-arguments/ | |
| 50 | Callow Cough Coverups | https://theamphour.com/the-amp-hour-50-callow-cough-coverups/ | |
| 58 | Multicopter, DIY drones & Tektronix - Zappy Zendik Zoilism | https://theamphour.com/the-amp-hour-58-zappy-zendik-zoilism/ | |
| 71 | An Interview with John Edmond - Luciferous LED Lucubrator | https://theamphour.com/the-amp-hour-71-luciferous-led-lucubrator/ | |
| 87 | An Interview with Ian Daniher - Nascent Nonolith Numquid | https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/ | |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 114 | Kickstarter, Manufacturing, Open Hardware - Judging Jurisdictional Junctures | https://theamphour.com/the-amp-hour-114-judging-jurisdictional-junctures/ | September 23, 2012 |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ | August 23, 2021 |
| 143 | PCBs, Tektronix & Ham Radio - Habitual Handicraft Hangups | https://theamphour.com/the-amp-hour-143-habitual-handicraft-hangups/ | April 29, 2013 |
| 147 | An interview with Jeri Ellsworth - Absorptive Augmented Actuality | https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/ | May 27, 2013 |
| 150 | Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness | https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/ | June 17, 2013 |
| 159 | Interview with Eric Ries - Transorted Testing Tachydidaxy | https://theamphour.com/the-amp-hour-159-transorted-testing-tachydidaxy/ | |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ | September 23, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25, 2013 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 201 | Cheap Respins And A Time Machine - Multiscience Mercenary Marketplace | https://theamphour.com/201-cheap-respins-and-a-time-machine-multiscience-mercenary-marketplace/ | June 2, 2014 |
| 215 | Wrong Hardware, Wrong Software - Fugacious Fan Funding | https://theamphour.com/215-wrong-hardware-wrong-software-fugacious-fan-funding/ | September 7, 2014 |
| 221 | Warming Up To IoT - Tendentious Thermal Tools | https://theamphour.com/221-warming-up-to-iot-tendentious-thermal-tools/ | |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20, 2015 |
| 259 | No More Naming | https://theamphour.com/259-no-more-names/ | July 21, 2015 |
| 282 | 3D Product Logistics | https://theamphour.com/282-3d-product-logistics/ | January 13, 2016 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 314 | An Interview with Josh Lifton | https://theamphour.com/314-an-interview-with-josh-lifton/ | September 7, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 328 | The Ghost of Keyzermas Past | https://theamphour.com/328-the-ghost-of-keyzermas-past/ | December 21, 2016 |
| 350 | An Interview with Zach Dunham | https://theamphour.com/350-an-interview-with-zach-dunham/ | July 3, 2017 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 358 | Mergers and People Acquisitions | https://theamphour.com/358-mergers-and-people-acquisitions/ | September 4, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 368 | The EEVblog Sparkgap Generator | https://theamphour.com/368-the-eevblog-sparkgap-generator/ | November 19, 2017 |
| 394 | Jeri Ellsworth and the demise of CastAR | https://theamphour.com/394-jeri-ellsworth-and-the-demise-of-castar/ | May 28, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 441 | Motivational Speaker | https://theamphour.com/441-motivational-speaker/ | May 5, 2019 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 544 | Standardizing Manufacturing with Pete Staples | https://theamphour.com/544-standardizing-manufacturing-with-pete-staples/ | June 1, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ | |
| 564 | Pavlovian Cheapskates | https://theamphour.com/564-pavlovian-cheapskates/ | October 31, 2021 |
| 592 | Product Design with Simone Giertz | https://theamphour.com/592-product-design-with-simone-giertz/ | June 6, 2022 |
| 593 | Publicly Traded Hobby with Ben Jordan | https://theamphour.com/593-publicly-traded-hobby-with-ben-jordan/ | June 14, 2022 |
| 608 | Vapor Phase with Saber Kaygusuz | https://theamphour.com/608-vapor-phase-with-saber-kaygusuz/ | November 7, 2022 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 693 | Small Scale Electronics Manufacturing with Colin O'Flynn | https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/ | May 13, 2025 |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ | May 7, 2026 |
