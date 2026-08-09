---
title: PCB Footprint
concept: pcb-footprint
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **PCB footprint** (also called a **land pattern**) is the arrangement of copper pads, solder mask, solder paste openings, and associated markings on a printed circuit board to which a single electronic component is soldered.[29][70] Footprints are the layout-side counterpart of schematic symbols, and their creation and verification dominate the library-preparation work that precedes board layout, with one practitioner estimating that eighty percent of layout time is spent building footprints for integrated circuits.[29] Because the purpose of designing a board is to have it assembled, footprint decisions are governed by the requirements of the assembly process that will build it, and errors that survive to production can render entire batches of boards or components unusable.[408][337]

## Role in the design flow

Footprint work is front-loaded: the schematic must be complete and annotated with design notes, and every footprint and library component verified correct, before routing begins.[16] On a substantial design this preparation is measured in weeks rather than hours, with as much as a month spent on schematic and library work before layout.[16] Component selection is followed by a drafting phase in which symbols and footprints are put in order before any visible progress is made on the board, a phase that can consume a fortnight on its own.[131]

Design tools differ in when the footprint is bound to the part: some bind a package to each device variant in the library, while others place only the schematic symbol at capture time and assign the footprint when the design moves to layout.[131] Routing can proceed before footprints are finalised, since the layout problem is largely about where the large parts go and how they connect; correcting footprint details afterwards rarely disturbs that work unless a pin assignment is wrong.[219] Verifying whether a part already exists in the library is the step designers routinely skip and later regret, and the presence of ready-made parts makes a simple demonstration board misleading as a measure of true layout time.[172]

## Creation and standards

### IPC land patterns

The industry standards body publishes land pattern guidelines specifying pad geometry for each package type, and professional tools include generators that produce a compliant footprint from dimensions typed out of the data sheet.[29] The standards define more than one land pattern per package — least, nominal and most material conditions, commonly described as small, medium and large — to be chosen according to the density of the board.[70] For a simple chip component, the land pattern is derived from a published formula combining the component's own geometry with the statistical variation in placement accuracy, specific enough to be reverse engineered into a spreadsheet.[29] Package dimension tables in data sheets use letter designations standardised across manufacturers, so the same letters map directly onto the fields of a footprint creation wizard.[408]

### Limits of the standards

The standards are not the final authority they are often taken for: many companies mandate the manufacturer's footprint instead, or their own in-house standard, or the footprint supplied by whoever assembles their boards.[29] The assembler's preferred footprint carries weight because that company has optimised it for the specific machine that will place the part, making it the version most likely to yield well; the question that settles disagreements is empirical — what actually works in the process that will build the board.[29] The relationship can also run the other way, with a company imposing its own standard footprints on the assembler, who generally accepts them and produces acceptable results.[70] A design taken to extreme density cannot use the standard land patterns at all, because they are simply too large for the space available.[29]

Even a tool shipping a complete standards-based library does not eliminate the work: new and obscure packages keep appearing, a part may or may not need a thermal pad, pads may need extending to accept test probes, and the pattern may need adapting for a particular assembler.[29] Essentially every project introduces at least one part needing a new footprint or a modification of an existing one, although the workload falls off once the common passives and standard packages are built.[29] Footprints bundled with entry-level tools are widely regarded as inadequate, being noticeably oversized relative to what a reasonable design would use.[29]

## Design for assembly

Choosing the footprint for the specific model of assembly machine that will build the board ties the design to that manufacturer and that line, since yield depends on the match between pattern and equipment.[143] In practice this coupling is accepted rather than hedged: boards are designed for one manufacturer and one assembly machine, rather than maintaining alternative outputs for different suppliers.[143]

Details of the footprint beyond the pads matter to the assembler. Placing the pin one marker directly over the pin one pad — a common default in supplied libraries — makes it useless to the assembler, who must then correct the reference and centroid point for every component by hand.[408] The solder paste layer is part of the footprint and can be modified so that a part intended for hand placement is excluded from the stencil.[415] Documentation aimed at manufacturing needs to record which footprints are troublesome, including patterns that cause components to tombstone during assembly.[373]

### Leadless packages

For leadless packages, extending pads past the edge of the package — against the manufacturer's advice — makes the part hand-solderable, because heat has to be applied to the pad from outside the body of the chip.[154] The central thermal pad of such a package can itself serve as the heat path: with vias placed under the pad, the joint is soldered from the underside of the board and heat travels up through the part to the perimeter pads.[154]

## Failure modes and verification

Footprint errors differ enormously in severity: a slightly wrong pitch or body width is recoverable in a way that a transposed pin assignment is not.[201] Bottom-view package drawings in data sheets are a recurring source of transposed pins; the three-dimensional package views manufacturers have begun including remove the ambiguity.[367] A further trap is a package that exists in narrow and wide body variants distinguished only by a suffix, where the library already holds a correct footprint for the other variant.[339]

A wrong footprint also compounds diagnosis: it produces soldering difficulties that absorb attention while the actual fault lies elsewhere, and because verifying the footprint tends to be the last thing anyone looks at, a footprint fault can absorb days of debugging directed at everything else.[203][137] A footprint error that survives to production is expensive at scale; in one case fifteen thousand switches were left unusable because the pattern was wrong.[337] Components can themselves be out of specification for their nominal package, as when a supposedly standard chip capacitor from a major manufacturer arrived physically narrower than the package definition allows.[299]

A thorough check assumes nothing: every pin on the schematic is cross-referenced against the data sheet, and the footprint's pitch, dimensions and pin mapping are each checked against the schematic in turn.[201] The working rule is to check the part against the data sheet first, rather than trusting that a footprint already present in one's own library is the right one.[339]

## Library management

