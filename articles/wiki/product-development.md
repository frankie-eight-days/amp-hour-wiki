---
title: Product Development
concept: product-development
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Product development is the path from a concept to a manufactured, saleable item, spanning concept definition and requirements, detailed engineering including schematic capture, PCB design and firmware, field trials and late-stage verification and validation, and finally EMC testing, safety testing and product approval.[624] It requires mechanical engineering, electrical engineering, embedded systems development, industrial design, and manufacturing and test prototype builds as distinct staffed disciplines.[402] The value of the result is the idea multiplied by the execution, so a strong idea executed poorly is worth very little and learning to execute is the critical skill.[232] Effort is heavily back-loaded: reaching a working prototype represents only about twenty percent of the total effort of a hardware programme, and the last twenty percent of the design work accounts for roughly eighty percent of the total.[340][608]

## Stages of a programme

A staged hardware programme runs proof-of-concept prototyping first, then an industrial design and user-interaction track alongside a separate engineering track, before the two are merged.[402] The engineering track comprises writing specifications, detailed engineering design, component qualification, and physical testing such as drop testing to confirm the product survives handling.[402] The industrial design track produces a looks-like prototype and the engineering track produces one or more works-like prototypes; fusing them into a single engineering prototype is the hardest and longest part of the programme, taking many months.[402]

Early production is typically run in-house before transferring to a manufacturer, at volumes ranging from five or ten units at a time up to about a hundred units a week shipped to customers.[402] Development obligations do not end at the point of sale, since returns and post-sale support are part of the programme and are commonly forgotten in hardware planning.[402] Working in an organisation of roughly 150 people rather than a several-thousand-person division required covering every step from conceptualisation through shipping and support, giving exposure to the whole process at once.[684]

## Where products come from

Ideas are abundant and cheap; the work lies in selecting the right one, reducing it to practice and carrying it to market.[336] Products that begin as a tool built for the designer's own use, and are only recognised as products afterwards, are a common and more reliable origin than starting from the intent to create a product.[218] A related method is the next-bench approach: building a tool that solves a real problem for a colleague at the adjacent bench, which supplies a local customer and rapid feedback on whether the work is worth doing.[232] In a small catalogue company any engineer can propose a product, the group reviews candidates together, and a product that sells modestly may be retained on judgement rather than a hard financial metric.[157]

One route bypasses original design entirely: locating an existing similar item and its manufacturer and commissioning a variant, which is faster than starting from scratch but forgoes the differentiation an original design provides.[255] Where a customer supplies the concept, the requirement typically arrives as a single line, and the engineering content is in the constraints attached to it, such as an aggressive cost target set by a competitor or survival in an extreme environment.[645] Among the hardest skills in the discipline is knowing the market: what it wants and what it expects in price and features.[682]

Most engineering work in this space is development rather than research, consisting of optimisation and part selection rather than novel investigation.[232]

## Validating before committing

Assembling a first prototype from off-the-shelf modules and putting it in front of a customer immediately is a deliberate method for testing whether the concept makes sense before committing development time.[326] Developing for months before showing anything to a customer risks completing a product the customer does not want.[326] Building one unit, ten, a hundred and a thousand are materially different problems, and the step most often skipped is selling ten units to establish that anyone will buy the product at all.[293]

The concept itself can be validated before the product exists, because customers buy against a representation of what the product is supposed to be, and that representation is the cheapest element to iterate.[159] Feedback must nonetheless be sought from the right population: soliciting design comment from an undefined general audience yields responses weighted toward superficial, visible attributes rather than the technical decisions that matter, because only a small fraction of respondents are actual users.[151]

The function of most prototypes is to demonstrate that an idea is unworkable, which is why a prototype precedes committing to full product development.[550]

## From prototype to production

Designing around available development boards and existing software libraries is standard practice, with custom engineering reserved for the parts that differentiate the product.[233] By the time a design reaches manufacturing it differs from the original development-board prototype in almost every respect, so an Arduino-based demonstrator establishes feasibility but not the manufacturable product.[628] Moving from a working idea or prototype into production consumes a large number of engineering hours, and that cost has to be justified against the size of the market.[330] 3D printing has become a standard part of the consumer product development process, used heavily during design even though it is not a mainstream consumer activity.[421]

Early prototypes are circulated with unfinished cosmetics, including hand-applied labels over front-panel controls and no final silkscreen, so that form factor can be evaluated before artwork is frozen.[491] Published specifications also change during development, with the final numbers often settled only at the point the production manual is written, well after prototypes have been circulated against provisional figures.[491] Mechanical and finish details of a polished product are the exception: they must be settled before the order is placed, because unlike much of the electronics they cannot be corrected later.[337]

