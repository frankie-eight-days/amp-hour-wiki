---
title: Oscilloscope
concept: oscilloscope
generated: 2026-08-08
model: kimi-k3
writer-bakeoff: true
---

An oscilloscope is a test instrument that makes circuit behaviour observable, serving as the primary means of seeing what a circuit is doing rather than inferring it.[289] Competence with the instrument, and with what its display represents, is treated as a defining skill for analog work, and effective use requires understanding how the instrument itself distorts what it shows.[476][289] In Australian usage the instrument is commonly called a CRO, from cathode ray oscilloscope.[481]

## Grounding and safety

The BNC connector shells on a mains-powered bench oscilloscope are referenced to mains earth, so grounding a probe at any node not at earth potential creates a fault path; this is the most common way beginners destroy a scope or a circuit.[20] The problem is general: almost all bench scopes and bench multimeters are ground-referenced, which is what makes floating measurement difficult.[274] Floating high-voltage measurement is performed with high-voltage probes combined with an isolation transformer on the instrument, or with isolated probes.[522]

In high-voltage service work the instruments are treated as consumable, channel damage from arc-over being routine.[431]

## Operation and technique

An unknown signal is approached from the fastest timebase setting and dialled downward until a trace appears, which guarantees the signal is never undersampled.[169]

A scope has a single trigger point shared by all channels, so two signals at slightly different frequencies yield one stable trace and one drifting at the difference frequency.[145] Alternate trigger mode resolves this; in its absence, viewing two unrelated signals stably requires two instruments.[145]

### Bus debugging

A dead bus is debugged from the physical layer upward: the line is probed for pull-up and edge integrity first, then device addressing is checked, then the protocol layer.[274] This ordering is motivated by the physical behaviour of I2C, whose edges are asymmetric by design, pulling low through a transistor almost instantly and high through a resistor, which is what makes the physical layer worth inspecting first.[274] Assumed configuration values should be measured rather than trusted; a serial decode failure attributed to instrument settings proved in one case to be an incorrect baud rate at the source.[551]

## Probing and bandwidth

Bandwidth beyond roughly 200–300 MHz is not useful on a general-purpose scope because the supplied passive probes cannot follow it.[567] A broadband high-impedance tap can be built by terminating the scope input at 50 ohms and placing a series kilohm resistance ahead of it, isolating cable capacitance and inductance.[474]

The value of bandwidth is contested as a purchasing matter. Jones has endorsed the position that essentially no individual has productive use for a 1 GHz instrument.[287] Gammell converts the same judgement into a lab provisioning rule favouring many mid-bandwidth instruments over a single high-bandwidth one: ten 100 MHz scopes rather than one 1 GHz scope.[287] The converse failure is documented in practice: working on gigahertz-rate serialisers with a 100 MHz instrument rendered the measurements useless.[173]

## Instrument architecture

### Front ends and resolution

The LMH6518 is used in the front end of most modern scopes; a silent revision reduced its input offset capability without a part-number change, with reports of instruments bricked by excessive front-end DC offset.[727] Higher ADC resolution yields real sensitivity: a 14-bit instrument resolved a 15-microvolt signal out of the noise floor that a 12-bit instrument could not.[677]

### Processing and update rate

Whether measurement functions run in dedicated silicon or in software is invisible at purchase and dominates real throughput: enabling a single horizontal measurement on one instrument collapsed its waveform update rate from a million waveforms per second to under a thousand.[619]

### Vendor economics

Test equipment must exist before the technology it measures, so scope vendors must ship an instrument fast enough for each new serial data rate before the first silicon implementing it is produced.[714]

