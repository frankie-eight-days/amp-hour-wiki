---
title: Design Rule Checking
concept: design-rule-checking
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**Design rule checking** (DRC) is the automated verification of an electronic design—an integrated-circuit layout or a printed circuit board—against a set of geometric and manufacturing rules before the design is released for fabrication.[706][718] A passing check establishes that a design is manufacturable, not that it functions: nothing in the check verifies design intent, so a layout that connects a converter to nothing can still be DRC clean.[501] Because the check is typically the last gate before an expensive fabrication run, it occupies a named place on release checklists, alongside generating Gerber files and the bill of materials.[287]

## Scope and relationship to other checks

Design rule checking has no inherent scope limit and can be extended to any checkable design constraint, including non-geometric ones such as a bill-of-materials cost target; electrical rule checking (ERC), by contrast, is confined to the electrical correctness of the connectivity.[342] Schematic-level ERC typically verifies only pin electrical type and voltage-level compatibility, and does not check that a signal has been connected to a functionally appropriate pin—for example, that an I2C bus lands on a device's I2C-capable pins where pin multiplexing allows many alternative assignments.[375] Some connectivity checking of the ERC kind is embedded directly in IC DRC decks, while layout versus schematic (LVS) provides the separate comparison of the drawn layout against the intended netlist.[501]

Rule checkers catch only errors that have been declared illegal, such as tying a power input to ground; they cannot catch a connection that is legal yet functionally wrong, such as reversed RX and TX lines.[499] Nor is there a rule-check equivalent for signal integrity: identifying insertion-loss or crosstalk problems requires setting up a field simulation rather than running a rule check, a recognised gap in the everyday hardware workflow.[681]

## Integrated-circuit verification

### History and scale

Integrated-circuit design rule checking was originally performed by teams of human checkers working with slide rules against a printed rule book; it is now a software step, with the foundry supplying a machine-readable rule file alongside the manual.[706] An advanced-node rule deck contains millions of individual rules, and a full check run takes a long time to complete.[706]

### Verification sequence

The IC physical-verification sequence runs DRC first, to a clean or almost-clean result with a small number of waived rules, then layout versus schematic, then parasitic extraction; where a PCB tool folds the shorts check into DRC, IC flows split connectivity checking into a separate step.[706] LVS checks that the drawn layout implements the circuit captured in the schematic; the subsequent extraction step reads only the layout and produces a SPICE netlist including parasitics, expanding a hand-drawn schematic of tens of lines into millions.[706] Chip layouts are run back through design rule checking before mask generation, confirming the geometry is legal for the process and manufacturable, though the check will not catch an accidental short between power and ground.[687]

### Rule content

Advanced IC processes carry voltage-dependent design rules: the minimum permitted spacing between two pieces of metal grows with the maximum voltage difference across them, so nets at 700 mV, 1.2 V and 1.8 V each require progressively larger separation.[706] Rule decks include electromigration checks, which limit current density in a wire: a sustained DC current through a very thin conductor progressively displaces the metal atoms through collisions with electrons and can open the wire years after manufacture.[706]

Metal density is itself a checked design rule because chemical-mechanical polishing depends on it: a die with too little metal polishes into a dip, which on a multi-project wafer damages neighbouring designs as well as its own.[579] Density violations are cleared by automated metal fill: a script walks the die zone by zone and inserts dummy metal polygons where the density is short.[579] Verification tooling extends past geometry to circuit-level hazards, with checks that report whether a layout will cause latch-up or an electrostatic-discharge failure.[579]

From the 16 nm FinFET generation onward, multiple patterning removed the freedom to orient devices arbitrarily: because a single layer is split across several exposures, all gates must run in the same direction, and the DRC rule stack grew enormously as a result.[553] Only two or three semiconductor companies in the world can run 5 nm and 3 nm processes—TSMC and Samsung, with Intel potentially joining them—and the tooling required is correspondingly expensive.[553]

