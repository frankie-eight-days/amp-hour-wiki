---
title: Soldering
concept: soldering
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Soldering is a joining process in which a filler alloy is melted to form electrical and mechanical connections between components and a board, and it is the dominant method of electronic assembly at both bench and production scale.[183][279] Despite its apparent simplicity, the field extends to land-pattern standardisation, long-term reliability chemistry, and volume-manufacturing process control, to the point that a product made in millions can justify a year of research into joint chemistry alone.[183][531] It is not, however, the most reliable joining method available: telecommunications practice favours crimping and wire wrapping, and building wiring standards prohibit soldered connections in permanently installed wiring outright.[183]

## Technique

The fundamental hand-soldering operation reduces to holding the iron tip flat against the joint so it makes thermal contact, letting heat transfer into the work, and then feeding solder into the heated joint.[413] The characteristic beginner error is attempting every part of the operation at once — holding the component, the board, the iron and the solder simultaneously — when the work should be arranged so that everything is already in position and the joint simply held long enough for heat to transfer.[413] Speed and joint quality trade against each other directly, a lesson typically learned by soldering as fast as possible and then having to rework the result.[459]

Drag soldering of surface-mount devices marks the boundary of a beginner's course, sitting just beyond through-hole work and short of preheaters and area-array packages.[166] Surface-mount work is a distinct skill rather than a harder version of through-hole soldering, requiring a steady hand, tweezers and usually a microscope, but it is achievable at an ordinary workbench once learned.[657]

### Fixturing and part retention

Header footprints with deliberately staggered pins hold the part in the board by friction, so the header does not fall out while being soldered.[43] Modules are attached to a host board through castellations — plated half-holes routed along the board edge — which allows the module to be machine-placed and soldered like any other component.[319]

## Materials

The value of flux is one of the slowest lessons to arrive unaided, and its absence produces joints that fail intermittently rather than obviously — a joint that breaks later or performance that drifts.[137] Solder mask is what makes solder go where it is intended: with flux applied, solder flows and settles onto the exposed pads rather than spreading, which is a substantial part of what the extra fabrication cost buys.[28]

Leaded solder flows more easily than lead-free and produces a better-looking joint; lead-free works but demands more care, and keeping leaded solder available tends to prevent the transition being made at all.[200] Claims that exotic solder alloys improve conductivity misplace the effect, since the solder accounts for roughly 0.1% of the resistance of a complete connection.[183]

## Equipment

The quality of the iron is itself a factor in a beginner's results, since most people start with the cheapest available tool while their technique is being judged.[413] Poor equipment degrades joint quality measurably, and moving to cartridge-tip irons that can be swapped from a stand as the work requires is a substantial step up from low-cost stations.[528]

Adequate light is a prerequisite rather than a refinement: roughly a thousand lux at the bench is the working minimum, and joints that appear sound from one angle frequently prove otherwise when the board is picked up and viewed from another.[200] A microscope with integral illumination and stereo optics reveals defects missed at the bench even with good light and good eyesight, and the property that makes an optical microscope suitable for soldering rather than only inspection is working distance — the iron has to fit between the objective and the board.[200][345]

Micro-soldering is supported by dedicated equipment rather than general-purpose tools, with a fine-tipped iron and a microscope treated as the pair required to begin.[318] As devices shrink, the response available to a repair practitioner is better magnification and finer tips rather than an objection to the trend; in Louis Rossmann's repair practice, reballing a three-hundred-ball part is treated as difficult but legitimate work.[507]

## Reliability and alternatives

Soldering is not the most reliable joining method available: telecommunications practice favours crimping and wire wrapping, and building wiring standards prohibit soldered connections in favour of screwed and clamped ones, on the grounds that a soldered joint is not reliable enough for permanently installed wiring.[183] A connector is likewise more reliable than a hand-soldered joint for anything that will be connected and disconnected repeatedly, which is why test fixtures use pluggable interfaces rather than soldered wiring.[534] Where a wire must be soldered directly, the practice is to solder it once, secure it with adhesive and never disturb it again, keeping any connection that needs to be broken on a mating connector instead.[606]

Manufacturers eliminate connectors to save cents at volume, soldering mains and output wiring directly to the board even where the enclosure retains the openings for the screw terminals that were designed out.[462] Terminating a high-pin-count connector by hand is measured in hours per connector, which is why such work is avoided where a terminated assembly can be bought instead.[496] Prefabricated connector pigtails — a connector on one end and stripped tinned wire on the other — remove the need to crimp, since two of them soldered together under heat-shrink produce an adapter between any two connector families.[121]

## Volume production

