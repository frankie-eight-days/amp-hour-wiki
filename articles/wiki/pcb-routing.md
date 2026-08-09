---
title: PCB Routing
concept: pcb-routing
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

PCB routing is the stage of printed circuit board design in which the copper connections between components are laid out across the board's layers. The difficulty of routing is dominated by component placement rather than by trace-drawing skill: "the old adage is that designing a PCB is 90% placement", with connections nearly falling out on their own once parts are correctly arranged and no amount of routing skill rescuing a bad arrangement.[16] The term also denotes a fabrication step, the milling of the board outline and breakaway features, which carries its own set of design constraints.[158][286]

## Placement

Routing is treated as a downstream consequence of placement, and placement is performed incrementally rather than all at once. A designer takes one functional group at a time — an amplifier consisting of an op amp and its surrounding passives being a typical block — places and routes that block on its own, then moves finished blocks together as units.[16] Placement begins from what cannot move: front panel controls, batteries and physical connectors are fixed first, turning the remaining work into a problem with known boundaries rather than an open one.[128] Setup belongs to the same phase: design rules, clearances and the board outline are established before any trace is drawn, so that routing proceeds as constrained work, with the constraints themselves making it go quickly.[482]

A placement is judged by how few rat's-nest lines cross, with parts rotated to test the arrangement — turning a large package ninety degrees is often enough to unpick a tangle — and components grouped into functional modules while doing so.[682] The few nets that must cross the whole board are left until last and then routed without concern for elegance; twenty vias carrying one such signal end to end is an acceptable answer where the trace has no performance requirement.[682] Ripping up half a routed board because moving one part improves everything downstream is normal practice rather than lost work, although the need to do so is also evidence that placement was not finished before routing began.[682]

## Trace discipline and geometry

The classical routing discipline assigns one direction per side — all traces one way on top, the orthogonal way on the bottom — because it guarantees that any two nets can cross by changing layer; diagonal runs across the board destroy that property along with the routing room.[636] A trace running the full width of a board is primarily a blockage rather than an interference problem, since it cuts the available routing channel in two and forces everything crossing it onto another layer.[410] Directional discipline still runs out of room on a sufficiently dense board: a four-layer board chosen to keep cost down, carrying a radio, a cellular module and a high-density mezzanine connector, was squeezed to the fabricator's stated 3.5 thou limit and still would not close.[504]

Package selection functions as a routing decision as much as a thermal one. A small-outline package lets traces pass underneath it, while a power package's thermal pad claims that board area outright, so taking the smaller package where the power handling is not needed buys back routing space.[580] A late component addition does not always require re-routing: placing a small part directly over existing wide traces on the opposite side can absorb the change without disturbing a layout that already works.[561]

Routing convenience can conflict with other constraints. Rotating a radio module so that slow signals route more easily is a common and expensive mistake because it puts the antenna in the middle of the board; the antenna belongs on an edge, preferably the short one, with a keep-out carrying no metal beneath it on any layer.[678] Board technology bounds signal performance independently of layout skill: ordinary FR4 with disciplined routing carries a few hundred megahertz of front-end bandwidth comfortably, while multiple gigahertz requires controlled-impedance materials and exotic construction.[654] On two-layer boards it was historically accepted that some connections simply could not be routed and were finished with wire after assembly, a practice that disappeared once cheap multilayer fabrication became available rather than because designers improved.[489]

## High-density packages and pin assignment

Fine-pitch ball grid arrays set the scale of professional routing effort. A thousand-pin BGA with all pins in use means roughly a thousand traces and a thousand vias placed individually, multiplied by however many times the work is ripped up and redone, which is why a large professional board is measured in weeks rather than days.[316] Sheer connection volume imposes its own floor: fifty pages of dense schematic implies connecting every pin on every part, and that volume alone puts a serious layout beyond a couple of weeks regardless of tool quality.[316]

Automated fan-out handles the first stage of a large BGA: with design rules and signal-layer count set, the tool escapes every ball to just outside the package, giving a reasonable start on work that is otherwise pure tedium.[393] With a programmable device the pin assignment can be decided last: the package is fanned out, surrounding circuitry is routed inward to whichever pin is convenient without connecting anything, and a pin-swap tool then matches each incoming trace to the nearest escaped pin and joins them, recording the swaps as reversible so the whole assignment can be undone.[393] Pin swapping is never fully automatic, because real devices carry dozens of placement requirements — signals that must stay within a particular quadrant to reach that quadrant's local clock among them — and those constraints must be imposed before the tool is allowed to optimise.[393] Swapping pins can also quietly break a capability requirement: on some devices a high-speed input is supported only on certain banks while the corresponding output is supported only on others, and a library that described what each pin can do would let the tool check this, which most libraries do not.[375]

Escape feasibility is tied to manufacturing technology. A 0.4 mm pitch BGA of three rows can be escaped with conventional board technology and manufactured cheaply; beyond three rows the escape requires laser-drilled vias, the point at which the part choice commits the whole board to a more expensive process.[59] A module's pad layout is an optimisation between leaving enough space between pads to escape every trace and keeping pads large enough to solder reliably, which is why vendors publish example escape patterns that stay inside ordinary board capability.[226] On one XESS board, Dave Vandenbout routed a 256-ball BGA facing SDRAM on the opposite side on four layers with two given over to power and ground, a result dependent entirely on finding the right pin assignment first.[181]

