---
title: Radio Frequency
concept: radio-frequency
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

**Radio frequency** (RF) is the portion of electronics practice concerned with signals whose frequency is high enough that physical dimensions, parasitic elements and return-current paths govern circuit behaviour.[185][533][476] The boundary between low-frequency and high-frequency design is not sharply defined and sits somewhere between 10 and 100 MHz: below about a megahertz the treatment is straightforward, while above about 100 MHz every aspect of a design has to be reconsidered—roughly the same threshold at which a circuit starts to radiate appreciably.[185] The field matters beyond radio products themselves, because the spectral content of a digital signal is set by its transition rate rather than its clock rate, so digital designers are engaged in radio-frequency design whether they recognise it or not.[165]

## Defining behaviour at radio frequency

The behaviour that changes with frequency is where the return current flows. At low frequency the return current spreads through the whole ground plane and the plane can be treated as an equipotential; as frequency rises the current takes the path of least inductance and concentrates directly beneath the forward trace to minimise the loop area. The underlying principles are unchanged, but this detail governs high-frequency layout.[185]

Physical length is the governing variable at radio frequency in a way it is not at low frequency. A comb-line filter works because a conductor shorted to the body at exactly the right length forms a shorted half-wave resonator that generates a field, with each comb element acting as a resonator coupled to that field and to its neighbours; the intuition for such structures comes from knowing the antenna size at the frequency of interest, since anything a large fraction of a wavelength long will affect the signal.[533]

Parasitic effects dominate at radio frequency in a way that changes how components must be regarded: nothing behaves as its schematic symbol suggests, and every parasitic element matters. This is the same lesson that makes simulation models useless when they omit the path through which current actually flows.[476]

The description of radio-frequency work as black magic is misleading, since the physics is the same physics operating throughout electronics; what the field requires is an appreciation of the physical properties in play, and a great deal can be done without any advanced qualification in electromagnetics.[492] Radio-frequency and signal-integrity knowledge also sit adjacent to physics research rather than to conventional circuit design: laser-physics work amounts to electromagnetics combined with quantum mechanics, and the modelling skills transfer directly into radio design, which is why some practitioners arrive at radio frequency first rather than last.[718]

## Relationship to digital design

Radio-frequency work is in one respect easier than fast digital work, because a radio signal occupies a single fundamental frequency while a fast digital edge is broadband and spreads energy across the spectrum; the difficulty on modern boards is therefore concentrated in fast digital rather than in the radio section.[260] What determines the spectral content of a signal is the transition rate rather than the clock rate, which makes digital designers radio-frequency designers whether they recognise it or not.[165]

The characteristic mixed-signal problem is a receiver looking at signals around −100 dB sitting on the same board as a clock. A 32 MHz clock sounds harmless until its rise time is considered: an edge of 100 picoseconds carries content out to roughly 3 GHz, which lands directly on a 2.5 GHz receive band. The design responses are to use the lowest clock frequency the design can tolerate and the longest rise time that still works, and to treat signal integrity seriously once clocks pass about 30 MHz in a mixed-signal board.[252]

Design rules that work at one speed do not scale. A two-layer development board whose power distribution wanders across the board is entirely adequate for an 8 MHz processor and is built that way deliberately to hit a low price, but the same rules do not survive past 10 or 20 MHz, while a modest set of additional rules will carry a design to around 100 MHz.[252]

## Spectrum, bands and propagation

The licence-free bands are where most product radio work happens, principally 2.4 GHz and the sub-gigahertz bands around 900 MHz, the latter favoured in building automation for its better coverage. In such systems the radio is generally not the hard part; the networking is, because users who already struggle with a home network will not manage a network of light fittings.[245]

Sub-gigahertz spectrum allocation is regional, with long-range links using bands from around 160 MHz up through 315, 433, 868 and 915 MHz depending on jurisdiction. A product intended for several markets must therefore either carry variants or use a chipset whose band is set by a register.[376]

Frequency selection changes propagation behaviour in ways that matter for a specific application: video links operate at 1.3, 2.4 and 5.2 GHz, and the bands bounce differently around obstacles, so a link that works in the open may drop out when the path bends around a corner.[105] Higher-frequency cellular service is inherently short range, on the order of hundreds of metres, which makes it incompatible with satellite delivery and forces dense ground infrastructure.[462]

Radio does not work underwater, being absorbed within a couple of feet, which is why underwater links use sound instead. That constraint can be designed around by moving the processing to the sensor: compressing a high-bandwidth video feed down to a few bytes of results allows the data to travel kilometres over an acoustic channel with bandwidth comparable to an early telephone modem.[517]

## Design practice

### Ground and return paths

The concept of ground is of little use at radio frequency, and low-noise performance does not follow from grounding practice; Eli Hughes makes the point by asking where ground is on a satellite, which has none and still achieves low-noise operation, summarising the idea as "ground is where the potatoes live".[511]

