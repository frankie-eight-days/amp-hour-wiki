---
title: Via
concept: via
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A **via** is a vertical electrical connection between the copper layers of a printed circuit board, formed by a plated hole that carries a signal, power, or heat from one layer to another.[121][522] Because a via turns a horizontal trace straight down through the stack, it is the sharpest possible right-angle transition in a board — the existence of reliable vias is itself the argument that right-angle trace corners are not a general signal-integrity problem.[77] Vias also appear in integrated circuits, where they connect metallisation layers in the same way they connect copper layers on a board.[390][687]

## Fabrication

Commercial board fabrication begins by drilling every hole in the raw copper-clad panel, so that via barrels and through-hole component holes can subsequently be plated; the drilling is carried out on banks of multi-spindle CNC machines running panels in parallel.[121] Drilling is a mechanical operation charged by machine time rather than a chemical process that occurs for free alongside etching, so every hole carries a per-hole cost in the board price.[170] Designing for minimum cost therefore pushes towards the fewest vias, the fewest layers, and the highest component integration, because each is a direct line item in fabrication.[170]

### Plating and aspect ratio

Electroplating never deposits as much copper inside a via barrel as it does on the board surface, and the deficit worsens as the aspect ratio of the hole rises.[522] Thick backplanes of around four millimetres carrying 0.25-millimetre vias present a very high aspect ratio to the plating process, which is the case that drives fabricators to pulse plating.[522] Reverse pulse plating alternates a positive plating pulse with a negative pulse of several times the amplitude, at pulse lengths down to the sub-millisecond range, to distribute copper evenly in high-aspect-ratio holes.[522]

### Annular ring and drill tolerance

A fabricator's annular-ring specification is quoted alongside a hole-size tolerance of about 0.1 millimetre, and that tolerance must be added to the ring, so at small drill sizes the via pad has to be drawn much larger than the nominal ring would suggest.[224] Where a design is against a fabricator's finest rules, reducing the requested drill diameter recovers the annular ring without enlarging the pad; one such design started from a 0.25-millimetre hole.[224] A recurring footprint error in the same family is taking a datasheet's hole dimension as the pad's outer diameter rather than the drill size, producing a hole too small for the part; an 85-mil figure treated this way required the part to be filed down to fit.[172]

### Inspection limits

Automated optical inspection compares scans of the board against the Gerber data and finds shorts and open traces, but it cannot detect plating faults inside a via barrel; only a final electrical test exposes a via that did not plate all the way through.[149] A pooled prototype service running boards without final electrical test reported a fault rate of about one in forty thousand.[149] A fabricator torture-test coupon can be built as a two-inch-square board carrying 286 linear inches of exposed trace at six-mil separation together with deliberate acid traps and small vias with small annular rings, so that a panel run reveals where a fab's process actually falls over.[149]

## Types

### Through, blind, and buried vias

When layer count is driven up by a dense BGA escape, blind and buried vias are preferable to through vias because through vias consume routing space on every intervening layer.[439] A via that terminates on an inner layer of a multilayer board also defeats visual reverse engineering from photographs of the outer layers, leaving continuity buzzing with a multimeter or X-ray as the only way to follow the net.[221]

### Laser and microvias

Below a certain diameter a via can no longer be produced with a drill bit and must be laser drilled, a separate process step that many fabricators do not have in house and subcontract to another factory.[414] A laser via connects only between two adjacent layers and cannot span the whole stack; in an any-layer build, laser vias are stacked on top of one another to carry a connection from the top layer to the bottom.[681] No single drilling operation passes through a complete HDI stack-up: each layer pair is drilled and plated in its own cycle, and the resulting via segments are joined when the stack is laminated together.[681]

### Via-in-pad and HDI

Escaping a chip-scale package is outside a standard PCB process and calls for HDI: via-in-pad using 0.2-millimetre vias on a 0.1-millimetre drill, with the barrels filled and plated over, which puts prototype cost into the thousands of dollars.[395] Where the package pitch allows escape on an ordinary four-layer board, regular-size vias avoid the HDI cost step entirely.[395] One escape technique for a fine-pitch package without HDI gangs four adjacent pads of the same net together and places a single via in the middle of them, sized so its annular ring touches all four pads while solder mask separates the pads from the barrel.[395]

