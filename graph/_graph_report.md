# Concept Co-occurrence Graph Report

Generated from `census/luna-v3` (717 episodes) + `canon/` alias table and vocabulary.

## Build parameters

| parameter | value |
|---|---|
| min episodes per node | 5 |
| co-occurrence window | +/- 2 paragraphs |
| edge weight | distinct episodes co-occurring |
| min edge weight | 2 |
| top-K prune per node | 8 |
| Louvain resolution | 1.6 |

## Counts

| metric | value |
|---|---|
| candidate concepts (>=5 episodes) | 5198 |
| isolated (no surviving edge), dropped | 1182 |
| **nodes in graph** | **4016** |
| raw candidate edges | 134506 |
| edges after weight>=2 | 18386 |
| **co-occurrence edges after top-8 prune** | **12437** |
| hierarchy (broader) edges | 339 |
| communities | 26 |

## Communities

Community 25 is a catch-all: 85 nodes from 39 micro-communities that sit in their own disconnected components (mostly isolated pairs), so there was no neighbouring community to merge them into. Every other community has >=10 members.

| id | auto-label (top-3 by degree) | size | top-10 members |
|---|---|---|---|
| 0 | capacitor, led, op amp | 316 | capacitor, led, op-amp, transistor, resistor, transformer, diode, soldering, inductor, mosfet |
| 1 | microcontroller, arduino, raspberry pi | 303 | microcontroller, arduino, raspberry-pi, python, adafruit, microchip, maker-faire, development-board, embedded-system, assembly-language |
| 2 | pcb fabrication, pcb, pick and place machine | 264 | pcb-fabrication, pcb, pick-and-place-machine, bga, pcb-assembly, pcb-lead-time, breadboard, reflow-oven, hand-soldering, solder-mask |
| 3 | bluetooth, wifi, internet of things | 262 | bluetooth, wifi, internet-of-things, antenna, esp32, radio-frequency, lora, 2-4-ghz-band, ham-radio, cloud-computing |
| 4 | kicad, altium, open source hardware | 260 | kicad, altium, open-source-hardware, pcb-layout, eagle, schematic, open-source-software, gerber, github, pcb-design |
| 5 | digi key, component sourcing, bill of materials | 241 | digi-key, component-sourcing, bill-of-materials, contract-manufacturer, mouser, china, china-manufacturing, connector, element14, supply-chain |
| 6 | fpga, arm, risc v | 231 | fpga, arm, risc-v, asic, verilog, xilinx, intellectual-property, compiler, altera, stm32 |
| 7 | linux, usb, ethernet | 207 | linux, usb, ethernet, zephyr, flash-memory, rtos, can-bus, windows, firmware-update, operating-system |
| 8 | youtube, twitter, consulting | 207 | youtube, twitter, consulting, camera, contextual-electronics, hackaday, engineering-career, facebook, podcast, reddit |
| 9 | oscilloscope, multimeter, soldering iron | 194 | oscilloscope, multimeter, soldering-iron, power-supply, ebay, agilent, logic-analyzer, test-equipment, hewlett-packard, tektronix |
| 10 | battery, electric vehicle, tesla | 187 | battery, electric-vehicle, tesla, solar-power, battery-life, solar-panel, spacex, power-grid, battery-pack, elon-musk |
| 11 | kickstarter, startup, venture capital | 176 | kickstarter, startup, venture-capital, prototype, crowdfunding, patent, hardware-startup, profit-margin, manufacturing, startup-funding |
| 12 | intel, texas instruments, semiconductor fab | 157 | intel, texas-instruments, semiconductor-fab, analog-devices, tsmc, samsung, freescale, chip-design, linear-technology, wafer |
| 13 | firmware, engineering education, software | 153 | firmware, engineering-education, software, reverse-engineering, electrical-engineering, jtag, def-con, automated-testing, hardware, mechanical-engineering |
| 14 | apple, google, amazon | 145 | apple, google, amazon, android, iphone, mit, smartphone, 6502, microsoft, radio-shack |
| 15 | analog to digital converter, i2c, spi | 137 | analog-to-digital-converter, i2c, spi, digital-to-analog-converter, uart, accelerometer, gpio, pwm, temperature-sensor, bandwidth |
| 16 | robotics, artificial intelligence, sensor | 133 | robotics, artificial-intelligence, sensor, robot, machine-learning, drone, motor, quadcopter, automation, lidar |
| 17 | 3d printing, 3d printer, injection molding | 100 | 3d-printing, 3d-printer, injection-molding, design-for-manufacturing, laser-cutter, makerbot, hackerspace, cnc-machine, 3d-modeling, 3d-cad |
| 18 | datasheet, internet, 555 timer | 65 | datasheet, internet, 555-timer, jim-williams, application-note, edn, bob-pease, analog-circuit-design, field-application-engineer, thermocouple |
| 19 | hiring, resume, jeff kaiser | 52 | hiring, resume, jeff-kaiser, jerry-ellsworth, augmented-reality, valve, cast-ar, hardware-engineer, software-engineer, virtual-reality |
| 20 | digital signal processing, software defined radio, microphone | 38 | digital-signal-processing, software-defined-radio, microphone, hackrf, gnu-radio, great-scott-gadgets, fm-radio, waterfall-plot, voice-recognition, audio-compression |
| 21 | signal integrity, differential signaling, electromagnetic interference | 35 | signal-integrity, differential-signaling, electromagnetic-interference, electromagnetic-compatibility, electrostatic-discharge, rf-engineering, differential-pair, crosstalk, howard-johnson, eye-diagram |
| 22 | lcd, electronics industry, off the shelf component | 28 | lcd, electronics-industry, off-the-shelf-component, seven-segment-display, oled, custom-lcd, micro-supply, multiplexing, potting, conformal-coating |
| 23 | circuit breaker, three phase power, electrical safety | 20 | circuit-breaker, three-phase-power, electrical-safety, split-phase-power, mains-electricity, air-conditioner, busbar, electrical-arcing, heat-pump, din-rail |
| 24 | user interface, graphical user interface, skype | 20 | user-interface, graphical-user-interface, skype, computer-mouse, xerox-parc, mumble, video-conferencing, google-hangouts, user-experience, audacity |
| 25 | unclustered fragments | 85 | vibration-testing, hackers, thermal-testing, thermal-chamber, war-games, hydrofluoric-acid, sputtering, nitrogen, sneakers, steve-blank |

## Top-20 bridge concepts (approx. betweenness)

| rank | concept | betweenness | community | degree | episodes |
|---|---|---|---|---|---|
| 1 | microcontroller | 0.1537 | 1 | 345 | 371 |
| 2 | fpga | 0.1104 | 6 | 301 | 312 |
| 3 | arduino | 0.0993 | 1 | 279 | 280 |
| 4 | oscilloscope | 0.0609 | 9 | 180 | 316 |
| 5 | kickstarter | 0.0481 | 11 | 168 | 246 |
| 6 | altium | 0.0470 | 4 | 177 | 229 |
| 7 | open-source-hardware | 0.0453 | 4 | 158 | 268 |
| 8 | digi-key | 0.0450 | 5 | 194 | 312 |
| 9 | kicad | 0.0386 | 4 | 180 | 241 |
| 10 | pcb | 0.0379 | 2 | 108 | 266 |
| 11 | bluetooth | 0.0374 | 3 | 130 | 217 |
| 12 | firmware | 0.0320 | 13 | 117 | 223 |
| 13 | led | 0.0314 | 0 | 94 | 213 |
| 14 | internet-of-things | 0.0300 | 3 | 99 | 198 |
| 15 | usb | 0.0285 | 7 | 112 | 224 |
| 16 | youtube | 0.0263 | 8 | 82 | 262 |
| 17 | capacitor | 0.0255 | 0 | 95 | 200 |
| 18 | pcb-fabrication | 0.0249 | 2 | 118 | 212 |
| 19 | component-sourcing | 0.0224 | 5 | 117 | 206 |
| 20 | apple | 0.0222 | 14 | 81 | 162 |

## Surprises and caveats

- **1182 of the 5198 qualifying concepts (23%) fell out as isolates.** They appear in >=5 episodes but never share a paragraph window with the same partner in 2+ episodes -- they are one-off asides scattered across the archive rather than parts of a recurring conversation. The weight>=2 rule is doing real work: it cut raw candidate edges from 134506 to 18386 (86%).
- **The top-8 prune is not a degree cap.** Because a kept edge only needs one endpoint to rank it, hubs still accumulate huge degree: max degree is 345 (microcontroller) while the median node has degree 3 and 18 nodes exceed degree 100. That asymmetry is what makes the betweenness ranking meaningful, but a force-directed layout will need hub-aware repulsion.
- **Betweenness reproduces the show's actual structure, not just popularity.** The bridges are the concepts that sit between design domains (microcontroller, fpga, arduino) and between engineering and commerce (kickstarter, digi-key, open-source-hardware). Note that `oscilloscope` ranks 4th on betweenness while sitting in a fairly self-contained test-gear community -- it is the hinge between hands-on debugging and everything else.
- **Strongest edges are substitution pairs, not topic pairs.** The heaviest weights are `digi-key`/`mouser` (100 eps), `altium`/`kicad` (80 eps), `eagle`/`kicad` (66 eps) -- tools that get named together because hosts compare them, not because the concepts are related. Anything ranking 'related concepts' for the wiki should expect rivals, not neighbours, at the top.
- **A canon bug surfaced through the graph:** community 19 contains `jerry-ellsworth`, but the person is Jeri Ellsworth (see episode 0173's own title slug, `an-interview-with-jeri-ellsworth`). The misspelling comes out of the census extraction and the alias table maps it to itself, so it never merged. Worth a canon fix -- other person-type nodes may have the same problem.
- **Hierarchy edges are sparse at this tier:** only 339 of the vocabulary's 7112 `broader` relations have both endpoints in the >=5-episode node set, so the hierarchy layer is a light overlay rather than a spanning tree.
- **Type mix of the graph:** component 850, company-product 463, software 396, technique 390, manufacturing 345, concept-principle 289.
- **522 nodes have zero `explains` mentions** -- named but never actually taught. These are the wiki's thin-content risk: a page can be generated for them, but there is no explanatory audio behind it.
