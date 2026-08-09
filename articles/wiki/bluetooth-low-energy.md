---
title: Bluetooth Low Energy
concept: bluetooth-low-energy
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

Bluetooth Low Energy (BLE) is a short-range wireless protocol that shares only the lowest layers of the Bluetooth specification, such as the physical layer, with classic Bluetooth; the protocol stack built on top of that radio is a different design.[144] Introduced in 2010 under the original name Wibree before being folded into the Bluetooth specification, it was designed around very small packets sent infrequently, enabling battery lifetimes of a year or more from a coin cell at the cost of the bandwidth and connection behaviour of classic Bluetooth.[155][664] BLE defines an asymmetric connection model in which a central device, typically a smartphone or PC, manages the connection while a low-power peripheral answers it, and it exposes application data through enumerated services with read, write and notify properties rather than through fixed profiles.[226][698]

## History

Bluetooth Low Energy dates from 2010 and originated under the name Wibree before being incorporated into the Bluetooth specification.[664] The technology addressed a specific power failure of classic Bluetooth: the classic baseband digital section has to run continuously in a connected peripheral, so devices such as wireless keyboards exhausted their AA cells in about two days.[169]

Because BLE support is a hardware property of the host, a phone with only a classic Bluetooth radio cannot communicate with a BLE device, and availability on handsets therefore depended on the replacement cycle of consumer hardware.[144] Apple introduced BLE support with the iPhone 4S.[155] Android hardware supported BLE earlier than the platform did; through Android 4.2 there was no common way to use it, as each handset required its manufacturer's own stack, and a common API was added only in Android 4.3, corresponding to API level 18.[155][226]

The silicon supply base differed markedly between the two variants: classic Bluetooth silicon came from roughly four main vendors, while BLE silicon was available from dozens.[175] When early demand for BLE outran the available integrated parts, designers placed a separate microcontroller die and BLE die side by side in one package, routing a memory bus, enable signals and power between them.[469]

## Relationship to classic Bluetooth

BLE and classic Bluetooth occupy exactly the same 2.4 GHz spectrum and the same set of channels, with BLE using a subset, so a dual-mode device cannot fully use both links at the same time.[155] Beyond the shared physical layer, the upper stacks diverge completely.[144] Classic Bluetooth profiles such as the serial port profile and HID are defined by the Bluetooth SIG and handed to the implementer, whereas BLE requires the developer to build the profile unless the chosen stack supplies one; this is more work but permits a much lighter, application-specific data model.[155]

Classic Bluetooth was designed as a wireless serial-port replacement and therefore has good support for implementing serial ports, a capability BLE does not carry over.[354] A BLE cable-replacement service can be made to work but bends the protocol into a role it was not designed for, performing worse than an equivalent classic serial port profile connection, and it does not present itself as a COM port at the host driver level, so software written against a classic serial port will not work unchanged.[155][354]

A BLE peripheral advertises a description of the data it offers, so any nearby application can discover it and attach, in place of the PIN exchange and pairing handshake that classic Bluetooth requires before communication.[144]

## Protocol model

### Roles

BLE defines two roles: the central, typically the phone, manages the connection, while the peripheral, typically the small low-power sensor, does the minimum of answering the central rather than transmitting whenever it chooses.[226] In the sample sets of vendor stacks the peripheral is the node device and the central is the side that accepts connections, with reference profiles provided for heart rate, health thermometer, HID and a UART service.[664] An iPhone can occupy the central and peripheral roles at the same time.[226]

### Services and properties

Service enumeration is built into the protocol, so a scanner application such as nRF Connect can list every nearby device that is advertising along with the services it offers, and usually connect to them without obstruction.[698] Each BLE service exposes properties, principally read, write and notify, that function as permissions on that item of data; notify behaves as a publish-subscribe channel from the device back to the host.[698] BLE has no native mechanism for asynchronous communication, but the pattern is constructed by using the notify property to receive data from the device and the write property to send data to it.[698]

## Power characteristics

BLE is a low-bandwidth link among the short-range radio options, while classic Bluetooth offers relatively high bandwidth at the cost of holding a connection open, and Wi-Fi is generally excluded from battery-powered products on power grounds.[145] An early integrated Bluetooth 4.0 low-energy part drew about 3.8 milliamps while receiving and transmitting, a figure considered low for a radio of that era.[152] Transmit current peaks at roughly ten milliamps for the short duration of a transmission, well above the average draw.[226]

A BLE peripheral that sends a one- or two-byte packet once a second and sleeps between transmissions can run for about a year on a coin cell, a duty cycle that classic Bluetooth cannot achieve.[155] Supporting classic Bluetooth alongside BLE forfeits the low-energy power saving, because the classic radio must run continuously at roughly two milliamps, which exhausts a coin cell in about two days.[155] Dual-mode Bluetooth radios are therefore normally placed at the end of the link that has a large battery, such as a smartphone or PC, while the peripheral implements one mode only.[155]

### Energy budgeting and coin cells

Sizing a BLE product's energy budget requires the duty cycle to be pinned down first: how often the user activates it, how often it must ping, how fast it must respond, and whether it can store and forward.[389] Battery life is estimated from the cell's capacity discharge curve against the nominal average current, and the transmit current spikes of a BLE radio are averaged out by the filter capacitors rather than being drawn from the cell directly.[389] A typical CR2032 coin cell has about 20 ohms of series resistance, which is why a BLE transmit current pulse must be supplied from local bulk capacitance instead of from the cell.[389] Five years of life from a coin cell is achievable only with a cell thicker than a CR2032, such as a CR2450-class part with roughly four times the capacity.[389]

## Hardware implementations

The BlueGiga BLE112 module is built on the Texas Instruments CC2540 and is driven by a host processor over a UART, but its on-board 8051 can also run BlueGiga Script so sensors attach directly to the module and no external microcontroller is needed.[144] The CC2540 itself combines a BLE radio and an 8051 core in a single package, and on that basis it was used as the BLE platform for battery-powered instruments.[218] The analogue-to-digital converter integrated in the CC2540 is nominally 12 bits but delivers roughly three effective bits, so it serves only to prove out a use case and not for measurement.[218]

The RFduino module packages an ARM Cortex-M0 with an integrated BLE radio in a footprint of about 15 by 15 millimetres, small enough for pendant-scale wearables.[204] Because a BLE device can be reprogrammed over the radio link itself, a development board can be built with no connectors at all.[226] On a BLE system-on-chip the vendor's Bluetooth stack occupies a fixed region of memory and the application image is linked to start at the end of that region, after which it runs as an ordinary program.[516] Nordic Semiconductor's nRF series is regarded as well suited to low-power personal area networking.[638] The BLE implementation on the ESP32 has been judged poor quality by practitioners who otherwise regard BLE as an attractive technology.[435]

## Platform considerations

A BLE accessory does not go through Apple's Made for iPhone hardware approval process; in the most demanding case the app review asks only for a video of the hardware working with the application.[226] Every host platform's BLE implementation behaves differently — "Each BLE implementation is a special snowflake" — so host-side application work must effectively be redone for each operating system and version.[354] In one cross-platform instrument application, the only platform-specific code was the BLE implementation for each device plus the touchscreen handling.[354]

Android 4.3 did not reliably support multiple simultaneous BLE connections even though the API implied it should, misbehaving when a second adapter was added, while Android 6, 7 and 8 handled it correctly.[354] Android 4.3 also contained a BLE defect that closed the application for reasons unrelated to the application itself, with no workaround available on that version.[354]

A general-purpose BLE scanning and inspection application is the standard bench tool for testing a peripheral, because it exposes whatever the device advertises without requiring a custom app.[226]

## Design selection and engineering practice

The choice between BLE and classic Bluetooth should be driven by the data the product must send and receive: if the traffic fits BLE, adding classic support as well is usually a kludge, and if the product is already pushing the limits of BLE the choice is wrong.[155] BLE performs poorly at high bandwidth because the protocol was built around very small packets sent infrequently, so throughput-oriented uses run into significant speed limits; a recurring design error is specifying BLE for a product whose application needs more bandwidth than the link can deliver, a problem compounded by BLE's non-deterministic timing.[155][264] There is no satisfying low-power alternative at higher data rates, so video transport forces a move to Wi-Fi and an order-of-magnitude jump in power consumption.[638]

BLE is the right choice when the product must run for a year or more from a coin cell such as a CR2032.[354] Mechanical form factor determines the battery, and the battery in turn determines the radio: a keyring-sized product implies a CR2032 and therefore forces BLE.[389] Conversely, for a product powered by four AA cells the low-energy power saving does not repay BLE's integration cost; in one such product a classic Bluetooth module would have been the better choice in hindsight, a conclusion arrived at too late because the unit was already at the test house for FCC certification and the radio module could no longer be changed without restarting certification.[354] A related practitioner position drawn from commercial products is to prefer classic Bluetooth and use BLE only where it is genuinely required; assuming BLE supports a proper serial implementation is a costly error, as implementing serial behaviour over BLE consumed substantial time, money and effort and ended as a kludge.[516]

BLE is fundamentally a mobile-connectivity protocol for linking a sensor to a nearby smartphone rather than a general-purpose sensor-network protocol, and it delivers value only when a phone is within range of the device; a remote unattended sensor whose whole purpose is to report while the owner is absent gains nothing from it.[245][272] A BLE device can achieve roughly a year of operation from a CR2032 coin cell, but at the cost of the connection reliability that classic Bluetooth provides.[389]

