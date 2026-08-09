---
title: Firmware Update
concept: firmware-update
generated: 2026-08-08
model: k3
spec: knowledge-only-v4-cluster
---

A **firmware update** is the replacement of the program stored in a device's non-volatile memory with a new image, performed after manufacture and typically in the field. The standard mechanism is a bootloader, a small program resident in flash that runs first at power-up, checks the application image for validity, and transfers execution to it if the image is good.[212] Updating requires a path for the application to re-enter the bootloader, after which the new image is received over whatever communication channel is available; any interface capable of getting data into the chip will serve, including CAN, USB, and a plain UART.[212] The capability matters in both directions: a device that cannot be updated is a permanent vulnerability, while the ability to update a device remotely is itself a vulnerability, so both the presence and the absence of the capability carry security cost.[561]

## Mechanisms

### Bootloaders

The bootloader is the foundation of field updating. It runs before the application on every boot, validates the application image, and hands over execution only if the image passes its checks.[212] A design invariant worth engineering towards is that no update can leave the device in a state where it cannot be connected to and reprogrammed, which takes deliberate work to guarantee.[226] One embedded Linux image built with a distribution builder was given a power-on self test and an automatic fall-back to the previous image, so that an update interrupted by loss of power does not brick the device.[614]

Where a vendor's update path is itself defective, the path may be abandoned entirely: one team, after finding a vulnerability in the read-only memory routine provided to handle updates, wrote their own bootloader, taking on flash partitioning for robust image updates and the versioning scheme along with it.[590]

### Wired and removable-media updating

Device firmware upgrade, usually abbreviated DFU, is a standard USB mechanism for uploading a new image, entered by holding a button at power-up and intended to make replacement possible with minimal risk of needing a hardware debug adapter to recover.[467] Pairing that low-level mechanism with a mass-storage presentation, so the device appears as a small USB drive for ordinary files, covers both the risky update path and everyday file transfer with standardised protocols.[467] The same standardised approach lets a programmable-logic bitstream and the soft-processor application running alongside it both be replaced in the field.[467] Presenting a device as a standard human-interface and storage class gives driverless updating, so a user drops a file onto the device rather than installing tooling.[453] An update can also be delivered through a web browser over a serial connection, using the bootloader's own transport protocol, removing the need for a separate command-line tool or vendor desktop application.[724]

Booting the whole firmware from a removable card removes the bricking risk entirely, because a bad image can be replaced by swapping the card.[325] With a card-based update path every firmware defect is recoverable in the field, with the single exception of a defect inside the bootloader itself.[370] Loading an update from a card also avoids requiring the user to have a serial interface, which is how most instruments that support updating at all do it.[364]

A controller chip already in a design for another purpose can carry the update path: remote debugging of the main processor and firmware updating were both routed over an isolated serial interface through a USB power-delivery controller.[449] Writing update code against a published protocol rather than a specific vendor's part means the controller can in principle be substituted with any compliant device years later without changing the code.[449]

### Wireless and over-the-air updating

A wireless update flow on a small microcontroller works by having the running application listen for an upgrade command, receive the compiled image wirelessly, store it in an external flash chip, and reboot; on the next boot the bootloader detects the new image, erases the old application, writes the new one, and jumps to it.[398] A similar arrangement was built by expanding the bootloader region of a part chosen for having more space, deriving the bootloader from an existing open-source one, and adding an external SPI flash the bootloader can also boot from, with the application downloading an Intel hex file into that flash.[250] Verifying the image before committing it protects against a corrupted transfer but not against a valid image that is wrong: a bad file published with a matching checksum still passes, a residual risk that is accepted rather than solved.[250]

An over-the-air update on a Bluetooth part is arranged with a bootloader alongside the vendor's radio stack, so that a phone application can load a new image and the enclosure never has to be opened.[510] The wireless route is not free: a bootloader chain and the space to hold a second image consume substantially more of the device's storage.[516] One instrument used a card-based path rather than wireless updating because implementing the wireless route was assessed as a great deal of work and updates were infrequent enough that removing a battery cover to reach the card was acceptable; the contrary judgement is that wireless updating is worth the effort even where a card slot exists, because sending someone firmware becomes a matter of opening an application and uploading it rather than shipping media.[364][516] Firmware updates are not performed over satellite links because the cost in both power and data is prohibitive, and are done over cellular where coverage allows.[614]

