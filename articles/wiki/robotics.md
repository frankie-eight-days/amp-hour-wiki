---
title: Robotics
concept: robotics
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

Robotics is a cross-disciplinary engineering field spanning mechanical, electrical, and software work, concerned with machines that sense and act in the physical world.[183] It is better understood as an approach to developing products and a toolset for solving problems than as an industry in itself, which is why some problems call for robotic solutions and others clearly do not.[425] The modern expansion of robotics has been driven primarily by cheap processing power for control systems, together with improved materials and falling component and sensor costs, rather than by advances in motor or actuator technology.[246][241][495]

## History

Collections of research robots spanning the 1980s to the mid-2000s double as a survey of electronics construction technique: wire wrap, sockets with IDC backs jumpered in magnet wire, and point-to-point protoboard dominate the earlier machines, with printed circuit boards appearing only by the mid-2000s.[162] Early projects built on the BeagleBoard single-board computer clustered around robotics and machine vision, including autonomous flying vehicles that used a Kinect sensor with LibFreenect to build 3D maps and recognize faces.[59]

College programs began packaging robotics education as mechatronics, deliberately combining electronics coursework with mechanical engineering rather than teaching either discipline alone.[67] Japanese robotics research long emphasized humanoid demonstration robots that could walk, dance, and wave; after the Fukushima nuclear accident, none of those robots could enter a reactor to locate fuel rods, and the research emphasis shifted.[369]

The PR2 research robot, developed by Willow Garage, runs the open-source Robot Operating System (ROS), which allowed outside groups to buy the hardware and develop applications such as laundry folding on top of it.[195] At one point ROS required ARMv7, so single-board computers with older ARM cores could not run it, while boards moving to ARMv7 inherited the whole existing ARM software ecosystem.[235]

Amazon paid roughly $750 million for Kiva Systems, whose warehouse robots move whole shelves rather than pick individual items.[321] 3D Robotics effectively exited drone hardware and became a software company after Chinese manufacturers drove component and product prices down faster than it could compete.[406]

Affordable 3D printing and free CAD tools in the mid-2010s became a common entry path into robotics, because the ability to design and modify parts, rather than only print existing files, is what pulls people into building machines.[712]

## Enabling technologies

Advances in prosthetic arms and robotics have been attributed to the combination of cheap microprocessors and improved materials rather than to any single mechanical breakthrough.[241] The wave of consumer robot products was likewise driven by cheap processing power for control systems, not by any improvement in motor or actuator technology.[246] Powered exoskeletons are an old concept whose recent feasibility came from real-time processing for sensor feedback and motor control plus falling cost, not from lighter motors or dramatically better batteries.[285]

Stepper motors, their drivers, and the surrounding circuits became dramatically cheaper over roughly a decade, which changed what a student robotics project could attempt even though the underlying motor technology was unchanged.[601] Brushless motors deliver power densities that make legged robots practical: a two-kilowatt brushed DC motor is physically enormous, while the brushless equivalent is small for the same output.[416] Shape memory alloy actuators can be built to produce linear motion with high force and precision, offering an alternative to conventional linear actuation in mechatronic systems.[426]

### Cost dynamics

LiDAR was described as potentially half of a robot's bill-of-materials cost at one point, with an expected fall to roughly five percent within five years, following the same cost curve that Wi-Fi integration went through.[342] Component cost sensitivity is application-dependent: a $10 incremental bill-of-materials cost for a speech recognition module is negligible on a robotics project but prohibitive on a commodity appliance, and volumes in the millions cut that cost by about 30 percent.[258] Standardizing an ecosystem on a single connector and cable family concentrates volume on those parts, which is what drives unit cost down.[277] An investment thesis in applied robotics was built by tracking such falling component costs and asking which new solutions become possible in a one-to-five-year window when a technology cost change meets a market change.[495]

## Control and motion

In robot builds the mechanical hardware is the easy half: without control software the actuators are inert — "dumb actuators" without a mind to drive them — and generating human-like motion is an extremely hard control-systems problem.[116] Making an animatronic limb move convincingly rather than jerkily depends on motor accuracy and mechanical tolerances as much as on the control software.[292]

Robotics and CNC machining use similar hardware but differ in required precision: a robot only needs to reach a target within an acceptable envelope and can close the loop with vision, while CNC must control every aspect of the path precisely.[438] Tasks whose target geometry varies each time, such as tying a shoelace, cannot be programmed as a fixed path and require the robot to sense the workpiece before deciding how to move.[438] Robotics and machine tools also differ in expected development cycle time: robotics assumes fast iteration while machine tools do not, which is why the same interfacing approach produces different outcomes in each domain.[208]

