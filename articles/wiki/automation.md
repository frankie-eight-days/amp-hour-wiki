---
title: Automation
concept: automation
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

**Automation** is the substitution of machinery, control systems, and scripted processes for human labour, a substitution governed primarily by economics rather than by technical capability.[335][141] The decision to automate is arithmetic: count the shifts, the workers on each, the hours and the wage, and compare the total against the cost of the equipment until a balance point appears.[335] Because equipment can run effectively around the clock, automation wins eventually in any task where it is suitable; the open questions are when, and which tasks go first.[300] The technology itself is rarely the constraint—industrial robot arms have been available for decades—so what changes when a workplace automates is the economic balance rather than what is possible.[335]

## Economics

Where a process stays manual it is usually about cost rather than capability: if people can be found to do the work cheaply enough there is no incentive to invest, so the presence of manual labour is evidence about wages rather than about technical difficulty.[141] Industrial robots are plausibly more expensive than the humans they replace, so automation is not automatically the cheap option and the case must be made per application.[391] Chris Denney, drawing on visits to assembly operations, holds that the underlying economics run the other way once equipment is in place—machines are cheap and people are expensive—so the visible sign of a well-run shop is machines running with nobody standing in front of them, while people manually loading and unloading equipment all day is the opposite signal.[411]

The decision rests on measurement. Dave Jones describes timing workers with a stopwatch across many employees to establish an average before concluding that an automated system delivering parts to them would be quicker.[240] Any competent operation measures the efficiency of an automation project against what preceded it, precisely to confirm the investment came out ahead; the absence of such measurement is itself a warning sign.[335] Published figures from automated plants are rare because companies keep them internal, which makes disclosed sets notable: one reported case replaced ninety percent of the workforce while production rose by 250 percent and defects dropped by eighty.[335]

Automation pays at small batch sizes and does not require huge runs: a buffer holding fifteen boards ahead of a machine and an unloader holding fifteen after it lets an operator start the job and leave, which is the whole benefit.[411]

## Electronics manufacturing

Electronics assembly crossed an economic threshold: where the cheap route was once hand-stuffing boards wherever labour was cheapest, buying even a low-end pick-and-place machine became both faster and cheaper than that.[143] The work does not vanish when a machine takes over; it moves. Loading a placement machine requires organisation, a stock room and continuous attention to keep the equipment running, so a substantial amount of labour surrounds the automated step.[143] A second-order effect runs the other way from the usual story: the facility needed to house automated assembly equipment must be of a higher standard than a hand-assembly shop, so working conditions can improve even as headcount falls.[143]

The self-assembly threshold for a small producer sits around a hundred units. Below it, assembling in-house can make sense under schedule pressure; above it, going to a contract manufacturer is the answer unless there is a specific financial reason not to.[319] What makes in-house assembly work at that scale is constraining the design to the process: using only parts already loaded in the machine and building up scripts over years, so the whole flow is optimised around one setup.[319] The human limit on repetitive kitting work is about a hundred units in one sitting before eyes and hands degrade; two or three hundred over a weekend leaves the person exhausted, which is the practical reason such work gets automated first.[229]

What separates well-run assembly shops is thinking about the whole flow rather than the machine. Denney reports that the good ones decide in advance how a new machine will be fed and unloaded and buy the automation around it rather than just the machine itself; across roughly a hundred contract manufacturers and original equipment makers visited, only fifteen or twenty had anything other than a table or a cardboard ramp catching boards coming out of the reflow oven.[411] The larger cumulative gains are in unglamorous places rather than on the production floor—receiving, shipping and clerical steps such as putting an order onto the schedule—each of which may take only thirty seconds but compounds when many are eliminated.[411] Programming boards during assembly has its own quantity threshold: at around fifty boards it does not pay; at five hundred it does, because the setup can be automated, though parts arriving pre-programmed from the supplier is better than either.[411]

Specific stages resist automation for physical reasons: parts that cannot pass through a water wash, masking operations, and anything requiring high dexterity.[141] Wiring harnesses remain substantially hand-made, built on large peg boards where an operator loops the wires by hand; there is automation around the process, but the first build of a new harness is where the difficulty concentrates.[619] The stubborn manual step in assembly automation is new component data: an unfamiliar part still requires a person to find the datasheet and determine its dimensions before the machine can handle it, and that problem is not solved.[411] On a benchtop placement machine, Stephen Hawes identifies the fully automated case as 8 and 12 millimetre tape, with wider tapes handled from strip or tray; which board suits the machine matters less than why the boards are needed, since that determines the acceptable degree of manual intervention.[686]

## Limits and failure modes