## Vehicles

The update mechanism exists in vehicles because the modules are not physically accessible: a microcontroller distributed through a car cannot be removed, opened, and reprogrammed through its debug header when a defect is found.[212] In a car, one module downloads the update and distributes it over the internal bus to whichever module is listening, across what are typically several buses.[662] Every microcontroller in a modern connected vehicle can be updated over the air and routinely is, which forces per-module version tracking across the whole vehicle.[518]

The financial contrast between recall and remote update is stark: one vulnerability required recalling roughly two and a half million vehicles, while another manufacturer pushed an over-the-air fix to every affected car before the vulnerability was even disclosed publicly.[265]

## Deployment at fleet scale

Updating a thousand devices and updating a million are different problems, and the difference is what makes staged rollout necessary rather than optional.[363] Remote updates must be staged rather than broadcast: a proportion of a tenth of a percent of the fleet is seeded first, then one percent, then ten, because a bad image cannot be recalled once it has gone to everyone.[363] The image programmed at the factory is flashed three to four months before the product reaches a customer, so what must be guaranteed is that it boots, reaches the backend, and updates itself to the current release on day zero.[363] Production programming and field updating are separate stages: a bootstrap image loaded at the factory runs a power-on self test that a production operator can act on without further knowledge, after which the device connects to a server and pulls the current firmware.[692]

Fleet management platforms show which of the deployed units are active and which firmware revision each carries, and manage the migration between revisions as well as delivering the images.[310] Doing that in-house requires two distinct competencies: hooks in the firmware capable of replacing the running image, and a cloud component to serve and track it, the latter being a separate discipline from embedded work.[422] Fleet software is not only about the image: it also has to report status and confirm devices are alive while they sleep, and carry small amounts of data.[422] A platform vendor's operating system absorbs that overhead, handling the transfer, checksum verification, and swap so a developer changes code and clicks a button, which is a substantial amount of firmware work to have done for you; the dependency is visible when the vendor stops, since customers whose devices ran on such a platform keep working but stop receiving updates and must take over development themselves.[477] A hosted update service also solves distributed development: a collaborator elsewhere presses reset, the device calls home, and fetches the version the other engineer uploaded, without needing the full development environment locally.[435]

Building the over-the-air update capability first is a development strategy rather than a shipping feature: it lets alpha units be distributed to testers who then receive every subsequent build, replacing a cycle in which each unit was physically posted back to be reflashed.[363] Self-programming parts allow a large deployed population to be updated at once: two thousand microcontrollers in an installation were reprogrammed in about two seconds.[135] At fleet scale, the practical obstacle to patching can be locating the units at all, even where the will and mechanism exist.[561]

## Failure modes and recovery

A poorly designed update procedure bricks devices outright, leaving the unit stuck at power-up with no recovery path short of an external programmer.[152] A defective update pushed to a fleet of home devices bricked a large number of them at once, the fleet-scale form of the same failure.[269] The update mechanism is itself the thing most likely to break and the hardest to recover: without regression testing, a change that made an image slightly larger altered the image layout, broke the device firmware update path, and bricked units in the field.[537] Where the product is sealed, losing the update path is terminal rather than inconvenient: recovering the device means drilling into it, and for an encased consumer product the unit is simply written off.[537] In the absence of automated regression testing, the compensating practice was extensive manual exercise of the device before every push, with the update mechanism the item watched most closely.[537] Even a change unrelated to a feature can break it: an adjustment to a message parser stopped notifications arriving although the modified code path was not the one involved.[537]

