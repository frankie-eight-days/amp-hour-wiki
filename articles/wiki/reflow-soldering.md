---
title: Reflow Soldering
concept: reflow-soldering
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

Reflow soldering is a surface-mount assembly process in which solder paste deposited on a board's pads is heated until it melts, wets the component terminals and pads, and solidifies into joints, with the surface tension of the molten solder performing much of the final alignment work itself.[153][501] The process underpins essentially all volume electronics assembly, but it also scales down to hot plates, toaster ovens, and even improvised heat sources for one-off and prototype work.[226][454] Its importance to board design is such that package selection, land pattern geometry, paste volume, and thermal mass distribution are all routinely arranged around what the reflow pass can tolerate.[299][411][486]

## Mechanism

The defining physical behaviour of reflow is that molten solder pulls on whatever it wets.[237] This has two opposite consequences. On the favourable side, surface tension gives the process a self-correcting placement tolerance: a chip part such as an 0805 set down slightly off its pads is pulled back into position as the paste melts, so hand placement need not be perfect.[153] For small parts the effect is stronger still — a chip resistor or a wafer-level chip scale package only has to be placed roughly in the vicinity of its pads, and the melting solder snaps it into precise alignment.[501] With decent paste application and decent placement, even by hand, the solder itself finishes the job.[610]

On the unfavourable side, the same pull acts destructively when wetting is asymmetric. Tombstoning occurs when only one of a chip component's two terminals wets during reflow: the surface tension on that pad pulls the part upright so the other terminal lifts clear of its pad entirely.[11] Very light chip parts such as 0402 or 0201 packages have too little mass to resist the pull, so if one end wets first the part is flipped or stood on end.[237] The condition for a chip part to stay flat is that the paste at both terminals liquefies at the same moment, which is why pad geometry, paste volume, and placement have to be balanced across the two ends.[237]

Solder mask is what keeps molten solder confined to the intended pads during reflow; on a bare board without mask, such as a milled or home-fabricated one, nothing dams the solder and the process depends entirely on the flux and paste to define the joint.[233]

## Solder paste and stencils

Paste application is the foundation of the whole process: a shop that cannot lay down good paste cannot get a good reflow, no matter how much the thermal profile is adjusted afterwards.[716] In one builder's in-house assembly experience, the failure point was never the placement step but the paste and reflow — a poorly done squeegee application, compounded by paste that was itself bad, produced problem boards even when parts were placed by hand afterwards.[686]

Dabbing paste onto pads by hand instead of using a stencil puts down uncontrolled volumes, and the excess bridges neighbouring pads as soon as the board is reflowed.[273] Dabbing also becomes impractical quickly as pitch shrinks, so the finer the parts on a board, the more a stencil stops being optional.[320] The case for buying a stencil is strongest exactly where builders resist it: on boards carrying expensive or very fine-pitch parts, the stencil cost is small next to the components and it buys a first-pass result instead of a rework job.[320] For persistent paste and reflow problems in a small shop, the recommended fixes are to move from loose stencils to a framed stencil and to switch to a high-grade paste such as GC10.[716]

Solder paste has to be kept refrigerated, which is a real barrier to setting up reflow in a small lab that has no fridge and a reason some builders stay with drag soldering.[170] Paste past its date degrades rather than fails outright: joints reflow badly, look visibly poor, and give unreliable conductivity, and a run of bad results can be traced back to old paste rather than to technique.[486] Expired paste remains usable, but its effectiveness falls off progressively, so date-expired stock is a gradual quality risk rather than a hard cutoff.[486]

Flux is a consumable within the reflow pass itself: if the preheat is too long or too hot, the flux is cooked off before the solder reaches reflow temperature, and the joints have nothing left to clean the surfaces when they need it.[716]

## Thermal profile

On the way to liquidus, solder passes through a plastic region, a narrow temperature band where it is neither fully solid nor fully liquid; moving through that band too slowly is one of the ways a cold joint is produced.[716] Setting a reflow run for the least heat that will do the job protects the parts and, where the board itself forms part of the product's visible case, protects the board's appearance too — but the price of running lean is the occasional joint that does not take.[182]

How long a board needs at temperature is set by thermal mass, not by board area: two-ounce copper takes longer than standard foil, and large-bodied components take longer than small ones.[486] The worst case for a reflow pass is a board mixing very large and very small thermal mass parts, because the soak time the big parts require is long enough to damage the small ones; the way out is to split the work — two separate passes, or reflow the small parts and hand solder the large thermal mass components afterwards.[486]

A cheap reflow station's setpoint is not the board's temperature. In one case, with a station set to around 240 and 220 degrees, FR-4 boards were repeatedly blackened, showing the actual heat delivered was well above what the display claimed.[454]

## Equipment and heat sources

Reflow is achievable across a wide range of equipment, from production ovens down to a bent spoon held over a candle, which — combined with sloppily applied paste, hand-placed components, and flux dispensed from a one-millilitre syringe — was enough to make working joints.[454] Modules terminating in plain square underside pads can be reflowed on a hot plate or toaster oven.[226]

