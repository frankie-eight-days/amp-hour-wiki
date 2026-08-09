---
title: Wi-Fi
concept: wifi
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

Wi-Fi is a wireless local-area networking technology operating in the 2.4 GHz and 5 GHz bands, with products required to cover both bands rather than one.[446] The name is a play on hi-fi and does not stand for wireless fidelity.[457] It is engineered for throughput rather than bounded latency, so a fast, predictable round trip is not something it provides.[264] Its defining engineering trade-off is power: it is high power relative to Bluetooth Low Energy and low power only relative to always-on Wi-Fi devices, so the comparison class must be stated before calling a Wi-Fi part low power.[249]

## History

In the mid-2000s the principal use of Wi-Fi was replacing the Ethernet cable on a laptop; the design premise behind the first wall-mounted Wi-Fi appliances, developed by Bunnie Huang, was that the same radio could deliver web content to a fixed device, a premise settled a year later when the smartphone arrived.[84] At that time, integrating Wi-Fi was expensive enough to take a large share of a product's bill of materials.[342] By the mid-2010s the planning assumption for a connected product had inverted, with a Linux-capable computer, Wi-Fi and Bluetooth all treated as free at the board level.[251]

The decisive event in low-cost Wi-Fi was the ESP8266, which put a Wi-Fi radio and a 32-bit Tensilica processor on a board selling for about $2.70.[232] The part was designed as a serial peripheral driven by AT commands from a host microcontroller, but users deleted the external host and ran the application on the processor inside the radio chip, for compactness and lower power; Espressif shipped a complete development environment as a downloadable virtual machine with compilers and full source, which enabled that repurposing.[232] The initial data sheet was readable only by native Chinese speakers, and a user community translated it before the chip could be used widely; rival low-cost Wi-Fi silicon of the same period never released usable documentation and went nowhere, while equivalent parts from established western vendors were far more expensive.[403][637] Wi-Fi crossed two cost thresholds: a module reaching five dollars, and then a single sub-dollar part combining microcontroller and radio, at which point adding connectivity stopped needing a justification in the bill of materials.[637] Engineers will accept a clumsy interface, in this case AT commands over a serial port, when the part is cheap enough, and will build the missing tooling themselves; low cost from the bottom of the market is the repeated pattern by which such parts displace established ones.[264]

## Bands and propagation

Wi-Fi has occupied both 2.4 GHz and 5 GHz for over a decade, so an antenna design for a Wi-Fi product must cover both bands.[446] In handsets, Bluetooth and Wi-Fi typically share one radio and one antenna, while GPS at 1.575 GHz either has its own antenna or shares with Wi-Fi or cellular; the antenna engineer works from the band list rather than the protocol names.[446]

The 2.4 GHz band is a shared and congested medium. A domestic Wi-Fi router radiates on the order of two hundred milliwatts, which sets the interference floor other 2.4 GHz devices in the same space must work against.[245] At public venues the band is unsuitable for mission-critical control links because every phone and access point in the room occupies it: wireless stage costumes running on 2.4 GHz, built by Akiba of Freaklabs, suffered unexplained random signal drops until the band itself was identified as the cause.[245] Amplitude-only demodulation in the band is likewise vulnerable: a live radio-reflection demonstration by Michael Ossmann failed outright in a room holding fifteen hundred people, and the remedy pursued was direct-sequence spread spectrum modulation to recover the signal from the interferers.[214] Dense venues degrade Wi-Fi through sheer user count rather than through any equipment fault, which is why conference and hotel networks fail for work that assumes a stable link.[217] Any product emitting in the 2.4 GHz band shares it with the customer's own network, so a design that interferes with nearby Wi-Fi creates a support problem regardless of whether it meets emissions limits.[445]

Line-of-sight range figures do not predict deployed performance: a radio that reaches five hundred feet in the open may not cross ten feet of concrete wall, so range testing must be done in the intended environment.[556] Range at fixed power is a function of frequency; moving below one gigahertz buys range that 2.4 GHz cannot reach without more power, and the sub-gigahertz FSK stack is far simpler than a Wi-Fi stack, so both range and software complexity push long-link designs off Wi-Fi.[398] Conversely, Wi-Fi run at its lowest coding rates, using the one-megabit schemes and vendor long-range modes, reaches roughly eight hundred metres, which puts it in competition with dedicated long-range radio for many links.[667] Millimetre-wave links do not pass through walls and beam steering does not fix that, so a millimetre-wave replacement for Wi-Fi implies an access point in every room.[483]

Radiated power from a fixed transmitter falls with the square of distance, so separation is the effective control on exposure, and an access point's transmit power can be reduced in its own settings when coverage allows.[45] Enclosing a router in a metal cage blocks the signal it is there to provide; where transmitted power is genuinely a concern, the setting can be lowered in the access point's configuration.[553] Regulatory limits on access-point transmit power of a few hundred milliwatts exist to protect other receivers from being blinded and to keep the shared band usable, not because of any exposure hazard at those levels.[430]

## Power consumption

Battery operation and Wi-Fi are in direct conflict: a battery-powered Wi-Fi device is designed around turning the radio off and sleeping whenever it is not transmitting, so the design question becomes how rarely the device can afford to wake.[202] Measured current on a small Wi-Fi module spans two orders of magnitude by state: one to two milliamps with the radio off, five to six milliamps connected in power-save mode, and about one hundred milliamps with everything on.[202] A low-cost Wi-Fi module draws two hundred to three hundred milliamps at peak and under one milliwatt in deep sleep, so average consumption is set almost entirely by duty cycle.[249]

The transmit-power behaviour differs from cellular networks. Under LTE a handset lowers its output so the base station can just hear it, while a Wi-Fi station wants every node in the cell to hear it and therefore transmits at maximum power, which is why Wi-Fi power budgets do not shrink with proximity to the access point.[202] On the supply side, Wi-Fi transmit bursts are supplied from bulk decoupling rather than drawn through the cell: heavy bypass capacitance smooths the peak so the current does not have to pass through the battery's equivalent series resistance.[249] Where a wearable must hold a Wi-Fi link on a single lithium cell, the module is selected for its sleep-mode behaviour rather than its active performance.[638]

For fixed indoor products the calculus inverts: Wi-Fi's only serious disadvantage for home devices is power consumption, and where the device is mains-powered and the network already exists, that disadvantage does not apply, which is what makes cheap Wi-Fi modules the default for that class of product.[245] Always-on infrastructure is not free, however: Wi-Fi and the broadband modem together can account for around sixteen watts of continuous household draw, eight watts each.[604] Adding Wi-Fi to a small single-board computer raises idle consumption measurably; the wireless variant of one board idles higher than the equivalent board without it, with a reported figure of about 260 milliamps.[565]

In sensor networks, a hub-and-spoke topology of low-power proprietary radio nodes feeding one Wi-Fi gateway consumes less total power than putting Wi-Fi on every node, even though the hub then runs two radio solutions; twenty nodes is enough for the aggregate to favour the two-radio design.[272] The reason not to put Wi-Fi on every leaf node is cost and, increasingly, power alone: a battery-powered leaf node cannot carry Wi-Fi at a usable service life.[272] A common industrial architecture puts battery leaf nodes on 802.15.4 and makes the mains-powered gateway the only device that carries the site uplink, with Wi-Fi or cellular fitted to the gateway as a build option.[334]

## Latency and determinism

Wi-Fi is engineered for throughput rather than bounded latency, so deterministic round trips are outside its design envelope.[264] Real-time audio work will not tolerate it: delays of tens of milliseconds are audible in a two-way recorded conversation, so a wired connection is used for the link that carries the audio.[477] Streaming continuous instrument data over a wireless link runs into the same problem as wired networking, only worse: neither Wi-Fi nor Ethernet is deterministic, and a transport that guarantees eventual delivery does not guarantee timely delivery.[209] Interactive products built on Wi-Fi round trips inherit the link's latency, so a device expected to respond immediately should not put the response path over the network.[304]

Industrial and SCADA installations resist wireless because their control loops treat any packet loss as unacceptable and retries as a hazard, a requirements position rather than a preference.[443] Against that preference, radio designer J.P. Norair holds from field experience that a modern Wi-Fi link is often more reliable than an RS-485 bus, not because the wire is at fault but because RS-485 has many implementations and many ways to be got wrong, whereas the wireless stack is monolithic and well tested.[443] A connected controller must keep its primary function when the network is gone: a Wi-Fi thermostat that loses its server or its association falls back to its local sensor and continues to regulate temperature, degraded but working, because the appliance function cannot be allowed to depend on the link.[657] At the building scale, structured cabling should be installed during construction because pulling new wire into a finished building is expensive and the opportunity does not return, and because Wi-Fi does not cover every case.[510]

## Module and system architecture

Wi-Fi modules carry a dedicated processor for the protocol stack because running the stack on the application microcontroller leaves too few resources for the application itself; the host then talks to the module over SPI, I2C or a serial link.[146] A vendor without a Wi-Fi part of its own adds connectivity by placing a third-party Wi-Fi module alongside its microcontroller and driving it in AT-command mode, which is why development boards pair an unrelated radio chip with the host processor.[659] Embedded Linux earns its place when a system must combine several subsystems at once, such as Wi-Fi with a camera and Ethernet; implementing Wi-Fi on a microcontroller that does not integrate the radio is impractical enough that the integrated part effectively decides the architecture.[515]

The ESP32 pairs two 240 MHz 32-bit cores running FreeRTOS with classic Bluetooth, Bluetooth Low Energy and Wi-Fi that supports both station and access-point modes as well as scanning.[330] A Wi-Fi microcontroller can run either as a station joining an existing network or as an access point that other devices join, and the two modes serve different product roles: pulling data from the internet versus offering a local configuration network.[326] Later parts moved the same integration onto RISC-V and added the second band, giving low-cost chips that serve both 2.4 GHz and 5 GHz networks.[597] A measured throughput figure for a low-cost Wi-Fi microcontroller board is about five megabits per second, which bounds what such a part can be asked to carry.[595] For point-to-point data between microcontrollers, the connectionless ESP-NOW mode of Espressif parts is used in preference to an ordinary Wi-Fi association, because it removes the access point from the path.[667]

Cloning a Wi-Fi system-on-chip is not a matter of copying silicon: clones of complex parts are behavioural reimplementations, and reproducing a Wi-Fi and Bluetooth chip means working from the standards and building the radio processing afresh.[359] At board level, a typical Wi-Fi product is manufactured in volume on ordinary FR4, so guidance to reach for a low-dielectric-constant PTFE laminate on a 2.4 GHz design mistakes the requirements of high-performance RF for the requirements of consumer wireless.[718]

## Antennas and regulation

Reverse-polarity antenna connectors on Wi-Fi equipment exist because United States regulators objected that a standard connector would let a user swap the supplied antenna for a high-gain Yagi and extend coverage well beyond the intended area; the non-standard gender is a compliance device, not an electrical one.[708] Regulatory transmit-power limits of a few hundred milliwatts exist to keep the shared band usable by preventing receivers from being blinded.[430] Consumer routers implement behaviour the Wi-Fi specification forbids, such as accepting a zero-length password, so a connected product must tolerate router defects rather than assume conformance.[202]

## Provisioning and deployment

The standard way a headless device joins a network is to open its own temporary access point so a phone can hand over the household credentials, which is why a newly installed appliance appears as an open SSID.[698] Provisioning can be moved off Wi-Fi entirely: giving the product a cellular path lets the owner enter network credentials in an app rather than making the installer hop onto the device's access point and back, which removes a step that costs installer time on every unit.[487]

Networked products routinely work in the development office and fail in the operating environment, because the office has a fibre backhaul and clear spectrum while the deployment site may sit among twenty-five overlapping Wi-Fi networks; testing difficult radio scenarios deliberately is the missing step.[556] Coverage gaps inside a building are commonly closed by repurposing a retired router as an access point fed by an Ethernet drop, and an 802.11n unit delivering around fifty megabits per second is sufficient for streamed video.[714] A product that relies on the customer's existing Wi-Fi inherits that infrastructure: field installations are commonly a consumer router in a closet on its default SSID and password, shared with everyone on the premises, down much of the time and knocked off the air by nearby switching equipment.[511] The argument that Wi-Fi is free does not survive deployment: someone pays for data eventually, and the engineering and support cost of using a site's Wi-Fi is what pushed one instrumentation product from Wi-Fi to a cellular link.[511] Cellular backhaul is also chosen over site Wi-Fi to avoid the customer's IT department: an industrial sensor product shipped its first deployment entirely on 3G because plant networks are not opened to new devices.[334] Utility customers reject Wi-Fi as a data path on reliability grounds, which constrains metering and energy-monitoring products that transmit over the householder's network.[371]

Shipping a fleet of Wi-Fi devices creates obligations beyond the radio: firmware must be updated across every unit in the field, the fleet's state must be visible, and data return must be verified, which is the service that connectivity platforms exist to provide.[422] The catalogue of router interoperability defects can only be assembled from a large deployed fleet: half a million shipped modules across thirty to forty countries produced connection data no individual small company could gather for itself, which is the argument for buying a connectivity platform rather than writing the link layer in-house.[202] Getting a device onto Wi-Fi is the easy part of a connected product; the sustained work is the service behind it, which is why connectivity vendors sell the backend rather than the radio.[202]

