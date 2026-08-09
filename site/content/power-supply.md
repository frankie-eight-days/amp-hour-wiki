---
title: Power Supply
concept: power-supply
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **power supply** is an electrical device or circuit that converts a source of electric power into the regulated voltages and currents required by a load. Nearly every circuit board carries one or more supplies, yet supply design is commonly absent from undergraduate curricula.[218] In embedded work the board-level task typically begins at a 5, 12 or 24 volt input — the AC-to-DC conversion itself being a commercial buy rather than a build — and steps down to the 3.3, 1.8 and 1.2 volt rails that logic families require.[704] The subject is a first-order design concern: the control loop is the central difficulty of a supply design,[377] and supply quality sets the performance of precision analogue circuits directly rather than as a second-order effect.[476]

## History

Early microprocessor systems required multi-rail linear supplies because the memory devices of the era were not single-voltage parts: an EPROM-based machine needed +12 V, −12 V and +5 V at many amps, all distributed to one processor board.[485] As logic families converged on single low-voltage rails, the supply problem shifted from generating many high-current rails from one unit to generating several tightly regulated low-voltage rails on each board.[485][704]

## Types and construction

### Linear and switch-mode

Linear supplies remain in use where regulation quality outweighs efficiency. Large laser installations still use linear supplies where current regulation matters: a 7-kilowatt current-regulated linear supply is practical, and removing the resulting heat is the dominant engineering problem.[521] At the other extreme, energy-efficiency requirements have driven the standby consumption of small commercial switch-mode mains supplies to around 0.1 watt.[39] Switching supplies pushed to higher speeds and powers have made power integrity a first-order design concern.[476]

### Bench and programmable supplies

No off-the-shelf integrated circuit provides an independently adjustable voltage and current bench-supply function that stays stable into all loads, which is why adjustable bench supplies are built discretely from operational amplifiers and transistors.[362] The constant-current behaviour is the difficult part of the design; a voltage-only output is straightforward by comparison.[360] Parts designed for unrelated purposes can sometimes be pressed into a supply role — a class-AB amplifier output driver driving the pass transistors from the positive or negative rail, with the remainder dissipated in the heat sink — but such substitutions must be breadboarded and measured rather than accepted from the data sheet.[362] A power operational amplifier intended for audio output stages, rated for roughly 120 watts, has been paralleled and reconfigured to serve as the pass element of a linear supply reaching about 700 watts of output.[315] A programmable supply channel can also be built as a digital-to-analogue converter followed by a power output stage: an I2C converter producing 0 to 4.96 volts feeding a power operational amplifier that scales and shifts it to ±8 volts, passing whatever current the upstream supply allows.[689]

A source measure unit is a controllable power supply that sources and measures simultaneously, which makes tasks such as tracing transistor curves routine.[78]

Some bench instruments switch their supply off by pulling a control input on the supply to ground, disabling the output while the supply itself stays energised, rather than breaking the mains input. Leaving the input capacitors charged avoids the inrush current surge that a mains switch produces at every power-on; repeated many times a day, that surge stresses the supply and shortens its life. The cost of the approach is continuous standby consumption.[39]

### Buy, build, and reuse

AC-to-DC conversion is a buy rather than build decision: thousands of qualified commercial options compete on price, so developing one internally rarely repays the time.[704] Building a bench supply is likewise no longer justified by cost: a conventional 30-volt, 3-amp linear bench supply can be bought for around fifty dollars, so a self-built instrument is worth the effort only where the requirement is genuinely niche — a reversal of the older situation in which home-built test equipment was the only affordable route.[229] The proposal to build hardware from drop-in library blocks — a shared power supply block taking 120 volts in and delivering 5 volts out, reused unmodified — has been attempted commercially and does not hold up: the blocks that circulate are the mediocre designs, and real requirements diverge from any fixed block.[163]

For most products, supply components should be chosen so that at least one part with a standard footprint is available from several manufacturers, keeping a second source available when one part goes obsolete.[532]

## Design constraints

### Control and regulation

