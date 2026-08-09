---
title: Wafer
concept: wafer
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

A wafer is the disc of silicon on which integrated circuits are fabricated, sliced from an ingot and processed through lithography, etch, doping and deposition before being sawn into individual die.[169][390][687] Wafers come in fixed diameters such as 150 mm and 300 mm, so only a fixed number of die fit on each one and daily chip throughput is set by wafer diameter against die size.[32] The sole motivation for moving to larger diameters is more die per wafer, which lowers the per-device cost.[63] Because only a shallow layer at the top of a wafer contains the processed devices and the remaining thickness is undoped bulk silicon, the wafer is as much a mechanical carrier as an electrical one.[303]

## Diameters and die counts

Volume wafer diameters reached 11 to 12 inches, with an industry push toward 18-inch, 450 mm wafers.[222] Early-1980s wafers were only around three and a half inches across, and process quality was poor enough that a run might produce only a couple of good die.[222] Mature product lines did not follow the migration: analog and power semiconductor fabs continue to run 180 nm and 250 nm feature sizes on 4-inch wafers because those products gain nothing from finer geometries, and LED manufacture continued on four-inch (100 mm) wafers long after logic had moved to much larger diameters.[5][48]

Die counts vary over several orders of magnitude with die size and process. A power chip die of roughly half a millimetre square yields on the order of 200 die on a 4-inch wafer, which remains commercially viable even with manual wafer handling.[5] Analog processes on four-inch wafers historically produced a couple of hundred die per wafer, and process and efficiency improvements later raised that to thousands and up to 50,000 die on the same diameter.[348] A die of two square millimetres gives roughly 21,000 dice per 300 mm wafer, and a wafer of RP2040 parts carries about 20,000 chips.[574][648] A six-inch LED wafer can carry about a million die.[71]

Growing the diameter is difficult chiefly because of uniformity. Distributing plasma or wet chemistry evenly becomes the limiting problem as diameter grows: on a 2-inch or 4-inch wafer the reaction can be concentrated in one region, whereas 18-inch wafers demand uniformity across a far larger area.[63]

## Process steps

In plasma etching the wafer is placed in a reactor, pumped down to near vacuum, and exposed to reactive gases that an RF field dissociates so the fragments chemically attack the target film.[169] The chamber works by loading a wafer, admitting process gases and striking a plasma with RF generators; the resulting reactive cloud consumes silicon, polysilicon or resist and is drawn away by a turbo pump beneath the wafer.[536] Etch equipment moved from effectively open-air chambers to high-vacuum systems because fine geometries cannot be produced without high vacuum, and wet etching persisted alongside plasma etching during the transition period, though most process steps had switched to plasma by the time open chambers disappeared.[134][169]

Photolithography defines the pattern. With positive photoresist the areas blacked out on the mask block UV and their resist is washed away in the developer, while with negative resist the exposed areas remain, so mask polarity must match the resist chemistry.[390] A wafer has no intrinsic origin coordinate, so layer-to-layer alignment during photolithography is the critical constraint on a multi-mask process.[390] Extreme ultraviolet lithography is the patterning method needed for the smallest feature sizes, but the industry first extended older wavelengths through double, triple and quadruple patterning where that was the more economical high-volume route.[666] Electron-beam patterning is a raster-based scan rather than a vector process, using multiple beams and increasingly exotic resist chemistries applied on top of the wafer; because rastering must be performed wafer by wafer, direct-write patterning has never displaced projection photolithography for volume production.[26][172]

Doping is done by ion implantation, which ionises a dopant gas in a plasma, focuses it into a beam and accelerates it to around 100 kilovolts or more so the phosphorus or boron atoms embed themselves in the silicon at precisely controlled positions.[390] The dopant gases involved are lethal at concentrations around 50 parts per million and can be absorbed through the skin.[390]