The practice of selling bandwidth and decoding features as software-unlocked options is defended on industry-sustainability grounds: Jones has argued that margin on high-end options funds continued development, and that selling a fully featured 1 GHz instrument with all decoding for $400 would destroy the industry.[117] Wolke agrees with the vendor position, citing the non-recurring engineering cost, while noting he held the opposite view for two decades as a customer.[117] Gammell argues tiered pricing helps buyers, because a lower entry price clears capital-expenditure approval thresholds that a full-featured instrument would not.[145] Jones also demonstrated that a bandwidth restriction sold as a licence key could be defeated in hardware, having assumed it could not.[339]

## Use in practice

A dual-processor bus fault was located on a scope as a transient on address line A10 occurring only when the second processor drove the bus, caused by a PCB stub; recognising it required knowing what normal bus activity looks like.[222] An intermittent supply fault caused by a lifting bond wire inside a diode was caught only by monitoring every rail continuously across two scopes and eight channels.[551] Capturing gigabit Ethernet through a differential probe at one terasample per second yielded roughly a hundred microseconds of data, sufficient for only a few packets.[600] Space-hardware power supplies are qualified by repeatedly shorting the output with a screwdriver while observing recovery on a scope, with full test re-qualification expected afterwards.[701] On a bus carrying signals in multiple directions, terminators were placed mid-bus and adjusted against the scope to minimise overshoot.[684] Electric fence energiser waveforms have been characterised in the field through attenuators at Kruger National Park.[481]

## Purchasing

Chris Gammell advocates buying the cheapest instrument that remains usable and upgrading only when a real limit is reached.[18] Dave Jones applies a disposal test to owned equipment: gear he would not buy at its market value is sold.[18] Jones places the hobbyist overkill threshold at four figures, holding that a $400 four-channel scope suffices indefinitely for general use and does not become obsolete.[606]

Both dismiss pocket scopes: Jones holds that they fill only a narrow niche defined by budget and portability,[190] while Gammell objects on pedagogical grounds, that a beginner cannot separate instrument artefacts such as aliasing from circuit behaviour.[606] Gammell recommends beginners prioritise repeatability and buy an instrument others already own, so that community support exists when problems arise.[567]

On the question of learning equipment, Gammell argues that starting on limited equipment is what makes better equipment legible later,[269] while noting the difficulty that a beginner cannot evaluate instrument quality before encountering a problem that requires it.[536] Older analog scopes are available at negligible cost and are recommended as learning instruments, with the single filter that the scope should be a triggered-sweep design rather than a recurrent-sweep one; learning the fundamentals on a simple instrument establishes what the display represents, after which a buyer can identify which digital features they actually require.[117] Jones answers the recurring beginner question of whether to buy a scope affirmatively, while noting he worked without one for years for cost reasons.[306]

## History and market

Before online instruction existed, scope operation was learned from the ring-bound manuals supplied with the instrument, which documented each control and the expected waveforms.[690] A first scope purchase in the 1980s was a dual-channel 20 MHz analog instrument at eight to nine hundred dollars, without delayed timebase.[117]

Sub-thousand-dollar digital scopes went from unavailable to commonplace over roughly five years to 2012, reaching the $250–300 range.[127] By 2013 a 100 MHz instrument could be bought secondhand for around two hundred dollars.[148] Entry-level four-channel scopes of the $400 class could be unlocked to 200 MHz.[606] By 2025 roughly a thousand dollars bought a four-channel instrument of 800 MHz to 1 GHz bandwidth with deep memory and a two-channel 100 MHz generator.[710]

Terminology diverged between analog and digital generations: the analog sweep speed control is the digital horizontal scale.[117]

Jones read Agilent's restructuring as a retreat from the low end rather than from research-grade instruments, on the basis that it cannot compete on price.[164] He also argued that a heavily promoted Tektronix launch had been preceded on specifications by a LeCroy instrument that received little attention.[347] Jeri Ellsworth described a recurring trade-show pattern of being condescended to about basic instrument function, and a practice of allowing it to continue before asking a specialist question.[35]

## Further reading