A hot plate lets a microscope sit directly over the board so the joints can be watched as they wet and the parts pull into alignment, which is impossible in an oven where the only view is through a small door window.[613] Hot-plate reflow works well for boards of ordinary low-profile surface-mount parts, but tall components develop a vertical temperature gradient between base and top, so boards with height on them are a poor fit for bottom-only heating.[613]

Bottom-terminated packages such as QFNs, whose joints sit under the body and cannot be reached with an iron, can be attached without an oven by preheating the board, flooding the area with liquid flux, and applying a hot air pencil until the part settles onto its pads.[158] Boards with large copper pours sink heat away from the joint faster than a hot air pencil can supply it, so the board should sit on a preheater for a minute or two and come up to roughly 200 degrees before any localised reflow is attempted; a bench preheater for this costs on the order of a couple of hundred dollars.[158]

In a small-batch assembly shop the reflow pass, not the placement machine, is sometimes the slowest step, so job throughput depends on which processes a given board needs rather than on placement speed alone.[243]

## Substrates and board types

FR-4 tolerates reflow heat shock better than cheaper laminates because the adhesive bonding the copper foil to the substrate is more robust, which matters when boards are sourced as blank copper-clad stock from low-cost suppliers.[454] Very thin prepreg-only boards can be run through standard pick-and-place and reflow by taping them down to a piece of ordinary FR4 as a carrier with kapton tape; no vacuum bed or exotic fixturing is needed because the material wants to stay flat.[412] Kapton-substrate flexible boards, by contrast, curl under their own internal tension as soon as they are unrestrained, which makes them awkward to place and reflow.[412] Rigid-flex construction keeps assembly cost down by letting all the parts sit on the rigid sections, since placing and reflowing a rigid board is always easier than working directly on flex, which needs stiffening underneath.[415]

Reflow also works on inkjet-printed conductive traces, using either leaded or lead-free alloys, with leaded solder giving the better result in practice; printed traces tolerate reflow even on a paper substrate, so the assembly step is not limited to conventional laminates.[260]

## Package-specific behaviour

### QFN and bottom-terminated parts

The large centre ground pad on a QFN is the hard part of the joint, because getting enough heat into that thermal pad for the solder under it to reflow properly is difficult compared with the perimeter leads.[501] Too much paste on the centre pad floats the package on a pool of molten solder, letting it settle with one side higher than the other and leaving perimeter leads unconnected.[501] Hand reflow success rates differ sharply by package: roughly a fifty percent failure rate on QFNs against about an eighty percent success rate on wafer-level chip scale packages, a gap large enough to justify avoiding QFNs in a design.[501] Wafer-level chip scale packages are easier to reflow than their size suggests, because the package is almost all die with very little thermal mass, so it comes up to temperature quickly and the joints reflow readily.[501]

Package choice also decides whether a design can be sold as a user-assembled kit: once a board carries QFN parts, the buyer has to reflow rather than hand solder, which rules out the kit format for most customers.[107]

### Grid arrays and modules

Reballing a grid-array part uses a stencil to deposit discrete solder spheres onto the package; heating then lets each deposit draw up into a ball, and the process depends on the balls releasing from the stencil rather than sticking to it.[195] BGA assembly is within reach of a first-time builder — a self-taught developer moving into hardware designed and successfully assembled BGA boards on the first attempt.[395] On one such design, Luke Valenty narrowed the BGA's outer row of pads to 0.1 mm and elongated them to 0.35 mm by 0.1 mm, preserving roughly the original pad area so the balls still wet and reflow properly while freeing routing channels between them.[395]

A module that terminates in plain square pads on its underside rather than solder balls attaches with ordinary paste and reflow, but the joints are hidden under the body and cannot be inspected visually afterwards; putting the pads underneath optimises for size and needs no ball array, since paste on flat square pads reflows into the joints directly.[226] Castellated edge holes give a part two attachment routes: they can be pasted, placed and reflowed like any surface-mount part, or, because the hole spacing matches 0.1 inch headers, pin headers can be soldered into them instead.[319] Supercapacitors are available in a 1206 surface-mount body, so CMOS and backup-power storage can go through pick-and-place and reflow as an ordinary part instead of forcing a through-hole coin cell or round leaded can into the build.[408]

## Double-sided assembly

Some parts are rated to survive only a single reflow pass, which constrains double-sided assembly: such a part has to be placed on whichever side goes through last, and everything else must be arranged around that restriction.[411] On the second pass the first side is inverted, and heavy parts such as large inductors and aluminium electrolytics will drop off their pads once the solder remelts unless they were glued down.[411] Glue layers in board CAD are a legacy of an era of heavier components; as parts have shrunk the need has receded, and a 1206 that would once have been at risk of dropping now generally stays put.[411] Heavy surface-mount parts such as transformers remain poor candidates for a second-side reflow — they need gluing down, and even then generally have to be touched up or fitted by hand afterwards.[716] Parts falling off the inverted first side is preventable at design review rather than on the line, which is what a manufacturability review before the build provides.[716]

## Failure modes

