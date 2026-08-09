---
title: Flash Memory
concept: flash-memory
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Flash memory is a non-volatile semiconductor memory in which the state of each cell is set by charge placed on a floating gate and read by sensing the cell's effect on a bit line.[297] Writing a cell requires a high voltage that drives carriers through a thin tunnel oxide, a mechanism that makes every write slightly destructive and limits both endurance and how far the cell can be scaled.[297] Density has been increased by aggressive process scaling and by storing multiple threshold levels in one cell, while limited write endurance, controller-managed wear levelling, and variable write latency have become defining concerns in system design.[296][297][41][324][356]

## Operating principles

### Cell programming and reading

A flash cell is written by applying a voltage large enough to drive carriers by tunnelling through a thin oxide onto a floating gate.[297] The carriers damage the oxide slightly as they pass through it, so every write contributes to the eventual wear of the cell.[297] Material limits on how thin the tunnel oxide can be made also place a floor on further scaling of the cell.[297]

A conventional read precharges the bit line, which is the column line running through the cells, and observes whether the selected cell discharges it.[297] An erased cell discharges the line while a programmed cell does not, with one or more comparators converting the result into a stored value.[297] An alternative read method holds the bit line at a constant voltage and measures cell current through a delta-sigma loop and a counter acting as a digital filter, producing the actual cell current rather than only a binary decision.[297]

Flash production has followed leading-edge process nodes rather than trailing them, with production flash at approximately 35 nanometres around 2007 and continued scaling from there.[297]

### Multi-level storage

Capacity has also been increased by distinguishing several threshold levels in a single cell instead of only an on and an off state.[296] A single-level cell stores one bit, while multi-level cells extend the same principle to four, eight, or more levels, with each additional level consuming voltage margin.[296]

## Endurance and write management

Endurance is the specification that most directly governs flash system design.[41] Modern flash parts are commonly quoted in the tens of thousands of write cycles, while a conservative planning figure of one to two thousand erase cycles is used where the effective endurance depends on controller behavior.[41] Ferroelectric memory provides a contrasting point on the endurance scale, with specifications in the region of a hundred trillion write cycles.[41]

Wear levelling exists because applications do not naturally distribute writes across a device.[324] Repeatedly writing one location can destroy that location within hours, while spreading the same traffic across the device converts it into a manageable lifetime.[324] Even with wear levelling, a continuously written device has a finite life that can be calculated from its write rate and rated cycles.[324]

The controller logic that makes flash usable also makes its timing non-deterministic.[356] An SD card performing internal wear levelling can stall for as long as two hundred milliseconds, and a FAT file system adds further delay when its allocation table must be rewritten, so buffering must be sized for worst-case rather than average latency.[356]

A single flash chip can sustain approximately two hundred megabytes per second of write bandwidth, allowing a high-speed camera to write captured frames directly to flash rather than buffering them in DRAM first.[325] In such a design, endurance rather than bandwidth becomes the binding constraint: at sixty thousand write cycles, continuously looping a recording consumes the rated life of the flash in approximately two weeks.[325] The alternative architecture buffers into DRAM, but the continuously written buffer limits such a camera to a few seconds of footage because practical DRAM capacity is bounded by the required write speed.[324]

Continuous data logging without a write budget is a deferred failure mode: vehicles that logged continuously into flash began failing after approximately four years as the parts exhausted their rated write cycles.[464]

## Manufacturing, packaging, and sourcing

Memory dies are repaired or redirected rather than discarded when they fall outside full specification.[241] Between fifteen and twenty percent of DRAM and flash parts fail specification and are sold at a substantial discount to buyers able to use them.[241] DRAM is commonly repaired at wafer level by laser-fusing spare rows, while flash uses flash-based fuses that can be configured later, so less wafer-level repair is performed on flash.[241]

Flash fabrication differs sufficiently from logic fabrication that omitting it from a logic die makes that silicon cheaper, and dedicated memory manufacturers building on memory-optimised advanced nodes can produce flash that a logic process cannot integrate as effectively.[713] Advanced packaging resolves the resulting tension by connecting a logic die built on a logic-optimised process to a memory die built on a memory-optimised process through an interposer close enough to preserve bandwidth and signal integrity.[713] Flash is also more forgiving than RAM as an off-die resource because its interface bandwidth matters less, so designs that must keep RAM on the die may still place flash outside it.[616]

