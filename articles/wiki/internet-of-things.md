---
title: Internet Of Things
concept: internet-of-things
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

The **Internet of Things** (IoT) is the practice of connecting physical devices—sensors, actuators, appliances and industrial equipment—to data networks so that they can report state and be controlled remotely. The category rests on two underlying trends: local computation approaching zero cost, and connectivity that is effectively ubiquitous through WiFi in buildings, Bluetooth carried on people, and cellular coverage between them.[327] The dominant architecture is not a direct connection of every sensor to the internet, but a local sensor network reporting to a gateway device that handles the internet-facing communication.[232] The engineering and commercial substance of the field lies in power budgets, fleet maintenance, service longevity and security rather than in the radio link itself, and the durable applications are those that remove technician visits, prevent expensive failures or tie directly to money saved.[495][272][179]

## Architecture

Putting every sensor directly on the internet is the wrong architecture for most deployments. The workable pattern is a local sensor network reporting to a gateway device that handles the internet-facing communication, a structure used, for example, in a wine-grape vineyard installation.[232] A gateway with a cellular backhaul talking to many low-power sensors needs a mesh topology rather than point-to-point links: a Bluetooth radio reaches one device at a time, whereas a mesh such as Thread over 802.15.4 at 2.4 GHz extends across a whole set of sensors.[587]

Processing that can be done locally should be done locally. Sending data to a cloud service, processing it there and returning the result adds layers without benefit, and a lost connection then costs the local function entirely.[272] For safety-critical local functions the principle is stronger: a house alarm should be built standalone rather than routed through a central server, because the network dependency adds a failure mode the standalone product does not have.[561]

On a bandwidth-starved link the useful technique is to encode composite state rather than transmit raw data. A single byte carries 255 possible encodings, which is enough to report that a person entered a zone and which items of safety equipment they were wearing, and fits within a LoRa link with no internet connection at all.[517]

## Addressing and protocols

Addressing is a scaling constraint: the number of directly addressable devices under IPv4 is limited, so wide deployment of connected devices depends on IPv6 uptake.[213]

MQTT is a lightweight publish-and-subscribe protocol widely used for machines to publish information, chosen for connected devices because of its small memory footprint.[200] Cellular carriers advise against building telemetry on SMS and want device traffic carried as internet data, so the resulting practice is to get on the internet by whatever modality is available—WiFi, Ethernet or a cell modem—and publish MQTT, which also keeps the service cost down.[429]

CoAP rebuilds the concepts of HTTP—visiting an endpoint, talking to a server—for constrained devices, optimising for low power, low bandwidth and ease of programming. HTTP was designed for browsers talking to web servers and assumes RAM and MTU sizes that constrained devices do not have; CoAP, formalised around 2014, keeps the HTTP model while sizing its packets for cellular links and 802.15.4, and is used inside cellular networks for provisioning and roaming.[526]

Thread is a self-healing wireless mesh built on 802.15.4 at 2.4 GHz in which every device can talk to every other, optimised for power and aiming at wired-network reliability. It was deliberately specified to reuse radios already available off the shelf for Zigbee, and an open implementation, OpenThread, lets any hardware developer build on it.[526]

## Standards

A single standard covering every connected application is the wrong target. Standards scoped to one application—temperature sensing, or home automation alone—are achievable, and a de facto standard can emerge once a few visible players adopt it. Radio is the hard part of standardisation because transmission is regulated.[245] In practice, competing short-range radio standards proliferated without convergence, so a home gateway intended to bridge devices has to carry every radio; an open plug-in interface is what makes such a hub useful rather than another closed island.[172] In the energy sector, communication between distributed energy hardware and utilities is standardised by SunSpec, developed jointly with inverter manufacturers, utilities and security specialists.[583]

## Provisioning and fleet management

A device with no user interface cannot be handed network credentials directly. The common solution is for the device to host its own WiFi access point on first power-up; the installer joins that network, supplies the router credentials, and the device then leaves its own network and joins the house one.[182] Credential changes are a hidden lifetime cost: when a homeowner replaces a router the device silently stops reporting, and the loss may not be noticed for months. Re-provisioning that requires an installer visit with a professional commissioning app consumes half a day that would otherwise have gone to installing a new system.[487]