The effort remaining after a prototype exists consists of certification, transferring to production and working with manufacturers, all of which take substantial time.[608] The share of total effort represented by the prototype depends on product complexity, ranging from around fifty percent for a simple product down to a few percent for a complex one.[608] For products going out to customers, most of the execution effort falls in the final tenth of the project, covering elements such as packaging and customer response, and that is where projects fail.[232] The difficulty in a seemingly simple product lies in the corner cases of deployment: sensor contamination, ingress protection, getting a radio signal out of a metal enclosure, and remote firmware update.[645] Products that require a firmware update immediately out of the box do so because firmware was still unfinished when the units were manufactured.[256]

Defects that survive into a production run are discovered only once units are in customers' hands, and the cost of replacing them scales directly with how many were shipped before the defect was found.[183] Yield close to unity is not always sufficient: a field-emission display programme reached 99 percent pixel yield across the array and still failed as a product, because the human eye detects the remaining 1 percent of dead pixels.[297]

## Tooling and volume economics

Soft tooling costs substantially less than hard tooling and wears out after far fewer parts, but produces units of high enough quality to function as saleable, testable product well before mass-production tooling exists.[159] Most technology platforms exist in a high-production-count and a low-production-count form, such as an FPGA versus a mask-programmed device, allowing early volumes to be served by the more expensive per-unit option.[159] Applying a fixed corporate development process that mandates hard tooling to a product whose forecast volume is thousands rather than millions commits a year of tooling work the volume does not justify.[159]

Regulated products must be built in prototype form well before mass production, because compliance to standards such as ENERGY STAR has to be demonstrated on physical units.[159] Safety approval for a simple mains product can be obtained directly from a local approval authority for on the order of a thousand dollars.[14]

Build quantities of around five hundred units are needed to reach component and assembly price breaks, which ties up a large amount of cash for a small company.[608] A low-volume product is not a priority for its contract manufacturer, so build slots take time and component shortages are often communicated only at the last moment.[342] Once the engineering NRE has been spent, the return comes from the ongoing maintenance and reordering phase, which in small operations remains manual spreadsheet work repeated for every build.[342]

## Schedules and cadence

An experienced designer taking a product from concept through to production has budgeted around a year, or eleven to twelve months, for the whole path.[168] A design cycle of under two years, with eighteen months as the commonly cited figure, has long been treated as the benchmark for consumer and instrument products, and a hardware accelerator's structured engagement with a company runs on average about eighteen months.[229][402] A turnkey design house takes a customer from concept through to production and even marketing over an engagement of a year or two, in contrast to services-only partners who supply a single discipline such as a firmware team.[694] A precision current-measurement instrument developed by a solo consultant took over two years to reach a first product.[527]

Longer figures recur at the far end of the range. The Apple Lisa took about five years to develop, from work starting around 1977 to release in January 1983.[229] A single underlying technology programme ran for sixteen years before it was incorporated into a shipping product.[232] In the appliance industry new models historically appeared only every five to seven years, a cadence set by the design time and the tooling investment rather than by demand.[159] The digital picture frame, by contrast, was developed in 1999 and brought to market in 2000, debuting at the Photo Marketing Association trade show and reaching retail distribution.[424]

In large corporate research laboratories the dominant pattern was to staff a product programme, run it for about two years and then cancel it, so that very few projects from a laboratory of several hundred engineers became products anyone could buy.[232] Large corporations also pipeline development so that successive releases track the semiconductor process cadence, producing yearly improvements an individual developer cannot match.[61] Using a trade show as a development milestone forces a working prototype to exist by that date, which historically produced demonstration units held together well short of production quality.[229]

## Working with manufacturing

A designer involved across all stages of development makes product decisions that are a function of how the item will be manufactured as well as how it is designed.[365] Product development therefore requires leaving the office to talk not only to customers but to the manufacturers, because physical distance from the production floor removes context and control over what is actually being built.[362] A plant's established practice resists processes it has not used before, so a designer proposing an unfamiliar approach is routinely told the line has not done it that way in decades.[365] Offshore production is not a hands-off transfer either; skilled engineers on the manufacturing side still have to shepherd the product through production, and that knowledge remains necessary to the developing company.[682]

