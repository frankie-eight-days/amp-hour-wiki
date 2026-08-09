---
title: Solder Paste
concept: solder-paste
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Solder paste is a slurry of tacky flux and powdered solder metal, applied to a board's pads before components are placed; its tackiness is load-bearing, because it holds every placed component in position until the joint is formed.[411] Paste application is the foundation of the whole assembly process, in the sense that without a good application there is no good reflow and no amount of tuning afterwards will recover it.[716] Stated as a priority order, paste is by far the most critical step: however good the placement is, bad paste produces bad boards, which inverts where most beginners direct their attention.[458]

## Physical behaviour

Paste is shear-thinning, which is why technique matters. Good paste becomes thinner while it is being spread and firms up again once the stroke stops, and that recovery is what produces the tack that holds parts, so components should not be placed onto paste that is still liquid.[320] The tack then does mechanical work during placement: the board flexes as the nozzle presses a part down and springs back as it releases, and it is the tack of the paste that keeps the component from being flicked off the board.[415]

Surface tension in the molten metal relaxes the demands on everything upstream. Placement accuracy requirements are more relaxed than they appear, because parts wiggle back into position as the solder melts, so for ordinary passives it is the tolerance of the paste deposit rather than the placement that matters.[153] The same effect makes ball grid array work more forgiving than its reputation suggests, since the package is pulled into position by surface tension and a cheap mylar stencil with the correct paste volume is enough to make it work.[291]

Solder mask contains the result. For a fine-pitch quad flat pack there is no need to place paste on each pad individually — laying a single line of paste across the whole row works, because the mask and surface tension sort it out during reflow without bridging.[259] This is what solder mask is for, and it is also why paste volume matters more than precision: put too much on and the mask cannot prevent bridging however well the stencil was aligned.[153]

## Shelf life and storage

Expired paste does not stop working outright; it degrades, so that reflow gets progressively worse, joints look bad and conductivity suffers, which makes the cause hard to identify because nothing fails cleanly.[486] Bad paste nonetheless has a recognisable physical signature, caking into something with the texture of material that could be peeled off a fingernail; it can sometimes be rescued on a hot plate with extra flux, but doing so is not good business.[716]

The cost of getting this wrong can be substantial. In one case, two months of boards on which nothing reflowed properly were traced to old paste kept out of frugality, with yields over that period of around forty percent; borrowing fresh paste fixed everything immediately.[458] Using long-expired paste is a recurring error even among experienced people — five-year-old paste in a fridge is not usable stock, and the expiration dates on these products are firm rather than advisory.[628] The resulting discipline is to throw paste out regularly and buy new, because there are many places in electronics where being frugal pays and this is emphatically not one of them.[686] The operating rule is to use fresh paste every time and to check the stencil alignment carefully, since those two factors dominate the outcome regardless of what the rest of the line is doing.[458]

Printed paste also has a working window once it is on the board: the assembly needs to reach the oven within a few hours, so populated boards cannot be left sitting overnight waiting for the rest of a panel to be finished.[337]

The most sophisticated factories treat paste as a tracked material like any component, recording which lot it came from, when it was taken out to come up to temperature, and the hours during which it was used, all against the boards it was used on.[451]

## Grades and selection

One particular paste is named repeatedly by people who assemble boards as having changed their results, with the catch being packaging: it is sold in tubes of five or six hundred grams, so the cost per gram is low but the entry cost is not.[473] The same product is reported to remain usable well past its rated one-year life, which is the exception that proves the rule about fresh paste rather than a licence to keep any paste indefinitely.[716] The combined recommendation for anyone struggling with reflow is accordingly to change two things at once — move to a framed stencil and switch to known-good paste — since those two changes address most of what goes wrong before the oven.[716]

## Stencils

A stencil is exactly what the name suggests, a mask ensuring paste lands only on the copper pads, whose purpose is to put the right amount of paste in the right places consistently rather than with the inconsistency of dabbing it on by hand.[320] Stencils stopped being a cost barrier once fabricators began cutting them from mylar in seconds and including them with the boards, which is what made stencilled application practical for one-off prototypes.[79]

### Aperture quality and clogging

Aperture quality has a direct effect on release: a smooth, almost flame-polished interior lets paste leave the aperture cleanly, while a jagged cut edge holds onto it, and clogging with old paste is the main thing that degrades a stencil over its life.[320] Clogging works by narrowing the aperture, which reduces the volume of paste deposited and produces exactly the defects associated with too little paste, tombstoning among them; a stencil that once worked can therefore start producing faults without anything else changing.[320]

### Aperture modification

Production engineers routinely modify individual apertures rather than accepting a defect, so that if one component consistently tombstones they will have a stencil made with a larger opening at that pad to give it more paste.[320] The reason the adjustment is needed is mechanical: an automated squeegee makes one pass at nominally constant pressure, and pads earlier in the stroke can absorb a clump of paste, leaving later pads slightly starved, so opening those apertures compensates for the position rather than for the pad.[320]

