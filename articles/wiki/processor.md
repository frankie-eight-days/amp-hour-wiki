---
title: Processor
concept: processor
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

A **processor** is the component at the centre of an embedded or computing system that executes program instructions, and its defining engineering property in practice is that it must stop and crunch the data it handles, which makes its timing non-deterministic compared with streaming alternatives such as programmable logic.[179] Its significance in system design lies less in the part itself than in the software ecosystem around it: building a processor is comparatively simple, while building the compilers, debuggers and libraries that make one usable is the hard part, and that asymmetry is what makes an established instruction set valuable to its owner.[374] Selection, power management and integration of the processor dominate real design effort, because switching the part means retargeting an entire software stack and forfeiting accumulated work.[300][148]

## Processors versus programmable logic

The boundary between a processor and programmable logic is sharp. Watching three signal lines toggling at ten megahertz and extracting a bit pattern on the fly is beyond any processor on the market, and that class of problem is where programmable logic earns its cost; where a fifty-cent microcontroller can do the job, it should be used instead.[103] The architectural difference is that a processor has to stop and crunch the data, producing non-deterministic timing, while programmable logic streams data through as it arrives; where the requirement is that timing be exactly right rather than merely fast, that difference decides the architecture.[179]

Within the programmable logic industry, vendors putting hard processors back into their devices was a concession rather than an advance: soft processors instantiated in the fabric were not what customers wanted, and the industry response was to commit the processor function to fixed silicon.[150]

## Performance, power, and size

Faster processors are not what unlocks new functionality; shrinking the size and the power is.[183] Useful processing happens at sub-microwatt power levels — a part clocking at thirty-two kilohertz still moves data around usefully — and what has enabled new applications is the collapse in the power required to do modest work rather than raw speed.[183] That reframing is what makes energy harvesting, even from static charge, worth pursuing, because the target it has to reach keeps coming down.[183]

The genuine demand for processing power lives in vision: even on the fastest available boards, real-time vision work was limited to something like 640 by 480 at fifteen frames per second, which makes the question of what all that performance is for concrete.[235]

## Power management in system design

Integrating touch sensing, security and similar continuous functions into a companion chip means the main processor never has to wake for them; battery life improves out of proportion to the function moved, because the cost avoided is the wake-up rather than the work.[269] In Colin Karpfinger's design pairing a radio module with an application processor, each processor can put the other to sleep, giving the power management decision to whichever one holds the relevant information — the radio module knowing there is nothing to send, or the application knowing the user has finished.[226]

Firmware behaviour also carries electrical consequences: a processor changing operating mode changes the current drawn from the supply, and that step translates into conducted emissions, so a compliance failure can originate in firmware that no schematic review would flag.[184]

## Selection and switching costs

Engineers stay with processors they already know because a working board support package or a default project that builds is worth more than a cheaper part; paying ten dollars more per chip to avoid starting from nothing is a rational trade, and it is how most part selection actually happens.[148] Changing processor means retargeting the software and forfeiting the accumulated polish that went into the existing stack, so the component saving has to exceed that lost work — which is why cost-reduction exercises so often stop at the processor.[300]

The claim that choosing a common architecture permits seamless movement between vendors does not survive contact with a real design: the instruction set ports, but the peripherals, the register maps and the tooling do not.[126] There is also no single obvious processor choice, because the range of applications is effectively unbounded and every one of them justifies another variant; selection is therefore a recurring cost of the discipline rather than a problem to be solved once.[187] For the engineer, being application-oriented rather than processor-oriented is a defensible stance — the processor is a means to an end, and the interesting constraints usually live in the application rather than in the part.[187]

### Capacity and obsolescence failures

Discovering at the third prototype that the firmware will not fit the chosen processor is a late and expensive failure, and the proposal that follows is usually to drop a feature and revisit the processor in a later revision — which in practice means the feature never arrives.[296] Before accepting that a processor change means rewriting the software, a designer should check for a pin-compatible member of the same family with the same tools; large families exist precisely so that a capacity problem can be answered with a different part number rather than a redesign.[296] Product line refreshes also routinely arrive as an obsolescence emergency: the assumption that the processor will remain available holds until it does not, and by then the redesign is unplanned and urgent.[363]

## Integration and packaging

