---
title: Kicad
concept: kicad
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

KiCad is an open-source electronic design automation (EDA) suite for schematic capture and printed circuit board (PCB) layout. The project dates from the mid-1990s and followed the trajectory common to long-lived open-source projects: little visible movement for many years, followed by a period in which capability accumulated faster than users could track.[501] Its development rate changed when a research laboratory assigned paid staff to work on the project, adding development capacity that a volunteer project cannot schedule.[172] The tool imposes no layer-count restriction of the kind free tiers of commercial tools have imposed, and supports high-speed differential pairs and arbitrary-angle routing.[669]

## History and development model

KiCad began in the mid-1990s, and for much of its early life visible progress was slow before capability began accumulating rapidly.[501] A contemporary open-source layout tool was arguably ahead technically in the early years; the outcome between the projects was decided by which one accumulated contributors and support rather than by the initial capability of either.[685]

A research laboratory dedicating paid staff to improving the software increased the development rate beyond what a volunteer effort can schedule.[172] The project also acquired a single lead who was employed full time to lead and co-develop it, on the principle that an open-source design tool needs one person driving a coherent direction rather than a committee pulling in different directions.[441]

### Distribution and releases

For years the project expected users who wanted current features to compile the tool themselves, and per-platform builds were maintained by individual volunteers rather than by the project, with different people covering the Linux, Windows and macOS packages.[167] Platform coverage was uneven; the macOS build was long unusable enough that presenting the tool meant running it in a virtual machine on another operating system.[213]

The project's position was that designating some builds as stable implies the others are not, so formal stable releases were avoided, leaving a design tool — where stability matters more than features — with no version the project itself recommended.[167] Working from nightly builds proved less hazardous than that policy suggests: one maintainer whose practice was to update roughly fortnightly reported opening a nightly to find it unusable about five times in a year.[167]

### Domain incident

The project's original domain was registered personally by an early contributor rather than by any foundation, and when it was sold the project had to move to a new domain without a redirect, leaving stale links inside the application itself pointing at an address it no longer controlled.[563] The abandoned original domain was subsequently cloned to look identical to the official site, with the instructions for verifying the downloaded package's hash removed; a design tool distributed by download is a supply-chain target, and the verification step is the defence that was deliberately taken away.[565]

## Versioning and upgrade constraints

The version 6 file format change is one-way: a project opened and saved in the new version cannot be returned to the old one, so upgrading is a decision about the whole project rather than a per-session choice.[523]

Rapid feature addition is simultaneously the project's advantage and its cost to institutional users, who value a tool that does not change between projects; interface changes are where users notice the pace most.[564] Anyone producing tutorial material against a fast-moving tool becomes pinned to an old version, because every interface change invalidates existing recordings; the alternative is maintaining a parallel track of the same course in the current version.[172]

## Design flow

The standard flow is a sequence of separate programs: draw the schematic, associate each schematic symbol with a footprint, import the resulting netlist and footprints into the layout tool, place, route, and plot the manufacturing files.[167]

Tools differ in when the package decision is forced. Where a schematic symbol carries its footprint, the choice is made at part selection; where symbol and footprint are associated at the point of layout, the designer becomes the librarian for every part that lacks a ready footprint. Professional-tier tools tend to require correct library data up front on the assumption that a separate librarian produces it.[131] The gap between having chosen the components and being able to draw the schematic is filled by creating symbols and footprints, a task measured in weeks on a new design and repeated by every engineer using a different tool for the same part.[131]

## Libraries

Shared library efforts fail on insufficient structure rather than insufficient content: a manufacturer's downloadable library of a hundred symbols and footprints, five years old, takes longer to search and validate than creating the one part needed from the datasheet.[131] Third-party libraries are installed by downloading files and placing them in the right location by hand rather than through the application, a barrier to using vendor-supplied parts even where they exist.[508] The official library is maintained in a public repository by designated librarians and bundled with the installer; other vendors' libraries remain separate downloads.[508]

Footprints have long been atomic files, but a downloaded symbol arrived as a whole symbol library rather than a single part, so accumulating parts one at a time produced a library file per part; version 6 makes symbols atomic in the same way, fitting the per-part download model that component library services use.[531] Converting footprints between design tools is limited by what each format can express: slotted holes have no native representation in some tools and must be emulated on a milling layer, and support for them arrived comparatively late in others.[531]