Automated validation of a new image can only confirm the tests that were written for it, so an image can pass every check and still be broken in a way nothing looked for; this is the standing nightmare scenario for automatic updating.[590] Rollback policy is a design decision with no clean answer: permitting a return to an older image reintroduces that version's defects, while allowing only forward movement fixes some defects and may introduce others.[590] A recurring self-inflicted debugging failure is spending a day chasing a defect while repeatedly loading the old image and never actually applying the update.[479] The update feature is also a common casualty of a processor that turns out to be too small: on one programme, at the third physical prototype, the manufacturer reported that everything would not fit and proposed dropping firmware updating.[296] A working device with a broken update path is nonetheless routinely presented as complete, with the missing capability described as a detail.[329]

## Security

The update mechanism is an attack surface. Access to a vehicle's internal bus, for example through an attached wireless device, makes it possible to reprogram parts of the car.[212] Vehicle internal networks are effectively open, or partitioned into a few weakly isolated open networks, so control of one device on the bus generally extends to control of many.[265] The over-the-air path that lets a manufacturer fix a fleet is a route for an attacker as well.[265] Intercepting an update in transit gives an attacker a trusted device inside an otherwise private network, from which further attacks can be launched.[211] The security requirement on a remote update path is that nobody else can perform the update on the manufacturer's behalf.[363]

The update system can be where the vulnerability lives: one defect was found in the read-only memory routine provided to handle updates, raising the question of what to do when the updating mechanism itself is broken.[590] Firmware is now recognised as part of the software supply chain and as a vector in its own right, so every part of a system has to be considered for what could be done maliciously through it.[590] Peripherals and cables carry updatable microcontrollers: a USB-C to VGA adapter was found to expose direct firmware update, allowing its firmware to be read out and replaced, and any cable doing more than basic USB contains a microcontroller.[346] Forcing a device into firmware update mode is a recognised attack step, used to move sensitive memory contents into a readable state; in one device the critical values were copied into RAM at power-up on the assumption that the chip's security would prevent RAM being read.[575]

The recommended structure for devices under certification regimes is a certified bootloader that can be locked down and uses sound cryptography to prevent malicious images being accepted, followed by regular tested updates on a schedule.[318] Server firmware is updated far less often than would be desirable, and in practice the major updates appear only after a catastrophic defect.[590] The difficulty of upgrading connected consumer products is what makes any vulnerability in them durable.[308]

### Open and third-party firmware

Most hardware never receives a firmware update after sale, because the manufacturer's involvement ends when the unit ships.[463] Understanding a vendor's firmware update file format is what makes third-party firmware possible, and documentation of that format for one product line was extended to a related one.[463] Open firmware changes the calculus in three ways: vulnerabilities are found and patched by a far larger community than the few dozen people at a firmware vendor, owners can patch on their own schedule, and a community can continue supporting hardware its manufacturer has abandoned.[463] The same option exists at consumer scale: an off-the-shelf device can be opened and reflashed with community firmware that its owner can then update as often as they choose, where the vendor's own product may never be updated.[657]

## Design and development practice

How a device will be programmed — at the factory, by a technician, over the air from a cloud service, or over the air from a phone — has to be decided early, because the firmware architecture, the security model for getting an image onto the device, and the backend that serves it all follow from that choice.[526] Deferring that decision is what makes it unrecoverable: omitting something as small as the button that puts the device into update mode cannot be corrected once the hardware exists.[526]

Memory budget determines whether a product can be updated at all: halving the available flash may remove the space needed to hold a second image, which eliminates the update capability and with it a product function.[551] That constraint argues for fitting the larger memory part from the outset, because a shipped unit cannot be changed and early customers would otherwise be excluded from firmware that needs more space than their device has; cost reduction and update capability pull against each other, and the sequence that works is to get the product working and shipped before attempting to cost down.[468] The number of processors in a product is limited in practice by the difficulty of delivering firmware updates to all of them.[249] Updating firmware on a spacecraft is a high-risk operation, which is part of the appeal of running an interpreted language on a stable core: functionality is changed by uploading a file for the interpreter to run rather than by reflashing the firmware itself.[323]

Longevity can be designed for by dividing the product: the parts physically fixed in place are specified to last, while the parts that must stay current are made field-serviceable so they can be swapped rather than updated indefinitely.[487] Where the whole software stack is certified, as in medical devices, firmware updates cannot be shipped without recertification, which makes that update cycle unviable for security maintenance.[318] Instruments whose readings carry safety consequences restrict updating: one meter's firmware can be updated only by dealers holding the programmer, on the reasoning that a reprogrammed meter reporting zero on a live circuit could kill its user.[680]

## Product completeness and engineering discipline

Products increasingly ship unfinished on the assumption that the update will complete them, which is why an out-of-the-box update is often required before a device does anything useful.[256] Treating that as normal is argued to be the harmful direction, since it licenses shipping poor products on the reasoning that firmware will fix them later.[256] The cost of easy updating is discipline: when a defect can be fixed by sending another update, the incentive to test thoroughly before release erodes, and the burden shifts to the customer who must keep updating.[363] A device requiring an update every couple of days indicates that testing was skipped, and there is a hard boundary on what firmware can repair: a wrong resistor value is not fixable in software.[537] The ability to push an update later produces a materially different engineering mindset from custom silicon, where a spin can cost millions of dollars and there is no field fix.[619]

## Economic and commercial significance

Firmware updates are used to unlock capability the hardware already had: a spectrum analyser's resolution bandwidth improved from ten hertz to one hertz through an update alone.[368] The same pattern appears as a paid upgrade: a video product's higher model differed from the cheaper one by a firmware upgrade costing several hundred dollars, roughly a third of the product price, with the hardware likely identical.[532] An update can also add an entirely new function to a shipped product, such as a handheld recorder gaining the ability to operate as a USB microphone.[296] A capability delivered as a firmware update rather than a hardware change is far easier for a customer to adopt, because nothing about their existing hardware has to change and the software can simply be removed if it does not work out.[728] A module vendor that publishes each new firmware release at no additional cost and makes upgrading straightforward removes the risk of being dependent on the manufacturer or having to buy a new part to get a fix.[155]

In infrastructure the return can be measured directly: updating the firmware of data-centre power supplies to switch more efficiently converts a fraction of a percent of efficiency into significant money across thousands of machines.[212] Putting a processor into a previously analogue product buys the ability to push fixes: control-loop constants that once required sending an engineer to solder resistors are changed through a menu, and a software mitigation can hold a customer's process running until a hardware fix is exchanged.[522] A telecommunications standard was deployed faster than its competitor because operators needed only to update the firmware of existing infrastructure, whereas the alternative required capital investment in new equipment.[509] Reconfigurable logic placed in servers for future use can be reprogrammed remotely to add hardware acceleration, with speed-ups reported from ten to a thousand times; the corresponding risk is that a faulty configuration pushed to a hundred thousand machines takes them all down.[317]

A firmware update can reveal the true cause of a hardware problem: a battery failure attributed publicly to mechanical design was mitigated by an update limiting charging to sixty percent of capacity, which is not a plausible remedy for a mechanical fault.[315] Whether a connected device continues to receive updates, rather than its power consumption, is what determines its useful life.[561]

## Regulation and ownership

European regulation now requires that a device carrying the conformity mark and having a programming port be updatable, with a stated commitment to supply updates and respond to disclosed critical vulnerabilities; devices using one-time-programmable memory fall outside it.[720] The objection to mandating updatability is that adding a programming path adds an attack vector, so the requirement trades one class of risk for another.[720] Whether a purchased device is genuinely owned is put in question by mandatory updates that can change its permitted behaviour, such as revising the geographic restrictions on where an aircraft may be flown.[538]

## Instrument firmware history

