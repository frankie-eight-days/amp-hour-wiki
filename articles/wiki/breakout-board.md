---
title: Breakout Board
concept: breakout-board
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A **breakout board** is a small printed circuit board that converts the pins of an electronic component or module—typically a fine-pitch surface-mount package—into a more accessible form, most commonly 0.1 inch header pins usable on a breadboard or with plug-in prototyping hardware.[68][454] The boards serve two broad purposes: they make packages that cannot be hand-assembled or breadboarded usable in prototypes, and they act as carriers that centralise a component's support circuitry so the rest of a design can be kept simple.[251][676] Breakout boards occupy a distinct niche in electronics practice, sitting between bare silicon and full custom PCBs, and their use shapes decisions about package selection, prototyping method, and product architecture.[110][522]

## Function and purpose

The basic function of a breakout board is pitch and format conversion: a fine-pitch connector or surface-mount footprint is routed out to larger, hand-solderable connections, typically 0.1 inch headers.[68][340] Building a breakout for every component in a working parts library, each breaking out to 0.1 inch pins, makes even sub-millimetre-pitch ball grid arrays usable on a breadboard and prevents package choice from silently ruling parts out of a design.[454] The conversion a breakout board performs is the same conversion performed inside a modern DIP package, where a tiny die is bonded out to a large lead frame; the breakout simply moves that adaptation outside the package.[454]

Beyond format conversion, a useful class of evaluation board is a breakout that also carries a communication link such as SPI or a serial interface, so a new chip can be dropped onto an otherwise fixed layout, fabricated, and exercised over that link without building the rest of a system around it.[110] A minimal breakout that routes the pins of a chip out to headers can likewise be driven from an off-the-shelf microcontroller board to prove out an application before committing to a custom PCB.[340]

## Construction techniques

Several construction methods are specific to breakout and adapter boards. Commercial SOIC-to-header breakout boards can be glued component-side-up onto an unetched copper-clad sheet and wired freestanding to the surrounding parts, giving a solid ground plane under everything; this is a long-standing construction technique that behaves well at high frequency.[56]

When several breakout modules must sit together in a fixed arrangement, soldering 90-degree headers instead of straight ones gives each module a flat face that effectively surface-mounts to a piece of bare FR4; the interconnect is then point-to-point wire with discrete parts added in line, and the result is compact, durable, and buildable the same day.[330] A related method replaces point-to-point wiring with a very simple custom carrier PCB: off-the-shelf sensor breakout boards keep their 0.1 inch headers and solder directly into the carrier, so no individual sensors have to be sourced or placed, and a five-board run from a low-cost fabricator is the entire production quantity needed for demonstrations.[604]

A carrier board can also expose a daughterboard's test points as well as its headers by giving the carrier a footprint for small pogo pins that are hand-soldered in place; when the daughterboard is soldered on top, the pogo pins bear against its test pads and bring the programming and debug nets out to the carrier.[395]

## Standard interfaces and footprints

Standardised header definitions allow breakout and carrier boards to interoperate. One such standard is a keyed 20-pin header arranged two-by-ten on 0.1 inch centres, occupying one inch by 0.2 inch, carrying two supply rails plus analog inputs, SPI, I2C and serial; this covers roughly ninety percent of typical small designs, and keying the connector prevents reversed insertion.[335] A reusable header definition of this kind should be chosen to span the common interface set rather than one project's needs, so that a single connector serves across most boards a designer produces.[335]

Matching the physical size and the power and ground pinout of an established development board lets a new board drop into the ecosystem of carrier boards already built for the original; signal pins cannot always be matched, so compatibility is partial and must be stated as such.[395] Pre-certified radio modules such as u-blox parts reduce the electrical work on a carrier to breaking out the module's pins, since the difficult circuit design is already inside the module.[362]

## Modular design

Breakout boards are one extreme of a broader modular design approach. Putting the processor on a pluggable module and designing only the carrier board around it isolates the design from obsolescence of that specific module: if the microcontroller board goes end-of-life, or the requirement changes to a wireless variant, the sensor carrier does not have to be redesigned.[339] Centralising the hard parts of a design into one reusable module—with cellular or Wi-Fi and the surrounding support circuitry on a six-layer board—leaves only a two-layer breakout carrying a battery and one sensor, so swapping an accelerometer for a pressure sensor becomes a trivial board change, and assembly is simplified because the complex board is a single placed part.[676] Because the interface between module and carrier is fixed and narrow, the simple carrier board can be handed to a separate design team or an outside specialist and plugged in.[676]