Where a subsystem falls outside the team's competence, using a vendor's prefabricated solution or a distributor's field applications engineer trades design ownership for schedule, and is preferred when the objective is shipping the product rather than maximising what the designer learns.[154] Development work has more broadly shifted toward integrating an existing, refined sensor module rather than designing a custom board around the raw sensor, moving the effort into communication, power and application integration.[645] Semiconductor vendors release large numbers of similar amplifiers and data converters because no single part can optimise every parameter, so each permutation of specifications answers a customer requirement an existing part misses.[348]

Engineering team composition on connected products has shifted away from hardware, with one company moving from a hardware-led team to roughly one hardware engineer, four firmware engineers and five software engineers, because software and firmware can be changed after the product ships.[219]

## Business structure

Reselling commodity products is a low-margin business with almost no barrier to entry, so developing proprietary products is the route to margin that is not set by suppliers' prices.[189] Consulting revenue can only be scaled by working longer hours or charging more, both of which have limits, which is the structural reason consultancies develop their own products.[232] Developing an own-brand product generates no revenue until the product is finished and shipping, unlike client work which is billed as it is performed.[470] A consultant developing an in-house product can schedule it as an internal client with carved-out time, accepting that it ranks below paying clients and that the unbilled hours are a direct opportunity cost.[527]

Announcing that a product is being discontinued reliably generates a wave of orders.[362]

Invention-promotion firms that offer to develop and market an inventor's idea have taken years and tens of thousands of dollars without delivering a product; in one case a mains cord with an inline switch took three years to reach market after two such firms produced nothing and one submission failed safety testing.[14] Customer involvement can also disrupt a programme directly: a non-technical customer who inserts themselves into board bring-up, wanting to power up and test the first article personally, typically forces the engineering team to travel to the customer site.[614]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 14 | China, Entrepreneurs and Blue Collar Reality | https://theamphour.com/the-amp-hour-14-china-entrepreneurs-and-blue-collar-reality/ |  |
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ |  |
| 151 | Google Glass, Lean Startup and VotC - Initializing Instructed Interviews | https://theamphour.com/the-amp-hour-151-initializing-instructed-interviews/ | June 24, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 157 | An Interview with the SparkFun Team - Efficacious Engineering Ensemble | https://theamphour.com/the-amp-hour-157-efficacious-engineering-ensemble/ | August 5, 2013 |
| 159 | Interview with Eric Ries - Transorted Testing Tachydidaxy | https://theamphour.com/the-amp-hour-159-transorted-testing-tachydidaxy/ |  |
| 168 | Specialized and/or Open Source Test Gear and Dev Boards - Vacation Videography Vorboten | https://theamphour.com/168-specialized-and-open-source-test-gear-and-dev-boards-vacation-videography-vorboten/ | October 21, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ |  |
| 233 | Glass and Gongkai GSM - Unzymotic Ursidae Upbuilding | https://theamphour.com/233-glass-and-gongkai-gsm-unzymotic-ursidae-upbuilding/ | January 20, 2015 |
| 255 | Inspirations and Aspirations - Recanting Rocket Rationale | https://theamphour.com/255-inspirations-and-aspirations-recanting-rocket-rationale/ | June 24, 2015 |
| 256 | Is This A Show? | https://theamphour.com/256-is-this-a-show/ | July 1, 2015 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 297 | An Interview with Jake Baker | https://theamphour.com/297-an-interview-with-jake-baker/ | May 4, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 336 | An Interview with Bunnie Huang (2nd) | https://theamphour.com/the-amp-hour-336-an-interview-with-bunnie-huang-2nd/ |  |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 365 | Wait, why is Jeff glowing? | https://theamphour.com/365-wait-why-is-jeff-glowing/ | October 30, 2017 |
| 402 | An Interview with Ben Einstein | https://theamphour.com/402-an-interview-with-ben-einstein/ | August 6, 2018 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 470 | Just Add Salt | https://theamphour.com/470-just-add-salt/ | December 8, 2019 |
| 491 | The Almighty Dollarydoo | https://theamphour.com/491-the-almighty-dollarydoo/ | May 3, 2020 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 550 | Finishing Prototypes with Zack Freedman | https://theamphour.com/the-amp-hour-550-finishing-prototypes-with-zack-freedman/ | July 18, 2021 |
| 608 | Vapor Phase with Saber Kaygusuz | https://theamphour.com/608-vapor-phase-with-saber-kaygusuz/ | November 7, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 624 | Design & Manufacturing Consulting with Scott Williams from Xentronics | https://theamphour.com/624-design-manufacturing-consulting-with-scott-williams-from-xentronics/ |  |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ |  |
| 694 | Voltage, Vibes, and VOCs | https://theamphour.com/694-voltage-vibes-and-vocs/ | May 21, 2025 |
