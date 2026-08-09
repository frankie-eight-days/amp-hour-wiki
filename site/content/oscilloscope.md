---
title: Oscilloscope
concept: oscilloscope
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

An **oscilloscope** is an electronic test instrument that plots signal voltage against time, giving a direct view of the waveform of an electrical signal.[613] It is the principal instrument for observing what a circuit is actually doing, and effective use of one requires understanding how the instrument itself distorts the view it presents.[289] The product category spans an extreme range: from USB-connected front ends and four-channel bench instruments around four hundred dollars to gigahertz-class real-time instruments at twenty-five thousand dollars and beyond, with the top of the market reaching a million dollars per unit.[606][347][236] Oscilloscopes are sufficiently central to weapons-relevant measurement that high-bandwidth models are export-controlled.[119]

## History

Early wartime radar sets such as the SCR-270 presented their output on an oscilloscope screen showing range and amplitude only, with all interpretation left to the operator.[729] The Tektronix 511 was that company's first oscilloscope; the later 556 was a dual-beam plug-in instrument whose two beams and two plug-in slots gave it unusual measurement flexibility.[119] Tektronix was vertically integrated to an unusual degree in that era, manufacturing its own cathode ray tubes and even supplying ceramic terminal strips and matched silver solder with its instruments.[421]

Consumer and kit oscilloscopes of the period, including Hickok, Heathkit, RCA and Eico models, commonly used a free-running rather than a triggered sweep, and typically reached only around 100 kHz of bandwidth with roughly six active devices.[424][655] Analogue oscilloscopes divide into recurrent-sweep instruments, which free-run, and triggered-sweep instruments; the recurrent-sweep class is far less useful.[117]

In the late 1970s Tektronix developed a purely analogue 1 GHz oscilloscope to order for the United States Atomic Energy Commission's nuclear weapons testing programme, at roughly 30,000 dollars per unit with a committed order of a thousand units and the right to sell the instrument commercially afterwards.[119] The export restrictions still applied to high-bandwidth oscilloscopes trace to that era, when the reason to want a very fast scope was nuclear or weapons instrumentation rather than communications.[119]

The micro-channel plate CRT, marketed by Tektronix as "bright-eye" and fitted to a small number of models including the 2467, placed an electron multiplier at the face of the tube that amplified beam electrons roughly ten thousand times before they struck the phosphor.[117] Hybrid instruments were also built with a genuine analogue front end and a button switching the same signal path into a basic megasample digital storage mode.[229]

Digital storage transformed the instrument. Before it, recording a trace meant photographing the screen with a Polaroid camera; analogue storage scopes existed but were priced for well-funded laboratories, and routine single-shot capture arrived only with digital storage.[600][690] Acquisition memory moved from 2K samples being respectable and 8K commanding an extreme price to a megapoint in a 300-dollar instrument.[119] Support for writing captures to USB mass storage reached bench oscilloscopes only around the mid-2000s, because the file-system and USB host stack that a general-purpose operating system provides had to be built from scratch on an embedded platform.[325]

Over roughly two decades the oscilloscope's role shifted from a visualisation and timing-measurement tool to an analysis platform expected to perform compliance measurement against standards, jitter decomposition, and frequency- and modulation-domain analysis in one instrument.[117]

## Principles of operation

### Display and acquisition

A conventional oscilloscope displays voltage against time, in contrast to a spectrum analyzer (amplitude against frequency) or a modulation domain analyzer (frequency against time).[613] In an analogue instrument the CRT beam is deflected electrostatically by plates rather than by the deflection coils used in television, because electrostatic deflection is much faster and more precise.[669]

A digital oscilloscope's acquisition is inherently discontinuous: it triggers, captures for a window, and is blind until it re-arms.[607] Memory depth and sample rate together fix the capture window — 100 megasamples at one terasample per second is 100 microseconds of record.[600] Where analogue delayed sweep expanded a region downstream of the trigger using a second, faster time base started after a dialled-in delay, a digital instrument instead relies on capture memory deep enough to hold the region of interest, which is then zoomed in software; only a small number of digital instruments retain two independent time bases with independent triggering.[690]

### Bandwidth and vertical resolution