A typical process flow exposes the wafer in photolithography, rinses it, then passes it to dry ash.[502] Modern fabs move wafers between process tools with overhead robotic transport systems that can span a dozen separate buildings.[502]

## Fab operation and risk

Fab economics depend on running the line at the highest possible utilisation, on the order of 90 to 95 percent.[32] Because the line is designed for full utilisation, a single tool going down costs both lost capacity and a growing queue of work-in-progress wafers behind it, and a single broken tool stalls every lot behind that step.[120][502] Wafers progressively contaminate dry etch chambers, so the quartz kits inside must be periodically swapped out, after which the chamber has to be pumped down, tested and verified before it returns to service.[120]

The wafers in process are themselves the exposure. A power failure in an etch bay drops the suspended reactive cloud straight onto the wafers below, and at fine geometries anything in process that cannot be cleaned immediately becomes scrap.[536] An etch tool holds wafers in FOUP pods of about 25 wafers each, with several pods and several process chambers loaded at once, so hundreds of wafers are at risk in a single machine.[536] Fabs therefore negotiate power service contracts with liability clauses, since a supply interruption destroys every wafer in process, and their large continuous load gives them bargaining leverage.[583]

Siting reflects the same sensitivities. Low seismic activity is a requirement because ground movement disrupts lithography alignment, and porous limestone bedrock that absorbs vibration is an advantage.[579] Analog Devices sited a fab in Ireland partly because wafers can be flown in and finished chips flown out cheaply, and the resulting cluster attracted further semiconductor investment and graduates.[579]

## Yield and process variation

Die area drives yield, so the larger the die the greater the risk that yield is too low for the part to be commercially viable, which is why very large devices such as FPGAs are rolled out cautiously.[136] For very large die at the start of a product's life, yield can be so poor that the useful metric inverts from die per wafer to wafers per die.[103] Moving a design to a smaller geometry shrinks the die and therefore increases the number of parts per wafer, which is the underlying cost argument for a process migration; an existing part can also be shrunk onto a newer process purely to fit more per wafer, a cost-reduction step distinct from designing a new device at a finer node.[102][271]

Process variation shapes analog design directly. Devices placed close together on one die match each other well, but their absolute values move from wafer to wafer by as much as 10 percent, because variation such as a few microns of extra film thickness alters device performance.[672] Analog integrated circuits are therefore designed around ratios between components rather than absolute values, so that a resistive divider still produces the intended output when every resistor shifts together on the next wafer.[672]

## Test

The number of test vectors needed for a chip scales roughly with the square of its complexity, so test cost rises faster than device size.[32] Wafer probe throughput is raised by multi-probe testers that lower multiple sensor heads and drivers at once so several die are measured in parallel.[71] Even so, a six-inch LED wafer carrying about a million die takes a day or two to test, so a fab keeps hundreds of testers running in parallel to avoid stockpiling untested wafers.[71] In volume production every chip is tested individually after the wafer is sawn and the die packaged, and the resulting tester data is monitored continuously as a process health signal.[687] Package qualification is repeated periodically during mass production to confirm that package materials and quality are not introducing new failures.[687]

## Supply chain

A single chip is rarely made in one country: the silicon wafer may be produced in one place, diced in another, tested in a third and packaged in a fourth, which is why data sheets commonly state that a part is manufactured in one or more of several listed countries.[591] Wafers are shipped between countries between process steps, with different sites performing wafer growth, lithography, packaging and test, because each region specialises in a different part of the flow.[582] Probe-tested wafers are packed into boxes and shipped overseas for assembly.[141] No existing facility performs the whole flow in one place: a fab produces the silicon wafer and then exports it, typically to Malaysia for packaging and elsewhere for die bonding, so a single-campus soup-to-nuts plant would be a departure from current practice.[720] One memory fab in Austin sourced its bare wafers from Japan and its equipment and process chemicals from Japan, Germany and the United States, then shipped finished tested wafers to Korea and on to the Philippines or China for dicing, packaging and final test.[322] Silicon ingots, from which bare wafers are sliced, came predominantly from Japan, and the supplier base for them is very small.[582] Cree, by contrast, performed all of its LED wafer fabrication and epitaxial layer growth at its Durham, North Carolina site, after which wafers are diced and the individual die encapsulated or packaged before assembly into products such as large display boards.[71]

