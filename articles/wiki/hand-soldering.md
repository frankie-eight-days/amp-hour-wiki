---
title: Hand Soldering
concept: hand-soldering
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**Hand soldering** is the manual assembly of electronic components onto a printed circuit board, in which each joint is formed individually with a soldering iron rather than by a reflow oven, wave, or selective soldering machine.[329][239] It remains a standard method for prototype construction, rework, and small-batch production, and it persists inside volume manufacturing wherever a part or process step resists automation.[407][366] The technique trades directly against machine assembly: it is slower per joint, but requires no stencil, fixture, or machine setup, and it accommodates parts that reflow processes cannot.[259][558]

## Technique

The basic motion is to heat the joint and feed solder into it: the iron touches the pin and solder is applied to both pin and pad together, rather than melting solder onto the tip and carrying it over to the joint.[329] For fine-pitch parts, the working method is to tack two opposite corners first so the part cannot move, then drag the iron along the remaining pins in a single pass.[628][415] Small leadless and fine-pitch parts are easier to place than their dimensions suggest, because the parts are light enough that the surface tension of the molten solder pulls them into alignment with the pads.[183] That self-alignment effect has a limit, and relying on it as a general technique rather than as a helpful tendency is where it stops working.[183]

The speed-versus-quality trade is the one discovered earliest: soldering as fast as possible produces joints that have to be reworked afterwards.[459] Practiced operators describe consistent requirements — substantial practice, steady hands, and bracing the hand against a fixed surface to damp shake.[489] Experienced solderers also use noticeably less flux than beginners expect, because excess flux leaves the board in a mess.[489] With adequate magnification, fine-pitch hand soldering is a learnable skill that becomes routine with practice rather than a knack.[628]

## Optical aids and materials

Fine hand assembly calls for magnification together with thin solder — around a third of a millimetre in diameter — so that each joint receives only the alloy it needs.[364] Adequate lighting can substitute for magnification for some work, which is worth establishing before investing in an optical system.[508]

## Solder paste and reflow in hand assembly

Hand assembly frequently mixes iron work with solder paste and reflow rather than treating them as alternatives. A practitioner fully comfortable with an iron may still use paste, stencil, and reflow for essentially all surface-mount work, which is the more reliable default; on one such practice, Luke Valenty uses paste and stencils almost exclusively for surface-mount assembly.[395] The two methods also combine within a single board: the stencil deposits the paste and most parts are placed for reflow, after which a part such as a quad flat pack is finished by hand with a single drag pass.[415]

### Applying paste without a stencil

Applying paste by hand is a matter of restraint — less than instinct suggests — since excess paste can be wicked away afterwards, whereas solder bridges have to be fixed.[259] A stencil is not always necessary: for an integrated circuit, a single line of paste along each side of the package is sufficient, and a small two-sided package takes two lines applied in a couple of seconds.[259] It is a board full of discrete passives that makes a stencil worth having, because each pad must then be dosed individually.[259] Paste dabbed on by hand and then reflowed bridges badly, which is the practical argument for waiting the couple of days a stencil takes to arrive.[273] Because forgetting to order the stencil is the usual failure, the stencil order belongs in the same step as the parts order rather than as a separate decision.[320] On one project, hand-applied paste without a stencil produced a measured failure rate of four non-working boards out of five, which motivated a package change.[717]

### Reflow heat sources

For a double-sided board, a hot air tool handles the second side, avoiding a second trip through an oven that would remelt the joints on the first.[259]

## Component and board constraints

Some parts survive an iron but not an oven. A poorly made connector melts and distorts during reflow, while hand soldering leaves it intact because only one pin is heated at a time and the connector body never reaches temperature.[239] This restriction is sometimes explicit in the datasheet: a through-hole connector rated only for hand-soldering temperatures will melt in an oven regardless of the thermal profile used.[558] Heavy surface-mount parts such as transformers may need to be glued down and may not reflow acceptably at all.[716]