An assistive exoskeleton is not commanded with coordinates or inverse kinematics; gyros and other sensors detect the motion the wearer's limb is beginning to make, and the actuators amplify it.[285] For his legged robots, James Bruton derived the kinematic model empirically: a springy tendon is wound up, a foot sensor detects ground contact, and the leg either complies or unwinds, so the model is computed from where the leg actually ends up.[416]

## Computing platforms and software

A Linux single-board computer used as a robot controller has a practical development advantage over a bare microcontroller: a monitor and keyboard can be attached to bring the robot up, after which the same board runs headless in the field.[97] A media-processing board can be repurposed as a robot controller by retrofitting motor controllers plus digital and analog I/O onto the existing design instead of starting a new platform from scratch; Bunnie Huang took this approach in adapting an existing board design for robotic use.[84]

Because ROS provides a common software layer, outside groups could buy PR2 hardware and develop applications on top of it.[195] Abstraction of that kind is not universally accepted: for his own device-testing robots, Jason Huggins deliberately avoided ROS because its abstraction layer obscured the stack he needed to understand end to end, from the browser issuing a command down to the motor executing it.[369] Off-the-shelf CNC stepper shields expose only a single global enable line, which blocks per-motor calibration routines and forces either a firmware workaround or a custom board — a limitation Huggins encountered in the same work.[369]

## Perception and positioning

Machine vision has been a central robotics workload since early single-board-computer projects, including autonomous flying vehicles that built 3D maps from Kinect data.[59] Huggins's robotic device-testing rig uses OpenCV against a video feed or camera to locate on-screen elements, convert them into targets, and then physically tap them.[369]

The core problem shared by machining and robotics is establishing where objects are in free space relative to an origin; Gregory Charvat's indoor positioning company addressed this by projecting a machine tool's coordinate frame out into 3D free space over a 10-meter radius of factory floor.[407] LiDAR has been a dominant sensing cost in mobile robots, though its share of bill-of-materials cost was expected to fall sharply.[342] Sensor systems for self-driving vehicles have been identified as a large near-term opportunity for electronics engineers, distinct from the automation of driving itself.[329]

## Industrial and logistics applications

Warehouse robots that move whole shelves in a mixed human-robot environment represent the deployed, revenue-generating end of practical robotics.[174] Even so, picking itself has stayed human: Kiva's robots move shelves rather than items, and human dexterity remains far better, especially for ad hoc situations where something goes wrong.[321] For the same reason, even a large electronics distributor still uses human packers walking to shelves rather than robots retrieving bins, because replicating human picking ability at the cost of a wage is very hard.[184]

In contract electronics assembly, surface-mount placement was heavily automated while reel loading and through-hole placement stayed manual, because robotics could not yet match human handling of those tactile steps.[121] A pick-and-place machine is itself a robot that needs per-component-type calibration and component libraries in addition to X-Y placement coordinates, so an unfamiliar part stalls the process.[411] Introducing a previously unseen component remains a manual step, because someone must look up the datasheet and determine the physical package size before the machine can place it.[411] Announced factory automation programs have targeted assembly and material handling rather than fine motor control tasks, so claims of wholesale worker replacement must be checked against which operations are actually being automated.[300]

Even as global labor costs rise, a low-paid human worker still outpaces an expensive robot in many electronics assembly scenarios, which limits how fast collaborative robots displace assembly labor.[291] The realistic near-term factory robot augments a worker rather than replacing them, taking over heavy lifting that previously required extra co-workers while the human retains decisions about stopping and moving.[469] The economically defensible robotics case is automating the simple repetitive portion of skilled work — easy welds, for example — so that scarce master craftspeople are freed for the complex operations.[495] Tasks that look simple can be hard robotics problems: automating a restaurant dish room requires both identifying unsorted mixed items and adapting the grasp to each object type, gripping a spoon differently from a plate.[495]

For her KnitYak knitwear manufacturing business, Fabienne Serrière chose to automate garment production specifically to avoid depending on low-wage overseas labor, treating robotics as an ethical sourcing decision rather than only a cost one.[257]

### Commercial considerations