### Rule decks

Foundry design rules are delivered as a PDF manual of numeric values covering metal spacing, metal overlap of via and similar geometry; building a usable checker means transcribing those numbers into a rule deck the layout tool can read.[503] A rule deck ports reasonably well between older process nodes because the physical effects and the number of metal layers are similar down to roughly 90 nm, so adapting a deck to another node is largely a substitution of parameters rather than a rewrite.[503]

Rule decks are validated against foundry-supplied reference layouts with known outcomes—one GDS designed to pass and another designed to fail specific rules; running the checker must reproduce the expected number of failures on each, and a shortfall means the deck is missing checks.[503] The manufacturing rules used for that validation cannot be waived: the deck under test and the foundry's design rules manual must express the same rules for the comparison to mean anything.[503] Pre-tapeout DRC at a foundry is exhaustive down to details such as the layers used and the number of elements in a polygon, leaving essentially no scope for a design to slip through with an irregularity.[579]

### Limitations of automated checking

An early design rule checker tested only proximity, not connectivity: metal routed directly across another conductor satisfied the spacing rule and passed. On the project Bil Herd described, the resulting chip shipped with the A10 address line shorted to A9, A8 and A7, so the part could not be addressed at all.[222]

ASIC place-and-route output routinely emerges from the tool with a couple of thousand design rule violations still in it, and repairing them by hand is a paid job rather than an exception.[501] Automatically generated mask output is likewise not trusted on its own for an expensive tapeout; the masks are inspected by hand before submission because a full manual review of a real chip takes a great deal of time.[390]

## Tools

Three vendors supply full analog IC tool stacks: Cadence, Synopsys and Siemens (formerly Mentor). A foundry may support only some of them for a given technology, forcing the choice; Siemens' Calibre is the de facto standard for DRC and LVS even where Cadence dominates schematic capture and layout entry.[706]

In the Magic VLSI layout tool, the process rules live in a `.tech` file holding minimum and maximum spacings between each pair of layers, layer thicknesses and MOSFET characteristics; with the file loaded, the editor flags a spacing violation as the geometry is drawn.[390] The Magic editor ran its checker continuously in the background while polygons were being drawn: a violating shape started blinking immediately, and clicking it named the rule that had been broken, allowing correction in effectively real time—an approach Tom Lee recalled from his own use of the tool.[459]

Some component domains have no design-rule-check infrastructure available to the customer at all: LCD manufacturers each perform the equivalent checking with their own in-house tools at their end.[400] A layout tool that permits arbitrary shapes gives up automated checking as the price of that freedom; Saar Drimer, whose work involves freeform board outlines, noted that nothing in such a tool reports that two routes have come close to each other, so all electrical and design rule checking has to be carried by the designer.[286]

## Printed circuit board practice

### Rule sources and net classes

Much of a modern PCB rule set is expressed through net classes rather than as global values, so clearance and width rules attach to groups of nets and the checker enforces different limits in different parts of the board.[177] Constraint-driven checking extends beyond geometry to electrical performance: propagation-delay limits are entered up front, the tool computes the RC of each trace, checks continuously during layout, and reports the violating locations for correction.[8]

Rule values must be taken from the fabricator's published capability sheet rather than left at the CAD tool's defaults. In the layout-review practice of Zachariah Peterson, designs are routinely submitted carrying hundreds to thousands of outstanding DRC errors—900 errors is common, with cases up to roughly 3000 observed—and the underlying cause is usually a rule set left at the tool's defaults rather than genuinely difficult geometry; five minutes spent retrieving a manufacturer's capabilities and entering those numbers clears roughly 90 percent of the violations that default rules generate.[718] Tool defaults exist only because the vendor has to ship some number, and are not a recommendation; determining the actual constraint the design will be built under, and then confirming the layout satisfies it, is the designer's responsibility.[718]