Packaging can narrow the gap between external and integrated memory.[12][687] Where one die cannot hold the required flash, two dies can be packaged together and joined inside the device so that a large flash array is presented as a single chip rather than as a processor with external memory.[12] On the RP2350, placing the flash die inside the microcontroller package rather than beside it on the board suited space-constrained designs and removed the memory connection from the exposed board routing.[687]

On a conventional microcontroller die, the processor core occupies only about ten to twenty percent of the area, while memory, principally flash, together with peripherals and analog blocks dominates the remainder.[95] A part with no on-board non-volatile memory falls outside the conventional definition of a microcontroller, which requires on-board RAM and read-only memory, and it forces the designer to determine whether bootloader code is required to fetch code from an external device before the application can run.[713]

Flash pricing at very high volume is set by long-term commitment rather than list price, and a purchaser able to sign a multi-billion-dollar, multi-year supply order obtains pricing unavailable to smaller buyers.[193] At the opposite extreme, small NOR flash memories have become harder to obtain because manufacturers prefer to sell larger devices, even though a small memory remains appropriate where cost and power dominate.[489] The counter-pressure is that ARM-class microcontrollers have become inexpensive enough to provide megabytes of memory for only a few dollars more than an eight-bit part, leaving peripheral requirements rather than the processor core as the usual reason to remain with smaller architectures.[489]

## Historical development

Flash established its commercial position by reaching mass production while several technically mature non-volatile alternatives were still in development, making physical parts available for purchase before competing technologies could occupy the same markets.[23] The demand that made flash a profitable segment of the semiconductor industry arrived through a sequence of product categories: small media players, mobile phones requiring removable cards, tablets, and finally solid-state drives in laptop computers.[241] Two decades of process development, yield improvement, and cost reduction now stand behind the incumbent technology, and its manufacturers retain room to reduce prices when challenged.[104]

Ferroelectric memory occupies an intermediate position between static RAM and flash, combining speed with freedom from flash's write-cycle limit, but it has remained a niche technology because of cost and lower production volume.[41]

Before reprogrammable memory was available on microcontrollers, development systems used EPROM emulators: devices that appeared to the target as erasable read-only memory while appearing to the development machine as RAM, avoiding repeated ultraviolet erase cycles.[247] The first microcontroller that was neither ultraviolet-erasable nor one-time programmable used electrically erasable memory, removing both the erase cycle and the need for an expensive in-circuit emulator, and a flash version followed with the same operating model.[24] A low-cost programmer connected to a serial port then placed reprogrammable microcontrollers within reach of individual developers.[413]

Flash-based microcontrollers appeared around 1995 and differed operationally from the electrically erasable parts that preceded them: the earlier technology could program and change a single byte, while flash erased and programmed the whole part.[632] The two process lines continued in parallel in the same fabrication plants for decades because products designed in each era continued to order parts built on the corresponding process.[632] In-circuit debugging arrived alongside flash around 1997 in a part combining flash memory with breakpoints and single stepping, forming the direct ancestor of later low-cost embedded debug interfaces.[485]

Replacing the mask-programmed ROM of a console cartridge with a flash chip became a route into embedded development because it converted a fixed device into one that could be reprogrammed at will.[359] A complete flash-based solid-state disk packaged as a 28-pin dual in-line device likewise removed the need to attach a mechanical hard drive to an embedded computer.[362]

Flash remained expensive enough in the 1990s that a camera using it might hold only about two megabytes, with images extracted through a 9600-baud serial link.[490] Under those constraints, a lower-quality camera writing to removable floppy disks could move images faster in practice and could be reloaded in the field.[490]

## Flash in microcontrollers

Executing code from flash consumes more energy than executing from RAM; on one low-power part the difference is approximately two microamps per megahertz.[636] A low-power design therefore balances the energy required to fetch from flash after each wake against the leakage required to keep RAM powered, with memory power domains able to remain on independently of the processor to preserve state.[636] The correct balance depends on wake frequency, while the number of power domains is itself constrained because each additional domain requires load switches and complicates power-routing integrity.[636][687]

