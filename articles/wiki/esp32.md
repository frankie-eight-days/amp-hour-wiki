---
title: ESP32
concept: esp32
generated: 2026-08-09
model: k3
spec: knowledge-only-v4-cluster
---

The ESP32 is a family of low-cost 32-bit microcontroller chips and modules built around Wi-Fi and short-range-radio connectivity, with early parts offering a pair of 240 MHz 32-bit processors running a real-time operating system and radios able to act as an access point or scan.[330] Its design significance comes from integration economics: a certified module combines two cores, both radios, and a large peripheral set for a few dollars, and the processing is cheap enough that the part appears in designs that never enable the radio at all.[422][403] The family has since broadened in both directions, including a single-core lower-power variant with a hardware USB peripheral, a radio-less dual-core 400 MHz design with a slower low-power companion core, and recent parts using an open instruction set with dual-band Wi-Fi.[500][615][597]

## Architecture

The original dual-core arrangement was conceived as asymmetric multiprocessing: two cores behaved as though two discrete microcontrollers had been placed side by side with a communication bus between them.[359] Sharing memory regions between the cores converted that arrangement into a symmetric multiprocessor, but only after the operating system it runs was extended to handle two cores.[359] Once symmetric, threads become transparent to the programmer: a thread can be pinned to a named core when control matters, or left for whichever core has the most free time when throughput matters, with ordinary inter-thread communication working in either case.[359]

The processor count is effectively three rather than two: two identical fast cores form the dual-core processor, while a separate ultra-low-power core is intended to keep running when the rest of the device is asleep.[435] Using both fast cores roughly doubles available compute, but the gain is not automatic because the cores must be synchronised, placing a real software burden on the developer.[435] Later members of the family deliberately step back from that peak: one single-core variant shares time on the same core that runs the radio stack, trading the second core for lower power, and adds a hardware USB peripheral so the data lines connect straight to the chip and the separate serial-conversion chip disappears from the board.[500]

Memory dominates the die: around half a megabyte of RAM accounts for roughly three quarters of the silicon area, which fixes the on-chip memory budget.[359] That budget is why a full operating system was never a candidate, because running Linux would demand external memory and, at those sizes, an external DDR part with high-speed signalling, which is a different product rather than a firmware choice.[359]

The family also includes a dual-core 400 MHz design with a secondary 40 MHz low-power core and no radio at all, extending the platform beyond connectivity parts.[615] Recent parts move to an open instruction set and add a second radio band, placing both common Wi-Fi bands on an inexpensive chip.[597] The naming is hazardous because parts sharing the base name may differ only by suffix while using completely different processor architectures, with the peripheral set rather than the core staying consistent across them.[554] The occupied gap is a market position as much as a capability: the earlier single-core part was judged too simple to serve as a standalone connected microcontroller, while the dual-core successor overshot in the other direction.[467]

## Modules, board design, and electrical limits

Most designs buy a module rather than a bare chip: under the metal can the processor is soldered to a tiny circuit board alongside a separate eight-pin package, while the working memory remains internal to the processor itself.[406] The reason to buy the assembly instead of the part is that the module carries radio certification with it.[406] That external storage is also the physical security weak point, because an attacker who disables every debug interface can still remove the shield, desolder the discrete storage part, and read it.[698]

Module footprint drawings share a general datasheet problem: they are rarely dimensioned from the centre of the part and instead show pad-to-pad spacing plus a central thermal pad.[408] A bare module can be programmed with an ordinary serial adapter, with only reset and one boot-selection pin needing to be broken out.[330]

Electrical behaviour constrains use in battery and high-impedance designs. Idle current is the recurring reason not to use the part by itself; a design that must sleep for long periods is better served by pairing it with a small always-on microcontroller that wakes the larger part and cuts its supply rail again afterwards.[565] Start-up inrush is large enough to matter physically, and on a connection with appreciable path resistance the part will not come up unless the supply connection is doubled up.[689]

For buses and harsh supplies, the processor is only part of the design. The automotive-bus controller is on the chip, but an external transceiver is still required to drive the bus at its own voltage levels.[568] In that environment the supporting parts matter more than the processor: automotive high-side switches behave like transistors with added protection against transients, over-temperature, and over-current, and the power conversion must be automotive-grade because an ordinary converter on a vehicle supply is likely to fail eventually under transients on the 12 V line.[568]

## Peripherals and signal routing