A board mixing very large and very small thermal masses is the hard case for reflow, because the soak the large parts require is long enough to damage the small ones; the solution is to split the job, either into two passes or by reflowing the small parts and hand soldering the large ones afterwards.[486]

Geometry creates further constraints. A via underneath a component must be soldered before the part is placed, since it cannot be reached afterwards.[275] A pad under the body of a part is the general form of that problem: perimeter pads can be reached with an iron, while the centre pad cannot.[96] Soldering onto a milled board is harder than onto a fabricated board because there is no solder mask to contain the joint.[494]

Difficulty tracks pitch rather than package family: a half-millimetre-pitch quad flat pack soldered without a board is harder to manage than a millimetre-pitch ball grid array.[120] Component size crosses a threshold where the technique stops scaling — after building a few boards with the smallest common passives (0201), the next size up (0603) stops feeling difficult at all.[226] Around that size the limit is usually rework rather than placement: parts can still be placed but cannot reliably be fixed afterwards by hand.[686]

Some hand work has no alternative and no shortcut. Terminating a multi-hundred-pin connector by hand takes one to two hours per connector.[496] Hand soldering also persists inside sophisticated products: ultrasound transducers are made by cutting a piezoelectric tile and hand soldering electrodes onto the individual pieces.[407]

## Design for hand assembly

Assembly method feeds back into design decisions. A useful voluntary constraint is that the board should be assemblable with an iron, choosing a leaded package over a ball grid array wherever the choice exists; on the HackRF project, Michael Ossmann holds his designs to that standard.[265] Changing a package for this reason is a real design decision: moving from a ball grid array to a leadless quad package made one board something its designer could solder and, more importantly, desolder without help.[717] Spacing parts out for access rather than packing them tightly is a legitimate optimisation when the board will be assembled and reworked by hand.[285] Newcomers often choose larger passives specifically so they can hand solder, which is understandable and also the habit that later has to be unlearned.[718] The mirror-image mistake is made by experienced designers: parts placed tightly on screen turn out to leave no room to solder a flying lead onto a specific point during bring-up.[718]

Refusing packages that cannot be hand soldered is no longer a workable position, because it removes a large fraction of the parts on the market.[259] For modules aimed at people new to the process, castellated edges are harder for a beginner to attach than plated holes.[395] On prototypes, designing in proper wire-to-board connectors instead of soldering wires directly to pin headers pays for itself immediately in rework.[534] Adapter boards that convert a surface-mount package to a through-hole footprint are supplied in panels covering many packages at once, so almost any part can be brought onto a breadboard by snapping off the adapter and soldering on header pins.[18]

At the production boundary, through-hole parts on an otherwise surface-mount board impose a keep-out: surface-mount parts within about ten millimetres of the through-hole pins prevent a selective soldering head from reaching, forcing hand work.[447] That single process constraint propagates backwards into layout, changing spacing and placement decisions across the board.[447]

## Speed, scale, and the transition to machine assembly

Hand assembly is slower than machine placement but not impossibly slow: tinning one pad of each position and then placing parts reaches roughly one part every couple of seconds.[428] What limits a session is the operator rather than the method — eye strain and hand cramp arrive well before the technique fails.[428] For a run of ten or fifteen evaluation units, the calculation usually comes out against hand assembly even with a stencil; the standard pattern is to build the first unit by hand to prove the design works and have the rest assembled.[434]

The transition point is recognisable in hindsight. On the early DIY Drones work, Chris Anderson's batch of a couple of hundred boards hand-soldered at a kitchen table ended the practice and moved the work to an assembly house.[105] Hundreds of units bring a second problem beyond assembly: every board must be verified, which is the point at which designing automated test fixtures starts to pay.[500]

Capability gaps in equipment can decide the whole approach. An assembly machine that cannot feed tubes or trays leaves those parts to be done by hand, which often means sending the entire job out instead.[148] A placement machine that still requires parts to be sorted or aligned by hand is not automation, and the honest comparison for such a machine is hand soldering rather than a production line.[191]

## Production economics

