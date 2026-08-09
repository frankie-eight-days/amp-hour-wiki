---
episode: 467
title: Stories from Supercon 2019
url: https://theamphour.com/467-stories-from-supercon-2019/
---

**Chris Gammell:** This is the Embarer Podcast. Released November 18th, 2019. Episode 467. Stories from Supercon 2019. All right, I am at Supercon 2019, and I'm talking to Sprite. How are you doing, Sprite? Yeah, I'm good. Thanks. Good to talk to you again. We've had you on the show before. Yep. And you did this badge. This thing is a work of art. I really like it. Yeah, it came out really well. Yeah. What was the genesis of, like, how did it all start?

**Super Nintendo:** So, as Mike said it, like, at some point there was something in the air. Seemingly, multiple people already asked about, like, can we do a badge with an FPGA and maybe a RISC-V processor? And seemingly, I was, like, in the third or fourth or something. And he was like, yeah, but, you know, FPGAs are really hard. And are people at Supercon going to be able to understand that? I mean, you always have a few people who just get it. And it actually took me a prototype. I prototyped up a RISC-V emulator plus a little BASIC interpreter and some graphics bindings and effectively programmed Pong in BASIC on more or less a virtual imaginary badge. And at that point he was like, yeah, if you can get that to work in hardware, then we should be good. So, yeah, at that point I started making the very first prototype.

**Chris Gammell:** Which I'm staring at right now. It's hand assembled. You said you have a 100% success rate?

**Super Nintendo:** Yes, yes, I can. Like, in all the BGAs I soldered up to now, I soldered successfully. All one of them.

**Chris Gammell:** Good. And what is the processor that's, or sorry, what's the FPGA that's on here?

**Super Nintendo:** It's a Lattice ECP5 45U something.

**Chris Gammell:** I saw you say 45,000 LUTs, right?

**Super Nintendo:** Yeah, yeah, yeah, 45,000 LUTs.

**Chris Gammell:** Yeah, that's pretty sizable, right? I mean, you fit two RISC-Vs and a PIC-24 in there.

**Super Nintendo:** Yeah, plus a graphics subsystem that's kind of sort of on par with a Super Nintendo. Plus an audio subsystem that's also pretty good. USBs in there. HDMI. Because, of course, you put HDMI in there. I mean, you've got to have the first on the batch. An interface to 16 megabytes of RAM. Well, there's a lot of stuff in there.

**Chris Gammell:** Yeah, that's great. I mean, I think that's a good measure of how big it is in general, right? I mean, it's just a sizable FPGA. Oh, for sure.

**Super Nintendo:** And we're not even using all of it. The thing is like 61% full, if I recall correctly. Got it, got it.

**Chris Gammell:** You know, so I've been interested in this. I'm kind of treating this weekend as like an opportunity to just try and get more tools in my toolkit.

**Super Nintendo:** Oh, yeah.

**Chris Gammell:** I think the Open, the Yosis stuff, we've had Clifford on the show. We've had Dave, FPGA Dave, on the show briefly. And, you know, the whole team that's working on all that stuff is amazing. But I think that like just having these as a way to deploy custom logic fast, too. That's another thing. It's like so fast to get all this stuff synthesized and onto a thing. It's just it feels like the future, you know?

**Super Nintendo:** Oh, for sure.

**Chris Gammell:** What is your take on like where you see it going?

**Super Nintendo:** Where I see it going, well, I kind of hope it just improves more and more. I think that the team, like the idea of being the GCC for FPGAs, at least they're going pretty far in that direction with the amount of FPGAs they support. Yes. They always supported the ICE 40 series. They support the ECP 5 series. I think there's going to be a talk at the Supercon on how they support the Xilinx Series 7 FPGA series.

**Chris Gammell:** That's Tim Ansell.

**Super Nintendo:** I think there's already some work going on to support like Chinese FPGAs, like the GoWin things.

**Chris Gammell:** I just learned about those. I did not. Those snuck up on me. I don't know where those came from.

**Super Nintendo:** But have you been around for a while? The company itself has been around for a while. They're doing multiple things. I think those guys are also the guys who make the STM32 knockoffs and who make like serial flash and stuff like that.

**Chris Gammell:** Giga devices.

**Super Nintendo:** Giga devices. Yeah, yeah. Okay.

**Chris Gammell:** Which is another thing. And they make a RISC-V now too.

**Super Nintendo:** Yeah, they do.

**Chris Gammell:** A Bumblebee core or something like that?

**Super Nintendo:** Yeah, yeah, yeah. At least it feels like they effectively took one of their arm things, just ripped off the arm and dumped a RISC-V in there. Yeah, that's great. Which is, I mean, valid.

**Chris Gammell:** Yeah, yeah. And then you have similar registers and see if it works. That's cool. That's an interesting future in that way, right? Of like this kind of swappable hardware.

**Super Nintendo:** Yeah, there's, I can see multiple companies going that way, just seeing, you know, if a RISC-V core makes sense.

**Chris Gammell:** Yeah. That's great. Well, speaking of cores, I mean, what's been going on? You're still at Expressive. Yep. What's been going on with that?

**Super Nintendo:** Well, let's see. This year we've had an IPO, which is good.

**Chris Gammell:** I did not know that, actually.

**Super Nintendo:** Well, we did.

**Chris Gammell:** Are you rich now?

**Super Nintendo:** No, unfortunately not. Well, you know, there's still time. It's true. No, there's, we've also been ramping up the CPUs. Sorry, the chips we're making. We've been developing a whole bunch of stuff in the background for the last years, but it's already been a while since we introduced the ESP32. So we're like on the verge of introducing the ESP32 S2. There's already some beta silicon out there. And we should have the final silicon of that, I think. Don't pin me down on this, but I think at the start of the next year. Oh, great. Okay.

**Chris Gammell:** Yeah, and people were excited about that because it's got the USB internal now. Yes. Definitely can simplify a lot of things.

**Super Nintendo:** I entirely agree. It's, I've been working on that, like, a fair bit. Just to have USB in there will probably simplify a whole bunch of designs.

**Chris Gammell:** It's literally like drop a chip now and it does all the things you, I was surprised that it went to single core, but that also helps with power and similar things.

**Super Nintendo:** Yeah, well, it's kind of, you've got to know about the way this is put in the market. Like, there's a whole bunch of manufacturers who think that the ESP8266 is looking a bit old and a bit simple. And, you know, it's nice to add Wi-Fi functionality to something, but it's too simple to be a standalone Wi-Fi microcontroller for their purposes. On the other hand, ESP32 is a beast with dual cores and lots of memory, et cetera, et cetera.

**Chris Gammell:** It's swung the heart the other direction, pretty much.

**Super Nintendo:** Exactly. So, the ESP32 S2 is kind of an in-the-middle device. It has a little bit less RAM. It's only single core. Obviously, there have been incremental updates to our IP as well, so it does get that. It's got USB. It's got a better PS RAM interface, stuff like that. We've upgraded SPI. So, there's a bunch of incremental updates there. But, in general, the thing is positioned to be kind of sort of in between the A266 and the ESP32.

**Chris Gammell:** Great. That's great. So, what about on the, oops, it's a little loud out there. Yeah, it is. We are in the, got a bunch of feedback during our survey this year. Like, well, we like when we interview people on site, but sometimes it's a little loud. It's like, oh, I know.

**Super Nintendo:** Yeah.

**Chris Gammell:** Yeah. It's like we're trying to run away from people. We're actually luckily in an office right now.

**Super Nintendo:** Yeah. This actually really isolates well.

**Chris Gammell:** Yeah. Yeah. Well, okay. So, you know, your handle is Sprite, and there's a lot of Sprites on here. I've never really done graphics stuff before, and that's been, there's been really good, like, kind of getting started docs and stuff like that. But what is, do you have background in doing all this stuff?

**Super Nintendo:** Well, technically not. I've been interested in a whole bunch of gaming systems and how they do things and, you know, how something, I mean, even a Super Nintendo only has a 16-bit CPU that runs at 3-point spare change megahertz. Really? I didn't know that. So, if you have graphics done the, like, in a naive way, but just having a frame buffer, like every single byte in memory equals a pixel in RAM, then first of all, you need a fair amount of RAM, at least at that time, and secondly, you need a fair amount of CPU power in order to push all those pixels.

**Chris Gammell:** Right, right. And then it's just like, and it's like, if the processor is doing it versus having, like, a specific device that's doing that dump or something.

**Super Nintendo:** So, the specific device would be, like, in the graphics controller and in both the SNES case as well as on the batch case, it can do a whole bunch of stuff with regards to compositing and overlaying, et cetera. You indeed have a bunch of sprites that you can just move around, so you don't need to actually paint them because the graphics subsystem will take care of it.

**Chris Gammell:** Yeah, so I guess when I think about, yeah, so, like, okay, so we're going to say, like, it's a 16, 4x4 thing, we're going to draw a checkerboard pattern, black, white, black, white, black, white, black, white, right? Yeah. So, in a traditional system without sprites and stuff like that, you would actually have to then hold all that stuff in memory, know that you're changing bit number 14, and then go draw bits 0 through 15 again, right? Yep. And so, the sprite allows you to basically, how does that work?

**Super Nintendo:** Well, a sprite wouldn't be a good fit for this. So, like, for instance, take the Mario game. Sure. You've got most of your basic graphics 2D primitives for a graphics subsystem around that age there. You've got your background, your actual level. That's all, that's large, as in, it's larger than the screen. Yeah. And it consists of elements that are fixed. They won't move relative to each other. So, it's actually a... The full canvas of what you can do. Exactly, exactly. Okay. So, you don't want to have a full canvas image in memory, because that would be way too big. Right. So, what you do is you have tiles. That's, like, in little images of, in the case of the batch, 16 times 16 pixels. And you effectively assemble all those tiles in a raster, so to say. So, by giving each position in the raster its own individual tile, you can draw graphics. So, you will have, for instance, tiles that make up a cloud, tiles that make up, like, in the pipes in Mario, you will have tiles that make up the ground. And you can effectively use those tiles to assemble a level.

**Chris Gammell:** And... So, then you know that the level is this big thing. Mm-hmm. But then it's, you basically are coding, like, it goes tile 1, tile 0, tile 0, tile 0, tile 2. Exactly. Okay.

**Super Nintendo:** So, the amount of memory you need to store is only the memory for the unique bits of your graphics, plus how you repeat those in the level, so to say. Okay. Yeah. So, that saves a lot of RAM, and that also makes drawing it easier, because it's effectively a level of indirection. Right.

**Chris Gammell:** You basically go out, grab that thing, bring it back.

**Super Nintendo:** Yeah, more or less. Paste it together. Yeah. Yeah. Yeah. So, those are tile layers. On top of that, you have the smaller things that need to move independently. So, for instance, Mario, like in any Goomba that passes along, stuff like that. Those are sprites. Those are individual images, usually tiles as well, so 16 times 16, or whatever, a fixed size. And you can effectively just give those a position independent of the grid that the rest of the level is on, and you can just place it. But the nice thing is that the actual drawing, again, the graphics hardware does that. So, if you want to move Mario, then it would effectively be update the variable that states where the Mario sprite is. Right.

**Chris Gammell:** He's jumping, and so now it's position Y. It goes from 0 to 20, or whatever it is.

