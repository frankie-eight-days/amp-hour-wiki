---
title: LoRa
concept: lora
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

LoRa is a proprietary physical-layer modulation for low-power, long-range sub-GHz radio, based on chirp spread spectrum and owned as intellectual property by Semtech.[443][376] The technology originated in the mid-2000s with a small French company whose technology Semtech acquired and productised; its modulation improved on earlier low-power radios in propagation, quality of service and multipath performance.[443] LoRa defines only what happens to the sub-GHz carrier to turn it into a data packet and carries no networking of its own; network protocols such as LoRaWAN are layered on top of it.[443][422] Its defining trade is a very low data rate in exchange for very high range, with good battery life following from the fact that a node transmits a short burst and then powers its radio down.[376]

## History

LoRa's origins lie with a pair of French engineers whose small company developed the underlying modulation in the mid-2000s; Semtech bought the technology and productised it into LoRa.[443] Semtech's commercial model for the technology has been to encourage small operators to stand up their own local networks, effectively duplicating cellular coverage so that sensors can be dropped anywhere and still reach the internet.[355] Early community gateways were priced around two hundred dollars each and were promoted as covering a radius of several miles, so that a handful of units could blanket a community.[272]

In 2015, The Things Network began publishing an open-source LoRaWAN network server, with participants buying gateways from any vendor and installing them at home to build shared coverage.[557] On the software-defined radio side, two independent open-source implementations of LoRa modulation and demodulation exist for GNU Radio, both published under the name gr-lora.[381] The DASH7 stack was later proposed as an alternative network layer to LoRaWAN, specifically to address LoRaWAN's collision behaviour, though it has not been widely deployed.[667]

## Modulation

LoRa's modulation is chirp spread spectrum.[443] A LoRa symbol is an up-chirp whose starting point within the sweep is shifted to carry data, rather than up-chirps and down-chirps representing ones and zeros; a single chirp carries roughly five to ten bits depending on how far it is shifted.[667] Down-chirps appear in a LoRa frame only in the synchronisation sequence, which uses two and a quarter of them; all remaining symbols in the frame are up-chirps.[667]

Because a LoRa receiver correlates against one precisely specified chirp shape, it can extract that waveform from signals far noisier than itself; this processing gain is what allows LoRa to be received below the noise floor.[667] Chirp detection is robust against terrestrial multipath because the receiver looks for tones rather than reconstructing symbols, whereas code-division schemes suffer inter-symbol interference when reflected copies arrive smeared in time.[667]

LoRa deliberately trades the full orthogonality of code-division schemes such as those used by GPS for far easier synchronisation and cheap receiver hardware; the cost is that two transmissions sharing frequency, spreading factor and timing collide in a way that is very difficult to separate.[667]

### Spreading factor

The spreading factor sets the length of the chirp: a longer chirp allows a more accurate lock and therefore greater range, while a shorter one gives a higher data rate over less distance.[667] At the highest spreading factor, SF12, throughput falls to a few bits per second and airtime per message becomes long.[677] The receiver must be configured for the same spreading factor as the transmitter to recover the message.[677]

Because a LoRa receiver's sensitivity is high enough to decode extremely weak signals, even the residual harmonic energy radiated when a microcontroller GPIO is toggled at a few megahertz can be received: pins not designed as high-speed outputs have slow edges, so the harmonics reaching the 900 MHz band are very low power, yet still decodable. This is the basis of software-defined LoRa transmission from a bare microcontroller.[667]

## Frequency allocation and regulation

LoRa is not tied to one frequency; it is applied across the ISM bands, commonly at 315 MHz, 433 MHz, 868 MHz and 915 MHz.[376] Regional allocation splits deployments: 915 MHz is used in the United States and Australia, and 868 MHz in Europe.[393] In the United States, LoRa occupies the spectrum from roughly 900 to 915 MHz, with uplink channels around 903 MHz.[667]

The sub-GHz LoRa bands are discontinuous between regions, so a device or network intended to work worldwide cannot settle on a single band the way a 2.4 GHz design can.[728] Operating near 900 MHz rather than 2.4 GHz roughly quadruples the wavelength, so an antenna array of equivalent directivity must be significantly larger, and the spread-spectrum nature of the LoRa waveform also makes beamforming harder.[728] Community gateway hardware has consequently needed region-specific firmware builds; a Things Network gateway bought for use in Australia required a custom compile and did not work out of the box.[393]