Practices imported from low-frequency analog design can actively harm a radio design. A cutout in a ground plane intended to steer low-frequency noise becomes an antenna once a radio-frequency signal meets it, so converter guidance written for low frequencies and radio-frequency practice cannot both be followed on the same board without resolving the contradiction.[457]

### Shielding and stack-up

Radio sections in high-performance instruments are physically partitioned, with machined aluminium enclosures over each functional block on both sides of the board, specifically to stop the front-end amplifier coupling to the local oscillator or to neighbouring stages; an instrument of that class can contain twenty-five or more separately shielded blocks in a traceable signal chain.[304]

Shielding leaks in predictable ways: energy at radio frequency couples onto the ground and supply wiring leaving a shielded enclosure and re-radiates from them as a passive radiator, so a design that relies on attenuation with distance rather than on containment is relying on a real but incomplete mechanism.[612]

Stack-up is one of the few areas a designer can ignore for an entire career unless the work demands it, and radio frequency is one of the cases that does demand it, alongside high-speed signalling, non-standard board thickness and heavy copper for high-current designs.[494]

### Electromagnetic compliance

Compliance outcomes cannot be predicted with confidence even by experienced practitioners, because the interactions are numerous: the cable with the chassis, the chassis with the board, the clocks with each other, and the ground plane itself radiating when current flows across it between two connectors, since its inductance produces a voltage difference between the two sides of the board. Good stack-up design and filtering on every power and signal line improve the odds without settling the result.[645]

Confidence about compliance follows a curve with experience. Someone who knows nothing expects to fail; someone who has learned a grounding technique and filtered every line expects to pass; someone who has taken a hundred products through full testing accepts that the outcome cannot be predicted, because a pragmatic product cannot always have a metal chassis, 360-degree bonding to its connectors or shielded cables.[645]

Anechoic chambers used for emissions work are expensive because of what lines them rather than their size: the absorber cones are normally too short to work alone, so the room must also be lined with ferrite tiles. A chamber large enough for cones of about 2.2 metres does not need the tiles at all, which is what makes such a chamber unusual as well as large.[61]

## Components and circuits

PIN diodes present a low impedance to radio-frequency signals when a direct current is passed through them, which makes them switching elements used throughout transceivers, and because the switched power can exceed the control power they can provide gain. Ordinary rectifier diodes behave as crude PIN diodes at some frequencies; Ted Yapo demonstrated that common switching diodes are sufficient to build any logic gate, constructing a working digital clock from diodes alone with a radio-frequency supply.[465]

Sub-gigahertz radio modules expose a register set and handle the radio work internally, so a driver library with sound default settings reduces the designer's task to naming a centre frequency and an encryption key. That abstraction is what allows engineers without radio experience to build working links, at the cost of not learning what the parameters do.[398]

## Test and measurement

Measuring impedance at radio frequency means measuring the reflected wave, since the two are related by a fixed equation for a given line impedance. Extracting the reflected energy from the same line requires a bidirectional coupler, and making that work across a wide bandwidth is the hard part of building a network analyser and the substance of what a good instrument is selling.[446]

Radio-frequency instrumentation assumes a matched 50 ohm system throughout, with no attenuator ahead of the input, which is what makes an inexpensive analyser usable for looking at a carrier: the signal is repetitive and the loads are matched, which is the environment such an instrument was designed for.[178] The lower frequency limit of a low-cost analyser usually reveals its architecture: an instrument built by repurposing a modern radio-frequency chipset inherits that chipset's design assumptions and cannot reach down towards direct current, which is why such instruments start at hundreds of megahertz rather than at kilohertz.[347]

A spectrum analyser function built into an oscilloscope is bounded by the oscilloscope's own bandwidth licence, so buying the 100 MHz model yields a 100 MHz analyser. That is adequate for switching power supply work and effectively useless for radio-frequency work, a purchasing trap where the capability appears to be present in the hardware.[184]

A cheap software-defined receiver is what makes the spectrum comprehensible, because seeing a spectrum change over time conveys in moments what is hard to grasp from mathematics alone; the same insight had to be built from drawings and chalkboards in the era before such instruments existed.[172] A spectrum measurement also settles disputes that assertion cannot: a claim that a wireless system would interfere with existing microphones was answered on the spot by showing the microphones at around 850 MHz and the equipment transmitting at 920 MHz.[245]

Radio-frequency test equipment carries a disproportionate cost, and the accessories are part of it: cabling for a second-hand analyser can cost as much again as the instrument, and a vector network analyser reaching 40 GHz is priced in the tens of thousands. Equipping a general laboratory to a good standard costs a fraction of entering radio work.[567] Losing access to instruments is a real cost of leaving an organisation: having a high-frequency network analyser on the desk encourages measuring everything out of curiosity, and that habit of investigation disappears with the equipment rather than with the skill.[472]