Getting the land pattern wrong produces the classic reflow placement defects: parts stand on end as tombstones or roll onto their sides as billboards while the solder is molten.[299] Chip passives are occasionally seen to flip completely over during the reflow pass, ending up inverted on their pads — a defect observed in production without a settled explanation.[299]

A tombstoned part does not always announce itself as a dead board. On an early Arduino Uno, resistor R1 below the crystal was found tombstoned with its left terminal making no contact with the land pad at all, yet the board still functioned normally, and the defect was only caught by inspecting under a stereo microscope.[11]

Substituted parts with cheap plastic bodies can look fine on arrival and then be destroyed by the reflow pass: boards assembled in Shanghai came back with surface-mount headers whose plastic had melted, leaving every pin at a distorted angle.[239] Hand soldering will not expose such a part, because an iron heats one pin at a time and the body never reaches full temperature; the same part fails as soon as the whole board is brought up together.[239]

A bare PCB used as a reflow heating element is not reusable: at around 200 degrees Celsius, hot enough for solder to reflow, the solder mask discolours and degrades, with damage visible after about five cycles.[663]

## Scale and economics

For a low-part-count one-off board, the setup time for paste dispensing can exceed the time it would have taken to hand solder the whole thing, which is why hand assembly still wins at the smallest scale.[233] Fine-pitch packages nonetheless push even one-off builders toward paste and reflow because some parts are simply not offered in anything else; a TSOP can be drag soldered by hand, but reflow is the route that gets it right first time.[170] Kapton stencils with hot-plate reflow are workable at very small volumes, but the economics change abruptly as volume rises, at which point handing the work to a small-batch assembly service is the sensible move.[255] OSH Stencils grew out of a first reflow project where the cost of a conventional stencil was out of proportion to a hobby-scale board, prompting a search for a cheaper way to produce them.[320]

A reflowed board is visibly better than a hand-soldered one: careful hand work under a microscope with enough time can approach reflow quality but does not match it.[176] Bringing assembly in house trades a vendor who can be held accountable for defects against owning the entire paste and reflow process, including the diagnosis when boards come out wrong.[686] Shenzhen placement services buy the stencil and hand-assemble and reflow small batches, turning out three to five boards for a technician's day wage — roughly an order of magnitude cheaper than standing up the equivalent capability in house.[341] High-grade solder paste has also become more expensive and harder to get on demand, with a tube that used to cost about $125 now running around $200.[716]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 11 | Ardui...no Dave This Week? | https://theamphour.com/the-amp-hour-11-ardui-no-dave-this-week/ |  |
| 107 | An interview with Tony Long - Millimeter Microwave Magician | https://theamphour.com/the-amp-hour-107-millimeter-microwave-magician/ | August 5, 2012 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 158 | Hyperloop, Upverter and Soldering - Unbelievable USB Ustulater | https://theamphour.com/the-amp-hour-158-unbelievable-usb-ustulater/ | August 12, 2013 |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 182 | Manufacturing By Wire And Skipping Testing - Calefacient Cuculine Cash | https://theamphour.com/182-manufacturing-by-wire-and-skipping-testing-calefacient-cuculine-cash/ | January 27, 2014 |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ | April 21, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 233 | Glass and Gongkai GSM - Unzymotic Ursidae Upbuilding | https://theamphour.com/233-glass-and-gongkai-gsm-unzymotic-ursidae-upbuilding/ | January 20, 2015 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 243 | An interview with Macrofab - Macro Manufacturing Mechanization | https://theamphour.com/243-an-interview-with-macrofab-macro-manufacturing-mechanization/ | March 31, 2015 |
| 255 | Inspirations and Aspirations - Recanting Rocket Rationale | https://theamphour.com/255-inspirations-and-aspirations-recanting-rocket-rationale/ | June 24, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 273 | Part Choice Triathlon | https://theamphour.com/273-part-choice-triathlon/ | October 28, 2015 |
| 299 | An Interview with Jonathan Hirschman of PCB:NG | https://theamphour.com/299-an-interview-with-jonathan-hirschman-of-pcbng/ | May 18, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 320 | An Interview with Brent of OSHstencils | https://theamphour.com/320-an-interview-with-brent-of-oshstencils/ | October 20, 2016 |
| 341 | All the way with DLJ | https://theamphour.com/341-all-the-way-with-dlj/ |  |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 486 | Medical Kits, They're The Future | https://theamphour.com/486-medical-kits-theyre-the-future/ | March 29, 2020 |
| 501 | Discussing the Open Source PDK with Tim Ansell | https://theamphour.com/501-discussing-the-open-source-pdk-with-tim-ansell/ | July 19, 2020 |
| 610 | Picking a Pick and Place Pickiness | https://theamphour.com/610-picking-a-pick-and-place-pickiness/ | November 20, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 663 | Motors on PCBs with Carl Bugeja | https://theamphour.com/663-motors-on-pcbs-with-carl-bugeja/ | March 25, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 716 | Electronics Manufacturing History with David Ray | https://theamphour.com/716-electronics-manufacturing-history-with-david-ray/ | February 25, 2026 |
