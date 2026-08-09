---
title: Gerber
concept: gerber
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Gerber is a vector file format used as the fabrication output of printed circuit board (PCB) design, in which every feature is expressed as lines rather than as higher-level objects, so that even text is rendered into line work rather than stored as fonts.[79] The format originates in photoplotting, in which a wheel of fixed apertures was selected by the file and light shone through the chosen aperture while an XY bed moved the artwork — a heritage that survives in the requirement that a Gerber file name an aperture before drawing with it.[462] Gerber functions as the lowest common denominator of board manufacture: it persists because fabrication houses accept it, occupying a role analogous to G-code for machine tools and PDF for schematics.[208]

## Format and structure

Gerber is a purely vector format: every feature must be expressed as lines, so there is no way to render fonts inside a Gerber file, and any text on a layer exists only as line work that looks like a font.[79] A shape can be expressed either as an arbitrary polygon or as a "flash", a defined primitive stamped from an aperture; pads are normally flashes, which is what allows downstream tools to recognise them as pads rather than as anonymous copper.[299]

The aperture mechanism descends directly from the original photoplotters, which exposed light through one of a set of fixed apertures on a wheel and therefore could only produce trace widths that physically existed on the wheel.[462]

Although nominally a standard, the format is interpreted slightly differently by every EDA package, so a recipient accepting files from all tools is in practice supporting a family of dialects rather than a single format.[320]

The chip-design analogue of Gerber, GDS, differs structurally in that all layers live in a single file rather than one file per layer; the foundry splits the single file back out into one mask per layer.[503]

### Coordinate format and units

The second digit of the Gerber coordinate format sets resolution in mils: 2:5 gives 0.01 mil, 2:4 gives 0.1 mil and 2:3 gives 1 mil, so exporting at too coarse a format quantises the geometry of the whole board.[504] Unit handling introduces a further hazard: laying out to a rounded imperial value taken from a metric specification drifts the board undersize — 0.09 mm is 3.54 thousandths of an inch, and a design built on a quoted 3.5 thou comes out under the intended metric dimension when the Gerber is exported back in metric.[504]

## Information content and limits

Gerber is a downsampling of the design. Net identity is gone once copper is flattened to shapes, so nothing downstream of the Gerber can tell that two touching pieces of copper were intended to be separate nets.[682] The same loss applies to exported outputs generally: Gerbers for boards, STLs for mechanical parts and binaries for firmware are all downsampled results from which the original design intent cannot be recovered.[442] Consequently, a Gerber set is not a reviewable representation of a design; an engineer accustomed to reading schematics has nothing to work from when handed only the fabrication output.[479]

Gerbers also cannot drive assembly by themselves. The Gerber states where the copper is but not which part goes on it, so an assembler additionally needs a merged bill of materials and placement file.[243]

Because the format encodes geometry only, manufacturing intent must be carried explicitly. It is standard advice to embed the stack-up in the Gerber set itself rather than in a covering email, so that the requirement travels with the files.[494] The mechanical layer serves as the carrier for this manufacturing information, not merely the board outline; large companies keep a title-block template on it holding the stack-up and the IPC standards the board must meet.[494] Embedding the stack-up also protects against the files being forwarded to a fab the designer never specified: a competent house compares the embedded stack-up with its own and queries a mismatch before building, whereas a bare Gerber set silently receives whatever stack-up that house happens to run.[494]

Rigid-flex designs cannot be conveyed by an unannotated Gerber set: the files must carry extensive notes on panelisation, the full layer stack, which layer the flex sits on, how far the flex penetrates the rigid section and how much the pads overlap, because the flex and rigid pads are glued together during pre-preg stacking.[415] Before online upload flows existed, the accepted method was a separate mechanical layer carrying worded instructions and arrows marking which region is flex and which is rigid; the format itself never encoded it.[727]

A known interchange break involves inner planes exported as negative images: Altium emits an inverse image for a plane layer, and at least one fab's front end displays those inner layers as blank while still reporting the correct layer count.[434]

## Pre-release verification

Because the Gerbers are what the fab will actually build from, design rule checking is run against the exported Gerbers before they leave, not only inside the schematic-capture tool.[14] A complementary practice is to open the exported files in a Gerber viewer other than the one built into the originating CAD tool: the second renderer draws the board slightly differently and surfaces mistakes the originating tool renders away.[286] Browser-based viewers accept the whole output zip dragged in and render a preview, which makes a pre-send visual check cheap enough to perform every time,[412] and online viewers render the set as a 3D board including vias, so the check covers what the copper and drill data actually say rather than what the layout tool intended.[96]

