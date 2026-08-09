---
title: LCD
concept: lcd
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A **liquid-crystal display** (LCD) is a display technology in which a layer of liquid crystal between crossed polarisers modulates light, either from a backlight behind the glass or from the ambient environment. It draws essentially no power in the steady state and consumes energy only when the displayed value changes, which is what made battery-powered calculators and the novelty formats that followed them possible.[725] The crossed polarisers throw away about half the incident light even when the cell is fully open, so a transmissive panel can never pass more than roughly fifty per cent of its backlight.[412] In embedded products the display is frequently the largest single cost on the bill of materials, and adding a capacitive multi-touch layer pushes it higher still, which can put the product above what its market will pay.[84]

## Optical construction

Optical losses in a colour panel multiply: about half the light is lost in the polarisers and roughly two thirds more in the RGB stripe filters, leaving at best about fifteen per cent of the backlight emerging from the panel, which is why the bare backlight of a monitor is painfully bright.[412]

Graphic glass is supplied either as transmissive, which is unreadable without its LED backlight, or as transflective, which modulates ambient light as well and so remains readable with the backlight off; the transflective option is what allows a low-power mode that leaves the backlight unlit.[700] A reflective custom segment display is cheap and gives very high contrast for almost no power because it modulates ambient light instead of a backlight, which makes it viable in a battery product that has to keep a real-time clock displayed continuously.[700]

Reflective electrophoretic displays reach a paper-like contrast that liquid-crystal technology has not matched despite decades of manufacturing refinement, which is why reflective e-paper is used in place of LCDs for long-form reading.[46] A memory LCD occupies intermediate ground: it is a liquid-crystal panel with a bit of static RAM behind every pixel, so the image is held on the glass at a holding current on the order of nanoamps, but unlike e-paper it is volatile and the image is lost when the supply is removed.[688]

Many panels have an asymmetric viewing cone, optimised for being read straight on or from below and washing out or inverting when viewed from above, which makes the mounting height and tilt of a bench instrument part of its usability.[528]

## Temperature and response

Liquid-crystal displays slow down as temperature falls: the crystals become less mobile, so the panel's response time lengthens and the visible update rate of the readout drops well before the display fails outright.[127] Low-temperature behaviour can be checked without a climate chamber by leaving the product in a domestic freezer for about half an hour and then watching how quickly the readout updates after it is removed.[434] Whether to engineer a portable instrument for sub-zero operation is a deliberate scope decision rather than an oversight; one bench-supply design was left with its display untested at zero degrees on the judgement that its intended users would not operate it there.[434]

## Latency

A CRT displays incoming signal essentially as it arrives, within the propagation delay of the electrical signal, whereas an LCD is inherently latent because it updates on a frame-by-frame basis and cannot show an input change until the next frame.[655] A television or monitor adds further latency in its own right, principally through the scaler upscaling the incoming image, with the delay measured in tens of milliseconds rather than microseconds and stacking with the interface, the game engine and the input device.[490]

## Segment and graphic displays

Choosing a custom seven-segment glass over a general-purpose graphic panel removes the need to build and store character fonts, since the segment shapes are etched into the glass, whereas a dot-matrix panel obliges the designer to generate fonts and the rendering code for them.[658] The cost of custom segment glass is inflexibility: the icon and digit layout is frozen in the tooling, so the product cannot later show additional items on screen, add text, or repurpose the display for a different function.[700]

Some graphic modules can be ordered with the font chip already fitted behind the glass, so the character set arrives as part of the display rather than as a separate part to place; the module's flexible connector, however, is typically on a 0.5 millimetre pin pitch that is awkward to lay out and hand-assemble.[700]

Display size in an instrument follows from the reading distance rather than the resolution wanted: a bench product intended to be read from across a room was specified at roughly three and a half to four inches diagonal, about 100 by 50 millimetres of active area, to carry a large enough font.[658]

## Driving and interfaces

