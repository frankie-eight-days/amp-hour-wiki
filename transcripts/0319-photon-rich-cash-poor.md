---
episode: 319
title: Photon Rich, Cash Poor
url: https://theamphour.com/319-photon-rich-cash-poor/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded October 12th, 2016. Episode 319. Photon rich, cash poor.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Hey, man. I was just thinking, we haven't actually, I mean, we've talked, obviously, but we haven't recorded talking together in a couple weeks.

**Dave Jones:** That's right. So here we are again. Yes. We've got a band back together.

**Chris Gammell:** Yeah, exactly. And an hour earlier, apparently.

**Dave Jones:** Yeah, once again, every year, daylight saving. I forgot to tell you about daylight saving. And, yep, our clock went forward. These things happen. It's okay.

**Chris Gammell:** We made it. Yep. What have you been up to? What's been new on your side of the big puddle?

**Dave Jones:** I just did a video exposing, well, exposing.

**Chris Gammell:** The expose.

**Dave Jones:** Keysight's, one of Keysight's popular multimeters, the U1272A or 1270 series.

**Chris Gammell:** Oh, you've done reviews on that before, right?

**Dave Jones:** Yeah, yeah, yeah. I've done teardowns reviews. Yeah. Otherwise, great meter. With some really nice features. And it's very popular. And wah, wah, wah, wah. It's susceptible, highly susceptible, to both conducted and radiated EM fields. Not really. Or electrostatic fields. I don't think it's magnetic.

**Chris Gammell:** Uh-huh. Yeah. But you're saying, like, so if you have a high voltage across, like, a probe, it'll actually impact your reading or something or what?

**Dave Jones:** Uh, no, well, no, well, yes. If you feed the single-ended output of a function generator onto the positive terminal while you're measuring current, boom, it just goes crazy. Interesting. It just goes huge. And then it's susceptible when you put your hand near it. I show in my video that you can make it just go from, like, one amp up to 10 amps just by moving my hand near it. And it is... Well, wait a second. Wait a second.

**Chris Gammell:** Maybe you've learned how to conduct electricity. Have you thought about this, Dave?

**Dave Jones:** I am obviously has some sort of superpower.

**Chris Gammell:** You're Magneto now. You're basically... Right. You know, you're Magneto, but you're doing the right-hand rule kind of backwards.

**Dave Jones:** Right. Yeah, yeah. You're doing security. Yeah, I should have done the right-hand thumb, you know, the right... Yeah, the thumb thing. Oh, that would be funny. Anyway, all I know is that sales of this thing are going to skyrocket to the free energy movement because... Nice. Oh, man. Right.

**Chris Gammell:** Just wave your arms and you generate electricity. So, wait a second, though. Would that have been caught in testing? I mean, that wouldn't have been caught in FCC testing or anything, right?

**Dave Jones:** Well, there is an IEC EMC standard. And if you read the most manuals for most, you know, high-end multimeters specify that they're compliant to the standard and they will meet a certain volts per meter field, right? You know, I think it's three volts per meter or something. And it's supposed... I'm not sure over what range, frequency range and everything else. It's, you know, I don't know the standard. But yeah, it's, you know, it's been tested for this sort of stuff. But all you have to do is sit it next to the BNC output of a function generator and it upsets the reading. Interesting. You don't even have to touch anything. Just sit it next to the coax that's generating a 10-volt square wave. Right. And boom, it's, you know, and your reading's way out of spec.

**Chris Gammell:** Wow.

**Dave Jones:** Like, yeah, it's serious.

**Chris Gammell:** You know, it's also interesting thinking about, like, that could have passed test. And then, you know, there could be that kind of, those same IEC standards tests, you don't always test for those in production. So there could be, over time, it could just be, like, a degraded problem where it just didn't get checked against, you know?

**Dave Jones:** Oh, no, I doubt it. I think it's inherent design. It must be an inherent design flaw. I don't think anything's changed in production.

**Chris Gammell:** Do you know what was the date code on your stuff? I mean, that would be the checker, right? I've got an old meter.

**Dave Jones:** It still has the Agilent name on it, right? Oh, there you go. So, you know. All right. Yeah, that's true. It's pretty old. Interesting. So, yeah. Anyway. Who found it?

**Chris Gammell:** Did you find it?

**Dave Jones:** No, one of my viewers emailed me and said, hey, look. What he was doing was he was testing. He was measuring current for a power supply of a project from his power supply, you know, putting the meter in series. As you do. And it was near to one of those RFID card readers.

**Chris Gammell:** Like in a lab? Like a door check-in kind of thing?

**Dave Jones:** Yeah. One of those, yeah. Swipey type things, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** And presumably one of the 13 megahertz versions.

**Chris Gammell:** Yeah.

**Dave Jones:** And he noticed all these readings were going funny. And he, you know, played around and finally found that, you know. Yeah, right. Yeah. It's susceptible.

**Chris Gammell:** Isn't that fun, too, when you're, like, doing that troubleshooting? You're, like, personally, I always, like, hold a piece of cardboard above it. I'm, like, is it the light? Is it inducing 60 hertz? Yeah, yeah, yeah, yeah. Exactly. What is going on here? You know, like.

**Dave Jones:** And ironically, somebody just replied, because I haven't in-depth tested this. I haven't swept it and found, you know, the sweet point frequency or whatever, you know, the worst case frequency. See, somebody on YouTube did it. Somebody in the comments said, hey, I tested mine, and it seems to be worse around 13 megahertz, which is precisely the RFID frequency. Right. It's 13.56. Isn't that, like, the standard RF? Yeah, yeah. Something like that. Yeah, yeah. Yeah. So, oops. It's totally reminiscent of the Fluke one. If you remember my videos from, video from, like, four years ago or something, the Fluke multimeter, five years ago. Hmm. Somebody found if you put a GSM phone next to it, it just locks up. And actually, you can brick it. Right. You can brick the, yeah. So, it took them a year to fix that and finally release a new version.

**Chris Gammell:** And that's because the GSM stuff is, like, super high pulse. It's super, yeah. It's like an amp of current for, like, 20 milliseconds, right?

**Dave Jones:** Yeah. Yes, exactly. And it just so happens that the GSM frequency range, from memory, this is, from, sorry, my memory is pretty rusty. But anyway, the GSM frequency range was matching to a tray, a PCB trace on one of the programming, on the programming line for the MSP430 processor that was putting it into some programming mode. So, but it was only worked on GSM. It wouldn't work on other mobile phone frequencies, right?

**Chris Gammell:** Yeah. Right, right, right. Yeah, because they're all different parts of the spectrum. Yeah, yeah, exactly. And then others hop around more and stuff, right? Yeah.

**Dave Jones:** So, that happened to be the frequency of, like, a PCB trace loop that they had in there on the programming line. And it's like, you know, you could not have found this. You know, you could have compliance tested this to the hilt and you would not have found it, you know? Right.

**Chris Gammell:** And it's probably, at a certain point, like, you can't test everything. No, no, that's right. That's crazy.

**Dave Jones:** But that's actually a common thing to do, actually, a tip. If you're designing your product and, you know, you don't want to do compliance, you know, or you just want to do some basic testing.

**Chris Gammell:** Right, right. Or you just want to do some basic testing. Yeah, right. You know, just some, you know, to see if it's... On the bench. Is this totally messed up, right?

**Dave Jones:** Exactly. Just get your mobile phone, put it near it because it's pumping out all sorts of crap. Yeah. Right?

**Chris Gammell:** And I think we used to key off some VHF radios as well. I mean, obviously, it's going to be different frequency ranges and stuff, but... Yeah, but it's got the... RF thing.

**Dave Jones:** Yeah, but it's not only got the RF, but I've done a video way back, like, episode 20 or something, on how there's a... I think it's 218 hertz is that it actually repeats those packets. As you were saying, you know, a pulse every 20 milliseconds or whatever, it's like... Yeah. I believe it's like 218 hertz. And that is picked up in audio stuff, you know, if you've ever heard that... Oh, yeah, yeah. You know, if you ever had your mobile phone near your car radio or something, you hear this... You know? Yeah. kind of thing. Yep, that's that 218 pulse cycle packet sending thing, and that gets picked up in audio circuits. And there's actually techniques to reduce that and stuff like that.

**Chris Gammell:** Dave, this must be why I'm getting sick all the time from all this radiation all around us, right? Yeah, radiation.

**Dave Jones:** You need to go to one of those towns in the U.S. that are radiation-free.

**Chris Gammell:** I was actually just thinking about lining my entire apartment with tinfoil. Tinfoil, yeah. Yeah, yeah, just, you know, not grounded, though, just floating. Oh, okay.

**Dave Jones:** Because you don't want any of that dirty energy from the earth. Right, right, yeah. Yeah, yeah. Anyway, so that's, yeah, that, you know, even big companies like this, you can come a gutter. And nobody, you know, this meat has been out there for five years, and basically nobody's found this until now, and it's bleedingly obvious when you know.

**Chris Gammell:** Well, that's the other interesting thing, right? So, okay, so what was on the list? I forget. One of the, there was a new open source RF project. I forget. It might have disappeared. But basically it was like a programmable radio, like an SDR radio type of thing.

**Dave Jones:** This is the Faraday RF?

**Chris Gammell:** Oh, there it is. Yeah, Faraday RF. So, you know, like a lot of these things. So I was hanging out with Mike Osman recently. And, you know, just like HackRF, all these things that are programmable radios. But two of the things, you know, you'd think, oh, well, maybe we could just set these up to test at different frequencies. But to get the same kind of power, like to be licensed to get that same kind of power, you know, you shouldn't just be, like you could just sweep through all these frequencies. Yeah, right. You'd be kind of breaking the law. Yeah, right. Your neighbors would be like, what the hell is happening here?

**Dave Jones:** My garage door just opened. Yeah, right, exactly. Yeah.

**Chris Gammell:** Yeah, so I just don't know if that, I mean, like there is, there's obviously testing labs and those are licensed to do this kind of stuff. But yeah, it's, I liked your idea about the, you know, just the kind of the gut check on the bench. But other than that, it's kind of, yeah, interesting.