The bandwidth needed to reproduce a given edge is approximately 0.35 over the 10–90 percent rise time, since the harmonics of a fast edge remain significant well above the fundamental.[252] The rule assumes a brick-wall response with zero amplitude above the bandwidth; a real front end rolls off gradually, so the figure is an approximation whose error depends on the instrument's actual response shape.[252]

General-purpose digital oscilloscopes almost universally use 8-bit converters; high-resolution modes recover an effective 10 to 12 bits by oversampling and averaging, at reduced bandwidth.[106] Higher native resolution has since reached the high end: the Tektronix 6 series, built on two in-house ASICs, provides 6.25 gigasamples per second per channel at 12 bits, and the LeCroy HDO8000A preceded it by two months with eight 12-bit channels at 10 gigasamples per second.[347] A 14-bit acquisition path adds spectral dynamic range: a signal below fifteen microvolts was recovered from the noise floor on a 14-bit instrument where a 12-bit instrument showed nothing under identical conditions, and a leading-edge 14-bit converter at 1 GHz is delivered as a hybrid module combining several processes rather than as a single die.[677]

Vertical sensitivity on a general-purpose bench scope bottoms out near 500 microvolts per division, because the inherent noise of the front end at high bandwidth into a 1 megohm input sets the floor.[87] The LMH6518 variable-gain amplifier, containing the differential and variable-gain stages, sits in the front end of almost every modern oscilloscope and was originally specified to handle 400 millivolts of input offset, which is what supports the front-panel vertical position control.[727]

### Triggering

Triggering exists because acquisition memory is finite: continuous capture at the rate needed to see a microsecond-scale event over days produces unusable volumes of data, so the instrument discards everything not associated with the qualifying event, and oscilloscopes default to 50 percent pre- and post-trigger capture so the operator sees what happened before the event as well as after.[510] An oscilloscope has a single trigger point shared by all channels, so only signals synchronous with the trigger source stand still; two inputs differing by one hertz give one stable trace and one travelling across the screen at a one-hertz rate.[145]

### Front end and processing

Where measurements are computed in software rather than in acquisition hardware, enabling one can collapse throughput: on one instrument a single horizontal frequency measurement took the waveform update rate from a million per second to under a thousand, while vertical measurements cost nothing.[619] Implementing serial decode, FFT and measurement functions in a custom acquisition ASIC allows them to run without reducing update rate, which is the practical reason a vendor develops its own silicon.[619]

Extending real-time bandwidth past 100 GHz depends on III-V semiconductor processes — indium phosphide heterojunction bipolar and high-electron-mobility transistor technology — whose wafers and chips are expensive, placing that capability with vertically integrated owners of the process.[98] The Keysight UXR reaches a true 110 GHz of real-time bandwidth on all channels at 256 gigasamples per second using an indium phosphide front end rather than an equivalent-time sampling architecture.[404]

Fast front ends are fragile and expensive to repair, and protection circuitry that disconnects the delicate stages on excess voltage or power dissipation, with a panel light indicating it has acted, is a deliberate design feature.[459]

## Probing

Probes, not the mainframe, set the practical bandwidth of a high-bandwidth scope: a 1 GHz instrument cannot reach its specification through the supplied 10:1 passive probe, and the active probe that can may cost on the order of the scope itself — a good FET probe can exceed the price of the instrument it plugs into.[76] For the same reason, buying a general-purpose scope much beyond two to three hundred megahertz is questionable when the supplied passive probes will not reach that bandwidth; a 10:1 passive probe rated to 1 GHz has been made by essentially one manufacturer.[567]

Probes must be compensated against a clean, fast edge or every measurement made through them is degraded, a step routinely skipped. At Tektronix, John Addis built a very fast, very clean square-wave source into the front panel of scopes such as the 485, removing the need for a separate pulse generator.[459]

Probes are microphonic: the piezoelectric effect is present in essentially every probe, so mechanical stimulation of the probe body produces a signal at the input with an orientation dependence.[38] Coaxial cable also generates charge when flexed — triboelectric noise — so moving a probe puts a visible blip on the screen, and the same effect corrupts measurements from charge-output sensors such as accelerometers.[215]