Direct-driving a segment display from a microcontroller consumes an enormous number of pins: a moderately sized custom glass took thirty-two segment lines plus eight commons, so at least forty pins of the package were dedicated to the display alone.[393] Microcontroller families tie LCD driver capability to package size, so buying more common lines forces a larger package that also carries more memory and a bigger die, and the resulting part can cost around three times as much, which is what makes a dedicated external driver chip the cheaper option.[393] That choice trades silicon cost for supply risk, since an external driver adds a bill-of-materials line that can go obsolete or become unobtainable, and commodity display drivers are often not stocked by broadline distributors and must be bought in quantity from a regional distributor.[393] Committing to a particular driver often means accepting a single-source part, and that sourcing exposure has to be weighed as part of the architecture decision rather than treated as a purchasing detail.[180]

A conventional character module needs a parallel bus of more than two signals, so on a pin-starved microcontroller it can only be used by adding external latching logic; an I2C display module avoids that by needing only the two bus lines.[74] At the other end of the range, a parallel 24-bit RGB interface runs a continuous pixel clock in the tens of megahertz, around 30 MHz for a modest panel, yet such a bus can still be wired up on a breadboard for evaluation with nothing worse than occasional visual glitching.[515] Driving a display over a parallel interface with DMA gives substantially more bandwidth than the SPI connection usually used for small panels, and moving the transfers to DMA keeps the processor free while the frame is written.[356]

Some microcontroller LCD peripherals include blink and animation engines that alternate between segment patterns autonomously, so a display can keep changing while the core stays in its deepest sleep mode and never wakes to service it.[629]

Two panels of similar size are not interchangeable at the software level, because each may use a different display controller; driving a second panel can mean rewriting the driver or reprogramming the controller on the evaluation board rather than reusing the working code.[700] Selecting a panel that ships with a manufacturer's demonstration board removes the display bring-up from the critical path, since fonts and sizes can be exercised on known-good hardware instead of a day being spent working out how to talk to the controller.[700]

On an embedded product with a display, the display driver is normally brought up before any other peripheral, because without it there is no channel for status output and nothing else can be observed while it is being debugged.[124] Putting display initialisation code inside a bootloader, however, means a display bug becomes a bootloader bug: one product had to have its bootloader updated in the field because the LCD contrast registers were set incorrectly, against the rule that a bootloader should be simple enough never to need changing.[364]

## Power

The LED backlight, not the liquid-crystal layer, dominates the power budget of a graphic panel; a four-inch panel's backlight drew on the order of 800 milliamps, which rules out running it continuously from a small battery.[700] A display and its backlight may both need a rail above the microcontroller's supply, and a PWM output driving a voltage doubler will generate it with no dedicated converter, at the cost of keeping a core awake that would otherwise sit in a low-power mode.[175]

An LCD can be preferred over OLED in a battery-powered product for power reasons rather than image quality; an 800-by-800 circular panel was selected for a handset on the grounds that it consumed acceptably little for its size.[475]

## Sourcing and cost

In a small instrument kit the display can be the single most expensive line on the bill of materials: one such kit used a display costing about ten dollars in ones and still about eight dollars in volume, more than any other part.[74] Distributor stock shown while a bill of materials is being compiled may be gone by the time the order is actually placed, and display panels are particularly exposed to this because a mechanically suitable panel often has no drop-in substitute.[74]

Panels are sold against minimum order quantities, so a prototype built from a sample panel can leave a small company unable to produce the product it has just demonstrated until it can commit to a full panel order plus its lead time.[328] Custom glass is generally out of reach for a low-volume buyer because panel makers will not tool for small quantities; the low-volume route that does exist is specialist military-grade custom glass at prices around a thousand dollars per screen.[328]

Display technology moves at the leading edge while automotive qualification requires parts that have been through a long test cycle, so a screen designed into a car is rarely replaceable from the open market later in the vehicle's life.[464] Vehicle manufacturers cover the obsolescence of custom display modules by building service stock during the production run and warehousing it, rather than expecting to re-source an equivalent panel years later.[464]