Supplier rating systems on manufacturing marketplaces are structurally unreliable, because a buyer who had a good project leaves five stars while a buyer who had a bad one silently walks away rather than damage a relationship they may need again.[405] An early-stage hardware investor's first working session with a company covers market definition, what products already exist and how they work, which technologies could be the differentiator, and what technical moat prevents a copycat six months later.[437]

## Design constraints and integration

A fielded robot must simultaneously interact with people, move through the real world, carry its own power, be safe, be small enough to maneuver, and be big enough to be useful — a set of mutually incompatible constraints.[425] How vertically integrated a robot must be depends on its size, weight, and power budget: tight SWaP constraints force embedded, integrated designs that make off-the-shelf components and outside firms harder to bring in.[614]

Chris Osterwood, who founded a robotics component company to fill the gap between building every subsystem in-house and buying off-the-shelf parts designed for other markets, frames the buy-versus-build calculation in engineer-months: a component that replaces four months of engineering and is guaranteed to work the first time is worth buying so engineers can attack domain-specific problems instead.[614][425] For robot joints, Bruton adopted the existing ODrive brushless controller rather than designing his own, judging it the one option aimed at robotics that handles accurate encoder-based positioning.[416] Highly productive independent builders standardize on a small reusable toolbox of parts and techniques and apply it project after project, changing platforms rarely and deliberately.[460]

For her augmented-reality hardware, Jeri Ellsworth considered splitting out the position tracker and leaving its raw ASCII position output exposed so third parties could build robotics on top of it, noting that hackability was the single most requested feature from makers.[147]

## Education and skill development

The mechatronics packaging of robotics education combines electronics and mechanical coursework in a single program.[67] FIRST Lego League competitions include a live-coding element in which teams must modify their robot on the spot for changes they were not told about in advance.[167] Choosing a hobby robot project for career value rather than utility changes the work: it justifies spending time on matrix math, kinematics, and drive mechanisms that can be explained in an interview, whereas a purely functional home project would not.[373] Access to 3D printing and free CAD in the mid-2010s provided a common entry point for students beginning to build robots.[712]

## Limitations