Modularity has an optimal granularity. Taking it to the limit with a breakout board per chip does make everything swappable, but the added interconnects and extra PCBs carry real cost, so the design question is where to draw the boundaries rather than how modular to be.[522] As more functionality is absorbed into modules, board-level work shifts from designing circuits to producing breakouts that connect modules together, a Lego-block style of assembly that matches what most customers want, since they are trying to finish a product rather than design circuitry.[362] A fully modular product built from simple functional boards is, in effect, an evaluation-board or demo-board style of product, useful for proving that a module plus a battery plus a sensor works rather than an end-product architecture in itself.[676]

Modularity also interacts with weight. On a weight-critical board the ideal interconnect is bare solder pads, but 0.05 inch pitch connectors are difficult enough for a general audience that dedicated adapter boards may be added for specific targets so users can simply plug in; the trade-off can be made explicit by perforating the adapter tabs so a builder who cares about grams can snap them off.[356]

## Trade-offs and failure modes

Adapting down to 0.1 inch is not free. Chaining a fine-pitch connector into an adapter board that converts it to 0.1 inch adds two extra interfaces and two extra failure points, so when board area is not scarce, placing the 0.1 inch header directly on the design is simpler than adapting down to it later.[68] Adapter boards for fine-pitch parts around 0.5 mm pitch are only useful as a shortcut if they are already on the shelf; ordering one specially takes about as long as ordering a purpose-built board that does the whole job.[110]

Exposed pins on a carrier or breakout board are a reliability concern: connecting external signals directly to a microcontroller pin without protection is a routine way to destroy the part, so the central design question for such a board is which protection measures to add around the exposed pins.[339] On the firmware side, adapting a modern interface chip can be trivial in hardware yet substantial in software: bringing up a USB-C physical-layer chip on a minimal breakout meant porting a library from an existing open embedded codebase, running to roughly four thousand lines of code on a small microcontroller.[340]

Add-on boards can also fail for system-level reasons. An Ethernet add-on board for a small hardware platform was discontinued after only around fifty units because wired networking drew far too much power for that class of product.[458]

## Fabrication constraints

Breakout boards remain necessary because in-house fabrication methods have a floor on feature size. In-house etching and milling processes with roughly a 10 mil feature limit are adequate for many boards but cannot resolve current fine-pitch footprints, so a purchased adapter board becomes a prerequisite for using new parts on home-made PCBs.[275] Desktop fabrication methods likewise cannot handle ball grid arrays, so as packages continue to shrink an adapter board remains necessary to use modern parts with them; for anything beyond a single one-off, even a run of ten, a professionally fabricated FR4 board is the sensible endpoint.[251]

Assembly behaviour differs by package class. Wafer-level chip-scale packages are small and light enough that solder surface tension dominates during reflow and they self-align much like a passive resistor, whereas ball grid arrays are large enough that surface tension helps considerably less.[501]

Keeping an in-house etching setup permanently loaded and ready—so that starting it heating is a single button press at the beginning of a layout—changes it from an occasional chore into a same-day process, and the workload it actually absorbs is dominated by simple adapter boards, against an alternative wait of two to four days for outside fabrication.[412]

## Prototyping and education

A prototype assembled from off-the-shelf breakout boards and plug-in prototyping boards is easy to change, which is the entire point of a prototype, and the wait for a fabricated PCB can instead be spent writing firmware.[412] A deliberately trivial first board, such as a simple breakout, is a suitable vehicle for learning a PCB tool, because the point is to build fluency with the software rather than to solve a design problem at the same time.[404] A first spin that does nothing but break out the pins of a part, with a couple of devices hung off the I2C bus, is worth building purely to confirm that a footprint is correct before that footprint propagates into a real design.[658] The same logic applies to larger skills: building a series of small boards that do nothing beyond booting and presenting a console is legitimate practice—ten such boards over six months, running only basic shell commands and a benchmark with no networking, served as the deliberate route to learning embedded Linux hardware before trusting the skill on a real product.[515]

Early module carrier designs accumulate mistakes that only become visible with more experience of the module itself, which is why makers of such boards go back and reissue revisions of boards that were already selling.[155]

## Economics and licensing