### Tented and hidden vias

Where the visible face of a board must stay clean, vias are tented under solder mask and then covered with silkscreen so they disappear from view.[600] The same selective mask relief is used deliberately: leaving solder mask over a via on the component side while relieving it on the opposite side makes the net contactable from the back as a probe or contact point without exposing copper on the front.[275]

## Electrical and thermal behaviour

Filling a via with solder halves its resistance, measured on a 1.2-millimetre via.[170] A ground trace run across a board behaves as a long inductive wire, so vias should be dropped from it into the ground plane at multiple points along its length rather than only at its ends.[410] A large board may carry several ground plane layers, tied together with vias so that they behave as one plane.[704] Stack-up choice interacts with via inductance: placing the power and ground planes in the centre of the stack forces every decoupling capacitor to reach them through vias running from the top surface to mid-board, adding inductance, with the compensating benefit of closer plane spacing and therefore more distributed interplane capacitance.[252]

Vias under a large thermal pad conducting heat directly into the ground plane are the standard heat path for a power part, and alternatives are used only where electrical isolation is required.[516] A via connected thermally to a copper pour is drawn with a bullseye of relief spokes rather than solid copper, visible in layout as circular segments around the via.[471]

## Routing and layout practice

Microcontrollers with remappable peripheral pins allow signals to leave the package in the order they are needed, so nets run straight out from the chip instead of requiring vias to duck under it and return on the other side.[125] At the other extreme, early autorouters constrained to route one layer horizontally and the other vertically would complete a net at the cost of roughly twenty vias to cross the board, a routing style that produces heavy radiated emissions.[128] A thousand-pin BGA with every pin used implies roughly a thousand traces and a thousand vias to be placed, multiplied by however many rip-up-and-retry passes the routing takes.[316] Long nets that must cross the whole board are best routed last, and the number of vias spent on such a net is not worth optimising once placement and grouping have been settled.[682]

Stitching a ground plane or fencing a board edge can require hundreds of vias, and placing them individually with the via tool gives uneven spacing; placing a few and then copying, pasting, or arraying them produces regular spacing with less work.[436] A via placed with the via tool picks up the net of the plane it is dropped onto, whereas a pasted copy may not inherit that net, so a copy-paste stitching array can arrive without connectivity.[436] In a planar transformer wound in board copper, a via carries the spiral down to the next layer so the winding can continue around.[432] Wiring an LED array end-to-end rather than in a conventional grid leaves room for a via directly between two adjacent pads, which allowed 0201 LEDs on a one-millimetre pitch to be routed on a two-layer board where a comparable one-millimetre-pitch matrix had needed four layers with blind vias.[697]

### Tool representation and design rules

In the PCB mode of some layout tools a via is represented as an ordinary component carrying a drill and pads, but unlike other components it can be placed directly rather than being declared in the source files and regenerated.[286] Clearance to a standard drilled via is larger than trace-to-trace clearance — in one case five mils — and where the design-rule system only supports clearance defined on the trace, the designer cannot relax it for an individual via.[482] Turning off the FR4 rendering in a layout tool's 3D viewer leaves only the copper and vias visible, an effective way for a new designer to build the mental model of how tracks on different layers connect through the stack.[512]

### Fabrication data handling

Board files edited by the manufacturer to add panel rails can come back corrupted, in one case with a via relocated onto the wrong layer, which is an argument for checking returned fabrication data rather than assuming it matches what was sent.[682] Solder mask cannot be relied on as an insulator between copper features, so routing a trace over an unused pad and covering it with mask risks intermittent faults.[395]

## Capability limits of standard processes

A domestic quick-turn fabricator offered a minimum drill hit of 8 mil with a 5-mil annular ring on two- and four-layer boards, with one-ounce outer and half-ounce inner copper — a capability adequate for ordinary vias but not for escaping small BGAs.[299] At the fine end of the standard process, a high-density module built on ordinary PCB technology rather than a substrate or interposer used 75-micron trace width and spacing with vias of 200 microns total diameter on an 81-to-85-micron drill; moving beyond that to substrate technology is a large step in price.[681]

## Non-plated processes

### Home etching and milling

