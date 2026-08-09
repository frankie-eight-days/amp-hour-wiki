---
title: Battery
concept: battery
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A battery is an electrochemical energy-storage assembly comprising one or more cells together with management circuitry and the interconnects between them.[399] The term entered electrical use by analogy with a battery of cannon, applied to any powerful arrangement; when Volta published his description of the first electric battery in 1800 he called it an artificial electric organ, a name that did not survive.[605] Batteries set the governing constraint in a wide range of designs: in a large electric vehicle the pack accounts for on the order of eighty percent of the bill of materials,[680] and in a modern smartphone the internal volume under the display is roughly sixty percent cell, thirty percent circuit boards and ten percent camera modules on flex.[367] Progress in the chemistries actually in service has come from small incremental improvements to existing technology rather than step changes, and claims of order-of-magnitude energy-density gains are inconsistent with the roughly linear historical record.[236][370][704]

## Terminology and construction

A cell is the individual electrochemical unit, such as a cylindrical 18650, while a battery is the assembled article: multiple cells, a management unit of some kind, and the connections between them.[399] A large battery assembly therefore consists of cells inside an enclosure together with battery-management and protection circuitry; one recorded aviation assembly used a steel box containing all of these elements.[130]

The 18650 designation encodes the cell's dimensions: 18 millimetres in diameter by 65.0 millimetres long, the trailing zero marking the decimal place on the length.[510] A cylindrical lithium cell is internally a wound roll of electrode material about a metre long, so current from the innermost windings must traverse the entire roll to reach the tabs; the resulting internal series resistance limits the power the cell can deliver independently of its capacity.[510]

A battery subsystem is more than the cell: the design also has to answer how the pack is charged and how the user is told the charge is running low.[479]

## Chemistries

### Primary cells

Alkaline has become the default primary chemistry for consumer cells, displacing zinc-carbon on price; zinc-carbon cells remain purchasable but are rarely specified.[253] An alkaline cell is effectively exhausted around 0.8 volts, where most of its energy has been delivered, with about 99.99 percent gone by 0.5 volts.[486] A cell that has fallen to its cutoff voltage under load recovers part of its charge once the load is removed, and the amount recovered depends on the discharge rate, so a voltage reading taken under heavy load understates remaining capacity.[486]

A primary cell powering a microamp-class part can have a shelf life on the order of eight years, which then becomes the limit on the design rather than the load current.[49] Alkaline cells leak more often than they once did across all brands; the contributing factors are unsettled, with temperature, humidity and pressure implicated, and a stiff spring terminal pressing on the cell ends a common hypothesis without hard evidence behind it.[690]

### Lithium-ion

Lithium-ion cells are made in two upper-voltage variants: a coke-anode cell that terminates charge at 4.1 volts and the more common graphite-anode cell that terminates at 4.2 volts; roughly ninety percent of available charger parts are built for the 4.2-volt figure.[46] The termination voltage has to be held accurately, to roughly half a percent, because overshoot damages the cell.[580] A lithium-ion polymer pouch cell reaches about 4.2 volts fully charged and spends most of its discharge in a flat region near 3.7 volts.[175]

The first generation of lithium cells was rated at roughly three hundred to four hundred cycles — energy-dense but not designed for longevity — because they were built for consumer products replaced every couple of years.[112] Lithium recovery from cell recycling reaches about ninety-five percent, so the mined material is largely retained across a cell's disposal cycle.[112]

### Nickel-metal hydride

Hybrid-vehicle manufacturers keep the pack centred on fifty percent state of charge and swing only plus or minus twenty percent, which is how nickel-metal-hydride packs achieve hundreds of thousands of cycles; cycling the same chemistry to full depth yields far fewer cycles, fewer even than lithium-ion.[112]

## Electrical characteristics

### Internal resistance

Cell internal resistance varies strongly with format: an AAA cell sits around 0.2 to 0.4 ohms while a nine-volt battery is on the order of an ohm, which limits deliverable current, causes the cell to heat under load, and makes the discharge self-limiting.[158] The internal resistance quoted on a data sheet is the ohmic term only and excludes ionic resistance — the contribution of the chemical reaction itself — which develops over timescales from a tenth of a second to tens of seconds and is therefore invisible in an instantaneous measurement.[158]

### Voltage and usable capacity