The most prominent public reversal on automation came from a heavily automated vehicle line whose own founder concluded that excessive automation had been a mistake and that humans were underrated.[391] The mechanism behind that reversal is inflexibility: reconfigurable robots do not really exist yet at large manufacturing scale, so tooling up a precisely automated process while the product is still changing locks in decisions that must be revisited.[391]

The characteristic failure mode of automation is silence: a process that stops working can go unnoticed for months precisely because its whole purpose was that nobody had to watch it, so anything automated needs its own check that it is still running.[326] An agricultural monitoring deployment failed on an assumption rather than on technology: Akiba describes water levels in rice paddies relayed to a smartphone application, but most of the farmers were older and did not have smartphones, so the automation reached nobody.[245]

The trajectory of machine design runs from custom toward general: most machines are bespoke now, more dexterous general-purpose arms will generalise and fall in price and then be integrated more widely, but a custom machine still beats a general one at its own task.[277] Nadya Peek frames the enabling direction as lowering the barrier to building automation, which gives access to precision that changes what can be built at all; a custom coil-winding machine assembled in about two hours produced identical coils every time, which hand winding could not.[208]

## Labour and employment

On the attribution question, Gerry Roston holds that most manufacturing jobs that disappeared went to automation rather than to offshoring, a different diagnosis with different consequences from the one usually offered.[334] The most exposed work is not the visible service jobs commonly imagined but long-haul driving and document-heavy professional work, where the task is well defined and the volume is large.[300] Long-distance haulage is a strong candidate for structural reasons: the vehicle can run continuously without rest, and much of the driving already happens at night when conditions are simplest.[334]

There is a wage mechanism separate from job losses: as machines take over more of a task, the residual human skill becomes less specialised, which puts downward pressure on the pay of the people still doing it.[582] The transition matters as much as the destination: automating a process that people currently perform creates dispute in a way that designing full automation from the start does not, so the same end state produces very different friction depending on the path.[278] The usual outcome of automating menial work is not elimination but a shift up the value chain with wider coverage—someone who checked the water in twenty pools a day becomes the person managing the pools for a region.[615] The disappointment with automation so far is that it removed drudgery without reducing hours; the freed time was absorbed by whatever came next, which is a choice about expectations rather than a property of the technology.[622]

## Automation in engineering work

The automation that displaces electronics designers is not automated design tools but silicon integration: chip companies absorb more functions onto the die to capture more of the system, removing the design work rather than performing it.[219] The visible consequence is that following an application note gets a newcomer capability that used to need a team, with high-speed interfaces working on a two-layer board provided the connector is close enough to the chip.[219] Nobody objects while this happens because each step is beneficial—products get built faster and more becomes possible—so the displacement is real but invisible in the moment.[219] Whoever owns the automation with human intelligence directing it comes out ahead, because the machinery supplies no creativity of its own; that is the argument for being on the building side rather than the displaced side.[219]

Command-line tools remain necessary for automation even as vendors push integrated environments, because scripting a build or a test requires something a graphical interface cannot provide; their absence closes off the whole approach.[78] Automated testing for hardware follows the software pattern: Jonathan Georgino describes a script that stimulates the board, runs a suite and reports which tests a change has broken, and bench instruments increasingly ship Python libraries, so measurement equipment can be pulled into the same scripts.[461] On the purchasing side, distributor interfaces lag: data access through published interfaces is reasonably established, but ordering programmatically is not, so full procurement automation remains out of reach.[542]

Laziness in the specific sense of refusing to repeat a manual loop is a virtue in engineering; Ryan O'Hara describes automating data acquisition and analysis rather than performing it repeatedly as what makes the measurement work tractable.[153] Jeremiah Gillis's rule as a consultant is to automate or buy out everything that is not what one's time is for: payroll, tax filing and bookkeeping through a paid service costs less than the hours it consumes, because those hours are better spent on client work.[492]

A realistic forecast for robotics is steady expansion rather than explosive growth; Ariel Briner expects no hockey stick comparable to the internet, but continued deployment wherever safety, price, performance and flexibility line up for a given problem.[614] The consulting opportunity in robotics is horizontal rather than vertical: power systems, radios, computing and cameras in a robot are not very different from those elsewhere, so expertise in one of those technologies transfers directly into helping robotics companies reach market sooner.[614]

## Keeping the human in the loop

The staged approach to automating a warehouse is to remove the movement first—bringing shelves to a stationary worker—and keep the human for recognising and picking the object; the second stage, replacing the picking itself, is the genuinely hard part.[240] The engineering counterpoint to full autonomy, drawn from spaceflight, is redundancy: the lunar module carried six independent methods of launching if things failed, and every account from the crews stresses backups upon backups.[654] The reason humans stay in the loop at all is the same reason those backups existed: something goes wrong and a person has to take over, which is why training for the manual case remains necessary even in a highly automated system.[654] Fran Blanche puts the argument against removing the human from the loop in non-technical terms: reliability and convenience are bought by giving up the randomness, mistakes and fallibility that come with people, and that trade has consequences worth naming explicitly.[263]