Version 7 added a database-backed library, so a company can hold its parts in a database with multiple contributors and a librarian rather than in per-part files — the infrastructure a team rather than an individual needs.[621] A community script converts a distributor's part identifier directly into a local library entry, fetching symbol, footprint and 3D model in one command; the convenience trades against the discipline of maintaining a curated library, which remains the sounder practice.[700] Designs built around one assembler's in-house parts library get the smoothest and cheapest quotation, but the parts available in that library change, so the bill of materials must be reworked for each build rather than reused.[700]

Creating symbols for large components that must be split across multiple units has been a recurring source of defects, and library work generally is where users coming from commercial tools report the sharpest difference.[549]

## File format, scripting and interoperability

KiCad project files are plain text, so they can be edited directly, diffed and placed under version control with ordinary tooling.[669] What made version control and collaborative workflows work in software was that source is text, which anyone can build tools to process; hardware's equivalent files are usually large, binary and proprietary, and that friction — not any difference in the work — is what has held equivalent hardware workflows back.[577]

Text files make export straightforward and import hard in the other direction: reading another vendor's binary format is where the difficulty lies, which is why importers for commercial formats are a continuing engineering effort rather than a solved problem.[660] Importers for commercial formats are treated as strategically necessary rather than optional, on the reasoning that a tool nobody can move their existing projects into cannot displace an incumbent; the Altium importer in particular has improved.[660] Import of the competing hobbyist format, Eagle, including its libraries, became reliable in version 5, removing the need to redraw an existing body of work in order to move.[404] An earlier approach went further than conversion, reading Eagle libraries directly with no import step, gated behind a compile-time switch while it was experimental.[167]

Because a design is text under version control, a repository hook fired by tagging a revision can regenerate the entire manufacturing package — Gerbers, schematic PDF and bill of materials — so that releasing a board becomes an act of tagging rather than a manual export sequence.[505] Such automation was for some time limited by the scripting interface rather than by the file format, since not every output step was reachable from a script.[530]

A Python scripting engine in the layout tool allowed community plugins to appear, including converters that turn the generic placement export into the format a particular pick-and-place machine expects.[217] An open format plus a scripting interface lets third parties add tooling on top without the tool vendor's participation, and that layer of community tooling has produced capability the core project did not have to build.[449]

## Layout and routing

Push-and-shove routing moves neighbouring traces out of the way while maintaining design-rule clearances as the trace is dragged, so rule compliance is continuous rather than checked after the fact.[480] The tool offers more than one rendering canvas, and the newer accelerated canvas handles operations such as reshaping a plane outline that are awkward in the default one; the choice of canvas therefore changes which editing operations are practical, not only how the board looks.[364]

Net classes are where much of the design-rule checking is configured, so grouping nets for one purpose changes the clearances applied to them.[177] Length matching across a wide bus has been done by assigning the signals to a custom net class and running a script that printed every net's length, then adding serpentine sections by hand until they agreed — a semi-automated loop built from the net class mechanism rather than a length-tuning feature.[177] Matching physical lengths is not the same as matching propagation delay: signals routed on an inner layer travel at a different velocity from those on an outer layer, so a bus split across layers needs delay matching, which the length-matching tool does not provide and which has been done in a spreadsheet alongside it.[469] Choosing a fabricator's published six-layer stack-up and routing on the outer layers gives a microstrip close to 50 ohms against a 40-ohm DDR3 target, close enough for a single memory device; moving those traces to an inner layer changes both impedance and propagation delay.[469]

Version 6 made design rules individually specifiable and scriptable, closing the gap with commercial tools where rules can be written per net, per area or per condition rather than applied globally.[520]

## Simulation and rule checking

The ngspice simulator is built into the schematic editor, so a captured schematic can be simulated without exporting to a separate package.[501] Electrical rule checking in schematic tools remains limited to pin types and voltage levels; checking that an I2C bus is connected to pins configured for I2C, on parts whose pin functions are set by internal multiplexers, is the class of error that current checking does not catch.[375]

## Mechanical integration and 3D

The board and its components can be exported as a STEP model for mechanical CAD, which makes fitting a board into an enclosure a mechanical exercise rather than a guessing one.[473] The exported 3D model carries only a plain board solid without copper or silkscreen, so producing a realistic render requires plotting the copper layers to SVG, converting them to an image and applying that as a texture to the solid in the mechanical tool.[473]

Switching to the three-dimensional view exposes mechanical conflicts, such as a button placed where a connector prevents it being pressed, that are invisible in the two-dimensional layout.[473] Hiding the substrate in the 3D viewer and looking only at the vias and tracks is an effective way to build the mental model of how a multi-layer board connects, the step beginners find hardest when moving from lines on a screen to a physical stack-up.[512] Direct mesh export, along with community add-ons that import a project with its 3D models intact, makes photorealistic rendering of a board possible without a commercial mechanical package in the path; KiCad is one of the few tools that exports directly to Blender as a mesh file.[695]