Usable capacity is set by the load's minimum operating voltage, not by the cell's rating: a three-volt cell feeding a part that stops working at 2.5 volts leaves most of the stored energy unreachable, so an eight-year nominal life collapses to months unless a DC-DC converter holds the rail constant as the cell falls.[191] Whether a load draws constant current or constant power decides how consumption tracks the falling cell voltage: behind a linear regulator the current is fixed so input power falls as the battery drains, whereas behind a DC-DC converter input power stays constant and current rises.[629]

A multi-cell pack whose terminal voltage sits near that of a single cell is wired in parallel rather than in series, so pack voltage is a direct read on the series count.[343]

### Temperature

Batteries perform poorly at low temperature, so an instrument specified to operate down to freezing or below can fail on its power source rather than its circuitry; alkaline cells in particular lose usable output near zero degrees Celsius.[106]

## Charging

Charging a lithium-ion cell follows a constant-current then constant-voltage algorithm, reproducible directly from a laboratory supply: set the compliance voltage to 4.2 volts so it cannot be exceeded, run the supply in constant-current mode, and the supply transitions itself into constant-voltage float as the cell approaches full charge.[662] Charge rate is bounded by heat: the ceiling on how fast a phone-sized pack can be filled is a thermal limit in the cell, not a limitation of the charger electronics.[240] Charging at high current drives cells to their upper voltage limit at a lower state of charge than trickling would, which is why a fast charge is terminated around eighty percent.[112]

### Charger selection and integration

Selecting a lithium charger IC begins with a parametric search on termination voltage, which distributors expose as a sortable characteristic, but the minimum charge current a part can deliver is not a parametric field and has to be read out of each candidate data sheet by hand.[46] Lithium charging parts have grown beyond simple chargers into management devices with control registers and state-of-charge reporting, so the same chip that regulates the charge also reports the pack level.[315] Integrated charge controllers of the BQ2400x family provide roughly two amps of charge current when the system is idle and switch the system load automatically between the battery and the adapter.[469] A general-purpose microcontroller is technically capable of implementing lithium charge control, but practitioners still buy a dedicated charge-management part because the consequences of a firmware error in that loop are severe.[637]

### Electric-vehicle fast charging

DC fast charging bypasses the vehicle's onboard AC-DC stage and drives current straight into the pack; the handshake requests a current rather than a voltage, so the charger behaves as a current source and pack voltage rises as it accepts the charge.[112] Fast charging follows a stepped curve rather than a constant rate — full power below fifty percent state of charge, a reduced step above it, and further reductions above sixty percent; every vehicle does this but the curve's shape differs between models.[524] Charging pauses at high states of charge, for instance at eighty and ninety percent, let cell voltages settle so that measured cell-to-cell deviation reflects the pack rather than transient charging offsets.[524] Eight-year pack warranties with a guaranteed remaining-capacity figure, written before any field history existed, are the commercial reason charge curves are derated: sustained high-power fast charging threatens the capacity the warranty promises.[524]

Charging a pack only to eighty or ninety percent as routine, reserving a full charge for trips that need the range, is a deliberate practice for extending pack life.[662]

### Fuel gauging

A coulomb-counting fuel gauge integrates charge into and out of the pack rather than inferring state from terminal voltage, and combining that count with a model of the cell's discharge characteristic curve is what makes a percentage or bar-graph display meaningful.[65] A charge gauge also reads cell temperature alongside the charge count, which improves the state estimate.[315]

## Battery management systems

A battery management system measures every cell in the pack individually, and the single cell nearest its upper limit sets the pace for the whole pack; when that cell reaches its threshold the charge-current request is reduced and the cell can be shunted so the rest continue to fill.[112] Cells connected in series each need their own floating voltage measurement plus a bypass path such as a shunt FET, because pack terminal voltage alone cannot reveal an individual cell drifting out of range.[216]

Cell-to-cell voltage deviation is used as an early indicator of an impending pack fault: one manufacturer's recall tightened the allowed spread to around 150 millivolts between the highest and lowest cell and shuts the vehicle down when it is exceeded.[524]

When the battery is user-replaceable, its negative terminal is no longer system ground, so a coulomb-counting shunt in that path has to be isolated; shorting across the shunt makes the device believe it is drawing no current at all, and using the same shunt for current control complicates charging a rechargeable cell.[640]

## Design considerations

### Power budgeting and runtime