Processes that consume a variable liquid or paste — soldering among them — are the hardest to hold consistent in volume manufacturing, and correspondingly the hardest to anticipate problems in.[365] Machine-applied paste is far more consistent than wire solder fed to a tip, so hand and semi-automated soldering operations vary more than reflow does.[279] A hand-soldered board does not match a reflowed one on appearance, though careful work under a microscope with sufficient time can approach it.[176]

Consistency in a manual operation is engineered through fixtures that make the correct action easier to perform than the incorrect one, rather than through instruction alone.[279] The standards body governing assembly publishes land-pattern specifications that fix pad geometry for surface-mount parts, on the basis that pad sizing determines whether a joint solders reliably in volume.[531]

The effective way to get an assembly defect corrected by a contract manufacturer is to document it with evidence rather than describe it: a high-resolution photograph of a tombstoned component typically produces a fix within the hour, where a general complaint does not.[279] Identifying and documenting the problem precisely is the larger share of the work with a remote factory, which is generally both responsive and capable once it knows exactly what is wrong.[279]

## Unconventional substrates

Soldering onto unconventional substrates is limited by temperature: printed conductive traces on paper or fabric, and the substrate itself, must survive several hundred degrees for the seconds a joint takes, which pushes such work toward low-temperature alloys, very fast technique, or welding instead.[172] Printed conductive traces on flexible substrates are also high-impedance compared with copper — on the order of ohms per inch — which restricts them to low-current sensor and battery wiring.[172]

At Cartesian Co, conductive traces printed on microfibre were soldered with small-outline packages and reflowed successfully, with leaded solder performing better than lead-free, and reflow onto paper was also demonstrated.[260] Substrate resolution rather than the soldering sets the limit on what can be attached: a package cannot be placed on ordinary cotton because the printed resolution is inadequate, whereas microfibre supports it.[260] Conductive adhesive dispensed in place of solder paste is an alternative attachment method that removes the temperature constraint entirely.[210]

## Rework and adaptation

Removing a multi-pin connector is easier if the plastic body is destroyed first so that each pin can be desoldered individually, which preserves the board.[493] Soldering to a component whose lead has been cut flush with its body remains possible by clearing material around the pin with a rotary tool and attaching a wire to what remains.[68]

Parts supplied only in leadless packages must be adapted to a breadboard-compatible carrier before they can be used in exploratory work, and leaded packages can be improvised from a surface-mount board by soldering stamped metal legs to its edge, producing the footprint of a through-hole part.[330][546]

## Soldering in debugging

Soldering faults are a favoured explanation during debugging and frequently the wrong one: a board that produced no response was assumed for days to have a soldering problem, and the part was replaced twice, before the actual cause proved to be a reset line held active.[203] Experience can work against the diagnosis, because an experienced engineer generates many plausible hypotheses and pursues them, where an inexperienced one might simply check every pin and find the fault immediately.[203] The reverse error is equally common: a week of elaborate protocol workarounds was built to cope with noise on an I²C bus that turned out to be caused by the soldering, and the workarounds proved entirely unnecessary once the joint was fixed.[622] Wires soldered on to reach a debug header or serial pins become their own source of doubt, since a broken lead leaves the engineer unsure whether the code or the wiring is being debugged.[537]

## Skill and training

Teaching is more effective when limited to safety and a single minute of demonstration before the learner starts, with technique refined over subsequent projects rather than delivered as a half-hour lesson up front.[413] Formal soldering training exists and is oriented to military and long-life assembly, so only a fraction of it transfers to hobbyist work; a week-long specialist course yielded roughly one useful day when filtered for that audience.[183]

Skill should be built on work where failure costs nothing rather than on a board that must function: running a bodge wire out from under an area-array package is a high-risk operation to attempt for the first time under deadline.[473] The skill degrades without regular use and improves sharply with daily repetition, which is why technicians who solder every day are markedly better at it than engineers who solder occasionally.[342] Deliberate practice on a board designed for repetition, aiming at the same joint made well over and over, is more effective than attempting real work and being disappointed by the result.[436] One published practice board, designed by Zach Fredin, arranges the same simple circuit five times in descending package sizes, from through-hole down through progressively smaller outlines and passives, so a single design exercises the full range of hand-assembly difficulty.[330] Scrap mobile telephone logic boards bought cheaply serve the cellular-repair trade as micro-soldering practice material, since they carry dense runs of the smallest passive sizes.[414]

Advanced hand-assembly techniques are learnable by persistence rather than talent: Scotty Allen had never worked with flexible boards, area-array packages or much surface mount before doing so on camera for Strange Parts, and found it demanding but achievable with the right tools and refined technique.[414] Soldering under a camera while narrating is substantially harder than soldering alone, so recorded technique is a poor guide to a practitioner's actual ability.[306]