A one-kilohm series resistor into a 50-ohm terminated scope input makes a 20:1 divider whose input impedance is high and broadband, isolating the cable's capacitance and inductance from the circuit under test.[474] Connecting any oscilloscope loads the circuit, and a circuit that works only while probed is usually one whose oscillation the probe's impedance is damping; RF test equipment avoids this by defining a common 50-ohm system impedance.[533]

## Grounding, isolation and safety

The BNC shells of a mains-powered bench oscilloscope are bonded to mains earth, so clipping the ground lead to any node not at earth potential shorts that node to earth through the instrument; this is the standard mechanism by which scopes and circuits are destroyed during work on mains-referenced equipment, and it is why battery-powered floating scopes are used for service work.[20] The earth path can carry considerable current, so even 5-volt or 3.3-volt rails can be damaged if the ground lead lands on them.[527] Working on deliberately floating electronics is straightforward until it must be measured, because almost every bench oscilloscope and bench multimeter is earth-referenced; handheld instruments are the usual way out.[274]

The safe default when a measurement must be taken off earth reference is to isolate the power supply rather than to lift the earth on the oscilloscope or laptop.[307] Measuring current through an inline shunt with an oscilloscope runs into the same problem — neither end of the shunt is at the scope's earth reference — and doing it correctly requires a true differential probe or differential current probe costing more than a dedicated current-measurement instrument.[607] An isolated instrument instead splits into a control side that talks to the host and a sensor side that performs the measurement, with the barrier crossed by a transformer for power and decoupled signal paths; measurement, auto-ranging and statistics can run on an FPGA on the isolated side so only summary data crosses.[527]

In high-current converter work, the dead time between switch pulses must be measured on a scope because overlap destroys the bridge, and the measurement is taken directly on the IGBTs using high-voltage probes with either isolated probes or an isolation transformer on the instrument.[522] In electron-microscope service, where rails run at thousands of volts, an arc-over inside a high-voltage tank destroys scope input channels, and oscilloscopes in that field are treated as consumables; on Adam McCombs's microscope work, lost channels were routine.[431]

## Instrument classes

### Bench and PC-based instruments

The useful distinction between a bench scope and a PC scope is form factor rather than capability: a bench instrument is a self-contained box with its own screen, while a PC scope has no display or controls of its own.[516] A traditional bench oscilloscope contains a complete embedded computer because it must both capture and display data; headless USB-connected instruments delete that computer and push display and processing onto the host.[527] Omitting knobs, screen and enclosure removes substantial cost, and a host-connected instrument can stream continuously to disk for data logging and offer channel counts a bench instrument does not, at the price of much lower sample rates.[87] A USB instrument faces a fundamental architecture choice between continuous streaming at whatever rate the bus sustains and a much higher sample rate with local triggering and capture memory read out slowly over the bus; the choice determines whether the device is a data logger or an oscilloscope.[198]

Early tablet-tethered mixed-signal instruments paired a single analogue channel of roughly 12 megasamples per second with four digital inputs, the phone or tablet supplying display and interface.[41] The roughly 200-dollar Analog Discovery pairs a 125-megasample 14-bit converter with a 1-megohm input rated to 20 volts and 250 microvolts per division.[106] The OpenScope, built on a Microchip PIC32MZ, combined two roughly six-megasample channels at up to 3 MHz analogue bandwidth with a waveform generator and logic analyzer, served to a browser over Wi-Fi.[302] Thunderscope, which grew out of a 2020 hardware contest project, presents a four-channel oscilloscope front end to a host over Thunderbolt as a PCI Express device.[627] The open-source Sigrok layer talks to multimeters and oscilloscopes for real-time capture across many vendors' hardware on Windows, Linux and macOS.[665] Remote or tablet control adds little to a bench oscilloscope because the operator is holding probes on the circuit and is always within arm's reach of the front panel.[122]

### Sampling oscilloscopes

In an equivalent-time sampling oscilloscope the bandwidth is set entirely by the front-end sample-and-hold, which captures the signal in a window of order ten picoseconds and holds it; the conversion afterwards can be arbitrarily slow, so a ten-cent microcontroller ADC suffices behind a 10 GHz front end.[178] A cheap sampling front end typically has no attenuator and only a 50-ohm SMA input, so probing a high-impedance source requires an active probe costing many times the instrument, and without one the fast edge the instrument exists to capture is rounded off.[178]