Microcontrollers commonly provide a small electrically erasable memory alongside program flash, ranging from a few hundred bytes to a few kilobytes, for constants and configuration data.[428] This memory has much higher endurance than program flash, whose rating of roughly ten thousand cycles reflects the expectation that it will be rewritten only a handful of times during the life of the device.[428]

At the bottom of the market, microcontrollers are specified in kilobytes rather than megabytes, with one class of parts carrying sixteen kilobytes of flash and two kilobytes of RAM at tens of megahertz.[637] Software for such parts is constrained to hand-optimised code or a lightweight library rather than a general hardware abstraction layer.[637] At the very lowest prices, self-programming on-chip flash may disappear entirely, creating a risk for designs expected to update themselves; purchasing vendor-pre-programmed parts shifts the programming step back to the supplier for approximately another cent per device.[412]

Parts are sometimes manufactured with more physical flash than the part number indicates, with the larger array locked out in software.[524] In one case, directly writing and reading addresses above the nominal size exposed 256 kilobytes on a device sold as a 128-kilobyte part.[524]

## Capacity planning in embedded software

Flash capacity is a common reason for moving up a microcontroller family: a program grows beyond the available memory, leaving a choice between reducing the code and selecting a larger part.[187] Fitting an application exactly into the available flash is a false economy at low volume because a program occupying 1,023 of 1,024 bytes leaves no room for later additions, and processor prices fall quickly enough that waiting six months can be cheaper than further optimisation.[187] The calculation reverses at high volume, where a fifteen-cent saving across a million units outweighs engineering time.[187]

Standard library functions consume flash out of proportion to their apparent use.[541] Linking a single formatted-print call can add one or two kilobytes of library code, which on parts with only tens of kilobytes has led developers to write smaller replacements.[541] A component shortage that forces substitution of a part with half the flash and half the RAM likewise requires the code base to be halved, a task made difficult when a vendor-supplied wireless protocol stack arrives as a large binary blob whose size cannot be reduced.[541]

The flash available to application code on a wireless part can be far below the headline capacity.[516] On a 512-kilobyte device, a vendor Bluetooth stack may occupy about sixty kilobytes, and reserving space for a second firmware image halves the remainder, leaving roughly two hundred kilobytes for the application.[516] Halving the flash on a module can remove the ability to hold that second image entirely, turning an apparent component substitution into the loss of field-update capability.[551]

Debug logging presents the same capacity problem from another direction.[614] Transmitting formatted strings over a serial link consumes flash for the strings, consumes transmission time, and cannot be performed from an interrupt context.[614] A more economical scheme compiles the strings out of the binary, leaves only symbols, and transmits pointers resolved against a host-side copy of the symbol table, reducing verbose logging to a few bytes per message.[614]

A file system can be placed directly in a microcontroller's internal flash; embedded Python ports carry a FAT file system internally and can extend it to an external flash chip or SD card so that files use the same calls as on a desktop system.[323] In such an interpreted environment, source conveniences cost flash directly because comments occupy space in the stored file, and importing that file loads the whole file into RAM.[323]

Memory size can determine part selection independently of architecture.[224] For video work, a small package offering 256 kilobytes of flash with 64 kilobytes of RAM can be preferable because RAM, rather than flash, is the first resource exhausted.[224] Running completely out of flash is also a legitimate trigger for a product revision because a design with no remaining space cannot accept new features.[293]

## Firmware update and security

A bootloader is a small program resident in flash that runs before the application, validates the application, and transfers execution to it when the check passes.[212] Updating the application requires a route back into the bootloader and a data path for delivering the new image, whether over a vehicle bus, USB, or an ordinary serial connection.[212]

Update capability must be included in the flash budget at design time, with enough space reserved to store and validate a second image against the current one.[526] The hardware path into update mode must also be planned at the same time, whether it is a button, a signal line, or a connector, because it cannot be retrofitted later.[526] Writing a bootloader therefore requires dividing flash into regions that support robust image update and then defining versioning and rollback policy above that layout.[590] Validation before switching images can only establish that the candidate passed the tests written for it, not that the new image is correct in every respect.[590]