Small kit production can reasonably be hand-built locally by one person, avoiding the purchase of reels and machine setup entirely.[1] At volume, local hand assembly stops being competitive, and the reason is structural: low-cost factories are also hand soldering, simply with lower labour costs and more practice.[366]

When a batch goes wrong, hand replacing one part can be cheaper than scrapping boards that already carry the value of every other component on them.[279] The counterweight is that rework itself carries risk, so scrapping is sometimes the cheaper decision despite appearances.[279]

## Appearance

A hand-soldered prototype looks visibly worse than a reflowed board, although careful work under a microscope closes most of the gap.[176]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 1 | What's In A Name? | https://theamphour.com/1-whats-in-a-name/ |  |
| 18 | Transistor Types and Where To Get Electronic Gear | https://theamphour.com/the-amp-hour-18-transistor-types-and-where-to-get-electronic-gear/ |  |
| 96 | Senseless Saccadic Shemozzle | https://theamphour.com/the-amp-hour-96-senseless-saccadic-shemozzle/ |  |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 120 | Prototyping, Machining & Accelerators- Mugwumps Mulling Milling | https://theamphour.com/the-amp-hour-120-mugwumps-mulling-milling/ | November 4, 2012 |
| 148 | Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood | https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/ | June 3, 2013 |
| 176 | Funding New/Manufacturing Old Projects - Radical Robotic Requisition | https://theamphour.com/176-funding-newmanufacturing-old-projects-radical-robotic-requisition/ | December 16, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 259 | No More Naming | https://theamphour.com/259-no-more-names/ | July 21, 2015 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 273 | Part Choice Triathlon | https://theamphour.com/273-part-choice-triathlon/ | October 28, 2015 |
| 275 | No One Even Missed Us? | https://theamphour.com/275-no-one-even-missed-us/ | November 19, 2015 |
| 279 | Merry Keyzermas! | https://theamphour.com/279-merry-keyzermas/ | December 22, 2015 |
| 285 | Something's Serially Wrong Here | https://theamphour.com/285-somethings-serially-wrong-here/ | February 3, 2016 |
| 320 | An Interview with Brent of OSHstencils | https://theamphour.com/320-an-interview-with-brent-of-oshstencils/ | October 20, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ |  |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 366 | Loopback | https://theamphour.com/366-loopback/ | November 5, 2017 |
| 395 | An Interview with Luke Valenty | https://theamphour.com/395-an-interview-with-luke-valenty/ | June 3, 2018 |
| 407 | Gregory Charvat and Three New Companies | https://theamphour.com/407-gregory-charvat-and-three-new-companies/ | September 16, 2018 |
| 415 | Ergs Per Second | https://theamphour.com/415-ergs-per-second/ | November 11, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 447 | Voltnuts for Flashlights | https://theamphour.com/447-voltnuts-for-flashlights/ | June 16, 2019 |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 486 | Medical Kits, They're The Future | https://theamphour.com/486-medical-kits-theyre-the-future/ | March 29, 2020 |
| 489 | An Interview with Jack Ganssle (2nd) | https://theamphour.com/489-an-interview-with-jack-ganssle-2nd/ | April 19, 2020 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 496 | Drab Olive | https://theamphour.com/496-drab-olive/ | June 14, 2020 |
| 500 | Two and a Half Orders of Magnitude | https://theamphour.com/500-two-and-a-half-orders-of-magnitude/ | July 12, 2020 |
| 508 | Doomed To The Flatland | https://theamphour.com/508-doomed-to-the-flatland/ | September 13, 2020 |
| 534 | Firmware Update Capabilities | https://theamphour.com/534-firmware-update-capabilities/ | March 14, 2021 |
| 558 | Toasted Marshmallow Connectors | https://theamphour.com/558-toasted-marshmallow-connectors/ | September 19, 2021 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
| 716 | Electronics Manufacturing History with David Ray | https://theamphour.com/716-electronics-manufacturing-history-with-david-ray/ | February 25, 2026 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