Power budgeting can be entered from either end, and the two orders give different designs: fix the chipset and size the battery to the resulting consumption, or fix the battery size and select a chipset whose budget fits inside it.[389] Where the form factor permits it, enlarging the battery is a cheaper route to runtime than the last increments of firmware power optimisation, which yield diminishing savings for substantial added complexity.[527] Fitting a pack considerably larger than the load requires buys two things at once: a full day of untethered operation, and fewer charge cycles across the product's life because each cycle uses a smaller fraction of the pack.[469]

A single-cell lithium rail sits near 3.7 volts, which almost never matches the voltage a load needs, so a boost or DC-DC stage is the normal answer; running a load from one cell therefore requires a boost converter, while stacking two cells in series raises the rail enough to remove that converter.[175][277] Instrument runtime can be multiplied several times simply by choosing a cell format with more capacity: swapping a single nine-volt battery for four AA cells in a handheld meter turns a five-to-six-hundred-hour life into a two-to-three-thousand-hour one.[130]

Powering a precision analogue circuit directly from cells lets the supply rail drift as the cells discharge, and any supply-dependent error term drifts with it; the fix is to insert a voltage regulator rather than run from the raw battery.[146] A supply-voltage-dependent offset error can invert the usual test intuition: in one case the offset was worse at higher supply voltage, so the circuit measured badly on fresh cells and only came into specification as the cells approached end of life.[146]

A bench power supply is not an equivalent substitute for the battery it replaces during debugging, because a battery is a two-quadrant device that can sink current as well as source it, and a single-quadrant supply cannot absorb energy pushed back by the load.[238] Any battery, including a primary cell not designed to be charged, will absorb current pushed back into it — for example from an inductive load whose current is interrupted — and charging a non-rechargeable cell hard enough makes it vent violently.[238]

### Sourcing and integration shortcuts

Replacing loose hobby-grade lithium-polymer cells with a packaged consumer USB power bank removes the custom charging circuit, the protection circuitry and the fuel-gauge telemetry from a one-off design at once, because those functions are already inside the purchased product and it can be re-bought off the shelf if damaged.[292] Power-tool battery packs expose four or five contacts — battery positive, battery negative, a coding or identification pin and a thermistor line; the tool uses only the thermistor and identification pins, while the additional contacts exist for the charger — which makes an existing tool-battery system attractive as a general-purpose supply through a printed or machined adapter with an inline fuse and switch.[662]

The energy cost of a high-level interpreted runtime is affordable on a mains-powered device and generally is not on a battery-powered one, which is why language choice on embedded targets tracks the power source.[295]

## Failure modes and safety

### Mechanical failure and internal shorts

Lithium-ion cells swell during charging and with age, and industry practice is to leave a defined mechanical clearance around a cell in the enclosure to accommodate that expansion; a rigid machined case removes that allowance.[326] Pushing capacity by adding layers and thinning the separator leaves the cell less able to survive its own swelling: pressure from expansion punches through the thinned dielectric and shorts adjacent layers internally, and the resulting current circulates within the cell rather than through the protection path, so external protection circuitry cannot intervene.[326]

Because a battery has no tabulated stiffness or failure stress the way a homogeneous metal does, mechanical simulation of a product containing a cell requires measuring real cells non-destructively and back-calculating the values into the model; two cells built to the same published specification can differ in chemistry and reaction kinetics between manufacturers, so a mechanical failure threshold cannot be stated a priori and has to be established by test.[399]

Battery safety qualification is destructive and physical: test houses run nail-penetration machines that drive nails into cells to see whether they ignite, alongside crush tests such as driving a vehicle over the pack.[450] Cells tested against the figures printed on their own data sheet have been found to melt internally, which is an argument for verifying cell performance by measurement rather than accepting the published specification.[727]

### System-level failures

A battery module can be specified without the ability to interrupt its own current when that function is assigned elsewhere in the system, which leaves the protection responsibility spanning a system boundary and is a candidate cause when a managed pack fails to shut itself down; in one recorded aviation failure the assembly caught fire and melted internally despite its protection circuitry.[130]

Smart packs that report their state over a management protocol are not interchangeable across suppliers: a substitute pack of the same nominal type failed to report voltage at all, which silently removed battery monitoring from a product built around the original pack's protocol.[325] A storage battery module can likewise be taken out of service by its management firmware rather than by its cells: one rack module had to be shut down while the cells themselves remained healthy, the defect being early firmware in the module's controller.[702] A pack can report itself as charging while actually discharging: in one laptop the system indicated charge in progress and the charger's own indicator lit, yet the pack fell overnight, then charged to fifty percent and stopped, with the fault reproduced across two different chargers.[702] A used pack legitimately reports reduced full-charge capacity against its original rating, but it should still charge to one hundred percent of that reduced capacity; failure to reach the indicated full state is a distinct fault from ordinary capacity fade.[702]

