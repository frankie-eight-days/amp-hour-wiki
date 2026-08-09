---
title: Profit Margin
concept: profit-margin
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**Profit margin** is the share of a product's selling price that remains after costs, and in hardware businesses it is typically managed through a multiplier applied to the bill-of-materials (BOM) cost rather than as an afterthought added to the parts total.[123][40] The multiplier matters because it has to absorb every cost between the parts arriving and the customer receiving the product — assembly, distribution, payment processing, yield loss and support — none of which appears in the BOM itself.[123][153] A business running at a sustained twenty percent annual profit is regarded as genuinely good performance in an ordinary industry, and revenue figures alone reveal almost nothing about the health of the operation behind them.[118][253]

## Pricing multipliers

The figure the hardware industry converges on is roughly 2.4 times bill-of-materials cost, and that is a floor — the absolute minimum for the exercise to be worth doing — rather than a target.[123] Kit businesses operate at a still higher multiple, needing three to four times parts cost, because a kit sold at parts cost plus twenty or fifty percent returns so little that the time is better spent elsewhere; twenty percent profit describes a good conventional business, not a viable kit margin.[40]

The arithmetic behind the multiplier is a bootstrapping constraint: ten percent profit on a batch of ten boards funds exactly one more board, so growing without outside money requires better than doubling the stake, which is the real reason the multiplier sits around two and a half rather than somewhere more modest.[417] A transparent version of the model prices at 2.6 times the bill of materials, built from two stacked forty-percent margins — one for the wholesaler and one for the retailer — with nothing charged for the intellectual property; priced that way, a competitor can undercut by roughly one of those margins and no further while still making money. On the open hardware model Chris Anderson described, that transparency is the point of the exercise.[105]

First-run pricing should be set so that a small initial batch — twenty-five units — recovers the one-off costs, board tooling included; if the margin cannot repay the setup within the first small batch, the pricing is wrong before volume enters the picture.[40]

## Margins along the distribution chain

Every party in the chain takes a margin and the price compounds as it passes along, with the last party before the customer usually taking the largest share — which is why a price that looks generous at the factory gate looks thin at retail.[157] Handing a product to a distributor typically returns ten to fifteen percent where selling it directly might return most of the margin; the gap buys fulfilment, marketing reach and the absence of individual order handling, and the decision turns on whether the maker wants that work rather than on the percentage.[189] Accepting less income per unit in exchange for someone else handling fulfilment is a legitimate and deliberate trade, and the right one for anyone whose time is better spent designing the next product.[197]

Channel costs take several forms. A marketplace typically takes around ten percent of each sale where a self-hosted store costs a fixed monthly fee, so the percentage model only makes sense above the volume where the flat cost is the smaller of the two — and on low-margin goods a percentage fee can consume most of what is left.[333] Payment processing takes a few percent of the transaction regardless of what the product earns, so any business running at a low single-digit margin has effectively already given its entire profit to the card network.[153]

Selling direct keeps both the channel margin and the customer relationship, and the relationship is arguably worth more: knowing who buys what, and in what quantity, is exactly the information a manufacturer needs to decide what to build next.[116] Pure distribution, by contrast, is structurally a race to the bottom — whatever margin one reseller accepts, another will accept half of it and customers will move — so distributors that survive do so on the other things they provide rather than on the resale itself.[244] Consolidation among distributors is itself a margin story: as the percentage available on each transaction falls, scale becomes the only way to keep the absolute number up, and acquisition is the fastest route to scale.[310]

## Revenue, profit and scale

Twenty percent annual profit marks a genuinely good business in an ordinary industry; on twenty million of turnover that is two million, before tax and before it is split among the owners — which is the scale check to apply before treating a revenue figure as impressive.[118] Revenue on its own reveals almost nothing: 1.4 billion in annual revenue against 45 million in profit is about three percent, the same order as a grocery store, and a far smaller business at a better margin can be worth more to its owner.[253] A hardware business turning over a million dollars a year can pay its owner less than an employed engineer earns, because the margin available in its segment determines take-home pay rather than the size of the revenue line.[152]

Margin structure, not revenue, also sets headcount. Two quite different businesses reach the same revenue — one selling large volumes of thirty-dollar products, which requires enormous shipping throughput and the staff to handle it, and one selling a few high-value products with a handful of people.[264] A ten-million-dollar business run at twenty percent throws off two million a year and can be built without venture money at all; the contrarian position attached to that arithmetic is to set out to build a good company rather than an exit, on the argument that a good company gets found at the right time anyway.[99]

Hardware and software businesses differ in cash flow more than in margin: hardware ties money up in parts before anything can be sold, while a software business commits almost nothing to inventory, which is why the two need such different amounts of working capital for the same revenue.[417]

## Margin as an engineering variable