An application processor and a bare processor are different products: an application processor arrives with display drivers, memory and peripherals integrated and is nearly a system, while a bare processor requires everything to be built around it before it does anything useful.[58] Large memory in a mobile-class part comes from stacking the memory die physically on top of the processor die inside one package, which is why such a device offers far more RAM than its pin count suggests and why the memory is not separately sourceable.[54]

Putting a microcontroller and an application processor on the same board gives both real-time behaviour and a general-purpose operating system with a graphical interface — a combination that neither a small development board nor a single-board computer provides alone.[316] At the other extreme of integration, embedding a small processor inside a custom chip to handle low-speed state during idle periods keeps the design from hard-coding behaviour into silicon, which is what preserves the ability to change the product after tape-out.[147]

The partitioning of work between hardware and firmware also follows a discipline: switch debouncing belongs in hardware, because handing the problem to firmware spends processor time and attention permanently to compensate for a component that a capacitor would have fixed once.[256]

## Toolchains and the software ecosystem

As Claire Wolf put it, "building a processor is actually very, very simple. The hard part usually is not building the processor": the compilers, debuggers and libraries around it are the hard part.[374] That asymmetry is what makes an established instruction set so valuable to its owner — the tools were built by a community, and the architecture's licence is what prevents anyone reusing them.[374]

Toolchain coupling to the target extends into interpreted environments. Adding compiled code to an on-device interpreted environment invokes the standard compiler against the whole firmware, so the toolchain has to know the target processor; inline assembly is handled separately by a small purpose-built translator rather than by the full compiler.[323]

## Manufacture and enabling conditions

Whatever happens to fabrication cost, processors will remain too complex to produce outside industrial facilities; predictions of home chip manufacture consistently underestimate how much of the difficulty is complexity rather than equipment cost.[31] At the market level, several enabling conditions arrived at once — adequate battery life, very cheap processors and reasonably mature software — and it is their coincidence rather than any single advance that moved connected devices from demonstration to product.[271]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 31 | Freescale, Hackerspaces, Printable Electronics - Publish Popular Parts Please! | https://theamphour.com/the-amp-hour-31-publish-popular-parts-please/ | |
| 54 | An Interview with Jack Ganssle - Embedded Elchee Epexegesis | https://theamphour.com/the-amp-hour-54-embedded-elchee-epexegesis/ | |
| 58 | Multicopter, DIY drones & Tektronix - Zappy Zendik Zoilism | https://theamphour.com/the-amp-hour-58-zappy-zendik-zoilism/ | |
| 103 | An Interview with Philip Freidin - Xenodochial Xilinx Ex-Employee | https://theamphour.com/the-amp-hour-103-xenodochial-xilinx-ex-employee/ | July 8, 2012 |
| 126 | eReaders, datasheets & board assembly - Yearly Yeasty Yapping | https://theamphour.com/the-amp-hour-126-yearly-yeasty-yapping/ | December 17, 2012 |
| 147 | An interview with Jeri Ellsworth - Absorptive Augmented Actuality | https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/ | May 27, 2013 |
| 148 | Contextual Electronics, ClubJameco and Solderpaste - Lifelong Learning Likelihood | https://theamphour.com/the-amp-hour-148-lifelong-learning-likelihood/ | June 3, 2013 |
| 150 | Solar, FPGAs and Maxim Integrated - Solar Shopper Sickness | https://theamphour.com/the-amp-hour-150-solar-shopper-sickness/ | June 17, 2013 |
| 179 | Greg Charvat Returns With A Book! - Laboratory Literature Laureate | https://theamphour.com/179-greg-charvat-returns-with-a-book-laboratory-literature-laureate/ | January 6, 2014 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 256 | Is This A Show? | https://theamphour.com/256-is-this-a-show/ | July 1, 2015 |
| 269 | Be Tidy | https://theamphour.com/269-be-tidy/ | September 30, 2015 |
| 271 | Amazon Moves In, Dave Says Run | https://theamphour.com/271-amazon-moves-in-dave-says-run/ | October 14, 2015 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 300 | Three Hundred Down, Three Hundred To Go | https://theamphour.com/300-three-hundred-down-three-hundred-to-go/ | May 25, 2016 |
| 316 | An Interview with Robert Feranec | https://theamphour.com/316-an-interview-with-robert-feranec/ | September 21, 2016 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