New fab construction in the United States has targeted leading-edge nodes, while the capacity that shortages actually exposed was in legacy lines running 100 mm wafers and older geometries that had been moved offshore because they no longer made financial sense domestically.[573]

## Capacity, lead time and allocation

A company that owns its own fab is capped by that fab's wafer starts, for example 20,000 wafers a week, and must allocate them among customers; this capacity ceiling produced the classic 40-week lead time and is a principal reason chip companies moved to fabless models using foundries such as TSMC and UMC.[44] Semiconductor lead times, historically quoted at 40 weeks and more recently at 14, represent the whole flow starting from bare wafers rather than a shipping delay, and vendors that hold no finished stock quote lead times reflecting wafer starts, so a customer must plan orders months ahead of running out.[367][377] Wafer-in to wafer-out processing alone took about 30 days in one fab, before probe test, overseas packaging, further testing and distribution are added, which is why chip lead times cannot be compressed the way a PCB order can be turned around in 24 hours.[502]

Foundries offer hot lots and expedited wafer starts that jump the queue, but when demand surges and every order is marked urgent the mechanism loses its meaning.[502] During the 2020–2021 shortage, suppliers quoted normal product lead times of 16 to 20 weeks and asked customers for at least 12 weeks of backlog visibility because they could not expedite every order.[502] Large customers hold negotiated wafer allocations that foundries trim under shortage, whereas a small customer can absorb odd spare wafers a foundry offers, which insulated one low-volume part during the 2021–2022 shortage; pre-buying wafers ahead of demand protected stock of the RP2040.[648]

Several practices shorten the path to finished parts. Holding a die bank of already-fabricated, untested die lets a supplier build finished parts in four to six weeks instead of waiting for a full wafer start.[129] Obsolete-part suppliers such as Rochester Electronics obtain wafers under agreement from the original vendor and then package and test them themselves to supply finished chips for parts designed in the 1980s.[567]

## Cost and access

A new leading-edge fab costs on the order of five to ten billion dollars, and the first company to reach a node can price its chips at a large premium for the years before competitors can match it.[64] A fab is financed by a multi-billion-dollar loan against the building and equipment and then repays it by selling wafers, so prices on a process tend to fall as it becomes trailing edge and the machinery is paid off.[672] The cost balance of an analog part has shifted so that packaging now generally exceeds die cost, reversing the older situation of four-inch wafers and five-micron geometries where the die dominated.[129]

For a customer, mask cost dominates a small run. Buying a dedicated mask set for a whole wafer at 65 nm costs a couple of hundred thousand pounds, which puts a private tape-out beyond a university research group, and even a roughly 20-year-old process such as Sky 130 carries a mask cost of about $200,000, after which per-wafer and per-die costs are comparatively low.[579][616] A full silicon run on Sky 130 costs roughly $200,000 to $300,000.[703] The minimum practical production run for an analog part is about twelve wafers, which on modern 8-inch foundry wafers already yields a very large number of parts relative to initial demand.[129] There is no low-commitment, self-service equivalent of cloud computing for silicon: a foundry engagement starts in the region of $300,000 for a lot of wafers, which excludes small startups.[271]

### Shared runs

Sharing a run is the standard answer to mask cost. Around 2010 a single prototype wafer run cost roughly $7,500, and sharing that run with other customers lowered the per-participant cost in the same way that sharing a panel lowers batch PCB prices, provided all participants use the same process.[15] Multi-project wafer services let several research groups commit a few times a year to a fixed area of silicon each, sharing one mask set and the resulting wafers; Europractice provides this in Europe and MOSIS in the United States, farming the combined design out to foundries such as TSMC.[579] The standard multi-project wafer slot is 4 mm by 4 mm, and services occasionally subdivide it further to offer a single square millimetre for about three and a half thousand pounds, which returns around a hundred packaged chips.[579]

