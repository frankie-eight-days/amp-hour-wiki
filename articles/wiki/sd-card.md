---
title: SD Card
concept: sd-card
generated: 2026-08-09
model: opus
spec: knowledge-only-v4-cluster
---

An SD card is a removable flash storage device that presents itself to a host as a managed block device rather than as raw flash: a controller inside the card performs wear levelling and block remapping that the host cannot see or schedule.[356] Because the card can be driven over a four-wire SPI link available on essentially every microcontroller, attaching mass storage to an embedded design is inexpensive in both parts and engineering effort, which is why cards appear as data loggers' media, as firmware distribution media, and as the boot device of small Linux systems.[187][514][515] The same removability and the same hidden controller behaviour are also the source of the card's characteristic problems: unbounded write latency, silent write failure, and an aperture through the product enclosure.[218][244][356]

## Host interface

An SD card can be driven over SPI, which lets a filesystem layer sit directly on top of a generic SPI driver rather than on a dedicated card controller; the hardware abstraction beneath the filesystem is then just the SPI peripheral and its pin assignment.[514] SPI mode needs only four pins and is supported by essentially every microcontroller, which makes it the portable way to attach a card, at the cost of forgoing the wider and faster native SD bus.[514] Because the attachment is this cheap, the presence of file storage in a product specification is not on its own a reason to move up from a microcontroller to a larger operating system.[187]

The card-reader and FAT components pulled into a bare real-time operating system are nominally free but are unvetted and may require porting to the target, whereas the same function taken from a vendor-backed hardware abstraction layer arrives already exercised across multiple silicon families.[514]

## Timing behaviour

The card's internal housekeeping makes the duration of an individual write non-deterministic from the host's point of view.[356] The interface can stall for far longer than a normal transfer would take; pauses on the order of 200 milliseconds have been observed while a card performs its own management work.[356] A FAT filesystem layered on top adds further latency spikes, because updating a file also forces a rewrite of the allocation table.[356]

The consequence for system architecture is that a logging task writing to a card cannot be run cooperatively alongside time-critical control code. It must be preemptible, so that higher-priority work such as actuator control still meets its deadlines.[356] The same reasoning applies to streaming: sending a long job to a machine over a host link risks buffer underruns that corrupt the output, whereas running the job from a card already in the machine removes the host link from the real-time path.[94] Putting a micro SD card on a motion-control module similarly decouples program size from the controller's RAM and from the reliability of the streaming link, since the job is uploaded once over the network onto the card and then executed locally.[438]

## Data integrity

Modifying a card's contents from a desktop computer — deleting, renaming or adding files — can leave the embedded device that owns the card unable to write to it again, because the device depends on the on-card structures being exactly as it left them.[244] The resulting failure is silent and intermittent: the device continues to display every indication of normal operation while nothing is committed to the card, so the loss is discovered only when the card is next read.[244]

Data written to a card is therefore not known to exist until it has been read back, on the same principle by which an unrestored backup is not a backup.[244] Read-back verification is nonetheless routinely skipped because modern flash almost never fails visibly, which is precisely what makes the rare failure expensive when it does occur.[244][563]

Removing power from a running system whose root filesystem is on a card can corrupt that filesystem, although how often this is seen in the field varies sharply between practitioners, making it a risk to design against rather than a certainty.[645] A card-based firmware update path should accordingly be validated destructively, by pulling the card out part-way through an update and confirming that the device still boots, rather than by assuming the write completes.[377]

## Reliability and grade

Consumer cards are judged insufficiently reliable for equipment left running unattended; industrial-grade cards are a genuine step up, but for industrial environments the storage is more often moved onto the board itself.[563] Compute modules reflect this split directly: a Lite variant omits on-board managed flash entirely, so the carrier board must provide an external card socket, while the non-Lite variants carry soldered flash instead.[563] Experience of shipping a card-booted embedded Linux consumer product, in which cards died in the field and an operating system and software stack had to be maintained, leads to a preference for a microcontroller with a wireless module on projects that do not genuinely need Linux.[189]

## Firmware distribution and booting