Cellular data costs recur where Wi-Fi appears free to the end user, which is the recurring commercial objection to cellular-connected products even when the radio itself is cheap.[509] Cellular network generations are switched off while products are still in service, stranding devices whose only uplink was that generation; Wi-Fi capability in the same device is what keeps it working, so the choice of uplink is a product-lifetime decision.[569]

## Security

Anyone with access to a Wi-Fi network is in a position to reach every computer on it and to keep that access after leaving radio range, so network membership should be treated as equivalent to physical access.[161] The KRACK weakness in WPA2 applied to essentially every Wi-Fi router and every Wi-Fi-connected device in the field, a class of exposure that patching cannot fully close because much of the installed base never receives updates.[364] Because Wi-Fi maintains association state, an attacker can forge disconnection messages so that station and access point each believe the other has gone, then impersonate the station; protocols with no connected or disconnected state are not open to that attack and can only be jammed.[376] Samy Kamkar demonstrated this class of attack against a consumer drone controlled over Wi-Fi without authentication: the drone was taken over by deauthenticating the owner and connecting in their place, using a single-board computer with a wireless card carried on a second drone, and the captured aircraft were chained into a following swarm.[308]

Security risk scoring ranks attack vectors from remote through local and adjacent to physical, where radio protocols including Wi-Fi and Bluetooth count as adjacent; once a device holds an IP address on a Linux stack it moves up that scale because network-reachable attack surface scores higher than RF-adjacent surface.[698]

## Non-communication uses

Wi-Fi doubles as a positioning system: a device reports the access points it can see and a database of network identifiers returns a position, which is faster than a satellite fix and works indoors.[376] A part may carry a Wi-Fi radio purely for identifier-based location rather than as a general network interface, so the presence of Wi-Fi in a device's block diagram does not imply it can carry data.[612]

Harvesting usable energy from ambient Wi-Fi is not practical: charging a phone battery from a Wi-Fi signal works out at something like twenty-six years.[98] Demonstrations of powering devices over Wi-Fi depend on a modified access point transmitting continuously at full power rather than on ordinary network traffic, so the result does not transfer to a standard router.[253]

## Relation to other wireless technologies