### Application architectures

A common architecture for a long-range radio product is to use BLE only as the short link to the user's phone while a separate transceiver, such as a VHF link in the 150 MHz region, carries traffic between units.[214] Battery-powered BLE devices can be reached from the cloud by adding Wi-Fi-to-BLE or cellular-to-BLE gateways; where no mains supply is available at the gateway site the gateway itself must also be a low-power battery-powered design.[635] BLE is a reasonable choice for local firmware update of a sealed battery-powered node, performed by a technician standing next to it, rather than pushing the update down from a long-range gateway.[376] Pairing BLE with NFC on the same sensor lets a user either stream data live to a phone carried during use or download the stored log later by touching the device to a phone, removing the requirement to carry the phone.[635] A wearable air-quality sensor measuring 18 by 18 by 8 millimetres and weighing about five grams carried a carbon monoxide sensor and reported over BLE, with the battery housed separately in the garment and coupled magnetically.[635]

A multi-node BLE network can be simulated on the bench by building a single card carrying several BLE microcontrollers, each addressable over a generic host interface.[518]

## Qualification and branding

Bluetooth SIG qualification is a voluntary association requirement rather than a government regulation: the 2.4 GHz band itself is largely unregulated, but a product may not carry Bluetooth branding or claim conformance without following the SIG's guidelines.[155]

## Security considerations

A BLE consumer device that advertises continuously discloses its usage pattern to anyone within radio range, since the advertisement itself is observable without connecting.[660] In practice a BLE link reaches across a small house but does not carry to a neighbouring property, so the exposure from continuous advertising is bounded by the low transmit power.[660]

A common BLE security weakness is a manufacturer transplanting an existing custom binary serial protocol onto GATT writes and notifies without added protection, leaving the traffic open to sniffing, reverse engineering and replay by anyone who can connect.[698] A BLE link is far easier to intercept than the wired serial connection it replaces, since observing it needs only a radio in range rather than physical access to the conductors.[698]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 144 | An Interview with Bob Davidson - Hoodied HP Hijinks | https://theamphour.com/the-amp-hour-144-hoodied-hp-hijinks/ | May 7, 2013 |
| 145 | PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness | https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/ | May 14, 2013 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 155 | An Interview with Jeff Rowberg - Mini Module Master | https://theamphour.com/the-amp-hour-155-mini-module-master/ | July 22, 2013 |
| 169 | An Interview with Vincent Himpe - Escaped Electron Elocution | https://theamphour.com/169-an-interview-with-vincent-himpe-escaped-electron-elocution/ | October 28, 2013 |
| 175 | An Interview With Andrew Witte - Telistic Timepiece Technomania | https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/ | December 9, 2013 |
| 204 | An Interview with Noah Feehan - Biloquistic Blinking Blush | https://theamphour.com/204-an-interview-with-noah-feehan-biloquistic-blinking-blush/ | June 23, 2014 |
| 214 | Impedance Matching With Charvat And Ossmann - Recurring RF Remontados | https://theamphour.com/214-impedance-matching-with-charvat-and-ossmann-recurring-rf-remontados/ | September 1, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 245 | An interview with Akiba from Freaklabs - Dimissory Diagraphical Debt | https://theamphour.com/245-an-interview-with-akiba-from-freaklabs-dimissory-diagraphical-debt/ | April 14, 2015 |
| 264 | The Cost Of Doing Business | https://theamphour.com/264-the-cost-of-doing-business/ | August 25, 2015 |
| 272 | An Interview With Luke Beno of Analog.io | https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/ | October 21, 2015 |
| 354 | A Meeting Of The Davids | https://theamphour.com/354-a-meeting-of-the-davids/ | August 7, 2017 |
| 376 | An Interview with Richard Ginus | https://theamphour.com/376-an-interview-with-richard-ginus/ | January 21, 2018 |
| 389 | Sipping Coulombs | https://theamphour.com/389-sipping-coulombs/ | April 22, 2018 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 469 | An Interview with Craig J Bishop | https://theamphour.com/469-an-interview-with-craig-j-bishop/ | December 1, 2019 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 635 | Low Power Connected Devices with Andrea Longobardi | https://theamphour.com/635-low-power-connected-devices-with-andrea-longobardi/ | June 4, 2023 |
| 638 | Building AR Headsets with Aedan Cullen | https://theamphour.com/638-building-ar-headsets-with-aedan-cullen/ | July 9, 2023 |
| 660 | My Toothbrush Is Broadcasting | https://theamphour.com/the-amp-hour-660-my-toothbrush-is-broadcasting/ | March 4, 2024 |
| 664 | Simulating doors falling off | https://theamphour.com/664-simulating-doors-falling-off/ | April 3, 2024 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