The control loop is the central difficulty of a power supply design, and a hand-rolled loop should be expected to ring before it is characterised and compensated.[377] A supply covering a wide output range — 3 to 48 volts at high efficiency across the full current range — is a hard design, because regulation must hold against dynamic loads and across the inductance of the output wiring.[727] On the physical side, a simple bench power supply board does not justify four layers; needing four layers for a design of that complexity indicates a layout failure rather than a requirement.[128]

### Multi-rail digital systems

On a densely integrated digital board the supply can dominate the physical design: multi-rail supplies need a separate inductor per rail, and the inductors alone can occupy more board area than the FPGA or system-on-chip they feed, adding cost and efficiency loss with each rail.[156] High-end FPGA and processor vendors publish application notes running to a hundred pages on supply and bypassing for a single device, and still reduce their advice to a fixed ladder of capacitor values — 100 µF, 10 µF, 1 µF, 100 nF, 10 nF — per rail, because testing and modelling bypass networks properly is impractical outside specialised work. A large FPGA presents very large current steps at power-on as its internal SRAM is initialised, and with around twenty power pins the recommended per-rail ladder results in something like a hundred bypass capacitors beneath one device.[488]

Board-level power management chips constrain what rails a design can offer: the power management IC on the Raspberry Pi 4 does not reach 3.3 volts. The earlier compute module deliberately exposed multiple separate supply inputs so the integrator could generate rails as needed, at the cost of a more complicated board.[529] Where a design's power envelope is otherwise undefined, pinning maximum consumption to an existing standard's envelope — the USB 3.0 power budget, for example — gives a defensible target even where the design does not implement that standard's data side.[318]

## Distribution and protection

Supplies should be specified with headroom rather than to the calculated load: a 10-amp requirement is met with a 15- or 20-amp supply, on the principle that anything that can go wrong will, so only pleasant surprises remain.[135] Low voltage is not by itself a safety argument; the available current from the supply, not the rail voltage, determines whether a fault starts a fire. A large supply feeding many loads over long thin cabling is a fire risk rather than merely a reliability risk: a short at the far end of a Cat5 drop backed by a kilowatt-class supply will burn the cable. The remedy is graded protection — heavy distribution wiring split through polyfuses so that every stage is individually protected.[135]

Where many high-power loads share one supply, an interlock built into the communication protocol can bound the worst-case draw: on an installation of roughly 100-watt panels, the protocol carried a single field naming which panel was lit, so no data fault could turn on more than one panel and trip the supply, allowing the supply to be sized for one panel instead of all of them.[135] A large-installation power architecture of this kind runs one high-current supply into a splitter that re-distributes individually fused feeds: a 24-volt, 25-amp supply feeding twelve fused 5-metre drop cables, each carrying both 24-volt power and 100 kbaud TTL data to a load drawing about 2 amps.[294]

Enclosure design is part of fault containment. Instrument enclosures intended to survive an internal fault use a deep case seam to contain flame; cheap mains-powered supplies omit it, and a failure inside one can vent burning material out of the case.[539] Micro-cracks in a ceramic capacitor, produced by board flexure, generally fail short rather than open; across a supply rail able to deliver substantial energy, that failure produces flame rather than a quiet fault.[367]

## Failure modes and reliability

Electrolytic capacitors dominate supply-related failures. The service life of a retrofit LED lamp is set by its integrated driver rather than by the LED: the dominant failure is the electrolytic capacitors in the driver, degraded by heat trapped inside the lamp body.[71] Only a small overvoltage is needed to destroy an electrolytic: 20 volts across a 16-volt part builds internal pressure until it vents, and a high-current supply accelerates the failure, though small capacitors need very little power to boil their electrolyte.[580] On second-hand bench instruments of a certain vintage the bulk electrolytics in the supply are universally degraded — one design used around twenty 1000-microfarad capacitors, all leaking. The only external symptom is rails drifting out of specification, and many of the leaking parts still measure in specification, so such an instrument should be recapped on acquisition before the escaping electrolyte damages the board.[613]