A switching fabric between peripherals and pins lets functions be routed to whichever pins the layout wants, which is especially useful on a part with relatively few pins.[521] For audio, the part carries two channels of digital audio output at twenty-four bits and a sample rate beyond consumer requirements, enough to drive four channels individually from one device when external stereo parts are used.[338]

The same integration changes system partitioning: the part works well as the second processor driving a display while a conventional microcontroller handles real-time work.[521] Enough headroom also lets the operator interface collapse into the device, because serving the control page from the chip itself replaces the host-side sender application entirely.[438] That headroom moves preprocessing off the workstation as well; geometry that used to be worked out by a script beforehand can be broken down in real time while the machine runs.[438]

## Firmware practice

Porting existing firmware is mostly mechanical when both sides are written in the same language, and the move from eight to thirty-two bits is an opportunity to simplify arithmetic that existed only to work around narrower registers.[438] The productive order for such a port is outside-in: enumerate the peripherals the code needs, prove each one works on the new part, and only then place the application logic on top.[438] Integrated radios also remove equipment from the workflow rather than merely adding features, because the previous processor needed extra modules bolted on for the same connectivity.[438]

For sensor work, firmware can be generated rather than written: a short declaration of the sensor type and the pins it is wired to produces the code.[621] A useful pattern for existing wireless sensors is a bridge that receives packets on an unlicensed sub-gigahertz band and republishes them onto the network.[621] Common long-range boards pair this processor with a separate spread-spectrum radio chip, using the processor’s short-range radio link to a phone application while the other radio does the long-distance work.[677] The historical obstacle to those radios was firmware rather than hardware: point-to-point libraries existed, and anything beyond that was bespoke until a community project supplied a common stack across many boards.[677]

The part also appears as a bolt-on rather than the main processor, with a module running command-mode firmware adding Wi-Fi to a design whose main processor comes from a vendor with no wireless part of its own.[659] During component shortages it became a substitute for parts it was never meant to replace, including use as a USB-to-serial bridge when dedicated bridge chips were unobtainable.[587] That substitution makes more sense when the board already carries one for another purpose, because the same part can absorb the extra function and the increased volume works in the design’s favour.[587]

## Security model and failure modes

Flash encryption is available in the vendor software kit but is not the default, and a product that skips it stores private keys in plain readable form.[698] A worse lifecycle failure is failing to rotate those keys: in one device they survived a factory reset and transfer to a different account, leaving the credential bound to the hardware rather than to the owner.[698] In that case the identity itself was a key-and-certificate pair doing mutual authentication against the cloud service, tied to the serial number of the individual unit.[698] The stronger arrangement is secure boot to prevent modified firmware from loading, plus a separate security part holding the cryptographic keys used to encrypt storage.[698]

A dedicated secure element earns its place through physical measures a general-purpose part does not have, including a mesh laid over the die that defeats imaging and physical probing in addition to logical protections.[656] Getting code to run remotely on a microcontroller is substantially harder than on a device running a full operating system, and that difficulty is the main barrier between a vulnerability and a compromise.[698] If that barrier is crossed, the device becomes a foothold, because anything properly joined to the home network can be used to reach other devices on it.[698]

Only five or six processor families account for the overwhelming majority of connected consumer devices, concentrating both tooling and attack surface.[657] Choosing deliberately obscure parts is security through obscurity and does not survive contact with a determined attacker.[657] Credential provisioning has the same shape: handing Wi-Fi credentials to a device is easier over the short-range radio, where a phone application connects, negotiates, and passes the credentials across, but the underlying problem may not be solvable in the wireless standard because most proposed fixes open a security hole of their own.[422]

Field updates need both halves of the mechanism: the part provides a bootloader capable of over-the-air replacement, and the software above it must receive a new image while running the old one and swap between them.[422]

## Selection, economics, and simulation

The economic change is that two cores, both radios, and a large peripheral set arrive inside a certified module for a few dollars.[422] A completed module at roughly that price is why the part appears even where the radio is never switched on: the processing is simply cheaper than the alternatives.[403] A working consultancy partition is to use this family when the application needs Wi-Fi, a different vendor’s part when it needs low-energy Bluetooth, and a general-purpose 32-bit family for everything else.[645] The discipline that keeps that from becoming laziness is staying deliberately uncommitted, because selecting a part for familiarity rather than fit is the failure being guarded against.[645]

