---
title: Capacitor
concept: capacitor
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A capacitor is a passive electronic component that stores energy in an electric field between conductors separated by an insulator, governed by the relation that the current through it equals its capacitance multiplied by the rate of change of the voltage across it.[33] Although circuit theory treats the capacitor as a pure capacitance, every physical part is a complex network of capacitance, inductance, and resistance, and working with that reality is one of the core skills of analogue design.[185] Capacitors appear in essentially every electronic system, in roles ranging from power-supply decoupling and energy storage to signal coupling, filtering, sensing, and memory, and their non-ideal behaviour — voltage-dependent value, finite lifetime, and mechanical fragility — is a recurring source of design error and field failure.[185][169][367]

## Operating principles

The defining relation of the capacitor is that current equals capacitance times the rate of change of voltage; its practical working use is recognising behaviours such as a current spike into an integrator producing a voltage step, while the hand calculation itself is rarely performed in practice.[33] Circuit design conventionally treats current as flowing "through" a capacitor, which is a deliberate simplification — charge in fact accumulates on the plates and returns the other way — retained because impedance as a function of frequency is the useful abstraction.[491]

The capacitance of a multilayer ceramic part arises from electrode surface area repeated over hundreds of interleaved layers of dielectric, the same stacking principle by which a battery gains capacity.[188] In modern high-capacitance ceramic parts, internal dimensions are of the order of 0.4-micron particles within a two-micron dielectric layer, while the sprayed termination penetrates the body by around a millimetre.[596] Capacitance need not come from a discrete component at all: a half-picofarad AC-coupling capacitor has been fabricated directly from printed circuit board material, applying at board scale the same technique used for on-chip capacitors,[76] and any two conductors separated by an insulator form a capacitor, a fact exploited to estimate cable length by capacitance measurement.[442]

## Dielectrics and component types

Ceramic capacitors are classified by dielectric. High-permittivity classes such as X7R and Y5U achieve large values in small cases but vary in capacitance with applied voltage and temperature, while NPO and C0G dielectrics are strictly linear and temperature-independent, and are selected wherever linearity with both temperature and voltage matters.[488][570] The stable dielectric classes historically reached only a few nanofarads — at one time about 2.2 nanofarads — forcing AC-coupling requirements to be met by paralleling many parts, though the same class now extends to around a hundred nanofarads.[539]

Electrolytic capacitors provide large values at low cost but carry finite lifetime and leakage as inherent properties.[9][401] Tantalum capacitors are selected when a small design needs both a large value and high instantaneous current availability, such as a cellular transmit burst, at a price of roughly a dollar fifty to two dollars per part against a few cents for a ceramic.[367]

## Voltage dependence and derating

Ceramic capacitor values are specified at zero volts of applied DC bias, a condition no working circuit ever meets; applying three volts to a nominally one-microfarad 25-volt X7R part leaves about 0.90 microfarads in a good part and a small fraction of that in a poor one, making the derating a design input rather than a footnote.[169] The effect is most severe in high-value parts in small packages: a 100-microfarad 0603 ceramic holds that value only at about one volt, and its capacitance falls steeply as the applied voltage approaches its rating.[570] The trade behind such a large value in a small case is the dielectric itself, typically a Y5U-class material whose capacitance varies with voltage, in contrast to X7R.[488] High-value multilayer ceramics additionally carry low voltage ratings, with parts available only at a few volts, so substituting them for electrolytics is bounded by rating as much as by dielectric behaviour;[188] small ceramics in high values are commonly rated at only six or ten volts, and fitting them to a boost-converter rail is a rating error that destroys them.[561] Voltage dependence of ceramic capacitance is a routine property that engineers frequently encounter for the first time in environments where it matters, such as aerospace hardware.[401]

## Decoupling and power distribution

Bypassing a device conventionally uses capacitors of different sizes in the manner of a two-way loudspeaker: a large electrolytic acts as a local reservoir of charge for low frequencies while a small ceramic suppresses high-frequency noise, and neither performs the other's role well.[185] The long-standing habit of fitting three bypass capacitors a decade apart in value arose from each part's impedance minimum — one capacitor presents its lowest impedance at one frequency, and overlaying several extends the low-impedance region across a wider band.[488] The counter-position holds that a single larger capacitor is effective across a wider band than a small one, and that the real obstacles to fitting large values everywhere are size, cost, and the dielectric behaviour that accompanies them.[488] Low-inductance constructions shift the calculation further: a low-inductance chip capacitor or a three-terminal feed-through part can give a ten-microfarad capacitor a broad operating frequency range on its own, whereas paralleling many parts introduces its own poles and zeros against board inductance.[596]