In a high-volume consumer product, every component that could be removed already has been, because at volume each part removed is margin straight to the bottom line — which is why such a board looks sparse next to an equivalent industrial one.[32] A demand for more margin is a routine trigger for redesigning a working product, with a target expressed in cents per unit rather than in features — a different engineering problem from the one that produced the original design.[64] Such savings are real and nearly impossible to claim credit for: a salesperson can point at a million dollars of new business, while an engineer who took ten cents off one board of a twenty-product line has improved margin invisibly.[580]

Driving down bill-of-materials cost deserves the overwhelming share of the engineering effort, because a low parts cost is what gives somewhere to retreat to when a competitor appears or the market shifts — margin held in reserve is optionality, not greed.[40] Purchase quantity feeds straight through to margin: buying in small lots raises the per-part cost and shrinks what is left, while buying volume improves it at the cost of cash tied up in inventory that must be held and tracked; no position optimises both.[542] On precision parts the gap can decide the product — four dollars against twelve for a single resistor, with the difference coming directly out of margin at low volume.[554] A company sitting on cash converts it into margin by pre-buying components at enormous volume, whole production runs at a time, which is also the argument for buying a supplier outright: owning it removes someone else's margin from the cost base.[500]

Semiconductor integration is margin-driven from the vendor's side: absorbing a function that used to be a separate chip lets the vendor sell one part that costs the customer less in total solution cost while capturing more of the value.[289] Semiconductor pricing carries margin deliberately because it funds the fab, the applications engineers and the sales organisation — which is why vendors resist anything that erodes it and why free support is not actually free.[351] Development boards, conversely, carry deliberately lower margin than production hardware and are frequently booked as marketing rather than as product, so their pricing says nothing about the economics of the parts they showcase.[422]

At Digilent, a deep partnership with one manufacturer bought a small company near-large-volume pricing, and margins were then raised gradually rather than opportunistically; the payoff, as Clint Cole described it, was predictability — knowing costs from build to build determined how many people could be employed and how many new designs could be started.[302]

## Failure modes

Taking the parts cost and adding twenty percent is the standard beginner's error in hardware pricing, because it accounts for none of the costs between the parts arriving and the customer receiving the product.[123] Yield is a pricing input, not a manufacturing detail: pricing at twenty percent margin and then achieving eighty percent yield means every fifth unit's cost has to come out of that twenty percent, which it cannot.[487] Costing a bill of materials in one currency and selling in another puts the margin at the mercy of the exchange rate — a twelve percent move in parts cost against a planned margin can consume most of it without anything changing in the design.[178]

The common crowdfunding failure is not missing the target but hitting it: the campaign funds, and then the creator discovers the pricing left no margin to survive manufacture; basing prices on local assembly costs and distributor part pricing is the conservative way to avoid it.[113] Before collecting money, four things have to be settled — the cash flow, the margins, who is manufacturing, and reward tiers priced from real quotes rather than estimates — because doing it afterwards is what turns a funded campaign into an obligation that cannot be met.[350]

Designers also routinely underprice their own work out of discomfort with charging for it, treating the need to make money as something to apologise for; it is a learned skill rather than a character trait, and the usual teacher is running out of money.[280] Regular price increases are normal in most industries and resisted in maker and hobbyist markets, where sellers would rather absorb cost than appear to be gouging; the result harms buyers too, because a seller with no margin does not stay in business — and electronics is unusual in that the same part genuinely does get cheaper each year, which trains exactly the wrong expectation.[564]

## Market structure

Manufacturing location follows the margin structure rather than preference: consumer margins are thin enough to require offshore volume pricing, while industrial products rarely have the volume to justify it and are better served locally.[362] Conversely, where a product is made is evidence about its margin — assembly in a high-wage country implies the price supports it, which usually means a strong brand and a premium the market accepts.[410]

In fast-moving consumer categories the window to earn back a design is on the order of four months, after which price competition removes the margin, which changes what level of engineering investment the product can carry.[70] Consumer categories differ enormously in the margin they allow, and toys sit near the bottom — tight enough that the engineering decisions available differ in kind from those in a wearable or an industrial product.[373] Adding connectivity to a mature commodity product is usually a margin response rather than a user requirement: once copies erode the price of a well-made kettle, a feature nobody asked for is the cheapest available differentiator.[319] Selling into an industry that itself runs on thin margins constrains the product hard — it has to work every time, cost little and be simple enough to need no attention, because the buyer has no headroom to absorb either the price or the failure.[585]

Instrument vendors capable of collapsing the price of a high-end capability decline to, because doing so destroys the margin pool for the whole market including themselves; the restraint is not collusion so much as everyone independently declining to undercut their own product line.[72]