Small-package adapter boards carry a large price premium relative to the bare silicon they host: a panel of SOT-23 or SC-70 breakouts has been quoted at around sixty dollars, far more than the parts being adapted.[35] Pricing on through-hole parts interacts with this premium: charging more for a DIP version of a part drives the low-volume user toward buying the cheap surface-mount version plus an adapter board instead, because the combination still comes out cheaper than the DIP.[111] At the other end of the market, a Bluetooth breakout board around a Nordic part—with battery charging, USB and an LED, thirteen pins down each side on 0.1 inch centres—has sold for three dollars delivered from China, below what the equivalent board can be built and shipped for elsewhere; at those prices the margin on the finished board is essentially nothing once postage is accounted for.[700]

One structural proposal for fine-pitch samples is for semiconductor vendors to ship free samples already mounted on adapter boards, though sample budgets are exactly where vendors are trying to spend less.[275] For a silicon shuttle program aimed at people without fine-pitch assembly capability, one option under consideration is returning fabricated ICs pre-mounted on breakout boards that expand the die out to a castellated-edge module or even a DIP footprint.[501]

Web-based carrier-board configurators such as Gumstix Geppetto let a user pick one controller, a limited set of components and modules, and a limited set of connectors, and generate the breakout board for a compute module; the constraint is the narrow parts catalogue, and the alternative of learning a full EDA tool costs well over a thousand dollars of a designer's time.[516]

Because development boards and breakout boards are built specifically so another engineer can learn from them or build on them, Dangerous Prototypes licenses its designs under the most permissive terms available, having moved from Creative Commons attribution-share-alike to effectively public domain while retaining only the trademark on the name, in order to remove licensing friction for users.[125]

## Notable examples

Several breakout and carrier boards illustrate the range of the form. Breakout boards designed to satisfy one personal project—a carrier for a Bluetooth class-2 module for a wearable—grew into a saleable product line covering the other modules in that family, and the boards themselves were electrically very simple.[155] Michael Ossmann built what amounts to an enlarged breakout board around the LPC4300 microcontroller family, adding an expansion interface and a fast USB interface so the part can be used without the user having to solve its board-level problems first.[265] The 1Bitsy is a simple breakout for a higher-end STM32 F4 part, developed alongside the Black Magic Probe, an open-hardware debugger for ARM parts.[326] Jason Cerundolo used a minimal breakout routing the pins of a USB-C physical-layer chip out to 0.1 inch headers, jumped over to an Arduino-class board, for the USB-C Easy Bake Oven project.[340] When no module existed for a particular radio part, Orkhan Amiraslanov built a castellated-edge module for it together with a matching Feather-format breakout board so the module could drop into other people's designs, publishing the design files and selling low-volume production units; an official vendor module for the same part appeared only about two years later, and the offshore low-volume production run returned roughly ninety percent total yield, considered acceptable for an uncertified self-built module.[557]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 35 | An Interview with Jeri Ellsworth - The Ternary Tussle | https://theamphour.com/the-amp-hour-35-the-ternary-tussle/ |  |
| 56 | Open Orbific Oratiuncle | https://theamphour.com/the-amp-hour-56-open-orbific-oratiuncle/ |  |
| 68 | Radiation Chips & Old Package Types - Technocratic Toilet Troubleshooting | https://theamphour.com/the-amp-hour-68-technocratic-toilet-troubleshooting/ |  |
| 110 | Armstrong, Camenzind & Museums - Outstanding Oneirophoros Obituaries | https://theamphour.com/the-amp-hour-110-outstanding-oneirophoros-obituaries/ | August 26, 2012 |
| 111 | DIP projects, OSHW & Trade Booths - Demonstrative DIP Dacrygelosis | https://theamphour.com/the-amp-hour-111-demonstrative-dip-dacrygelosis/ |  |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 155 | An Interview with Jeff Rowberg - Mini Module Master | https://theamphour.com/the-amp-hour-155-mini-module-master/ | July 22, 2013 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 275 | No One Even Missed Us? | https://theamphour.com/275-no-one-even-missed-us/ | November 19, 2015 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 335 | When the TV watches you | https://theamphour.com/335-when-the-tv-watches-you/ | February 8, 2017 |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ | March 12, 2017 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 404 | Proof Of Blink | https://theamphour.com/404-proof-of-blink/ | August 26, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ |  |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 658 | Uncle Al's Eating Garbage Again | https://theamphour.com/658-uncle-als-eating-garbage-again/ | February 12, 2024 |
| 676 | Moving House (And Lab) | https://theamphour.com/676-moving-house-and-lab/ | September 2, 2024 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