A shuttle run places all participants' designs on a single mask so the mask cost is shared, for example $200,000 across 40 participants; every wafer receives a shot of that same combined mask, stepped repeatedly, and the die are sorted at dicing so each participant receives only their own.[616] Shared among about 40 eFabless participants, a Sky 130 run gives a slot price near $10,000.[703] Tiny Tapeout subdivides a single multi-project wafer slot into 250 further slots, pushing the cost of an individual design down another order of magnitude.[616] Subdividing further brings the price of a custom silicon design to about $200, at which point the participant receives a PCB with their packaged chip mounted and ready to use.[703]

## Custom processes

Custom process development is slow because many lots must be processed wafer by wafer and the resulting defects are distributed, making it hard to separate a design error from a tool error; a company that does not own its fab is also dependent on the foundry scheduling it in.[729] After building several sensor-on-chip companies, the recommended approach is to minimise reliance on custom process steps and leverage standard high-volume processes, locating the competitive advantage in design, applications and test rather than in the process itself.[729]

## Amateur wafer processing

Hobby-scale silicon processing can be reduced to a furnace or pottery kiln capable of 1,000 degrees C, replacing the racks of dedicated diffusion equipment used in a production fab.[52] A CPU fan with double-sided tape can serve as a spin coater for small wafer pieces, cut vinyl stickers applied directly to the wafer can substitute for photolithographic masking at hobby feature sizes, and oxide etching can be done with consumer products containing dilute hydrofluoric acid, such as glass etchant or a rust and stain remover containing 2 percent hydrofluoric acid.[52] Production fabs choose the strongest practical acid concentration for oxide etch because throughput dominates, whereas a hobbyist can accept a 20-minute etch with a far weaker chemistry.[52]

Energy accounting differs just as sharply. The thermal steps dominate the energy cost of silicon processing: running a furnace at 1,000 degrees C for six hours to make a small solar cell consumes more energy than the cell will ever return, whereas a production fab holds furnaces continuously at temperature and feeds wafers through without cooldown, driving the energy cost per wafer down to fractions of a penny.[52]