A fab's upload preview doubles as a file check. OSH Park identifies the layers from an uploaded zip and returns preview images of the finished board, and the service's own operator, Laen, routes in-progress designs through the site for that preview rather than trusting a desktop Gerber viewer.[149] A commercial board house processes and inspects incoming Gerbers before manufacture and emails back anything that looks wrong; a fab that never queries anything is not checking the files.[74]

Output automation is a common source of error. Altium's output jobs script the whole release — Gerber layers, formats and bill of materials — so that a company-standard job produces identical output conventions across every project.[434] A scripted output job is also a single point of failure: a misconfigured job has silently exported only two layers of a four-layer board, and the error was caught by the fab's upload preview showing two layers rather than by anything in the CAD tool.[434]

### Revision comparison

Hardware diffs can be performed by generating Gerbers per layer for two commits, colouring one set red and the other blue, and overlaying them to see what moved between revisions.[162] Overlay diffing requires a common registration mark, so the board outline must be present on every layer for the comparison to align — and then removed before the files are sent out.[162] Automated regression testing of the CAD tool itself can drive the package through building a board and compare the generated fabrication output against a known-good set, catching the case where a tool change silently alters what gets manufactured.[167]

### Fab-side modification

Gerbers are routinely modified by the fab after upload, so debugging a board against the designer's pristine output can hide defects introduced downstream; the corrective practice is to ask the fab for the files it actually built from.[682] The fab's incoming check is scoped to protect its own process rather than the customer's netlist, so a short introduced between two nets during the fab's own file handling passes that check untouched.[682] Comparing fab-modified Gerbers against the original has in practice meant toggling layers manually with maximally contrasting colours assigned across the colour wheel — roughly three hours of visual comparison in a documented case, with no automated tool able to do it.[682]

## Role in fabrication

Fabrication houses each run different Gerber front ends and different CNC routing machines, so every incoming file set is translated into that shop's own machine format — which is why identical Gerbers do not produce identical results everywhere.[149] A fab's own Gerber tooling can also add data the designer never drew, such as a customised serial or QR code auto-incremented across the panel.[680]

At a photo-imaging fab, each submitted Gerber layer becomes a physical exposure transparency — roughly ten to twelve per board, one per copper layer plus solder mask on each side — which are consumed per job.[414]

Automated optical inspection compares scans of the finished board against the submitted Gerbers to catch shorts and breaks.[149] Optical comparison cannot see plating defects, however: a via that did not plate through is invisible to AOI and requires a final electrical test to find.[149] Running optical inspection without final electrical test produced a reported failure rate of about one in 40,000 boards at a prototype-volume fab.[149]

Uploaded designs routinely request capabilities the service does not have — microvias, one-mil clearances — because process limits sit in help files few read; the Gerber upload is where that mismatch first surfaces.[299] The factory's habitual process can also constrain design from the other direction: on Jesse Vincent's keyboard manufacturing programme, the factory's usual board house ran an older two-layer process preferring 12/12 design rules over 8/8, which would not support a USB Type-C connector or fine-pitch parts, so process capability had to be checked before layout was committed.[450] On the same programme, when the manufacturing partner's engineers could not open the design files at all, review ran on printed PDFs marked up by hand with the changes made back in the CAD tool — slow, but keeping design control on the design side.[450]

Boards drawn in a general-purpose illustration tool export Gerbers carrying large amounts of redundant geometry that fab vendors struggle with, and the resulting artwork can carry wrong or missing connections that surface only as a troubleshooting job after assembly.[609]

### Quoting and design-for-manufacture

Every field on a conventional quoting form is already derivable from the Gerber and drill files, so asking the customer to re-enter it is redundant work rather than a technical necessity.[299] Pricing computed straight from the files supports a flat rate by area — a fixed charge per square inch at a six-board minimum, independent of component count as long as courtyard rules are respected.[299] Online design-for-manufacture front ends digitise what a board house's engineers would otherwise report by hand, so uploading Gerbers returns manufacturability findings, a visualiser and pricing without a sales engineer in the loop.[504]

## Conversion to other machine processes

Milling a board in-house is a Gerber-to-G-code conversion followed by a normal CNC job; the conversion works well and the practical failure mode is mechanical, breaking the small drill bits.[223] The conversion reduces the format to a set of lines and then emits a cut move per line segment, which is why curved traces emerge as chains of micro steps rather than as arcs.[462] The same approach drives a desktop vinyl cutter from the paste layer to cut solder paste stencils.[223]

