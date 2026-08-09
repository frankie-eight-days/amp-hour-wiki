import json, sys

BASE = "/Users/frankwalsh/Documents/vibecoding/amp_hour_wiki/articles/factory"
b = json.load(open(BASE + "/bundles/electromagnetic-interference.json"))
P = b["passages"]

# (passage_index, claim_text, quote, speaker, depth_regraded, kind)
C = [
(2, "A pull-up or bias resistor placed across a microcontroller's crystal may be present for emissions reasons rather than for oscillator function; on an AVR-based board the part was not required for the oscillator to start, and its likely purpose was to control high-frequency noise so the board would pass FCC testing. Because such a component is not needed for the product to work, a functional bring-up test does not detect its absence.",
 "it's possible that they added the resistor there to improve like high frequency noise or some kind of like an EMI or RFI issue, because I know that these boards were FCC tested",
 "Chris Gammell", "explains", "mechanism"),

(2, "Compliance-only components are invisible to end-of-line electrical test: a board missing a part fitted purely for emissions control powers up and behaves normally, so the unit ships and the defect surfaces only in the field or at retest.",
 "their electrical testing didn't uncover that there was a problem because they turned on the board and it, you know, it worked just fine",
 "Chris Gammell", "explains", "failure-mode"),

(3, "Phase-cut mains dimmers work by chopping the AC waveform, and the resulting fast discontinuity in the current makes them a strong broadband emissions source; solving the same dimming function cleanly at low cost and in volume is the hard part.",
 "it's horrible from an EMI point of view too. It spews out all this EMI",
 "Dave Jones", "explains", "mechanism"),

(5, "Early anti-lock braking systems, first fitted to heavy trucks because a locked-wheel jackknife is so costly, proved susceptible to nearby transmitters: a radio keyed from a vehicle alongside could apply all the brakes on the rig. Safety-critical actuators in vehicles were an immunity problem from the moment they were introduced.",
 "it would sometimes jam on all the brakes on the big rig",
 "Howard Johnson", "explains", "failure-mode"),

(7, "Most product companies have no in-house EMI compliance chamber and buy chamber time from an external laboratory, so every emissions question costs both money and calendar time and cannot be answered on the bench. An intermittent result is the worst case: a unit that fails one run in five leaves the team with no clear pass and no clear defect.",
 "They test it five times and it fails once out of five times",
 "Alan Wolke", "explains", "constraint"),

(7, "Transient emissions from a product often do not originate in a single source. They are frequently a mixing or intermodulation product of several subsystems, so the offending emission appears only when two or more buses happen to line up, which is why such failures present as intermittent and resist single-cause debugging.",
 "a lot of times these transient emissions that you get out of a product are not from one particular source. A lot of times it's a mixing product or an intermod product of many things conspiring together",
 "Alan Wolke", "explains", "mechanism"),

(8, "Closing a module into its metal housing can create a resonant cavity that produces oscillations or spurious behaviour absent when the unit is open, an effect diagnosed by the symptom disappearing whenever the lid comes off and remedied by packing conductive foam inside the enclosure.",
 "when they sealed the module up in its housing, they were getting some kinds of oscillations or some spurious results or something like that",
 "Alan Wolke", "explains", "failure-mode"),

(11, "Noise and interference control is largely absent from electrical engineering curricula, so practitioners who need it typically teach themselves on a live problem. The field's early literature was thin enough that an engineer solving noise coupling problems on the job could become his organisation's resident expert on the strength of that self-teaching alone.",
 "I had no idea how to control the noise because that was never taught in school and still seldom is",
 "Henry Ott", "explains", "history"),

(12, "Emissions remedies redistribute energy rather than remove it: a patch such as copper tape over one leak commonly makes the noise escape somewhere else, the way pressing on a balloon makes it bulge elsewhere. That behaviour is not a reason to skip the first fix, because each leak can be closed in turn.",
 "you push it here on the balloon, it pops out over there",
 "Henry Ott", "explains", "practice"),

(13, "Automotive EMC requirements began as manufacturers' self-imposed restrictions rather than as external regulation, because the consequences of interference in a car — an airbag firing, an engine control circuit disturbed, cruise control misbehaving — followed directly from what the product was.",
 "automotive has a lot of – it originally started out as self-imposed restrictions",
 "Henry Ott", "explains", "history"),

(15, "Very high gain analogue instruments are commonly built inside a fully enclosed metal box, because at high gain any coupled interference appears at the output as signal; a field photometer built around an ultra-high-gain op-amp stage was completely enclosed in aluminium for that reason.",
 "it's completely enclosed in an aluminum box because the gain is so high, you cannot have any electromagnetic interference",
 "Forrest Mims", "explains", "practice"),

(17, "Physically small boards have inherently small current loops, which limits both radiated emission and field pickup; on a product of roughly two by one centimetres with reasonable layout, EMC did not become a design problem at all, while antenna performance did.",
 "we're dealing with in the grand scheme of things, such small currents. And the board is so tiny. It's like two by one centimeters or something. So there's inherently any loop on there is going to be tiny",
 None, "explains", "mechanism"),

(18, "Radiated emission is governed principally by loop area, so long traces that enclose area with their return path are the structures that cause emissions problems; reviewing a layout for large loops is the fastest way to predict which circuits will fail a scan.",
 "Yep, EMI is all about the loop area.",
 "Dave Jones", "explains", "mechanism"),

(18, "On USB and similar interfaces the radiating structure is often not the cable itself but the termination at its end, so an expensive well-built cable plugged into a poor jack can still cost a product its compliance result.",
 "with these USB things that it's oftentimes not like the cable that's the problem. It's just that very end termination",
 "Dave Jones", "explains", "failure-mode"),

(19, "The boundary between low-frequency and high-frequency circuit behaviour is not sharply defined but sits somewhere between 10 and 100 MHz; below about a megahertz design is comparatively simple, and above 100 MHz circuits must be treated differently. That boundary is roughly the same one at which a circuit starts to radiate appreciably.",
 "when we start talking about low frequency versus high frequency, generally it's someplace between 10 and 100 meg",
 None, "explains", "numbers"),

(21, "Digital isolators that integrate their transformer on-chip are relatively immune to external magnetic fields because the enclosed loop is tiny and couples little energy. An outboard transformer is larger and adds the traces running out to it, enclosing more area and making the same function more susceptible.",
 "you've got the traces going to the transformers. You've got the transformer sitting there, not quite as small, so they are more susceptible to fields",
 "Hank Zumbahlen", "explains", "tradeoff"),

(23, "A bus line that is left undriven during a read, without an adequate pull-up to define its state, returns whatever RF the node has picked up rather than a defined logic level, turning an ordinary input into an antenna and producing data-dependent intermittent faults.",
 "you would do a read cycle and either it'd be ground or high or whatever RF it had picked up",
 "Bil Herd", "explains", "failure-mode"),

(23, "An immunity fix can be demonstrated by deliberately exposing the repaired hardware to a worst-case field rather than by retesting in the normal environment: fitting a six-foot cable and wrapping it around an uncased CRT deflection yoke proved the circuit was no longer sensitive.",
 "I had taken the case off of the monitor and I had wrapped the cable around the yoke",
 "Bil Herd", "explains", "procedure"),

(27, "A GSM handset transmits in high-current bursts — on the order of an amp for roughly twenty milliseconds — which makes a phone an unusually severe local interference source compared with continuous-carrier transmitters.",
 "It's like an amp of current for, like, 20 milliseconds",
 "Dave Jones", "explains", "numbers"),

(27, "A handheld multimeter that locked up near a GSM phone was traced to a PCB trace on the MSP430 programming line coupling energy at the GSM band and driving the processor into a programming mode. The failure was frequency-specific: handsets on other cellular standards, in other parts of the spectrum, did not reproduce it.",
 "the GSM frequency range was matching to a tray, a PCB trace on one of the programming, on the programming line for the MSP430 processor that was putting it into some programming mode",
 "Dave Jones", "explains", "failure-mode"),

(28, "Holding a mobile phone next to a powered product is a standard informal bench check for susceptibility, since the handset radiates strongly across its band; keying nearby VHF radios has been used the same way. It gives no compliance data but reveals gross immunity problems before any chamber booking.",
 "Just get your mobile phone, put it near it because it's pumping out all sorts of crap",
 "Dave Jones", "explains", "procedure"),

(29, "A lightning strike near the installation or an ungrounded operator handling the hardware injects a large surge current at the supply input that can destroy the switching converter electronics, so the input needs dedicated protection such as TVS diodes rather than relying on the converter's own ratings.",
 "there's going to be a huge surge current that comes in to the input and blow out the, you know, the, the, um, the switching converter electronics. So you have to protect against that with, you know, maybe TVS diodes",
 None, "explains", "practice"),

(29, "Filtering cannot simply be applied everywhere on a mass- and vibration-constrained platform: filter components make the design physically larger and heavier, and a heavy, bulky assembly survives launch vibration and shock less well. On a satellite power bus shared with transmitters, computers, actuators and motors, how much to filter is a mass-versus-immunity judgement rather than a default.",
 "If you add, if you just filter everything, you have a really big design. It's heavy and you know, heavy, big designs probably can't survive, probably can't survive high vibrations",
 None, "explains", "tradeoff"),

(31, "Precompliance emissions work on the bench is done by sweeping a near-field probe over the powered assembly looking for spurs and anything else coming out of it, which localises the radiating structure before any chamber time is bought.",
 "just looking for spurs and things like that anything that comes out of it",
 "Dave Jones", "explains", "procedure"),

(31, "Precompliance scanning is deferred to the final prototype before production rather than run on early iterations, on the same reasoning that a test fixture is not built until the design is settled: earlier boards will still change, so measurements made on them do not carry forward.",
 "you wouldn't build a test fixture until you know your stuff's relatively finished anyway so it's the same kind of thing",
 "Dave Jones", "explains", "practice"),

(33, "Slowing the configured slew rate on a device's outputs reduces the harmonic content of its switching edges and can turn a failed EMC scan into a pass, at the cost of the timing margin the faster edges were providing.",
 "you can magically pass your EMC standard by setting all your slew-rate outputs slow",
 "Jeff Keyzer", "explains", "practice"),

(33, "The ESD immunity requirement for a consumer product is 4 kV contact discharge and 8 kV air discharge, representing the spark that reaches the device from a held metal object or across the gap from a finger to a front panel. Real discharges of 15 kV are entirely ordinary on a dry day, so the standard is a floor rather than a description of the service environment.",
 "The ESD requirements for, like, a consumer product is 4KV contact discharge and 8KV air discharge",
 "Jeff Keyzer", "explains", "numbers"),

(33, "European requirements place more weight on immunity — a product's ability to keep working amid interference from other products — than United States requirements do, which are weighted toward limiting what a product emits.",
 "Europe is much better about this than the U.S.",
 "Jeff Keyzer", "opinion", "constraint"),

(33, "Regulatory EMC limits function as a minimum bar rather than a design target, and companies making products that are handled daily across wide temperature, humidity and RF conditions generally hold internal requirements that exceed them. The appropriate level scales with the product: a giveaway novelty and a cell phone do not warrant the same standard.",
 "they have internal requirements which go beyond the requirements of EMC",
 "Jeff Keyzer", "opinion", "practitioner-judgment"),

(34, "The recurring offender on radiated emission scans of audio hardware is the I2S master clock, precisely because its edge rate is deliberately made fast to meet the rise-time specification of the DAC or ADC it drives; the requirement that makes the clock work is the requirement that makes it radiate.",
 "it's the master clock because the master clock has this nice fast edge rate to meet some rise time spec at the DAC or the ADC",
 "Nash Reilly", "explains", "mechanism"),

(34, "A fast repetitive clock shows up on an EMI scan not at its third or fifth overtone but at much higher-order overtones, which for typical audio clock rates land near 100 MHz — the region where the cable interconnects running between boards inside the product are efficient antennas. The emission is therefore radiated by the internal wiring, not by the clock trace itself.",
 "right in like a hundred megahertz where all of your cable interconnects inside of the product function is really good antennas",
 "Nash Reilly", "explains", "mechanism"),

(35, "Utilities inject control signalling onto the mains supply, and that signalling has been known to disturb connected equipment; the common remedy is to fit a reasonably capable mains filter to susceptible products so the provider's control signals are attenuated at the input.",
 "quite common to put filters on products that are susceptible to this. You have to put a mains, you know, a fairly decent mains filter on there to filter out all these control signals coming from the power provider",
 "Dave Jones", "explains", "practice"),

(36, "Electric fence energisers, and lightning during storms, disturb nearby digital television receivers: the impulsive field swamps the front end, packets are lost and the picture freezes while error correction reruns. Digital modulation changes the symptom from a visible analogue smear to a hard dropout, which makes the interference harder for the user to attribute.",
 "it'll freeze frame because it has to re-error correct because it's just been swamped by the magnetic field",
 "Dave Jones", "explains", "failure-mode"),

(37, "Bench equipment can be the interference source in the fault being investigated. A hot air gun brought near a board induces disturbance through its own field, so the symptom is wrongly attributed to temperature when the actual stimulus is the large coil energised inches from the hardware.",
 "you think it's the heat but it's not it's the fact that you've turned on this giant magnet",
 "Dave Jones", "explains", "failure-mode"),

(38, "A connected product sold internationally is qualified for emissions against several regional regimes at once — FCC in the United States, the Canadian regulator renamed from Industry Canada to ISED, and CE marking for Europe — so the board must be shown free of EMI issues in each region rather than in one.",
 "So making sure that there's no EMI issues with the board and any of those regions.",
 "Jared Wolff", "explains", "constraint"),

(39, "A single non-compliant legacy appliance can disrupt shared infrastructure: an old television emitted a single high-level impulse noise event at switch-on that took out a village's broadband connection. Its strict 7 a.m. regularity was the clue that identified it, because a fault repeating at a fixed hour points at someone's daily routine rather than at the network.",
 "The TV was found to be emitting a single high-level impulse noise",
 "Dave Jones", "explains", "failure-mode"),

(42, "Electromagnetic compatibility covers the requirement that a product not radiate harmful interference capable of stopping other equipment from working, aircraft being the canonical example, as well as the converse requirement that the product itself keep working in the presence of others.",
 "EMC is electromagnetic compatibility, which is making sure that your product doesn't radiate harmful interference that can cause other products to stop working",
 "Jeff Keyzer", "explains", "constraint"),

(44, "DC-DC converters that sit near a radio have their switching frequency chosen to fall outside the receiver's sensitive bands; parts switching at 2 MHz were introduced so that the fundamental sat clear of the AM band, and the practice of choosing switching frequency by the radio's bands rather than by converter efficiency alone followed.",
 "was the first one to do two megahertz DC, DC converters. So they were out of the AM band",
 "Andrea Longobardi", "explains", "practice"),

(44, "Deliberately modulating a converter's switching frequency spreads its emitted energy over a band instead of concentrating it in narrow harmonics, lowering the peak the customer's EMC scan measures and easing the customer's path through testing without changing the total energy emitted.",
 "on the switching frequency to spread the noise and reduce, reduce the switching noise",
 "Andrea Longobardi", "explains", "mechanism"),

(45, "A product built with two isolation domains is difficult to take through type approval, because the interconnecting cables have very little return path available and consequently carry and radiate harmonics that a single-domain design would not present.",
 "doing type approval of a device that has two isolation domains it's very difficult to not have some interesting harmonics show up on your cables",
 "Werner Johansson", "explains", "constraint"),

(46, "Regulatory testing for medical devices is more demanding than consumer compliance: applied EMI, applied ESD and magnetic field exposure are all imposed and the system must continue functioning throughout, with no reset or crash permitted during an ESD pulse. The priority ordering resembles aerospace, with reliability first and cost a secondary consideration.",
 "You've got applied EMI issues, applied ESD issues, magnetic field issues, and things like that where the system has to keep working throughout all of that stuff",
 "Jerry Twomey", "explains", "constraint"),

(46, "Running a single-ended, ground-referenced data signal off a board on a cable is a standing immunity failure in a hostile electromagnetic environment, because it provides no common-mode rejection of the noise the cable picks up; differential signalling with error detection on the link is the corresponding remedy. A medical device that failed regulatory testing showed exactly this pattern, together with no ESD protection at all on its external interfaces.",
 "There was no common mode rejection of noise. It was ground reference signal going off of a board, which is a suicide jump when you're trying to have something work in a hostile environment.",
 "Jerry Twomey", "explains", "failure-mode"),

(47, "Noise, EMI and ESD contingencies are cheapest when built into the architecture and board layout from the outset — the protection, the filtering and the fallback options designed in before there is a symptom — rather than retrofitted after a failed compliance run, since by then the architecture and layout decisions that caused the problem are fixed.",
 "I include all of the contingencies and all of the proactive solutions to noise and EMI and ESD issues from the get-go",
 "Jerry Twomey", "explains", "practice"),
]