A scalable bitmap can be placed in the layout as a tracing template, which is how an existing board with no surviving design files is recreated: the image is imported and the connections traced over it.[621] Converting a bitmap into silkscreen artwork is handled by a conversion utility rather than being native to the editor, an approach shared with other tools where the same job is done by a long-lived script documented in the vendor's help pages.[209]

## Manufacturing output

Plane layers are plotted as positive images, unlike tools that treat plane layers as a distinct type plotted as negatives; the distinction matters at the fabricator, and the same board drawn with flooded signal layers instead of dedicated plane layers avoids the issue in either tool.[434] Panelisation is not built in and is done by hand or by external scripts, a routine requirement for anyone having boards assembled rather than merely fabricated.[415]

The drawing origin sits at the top left while the assembly industry works from the bottom left corner of the board, so pick-and-place files carry coordinates in an unexpected frame; telling an assembler where zero is becomes a recurring source of confusion, and writing a parser for the format begins with resolving it.[564] Generating a usable placement file means setting the drawing origin deliberately to match the offset the machine expects, and converting the exported position file into the machine's own format, since the exported format is generic rather than machine-specific.[403] One workable convention places the origin at the centre of the first component so every placement coordinate is measured from it, leaving the machine to relate that origin to the board's fiducials.[477]

Hatched copper fills are not supported, and the workaround is to place a repeated keepout or copper shape on a grid and let the fill flow around it; the technique is needed for capacitive touch designs, where a hatched plane lowers the plane's capacitance so it does not swamp the finger capacitance being measured, while still providing shielding.[288]

Where a factory's engineers cannot open the design files, review can still be iterative: printing the board to PDF for annotation by hand and making the changes in the design tool keeps control of the design with its author rather than handing it to the factory.[450] A supply chain that cannot read the design files at all constrains tool choice, since the interchange format becomes whatever both sides can process.[450] A newer tool can serve manufacturing only because the industry's interchange formats are standardised and open; where the handoff runs on Gerbers and spreadsheets, the design tool at the other end is irrelevant to the assembler.[503]

## Capabilities and limits

There is no layer-count restriction of the kind free tiers of commercial tools have imposed, and high-speed differential pairs and arbitrary-angle routing are supported, so for the majority of professional work the licence rather than the tool is not the limiting factor.[669] The identified limits are at the extremes — very high-density interconnect and very high-frequency designs — where the integrated simulation and interactive design assistance that commercial tools provide are absent; one consultant drew his own line at around twelve layers.[669]

Capability and efficiency are separate questions: any board that can be designed at all can be designed in KiCad, and the argument for a commercial package is the time it saves on a design that occupies a layout engineer for a month, not something it makes possible.[574] Reusing a designed and laid-out block across projects is weak, which matters for consultancies that would otherwise carry a library of proven subcircuits from job to job.[645]

Because there is no vendor, there is no established route for a user to submit a feature request — a real cost of the model rather than an oversight. Version 5 brought the tool into line with standard interface conventions, including copy and paste of symbols.[424]

## Ecosystem position

The cost of a company changing design tools is dominated by recreating library data rather than by licences or retraining, which is why moving is expensive even when the destination tool is free.[441] Inside companies nobody is rewarded for evaluating design tools, and the switching cost is already sunk into the incumbent, so a better tool does not displace it on merit; an open-source tool's route in is from the bottom, by being good enough that individuals bring it with them.[286] An open tool does not replace incumbents by matching them feature for feature; it does so by being distinctly good at enough of the work to be brought in from below, where no procurement decision is required.[286]

Download statistics from a cross-tool component library service put Altium at roughly 30 percent, Eagle at about 25 percent, and KiCad, OrCAD and Allegro at roughly 15 percent each, with the remainder spread across smaller tools.[531] A shared-panel prototype service that began with almost all boards arriving in Eagle format saw KiCad rise to about 75 percent of submissions, with Eagle falling to a quarter or less; as professional firms began using the same service, commercial tools reappeared in the mix.[149] Uptake in Asia has been low relative to the rest of the market, which matters because tooling and ecosystem support follow the installed base.[652]

Moving between layout tools is largely a matter of relearning where the commands are, since the underlying flow of placing symbols, defining pins and connecting them is common; the transferable skill is the flow, not the tool.[675]

## Open licensing in practice