**Super Nintendo:** Exactly. And if you do that, the hardware will take care of the rest. The CPU doesn't need to think about, like, oh, this is actually a Mario image. Right. That's all the hardware that does that.

**Chris Gammell:** And do I draw a green pixel here or a red pixel? Exactly. Exactly.

**Super Nintendo:** That's all hardware accelerated.

**Chris Gammell:** Interesting. And that was happening back in the 80s.

**Super Nintendo:** Yeah, very much so. They had to because having enough memory to store the entire... Super expensive. That would cost an arm and a leg, for sure.

**Chris Gammell:** Price fixing was a thing then.

**Super Nintendo:** Yeah. Yeah, back in the day. Yeah. Yeah.

**Chris Gammell:** Big money. Big money. I remember, like, opening up... I think it was a Game Boy.

**Super Nintendo:** Mm-hmm.

**Chris Gammell:** And it's just like... I think that one has a linear regulator on it, doesn't it?

**Super Nintendo:** No. Actually, the Game Boy has...

**Chris Gammell:** Is it a switching regulator on there?

**Super Nintendo:** Yeah, it's actually a...

**Chris Gammell:** I remember there was one that had, like, a linear regulator.

**Super Nintendo:** I was just like, whoa. There's some in there, but the Game Boy is actually pretty nice. It actually has a separate board made by Alps, if memory serves. That's the switching regulator. Okay. It kind of needs that because it needs minus 20 volts or something for the display to work. Got it. Okay. So there were a few consoles that used a linear regulator. I think the... At least the Atari 2600 used a linear regulator.

**Chris Gammell:** Yeah. It's wall-plugged, at least, though, right? Yeah, yeah, yeah. That helps.

**Super Nintendo:** I wouldn't be surprised if, like, in anything up to the SNES used a linear regulator because, you know, it wasn't that power intense. It's super cheap, too. Exactly.

**Chris Gammell:** Yeah. Yeah. Well, getting back to this thing, I mean, so what was your experience with the RISC-V and the ECP-V prior to this? Was it kind of just figured out it was going along or a dense project?

**Super Nintendo:** Yeah. I had some, like, FPGA experience, like, in general. I've messed around with FPGAs before. Never got around to building an entire SOC from the ground up. But, you know, I knew my VACL. I knew my VariLog. So that bit I had. The ECP-V I had no experience with. Like, the first prototype you see there is actually the first ECP-V board I own. I don't really... Well, that one worked. So I didn't need to buy an actual, like, in dev kit for the ECP-V. Yeah.

**Chris Gammell:** Well, in the bitstream, so bitstream for that, it went Ice40 was first and then ECP-V was later. Yeah. How much after the time when the ECP-V bitstream was released that you started working on this? It had been out for a while or?

**Super Nintendo:** I don't know. I think I made sure that it was more or less stable and usable. But I don't exactly know the time span. It may have been a year or something or half a year. It's, like, yeah, pretty soon. But, yeah, most of it seems supported and stable. To be fair, at that moment, it wasn't entirely, like, it's nice how the toolchain just grows and improves, like, as I went along that year. Yeah, right, right. And there are still some things in the repo that are in there, but are actually workarounds for things that the toolchain didn't do back then.

**Chris Gammell:** Ah, really?

**Super Nintendo:** Yeah. So I could actually delete them and fix those in the more obvious way. Yeah, right.

**Chris Gammell:** Yeah. That's great. And then, so it has two RISC-Vs in there. Why does it have two RISC-Vs and a PIC-24?

**Super Nintendo:** PIC-16, actually. PIC-16. Oh, I thought it was PIC-24. It's the old school PIC-16C84. Got it. So the two RISC-Vs are in there because... Why did I put two RISC-Vs in? Oh, yeah, I know. So the RISC-V core that's in there is a Pico RV32 core. It's a really nice core. It's written in pure varilog. It's formally verified. It's used all over the place.

**Chris Gammell:** That's the one that... What's his name? Yeah. Did, right?

**Super Nintendo:** Exactly.

**Chris Gammell:** Formally verified probably because of Symbiosis. Oh, yeah, for sure. Right at EDA.

**Super Nintendo:** But it's really nice and simple. And my idea for the batch would be that it's something that people should be able to hack. And if I use, like, in three different high-level languages only for the FPGA load, then it's probably going to be too much for people to just try to read up in one weekend. So I wanted to have something that's very log-based and is simple and, you know, there's some documentation out there. So Pico RV32. The problem with the Pico RV32 is that it's... Well, the implementation as is on the FPGA is slow. It's a CPU that is meant to have a high clock speed. And in this FPGA, it only gets, like, in a medium clock speed. But in order to get a high clock speed, the trade-off is that it has a lot of cycle per instruction. So even something as simple as a load, it takes, like, three or four cycles, where most normal CPUs would take, give or take, one cycle per instruction. So there's a lot of slowdown. And that causes the memory bus, for instance, not to be utilized to the maximum. So my idea was, okay, I'll just plunk in a second RISC-V core because the memory bus can handle it. And that way, we get twice the speed.

**Chris Gammell:** Yeah, right. And so I remember you were showing... So you were showing this morning, you were showing some of the gotchas and, like, how the access works. And I remember you said that there was... You said there was the four-bit access to the bus, but that was because of 32-bit.

**Super Nintendo:** Yeah, there's... Well, that's actually a standard thing. It's just something that you need to know about the bus. Like, the RISC-V is a 32-bit processor, so it has a 32-bit bus to the memory. But it can... I mean, obviously, it can also read and write 16 and 8-bit values. And the way it implements it is it'll send a 32-bit value over, but it'll tell you using the right strobe, oh, I only want to write this byte of the 32-bit value. You can ignore the rest. And that's the trick, more or less.

**Chris Gammell:** Right. So instead of doing masking...

**Super Nintendo:** Exactly, exactly.

**Chris Gammell:** Yeah, that helps with instructions.

**Super Nintendo:** Yeah.

**Chris Gammell:** So I remember something about, in that part you were talking about, there was something that felt like it was like two 32-bit... It was like two reads or two writes? I thought there was something in there. Is that out there talking on the bus, or is there a...

**Super Nintendo:** Yeah, there's actually where you would normally, if you go back to the Z80 days and stuff, you would only have one bus, and that would be bi-directional. So if you read from a peripheral, the data goes over the same bus as if you write to a peripheral, which is really nice. But FPGAs, well, it needs tri-stating. Like, if the CPU speaks, then the peripherals should shut up and tri-state their bus. That's right. But FPGAs don't really do that, at least not nowadays. There used to be silenced processors way, way back that could do that. But because of a variety of reasons, they don't do that anymore. So a lot can only have an output or only have an input. So in order to make that work, you need two buses. Like, in one bus from the master to all the peripherals, and then from all the peripherals, there's like a separate bus that goes into a multiplexer that goes back into the master. Just because you can't do that. Got it. Got it. That's cool. Okay.

**Chris Gammell:** So what else should we know about the badge? I mean, there's going to be obviously a lot of hacking that happens over this weekend. Sure.

**Super Nintendo:** It's really open. People can hack so much with it from the hardware. I mean, you can solder to the badge, obviously.

**Chris Gammell:** Oh, that cartridge thing? That's cool. Yeah, yeah, yeah.

**Super Nintendo:** We have a nice cartridge.

**Chris Gammell:** To explain what it looks like, maybe, too. That helps for people listening.

**Super Nintendo:** Yeah, audio only, right? Yeah, that's right. Yeah. So the cartridge is a PCB that slots into the back of the badge. Like, the badge kind of looks like a Game Boy, and the cartridge would be like the cartridge, as in the game cartridge. The cartridge that you get with the badge is effectively a prototyping board. So it has lots of pads in there that are connected, and you can just solder your own random stuff on there. And it also has a little bit of flash on there.

**Chris Gammell:** I really like that. And it shows up. Also, it enumerates and shows up when you plug in the USB.

**Super Nintendo:** Yeah, yeah, yeah. Exactly.

**Chris Gammell:** It's super easy to just drop an application on there.

**Super Nintendo:** Yeah, yeah, yeah. The entire idea was that, like, previous years, the batches varied a little bit in programmability. They went all the way from, I think, the first or the second batch, also just enumerated as a USB mass storage device. But later on, either you needed a pick kit or something else, and I never really liked that. I mean, especially since I'm also a Linux user, and most of that embedded stuff tends to be slightly Windows-focused. It's getting better, honestly.

**Chris Gammell:** A lot of the tools are getting better.

**Super Nintendo:** True, true, true. It's still not entirely there, though. Yeah, I agree. So I was like, for the batch, simple and stupid. There are USB protocols that are, like, standardized. So you have DFU for the low-level stuff that you want to update. And for the rest, there's a file system. If you plug the batch in, it looks like a USB stick. Tiny USB stick, but still a USB stick.

**Chris Gammell:** Oh, 14 megabytes. Okay. Yeah.

**Super Nintendo:** And the cartridge, yeah, just enumerates as a second USB stick. And you can just drag and drop your files and your programs onto there. And the idea of also putting some memory on the cartridge is that, well, first of all, even if you don't use the prototyping space, it's probably fun just to be able to give your game or your whatever to someone else by just passing the cartridge. Yeah, that's totally awesome. But also, if you do put stuff on there, say, like, in the canonical example would be if you were to put, for instance, a bunch of DACs on there and a front end to make a scope, you can put both the bitstream that has the interface to the DACs, like in hardware, you can put that on the flash, plus you can put the application that actually shows you the scope user interface, you can put that on the flash. And that way you can turn any random batch into a scope by just inserting the cartridge and booting from the cartridge. Right.

**Chris Gammell:** So it makes the entire thing, the entire batch is reconfigurable with a cartridge. Exactly. Which is pretty crazy. Yeah. Yeah, that'll be interesting to see what people do with that.

**Super Nintendo:** Yeah, I haven't got time for it, but one of the things you could do is, for instance, take, there's some IP out there, for instance, from people who converted, like in a Game Boy to Verilog, so you can put it in an FPGA. Right. Theoretically, what you could do is build an interface cartridge with the cartridge connector for the badge on one side and an interface for a Game Boy cartridge on the other side. And if you slot it in and then slot a Game Boy cartridge in there, you affect the...

**Chris Gammell:** A cartridge-in-cartridge kind of thing?

**Super Nintendo:** Exactly. And then you can play that Game Boy game because the FPGA all of a sudden becomes a Game Boy and it can read the original Game Boy cartridge through the interface logic.

**Chris Gammell:** Right, and in theory, if there was a Sega Game Gear Verilog, you could then plug in a different cartridge. Exactly. It then becomes a Game Gear and you could play a Sonic or whatever. Exactly. Yeah, that's, you know, it's really hard. I remember the first time I started, like, learning and thinking about FPGAs. It's so hard to visualize at first, you know, and it's hard to remember what that feeling is like, especially coming from, like, a microcontroller background and things like that.

**Super Nintendo:** Yeah, it's so flexible.

**Chris Gammell:** Yeah.