**Dave Jones:** Hmm. So there you go. This can happen to the best, you know, Fluke, both, this has happened to both Fluke and Keysight now. I mean, you know, it's huge. And it's not easy to fault find these things. People say, oh, why didn't I just take it apart and find the faulty component? You know, it's like, it ain't that easy. As Fluke found out, yeah, it was some resonant. It was, you know, the loop track, you know, the loop going through ground and going through the trace and everything into the programming line was at the correct wavelength of that.

**Chris Gammell:** Yep.

**Dave Jones:** You know, I think that's not easy to find, you know.

**Chris Gammell:** Right, and that's done probably a lot of trial and error, a lot of isolating, removing parts off the board, that kind of thing. Like, yeah, that's a tough find.

**Dave Jones:** So anyway, I might do a second video on that, actually opening up the meter and at least having to squeeze around. I might be able to, you know, come up with something. But I don't even have a schematic. Yeah. Anyway, so there you go.

**Chris Gammell:** Mm. Crazy.

**Dave Jones:** I've got a project too.

**Chris Gammell:** Oh, yeah? What's going on with that?

**Dave Jones:** Which, yeah, I was going to do a video on it yesterday, but I did the, yeah, this meter thing instead. Um, so yes, hopefully a video will come in shortly on this. I haven't really started on it. Well, I've done some, I've taken apart something. I've done some, um, basic background research and stuff. Um, and I've mentioned it before. Oh, I, um, you know, I purchased those, uh, what are they, not Raspberry Pi, they're the Banana Pi.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Or is it, oh, no, Orange Pi. Sorry, there's too many bloody pies out there. Too many slices of the pie. Orange Pi. I, uh, the Orange Pi one, I got like 10 of those because I was going to have like an Orange Pi, like cluster supercomputer kind of thing.

**Chris Gammell:** And you wanted to do that for, uh, not SETI, but something like SETI, right?

**Dave Jones:** The, uh, SETI Boink. Uh, yeah. Oh, Boink, that's right. Boink software, which allows you to process for anything, you know. And that's Boink with a C, right? Yes. Boink with a C, yes. Correct. Berkeley, it stands for Berkeley something or other. Because it comes from Berkeley. Anyway. Um, so I, um, you know, look, I could just cobble this together in a day, right? All I've got to do is join the boards together, hook up the power to each one, hook up an Ethernet cable through to a hub, and, you know, Bob's your uncle, right? And slap him in some sort of case with a power supply. No. Right?

**Chris Gammell:** I don't believe that. But okay, go ahead. We'll, we'll, we'll use it as the, as the crutch for this, for this, uh, discussion. What don't you believe? In a day? Come on, man.

**Dave Jones:** It's not hard to hook up power to 10 boards and then hook an Ethernet cable into it.

**Chris Gammell:** Uh-huh.

**Dave Jones:** That's literally all it is.

**Chris Gammell:** Well, that's assuming everything works and that's in the boot up and everything too, though.

**Dave Jones:** No, but I've already done that. I've already programmed a board to do its thing. Okay, I didn't know that. Right, so all I've got to do is copy the SD card over to each one and program, and individually set up the channel on each one and boom.

**Chris Gammell:** Okay.

**Dave Jones:** You know, yeah.

**Chris Gammell:** So, so you were saying you weren't doing this for a certain reason or what?

**Dave Jones:** Oh, well, no, that, that just seemed boring, right? So I wanted like a more polished solution, right? I mean, you know, there's lots of people out there who've done this, right? They've just got, you know, 20 Raspberry Pis and they've hooked them all, you know, built a nice case for them. It's all about building the case, you know, and everything, but it's just like, that's all it is, right?

**Chris Gammell:** It's like the best excuse to get a laser cutter ever.

**Dave Jones:** Yeah, yeah, totally, right? Which is fine, you know, great. I can certainly appreciate that.

**Chris Gammell:** No, no, honey, I need to get this for sure. Yeah, for sure, yeah. Got to build a computer. Definitely couldn't do it in a box. Laser cutter. And they look fantastic, right? $4,000. And they look great.

**Dave Jones:** But yeah, that's all it is. Like, it's just plugging cables in. It's not, you know, there's no laying out boards. There's no doing nothing. No making it elegant, you know. Anyway, so I thought it'd be interesting to actually, instead of just buying an Ethernet router, actually just like design my own onto the board, right? Have like a base board that all these boards plugged into, be it a Raspberry Pi or an Orange Pi 1 or whatever. In fact, I might be using the Raspberry Pi Zero. I'll talk about that in a sec. So I was going to make like a, design like a base board where all these plugged in. But instead of having like all the Ethernet cables and stuff coming out, which is boring, I'd actually do Ethernet via the SPI bus because the SPI bus is available via the header, you know, the expansion, what's it called? Not hat. It's the Raspberry.

**Chris Gammell:** The hat is like the shield type things, right?

**Dave Jones:** Yeah, the shield thing. Yeah. What's the Raspberry Pi's name for the shield?

**Chris Gammell:** Well, no, I think hat is the official name. There was also plates. That was also, they were called that. Oh, okay.

**Dave Jones:** I thought hat was beagle bone. Anyway, I don't know.

**Chris Gammell:** No, that's capes. Oh, capes.

**Dave Jones:** Oh, God. Get with the program.

**Chris Gammell:** Jeez. Didn't you get your card, your little handy reference card? Oh, God.

**Dave Jones:** So many of these things.

**Chris Gammell:** Board that plugs into other board. Board.

**Dave Jones:** Anyway, so I was going to like stack these like high density, you know, like 20 of them on one motherboard and then have like actually design the Ethernet chipset. Because you can buy them from DigiKey, right? You just get like a microchip Ethernet chipset or whatever, right? And you just put that on the board and then you can fan that out and then have those. So you basically build your own Ethernet controller onto the main board. So there's no big Ethernet cables running everywhere and all the other crap, you know. Wait, wait, wait.

**Chris Gammell:** So like one Ethernet chip per board?

**Dave Jones:** No, one Ethernet chip. Like usually like they might be like a four or eight channel Ethernet chip. So you would have to have, you know, two or three of these Ethernet chips on there if you wanted to run 20 of these boards. But then you'd also have to have an Ethernet to SPI bus converter. Once again, microchip do one of those and it's supported in the Linux build for Raspberry Pi. Yeah, yeah. Yeah, I found out this. Oh, I didn't know that. Did you know the part number? I've got it open here. Hang on. It's still in my tab, surely. Okay. Still in my tab. Come on.

**Chris Gammell:** Yeah, because I was thinking that would be one of the hard parts of like writing that driver. Oh, yeah, yeah, yeah. No, no, totally.

**Dave Jones:** No, I'm...

**Chris Gammell:** That's great.

**Dave Jones:** I probably could in theory write that driver, but I'm not going to spend a week doing it, you know. Yeah. No, that's just not my thing anymore. I used to be into that sort of stuff. Anyway, it's the microchip ENC28J60. So we can link that in. Chip of the week. Yeah. Anyway, yeah, it's in basically Ethernet to SPI. And it's good for boards like the Raspberry Pi because the Raspberry Pi... Sorry, the Raspberry Pi Zero, the $5 one, right? Which is a pretty almost... I hate to say it, but pretty useless board on its own. Unless you're doing just a completely standalone embedded controller, it is useless because it has no Ethernet. It has no internet connectivity. Right.

**Chris Gammell:** It's meant to be plugging into something else, right?

**Dave Jones:** It's meant to be in your Internet of Things wearable or something, right? Sorry, no, it's not even Internet of Things because it has no connection. It has no Wi-Fi. It has no Ethernet. It has no communications at all, right? Apart from SPI and UART, right? So, yeah, it's basically a standalone board. So, as far as most people use what they use Raspberry Pis and other things for, they always connect to the Internet somehow, you know? Right. It's because there's so much more you can do.

**Chris Gammell:** Yeah, I was just looking up. You have to, like, get to, like, hack, right? So, you see Raspberry Pi Zero hack or Wi-Fi. Right. You search for these terms and stuff. Right.

**Dave Jones:** You search for these terms. And anyway, so you can go via, and all you've got to do is, like, change the config file in the Linux thing. Like the build? The build, yeah. Just edit the config file into one line of code or whatever, and it routes Internet connectivity through the SPI bus, you know? Oh, interesting. And it's got support for this chip. Right.

**Chris Gammell:** So, usually it would go through, like, the ETH Zero, ETH Zero. Something like that. You switch it like that. Yeah, yeah. Interesting.

**Dave Jones:** And you switch it to this ENC28J60, and that's almost the command. The command is, like, 28J60 or something, you know?

**Chris Gammell:** I was just looking at the data sheet. It's only 10 base T. Does that matter that you're only a 10?

**Dave Jones:** Oh, no, no. Yeah, it doesn't matter because speed is an issue with, you know, with something for the purpose I want it for. I just want to connect to the Internet. It doesn't matter how slow it is, really.

**Chris Gammell:** Okay. So, this is for, oh, this isn't for hooking board to board. This is for hooking everything's going back to a server.

**Dave Jones:** Everything's going back to the Internet, and, yep. I see. Anyway. Interesting. Okay. Yep. And? Yes, so for those out there playing along at home, DToverlay equals ENC28J60. That's the command you've got to put in your config.txt file, and bam, it routes your Internet through the, uh, SPI bus. So, that's really cool. Um.

**Chris Gammell:** And so, this has a Mac and a PHY. So, that's maybe something that's good to explain to people, too. Oh, yes. Because I always got really confused about this. This has a Mac and a PHY on it. Correct. So, basically, you can just plug this thing right to a connector, right? You don't need any. You need the. You need the. You need magnetics. You need the magnetics, yes. Right.

**Dave Jones:** But I shouldn't need the magnetics, because I'll be talking directly to the Ethernet chip on the same board, directly between two Ethernet PHYs. So, in theory, I think, I haven't done this, but I shouldn't need the magnetics. The magnetics are only when you're driving the cables and everything else, right? But I'm going, like, from chip to chip, basically.