A defective charger or fixture can destroy successive replacement cells rather than one, and cells killed that way are generally unrecoverable; applying a fixed voltage for a set period to revive them does not reliably work.[662] Where a cell-level defect cannot be fixed in the field, a firmware change that stops the pack short of one hundred percent charge is the standard mitigation.[315]

At consumer volumes of tens of millions of units a year, a one-in-a-million battery failure rate is a serious problem rather than an acceptable defect level, which is why rare, hard-to-reproduce battery faults attract dedicated engineering effort at that scale.[437]

### Logistics

Lithium cells cannot be air-freighted as ordinary cargo, and overseas shipment is both expensive and restricted; some countries cannot be shipped to at all, so shipping restrictions rather than availability are what stop buyers in some countries getting cells from the large distributors, and a distributor declining to ship to a destination is a regulatory signal rather than a stocking decision.[458]

## Applications

### Electric vehicles

An electric-vehicle pack is treated as having reached the end of its first life when it has lost twenty percent of its capacity; whether that takes five, eight or ten years depends on cell stress, temperature and how conservatively the pack is managed.[112] In an electric drive the current ceiling is set on the battery side, not the motor side: a motor is essentially copper wire and will absorb as much power as it is given provided it is cooled, so the limit is the pack's safe discharge current and the capacity of the interconnects to carry it.[259] Traction packs run at three to four hundred volts.[358] Building vehicle packs from 18650 cells lets a maker ride a cell market already scaled and paid down by laptop manufacturing, whereas a chemistry aimed only at grid storage has no comparable volume to amortise its development cost against.[343]

### Stationary storage

Home storage packs are commonly assembled at stack-up voltages around sixty volts, an order below electric-vehicle traction packs.[358] A hybrid or storage inverter must speak the firmware protocol of the pack's management system, so it works only with one or a few battery brands; another brand may physically install but leaves the management non-functional, and accepting a subsidised or free inverter locks the installation to one battery manufacturer and often to specific models within that brand.[612][617]

Rack-mounted modules are heavy enough to dominate installation planning: each 19-inch battery module weighs around 41 kilograms and the empty rack around 91 kilograms, which can require a lift truck to unload; a pre-wired rack turns capacity expansion into a mechanical operation, with a spare slot taking another module slid in and connected in minutes without rewiring.[674] A twenty-five kilowatt-hour domestic pack can be fully discharged in a single day once dryer, oven, cooktop and an unplanned electric-vehicle charge are on it, while a frugal evening of lighting, refrigeration and a little cooking consumes only twenty to twenty-five percent of it.[696]

Monitoring pack voltage and shedding the load when it falls below a threshold is the basic protection against over-discharge in an unattended solar installation, implemented in the controllers of solar lighting towers and repeater sites.[281]

### Spacecraft

Commercial off-the-shelf batteries flown in vacuum have to be stripped of PVC jacketing, because PVC outgasses chlorine and contaminates the surrounding spacecraft.[220] Spacecraft keep the batteries physically disconnected from the bus until deployment using separation switches that detect release from the dispenser, after which a timed sequence gates antenna deployment and then transmission.[679] Splitting a spacecraft's storage into several smaller battery modules with their own management, rather than one large module, means the loss of one critical part costs a fraction of the energy system instead of all of it.[679]

### Portable and remote devices

Sealed remote sensor units carrying their own cells are commonly specified for a five-year service life with no intervention, which makes average power consumption, not sensing performance, the governing design constraint.[179] Battery power should be avoided in a sensor fleet unless it is genuinely required: at a thousand nodes averaging three years of life, replacement becomes a continuous maintenance task, and the cells involved are expensive lithium primaries rather than cheap consumer cells.[511] A battery-powered camera cannot sustain continuous operation, so wireless camera products are built around periodic removal and recharging on a magnetic mount rather than permanent installation.[631] On a mobile robot the energy source is carried, and allocating around ten percent of vehicle mass to batteries is already generous; wanting two to eight hours of runtime on that allowance is the hard constraint on the design.[425] On the CastAR headset, Jeri Ellsworth moved the cells into a belt-worn puck connected by a thin cable, keeping the headset light while carrying about six hours of battery.[394]