The firmware image flashed into a product at manufacture is typically three to four months old by the time a user powers it on, so the day-zero requirement is that the gold master boots, reaches the backend and updates itself to current firmware—and that this path is solid before anything else.[363] Fleet management is a distinct product requirement: a console reporting how many units are deployed, how many are active and which firmware revision each carries, with migrations managed rather than pushed blind.[310] Distribution costs scale with the fleet: pushing an update to ten thousand devices is unremarkable, but the same operation against a million or a billion devices is a different engineering problem, with security layers on top.[271] A hosted firmware distribution service can let a device call home on reset and fetch a newer build, with the device deciding whether it needs the update, which removes the need for a remote collaborator to hold the whole development environment.[435]

The corporate IT organisation that inherits a deployed device cares about three things the device engineering does not address: setting up and installing it, managing and decommissioning it, and integrating its data into a business process such as building management or customer records.[526]

## Cloud services and service longevity

A connected product carries a recurring server cost against what is usually a single payment from the customer, so a product plan that does not define an end of service will lose money over the product's life.[272] Service longevity, not hardware life, sets the usable life of a cloud-dependent product: a temperature logger tied to a large hosted service stopped working within about two years when the company was sold, went out of business or changed its protocol.[272] Any product whose function depends on a service on the internet should be assumed to outlive that service; light bulbs that need a remote service to switch will eventually stop switching. Self-hosted or clonable server images are the mitigation, and they are rare.[296]

Back-end reliability is the hardest part of a connected product, and the failure is silent: hosted services go down without the vendor knowing immediately, and the customer, who has no visibility of the layers, reports the device as broken.[272] A connected-hardware company that runs out of money still carries an obligation to its installed base: one such company stopped product development and went quiet specifically to preserve enough money to keep its cloud services running.[249] The end of a vendor's service is not always the end of the hardware, however: devices bricked when a back end goes offline can sometimes be recovered by hardware attack, and some vendors are content for that to happen to products they no longer wish to support.[552]

Buying into a vendor ecosystem trades control for not having to write a mesh stack, an operating system and a firmware loader; the price is that the vendor sets the schedule, and features such as network management can be discontinued under the buyer.[477] Local control is an alternative to the cloud-dependent model: a home automation controller run on a single-board computer keeps automation working without a subscription or handing data to a provider, and a declarative firmware tool lets a device be described—this board, a switch on these pins—instead of written in C with API calls.[651]

On a commercial IoT back end, the device authenticates itself with a certificate before it is allowed to publish; it then writes to a verified MQTT endpoint at a web address that is reachable but not open.[432] The platform model splits an application in two: server-side code the developer writes that runs in the vendor's cloud, and device-side code checking in over WiFi, with handlers passing events between them.[271]

## Hardware and silicon

The enabling component of the category is the integrated radio system-on-chip: an ARM core, SRAM, baseband, encoding and radio circuitry on one small, low-cost part that a sensor board can be built around, drawing single-digit milliamps in receive and transmit.[152]

The ESP8266 was not designed as an IoT part. Espressif built WiFi silicon for cheap Chinese tablets, whose makers used a WiFi module because carrying 2.4 GHz signals on a cheap PCB is difficult; integrating the radio with auto-calibration so it tolerates a poor board eliminated the module and its roughly 50 cents of cost. The ESP8266 was a variant of that tablet WiFi chip given the ability to run its own program from external flash, with the connected-device market added almost as an afterthought—which is why it has very few peripherals and only one ADC channel. The ESP32 reversed the priority and was designed for connected devices first.[359] The ESP32 pairs two 240 MHz 32-bit processors running FreeRTOS with Bluetooth classic, Bluetooth Low Energy and WiFi including access-point and scanning modes, on a single low-cost part.[330]

For cellular, a module combining LTE-M and NB-IoT with GPS in a package around 20 by 10 millimetres listed at roughly fifteen dollars, which put low-power cellular within reach of small designs without being commodity-priced.[432] A cellular modem on a board, however, is only one third of the problem: the design also needs a carrier contract, the translation from modem to server, and the server infrastructure behind it. Those three pieces—hardware, connectivity and software services—are separable, and a design can take any one of them from a vendor.[373] A SIM that can attach to many providers and towers rather than one carrier's network lets a device built by a small team be deployed wherever there is coverage without negotiating separate carrier agreements.[358]