Rules of thumb degrade with clock speed: a hundred nanofarads beside every digital device was adequate at ten-megahertz clocks, but at a hundred megahertz those parts behave as inductors and contribute nothing, so scattering them by habit does not constitute power-distribution design.[169] The engineering method for a power distribution network is measurement rather than habit: remove the switcher, feed the device from a clean supply, sweep the impedance of the distribution network with a network analyser and bias tee, identify the frequency at which emissions exceed the limit, and select capacitors with the vendor's tool for that frequency, DC bias, and temperature.[169] Bulk capacitance for a switching regulator is sized from load current, switching frequency, and duty cycle to hold ripple below a target — for example, 22 microfarads to keep ripple under ten millivolts — and correct sizing still leaves harmonics that can surface as an electromagnetic-compatibility failure.[169]

Decoupling package size is decided together with pin assignment at the concept stage, not after layout: whether 0402 parts can be packed close or 0603 is required is settled early, and the high-current switching node is kept away from voltage-sense lines from the start.[566] Board practice migrated downward in size over roughly a decade, from 0805 and 1206 parts to 0603 and smaller, with many designs going all-ceramic and accepting the consequences that follow.[566]

## Energy storage and pulse applications

A capacitor can buffer a radio's transmit burst, supplying on the order of ten milliamps for a fraction of a second; where the source is energy harvesting, the binding constraint becomes recharge time rather than peak current, with software scaling of transmit power as the complementary lever.[226] A pulse output stage may store energy in a capacitor bank at a voltage far above the output requirement — thirty volts for a five-volt output — because the drive voltage produces sharp edges, without which the output degenerates from a square wave toward a sine.[522] In a pulsed energiser the capacitors and output transformer are the life-limiting components, since the design dumps stored energy repeatedly; the charging circuit monitors the rate of rise of capacitor voltage to detect a shorted capacitor before charging it, because charging a shorted capacitor is a fire risk.[481]

A Marx generator charges a ladder of capacitors in parallel through a resistor chain and then fires spark gaps that reconnect them in series, converting twenty-five kilovolts across many capacitors into hundreds of kilovolts across one; the device is simple in principle and difficult to make reliable.[135] At the other extreme of scale, a tuned loop antenna requires a tuning capacitor rated far above the supply voltage — on the order of six to ten kilovolts for a hundred watts — because flyback effects in the antenna drive the voltage up and an ordinary low-voltage ceramic arcs through immediately; vacuum variable capacitors serve where available, with home-built sliding-plate and trombone capacitors as substitutes.[394]

Capacitor banks are used for power-factor correction at industrial sites running large inductive loads such as motors, where billing on apparent power makes correction worthwhile.[215] The same physics does not transfer to domestic supplies, because residential metering charges for real power and does not measure power factor, so a capacitor sold as a household energy saver cannot reduce a domestic bill.[64]

## Signal, sensing, and parasitic roles

Dynamic memory stores each bit on a tiny capacitor, which is why it must be refreshed and why its behaviour differs fundamentally from non-volatile memory.[43] A condenser microphone is a capacitor whose plate spacing, and therefore capacitance, is modulated by air pressure.[410] Digital isolators can use capacitive coupling across their barrier, built from tens of picofarads of deliberately large capacitance rather than a magnetic or optical path.[524] Automatic reset over a serial connection was discovered by accident: a capacitor soldered between the port's data-terminal-ready line and the reset pin converts the line's transition into a reset pulse, removing the need to press a button before every upload.[726] Charging the internal capacitance of a chip's data lines consumes power, so a power trace taken on each clock edge reveals how many bus lines went high — the physical basis of power-analysis side-channel attacks.[239]