**Super Nintendo:** I actually have one line in the Verilog code that I really like. It's something like a parameter CPU count equals two. And the nice thing is that if you look at that line naively without knowing anything about programming, then you make a certain assumption. And then if you know how to program, you're like, nah, that's probably wrong. That's just a constant for something. Yeah. But in this case, your initial assumption would actually be right. If I put a three in there, there would be an extra core that shows up in the FPGA. Oh, really? Yes. It's just a, literally just a variable. It literally sets the amount of cores that you have in your SoC. Right. And it errors out when you put in 64 because you... Well, yeah, you wouldn't have the space. And in general, above a certain count, it doesn't make sense because the memory bus gets so constrained that all the CPUs are waiting on each other.

**Chris Gammell:** But in theory, that's the flexibility of it all. Yeah. Right.

**Super Nintendo:** Yeah. Just the fact that you can write such a line and it does actually what you think it might do is weird.

**Chris Gammell:** I mean, well, I mean, the idea of like, if you say you could take it to a large number, right, and they actually did work and you had the memory for it and everything, like, then you have that many CPUs, you basically become a GPU, right? And that kind of like the idea of like, I mean, in theory of like having lots of parallel...

**Super Nintendo:** Yeah, yeah, yeah, for sure. Yeah, you can do that.

**Chris Gammell:** Yeah. So that's, yeah, it's just, there's the parallel nature of it. Like, that's one thing that I think is hard, was always hard for me to wrap my head around.

**Super Nintendo:** Oh, yeah, for sure.

**Chris Gammell:** And then, and that's, I always try and like talk about like streaming data and like thinking about like, like putting data through a pipe, but then there's like little release valves and it, you know, it's trying to do stuff as it's still streaming. It has to still be moving through the pipe.

**Super Nintendo:** Yeah, it's, it's, it's, it's more like mechanics than it is like programming actually. Yeah, right, right. The way everything happens in parallel. It's a Rube Goldberg machine, right? Yeah, for sure.

**Chris Gammell:** Yeah. Yeah. Continuous Rube Goldberg machine. Yeah. It's, it's, it's, it's tough to think about, but then I think the, the, the fact that then, okay, then they're also, you're also able to put logic on there that, you know, is a CPU. It's like another layer. There, I finally remembered what the name of the, I used to work on the Microblaze. Do you ever use those?

**Super Nintendo:** Oh yeah, that's Xilinx, right? Yeah.

**Chris Gammell:** Xilinx and then Neos is the Altera one someone was talking about earlier. And they're always like, they're, it's been possible for a while to do this kind of thing. Oh yeah, certainly. It's a new thing, but it feels like this is better.

**Super Nintendo:** So, so the nice thing about RISC-V, like there have been, if you, if you go to opencores.org, you can download like in CPUs and all shapes and forms. Yeah, you can get an M0, right? You can get like a. Nowadays you can get an M0. Yeah. But at least before RISC-V was there, I feel it was really hard to get an IP that was unencumbered by, if I use this in a product that grows anywhere near big, then I will have Intel or ARM or whatever. Or open a can of lawyers. That's right. Yeah. So, or, or was actually usable. Like you would have a few CPU cores that were really nice, but they were made by one random guy who also developed the ISA and there is a GCC, you know, fork that never has been mainlined, that has been updated like 10 years ago. That's right. Yeah. That, that, that, that, that's all, you know, those were the choices you had. Or like the third choice was to go with something antique like a Z80 and. Right, right.

**Chris Gammell:** 8051 with, you know, hopefully again, the GCC is all set up for it.

**Super Nintendo:** Exactly, exactly. But the thing that RISC-V has done is allow, so just as a user, what I see is that there's an explosion of RISC-V processors in all shapes and forms from, from really small to, to, to really large and most of them I can just download and plunk in my design and all of them are RISC-V. So I can just go and download the RISC-V GCC thing, which is actively being developed on by a lot of people, which is stable, which is, you know, solid.

**Chris Gammell:** Well defined and open and yeah.

**Super Nintendo:** Exactly. And, and, and because everything is open and just given away for free, I don't have to worry about like in a can of lawyers ending up at my front door. Yeah. So that's, that's the big advantage that I think RISC-V has. Yeah.

**Chris Gammell:** Right. It's like agency and it's also like, uh, yeah. Freedom to. Yeah, for sure.

**Super Nintendo:** It's, it's, yeah, you get choice. You get, uh, like in the freedom to pick something because there are actually multiple choices there and, and you get good tool change support.

**Chris Gammell:** Yeah. And I think that's another thing too, is like having focus too, of like having focus from the community, having, you know, people working on it. It's like this weird kind of like buzz that's kind of like behind you. Like, oh, well it's probably going to be okay versus like, you know, like otherwise it's like you talk to a bunch of vendors and then it's like a feeling of like, well, it seems like they're supporting their customers and I'm paying a lot to pay for their support. And, you know, like.

**Super Nintendo:** Yeah. It's, it's like, you know, the other thing is that it's not, not, not unprecedented that for instance, a, an architecture has been mainlined in GCC and then drops out because, you know, there's, there's no one around. Falls in favor. Yeah, exactly. And, and, and, and the manufacturer doesn't really care about the CPU thing. So it doesn't send any patches and it kind of sort of erodes away. And at some point the maintainers just go like, yeah, it's not going to be in the next release. Right, right.

**Chris Gammell:** It's a natural selection for, for processors.

**Super Nintendo:** Yeah, more or less.

**Chris Gammell:** Yeah. That's crazy. Well, Sprite, thank you for this great badge. This has been great. It's good to see you. It's good hearing about everything you're doing. And thanks for telling us about the badge. Hey, you're welcome.

**Super Nintendo:** Hello.

**Chris Gammell:** Hello. We're back from a, in a very quiet room at, at Supply Frame during a Supercon 2019, thankfully. And I'm here with...

**Dave Jones:** Sylvain Minot.

**Chris Gammell:** Sylvain Minot. Sylvain. Sylvain. And what, what are you working on here?

**Dave Jones:** Um, so I'm doing great at the moment. Sylvain Minot. And I'm helping with the FPGA badge workshop, um, that are, you know, helping people hack on the, the brand new FPGA. This thing is beautiful.

**Chris Gammell:** It's really nice.

**Dave Jones:** It's really nice. Yeah. And it's very powerful as well, so.

**Chris Gammell:** Yeah. Well, so we just, I just talked to Sprite. I just did an interview with him. And, uh, it's big. I mean, like 45,000 LUTs is like not a small part.

**Dave Jones:** No, no. It's definitely, um, a very decently sized FPGA, um, and half of it is still free despite everything we've crammed on it. So, which means that if people want to do, like, advanced applications, stuff like that, they won't run into, um, like, space limitation.

**Chris Gammell:** Yeah. Anytime soon. And you did the, uh, the DFU for this thing?

**Dave Jones:** So, yeah. Uh, so what I did for this badge is, uh, the DFU bootloader. Um. What does DFU stand for? Oh, yeah. So, uh, DFU is, uh, device firmware upgrade. I think. Uh, which is just a standard way to, um, upload new firmwares onto the badge, basically. So, it's, uh, what allow people to replace the FPGA bitstream and the, um, the, uh, soft core application that is running on the badge with hopefully minimal risk of actually breaking the badge and needing a JTAG adapter to restore it. That's good.

**Chris Gammell:** Yeah. I think I've used some particle devices that have that. There's a bunch of devices that are in the market that have that. But it's like, hold a button. It goes into some blinky mode. And you're like, okay, now we're good. Exactly. Yeah.

**Dave Jones:** Yeah. And, um.

**Chris Gammell:** So, what did that take to actually write that for, for this, uh, scenario?

**Dave Jones:** Well, um, not that much because I, so I, I'd previously written a USB device core for FPGA, which is actually the device, the USB core which is used in the main firmware as well. Okay. Um, and so I already had, uh, this, uh, USB core and a DFU enabled firmware for another device for an ice 40, uh, FPGA. Oh, okay. And so I mostly had to adapt to, you know, uh, and so I mostly had to adapt a few things for the ECP5, um, and then try to optimize it for the badge, uh, basically make it faster. Okay. Try to minimize the, uh, the flash time.

**Chris Gammell:** Okay. Yeah. Yeah. Yeah. Yeah. That's interesting. So, so this is like a piece of IP that you had that you use on other projects.

**Dave Jones:** Yes.

**Chris Gammell:** And it was repurposable.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** So what does that process look like? Because like that is kind of the promise of, I mean, I guess it's the promise of even C and writing, you know, being able to, you know, retarget devices and, you know, port stuff. But like FPGAs kind of take that to another level.

**Dave Jones:** Yeah. Yeah. Definitely. So what it took, uh, in this specific instance, um, is there are a few, um, so you, you described your, you know, your, uh, your hardware in, uh, HDL, right? In this case, Verilog. Um, most of it is generic and, uh, the synthesis tool is going to do the work of translating that generic description into, uh, hardware specific, um, primitives. Uh, but for some of them, um, the tool isn't really ready yet to do it. Perfectly. And so you help him, you help the tool by instantiating primitives. Uh, in this case, the, the two things that were instantiated manually were, um, block ramps. So in the FPGA, you have a, uh, like a small amount of ramps, um, that you can use that they're really small memory, like four kilobits or 16 kilobits and that kind of stuff. And these are, uh, vendor specific. Uh, right. And so I just had to replace the specific primitive that I was using in the, for the ICE 40 by the equivalent for the ECP5. Um.

**Chris Gammell:** And when you say primitive, is this almost like a reserved word in C or something?

**Dave Jones:** Yeah, exactly. It's, it's like, uh.

**Chris Gammell:** It's like a magic word to just use what the Xilinx version is or the Lattice version is.

**Dave Jones:** It's basically, uh, like, you know, Verilog, it's a, it's a bunch of modules that you connect together, right? And you describe those modules. And some, some of these modules, you actually, they are actually like black boxes that will just get converted to actual blocks in the hardware. Yeah, right. They're just there. They exist.

**Chris Gammell:** Right.

**Dave Jones:** You don't have to describe it.

**Chris Gammell:** It's like an API for existing hardware. Exactly. Yeah.

**Dave Jones:** And so the kind of hardware block that you would find in the FPGA are, well, mostly the RAMs. You also have, like, a DSP block, like hardware multipliers. Max, right? I remember those. Yeah, multiply, accumulates, right? Multiply, accumulates. Yeah. Um, and, and the other one that I had to deal with here is the IO blocks, like how to talk to the outside world is often, um, specific to a, to an FPGA family. Um, and so that was really minor adaptations. Um, and yeah. And the rest was, you know, dealing with the specificity of the badjack, which pins, you know, connected to the flash. Right, right. The mapping to the pin that it is. Mostly it's dealing with the external, external world.

**Chris Gammell:** Right. Whatever sprite decided the pin would be hooked up to. Exactly. Yeah. Yeah. Okay. Interesting. Yeah. And the, uh, what's the other, oh, CERT is the other one that I've, I've, I think I've worked on in the past. Isn't that like usually like a targetable block? Like a S-E-R-D-E-S? A serial? Oh, yeah, yeah. A serial serial. A serial serial.

**Dave Jones:** It's actually part of the IO. Yeah. Oh, right. Most of the, most of the time the IO, they can, um, you know, just take a signal and put it to the outside, or they can also, um, have a flip-flop directly inside the IO to kind of guarantee the, the, uh, the timing, you know, so you have guaranteed a set up at all times. Right. Uh, that kind of stuff. And then sometimes you want to take multiple bits and serialize them very fast. So you input eight bits and then the, the IO block will basically serialize them into, uh, eight sequential bits for you. That's the, that's kind of stuff. Uh-huh.