A wireless sensor node designed for retrofit is shaped by the installation: small enough for light switches and confined spaces yet breadboard friendly, and wireless because an existing house cannot practically be rewired.[398]

## Firmware development

Adding networking is the point at which a firmware design moves up the stack: a bare-metal build against a vendor SDK stops being the right approach once the device has to talk to the internet.[548] Connectivity drags in threading, encryption and queuing, and writing that stack was previously only affordable for a large company that could staff a team per subsystem. A maintained real-time operating system such as Zephyr or FreeRTOS moves that work off a small team, at the cost of an initial steep climb.[622] Zephyr's network stack can be compiled and run on a PC, so protocol code can be exercised and abused off-target with a reasonable expectation that it behaves the same on the device; Nordic's cellular library uses the same network calls, which extends the technique to cellular work.[511]

A vendor's reference solution is a head start only while the design stays on the exact supported part; moving to a neighbouring device in the same family puts the team back into integration work with none of the advantage. The related trap is a proof of concept approved on a development kit, after which a cost or memory requirement forces a different part and months of schedule.[370] A connected product is hard to ship even for a company that already has electrical, mechanical, embedded and cloud engineers on staff; a couple of years to get such a product out of the door is normal, before security is considered.[526]

## Power

Battery replacement scales with fleet size and becomes the dominant field cost: a thousand deployed devices whose batteries last a year means replacing about three batteries every day, which is a different proposition from a phone that returns to a charging stand each night.[527] A two-year battery life is a common target for wireless connected devices, and the architectural question that precedes it is whether the device needs to be battery powered at all—mains power removes the battery as a reliability variable.[704] Battery life in a connected device is set by the wake, connect, transmit and sleep cycle rather than by processor efficiency, so that path is what a low-power design optimises.[359]

## Wide-area and satellite connectivity

Community long-range radio networks route a node's readings through a gateway that authenticates it onto the network before the data reaches a server; the low duty-cycle radios draw far less than 3G or GSM, so solar-powered nodes distributed across a country are practical at a per-node cost around fifteen dollars.[380]

Low Earth orbit changes what satellite connectivity can serve: at a small fraction of the roughly 36,000 kilometre altitude of broadcast satellites, a spacecraft circles fast enough that a single satellite passes over every part of the Earth at least once a day, giving worldwide reach at the cost of intermittent rather than real-time service. The applications that fit this are those without terrestrial coverage and without a latency requirement: logistics tracking of containers and rail cars, and agriculture—soil moisture and yield management—on farms whose scale defeats local infrastructure.[427] A high-bandwidth satellite internet constellation is not a substitute for satellite sensor connectivity: its ground segment is a phased-array terminal sized for internet service, not something to put on a stake in a field to report humidity.[518] Constellations for low-rate device connectivity became possible only when launch costs and small, capable spacecraft made deploying dozens of satellites affordable; the same economics could not have supported the service under earlier launch pricing.[679]

## Security

Embedded products historically relied on obscurity or on simply having no external interface; adding a WiFi or Bluetooth module and an IP address removes that protection entirely and makes the device reachable from anywhere in the world.[239] The attack surface of a connected product is not only the device: once many devices share a platform, the platform is the target, and compromising it reaches every device behind it.[211]

Defence is asymmetric—a single hole compromises a system—and connected devices add classes of attack that are not about the network: exploiting one radio protocol to reach another on a device carrying both, glitching a microcontroller to dump flash and recover keys, and side-channel attacks that recover a key from the sound or power draw of the machine performing the operation.[308] Putting an account-bearing interface on an appliance imports the account's risk into the appliance: a refrigerator with a screen that needed the owner's credentials to reach a calendar and send mail became a route to extracting those credentials.[308] Consumer connected products are routinely found storing private keys in flash, where they can be extracted from the device.[698]

Certification blocks the security update cycle in regulated products: where the software and the full stack are certified together, firmware cannot be updated without recertification. The recommended baseline is a locked-down bootloader with proper cryptography so malicious updates cannot be pushed, followed by regular, tested updates.[318] Vendors get the disclosure behaviour their process earns: if reporting a vulnerability means a flight, an NDA and no compensation while a grey market pays cash, researchers will take the cash, and a funded, easy bug-bounty path changes that calculus.[318]

