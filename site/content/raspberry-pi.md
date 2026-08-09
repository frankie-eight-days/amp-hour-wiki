---
title: Raspberry Pi
concept: raspberry-pi
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Raspberry Pi is a family of low-cost single-board computers and associated microcontroller boards built around media-processing silicon originally developed for high-volume consumer products.[97][529] The project is structured as a charity carrying an educational mission, funded by the profits of a trading subsidiary that employs the engineers and sells the hardware at prices held uniform regardless of volume.[529] The range extends from full single-board computers through compute modules intended for design-in to a dual-core microcontroller sold on pick-and-place reels at prices measured in tens of cents.[235][528][574]

## History

The founding observation was a price gap rather than a technical one: the same silicon costs an individual buying in ones far more than it costs a high-volume customer such as a phone or media-centre maker, and that gap constitutes a structural advantage for large companies.[97] Getting one of those high-volume media processors onto a board an individual could buy was the point of the exercise.[97] The immediate predecessor was a hand-built machine on stripboard at the same target price, producing composite video at 320 by 240 with some accelerated graphics operations, assembled in an afternoon from freely available components with a soldering iron.[97]

The system-on-chip used in the first boards already existed as a media processor before the project began; the founding insight was recognising that an existing part suited the machine, and several of the hardware team had worked on that chip at the vendor.[529] Subsequent generations were evolutions of that same silicon, replacing the weaker processor cores and adding more of them, until the fourth-generation part became a new design on a 28-nanometre process where the earlier chips had been 40 nanometres; by then the sales volume made the customer significant enough to ask the vendor for specific features.[529]

## Hardware design

### Silicon integration

Across generations the design has absorbed external support silicon into the main chip, the power-management chip or the input-output controller, leaving a board of connectors, capacitors and resistors.[648] This lowers cost and simplifies the supply chain, and it is also forced by board area, since fitting everything within a credit-card outline becomes harder each generation.[648]

With the RP1 generation, the peripheral set was split into a separate input-output controller chip designed in-house, removing the need for the main silicon vendor to carry board-specific medium-speed functions such as USB and general-purpose input-output, which the vendor prefers to keep generic.[648] One consequence is latency: toggling pins directly from the application processor was always a comparatively high-latency operation, and placing the input-output controller behind a PCI Express link makes it worse, because each pin change becomes a message across the bus; timing-critical uses such as driving addressable LED strings are where that penalty shows up.[648]

### Microcontroller board

The microcontroller board was cost-engineered from the start, with a dual in-line form factor chosen deliberately so the board could be used as a component inside other products rather than only as a development board.[529] The board layout and the chip pin assignment were designed together, because getting the pins into a sensible order takes iteration and having a board to lay out is what reveals whether the ordering works for other users as well as for the vendor's own product.[529] The resulting board is two layers with single-sided surface mount and a simple but flexible power chain, chosen so that it is easy to automate, easy to package and therefore as cheap as it can be made.[529] The board ships on a pick-and-place reel with castellated edges, and its width was chosen to match a standard reel width, a design decision made years ahead in anticipation of customers placing the module by machine.[528]

The part itself is a dual Cortex-M0+ running at 133 MHz with 264 kilobytes of SRAM, which is substantial for its price but is explicitly not in the class of an application processor and does not reach the hundred-nanoamp sleep currents of parts designed for that.[528][529] The design target was performance at a price point rather than low power; the part competes where the required performance is unaffordable elsewhere rather than where sleep current dominates.[529] It carries no internal flash, only RAM, so it is inert until code is loaded from outside; the reason is cost, since adding a flash process to the die is a different and more expensive process.[713] Demand for the bare chip led to it being sold by the reel at around eighty cents in quantities of five hundred and seventy cents in reels of thirty-four hundred, with customers asking for tens of thousands at a time.[574] Adding a wireless part to the same board raised its price by about two dollars, which is the scale at which decisions are made on a board of that cost.[595]

## Supply and openness

The processor at the centre of the single-board computers cannot be bought through ordinary channels: obtaining it means presenting as a large customer, signing non-disclosure agreements and committing to volume, which is the practical meaning of the platform not being open hardware.[319] No schematic or board files are published for the boards, so a user cannot reproduce one; documentation has improved, but the design itself is not available.[664]

That difference has a concrete consequence for anyone designing a board into a product: where the design files are open, a customer whose supplier stops production can take the files to an assembly house and have more built, and where they are closed, that option does not exist.[207] The contrasting case is the BeagleBone, an open competitor board that can be produced by anyone from its published files and is manufactured by more than one company.[207] A business built on a board it cannot manufacture is exposed the same way as one built on a proprietary chip: if the board is discontinued or the version abandoned, the choice is a forced port or the end of the product, with the mitigation a board offers over a chip being that a connector can be made the abstraction boundary.[351] On this point, Chris Gammell frames the underlying question as how much of a product's destiny its maker wants to control: the attraction of the platform is the graphical interface, the Linux capabilities and the community, and the price is control over the product's own supply.[372]

