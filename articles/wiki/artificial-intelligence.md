---
title: Artificial Intelligence
concept: artificial-intelligence
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Artificial intelligence, as the term is applied in electronics practice, covers machine-learning systems that derive their behaviour from training data rather than from hand-written rules.[435] The field divides cleanly into an expensive rule-creation phase, exemplified by training frameworks such as TensorFlow, and a cheap rule-application phase that even a small microcontroller can execute; the difference from a hand-written expert system is that no human ever knows what the derived rules are.[435] The release of ChatGPT marks the point at which the field entered public consciousness and companies began renaming products and businesses around it.[685] For hardware engineers the practical consequences run in two directions: machine-learning systems consume sensor inputs, which places electronics designers in the role of producing data that downstream decision-making systems can digest,[428] and the same tools are increasingly applied to the design work itself.[626]

## Historical background

The Eliza conversational program was implemented in roughly forty lines of BASIC, showing that convincing dialogue behaviour could be produced with almost no underlying intelligence.[258] Claims that electronic design automation tools use artificial intelligence are likewise not new; vendors have made the same marketing claim for around thirty years.[470]

Expectations about the underlying hardware have also shifted. Field-programmable gate arrays were initially expected to dominate machine-learning hardware because of their versatility, but graphics processors proved better suited and displaced them for that workload.[660] The economic argument against gate-array-based inference at scale is chip count and unit cost: the number of devices required makes them expensive relative to graphics processors, which are themselves not cheap.[660] NVIDIA's shift from the GTX to the RTX architecture made its consumer cards inference-capable, enabling locally hosted assistants that run on a user's own graphics card and index the user's own files and video.[660] Intel's competitive position eroded on several fronts at once over the same period: TSMC pulled ahead on process, Arm and AMD pressed the server market, RISC-V grew from a small base, and the graphics and accelerator segment was ceded to NVIDIA.[685] Intel's earlier acquisition of Movidius had been aimed at the spatial half of machine vision, combining stereo depth sensing and inference on the same silicon.[517]

## Training and inference

A model is not a self-contained algorithm; it must be trained on large volumes of real-world data, which is why Tesla built its own processors and supercomputer racks to run that training.[604] Training hardware pushes power delivery to extremes: Tesla's training racks were presented as containing one of the densest power supplies in the world measured in watts per square centimetre.[604] A characteristic failure mode of massively parallel training racks is intermittent dropout of individual processors among thousands, which disrupts the distributed job rather than crashing the machine outright.[604]

Training custom models remains out of reach for most individual developers, who are limited to using models built by others.[651] Useful competence with these tools does not require building or training models at all; knowing which tool suits which application and how to drive it is sufficient skill for most workplace needs.[631] For engineers without a data science background, the fast.ai course is an accessible entry point.[428]

Labelling is often simpler than it appears. A domain expert can produce labelled training data by physically performing the event — repeatedly opening and closing a door while watching the sensor waveform — without understanding the data itself.[525] This inverts conventional event detection, which forces the engineer to impose a mathematical model such as fixed thresholds or slope detection onto a natural signal and iterate by guess and check; a trained classifier instead starts from the desired output and derives the detector.[525] A machine-learning sensor proof of concept can be assembled for about fifty dollars, using a fifty-dollar development board with a free community edition of the model-building tooling.[525]

## Inference at the edge

Low-cost single-board modules costing around eighteen dollars combine graphics-class silicon with camera input to perform inference on board rather than in the cloud.[428] The Raspberry Pi 5, with on-chip inference acceleration, performs roughly like a good laptop of five to eight years earlier, making it practical to ingest camera data, compress video and stream it from a small embedded board.[651] Dedicated audio inference accelerators run a programmed model over a live microphone stream to classify background acoustic events such as typing, several people talking, a person shouting, or a plate being thrown.[661] Custom hardware accelerators for image and audio processing are often commissioned as exploratory projects, built first and kept only if the measured benefit justifies it.[661]