Wi-Fi is chosen over Bluetooth when content must be pushed to a device, because Bluetooth's practical ceiling of about one megabit per second or less limits how much can be sent, and a device with little local compute depends on receiving rendered content over the link.[638] Thread was built to reuse the 802.15.4 radios already shipping in Zigbee products, forming a self-healing mesh that is a separate backbone from Wi-Fi, cellular and Ethernet and sits just above IP networking so higher-level protocols can run on top of it.[526] A protocol carried into a router must stay simple enough to run in a couple of kilobytes on a three-dollar device and to be usable at hundred-piece volumes, not just at hundred-thousand-piece volumes, or the low-power tier never materialises; the gateway problem disappears when the low-power radio is built into the router, because the router is the one always-powered internet hub already present at every site.[272]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 45 | Texas Instruments, OPA & Chevy Volt - Nerdy Neuroelectronic Neurosis | https://theamphour.com/the-amp-hour-45-nerdy-neuroelectronic-neurosis/ | May 30, 2011 |
| 84 | An Interview with Bunnie Huang - Bunnie's Bibelot Bonification | https://theamphour.com/the-amp-hour-84-bunnies-bibelot-bonification/ | February 27, 2012 |
| 98 | Proemial Passive Poiesis | https://theamphour.com/the-amp-hour-98-proemial-passive-poiesis/ | June 3, 2012 |
| 146 | Hamvention, Arduino and Intel - Burdensome Background Battology | https://theamphour.com/the-amp-hour-146-burdensome-background-battology/ | May 21, 2013 |
| 161 | Interview with Michael Ossmann - Gifted Grimgribber Grokker | https://theamphour.com/the-amp-hour-161-gifted-grimgribber-grokker/ | September 2, 2013 |
| 202 | An Interview With Brandon Harris - Impish Internet Iamatology | https://theamphour.com/202-an-interview-with-brandon-harris-impish-internet-iamatology/ | June 9, 2014 |
| 209 | Headless Units and Baseless Batteries - KiCad Kickoff Kopophobia | https://theamphour.com/209-headless-units-and-baseless-batteries-kicad-kickoff-kopophobia/ | July 28, 2014 |
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 217 | 3D Printed Shark Jumps - Edifying Edison's Energy | https://theamphour.com/217-3d-printed-shark-jumps-edifying-edisons-energy/ | September 22, 2014 |
| 232 | Impedance Matching" with Davidson and Vandenbout - Presbytes Pushing Portfolios | https://theamphour.com/232-impedance-matching-with-davidson-and-vandenbout-presbytes-pushing-portfolios/ |  |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 249 | Wearables Might Have Limited Fashion Options - Lachrymogenic Lane Language | https://theamphour.com/249-wearables-might-have-limited-fashion-options-lachrymogenic-lane-language/ | May 12, 2015 |
| 251 | Shifting Away From DIY - Pedetentious PnP Progress | https://theamphour.com/251-shifting-away-from-diy-pedetentious-pnp-progress/ | May 26, 2015 |
| 253 | Consolidate All The Things - Zonked Zelotic Zaitech | https://theamphour.com/253-consolidate-all-the-things-zonked-zelotic-zaitech/ | June 9, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 272 | An Interview With Luke Beno of Analog.io | https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/ | October 21, 2015 |
| 304 | Alexa joins the fray | https://theamphour.com/304-alexa-joins-the-fray/ | June 22, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 326 | Magical Fire Bags | https://theamphour.com/326-magical-fire-bags/ | December 7, 2016 |
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 334 | An Interview with Gerry Roston | https://theamphour.com/334-an-interview-with-gerry-roston/ | February 1, 2017 |
| 342 | Our first in-person show | https://theamphour.com/342-our-first-in-person-show/ | April 9, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 371 | An Interview With Joe Bamberg | https://theamphour.com/371-an-interview-with-joe-bamberg/ | December 10, 2017 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 430 | Shahriar Discusses 5G | https://theamphour.com/430-shahriar-discusses-5g/ | February 17, 2019 |
| 443 | An Interview with JP Norair | https://theamphour.com/443-an-interview-with-jp-norair/ | May 19, 2019 |
| 445 | Ludicrously High Frequency Interference | https://theamphour.com/the-amp-hour-445-ludicrously-high-frequency-interference/ | June 2, 2019 |
| 446 | An Interview with Pete Bevelacqua | https://theamphour.com/446-an-interview-with-pete-bevelacqua/ | June 9, 2019 |
| 457 | Dotty Ernest Annty Frost | https://theamphour.com/457-dotty-ernest-annty-frost/ | September 8, 2019 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 483 | An Interview with Adrian Tang | https://theamphour.com/483-an-interview-with-adrian-tang/ |  |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 509 | Cellular IoT with Jared Wolff | https://theamphour.com/509-cellular-iot-with-jared-wolff/ | September 20, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 511 | Brewing Electronics with Eli Hughes | https://theamphour.com/511-brewing-electronics-with-eli-hughes/ | October 4, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 526 | Why IoT Is Difficult with Jonathan Beri | https://theamphour.com/526-why-iot-is-difficult-with-jonathan-beri/ | January 18, 2021 |
| 553 | Debunking with Shahriar | https://theamphour.com/553-debunking-with-shahriar/ | August 10, 2021 |
| 556 | Firmware for Hardware Engineers with Phillip Johnston | https://theamphour.com/556-firmware-for-hardware-engineers-with-phillip-johnston/ | September 6, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 569 | Electric Fields, Son. | https://theamphour.com/569-electric-fields-son/ | December 5, 2021 |
| 595 | Trade Show or Conference? | https://theamphour.com/595-trade-show-or-conference/ | July 10, 2022 |
| 597 | Wow, Dave REALLY likes Top Gun | https://theamphour.com/597-wow-dave-really-likes-top-gun/ | July 24, 2022 |
| 604 | Robo Fry Guy | https://theamphour.com/604-robo-fry-guy/ | October 9, 2022 |
| 612 | Slapping Industries | https://theamphour.com/612-slapping-industries/ | December 13, 2022 |
| 637 | CH32V003...fun! with CNLohr | https://theamphour.com/637-ch32v003-fun-with-cnlohr/ | June 25, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
| 659 | Altium...Acquired! | https://theamphour.com/659-altium-acquired/ | February 20, 2024 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
| 708 | All the Connectors with Davide Andrea | https://theamphour.com/708-all-the-connectors-with-davide-andrea/ | November 1, 2025 |
| 714 | The Measurement Blues with Martin Rowe | https://theamphour.com/714-the-measurement-blues-with-martin-rowe/ | February 2, 2026 |
| 718 | Layout Review with Zachariah Peterson | https://theamphour.com/718-layout-review-with-zachariah/ | March 11, 2026 |
