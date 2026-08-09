#!/usr/bin/env python3
"""Build the ethernet extraction packet by slicing quotes out of bundle passages."""
import json, sys

ROOT = "/Users/frankwalsh/Documents/vibecoding/amp_hour_wiki"
b = json.load(open(f"{ROOT}/articles/factory/bundles/ethernet.json"))
P = b["passages"]

# (passage_index, quote, speaker, depth_regraded, kind, claim_text)
SPEC = [
(1, "It didn't work out of the box, and he spent ages trying to get it working",
 "Dave Jones", "opinion", "practitioner-judgment",
 "Bringing an Ethernet interface up on an early single-board Linux computer was not a plug-and-play exercise: the port did not work out of the box and required extended work at the operating-system level before a link and stack were usable."),

(4, "gigabit Ethernet on ordinary category 5 plus UTP is a five-level signal",
 "Howard Johnson", "explains", "mechanism",
 "Higher data rates over an unchanged physical medium are obtained by adding levels to the transmitted signal rather than raising the symbol rate indefinitely. Gigabit Ethernet over ordinary Category 5 unshielded twisted pair uses five-level signalling for this reason."),

(5, "it's got the whole Mac in there and the whole thing. And it just converts serial SPI into web-enabled",
 "Dave Jones", "explains", "mechanism",
 "Self-contained Ethernet modules integrate the MAC and the protocol stack behind a serial or SPI interface, so a microcontroller design gains a network port without the host having to implement TCP/IP. Such modules were available for around twenty dollars."),

(8, "those were standalone kind of bus interface chips, not just the physical layer, but also like the Mac",
 "Tom LeMense", "explains", "market-structure",
 "Early automotive bus silicon was sold as standalone interface chips that carried both the physical layer and the MAC, and the protocols were licensed, which made the parts expensive relative to the function they provided."),

(9, "built into the physical layer is arbitration",
 None, "explains", "mechanism",
 "CAN is a multi-drop bus whose arbitration is built into the physical layer, so contention is resolved deterministically as frames are transmitted. Ethernet instead resolves contention above the wire with detection and retry."),

(10, "There's the network series, which sends the samples over gigabit ethernet to the host computer",
 "Matt Ettus", "explains", "tradeoff",
 "Software-defined radio platforms are partitioned by their host interface: one variant streams samples to an external computer over gigabit Ethernet, while an embedded variant puts a Linux host processor inside the box so the sample stream never has to be squeezed through an external link at all."),

(11, "you would... You know, it shows up like a flash drive, and then you eject it, and then it's like, oh, hey, I'm an Ethernet peripheral now, and it's all through your USB",
 "Chris Gammell", "explains", "practice",
 "A Linux single-board computer can present itself over USB as Ethernet, first enumerating as mass storage to deliver drivers and then switching to an Ethernet peripheral. Because the same cable supplies power, development needs only one connection to the host."),

(12, "So, it's two chips. It's a Mac PHY, and then it's a front-end",
 "Chris Gammell", "explains", "mechanism",
 "An Ethernet port on a board is normally partitioned into a MAC/PHY device plus an analogue front end between the PHY and the connector, so a design that already has a MAC may still need a separate PHY added to it."),

(13, "you couldn't even use tcp because it had to be deterministic",
 "Dave Jones", "explains", "constraint",
 "Streaming instrument data reliably is a determinism problem rather than a raw bandwidth problem. Where delivery timing has to be bounded, TCP is unsuitable because its retransmission behaviour makes arrival times unpredictable."),

(16, "the Raspberry Pi is not a good NAS because USB and Ethernet are shared",
 None, "explains", "constraint",
 "On early Raspberry Pi boards the Ethernet controller hangs off the same internal USB bus as the external USB ports, so disk traffic and network traffic contend for one link and total throughput is limited."),

(17, "the model a takes away the ethernet port and three of the four USBs",
 "Matt Richardson", "explains", "tradeoff",
 "Removing the Ethernet port and three of the four USB host ports yields a smaller, lighter and lower-cost variant of the same single-board computer, which suits embedded projects that do not need wired networking."),

(20, "replace the USB interface with a gigabit Ethernet interface and support power over USB. Sorry, power over Ethernet",
 "Michael Ossmann", "explains", "practice",
 "Replacing a USB host interface with gigabit Ethernet plus Power over Ethernet converts a computer peripheral into a standalone networked instrument, since one cable then supplies both the data path and the power."),

(21, "BeagleBone Black only has 10100 Ethernet. It doesn't have gigabit Ethernet. And so you would actually have a significant downgrade in speed from USB 2.0",
 "Michael Ossmann", "explains", "numbers",
 "A host board with only 10/100 Ethernet is a bandwidth downgrade relative to USB 2.0 for streaming sampled data off the platform, so an embedded carrier board is only a good host when the processing stays on board rather than being exported over the network."),

(22, "Every time that people said, oh, why don't you use Ethernet, RS485 is just so much. Direct, there's no stack",
 "Mike Harrison", "opinion", "tradeoff",
 "For short cable runs and modest data rates RS-485 is often preferred over Ethernet because it has no protocol stack, can be probed directly with an oscilloscope during debugging, and needs no switching infrastructure."),

(23, "you wouldn't use TCP IP. You just use raw Ethernet packets",
 "Dave Jones", "explains", "practice",
 "Because many microcontrollers integrate Ethernet MAC hardware, that hardware can be used as a fast point-to-point serial link by sending raw Ethernet frames and omitting TCP/IP entirely; a unidirectional link of this kind also removes collisions because the transmitter shares its segment with nothing else."),

(23, "you need all these switches and all this. It gets messy really quickly",
 "Dave Jones", "opinion", "constraint",
 "Ethernet carries an infrastructure cost that simpler buses do not: a general network needs hubs or switches and the cabling that goes with them, which grows the bill of materials and the physical complexity of an installation."),

(24, "I'd actually do Ethernet via the SPI bus because the SPI bus is available via the header",
 "Dave Jones", "explains", "practice",
 "Where several single-board computers plug into a common baseboard, distributing Ethernet to each slot over the SPI signals already present on the expansion header avoids a bundle of external cables and separate connectors."),

(25, "it's the microchip ENC28J60",
 "Dave Jones", "explains", "numbers",
 "The Microchip ENC28J60 is an Ethernet controller with an SPI host interface, which lets a board that has no Ethernet MAC of its own gain a wired network port over a few existing pins."),

(29, "Because it's standard. It's cheap. You can buy the cables off the shelf. They're already terminated",
 "Dave Jones", "explains", "practice",
 "RJ45 connectors and Category cabling are frequently reused for interfaces that are not Ethernet, because the connector is standard and cheap, pre-terminated assemblies can be bought off the shelf, and the cable's electrical behaviour is characterised."),

(30, "You can easily go a hundred meters with RS2, RS485 over, or a 422 over, over ethernet cable",
 "Dave Jones", "explains", "numbers",
 "RS-485 and RS-422 signalling will run roughly a hundred metres over ordinary Ethernet cable, which covers most installation distances without any Ethernet protocol being involved."),

(30, "my number one requirement was I'm not making a goddamn cable",
 "Dave Jones", "opinion", "practice",
 "Designing a product around standard off-the-shelf cable assemblies rather than a custom cable is a strong default, because custom cables carry engineering, tooling and supply effort that almost never repays itself."),

(66, "You think that, oh, this is an RJ 45, right? It must be an ethernet and you plug it in. No, it's some custom bloody, you know, interface",
 "Chris Gammell", "opinion", "failure-mode",
 "Reusing an RJ45 jack for a non-Ethernet interface invites a user to plug a network cable into it, which at best fails silently and at worst applies the wrong signals; the connector has become strongly associated with Ethernet even though it did not begin that way."),

(31, "we do find that for power over Ethernet in particular, a lot of people are buying either our PoE modules or the boards with PoE support on them",
 "Jon Oxer", "explains", "market-structure",
 "Across a maker-oriented board vendor's range of roughly sixty to seventy products, the Ethernet-based boards were the strongest sellers, with Power over Ethernet modules and PoE-equipped boards prominent among them."),

(31, "it's just not economical to take a whole board, plug it in",
 "Jon Oxer", "explains", "practice",
 "Plugging a ready-made module into a product is economical only at low volume; once quantities reach the thousands the module's cost and assembly overhead justify designing the same function directly into the board."),

(32, "the ethernet is 3 megabit per second coaxial cable. So it's basically entirely incompatible with modern ethernet",
 "Ken Shirriff", "explains", "history",
 "The Ethernet on the Xerox Alto ran at 3 Mbit/s over coaxial cable and is electrically and logically incompatible with modern twisted-pair Ethernet, so connecting such a machine to a current network requires a purpose-built gateway; an FPGA-based bridge was built to do exactly this."),

(33, "that's all, um, uh, converted to ethernet and trunked to a software mixing",
 "Tim Ansell", "explains", "practice",
 "In a lecture-theatre video capture rig the camera and presenter feeds are converted to Ethernet and trunked to a software mixer, because HDMI runs are limited to roughly ten metres and cannot span the room."),

(34, "why is there two Ethernet ports? Well, turns out Mac recognizes one, Windows recognizes the other",
 None, "explains", "mechanism",
 "A USB gadget board may expose two Ethernet-over-USB interfaces at once because the host operating systems support different gadget protocols; macOS binds to one and Windows to the other, while Linux enumerates both."),

(35, "the Pocket Beagle is actually a DHCP client. So when you plug it in, it'll tell the other PC and it'll give it an IP address",
 None, "explains", "procedure",
 "On a USB-gadget Ethernet link the board handles address assignment by DHCP so that the interface comes up automatically in the large majority of cases; what remains for the user is changing the routing and gateway on the host if the board is to reach the wider network."),

(37, "It goes over long distances. There's a lot of, there's a reason that some of this stuff sticks around",
 "John Davis", "opinion", "tradeoff",
 "Legacy industrial interfaces such as 24 V discrete inputs and 4-20 mA current loops persist alongside networked control because they tolerate long cable runs and can be diagnosed with simple instruments, which an Ethernet-based control network cannot match on those terms."),

(38, "if you looked in a control cabinet, you would see a bunch of Ethernet switches and, you know, cat five, six, seven cable",
 "John Davis", "explains", "market-structure",
 "Modern industrial control cabinets are wired with ordinary Ethernet switches and Category 5, 6 or 7 cable, and the switches are interchangeable commodity parts rather than special industrial silicon, because the control protocols sit on top of the standard networking stack."),

(40, "you couldn't do that over a standard CAN bus",
 "Collin Kidder", "explains", "tradeoff",
 "Sensors used for autonomous driving, such as lidar, generate data faster than a standard CAN bus can carry, which pushes vehicle architectures towards higher-rate buses including FlexRay and Ethernet."),

(42, "I tend to use like RS485, but this had enough bandwidth. The RS485 was going to be struggling. So I decided to start looking into Ethernet",
 "Mike Harrison", "explains", "tradeoff",
 "The practical trigger for moving an installation from RS-485 to Ethernet is bandwidth: once the required data rate makes the simpler differential bus struggle, the extra stack and infrastructure of Ethernet become worth paying for."),

(43, "With like 100 meg Ethernet, you can't just stick a scope on the line because it looks like noise because of the encoding",
 "Mike Harrison", "explains", "failure-mode",
 "100 Mbit/s Ethernet cannot usefully be probed by putting an oscilloscope on the pair: the line coding makes the waveform look like noise, and it is not even possible to tell by eye when the link is transmitting."),

(43, "I started playing around with an Ethernet FI, which gives you like a data is valid thing",
 "Mike Harrison", "explains", "procedure",
 "To observe Ethernet traffic timing on a mixed-signal oscilloscope, an Ethernet PHY is used to recover the received data together with a data-valid indication, and a small FPGA parallelises that stream into the scope's parallel bus input so the logic analyser can decode packets."),

(46, "as soon as you say, I want USB, maybe USB host, like I had in this box, I need to do all this Ethernet where you might be blocking a lot",
 "Eli Hughes", "opinion", "practice",
 "An embedded product that accumulates USB host support, a file system and an Ethernet stack acquires several long-running background tasks that spend most of their time blocked, and that combination is the point at which a real-time operating system starts to earn its complexity."),

(47, "Even like a hundred meg ethernet five. You're yeah. You're going to get some packet errors. Who cares?",
 "Jay Carlson", "explains", "practice",
 "Application-processor interfaces including 100 Mbit Ethernet will run well enough over 0.1 inch headers and jumper wires for prototyping; the resulting packet errors are absorbed by the CRC checks and retransmission already built into TCP/IP, so a breadboarded link still proves the design out."),

(48, "you get your ethernet FI going and you know, the ethernet Mac works and, and you know, you're getting packets, you've got DHCP working and everything seems like it's working. And then a couple hours later, it stops sending packets",
 "Jay Carlson", "explains", "failure-mode",
 "A bare-metal or RTOS networking bring-up characteristically demonstrates well and then fails hours later: the PHY, MAC and DHCP all come up and pass packets, and then transmission stops with the processor sitting in a hard fault. An operating system that isolates and restarts a failed process contains the same class of bug far better."),

(49, "It's got dual gigabit max. It's got Ethernet switch built in",
 "Jay Carlson", "explains", "mechanism",
 "Some application processors aimed at industrial equipment integrate two gigabit Ethernet MACs and an Ethernet switch on chip, alongside real-time coprocessor units capable of running fieldbus protocols such as EtherCAT, which is what makes them worth using in that role."),

(52, "Luckily it's not working on wifi. It's a ethernet cable. So you do just plug it in",
 "Pete Staples", "explains", "practice",
 "A deployed monitoring product was specified with a wired Ethernet connection rather than Wi-Fi so that installation is a matter of plugging in a cable at a customer site, with a cellular modem recommended as a fallback where the site's own internet connection is unreliable and the data volume is small."),

(53, "ethernet is galvanically isolated. So like you could seal off that",
 "Chris Gammell", "explains", "mechanism",
 "An Ethernet port is galvanically isolated at the magnetics, which makes a sealed, weatherproof outdoor interface practical, and Power over Ethernet can carry supply current on the same cable so no separate power entry is needed."),

(54, "There are other protocols like AVB that actually require the, the PTP to be implemented at a switch level. So then you need an ethernet chip that can actually do that",
 "Remco Stoutjesdijk", "explains", "mechanism",
 "Audio-over-Ethernet transports differ in what they demand of the network. One widely used transport rides on UDP and therefore tolerates occasional lost packets, whereas AVB requires precision time protocol support implemented in the switch itself, so the switch silicon has to be chosen for it."),

(54, "In the beginning, you, you even had to buy the chips from Dante",
 "Remco Stoutjesdijk", "explains", "market-structure",
 "Networked audio over Ethernet has no open standard, so vendors implement proprietary transports; one leading transport originally required buying the silicon from its owner and later moved to licensed FPGA code, leaving the ecosystem fragmented across incompatible implementations."),

(55, "basic stuff like cost and availability are going to go into like which processor you're selecting and ethernet switches",
 "Charles Aylward", "explains", "practice",
 "Choosing Ethernet as a vehicle's internal network makes the Ethernet switch a first-class part-selection problem alongside the processor, with cost and component availability among the deciding factors."),

(56, "the basic ethernet packet is 1500 bytes and there's this much preamble",
 "Charles Aylward", "explains", "procedure",
 "A network link budget can be worked out on paper before any hardware exists: starting from the Ethernet frame payload size and the preamble and header overheads, then subtracting a TCP or UDP header, gives the bytes left for sensor data and therefore how many sensor channels the link can carry at a given rate."),

(56, "I know you want 200 temperature sensors on here, but that's just not going to happen",
 "Charles Aylward", "explains", "practice",
 "The paper link budget is what lets an avionics team answer sensor-count requests from other disciplines with a number rather than an opinion, early enough that the request can still be renegotiated."),

(57, "if you care about sort of like variant, like your jitter and latency or just wanting to know what they are and what they will be",
 "Charles Aylward", "opinion", "constraint",
 "A desktop user can treat an Ethernet switch as a black box, but a control system cannot: designing with Ethernet in a real-time role requires knowing the jitter and latency the switch contributes and being able to bound them."),

(58, "all those different ports coming in, have their own cues. And then internal logic is like, you know, depopulating those cues and sending the packets to the right place",
 "Charles Aylward", "explains", "mechanism",
 "A modern Ethernet switch gives each ingress port its own queue and forwards from those queues to the correct egress port, so the collision behaviour of shared-medium Ethernet largely does not arise on a switched network; what replaces it is queueing delay."),

(59, "generally you want to just limit that to like one major, like network",
 "Charles Aylward", "opinion", "practice",
 "Keeping a vehicle's avionics on a single major network, rather than bridging several, keeps the number of hops between a command and an actuator small and the timing behaviour analysable."),

(60, "We just duplicate that board and we say, all right, now there's just a second. There's just a second node on the network",
 None, "explains", "practice",
 "When a control subsystem runs out of I/O, the scalable answer on an Ethernet architecture is to duplicate the controller board and add it as another addressable node rather than hanging sub-processors beneath the existing one. This keeps the topology hub-and-spoke, where adding a spoke changes nothing else, instead of a tree that must be rebalanced against bandwidth limits."),

(62, "it could collect a hundred mega samples at one tera sample per second, which multiplies out to a hundred microseconds of data",
 "Chris Gammell", "explains", "numbers",
 "Capturing gigabit Ethernet on an oscilloscope is memory-bound: a hundred megasamples at one terasample per second is only about a hundred microseconds of record, enough to hold roughly one to three UDP packets, which is why differential probing of the pairs is a last resort rather than a routine debugging method."),

(64, "you can jump on there anytime you like, and then they'll tell you to bugger off",
 "Dave Jones", "explains", "mechanism",
 "Ethernet's classical shared-medium access is contention-based: a station may transmit whenever it likes, a collision is detected and signalled, and the station retries after a randomised delay. This is what makes unswitched Ethernet non-deterministic."),

(67, "there was an ST Micro where you couldn't get Ethernet and high speed USB in the same silicon",
 "Werner Johansson", "explains", "constraint",
 "Requiring both an Ethernet port and high-speed USB on one microcontroller can eliminate whole vendor families, because some parts do not offer the two peripherals in the same silicon; in a 2019 Cortex-M7 selection this constraint cut the candidate list to two devices."),

(67, "which had like 20 pages of errata",
 "Werner Johansson", "explains", "practice",
 "Reading the errata sheet is part of microcontroller selection: a candidate carrying about twenty pages of errata was set aside in favour of a part with a cleaner document, even though both met the peripheral requirements."),

(68, "it was something with the Ethernet losing basically on a cycle, it was losing, it was losing its connection",
 "Chris Gammell", "explains", "failure-mode",
 "An Ethernet link that drops on an exact, repeating period is a lease-expiry symptom rather than a physical-layer fault: the DHCP lease reaches its end and the interface resets while the address is renegotiated."),

(69, "there's an Ethernet one that actually bit bangs like the Ethernet protocol itself only at 10 megabit. And you need a bunch of resistors to make it work",
 "Liam Fraser", "explains", "mechanism",
 "The programmable I/O blocks on a low-cost microcontroller have been used to bit-bang 10 Mbit/s Ethernet directly, needing only a resistor network in place of a PHY, and the same blocks have been driven at the RMII interface level to talk to a real PHY."),
]

