---
title: Antenna
concept: antenna
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

An antenna is a structure that converts between guided electrical signals and radiating electromagnetic waves, and its dimensions are fixed by physics rather than by design preference: the working target is a total dimension of about half a wavelength shared between the radiating element and the ground plane.[678] Because antenna size cannot be designed around, the subject dominates the integration of any radio into a product, from the placement of elements on a printed circuit board to the certification programme that follows.[678][175] Antennas also appear where they are not wanted: signal traces, cables, and cutouts in ground planes can all radiate unintentionally, making antenna behaviour the central problem in electromagnetic compliance.[452][338]

## Physical constraints

Antenna size is set by wavelength and cannot be designed around; at the low cellular bands of 600 to 700 MHz, roughly 180 millimetres of total dimension is required, and a device smaller than that simply has a less efficient antenna, with no design technique, fractal geometry included, recovering what the physics removes.[678] The radiating element is only part of the antenna: it does not work unless connected to the printed circuit board or ground plane, which itself participates in the radiation, so the ground plane must carry at least a quarter wavelength while the element carries the other quarter.[678]

The energy a receiver can capture is bounded by the capture area of its antenna relative to the sphere over which transmitted power has spread, which grows as four pi r squared; together with inverse-square fall-off, this sets a theoretical ceiling on received power at a given distance that no amount of transmitter design changes.[211] Everything except antenna size argues for lower frequencies—semiconductors are cheaper, gain is easier to obtain, power consumption is lower, and propagation is better—and the willingness to accept a large antenna is what makes a low-frequency design viable, the same propagation advantage being why bidders compete hardest for the lower spectrum bands.[109]

Regulatory limits below 30 MHz are framed the way they are because most products are not physically large enough to be efficient antennas at those wavelengths, so the emission risk is bounded by geometry rather than by design intent.[165] At the other extreme, millimetre-wave operation is not an incremental change to an existing radio design: the frequencies, the antennas, and even the cabling are all different.[678]

## Common forms

A dipole is half the physical size of a monopole for the same frequency, while a monopole radiates around itself and requires a feed point; consumer antennas are commonly shrunk below either figure by meandering the conductor or using only a fraction of a wavelength in the space available, at a cost in efficiency.[678] A quarter-wave wire monopole is both simple and highly effective—a length of wire cut to a quarter of the transmitting wavelength—with link performance depending on both ends using matching antennas oriented the same way, since orthogonal orientation degrades the path substantially.[398]

Antennas, like inductors and transformers, can be etched into copper that is being fabricated anyway, so the component itself is free and the only cost is board area.[76] A wire antenna that mounts into the board and rises into three-dimensional space above it is an alternative to a radio module and shrinks the footprint substantially, because the module carries regulation, an oscillator, and other parts the bare design does not need.[370] Some designs use a passive radiator: a floating piece of copper not electrically connected to the transmitter, which radiates by coupling to it and so can be placed where a connected element could not go.[639]

Printed log-periodic antennas made as bare circuit boards give good performance for their cost and size across a wide range—one hand-sized design covers 850 MHz to 6.5 GHz—making them a practical default for wideband receiving work.[214]

## Arrays, gain, and diversity

Antenna gain is obtained by concentrating radiation into a narrower beam using more elements, which is necessary at long range because transmitting omnidirectionally wastes too much energy; long-distance and high-frequency systems are therefore built as phased arrays that must locate the receiver and steer the beam onto it.[533] Beam steering works by adding and cancelling signals across an array so that energy is directed without anything moving, and the difficulty lies not in the principle but in the digital processing: fourth-generation cellular equipment manages perhaps six beams per sector, while fifth-generation systems produce hundreds, each tracked to a separate user.[533]

Multiple-input multiple-output (MIMO) systems use spatially separated antennas so that each receives a differently reflected version of the signal; because the probability of two well-separated antennas being in a fade simultaneously is uncorrelated, the arrangement buys reliability, which can then be traded for lower transmit power or higher data rate.[101] Antenna count drives board architecture in software-defined radio hardware: an early design fitted two daughter boards and therefore two antennas on one motherboard, while later designs using higher-precision separate converters had too many pins to fit two, so multiple-antenna operation moved to linking several motherboards together.[101]

