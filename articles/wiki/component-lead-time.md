---
title: Component Lead Time
concept: component-lead-time
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Component lead time is the interval between placing an order for an electronic part and receiving it, and it governs whether a design can be built at the scale and on the schedule intended. The divide between hobby and production buying is where lead time first bites: obtaining five parts from a distributor is easy and obtaining five thousand is a different problem entirely, so a listing showing a handful in stock says nothing about whether ten thousand units can be built.[1] The threshold at which it starts to matter is a few hundred units, below which the market absorbs the demand invisibly and lead time is never considered at all, which is why it arrives as a surprise to those scaling up for the first time.[287] The working maxim is that parts are not real until they are in hand, since confirmations, quoted dates and stock listings are all provisional in a way that plans built on them are not.[558]

## Normal lead times and their physical basis

Six to eight weeks is a normal lead time even in good conditions rather than a sign of trouble, which is worth knowing before treating any quoted delay as evidence of a shortage.[287] There is a physical floor underneath that number: a fab run alone takes at least thirty days, before testing, packaging and shipping, so nothing short of a priority lot compresses it much.[210] Because supply must be committed ahead of that floor, vendor sales organisations are measured on forecasting accuracy; they must predict demand well enough to avoid both shortage and excess inventory, and that estimate is what determines the lead time a buyer is quoted.[210]

## Stock listings and allocation

Distributor stock is not a reservation. Five thousand pieces showing in stock looked like a safe margin for a design in progress, and a single other buyer took nearly all of it before the design was finished.[8] The same thing happens at small scale and fast: parts in stock the previous day can be at zero when the order button is pressed, with a twelve-week lead time behind them.[287]

Allocation is hierarchical rather than first-come. A very large customer arriving bumps everyone else, and the displacement ripples down through the chain to the smallest buyers, who experience it as an unexplained delay.[287] Position in the queue also depends on the channel: distributors place their own long-lead orders and are fulfilled first, which puts a manufacturer's web storefront a distant second in the same queue.[546] Where a part is bought therefore changes a buyer's position, not just the price.[546]

An absurd quoted date is an admission rather than a schedule; when a vendor quotes years into the future it usually means it genuinely does not know, and the number carries no information beyond that.[558]

## Sources of disruption

Boutique parts concentrate supply risk in a single facility, so a fire, a strike or a trade restriction removes the entire supply at once with no second source to fall back on, which is the real cost of a specialised part.[524] Natural disasters propagate through the chain for months rather than weeks: a flooded factory supplying automotive components produced six-month waits on finished goods far downstream of it.[245]

Shortages do not respect assumptions about which parts are safe. One year saw long lead times specifically on through-hole components, and older packages were sometimes more available than modern equivalents, which inverts the usual advice.[472] Long lead times also returned after a period in which the industry had come to treat them as historical, with six-month waits on common modules arriving barely a year after the subject was being treated as a thing of the past.[520]

A reputation for poor supply is durable and expensive. One manufacturer's inability to ship led to blanket internal rules at large companies never to design in its parts, and engineers burnt by it still refuse decades later.[44] The cause in that case was product proliferation: introducing hundreds of new chips a year while being unable to supply them in volume, which is a warning against judging a vendor by catalogue breadth.[326]

## Consequences for design and business

For a funded product the consequence is that the design gets locked far earlier than anyone would choose, with orders for production quantities going in immediately after funding closes because the lead times leave no alternative.[175] The same pressure applies at small scale, where committing several thousand dollars to a reel of parts before a campaign even launches is what makes prompt delivery possible, so the money goes out before any comes in.[175]

Being single-sourced on a part with a three-month lead time can force a board respin purely to escape the situation, which is far more expensive than the part itself.[104] A recurring root cause of such trouble is part selection made for the wrong reason: choosing a chip because somebody supplied a development board, then discovering at production that it carries a twelve-week lead time or is obsolete, happens often enough to be a pattern.[135] Sorting by distributor price is reasonable but carries a hidden risk, since a low price may reflect stock being cleared rather than a competitive position, leaving long lead times or a much higher price once that stock is gone.[211] Engineers make these decisions without supply-chain visibility, and the short-term choice damages the product's longevity, which is the argument for identifying replacement parts during design rather than during a shortage.[211]