**Chris Gammell:** Interesting.

**Dave Jones:** So, yeah. Yeah. In theory, I think that's true.

**Chris Gammell:** So, you're doing this versus, like, an RS-485 or some other chip-based solution where you'd go board to board or chip to chip kind of thing because the built-in support on the software side? Is that right?

**Dave Jones:** Yes. Yeah. It just has the built-in support. And each board, effectively, is its own computer, right? So, it's not, you know, so it's not a sort of a supercomputer as such, right? Because it's not, you know, the processors can't, well, they could talk to each other. I could wire I.O. between them, right? Or they could talk via the Ethernet locally. But, yeah.

**Chris Gammell:** But then, again, you'd have to get back into the software side of things and write your own drivers.

**Dave Jones:** Exactly. And people could do that. Anyway. But, no. All I wanted to do was just have, I don't know, 50 or 100, you know, ARM processors just because I thought it'd be cool, you know, just all running as separate computers, all going back. To the Boink system. Anyway, I thought that'd be really cool. Now, it's probably not that practical from a performance per watt point of view or a performance per cost. You know, it's probably cheaper just to simply go and buy a NVIDIA GPU card, right? Right. And its performance per watt is probably going to be, you know, twice as good or three times better. Yeah, exactly.

**Chris Gammell:** How many flops and how many calculations you can get for...

**Dave Jones:** For a given price and a given power consumption. Right. Right.

**Chris Gammell:** Because over time, once that first initial cost is consumed, then, yeah, it's just cost of power. Yep. And that's right. Because you said you're doing this because you have extra solar power, right?

**Dave Jones:** I have extra solar power, yes. So, power is not a huge, you know, deal. Yeah. I'm so rich.

**Chris Gammell:** I'm rich in electrons.

**Dave Jones:** Get your electrons here. I'm photon rich, cash poor. There you go. I like that. That's got t-shirt. Yeah. Oh, dear. Anyway.

**Chris Gammell:** That's cool. So, we had talked a little bit before. You were looking at this board that was just announced on here. And we've talked about that before, but there's a new variation on it. Yes.

**Dave Jones:** We've talked about the chip before, which I don't like the name. It's too generic, you know? Like, it's just...

**Chris Gammell:** Yeah. It's like an acronym or something, right?

**Dave Jones:** Yeah. Like, yeah. It probably is. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm sure we... Anyway, we have covered it on here before, but they've got a new one called the Chip Pro. And I thought, aha.

**Chris Gammell:** Right. And the chip was the $9... That was the $9 computer that we...

**Dave Jones:** $9 one. This one's $6, is it?

**Chris Gammell:** We were a little bit skeptical of it. They are producing it. It seems like...

**Dave Jones:** Yeah, they are making it.

**Chris Gammell:** We were wrong on that, I guess. I don't know.

**Dave Jones:** Unfortunately, it's not suitable. The chip is not suitable for my... Well, this is like... Yeah, this is like a media...

**Chris Gammell:** I think it's MediaTek or someone. It's definitely like one of those consumer-level chips that's really hard to get at. And so that's what's interesting about it, because it's making that more accessible with the range, because it has built-in Wi-Fi and Bluetooth and all that stuff. Yeah. So those pieces are interesting. But... So, yeah, like Dave said, they just announced the new thing, the Chip Pro.

**Dave Jones:** Anyway, I looked at it and I thought, oh, maybe I can use this. But then I looked at the photos of it and... What? Anyway, we will post a photo. And, of course, it's a typical little small module, right? It's designed to mount directly on the PCB. So they've done the castellation thing, right? Yeah. Which is routing off your half holes on the side of the board, right? So that they're little, you know, half-moon-plated holes on the edge of your board. And this is a common technique for soldering, you know... Yeah, like Wi-Fi modules, stuff like that. Wi-Fi modules, everything else, right? Yeah. Right. Soldering them directly to your board.

**Chris Gammell:** Because you can actually pick and place it, right?

**Dave Jones:** You can pick and place and reflow them. Yes. Yes, it is actually possible to reflow them. Or, because they're holes, the holes are the same size as your 0.1-inch pinheaders, you can plug pin it, you can solder pinheaders to them as well.

**Chris Gammell:** Right, right.

**Dave Jones:** And, you know, great. Okay, fine. And, but... Wah, wah, wah, wah. By looking at the photo here, they've populated the bottom side of the board. They've got a double-sided load. Yeah. And that means that this thing can't sit flat on the PCB.

**Chris Gammell:** Right. Because the component is going to lift it off. Yeah, one of the uses is, obviously, you solder 0.1-inch headers in there, and then it could plug in a breadboard or...

**Dave Jones:** But that's the only way you can do it.

**Chris Gammell:** ...plug into another body. You know, you could do headers between boards if you wanted to, but that's definitely not pick and placeable then.

**Dave Jones:** Yeah, no, it's not reflowable directly onto your board, and I...

**Chris Gammell:** Which is weird, because it does, it seems, it says, optimizer SMT with cast-related edges, machine-placeable and robot-friendly. But, like, yeah, like Dave's saying... How?

**Dave Jones:** It's going to sit, like, what, two, three millimeters off the board?

**Chris Gammell:** Just, like, big globs of solder between, maybe.

**Dave Jones:** Yeah, I don't... I don't get it.

**Chris Gammell:** I mean, you could do it with a... I mean, well, I don't know about the reflowable on that piece. Now, but the interesting thing is actually, I personally... So, this is nice. It's the shrunk-down version of the existing chip, and it's got the one gigahertz processor with the... Oh, yeah, no. Whatever, whatever, whatever.

**Dave Jones:** It's a fine board. Yeah, it's a fine board.

**Chris Gammell:** The interesting thing is actually the other piece, the GR8, or the great. And so, they're actually selling... So, basically, I'm not sure what the actual number on the part number, the R8 processor is, but they're selling that system... Was it system-on-module? They call it, like, it's not... It's, like, basically...

**Dave Jones:** It's a system-on-module, yeah. Is that what it's right? Yes. Yeah, that... Yeah. Yeah, SOM, yes. Yeah. Yeah, SOM dates back to all before this new Internet of Things bullshit. You know, I was buying and using SOMs back in the late 90s.

**Chris Gammell:** Right.

**Dave Jones:** System-on-module, yeah.

**Chris Gammell:** And so, it must be on the backside. So, they're showing this Toshiba... Again, Dave said, like you said, we'll link it in so that you can see the picture. On the backside of the actual board, which is the chip pro, there's... I'm actually not sure what it is. I mean, the Toshiba TC58, whatever. That must be Flash, right?

**Dave Jones:** That's just the Flash, yep.

**Chris Gammell:** So, that's Flash. So, but you can... The GR8 has integrated DDR3. So, basically, you can get the processor and the DDR3 together in just that SOM. And that's what's interesting, because that basically makes it accessible. And then they have this slightly gimmicky thing about one to a million. It's $6. And then they have a slider where you can put in one to a million. It's like, okay, I get it. I know how to multiply. But it's... I think this piece is actually really interesting, because it opens up this chipset that definitely isn't possible to people that are buying in less than a million. So, they're rebranding it as their chip, right? I mean, obviously, it's someone else making it, but it's...

**Dave Jones:** Yeah, and they're releasing a data sheet. They're going, no NDA required, you know? Right. Yeah. Right.

**Chris Gammell:** So, that actually is really... And so, like what Dave's saying, I think it would take a lot more, because you'd have to plop down your own Flash memory and stuff like that. And you'd have to do all the other power stuff and everything. But that actually... This is an interesting move forward, because using it as a measuring stick against like a Raspberry Pi, right? So, people are designing with a Pi Zero or a Pi Three, whatever. And then they say, okay, we're ready to do something with this. There almost is literally no way to get that Broadcom chip from Broadcom.

**Dave Jones:** No, you can get it, but you've got to go in and be... sound like a big customer. You've got to sign an NDA, and you've got to commit to volume, and blah, blah, blah. I'm sure. Yeah. Yeah. So, yep.

**Chris Gammell:** Oh, here we go. It's the Allwinner R8, which is a Cortex-8 processor with...

**Dave Jones:** That's what's used in the Orange Pi one, I think.

**Chris Gammell:** Oh, is it? Yeah. Okay.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. So...

**Dave Jones:** Yes, and you can get the full data sheet for it. I wouldn't even know what I'm doing with this stuff.

**Chris Gammell:** Like, honestly, I'd be like, okay. Well, yeah. Yeah. All right. So... But, yeah, getting the data sheet is really nice, and data sheet... What am I saying? Why do I sound like you? What are you doing to me here, Dave? Sorry. But, yeah, that's nice. I mean, being able to see all that stuff. So, Allwinner may be the game winner. Who knows?

**Dave Jones:** Although they've had issues with security and stuff we've talked about in the past. Yeah. Anyway. Yep.

**Chris Gammell:** Well, I applaud this. But they're cheap. I mean, this is a nice... I mean, this really is a nice move. And so, it'll be interesting to see if people take them up on it. So, we'll see.

**Dave Jones:** Why do they have a banana in the picture?

**Chris Gammell:** For scale, maybe? Where is it?

**Dave Jones:** Yeah, but you can get big or little bananas. Anyway, maybe...

**Chris Gammell:** That's like a Reddit joke. You never heard about that? No. I don't see this banana picture you're talking about.

**Dave Jones:** Oh, sorry. It's on the main chip page if you go to the chip, not the chip pro.

**Chris Gammell:** Chip. Yeah. Yeah. That's always a... That's like a Reddit thing. I never actually understood it. It's banana for scale. So, I'm sure people can fire up their meme engines, you know.

**Dave Jones:** Got it.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. Unfortunately, I can't use this thing because it's just not the form factor I need. I can't... I need something to mount vertical. I need to densely pack these processor boards vertically on my main board. So, this one can't mount vertically unless you happen to use all the pins on one edge and not the other edge.

**Chris Gammell:** So... Yeah. Yeah. I guess if it's not like a bus system, right? You're not like able to plug board to board to board because they're not going to be sharing pins and tri-state between them.