## Application technique

The technique rule for squeegeeing is counterintuitive: use the smallest pressure that will distribute paste evenly across the stencil in a single pass, because pressing harder makes the result worse rather than more complete.[320] The traditional advice to squeegee in one single stroke is likewise worth testing rather than obeying — one practitioner gets better results with a stroke down, a stroke back up, and a final pass at a sharp angle to scrape the surface clean.[473]

A workable home stencilling setup surrounds the board with spare boards of the same thickness so the surface is level, tapes the stencil down along one edge, lays a bead of paste along the top and squeegees with a stainless blade.[473] Stated at its simplest, the method is a blank board to sit the work in, the stencil on top, and an old credit card to draw the paste across, with getting the surrounding surface flush with the board being the part that matters.[561] For very small boards even the stencil can be improvised, using two strips of tape either side as shims to set the thickness and then skimming a credit card along them to leave an even layer.[454]

The accessibility argument for paste is that people assume surface-mount work requires a soldering iron, which is genuinely hard, and are surprised how much easier paste methods are; demonstrating a reflow over a candle flame makes the point that the process is more approachable than the equipment implies.[454]

## Dispensing equipment

At the low-cost end of dispensing, an air-compressor syringe dispenser is likely to fail quickly because of its seals, whereas a mechanical lever press gives slow controlled dispensing calibrated to the hand and has nothing to wear out.[170] At the other end, dispensing machines plot paste dot by dot with an XY head rather than squeegeeing it through a stencil, achieving high accuracy at a cost of tens of thousands of dollars.[79]

Assembly houses have been moving from stencils to paste printers for speed rather than quality, because a printer removes the wait for a stencil to be made and shipped, which matters most for high-mix work where fifteen designs in a day would otherwise need fifteen stencils.[320] Component size feeds directly into assembly price in the same way: smaller parts cannot be jet-printed and require finer, more expensive stencils, which is one of the specific ways that going outside the normal envelope starts to incur cost.[411]

## Print defects

The dominant error in hand application is using too much paste. Only a small amount is needed to make a connection, and excess is what produces bridges, so the instinct to be generous is precisely wrong.[291] Under a ball grid array that error becomes serious, because the resulting shorts sit underneath the package where they cannot be seen and will never be found by inspection.[291]

Board features can remove paste as well as add it. A via inside a pad wicks paste away down the hole by capillary action, starving the joint of solder, which is the hidden cost of putting vias in pads when there was no room to route them out.[96]

Tombstoning has several independent causes, so diagnosing it means checking all of them: a mismatch between the part, the paste volume and the pad geometry; the reflow profile itself; and thermal asymmetry where one pad connects to a ground plane and therefore heats and cools differently from the other.[237]

Gross print failures are also possible and can be mistaken for something else. In one case an entire region of a panel came out unpopulated, which looked like a placement problem and turned out to be paste never having been scraped across that part of the panel at all.[419] At the small scale, paste application can dominate the yield of a hand-built board outright: one builder obtained a single working board out of five, which was the reason for moving the design from a ball grid array to a leaded package that could be inspected and reworked.[717]

## Boards without solder mask

On a milled board there is no solder mask to contain the paste, so the process depends on flux behaviour alone and bridging is much more likely; by the time the machine is set up to dispense, hand soldering the board would often have been faster.[233]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 79 | Ludibrious Luxating Layout | https://theamphour.com/the-amp-hour-79-ludibrious-luxating-layout/ | January 23, 2012 |
| 96 | Senseless Saccadic Shemozzle | https://theamphour.com/the-amp-hour-96-senseless-saccadic-shemozzle/ |  |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 233 | Glass and Gongkai GSM - Unzymotic Ursidae Upbuilding | https://theamphour.com/233-glass-and-gongkai-gsm-unzymotic-ursidae-upbuilding/ | January 20, 2015 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 259 | No More Naming | https://theamphour.com/259-no-more-names/ | July 21, 2015 |
| 291 | Artificially Intelligent Party Platform | https://theamphour.com/291-artificially-intelligent-party-platform/ | March 16, 2016 |
| 320 | An Interview with Brent of OSHstencils | https://theamphour.com/320-an-interview-with-brent-of-oshstencils/ | October 20, 2016 |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 419 | Feels over reals | https://theamphour.com/419-feels-over-reals/ | December 9, 2018 |
| 451 | An Interview with Scott Miller (2nd) | https://theamphour.com/451-an-interview-with-scott-miller-2nd/ | July 21, 2019 |
| 454 | An Interview with MG (Mike Grover) | https://theamphour.com/the-amp-hour-454-mike-grover/ | August 11, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 486 | Medical Kits, They're The Future | https://theamphour.com/486-medical-kits-theyre-the-future/ | March 29, 2020 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 716 | Electronics Manufacturing History with David Ray | https://theamphour.com/716-electronics-manufacturing-history-with-david-ray/ | February 25, 2026 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