- [Agilent is changing names](http://www.agilent.com/about/newsroom/presrel/2013/19sep-gp13016.html) — via #164
- [Siglent entry level 200 MHz - Teardown](https://www.eevblog.com/forum/blog/eevblog-985-siglent-sds1202x-e-oscilloscope-teardown/) — via #347
- [Nash Reilly](https://cushychicken.github.io/) — via #474
- [Blog post about emissions](https://cushychicken.github.io/signal-integrity/) — via #474
- [Staying well grounded](https://www.analog.com/en/analog-dialogue/articles/staying-well-grounded.html) — via #474
- [Logic probe](https://en.wikipedia.org/wiki/Logic_probe) — via #600
- [Joulescope](https://www.joulescope.com/) — via #677
- [Martin Rowe of EE World](https://www.eeworldonline.com/author/mrowe/) — via #714
- [Kenneth Wyatt](https://benchtopemc.com/) — via #714
- [Dave has a take on it here](http://www.eevblog.com/forum/testgear/new-2ghz-touchscreen-scope-from-tek-june-6th/msg1227211/#msg1227211) — via #347
- [his talk at Supercon and the associated article on Hackaday.com](https://hackaday.com/2019/02/18/electron-microscopes-are-awesome-everything-you-didnt-know-you-wanted-to-know/) — via #431
- [the Black Magic book](https://www.amazon.com/High-Speed-Digital-Design-Handbook/dp/0133957241) — via #474
- [Analog Discovery Pro](https://digilent.com/shop/analog-discovery-pro-3000-series-portable-high-resolution-mixed-signal-oscilloscopes/) — via #567
- [What kind of scope can I get for $30k?](https://www.eevblog.com/forum/testgear/what-is-the-best-oscilliscope-that-i-can-get-for-$30-000/) — via #567
- [Analog Discovery 2](https://digilent.com/shop/analog-discovery-2-100ms-s-usb-oscilloscope-logic-analyzer-and-variable-power-supply/) — via #600
- [asked on his forum](https://www.eevblog.com/forum/testgear/is-a-rigol-mso5000-overkill-for-a-hobbyist/100/) — via #606
- [How did you learn about oscilloscopes without the internet](https://www.eevblog.com/forum/beginners/retired-engineers-how-did-you-learn-using-oscilloscope-in-80s-without-internet!/?topicseen) — via #690

## References

| Episode | Title | URL |
|---|---|---|
| 18 | Transistor Types and Where To Get Electronic Gear | https://theamphour.com/the-amp-hour-18-transistor-types-and-where-to-get-electronic-gear/ |
| 20 | Military Electronics and The Free Eagle (Freagle) Campaign | https://theamphour.com/the-amp-hour-20-military-electronics-and-our-first-wotws/ |
| 35 | An Interview with Jeri Ellsworth - The Ternary Tussle | https://theamphour.com/the-amp-hour-35-the-ternary-tussle/ |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ |
| 148 | Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood | https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/ |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ |
| 190 | Let's Hear It For The Buoys - Vanishing Vessel Vexation | https://theamphour.com/190-lets-hear-it-for-the-buoys-vanishing-vessel-vexation/ |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ |
| 269 | Be Tidy | https://theamphour.com/269-be-tidy/ |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ |
| 306 | Catalyzing Change Agents | https://theamphour.com/306-catalyzing-change-agents/ |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ |
| 431 | An Interview with Adam McCombs | https://theamphour.com/431-an-interview-with-adam-mccombs/ |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ |
| 481 | An Interview with Paul Thompson | https://theamphour.com/481-an-interview-with-paul-thompson/ |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ |
| 536 | NFT Schematics | https://theamphour.com/536-nft-schematics/ |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ |
| 701 | Electric Propulsion with Todd Bailey | https://theamphour.com/701-electric-propulsion-with-todd-bailey/ |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ |
| 714 | The Measurement Blues with Martin Rowe | https://theamphour.com/714-the-measurement-blues-with-martin-rowe/ |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ |
