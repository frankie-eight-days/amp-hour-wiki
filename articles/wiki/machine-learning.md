---
title: Machine Learning
concept: machine-learning
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

Machine learning is the practice of deriving a decision rule from labelled examples rather than specifying it by hand, and in electronics it is applied most often to classification of sensor and image data.[525][546] It inverts the classical signal-processing workflow: instead of an engineer searching the space of transforms for one whose output separates the cases of interest, the engineer supplies the desired output for a set of labelled examples and the tooling searches for the algorithm that produces it.[525] The approach suits problems whose answer is a category and whose input conditions are tightly controlled, and it fits poorly where a task demands repeatable numerical accuracy on every cycle.[344][407] For hardware engineers the work usually sits upstream of the model itself, in designing the sensing, collecting the data and packaging it for whatever consumes it.[428]

## Where learned models fit

Because the output of a classifier is a label rather than a measurement, classification tasks such as image tagging tolerate far coarser numerical precision than instrumentation work; an implementation that is only roughly in the ballpark still returns the correct category.[344] The same tolerance does not extend to guidance. Guiding a robot demands repeatability and accuracy on every cycle, while a learned classifier is characterised by a success rate, and hit rates that count as aspirational for machine learning are far below what a positioning task tolerates.[407]

Machine vision built on learned models performs well where the field of view is tightly controlled and the subject is presented identically every time, such as aligning a part on a printed circuit board viewed straight on, and degrades as the viewing angle and framing are allowed to vary.[407] One motivation for applying learning to robot arm control is narrower: to avoid deriving and solving the inverse kinematics of the arm explicitly.[344]

The set of ordinary embedded products that justify an on-board learned model is small, and most low-cost devices gain nothing from one.[428]

## Training data and labelling

Data collection for an embedded classifier is a physical procedure. The event is repeated on the order of a hundred times while the sensor records, and the resulting set of traces is labelled as that event.[546] Labelling this kind of data requires domain knowledge rather than data-science knowledge: an engineer who performs the physical event while recording the waveform knows when it happened and can mark the data accordingly, without interpreting the signal.[525]

In wireless sensor network research the hardware task and the learning task are separated in time. Purpose-built Bluetooth, WiFi or custom 2.4 GHz nodes are designed first to read and collect data during controlled experiments, and the learning is applied afterwards to the collected set.[557]

Input dimensionality is often reduced aggressively before training. Interactive demonstrations downsample a camera feed drastically before it reaches the model, dropping from a native 640 by 480 or higher frame to a grid of a few tens of pixels per side, which keeps the input small enough to train and run in real time.[296]

Reinforcement learning is normally staged from simple examples to complex ones. An agent dropped straight into a large maze wanders at random and never produces a run good enough for the algorithm to identify which behaviour was correct, so training starts on small mazes and grows them.[374]

## Adaptation and updates in deployed systems

A whole-home electricity monitor that disaggregates appliance loads ships with generic per-appliance models — a generalised refrigerator, a generalised washer — and then specialises those models against the individual appliances it observes once installed, because the current signature of a given unit differs from the class average.[371] Because the models keep changing, the product is built around frequent connected software updates: tailored models are refreshed regularly, and newly derived appliance-type models are pushed out to the whole installed fleet.[371]

Adaptation is sometimes deliberately bounded. Automotive active noise cancellation does not need to learn its environment from scratch, because the acoustic transfer function from noise source to the occupant's ears is largely stable in a given cabin; the system is pre-tuned to that rough transfer function and given only a limited adaptive range around it.[560] Such a system fails gracefully rather than re-converging when the condition changes: opening a window alters the transfer function beyond the range the system was allowed to adapt over, and cancellation performance simply falls off.[560]

Divergence from human behaviour can itself serve as the training signal. A reported method for validating driver-assistance software in the field runs the candidate algorithm alongside the live system, records what the human driver actually did, and treats each divergence between the algorithm's intended action and the driver's action as a training case uploaded for analysis.[524] A related proposal applies to flight control: an autopilot flown on anything other than the vendor's stock airframe has to have its control gains tuned by hand for that airframe, and an alternative is to fly the vehicle manually for a short period and let the autopilot infer the gain settings from that flight.[105]

## Relation to hand-written signal processing

The conventional way to detect an event in a sensor stream is to hand-build a threshold or a slope detector and iterate until it fits, which amounts to imposing a chosen mathematical form on a physical phenomenon and checking the result by trial and error.[525] Automated machine-learning tooling reverses that search direction, taking the labelled desired output as its starting point.[525]

Tooling of this kind is typically split across the network boundary. A cloud-hosted model-generation service takes labelled sensor data as its input and emits inference models sized to run on a resource-constrained microcontroller, so that the constrained target is only ever asked to perform inference.[525] Inference of this kind is targeted at ordinary Cortex-M4 class microcontrollers rather than dedicated accelerator hardware, which is what allows it to displace hand-written signal processing in existing sensor products.[546]

## Hardware and platform constraints

Running heavy inference on a battery-powered device is bounded by energy rather than by feasibility: the computation can be made to work, but the battery required to sustain it dominates the product.[428] Workloads dominated by large matrix multiplication cannot be served by a general-purpose core alone and require a dedicated accelerator block on the die, which is why machine-learning acceleration is treated as a core component of a modern custom-silicon platform rather than an option.[650]

