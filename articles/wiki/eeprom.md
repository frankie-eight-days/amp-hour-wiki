---
title: EEPROM
concept: eeprom
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**EEPROM** (electrically erasable programmable read-only memory) is a non-volatile memory technology whose defining role in electronics was to make program and configuration storage changeable after manufacture, sitting between factory-programmed and one-time programmable memory and the flash memory that followed it.[236] The first microcontroller built on electrically erasable memory was the first such part that was neither ultraviolet-erasable nor one-time programmable, and therefore the first that could be reprogrammed in place without removal from the circuit.[24] Its commercial significance came when electrically erasable parts became cheap enough to ship in production rather than serve only as development devices, eliminating both the financial risk of a code bug committed to a mask and the factory lead time from product schedules.[485]

## History

### Preceding technologies

Microcontroller program storage developed through a sequence of mask ROM, one-time programmable (OTP) memory, EEPROM, and finally flash, with each step trading unit cost for the ability to change the stored code after manufacture.[236] Mask ROM was programmed by the semiconductor manufacturer as part of chip fabrication, using a mask specific to the customer's code and requiring a minimum order, which made it the cheapest option at volume and the most inflexible everywhere else.[236]

The development loop this imposed was slow. Engineers debugged through a bulky in-circuit emulator plugged in place of the actual part, typically wrote in assembly because compilers were often unavailable, and then sent a hex file to the manufacturer and waited.[485] The exposure was total: a ROM sample arriving six weeks later that did not work left no way to debug it and required paying another mask charge to try again.[485] Before either EEPROM or flash existed, retaining settings on a machine meant battery-backed static memory, with a protection switch diverting a rechargeable cell to keep the memory alive; machines from that era recovered from storage have invariably lost their contents, because the cell died years earlier.[688]

The intermediate technology was the windowed ultraviolet-erasable part, which carried a cost premium because of the quartz window itself. The working cycle was to erase the device in a UV eraser for around thirty minutes, program it, test it, and repeat with a code change, typically rotating several parts through the process at once.[485] A common development workaround of the period was an emulator that appeared to the target system as its memory chip while appearing to the development machine as ordinary writable memory, so code could be iterated without repeatedly burning and erasing physical parts.[247]

### Electrically erasable microcontrollers

The first EEPROM-based microcontroller removed the two existing development burdens at once: there was no longer a need to remove the chip and place it in a UV eraser between attempts, and no need to buy a large and expensive in-circuit emulator to stand in for the device.[24] The corporate version of this transition is anchored at Microchip, where, as chief executive Steve Sanghi describes it, a company losing money selling commodity memory applied its own EEPROM process to a microcontroller architecture, producing parts the customer could program instead of parts the factory programmed.[632] The cycle time this replaced was sixteen weeks of waiting for factory-programmed parts, during which the code would change and the process would start over; compressing that loop is what made the architecture take hold.[632]

These were separate fabrication technologies rather than successive replacements. Decades later, the original ROM-based part, the electrically erasable part, and a wide range of flash parts all continued to run through the same fab, each on the process it was designed for.[632]

The part that opened microcontroller work to hobbyists executed directly from electrically erasable memory rather than flash, and with one or two kilobytes as the largest capacity available, assembly language was required simply to achieve useful speed and fit.[490] Reprogrammability alone was not what made such parts accessible; the decisive factor was the availability of cheap programmers for them, and it was the combination of an electrically erasable chip and a programmer an individual could afford that moved microcontroller development out of professional laboratories.[287]

## Device characteristics

The high voltage needed to erase the memory cells was never eliminated; it was moved inside the package. On-chip boost circuits generate the required voltage, so the part operates from an ordinary low-voltage rail and the designer never sees the requirement.[236]

Write endurance is a primary constraint in technology selection. Even good electrically erasable memory is rated in the region of a million write cycles, so an application writing hundreds or thousands of times per second requires ferroelectric memory with effectively unlimited endurance, and pays the associated cost.[428]