A mobile handset needs far more antennas than its radio count suggests: cellular operation requires polarisation diversity so the device works however it is held, plus a backup path when one antenna is blocked by a hand, plus additional elements for MIMO, and then separate provision for wireless networking, satellite positioning, ultra-wideband, and near-field communication—the last of which is still an antenna even though it works in the near field.[678]

## Integration into products

The design sequence for a multi-antenna device starts by treating the product as a bare ground plane of its finished dimensions and placing the cellular antennas first, because the low bands are the most constrained and dictate what space remains for everything else.[678] The recurring failure is leaving the antenna until last, which produces a bad location, insufficient clearance, and metal in the wrong places; by the time a specialist is consulted the design is fixed, because the money has been spent and the client will not fund changes, so the specialist inherits constraints rather than a problem.[678] Antenna work must be complete and signed off before a prototype build, with the switching arrangement, band coverage, and element locations fixed; discovering during prototyping that another switch is needed indicates the antenna was not designed at all.[446]

The mistakes seen most often in submitted designs are placing the antenna in the middle of the board, providing no clearance area, and leaving metal below and around the element; where two antennas are present, the usual corrections are rotating one through ninety degrees and moving it to the shorter side of the board so the two do not couple.[678] The fundamental integration rules are short: aim for a half-wavelength dimension and keep metal away from behind the element.[446] Antennas at 2.4 GHz are forgiving enough that a competent board designer without antenna training can integrate one successfully by following the reference footprint and the vendor's guidelines on clearance and keep-out, whereas anything more complex than a 2.4 GHz inverted-F warrants an antenna engineer, because designing rather than placing an element requires simulation.[678]

Simulation of a handheld product must model the user, since a hand or body absorbs signal and changes the antenna's behaviour, which makes the mechanical design and the way the device is held part of the antenna problem rather than context around it.[678]

### Modules and integrated radios

Wireless products are commonly tiered by how much radio work the customer is expected to do: a removable card form for prototyping, a solder-down module with an integrated antenna for customers with no radio experience, and a smaller, cheaper bare device for customers who will provide their own external front end and antenna and carry their own certification.[202] Integrating a radio into a very small form factor is dominated by the antenna rather than the electronics: on Brandon Harris's wireless memory card, the antenna occupied roughly a third of the total area alongside the processor and radio.[202]

The board layout for a wireless module is undemanding—the device with a few passive components around it, stitched to a large ground plane, and a single controlled-impedance trace out to the antenna—with the practical rule that the trace to the connector be kept as short as possible.[453] For a designer without radio experience, the reliable method is to copy the vendor's application note exactly rather than adapt it, since the shapes in a reference design encode work the copier is not in a position to redo.[462] Once a radio section is working and certified, the productive approach is to leave it untouched and change only the sensors and interfaces around it, preserving the compliance position across a family of products.[549] A built-in printed antenna can still be the wrong choice even where it works: on Michael Ossmann's Jawbreaker development board, one was included only so testers without antennas could use it out of the box, and it was removed from the production design along with unused development pads to shrink the board by about a third.[161]

## Matching and simulation

Complexity in a matching network is itself a cost, adding loss and difficulty, so the value an experienced antenna engineer provides is keeping the arrangement simple rather than elaborating it.[446] Antenna engineering requires rework skill as well as design skill, since impedance matching is tuned by soldering and replacing 0201 components on the board.[446] Where two radio systems must operate simultaneously, the analysis is done from data sheets: take the two frequencies, find the transmitter's roll-off and the other receiver's sensitivity, determine the filtering needed between them, and then search a distributor catalogue for a filter with those parameters.[446]

Capable radio design tools are available without the professional packages: a general-purpose circuit simulator handles filter synthesis and impedance matching networks, method-of-moments antenna codes simulate printed antennas with results good enough to trust, and measured S-parameter files can be exported from an instrument and imported into those tools to synthesise a matching network directly.[229] Simulating a printed antenna from the actual layout means exporting the board geometry with its copper as a 3D model and defining the mesh by hand, concentrating mesh density where the antenna is; that meshing step is the part that takes the time, rather than the simulation setup.[695]

## Measurement

Two instruments cover almost all antenna verification: a vector network analyser (VNA) for impedance, and an anechoic chamber for efficiency and radiation pattern, with the chamber also giving the isolation between elements in a multi-antenna system; simulation tools are an addition rather than a substitute.[446] A network analyser measures impedance by measuring the reflected wave, the two being related by a fixed equation for a given line impedance; the difficult component is the bidirectional coupler that separates reflected energy from forward energy on the same line, and getting that right across a wide bandwidth is what a good instrument is really selling.[446]

