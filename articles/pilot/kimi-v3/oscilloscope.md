---
title: Oscilloscope
concept: oscilloscope
generated: 2026-08-08
model: kimi-k3
spec: knowledge-only-v3
---

An oscilloscope is the primary instrument for observing circuit behaviour directly rather than inferring it: it makes the time-varying state of a node visible.[289] Because the instrument itself conditions, samples and renders every signal it displays, interpreting a trace requires understanding how the scope distorts what it shows — probe loading, bandwidth limits, aliasing and trigger behaviour all shape the displayed result.[289][606]

Entry-level pricing has fallen continuously: sub-thousand-dollar digital scopes went from unavailable to commonplace over roughly five years to 2012, reaching the 250–300 dollar range; by 2013 a 100 MHz instrument could be bought secondhand for around two hundred dollars; and by 2025 roughly a thousand dollars bought a four-channel instrument of 800 MHz to 1 GHz bandwidth with deep memory and a two-channel 100 MHz generator.[127][148][710]

## Safety and grounding

Almost all bench scopes and bench multimeters are ground-referenced, which is what makes floating measurement difficult on standard bench equipment.[274] The BNC shells on a mains-powered bench scope are referenced to mains earth, so connecting the probe ground clip to a node at any other potential creates a direct fault path; this is the most common way beginners destroy a scope or a circuit.[20] Floating high-voltage measurement is performed with high-voltage probes plus an isolation transformer on the instrument, or with isolated probes.[522]

In high-voltage service work, scopes are treated as consumable items because channel damage from arc-over is routine.[431]

## Measurement practice

### Acquiring an unknown signal

An unknown signal is approached from the fastest timebase setting and dialled downward until a trace appears; this procedure guarantees the signal is never undersampled during the search.[169]

### Triggering

A scope has a single trigger point shared by all channels, so two signals at slightly different frequencies yield one stable trace and one trace drifting at the difference frequency. Alternate trigger mode resolves this; without it, viewing two unrelated signals stably requires two instruments.[145]

### Bus debugging

A dead bus is debugged from the physical layer upward: probe the line for pull-up and edge integrity first, then check device addressing, then the protocol layer.[274] The physical layer is worth inspecting first on I2C in particular because its edges are asymmetric by design — the line pulls low through a transistor almost instantaneously but rises through a resistor.[274] Assumed configuration values should be measured rather than trusted: a serial decode failure initially attributed to instrument settings proved to be an incorrect baud rate at the source.[551]

### Probing technique

A broadband high-impedance tap is built by terminating the scope input at 50 ohms and placing a series kilohm resistance ahead of it; this isolates the cable's capacitance and inductance from the node under test.[474] On a bus carrying signals in multiple directions, terminators have been placed mid-bus and adjusted while observing the scope to minimise overshoot.[684]

## Specifications and instrument architecture

Bandwidth beyond roughly 200–300 MHz is not useful on a general-purpose scope because the supplied passive probes cannot follow it.[567] Higher ADC resolution yields real sensitivity: a 14-bit instrument resolved a 15-microvolt signal out of the noise floor that a 12-bit instrument could not.[677] Whether measurement functions run in dedicated silicon or in software is invisible at purchase and dominates real throughput: enabling a single horizontal measurement on one instrument collapsed its waveform update rate by three orders of magnitude, from a million waveforms per second to under a thousand.[619]

The LMH6518 amplifier is used in the front end of most modern scopes; a silent revision of the part reduced its input offset capability without a part-number change, with reports of instruments bricked by excessive front-end DC offset.[727] Scope vendors must ship an instrument fast enough for each new serial data rate before the first silicon implementing it is produced, because test equipment has to exist before the technology it measures.[714]

## Selection and provisioning

A purchasing policy is to buy the cheapest instrument that remains usable and upgrade only when a real limit is reached.[18] For owned equipment, a disposal test applies: gear that would not be bought at its market value is sold.[18] For hobbyist use, the overkill threshold sits at four figures — a 400 dollar four-channel scope suffices indefinitely for general use and does not become obsolete.[606] Entry-level four-channel scopes of the 400 dollar class can be unlocked to 200 MHz.[606]

Bandwidth restrictions sold as a licence key have been defeated in hardware; the discovery is relevant when valuing lower-bandwidth SKUs.[339] Tiered pricing has a practical function beyond discounting: a lower entry price clears capital-expenditure approval thresholds that a full-featured instrument would not.[145]

Beginners are advised to buy an instrument others already own, so that community support exists when problems arise.[567] Pocket scopes are poor learning instruments because a beginner cannot separate instrument artefacts such as aliasing from genuine circuit behaviour.[606] Older analog scopes are available at negligible cost and serve as learning instruments, with a single filter — the scope should be a triggered-sweep design rather than a recurrent-sweep one.[117] Learning the fundamentals on a simple instrument establishes what the display represents, after which a buyer can identify which digital features they actually require.[117] Terminology diverged between generations: the analog sweep-speed control is the digital horizontal scale.[117]

A lab provisioning rule derived from the same bandwidth economics favours many mid-bandwidth instruments over one high-bandwidth instrument — ten 100 MHz scopes rather than a single 1 GHz scope.[287]

## Failure modes and field practice

- A dual-processor bus fault was located as a transient on address line A10 occurring only when the second processor drove the bus, caused by a PCB stub; recognising it required knowing what normal bus activity looks like.[222]
- An intermittent supply fault caused by a lifting bond wire inside a diode was caught only by monitoring every rail continuously across two scopes and eight channels.[551]
- Capturing gigabit Ethernet through a differential probe at one terasample per second yielded roughly a hundred microseconds of data — sufficient for only a few packets — illustrating the capture-length ceiling on deep-memory analysis of fast serial traffic.[600]
- Working on gigahertz-rate serialisers with a 100 MHz instrument rendered the measurements useless; the signals appeared as DC.[173]
- Space-hardware power supplies are qualified by repeatedly shorting the output with a screwdriver while observing recovery on a scope, with full test re-qualification expected afterwards.[701]
- Electric fence energiser waveforms were characterised in the field at Kruger National Park by observing the fence through attenuators.[481]

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
|---------|-------|-----|
| 18 | Transistor Types and Where To Get Electronic Gear | https://theamphour.com/the-amp-hour-18-transistor-types-and-where-to-get-electronic-gear/ |
| 20 | Military Electronics and The Free Eagle (Freagle) Campaign | https://theamphour.com/the-amp-hour-20-military-electronics-and-our-first-wotws/ |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ |
| 148 | Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood | https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/ |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ |
| 173 | An Interview with Jeri Ellsworth - Intense Illusion Introduction | https://theamphour.com/173-an-interview-with-jeri-ellsworth-intense-illusion-introduction/ |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ |
| 431 | An Interview with Adam McCombs | https://theamphour.com/431-an-interview-with-adam-mccombs/ |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ |
| 481 | An Interview with Paul Thompson | https://theamphour.com/481-an-interview-with-paul-thompson/ |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ |
| 701 | Electric Propulsion with Todd Bailey | https://theamphour.com/701-electric-propulsion-with-todd-bailey/ |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ |
| 714 | The Measurement Blues with Martin Rowe | https://theamphour.com/714-the-measurement-blues-with-martin-rowe/ |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ |
