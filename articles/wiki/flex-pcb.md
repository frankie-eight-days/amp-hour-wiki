---
title: Flex PCB
concept: flex-pcb
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A **flex PCB** is a printed circuit board built as copper laminated onto a plastic film rather than onto rigid fiberglass, and ordering one from a board house is the default route to a conforming circuit unless same-hour turnaround is needed.[415] Unlike a flat flexible cable, which is a polyimide interconnect of fixed form, a flexible printed circuit is a genuine custom board that can take any outline and may terminate in a tail resembling an FFC.[708] Flex is used in compact consumer products because routing a circuit around internal corners is often the only way to fit the electronics into the required form factor, and mounting components directly onto flexible substrates is not a recent technique: populated flex boards appear in consumer products of the 1970s and 1980s such as Polaroid cameras.[28] Much of the flex circuitry in production equipment is not a standalone flex board at all but rigid-flex, in which flexible layers sandwiched into the inner layers of the stackup join two rigid boards that then fold onto each other.[415]

## Terminology

Flat flexible cable, flexible printed circuit and conductive ink circuit are distinct technologies, and none of them is a ribbon cable, a term that specifically denotes the multi-conductor cable terminated with insulation-displacement connectors.[708] A conductive ink circuit resembles a flexible printed circuit but is drawn with conductive ink rather than etched copper; microwave oven keypads use one, ending in a flexible tail that plugs into an FFC connector.[708]

## Construction

Layers of polyimide in a flex circuit are joined with a bond film rather than a liquid adhesive: a thin sheet of adhesive handled like tissue paper that melts and bonds the stack when heated and collapsed in a press.[153] The bond film can be bought either pre-applied to polyimide or as a standalone sheet, which allows a designer to build arbitrary multi-layer sandwiches of dissimilar materials such as carbon fibre and polyimide.[153] The same construction principle extends beyond electrical circuits: laminating stiff carbon-fibre layers around a polyimide core and then laser-cutting the carbon away in selected regions produces a mechanical flex hinge.[153]

Flexible printed circuit fabrication requires machined steel tools to stamp the coverlay, so each design carries hard tooling that the factory shelves and reuses much like an injection-mould tool.[414] For very small flex boards that tooling charge dominates the quote, so ordering ten and ordering a hundred cost effectively the same, with the price stepping up only at the next panel bracket.[468]

Feature sizes in laser-machined flex and polyimide work are conventionally expressed in microns: 25 microns is one thousandth of an inch, and a human hair is roughly three thousandths of an inch, or 75 microns. Production features of that era ran in the 100 to 200 micron range, against machine accuracy of two to five microns.[153]

Layer counts vary widely with the application. A lightning-to-audio connector assembly may use four to six layers, while a tablet processor flex can reach twelve layers and still bend; a two-layer flex behaves like a sheet of paper.[415]

## Rigid-flex

Early flex construction was cruder, with the flexible material applied simply as a bottom layer, whereas modern rigid-flex embeds the flexible layers within the board stackup.[468] Construction can go well beyond the familiar two-layer flex board, placing multilayer rigid sections on top of the flexible core.[718]

The advantage of rigid-flex is that it removes the cost and the reliability exposure of the connector-plus-ribbon-cable pair it replaces, since the interconnect becomes part of the board stackup rather than a mated assembly.[415] A related construction places several small rigid board islands along a single flexible circuit that runs continuously between them, so the flex itself acts as the interconnect.[28]

## Design and ordering

Designing and ordering a plain single-piece flex board differs from a rigid board mainly in the stackup specified to the fabricator, for example a 0.1 mm flex board in place of 1.6 mm fiberglass.[468] Complexity rises sharply only when flexible layers are combined into a rigid stackup; a standalone flex board is close to an ordinary board order.[468]

Where a flex tail must fold to position a display in a head-mounted assembly, the fold path is worked out during board layout, and the layout is kept deliberately open-ended so that mechanical revisions do not force a board re-spin.[638] Budgeting only a single board spin on a first flex design is a recognised risk, because flex introduces mechanical and folding variables that a first prototype rarely resolves.[575]

Cost has moved over time. Flexible boards carried a substantial premium over rigid boards in the early 2010s, enough that a flex build was treated as an expensive choice rather than a default one,[28] and they remained a premium over rigid FR4 into the late 2010s, which is what left room for lower-cost conformal circuit processes at the low end.[415] Flexible PCB pricing then fell substantially across the 2010s, moving flex from an unaffordable option for hobby and student projects to a routinely orderable one.[663]

The justification for choosing flex over rigid FR4 is often the elimination of discrete wires, since hand-soldering wires does not scale once hundreds of units are produced.[663]

## Assembly

Populating components directly onto flex is harder than populating a rigid board, since pick-and-place and reflow assume a stiff, flat panel and flex generally needs a stiffener or carrier beneath it.[415] Assembly on polyimide in particular demands a vacuum bed or similar fixturing because the material curls and takes on tension.[412] A very thin board made from bare prepreg avoids that problem: it can simply be taped to a sheet of standard FR4 with polyimide tape and then run through normal pick-and-place and reflow, because prepreg wants to stay flat instead of curling.[412] Sourcing such boards is the difficulty, since board houses stock prepreg for building up multilayer boards but few will supply it as a finished single-layer board.[412]

A flex board designed to be folded into a three-dimensional assembly pushes cost into labour: operators must be trained to fold the panel in a fixed sequence and tack it with solder so it holds its folded shape.[537] Final test of a flex assembly should therefore confirm that the board has not been folded or bent in the wrong manner, since an incorrect fold is a defect the electrical test alone will not catch.[663]

Flex has one inspection advantage over rigid board. A BGA placed on a flex circuit with no stiffener under it can be inspected optically without X-ray, because the polyimide substrate is translucent and the ball array is visible through the back of the board.[414] The 0.4 mm pitch CPU BGAs used in phones nonetheless sit at the difficult end of rework, where experienced technicians reach a working result within a couple of attempts rather than first time every time.[414]

## Rework

Cutting a trace to patch a flex board is far harder than on rigid FR4, because the substrate is very thin and traces on the opposite layer sit directly beneath the cut.[575] Flex can also serve as the repair medium rather than its subject: when an expensive board built on controlled-impedance material cannot be re-spun, a flex overlay can carry a rework connection between distant points on the board in place of loose mod wires.[496]

## Applications

Hearing-aid electronics are typically built as three stacked dies covering DSP, analogue and memory, all bonded down to a small flex print that also carries the microphones.[338] Building a sensing electrode array on a single flex circuit fixes the spacing between electrodes, and that known geometry is what allows an accurate tomographic image reconstruction.[448] Flex PCB has also been used as the substrate for a polymer banknote-style token, printed in full colour with an RFID chip embedded in the flexible material.[464]

Planar motors can be built by etching the drive coil into a flex PCB and energising it with a driver; a haptic motor driver intended for phone vibration motors can substitute for a discrete H-bridge in this role.[493] A folding flex actuator can be built from a single flexible PCB with three aluminium stiffeners that both fold the board into shape and form a pocket for the magnet the etched coil acts against.[663]

Antennas are a poor fit for flexible substrates. At 2.4 GHz and above a positional shift of one millimetre materially changes antenna behaviour, so an antenna carried on a flexible substrate that can move is less stable than one fixed to a rigid structure.[435] A degraded antenna can lose around half the radiated RF power, which shows up either as lost range or as shortened battery life once transmit power is raised to compensate.[435]

## Related conformal processes

Circuitry patterned directly onto an injection-moulded housing costs more per unit than flex, so it suits small high-margin products such as hearing aids and payment terminals where internal volume is the binding constraint.[435]

Conductive traces printed onto fabric or paper have far higher resistance than etched copper, on the order of a couple of ohms per inch, which restricts them to low-current sensor and battery-scale signals rather than power distribution.[172] Additive printing of circuits is also a rastered, line-by-line deposition process whose time scales with the total area covered, which keeps it in the prototype and one-off niche rather than batch production.[172]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 28 | Bowie and The Brown Note | https://theamphour.com/the-amp-hour-28-bowie-and-the-brown-noise/ | February 1, 2011 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 448 | An Interview with Jean Rintoul | https://theamphour.com/448-an-interview-with-jean-rintoul/ | June 23, 2019 |
| 464 | KonnectorPanik | https://theamphour.com/464-konnectorpanik/ | October 27, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 493 | PITA Package | https://theamphour.com/493-pita-package/ | May 17, 2020 |
| 496 | Drab Olive | https://theamphour.com/496-drab-olive/ | June 14, 2020 |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ | April 5, 2021 |
| 575 | New Life Skills with Joe Grand | https://theamphour.com/575-new-life-skills-with-joe-grand/ | January 30, 2022 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 663 | Motors on PCBs with Carl Bugeja | https://theamphour.com/663-motors-on-pcbs-with-carl-bugeja/ | March 25, 2024 |
| 708 | All the Connectors with Davide Andrea | https://theamphour.com/708-all-the-connectors-with-davide-andrea/ | November 1, 2025 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