Arduino's move into industrial control paired familiar Arduino programming with terminal-block termination and ladder diagram support, with the claimed differentiator over conventional programmable logic controllers being the ability to run tiny machine-learning models on the same controller.[620]

## Robotics and autonomous systems

Onboard learning for aerial robotics is limited less by the algorithms than by resources: it demands heavy statistics plus enough memory to record flight data and process it in real time.[105] Where a drone has a fast telemetry link, the learning and heavy processing can be run on the ground station instead of onboard, with a self-contained airborne implementation being the harder ideal.[105] The Skydio drone performs onboard obstacle avoidance built on NVIDIA processors, allowing it to follow a person through a forest while avoiding branches and twigs.[538]

Tesla's own stated position was that full self-driving requires a gigantic leap in artificial intelligence before it becomes viable, while the feature was still sold as an option for around ten thousand dollars.[582] At the consumer end, a pool-cleaning robot sold on its intelligence failed to climb the pool walls, moved largely at random, and reset its own algorithm mid-run, with only partial mapping behaviour observed across repeated timed tests.[656]

## Machine vision and sensing

Most spatial-vision systems are assembled from two or three separate pieces — a neural accelerator, a general processor and a depth camera — whereas an integrated part combines the depth and inference functions.[517] Depth-and-inference boards are designed so that retargeting a reference example to a different tracked object takes roughly three lines of changed code, and some products boot straight into a person-tracking demonstration.[517]

Computed imaging is now the norm rather than the exception: modern phone cameras and large scientific instruments no longer capture an image directly but compute one by averaging and combining many frames or datasets in software.[618] The distinction still matters at the high end. High-end imaging radar is moving to full lambda-over-two phased arrays with thousands of channels at chip scale, pulling real signals out of the noise, rather than to sparse compromise arrays whose gaps are filled by inference.[729]

## Electronic design automation

DeepPCB is a cloud auto-routing service marketed on deep learning that accepts KiCad board files.[470] One proposed route to a machine-learning auto-router is supervised training on thousands of known-good board layouts with substantial graphics-processor resources behind it.[412] The structural objection is that board layout quality is dominated by component placement rather than track routing, estimated at about ninety percent placement, so an automated router that does not solve placement addresses the smaller part of the problem.[412]

Automated layout services such as Quilter are best understood as an incremental tool for board layout rather than as general intelligence, and their value judged on that basis.[654] One such service treats machine learning as one tool among several in service of a finished, verified board, and accepts human intervention in the loop when the software struggles, since the customer bought a layout rather than an algorithm.[626]

There are limits to what automation surfaces. A practising engineer's mental catalogue of parts covers cross-cutting facts — such as an eight-bit microcontroller in a five-pin package that also carries an I2C output — a kind of lateral part substitution that automated part suggestion does not surface.[262] Time spent personally laying out a board and studying its schematic also builds the mental model that makes hard debugging possible, such as tracing an unexplained result in an EMC chamber; delegating generation to a tool forfeits that context.[722]

## Software development

Vibe coding describes delegating the writing of code to a model while the human acts as product manager, supplying the specification and feedback on what works and what does not.[694] Generated code still requires a competent programmer to integrate the pieces and verify the result, because models confidently report success on tasks they have not actually completed.[631] Mistakes in generated code are harder to catch than mistakes in one's own work, both because the author of hand-written code has already formed a mental model of it and because the confident phrasing of model output lends the answer more weight than it merits.[614]

A concrete and modest use for a coding assistant is getting past the blank editor: producing something that at least semi-compiles, which the engineer then tweaks into working form.[713] On one personal project a coding assistant produced practically all of the code, an application the same practitioner distinguishes sharply from generative tools for board layout.[683] For students who have not previously written C, assistants are useful for getting syntax close enough to what they logically intend, which lets them cross from intent to compiling code.[711]