A recurring part-selection trap is the assumption that a microcontroller includes a few hundred bytes to a few kilobytes of internal non-volatile storage for constants and settings, discovered late when the specific chosen part turns out to have none.[428] Within a single vendor family, the low-power variant may include that internal storage while the otherwise identical standard part does not, and the premium for the version that has it can be around forty cents, which is substantial at the volumes these parts sell.[428] The cheaper resolution is usually an external serial memory chip, available for a few cents, rather than upgrading to a more expensive microcontroller variant; adding a part beats changing the processor when the only thing missing is storage.[428]

## Failure modes

The classic field failure of windowed erasable parts is light ingress. A product shipped with the erase window uncovered allows ambient light in through vent holes, slowly erasing the memory over years so the product begins misbehaving long after it left the factory.[27] The variants of the failure are defined by what was used to cover the window: tape that eventually falls off, paint that ultraviolet light penetrates anyway, or a white paper label that passes enough light to erase the device slowly.[236]

What makes these failures expensive is that a single flipped bit rarely fails cleanly. Rather than producing an obvious memory fault, it produces behaviour that leads the investigation toward an entirely different part of the circuit, and a week can disappear into finding one dead bit.[68] The same shape of failure appears as a characteristic debugging nightmare for the solo engineer — one unset bit in one memory device on which an entire chain of behaviour depends — and the countermeasure relied on in the absence of colleagues to check the work is obsessive written notes acting as a second brain.[474]

Long dormancy is its own failure mode. Equipment powered up only once a year can come back with its stored configuration degraded, presenting as a machine that no longer knows what it is and raising unrelated fault indications.[220]

## Applications

### Board identification and configuration

A standard use of a small EEPROM is board identification: an add-on board carries a small memory holding a description of how its pins are used, and the host reads it at boot and configures its pin multiplexing accordingly.[235] The motivation is beginner experience rather than technical necessity — selecting the right library manually works, but the design goal is that someone attaching a sensor board can plug it in and have it configured at boot without knowing anything about it.[235]

The production version of the same idea pairs a unique serial number with about ten bytes of writable memory holding a product code, written at the factory on a programming jig, so a system can identify both which type of board is plugged in and which individual unit it is.[337] Serial numbering can be folded into the existing test step: the automated test software writes the serial number to on-board memory and increments it for each board, whether that memory is inside the microcontroller or a separate chip.[585] A comparable per-unit configuration flow programs customer-specific parameters at the end of the line: the shipping label is scanned, a database lookup returns the frequency that customer chose, the value is flashed into the device's memory on a pogo-pin bed, and a test signal is transmitted at that frequency to verify the unit before it is boxed.[350]

### Device identity and security

Memory parts with a factory-programmed unique network address solve the unique-identifier problem cleanly, provided a different part goes into each unit; pulling parts from one bag and reusing a single device gives every unit the same address, defeating the entire purpose.[125]

Because device identity often lives in a few bytes of memory rather than in the silicon, cloning a USB instrument can be accomplished by copying the memory contents so the counterfeit identifies itself as the genuine product to the host software. On the Saleae programme, where this occurred with the company's logic analysers, Joe Garrison describes one vendor's response as writing gibberish into a suspect device's memory — bricking it by corrupting the one part that cannot be replaced from the outside, an aggressive countermeasure with obvious consequences for anyone misidentified.[237] A widely repeated theory that another vendor detected clones by timing memory reads was, per Mark Garrison's account of the same episode, simply wrong: the repeated read attempts were a routine check for a failed memory part, a useful reminder that inferred intent behind observed behaviour is often invented.[237]

Tamper resistance in payment and gaming hardware is built around the opposite principle — erasing the stored secret. Conductive meshes are arranged so that drilling into the enclosure shorts a trace and wipes the memory, with battery backup keeping the mechanism live while the device is off.[318] The inverse design appeared in early mobile phones, where the identity number sat in a socketed memory chip and the connector to the main board used the same eight-pin arrangement as the chip itself; reprogramming the identity required only unplugging one part, which made riveting the assembly into the chassis pointless.[294]

### Non-storage roles