Early portable calculators used vacuum fluorescent displays, whose heated element wasted power even though it lowered the voltage requirement, and the resulting consumption forced the use of bulky C or D cells.[725] An H-bridge on both sides of a transformer makes a battery interface bidirectional: power flows through it into the battery to charge, and back out through the transformer onto the high-voltage bus to discharge.[671]

## Energy density and harvesting

A gallon of gasoline carries on the order of thirty-two kilowatt-hours of energy, which is the reference figure against which battery energy density is judged.[38] The presence of a voltage from an energy-harvesting source says nothing about available energy or power; arithmetic on harvested power against a phone battery's capacity gives charging times measured in decades.[98] Ambient radio-frequency harvesting delivers so little average power that a receiver a metre from a Wi-Fi antenna would take weeks to fill a small cell; any apparently fast delivery afterwards comes from the battery's low impedance dumping stored energy, not from the harvester.[211]

## Manufacturing and market structure

The 18650 is the industry-standard cylindrical lithium cell and the default choice for a design that does not need a custom form factor.[360] A product built at millions of units can fund the tooling for a battery in a custom form factor and amortise it across the run, while a lower-volume product is confined to catalogue cells; the cost of going custom is becoming the entire supply chain for that part, with no second source to fall back on.[365]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 38 | An Interview with Jeff Keyzer - Comical Keyzer Comes a-Callin' | https://theamphour.com/the-amp-hour-38-comical-keyzer-comes-a-callin/ | |
| 46 | Autorouter, Datasheets & Obscure Chips - Cloddish Collegiate Conversations | https://theamphour.com/the-amp-hour-46-cloddish-collegiate-conversations/ | |
| 49 | Analog Devices, Design Spark - Unusual Usenet Usurpation | https://theamphour.com/the-amp-hour-49-unusual-usenet-ursurpation/ | |
| 65 | Silego, ADCs & Seismic Detection - Dave's Dingo Dystocia | https://theamphour.com/the-amp-hour-65-daves-dingo-dystocia/ | |
| 98 | Proemial Passive Poiesis | https://theamphour.com/the-amp-hour-98-proemial-passive-poiesis/ | June 3, 2012 |
| 106 | Tektronix, ChipReport.tv, & the Signal Path - Temperative Tegmen Temperature | https://theamphour.com/the-amp-hour-106-temperative-tegmen-temperature/ | July 29, 2012 |
| 112 | An Interview with Bob Simpson - Ardent Automotive Artisan | https://theamphour.com/the-amp-hour-112-ardent-automotive-artisan/ | September 9, 2012 |
| 130 | Boeing, PCBs & Startups - Awful Airplane Aeration | https://theamphour.com/the-amp-hour-130-awful-airplane-aeration/ | January 28, 2013 |
| 146 | Hamvention, Arduino and Intel - Burdensome Background Battology | https://theamphour.com/the-amp-hour-146-burdensome-background-battology/ | May 21, 2013 |
| 158 | Hyperloop, Upverter and Soldering - Unbelievable USB Ustulater | https://theamphour.com/the-amp-hour-158-unbelievable-usb-ustulater/ | August 12, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 179 | Greg Charvat Returns With A Book! - Laboratory Literature Laureate | https://theamphour.com/179-greg-charvat-returns-with-a-book-laboratory-literature-laureate/ | January 6, 2014 |
| 191 | Chairs, Sparks and Devices - Optional Olent Obreption | https://theamphour.com/191-chairs-sparks-and-devices-optional-olent-obreption/ | March 31, 2014 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 216 | Last Minute Decisions - Obdurate Onepercenter Obstacles | https://theamphour.com/216-last-minute-decisions-obdurate-onepercenter-obstacles/ | September 15, 2014 |
| 220 | An Interview with Shaun Meehan - Doctiloquent Dove Deployer | https://theamphour.com/220-an-interview-with-shaun-meehan-doctiloquent-dove-deployer/ | October 13, 2014 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 238 | Old Books, New Tricks - Iterant Inscription Irrationality | https://theamphour.com/238-old-books-new-tricks-iterant-inscription-irrationality/ | February 25, 2015 |
| 240 | Compare and Contrast Tech Entitlement - Worldly Working Wonks | https://theamphour.com/240-compare-and-contrast-tech-entitlement-worldly-working-wonks/ | March 10, 2015 |
| 253 | Consolidate All The Things - Zonked Zelotic Zaitech | https://theamphour.com/253-consolidate-all-the-things-zonked-zelotic-zaitech/ | June 9, 2015 |
| 259 | No More Naming | https://theamphour.com/259-no-more-names/ | July 21, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 281 | Crossovers and Call-ins | https://theamphour.com/281-crossovers-and-call-ins/ | January 6, 2016 |
| 292 | An Interview with Timothy Lamb | https://theamphour.com/292-an-interview-with-timothy-lamb/ | March 23, 2016 |
| 295 | An Interview with Omer Kilic | https://theamphour.com/295-an-interview-with-omer-kilic/ | April 20, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ | |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 343 | Road trip to the deep space network | https://theamphour.com/343-road-trip-to-the-deep-space-network/ | April 17, 2017 |
| 358 | Mergers and People Acquisitions | https://theamphour.com/358-mergers-and-people-acquisitions/ | September 4, 2017 |
| 360 | A Total 360 | https://theamphour.com/360-a-total-360/ | September 18, 2017 |
| 365 | Wait, why is Jeff glowing? | https://theamphour.com/365-wait-why-is-jeff-glowing/ | October 30, 2017 |
| 367 | Not Reely An Issue | https://theamphour.com/367-not-reely-an-issue/ | November 12, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 394 | Jeri Ellsworth and the demise of CastAR | https://theamphour.com/394-jeri-ellsworth-and-the-demise-of-castar/ | May 28, 2018 |
| 399 | An Interview with Steve Kreuzer | https://theamphour.com/399-an-interview-with-steve-kreuzer/ | July 15, 2018 |
| 425 | An Interview with Chris Osterwood | https://theamphour.com/425-an-interview-with-chris-osterwood/ | January 13, 2019 |
| 437 | An Interview with Chrissy Meyer | https://theamphour.com/437-an-interview-with-chrissy-meyer/ | April 7, 2019 |
| 450 | Stories from Teardown 2019 | https://theamphour.com/450-stories-from-teardown-2019/ | July 7, 2019 |
| 458 | An Interview with Ken Burns | https://theamphour.com/458-an-interview-with-ken-burns/ | September 15, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 479 | Why isn't this working? | https://theamphour.com/479-why-isnt-this-working/ | February 13, 2020 |
| 486 | Medical Kits, They're The Future | https://theamphour.com/486-medical-kits-theyre-the-future/ | March 29, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 511 | Brewing Electronics with Eli Hughes | https://theamphour.com/511-brewing-electronics-with-eli-hughes/ | October 4, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 580 | Electrical Archeology | https://theamphour.com/580-electrical-archeology/ | March 6, 2022 |
| 605 | The Lightning Tamers with Kathy Joseph | https://theamphour.com/the-amp-hour-605-the-lightning-tamers-with-kathy-joseph/ | |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 617 | Conference Room Innovation | https://theamphour.com/617-conference-room-innovation/ | January 29, 2023 |
| 629 | At least my house isn't haunted | https://theamphour.com/629-at-least-my-house-isnt-haunted/ | April 23, 2023 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 662 | The non-Stinky Car | https://theamphour.com/662-the-non-stinky-car/ | March 20, 2024 |
| 671 | NDA Sideshow | https://theamphour.com/671-nda-sideshow/ | June 19, 2024 |
| 674 | Turtles as a Service | https://theamphour.com/674-turtles-as-a-service/ | July 25, 2024 |
| 679 | Satellite Design Engineering with Dan Esparon | https://theamphour.com/679-satellite-design-engineering-with-dan-esparon/ | October 11, 2024 |
| 680 | Catching Rockets with Musk Sticks | https://theamphour.com/680-catching-rockets-with-musk-sticks/ | October 15, 2024 |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11, 2025 |
| 696 | It Works With Option Number 5 | https://theamphour.com/696-it-works-with-option-number-5/ | June 18, 2025 |
| 702 | Test Point Accupuncture | https://theamphour.com/702-test-point-accupuncture/ | September 14, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 725 | The Secret Life of Circuits with lcamtuf / Michał Zalewski | https://theamphour.com/725-the-secret-life-of-circuits-with-lcamtuf-michal-zalewski/ | June 3, 2026 |
| 727 | Boat Anchor Warehouse | https://theamphour.com/727-boat-anchor-warehouse/ | July 1, 2026 |