Proposed reallocations of the 900 MHz ISM band, such as a navigation system seeking a change, are a live regulatory risk for LoRa deployments, and community projects including Meshtastic have filed comments against them.[680]

## Range

Vendor range figures of the order of ten kilometres on a couple of batteries are the headline specification for LoRa.[376] Achieved range is governed by line of sight rather than by transmit power: a node flown on a radio-controlled aircraft over the Netherlands reached gateways in Utrecht and in Antwerp, Belgium, purely because altitude put it over the horizon.[376] Line-of-sight testing from elevated terrain has demonstrated links of roughly 36 kilometres.[628] Reported record links reach into the hundreds of kilometres, on the order of 240 kilometres, but require line of sight, considerable elevation and a high-gain antenna, so they are not representative of deployed range.[677] For comparison, WiFi driven at its lowest coding rates and long-range modes tops out at around 800 metres, which is the baseline LoRa has to beat to justify a second radio.[667]

## LoRaWAN

LoRa and LoRaWAN are distinct layers sharing a confusingly similar name: LoRa describes how one chip's radio talks to another, while LoRaWAN is a network protocol layered on top that routes packets to an application over the internet.[422]

### Architecture

In LoRaWAN a node transmits without addressing any particular receiver; every gateway in range hears the packet, and the packet header determines where the network forwards it.[422] Multiple gateways commonly receive the same packet, and the server side deduplicates the repeated copies before handing the reading to the application.[422] The gateway is a dumb forwarder that relays received packets to the network server; the account, key management and data handling all sit on the server side, which is where the system's complexity lives.[557]

LoRaWAN traffic carries layered encryption: the outermost key tells the gateway whether the packet belongs on that network and should be forwarded rather than dropped, while the payload remains encrypted beneath it up to the application server.[677] LoRaWAN is bidirectional, so data can be sent down to a node as well as up from it, but the mechanism is centralised through the network and application servers.[677]

LoRa links are half duplex; an application built directly on the physical layer picks its own transmit and listen times, whereas LoRaWAN defines three schemes governing when a node listens.[376] Gateway-initiated downlink to a node is not what LoRa is suited to, so applications that need to command a remote device on demand require another technology.[376]

Node transceivers such as the SX1276 receive on a single channel, while gateway builds use eight-channel receivers so that many nodes on different channels can be heard at once.[667] The value of building on LoRaWAN rather than a private protocol is the existing density of gateways: the radio provides a wide net of receivers and the internet carries the traffic the rest of the way.[667]

## Hardware and power

LoRa is an intellectual-property block describing a modulation rather than an open standard, and building a node requires an SPI-controlled radio chip from Semtech, the owner of that IP, plus a software library to extract the data.[376] This single-source silicon is a design and supply constraint: the transceiver can only be bought from Semtech, unlike Bluetooth radios, which are already integrated into most electronics.[728]

Complete node hardware is inexpensive: modules built around a Semtech chip sell for around five dollars, and combined ESP32-plus-LoRa development boards for fifteen to twenty dollars.[677] LoRa transceivers reach sleep currents below one microamp, which is what makes multi-year battery operation practical; current is materially higher during transmit and lower during receive.[557] A coin cell has an internal resistance measured in tens of ohms, so most transmitters collapse its terminal voltage when the radio turns on; LoRa is among the few radios that can be run from one, and even then bulk capacitance is normally added to absorb the transmit pulse.[640]

Relative to plain sub-GHz FSK, LoRa's maximum data rate is roughly a tenth of that achievable with a module such as the RFM69, and that gap is inherent to the protocol rather than an implementation limit.[398] LoRa transceiver modules also cost more per unit and are inherently more complex to work with than plain FSK sub-GHz modules, so range is the only reason to accept the trade.[398]

## Capacity, coexistence and security

LoRa occupies a wide band, so widespread deployment leaves measurably less spectrum for other users, and coexistence problems are expected to appear as density rises.[376] Network capacity, not link budget, is the scaling limit: channels are few and slow, so collisions rise with the number of devices sharing a network.[618]

LoRa has no connected or disconnected state, so the deauthentication-style attacks that work against WiFi have no analogue; jamming the receiver remains the available attack.[376]

## Applications and related networks

