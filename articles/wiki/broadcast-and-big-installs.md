---
title: Stage, Broadcast, and Giant Installations
concept: broadcast-and-big-installs
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Stage, broadcast and giant installation electronics covers the design of very large, very public light and display systems: architectural light pieces, suspended structures, museum exhibits, stage dimming and large-screen video. The field inverts the ordinary prototype-then-production sequence, because a typical job is a single build of a couple of hundred boards with no budget for a prototype run and no schedule for a respin, so the design must work first time or every board has to be reworked by hand.[135] Its characteristic constraints are physical and perceptual rather than purely electrical: LED colour binning, the eye's non-linear response to light, power distribution across long runs, and site access windows that the electronics must be built around.[294][412][135] A modest bespoke light installation readily costs ten to twenty thousand pounds or more, because it combines specialist contractor time with one-off PCBs and large LED counts.[135] In the United Kingdom a significant share of large architectural light installations was funded by Section 106 planning conditions, under which a developer had to devote a percentage of a large development to public benefit, one qualifying category being public art.[135]

## Design method

The usual schematic-then-layout order does not survive contact with a large irregular LED array. Which LED connects to which driver channel is decided by the physical layout, so the design has to start from the board and the netlist falls out of it rather than the reverse.[224] On a severely compressed timescale the schematic can be dropped from the critical path altogether: a board layout and a parts list are what physically block fabrication, and no schematic is needed to get boards made.[224] Event and installation work occasionally compresses a whole design into a two-day cycle, with layout, fabrication, assembly and delivery of finished boards running to roughly a day or two from the initial request.[224]

Several practices shorten that loop. Exporting the bill of materials directly out of the PCB layout turns the layout itself into the shopping list, and keeping the CAD footprint library orientation matched to the part orientation in the pick-and-place feeders removes a whole class of rotation errors on repeat parts.[224] For very small build quantities, a board needing a mirrored variant can be handled by mounting the driver ICs rotated 180 degrees and re-laying-out only the few parts that genuinely cannot be flipped, such as MOSFETs and connectors; on a four-off build this costs far less engineering time than producing a second mirrored layout.[224]

Board outlines are often set by machine capacity rather than by the artwork. A 500 mm diameter LED display was split into four quadrant PCBs of about 250 mm square specifically so each board would fit the pick-and-place machine.[224] Dense LED matrix boards can push a fabricator to its finest design rules — in one case 0.125 mm track and space with a 0.15 mm drill, beyond what can be made in-house.[224] A fabricator's annular ring specification also has to be read together with its hole-size tolerance, since an extra 0.1 mm of drill tolerance forces visibly oversized via pads; the fix is to shrink the specified hole so the annular ring is still met at the tolerance extreme.[224]

Prototypes that work at a couple of hundred LEDs routinely fail to scale to tens of thousands, and the two things that break first are power distribution and data bandwidth rather than the microcontroller itself.[524] Replicating a development-board prototype a hundred times over is generally worse than consolidating onto one purpose-built PCB, because the cabling and connector count of the replicated approach becomes the dominant cost and failure surface.[524]

### Per-LED microcontrollers

One approach to irregular structures places a tiny microcontroller behind every one to three LEDs. This converts routing from a problem into a copy-and-paste operation, because every node needs only power, ground and a single shared data line; the alternative of 16-channel drivers forces tedious individual routing on any shape that is not a regular grid.[135] A six-pin PIC10F322 at about 25 pence in thousand-up quantities has interrupts, self-programming and PWM channels, and can be made to receive the 250 kbit DMX serial stream directly, which makes the approach economically plausible.[135] Parts cost works out a little under 30 pence per node, more than a shared multi-channel driver, but it is chosen because it collapses the layout and turnaround time on a one-off; a vendor programming service that loads firmware for about two pence a part avoids thousands of manual programming operations.[135]

Where a rectangular LED grid is cut into a circle, whole driver blocks fall outside the outline, so LEDs on the curve must be reassigned to drivers from other rows. Deriving the resulting pixel map took about a day, done by lighting one LED at a time and marking its position on tracing paper laid over the display.[224]

## LEDs and colour

A monochrome white LED delivers far more light per watt than an RGB device driven to produce white, and RGB mixing gives poor white in any case, so installations that only need white should use white parts.[224] Lighting-class white LEDs of a few millimetres square fell to under one cent each in reel quantities and are extremely bright; long thin formats and multi-die parts intended to run directly from 12 V are also standard.[294] White LEDs with improved colour rendering generally achieve it by adding extra red or orange emitters alongside the phosphor-converted die rather than by using a better phosphor alone.[412] Plessey entered the LED market from a semiconductor foundry background using a gallium-nitride-on-silicon process, which lowered the cost of blue LEDs relative to conventional substrates and produced parts as small as 0402.[224]