A memory chip can replace combinatorial logic outright by acting as a lookup table, taking the inputs as an address and returning the output word. In Ben Eater's breadboard computer project, this substitution is presented as a legitimate alternative that also sidesteps the logic minimisation techniques usually taught alongside it.[444] In some programmable logic devices the memory cells are the configuration rather than a store of it: the cells themselves join the logic together, so the device is configured the instant it powers up with no separate bitstream to load.[504]

Small serial memories are also sold as finished data products rather than blank storage; a six-pin font chip, for example, carries multiple character sets and sizes ready to be read out by a microcontroller, removing the font from the firmware image entirely.[700] An unusual programming channel demonstrated on a board designed by Adam Wolf uses no programmer or cable at all: the board is held against a computer monitor, the screen blinks black and white squares at a pair of light sensors on the board, and the microcontroller rewrites its own stored pattern from what it reads.[167]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 24 | Solar Cells, SparkFun, TSMC - The Detroit Debunking | https://theamphour.com/the-amp-hour-24-the-detroit-debunking/ | |
| 27 | 555 Contest, Computer Museum, Octopart - The Green Pen Hornswoggle | https://theamphour.com/the-amp-hour-27-the-green-pen-hornswoggle/ | |
| 68 | Radiation Chips & Old Package Types - Technocratic Toilet Troubleshooting | https://theamphour.com/the-amp-hour-68-technocratic-toilet-troubleshooting/ | |
| 125 | An Interview with Ian Lesnet - Bus Buccaneer Builder | https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/ | December 10, 2012 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 220 | An Interview with Shaun Meehan - Doctiloquent Dove Deployer | https://theamphour.com/220-an-interview-with-shaun-meehan-doctiloquent-dove-deployer/ | October 13, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 236 | Questioning Everyday Prototyping - Verrucose Vehicle Vitilitigation | https://theamphour.com/236-questioning-everyday-prototyping-verrucose-vehicle-vitilitigation/ | February 10, 2015 |
| 237 | An Interview with Joe and Mark Garrison - Subtly Spelling SayLeeAy | https://theamphour.com/237-an-interview-with-joe-and-mark-garrison-subtly-spelling-sayleeay/ | February 17, 2015 |
| 247 | An Interview with Voja Antonic - Gerontogenous Galaksija Genesis | https://theamphour.com/247-an-interview-with-voja-antonic-gerontogenous-galaksija-genesis/ | April 29, 2015 |
| 287 | Pull The Trigger | https://theamphour.com/287-pull-the-trigger/ | February 17, 2016 |
| 294 | Live from Serbia with Mike Harrison | https://theamphour.com/294-live-from-serbia-with-mike-harrison/ | April 13, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 337 | Fake it till you make it | https://theamphour.com/337-fake-it-till-you-make-it/ | February 22, 2017 |
| 350 | An Interview with Zach Dunham | https://theamphour.com/350-an-interview-with-zach-dunham/ | July 3, 2017 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 444 | An Interview with Ben Eater | https://theamphour.com/444-an-interview-with-ben-eater/ | May 27, 2019 |
| 474 | An Interview with Nash Reilly | https://theamphour.com/474-an-interview-with-nash-reilly/ | January 12, 2020 |
| 485 | An Interview with John Day | https://theamphour.com/485-an-interview-with-john-day/ | March 22, 2020 |
| 490 | An Interview with Ben Heck(endorn) | https://theamphour.com/490-an-interview-with-ben-heckendorn/ | April 27, 2020 |
| 504 | This Is Just A Tribute | https://theamphour.com/504-this-is-just-a-tribute/ | August 9, 2020 |
| 585 | Return of the Trade Show Jedi | https://theamphour.com/585-return-of-the-trade-show-jedi/ | April 10, 2022 |
| 632 | Steve Sanghi - Microchip CEO for 31 Years! | https://theamphour.com/632-steve-sanghi-microchip-ceo-for-31-years/ | May 15, 2023 |
| 688 | The Tandy Train | https://theamphour.com/688-the-tandy-train/ | February 11, 2025 |
| 700 | Beware of the Overachievers | https://theamphour.com/700-beware-of-the-overachievers/ | August 7, 2025 |