The practical value of the tool being open source, for a user who does not contribute to it, is the option of fixing a blocking defect rather than waiting for a vendor; knowing the option exists changes how much risk the tool carries for that user.[198] Long-term access to a design is a licensing question rather than a technical one: an open tool can be preserved in a virtual machine and will still open the files decades later, with no licence server or expiry in the path.[442] A competitor's move to subscription licensing was the trigger for experienced users to evaluate the open-source alternative, a pattern repeated across the professional user base rather than an isolated case.[480]

On his own open-source hardware project, Michael Ossmann moved off Eagle when the design needed four layers: rather than pay to raise the licence tier, the project moved to a tool that anyone receiving the design could use to modify it, and the same tool was subsequently used for designs involving FPGAs and USB 3.0.[161]

A tool with no licence cost can be introduced two years earlier in an engineering curriculum than one requiring seats, which changes what students can be asked to do and what they can demonstrate outside the course.[711] Running the tool on identical single-board computers with pre-imaged storage removes the first hours of an in-person course, which are otherwise spent installing drivers and software on a room of dissimilar laptops; KiCad runs on the Raspberry Pi.[242]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 131 | An Interview with Andrew Seddon - Necessary Networked Novelty | https://theamphour.com/the-amp-hour-131-necessary-networked-novelty/ | February 4, 2013 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 177 | Discussing Innovation and the Future with Mike Ossmann - Fiesty Festivus Futurology | https://theamphour.com/177-discussing-innovation-and-the-future-with-mike-ossmann-fiesty-festivus-futurology/ | |
| 198 | Mike Ossmann Returns! - Planetic Portalab Packaging | https://theamphour.com/198-mike-ossmann-returns-planetic-portalab-packaging/ | May 12, 2014 |
| 209 | Headless Units and Baseless Batteries - KiCad Kickoff Kopophobia | https://theamphour.com/209-headless-units-and-baseless-batteries-kicad-kickoff-kopophobia/ | July 28, 2014 |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ | |
| 217 | 3D Printed Shark Jumps - Edifying Edison's Energy | https://theamphour.com/217-3d-printed-shark-jumps-edifying-edisons-energy/ | September 22, 2014 |
| 242 | Can't We All Just Get Arduino? - Tardiloquent Trademark Tirade | https://theamphour.com/242-cant-we-all-just-get-arduino-tardiloquent-trademark-tirade/ | March 24, 2015 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 288 | Call In Show #3 | https://theamphour.com/288-call-in-show-3/ | February 24, 2016 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 404 | Proof Of Blink | https://theamphour.com/404-proof-of-blink/ | August 26, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 441 | Motivational Speaker | https://theamphour.com/441-motivational-speaker/ | May 5, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ | June 30, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 480 | An Interview with Ben Krasnow, 8 years on | https://theamphour.com/480-an-interview-with-ben-krasnow-8-years-on/ | February 16, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 503 | Fabless Chip Design with Mohamed Kassem | https://theamphour.com/503-fabless-chip-design-with-mohammed-kassem/ | August 2, 2020 |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ | August 16, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 523 | A Keyzermas Story | https://theamphour.com/523-a-keyzermas-story/ | December 27, 2020 |
| 530 | Living Through Chipageddon | https://theamphour.com/530-living-through-chipageddon/ | February 15, 2021 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 563 | Grumpy Collaboration | https://theamphour.com/563-grumpy-collaboration/ | October 24, 2021 |
| 564 | Pavlovian Cheapskates | https://theamphour.com/564-pavlovian-cheapskates/ | October 31, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 577 | Product Lifecycle Management with Michael Corr | https://theamphour.com/577-product-lifecycle-management-with-michael-corr/ | February 13, 2022 |
| 621 | The Magic of Calipers | https://theamphour.com/621-the-magic-of-calipers/ | February 26, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 669 | Freelance PCB Design with Petr Dvorak | https://theamphour.com/669-freelance-pcb-design-with-petr-dvorak/ | June 6, 2024 |
| 675 | Changing Course with Shawn Hymel | https://theamphour.com/675-changing-course-with-shawn-hymel/ | August 8, 2024 |
| 685 | Data Provenance in the Home, Server, and Fab | https://theamphour.com/685-data-provenance-in-the-home-server-and-fab/ | December 23, 2024 |
| 695 | Making The Invisible, Visible with Sam Aldhaher | https://theamphour.com/695-making-the-invisible-visible-with-sam-aldahar/ | June 3, 2025 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
| 711 | Medical Electronics Education with Mark Palmeri | https://theamphour.com/711-medical-electronics-education-with-mark-palmeri/ | December 21, 2025 |