Bare material is obtainable at small scale. New 50 mm (two-inch) wafers can be bought in low quantity from suppliers such as University Wafer for about ten dollars each, giving known specifications, whereas surplus wafers bought secondhand often come with no reliable information about what they are; the dopant type of an unlabelled wafer can be determined after purchase by measuring parameters such as resistivity.[390]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ | |
| 15 | Analog Components, First Person Flying and Idea Ownership | https://theamphour.com/the-amp-hour-15-analog-components-first-person-flying-and-idea-ownership/ | |
| 26 | The Ben & Jeri Show | https://theamphour.com/the-amp-hour-26-the-ben-jeri-show/ | |
| 32 | Cores, Digikey, Electronic Design - The Commercial Competitor Commencement | https://theamphour.com/the-amp-hour-32-the-commercial-competition-commencement/ | |
| 44 | BASIC, Chip companies & Robots - Pernicious Projects, Puppies in Peril | https://theamphour.com/the-amp-hour-44-pernicious-projects-puppies-in-peril/ | |
| 48 | Bob Pease, Jim Williams - Posthumous Pease Porridge | https://theamphour.com/the-amp-hour-48-posthumous-pease-porridge/ | |
| 52 | An Interview with Jeri Ellsworth - Carnassial Chip Chemicals | https://theamphour.com/the-amp-hour-52-carnassial-chip-chemicals/ | |
| 63 | Shop bots, 450 mm fabs & redFrog - Pick and Place Palillogy | https://theamphour.com/the-amp-hour-63-pick-and-place-palillogy/ | |
| 64 | OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster | https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/ | |
| 71 | An Interview with John Edmond - Luciferous LED Lucubrator | https://theamphour.com/the-amp-hour-71-luciferous-led-lucubrator/ | |
| 102 | Gouging Green Gardyloo | https://theamphour.com/the-amp-hour-102-gouging-green-gardyloo/ | July 1, 2012 |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 120 | Prototyping, Machining & Accelerators- Mugwumps Mulling Milling | https://theamphour.com/the-amp-hour-120-mugwumps-mulling-milling/ | November 4, 2012 |
| 129 | An Interview with Brett Fox and Dr Jeroen Fonderie - Device Doubling Decretum | https://theamphour.com/the-amp-hour-129-device-doubling-decretum/ | January 21, 2013 |
| 134 | Intel, EPA & Brown Field - Google's Ground Gurgitation | https://theamphour.com/the-amp-hour-134-googles-ground-gurgitation/ | February 25, 2013 |
| 136 | Hardware, Surveys and Giveaways - Radular Rental Ranting | https://theamphour.com/the-amp-hour-136-radular-rental-ranting/ | March 12, 2013 |
| 141 | FPGAs, Robots & Thermocouples - Wampum's Wavering Worth | https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/ | April 15, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 271 | Amazon Moves In, Dave Says Run | https://theamphour.com/271-amazon-moves-in-dave-says-run/ | October 14, 2015 |
| 303 | An Interview with Dmitry Nedospasov | https://theamphour.com/303-an-interview-with-dmitry-nedospasov/ | June 14, 2016 |
| 322 | World Trade Futurity (WTF) | https://theamphour.com/322-world-trade-futurity-wtf/ | November 9, 2016 |
| 348 | An Interview with Art Kay | https://theamphour.com/348-an-interview-with-art-kay/ | June 18, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 390 | An Interview with Sam Zeloof | https://theamphour.com/390-an-interview-with-sam-zeloof/ | April 29, 2018 |
| 502 | Lowest Common Denominator Design | https://theamphour.com/502-lowest-common-denominator-design/ | July 26, 2020 |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ | March 28, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 573 | Mixed Signal Education with Philip Salmony | https://theamphour.com/573-mixed-signal-education-with-philip-salmony/ | January 17, 2022 |
| 574 | Bubblegum Tap Shoes | https://theamphour.com/574-bubblegum-tap-shoes/ | January 23, 2022 |
| 579 | ADC Chip Design with Anthony Wall | https://theamphour.com/579-adc-chip-design-with-anthony-wall/ | February 27, 2022 |
| 582 | The Same Wavelength | https://theamphour.com/582-the-same-wavelength/ | March 20, 2022 |
| 583 | The Smart Grid with Paul Zawada | https://theamphour.com/583-the-smart-grid-with-paul-zawada/ | March 27, 2022 |
| 591 | Olive-a The World | https://theamphour.com/591-olive-a-the-world/ | |
| 616 | Open Source Tapeout with Matthew Venn | https://theamphour.com/616-open-source-tapeout-with-matthew-venn/ | January 22, 2023 |
| 648 | The RP1 and beyond with the Raspberry Pi Hardware team | https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/ | October 22, 2023 |
| 666 | Good Energy Citizen | https://theamphour.com/666-good-energy-citizen/ | May 8, 2024 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 687 | The RP2350 with the Raspberry Pi Team | https://theamphour.com/687-the-rp2350-with-the-raspberry-pi-team/ | January 28, 2025 |
| 703 | Building wafer.space with Tim Ansell | https://theamphour.com/703-building-wafer-space-with-tim-ansell/ | September 24, 2025 |
| 720 | Hyper Growth and OpenClaw Interns | https://theamphour.com/720-hyper-growth-and-openclaw-interns/ | March 31, 2026 |
| 729 | The Terahertz Frontier with Greg Charvat of Teradar | https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/ | July 22, 2026 |