Marketplace-sourced LEDs are acceptable for experiments but not for permanent installations, and competition has made brand-name parts such as Osram cheap enough that there is little reason to take the risk on a fixed install.[294]

### Binning

White LEDs vary in colour by bin, and a single reel carries one bin code. A matrix panel can therefore be kept visually uniform by sizing it to consume whole reels; one display was deliberately trimmed slightly in size so that boards never straddled two reels.[294] Very high volume luminaire manufacturers take the opposite approach, deliberately mixing reels so each fixture contains a random distribution of bins and the variation averages out. Smaller buyers cannot do this and instead negotiate with distributors for the closest matched bins available.[294]

Binning differences are not always apparent during bring-up. Looking directly at bare LED points saturates the eye and flattens perceived grey scale, so a display can look uniform until a diffuser is added, at which point differences in colour temperature between individual LEDs become obvious.[224]

### Gamma and perceived brightness

Gamma correction originates in the non-linear response of CRT phosphors, which cameras pre-correct for. For LEDs the perceptual relationship is empirically close to a square law, so doubling apparent brightness needs about four times the drive.[412] Monochrome LED displays consequently need gamma correction to look like a smooth grey scale, which requires at least 12-bit drive resolution; a practical implementation takes 8-bit source data through a correction lookup table, with squaring as a good first approximation of the curve.[224]

## Drivers and data distribution

Installation LED systems are commonly driven over RS-485 or TTL serial at rates up to about 6 megabaud, with a host-side tool that takes an ordinary video file and applies the pixel mapping before sending it to the array.[224] Such protocols are usually specified one-way with no return path, because adding a return path forces error handling into a system that otherwise does not need it.[294]

Among addressable LED parts, the one-wire WS2812 offers only eight bits per colour and no global dimming, so dimming the whole array eats into the available intensity levels. The two-wire APA102 adds about five bits of global control and is easier to drive over SPI, but its PWM rate drops as global dimming is applied and the part is not constant current, so brightness follows the supply rail.[412] Because the APA102 is not constant current, a supply sag from about 4.5 V to 4 V along a long run visibly changes LED intensity, which makes power distribution part of the visual design rather than only an electrical concern.[412]

Integrated-driver LED parts have been avoided on permanent installations on reliability grounds, with discrete Texas Instruments drivers plus brand-name LEDs used instead; the integrated parts get specified when a project is tight enough on cost that the client accepts the failure risk.[524]

Where a client's own staff must extend the firmware, a single-vendor toolchain has a practical advantage over a general one: the client installs one IDE, opens one project and starts writing content code, instead of assembling a specific IDE version plus plugins.[524]

## Power

Sizing an LED board's DC-DC converter for the theoretical all-on current wastes money and space, because a display with thousands of LEDs is almost never run at full brightness, and the required current is not known until the assembled board is seen at the intended brightness.[224] A 500 mm diameter board carrying several thousand LEDs drew roughly 40 A at 5 V at full brightness yet did not run hot, because the dissipation was spread over the whole area of the board.[224]

Designing for reliability otherwise means assuming every failure mode will occur and derating accordingly: a load needing ten amps is given a fifteen or twenty amp supply, and clients are told up front which parts may fail so spares are bought before the install.[135] A generic 48-channel DMX dimmer at one amp per channel implies a 50 A supply feeding one box; the channel count was chosen because it factors cleanly into 16 RGB, 12 RGBW or 48 monochrome strips, letting one product serve many jobs.[135] Automotive high-side driver ICs that shut down within about 20 microseconds on a short allow such a multi-channel dimmer to be fully short-circuit protected on a one-kilowatt supply, without fitting a MOSFET per output large enough to survive the fault.[135]

Where mains is unavailable, generator choice is governed by weight distribution. Above roughly 5 kVA portable generators are diesel and substantially heavier than petrol units, so one large suspended structure was powered by four 3 kVA petrol generators distributed around it rather than a single large set, avoiding a heavy point load.[135]

## Mains dimming

Mains dimming products are polarised between stage-lighting racks rated around a kilowatt per channel and nothing suitable for many small mains LED loads, leaving a gap for eight- and sixteen-channel dimmers of a few hundred milliamps per channel for GU10 lamps and mains LED tape.[524]