Radiation pattern measurement is a mechanical scan: the device is rotated through angles in a chamber and measured at each step, so the cost of a full three-dimensional pattern is measurement time proportional to the angular resolution wanted, with a characterised reference antenna receiving and the device under test judged against it.[678] Passive measurement—network analysis plus chamber measurement without the radio actually operating—is sufficient to confirm an antenna works in roughly ninety-nine percent of cases, with active measurement reserved for the rare cellular case that needs it.[678]

Multiport network analysers exist because measurement count scales badly with switching: testing every path between N ports one pair at a time requires N(N−1)/2 measurements, so a 32-port device implies hundreds of sequential measurements, and an instrument that drives one port and measures all the others simultaneously collapses that—which matters when an automotive antenna must be tested in a second rather than ten minutes.[533]

Antennas must also be designed for testability as well as performance: on one of Shrouk El-Attar's designs, the antenna was buried on the far side of the board such that the product had to be drilled to reach the BNC test connector, making compliance measurement impractical and limiting how many units could be measured at all.[549]

## Unintentional antennas

Unintentional antennas are the main electromagnetic compliance problem, and the classic case is a signal trace crossing a split in an adjacent plane: because return current must follow the signal, a clock routed over the boundary between two supply planes on the neighbouring layer radiates remarkably strongly, and finding signals crossing splits is the first thing to check when a board is emitting.[452] Techniques that help at low frequency actively hurt at radio frequency: a cutout in a ground plane intended to control low-frequency noise becomes an antenna once a radio-frequency signal encounters it, so low-frequency converter practice and radio practice cannot be applied together without contradiction.[457] Cabling turns into an antenna as readily as a trace: a long run from an amplifier out to a remote speaker radiates the switching edges driving it, and that becomes the obstacle when the product is taken for compliance testing rather than a problem visible on the bench.[338]

Emissions problems are found with near-field probes—either a loop responding to magnetic field or a stub responding to electric field—waved across the board with a spectrum analyser to localise the source; a usable probe can be improvised from an oscilloscope probe by shorting its ground lead to the tip, and modern practice adds recording radio-frequency behaviour over time alongside other signals.[117] An emissions defect found late in hardware has no equivalent of a software patch: a wireless product in a plastic enclosure cannot simply be shielded, because the thing that must radiate and the thing that must not are in the same box, so the remedy is another board revision, which is the argument for considering the problem at the start of a hardware project.[452]

## Certification and connectors

Designing a custom antenna rather than using a pre-certified module means running one's own certification programme, which can still be justified on unit cost at sufficient volume; Andrew Witte's team took this path for a wireless product and had to carry its own certification process.[175] A module vendor can absorb radio certification across several regions on the customer's behalf, so the customer buys the module and transmits legally; what does not transfer is the per-country landing and licensing framework, which is separate paperwork in every jurisdiction and requires a substantial legal effort rather than an engineering one.[427]

The reverse-polarity connector convention on consumer radio equipment exists for regulatory rather than technical reasons: regulators objected that a user could unscrew a supplied antenna and fit a high-gain one, so manufacturers commissioned connectors with the pin and socket swapped—a measure defeated as soon as antennas with the reversed connector became available to consumers.[708] Low-cost receiver hardware often ships with a connector chosen for the market it was originally sold into rather than for radio work, so an adapter to a standard radio connector—PAL to SMA or PAL to BNC—is what makes the wider antenna ecosystem usable with it.[214]

## Propagation and practice

Propagation is a condition rather than a design parameter: a modest station with a simple wire antenna fifteen or twenty feet up and a few watts can reach the other side of the world when conditions allow, and when the solar cycle turns, the same equipment will not, requiring materially more power or a larger antenna to compensate.[613] Location can outweigh equipment: operating from elevation, in the open, and away from sources of electrical noise improves what can be heard more than a better antenna would, and proximity to salt water improves propagation, so a poor antenna in a quiet location outperforms a good one in a noisy urban environment.[613]