## Limits of scope

The strongest counter-argument to automating everything is that the simple version is often better: a light switch will always be simpler, cheaper and more reliable than any automation system that replaces it, and that comparison does not change with technology.[351] The rebuttal is that such comparisons reason from the systems already known, while the real opportunity in a domain is usually something the current framing cannot see, in the way that a paper-reel calculator argument does not anticipate what a computer becomes useful for.[351] The dividing line is universality: where automation is genuinely useful to everyone it wins and doing the task any other way becomes silly; where it is not, people keep the older method because it remains better and simpler for them.[351]

At the individual scale, a defensible limit is that over-automation costs more effort than it returns, and there is real value in keeping direct manual control of things one actually enjoys controlling.[683] Useful home automation is conditional and retrofitted rather than wholesale: an existing door with a sensor added, plus a rule that closes it if it has been open for twenty minutes, solves a real problem without replacing anything.[660]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 78 | Alteritous Andy's Absquatulation | https://theamphour.com/the-amp-hour-alteritous-andys-absquatulation/ | January 16, 2012 |
| 141 | FPGAs, Robots & Thermocouples - Wampum's Wavering Worth | https://theamphour.com/the-amp-hour-141-wampums-wavering-worth/ | April 15, 2013 |
| 143 | PCBs, Tektronix & Ham Radio - Habitual Handicraft Hangups | https://theamphour.com/the-amp-hour-143-habitual-handicraft-hangups/ | April 29, 2013 |
| 153 | An Interview with Ryan O'Hara - Keyed, Kerfed Kapton | https://theamphour.com/the-amp-hour-153-keyed-kerfed-kapton/ | July 8, 2013 |
| 208 | An Interview With Nadya Peek - Gallant Gcode Gerontology | https://theamphour.com/208-an-interview-with-nadya-peek-gallant-gcode-gerontology/ | July 21, 2014 |
| 219 | Get Smart About Automation - Caducous Cyborg Concerns | https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/ | October 6, 2014 |
| 229 | MightyHohm For The Holidays - Kaiser Keyzer's Kits | https://theamphour.com/229-mightyhohm-for-the-holidays-kaiser-keyzers-kits/ | December 23, 2014 |
| 240 | Compare and Contrast Tech Entitlement - Worldly Working Wonks | https://theamphour.com/240-compare-and-contrast-tech-entitlement-worldly-working-wonks/ | March 10, 2015 |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 263 | An Interview with Fran Blanche | https://theamphour.com/263-an-interview-with-fran-blanche/ | August 19, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 278 | Our Second Callin Show(ish) | https://theamphour.com/278-our-second-callin-showish/ | December 16, 2015 |
| 300 | Three Hundred Down, Three Hundred To Go | https://theamphour.com/300-three-hundred-down-three-hundred-to-go/ | May 25, 2016 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 334 | An Interview with Gerry Roston | https://theamphour.com/334-an-interview-with-gerry-roston/ | February 1, 2017 |
| 335 | When the TV watches you | https://theamphour.com/335-when-the-tv-watches-you/ | February 8, 2017 |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 391 | Only A Transmitter | https://theamphour.com/391-only-a-transmitter/ | May 6, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 461 | An Interview with Jonathan Georgino | https://theamphour.com/461-an-interview-with-jonathan-georgino/ | October 6, 2019 |
| 492 | More Electronics Consultant Impedance Matching | https://theamphour.com/492-more-electronics-consultant-impedance-matching/ | May 10, 2020 |
| 542 | Component Management with Jan Rychter | https://theamphour.com/542-component-management-with-jan-rychter/ | May 17, 2021 |
| 582 | The Same Wavelength | https://theamphour.com/582-the-same-wavelength/ | March 20, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 615 | Augmented Engineering | https://theamphour.com/615-augmented-engineering/ | January 16, 2023 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 622 | Building Firmware and Hardware for Trade Shows with Mike Szczys | https://theamphour.com/622-building-firmware-and-hardware-for-trade-shows-with-mike-szczys/ | March 5, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 683 | Troubleshooting is the skill | https://theamphour.com/683-troubleshooting-is-the-skill/ | November 20, 2024 |
| 686 | A Benchtop Pick and Place with Stephen Hawes | https://theamphour.com/686-a-benchtop-pick-and-place-with-stephen-hawes/ | January 21, 2025 |