Abandoned connected products create an indefinite patching liability, because devices that never receive another update stay deployed and reachable long after the vendor stops maintaining them.[364] Permanently embedding networked electronics into walls and ceiling fixtures is both a fire hazard and a long-lived attack surface, since the hardware outlasts anyone's willingness to maintain its software.[539]

## Economics and business models

Hardware by itself is a poor venture business at twenty to thirty points of gross margin, which is why hardware startups were historically underfunded; what changed the assessment was the redefinition of hardware as the mechanism for delivering software into a user's life away from a screen.[402] Connected consumer hardware is difficult to sustain on hardware margin alone: a thermostat retailing at 250 dollars returned only about 60 dollars to the company. Shifting the recovery to back-end services lowers the hardware price but makes the customer's product dependent on the vendor continuing to operate.[324] In a connected-device company the durable business is in the software and the platform rather than in the hardware itself.[202] The commercial value of connecting equipment is the maintained relationship with the customer after the box ships—continuing feedback about whether the thing is working—which survives even multi-tier distribution chains that otherwise sever the vendor from the user.[603]

The easiest connected-device sale is one denominated in money saved or made, and it supports a higher price than a proposition framed as convenience or novelty.[511] Deployments whose payback is directly tied to money already being lost—municipal parking, for instance—sell far more readily than ones offering a twenty-year payback period with an uncertain return.[179] The value case that holds up is preventing an expensive mistake rather than adding a feature: detecting a water leak in a house before it becomes damage pays for the instrumentation.[272]

A connected-device startup typically carries no science risk—the modules exist and are assembled—which allows very fast iteration, in contrast with a company that must solve an unsolved physical problem before it has a product at all.[260] The common failure mode is fitting a radio because it is possible rather than establishing the value first.[327]

## Applications

The industrial proposition is access to a system that is hard to reach or far away: a sensor on a tower reporting back removes the need to climb it in a snowstorm to collect data or troubleshoot.[385] The value of instrumenting equipment in the field is removing the technician trip to push a button or take a reading, which is why the industrial sector adopted connectivity ahead of the consumer one.[495] A typical industrial deployment puts intelligent wireless sensor nodes on manufacturing equipment, extracts information from them and watches for changes suggesting a current or developing fault, alerting plant personnel to act before the equipment causes downtime.[334] Large industrial facilities are a genuine big-data case—five hundred to a thousand nodes recording data continuously—and the useful application is predictive maintenance rather than firefighting after a failure; the obstacle is that the pattern-recognition analytics are tedious and time consuming to run.[426] Trend data from deployed sensors supports statistical process control: watching a monitored quantity over time shows when a process has gone out of control, the same discipline already used inside manufacturing.[355] Searching for a single consumer application that sells millions of units is the wrong search; the applications that work are niche and industrial, where a specific process can be optimised.[355]

In agriculture, market segmentation for remote monitoring is middle-out: large growers will not trust tens of millions of dollars of crop to a 300-dollar irrigation controller driven by a phone app and often already run proprietary systems, while the smallest operators live on the property and do not need remote visibility; the demand is from the operator who has another job and cannot be on site all day.[429] Retrofitting connectivity onto electromechanical equipment is illustrated by an irrigation system modernised with battery-powered smart sprinklers configured over Bluetooth Low Energy from a phone, plus WiFi-to-BLE and cellular-to-BLE gateways so the schedule could also be driven from the cloud; the gateways themselves had to be offered in a battery-powered variant because a garden pole has no mains.[635]

Distributed air-quality measurement has been built on low-cost metal-oxide semiconductor sensors rather than the instrumentation used at government monitoring sites, with the data pooled globally so it could be analysed together.[250] Whether laboratory equipment gets instrumented is decided by the lab, not by the engineering: biology labs freeze a protocol and the equipment it was validated on for years, because a failed experiment costs thousands of dollars in reagents and weeks of time, so the barrier is getting the first lab to accept a new instrument and publish with it.[336]

## Interface and automation design

What the operator wants from a monitoring product is a state, not a plot: a platform that opens on a graph has misread the user, who wants to know whether the thing is in trouble right now.[511] On his fermentation-monitoring product, Eli Hughes's team deliberately reduced the display to a tank that is either bubbling or not, so a customer checking a phone from a fishing boat gets the answer immediately, with the acoustic sensing and embedded detail available only to whoever wants it.[511]

Unlimited configurability is a liability rather than a feature: every additional adjustable parameter raises the chance the user ends up with a configuration they are unhappy with, which is why an on-off control often beats a programmable one.[114] Rule engines that pipe one event straight to one action are too simple for real automation: turning on lights when motion is detected at night requires the rule to carry conditions and durations—whether it is night, how long the lights stay on—and a service built on one-to-one piping cannot express that.[189] For lighting itself, distributing 24 volts DC around an installation from a modular, power-factor-corrected supply would make dimming straightforward by pulse modulation, whereas traditional phase-angle dimmers are incompatible with modern electronic loads and produce spiky, flickering results.[539]

## History

Remote meter reading predates the term and the standards: a utility-meter product used plain radio to relay readings to access points before cellular coverage existed, an architecture since re-implemented with standardised parts and wider availability.[238] Home automation over house wiring existed long before wireless: the X10 system, developed by BSR and later carried by RadioShack, was supplanted by radio-based systems such as Z-Wave and Zigbee, though installations remain in service.[424] The ESP8266, later a defining IoT part, originated as WiFi silicon for inexpensive tablets, with connected-device capability added as a secondary consideration before the ESP32 reversed the design priority.[359] A crowdfunding campaign for a connected light bulb was deliberately ended early after raising about one and a half million dollars in five days, because the team had a prototype and no manufacturing plan and did not want to owe delivery to a still larger backer base.[382] Intel withdrew from the connected-device development board market, discontinuing the Joule, Galileo and Edison lines.[351]

## References