In reverse engineering, the realistic contribution of a language model is recognising familiar code signatures — spotting that a block of assembly is a printf implementation or a Linux syscall — rather than explaining what unnamed variables mean.[614]

## Limits and failure modes of language models

Language models answer well-trodden questions competently but cannot be asked to extend past the boundary of what is documented, because they have no knowledge beyond their training material.[693] Current systems do not originate ideas, and building genuine machine intelligence would first require defining and encompassing what real intelligence is, a task barely begun.[684] A practical way to calibrate how much to trust a model is to question it on the subject in which one has the deepest personal expertise, which exposes the limits of its answers.[704] Taking a confidently phrased answer on faith, without checking references, multiple sources and primary texts, is hazardous in domains such as signal grounding where established best practice governs the result.[704]

Training-data bias shows up directly in engineering answers. Asked to design a circuit, general-purpose models converge on the ESP32 roughly eight times out of ten, a bias that follows from how heavily that part appears in the online projects the models were trained on.[724]

Staleness is a related problem. Assistants that scrape the web propose deprecated Zephyr APIs, because the real-time operating system evolves faster than the scraped material and has introduced new constructs such as hardware models; students are shown this failure in the second week of one course so they are not led down an outdated path.[711] Gemini's web index was dated January 2025, an age that matters for fast-moving frameworks, and the practical outcome was abandoning language-model assistance for Zephyr work entirely.[711]

Fabrication is the blocking failure mode for control applications: the model invents events and states that never occurred and treats them as legitimate.[654] In a home automation stack, device control sits below a scheduling layer that handles priorities and external inputs, and any language-model layer belongs above that scheduler rather than in the control path.[654]

Media tooling shows similar limits. Tools that claim to cut long-form video into viral short-form clips produced no usable output across repeated trials, a zero percent hit rate; the clips are correctly formatted but lack the editorial quality that makes a short work.[668] Voice cloning trained on a speaker's own recordings, including a guided online session reading prescribed words, produced unusable results across three or four different services.[677] Image generators reconstruct a subject rather than reusing the supplied photographs, and results degrade badly unless the input is a pristine photograph of a single person; human faces remain the weakest case.[613]

## Defensible applications

Generated illustration has been used in place of commissioned artwork on the basis that the output carries no royalty obligation, although the legal position on such licensing remains contested.[613] A defensible use of a chat model in technical writing is breaking writer's block, taking its output as bullet points to research rather than as finished text.[614] Using generated data-gathering to assemble a corporate dependency map is similarly defensible, since the alternative is manually reading hundreds or a thousand separate articles to trace the connections.[717]

Component and product discovery, historically done through web search and before that the new-products pages at the back of trade magazines, is shifting toward querying a language model with a specification such as an op-amp with given parameters.[714] A purchase decision informed by model-supplied links was nonetheless settled by asking a known expert whose judgment could be trusted, illustrating that generated shortlists are a starting point rather than a source of truth.[714]

The work most exposed to language models is boilerplate text that nobody reads closely, such as legal contract language and filler marketing copy, where slightly worse output is still good enough for the purpose.[684] Large language models themselves are treated as a commodity layer, with the unsolved and valuable part being reasoning over context, such as deciding which item in a calendar or inbox actually matters.[668]

Labour-market effects are visible in specialist roles: prompt engineer positions were advertised at between 175,000 and 335,000 dollars a year, with the work amounting to an internal audit of a company's own model behaviour.[625]

## Infrastructure and power