Setting the working design rule slightly looser than the fabricator's stated minimum—for example 3.75 mil against a 3.5 mil capability—preserves headroom to tighten locally where the routing demands it, instead of designing the whole board at the process limit.[504] Conversely, changing a clearance or width rule after the board is routed generates violations in bulk and leaves the layout over-constrained: one such change produced 850 DRC errors, made push-and-shove routing unusable, and would have required a full reroute or a move to more layers.[504]

Live design rule checking during routing gives continuous feedback at the point of editing, but working permanently at that zoom level obscures board-level problems that only become apparent when the physical board arrives.[718]

### Fabricator-side checking

Some fabricators run fully automated inbound checking and reject a design for a single track 0.001 mm outside the stated capability, so the design's own rule set must be set strictly to that fabricator's limits rather than to approximate values.[224] Other prototype board houses run no design rule check on submitted Gerbers at all and will fabricate a design that breaks their own published rules, which makes the designer's local DRC the only check performed.[291]

Fabricator-side checks on Gerber data have no net-name knowledge because connectivity is discarded in the Gerber format; they can only test whether copper is too close to copper, which protects the fabricator's process but cannot distinguish an intended connection from an accidental short between two nets.[682] On the CircuitHub contract-manufacturing line, inbound designs are run through a suite of tools that checks the submitted design against the netlist and confirms it can physically be manufactured and that any stack-up complexity is feasible; simple two- and four-layer boards generally pass without human involvement, while designs pushing the process envelope still receive human review.[699] Omitting local DRC and ERC transfers the checking to that inbound review, turning each error into a reject-and-resubmit cycle that can take a day per iteration across time zones.[699]

Running a design rule check across a panelized array is substantially harder than on a single board, and manually copy-pasting a board to build a panel risks omitting objects from the selection; panel-level checking is practical mainly at the Gerber stage, which is where fabricators perform it.[400] Artwork or graphics constructed as pseudo-components on the copper layer defeat design rule checking: once a real component is placed over such a fill, the checker can no longer be relied on for that area.[288]

### Tight-pitch routing

A 0.35 mm-pitch wafer-level chip-scale package was routed on a six-layer via-in-pad process where 0.25 mm is the minimum via-to-pad distance; sitting exactly at that limit requires the layout grid to be configured to match, because anything off-grid is rejected by the fabricator's DRC.[692]

### Automated layout

For layouts produced by automated routing tools, the acceptance baseline before any signal-integrity or physics consideration is 100 percent routing completion with zero DRC violations; anything short of that counts as a failure of the tool.[626] Such output is run back through an independent design rule check on the downloaded board file as a final confirmation before release to fabrication.[626]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 8 | Layouts and Design-Outs | https://theamphour.com/the-amp-hour-8-layouts-and-design-outs/ |  |
| 177 | Discussing Innovation and the Future with Mike Ossmann - Fiesty Festivus Futurology | https://theamphour.com/177-discussing-innovation-and-the-future-with-mike-ossmann-fiesty-festivus-futurology/ |  |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ | February 24, 2016 |
| 291 | Artificially Intelligent Party Platform | https://theamphour.com/291-artificially-intelligent-party-platform/ | March 16, 2016 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ | April 29, 2018 |
| 400 | Once Every Couple Months | https://theamphour.com/400-once-every-couple-months/ |  |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 504 | This Is Just A Tribute | https://theamphour.com/504-this-is-just-a-tribute/ | August 9, 2020 |
| 553 | Debunking with Shahriar | https://theamphour.com/553-debunking-with-shahriar/ | August 10, 2021 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 692 | Like a steam engine in your house | https://theamphour.com/692-like-a-steam-engine-in-your-house/ | April 15, 2025 |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ | July 31, 2025 |
| 706 | Leading Edge Analog with Joren Vaes | https://theamphour.com/706-leading-edge-analog-with-joren-vaes/ |  |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