| Episode | Title | URL | Date |
|---------|-------|-----|------|
| 114 | Kickstarter, Manufacturing, Open Hardware - Judging Jurisdictional Junctures | https://theamphour.com/the-amp-hour-114-judging-jurisdictional-junctures/ | September 23, 2012 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 172 | CAD courses and cross platform creation - Printing Propaedeutic Patterns | https://theamphour.com/172-cad-courses-and-cross-platform-creation-printing-propaedeutic-patterns/ | November 19, 2013 |
| 179 | Greg Charvat Returns With A Book! - Laboratory Literature Laureate | https://theamphour.com/179-greg-charvat-returns-with-a-book-laboratory-literature-laureate/ | January 6, 2014 |
| 182 | Manufacturing By Wire And Skipping Testing - Calefacient Cuculine Cash | https://theamphour.com/182-manufacturing-by-wire-and-skipping-testing-calefacient-cuculine-cash/ | January 27, 2014 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 200 | SolidCon and Traveling Tech - Joined Junk Jocularity | https://theamphour.com/200-solidcon-and-traveling-tech-joined-junk-jocularity/ | May 26, 2014 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 213 | Travel Recaps and Altium Announcements - Artisinal Aussie Assemblage | https://theamphour.com/213-travel-recaps-and-altium-announcements-artisinal-aussie-assemblage/ | |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ | |
| 238 | Old Books, New Tricks - Iterant Inscription Irrationality | https://theamphour.com/238-old-books-new-tricks-iterant-inscription-irrationality/ | February 25, 2015 |
| 239 | An Interview with Colin O'Flynn - Aspirated Adamantine Attacks | https://theamphour.com/239-an-interview-with-colin-oflynn-aspirated-adamantine-attacks/ | March 3, 2015 |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 249 | Wearables Might Have Limited Fashion Options - Lachrymogenic Lane Language | https://theamphour.com/249-wearables-might-have-limited-fashion-options-lachrymogenic-lane-language/ | May 12, 2015 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20, 2015 |
| 260 | An interview with Ariel Briner of Cartesian Co | https://theamphour.com/260-an-interview-with-ariel-briner-of-cartesian-co/ | July 28, 2015 |
| 271 | Amazon Moves In, Dave Says Run | https://theamphour.com/271-amazon-moves-in-dave-says-run/ | October 14, 2015 |
| 272 | An Interview With Luke Beno of Analog.io | https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/ | October 21, 2015 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 310 | Mergers and Acquiescence | https://theamphour.com/310-mergers-and-acquiescence/ | August 3, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 324 | Mapping Out Nerdery | https://theamphour.com/324-mapping-out-nerdery/ | November 23, 2016 |
| 327 | An Interview with Avidan Ross | https://theamphour.com/327-an-interview-with-avidan-ross/ | December 14, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 334 | An Interview with Gerry Roston | https://theamphour.com/334-an-interview-with-gerry-roston/ | February 1, 2017 |
| 336 | An Interview with Bunnie Huang (2nd) | https://theamphour.com/the-amp-hour-336-an-interview-with-bunnie-huang-2nd/ | |
| 351 | The Automation Amish | https://theamphour.com/351-the-automation-amish/ | July 10, 2017 |
| 355 | The Internet of Septage (with Akiba) | https://theamphour.com/355-the-internet-of-septage-with-akiba/ | August 13, 2017 |
| 358 | Mergers and People Acquisitions | https://theamphour.com/358-mergers-and-people-acquisitions/ | September 4, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 373 | Pedantic or Andrantic | https://theamphour.com/373-pedantic-or-andrantic/ | January 2, 2018 |
| 380 | Just Terrestrial and Space Things | https://theamphour.com/380-just-terrestrial-and-space-things/ | February 18, 2018 |
| 382 | The Toggle Boggle | https://theamphour.com/382-the-toggle-boggle/ | March 4, 2018 |
| 385 | An Interview with John Davis | https://theamphour.com/385-an-interview-with-john-davis/ | March 25, 2018 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 402 | An Interview with Ben Einstein | https://theamphour.com/402-an-interview-with-ben-einstein/ | August 6, 2018 |
| 424 | An Interview with Julia Truchsess | https://theamphour.com/424-an-interview-with-julia-truchsess/ | January 6, 2019 |
| 426 | An Interview with Dean Pick | https://theamphour.com/426-an-interview-with-dean-pick/ | January 20, 2019 |
| 427 | An Interview with Maarten Engelen | https://theamphour.com/427-an-interview-with-maarten-engelen/ | January 27, 2019 |
| 429 | An Interview with Charles Alexanian | https://theamphour.com/429-an-interview-with-charles-alexanian/ | February 10, 2019 |
| 432 | Check The Dummy Box | https://theamphour.com/432-check-the-dummy-box/ | March 3, 2019 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 495 | An Interview with Eric Klein | https://theamphour.com/495-an-interview-with-eric-klein/ | June 7, 2020 |
| 511 | Brewing Electronics with Eli Hughes | https://theamphour.com/511-brewing-electronics-with-eli-hughes/ | October 4, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 526 | Why IoT Is Difficult with Jonathan Beri | https://theamphour.com/526-why-iot-is-difficult-with-jonathan-beri/ | January 18, 2021 |
| 527 | Measuring Current with Matt Liberty | https://theamphour.com/527-measuring-current-with-matt-liberty/ | January 24, 2021 |
| 539 | The King of Trash with Big Clive | https://theamphour.com/the-amp-hour-539-the-king-of-trash-with-big-clive/ | April 26, 2021 |
| 548 | The Last Line of Defense | https://theamphour.com/548-the-last-line-of-defense/ | July 5, 2021 |
| 552 | Shouting at chips with Colin O'Flynn | https://theamphour.com/552-shouting-at-chips-with-colin-oflynn/ | August 1, 2021 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 583 | The Smart Grid with Paul Zawada | https://theamphour.com/583-the-smart-grid-with-paul-zawada/ | March 27, 2022 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 603 | An Interview with Ray Ozzie (Blues Wireless) | https://theamphour.com/603-an-interview-with-ray-ozzie-blues-wireless/ | September 25, 2022 |
| 622 | Building Firmware and Hardware for Trade Shows with Mike Szczys | https://theamphour.com/622-building-firmware-and-hardware-for-trade-shows-with-mike-szczys/ | March 5, 2023 |
| 635 | Low Power Connected Devices with Andrea Longobardi | https://theamphour.com/635-low-power-connected-devices-with-andrea-longobardi/ | June 4, 2023 |
| 651 | Learning Computing with Jeff Geerling | https://theamphour.com/651-learning-computing-with-jeff-geerling/ | November 20, 2023 |
| 679 | Satellite Design Engineering with Dan Esparon | https://theamphour.com/679-satellite-design-engineering-with-dan-esparon/ | October 11, 2024 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
| 704 | Applied Embedded Electronics with Jerry Twomey | https://theamphour.com/704-applied-embedded-electronics-with-jerry-twomey/ | October 2, 2025 |
