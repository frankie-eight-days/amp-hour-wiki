---
title: Oscilloscope
concept: oscilloscope
episodes: 314
guests: 71
explains: 74
opinion: 31
generated: 2026-08-08
model: claude-opus-5 (pilot batch, pipeline steps 6-8)
---

<!--
PRODUCTION NOTES (not for readers)
Gather: 822 census mentions across 314 episodes -> 343 pinned explains/opinion
passages after paragraph-level dedupe, CAPPED at 150 (all explains kept; opinion
selected by recency + speaker diversity, non-host speakers first).
Re-grade: of the 150 examined, 105 retained as substantive (74 explains, 31
opinion) and 45 discarded. The census over-grades this concept badly: "oscilloscope"
is the corpus's most common technical noun, so it is pinned as "explains" whenever
it appears as scenery (a film prop, a swap-meet purchase, a bench-layout anecdote,
a career origin story). Discards were passages where nothing about scopes was taught.
Evidence packet: _packets/oscilloscope.json (54 claims, 5 disagreement groups).
ATTRIBUTION: eps 222, 431, 476, 481, 522 and 701 are among the 144 corpus files
whose host/guest labels are swapped. All citations from them were assigned by
content. Ep 222's key passage is labelled "Chris Gammell" but is plainly Bil Herd
(his Commodore 6502/Z80 debugging story); ep 476's is labelled "Dave Jones" but is
Kendall Castor-Perry. See _pilot_report.md.
-->

An oscilloscope displays voltage against time and is the primary instrument for observing circuit behaviour rather than inferring it.[289] Recurring technical guidance concerns three properties that are not obvious from a specification sheet: the BNC shells of a mains-powered bench scope are referenced to mains earth, which is the most common way beginners destroy an instrument;[20] a scope has one trigger point shared across all channels, which is why a second asynchronous signal drifts;[145] and usable bandwidth is bounded by the supplied passive probes rather than by the instrument.[567] Purchasing is contested across the full price range, with a stated hobbyist overkill threshold at four figures[606] and a sixteen-year decline in the price of a given capability of roughly two orders of magnitude.[117][710]

## Measurement practice

The instrument's value is in making behaviour visible, with the qualification that interpretation requires understanding how the instrument itself distorts what it shows.[289] Competence with a scope and with what it displays is treated as a defining skill for analog work.[476]

**Safety and grounding.** The BNC shells on a mains-powered bench scope are tied to mains earth, so grounding a probe at any node not at earth potential creates a fault path.[20] Almost all bench scopes and bench [[multimeter]]s share this ground reference, which is what makes floating measurement difficult.[274] High-voltage switching work is measured with high-voltage probes plus an isolation transformer on the instrument, or with isolated probes.[522] In high-voltage service work the instruments are treated as consumable, channel damage from arc-over being routine.[431]

**Approaching an unknown signal.** The signal is applied at the fastest timebase and the timebase dialled downward until a trace appears, which guarantees the signal is never undersampled.[169]

**Triggering.** A scope has a single trigger point shared by all channels, so two signals at slightly different frequencies produce one stable trace and one drifting at the difference frequency. Alternate trigger mode resolves this; without it, viewing both stably requires a second instrument.[145]

**Debugging order.** A dead bus is worked from the physical layer upward: probe the line for pull-up behaviour and edge integrity, then check device addressing, then the protocol.[274] The physical layer is worth inspecting first because I2C edges are asymmetric by design, pulling low through a transistor almost instantly and high through a resistor.[274] Configuration values assumed rather than measured are a recurring fault source; a serial decode failure attributed to instrument settings proved to be an incorrect baud rate at the source.[551]

**Probing.** Bandwidth beyond roughly 200-300 MHz is not useful on a general-purpose instrument because the supplied passive probes cannot follow it.[567] A broadband high-impedance tap is constructed by terminating the scope input at 50 ohms with a series kilohm resistance ahead of it, isolating cable capacitance and inductance.[474]

## Learning and instrument selection

Older analog scopes are available at negligible cost and are recommended as learning instruments, with the single filter that the design should be triggered-sweep rather than recurrent-sweep.[117] The argument is that fundamentals established on a simple instrument determine which digital features a buyer actually needs.[117] Terminology diverged across the generations: the analog sweep speed control is the digital horizontal scale.[117]