Marginal regulator selection shows up as a population failure: a 5-volt regulator rated for 21 volts maximum input, fed from a 24-volt supply, ran outside its rating and failed in large numbers; fitting a correctly rated part is the standard repair.[490] A supply that measures correctly on the bench can still be the fault: rails tested good throughout a methodical repair, and the defect proved to be an intermittent bridge rectifier that only failed once it had heated up.[551] An amplifier's input offset voltage can depend on its supply rail without the data sheet documenting the dependence, producing an error found only by varying the rails during debugging.[146]

Single-board computers brown out readily on marginal supplies. A Raspberry Pi Zero 2 draws roughly 275 milliamps idle and close to 600 milliamps under load; the original Pi idled at around 2 to 2.5 watts, low enough to run from a 500-milliamp USB port.[565] A single-board computer's USB ports cannot be treated as a supply for peripherals with real current draw: WiFi adapters needing roughly 900 milliamps will not run from a 500-milliamp port and must be powered separately.[308]

Extreme power density forces unrelated functions onto the supply board and creates failure paths that have nothing to do with the power path: on a 1-kilowatt, 12-phase brick supply, the processor's main oscillator had been placed on the supply board, and that was the source of intermittent dropouts in a supercomputer rack.[604] A supply in constant-current mode connected to an electronic load in constant-resistance mode oscillates: the supply's current limit pulls the voltage down, the load responds by changing its draw, and the two fight each other in a hiccup cycle.[623]

Supply voltages should be the first item on a troubleshooting list and are commonly skipped, because a lit power indicator is taken as evidence that the rails are correct.[476]

## Noise and electromagnetic compatibility

Power system failures in otherwise digital designs are predominantly analogue and predominantly noise: buck converters generating switching noise couple into sensitive analogue front ends, or push radiated emissions past the FCC Part 15 limit. Powering a sensitive signal-processing front end from a switching converter is the classic instance of digital reasoning applied to an analogue problem.[704] A processor changing power mode alters the current drawn from its supply, and that current change couples back as conducted emissions; a firmware-driven mode change can therefore be the cause of a conducted-emissions failure.[184]

In an audio digital-to-analogue converter the output is a digital fraction multiplied by a reference voltage, and that reference is overwhelmingly the supply rail itself, so supply quality sets converter performance directly. Distortion faults in audio products are routinely traced back to the supply rather than to the signal chain.[476]

The board is a component of the circuit, and its layout is a component too: the same schematic built by two designers can measure differently.[476] USB signalling is pseudo-differential, swinging between 0 and 3.3 volts rather than about zero, so the two edges do not cross at exactly the same instant; the skew at each transition produces a common-mode spike, which is why common-mode chokes are fitted on USB lines.[645] A conducted-emissions pass is weak evidence about a product powered from an off-the-shelf plug pack, because the adapter's own filtering masks the product's noise; radiated emissions measure what the product and its cabling actually emit.[645] A bought-in module with full compliance markings can itself be the radiated-emissions failure and cannot be predicted from its documentation: after a week of filtering the custom boards of a charging dock, the failure was traced to a low-cost USB hub sourced outside distribution, which may itself have passed testing in a different configuration.[645]

## Test and bench practice

A bench supply output should be left isolated from earth by default and earthed only when a specific ground-system problem requires it, because an isolated output is the safer default when the supply is combined with earthed instruments such as an oscilloscope.[307] A two-person rule governs first power-up of expensive prototypes: a second engineer verifies the bench supply settings before the board is energised, because a single mistaken setting destroys a board carrying six figures of parts.[494]

A hard short is used as an acceptance test rather than avoided. On Todd Bailey's electric propulsion converter work, a screwdriver is jammed across the finished supply's output repeatedly while the recovery is watched on an oscilloscope, and the unit must then pass its full test sequence again.[701]

## Applications