Range results in the laboratory can mislead in both directions: in CNLohr's low-power link experiments, a link that struggled at a few inches on the bench—once genuine protocol defects were fixed—reached several hundred feet, then thousands, and eventually about 2.5 kilometres from a pair of wires on a development board, partly because forward error correction had been masking encoding errors as poor signal.[667]

Antenna work is approachable by experiment rather than only by analysis: practitioners routinely calculate the wavelength, build something close, then trim it while measuring, deriving the mathematics afterwards if at all.[301] Copying a reference antenna from a published image—tracing it into a vector drawing—is a legitimate if crude starting point when no reference design exists for the band in question, though the outcome is often a plain monopole that could have been made from a cut length of wire of the calculated quarter-wave length.[464]

Antenna design is a distinct specialism that competent digital engineers do not possess, and the appropriate response in a small company is to recognise the gap and bring in someone who does, particularly where the product is difficult—such as a device to be installed inside a wall with metal behind it acting as an unintended ground plane.[295] Knowing how to design an antenna does not make it the right decision: at low volumes the effort is not repaid, and buying a prefabricated module is the better engineering choice even for someone capable of the controlled-impedance and antenna work.[604] An antenna designed to be tolerant rather than optimal can also be a deliberate product decision: Alex Haro's satellite service was built to work with whatever printed omnidirectional antenna of around fifty percent efficiency a device already has, on the reasoning that requiring customers to change their hardware would prevent uptake, leaving efficiency improvements as an optional later gain.[728] Finally, making antennas efficient over a broad frequency range remains hard—like broadband efficient power amplifiers, it is an open problem rather than solved engineering.[162]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 76 | Fremescent Floccose Fortification | https://theamphour.com/the-amp-hour-76-fremescent-floccose-fortification/ | January 2, 2012 |
| 101 | An Interview with Matt Ettus - Quality Quadrature Quidam | https://theamphour.com/the-amp-hour-101-quality-quadrature-quidam/ | June 24, 2012 |
| 109 | An Interview with Larry Sears - Hexagram Hardware Holism | https://theamphour.com/the-amp-hour-109-hexagram-hardware-holism/ | August 19, 2012 |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ | August 23, 2021 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 165 | An Interview with Henry Ott - Forced FCC Filtering | https://theamphour.com/165-an-interview-with-henry-ott-forced-fcc-filtering/ | September 30, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 295 | An Interview with Omer Kilic | https://theamphour.com/295-an-interview-with-omer-kilic/ | April 20, 2016 |
| 301 | The Nerd Calendar | https://theamphour.com/301-the-nerd-calendar/ | June 1, 2016 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 427 | An Interview with Maarten Engelen | https://theamphour.com/427-an-interview-with-maarten-engelen/ | January 27, 2019 |
| 446 | An Interview with Pete Bevelacqua | https://theamphour.com/446-an-interview-with-pete-bevelacqua/ | June 9, 2019 |
| 452 | An Interview with Kieran O'Leary | https://theamphour.com/452-an-interview-with-kieran-oleary/ | July 28, 2019 |
| 453 | Vertically Integrated Design Engineering | https://theamphour.com/453-vertically-integrated-design-engineering/ | August 4, 2019 |
| 457 | Dotty Ernest Annty Frost | https://theamphour.com/457-dotty-ernest-annty-frost/ | September 8, 2019 |
| 462 | Boat Anchors | https://theamphour.com/462-boat-anchors/ | October 13, 2019 |
| 464 | KonnectorPanik | https://theamphour.com/464-konnectorpanik/ | October 27, 2019 |
| 533 | Microwave measurement with Joel Dunsmore | https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/ | March 7, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 639 | Daaaamn We're Duuuummmb | https://theamphour.com/639-daaaamn-were-duuuummmb/ | July 17, 2023 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 678 | All About Antennas with Katerina Galitskaya | https://theamphour.com/678-all-about-antennas-with-katerina-galitskaya/ | September 30, 2024 |
| 695 | Making The Invisible, Visible with Sam Aldhaher | https://theamphour.com/695-making-the-invisible-visible-with-sam-aldahar/ | June 3, 2025 |
| 708 | All the Connectors with Davide Andrea | https://theamphour.com/708-all-the-connectors-with-davide-andrea/ | November 1, 2025 |
| 728 | Space Age Bluetooth with Alex Haro | https://theamphour.com/728-space-age-bluetooth-with-alex-haro/ | July 9, 2026 |