Remote sensing is the application LoRa fits best, and the clearest case for it is a site where no other network exists and one has to be built regardless.[376] Deploying hundreds of sensors with individual cellular modems is uneconomic in module cost, power and connectivity charges, which is the structural argument for a LoRa network with shared gateways.[380] Where the deployment location is not under the builder's control, cellular is the better wide-area choice; LoRa's observed sweet spots are smart-city and agricultural installations where the operator owns the site.[603] LoRa is the wrong choice for applications that generate a lot of data or need it in near real time; a body-worn cycling telemetry system failed on both counts because its data volume and latency requirement ran directly against LoRa's strengths.[376]

Payload budgets on LoRaWAN are small enough that application state is bit-packed rather than sent as structured data; a single byte encoding 255 distinct states is a normal way to report a combination of detected conditions.[517] Where the payload is only an identifier and a position, the bare LoRa transceiver used point to point is sufficient and the LoRaWAN ecosystem can be skipped entirely, an approach Greg Davill took in his own hardware work.[473]

Meshtastic is a firmware and application layer over bare LoRa that forms an ad-hoc mesh rather than a LoRaWAN-style star; a packet hops between nodes but reaches the internet only if some node on the network is bridging it.[677] Amazon Sidewalk, by contrast, is built on LoRa radios but operates point to point rather than as a mesh, and participation is opt-in.[628]

Stock firmware libraries such as RadioHead give only point-to-point links, and layering channels on top of them produces a bespoke, non-standard system, making firmware rather than radio hardware the practical barrier in many LoRa projects.[677]

Two deployment decisions illustrate the structural trade-offs. On the Blues Wireless radiation and air-quality monitoring deployment in the Fukushima exclusion zone, Ray Ozzie's team used solar-powered boxes with dual particle counters and dual Geiger counters backhauled over LoRa through a Raspberry Pi-based concentrator, and moved to cellular as service became available because building and maintaining a private LoRa network is difficult in that environment.[603] On the Hubble Network satellite IoT programme, Alex Haro's team evaluated LoRa against Bluetooth and chose Bluetooth, because Bluetooth radios are already present in nearly every device and 2.4 GHz is unlicensed worldwide, whereas LoRa requires adding a single-source radio in region-specific bands.[728]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 272 | An Interview With Luke Beno of Analog.io | https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/ | October 21, 2015 |
| 355 | The Internet of Septage (with Akiba) | https://theamphour.com/355-the-internet-of-septage-with-akiba/ | August 13, 2017 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 380 | Just Terrestrial and Space Things | https://theamphour.com/380-just-terrestrial-and-space-things/ | February 18, 2018 |
| 381 | An Interview with Derek Kozel | https://theamphour.com/381-interview-with-derek-kozel/ | February 25, 2018 |
| 393 | I've bitten myself | https://theamphour.com/393-ive-bitten-myself/ | May 20, 2018 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 443 | An Interview with JP Norair | https://theamphour.com/443-an-interview-with-jp-norair/ | May 19, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 517 | Depth and AI with Brandon Gilles and Brian Weinstein | https://theamphour.com/517-depth-and-ai-with-brandon-gilles-and-brian-weinstein/ | November 15, 2020 |
| 557 | Generic Nodes with Orkhan Amiraslanov | https://theamphour.com/557-generic-nodes-with-orkhan-amiraslanov/ |  |
| 603 | An Interview with Ray Ozzie (Blues Wireless) | https://theamphour.com/603-an-interview-with-ray-ozzie-blues-wireless/ | September 25, 2022 |
| 618 | Refrigerators and Robots with Amitabh Shrivastava | https://theamphour.com/618-refrigerators-and-robots-with-amitabh-shrivastava/ | February 5, 2023 |
| 628 | Two Dads Puzzlin Things Out | https://theamphour.com/628-two-dads-puzzlin-things-out/ | April 16, 2023 |
| 640 | Software Defined Power Supplies with Werner Johansson | https://theamphour.com/640-software-defined-power-supplies-with-werner-johansson/ | July 25, 2023 |
| 667 | Long Distance with CNLohr-a | https://theamphour.com/667-long-distance-with-cnlohr-a/ | May 23, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
| 680 | Catching Rockets with Musk Sticks | https://theamphour.com/680-catching-rockets-with-musk-sticks/ | October 15, 2024 |
| 728 | Space Age Bluetooth with Alex Haro | https://theamphour.com/728-space-age-bluetooth-with-alex-haro/ | July 9, 2026 |