claims = []
bad = []
for idx, ct, q, spk, dep, kind in C:
    p = P[idx]
    if q not in p["text"]:
        bad.append((idx, q[:60]))
        continue
    if p["episode"] is None:
        bad.append((idx, "NULL EPISODE"))
        continue
    claims.append({
        "claim_text": ct,
        "quote_verbatim": q,
        "speaker": spk,
        "episode": p["episode"],
        "episode_title": p["episode_title"],
        "episode_url": p["episode_url"],
        "depth_regraded": dep,
        "kind": kind,
    })

if bad:
    print("BAD QUOTES:")
    for x in bad:
        print(x)
    sys.exit(1)

packet = {
    "concept": "electromagnetic-interference",
    "name": b["name"],
    "spec": "knowledge-only-v4-cluster",
    "scope": {
        "cluster": b["cluster"],
        "stats": b["stats"],
        "cap": b["cap"],
        "capped": b["capped"],
        "total_available": b["total_available"],
    },
    "capped": b["capped"],
    "claims": claims,
    "attribution_notes": [
        "Episode 175: bundle labels the passage 'Chris Gammell', but the content is the interviewee answering a question about his own product's EMC results; the guest is not identified unambiguously inside the passage text, so speaker is null.",
        "Episode 185 (10-100 MHz boundary passage): bundle labels 'Chris Gammell' but the frequency-boundary statement is the answer given to the host's question; the passage does not settle which voice it is, so speaker is null.",
        "Episode 222: bundle marks attribution unreliable and labels 'Chris Gammell'; the passage content is unambiguously the guest recounting his own schematic, his own boss and his own fix, so both claims are attributed to Bil Herd.",
        "Episode 401: bundle marks attribution unreliable and labels 'Chris Gammell'; the content is one of the two guest engineers describing satellite power design, but the passage does not distinguish which of the two brothers is speaking, so speaker is null.",
        "Episode 523: bundle marks attribution unreliable and labels 'Chris Gammell'; the definition of EMC is the guest's answer to the host's request to define the terms, so it is attributed to Jeff Keyzer.",
        "Episode 640: bundle marks attribution unreliable but the passage content ('that's how the first design was done', 'looking back') is the guest describing his own product, so the Werner Johansson label is retained.",
        "Episode 704: bundle labels both passages 'Dave Jones'; the content is the interviewee describing a client engagement he was called into and his own book, so both are attributed to Jerry Twomey.",
        "Episode 165 (balloon-effect passage): the copper-tape remark is the host's, but the quoted balloon analogy is the guest's reply, so the claim is attributed to Henry Ott.",
    ],
}

out = BASE + "/packets/electromagnetic-interference.json"
json.dump(packet, open(out, "w"), indent=1, ensure_ascii=False)
print("wrote", out, len(claims), "claims")