The visible symptom of that failure is a sixty-to-hundred-dollar embedded computer used where a four-dollar microcontroller would do, in a design that uses none of the interfaces the expensive part exists to provide.[645] The reasoning has a floor as well: dropping from a five-dollar part to a fifty-cent part is not worth a year spent learning an unfamiliar platform, because at realistic volumes development cost exceeds the material saving.[645] Having working example code already in hand is a legitimate selection criterion in its own right rather than a shortcut to apologise for.[702] The counterweight is knowing what the part is not for: a design that must be genuinely dependable, or that needs serious processing headroom, is the case for paying properly rather than reaching for the cheap option.[403] There is also a real cost of entry for engineers who work close to the hardware, because the software kit is large and the dual-core arrangement complicates low-level code.[403]

Simulating the part is a large step up from simulating an eight-bit microcontroller because it has thirty-two bits, two cores, and a much larger instruction set.[599] Rewriting a simulator core from a scripting language into a compiled web format produced no speed gain, because the runtime’s just-in-time compiler had already optimised the handful of functions the simulation runs repeatedly.[599] The distinction is workload shape: a long-running loop pays the translation cost once in the first few hundred milliseconds, whereas code that runs briefly and exits pays it every time.[599] Running the network gateway locally rather than on a remote server puts a simulated device on the user’s own network, so a browser can reach a server running inside the simulation.[599]

## References

| Episode | Title | URL | Date |
|---:|---|---|---|
| 330 | An Interview with Zach Fredin | https://theamphour.com/330-an-interview-with-zach-fredin/ | January 4, 2017 |
| 338 | An Interview with Jørgen Jakobsen | https://theamphour.com/338-an-interview-with-jorgen-jakobsen/ | March 5, 2017 |
| 359 | An Interview with Jeroen Domburg (Sprite_tm) | https://theamphour.com/359-an-interview-with-jeroen-domburg-sprite_tm/ | September 11, 2017 |
| 403 | An Interview with Mike Szczys | https://theamphour.com/403-an-interview-with-mike-szczys/ | August 12, 2018 |
| 406 | Nerds In A Corner | https://theamphour.com/406-nerds-in-a-corner/ | September 9, 2018 |
| 408 | Tronnort Software Rises Again! | https://theamphour.com/408-tronnort-software-rises-again/ | September 23, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 438 | An Interview with Bart Dring | https://theamphour.com/438-an-interview-with-bart-dring/ | April 14, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 500 | Two and a Half Orders of Magnitude | https://theamphour.com/500-two-and-a-half-orders-of-magnitude/ | July 12, 2020 |
| 521 | Outdoor Laser Projection & Object Mapping with Daryl Tewksbury | https://theamphour.com/521-outdoor-laser-projection-object-mapping-with-daryl-tewksbury/ | December 13, 2020 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 565 | Here for a reason | https://theamphour.com/565-here-for-a-reason/ | November 7, 2021 |
| 568 | YouTube to Consulting with Florin of Voltlog | https://theamphour.com/568-youtube-to-consulting-with-florin-of-voltlog/ | November 28, 2021 |
| 587 | Biblical Broker Bucks | https://theamphour.com/587-biblical-broker-bucks/ | May 1, 2022 |
| 597 | Wow, Dave REALLY likes Top Gun | https://theamphour.com/597-wow-dave-really-likes-top-gun/ | July 24, 2022 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 615 | Augmented Engineering | https://theamphour.com/615-augmented-engineering/ | January 16, 2023 |
| 621 | The Magic of Calipers | https://theamphour.com/621-the-magic-of-calipers/ | February 26, 2023 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 656 | Pneumatic Tubes, Straight To The Home | https://theamphour.com/656-pneumatic-tubes-straight-to-the-home/ | January 22, 2024 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
| 659 | Altium...Acquired! | https://theamphour.com/659-altium-acquired/ | February 20, 2024 |
| 677 | Watt Is The Deal | https://theamphour.com/677-watt-is-the-deal/ | September 23, 2024 |
| 689 | A Jumperless Breadboard with Kevin Cappuccio | https://theamphour.com/689-a-jumperless-breadboard-with-kevin-cappuccio/ | February 26, 2025 |
| 698 | Hardware Security with Matt Brown | https://theamphour.com/698-hardware-security-with-matt-brown/ | July 17, 2025 |
| 702 | Test Point Accupuncture | https://theamphour.com/702-test-point-accupuncture/ | September 14, 2025 |