### Adjacent and hybrid instruments

A mixed-domain oscilloscope is defined by synchronous capture across the time and frequency domains; a later cost-reduced model in one such family kept the name but removed that capability, so its spectrum and waveform captures cannot be tied together in time.[186] A logic analyzer's timing mode is an oscilloscope with one-bit vertical resolution, sampling asynchronously at a fixed rate and rendering square transitions, and the analogue input on a device such as the Saleae Logic 4 reaches only around six megahertz on a single channel, supplementing rather than replacing an oscilloscope.[436][355] A dynamic signal analyzer is an FFT instrument working in the frequency domain, differing from a spectrum analyzer in targeting very low, typically audio, frequencies.[570] A vector network analyzer returns magnitude and phase directly; the same sine waves can be seen on an oscilloscope, but extracting magnitude and phase from them is difficult, which is the practical reason for the separate instrument.[533] A significant class of instruments marketed as multimeters or oscilloscopes are data loggers built around a 16-bit converter, specified by accuracy rather than digits or bandwidth, and should be assessed on the logging specification.[199] Instruments intended for long-duration energy measurement must stream without the trigger-and-rearm gaps inherent to an oscilloscope.[607]

## Measurement practice

For an unfamiliar signal on an unfamiliar oscilloscope, Vincent Himpe's procedure is to set the fastest time base, apply the signal, and slow the time base until something appears, which guarantees the display is never undersampled; modern instruments with a built-in frequency counter warn of undersampling directly.[169] Linear Technology application note 47 contains a full tutorial on oscilloscopes, probes, connections and grounding, and Kent Lundberg treated it as the standard reference for a student who cannot get a clean trace, since most such failures are instrumentation and grounding problems rather than circuit problems.[119]

The debugging order for a non-working serial bus is physical layer first: scope the lines to confirm pull-ups and clean edges, then check addressing and enables, and only then question the protocol implementation.[274] The scope shows the asymmetry between totem-pole outputs (SPI and most digital outputs) and open-collector I2C directly — a near-instant fall and an RC-shaped rise set by the pull-up resistor.[274] When a scope will not decode a serial stream at the configured rate, the assumption to check is the rate itself: measure the bit period on screen and calculate the actual clock.[551] Clean edges on a scope do not confirm correct protocol behaviour; the scope answers the analogue question while a logic analyzer with protocol decode answers the framing and content question.[396] Probing a vehicle diagnostic port shows only the raw digital waveform: CAN bus, mandated for vehicle communications since about 2009, cannot be interpreted from the analogue trace without protocol decode.[388]

Other established scope techniques include compensating a control loop empirically by injecting a square wave at the input and adjusting until the scoped output is rounded with no overshoot;[377] measuring a switching regulator's switching frequency under several loads to establish whether it is fixed or variable before designing a filter;[360] tuning mid-bus terminators by watching the waveform and minimising overshoot, a practice Lee Felsenstein describes from early computer-bus work;[684] and observing DAC quantisation steps directly by probing an arbitrary waveform generator's output at high vertical gain, which is why reconstruction filters are fitted.[278] An intermittent fault traced to a lifting bond wire inside a diode was caught only by monitoring every rail continuously on about eight channels across two oscilloscopes — a fault that appears between spot measurements cannot be found by spot measurement.[551] A JTAG port left enabled gives a usable improvised scope: boundary scan in bypass mode shifts bits through at up to a few hundred megahertz, sampling pin states with no external instrument.[693] A power supply intended for harsh service is qualified by deliberately short-circuiting its output with a screwdriver repeatedly while watching the recovery on a scope, then re-running the full acceptance suite.[701] Putting a scope across the grounds of two powered boards demonstrates that the two grounds move relative to each other; differential signalling absorbs a volt or two of common-mode difference, adequate between adjacent boards but not over a hundred-foot run.[704]

## Failure modes and limitations