**Dave Jones:** No. No, exactly.

**Chris Gammell:** Right.

**Dave Jones:** Yeah. Well, I don't know if they're tri-stateable. I assume they are. But then the chips that have to talk to each other and negotiate who's going to...

**Chris Gammell:** Right. Right. Yeah. You get into the same problem with like having some kind of interface chip like a whatever.

**Dave Jones:** Yep. Anyway.

**Chris Gammell:** Well, but still, interesting news.

**Dave Jones:** There you go. So, anyway, I'm working on that, hopefully. Okay.

**Chris Gammell:** Cool. That's great. That's a great little project.

**Dave Jones:** I should be working on more worthwhile projects from my business standpoint. But I don't know. I just thought it'd be fun.

**Chris Gammell:** Worthwhile. What is worthwhile?

**Dave Jones:** Worthwhile is something that generates income for me. As a self-employed... With a wife and two kids. Oh, yeah.

**Chris Gammell:** Yep, yep, yep.

**Dave Jones:** Dude, we were talking about this before the show. You're almost unrecognizable now. You've changed your appearance. I started seeing photos of you and who's this hip, young looking dude? You totally changed. And this is deliberate, you were saying. Sorry, I'm bringing it up because it's hilarious.

**Chris Gammell:** Yeah, man.

**Dave Jones:** You've got some new hipster haircut.

**Chris Gammell:** Yeah, I guess so. I've been traveling a lot, so I guess I post pictures when I do that.

**Dave Jones:** Yep. I seriously did not recognize you. You had changed... Your appearance had changed so much.

**Chris Gammell:** Well, when I show up in Australia, you better...

**Dave Jones:** I know.

**Chris Gammell:** Hold up a sign at the airport or something, man.

**Dave Jones:** Right. I would love to film that, but you can't film in airports. They'll shoot you or something.

**Chris Gammell:** Really? I didn't know that.

**Dave Jones:** Yeah. Oh, yeah, yeah. No, you're not allowed to film in airport lounges and stuff. Yeah. Yep.

**Chris Gammell:** Well, I have been traveling a lot, and so I just got back from... I did... So at the end of my Europe trip, I went to Maker Faire New York for a day and got to see some people. I think those are the pictures you're talking about. Yep. Got to hang out with the Adafruit folks for a little bit. Um, and I got to see the chipset are actually up close and personal. So... Right. We had talked about that in our back and forth episode. We did. Neither of us seemed that keen on it. And I have since switched my thought about the actual machine.

**Dave Jones:** But he's young and impressionable folks. Oh, yes.

**Chris Gammell:** I'm so... Yes. Uh, but no, I got to talk to the... I got to talk to the team for a little bit, and I got to see the machine up close. And, uh, so I told them, and I'll say it here as well, I'm still not sold on... You know, it's the same thing we've talked about here a bunch, right? I'm not sold on the idea of needing a personal pick-and-place machine. The value proposition. Yeah, exactly.

**Dave Jones:** The value proposition for it being a good return on your time and investment.

**Chris Gammell:** Now... Yeah. Their price point is what, like, it was like $4,000, $5,000?

**Dave Jones:** $4,000, $5,000, yeah. Yeah.

**Chris Gammell:** So, probably not for a personal... You know, maybe someone like, uh, you know, like, Mike Harrison does that kind of stuff. But he basically... You know, he did that stuff. And, like, other small job shop type stuff where... Yeah, I mean, but that's really not personal. That's more business type thing, right? And, um... So, yeah, I stick by that. I... I do. I think that more companies probably would be on board. And I think that this thing is great.

**Dave Jones:** Now... Unfortunately, it appeals. People, like, you know, their eyes light up when they think about the possibility of manufacturing their own boards. But then they don't realize the practical reality of doing so.

**Chris Gammell:** Right. I have just, like, an urge to start drinking beer when I start thinking about that. Like, oh, I have to do it myself? Oh, God. I don't want to... Yeah. But that's just experience talking, right? Yeah, yeah.

**Dave Jones:** I mean, it makes sense for guys like Mike, right? And he's talked about this many times. And he's the same position we are. He happens to be in the position where, yeah, he's got these clients. You know, he works for himself. He's got these clients where he manufactures, you know, runs of, you know, maybe a hundred of, you know, some blinky lead controller board that he's done for a new client. And usually he's under the pump. Right, exactly. He's really under the pump to get these done. And it makes sense for him to do them himself. But he's put also years into automating that thing, writing scripts and to do directly. He only uses parts that he knows are in his pick and place machine and blah, blah, blah, blah, blah, blah. Yep. Right? You know?

**Chris Gammell:** Yeah, that is an optimized process. And I think that would resonate with a lot of people that are doing their own, you know, anywhere from 10 to 100. Yeah, you're there, right? But once you get above 100, you know, like why? And this is what, that's what Macrofab is trying to like replace for people or give to people without having your own equipment. And, you know, same with PCB and G and Circuit Hub, all those people, right? They're trying to kind of serve that market. But once you get above 100, even Mike will tell you, you know, like he's maybe not 100, but whatever the number is, you should go to a manufacturer at that point. It just doesn't make sense to keep doing it yourself unless you have some financial reason to do so, right? If you've got some crazy deal on parts or something, right?

**Dave Jones:** Right. Yeah. If you've got reels. Well, even if you've got reels and reels and parts or something, you give them to the assembly house. That's what I do. I buy the parts. I ship them to the assembly house. Yeah.

**Chris Gammell:** Right. Job shipping is great. I mean, that's awesome. So, yeah. And so, I told the team this, right? I sat there with them. But then, okay. So, let me talk about the machine. I've never seen a pick and place machine that's dense before. Yes.

**Dave Jones:** It does look very dense. Yes. I'll give them that. It looks very good. Incredibly dense. Yes.

**Chris Gammell:** Dense in a good way, people. Your machine's so dense.

**Dave Jones:** Please explain what you mean by dense for those who don't.

**Chris Gammell:** So, and actually, it's an interesting offset. So, I've seen that TM245 as well, right? That's the-

**Dave Jones:** Yeah. The Chinese one. Yep.

**Chris Gammell:** Yeah. And that's a nice little machine too, but that- Two and a half, $3,000.

**Dave Jones:** But yeah, it's got the reels hanging out the side and-

**Chris Gammell:** Exactly. So, basically, if you think about it, it's like, so if someone was holding their arms out, right? And they were like flexing their biceps, right? And they're holding their arms out above their shoulders. And in each hand, they had a set of reels, right? Yeah. That's what a lot of pick and place machines look like. They're hanging out- Right. Outside the envelope of the machine. This is like basically turning your arms over and then kind of folding them in towards your hips. Like you're almost got your hands on your hips. And then your, the reels are down underneath your arms then. Is that good visualization? I don't know if that-

**Dave Jones:** It looks like a MakerBot. It looks like a 3D printer. Maybe. Like it's all in the one case. There's nothing hanging out the side.

**Chris Gammell:** Yes. That is true. And it is all enclosed. And I'm not sure if that's for a reason. But then the actual holders, the actual, the, what are those called? The real holders? God, my brain is-

**Dave Jones:** The- The-

**Chris Gammell:** Loaders? My brain is broken, Dave.

**Dave Jones:** I, I, you've just mental blocked me as well.

**Chris Gammell:** All right. The rest of the amp hour will be Chris and Dave trying to sound younger than they are because their brains are broken.

**Dave Jones:** Feeters. Feeters. Thank you. Oh my God. The fetus.

**Chris Gammell:** Yeah. So they had built completely custom feeders. Now-

**Dave Jones:** Yeah.

**Chris Gammell:** There is a ton of risk from that too, but these are basically, they're at prototype stage. They're past prototype stage.

**Dave Jones:** Without feeders, a pick and place machine is essentially useless.

**Chris Gammell:** It's basically a gantry robot with-

**Dave Jones:** And there is no universal feeder out there. Every company protects the technology of their feeder. They're a single source. You cannot buy clones or anything else.

**Chris Gammell:** Well, and usually they're all, and that's the other thing. So usually they're very, you know, they're machine metal. They're, you know, they're built for speed. So they have to be, you know, really, or not really precise, but really reliable. Right. That's what a lot of those feeders are.

**Dave Jones:** And they make a lot of money on those. Oh, you want to buy your $50,000 pick and place machine? Would you like feeders with that? That'll be another $50,000. Right. Exactly.

**Chris Gammell:** Right. And that's the thing where you get the most bang for your buck if, in terms of loading time, if you could buy a thousand feeders, you could just keep your reels on them, but that is cost prohibitive for everyone. Right. So that's really where I am very impressed with these guys. They said they're, you know, they've got a pulley mechanism in there. I posted a couple pictures, but I think they've done some other stuff. You know, they talk about the speed on this thing. It's not, it's not, it's not going to be, you know. It's not fast. Yeah. It's like 1,200 parts an hour or something like that, which is lower than a bunch of other ones. But in terms of cost and if you really look at other costs of like having more reels and lowering your load time, that's where you start. And then software stuff too. I think that's another big piece. All of these things are very positive. And so that's where my mind was changed. Okay. And they said they're at the, so they had a bunch of, was it SLS? Like the, you know, like the powder printed, 3D printed stuff.

**Dave Jones:** Yeah. The selective.

**Chris Gammell:** Yeah. Laser. Laser scinting. Yeah. I think it was that kind of material. It was 3D printed, but they were basically going, said they're going towards molds right now. So obviously that's an expensive piece, but yeah, I was, like I said, those reels or sorry, those feeders were super impressive. Um, you know, I didn't really, I didn't really get a feel for the actual machine itself, but, um, you know, it, like you said, the, the, the feeders are a big, big piece of it.

**Dave Jones:** A tip for those who want to design their own pick and place machine, maybe start a company with pick and place machines, design a feeder first, pick and play, design the pick and place machine. Ain't that hard. It's XY motors, camera and software, right? And it's a vacuum suction head, right?

**Chris Gammell:** I think the software is probably a very difficult piece. Yeah. Yeah.

**Dave Jones:** Software and feeders. Yeah. Right. Feeders are, are, are the key to pick and place, reliable feeders. Right.

**Chris Gammell:** Yeah. Reliability being the main thing, right? Because if you, if you, if you think you're getting 1200 parts an hour and it jams in minute five, you're not getting 1200 parts an hour.

**Dave Jones:** And you've got to sit there and message it. Even, uh, even the professional pick and place machines, the half million dollar ones have somebody there 24 seven to massage these things. Right. Right. That's the other cost. Right. It's the cost of rework.

**Chris Gammell:** It's the cost of monitoring. It's the, it's the people costs. So, yeah. Yeah. So all these things. And so I, like I said, I'm excited about it. Um, and it's, yeah. Okay. So cool. That was good.

**Dave Jones:** I still think it's a very limited market. I, you know, of course.

**Chris Gammell:** And I think they, I think they understand that too. So, uh, it was interesting though, because there was the Wazer right next to what we mentioned at the same time, or I mentioned in my version, that's, that's that, uh, water jet cutter.

**Dave Jones:** Oh, right. Yep.

**Chris Gammell:** Which is already like way, but I think the thing is, it's all about perception, right? It's about the same cost. I think it's like four or five grand. Maybe, maybe it's three or four grand, but it's a water jet cutter where it's got, uh, what do they call? Garnet. Like basically crushed up garnet is the abrasive and then you float it in water and then you shoot it in a, like a laser like stream down at something. So it's like a laser cutter, but you can use it on things like metal and, um, stone and stuff like that. And that thing is just, it's gone gangbusters on Kickstarter. But so like, what's the difference there? Right. And it's just perception, right? No one needs a frigging water jet cutter. Right. I don't care how many, how many times you say you're going to, you're going to have a, uh, a ceramics project that you need to do. As someone who had a bunch of tools, still has one of them that do not get, you know, like, it's like, okay, some people need them, but definitely not that whole cadre of people that are backing the project. So some of that is just perception.

**Dave Jones:** Because it's cool. Yeah. It's perception. They think they might need it.

**Chris Gammell:** And people have disposable income. And that is honestly a great part of Kickstarter, right? Absolutely. You know, you help, you get people that are dreaming about needing something and, you know, like those, anyways, doesn't need to talk about that. Sorry. Uh, so, uh, that was great and got to see a lot of good people there. And then, uh, the following weekend I was at, uh, Open Hardware Summit. And so we've talked about that before, um, and had some really good conversations actually. So, um, I know there was, but I was kind of watching Twitter after, uh, stuff was, were talked about. And I know you and I have talked about this stuff before. And some of this stuff I didn't quite understand. So it was good to like, to get that clarification. Um, Michael Weinberg, who's one of the, uh, he's like the lawyer behind the whole thing. Okay. Who kind of did that stuff. And he's, he's always been really, he's been part of the, the, um, the association for a long time as well. I think since the beginning. And so, uh, I didn't realize, okay, so, so two things. One was you don't have to stop using the gear logo. That's not a big deal at all.

**Dave Jones:** Right.

**Chris Gammell:** Uh, and so that's good. I, I, cause I thought everyone was just going to switch over. I talked to a couple of people there and they're like, yeah, I'll just use both. I'm like, okay. Yeah.

**Dave Jones:** Well, no, there's no, I never thought that would, I didn't think that you would stop using it. Um, you would use both. You would have the open source and you'd have the certified logo as well. Yeah.

**Chris Gammell:** Right. Exactly. And then the other piece was, um, so I knew it was about trademark, but I didn't quite understand how all that stuff worked. Um, you know, so like there was just more explanation about that. I'm not going to try and replicate the talk cause I, I didn't catch all of it. I think that stuff is either published already or will be published. And that's probably the best way to do it, uh, is to watch Michael's talk. Um, because I, I went and read some of the certification stuff too, like this licensing and I'm just like, huh, I don't, you know, I've seen it. I don't care. Right.

**Dave Jones:** No, Mike, um, on Twitter, I don't know if you've seen it, but it was hilarious. He said, who the hell would, who the F would sign this? Yeah.

**Chris Gammell:** You know, like, and I think it's kind of a, well, okay. So I don't know how effective it will be, but I think for me, at least if I was going to start doing this stuff, it would be like, it's like another mark that makes sense. And there's really no downside to the people doing it. Maybe that's a misperception again, but I, I don't think there's any, uh, downside.

**Dave Jones:** If you meet the requirement, if you meet the strict requirement.

**Chris Gammell:** Sure.

**Dave Jones:** Yeah, exactly.

**Chris Gammell:** And if you, yeah, and, and if not, like, so people that are going to be interested in doing that in the first place, right. Are people that are already bought into the whole, uh, you know, all the, all the requirements that are there meeting all of them, uh, the community definition thing. That's great. Uh, and then, you know, there's probably there, there's definitely more teeth behind any kind of, uh, prosecution if you really wanted to do it. So that's, that's, that's all I got to say about that. Right. Um, nothing. You get shatter in there, folks. No, and it's really not. And, um, so that's one thing that happened. Another thing that happened was, so I also talked to, so, uh, I talked to Mike Osman and, and Dimitri last week when, when, uh, before, and then I got to see Mike right after. And I was kind of stating, why would anyone even do this? And Mike had a very passionate argument, much of which I forget. Uh, but Mike made a lot of sense about it too. So definitely Mike is the person to ask. Cause like, uh, what did he say? He was talking about like everything was designed to be, so he was very interested in licensing his stuff as open source and defending it as open source. Right. So basically he said, hack RF, all that stuff has been designed from, from the beginning to be open source and having something behind it that is enforceable is important to him. And I was like, okay, I respect that. Um, yeah. Yeah. And so I think what it comes down to is what we've basically been saying is like, it's good. Yeah. It's going to be a big spectrum. Some things are going to be licensed. Some things aren't. Okay. Let's keep going. Um, do you have any thoughts before I keep going?

**Dave Jones:** No, no, I think, no, we don't get me started. We right. No, I, yeah, of course.

**Chris Gammell:** We have totally fucked it. Now what's, what was interesting though, is that when on the way out of town, so at the airport, then I was hanging out with, uh, Jason Kreider, right? So we've had him on the show before a long time ago, but he's from Beagleboard and they've been doing open source a long time. Beagleboard is actually a foundation now, uh, before it was like a project and now it's outside of TI as a foundation or something as well. And what we started talking about was interesting, um, about what was really needed. Right. And like this stuff is probably needed, right? Some, at some level, all this legal stuff's needed. But the thing that we were really talking about is what we really need is, you know, this is all very inward facing, you know, you're open hardware, you're not, you're this, you're that. What we really need is a PR team. Right?

**Dave Jones:** Oh God, no.

**Chris Gammell:** No, no, no. Seriously. Hear me, hear me out. Right?

**Dave Jones:** Okay.

**Chris Gammell:** Why does this even matter in the first place? Right? Right. We think it's important, right? Mike Osman made a great point that I don't remember about why, I mean, like he obviously said it's important to him. It's important based around what he wanted to do and all that stuff, right? You think it's important. I think it's important.

**Dave Jones:** Well, hang on. You weren't saying that two weeks ago, a couple of weeks back. You said, man, I don't care. What's the...

**Chris Gammell:** I don't care about, about the details of this legal stuff because I, I think it's important to share ideas, but I don't think it's important to enforce it. You know, like for my stuff, it doesn't matter, right? Because this is all about marketing a product based on it's being open, right?

**Dave Jones:** Oh, look, if you're, if you're going their route, right? With this certified open hardware logo, yes, they need, they need PR, right?

**Chris Gammell:** No, no, no. So I'm actually not saying about that logo even.

**Dave Jones:** Oh, you're saying about open hardware in general.

**Chris Gammell:** Yeah. Why does it even matter? Right? Right. And, and that's, it was an interesting conversation around that because like most people like, okay, so you're going to buy, uh, and okay, so I'll use Jason as an example, right? You're going to buy a Raspberry Pi versus a BeagleBone Black, right? Yeah. One's open, one's not. Does it matter? And I don't know. Should it? I think it does personally, but...

**Dave Jones:** Well, who's your target market for the PR?

**Chris Gammell:** Right. Well, that's the thing. It has to be people not even in the community. It's people like...

**Dave Jones:** Right.

**Chris Gammell:** Yeah. And that's, and that's where it was very interesting to me. So, uh, and it's, it's something I, I don't know.

**Dave Jones:** Do those people care? Right. Exactly. Will the PR influence their buying decision?

**Chris Gammell:** Right. Well, what, what we basically came down to is like, it's like a got milk campaign for, uh, open hardware, right? And it's like...

**Dave Jones:** Sorry, I got milk? What's that?

**Chris Gammell:** Oh, you guys don't have that there. No. It was, uh, it was basically like the, the equivalent of the open hardware, uh, association would be like the, the dairy farmers of America. Yeah, that's right. Of course you wouldn't have that. Basically, there was all of these, these campaigns about drinking milk, the importance of drinking milk, right or wrong. It doesn't matter. It was a PR campaign where they basically said, you should be drinking milk. Your children should be drinking. Like, and it's like, it's just a pure PR campaign. And it had people thinking about milk. Uh, and...

**Dave Jones:** I have seen this actually on the, on the Gruen, uh, transfer, which is an Australian, uh, TV show about advertising. Yep. And it's absolutely fascinating. Yeah. And they were talking about this. That is one of the most famous campaigns ever, right? Yep. Yeah. They were talking about that campaign. Right. Yep.

**Chris Gammell:** And yeah, especially for like, for like catchphrases and like...

**Chris Gammell:** Yeah. So, uh... Cool. Very interesting. Uh... I don't know. Maybe I'm just less cranky than last week.

**Dave Jones:** I think you are. Yep. Yep. Definitely. You were so cranky the other week. I was like, I don't care.

**Speaker ?:** What?

**Dave Jones:** Tell someone he gives a toss. Well, you know. He's chilled out with his new hipster hairdo.

**Chris Gammell:** That's what it is. You know, I let some of the steam off with the haircut. That's what it is.

**Dave Jones:** Oh, boy. Yep. Oh, can we talk about...

**Chris Gammell:** Do we have to?

**Dave Jones:** Can we talk about the Wi-Fi kettle?

**Chris Gammell:** Oh, that one. Oh, I thought you were going to go solar. Yeah, yeah. What? No, no, no. Solar roadways, I thought you were going to go back to. Oh, no, no.

**Dave Jones:** I'm going to do solar roadways to finish off. Yeah. Hell yeah. Oh, okay.

**Chris Gammell:** Right, right. End of a bang. Yeah. Yeah, we've got another 10 minutes. Yeah. So, the Wi-Fi kettle. This was actually really funny.

**Dave Jones:** We told... Can we say we told you so? Like, you know... Wow. You know, your Wi-Fi connected light bulb. It's like, this is what the world's come to.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, and this is not a good future. Right.

**Chris Gammell:** This is not what I signed up for. The thing I don't get is... Okay, so, like, it's still connected by... It's just the base that's enabling a single relay, right?

**Dave Jones:** Yeah, yeah, yeah. That's basically it.

**Chris Gammell:** Okay, so explain the device first, because maybe that would make sense.

**Dave Jones:** A guy... Sorry, we don't know his name. I could probably call it up. He was on Twitter. He bought this Wi-Fi connected kettle, right? So, you can be able to turn it on through your phone or through bloody Amazon or whatever. I don't know. Right? And the Internet of Things kettle.

**Chris Gammell:** Internet of Things.

**Dave Jones:** And you can tell what's going to go wrong here. Anyway, he got up in the morning and he thought, right, I'm going to use my new kettle today.

**Chris Gammell:** Today is the day.

**Dave Jones:** And it took him 11 hours to boil water. And he live tweeted this, right? And it was followed by, like, thousands of people retweeting and loving it and, you know, everything else. And it took... And we'll link in the page below. It is hilarious. They've screen-captured his tweets and all of his efforts trying to get the software stack platform infrastructure working just to turn on his freaking Wi-Fi kettle. And he finally did it. He finally nailed him. And the whole Internet cheers, you know, at the end of the day when he finally did it. He boiled his water and he posted a video of the thing finally working and boiling water. That is so crazy. 11 hours full-time, nonstop trying to get this thing working. I'm not sure what the actual issue was in the end. Yeah. You know, it could have been something simple that was obvious in hindsight. But anyway...

**Chris Gammell:** Well, still, I mean, like, okay, usability stuff.

**Dave Jones:** It's got voice control as well.

**Chris Gammell:** Let's compare it to the exact same thing in any other British kitchen, right? Yep. Walk in, fill the kettle, flip the switch. Flick the switch. Come back when it's done. Like, and it's just...

**Dave Jones:** Flick the switch. That electricity stuff goes to an element through some copper and then it heats up using Ohm's law and boils your water.

**Chris Gammell:** Right, but it boils it faster than an American's kettle, as the Brits like to remind me. Oh, right, okay. Because 240 over 120. More wattage, yep. Yeah, blah, blah, blah. Thanks a lot. I know. Please don't write in.

**Dave Jones:** 2400 watts of goodness. Yeah.

**Chris Gammell:** Yeah, and so, like, from a user... Someone was telling me the other day about a toothbrush that was Wi-Fi connected.

**Dave Jones:** Yeah, Wi-Fi connected, yep. What the hell? And there's an app that monitors your... Oh, no, no, no, this wasn't even for that.

**Chris Gammell:** It was just like, oh, you need to stop brushing on that one side and switch to the other side.

**Dave Jones:** Mine has got, like, a little buzzer in it that goes beep when the 30 seconds are up and you're supposed to switch to the other side.

**Chris Gammell:** If that's even necessary, right?

**Dave Jones:** I thought that was advanced black magic technology that shouldn't be in there, you know? Black magic.

**Chris Gammell:** Don't tell me what to do, toothbrush. Yeah, okay, so let's talk about margin. This is... I think this is actually a large... It's largely due to margin problems, right? Because if you make a kettle the same way for 10 years, let's be generous to say 10 years. As you do it, say you come up with the greatest new whiz-bang kettle design, other people, you know, you lose brand loyalty, you get copycats from China, everything happens. How do you start to differentiate? Well, you differentiate by saying, now with Bluetooth, now with Wi-Fi, right? You can't live without this. And so it's like, oh, God.

**Dave Jones:** And it probably works. I mean, I would love to see, no, oh, we now, how to differentiate yourself. Oh, now it's made in the US of A. You know, something that may be, right? That's another PR thing. Yeah, or it uses a new titanium alloy that's lighter and stronger and never rust or whatever. I don't know, something like that, right?

**Chris Gammell:** People don't look at the box and say, if they even go to the store and look at a box, they don't look at the Amazon review and say, oh, look, it's exactly the same as everything else. Like, people are looking for some kind of differentiation in a marketplace with tons and tons of devices.

**Dave Jones:** Because then it can be in the title, the Amazon title, right? It's got Wi-Fi in the title. Sure. You know, it's an extra feature.

**Chris Gammell:** You know what you and I should do? We should come up with some vaporware feature that we license the name to, right?

**Dave Jones:** We can call it... Yes, yes, let's do it.

**Chris Gammell:** DC... So, Dave and Chris, DC enabled. Hmm, DC enabled. No, that wouldn't work. That might be confusing.

**Dave Jones:** DC Ether or something. I don't know.

**Chris Gammell:** DC Ether. There we go. DC Ether. We can brainstorm this. And you have to be part of the consortium, right? Of course. Right, right. To be DC Ether certified. DC Ether certified. And then if you are, then you can use that legally. It's a trademark name, right?

**Dave Jones:** Right, and you get the logo and the stamp you can put on your webpage. Yep.

**Chris Gammell:** And yeah.

**Dave Jones:** I mean, you only have to pay us how much?

**Chris Gammell:** Oh, I don't know.

**Dave Jones:** One percent of your revenue or something.

**Chris Gammell:** I don't know how... Yeah, because HDMI does that too, right? Yeah, yeah. USB all... Like, even SPI, right? That was started as a Motorola thing.

**Dave Jones:** Right, yes.

**Chris Gammell:** Yeah. And Motorola lost it at some point. I don't know how that happened.

**Dave Jones:** So was I2C. I2C was a Philips thing.

**Chris Gammell:** Oh, interesting. Okay.

**Dave Jones:** And I don't know if it was licensed. I think it might have been... Yes, it was licensed if you wanted to use the official logo, because the logo was trademarked.

**Chris Gammell:** Uh-huh, yeah.

**Dave Jones:** But if you didn't... So if you wanted to use the... You know, they had a specific logo, the I2C with a TM next to it, right? If you wanted to... Like, it was old Philips data books used to have data sheets, used to have this logo. Oh, yeah. You know, it was like an outline. If you search for I2C logo, you'll find it. And if you wanted to use that logo and say your chip... Targeted other chip makers. If your chip was I2C compatible, yeah, you had to pay Philips a bloody royalty.

**Chris Gammell:** And now you'd have to pay at the Broadcom.

**Dave Jones:** Yeah. So that's why others started calling it... Oh, you missed it. Oh, the two-wire. Oh, two-wire. Yeah. You know, they called it like two-wire interface. So, you know, maximum come. And this is a two-wire interface chip. Nudge, nudge, wink, wink. Happens to work exactly the same. Right, because they also had their one-wire, the Dallas one-wire thing, right? Yeah, yeah, yeah, yeah. Yeah, the Dallas one-wire. And it's like, yeah, that's how they got around paying Philips their royalty. So, anyway. Hey. Yeah. Isn't that fun? I guess that's still around, but... I don't know. You sort of see iSquad C and everything, but they don't use the logo any further. I think the logo's gone the way of the code.

**Chris Gammell:** Well, it's the thing when you lose it. When you lose trademark, then it's just, you know, it's like Kleenex or anything else, right? Yeah, yeah. Basically, you have to fight against that to...

**Dave Jones:** Yep. Yes, to keep your trademark. Otherwise, it becomes invalid. If you let everyone use it, then it becomes public domain, essentially. Mm-hmm. Yeah. Yep. So, Wi-Fi, what a fail. Anyway, it's hilarious. We'll link in the article. Just read it. It's great. It's really good. Yep. And I love the fact that, you know, the whole internet cheers when he, you know... Yeah. Somebody tweeted, and I'm going to drop an F-bomb here. Why don't you just get a normal fucking kettle?

**Chris Gammell:** Yeah. They ain't wrong.

**Dave Jones:** And it got 79, you know, 250 likes, you know? Yeah. Yeah. And somebody else tweeted, at this point, I'm desperate to avoid this future at all costs. Yep. It's just... It's sad.

**Chris Gammell:** So, I think about this stuff. So, okay. So, I also wanted to talk about the XKCD comic, which I loved. It was called Work 1741. And basically, Randall's pointing out all of the arguments and meetings that happen around design decisions, you know, for stuff like this. At some point... Yeah, yeah. Yes, I've seen this one. At some point, at the kettle manufacturer, they had to decide if it was going to be Wi-Fi or Bluetooth, right? Yep. You know, then all the buttons they had to do and everything else.

**Dave Jones:** I think he could have really gone to town with that one. Oh, yeah. He could have made this poster size, right? Yeah, I know. Yeah, poster size. Yeah.

**Chris Gammell:** And... I think we get the point, though. That's the right thing, you know? Yeah, exactly.

**Dave Jones:** We should redo this. We should draw... We should redraw this and add, you know, like, real-world engineering stuff to it. And, like, yeah, you could add a hundred things.

**Chris Gammell:** Inductor change by 20 micro-Henrys because of FCC testing. Right. Figured out empirically.

**Dave Jones:** Supply change change because component obsolescence. Right, right. There's just countless.

**Chris Gammell:** Found out at 4 p.m. on a Friday.

**Dave Jones:** Yeah. The CEO did not like the shade of matte black. Oh, yeah. We had to. There's that one.

**Chris Gammell:** Yeah. Yeah. Yeah. Coming from out here, that's... This is the outsider perspective. This is the... We're just reacting. We're not pushing for something. We're just reacting to the world that we're... Yeah. Yeah.

**Dave Jones:** I wonder how big you could make that. That'd be awesome.

**Chris Gammell:** Oh, I'm sure you could do a whole... Yep. But, I mean, like, so the main thing, though, is, like, all of these things, I think about this stuff often, like, especially with home goods and stuff like that. How much stuff is really needed here, right? Okay, so, like, you could really take the entire spectrum of, you know, IoT home devices, right? Some of the things are... I will finally capitulate and say some of the things are convenient. A Nest, a connected thermostat like Nest is convenient if you want to warm up your house before you get home. Is it necessary? No. People have been getting away with programmable thermostats for a long time, and before that, they had regular thermostats, and sometimes you just wait until it warms up, right? That's just the cranky old man, Gene, kicking in. Back in my day.

**Dave Jones:** But you don't need a phone-connected, app-connected light bulb. Like, just stop it. Stop it.

**Chris Gammell:** Yeah, I don't know. I don't know. I don't think there's much of anything that's needed, right? It's all about... We're into the age of convenience, and that's because that's all that's really... I would be interested to hear about... We're in the age of wankery, too. Sure, of course. But no, let's be fair. That's always happened, right? If you look at, like, those old computer models, like, those old computer ads, like, oh, now has... You had 16 colors. Now you have 24.

**Dave Jones:** I can remember back in the 80s, you remember... No, you wouldn't remember. But the personal robot craze. You need a home personal robot. Right. The Robot 2000, you know.

**Chris Gammell:** Asimo.

**Dave Jones:** Yeah, but these things were big in the 80s. And it was like, you need to have the robot with the coffee cup holder so it can, you know, so it can follow you around with your coffee cup and, you know, holding your coffee cup for you. Sure, right. Yeah, like...

**Chris Gammell:** And so that's the thing, like, in terms of actual, like, new appliances that people need...

**Dave Jones:** Right.

**Chris Gammell:** That hasn't happened in a while. I mean, cell phones were probably one of the big ones. But even that was just an extension of the phone. Like, so all these things, like, a lot of this is just lifestyle enhancement, not like... No one needs any of this stuff. No, that's right. And I know that that argument can be taken very far back of, like, oh, what do you really need other than a grass hut and, you know, maybe clothes? You know, like... Yeah, I'm sure... Okay, so, yeah, I can go all the way there. But especially with this network-enabled stuff, I love hearing... So there are some legitimate uses, right? Accessibility, certain things, but probably not mass market. You know, like... I mean, like... Like, handicap accessibility, stuff like that. Like, there are some legitimate uses there. But in terms of, like, needing a lot of this stuff, it's just an extra layer of marketing, basically. Right now. We'll see. Right. Speaking of marketing, you had one last thing you wanted to talk about?

**Dave Jones:** Solar freaking roadways. Oh, my goodness. I'm debating... I'm still debating whether or not to do a video on this. Leave your thoughts down below if I should or not. They have finally done their first big public installation. Is it on a road? Because it's solar roadways. No. No, they weren't allowed to do that. It's on the footpath out front of some dunnies, which is, for you, Yakes, it's a toilet block. I don't know. Uh-huh. Does it generate power? Because it's solar freaking roadways. No. It doesn't generate any power at all. They haven't even hooked the solar cells up.

**Chris Gammell:** Oh, Dave. Do the... You gotta... You gotta... You gotta let it go, man. It's just gonna eat your life.

**Dave Jones:** Do the blinky LEDs work? No. Only seven of them out of 30 still work. Like, two-thirds of them were delivered faulty.

**Chris Gammell:** Maybe you could do the XKCD comic about the solar roadways. Like, do, like, the drawing thing.

**Dave Jones:** Yeah, yeah, right. It's like... Have they... Like, do they install drainage on this thing? No. They've got... You know, like... It's just... It is the most... Uh... It is the biggest installation debacle I've ever seen. It is ridiculous. Right? They... When they actually got there, there's a link... We can probably add a link to a news report. We only found out this later. That they've now admitted, yeah, it doesn't generate any power. Yes, all the panels were delivered faulty. But they still installed them. They knew this. They knew it wouldn't generate any power. They knew the LEDs wouldn't work. Most of the LEDs wouldn't work. And they... And it wouldn't hit the tiles. The heaters didn't work. Right? So, the three big things. The three only things that this thing is supposed to do. Well, out of four, actually. You know, it's supposed to have cars going on it, which they didn't do either. So, the four things this thing is supposed to do. Generate power. Have cars going on it. Blink its bloody lights. And melt snow. The four things. It can't do a single one of them. And they still went ahead with the installation.

**Speaker ?:** What the...

**Chris Gammell:** Marketing, man. Marketing.

**Dave Jones:** Oh, yeah. Because they had to... PR. Because they knew the press was showing up. And they had to be shown to do... And we can get some blinking LEDs working. Oh, that'll keep everyone happy. And it did, apparently. There's no news reports. People glowing about this is the future. Holy shit.

**Chris Gammell:** Hey, got you talking about it.

**Dave Jones:** Got you talking about it.

**Chris Gammell:** You're just a slave to the machine, man. You're just a slave to the machine.

**Dave Jones:** Oh, man. Unfortunately, I have to. Because I've done five videos. I know. Yes, you're invested now. I'm invested. But why would you go ahead? Has anyone else been in that situation where your product does not do a single thing that you claim, but you went ahead and did a trial or something anyway?

**Chris Gammell:** Like... Didn't you talk about that at, like, trade shows? Isn't that what a trade show is?

**Dave Jones:** No. Last minute soldering? Oh, I said the old smoke and mirrors demo.

**Chris Gammell:** Yeah, yeah, yeah. Yeah.

**Dave Jones:** Yeah. But no, we always got something working in the end. Oh, okay. You know, that was, you know, good enough.

**Chris Gammell:** Sounds like they got some LEDs working, Dave. I'm just saying.

**Dave Jones:** They got some LEDs blinking. And it's hilarious. There's video of somebody coming along, some member of the public coming along, and some of these LEDs are just failed, right? So they're just, like, stuck on. They're supposed to be blinking and doing patterns and stuff. And somebody comes along and jumps up and down on it, and it fixes it. All the LEDs go out. It's hilarious. It's just so funny.

**Chris Gammell:** I don't know. At a certain point, you just, you write it off, you say, I mean, it's going to make you upset that they keep getting press about it, but they're not the first hucksters. They're not going to be the last ones.

**Dave Jones:** Yeah. It's just, anyway, I thought that was, so I might do a video just, like, laughing at it. Just, like, five minutes of just laughter. So, I don't know. Anyway.

**Chris Gammell:** Okay, let's end on some positive stuff. We can just run through some of these links. Because we don't even know what I would say about them. We've talked about Megabots in the past. They're actually showing all their design decisions as they redesign this robot. I still think it's crazy. So, I don't know if people don't know. It's that American team that's going to fight a Japanese team with giant fighting robots. And they, but basically, they're making it into, like, a series, too. So, worth taking a couple minutes to watch. They've done some testing, and, you know, it's cool. So, what else? Well, you mentioned the 3D robotics thing. You had posted about that.

**Dave Jones:** Oh, yes. I had no idea until I saw this article today. This is huge. Of course, we've had Chris Anderson on the show before.

**Chris Gammell:** Yeah, maybe this isn't really an uplifting note.

**Dave Jones:** No, it's not. I thought they were, like, number one or number two in the drone business. They've basically collapsed and have completely gotten out of the hardware drone business. It just did not work for them. They burned through, like, $100 million in cash, in VC cash.

**Chris Gammell:** Well, they did a big thing with the Solo. That's what the big bet was.

**Dave Jones:** I don't know how you can invest so much money into one little drone. Like, how many freaking engineers have they got working on this thing? Oh, no, no.

**Chris Gammell:** I'm sure it was – come on. You've got to build out the factory and stuff, too. Oh, yeah. If you're trying to make a consumer product –

**Dave Jones:** You can build a lot of cash on a factory. Yeah, right.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Yeah, and build up for production and all that sort of stuff. But anyway –

**Chris Gammell:** Well, they moved out of Mexico a long time ago, too. Right. That was one of the things they'd done, and they moved everything to China, I believe.

**Dave Jones:** Because I remember the talk – Chris was saying, yeah, there was a big step for them to bring their pick-and-place machines in-house. They were doing their in-house boards and stuff like that, and that really worked well for them.

**Chris Gammell:** Wait, when he was on the show?

**Dave Jones:** Yeah.

**Chris Gammell:** How long ago was that? That was one of our early interviews, wasn't it?

**Dave Jones:** Yeah, yeah. It was one of our early interviews, yeah. Like, 50 or something. 30. I don't know.

**Chris Gammell:** No, not – well, anyway, it was right after you'd done Makers. Oh, episode 105. So, that was 2012. So, four years ago, yeah. Yeah, wow. Wow.

**Dave Jones:** And, anyway, yeah, they've basically – well, they haven't gone bankrupt, but they basically had to completely pivot. So, now, in 12 months, they've gone from the world's leading drone company to a company that now no longer makes drones, and they're doing – what is that? They've now pivoted to software – enterprise software is their new focus.

**Chris Gammell:** Yeah, because one of the things they were talking about doing was also making, you know, these consumer-level drones, but also then the SaaS level, like, okay, so now you buy a drone as an architectural firm. You throw this thing in the air, it zooms around, and then it basically scans and does, like, modeling, I think, like, in the cloud. Right, okay. I believe that's what it was. Right.

**Dave Jones:** So, it's some sort of image processing, maybe a drone collaboration and communication stuff or something like that.

**Chris Gammell:** Yeah, they were working with Autodesk, I think, at some point. Oh, okay, right. Yeah.