Parasitic capacitance produces observable effects in ordinary wiring: stray capacitance in a wall switch and its wiring passes enough current to make modern LED lamps glow faintly with the switch off, because the lamps operate at such low current.[629] Stored charge is also a hazard and a weapon: a 6.8-microfarad capacitor rated at four hundred volts and left charged to two hundred and forty volts by removal of its discharge resistor delivers a substantial shock,[539] and a malicious device that buck-boosts an internal capacitor bank to two hundred volts and dumps it repeatedly into a port's data lines destroys the host hardware by direct electrical attack.[315]

## Failure modes

### Mechanical failure of ceramics

A printed circuit board flexes and a multilayer ceramic capacitor mounted on it does not: the rigid layer stack, soldered at both ends to a bending substrate, cracks before the solder joint does.[367] Cracked ceramic capacitors commonly fail short rather than open, and because most sit across a power rail, a short becomes a path for the supply's full energy — the mechanism by which capacitor cracks become fires.[367] Modern layer thicknesses aggravate the problem: with layers that thin, the slightest stress or fracture turns the part into a resistor rather than an open circuit.[539] Damage often begins before the board is powered, as the compression of vacuum pickup and forced placement, followed by solder surface tension and thermal shock in reflow, initiates micro-cracks in the brittle ceramic body.[188] A documented case involved a permanently powered alarm panel with a small ceramic across its supply that went short, caught fire, and destroyed the board, in a benign vibration environment with no power cycling.[561]

Mitigations against flex cracking include extra standoffs to stop the board flexing, rotating the component ninety degrees because the parts break along their longitudinal axis, and routing stress-isolation slots around mounting posts and around the components themselves.[367] Parts with compliant terminations, whose end caps flex and absorb stress instead of transmitting it into the ceramic, exist for the automotive and high-vibration industries.[539] In circuits that must not fail, two capacitors are placed in series wherever one would normally sit across a rail, so a single shorted part leaves a working capacitor rather than a short, at the cost of halved capacitance and doubled component count.[561]

### Microphony

Multilayer ceramic capacitors are piezoelectric in both directions: they emit audible sound under a varying voltage, heard as a singing or buzzing board, and they generate a voltage when the board is tapped or vibrated.[127] Microphony is therefore a diagnosis to reach for when a qualified filter misbehaves in the field; swapping the ceramic for a film capacitor is the quick test.[169]

### Electrolytic ageing and abuse

Electrolytic capacitors in a high-temperature environment can reach end of life in about a thousand hours, which forces a different technology into long-life designs; substituting high-value ceramics moves the problem rather than removing it, since those parts are expensive and stress-sensitive in a high-vibration installation.[9] The rated lifetime of a lamp or luminaire is in practice the lifetime of its capacitors, with an electrolytic waiting to dry out setting the ceiling under any figure quoted for the emitters themselves,[56] and most failures of retail LED lamps are the capacitors in the driver rather than the diodes.[71]

Overvoltage does not require mains potential: twenty volts across a sixteen-volt part heats and boils the electrolyte until pressure bursts the can, accelerated by a supply able to deliver current.[580] A classic version of the mistake is designing a voltage doubler around nominal line voltage rather than its peak — a 120-volt line reaches about 170 volts — which condemns hundred-volt parts fitted to the circuit.[485] Long-stored equipment fails through its electrolytics, as decades of storage dry the electrolyte, though capacitance can sometimes be recovered by reforming rather than replacement.[688] In one family of second-hand instruments, every unit's power supply is found leaking, with rails drifting out of specification while many capacitors still measure in tolerance; the remedy is immediate recapping, because leaked electrolyte on the board is itself destructive.[613]

### Other failure mechanisms

Metallised-paper mains-rated capacitors of a well-known series approach a hundred percent failure rate with age, and replacing them in old equipment is routine restoration work.[570] The mechanism is moisture ingress: the case cracks, the paper absorbs moisture, and switch-on produces a conductive path and a violent failure; film capacitors are not immune, with ingress found in a part only a year old.[596] Mains-rated X and Y class capacitors are required to be self-healing, so that a localised dielectric breakdown clears itself rather than propagating.[707] A microscopic arc between the plates of an ageing electrolytic produces a current pulse, and where that capacitor sits in an audio signal chain the pulse is heard as an intermittent pop — a repair symptom that points directly at the capacitor.[707]