A circuit oscillating above the oscilloscope's bandwidth produces no trace but wrong voltage readings and nonsensical waveforms; damping the suspect nodes by touch, then soldering in a few picofarads of capacitance between them, both confirms and cures it — a diagnosis Alan Wolke describes from practical debugging.[117] Instrument documentation specifies capability and is silent on limits, so the measurement error mode that matters is the one outside the stated envelope.[117] There is no known-perfect oscilloscope at the top of the bandwidth range: a published study applying one input to nine of the fastest sampling oscilloscopes in the world produced nine visibly different results, so at those speeds the instrument's own response must be characterised and removed from the measurement.[465] An oscilloscope's bandwidth can be verified on the bench with a known fast edge and the reproduced rise time, a technique documented in Jim Williams's application notes.[465] Developing fast instrumentation is bootstrapped — verifying a fast front end requires a faster instrument than the one being built — and Ted Yapo's project walked through a 300 MHz scope, a used 1 GHz unit and a 20 GHz sampling head in under a year.[465]

Specific hazards include a trailing-edge dimmer case in which transformer-secondary inductance produced an 800-volt spike at turn-off that destroyed an internal PCB-mount mains supply, found by scoping the incoming mains;[524] encrypted links such as electric-vehicle CCS charging, which defeat the hang-a-scope-on-it diagnosis that works on an unencrypted bus;[524] and a silent redesign of a front-end amplifier that reduced input offset capability below the original 400 millivolts without a part-number change, bricking scopes through excessive front-end DC offset.[727] In a dual-processor system Bil Herd found a bus fault as a faint spike on one address line present only when the second processor drove the bus, the inactive processor forming an unterminated stub — reading such a trace requires knowing which on-screen artefacts are normal.[222] A modern processor core rail is not a static voltage: it is commanded dynamically between roughly two volts and 0.3 volts and into sleep states, and a 15-to-20-watt part can demand 150-amp peaks within ten microseconds of waking.[566] A digital multimeter's AC accuracy typically applies only above about a tenth of full scale, so low-level AC measurement needs a dedicated AC millivoltmeter or an oscilloscope with a preamplifier front end.[464]

## Maintenance and repair

Intermittent or dead front-panel controls on an older scope are commonly failed rotary encoders, often from stored moisture ingress; the encoders are frequently generic catalogue parts, and manufacturers have supplied full service manuals on request, making the repair routine.[229] Serviceability falls off sharply with date of manufacture: between Tektronix scopes of the 1970s and those of the 1980s, complexity rose steeply with switching power supplies and proprietary custom ICs, and parts that no longer exist make the later ones much harder to repair.[655]

## Market structure

The entry-level oscilloscope bandwidth stayed at 25 MHz, later 50 MHz, for many years, because a manufacturer that unilaterally raises the low-end specification must build enough volume to supply the whole segment; Rigol broke the stasis by collapsing the price of its 100 MHz model to the 399 dollars of its 50 MHz model, making the lower-bandwidth unit obsolete overnight.[72] The Rigol DS1052E entered at eight hundred dollars, dropped to four hundred within a year or two, and later sold around 349 dollars; the floor on a bench scope's price is set by the enclosure, display, probes and silicon rather than the design.[455] Digital oscilloscopes went from nothing under a thousand dollars to capable instruments at 250 to 300 dollars within about five years.[127] The modern price ladder runs from a four-channel Rigol or Siglent around four hundred dollars, through an eight-hundred-dollar tier buying a larger touchscreen, higher sample rate and more memory, to four-figure instruments; the traditional entry price of eight hundred dollars bought a dual-channel 20 MHz analogue instrument in the 1980s.[606]

Oscilloscope vendors sell sample memory, serial decode and bandwidth as separately licensed options on hardware that already contains the capability, with bandwidth in particular limited in software below what the front end can do; some vendors state the bandwidth models are physically different hardware when the boards are in fact identical.[117][136] The stated economic case is that leading-edge development is funded by margin on high-end features.[117] Because the firmware setting only configures hardware already present, the hardware can also be modified directly, and some scopes ship with unpopulated memory pads whose population converts the unit into a higher model.[339][434] The four-channel entry-level scopes sold around four hundred dollars carry hardware capable of 200 MHz and can be unlocked to it, and unlocking a 999-dollar four-channel instrument yields 800 MHz to 1 GHz of bandwidth with around 500 megapoints of memory plus a dual-channel 100 MHz signal generator.[606][710] Rigol committed to a multi-year in-house ASIC programme after Siglent took the value position in the low-end market, then priced the result at 999 dollars against competition around double that.[710] Acquisition silicon has a long service life: one chip carried through a vendor's 1000 and 2000 series into the TBS basics line, a roughly 300-dollar scope sold largely into school laboratories.[646]