A traditional triac dimmer is leading-edge: it waits past the mains zero crossing, then latches on for the rest of the half cycle. Dimmable mains LED lamps prefer trailing-edge phase cutting, because their front end is a rectifier and electrolytic capacitor that draws a large surge if switched on partway up the sine wave — which is also why conventional dimmers contain a sizeable choke to slow the turn-on edge.[524] Trailing-edge dimming interrupts current abruptly, and when the supply comes through a transformer the leakage inductance turns that interruption into a large spike: switching about 4 A off through an isolating transformer produced an 800 V transient that destroyed the internal PCB-mount mains supply. The remedies are either not to feed such a dimmer from a transformer or to place a few microfarads across the transformer output.[524]

In a multi-channel mains dimmer each channel's MOSFET source floats independently even though all channels share one live feed, so every channel needs its own isolated gate-drive reference. This is trivial at one or two channels and becomes the dominant packaging problem at sixteen, since a separate DC-DC converter per channel does not fit.[524] Short-circuit protection is also hard, because fault currents are large enough that the switching MOSFET fails before the fuse does; current sensing that acts faster than the fuse is needed instead of relying on the fuse.[524] Where a component is rated only for basic rather than reinforced insulation, a second independent isolation barrier can be added instead of replacing the part; in one mains dimmer this meant an isolated DMX receiver in series with the isolated gate drive, giving two separate barriers.[524]

Compliance practice differs sharply between temporary and permanent work: a one-event temporary piece may simply reuse a chip vendor's reference design without formal approval, while permanent installations are treated much more carefully.[135]

## Large-screen display technologies

Large-screen CRT projection was limited by the brightness obtainable from the tube face, and pushing the EHT voltage high enough to gain brightness produced significant X-ray emission. The Eidophor oil-film projector, developed in the 1950s, worked around this and dominated large-screen video projection for several decades.[294]

A transparent LCD panel loses at least half the light passing through it because of its polarisers even in the fully clear state, so installations built from clear LCDs depend entirely on strong ambient or architectural backlighting to work.[412] OLED displays cannot cover the military temperature range, which is why some ruggedised optical instruments still use LED dies deposited directly onto a substrate; the smallest standard parts, such as a 0.8 mm high seven-segment display, require a wire bonder to use at all.[412]

## Assembly, jigs and test

Assembly work on installations is heavily jig-driven. A large shopping-centre Christmas installation was built entirely from PCB: roughly 200 mm strips carrying three RGBW LEDs on each side plus a six-pin microcontroller, assembled into hexagonal star modules on a jig.[294] Physical position can be assigned at assembly rather than by wiring: a locating jig fitted with pogo pins at each module position programs each strip's ID as it is dropped in, so the strip knows where it sits in the structure, and the jig itself is built to be reconfigured for a different shape.[294] Assigning bus addresses is easy; the hard problem in a large lit structure is making each node know its physical position, and a handheld probe that both sends the address command and senses contact can auto-increment after each touch, so the installer only sets a starting address and then touches each node in order.[294]

Purpose-made pocket test boxes that light a strip at low brightness from a small battery let an installer verify a part in seconds without meters or bench supplies, and building such jigs and one-off tools pays for itself whenever the same operation is repeated hundreds of times.[294] In a three-dimensional installation that is winched up in layers, anything at the top becomes effectively unreachable once the layers below are fitted, so every drop cable and splitter is tested with a go/no-go plug-in tester before assembly begins.[294]

Machine assembly is not always applied to the whole board: it is often faster to machine-place only the high-count parts, such as hundreds of LEDs, and hand-solder the few large packages, since the stencil has already deposited paste for them and setting up a feeder for a handful of parts costs more than it saves.[415] Pick-and-place nozzle Z-height is a per-part calibration, and a machine that happens to work on one component can fling later parts off the board when the height is wrong, because solder paste tack is not enough to hold a part that is being struck rather than placed.[415] Carrier tape quality is a comparable yield risk: a batch of white LEDs supplied on unusually thin tape bounced out of the pockets as the feeder indexed, and even after modifying the feeder the loss stayed around 10 percent of a 22,000-piece build, recoverable only because the distributor had one more reel in stock.[412]

Very thin flexible-feeling LED boards can be made in 0.1 mm FR4, which is not an exotic material but the ordinary prepreg that fabricators already stock for the inner layers of multilayer boards.[412] Plastic push rivets are quick to install but awkward to remove, since the centre pin must be driven back out from the underside before the rivet can be extracted — a consideration when an installation is intended to be dismantled and reused.[294]

Where large assembled volumes must cross borders, logistics rather than labour rate often decides where the work is done: for a Hong Kong installation with about 28,000 assembled LED strips, shipping from the United Kingdom would have cost roughly 3,500 pounds, which drove local assembly even though the assembly cost itself was not very different.[294]

