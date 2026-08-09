---
title: Surface Mount Technology
concept: surface-mount-technology
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Surface mount technology is the construction method in which components are attached to pads on the face of a printed circuit board rather than through drilled holes, and it is the process that contemporary assembly infrastructure is built around.[391] Choosing through-hole construction now means working against that infrastructure, because assembly houses are optimised for surface mount and the exception carries a premium; the relationship is not symmetric with component size, since a machine that places small passives places large ones just as easily, so going up in size costs nothing while going back to leads costs a whole process.[391] The consequences reach beyond the assembly line into component selection, layout rules, product form and the economics of small-scale hardware.[82][367][447]

## Relationship to through-hole construction

Through-hole construction is not disappearing. Opening almost any modern consumer product reveals a power supply built on a single-layer phenolic board with leaded parts, because that remains the cheapest way to build that particular thing.[472] Asked how long leaded parts will remain available, the working answer is decades rather than years, since the demand is real and the parts are cheap and easy to produce.[472] Vendors also still ship new parts in dual in-line packages for two practical reasons: prototyping, and being able to pull a damaged device out of a socket and replace it immediately after a static discharge.[3]

There are designs where leaded parts win on specification rather than nostalgia. Surface-mount resistors have modest voltage ratings, around 300 volts even for the extended packages, which makes a several-hundred-volt supply awkward to build entirely in surface mount.[472] Mixing the two technologies on a single part is sometimes the point as well: combining through-hole and surface-mount attachment on a connector gives mechanical retention against shear forces that surface mount alone does not provide.[723]

Construction method also governs repairability. Older equipment built with through-hole or large surface-mount parts, low clock speeds and five or three volt logic has no high-speed differential signalling, so a fault can usually be traced and fixed, or the missing function rebuilt with a small modern board.[463]

## Design consequences

Surface-mount availability now drives which component types get chosen at all. Capacitor selection in particular is influenced by which technologies can be placed by machine, because avoiding a through-hole process entirely is worth a great deal.[367] The same effect appears part by part: a supercapacitor offered in a 1206 reflow-compatible package replaces a leaded round device and simply joins the existing placement run, removing an entire process step from the board.[408]

Component count rather than component value drives placement cost, so cost reduction in a redesign came from shrinking the passives and merging individual resistors into arrays; fewer and smaller parts is a cost decision more than a size one.[11] The floor on how small is set externally: low-cost assembly services publish a smallest acceptable passive size, often 0402, which constrains the design before layout begins rather than after quoting.[285] Capability for the very smallest passives, 0201 and below, sits where phone volumes are, because that is what justifies the equipment, although for genuinely cutting-edge process work domestic suppliers can be easier to work with than distant ones.[113]

A cost-engineered module shows what optimising for assembly looks like: a two-layer board, single-sided surface mount, a simple power chain and a dual in-line form factor, all chosen so that it is easy to automate, easy to package and usable as a component inside somebody else's product.[529]

## Mixed-technology assembly

The process time asymmetry inside a real factory is worth internalising: a board passes through surface-mount assembly in about four and a half minutes, while trimming the leads on its through-hole parts before selective soldering takes around ten.[243]

Selective soldering is how a mostly surface-mount board gets its few leaded parts attached without passing the whole assembly through a wave, using a small nozzle of molten solder on an XY robot that rises from below and solders each pin in turn.[447] That process imposes a layout rule: surface-mount parts on the underside must be kept at least about ten millimetres away from through-hole pins, because otherwise the selective head cannot reach and those joints have to be hand soldered, which is where the cost appears.[447] The alternative is a shield masking whole sections of the board so it can pass through a wave, which is more expensive again, and the ordering of these options is what determines what a leaded connector actually costs.[447] The design-phase consequence is that a single through-hole part brings an extra process step and keep-out areas that constrain the rest of the layout, which makes the question of whether the part is genuinely necessary worth asking before the board is laid out rather than after.[447]

Some assembly services forbid through-hole outright as policy, and refusing the exception is what lets them run every job through one fixed process, which is where their price comes from.[299]

## Process characteristics

Of the available assembly processes, surface mount is the forgiving one: placement alignment has real tolerance and hot air reflow is straightforward, compared with trimming leads on through-hole parts and dealing with solder pots and wave equipment.[153] The physical reason for that tolerance is surface tension, since the parts are small and light enough that molten solder pulls them into alignment on their pads, so heating the board and letting the parts settle works within limits.[183]

Process variability concentrates wherever a liquid consumable is involved. Machine surface mount is remarkably consistent, while hand soldering and fed-solder processes vary much more, which is why the automated step is rarely the source of a yield problem.[279] Placement itself is a solved automated problem rather than a frontier; what remains human is keeping finicky machines running, which is a maintenance role rather than an assembly one.[141]

The quality bar is nonetheless unforgiving. A prototype order may involve one or two thousand individual placements, and every one must be the right part in the right place in the right orientation, so a single dry joint spoils the order.[699] Improving one process step also does not improve the whole: making surface mount ten times more efficient barely moved the overall system, because through-hole, reflow, selective soldering, hand assembly and inspection all remain in the path.[699]

When a defect does occur, evidence rather than description is what gets a factory to act — saying something feels wrong achieves nothing, while a high-resolution photograph of a tombstoned component is acted on within the hour.[279] Co-locating surface-mount assembly with final assembly is worth arranging deliberately for the same reason, because board-level problems are always discovered on the final assembly line and being able to walk between the two is what makes them fixable quickly.[437]