At the top of the market, instruments reach a million dollars, at which point demonstration units are not shipped to prospective customers, and the systems needed to test, calibrate and qualify a gigahertz-class scope are themselves major instruments whose cost scales sharply with bandwidth.[236] High-value manufacture does not follow offshoring logic: at fifty to a hundred thousand dollars per unit the labour content is negligible against calibration, qualification and volume, so production stays where the engineering is.[236] The incumbent high-end makers have retreated from the low end, where they cannot compete on price, because the margin that funds work such as 80 GHz front ends is at the top of the range.[164] Test equipment must also lead the technology it measures: each new serial data rate requires an oscilloscope fast enough to see it before the first silicon exists, and the maker must be able to prove the display is correct.[714] A high-end oscilloscope is sold as a compliance instrument rather than a waveform viewer — automated analysis of high-speed serial signals against a standard such as SATA, including jitter decomposition over billions of measurements — with the analysis software typically a costly extra.[104] Real-time bandwidth above 100 GHz lets a 50 GHz transmitter be sampled live and its modulation analysed in the instrument, with customers largely in high-speed serial links inside FPGAs and similar silicon.[404] The design techniques inside classic HP, Agilent, Keysight and Tektronix instruments were deliberately scattered across application notes, schematics and patents rather than documented in one place.[459]

Second-hand markets are badly mispriced at the edges: a 300 MHz four-channel Tektronix DPO4034 with probes plus a Fluke 87 multimeter, a combination listing near ten thousand dollars new, has sold for five hundred dollars on a local classifieds site.[18] Institutional purchasing is governed by which budget the money comes from: rental at two hundred thousand dollars a year can be approved where a fifty-thousand-dollar capital purchase cannot, and field-upgradeable bandwidth suits capital-expenditure thresholds by letting a lower-specification instrument clear approval now with licence upgrades bought a year at a time.[136][145] Educational sales are won by supplying courseware that removes the lecturer's preparation effort, and for teaching laboratories the selection criteria are warranty and replacement support, the supplied teaching material, and whether the same model will still be purchasable in ten years so that lab notes remain valid.[189][170]