Where a product already has a card slot, distributing firmware as a file on the card is chosen over a wireless update path because the wireless route requires building an update stack that does not otherwise exist.[364] The economics rest on vendor-supplied code: a silicon vendor that already ships both a card-reading library and a firmware bootloader turns the update mechanism into integration rather than development.[364] A manual update requiring the user to open a battery cover and remove the card is an acceptable burden for a product whose firmware is revised rarely, so update ergonomics should be weighted by expected update frequency.[364]

Loading application firmware from a card makes every application-level defect field-recoverable, confining the residual unrecoverable risks to the bootloader itself and to the hardware.[370] Booting from a removable card likewise means a bad image is repaired by rewriting the card rather than by returning the unit, which makes it considerably less risky to ship early hardware with immature software.[325] An application processor with a mature boot ROM and build-system support can bring up Linux from a card with no on-board storage at all, which is why boot-media and build-system support matter as much as the silicon when such a part is selected.[515]

### Imaging and provisioning

Small-batch provisioning of card-booted devices is done by cloning one prepared card image to every unit and then applying only the per-unit configuration, such as a channel assignment, afterwards.[319] Handing out prepared images with a fixed single-board computer target likewise removes the first hours of a hands-on course, which otherwise go on reconciling drivers and tool installations across each attendee's own laptop.[242] Card-imaging tooling has converged on cross-platform writers, replacing the earlier situation in which the procedure for writing a boot image differed between Windows, Linux and macOS.[378]

Boards designed around a keyboard-and-monitor first boot must have their headless configuration written into the card image before first power-up; discovering the requirement afterwards means re-imaging the card repeatedly.[515]

## Mechanical and enclosure constraints

A user-accessible card slot punches an opening through the enclosure and therefore through the isolation barrier, which is why an exposed slot is difficult to reconcile with high-voltage safety qualification on measurement instruments.[218] Calculated isolation margin is not the same as tested margin: one design that had margin on paper withstood only two and a half seconds of a required five-second high-voltage exposure after the degradation caused by earlier tests in the sequence, and its user-accessible slot was sealed as a result.[218] The qualification sequence preconditions the disassembled unit at 93 percent relative humidity for 48 hours, reassembles it, wraps it in foil and applies a 5,400 volt stress, so any aperture in the enclosure is judged after the insulation has absorbed moisture rather than when dry.[218]

A rugged battery-powered logger can instead keep the card entirely inside the sealed enclosure and expose only a USB port for offload, avoiding both the ingress path of a user-accessible slot and the handling wear of repeated insertion.[473] Full-size sockets have in any case become the harder part to source as the market moved to micro form factors, so a design that wants the full-size outline must plan for connector availability.[681]

## Cards as components

The volume at which cards are manufactured can make a complete, controller-managed card cheaper than the bare flash die it contains, to the point that finished cards are reflowed directly onto product boards as the storage component.[690] Consumer products are also found using an ordinary card fixed permanently to the board with silicone rather than a socket, taking the card's cost advantage while removing the socket, its cost and its mechanical failure path.[690]

The card outline is large enough to serve as a carrier for a complete system-in-package. Earlier commercial wireless cards fitted into that outline were restricted in compute and closed to user code, whereas a system-in-package built into the same outline can run Linux and arbitrary firmware.[681]

## Applications

Logging instruments write to the card in plain FAT rather than a private format, so that the card can be pulled and read directly on any computer without a vendor tool.[690] Local card storage is also what allows speech recognition to run entirely offline on a small board: a four gigabyte card carries a two gigabyte pronunciation dictionary against which spoken sentences are decomposed into phonemes.[258] Cards further displace obsolete removable media in reimplementations of old systems, because the original drives and discs are both unreliable and hard to buy, and one card holds what previously required a shelf of media and minutes of load time.[47]

Two consequences follow from the card being an ordinary, readable filesystem. Holding a device's operating system on a removable card instead of in on-chip flash makes the entire firmware image trivially extractable by anyone who opens the case and reads the card.[646] And simulating a card faithfully means synthesising a real FAT image from the supplied files, because the firmware under simulation issues the same filesystem reads it would issue against physical media.[599]

## References