Two properties invisible at purchase dominate real performance. Whether measurement functions run in dedicated silicon or in software determines throughput — enabling a single horizontal measurement on one instrument collapsed its waveform update rate from a million per second to under a thousand.[619] ADC resolution yields real sensitivity, a 14-bit instrument resolving a 15-microvolt signal out of the noise floor that a 12-bit instrument could not.[677] A third hazard is upstream: the LMH6518 used in the front end of most modern scopes was silently revised to reduce its input offset capability without a part-number change, with reports of instruments bricked by excessive front-end DC offset.[727]

The instrument class exists under an unusual constraint, in that test equipment must precede the technology it measures: vendors must ship a scope fast enough for each new serial data rate before the first silicon implementing it is produced.[714]

## Purchasing debate

How much a non-professional should spend is disputed at every tier. Chris Gammell advocates buying the cheapest instrument that remains usable and upgrading only at a real limit;[18] Dave Jones applies the mirrored disposal test, selling gear he would not buy at its market value.[18] Jones places the hobbyist overkill threshold at four figures, holding that a 400-dollar four-channel instrument suffices indefinitely for general use and does not become obsolete.[606] Both reject the pocket-scope category, Jones as a narrow niche defined by budget and portability,[190] and Gammell on pedagogical grounds, since a beginner cannot separate instrument artefacts such as aliasing from circuit behaviour.[606] Gammell's positive criteria for a first instrument are repeatability and community: buying what others already own means support exists when problems arise.[567]

Whether beginners should start on limited equipment is argued both ways by the same person. Gammell holds that limitation is what makes better equipment legible later,[269] while also noting that a beginner cannot evaluate instrument quality before encountering a problem requiring it.[536] Asked directly whether a beginner should buy a scope at all, Jones answers affirmatively, while noting he worked without one for years on cost grounds.[306]

The sharpest disagreement concerns software-locked features. Jones defends the practice on industry-sustainability grounds, arguing that margin on high-end options funds continued development.[117] Alan Wolke, a Tektronix employee, agrees while noting he held the opposite view for two decades as a customer, and cites non-recurring engineering cost as the justification.[117] Gammell supplies a buyer-side defence: a lower entry price clears capital-expenditure approval thresholds that a full-featured instrument would not.[145] Jones's own position is not consistent — he separately demonstrated that a bandwidth restriction sold as a licence key could be defeated in hardware, having assumed it could not.[339]

On high-end requirements Jones endorsed the forum consensus that essentially no individual has productive use for a 1 GHz instrument,[287] and Gammell converted that judgement into a lab provisioning rule favouring ten 100 MHz instruments over one at 1 GHz.[287] On vendor strategy Jones read Agilent's restructuring as a retreat from the low end rather than from research-grade instruments, on the basis that it cannot compete on price,[164] and argued that a heavily promoted Tektronix launch had been preceded on specifications by a LeCroy instrument that received little attention.[347]

## Price history

A first scope purchase in the 1980s was a dual-channel 20 MHz analog instrument at eight to nine hundred dollars, without delayed timebase,[117] learned from the ring-bound manual supplied with it, which documented each control and the expected waveforms.[690] Sub-thousand-dollar digital instruments went from unavailable to commonplace over roughly the five years to 2012, reaching the 250-300 dollar range,[127] and by 2013 a 100 MHz instrument could be had secondhand for around two hundred dollars.[148] By 2016 a 1 GHz instrument of the 15,000-dollar class was being given away daily as a promotional prize.[287] By 2022 the entry-level four-channel class sat at 400 dollars and could be unlocked to 200 MHz,[606] and by 2025 roughly a thousand dollars bought a four-channel instrument of 800 MHz to 1 GHz bandwidth with deep memory and a two-channel 100 MHz generator.[710]

## Notable instances

A dual-processor bus fault was located as a transient on address line A10 occurring only when the second processor drove the bus, caused by a PCB stub; recognising it required knowing what normal bus activity looks like.[222] An intermittent supply fault caused by a lifting bond wire inside a diode was caught only by monitoring every rail continuously across two scopes and eight channels.[551] Capturing gigabit Ethernet through a differential probe at one terasample per second yielded roughly a hundred microseconds of data, enough for only a few packets.[600] Space-hardware power supplies are qualified by repeatedly shorting the output with a screwdriver while observing recovery, with full test re-qualification expected afterwards.[701] On a bus carrying signals in multiple directions, terminators were placed mid-bus and adjusted against the scope to minimise overshoot.[684] Electric fence energiser waveforms were characterised in the field, through attenuators, at Kruger National Park.[481]

Working on gigahertz-rate serialisers with a 100 MHz instrument rendered measurement useless — "Everything looks like DC to my crappy old oscilloscope."[173]

Jeri Ellsworth described a recurring trade-show pattern of being condescended to about basic instrument function, and a practice of allowing it to run before asking a specialist question.[35] In Australian usage a scope is a CRO, from cathode ray oscilloscope.[481]