Converting an existing data centre to inference and training workloads required an entire additional building section devoted to power, on roughly the same computing floor area, with new trenched feeders and external transformers installed to supply it.[724] The additions are dominated by cooling plant, power distribution and diesel generators rather than by extra server floor space, reflecting an order-of-magnitude rise in power density.[724]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 258 | An Interview with Bertrand Irrisou and Gerald Friedland of Audeme | https://theamphour.com/258-an-interview-with-bertrand-and-gerald-of-audeme/ | July 14, 2015 |
| 262 | Jobs For Weirdos | https://theamphour.com/262-jobs-for-weirdos/ | August 12, 2015 |
| 412 | 3 Cent Micros And 1000s of LEDs | https://theamphour.com/412-3-cent-micros-and-1000s-of-leds/ | October 21, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 470 | Just Add Salt | https://theamphour.com/470-just-add-salt/ | December 8, 2019 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 538 | Missle Man with Bruce Simson | https://theamphour.com/538-missle-man-with-bruce-simson/ | April 12, 2021 |
| 582 | The Same Wavelength | https://theamphour.com/582-the-same-wavelength/ | March 20, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 613 | It's a Keyzermas Miracle! | https://theamphour.com/613-its-a-keyzermas-miracle/ | December 18, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 618 | Refrigerators and Robots with Amitabh Shrivastava | https://theamphour.com/618-refrigerators-and-robots-with-amitabh-shrivastava/ | February 5, 2023 |
| 620 | Engineering Education with Dr Don Wilcher | https://theamphour.com/620-engineering-education-with-dr-don-wilcher/ | February 20, 2023 |
| 625 | Gremlins in the machine | https://theamphour.com/625-gremlins-in-the-machine/ | March 26, 2023 |
| 626 | Intelligent Routing with Sergiy Nesterenko | https://theamphour.com/626-intelligent-routing-with-sergiy-nesterenko/ | April 2, 2023 |
| 631 | A Noisy Rude Bus | https://theamphour.com/631-a-noisy-rude-bus/ | May 7, 2023 |
| 651 | Learning Computing with Jeff Geerling | https://theamphour.com/651-learning-computing-with-jeff-geerling/ | November 20, 2023 |
| 654 | Pseudo Code...Pseudo Good | https://theamphour.com/654-pseudo-code-pseudo-good/ | December 18, 2023 |
| 656 | Pneumatic Tubes, Straight To The Home | https://theamphour.com/656-pneumatic-tubes-straight-to-the-home/ | January 22, 2024 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 661 | Blogging Electronics with Pallav Aggarwal | https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/ | March 10, 2024 |
| 668 | 50.0000 Ohms | https://theamphour.com/668-50-0000-ohms/ | May 30, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
| 683 | Troubleshooting is the skill | https://theamphour.com/683-troubleshooting-is-the-skill/ | November 20, 2024 |
| 684 | Lee Felsenstein: The Computer Revolution & Counterculture | https://theamphour.com/684-lee-felsenstein-the-computer-revolution-counterculture/ |  |
| 685 | Data Provenance in the Home, Server, and Fab | https://theamphour.com/685-data-provenance-in-the-home-server-and-fab/ | December 23, 2024 |
| 693 | Small Scale Electronics Manufacturing with Colin O'Flynn | https://theamphour.com/693-small-scale-electronics-manufacturing-with-colin-oflynn/ | May 13, 2025 |
| 694 | Voltage, Vibes, and VOCs | https://theamphour.com/694-voltage-vibes-and-vocs/ | May 21, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
| 711 | Medical Electronics Education with Mark Palmeri | https://theamphour.com/711-medical-electronics-education-with-mark-palmeri/ | December 21, 2025 |
| 713 | Rubber Duck Incarnate | https://theamphour.com/713-rubber-duck-incarnate/ | January 25, 2026 |
| 714 | The Measurement Blues with Martin Rowe | https://theamphour.com/714-the-measurement-blues-with-martin-rowe/ | February 2, 2026 |
| 717 | Back on the road in '26 | https://theamphour.com/717-back-on-the-road-in-26/ | March 4, 2026 |
| 722 | AI Tooling with Matt Liberty and Luke Beno | https://theamphour.com/722-ai-tooling-with-matt-liberty-and-luke-beno/ | April 22, 2026 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
| 729 | The Terahertz Frontier with Greg Charvat of Teradar | https://theamphour.com/729-the-terahertz-frontier-greg-charvat-teradar/ | July 22, 2026 |