An external flash chip used as a staging buffer makes wireless update robust against interrupted transfers.[398] The incoming image is written to the external device, the processor reboots, and the bootloader erases and rewrites internal flash only when it finds a complete image; an interrupted transfer leaves no complete image, so the existing firmware continues to run.[398]

One-time programmable microcontrollers remain in shipping products because they save a few cents, but they make field bug fixes impossible except by desoldering and replacing chips for a small number of customers.[619] Moving to a flash-programmable part is what makes firmware update available as a product feature at scale.[619]

The same reprogramming mechanism is also an attack surface, because an externally reachable link such as a wireless bridge onto a vehicle bus can become a path for reprogramming the devices attached to that bus.[212] Voltage glitching during a flash read can make the read return data different from the stored contents or corrupt values held on the stack; against a counted lock-out loop, the attack objective is to escape the loop and regain further credential attempts.[418] Dumping the entire flash contents defeats read protection and provides the information needed to replicate a product, so such protection functions as a delay against a determined cloner rather than as an absolute defence.[656]

In a firmware-development tool built by Trammell Hudson, logging every flash access and serving the contents from emulated memory instead of the flash chip exposed a security defect in which certain addresses were read twice.[463] Disassembly showed that the second read was a code fetch occurring after signature validation had already passed.[463]

## Further reading

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 12 | Dave Is Back And Blogging! | https://theamphour.com/the-amp-hour-12-dave-is-back-and-blogging/ | |
| 23 | The Innovation Speculation | https://theamphour.com/the-amp-hour-23-the-innovation-speculation/ | |
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ | |
| 41 | An Interview with Jeff Keyzer - Exhilarating ESC Escapades | https://theamphour.com/the-amp-hour-41-exhilarating-esc-escapades/ | May 4, 2011 |
| 95 | An Interview with Øyvind Janbu - Feracious Fabless Facilitator | https://theamphour.com/the-amp-hour-95-feracious-fabless-facilitator/ | |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 193 | We're Sorry! But Apple Ain't! - Remorseless RAM Racketeering | https://theamphour.com/193-were-sorry-but-apple-aint-remorseless-ram-racketeering/ | April 7, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 241 | An Interview With Chuck Peddle - Charismatic Chipmaking Coryphaeus | https://theamphour.com/241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus/ | March 18, 2015 |
| 247 | An Interview with Voja Antonic - Gerontogenous Galaksija Genesis | https://theamphour.com/247-an-interview-with-voja-antonic-gerontogenous-galaksija-genesis/ | April 29, 2015 |
| 293 | Call In Show #4 | https://theamphour.com/293-call-in-show-4/ | March 30, 2016 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 297 | An Interview with Jake Baker | https://theamphour.com/297-an-interview-with-jake-baker/ | May 4, 2016 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 324 | Mapping Out Nerdery | https://theamphour.com/324-mapping-out-nerdery/ | November 23, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 413 | A House of FR4 | https://theamphour.com/413-a-house-of-fr4/ | October 28, 2018 |
| 418 | An Interview with Josh Datko | https://theamphour.com/418-an-interview-with-josh-datko/ | December 2, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 464 | KonnectorPanik | https://theamphour.com/464-konnectorpanik/ | October 27, 2019 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 489 | An Interview with Jack Ganssle (2nd) | https://theamphour.com/489-an-interview-with-jack-ganssle-2nd/ | April 19, 2020 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 526 | Why IoT Is Difficult with Jonathan Beri | https://theamphour.com/526-why-iot-is-difficult-with-jonathan-beri/ | January 18, 2021 |
| 541 | Chip Shortage Denier | https://theamphour.com/541-chip-shortage-denier/ | May 10, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 590 | Finding Hardware Flaws with Laura Abbott | https://theamphour.com/590-finding-hardware-flaws-with-laura-abbott/ | May 22, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 632 | Steve Sanghi - Microchip CEO for 31 Years! | https://theamphour.com/632-steve-sanghi-microchip-ceo-for-31-years/ | May 15, 2023 |
| 636 | Discovering Cursed Connectors | https://theamphour.com/636-discovering-cursed-connectors/ | June 19, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 656 | Pneumatic Tubes, Straight To The Home | https://theamphour.com/656-pneumatic-tubes-straight-to-the-home/ | January 22, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