**Chris Gammell:** Yeah. That's great.

**Dave Jones:** That's great. That's what's used on the badge for the HDMI, for instance, I think. Right. Right. Yeah.

**Chris Gammell:** Okay. And so you do, you do this professionally too?

**Dave Jones:** Yes. Yes. I do that. Um, it's actually my, my first job was, uh, doing FPGA stuff.

**Chris Gammell:** Um, so, so in a commercial context, I mean, we don't need to talk about the specifics of your companies, but like they, uh, but do you use the open tool chains for that? Or what is, um, what is your take on the industry with FPGA?

**Dave Jones:** So at the moment, uh, I don't use this, the, the open tool chain, uh, synthesis, uh, for my work because I mostly work on Xilinx and the tool chain is currently not, not there, not in a state that I can, uh, uh, use it professionally. I do use, um, iVerilog, for instance, like for simulation, um, I use that because, well, honestly, model sim just costs too much money. Yeah. True. And iVerilog is perfectly suitable for my needs. And so I use that. Um, but if I, um, the state of the tool chain for the ICE 40 and for the ECP5 is starting to reach a point where it would actually be usable for, uh, some commercial projects.

**Chris Gammell:** Right. So if you had a commercial project that was, had a lattice part on it.

**Dave Jones:** There are, there are, you know, something it doesn't handle yet, um, perfectly. Um, mostly there are very advanced features like dealing with multiple, uh, multiple clock domains. You have to be able to constrain, uh, the, the paths between different clock domains. At the moment, the tool will report them, but doesn't allow you to constrain them. Uh, and the other thing is IO timing. Uh, so when you have a, um, signal inside the FPGA, you need to know, you know, how many nanoseconds it's going to get to the outside. Yeah. Uh, that kind of stuff, uh, when you're talking with, uh, high speed interfaces. Um, and for that step, we actually still have to, um, rely either on the proprietary tools, um, or just open.

**Chris Gammell:** Take a shot. Yeah. Yeah. Right. That's, that's a tough, tough selling business, right? Where you're like, no, this needs, this needs to work. Yeah, exactly. Yeah. Yeah. That's true. Hmm. Well, uh, it's interesting. Like one of the things that's going to be happening this weekend is Tim's going to give a talk about, um, Tim Ansel. Yeah. We'll be giving a talk about design links. Yeah. Seven is, uh, seven series. I don't actually know. Yeah. The seven series. Yeah.

**Dave Jones:** I mean, I think, or the architecture for the seven series is pretty similar.

**Chris Gammell:** Okay.

**Dave Jones:** And so I think they're targeting one specific part at the moment, but most of it will be applicable to translate. Yeah. Yeah.

**Chris Gammell:** Okay. Okay. Huh. So what does it look like then when you're, um, so now you're switching back and forth between like open tools and proprietary tools. What does that look like then for you? Is it, is it kind of just you're used to it or what does it feel like?

**Dave Jones:** Yeah. I'm kind of used to it because, um, ever since I've been, uh, using the, um, so I'm using mostly the design tools, uh, for, uh, work, but I never use the GUI. Like my flow was always make file based and using the command line tool and stuff like that. So except for the fact that, um, it takes a little more time to build. Uh, it's pretty much the same. Like I just type make at the end. I've got my bit stream, right? Yeah. It's just, uh, yeah. I, you only don't, yeah, I need a license basically. That's, that's, that's, that's, and I need to download like what 80 gigabyte. I think that is still a thing. Um, but other than that, it's, it's fairly similar, um, at the moment, at least for me, it, it, the setup is much, you know, if you start from nothing, it's much easier with the open source, uh, tools, I think, uh, because getting a working make file based flow for the, um, the propria tool was, uh, yeah, it took some time at the beginning, but no, I have it and it works. Um, if you're familiar, if you're familiar with, uh, TCL, it might actually be easier for you to use Xalings because everything is TCL based. That's right. So it kind of depends.

**Chris Gammell:** It's TCL for people that haven't seen that before. Yeah. It's, I remember the first time it was like TK, TCL, what, what the hell is this? You know? Yeah. And, uh, but that's like the scripting language that a lot of the FGA uses.

**Dave Jones:** Exactly. Everything is based, uh, and it's, yeah. It's like a whole, it's not a holdover,

**Chris Gammell:** but it's just a, it's the chip industry in general uses it a lot.

**Dave Jones:** I think, I think so. I mean, I'm not, I've only been in the chip industry starting with Xilinx, so I've only done then, but I've been told that, yeah, it's, uh, like a historic thing that just continues up to today. Right. Well, I mean, yeah, there's

**Chris Gammell:** so much invested stuff there, so that makes sense. True. So when I saw, I saw you at, uh, CCC camp or CC camp, I guess, um, you were doing some Osmo comm stuff there too. Um, uh,

**Dave Jones:** yes. Oh, this camp? Yeah. Yeah. Yeah. We saw each other there briefly. Yeah. Sure. Yeah.

**Chris Gammell:** Of course. I think you were working on some of the, um, the cell service stuff, right? That

**Dave Jones:** was there. Yes. So, uh, well, I wasn't directly involved in running the cell service, the cell service at, uh, at camp that was handled by, uh, another team. Um, I was just working on different, uh, projects. Actually one of the projects I'm working on at the moment for Osmo comm is sort of related with the CP five. It's, uh, we're trying to use the CPRI radio heads. Uh, so, um, in modern cell networks, you will have a, what's called the radio head, which is basically the software defined radio that you're going to Mount near the antenna. Oh, okay. And then it has like a fiber connection to the base band unit, which does all the protocol

**Chris Gammell:** stuff. Oh, okay. Okay. And so it's basically piping already encoded data. Exactly. It's, it's

**Dave Jones:** piping IQ data basically, uh, through fiber. Oh, wow. Um, and then the radio amplification

**Chris Gammell:** and all the, the putting it into amplifier. Well, I guess that whole signal chain is, is

**Dave Jones:** the radio head. Exactly. Okay. And so we're trying to use those radio heads on the, on their own and talking to them, uh, using an, uh, an ECP five. Wow. Um, and CPRI is, is, is the standard to do that. And it specifies a standard, um, like sample format for the IQ data. But of course there is also the encapsulated vendor specific commands. Okay. Because, um, like to start up the radio at Talib, uh, what power to transmit, uh, what frequency to transmit on. All of that is not specified, which I knew we actually need to find a way to sniff a multi gigabit link to, uh, see exactly how do this. Right. Right. Cause you could just copy the package you're saying. Exactly. You need to see what they are first. We have both side and we're trying to basically sniff the link between using the ECP five. For that gigabit link to the, yeah. Wow. I mean, the ECP five is a variant, uh, with gigabit transceivers. And so we basically plug one SFP on one side, one SFP on the other, plug both. That's the theory. I mean, at the moment we haven't actually tried it yet. We're, we're, we're trying to get the, uh, the third S up and running with the correct rate and everything to get the link up. Wow. And, uh, sorry, SFP is SFP is, uh, like a small fact pluggable. It's like those small fiber modules like that are standard that you just plug off the shelf. Yeah. They're off the shelf thing. You can buy them for like five bucks on eBay. Okay. They, they take

**Chris Gammell:** the electrical signal and convert it to the optical thing. Cool. That's great. How'd you

**Dave Jones:** get involved in that? Uh, oh wow. I can't remember. Uh, in a smoke home or in the, in the, in that particular. Well, either one. Yeah. Yeah. So, um, that particular project, honestly, I don't remember. Um, I think I was just curious about how the CPRI radio heads work because they, they became the, the great radios because they, they have like, uh, powerful amplifiers, great filters, like a, it's a very good hardware. Yeah. That sounds like you

**Chris Gammell:** could do any, I mean, software defines, you could do a lot of things with it. And you

**Dave Jones:** can buy them used for like 200 bucks or something. Oh wow. Yes. And for that, you get like an 80 watt amplifier that can transmit with, wow. And like multi gig kind of like multi gigahertz kind of. Yeah, exactly. That's a, with like a wide bandwidth. I think the, some have like up to 80. You could really make the FCC upset. Yes. I mean, it's good you don't. I mean, yeah. But, uh, yeah, our goal is obviously to be able to use those radio heads with the, the open source base station we have for GSM, LTE, like a SRS, LTE, that kind of stuff. Yeah. Cause if people

**Chris Gammell:** don't know at a chaos camp and then one year at tour camp, I think as well, they have maybe

**Dave Jones:** at Congress too, do they have this? At Congress we do GSM. Yeah. Yeah. Yeah. So it's like a totally on its own network, right? Yeah. Yeah. We, we run, uh, um, GSM network for several years. Uh, for a couple of years now, we also run a 3G network and for the first time at a camp this year, we actually run an LTE network in addition. So we had 2G, 3G and 4G coverage at the camp. That's trippy, man. Uh, using, um, yeah, open source, uh, software. Yeah.

**Chris Gammell:** But not 5G because in my opinion, 5G doesn't exist yet. Well, I haven't, I haven't, yeah, I haven't seen anything yet. Uh, yeah. Yeah. Sorry. I just love 5G. Yeah. It just doesn't exist. It's just not a thing yet. I know it's a thing, but like, I haven't seen it yet. Yeah. Right. Right. Right. Uh, yeah, that's, that's cool though. Um, so, uh, I lost my train of thought already. Uh, Osmocom. Oh, that was what it was. So Osmocom, I had first been introduced to that through, I think HackRF also ties into that. Um, so wait, I mean, there was some of like the, I think maybe it's the receiver. They have a driver. The driver.

**Dave Jones:** So the, the story behind, uh, that is a, it's a little funny. So a long time ago, um, or some people in Osmocom, they, we wanted to make like a very cheap receiver only SDR. Okay. That's what that was called Osmo SDR. Okay. And that was, uh, like, uh, an arm with an external ADC and an Elenix tuner or something. Yeah. And we've, we were working on that, the firmware for it and a new radio driver for it. And not long after, I mean, not actually at the same time, like roughly the same, in same timeframe. Um, uh, Steve, uh, Steve McGrath, um, actually, uh, you know, made, um, actual SDR basically. Oh yeah. Yeah. So it's like finding those. Yeah, exactly. And so at that point that kind of made the Osmo SDR project a little bit irrelevant because there was no way we were going to compete in price. 20 bucks or whatever it is. Yeah. With, with, with that. Yeah. And although the, the receiver was better, the ratio, you know, price performance wasn't, uh, quite there.

**Chris Gammell:** So that, uh, yeah, it says, I mean, like even just a distribution kind of thing where you

**Dave Jones:** have all of these DVB tuners that are out there. And they, at the time they were using the ATLS, yeah, we're using the same two tuners, the E4000 that we were using. Oh really? Okay. Yeah. So, um, so yeah, in the end, uh, um, the, the, the new radio driver that we made that was called GR Osmo SDR, uh, uh, uh, Dmitry Stolnikov, uh, basically added an option in it so that it could use either the Osmo SDR hardware or the RTL SDR. Uh-huh. Uh, and then some people, yeah. And then people started using that in the new radio project, right? To interface with the hardware. Yeah. And then some other SDR came out. I think possibly the ACRF right after that to be able to reuse all the same, uh, flow graphs and applications that were already existing. It just added ACRF support into GR Osmo SDR. Yeah. And then basically every SDR that came after that, they just, yeah, the Lime and all of those. But it always kept the name GR Osmo SDR and. That's good. That's branding right there. Yeah, exactly. Um, yeah. And, uh, and what's funny is that for a long time, I don't know if it still does that, but for a long time, like when you installed it with the, uh, new radio, uh, like installer or the, it actually still pulled the, the library and driver for the Osmo SDR hardware. Oh yeah. That five people in the world have, but everybody has

**Chris Gammell:** support for it. Yeah. That's great. Well, you know, if it ever makes a resurgence, you know, it'll be, yeah. Smart people will just target it and pretend it's that thing and then it's good to, good to go. Yeah. That's pretty much a tie between. So what, what does Osmo come in the first place? I don't actually know the genesis of the group. So it kind of

**Dave Jones:** started with, um, Harold, well, and it is par like, um, I think it was at, uh, our, so the, uh, uh, hacking at random, I think it's 2009 or something. Okay. They, they created this project called open BSC, which was using the BS 11 base station to run the first like open source based GSM network at a hacker conference. Um, it was kind of, you know, compared to what we have today, it was really primitive code and it was barely initializing the BTS and allowing calls or SMS. I don't, I wasn't there, so I don't remember. Um, and then meeting up with, um, with Harold, uh, I think I met him at 2063 at the Congress. Um, wow, that's almost 10 years ago.

**Chris Gammell:** Does that make you feel old? Yeah. Yeah. It keeps hitting me. You know, with 2020, like creeping around the corner, I'm like, Oh, I was like, you know, remember when they were playing Prince's 1999 and everyone's like, Oh God, this song is so old. That was 20 frigging years ago. You know, I'm just like, Oh God. Anyways, sorry. Go on.

**Dave Jones:** Yeah. Yeah. So yeah, I met him there and, um, we, I started working on open BSC and, you know, improving things and adding support for other features. I don't remember exactly what I worked on at that time. And another project was started, uh, that was targeting the kind of the other side, which is like making an open source baseband firmware, sort of the phone side. Yeah. And at that point, uh, we were looking for a, for a name kind of, uh, to, to put all of these like, uh, open source telecom project, uh, under like an umbrella brand. And we came up with the name, uh, open source mobile communication, which is like Osmocom. Yeah. That's, that's where the name came from. And originally it was like open BSC and then, uh, Osmocom BB, that Osmocom baseband. Right. And then other project came and, uh, were added on top and under the same umbrella. Now, if you go to osmocom.org, you have like a bunch of projects. The most active ones are still the GSM and core network kind of, uh, things, but we have, uh, we worked on Tetra. We worked on GMR one, which is like satellite phones. We, uh, worked on a bunch of, uh, it's always interesting to me because

**Chris Gammell:** it's like, it feels like telecom is such a closed off industry. Obviously there's people working on it, but like the people that are willing to talk about it and like, it feels like a ton of reverse engineering because you have to, you're not going to get someone to be like, Hey, what were you doing there? No, I'm not telling you that. That was actually

**Dave Jones:** one of the goal of, uh, of Harald is that, um, he, there was a lot of people working on, you know, um, like wifi stuff, basically like wifi security and that kind of stuff. And nobody looking at, uh, a ton of other telecom protocol that are used by, you know, millions, billions of people. Uh, and nobody was looking at them. And I remember the first

**Chris Gammell:** year this, the, the, the towers got spoofed at DEF CON or something like that. Everyone's like, what? Oh no, you can, you can get our cell phones too.

**Dave Jones:** Yeah. A lot of things that people don't realize. And, uh, and so, yeah, the, I think the goal was mostly to get people to looking at that, uh, because a lot of those protocols, they're not actually, um, more complicated or, um, or secure or, and a lot of them are actually documented. Like, because you have to have interoperability and between and thing, you can actually, uh, most of the time the standard are available freely. Sometimes you have to like buy them, but it's just like a few hundred bucks. And. Oh really? Okay. It's like standards body that you buy. Yeah, exactly. You have to interpret the legalese or whatever's in there, right? Yeah. That kind of stuff. Uh, I'm not, yeah, I don't really look at the details. You don't read that for fun on like a weekend or? Not really. Um, and so, yeah, that, that was really the goal is to basically encourage people to look at, um, that kind of stuff and provide tools to be able to analyze them. Yeah. Because previously for GSM, like if you wanted to, to like, uh, first your, um, Wi-Fi card, you know, you could find like monitor firmware, that kind of stuff to inject raw packets, that kind of stuff. And the goal was to develop that, the same kind of tool for GSM and then for 3G and then for other protocols.

**Chris Gammell:** Right. Right. Much than this. Yeah. Like you said, uh, make things actually safer, right? I mean, that's, that's always the thing that the first time I remember like being exposed to the security industry, I'm like, why are they doing this? It feels like it's so like malicious and it's like, no, you have to have attack tools to make defense tools basically.

**Dave Jones:** Yeah. I mean, if you look at GSM, some of the attack that we, uh, demonstrated for, uh, like real, I mean, they were known for a while and, but nobody, okay. Yeah. Everybody, the response was, uh, always okay. Yeah, but it's not doable in practice. You, you can't, it's a theoretical attack or you can't pull it off unless you have a gigantic budget or that kind of stuff. Right. Right. And then like, uh, Basically someone's screaming, Hey hackers, come try this right now. Yeah, exactly. And then, you know, we prove, okay, we can listen to a phone call with like, uh, a $25 mobile phone of which we've replaced the firmware. Wow. You know, how much cheaper and how much practical do you need? Yeah, exactly. So that you fix your stuff, right? Uh, that kind of stuff.

**Chris Gammell:** That's great. Man, it says a lot of, uh, security implications, I suppose. It's yeah. Yeah,

**Dave Jones:** it does. And, um, and of course the, uh, besides the security, there's also just, uh, making technology, uh, just more available where at places where, where it wouldn't be, uh, because sometimes operators don't have, uh, like the financial incentive to provide coverage in, you know, if you have a huge area to cover, but not many subscriber, uh, you might need a solution that is much cheaper than what you can buy from Erexon, for instance.

**Chris Gammell:** Right, right, right. And if it's accessible and people can, you know, it's not necessarily easy, but it's accessible and like people can learn their way into the system and stuff like that. Yeah, that's great. I think there was, I think it was actually more on the fiber side, but there was like people setting up ISPs and like, like downtrodden communities and like some of the inner cities of the states that like, no one was gonna, I think it was Detroit, maybe it was like nobody was gonna give them service there. Maybe it was even self service too. I don't know.

**Dave Jones:** Yeah. Uh, I mean, um, at least I've heard it for the self service, uh, for the self service, sorry. Um, in some places, I, I don't remember the specifics, but it was like in the, in the UK or something like a, like a particular zone, like there would be no coverage and no operator would be interested. And so they had to provide self service, self service for themselves. Right. Basically. Right. Right. Uh, cause they're still commercial enterprise. It's not like national. Yeah. And it's always, it's like, it's in the UK, it's not in, in like, uh, you know,

**Chris Gammell:** Yeah. Subterranean Africa with like, yeah, it's a user area to cover. Right. It's still like a somewhat decent, uh, yeah, you, well, you would expect, you know, somewhat decent, uh, population density, I should fix that thought. Not somewhere. Yeah, no, no, no, no, no, no, no, no, no, no,

**Dave Jones:** yeah, exactly. Um, yeah, somewhere. Yeah. Well, you would expect self service to be a bit. Yeah. Right. Right. Um, yeah. I don't remember the details, but it was an Osmo.com talk at some point. Yeah. That's great. That's, I mean, like that's, that's a feel good project too. Yeah. Yeah,

**Chris Gammell:** definitely. Yeah. That's great. Well, what else are your interests these days? I mean, what else do you, I mean, Oh, you worked on the cube too with, uh, Peter, right? Uh, yes, yes. So yeah.

**Dave Jones:** Uh, the LED cube, I should say. Sorry. Uh, I mean, it's basically the ice for the dev board. Um, how did I come to work on that? Uh, Peter bugs you and he bugs you and when you, yeah, but I don't remember how did I meet Peter? Like that's, that's the question. I don't remember Congress a couple of years ago, maybe. Did I meet it in my Congress?

**Chris Gammell:** It's possible. I don't. This is Peter as in Temsky who we've had before. He's our, uh, our, uh, roaming correspondent at Congress. I think I'm going to try and talk him into recording again this year. So we'll see how that goes. But anyways, I mean, basically I was working.

**Dave Jones:** Oh yeah. No, I remember it was, um, I was, uh, on, uh, the open FPGA, uh, IC channel. Okay. And I was trying to get, uh, I was working on my USB stack actually. Okay. Oh no, no. I wasn't working yet on my USB stack. I was trying to get the, uh, tiny, uh, so Luke's Valenti tiny FPGA, uh, USB thing, uh, working on the UP5K, the, the, the ultra plus, uh, FPGA. Uh, because before I saw that project, I didn't even imagine for a second that I could implement USB with just FPGA IOs, right? Right. It was just that. Like they wouldn't be fast. Yeah. And so I, I found, uh, Luke's Valenti project like, uh, amazing, but it wasn't targeted at the FPGA that I had. Um, and so I wanted to get it working on that. And, um, I came to discover the icebreaker, uh, bit C board, which is actually a yet unreleased board that Peter, uh, worked on. Um, and yeah, acted so that, uh, I managed to, in the end, I managed to get it to run and I saw a couple of streams that, uh, Peter did, uh, we tried to assemble that board and make it work, that kind of stuff. And I think I met it at the Congress afterward and he started the icebreaker, um, board and he sent me a, like a prototype, I think. And, uh, yeah, I, uh, uh, that was actually at, uh, at Supercon last year. Yeah. That was, that was at Supercon last year. Okay. Yeah. Uh, no, I remember because, uh, I didn't have any lead panels before and he had a couple with him and, uh, I, he, he gave me one and the, uh, associated P mod and I just basically started working on a, uh, uh, a lead driver using as reference because I had no idea to drive those either. Yeah. Right. And so I watched a video by, uh, Mike Harrison. Mm-hmm. Which explained how to, like a binary coded modulation and how to drive those lead panels. Yeah. And.

**Chris Gammell:** Because those things are like, there's a ton of LEDs on those things.

**Dave Jones:** Yeah. Yeah. So yeah, there's a very specific way to drive them efficiently, basically. There's a ton of ways you can drive them, but there's only so many ways you can drive them well. Um, and yeah, I basically developed, um, uh, a core to drive that that was generic enough that apparently a bunch of people decided to use that. Oh, great. To drive, uh, the LED cube. Oh, that's cool. So I wrote the. Is that what Greg Devel's using too? So yeah, Greg Devel uses a heavily modified version. Okay. Because his, his lead panels don't really look like up 75. Yeah. He had to do a bunch of hacks. Oh, that's right. So he's, yeah, you were, you were, uh, these

**Chris Gammell:** are the off the shelf. Yeah. Yeah. Exactly. The panels that you guys were working with. Yes. And then he developed his own, he developed

**Dave Jones:** his own, uh, made of driving them, um, like optimized for his form factor and his custom, um, thing. And so he had to, he took my code, modified it. Um, I don't know. I, yeah, I think he uses it in also in not his cube. It's, um, what is it?

**Chris Gammell:** Decorhedrin. Yeah. That, that, that thing. It's like, it looks like a 26 sided die pretty much. I don't know what the, I don't know what the true shape is. It looks like a, yeah.

**Dave Jones:** Okay. Yeah. This one, um, I think he uses an even more modified version of it because that's not square anymore. Whatever works. Whatever works. Yeah. So, yeah. But yeah.

**Chris Gammell:** Oh, cool. And so to go back to the USB thing real fast. Yeah. So you said that you couldn't use, so like I think about, you know, microcontrollers I use, they have transceivers on board. Those are effectively differential special inputs, right? That are taking in USB signals and then

**Dave Jones:** translating those, right? The thing is like USB, you know, um, so low speed and full speed, which is always support on the badge and on the thing. It's not really different. I mean, it's different in the sense that most of the time the signal are opposite of each other, but that's only most of the time. Like sometimes they're both low. Yeah. Okay. So it's not true differential and you don't actually need a differential receiver. You can just look at

**Chris Gammell:** each signal independently. Oh, I see. Okay. So you just take one pin and you say, well,

**Dave Jones:** if I can detect a high and low, fine. Yeah. I mean, usually, usually you take both and you did, you detect, uh, all four state possible, which is both zero. Right. And transitioning. Both one is a narrow condition that shouldn't happen. Okay. Okay. And then you have the J and K state, which are like a, one is DP positive and the other is negative. Uh-huh. Yeah. Yeah. And so you do, you extract those three states from there. Okay. Huh. Okay. And then, so then that's enough though. You're saying that you didn't need specialized hardware. Exactly. If you want to go to like, uh, the high speed things, which is like 480 megabits, uh, uh, there you need true differential receiver and you need also a five because I mean 480 megabits, uh, like you can't, you can't do that with. Yeah. It's kind of, it's kind of fast. It is fast. And so you need to take a dedicated hardware. Yeah. Um, that translate that. So it's usually like a ULPI fee and then that this realize essentially this into eight bits in part of that thing.

**Chris Gammell:** Would it be possible to put USB into like a certas at some point to do, cause it's doing a serial

**Dave Jones:** to do, to parallel kind of thing. Um, I don't know. Oh, you do, because you need to do the clock recovery as well. And I don't know if they're going to do that. Um, at a certain point, it makes sense to have external hardware. Yeah, exactly. Uh, I mean, this helps you can do that. You can, you can do USB three with this, with the, the gigabit set us off the CP five. You can do USB three. Okay. Does that have it on here? No, the badge doesn't have them. It's a special, uh, it's the dash something. Yeah. Dash dollars. And you need, there is no like high speed rated

**Chris Gammell:** connection on the badge anyway. Uh, because yeah. Right. You need a bunch of firmware on top to handle all that stuff too. Right. Yeah. Yeah. I think, um, well, what does this do then? So how much can it do? A 1.1 can do what? A couple of megabits. It's 12 megabits. Yeah. So that's still good for a lot of stuff. Right. And it shows up as, yeah, sure. I mean, you can, it only, it only

**Dave Jones:** has like nine megabyte of flash. So it's, it's not like you can, you need a lot of time. Even if you, if you were writing the entire flash every time. Right. It doesn't take that long. And to do things like, um, you know, USB console or that kind of stuff, it's, or firmware update. It's, it's perfectly appropriate. Yeah. Yeah. Cool. Well, thank you for telling

**Chris Gammell:** about us all about all this stuff. This is, this is, I mean, I love this hardware. It's great. Um, how, what do you think the best? So, you know, you've been doing FPGA stuff for a while now. Yeah. What is your, your favorite way? How do you think people should get started with FPGAs and then kind of continue the practice? Wow. That's a really hard question.

**Dave Jones:** Um, that's what I'm here for. I ask the difficult questions on the empire. I would actually start with either, um, Verilog or VHDL. I tend to lean toward Verilog because, uh, most of the open source tools, um, use Verilog more than VHDL. So you, you will have more choices. I won't lie. Like the learning curve is, is rather steep, but, um, I think it will allow you to go, um, further basically, um, because of all the existing code, all the existing examples. All the cores are usually Verilog too, right? Yeah. I mean, there's a lot of VHDL ones as well. Uh, yeah, there are. Um, but yeah, I, I started, you know, doing FPGA using VHDL, but I switched to Verilog basically when I started working with US companies and when doing, um, open source work, uh, yeah, with the open source tool, I mean, um, so yeah, it's, it's not necessarily easy, but at least you won't be limited. Yeah. Another good option would be, um, and my gen. Oh yeah. Uh, which is basically using Python as, uh, other description language. Um, so it's kind of a taste thing, but at least it was in my gen. You won't be limited either. Um, yeah, it's, it's really new. Like I think it's version 0.1 has been released, like, uh, uh, not so long ago. So documentation is probably not, um, great at the moment. Um, so yeah, it's, is there a good project kind of that you usually tell people to start with? Not really. A good project is whatever is going to keep you motivated. I think, you know, choose something you want to do. Uh, that would be for instance, like kind of hard to do with a microcontroller, but that you heard would be easy with an FPGA. That's a good point. Um, usually driving is probably a great example of that. Exactly. Exactly. Because, uh, if you want to do it, um, like perfectly or like fast and parallel, it's, it's tight timings that are really deterministic, that kind of stuff, which is hard to guarantee on a microcontroller. Interrupts. Uh, yeah, exactly. And, and, and like trivial on a FPGA. So that's really a very good project. Um, and it's not, it's not too hard. It's easy to simulate. Uh, that's actually the other thing that I would recommend for people is to learn to simulate first. You said use iVerilog for that? Yeah, I use iVerilog for that. Um, people have had good success with Verilator as well. Okay. Um,

**Chris Gammell:** yeah, I'm not using either of those. I've used, I've used the Model Sim in the past, but. Yeah,

**Dave Jones:** I use Model Sim as well. Yeah, right. But, uh, it's, uh, it's expensive and most likely for a lot of projects, you know, if you're simulating a giant FPGA and you need to simulate like billions, of cycles. Yeah. The speed advantage of Model Sim makes sense. Yeah. But if you're simulating like a driving in a LCD panel for a few milliseconds, it's really doesn't matter. Yeah. Um, and yeah, simulate, simulate, simulate because, uh, debugging hardware inside an FPGA. Well, I have one LED I could blink. So that helps. Yeah, it helps. Uh, I mean, connecting like a logic analyzer outside is, and, and on the, on some bigger FPGA, you can actually instantiate like an internal logic analyzer. Yeah. Yeah. As it is. But, uh, the tools to do that with the open source, uh, are not yet as convenient as the open source, uh, to gen. And then depending on the FPGA that you use, like the S4, it's such a small FPGA. Yeah. That it could consume a lot of resources. Yeah. Um, simulating on the other hand, it doesn't cost you anything. And, um, you can inspect every single signal in your design at any point in time. Yeah. Uh, it's pretty trippy. It's, it's really great.

**Chris Gammell:** Um, to debug stuff. Yeah. Great. All right. Well, thanks for joining us today. I appreciate it. Well, thank you for having me. Yeah. All right. We are back at Supercon 2019. We've been interrupted a couple of times here, but we're, we're going to get it this time. I'm here with Matt Venn. Matt, how are you doing? Yeah, I'm doing great. Thanks, Chris. Yeah. So, um, you do FPGA stuff. Yeah. How did you get into

**Chris Gammell:** that? I got into that through a interesting technology strategy boards, uh, grant, which is like an English system that the government makes available money to do projects. And I was working for a company at the time called the Arcola theater, which also had like a technical incubator attached to it. Really? And they were doing hydrogen powered stuff. Really? Okay. It was quite hydrogen powered theater. Yeah. Like the direct very far afield. Yeah. Yeah. The director, of the theater was a, like did a PhD in hydrogen fuel cell stuff. So he was like interested in looking at the merge between. It sounds like someone who's like, I've got money and I'm spending it exactly how I want to. No, they never had money. Well, I mean some kind of grant money though. Yeah. He was like interested in the world of like super controlled engineering and how everything takes a long time and is very controlled. And then also theater where like, it doesn't matter if it's not ready, you show must go on. Right. And he was like interested in looking at if it was possible to kind of do a merge of those things. I'm glad that there's not hydrogen fuel cells that are just, well, we'll figure it out. It has to go. So we'll just blow that stuff up. Yeah. Right. Right. So, uh, yeah, actually you overheard when we were talking with Ted earlier, but, um, this was for a, a project to detect if a, um, a high pressure tank of hydrogen was being damaged through being filled by listening to the sounds that it makes. Right. Um, yeah, you're doing like filtering and application and, uh, that guy, that project was being worked on by another engineer who had to leave due to health reasons. And he, uh, asked if I could do it. And I was like, yeah, sure. Why not? Yeah. And then I had to kind of learn how to do everything, take over from that project, which at the time was a beagle bone and an FPGA together, um, listening to ADCs. And so that was like my first, that's a, that's a deep end dive right there. Yeah. And it was, uh, okay. I did that totally classic thing of coming at it completely from the software side and thinking it's like each line of, it was VHDL. Oh, sure. It was like a sequential program. And, uh, yeah, just, and then,

**Chris Gammell:** uh, I don't know how to like, so I've been, you know, I've had two other guests on so far and I'm not sure what order I'm going to post them in, but, um, it's hard to like try and it's like, you can't, you don't know the matrix until you see it. You know what I mean? Like, it's like, it's really hard to, to remember what it felt like before understanding that switch over, you know, it's hard to explain that to someone. Yeah. You just have to kind of do it a little bit.

**Chris Gammell:** Have you ever, uh, worked with kids, uh, doing computer programming? I have not, no. Okay. There's this, um, software system called scratch. Okay. I've heard of that. I've heard of that. So that's quite interesting because in the UK with the, uh, new, um, computing curriculum, there's like this sequence of software that kids often use. And the classic thing is they start on scratch and then they move to other things and end up in Python or something. Okay. And with scratch, everything is happening in parallel. You make a new, really, I didn't know right. Yeah. And then you give it some instructions and it starts doing, and then you make another sprite and you give it some instructions. Yeah. It's like the incredible machine kind of thing, right? Everything is going on at once and it's just very, very simple and straightforward. And then they transition to Python and they want to make something like they've done in scratch with things happening at the same time. So they should switch to FPGA as you're saying? Maybe. Yeah. Wow. But yeah. So then it's interesting that like scratch works in a very parallel way. Yeah. Right. You have to work hard to make things work. Like you need to use a library, like pie your game or something like that to get some multi-threaded stuff going on. Yeah. Wow. I didn't know that. And then with electronics, I started with, you know, firmware and C and doing everything step by step. And then with FPGAs, it's like, no, it's actually like someone's given you a huge bag of those one by one by one Lego blocks. Right. You can make anything you want. Or a lot of 74 series logic. Yeah. Yeah. Like, um, like, uh, Pepin who did the, um, he did the, uh, the little LED blinky that was wrote the Verilog and then synthesized it to 74 series logic. Oh, that's right. Yeah. Yeah. Yeah. Yeah. Okay. Yeah. That's great.

**Chris Gammell:** Yeah. Yeah. It's tough. I mean, it's just a tough mental switch. I think, I think it's tough for kids in general just because the abstraction kind of stuff that's happening in ways, but yeah. Um, okay. So that's how you, that's the first project you got into or that was the first exposure I had

**Chris Gammell:** to FPGAs and that was before the open source tools and that project's like being, it's a kind of R and D ongoing project. Okay. And then I made the switch to using the open source tools, which for me was great because, um, like you, I work kind of in a, uh, it, I want that really tight feedback loop so I can learn quickly because I learn better through application rather than textbook. Right. And having a 30 second synthesis to bit stream to programming. Right. Even though you're not really meant to do it. Like, we should probably think through things. Yeah. Um, yeah, it's good to have that very fast and that's what makes it possible for the, you know, the badge hacking workshops, the open source tool, like, cause you can install this stuff. It only takes up a hundred meg or something and then you can run that whole process and well, the tool chain takes up more than that. Right. Yeah, probably. I was just thinking I downloaded, well, I downloaded the, um, badge hacking toolkit. That was 300 meg. Yeah.

**Chris Gammell:** Yeah. Tar GZ. But compared to like a, you know, yeah. And that includes the risk five tools. Right. Right. Yeah. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. So it's that tight feedback loop that I think is a helpful for, uh, when you're beginning, but then as things grow in complexity, then you've got to learn how to do the simulation. Right. Right. Otherwise you're going to crank. It's just horrible. You end up in FPGA hell is Dan Gisselquist calls it. What, uh, what, what is FPGA hell? It's where your, uh, your design doesn't work and you've got no idea why not. Oh, you're waiting, you're like cargo culting it. You're like,

**Chris Gammell:** well, if I touch my ear and I hold my elbow like this, then, then it works this time. Otherwise it doesn't. Yeah. Yeah. That's, that's tough. I think any kind of thing where it's like a new, a new field like that, you're just trying to figure out what works, you know, sometimes it really helps to have that working example to start from, but you know, for new projects, you just don't, don't always have that, you know? Yeah. So you made the switch to open, uh, open, uh, tools and which we've obviously been highlighting a lot here, but now you also work on symbiotic EDA.

**Chris Gammell:** Yeah. So that was, um, that was just, I mean, that was just a kind of lucky coincidence really, because as I was doing more stuff with the FPGA stuff and with the open source tools and following Clifford and the other guys involved in developing the tool chain, I would like sometimes see some tweet that they'd written about fixing a bug or something new thing or some documentation, whatever. And I was stuck on some problem and I was like, I'm going to go back and search. And you know how awful Twitter is to find anything that's happened. It's like even five minutes ago. Yeah. So I was searching through Clifford's tweets and then saw like a, a job offer posting. Wow. Like we need more people to get involved in the FPGA stuff. Right. And we should say that's Clifford Wolf who started the Oasis project and now

**Chris Gammell:** project iStorm. Yeah. Yeah. Oh, iStorm. Sorry. Yeah. So I, um,

**Chris Gammell:** I applied for that, but it was like a year and a half out of date. Oh really? Oh, wow. But they said, oh, we need somebody to help with the education and the workshops and the trainings. Yeah. And, um, although I do, uh, like quite straightforward engineering stuff, I'm also, uh, really interested in science communication. Yeah. In general. So same. Yeah. So, um, this is a really good opportunity because I can work with a team of absolute FPGA masters and learn a lot from them. Yeah. And, and when I think it's a, I think it's, it's a bit of a cliche, but people say, you know, to learn something, you have to teach it. Yes. And I think, um, like certainly with the formal verification side, like it's taken me, I don't know, like six or eight months to feel like I can explain the concepts of that. Okay. You have 30 seconds to go. So how, what is, what is formal verification? Put me on the spot. Oh, totally. Yeah. Yeah. Um, so formal verification is, uh, a different way to verify your, um, your projects, mostly FPGA, because it's, um, for it to work, you need quite a limited space of opportunities for things to happen. So with an FPGA design, you've got limited width registers and limited things that things, the state, like the total number of flip-flops in your design is small compared to like a Python or C program where every, like in Python, you make something, you make a variable and it's actually an object and it could be a 64 bit float and it's like just huge. Yes. What it could encompass all the values that it could, yeah, I hold in there. Yeah. Um, and then how that propagates through the system. Yeah. So if you were like testing like a C program, you might like write a test bench that exercises it. And then it has to be like a strategic and smart. Yeah. Hopefully. But it depends on, uh, the imagination of the person that writes the test. That's right. Yeah. Yeah. That's a smart piece. Yeah. Yeah. Yeah. Whereas formal verification works in a different way. It's like you say what would be bad for you, a bad state to get into. And then you give that whole thing to something called a sat solver. And the sat solvers job is to find a way of, uh, like progressing from an initial state to a state that is broken, that violates your properties. And if it can do that, then it kind of wins and it writes you out the trace of how it got there and then say fail. And then you open up that trace. And that's cool because

**Chris Gammell:** I'd actually did. I had not, I, the way I remembered it from, I think when Clifford was talking about it, maybe after that, even was the idea of you try, you could try every combination of every bit in your entire system, or there's a subset of those bits that will cover everything. And so you just do that instead. But that doesn't sound like what you've just said. I think it's related. Okay.

**Chris Gammell:** Um, but it's like, this sounds like a constraint that you're putting on the system. Yeah. So there's, there's a few different ways. Like, um, you have your properties, uh, um, like your safety properties, where you say, I assert that this thing must never happen. Okay. And then the solver, the sat solver will try and find a way of getting your design into that state. Huh. And if it can, it will write out a trace that you can then load up. And it's usually very short, which makes it easy to trace your bugs. Then you fix your code if it's a bug, or you might think, yeah, but my code could never have got into that state because that's kind of outside the, and then you would limit your search space by using a different operator. So the sat solver, though, how is it actually, is it just varying input like randomly? I can explain how it works. That's still like the magic side for me.

**Chris Gammell:** Yeah. Okay. Um, that's okay though. I mean like, but it's doing something that is getting it to that

**Chris Gammell:** state. So yeah. So the, one of the examples I use when I'm explaining it on like the videos and stuff is that I use a Python library called pySMT, which is just like a wrapper for these sat solvers. Okay. And you can do something like the example I use is you take the letters in hello, H E L L O and the letters in world, W R O L D. And you say to the sat solver, if you assign them all a value from one to 10 in those letters, hello, in those letters, world, and they both got to add up to 25 and they've both got to equal each other. Okay. Can you come up with a way of assigning the numbers that satisfy those constraints? Okay. Another classic one is like solving Sudokus. You know, you give it these certain things, those puzzles, animators, and then it will go away and it will find, it will find if it's possible or not. But the interesting thing about them is they never come back and say, I don't know. They say either yes or no. There's no kind of in between. Like if you might decide to get to the end and it's like, you know, I've tried everything. That's not possible. Right. Maybe it's, there's too many combinations and it is just, it's running for three or four or five days and you decide, okay, I need to limit my space a bit. You stop that job and you change it a bit and you run it again. Yeah. But it's never going to come back and say, no, there's no way. But actually there was a way. Right. Right. Yeah. So that's the kind of the power of the formal tools is you can say like, we used it recently in this machine learning accelerator, which has got a single ported memory with a pipeline to control the kind of accelerated multiplications. And it was important that you can't read or and write to the single ported memory at one time. So you can just write one assertion that you just say, I assert that only one or the other of those lines can be true at once. And that's all you need to do. Then you run the formal tools on that. And then it will try and find any way at all to give the input to the pipeline in a way that messes it up and gets it to read and write at once. So if it says no, you're guaranteed that your design is good in a mathematical way, a mathematical certainty, which it would be very difficult to get that kind of certainty from a test bench, right? Because how could you test every combination? Of course, of course. Right.

**Chris Gammell:** And it's like the test bench is like, well, your input is now five, your inputs now, you know, or your inputs five from five to 27. Right. You could say that as like a test bench. Yeah.

**Chris Gammell:** But I might not think to make my input. Again, it's up to the imagination of the test. Yeah. But if you've got something with too many combinations to test and you'll never get all the corner cases. Right. Right. Right. Huh. But there's things that it's no good for, like multiplication. Again, that's not something I can explain right now. That's like, on one of my ongoing questions. To the TVD. Yeah. To be able to explain that. Yeah. But much better to do something in like with Verilator or like C++, you write something that just exercises the entire space, checks all the inputs and the output is correct and run it. And it takes 20 minutes to test. Verilator is the Verilog simulator, right? Yeah. It's like a, it's like a C wrapper for simulating your Verilog code. Okay. Yeah.

**Chris Gammell:** Okay. Yeah. It's hard. Yeah. This is definitely hard to wrap my head around. Yeah. But yeah, you should watch my videos. I've watched one. Sorry. Well, here's, I guess that's a good question then. Who would be using this? I mean, like, so is this chip companies and, you know, like industrial companies, like people, who needs to use formal verification?

**Chris Gammell:** Well, I think historically it's been people that can't tolerate failures. Okay. So space shuttles. Or when the failures are too expensive. So if you build an ASIC and I was talking to an ASIC engineer recently and they were like, one of the things that terrifies us is that we build a state machine into the ASIC that ends up getting stalled or blocked. Oh. And then there's no way of unblocking that. And we have to do a new spin. Yeah. New mask. A huge amount of cost on that. Yeah. 10 million dollars. Yeah. Yeah. So people like that, where they've got this huge investment or like you said, like space or

**Chris Gammell:** aeronautics and stuff like that. Right. No coming back from it kind of thing. Yeah.

**Chris Gammell:** And typically the price of the tools is reflected like that kind of niche area. Yeah. And the one thing that we're trying to do here is as well as the tools being open source so that you can download and compile and start using them at no cost. Yeah. We're selling licenses that kind of come with the backup, the technical support of. Yeah. Yeah. It's a service contract. Yeah. That kind of thing. Yeah. And or being able to buy online hours so you can try it out quite cheaply. Yeah. Like I think the cheapest license is maybe a thousand dollars a month. Probably a lot cheaper than a former tool.

**Chris Gammell:** Oh, God. Yeah. It's unbelievable. It sounds so niche and so like important that I can imagine

**Chris Gammell:** a six figure type of. Yeah. I think there's a lot of room for people that have never heard of it or have heard of it and think it's too hard or heard of it and think it's too hard and it's too expensive. Yeah. And it's yeah, I think it's another valuable tool in the toolbox to at least know is there and occasionally use it. Yeah. I don't like I think also some people have the impression that you have to like formally verify everything or nothing. But again, like a couple of properties in the occasional file to like the bits where you're confused or you think what's going to happen if this I just can't look at I'll just write my one formal property that says the state machine must never get to this state. Yeah. Okay. So let's run with that example real quick. I know that this is a

**Chris Gammell:** stupid question before you even ask it. But like there is no stupid. There's a stupid question. I'm about to ask it. How long would that take? Now, I know that that's a stupid question because that's an undefined problem, right? To write or to run it. To run it. So you said sometimes they take three or four to five days, right? But maybe let's constrain the problem, right? Like, so we've got an ECP 5 badge, right? I want to have the state machine example you talked about earlier. Yeah. How many inputs could it even have? Like how long would that take to simulate that or to verify that sort of thing?

**Chris Gammell:** Uh, it's really an open question because you can have, you can have, um, uh, like a proof that can run in seconds and be done. Okay. Um, because, uh, because there's only like a couple of branch points that could, yeah. Like if you imagine you have like a register and you're saying this register must never equal zero and you set it to one when the program starts, but then there's no logic in the, um, in the design that would ever set it to zero. Oh, right. Then the, the, the, the formal tools would just immediately see there's no way of ever being changed and just be like finished, done. But if you had that as say, the output of an ADC or something, there's a 16 kilobyte block ram and the out, the, when you're reading an address, the output must never be more than 200. Yeah. Then that's a different problem. You've got to kind of approach that in a bit of a different way. Yeah. So I know

**Chris Gammell:** that this is going to lead me back to asking you how it works under the hood, which I realized you said was a thing that you're still a bit magical. Yeah. Yeah. Yeah. But it's like, it feels like it's like almost like a sensitivity analysis. The way you've talked about, it's like almost a sensitivity analysis of like, like how much, what could change, like how, like how powerful is this knob that you're trying to test? Right. So, uh, sensitivity analysis, the way that I think about it is you kind of back calculate to say, I want to know if I turn the knob for, uh, I don't know, voltage gain, right? How much does it change the output way, way over there? Right. And if it changes a lot, the sensitivity is very high. If it changes a little sensitivity is low. Yeah. And it sounds like it's that, but then

**Chris Gammell:** back calculating it for all of the digital and the combinatorial stuff, which is why the, which is why I think that the multiply stuff is more difficult for a formal proof. Because there's so many, a state machine is easier because there's only a certain number of ways of transitioning from state to state. I see. So you talked about constraining the problem space. Yeah. What did you call that? Yeah. So like this, the search. So if your design has got a thousand flip-flops in it, Yeah. So it's got that combination of all those different. So if you looked at all the possible states your design could have, it would be two to the thousand. Uh huh. So it's a really big space. Yeah. But if you can constrain the space that the solver is working within, then you can also make things work faster. So you can use this as a keyword, an operator called assume, where you can just say, for the sake of this problem, assume that this entire area of the state is never going to change, or is always going to be like this. Okay. And then it will only ever consider. So do you ever start tests where they're so constrained that you know it's going to be super short? Well, that's one of the, uh, that's one of the, um, uh, the dangers is for like, for example, you could say, okay, I've got my property set up. The state machine must never enter this state here. And then you've got an assumption that says, um, assume reset equals high. And then actually your design never moves forwards because the reset is always high and the design can't change. So the tools will finish immediately and say your design passes. Right. And you go, woohoo, I'm getting beer. But actually you made an assumption that prevented your design from ever working. Right. So that's, um, so the, the formal tools aren't some kind of magic bullet. They're only as good as the properties and to write good, well-meaning properties that cover the important stuff is the work of getting to be good at

**Chris Gammell:** using the tools. Huh? But there, it seems like there's a balance point between like something that is super under constrained and it runs forever and super over constrained where it finishes.

**Chris Gammell:** Right. Yeah. So how do you strike that balance? I think, um, that's again, part of the, this is what orange you the big bucks. Yeah. If you can answer that question. Well, it's yeah. Knowing what stuff is the important stuff to test and how to test that. And sometimes it's very straightforward what the answer is like in the example I used earlier about the, um, the memory access, because, um, I like, I, I could do a lot of work on how the, um, the bit that dispatches commands into the pipeline works. But actually the only thing I care about is that the read and the right line are never high at the same point. So I just put one assertion there. And then if there is a bug that leads me to the problem in the dispatch for the pipeline, but then other designs are not that near straight forwards to work out what properties you need to fully understand it. Like to, to formally verify a FIFO, uh, there's like a few different things you've got to do. You've got to like say that, um, when you make a read at a certain address and a certain bit of data goes in, when you make it right, then the data ends up inside the FIFO and then it doesn't get lost. And then there's a little bit of kind of construction you need to do. Like sometimes you have to build a state machine that, uh, handles the formal testing of, Oh, okay. Okay. Of another state machine. So that different assumptions or assertions are made depending on

**Chris Gammell:** the current operating state. Yeah. Well, that's good. I mean, it, I guess, you know, it's not like, I don't think anyone listening to this expects FPGAs to be a panacea, you know, like to like solve all digital problems and that, but I think tools like this also make it a little bit more accessible as well. Right. Cause you can run a lot more tests and, and this is honestly what people are doing when they verify like an ARM core as well. Right. Like that's just kind of all pre-done for you. ARM, someone at ARM is running similar testing. You hope so, yeah. Well, yeah, I actually don't know. Is that, is that a thing that they do?

**Chris Gammell:** Um, I don't know. Well, maybe a better question is who, who are your clients? Well, I had a great conversation, um, with a guy who works at, um, a particle accelerator in the States. Oh, cool. Just trying to remember that, uh, Fermi? No, it's, um, ALS, advanced light source. I think that's it. Um, and they used, um, Clifford's Pico RV 32, which is the same thing I've got two of in there. Yeah. It's in the conference match. Yeah. Um, and I was interested in, I'm interested in big science anyway. Yeah. And I was asking like, what, like, why did you choose this? And was it important that it was formally verified? And they use it for the interlocks for the RF safety system.

**Chris Gammell:** I think you might've mentioned this when he was on the show. Right.

**Chris Gammell:** There was someone, there was someone at a particle. I thought it was CERN, but maybe it was someone.

**Chris Gammell:** He also, they're used in CERN as well. They're used in CERN too.

**Chris Gammell:** Okay. But the guy that I interviewed was in, unless. Oh, great.

**Chris Gammell:** Great.

**Chris Gammell:** Um, and yeah, it would, it kind of gave them confidence that by using a formally verified processor to control the safety features of their accelerator. Yeah. Gave them confidence that it was going to do the right thing. Yeah. Yeah. The code could still mess up. Just saying. Yeah.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Chris Gammell:** Absolutely. But I guess that's one less thing you have to worry about. Yeah. Like weird bugs happening. Yeah. And having it open source means that you can check it for yourself.

**Chris Gammell:** Yeah. Okay. So that's, yeah, definitely. Well, I mean, uh, are there other people out there that should think about, do I guess I kind of already asked that though.

**Chris Gammell:** I would say that, um, uh, if you were getting started with, uh, the FPGA stuff, then hold off a little bit. Um, well, you're going to, uh, probably just immediately want to get your hands dirty. Yeah. Like I did. And like do a bunch of examples and you load them onto the FPGA and you're taking a bit of the cargo cult stuff like you mentioned. Yeah. And then stuff's going to stop working and you're going to be an FPGA help. Got it. And you're going to, uh, you're going to ask somebody and they'll say, well, have you simulated the design? What happens when this happens? And you'll say, no, what simulation? And then you'll have to learn how to do simulation. And I would say. Down the rabbit hole you go. At that point, uh, then it's also worth checking out, uh, some basic formal verification stuff because it's always an hour free to experiment. Yeah. Yeah. And, um, one of the, they, they can help you accelerate the time to find and fix bugs. So, you know, like test driven software. Yeah. Right. That's a great. You write your test first. Yeah. And then you write the, so you write your formal properties first. Like when this thing happens, then this thing must happen. Then you write your Verilog and you run the formal proof and it just says, no, it didn't work. And then you, you get your trace back and you're like, oh yeah, because if resets high when that's low, then it can end up in this state. And then you write that extra bit and that stops that. And then you run it again. It fails again. And it says, oh yeah, because if it was in this state when the bus was like that, then this is going to happen. I'd write the thing that does that. And then it passes and you're like, okay, cool. Now I've got a bit more confidence. And you probably do simulation as well. Yeah. Well, I used to just simulate FPJs actually back in the day, but it was always very visual.

**Chris Gammell:** And that's interesting too, because this is decidedly not visual, right?

**Chris Gammell:** Well, it can be, I'm sure, but it's visual. If, um, do you mean like looking at waveforms? Yeah.

**Chris Gammell:** Yeah.

**Chris Gammell:** Yeah. It's visual when it fails because then it writes you out your trace. Yeah. I meant more like looking at charts of highs and lows and highs and lows and highs. Yeah. Because that's, uh, you know, if you've got like, um, like a hundred megabytes of traces and you've got your bug in there somewhere, that is, that can be really eye-watering to work your way through all of that. So one of the things I love about working with the formal tools is that I'll probably, all my traces will be 20 clocks long and it will just go from a running state to a failed state and I can just see how it happened. What is a trace? I guess I don't know what that is. Um, it traces like the steps that it's going through. Yeah. Like imagine. Yeah. So it's like, um, each waveform shows you the state of the flip flop for each of the flip flops and you could like load all of them at once and see how the state of the design is changing all the time. But maybe you just have the clock, the reset, what state the state machine is in, what is going on on the data bus. And you see these things changing as the design progresses through. Okay. So you run your simulation and it dumps like a VCD file, value change dump. Uh-huh. And then you load that up in a program like GTK wave and that's got all the, the traces. The stuff that I'm used to. Yeah. Yeah. Looks like a logic analyzer. Yeah. Yeah. That's what I was thinking. Okay.

**Chris Gammell:** Okay.

**Chris Gammell:** Cool. I call it traces, but.

**Chris Gammell:** Yeah, that's cool. That's cool. Well, uh, where can people find out more about this stuff?

**Chris Gammell:** Um, for formal verification, uh, you can get in touch with me, Matt at symbioticeda.com to arrange a demo. Demos. If you want to do like a demo, um, if you don't want to do a demo, but you want to watch some videos, check out and subscribe to our YouTube channel.

**Chris Gammell:** Hit that bell. Hit that bell.

**Speaker ?:** Ding, ding.

**Chris Gammell:** Search YouTube for symbioticeda. Symbioticeda. Um, I'm just, I just published my second video. I did like a series on how the open source FPGA tool chain works. Yeah. And now I'm doing a series on like an introduction to formal verification. Great. I just published the second one working on the third one. Awesome. So, um, yeah. And we've got a webinar coming up in one week time. I don't know when this is going to go up. I don't like webinars, but you know. You don't like them? I don't.

**Chris Gammell:** I don't like the word, honestly. Like the idea of like someone like being there, like teaching me, like transferring knowledge. I just wish it was a different name. Yeah. Webinars.

**Chris Gammell:** Never liked the name. Yeah. I agree with you. We're trying it out. I don't know how well it's going to, we think we've got maybe 30 or 40 people registered so far. Like live video lecture.

**Speaker ?:** Yeah.

**Chris Gammell:** Okay. Yeah. We've got a live video lecture. Oh, I'm so interested. Yeah. Yeah. You can sign up. On our web list.

**Chris Gammell:** On our mailing list. Yeah.

**Chris Gammell:** On our Webber tweet. Yeah. Um, and that's going to be like, uh, me and Clifford Wolf talking about getting started with the formal tools. It's great. Yeah. Cool. All right. Well, thanks, man. You're welcome. Thank you.