## Failure modes

The characteristic long-term failure of older handheld multimeters is the display itself fading rather than any circuit fault, to the point that replacement glass is sold as a repair kit for those instruments.[180] Liquid-crystal glass is otherwise generally reliable, so a dead segment display is more often a connection failure, with the elastomeric bonding strip carrying conductive adhesive along the edge of the glass the usual suspect.[539] Panels can also fail progressively rather than all at once: a row of pixels along one edge bleeding into the display is a symptom of the glass or its edge connection degrading, and it can appear within hours of first powering a new panel.[700]

Flat flex cables running to a display are a mechanical weak point when the two ends are far apart and the cable is left unsupported, since the free length flexes in service and the copper in the flex eventually fatigues and opens.[292] A display assembled into an enclosure with insufficient vertical clearance will be destroyed by the closing action itself: repeatedly snapping a phone screen shut cracked the back of the LCD until enough material was shaved from the wiring, connector bodies and case interior to recover the missing height.[414]

A visible fade of an LCD when a load switches on indicates that the display bias is being taken from an unregulated supply; in cost-reduced consumer products the regulator is omitted, so a print motor's current draw pulls the rail down and the contrast collapses with it.[633]

## Other applications

Masked stereolithography 3D printers use a liquid-crystal panel as a programmable photomask, switching pixels to expose the whole of each resin layer at once instead of scanning a beam across it.[488]

## History

The Intersil 8020-class converter was the first single chip to perform a complete digital-multimeter measurement and drive the result straight onto an LCD, and that integration is what made the handheld meter form factor possible.[180] Converting an analogue 640-by-480 VGA signal into the parallel drive needed by a flat panel once required a board the size of a pizza box full of logic, sampling and clock-regeneration circuitry; the same function is now a single commodity chip on a small converter board.[633]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ |  |
| 74 | Younker Youtube Yarling | https://theamphour.com/the-amp-hour-74-younker-youtube-yarling/ |  |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 124 | SpaceX, Enclosures & Startups - Urging Unemployment Ullagone | https://theamphour.com/the-amp-hour-124-urging-unemployment-ullagone/ | December 3, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 180 | An Interview with Dave Taylor - Multi-talented Meter Maker | https://theamphour.com/180-an-interview-with-dave-taylor-multi-talented-meter-maker/ | January 13, 2014 |
| 292 | An Interview with Timothy Lamb | https://theamphour.com/292-an-interview-with-timothy-lamb/ | March 23, 2016 |
| 328 | The Ghost of Keyzermas Past | https://theamphour.com/328-the-ghost-of-keyzermas-past/ | December 21, 2016 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 393 | I've bitten myself | https://theamphour.com/393-ive-bitten-myself/ | May 20, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 464 | KonnectorPanik | https://theamphour.com/464-konnectorpanik/ | October 27, 2019 |
| 475 | An Interview with Christina Cyr | https://theamphour.com/475-an-interview-with-christina-cyr/ | January 19, 2020 |
| 488 | Sowing Discord | https://theamphour.com/488-sowing-discord/ | April 12, 2020 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ | January 31, 2021 |
| 539 | The King of Trash with Big Clive | https://theamphour.com/the-amp-hour-539-the-king-of-trash-with-big-clive/ | April 26, 2021 |
| 629 | At least my house isn't haunted | https://theamphour.com/629-at-least-my-house-isnt-haunted/ | April 23, 2023 |
| 633 | Engineering Optimization | https://theamphour.com/633-engineering-optimization/ | May 22, 2023 |
| 655 | The Twelfth Day of Keyzermas | https://theamphour.com/655-the-twelfth-day-of-keyzermas/ | January 8, 2024 |
| 658 | Uncle Al's Eating Garbage Again | https://theamphour.com/658-uncle-als-eating-garbage-again/ | February 12, 2024 |
| 688 | The Tandy Train | https://theamphour.com/688-the-tandy-train/ | February 11, 2025 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