claims = []
for idx, quote, spk, depth, kind, text in SPEC:
    p = P[idx]
    assert p["episode"], f"passage {idx} has null episode"
    t = p["text"]
    s = t.find(quote)
    assert s >= 0, f"QUOTE NOT IN PASSAGE {idx}: {quote!r}"
    claims.append({
        "claim_text": text,
        "quote_verbatim": t[s:s + len(quote)],
        "speaker": spk,
        "episode": p["episode"],
        "episode_title": p["episode_title"],
        "episode_url": p["episode_url"],
        "depth_regraded": depth,
        "kind": kind,
    })

notes = [
 "One passage (episode title 'EEVblog, National Semiconductor, Texas Instruments - The Chinese Clairvoyancy') has episode=null in the bundle and cannot be cited, so it was dropped entirely.",
 "ep 93 (Tom LeMense): attribution_reliable is false on both passages. The description of standalone automotive bus interface chips containing MAC and PHY is the interviewed automotive engineer's own material and is attributed to Tom LeMense; the adjacent CAN-arbitration exchange straddles a host question and the guest's answer, so that claim carries speaker null.",
 "ep 101: speaker_repaired renders the guest as 'Matt Eddis'; the episode is an interview with Matt Ettus of Ettus Research and the passage describes his own product line, so the name was corrected to Matt Ettus.",
 "ep 235: the observation that USB and Ethernet share a bus on the Raspberry Pi is voiced across a host/guest exchange and cannot be assigned cleanly, so speaker is null. The Model A feature-set passage is the guest describing the product and is kept as Matt Richardson.",
 "ep 265: speaker_repaired says Chris Gammell but the content is the interviewee describing his own future design ('my idea that I'm kind of leaning toward', 'that is definitely something that I considered'), so both claims are attributed to Michael Ossmann.",
 "ep 337 / ep 636: attribution_reliable is false on the ep 636 passage; the RJ45-confusion material is the host putting the question and is kept as Chris Gammell, while the ep 337 rationale for reusing RJ45 cabling is kept as Dave Jones.",
 "ep 378: the two-gadget-Ethernet and DHCP explanations come from the BeagleBoard side of a two-guest interview and cannot be separated between Jason Kridner and Robert Nelson, so speaker is null on both.",
 "ep 401, ep 250, ep 425, ep 544, ep 515, ep 584, ep 640: attribution_reliable is false throughout. Where the passage is unmistakably the named guest describing their own work (Jay Carlson on embedded Linux, Charles Aylward on rocket avionics, Werner Johansson on his power-supply design, Pete Staples on his product line) the bundle's speaker label was retained.",
 "ep 560: speaker_repaired says Dave Jones, but the passage is the audio guest explaining Dante and AVB and the licensing of the silicon; attributed to Remco Stoutjesdijk after the episode title.",
 "ep 584 (node-duplication claim): the statement is the host's summary that the guest confirms, so speaker is null.",
 "ep 434 and several banter-only passages (Altium office cabling, home network runs, hacking-contest colour, ham-radio framing) were dropped as carrying no transferable hardware content.",
]

pkt = {
 "concept": "ethernet",
 "name": b["name"],
 "spec": "knowledge-only-v4-cluster",
 "scope": {k: b[k] for k in ("cluster", "stats", "cap", "capped", "total_available")},
 "capped": b["capped"],
 "claims": claims,
 "attribution_notes": notes,
}
json.dump(pkt, open(f"{ROOT}/articles/factory/packets/ethernet.json", "w"), indent=1)
print("claims", len(claims))