The principal countermeasure the platform offers is a defined production lifetime; one compute module is advertised up front as having an eight-year production life, which is what makes an industrial design-in defensible and is one of the first things asked of any part designed into a system.[514]

## Use in products

The compute module exists as a deliberate stepping stone for people whose projects outgrew the development board but who are not ready to lay out their own processor, memory and high-speed interfaces; it is not aimed at very high volume, because the pricing carries no volume breaks, and is positioned at runs on the order of a few thousand units.[235] A system on module of this kind solves a specific layout problem: laying out a high-speed memory interface is the hard part, so pairing the processor and its memory in a qualified unit and exposing everything else through a connector moves the difficult work into the module and leaves the low-speed peripherals on a carrier board.[650]

Dave Jones's rule of thumb is that a development board belongs in a run of about a hundred — for instance controlling production jigs, where designing a custom board would be wasted effort — while the same choice at volume is a different decision.[282] His stated reasons against building such a board into a product at scale are mechanical: the integration needs its own connectors and additional circuitry, the result is an awkward stack that is difficult to mount, and the money saved on the board is spent on making it fit.[282] Where the architecture really is right, Jones's professional route is to take the circuit and design the processor onto one's own board, accepting the vendor agreements and higher unit cost that come with it.[282] He also cautions against fitting compute modules to designs that never use their USB, video or camera interfaces, which means choosing a sixty-to-hundred-dollar embedded computer over a four-dollar microcontroller, usually because the team knows Python; the counterweight is that development cost against volume can still justify a familiar platform, and the error is choosing without doing that arithmetic.[645]

For a product needing HDMI output, audio and graphics acceleration, Jay Carlson's position is that the compute module is the first part to reach for, because the underlying chip is built in very high volume for media applications and carries HDMI transmitters, graphics acceleration and hardware video encode and decode that general-purpose application processors charge heavily for.[515]

## Electrical and power characteristics

A five-volt supply capable of two and a half amps is a real constraint that rules the platform out of many embedded power budgets before any other consideration.[428] The boards are unforgiving about their supply: they brown out and reset on marginal power, and Samy Kamkar found that an early model could not run two USB wireless adapters at once, where a five-hundred-milliamp port is not enough against nine hundred milliamps expected.[308] Plugging in a USB device draws a surge of current to charge the bulk decoupling capacitors downstream of the port protection device, which can trip that device into overcurrent and produce a warning that has nothing to do with the attached device's steady-state draw.[408] Measured consumption on the small wireless variant is around 275 milliamps at idle and close to 600 milliamps under load, and a full-size board idles at roughly two watts, so an ample supply rather than a nominal one is the working recommendation.[565]

Peripheral blocks are power decisions taken in the device tree: on one compute module the USB core is disabled by default and enabling it costs a substantial share of the board's consumption, which is invisible until measured.[548] Running a compute module near its input voltage limit leaves no margin for switching transients; Gammell had a module powered through a switching circuit destroyed, with inductive kickback the suspected cause, having already been close to the voltage limit on the CM4.[551]

## Software and expansion

A single-board computer is designed on the assumption of a keyboard, mouse and monitor, which is why booting one headless requires changing the configuration first rather than being the default case.[515] The boards do not boot a generic operating system image the way a personal computer does: the bootloader and initialisation are board-specific rather than following the ARM standard for a discoverable boot, so each board needs its device tree and its own build, which is why distributions ship board-specific images.[651]

The expansion header moved from twenty-six to forty pins across a hardware revision while keeping the original pins in place, so existing add-on boards continued to fit; maintaining that compatibility, and not diverging the firmware alongside it, is what keeps a platform's accessory ecosystem intact through a revision.[207] Add-on boards identify themselves through an on-board memory device rather than requiring the user to select a library by hand, with pin configuration handled by device tree overlays because the pins are multiplexed.[235]

## Applications

Industrial input-output must never be wired straight to the board's pins, because a 24-volt industrial signal is not a logic level; interposing proper interface circuitry is the point that separates a working installation from a destroyed board.[385] Single-board computers are established in university and technical-school laboratories for sampling and motion-control experiments and are crossing into industrial use, but they do not replace a programmable logic controller and are not supported to that standard.[385]