The worst outcome is not the wait but the cancellation at the end of it: waiting twenty-eight weeks and being told in the twenty-eighth week that the order is cancelled, because someone else paid more, destroys the plan the wait was supposed to protect.[570] That pattern is what closes small businesses, since being told six months, planning around it, and then learning at the end that the parts will never arrive makes running a small operation close to impossible on those terms.[613]

## Second sourcing

Designing a high-volume product means choosing parts with reason to believe they will remain available, and that have a second and preferably a third source, because a part available from only one vendor makes the product hostage to that vendor's decisions.[5] Genuine second sourcing has nonetheless become harder because manufacturers use different packaging and footprints, sometimes protected, so the old practice of one company simply producing another's part has largely gone.[104]

A broader and still workable definition of second source is a different variant from the same manufacturer: the higher-performance version of the same part costs more but may be available immediately, which is a way out of a shortage rather than a design compromise.[104] A vendor publishing its wafer stock position, such as having enough on hand to produce twenty million chips, is likewise making a supply commitment rather than a technical claim, aimed at designers deciding whether to commit to the part.[574]

## Mitigation and purchasing practice

A scheduling arrangement solves much of the problem for a small buyer: the distributor is told the expected volumes over coming months, holds the parts against that forecast, and the payment clock starts when it ships rather than when the buyer commits.[237] Getting into the queue is the part that matters, and it does not necessarily commit the buyer to taking delivery of everything ordered, which makes placing an early order on a long-lead part a cheap piece of risk mitigation rather than a financial commitment.[455] A stock-on-hand strategy makes fast work possible in the same way: buying reels of a known good part in quantity, two thousand at a time, so any project can start immediately, because even the normal lead time on that part is several weeks.[224]

Direct manufacturer relationships can produce structural priority. In one case the manufacturer arranged a distributor part number flagged specifically so that orders against it were handled differently from ordinary ones.[178] Going directly to the manufacturer for help works even at very small volume when the part is genuinely irreplaceable, and is worth trying before redesigning around the shortage.[527] The position that prompts such a request is a microcontroller on allocation with an advertised lead time beyond fifty-two weeks, which automotive customers spending far more money were also unable to obtain.[527]

During a shortage the practical mitigation is footprint-compatibility searching: working down every datasheet in a category looking for anything that shares the footprint of the part that is now a year out, then judging which compromise is least bad.[637] Shortages also push designs toward highly integrated modules chosen for availability rather than suitability, where a converter module with everything inside is overkill and costs more but is purchasable, which outranks elegance.[558] The conversation this forces with a client is about total elapsed time rather than the shortage itself, since redesigning around an unavailable part means design, prototypes, qualification and the risk of something being wrong, so waiting twenty weeks can be the better option.[601]

## Market intelligence

Large distributors employ analysts who model shortages properly. For ceramic capacitors the analysis runs to which eight companies make ninety percent of the market, how much research budget each has, and where that budget is going.[451] That analysis converts a static number into a forecast: a seventy-two week lead time with a strong probability of improving within weeks is a different decision from the same number treated as fixed, and it can change whether the part is designed in at all.[451] Access to that analysis comes from engaging with the distributor early rather than at the point of ordering, which is one of the concrete advantages that scale confers on a buyer.[451]

A free approximation is available to anyone: entering an absurdly large quantity on a distributor's site and reading back the lead time it quotes exposes the real supply position behind a stock number.[377] Commercial terms are another indicator. During the worst period quotes became non-cancellable and non-returnable with payment up front, and as supply recovered they became cancellable and changeable again, which signals where the market actually is.[693]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 1 | What's In A Name? | https://theamphour.com/1-whats-in-a-name/ |  |
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ |  |
| 8 | Layouts and Design-Outs | https://theamphour.com/the-amp-hour-8-layouts-and-design-outs/ |  |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ |  |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 210 | Risky Components and Hardware Innovation - Slipshod Shack Shutdown | https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/ | August 5, 2014 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 451 | An Interview with Scott Miller (2nd) | https://theamphour.com/451-an-interview-with-scott-miller-2nd/ | July 21, 2019 |
| 455 | Bill and Dave's Excellent Equipment | https://theamphour.com/455-bill-and-daves-excellent-equipment/ | August 19, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 558 | Toasted Marshmallow Connectors | https://theamphour.com/558-toasted-marshmallow-connectors/ | September 19, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 693 | Small Scale Electronics Manufacturing with Colin O'Flynn | https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/ | May 13, 2025 |