Human operators remain necessary in otherwise autonomous systems precisely because robots handle unexpected situations poorly.[334] Building good robots remains hard enough that even state-of-the-art humanoid platforms fall over, a useful corrective to demonstration videos.[353] Companies operating at the experimental edge of robotics accept that their platforms will be unstable; Chris Anderson's position at 3D Robotics was that buyers who want stability should choose a consumer product and wait, while the company's actual customers demand the newest sensors and computing platforms.[105]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 59 | An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics | https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/ | |
| 67 | BeagleBoard successors, CAD & Robots - Haussmannized Halloween Hypostrophe | https://theamphour.com/the-amp-hour-67-haussmannized-halloween-hypostrophe/ | |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 97 | An Interview with Eben Upton - Morbus Moilsome MakerFaire | https://theamphour.com/the-amp-hour-97-morbus-moilsome-makerfaire/ | |
| 105 | An Interview with Chris Anderson - Deambulatory Daedal Drones | https://theamphour.com/the-amp-hour-105-deambulatory-daedal-drones/ | July 23, 2012 |
| 116 | Distribution, Wozniak & Robots - Early Eight-bit Endgame | https://theamphour.com/the-amp-hour-116-early-eight-bit-endgame/ | October 7, 2012 |
| 121 | An Interview with Zach Hoeken Smith - Creative China Commorant | https://theamphour.com/the-amp-hour-121-creative-china-commorant/ | November 11, 2012 |
| 147 | An interview with Jeri Ellsworth - Absorptive Augmented Actuality | https://theamphour.com/the-amp-hour-147-absorptive-augmented-actuality/ | May 27, 2013 |
| 162 | Discussing The Open Hardware Summit With MightyOhm - Ostrobogulous Openness Occasion | https://theamphour.com/the-amp-hour-162-ostrobogulous-openness-occasion/ | September 8, 2013 |
| 167 | An Interview with Adam Wolf - Brick & Board Biuners | https://theamphour.com/167-an-interview-with-adam-wolf-brick-board-biuners/ | October 14, 2013 |
| 174 | Motors And Upgrading Sinclairs - Adapting Apraxiated Automobiles | https://theamphour.com/174-motors-and-upgrading-sinclairs/ | December 2, 2013 |
| 183 | An Interview with Scott Driscoll - Impacable Interdisciplinary Inventor | https://theamphour.com/183-an-interview-with-scott-driscoll-impaccable-interdisciplinary-inventor/ | February 3, 2014 |
| 184 | Chris Becomes Self Employed - Quixotic Quitting Quaere | https://theamphour.com/184-chris-becomes-self-employed-quixotic-quitting-quaere/ | February 10, 2014 |
| 195 | Guns and Mobile Labs - Nuanced Nomadic Non-essentials | https://theamphour.com/195-guns-and-mobile-labs-nuanced-nomadic-non-essentials/ | April 21, 2014 |
| 208 | An Interview With Nadya Peek - Gallant Gcode Gerontology | https://theamphour.com/208-an-interview-with-nadya-peek-gallant-gcode-gerontology/ | July 21, 2014 |
| 235 | An Interview with Matt Richardson - Raspberry Risorgimento Regent | https://theamphour.com/235-an-interview-with-matt-richardson-raspberry-risorgimento-regent/ | February 3, 2015 |
| 241 | An Interview With Chuck Peddle - Charismatic Chipmaking Coryphaeus | https://theamphour.com/241-an-interview-with-chuck-peddle-charismatic-chipmaking-coryphaeus/ | March 18, 2015 |
| 246 | Robots are coming - Ominous Operational Overhaul | https://theamphour.com/246-robots-are-coming-ominous-operational-overhaul/ | April 21, 2015 |
| 257 | An Interview with Fabienne Serrière of KnitYak | https://theamphour.com/257-an-interview-with-fabienne-serriere-of-knityak/ | July 8, 2015 |
| 258 | An Interview with Bertrand Irrisou and Gerald Friedland of Audeme | https://theamphour.com/258-an-interview-with-bertrand-and-gerald-of-audeme/ | July 14, 2015 |
| 277 | Interconnectorama | https://theamphour.com/277-interconnectorama/ | December 9, 2015 |
| 285 | Something's Serially Wrong Here | https://theamphour.com/285-somethings-serially-wrong-here/ | February 3, 2016 |
| 291 | Artificially Intelligent Party Platform | https://theamphour.com/291-artificially-intelligent-party-platform/ | March 16, 2016 |
| 292 | An Interview with Timothy Lamb | https://theamphour.com/292-an-interview-with-timothy-lamb/ | March 23, 2016 |
| 300 | Three Hundred Down, Three Hundred To Go | https://theamphour.com/300-three-hundred-down-three-hundred-to-go/ | May 25, 2016 |
| 321 | Monster Scale Production | https://theamphour.com/321-monster-scale-production/ | October 27, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ | |
| 334 | An Interview with Gerry Roston | https://theamphour.com/334-an-interview-with-gerry-roston/ | February 1, 2017 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 353 | IoT Degree | https://theamphour.com/353-iot-degree/ | July 23, 2017 |
| 369 | An Interview with Jason Huggins | https://theamphour.com/369-an-interview-with-jason-huggins/ | November 26, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 405 | An Interview with Spencer Wright | https://theamphour.com/405-an-interview-with-spencer-wright/ | September 3, 2018 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 407 | Gregory Charvat and Three New Companies | https://theamphour.com/407-gregory-charvat-and-three-new-companies/ | September 16, 2018 |
| 411 | An Interview with Chris Denney | https://theamphour.com/411-an-interview-with-chris-denney/ | October 14, 2018 |
| 416 | An Interview with James Bruton | https://theamphour.com/416-an-interview-with-james-bruton/ | November 18, 2018 |
| 425 | An Interview with Chris Osterwood | https://theamphour.com/425-an-interview-with-chris-osterwood/ | January 13, 2019 |
| 426 | An Interview with Dean Pick | https://theamphour.com/426-an-interview-with-dean-pick/ | January 20, 2019 |
| 437 | An Interview with Chrissy Meyer | https://theamphour.com/437-an-interview-with-chrissy-meyer/ | April 7, 2019 |
| 438 | An Interview with Bart Dring | https://theamphour.com/438-an-interview-with-bart-dring/ | April 14, 2019 |
| 460 | Rubber Ducking | https://theamphour.com/460-rubber-ducking/ | September 29, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 495 | An Interview with Eric Klein | https://theamphour.com/495-an-interview-with-eric-klein/ | June 7, 2020 |
| 601 | Rebuilding Projects with Dave Young | https://theamphour.com/601-rebuilding-projects-with-dave-young/ | August 28, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 712 | Robots Everywhere with Aaed Musa | https://theamphour.com/712-robots-everywhere-with-aaed-musa/ | January 19, 2025 |