At the single-board-computer scale, AI acceleration now sits alongside compute roughly equivalent to a good laptop of five to eight years earlier, which is enough to take in camera data, compress it more efficiently and stream it out from a device small enough to strap to the equipment being observed.[651] Compute is not the whole deployment problem, however. Edge machine-learning modules sold as development boards are marketed on their compute and leave deployment to the user; putting one into an industrial setting such as watching a robot arm requires an enclosure, thermal protection and the actual peripheral interfaces the installation needs, none of which the dev board provides.[608]

Simulation is used to characterise these targets before silicon is in hand. Running embedded firmware inside a simulator on a host removes the memory ceiling of the target part and of an external debug probe, so instrumentation and trace that the real device could never hold become possible.[519] Simulation of the target microcontroller is used on that basis to benchmark embedded machine-learning runtimes such as TensorFlow Lite, measuring how well inference code executes on small platforms without needing the physical silicon in the loop.[519]

## Inspection and manufacturing

Automated optical inspection has worked by taught comparison since well before the machine-learning label was applied to it: a camera images the finished board and software compares that image against reference examples an operator has taught the machine.[411] The image of electronics manufacturing as a fully automated line does not describe most factories. Manual assembly steps remain common, and those steps are typically verified by a second human performing visual inspection, which is the gap machine-vision inspection products target.[437]

## Other applications

A learned model trained on separate corpora of recorded instrument samples can represent the instruments in a shared space, which allows a synthesiser to interpolate continuously between two timbres rather than switching between fixed samples.[384]

Individuals can be identified from gait alone using non-imaging sensors: a worn accelerometer captures walking and movement patterns, and capacitive sensors installed under a carpet support the same identification from footfall, avoiding a camera in the space.[557]

Machine learning applied to MRI data conventionally registers each subject against a standard anatomical model, which averages across individuals; where the clinically interesting feature is an individual anatomical detail, that averaging can remove the very signal being sought.[448]

## Origins in embedded tooling

Early machine learning on small Arduino-class boards was enabled by a hardware pattern-matching engine present in an Intel embedded processor. The block was scheduled for removal as unused before an application was found for it, and TinyML work on that platform began in 2017.[726]

The software stack behind one embedded machine-learning toolchain has a related origin: it was the group inside Intel that supported the Curie IoT module from 2015, formed on the recognition that developing such applications without a data scientist required a software platform, and when Curie was cancelled the software outlived the silicon.[525]

## References

| Episode | Title | URL | Date |
| --- | --- | --- | --- |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 344 | Back Into The Swing Of Things | https://theamphour.com/344-back-into-the-swing-of-things/ |  |
| 371 | An Interview With Joe Bamberg | https://theamphour.com/371-an-interview-with-joe-bamberg/ | December 10, 2017 |
| 374 | An Interview with Claire (née 'Clifford') Wolf | https://theamphour.com/374-an-interview-with-claire-nee-clifford-wolf/ | January 7, 2018 |
| 384 | A++++++ Will Buy Again | https://theamphour.com/384-a-will-buy-again/ | March 18, 2018 |
| 407 | Gregory Charvat and Three New Companies | https://theamphour.com/407-gregory-charvat-and-three-new-companies/ | September 16, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 428 | Setting Fire To The Tracks | https://theamphour.com/428-setting-fire-to-the-tracks/ | February 3, 2019 |
| 437 | An Interview with Chrissy Meyer | https://theamphour.com/437-an-interview-with-chrissy-meyer/ | April 7, 2019 |
| 448 | An Interview with Jean Rintoul | https://theamphour.com/448-an-interview-with-jean-rintoul/ | June 23, 2019 |
| 519 | Simulating Embedded Hardware with Michael Gielda | https://theamphour.com/519-simulating-embedded-hardware-with-michael-gielda/ | November 29, 2020 |
| 524 | LEDs and EVs with Mike Harrison | https://theamphour.com/524-leds-and-evs-with-mike-harrison/ | January 3, 2021 |
| 525 | Open FPGA Toolchains and Machine Learning with Brian Faith of QuickLogic | https://theamphour.com/525-open-fpga-toolchains-and-machine-learning-with-brian-faith-of-quicklogic/ | January 10, 2021 |
| 546 | Thousands Of Dependencies | https://theamphour.com/546-thousands-of-dependencies/ | June 21, 2021 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ |  |
| 560 | High End Audio with Remco Stoutjesdijk | https://theamphour.com/the-amp-hour-560-high-end-audio-with-remco-stoutjesdijk/ | October 3, 2021 |
| 608 | Vapor Phase with Saber Kaygusuz | https://theamphour.com/608-vapor-phase-with-saber-kaygusuz/ | November 7, 2022 |
| 650 | Accessible ASICs with Andreas Olofsson | https://theamphour.com/650-accessible-asics-with-andreas-olofsson/ | November 12, 2023 |
| 651 | Learning Computing with Jeff Geerling | https://theamphour.com/651-learning-computing-with-jeff-geerling/ | November 20, 2023 |
| 726 | Arduino's Invisible Touch with Massimo Banzi | https://theamphour.com/the-amp-hour-726-arduinos-invisible-touch-with-massimo-banzi/ | June 17, 2026 |