A production test station documented on one product line was built around one of these boards: a barcode scan of the shipping label looked up the customer's chosen radio frequency, the board flashed that frequency into the unit on a pogo-pin bed, and then transmitted a test tone on that frequency using a software radio library that drives an output pin with a short wire as the antenna, so a working unit announced itself audibly.[350] Jørgen Jakobsen's accelerated-life test rig ran amplifiers for a month with the boards generating the audio, monitoring device temperatures and logging into a database, an instance of the boards serving as long-duration test controllers.[338] A long-range radio gateway is commonly built as one of these boards carrying the network software connected through its header to a concentrator board holding the radio silicon, rather than as a purpose-built device.[380]

In vision work, routing all the data through the host board is the bottleneck: Brandon Gilles's prototype combining a depth camera with a neural accelerator passed every video and depth frame through the single-board computer for reformatting and overlay, which was the argument for moving that processing onto the module itself.[517]

Jeff Geerling defends building a cluster from several cheap boards as a learning exercise rather than a performance one: it forces the builder to solve networking, power and management, and those skills transfer to real infrastructure in a way one faster machine would not teach.[651] His selection rule is that the small wireless model is among the most efficient ways to put a wireless connection into a small project without dropping to a microcontroller, and for work that is mostly toggling pins the top-of-range board's processing is not needed; the newest and fastest board is not the best board for many of the platform's ordinary uses.[651]

## Organisation and market position

The organisation is structured as a charity that owns a trading subsidiary, with the subsidiary employing the engineers who design the products and the charity carrying the educational mission; the profit from hardware sales funds that mission, which is also why pricing is kept the same for everyone rather than discounted by volume.[529] Cost optimisation is the first lens applied to every decision in the silicon, and the boards have been sold below what an ordinary buyer could purchase the constituent chips for, which is what the high-volume chip relationship buys.[528] Gammell characterises the approach as a disruption from below rather than a cheaper version of an existing computer: starting from a media-processing chip obtained cheaply and asking what could be built produces a different object from starting with the requirement for a screen and a keyboard and trying to reduce its cost.[558]

Dave Jones locates the value of the platform in the integration rather than any single part: the boards are the assembled, tested combination of silicon, software and support, and a buyer's whole interest is that the top level works.[652] Geerling's assessment of the competitive field is that rival single-board computers now match or beat the platform on raw performance and efficiency, and the durable advantage is maintenance and software support rather than hardware.[651] Jones adds that availability is part of the comparison — boards with better processing per dollar exist, and the question that settles the choice is "But can you buy them?"[520] Under shortage conditions buyers were pushed to scalpers; Dave Young's programme concluded its best approach was to pay them, and placing back orders carries its own penalty when they arrive months later against a programme that has already moved on.[628]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ | |
| 207 | B Plus Boards and D Minus Cities - Uneath Urban Ubication | https://theamphour.com/207-b-plus-boards-and-d-minus-cities-uneath-urban-ubication/ | July 14, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 282 | 3D Product Logistics | https://theamphour.com/282-3d-product-logistics/ | January 13, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 350 | An Interview with Zach Dunham | https://theamphour.com/350-an-interview-with-zach-dunham/ | July 3, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 372 | Year End, 2017 | https://theamphour.com/372-year-end-2017/ | December 17, 2017 |
| 380 | Just Terrestrial and Space Things | https://theamphour.com/380-just-terrestrial-and-space-things/ | February 18, 2018 |
| 385 | An Interview with John Davis | https://theamphour.com/385-an-interview-with-john-davis/ | March 25, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 514 | Focus, Dammit | https://theamphour.com/514-focus-dammit/ | October 25, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 520 | Inductance and Stuff | https://theamphour.com/520-inductance-and-stuff/ | December 6, 2020 |
| 528 | New Year, New Gear | https://theamphour.com/528-new-year-new-gear/ | January 31, 2021 |
| 529 | Embedded Hardware with the Raspberry Pi Team | https://theamphour.com/529-embedded-hardware-with-the-raspberry-pi-team/ | February 7, 2021 |
| 548 | The Last Line of Defense | https://theamphour.com/548-the-last-line-of-defense/ | July 5, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 558 | Toasted Marshmallow Connectors | https://theamphour.com/558-toasted-marshmallow-connectors/ | September 19, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 595 | Trade Show or Conference? | https://theamphour.com/595-trade-show-or-conference/ | July 10, 2022 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 650 | Accessible ASICs with Andreas Olofsson | https://theamphour.com/650-accessible-asics-with-andreas-olofsson/ | November 12, 2023 |
| 651 | Learning Computing with Jeff Geerling | https://theamphour.com/651-learning-computing-with-jeff-geerling/ | November 20, 2023 |
| 652 | For a couple weeks there... | https://theamphour.com/652-for-a-couple-weeks-there/ | November 28, 2023 |
| 664 | Simulating doors falling off | https://theamphour.com/664-simulating-doors-falling-off/ | April 3, 2024 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