## Further reading

- [Agilent is changing names](http://www.agilent.com/about/newsroom/presrel/2013/19sep-gp13016.html) — via #164
- [Dave has a take on it here](http://www.eevblog.com/forum/testgear/new-2ghz-touchscreen-scope-from-tek-june-6th/msg1227211/#msg1227211) — via #347
- [Siglent entry level 200 MHz - Teardown](https://www.eevblog.com/forum/blog/eevblog-985-siglent-sds1202x-e-oscilloscope-teardown/) — via #347
- [his talk at Supercon and the associated article on Hackaday.com](https://hackaday.com/2019/02/18/electron-microscopes-are-awesome-everything-you-didnt-know-you-wanted-to-know/) — via #431
- [Blog post about emissions](https://cushychicken.github.io/signal-integrity/) — via #474
- [Nash Reilly](https://cushychicken.github.io/) — via #474
- [Staying well grounded](https://www.analog.com/en/analog-dialogue/articles/staying-well-grounded.html) — via #474
- [the Black Magic book](https://www.amazon.com/High-Speed-Digital-Design-Handbook/dp/0133957241) — via #474
- [Analog Discovery Pro](https://digilent.com/shop/analog-discovery-pro-3000-series-portable-high-resolution-mixed-signal-oscilloscopes/) — via #567
- [What kind of scope can I get for $30k?](https://www.eevblog.com/forum/testgear/what-is-the-best-oscilliscope-that-i-can-get-for-$30-000/) — via #567
- [Analog Discovery 2](https://digilent.com/shop/analog-discovery-2-100ms-s-usb-oscilloscope-logic-analyzer-and-variable-power-supply/) — via #600
- [Logic probe](https://en.wikipedia.org/wiki/Logic_probe) — via #600
- [asked on his forum](https://www.eevblog.com/forum/testgear/is-a-rigol-mso5000-overkill-for-a-hobbyist/100/) — via #606
- [Joulescope](https://www.joulescope.com/) — via #677
- [How did you learn about oscilloscopes without the internet](https://www.eevblog.com/forum/beginners/retired-engineers-how-did-you-learn-using-oscilloscope-in-80s-without-internet!/?topicseen) — via #690
- [Kenneth Wyatt](https://benchtopemc.com/) — via #714
- [Martin Rowe of EE World](https://www.eeworldonline.com/author/mrowe/) — via #714

## References

| Ep | Title | URL | Date |
|---|---|---|---|
| 18 | Transistor Types and Where To Get Electronic Gear | https://theamphour.com/the-amp-hour-18-transistor-types-and-where-to-get-electronic-gear/ | - |
| 20 | Military Electronics and The Free Eagle (Freagle) Campaign | https://theamphour.com/the-amp-hour-20-military-electronics-and-our-first-wotws/ | - |
| 35 | An Interview with Jeri Ellsworth - The Ternary Tussle | https://theamphour.com/the-amp-hour-35-the-ternary-tussle/ | - |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ | August 23rd, 2021 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7th, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14th, 2013 |
| 148 | Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood | https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/ | June 3rd, 2013 |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ | September 23rd, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28th, 2013 |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ | November 25th, 2013 |
| 190 | Let's Hear It For The Buoys - Vanishing Vessel Vexation | https://theamphour.com/190-lets-hear-it-for-the-buoys-vanishing-vessel-vexation/ | March 24th, 2014 |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27th, 2014 |
| 269 | Be Tidy | https://theamphour.com/269-be-tidy/ | September 30th, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4th, 2015 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17th, 2016 |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ | March 2nd, 2016 |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ | July 6th, 2016 |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ | 2017 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13th, 2017 |
| 431 | An Interview with Adam McCombs | https://theamphour.com/431-an-interview-with-adam-mccombs/ | February 24th, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12th, 2020 |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ | January 26th, 2020 |
| 481 | An Interview with Paul Thompson | https://theamphour.com/481-an-interview-with-paul-thompson/ | February 24th, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20th, 2020 |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ | March 28th, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | - |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21st, 2021 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21st, 2022 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23rd, 2022 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | - |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | - |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ | - |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11th, 2025 |
| 701 | Electric Propulsion with Todd Bailey | https://theamphour.com/701-electric-propulsion-with-todd-bailey/ | 2014 |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ | December 6th, 2025 |
| 714 | The Measurement Blues with Martin Rowe | https://theamphour.com/714-the-measurement-blues-with-martin-rowe/ | 2010 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1st, 2026 |