A stencil order is a one-layer job: only the paste layer matters, top and possibly bottom, and drill files are irrelevant, which is why stencil services avoid most of the interchange problems a board house must handle.[320] Because a stencil service needs only a single vector layer, non-electronics work reaches it by converting artwork into Gerber — paint stencils, UV and photo masking, and metal plates for manufacturing.[320]

## Role as an interchange format

Gerber persists on the demand side rather than on technical merit: it survives because fab houses accept it, making it the lowest common denominator in the same way G-code is for machines and PDF is for schematics.[208] As a neutral interchange format it is also what allows a new or open-source CAD tool to reach existing assembly houses at all; without spreadsheets for the bill of materials and Gerbers for the artwork, a shop tooled around the incumbent packages has no way to take the work.[503] For the same reason, a CAD vendor building a board-ordering service is expected to accept Gerbers from any tool rather than only its own output, since tying the service to the tool converts a useful feature into a lock-in mechanism.[122]

Access to fabrication is uneven by region: shops without an online front end require Gerbers by email plus back-and-forth follow-up, while portal-based shops return an instant quote from the same uploaded files.[661] Assembly front ends have moved placement into the browser, so the Gerber upload becomes the canvas on which component positions and rotations are set, rather than those being supplied as a separate file.[700] Conversely, an automated layout service that returns a minimally modified native board file rather than Gerbers keeps the design editable, so the engineer can accept part of the result and rework the rest instead of being pushed straight to manufacture.[626]

## Design data management

When a CAD package goes obsolete and the source files become unopenable, maintenance degrades into editing the Gerbers directly — reconnecting copper by hand, closer to bitmap retouching than to design work.[213] Archiving the version of the design software alongside the design files is a defensible practice precisely because the alternative is being left with only Gerbers years later.[333] For an open-source project built in a proprietary tool, publishing the Gerbers alongside the native files is worth the duplication, because a reader without the tool cannot get at the data in a PCB or schematic document even when viewers exist.[530]

In contract design work, a deliverable of just a hex file and a set of Gerbers undersells the work; in consultant Kieran O'Leary's practice, the client is paying for judgment that appears later as a board passing EMC certification first time, rather than paying for four board spins plus repeated test fees.[492]

Because the Gerber encodes the full copper geometry of a board, it is also a security boundary. Compartmentalising by output format is how design data is kept from suppliers: the board house receives only Gerbers and the test house only test files, and neither sees the design database.[545] Some contracts forbid sending Gerbers out at all, on the basis that they can be reverse engineered, which pushes those companies into in-house fabrication and milling for prototypes.[406]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 14 | China, Entrepreneurs and Blue Collar Reality | https://theamphour.com/the-amp-hour-14-china-entrepreneurs-and-blue-collar-reality/ |  |
| 74 | Younker Youtube Yarling | https://theamphour.com/the-amp-hour-74-younker-youtube-yarling/ |  |
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 96 | Senseless Saccadic Shemozzle | https://theamphour.com/the-amp-hour-96-senseless-saccadic-shemozzle/ |  |
| 122 | Processors, CEOs & Soldering irons - Plentiful Perfunctory Programs | https://theamphour.com/the-amp-hour-122-plentiful-perfunctory-programs/ | November 19, 2012 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 208 | An Interview With Nadya Peek - Gallant Gcode Gerontology | https://theamphour.com/208-an-interview-with-nadya-peek-gallant-gcode-gerontology/ | July 21, 2014 |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ |  |
| 223 | Space Difficulties and Lost Heroes - Wanzing Workshop Whemmle | https://theamphour.com/223-space-difficulties-and-lost-heroes-wanzing-workshop-whemmle/ | November 4, 2014 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 320 | An Interview with Brent of OSHstencils | https://theamphour.com/320-an-interview-with-brent-of-oshstencils/ | October 20, 2016 |
| 333 | Science, Not Silence | https://theamphour.com/333-science-not-silence/ | January 25, 2017 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 479 | Why isn't this working? | https://theamphour.com/479-why-isnt-this-working/ | February 13, 2020 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 504 | This Is Just A Tribute | https://theamphour.com/504-this-is-just-a-tribute/ | August 9, 2020 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15, 2021 |
| 545 | Fear of Banjos | https://theamphour.com/545-fear-of-banjos/ | June 6, 2021 |
| 609 | Open Circuits with Eric Schlaepfer and Windell Oskay | https://theamphour.com/609-open-circuits-with-eric-schlaepfer-and-windell-oskay/ | November 13, 2022 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 680 | Catching Rockets with Musk Sticks | https://theamphour.com/680-catching-rockets-with-musk-sticks/ | October 15, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1, 2026 |