Most established companies maintain their own libraries as a matter of policy, using neither the manufacturer's parts nor those supplied with the design tool.[70] A component librarian's job is to verify the footprint dimensions against the data sheet, follow the land pattern standard, obtain the three-dimensional model, confirm every pin on the symbol, and maintain the library over time.[358] Dedicated librarians can be a separate function in another location, producing footprints on request while design engineers tie parts together at a higher level.[445]

Assigning internal part numbers to approved components is long-established practice at large manufacturers.[408] The value of an approved-parts database is that a defect found on one project propagates to every other project: a part that has been signed off, given an internal part number and proven in a previous design carries a footprint known to be correct.[408]

The number of library entries for a nominally simple component multiplies as a tree — schematic symbol style, then tolerance, then temperature coefficient, then the small, medium or large land pattern — so a single resistance value can occupy twenty entries in the system, and the immediate consequence is picking the wrong variant, since the entries differ only in attributes not visible on the schematic.[445] The formal process for requesting a new part — submitting the specification, an example data sheet, an approved manufacturer part number and the required footprint variant, and waiting for it to be tied back into the database — can consume hours on a single resistor.[445] Where getting a footprint defined takes weeks, engineers route around the official tool entirely and lay out small boards in whatever package they can access themselves.[472]

Storing each footprint and each symbol as its own file rather than as entries inside a monolithic library makes the collection tractable under revision control and allows parts to be moved individually.[370] Editing a footprint in place on the board, where a tool allows it, is convenient and correspondingly dangerous, since a stray action can change the placed part's package without any separate step to catch it.[315]

## Shared and universal libraries

A single universal component library is a perennial question in the design-tool industry and works only in principle, because every tool has its own conventions and every company its own requirements.[408] Standardisation across tools, with an open interchange format as the route to shared libraries, is characterised as the industry's unattained goal.[70]

A shared library service can avoid being siloed by tool if symbols and footprints are authored in a neutral editor on the service and converted to each design tool's format on the back end, so every part is available in every tool.[131] The cost is that existing libraries cannot simply be uploaded: each part must be entered once in the neutral form before it becomes available to everyone.[131]

The deeper obstacle is trust. Shared library services struggle commercially because companies verify every part regardless: a service correct on 99.9 percent of parts still leaves an error that could cost hundreds of thousands or millions of dollars, and that checking can cost more time and money than building the footprint from scratch.[118] A footprint obtained from someone else generally gets taken apart and rebuilt anyway, so the notional saving does not materialise.[29] On this point Tim Ansell, speaking as an experienced designer, held that shared part libraries offer little value because the footprint is essentially the whole content and building it oneself is the only way to know it is right.[375] Outsourcing library work can nonetheless be defensible on cost: paying fifty or a hundred dollars for a part looks expensive until compared against the two hours a footprint can take to build properly.[358]

Distributors have their own interest in libraries. A component distributor acquires a design tool in order to sell components, which drives the goal of a library in which every part carries its footprint, symbol and data sheet linked to the catalogue.[21] Distributor-linked libraries with parametric search built into the design tool were expected to become universal, though early implementations were incomplete and frequently lacked footprints for less common parts such as connectors.[145]

## Prototyping and packaging constraints

Breakout boards that convert a surface-mount package to a through-hole footprint are cheap to produce and are sold as panels carrying many different patterns, so a single inexpensive panel covers most packages a designer will meet.[18] Modern package footprints have grown too fine for in-house board milling, so a breakout is needed regardless — an argument for manufacturers supplying samples already mounted on carriers.[275] Patents covering package and footprint technology are part of why straightforward second sourcing has become rare, since two manufacturers' equivalent parts no longer share a land pattern.[104]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ | |
| 18 | Transistor Types and Where To Get Electronic Gear | https://theamphour.com/the-amp-hour-18-transistor-types-and-where-to-get-electronic-gear/ | |
| 21 | More Freeagle, More Benches and More Engineers on Twitter | https://theamphour.com/the-amp-hour-21-more-freeagle-more-benches-and-more-engineers-on-twitter/ | |
| 29 | DJ and Jazzy Jeff | https://theamphour.com/the-amp-hour-29-dj-and-jazzy-jeff/ | |
| 70 | Idiorhythmic IPC Inconcinnity | https://theamphour.com/the-amp-hour-70-idiorhythmic-ipc-inconcinnity/ | |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 118 | Kickstarter, Open Source RC & Modelsource - Facinorous Financial Foulness | https://theamphour.com/the-amp-hour-118-facinorous-financial-foulness/ | October 21, 2012 |
| 131 | An Interview with Andrew Seddon - Necessary Networked Novelty | https://theamphour.com/the-amp-hour-131-necessary-networked-novelty/ | February 4, 2013 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 143 | PCBs, Tektronix & Ham Radio - Habitual Handicraft Hangups | https://theamphour.com/the-amp-hour-143-habitual-handicraft-hangups/ | April 29, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 154 | Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing | https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/ | July 16, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 201 | Cheap Respins And A Time Machine - Multiscience Mercenary Marketplace | https://theamphour.com/201-cheap-respins-and-a-time-machine-multiscience-mercenary-marketplace/ | June 2, 2014 |
| 203 | Tesla, Checklists and Bullies - Emerging External Eupsychics | https://theamphour.com/203-tesla-checklists-and-bullies-emerging-external-eupsychics/ | June 16, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 275 | No One Even Missed Us? | https://theamphour.com/275-no-one-even-missed-us/ | November 19, 2015 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ | March 12, 2017 |
| 358 | Mergers and People Acquisitions | https://theamphour.com/358-mergers-and-people-acquisitions/ | September 4, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 445 | Ludicrously High Frequency Interference | https://theamphour.com/the-amp-hour-445-ludicrously-high-frequency-interference/ | June 2, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