Purchasing guidance in the practitioner literature converges on a few rules: buy the cheapest option until it demonstrably will not do the job, since most work uses only base functionality and the real limitation announces itself clearly;[18] a near-free older analogue scope is a rational first instrument because it teaches the fundamentals, after which the buyer can name the specific features the next instrument must have;[117] about 10 MHz of bandwidth is enough for a beginner, with USB scope families offering an upgrade path;[549] a first instrument should be a model many other people own, because community knowledge is the only support available and the bottom of the market brings noise, instability and aliasing artefacts a beginner cannot distinguish from circuit faults;[567][606] and for a shared laboratory, ten 100 MHz oscilloscopes serve better than one 1 GHz instrument, since gigahertz bandwidth serves only a handful of specialists.[287] Bandwidth that will not be used daily should be bought second-hand rather than new, and before buying bandwidth to see the analogue behaviour of a fast digital signal the question to settle is whether a logic analyzer answers the actual question.[606] The case for owning more than one oscilloscope is concurrent measurement — motor work may need a channel on every winding.[545]

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

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 18 | Transistor Types and Where To Get Electronic Gear | https://theamphour.com/the-amp-hour-18-transistor-types-and-where-to-get-electronic-gear/ | |
| 20 | Military Electronics and The Free Eagle (Freagle) Campaign | https://theamphour.com/the-amp-hour-20-military-electronics-and-our-first-wotws/ | |
| 38 | An Interview with Jeff Keyzer - Comical Keyzer Comes a-Callin' | https://theamphour.com/the-amp-hour-38-comical-keyzer-comes-a-callin/ | |
| 41 | An Interview with Jeff Keyzer - Exhilarating ESC Escapades | https://theamphour.com/the-amp-hour-41-exhilarating-esc-escapades/ | May 4, 2011 |
| 72 | Kismetic Keithley Katowse | https://theamphour.com/the-amp-hour-72-kismetic-keithley-katowse/ | |
| 76 | Fremescent Floccose Fortification | https://theamphour.com/the-amp-hour-76-fremescent-floccose-fortification/ | January 2, 2012 |
| 87 | An Interview with Ian Daniher - Nascent Nonolith Numquid | https://theamphour.com/the-amp-hour-87-nascent-nonolith-numquid/ | |
| 98 | Proemial Passive Poiesis | https://theamphour.com/the-amp-hour-98-proemial-passive-poiesis/ | June 3, 2012 |
| 104 | Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia | https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/ | July 15, 2012 |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 117 | An Interview with Alan Wolke (Re-broadcast) | https://theamphour.com/117-an-interview-with-alan-wolke-re-broadcast/ | August 23, 2021 |
| 119 | An Interview with Dr. Kent Lundberg - Luculent Linear Legacy | https://theamphour.com/the-amp-hour-119-luculent-linear-legacy/ | October 28, 2012 |
| 122 | Processors, CEOs & Soldering irons - Plentiful Perfunctory Programs | https://theamphour.com/the-amp-hour-122-plentiful-perfunctory-programs/ | November 19, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 136 | Hardware, Surveys and Giveaways - Radular Rental Ranting | https://theamphour.com/the-amp-hour-136-radular-rental-ranting/ | March 12, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 164 | Agilent's New Name, Molex's New Owner and PCB artwork - Nonsensical Naming Neolatry | https://theamphour.com/164-agilents-new-name-molexs-new-owner-and-pcb-artwork-nonsensical-naming-neolatry/ | September 23, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 170 | What defines an engineer? - Job Judging Jeremiad | https://theamphour.com/170-what-defines-an-engineer-job-judging-jeremiad/ | November 4, 2013 |
| 178 | A 2013 Recap - Year-end Yarn Yakking | https://theamphour.com/178-a-2013-recap-year-end-yarn-yakking/ | December 30, 2013 |
| 186 | Someone is watching...we think - Horme Hostility Hypochondriac | https://theamphour.com/186-someone-is-watching-we-think-horme-hostility-hypochondriac/ | February 25, 2014 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 198 | Mike Ossmann Returns! - Planetic Portalab Packaging | https://theamphour.com/198-mike-ossmann-returns-planetic-portalab-packaging/ | May 12, 2014 |
| 199 | The 2014 Maker Faire Show - Traveling Technology Trangam | https://theamphour.com/199-the-2014-maker-faire-show-traveling-technology-trangam/ | May 19, 2014 |
| 215 | Wrong Hardware, Wrong Software - Fugacious Fan Funding | https://theamphour.com/215-wrong-hardware-wrong-software-fugacious-fan-funding/ | September 7, 2014 |
| 222 | An Interview With Bil Herd - Zany Z80 Zygology | https://theamphour.com/222-an-interview-with-bil-herd-zany-z80-zygology/ | October 27, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 252 | An Interview with Eric Bogatin - Tilded Thumb Tenets | https://theamphour.com/252-an-interview-with-eric-bogatin-tilded-thumb-tenets/ | June 2, 2015 |
| 274 | Our First Call In Show | https://theamphour.com/274-our-first-call-in-show/ | November 4, 2015 |
| 278 | Our Second Callin Show(ish) | https://theamphour.com/278-our-second-callin-showish/ | December 16, 2015 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 289 | Documentation Is A Waste Of Time | https://theamphour.com/289-documentation-is-a-waste-of-time/ | March 2, 2016 |
| 302 | An Interview with Clint Cole of Digilent | https://theamphour.com/302-an-interview-with-clint-cole-of-digilent/ | June 8, 2016 |
| 307 | Call In Show #5 | https://theamphour.com/307-call-in-show-5/ | July 13, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 339 | Look at nature and meet nerds | https://theamphour.com/339-look-at-nature-and-meet-nerds/ | March 12, 2017 |
| 347 | Re-scoping the problem | https://theamphour.com/347-re-scoping-the-problem/ | June 13, 2017 |
| 355 | The Internet of Septage (with Akiba) | https://theamphour.com/355-the-internet-of-septage-with-akiba/ | August 13, 2017 |
| 360 | A Total 360 | https://theamphour.com/360-a-total-360/ | September 18, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 388 | An Interview with Earl Sharpe and Collin Kidder | https://theamphour.com/388-an-interview-with-earl-sharpe-and-collin-kidder/ | April 15, 2018 |
| 396 | The Synergy Bus | https://theamphour.com/396-the-synergy-bus/ | June 10, 2018 |
| 404 | Proof Of Blink | https://theamphour.com/404-proof-of-blink/ | August 26, 2018 |
| 421 | The Legend of Keyzermas | https://theamphour.com/421-the-legend-of-keyzermas/ | December 23, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 431 | An Interview with Adam McCombs | https://theamphour.com/431-an-interview-with-adam-mccombs/ | February 24, 2019 |
| 434 | Use The Protection Circuit | https://theamphour.com/434-use-the-protection-circuit/ | March 17, 2019 |
| 436 | Downward Sloping Trace | https://theamphour.com/436-downward-sloping-trace/ | March 31, 2019 |
| 455 | Bill and Dave's Excellent Equipment | https://theamphour.com/455-bill-and-daves-excellent-equipment/ | August 19, 2019 |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 464 | KonnectorPanik | https://theamphour.com/464-konnectorpanik/ | October 27, 2019 |
| 465 | An Interview with Ted Yapo | https://theamphour.com/465-an-interview-with-ted-yapo/ | November 3, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 533 | Microwave measurement with Joel Dunsmore | https://theamphour.com/533-microwave-measurement-with-joel-dunsmore/ | March 7, 2021 |
| 545 | Fear of Banjos | https://theamphour.com/545-fear-of-banjos/ | June 6, 2021 |
| 549 | Creative Engineering with Shrouk El-Attar | https://theamphour.com/549-creative-engineering-with-shrouk-el-attar/ | July 11, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 566 | Switching Converter Engineering with Carmen Parisi | https://theamphour.com/566-switching-converter-engineering-with-carmen-parisi/ | November 14, 2021 |
| 567 | The Rodeo Drive of Electronics | https://theamphour.com/567-the-rodeo-drive-of-electronics/ | November 21, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 600 | The Custodial Arts | https://theamphour.com/600-the-custodial-arts/ | August 21, 2022 |
| 606 | Professional Scooter Charger | https://theamphour.com/606-professional-scooter-charger/ | October 23, 2022 |
| 607 | The Joulescope Upgrade with Matt Liberty | https://theamphour.com/607-the-joulescope-upgrade-with-matt-liberty/ | October 30, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 627 | Works on my machine | https://theamphour.com/627-works-on-my-machine/ | April 9, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 655 | The Twelfth Day of Keyzermas | https://theamphour.com/655-the-twelfth-day-of-keyzermas/ | January 8, 2024 |
| 665 | Really long needle nose pliers | https://theamphour.com/665-really-long-needle-nose-pliers/ | April 24, 2024 |
| 669 | Freelance PCB Design with Petr Dvorak | https://theamphour.com/669-freelance-pcb-design-with-petr-dvorak/ | June 6, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ | |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11, 2025 |
| 693 | Small Scale Electronics Manufacturing with Colin O'Flynn | https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/ | May 13, 2025 |
| 701 | Electric Propulsion with Todd Bailey | https://theamphour.com/701-electric-propulsion-with-todd-bailey/ | August 21, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 710 | Tugging on the Nerd Heartstring | https://theamphour.com/710-tugging-on-the-nerd-heartstring/ | December 6, 2025 |
| 714 | The Measurement Blues with Martin Rowe | https://theamphour.com/714-the-measurement-blues-with-martin-rowe/ | February 2, 2026 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1, 2026 |
| 729 | The Terahertz Frontier with Greg Charvat of Teradar | https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/ | July 22, 2026 |