| Episode | Title | URL | Date |
|---|---|---|---|
| 47 | Apple HQ and Vintage Arcade Games - The Mothership Manifesto | https://theamphour.com/theamphour47-the-mothership-manifesto/ | June 15, 2011 |
| 94 | Gnomic Gazumping Gobemouche | https://theamphour.com/the-amp-hour-94-gnomic-gazumping-gobemouche/ | May 6, 2012 |
| 187 | An Interview with Elecia White - Wirewove Worshipping Wookieist? | https://theamphour.com/187-an-interview-with-elecia-white-wirewove-worshipping-wookieist/ | March 3, 2014 |
| 189 | An Interview with Marcus Schappi - Kit Ketch Kenophobia | https://theamphour.com/189-an-interview-with-marcus-schappi-kit-ketch-kenophobia/ | March 17, 2014 |
| 218 | An Interview with Eric VanWyk - Meiotic Mountenance Mooshimeter | https://theamphour.com/218-an-interview-with-eric-vanwyk-meiotic-mountenance-mooshimeter/ | September 29, 2014 |
| 242 | Can't We All Just Get Arduino? - Tardiloquent Trademark Tirade | https://theamphour.com/242-cant-we-all-just-get-arduino-tardiloquent-trademark-tirade/ | March 24, 2015 |
| 244 | The Art Of Staying Interested In Electronics - Exponible Electronics Ennui | https://theamphour.com/244-the-art-of-staying-interested-in-electronics-exponible-electronics-ennui/ | April 7, 2015 |
| 258 | An Interview with Bertrand Irrisou and Gerald Friedland of Audeme | https://theamphour.com/258-an-interview-with-bertrand-and-gerald-of-audeme/ | July 14, 2015 |
| 319 | Photon Rich, Cash Poor | https://theamphour.com/319-photon-rich-cash-poor/ | October 12, 2016 |
| 325 | An Interview with David Kronstein (Tesla500) | https://theamphour.com/the-amp-hour-325-an-interview-with-david-kronstein-tesla500/ | November 30, 2016 |
| 356 | An Interview with Piotr Esden-Tempski | https://theamphour.com/356-an-interview-with-piotr-esden-tempski/ | August 20, 2017 |
| 364 | The Endless Y2K | https://theamphour.com/364-the-endless-y2k/ | October 22, 2017 |
| 370 | Alternate Info Sources | https://theamphour.com/370-alternate-info-sources/ | December 3, 2017 |
| 377 | Debugger vs Printeffer | https://theamphour.com/377-debugger-vs-printeffer/ | January 28, 2018 |
| 378 | An Interview with Jason Kridner and Robert Nelson | https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/ | February 4, 2018 |
| 438 | An Interview with Bart Dring | https://theamphour.com/438-an-interview-with-bart-dring/ | April 14, 2019 |
| 473 | An Interview with Greg Davill | https://theamphour.com/473-an-interview-with-greg-davill/ | January 5, 2020 |
| 514 | Focus, Dammit | https://theamphour.com/514-focus-dammit/ | October 25, 2020 |
| 515 | Embedded Linux with Jay Carlson | https://theamphour.com/515-embedded-linux-with-jay-carlson/ | November 1, 2020 |
| 563 | Grumpy Collaboration | https://theamphour.com/563-grumpy-collaboration/ | October 24, 2021 |
| 599 | An Interview with Uri Shaked (Wokwi.com) | https://theamphour.com/599-an-interview-with-uri-shaked-wokwi-com/ | August 14, 2022 |
| 645 | Moving Down The Stack with Scott Williams | https://theamphour.com/645-moving-down-the-stack-with-scott-williams/ | September 4, 2023 |
| 646 | Fan Fanboys | https://theamphour.com/646-fan-fanboys/ | September 11, 2023 |
| 681 | Compact High Speed Design with Lukas Henkel | https://theamphour.com/681-compact-high-speed-design-with-lukas-henkel/ | October 30, 2024 |
| 690 | Clap on, clap off, lights flicker | https://theamphour.com/690-clap-on-clap-off-lights-flicker/ | March 11, 2025 |