## On site

Installation sites impose hard scheduling constraints that the electronics has to absorb. A shopping centre may only be accessible at night, an immovable opening date fixes the delivery, and access equipment such as a cherry picker has to be negotiated with site management rather than assumed.[135] The dominant principle is to move everything possible off site: pre-assemble and pre-test so that on-site work is screwing down and plugging in, because access, light, power and tools cannot be relied upon and other trades may block the work area for hours.[135] Spares are budgeted primarily for the install itself, since a dropped or damaged connector on site with no replacement stops the job; boards are also rounded up to the next panel so that badly reworked units can simply be set aside instead of repaired under time pressure.[135]

Lifting is a cost variable in its own right. Helicopter lifting can be cheaper than crane hire for rooftop and large-structure work, because a crane requires closing the street and shutting the site down for a couple of days while the helicopter completes the lift in well under an hour.[135]

## Reliability and failure modes

RS-485 fails in a misleading way when one of the differential lines is not connected: depending on how the floating line settles, the link can appear to work, so every RS-485 installation should be checked end to end from one end for the presence of the far termination.[294]

Ceramic capacitors on a PWM-driven LED board are piezoelectric enough to audibly buzz at the PWM rate, which is a reason to choose a different decoupling technology on quiet installations.[224]

Connector keying is a weaker safeguard than it appears. A field failure that killed the first LED driver on each strip was traced not to ESD but to a substituted connector housing whose keying was slightly undersized, so a keyed Micro-Fit connector that should have been impossible to reverse could be forced in backwards, and one reversed orientation destroyed the first driver.[412] The general lesson is that keying alone should not be trusted as the only protection when assembly is subcontracted and done remotely; a series protection resistor on the vulnerable input would have made the failure impossible for negligible cost.[412] The same principle applies to physical security measures generally: one car phone riveted its serial-number EEPROM into the chassis, but the cable plug to the main board carried the same eight-pin DIL pinout as the memory itself, so the part could simply be unplugged and reprogrammed.[294]

Rules such as always fitting decoupling on every device or never paralleling LEDs carry an unstated context: high-reliability industrial design fits them everywhere by default, while cost-driven toy design starts from none and adds only what testing shows is needed.[294]

### Serviceability

Maintenance exposure depends on installation geometry. A single dead pixel in a regular array is immediately visible, while an irregular cluster of light points hides individual failures, which is worth weighing at concept stage for a permanent piece nobody will service often.[412] Serviceability otherwise means designing so a failed strip can be pulled and replaced without dismantling the installation around it, since replacement rather than repair is the realistic maintenance path.[524]

## Clients and requirements

Art commissions produce requirements that are arbitrary from an engineering standpoint, such as rejecting a motor for its sound or a heatsink for its appearance, but those requirements are as binding as functional ones and act as genuine design constraints.[194] Museum clients commonly require full design information for anything installed, so they can repair it or have replacement hardware built themselves; commercial art clients, by contrast, have generally shown no interest in owning the intellectual property in the hardware.[524] Museum work can also bring conservation approval into the engineering schedule: a piece that involved cooking in a natural history collection had to be demonstrated on a surrogate specimen not to leave a permanent odour before the installation was permitted.[204]

Sensing hardware for such pieces has become inexpensive. The Panasonic Grid-EYE is an 8 by 8 thermal camera with a per-pixel thermal resolution around 0.025 degrees Celsius, cheap enough to build into a battery-powered handheld with an OLED screen and a Bluetooth link.[204]

Component selection in nearby consumer products shows the opposite economics. A teardown of radio-controlled audience wristbands found a Silicon Labs radio paired with a Silicon Labs microcontroller costing well over a dollar in thousand-off quantities, for a job of listening for a signal and flashing LEDs that a thirty pence microcontroller could do; buying a whole solution from one silicon vendor tends to carry that kind of bill-of-materials penalty.[135]

One-off installation work and volume production work also sit badly together in a small consultancy, because production jobs go quiet for months between design and manufacturing support, by which time the designer has cycled through many other jobs and lost the context.[224]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 194 | An Interview With Todd Bailey - Embedded Embrasure Engineering | https://theamphour.com/194-an-interview-with-todd-bailey-embedded-embrasure-engineering/ | April 14, 2014 |
| 204 | An Interview with Noah Feehan - Biloquistic Blinking Blush | https://theamphour.com/204-an-interview-with-noah-feehan-biloquistic-blinking-blush/ | June 23, 2014 |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 294 | Live from Serbia with Mike Harrison | https://theamphour.com/294-live-from-serbia-with-mike-harrison/ | April 13, 2016 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