A home-etched board has no plated through-holes, so every via must be formed by feeding a wire through the hole and soldering it on both sides to join the two layers.[32] On a board whose vias are wired by hand, any via sitting under a component must be soldered through before that component is placed, because it becomes inaccessible afterwards.[275] A layout destined for in-house milling should avoid vias under surface-mount parts, because each hand-made via is a wire soldered on both sides whose stub prevents the package from sitting flat and must be cut and shaved flush.[345] On desktop-milled boards, vias can also be formed by threading enamelled wire through the drilled holes and melting solder onto both ends.[686] Rivets are an alternative to soldered wire for forming vias on boards that cannot be plated through.[345]

On a milled or routed board the holes must be drilled before the surrounding copper is routed out; routing the via pad first and drilling into it afterwards tears the isolated annular ring off the substrate.[111]

### Additive processes

Additive and printed board processes handle single-sided work well but do not solve plated through-holes, drilling, or the registration problem of aligning artwork when the board is flipped, which limits them to one-off or coarse double-sided boards.[35] Conversely, an additive process that builds a board layer by layer produces blind vias inherently, because the interlayer connection is left as a cutout during printing rather than drilled through the finished stack.[505]

## Vias in integrated circuits

Integrated circuits use vias between metallisation layers in the same way a printed circuit board does, with modern parts stacking eight or nine metal layers and requiring chemical mechanical planarisation to keep each layer flat before the next is deposited.[390] Each metal layer is paired with a via layer that provides its vertical connectivity, and because a mask change costs on the order of fifty thousand dollars per layer at 14 nanometres, metal fixes are batched so that a layer already being changed absorbs as many corrections as possible.[687]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 32 | Cores, Digikey, Electronic Design - The Commercial Competitor Commencement | https://theamphour.com/the-amp-hour-32-the-commercial-competition-commencement/ | |
| 35 | An Interview with Jeri Ellsworth - The Ternary Tussle | https://theamphour.com/the-amp-hour-35-the-ternary-tussle/ | |
| 77 | An Interview with Dr. Howard Johnson - Winsome Waveform Wizardry | https://theamphour.com/the-amp-hour-77-winsome-waveform-wizardry/ | January 9, 2012 |
| 111 | DIP projects, OSHW & Trade Booths - Demonstrative DIP Dacrygelosis | https://theamphour.com/the-amp-hour-111-demonstrative-dip-dacrygelosis/ | |
| 121 | An Interview with Zach Hoeken Smith - Creative China Commorant | https://theamphour.com/the-amp-hour-121-creative-china-commorant/ | November 11, 2012 |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 149 | An Interview with Laen - Purple PCB Philosophy | https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/ | June 10, 2013 |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 221 | Warming Up To IoT - Tendentious Thermal Tools | https://theamphour.com/221-warming-up-to-iot-tendentious-thermal-tools/ | |
| 224 | Meracious Mike Manuduction | https://theamphour.com/224-meracious-mike-manuduction/ | November 12, 2014 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 275 | No One Even Missed Us? | https://theamphour.com/275-no-one-even-missed-us/ | November 19, 2015 |
| 286 | An Interview with Saar Drimer | https://theamphour.com/286-an-interview-with-saar-drimer/ | February 10, 2016 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 345 | Milling About | https://theamphour.com/show-345-milling-about/ | May 30, 2017 |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ | April 29, 2018 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ | October 7, 2018 |
| 414 | An Interview with Scotty Allen (Strangeparts) | https://theamphour.com/414-an-interview-with-scotty-allen-strangeparts/ | November 5, 2018 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 439 | Grow A Superbrain | https://theamphour.com/the-amp-hour-439-grow-a-superbrain/ | April 21, 2019 |
| 471 | An Interview with Matt Berggren | https://theamphour.com/471-an-interview-with-matt-berggren/ | December 15, 2019 |
| 482 | Shine A Light | https://theamphour.com/482-shine-a-light/ | March 1, 2020 |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ | August 16, 2020 |
| 512 | Design For Longevity | https://theamphour.com/512-design-for-longevity/ | October 11, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 682 | Your Mind Is The Tool | https://theamphour.com/682-your-mind-is-the-tool/ | November 5, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 697 | LEDs Everywhere with Tim from Mitxela | https://theamphour.com/697-leds-everywhere-with-tim-from-mitxela/ | July 8, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