Margin arithmetic also disciplines valuation claims. At sixty percent margin on a two-hundred-dollar product, justifying a 3.2-billion-dollar price means selling 250 million units over the product's life — a number that immediately fails a sanity check for a niche device.[182] The same check applied elsewhere — around two million boards a year with roughly eighty percent of income from hardware — does not produce the profit that would support a valuation in the hundreds of millions, whatever the brand is worth.[707] A product retailing at two hundred and fifty dollars that returns sixty to its maker is the argument for becoming a services business rather than a hardware one, because that share will not sustain the organisation that built it.[324] When an acquisition price cannot be justified by units sold or by margin, and the technology is largely open anyway, what is being bought is the brand and the community around it — a legitimate purchase, just not the one the financial framing suggests.[151]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 32 | Cores, Digikey, Electronic Design - The Commercial Competitor Commencement | https://theamphour.com/the-amp-hour-32-the-commercial-competition-commencement/ | |
| 40 | Adafruit, Chip heist, Hackerspaces - The Kit Conniption | https://theamphour.com/the-amp-hour-40-the-kit-conniption/ | |
| 64 | OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster | https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/ | |
| 70 | Idiorhythmic IPC Inconcinnity | https://theamphour.com/the-amp-hour-70-idiorhythmic-ipc-inconcinnity/ | |
| 72 | Kismetic Keithley Katowse | https://theamphour.com/the-amp-hour-72-kismetic-keithley-katowse/ | |
| 99 | An Interview with Steve Leibson - Impavid Ideopraxist Insider | https://theamphour.com/the-amp-hour-99-impavid-ideopraxist-insider/ | June 10, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 113 | An Interview with Scott Miller - Sudden SinoAmerican Synthesis | https://theamphour.com/the-amp-hour-113-sudden-sinoamerican-synthesis/ | September 16, 2012 |
| 116 | Distribution, Wozniak & Robots - Early Eight-bit Endgame | https://theamphour.com/the-amp-hour-116-early-eight-bit-endgame/ | October 7, 2012 |
| 118 | Kickstarter, Open Source RC & Modelsource - Facinorous Financial Foulness | https://theamphour.com/the-amp-hour-118-facinorous-financial-foulness/ | October 21, 2012 |
| 123 | An Interview with Jon Oxer - Innoxious Implant Innovator | https://theamphour.com/the-amp-hour-123-innoxious-implant-innovator/ | November 26, 2012 |
| 151 | Google Glass, Lean Startup and VotC - Initializing Instructed Interviews | https://theamphour.com/the-amp-hour-151-initializing-instructed-interviews/ | June 24, 2013 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 157 | An Interview with the SparkFun Team - Efficacious Engineering Ensemble | https://theamphour.com/the-amp-hour-157-efficacious-engineering-ensemble/ | August 5, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 182 | Manufacturing By Wire And Skipping Testing - Calefacient Cuculine Cash | https://theamphour.com/182-manufacturing-by-wire-and-skipping-testing-calefacient-cuculine-cash/ | January 27, 2014 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 197 | Spacing Out On Space - Dave's Dongle Designing | https://theamphour.com/197-spacing-out-on-space-daves-dongle-designing/ | May 5, 2014 |
| 244 | The Art Of Staying Interested In Electronics - Exponible Electronics Ennui | https://theamphour.com/244-the-art-of-staying-interested-in-electronics-exponible-electronics-ennui/ | April 7, 2015 |
| 253 | Consolidate All The Things - Zonked Zelotic Zaitech | https://theamphour.com/253-consolidate-all-the-things-zonked-zelotic-zaitech/ | June 9, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 280 | New Year Education | https://theamphour.com/280-new-year-education/ | |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ | March 2, 2016 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 310 | Mergers and Acquiescence | https://theamphour.com/310-mergers-and-acquiescence/ | August 3, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 324 | Mapping Out Nerdery | https://theamphour.com/324-mapping-out-nerdery/ | November 23, 2016 |
| 333 | Science, Not Silence | https://theamphour.com/333-science-not-silence/ | January 25, 2017 |
| 350 | An Interview with Zach Dunham | https://theamphour.com/350-an-interview-with-zach-dunham/ | July 3, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ | October 7, 2018 |
| 417 | Cash Is King | https://theamphour.com/417-cash-is-king/ | November 25, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 500 | Two and a Half Orders of Magnitude | https://theamphour.com/500-two-and-a-half-orders-of-magnitude/ | July 12, 2020 |
| 542 | Component Management with Jan Rychter | https://theamphour.com/542-component-management-with-jan-rychter/ | May 17, 2021 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 564 | Pavlovian Cheapskates | https://theamphour.com/564-pavlovian-cheapskates/ | October 31, 2021 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6, 2022 |
| 585 | Return of the Trade Show Jedi | https://theamphour.com/585-return-of-the-trade-show-jedi/ | April 10, 2022 |
| 707 | Welding with an HDMI Cable | https://theamphour.com/707-welding-with-an-hdmi-cable/ | October 26, 2025 |