Transferring a working breadboard circuit onto soldered perforated board is a productive exercise precisely because mistakes are likely and are cheap to correct with solder and wire, which is where the troubleshooting is learned.[276] Perforated-board construction remains viable for demanding circuits including radio-frequency work, where the requirements are avoiding excess coupling and checking carefully that nothing is bridged; careful visual checking under magnification that every joint is isolated from its neighbours is the discipline that makes hand-built board construction reliable.[284] Attaching a fine-pitch part to a board whose footprints differ from the reference design turns a routine operation into a problem of locating the correct pads, which is where the instructive difficulty lies.[276]

A recurring failure mode among people new to modular boards is not soldering at all: stacking a shield onto headers without soldering them produces a board that appears connected and does nothing.[331] Kit vendors receive returns for exactly that error, which indicates it is a gap in the mental model rather than carelessness on the part of individuals.[331] A kit built with poor joints and then returned as defective is a recognised pattern, and one where the assembly rather than the design is the cause is usually evident from photographs of the board.[176]

## Workspace and safety

Soldering produces fumes and requires extraction, which rules it out of ordinary commercial office space along with reflow ovens and chemical etching.[195] A workshop space intended for hands-on assembly has to be provisioned deliberately with ventilation, good table lighting and long enough working sessions, rather than being an ordinary room with tables.[257]

## Repair constraints

Repair work at the fine end is constrained less by soldering skill than by parts availability, since a replacement controller that differs only in how it communicates may be unobtainable at any price because the manufacturer will not sell it.[507]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 28 | Bowie and The Brown Note | https://theamphour.com/the-amp-hour-28-bowie-and-the-brown-noise/ | February 1, 2011 |
| 43 | An Interview with Jeff Keyzer and Jeremy Blum - Audacious Arduino Arguments | https://theamphour.com/the-amp-hour-43-audacious-arduino-arguments/ | |
| 68 | Radiation Chips & Old Package Types - Technocratic Toilet Troubleshooting | https://theamphour.com/the-amp-hour-68-technocratic-toilet-troubleshooting/ | |
| 121 | An Interview with Zach Hoeken Smith - Creative China Commorant | https://theamphour.com/the-amp-hour-121-creative-china-commorant/ | November 11, 2012 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 166 | Prior Art, Wafer Fabs and Guns - Whimsical Wafer Waffling | https://theamphour.com/166-prior-art-wafer-fabs-and-guns-whimsical-wafer-waffling/ | October 7, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ | April 21, 2014 |
| 200 | SolidCon and Traveling Tech - Joined Junk Jocularity | https://theamphour.com/200-solidcon-and-traveling-tech-joined-junk-jocularity/ | May 26, 2014 |
| 203 | Tesla, Checklists and Bullies - Emerging External Eupsychics | https://theamphour.com/203-tesla-checklists-and-bullies-emerging-external-eupsychics/ | June 16, 2014 |
| 210 | Risky Components and Hardware Innovation - Slipshod Shack Shutdown | https://theamphour.com/210-risky-components-and-hardware-innovation-slipshod-shack-shutdown/ | August 5, 2014 |
| 257 | An Interview with Fabienne Serrière of KnitYak | https://theamphour.com/257-an-interview-with-fabienne-serriere-of-knityak/ | July 8, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 276 | Eating An Elephant | https://theamphour.com/276-eating-an-elephant/ | December 2, 2015 |
| 279 | Merry Keyzermas! | https://theamphour.com/279-merry-keyzermas/ | December 22, 2015 |
| 284 | An Interview with Great Scott | https://theamphour.com/284-an-interview-with-great-scott/ | January 27, 2016 |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ | July 6, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 331 | An Interview with Simone Giertz | https://theamphour.com/331-an-interview-with-simone-giertz/ | January 11, 2017 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 345 | Milling About | https://theamphour.com/show-345-milling-about/ | May 30, 2017 |
| 365 | Wait, why is Jeff glowing? | https://theamphour.com/365-wait-why-is-jeff-glowing/ | October 30, 2017 |
| 413 | A House of FR4 | https://theamphour.com/413-a-house-of-fr4/ | October 28, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 493 | PITA Package | https://theamphour.com/493-pita-package/ | May 17, 2020 |
| 496 | Drab Olive | https://theamphour.com/496-drab-olive/ | June 14, 2020 |
| 507 | Right To Repair with Louis Rossmann | https://theamphour.com/the-amp-hour-507-right-to-repair-with-louis-rossmann/ | |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ | January 31, 2021 |
| 531 | Footprints and Symbols with Natasha Baker | https://theamphour.com/531-footprints-and-symbols-with-natasha-baker/ | February 21, 2021 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ | April 5, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23, 2022 |
| 622 | Building Firmware and Hardware for Trade Shows with Mike Szczys | https://theamphour.com/622-building-firmware-and-hardware-for-trade-shows-with-mike-szczys/ | March 5, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