The available current from a host port has shifted upward with USB-C: 1.5 amps at 5 volts, or 7.5 watts, is advertised by laptop ports and has displaced 500 milliamps as the assumed baseline for peripheral power.[340] Product designers treat the supply requirement as part of usability: each obstacle between unboxing a product and getting it working is estimated to cost about thirty percent of the people who would otherwise use it, so requiring an unusual supply the customer is unlikely to own — a 3.3-volt AC adapter, for instance — is exactly such an obstacle, and these are also the origin of most support calls.[232] Electronics kits are commonly shipped without a supply at all: wall-wart adapters are unusable by international recipients, batteries are heavy and restricted in shipping, so the recipient must determine the supply requirement themselves, which becomes part of what the kit teaches.[420]

In scientific instrumentation, an electron-beam column needs more than its high acceleration supply: auxiliary supplies deflect, focus and shape the beam through electrostatic and electromagnetic lenses, and noise on the acceleration voltage limits achievable resolution.[669] In spacecraft electric propulsion, the discharge converter — the supply that runs the ion beam — dominates the electronics board area and needs custom magnetics. One such converter runs from a 28-volt spacecraft bus, produces up to about 250 volts, and is throttleable across a 300 to 800 watt range, because efficiency across the throttled range is the figure of merit.[701]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 39 | Dan Pink, Dual Core, level translators - Mumble Mumbo Jumbo | https://theamphour.com/the-amp-hour-39-mumble-mumbo-jumbo/ | |
| 71 | An Interview with John Edmond - Luciferous LED Lucubrator | https://theamphour.com/the-amp-hour-71-luciferous-led-lucubrator/ | |
| 78 | Alteritous Andy's Absquatulation | https://theamphour.com/the-amp-hour-alteritous-andys-absquatulation/ | January 16, 2012 |
| 128 | Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge | https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/ | January 15, 2013 |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 146 | Hamvention, Arduino and Intel - Burdensome Background Battology | https://theamphour.com/the-amp-hour-146-burdensome-background-battology/ | May 21, 2013 |
| 156 | Tesla, FPGAs and DigiKey - Zesty Zippy Zynq | https://theamphour.com/the-amp-hour-156-zesty-zippy-zynq/ | July 29, 2013 |
| 163 | Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs | https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/ | September 16, 2013 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 294 | Live from Serbia with Mike Harrison | https://theamphour.com/294-live-from-serbia-with-mike-harrison/ | April 13, 2016 |
| 307 | Call In Show #5 | https://theamphour.com/307-call-in-show-5/ | July 13, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 340 | An Interview with Jason Cerundolo | https://theamphour.com/340-an-interview-with-jason-cerundolo/ | March 19, 2017 |
| 360 | A Total 360 | https://theamphour.com/360-a-total-360/ | September 18, 2017 |
| 362 | Secret Squirrel | https://theamphour.com/362-secret-squirrel/ | October 1, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 420 | An Interview with Joe Long | https://theamphour.com/420-an-interview-with-joe-long/ | December 16, 2018 |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ | January 26, 2020 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 488 | Sowing Discord | https://theamphour.com/488-sowing-discord/ | April 12, 2020 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 494 | The Two Person Rule | https://theamphour.com/494-the-two-person-rule/ | May 31, 2020 |
| 521 | Outdoor Laser Projection & Object Mapping with Daryl Tewksbury | https://theamphour.com/521-outdoor-laser-projection-object-mapping-with-daryl-tewksbury/ | December 13, 2020 |
| 529 | Embedded Hardware with the Raspberry Pi Team | https://theamphour.com/529-embedded-hardware-with-the-raspberry-pi-team/ | February 7, 2021 |
| 532 | Recalling Recalls | https://theamphour.com/532-recalling-recalls/ | February 28, 2021 |
| 539 | The King of Trash with Big Clive | https://theamphour.com/the-amp-hour-539-the-king-of-trash-with-big-clive/ | April 26, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 623 | Artisanal Crystals | https://theamphour.com/623-artisanal-crystals/ | March 12, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 669 | Freelance PCB Design with Petr Dvorak | https://theamphour.com/669-freelance-pcb-design-with-petr-dvorak/ | June 6, 2024 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
| 701 | Electric Propulsion with Todd Bailey | https://theamphour.com/701-electric-propulsion-with-todd-bailey/ | August 21, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1, 2026 |