Environment imposes further exclusions. Tantalum capacitors are excluded from spacecraft hardware, and a payload built without that knowledge emitted smoke aboard a crewed station.[459] Electrolytics are the first exclusion for airborne and space hardware, because their lifetime is limited, they leak, and reduced pressure at altitude or in vacuum dries them out.[401] Deep-submergence electronics must survive hydrostatic pressure at the component level: capacitors implode, and even a sealed enclosure transmits pressure into the potting compound and the parts inside it.[407] Capacitors are not, however, always the culprit in old equipment: in laboratory instruments built with good parts and adequate cooling, capacitor failures are rare and drifting resistors are the more common fault.[431]

### Assembly, identification, and circuit-level pitfalls

Surface-mount capacitors carry no printed value, so they must be bagged and identified individually for kits, and a recipient without a capacitance meter cannot verify them; through-hole parts carry their values in print.[143] Two unmarked capacitors of similar appearance were once swapped on a bench, placing a hundred nanofarads where a microfarad was needed; the low-dropout regulator went unstable for want of its minimum output capacitance and produced random resets that were first blamed on software.[53] A regulator's ceramic output capacitor must also meet a specified equivalent series resistance, not merely a capacitance value, a requirement often buried deep in the data sheet.[276] A vendor's own application circuit destroyed parts in the field when a capacitor on a regulator's set pin held charge such that shorting the output created a voltage differential between the set and output pins exceeding the device's undocumented limit; later variants added a series resistor with the back-to-back protection diodes while the original part was never respun.[140] Counterfeit capacitors are built to pass inspection by weight and appearance — a part marked at sixty-eight thousand microfarads, cut open, contained a much smaller capacitor inside the casing.[5]

Lighting dimmers interact destructively with capacitive and inductive front ends. Trailing-edge dimming into a transformer destroyed the mains supply behind it when switching off about four amps from an inductive secondary generated roughly an eight-hundred-volt spike; the remedies are to avoid the transformer or place a few microfarads of capacitance across its output.[524] Leading-edge dimmers create the opposite problem, since switching on part-way through the cycle drives a high current surge into the rectifier and electrolytic front end of a switch-mode load, which is why conventional dimmers contain a sizeable choke to limit the rise time.[524]

## Capacitors in integrated circuits

On silicon, a capacitor is two metal plates placed close together, and the difficulty is reproducibility: capacitors and resistors both spread by around twenty percent across a process, which destroys an error budget built on absolute values.[338] Analogue silicon design answers the spread by designing with ratios rather than absolute values, since adjacent devices on the same die match closely even when the next wafer differs by ten percent.[672] On-chip capacitance is scarce: devoting an entire small shared-shuttle tile to one capacitor yields on the order of a picofarad, with the value moving by around ten percent from run to run.[672] Large capacitors and inductors are among the elements that do not integrate into silicon at all, remaining on the package substrate or the board no matter how much else is absorbed into a single device.[499]

## Design and manufacturing practice

0603 is the smallest case size an ordinary assembly house can handle; below it the customer needs a shop with more specialised placement equipment, making package choice a supplier decision as well as a board decision.[391] Changing package size to hedge against component shortages changes the whole assembly process technology, lowers yield, and may force a change of assembler.[391] Assembly also consumes more parts than the board needs, because winding a reel onto the machine wastes ten or twenty components; the customer must supply excess and flag expensive parts for careful handling.[24]

Component supply is structured and forecastable. About eight companies make ninety percent of the ceramic capacitor market, and because a phone contains on the order of a thousand capacitors of one small size, development money flows to smaller footprints; lead times on small parts therefore improve while large-footprint parts stay long, which matters when choosing a part to design in.[451] Shortages are selective rather than universal: through one shortage, high-voltage, high-value parts were effectively unobtainable while hundred-nanofarad 0603 parts remained available at a slightly higher price, with parts going out of stock between quotation and purchase.[412]

Sourcing discipline treats capacitors differently from other passives. On the Keyboardio programme, Vincent's practice was to leave resistors and diodes to local brands while specifying capacitors from known Japanese or Korean manufacturers, with the factory assisting sourcing where the customer's knowledge of local brands was thin.[450] Brand selection rests on accumulated industry trust rather than incoming inspection, because a buyer cannot run parts in a thermal chamber for ten thousand hours; the brands that matter are those in the stressed positions of a power product.[671] Lot traceability separates factory tiers: a top-tier plant tracks the solder paste lot, its four-hour warm-up, and its window of use, and can say which reel went into which serial number — a capability that matters when a bad batch of capacitors reaches the field.[451] Constraining the approved part catalogue functions as a design aid: a designer denied a new part number fits two 2.2-microfarad capacitors instead of registering a 4.7, and having the decision made in advance removes a class of choices from every project.[137]

### Bench practice

A quick sanity check when probing a working board is that bypass capacitors should have voltage across them and resistors should not, since voltage across a resistor means power is being dissipated where none was intended.[527] Continuity testing on a populated board produces false short indications, because a capacitor is a short circuit at the moment voltage is applied and the meter latches on the resulting beep.[690]

Adding a capacitor to stop an oscillation is not an incremental change: it alters the whole system and invalidates the preceding analysis; the disciplined form is to place the component in the system design from the start, with a value that may turn out to be zero, and to reason about the consequences of its presence.[476] Finding the fix by touch — putting a finger on a node until the oscillation stops and fitting a capacitor there — solves the day's problem but leaves no understanding, and the follow-up work is to determine what the intervention actually did, by hand analysis or simulation.[476] Empirical swapping must be recorded as it happens: fitting a capacitor, removing it, fitting another, and failing to note which value was in place at each measurement costs the rest of the day.[341] Tuning loop stability by trying capacitors is legitimate, but a value that works only under precise conditions is a warning rather than a solution, with slowing the loop down as the fallback; a one-off fixture can be tuned to a known load, while a general-purpose product must remain stable into an unknown load that may be strongly inductive or capacitive.[184] In class-D amplifier output filters, the inductor and capacitor configuration must be chosen so that fluxes cancel and impedances at both ends balance; imbalance produces an audible click or pop at startup, and the same filters appear on radiated-emissions scans, making late discovery expensive against a production ramp.[474]

A cost-reduction method attributed to a mid-century television maker was to remove components from a working product one at a time until it stopped working and then restore the last one — a working description of finding which capacitors a design actually needs.[391]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 5 | Girl Power | https://theamphour.com/the-amp-hour-5-girl-power/ | |
| 9 | From Boston In Boxers? | https://theamphour.com/the-amp-hour-9-from-boston-in-boxers/ | |
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ | |
| 33 | Bob Widlar, Electronic Design, FIRST Robotics - Monday, Meta Monday | https://theamphour.com/the-amp-hour-33-monday-meta-monday/ | |
| 43 | An Interview with Jeff Keyzer and Jeremy Blum - Audacious Arduino Arguments | https://theamphour.com/the-amp-hour-43-audacious-arduino-arguments/ | |
| 53 | Biarchy Birthday Bavardage | https://theamphour.com/the-amp-hour-53-biarchy-birthday-bavardage/ | |
| 56 | Open Orbific Oratiuncle | https://theamphour.com/the-amp-hour-56-open-orbific-oratiuncle/ | |
| 64 | OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster | https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/ | |
| 71 | An Interview with John Edmond - Luciferous LED Lucubrator | https://theamphour.com/the-amp-hour-71-luciferous-led-lucubrator/ | |
| 76 | Fremescent Floccose Fortification | https://theamphour.com/the-amp-hour-76-fremescent-floccose-fortification/ | January 2, 2012 |
| 127 | FPGA, Xess, 32 Bit - Quirky Qualitative Questions | https://theamphour.com/the-amp-hour-127-quirky-qualitative-questions/ | January 7, 2013 |
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 137 | Mars, System Design & NAND - Mercurial Mars Mission | https://theamphour.com/the-amp-hour-137-mercurial-mars-mission/ | March 19, 2013 |
| 140 | Project Management, Lasers & Robots - Staunch Specialty Sanctanimity | https://theamphour.com/the-amp-hour-140-staunch-specialty-sanctanimity/ | April 8, 2013 |
| 143 | PCBs, Tektronix & Ham Radio - Habitual Handicraft Hangups | https://theamphour.com/the-amp-hour-143-habitual-handicraft-hangups/ | April 29, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 185 | An Interview with Hank Zumbahlen - Zoppa Zumbahlen Zateticism | https://theamphour.com/185-an-interview-with-hank-zumbahlen-zoppa-zumbahlen-zateticism/ | February 17, 2014 |
| 188 | Capacitors, Simulation and Closures - Deonerated Design Dealmaking | https://theamphour.com/188-capacitors-simulation-and-closures-deonerated-design-dealmaking/ | March 10, 2014 |
| 215 | Wrong Hardware, Wrong Software - Fugacious Fan Funding | https://theamphour.com/215-wrong-hardware-wrong-software-fugacious-fan-funding/ | September 7, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 276 | Eating An Elephant | https://theamphour.com/276-eating-an-elephant/ | December 2, 2015 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 341 | All the way with DLJ | https://theamphour.com/341-all-the-way-with-dlj/ | |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 394 | Jeri Ellsworth and the demise of CastAR | https://theamphour.com/394-jeri-ellsworth-and-the-demise-of-castar/ | May 28, 2018 |
| 401 | An Interview with Brent and Bryce Salmi | https://theamphour.com/401-an-interview-with-brent-and-bryce-salmi/ | July 29, 2018 |
| 407 | Gregory Charvat and Three New Companies | https://theamphour.com/407-gregory-charvat-and-three-new-companies/ | September 16, 2018 |
| 410 | Secret Buzzer Handshake | https://theamphour.com/410-secret-buzzer-handshake/ | October 7, 2018 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 431 | An Interview with Adam McCombs | https://theamphour.com/431-an-interview-with-adam-mccombs/ | February 24, 2019 |
| 442 | An Interview with Travis Goodspeed | https://theamphour.com/442-an-interview-with-travis-goodspeed/ | May 12, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 451 | An Interview with Scott Miller (2nd) | https://theamphour.com/451-an-interview-with-scott-miller-2nd/ | July 21, 2019 |
| 459 | An Interview with Tom Lee | https://theamphour.com/459-an-interview-with-tom-lee/ | September 22, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 476 | An Interview with Kendall Castor-Perry | https://theamphour.com/476-an-interview-with-kendall-castor-perry/ | January 26, 2020 |
| 481 | An Interview with Paul Thompson | https://theamphour.com/481-an-interview-with-paul-thompson/ | February 24, 2020 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 488 | Sowing Discord | https://theamphour.com/488-sowing-discord/ | April 12, 2020 |
| 491 | The Almighty Dollarydoo | https://theamphour.com/491-the-almighty-dollarydoo/ | May 3, 2020 |
| 499 | Discussing Chiplets with Ming Zhang | https://theamphour.com/499-discussing-chiplets-with-ming-zhang/ | July 5, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 539 | The King of Trash with Big Clive | https://theamphour.com/the-amp-hour-539-the-king-of-trash-with-big-clive/ | April 26, 2021 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 566 | Switching Converter Engineering with Carmen Parisi | https://theamphour.com/566-switching-converter-engineering-with-carmen-parisi/ | November 14, 2021 |
| 570 | Keyzermas All The Way | https://theamphour.com/570-keyzermas-all-the-way/ | December 19, 2021 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6, 2022 |
| 596 | Capacitor Schoopage with Ron Demcko from AVX | https://theamphour.com/596-capacitor-schoopage-with-ron-demcko-from-avx/ | July 17, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 629 | At least my house isn't haunted | https://theamphour.com/629-at-least-my-house-isnt-haunted/ | April 23, 2023 |
| 671 | NDA Sideshow | https://theamphour.com/671-nda-sideshow/ | June 19, 2024 |
| 672 | Silicon Revolution with Matt Venn | https://theamphour.com/672-silicon-revolution-with-matt-venn/ | June 30, 2024 |
| 688 | The Tandy Train | https://theamphour.com/688-the-tandy-train/ | February 11, 2025 |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11, 2025 |
| 707 | Welding with an HDMI Cable | https://theamphour.com/707-welding-with-an-hdmi-cable/ | October 26, 2025 |
| 726 | Arduino's Invisible Touch with Massimo Banzi | https://theamphour.com/the-amp-hour-726-arduinos-invisible-touch-with-massimo-banzi/ | June 17, 2026 |