More aggressive construction relaxes escape constraints at a price. An any-layer build places a laser via between every pair of layers, so a via can drop from any layer to any other and routing becomes almost unconstrained; the cost is a lamination, plating and drilling cycle per layer, and at 120 boards fitting on a single A4 panel, a ten-layer any-layer board still came to about ten dollars each in Lukas Henkel's compact high-speed work.[681] Where silicon is designed in-house, the pinout itself can be laid out to suit the board: on the Raspberry Pi RP1 programme a multi-lane differential bus between two chips runs as a straight bank of pairs with no crossings, because a single crossing would force the whole board onto more expensive technology.[648]

## Automation

Full auto-routing has a poor record in practice. Robert Feranec's account of using one is representative: a week spent setting up the rules, followed by a run that reported the board could not be routed at all, with the setup cost being the part omitted from demonstrations.[316] The useful form of automation constrains rather than decides: telling the tool which corridor the tracks should run through and letting it place them there reduces clicks on work the engineer has already planned, instead of asking the machine to plan it.[316] Interactive auto-routing — starting a trace and letting the tool complete it — is genuinely useful for the last one or two connections on a board and a poor idea at the beginning, where accepting the tool's choices forecloses arrangements the designer has not yet found.[682]

The comparison of routing to board games does not hold: those games have a fixed rule set however large the search space, whereas moving one component two millimetres changes the rules themselves, a different class of problem from searching a fixed space well.[367] Any claim about automated routing has to include placement to be meaningful, because placement is where the difficulty lives and a router handed a poor arrangement is being asked to solve the wrong problem.[367]

## Application-specific practice

Some design domains restructure the routing problem itself. Driving irregularly shaped LED arrays from multi-channel driver chips makes the board routing dominate the project, and for a one-off installation that work is almost entirely wasted; Mike Harrison's practice for such installations is to put a tiny microcontroller behind every one or three LEDs, collapsing the problem to power, ground and a single data line run in parallel to every device, so a four-layer board becomes a copy-and-paste job with unit cost rising by well under a pound per device and design time falling by more than that is worth.[135] Harrison also notes that no CAD system expresses the constraint that actually applies to a microcontroller — that a net may go to any of several particular permutations of pins — so experienced designers keep libraries of bare footprints, rat's-nest them by hand and route directly, sometimes without a schematic existing at all.[135]

Progress per minute is the signal to watch while routing: ten hours into a four-layer board, Kerry Scharfglass found the rate collapsing and the remaining connections turning out to be impossible, and recognising that at ten hours is far better than discovering it at what feels like ninety percent complete.[487] Layout is also regarded as the part of board design that resists instruction: schematics and libraries can be given away, but deciding where the vias go and which traces run where transfers only by doing it, so teaching layout means withholding the finished layout.[573]

## Outline routing in fabrication

The fabrication sense of routing — milling board outlines and panel separations — carries its own constraints. Breakout tabs snapped with pliers leave fibreglass shards and ragged edges unless designed carefully: tabs in the corners can be trimmed square with side cutters, while tabs part-way along an edge need a half-moon relief in the outline and leave a visible scallop behind.[158] Where appearance matters, the two separation methods are mixed: edges that will be seen are routed for a clean profile and the others V-scored, with the scored edges accepted where they face away from the user.[188] Unless a board is scored, the outline must be routed anyway, which means a curved or unusual outline costs nothing extra since the machine follows a path either way.[286]

Which line the router follows — inside the outline, outside it, or on it — differs by fabricator, so the intent must be stated explicitly in the fabrication notes rather than assuming a previous vendor's convention carries over.[162] Not every CAD package emits a usable outline path, and deprecated output formats create real friction with board vendors, which is why low-cost services restrict which files they accept rather than attempting to interpret everything.[299] Board house quality is not stable over time: a vendor that was consistently excellent began returning panels with boards rotated within the panel and outlines cut wrong, and keeping at least three qualified vendors with orders spread across them is insurance against a supplier quietly slipping.[299] Embedding a component inside the board requires a very fine routing bit and controlled-depth routing, taking the job off any shared panel service; bonding several thin boards together is the alternative route to the same result, and both belong to fit-to-envelope products where the enclosure dictates the board.[617]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 16 | LED Designs, Last Minute Designs and Board Designs | https://theamphour.com/the-amp-hour-16-led-designs-last-minute-designs-and-board-designs/ | |
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ | |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 158 | Hyperloop, Upverter and Soldering - Unbelievable USB Ustulater | https://theamphour.com/the-amp-hour-158-unbelievable-usb-ustulater/ | August 12, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 181 | An Interview with Dave Vandenbout - Xceptional XESS Xenagogue | https://theamphour.com/181-an-interview-with-dave-vandenbout-xceptional-xess-xenagogue/ | |
| 188 | Capacitors, Simulation and Closures - Deonerated Design Dealmaking | https://theamphour.com/188-capacitors-simulation-and-closures-deonerated-design-dealmaking/ | March 10, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 375 | An Interview with Tim "Mithro" Ansell | https://theamphour.com/375-an-interview-with-tim-mithro-ansell/ | January 14, 2018 |
| 393 | I've bitten myself | https://theamphour.com/393-ive-bitten-myself/ | May 20, 2018 |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ | October 7, 2018 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 489 | An Interview with Jack Ganssle (2nd) | https://theamphour.com/489-an-interview-with-jack-ganssle-2nd/ | April 19, 2020 |
| 504 | This Is Just A Tribute | https://theamphour.com/504-this-is-just-a-tribute/ | August 9, 2020 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6, 2022 |
| 617 | Conference Room Innovation | https://theamphour.com/617-conference-room-innovation/ | January 29, 2023 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 678 | All About Antennas with Katerina Galitskaya | https://theamphour.com/678-all-about-antennas-with-katerina-galitskaya/ | September 30, 2024 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