## Supply chain

One missing component stops the entire line regardless of how much of the bill of materials is available: ninety percent of the parts in hand produces nothing at the end of a surface-mount line, which is why shortages hit assembly disproportionately.[628] The supply-chain reality behind moving assembly closer to home is correspondingly unglamorous, since when a line stops for a missing part there is no local market to walk to and buy a reel, because the component distribution that supports the line has followed the manufacturing.[175]

## Bringing assembly in-house

The trap in bringing assembly in-house is that the placement machine is only the first purchase. A reflow oven and a stencil printer follow, and the machines themselves need constant attention both to get working initially and to keep working afterwards.[250] The volume band that forces the decision is a genuinely bad one: several hundred to about a thousand units is too many to hand build and too few to attract good contract pricing, which is what pushes people into buying equipment they had not planned on.[250]

Ball grid arrays are where the home or small-office line stops, because placement accuracy and X-ray inspection are both required and neither is available on a bench.[3]

## Hand work and skill

The intimidation around surface mount rests on a false assumption: people imagine it must be done with a soldering iron, which is genuinely hard, and when shown solder paste methods instead the same people find it easier than through-hole work.[454] The practice this points to is to use paste, a stencil and reflow almost exclusively for surface mount rather than hand soldering, even for one-off boards.[395] A hot plate holds temperature closely and allows a microscope to be placed over the board so the joints can be watched as they reflow, though it struggles with tall components and large boards where thermal gradients across the assembly become the problem.[613]

The honest skill assessment is that surface mount is different rather than difficult: it needs a steady hand, tweezers and probably a microscope, and once learned it is straightforward work at an ordinary bench.[657] The steady hand is a real prerequisite rather than a figure of speech — hand surface-mount work becomes impossible with a tremor, and the work is demanding enough that a medical change can end it regardless of experience or skill.[538]

An educational approach to the process is an oversized working replica of a classic part, made in a surface-mount package with gull-wing leads at matched scale, specifically so that people have something forgiving to practise on.[609]

## Effect on kits

Kits made sense historically because small-scale players had no access to manufacturing at all: nobody would build a hundred boards for an individual, and everything was through-hole and therefore easy to handle by hand, so selling the parts was the only viable form.[178] The economics that ended that era are stark, since a board can be assembled at a local house for a couple of dollars while kitting the same components into bags and labelling them costs more of the seller's own time than that, quite apart from the customer's build time.[178] Kits also carry a negative cost through support, because selling a kit means supporting a kit and a small business cannot afford the time that consumes, which is a separate consideration from whether the kit sells.[82]

A workable rule for whether something functions as a kit at all is that if it takes more than about an hour for an average person to build, it probably does not, unless the act of building carries real value or the product is genuinely impossible to manufacture otherwise.[82] Choosing through-hole purely to keep a product kittable is in any case self-defeating, because it removes the cost advantage that was the argument for selling a kit in the first place; the modern answer for most products is surface mount and current parts, which may cost less outright.[82]

Surface-mount kits are themselves unpleasant to assemble for reasons unrelated to soldering skill: components arrive cut from strips and the passives carry no markings, so identifying what one is holding becomes the hard part.[73] One response is to make the kit cheap enough that failure does not matter, as with a deliberately minimal surface-mount kit sold in a three-pack so that a beginner frightened of the process can destroy one without feeling bad about it.[167]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 3 | HP, IEEE, and Human Interface | https://theamphour.com/3-hp-ieee-and-human-interface/ |  |
| 11 | Ardui...no Dave This Week? | https://theamphour.com/the-amp-hour-11-ardui-no-dave-this-week/ |  |
| 73 | Horrisonous Holiday Habromania | https://theamphour.com/the-amp-hour-73-horrisonous-holiday-habromania/ |  |
| 82 | Vecordious Vacation Variorum | https://theamphour.com/theamphour-82-vecordious-vacation-variorum/ | February 13, 2012 |
| 113 | An Interview with Scott Miller - Sudden SinoAmerican Synthesis | https://theamphour.com/the-amp-hour-113-sudden-sinoamerican-synthesis/ | September 16, 2012 |
| 141 | FPGAs, Robots & Thermocouples - Wampum's Wavering Worth | https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/ | April 15, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20, 2015 |
| 279 | Merry Keyzermas! | https://theamphour.com/279-merry-keyzermas/ | December 22, 2015 |
| 285 | Something's Serially Wrong Here | https://theamphour.com/285-somethings-serially-wrong-here/ | February 3, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 437 | An Interview with Chrissy Meyer | https://theamphour.com/437-an-interview-with-chrissy-meyer/ | April 7, 2019 |
| 447 | Voltnuts for Flashlights | https://theamphour.com/447-voltnuts-for-flashlights/ | June 16, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 529 | Embedded Hardware with the Raspberry Pi Team | https://theamphour.com/529-embedded-hardware-with-the-raspberry-pi-team/ | February 7, 2021 |
| 538 | Missle Man with Bruce Simson | https://theamphour.com/538-missle-man-with-bruce-simson/ | April 12, 2021 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
| 699 | CircuitHub, 12 Years Later with Andrew Seddon | https://theamphour.com/699-circuithub-12-years-later-with-andrew-seddon/ | July 31, 2025 |
| 723 | BeagleBoard's Back with Jason Kridner | https://theamphour.com/723-beagleboards-back-with-jason-kridner/ | May 7, 2026 |