## Prototyping and manufacturing

Milled prototype boards suit radio and analog iteration because those designs need frequent tweaking and cannot absorb a two-week fabrication cycle each time. The compromise is real: a milled board has no plated through-holes, no solder mask and no silkscreen, and its impedances differ from the production board, so the layout must be drawn in the knowledge that it will be milled and then redone properly for production.[345] The absence of plated holes forces via stitching by hand, and the wire through each hole must be soldered on both sides and then cut and shaved flush, because the residual height prevents a surface-mount component from seating.[345]

Printed conductors on additively manufactured boards have perhaps a fifth to a tenth of the conductivity of copper, which can be compensated simply by printing them thicker; what matters more for radio work is knowing the dielectric constant of the material between layers, which such a process controls directly rather than through ordering standard laminate.[505]

Potting is used where the operating environment attacks the electronics, and a tyre pressure sensor is the extreme case: sulfur from the rubber vulcanisation process combines with moisture condensing out of the fill air to produce sulfuric acid inside the tyre. The cost is that potting adds hours to the manufacturing cycle, so the rule is to pot only when the environment requires it.[93]

Radio modules of different frequency variants can be visually indistinguishable, differing only by a part-number suffix, which makes them a dangerous class of part. An entire production run was built with the wrong regional variant, could not be reworked without damaging the boards, and went straight from the line into the bin; the root cause was a part number corrupted while exporting data between systems through a spreadsheet.[577]

## History

The earliest radio transmitters worked by charging an antenna against a spark gap, the gap width setting the voltage at which the charge jumps, with each discharge radiating energy. Radar was then found by accident rather than sought: researchers experimenting with radio noticed interference as an aircraft passed and recognised the effect could be used.[62]

## Practice and expertise

Radio-frequency competence is treated as a distinct pillar of expertise rather than a subdivision of analog design. Tom LeMense describes his career in those terms, with the radio specialism as the deep vertical and other domains held only to the depth needed to be useful.[93]

Practitioners describe learning radio frequency by acquiring an instrument, struggling to use it, consulting people who know more and returning to it, rather than by studying theory first; the field is deep in the same way firmware is deep, and depth is reached incrementally.[500]

Once a radio design is working and certified, subsequent products reuse the board with only the sensors and interfaces changed, which is why building a wireless product does not require radio expertise so long as nobody disturbs the radio section.[549] Supporting users of radio products is harder than supporting wired ones, because the standard debugging advice does not apply: a customer cannot be told to put an oscilloscope on the problem, so support falls back on shared community knowledge and direct contact.[398]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 61 | Moore's Law, GaN and SiC devices - Gallimaufry GaN Gabble | https://theamphour.com/the-amp-hour-61-gallimaufry-gan-gabble/ | |
| 62 | Op amps, Microchips & Mergers - Narquois Nerd Nescience - Narquois Nerd Nescience | https://theamphour.com/the-amp-hour-62-narquois-nerd-nescience/ | |
| 93 | An Interview with Tom LeMense - Cacaesthestic Chronometric Carriwitchet | https://theamphour.com/the-amp-hour-93-cacaesthestic-chronometric-carriwitchet/ | April 29, 2012 |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 185 | An Interview with Hank Zumbahlen - Zoppa Zumbahlen Zateticism | https://theamphour.com/185-an-interview-with-hank-zumbahlen-zoppa-zumbahlen-zateticism/ | February 17, 2014 |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 304 | Alexa joins the fray | https://theamphour.com/304-alexa-joins-the-fray/ | June 22, 2016 |
| 345 | Milling About | https://theamphour.com/show-345-milling-about/ | May 30, 2017 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 446 | An Interview with Pete Bevelacqua | https://theamphour.com/446-an-interview-with-pete-bevelacqua/ | June 9, 2019 |
| 457 | Dotty Ernest Annty Frost | https://theamphour.com/457-dotty-ernest-annty-frost/ | September 8, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 472 | Keyzermas Vacation | https://theamphour.com/472-keyzermas-vacation/ | December 22, 2019 |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ | January 26, 2020 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 500 | Two and a Half Orders of Magnitude | https://theamphour.com/500-two-and-a-half-orders-of-magnitude/ | July 12, 2020 |
| 505 | Hardware Revision Control with Kyle Dumont | https://theamphour.com/505-hardware-revision-control-with-kyle-dumont/ | August 16, 2020 |
| 511 | Brewing Electronics with Eli Hughes | https://theamphour.com/511-brewing-electronics-with-eli-hughes/ | October 4, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 533 | Microwave measurement with Joel Dunsmore | https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/ | March 7, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 577 | Product Lifecycle Management with Michael Corr | https://theamphour.com/577-product-lifecycle-management-with-michael-corr/ | February 13, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