**Dave Jones:** Interesting.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, they haven't gone bankrupt, but they're basically totally collapsed. They had to sack a whole bunch of people, I think. Yeah. Yeah, they've – I would say they've essentially gone bust. I mean, you know, if you're not making drones anymore –

**Chris Gammell:** I don't really know, but, yeah, I don't know how this stuff works.

**Dave Jones:** Well, to me, if you're a drone – the world's leading drone company and you don't make drones anymore, you've gone bust. I mean, that's just, you know, like –

**Chris Gammell:** I don't know. Just fail. IBM doesn't make hardware anymore. Right. Yes, they do. What? Some. What do they make? They make – Not much. I don't think they even make servers anymore, do they?

**Dave Jones:** Did they sell their server division? I can't remember. Anyway.

**Chris Gammell:** I thought they did, yeah.

**Dave Jones:** Anyway. Yes. Okay, sure. Didn't they sell it to Fuji or something? I don't know. Anyway, whatever. But, yeah, they'll survive as a company, but they've basically completely failed.

**Chris Gammell:** Yeah. Well, it's very different. I mean, so they had already moved away from the DIY piece, right? And that's fine. Yeah, they'll go in – You and I were talking before the show, and, like, this – you know, we don't know any of the dealings, but one thing that I know is that the NBA playbook says once you've – if you want to grow, you've got to keep going more and more towards B2B, large-scale, like, enterprise-level stuff. Right. Yeah. And it's like, you can do that, but then, you know, these big bets, it's more dependent on smaller companies. Yeah. And I was telling Dave about the – there was an article about – I forget where I was hearing about it, but it was about MailChimp, right? And MailChimp is a – we actually use it for the Amp Hour and stuff like that. It's an email program. But they've been around – there's a software company that's been around 16 years, and they've held on by just, like, not taking on debt.

**Dave Jones:** Basically giving everyone the finger. Yeah. Saying bugger off. Yeah.

**Chris Gammell:** Every time someone comes in and says, oh, you should really pivot to, you know, enterprise level, and they just kept serving.

**Dave Jones:** Or we'll invest money in you, and, you know, like, you can – yeah. No, they've given them the middle finger, and I love that. There is something to be said. I was, like, screaming this at Altium for every day I was working there. It's like, there's nothing wrong with being the world's best PCB tool company. Why try and do anything else? There's nothing wrong with being the world's best mail, email client, right? Yeah, sure, sure. Like, why?

**Chris Gammell:** Okay, so I actually do have an interesting point. I was thinking about this as – so I was driving – when I was going to Maker Faire New York, I was driving into the Lincoln Tunnel, right? Well, I wasn't driving. I was getting driven, right? Right. And I was thinking, who the hell planned this? Like, there are – like, obviously, like – so I think the counterpoint to that is that at some point, there are people that are thinking that big, and I know that it takes a lot of stuff to get to that point. Right. And there's tradeoffs to do so, right? Long timelines, lots and lots of money invested, lots of community interest, obviously, for infrastructure projects like that. But, like, I just started – I started to have a panic attack just thinking about all the planning you would have to do to make a tunnel that goes under the water that then you build so that people don't die, and then all those commuters go through every day. And so, like, there are big dreamers out there, and there's obviously a lot of players in that too. So, I think that's the positive side of it, but it's often misguided, right? It's not like –

**Dave Jones:** Well, yeah, people think –

**Chris Gammell:** Yeah, for an email company, you're not building a tunnel, right?

**Dave Jones:** This comes back to bite governments as well. People – people – people. People. Quite much. People think that the only way to grow a company is to keep expanding it, you know? And this is like – it's like you must have growth. You know, you must have that 10% compound of growth every, every year, right? Why? Why?

**Chris Gammell:** Well, you're saying the only – I mean, that is the only way to grow a company, but yeah, that's not the only way to have a company or for a company to thrive.

**Dave Jones:** No, exactly, and governments work the same way. You know, governments are operating like a business. Like, ooh, we must have 10% growth per year. Our country must have 10% growth. Why?

**Chris Gammell:** Right. Like – Yeah, no, no, that's true.

**Dave Jones:** Like, sometimes treating it like a big business like that is – that's why often going – floating your company on the share market is the wrong move because then you have shareholders and they want this. They want this compound of growth every year. They expect it. So, it's ruined countless companies because of that.

**Chris Gammell:** Right, exactly, and it's basically – it's like a – it's a contract that's made, right? It's like, okay, we're going to grow, we're going to make money for people, and there's – yeah, there are certain ways you're going to do that by expanding into new markets or whatever you're going to do. So, maybe that's part of the MBA playbook. It's also tied to the shareholder value and stuff, but it's not always fun and it does, unfortunately, hurt companies sometimes. Yep. So, interesting, since you mentioned the government piece as well, I saw they were talking about economic output based on space, and the thing we didn't mention last two weeks ago is the whole space race, Boeing, SpaceX. I was really surprised. I honestly thought you were –

**Dave Jones:** I didn't know there was any race between Boeing. I knew I watched SpaceX, Elon Musk's SpaceX.

**Chris Gammell:** Yeah, and that was like a special kind of crazy, right? I heard that was a little crazy, but yeah, Boeing's trying to get there too, apparently. Right. And –

**Dave Jones:** I don't think they will because there's no profit in it. There's no profit motive. Right. They can't do it. Elon Musk can do it because Elon Musk is the biggest shareholder in SpaceX. He's got it by the balls, and he can say, we're going to waste $100 million – or spend, invest $100 million cash in this. I don't care if there's a return. And he said this basically in his speech. It's like, I'm going to do it anyway, right?

**Chris Gammell:** Right, right. He said the only reason he makes money anymore is to get off the planet, right?

**Dave Jones:** Right. Yeah. And you need someone like that to do it. Boeing, they cannot do it. The shareholders will not allow it. Once the shareholders realize there's no return on their investment, they will force them to scrap it. Guaranteed. Right. Guaranteed. Unless they can get money from the taxpayer somehow.

**Chris Gammell:** Right. Well, I was trying to find the article. So, basically, it was a discussion on Reddit. And I apologize. I can't find it right now. But they were talking about some of the multiples of space investment and stuff like that. But basically, also, the space – sorry, the space race. So, like the Cold War space race type stuff. And how that is an actual natural outlet for economic surplus, right? Right. So, you can either use your economic surplus to go invade other countries or you can use it to get off the planet. And obviously, the second one is a lot better. Yeah. Hello, America. But then all of it's just the benefits of having investment in that end goal, right? So, obviously, that's the same thing of dreaming really big and having shared interest with the public of why do we want to do this in the first place? But once you do that and there's money behind it and then it's like that money just goes everywhere. You know, like it improves science on multiple levels. No, totally. Technology benefits from all the ricochet inventions and everything. So, it's great.

**Dave Jones:** The moonshot, the Apollo program and Gemini and everything before that and the Mercury program, that was the single best investment America ever made.

**Chris Gammell:** Oh, yeah. Without a doubt. Everything we talk about on this show is directly tied to that.

**Dave Jones:** Exactly.

**Chris Gammell:** There is nothing that isn't – I mean – Exactly. Yeah.

**Dave Jones:** Yep. And I watched a documentary last night on the Large Hadron Collider. How, you know, how – It was like how it went from, you know, like building the thing to, you know, finally finding the Higgs boson and everything else, right?

**Chris Gammell:** Mm-hmm.

**Dave Jones:** And –

**Chris Gammell:** They didn't find it yet, did they? Yeah. Did they?

**Dave Jones:** Yeah.

**Chris Gammell:** I thought they disconfirmed that.

**Dave Jones:** Oh, did they? Okay. I didn't – I haven't heard a follow-up since. Okay. I'll have to check. Anyway. I'm sure people were screaming at us and correct. Whatever. Yeah. Yeah. Yeah, whatever. Anyway, yes, it was bigger pressman announcement saying, I think we found it, you know. Oh, yeah, yeah. Yeah. And everyone cheered and, yeah, right.

**Chris Gammell:** And then we forgot about it, yeah. Right.

**Dave Jones:** And science continues, you know, like, yep.

**Chris Gammell:** Well, we'll link in that documentary. I'd love to actually watch that because that's great.

**Dave Jones:** Yeah.

**Chris Gammell:** I was actually going through my email the other day and I found a link to a URL. Is the Large Hadron Collider blown up the world yet or something like that? Oh, right. Yeah, yeah. Yeah. It was like one of those.

**Dave Jones:** You can have a count, a number of days since the world has been blown up. It's just like you go there and it says, nope.

**Speaker ?:** Right, yeah.

**Dave Jones:** No. Yeah, I see that. Yeah. Yeah, it's good.

**Chris Gammell:** Oh, sorry. Has the Large Hadron Collider destroyed the world yet, dot com? Yep. Nope. It's great.

**Dave Jones:** Hats off to whoever did that.

**Chris Gammell:** Yeah.

**Dave Jones:** And anyway, yeah, somebody got up in this documentary, in the press conference and said, you know, I'm an economist. What financial benefit will come from this? You know, look, you have to have a financial benefit. And the dude just said, I don't know. And that's a good part about it. You know, like that's why we need to do it. And yeah.

**Chris Gammell:** I don't think, yeah, I don't think we're, I think we're going to preach to the choir on the benefits of hard science and investing in space travel. Right. If you don't agree with us, we would love to hear from you. Please tweet us. We are at the Amp Hour or Dave's at EEVblog. I'm at Chris underscore Gamble. We will promptly probably ignore you, but we'd love to hear from you anyways. You can write to us, feedback at theamphour.com, or you can give us more money than we already have on our Patreon page so that we keep spouting our ridiculous, know-nothing ideas. And you can hear us every single week. Anywhere else, Dave?

**Dave Jones:** Nah, that'll do it.

**Chris Gammell:** Okay.

**Dave Jones:** That was so professional.

**Chris Gammell:** Thanks, man. That was like an outro without doing an outro. All right. Talk to you next week. Yeah, to next time. It's because of my hair. That's why. I have broadcaster hair now. Yeah, yeah. Yeah.

**Speaker ?:** Yeah. Yeah. Yeah.