Most instruments historically used one-time-programmable parts, so the unit bought was the unit kept, and moving to a flash-based microcontroller was what made bug-fix updates possible at all.[619] Where updating exists but is not exposed to users, it is performed at the factory through an internal header or a bed-of-nails fixture, with the consequence that two units of the same model bought at different times probably carry different firmware.[554]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 135 | An Interview with Mike Harrison - X-ray Examining Xenogogue | https://theamphour.com/the-amp-hour-135-x-ray-examining-xenogogue/ | March 4, 2013 |
| 152 | Firmware, Netburner and Semiconductors - Chris's Capitalism Colloquy | https://theamphour.com/the-amp-hour-152-chriss-capitalism-colloquy/ | July 1, 2013 |
| 155 | An Interview with Jeff Rowberg - Mini Module Master | https://theamphour.com/the-amp-hour-155-mini-module-master/ | July 22, 2013 |
| 211 | Design Reviews Are Important - Habitual Hype Hebetude | https://theamphour.com/211-design-reviews-are-important-habitual-hype-hebetude/ | August 11, 2014 |
| 212 | An Interview with Trey German - Launchpad Laden Lodesman | https://theamphour.com/212-an-interview-with-trey-german-launchpad-laden-lodesman/ | August 18, 2014 |
| 226 | An Interview with Colin Karpfinger - Blendling Bean Brio | https://theamphour.com/226-an-interview-with-colin-karpfinger-blendling-bean-brio/ | December 2, 2014 |
| 249 | Wearables Might Have Limited Fashion Options - Lachrymogenic Lane Language | https://theamphour.com/249-wearables-might-have-limited-fashion-options-lachrymogenic-lane-language/ | May 12, 2015 |
| 250 | An Interview with Vic Aprea - Federated Firmware Functionalism | https://theamphour.com/250-an-interview-with-vic-aprea-federated-firmware-functionalism/ | May 20, 2015 |
| 256 | Is This A Show? | https://theamphour.com/256-is-this-a-show/ | July 1, 2015 |
| 265 | A Security Update with Michael Ossmann | https://theamphour.com/265-a-security-update-with-michael-ossmann/ | September 2, 2015 |
| 269 | Be Tidy | https://theamphour.com/269-be-tidy/ | September 30, 2015 |
| 296 | Gotta Update My Dog | https://theamphour.com/296-gotta-update-my-dog/ | April 27, 2016 |
| 308 | An Interview with Samy Kamkar | https://theamphour.com/308-an-interview-with-samy-kamkar/ | July 20, 2016 |
| 310 | Mergers and Acquiescence | https://theamphour.com/310-mergers-and-acquiescence/ | August 3, 2016 |
| 315 | Mashuppery (with MEP) | https://theamphour.com/315-mashuppery-with-mep/ |  |
| 317 | A Decoupled Episode | https://theamphour.com/317-a-decoupled-episode/ | September 28, 2016 |
| 318 | Impedance Matching with Michael Ossmann and Dmitry Nedospazov | https://theamphour.com/318-impedance-matching-with-michael-ossmann-and-dmitry-nedospasov/ | October 5, 2016 |
| 323 | An Interview with Tony DiCola | https://theamphour.com/323-an-interview-with-tony-dicola/ | November 16, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 329 | Work on it for 10 years... | https://theamphour.com/329-work-on-it-for-10-years/ |  |
| 346 | An Interview with Joe FitzPatrick | https://theamphour.com/346-an-interview-with-joe-fitzpatrick/ | June 4, 2017 |
| 363 | An interview with Alvaro and Jen from the URE Podcast | https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/ | October 15, 2017 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 368 | The EEVblog Sparkgap Generator | https://theamphour.com/368-the-eevblog-sparkgap-generator/ | November 19, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 398 | An Interview with Felix Rusu | https://theamphour.com/398-an-interview-with-felix-rusu/ | July 9, 2018 |
| 422 | Stick 'Em On Whales | https://theamphour.com/422-stick-em-on-whales/ | December 27, 2018 |
| 435 | An Interview with Andreas Spiess | https://theamphour.com/435-an-interview-with-andreas-spiess/ | March 24, 2019 |
| 449 | Pulled From A Working Environment | https://theamphour.com/449-pulled-from-a-working-environment/ | June 30, 2019 |
| 453 | Vertically Integrated Design Engineering | https://theamphour.com/453-vertically-integrated-design-engineering/ | August 4, 2019 |
| 463 | An Interview with Trammell Hudson | https://theamphour.com/463-an-interview-with-trammell-hudson/ | October 20, 2019 |
| 467 | Stories from Supercon 2019 | https://theamphour.com/467-stories-from-supercon-2019/ | November 18, 2019 |
| 468 | The Tiny Lab Movement | https://theamphour.com/468-the-tiny-lab-movement/ | November 24, 2019 |
| 477 | EcoWoke and Going Broke | https://theamphour.com/ecowoke-and-going-broke/ | February 2, 2020 |
| 479 | Why isn't this working? | https://theamphour.com/479-why-isnt-this-working/ | February 13, 2020 |
| 487 | An Interview with Kerry Scharfglass | https://theamphour.com/487-an-interview-with-kerry-scharfglass/ | April 5, 2020 |
| 509 | Cellular IoT with Jared Wolff | https://theamphour.com/509-cellular-iot-with-jared-wolff/ | September 20, 2020 |
| 510 | Knob and Tube Wiring | https://theamphour.com/510-knob-and-tube-wiring/ | September 28, 2020 |
| 516 | Thermions Aren't A Thing | https://theamphour.com/516-thermions-arent-a-thing/ | November 8, 2020 |
| 518 | Satellites and EVs with Joris Aerts | https://theamphour.com/518-satellites-and-evs-with-joris-aerts/ | November 22, 2020 |
| 522 | High Current Power Supplies with Fredrik Kensander | https://theamphour.com/522-high-power-supplies-with-fredrik-kensander/ | December 20, 2020 |
| 526 | Why IoT Is Difficult with Jonathan Beri | https://theamphour.com/526-why-iot-is-difficult-with-jonathan-beri/ | January 18, 2021 |
| 532 | Recalling Recalls | https://theamphour.com/532-recalling-recalls/ | February 28, 2021 |
| 537 | Firmware Deployment and Troubleshooting with Akbar Dhanaliwala | https://theamphour.com/537-firmware-deployment-and-troubleshooting-with-akbar-dhanaliwala/ | April 5, 2021 |
| 538 | Missle Man with Bruce Simson | https://theamphour.com/538-missle-man-with-bruce-simson/ | April 12, 2021 |
| 551 | Feed the Mouse | https://theamphour.com/551-feed-the-mouse/ | July 25, 2021 |
| 554 | PLEASE be a die shrink | https://theamphour.com/554-please-be-a-die-shrink/ | August 15, 2021 |
| 561 | Assembly Chat | https://theamphour.com/561-assembly-chat/ | October 10, 2021 |
| 575 | New Life Skills with Joe Grand | https://theamphour.com/575-new-life-skills-with-joe-grand/ | January 30, 2022 |
| 590 | Finding Hardware Flaws with Laura Abbott | https://theamphour.com/590-finding-hardware-flaws-with-laura-abbott/ | May 22, 2022 |
| 614 | Reunion Impedance Matching and 2023 Predictions | https://theamphour.com/614-reunion-impedance-matching-and-2023-predictions/ | January 8, 2023 |
| 619 | Super Tecmo Bug | https://theamphour.com/619-super-tecmo-bug/ | February 13, 2023 |
| 657 | Automating the Home with Keith Burzinski | https://theamphour.com/657-automating-the-home-with-keith-burzinski/ | February 5, 2024 |
| 662 | The non-Stinky Car | https://theamphour.com/662-the-non-stinky-car/ | March 20, 2024 |
| 680 | Catching Rockets with Musk Sticks | https://theamphour.com/680-catching-rockets-with-musk-sticks/ | October 15, 2024 |
| 692 | Like a steam engine in your house | https://theamphour.com/692-like-a-steam-engine-in-your-house/ | April 15, 2025 |
| 720 | Hyper Growth and OpenClaw Interns | https://theamphour.com/720-hyper-growth-and-openclaw-interns/ | March 31, 2026 |
| 724 | All Heat, No Useful Work | https://theamphour.com/724-all-heat-no-useful-work/ | May 25, 2026 |
| 728 | Space Age Bluetooth with Alex Haro | https://theamphour.com/728-space-age-bluetooth-with-alex-haro/ | July 9, 2026 |
