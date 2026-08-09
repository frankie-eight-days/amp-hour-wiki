---
episode: 463
title: An Interview with Trammell Hudson
url: https://theamphour.com/463-an-interview-with-trammell-hudson/
---

**Trammell Hudson:** Roden Schwartz is a leading manufacturer of value instruments designed to help you maximize your bench's performance for everyday applications. They just announced an industry-first, complete solutions with all the upgrades up front for one price. Now through December 31, 2019, save up to $10,000 on Roden Schwartz solution packages that come with fully loaded test and measurement instruments right from the start. When you invest in Roden Schwartz products, you get the highest quality engineering, plus all the bandwidth, channels, inputs, memory interfaces, and signal generation you'll ever need. Learn more about Roden Schwartz value instruments and this limited time promotion at askanengineer.us. That's askanengineer.us. This is The Amp Hour Podcast. Released October 20, 2019. Episode 463. An interview with Trammell Hudson. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Trammell Hudson:** And I'm Trammell Hudson, a hardware and firmware security researcher, and I like to take things apart.

**Trammell Hudson:** Hey, Trammell. Welcome to the show. I've admired your work from afar for a long time.

**Trammell Hudson:** Yeah. Thanks for having me. It's really a fun chance to get to chat about some of the projects, and I think we have a lot of interests in common.

**Trammell Hudson:** Yeah, I think so. And I think that we have a lot to talk about, too. Your site is a repository of hacks and a variety of interests that we're going to go through. And it's really, really fun to follow your site. So it's trmm.net for people who want to follow along at home. We'll be going through some of the projects there. But why do you do all this stuff? I mean, you do a lot of different things, and you document it really well. And that's not necessarily the most common thing. How did you get into hacking and documenting all these things that you do?

**Trammell Hudson:** Well, the main reason I like to document everything is because my attention span is really short. So Charles Strauss jokes that people like me fail our saving throws versus the next shiny thing too easily. And so usually after I have a project sort of to the proof of concept stage, I like to photograph it. I like to write up about it. I like to push everything to GitHub or somewhere and then move on to the next thing. And over the past 10 or 15 years, I've been doing a lot of projects like that. So most of the time, they get to the point where they work for me. And I hope that they are going to work and be helpful for other people. And it's really a delight when I get email from people who have picked up my other projects and use them in their own or they've extended them. So I joke that my favorite day is starting a new project. And my second favorite day is handing the commit keys over to somebody who wants to maintain it and turn it into something even better.

**Trammell Hudson:** Yeah, it's like owning a boat. First, the best days are when you get it, when you sell it. Apparently, I've never had a boat. Exactly.

**Trammell Hudson:** Yes. I think it's a similar sort of thing that I really love the finding out how things work. I really like to take things apart and dig through the firmware and understand what makes a lot of these devices function. One of my real passions has been making it possible for people to run their own firmware or extensions on firmware on devices that they've purchased. And this is a lot of fun for me because it lets me focus on the interesting part of how do we get inside some of these systems. And then it lets people turn the devices they own into things that are more functional for what they want to do with them. So a lot of the projects have that sort of focus.

**Trammell Hudson:** Yeah, and I'd love to hear about your – I mean, so I definitely want to talk about the individual projects themselves. But up front, I'd love to hear about – when I think about reverse engineering and I think about the kind of stuff that you work on, you talk about troubleshooting a lot too. You gave a talk about – I think it was the joy of taking things apart. That's kind of a great overview of your thinking, at least as far as I could tell. But the thing I always think about is like the amount of stick-to-it-ness or mental fortitude or just like staying in it, staying in that discomfort. How did you – first off, how do you deal with it? And second off, how did you get to the point where you like staying in it? I always kind of get frustrated myself and I kind of jump out of it a little too soon. So like how do you think through a problem and stick to it so that you're getting that first piece of firmware on there?

**Trammell Hudson:** There's a wonderful quote by Matthew Garrett about that he doesn't think he's very good with computers. He's just really bad at knowing when to give up. And I think that that – I share that sort of attitude towards it. I think one of the reasons I tend to stick to it long enough to get things working is I've had enough success in the past that I feel that once I find the sort of the first way to get some good execution or to get a better picture of what's going on inside a system, I have a good feeling that I'll be able to do more with it. And we found that a lot in like when we do classes at NYC Resistor, the hackerspace that I used to belong to, that if people have enough early success that they're able to stick with things further and power through the adversity of sort of the next levels. And I think after doing enough of these projects, I feel that I've – I can have a good feeling that of seeing the light at the end of the tunnel and seeing that end goal of going beyond the hello world. But a lot of times, you know, things don't pan out. And I try to document a lot of my failures as well. Perhaps they'll be helpful for someone else. Perhaps there'll be a warning for someone else.

**Trammell Hudson:** I think the documentation itself is actually a troubleshooting method. And like it seems like that's kind of how you think through problems or, you know, you're able to capture what you're working on. And that kind of helps you to probably come back to it as well.

**Trammell Hudson:** And having good notes definitely helps out with figuring out what have I tried and where are some ideas to try some other paths. So it serves both for me to keep track of what I'm doing and then, like I said, hopefully it helps other people as well.

**Trammell Hudson:** So what were some of the early successes that you talked about that kind of gave you the confidence to keep going?

**Trammell Hudson:** So the one that I had the most success with was the Magic Lantern firmware for the Canon cameras. And that came out of seeing the CHDK project, which was building GPL firmware for some of these cameras, or excuse me, for the point and shoot cameras. So I had a good feeling that it was possible to do a similar thing for the SLR, the higher end SLR cameras. And the motivation that I had was that the initial firmware from Canon had a lot of limitations. And at the time I was trying to make some short films and involved in that community. And there was a lot of complaints about the fact that it didn't have on-screen audio meters or manually controllable audio levels. And I knew that that was just a simple matter of programming. So based on what the focus on the CHDK site had done, I was able to understand a little bit about the Canon's firmware update files and able to apply what they had documented to stand on their shoulders and extend all of that for the SLRs.

**Trammell Hudson:** So how much of it does, so you said CHDK, is that the right?

**Trammell Hudson:** CHDK, it's the Canon Hackers Development Kit.

**Trammell Hudson:** DK, okay, sorry. So how much of that, so like you're approaching a problem like this, you're taking an off-the-shelf consumer level, well, maybe prosumer level, I guess that's a nice camera. How much do you have to know about the actual hardware? I mean, are you taking a camera apart? Do you need to know the processor? Or is it more about dumping firmware files and just kind of operating within the scope of what firmware you see?

**Trammell Hudson:** It's mostly dealing with the firmware side of it. Since a lot of these devices have firmware updates that the vendors ship, that gives us something that we can look at to try to understand what's going on inside. But it's not always that case. That some of the other firmware dumps have involved, say, getting a little bit of code execution and then toggling the rest of the firmware out via a LED or a GPIO line. So it's not always as easy as being able to download a firmware from the vendor website. But typically, it very quickly moves from that sort of hardware work to using a disassembler like Hopper or Ida or the new one from the NSA, Ghidra, to try to make sense of the firmware and figure out how it's constructed, what the sort of various, what the programming model inside was, so that we can then build extensions on top of it.

**Trammell Hudson:** And you had mentioned you toggle the entire firmware dump out of the LED. Is that right?

**Trammell Hudson:** So one of the initial versions of a CHTK was toggled out via an LED.

**Trammell Hudson:** That's pretty crazy.

**Trammell Hudson:** I mean, LEDs have a reasonable amount of bandwidth. So put a photo transistor on there and you can get a ROM dump.

**Trammell Hudson:** So that's – I figured you were like probing onto it, but you're saying you don't even have to – so you're not opening the camera at all in some of these cases.

**Trammell Hudson:** Most of the time, you don't have to open the camera at all. That's right.

**Trammell Hudson:** Yeah, I mean, because I've seen at least images inside cameras and they're all flex PCBs and tiny circuits and yeah. And not to mention, you know, cameras aren't cheap. So there's that too.

**Trammell Hudson:** One of the consumer devices I'm playing with right now are the IKEA Tradfry smart bulbs and LED dimmers. And in that case, in order to reprogram them, I am, you know, opening them up and hooking up to the debug port. And again, we're benefiting from the fact that most of these devices are ARM-based. And there are lots of really good tools for working with ARM CPUs and ARM firmwares. So it's pretty easy to disassemble it, figure out what needs to be patched, and then using either SWD or JTAG or something to be able to flash a new modified version back onto the embedded device.

**Trammell Hudson:** Yeah. And what about like locking and stuff like that, like security bits and firmware locking? And how do you deal with that usually if it exists? Yes.

**Trammell Hudson:** So that sort of segues into my other area of research, which is boot time security on devices. So I gave a talk recently at Hack in the Box here in Amsterdam about a time of check, time of use vulnerability that I found in Intel Boot Guard, which is attempting to do a signature verification on the flash that it's using to boot from the firmware. And due to an issue in the way that the cache is RAM, excuse me, the cache invalidation happened, it ended up fetching a few instructions a second time from the flash after it had already checked the signature on them. And that was enough to be able to replace those instructions with my own that would jump somewhere else in ROM and then gave us code execution.

**Trammell Hudson:** So is that because the first time it's checking that the stuff is valid and then it says, oh, it's good, whatever comes after this is cool, and then you put something different in there?

**Trammell Hudson:** It's that it checks the signature on it, and then it tries to run the code that it has validated the signature on. And so it's a time of check, time of use error, where if you can change what's in the ROM between when it has checked that signature, and then when it goes to execute it, you can have it execute your code instead.

**Trammell Hudson:** How do you start to look at that something like that might even exist? Are you just kind of following along the boot pattern and trying to figure out where there might be a time to insert reverse engineered code?

**Trammell Hudson:** So in that case, I do a lot of work on a project called Linux boot, which is replacing x86 firmware with open source software. And because I ended up having to reflash these chips all the time, I built a piece of open hardware called the Spy Spy that will log all of the flash memory accesses and then be able to provide them from an emulated DRAM rather than from flash memory. And as part of building that, I noticed that there were some addresses that were being read twice from the flash chip. And again, going with the disassembler, I was able to track down that that was a code fetch, not a data fetch, and that it had happened after that signature validation. So this is the case where we built a tool to speed up firmware development that then revealed a security vulnerability and then spent almost 10 months working with Intel for them to come up with a patch for it. Wow.

**Trammell Hudson:** Yeah, that's pretty intense. What does the Spy Spy look like? What is it developed with?

**Trammell Hudson:** So it's built on the ECP5 FPGA. There's a Croatian hackerspace, Radiona, that has made a really nice development board with the latest ECP5, 32 megs of DRAM, and a bunch of other fun things. It has HDMI and microSD and whatnot. So I gave a talk at CCCCamp about the Spy Spy and the difficulties in emulating the flash chips. There's a really hard real-time task where you have to be able to serve up a response from the memory in basically one clock cycle, which could be just tens of nanoseconds. And most DRAM has hundreds of nanoseconds of latency. So developing this in an FPGA allowed us to build our own memory controller that could do some interesting cheats to meet that timing requirement. Yeah. And so this is fun because it's open-source software running on open hardware using the open-source FPGA toolchain from EOSIS and Project Charleston XP&R. And again, it's really amazing how much we're able to use these open-source projects to stand on their shoulders and make things that would be very, very complex if we had to do it all from scratch.

**Trammell Hudson:** So let's hear about that memory controller then. So internally, so you're saying that you have to basically have the response kind of built into the logic fabric? Is that how it's fast enough? Or how do you get that? What are those cheats that you mentioned?

**Trammell Hudson:** So the big cheat is that DRAM, when you do a read from DRAM, it's a multi-stage operation that we think of in a normal program language, you read from an array, that's one sort of atomic step. The address goes off to the memory controller, data comes back. But under the covers, DRAM has a row activation stage where it has to copy the bits from the capacitors where they're stored in the actual dynamic RAM into registers. And then once that, and that row activation takes multiple DRAM clocks, and then when you do a read of a column from that row, that again takes a couple clocks to happen. Since we're receiving the address bit by bit on the SPY interface, we can actually start the row activation once we have 15 bits worth of the address. Oh, nice. And then we can do the column read once we have an additional eight bits of the address. And then we can do the final byte select when we get that last bit of the address. And that way we can have the data available for the SPY bus output on the next SPY clock cycle. So it's being able to interface with the memory on that sort of fundamental level rather than on the very abstract level.

**Trammell Hudson:** Yeah, that is really cool. Okay, and that actually helped clear up too. I was wondering when you were saying like a single clock cycle. So you were saying a SPY, like a SPY read cycle. That's what you really mean? You have to do it by one of those?

**Trammell Hudson:** That's right. Because you get a 24-bit address, you know, clocked one bit per SPY clock.

**Trammell Hudson:** Yeah.

**Trammell Hudson:** And so you need to have a result ready basically from the rising edge of that last bit of the address. You need to have the data present on the output pretty much on the falling edge of that clock. So you really only have half a SPY bus clock cycle.

**Trammell Hudson:** Oh, I see. Yeah. So it is still... I was thinking that like the SPY... Because like what is a SPY being clocked at like 10, 20, 30 megahertz? I don't know. More than that?

**Trammell Hudson:** Yeah, 20 to 80. Okay.

**Trammell Hudson:** Yeah. I was thinking that it was like because you get multiples of that, but you're saying that because you have to... You're basically like live decoding that stuff. Then it's from that last one. That's when it like finalizes it. And you're saying it has to pull it all the way back.

**Trammell Hudson:** That's right. That's right. So if you had to wait till you had the full address to do the read, the DRAM would delay you hundreds of nanoseconds. Yeah. And you really only have about 10.

**Trammell Hudson:** Got it. Okay. Man, that's a really interesting problem. And then so how does the... Is this because it is specifically in DRAM versus like... The normal case, I guess, is like a... X86 is going out and reading a SPY flash. Is it like hard-coded in the SPY flash normally? Or what is the normal case that you're trying to replicate, I guess?

**Trammell Hudson:** In the normal case, yeah, it's in a... I actually don't know what the internals of the flash memory looks like. But it's able to deliver the data at this sort of speed. Probably my guess is it doesn't have to do this sort of row column activation. And it's able to... Actually, I really don't know what they look like inside. Sure. Sure. That's fine. Yeah. That's... My expertise... I haven't pulled apart those chips. Yeah.

**Trammell Hudson:** So you're just saying, though, that it is effectively immediately available. And that's what you're trying to replicate.

**Trammell Hudson:** I think so. You know, if you had like StaticRam, for instance, you'd be able to do these sorts of reads, these random reads without any problem. Right. Yeah.

**Trammell Hudson:** Because StaticRam is just actual like flip-flops, right? That's what's internal on those?

**Trammell Hudson:** Pretty much, yeah. Yeah. But to buy 8 or 16 megabytes of StaticRam is pretty expensive. That's right.

**Trammell Hudson:** Yeah.

**Trammell Hudson:** Yeah. Yeah. And so then why do you need that much RAM in the first place? Is it just to do all the computation you're hoping to do or to have like multiple versions? Or why is it a larger RAM set?

**Trammell Hudson:** Well, the spy flashes that we're emulating are 16 or 32 megabytes.

**Trammell Hudson:** Okay.

**Trammell Hudson:** We've come a long way from the original 64 kilobyte BIOS chips that they're now... Yeah. Right. You know, they have an entire operating system inside of there.

**Trammell Hudson:** Well, that's actually a good... That's a good segue. So you also do retro computing. Moving along to the next interest of yours. So you've done a lot of retro computing stuff as well. What's your interest there? And like, what has been some of the projects you've worked on?

**Trammell Hudson:** I'm not really sure why I got into it. You know, I've been... For some of them, they're not really retro for me because I used them when I was growing up or when I was much younger.

**Trammell Hudson:** Right. Yeah. But contemporary computing just doesn't sound that cool, you know?

**Trammell Hudson:** And it's... One thing that I find really fun about them is how approachable they are. That, you know, a modern computer has so many moving parts and the operating systems are so incredibly complex that an ordinary user can't be expected to understand what all is going on. But with a lot of these old computers, they were built assuming that the computer owners would be knowledgeable about the insides, that many of them shipped with schematics. And people were expected to solder together expansion boards and things. In many ways, what I really like about the sort of Arduino movement is that it's brought back that kind of playfulness and the expectation that everything has schematics and data sheets. So, you know, with the retro computers, they're mostly understandable. And a lot of things are also then very much fixable because they're built with through-hole components or large-scale surface mount. The clock speeds aren't that high. They're typically five volts or three volts. So it's not, it doesn't require any high-speed differential signaling type things. So, you know, if something's broken in your antique retro machine, you can probably fix it. Or you can build a small microcontroller or FPGA part that replicates the pieces that are no longer functional. And there's a lot of fun areas where people have done exactly that. So, you know, disk drives, for instance, have pretty much all failed. But you can buy kits that will give you an emulated SCSI disk so that you can still boot your machine off a solid-state drive or compact flash card. You know, it's possible to build adapters. Say, take a USB keyboard and adapt it to some of the older formats so that you can still talk to these machines. And as you start to go even further back, things like the PDP-11 that we restored just has a regular serial port. So you can hook it up to whatever machine. It's very easy to connect it to a modern computer.

**Trammell Hudson:** And there's just something fun about, you know, putting a PDP-11 onto a network or doing similar things with that. I mean, they have their own aesthetic and everything, too. And sometimes you find fun things inside. I saw the Easter egg you found in the Mac SE. How did you find that?

**Trammell Hudson:** So that one was a lot of fun. We literally found a Mac SE on the side of the road in Brooklyn with a failed hard disk and a non-working floppy disk. So we were discussing what to do with it. And one of the hobbies that some of us at NYC Resistor had was dumping the ROMs and digging through them, looking for fun either fonts or bitmaps or Easter eggs. And Adam Mayer at Resistor noticed that, hey, there's something that looks kind of like faces if you plot these bits out. And that led us down the rabbit hole of figuring out the old Mac PICT format and putting together little Python programs as you code them. And, you know, the Easter egg itself was pretty well known that you could get to it through the Mac bug or Max bug debug hardware. So this was just a really fun exercise in understanding an ancient file format and looking for interesting things. And there's also a really fun thing that came out of that are the Mac ROM scarves from Knit Yak. Fabian is doing this cool computational knitwear, and she saw the sort of the black and white ROM dump images that we were making and converted it into a physical item. So you can actually, you know, wear the bits when it gets called out.

**Trammell Hudson:** Yeah, Fabian has been a past guest of the show as well. So people can go and listen to that Knit Yak episode that is back in 2015. That was episode 257. So we'll link that in the show notes too. But yeah, that's kind of weird to think about like wearing code, but it's a fun idea.

**Trammell Hudson:** And the other fun thing about a lot of those machines is they didn't have a lot of storage space, but they also didn't want to build complicated code. So bitmaps are frequently stored just as literal one bit per pixel or eight bits per pixel. So if you plot them out, you can see the fonts or the images. So yeah, some of the scarves have the Happy Mac on it because it's literally in the ROM just as a 32 by 32 image.

**Trammell Hudson:** That's great. That's great. Because you're saying it's because it's part of the entire ROM image that might be plotted on there.

**Trammell Hudson:** Right. Exactly. Yeah. Yeah.

**Trammell Hudson:** Yeah. And it's interesting too to kind of, you know, I feel like the theme I'm seeing with you as well is that you're taking this knowledge, you know, you're kind of like not just reverse engineering the thing itself, but reverse engineering the knowledge, like how they might pack bits or how they might, you know, interact with hardware or the file formats. And there seems like there's a lot of value there too.

**Trammell Hudson:** I think there is. And there's folks from archive.org that have a project to try to document all of the file formats. One nice thing about the retro formats is they tend to be very, very approachable, you know, because there wasn't a lot of code space. There wasn't a lot of fast CPUs. So most things tended to be in relatively legible forms. You know, it's much, much easier to decode a PICT or a bitmap than it is if you encounter a JPEG, you know, which is just a bunch of DCT coefficients. You know, there's... Right. Yeah. So in a lot of ways, it's easier to handle those older formats. And, you know, I'm definitely concerned about the sort of digital dark ages where, you know, if... Where we've lost knowledge about how to decode, you know, some works. You know, if somebody gave you a, I don't know, 123 file on a five and a quarter inch floppy, you know, how would you be able to recover that?

**Trammell Hudson:** Right. Without being able to go and Google a .123 recovery tool or whatever it is, which would have been my go-to.

**Trammell Hudson:** Yeah. And 123 might be a bad example because I would not be at all surprised if Excel wouldn't read that just fine. Yeah. But, you know, maybe if you had a, I don't know, some Amiga IFF image or, you know, something more obscure.

**Trammell Hudson:** You know, I think that that is a... You know, I think that kind of feeds into the open source idea as well, right? It's like as you move away from more open things, file formats, open tools, whatever, the chance for data loss or data obfuscation forever is like, it's very high. And I'm sure that that's a topic near and dear to your heart as a reverse engineer, kind of, you know, your ability to go and open things back up and reuse them or repurpose them is pretty important.

**Trammell Hudson:** Yeah. And I'm definitely much more concerned about the closed source files and formats. The wonderful thing about open source is you can probably set up a virtual machine and install an ancient version of Linux and still build that code from 1995 to read something from 25 years ago. But yeah, if you have to find a, yeah, an Atari ST or something, it's probably gonna be a lot harder.

**Trammell Hudson:** I'm just sitting over here thinking you're having a panic attack that 1995 was 25 years ago. It's, yeah, time keeps on marching.

**Trammell Hudson:** Yeah, it's, uh, back in 95, I read a book by Peter Solis called A Quarter Century of Unix. That was a history of, um, you know, the, the 25 years of, uh, of Unix leading up to that point. And I think we're, we're due for now a quarter century of Linux.

**Trammell Hudson:** Wow. Yeah.

**Trammell Hudson:** 50 years of, 50 years of Unix and a quarter century of, uh, of Linux.

**Trammell Hudson:** That's, that's, uh, that's pretty crazy. Yeah. I mean, the other thing that kind of pops out from thinking about the retro computing stuff is like how close, you know, the, the lines between like full scale computing. I don't even know how the words here, but like full scale computing versus like embedded computing, like retro computing seems more like embedded is today. And it is that, uh, you know, you need to have that low level control. You need to have compressed code space and stuff like that. And it, there's a lot of benefit to that, I think, but there's, um, things are moving away from that. You know, speaking of Linux, I guess, you know, things, systems get more complicated just to be able to do more.

**Trammell Hudson:** It's really shocking how, uh, powerful a microcontroller today is that, uh, the, the teen C4 that was announced, uh, a few months ago, uh, you know, it's, I think it's multi-core 600 megahertz. With a floating point unit and, uh, branch prediction and maybe speculative execution. This is, this would have been a incredibly powerful machine, uh, a few years ago. And now it's a, um, you know, a 10 or $15, uh, throw away, uh, embedded device.

**Speaker ?:** Right.

**Trammell Hudson:** Right. When you have another, uh, section on your site about, I'm trying to find it now, but it was about tiny microcontrollers and stuff like that. I, I wanted to call out the, uh, the RFID thing you did with two pin, was it two pins? What was that one?

**Trammell Hudson:** Yeah. Yeah. So the, uh, so this is based on some work that, um, uh, that scan line, uh, did, she, uh, had figured out a way to get a tiny 85 to act like a RFID chip. Uh, so I, uh, starting with her research, I was able to extend it a little bit, make it a little more flexible. Um, my, at the time I, I was carrying three different RFID tags and was frustrated when I'd go up to, uh, uh, to the different doors and, you know, had to fumble to find the right card to, uh, to scan. So I wanted to make, uh, one card that I could select the different IDs with. Um, so, uh, again, starting with scan lines work, I was able to, uh, modify her code to, uh, compress it enough to fit these multiple IDs and into the one. Um, and the actual circuit, like I say, it's just, uh, literally a, a trace on the circuit board that makes a couple of loops and connects the two clock pins. And it completely abuses everything about this, this, uh, poor microcontroller. There's no power. There's no ground. Um, the clock is being provided by the, uh, the RF, uh, the 125 kilohertz RF. Um, but it's dependent on the fact that there are protection diodes to rectify that. And it's dependent on the fact that there's enough leakage, uh, uh, current through the dye to, uh, power up the CPU from the clock signal coming in. Uh, and it's also dependent on the fact there's enough sort of stray capacitance on the dye to keep it running, uh, when the, when the signal is being rectified. Um, everything about this shouldn't work.

**Trammell Hudson:** Yeah. And it's like, uh, like, I think you wrote, like, it's a testament to the, the robustness and the, the process capabilities of, of chips these days. It's just.

**Trammell Hudson:** And it worked quite reliably. Um, I mean, the whole, uh, passily powered through the, uh, through the RF is, is pretty magical to begin with. Um, but then just the, uh, the fact that everything else worked, um, is pretty amazing. Um, with some of them, uh, with one of the ones I've added, uh, a few more loops to the, to the antenna, which seemed to make it more effective and produced, uh, enough voltage and current to light up LEDs, uh, on the RFID. And then, uh, you want to get scanned, which, you know, uh, makes it a little more fun.

**Trammell Hudson:** And so it has to have enough, does it have to have enough, uh, like capacity, straight capacitance to basically power a response as well? Or, or what is the, how much power are we talking about here?

**Trammell Hudson:** I never actually tried to actually measure the power. I'm not even sure how we could, you know, if we put an ammeter on it, maybe we could see some current going through.

**Trammell Hudson:** Um, yeah, the load of the load of the, uh, ammeter might, uh, might, uh, take it all down. Exactly. There's lots of cards there.

**Trammell Hudson:** Everything was very fragile in that respect. Um, the, uh, so the, the interesting thing is that with RFIDs, the, the card itself doesn't transmit. Which, uh, was really sort of surprising to me. Uh, what it, what it does is it, um, uh, it shorts the, uh, the, the antenna, the two leads on the antenna together. Uh, and then the, the card reader is measuring the, the power being consumed by the transmitter.

**Trammell Hudson:** Huh.

**Trammell Hudson:** Uh, so it's basically like, like, uh, uh, like, uh, uh, half of a transformer. So it measures the current going through, uh, through its side of the coil. And when the card shorts, uh, its side on the antenna, that causes an increased current draw. Uh, and so by pulsing, uh, that, um, but by shorting and, and, uh, unshorting the antenna, uh, that signals through the, the induced current draw, uh, what, what the data stream is.

**Trammell Hudson:** Well, that's really, that's really, I never looked into that before. That's, that's interesting. I guess that makes sense too. Cause you're going to have like a, in like a passive system, you're not going to have much power for retransmit. Um, and that's kind of, I guess the, there's like, like farther field versions of this now too, right? Where they're doing the same thing with like radar or something similar where they're able to tiny devices are able to basically transmit where they are in a factory or, or, uh, uh, the floor of a, uh, warehouse. Right, right.

**Trammell Hudson:** Yeah. I've read about these sort of, uh, uh, millimeter wave things, but I'm not, uh, despite being, uh, you know, an amateur extra, uh, radio operator, I don't actually know anything about RF. I just kind of muddle through it and, and hope that I can figure out how to make things work.

**Trammell Hudson:** Yeah. Well, I think a millimeter wave is its own, you know, emergent category. So, uh, well, that's good. What is your, uh, so what is your RF? You know, we're, we're doing a speed run here through all your projects, but, uh, what are some of your radio, radio interests?

**Trammell Hudson:** So I'm, I'm a really big fan of, uh, some of the digital modes like, uh, PSK 31. That's a, uh, ultra low bandwidth, um, uh, 15 Hertz of bandwidth, um, uh, uh, digital, uh, uh, kind of like a teletype mode. And it's, uh, really sort of amazing, uh, to see, you know, how much, uh, how much data you can pack onto, onto a shared channel with, um, with, uh, PSK 31 over single sideband. So there's no carrier, uh, everything is, um, uh, cosine squared ramped so that it minimizes the, uh, sort of splatter. It's, it's a really neat protocol. Um, uh, I also really enjoy the, uh, uh, playing with SDRs for a lot of these things. Um, and I think one of the things that SDR, uh, that I found just most magical is the realization that the term bandwidth, uh, literally means the width of the data near the width of the signal on this RF band.

**Trammell Hudson:** Yeah, right. Exactly. I had the exact same thing. Like the first time you see a waterfall plot, you're like, Oh my God.

**Trammell Hudson:** You're like, Oh wow. Yeah. The, the wider it goes, the more data you can send.

**Trammell Hudson:** That's right. Yep. Yeah. And, uh, um, for, yeah, I don't know. I, I, I, the first thing I had the same reaction to you. The second thing I was, I was incensed that when I was being taught that, you know, taught radio stuff and communication stuff in school that I did not, that they did not just show you that right away. You know, like, like when you like decode an FM, you know, you're like, you're looking at a waterfall plot of an FM station and then you like turn your head sideways. You're like, Oh my God, there's an audio waveform. It's just like, why didn't anyone tell me this? You know, it's just, uh, it's very frustrating.

**Trammell Hudson:** It's really neat to see on the waterfall plot how much you can visually pick out that, Oh, that's an FM. Uh, that's an AM. That's some CW stuff.

**Trammell Hudson:** Yep.

**Trammell Hudson:** Um, the spread spectrum, uh, frequency hopping things that, where you get the blips that sort of race across the waterfall. It's, it's really a magical way to see a, um, this invisible RF world.

**Trammell Hudson:** Yeah. I'm just amazed that people did it before they had those tools. You know, they're just able to visualize it outside of it. And it's just, yeah, there's some, there's some wizards among us. Yes.

**Trammell Hudson:** Yes. The, uh, the, the, the other part that I really like about SDR is that it, uh, it brings things back into the software world where I feel more comfortable that, you know, if you ask me to design a, uh, you know, a, uh, super heterodyne regenerative receiver, I'd have no clue. But, you know, once I get an IQ waveform, I can probably figure out some way or some libraries to, to throw at it, to, to get, uh, the data out. But trying to do it in an analog circuit is largely beyond what I feel comfortable with. And, um, you know, between the, uh, the, uh, SDR is letting me do that in the RF world and FPGA is letting me do that in the hardware world. You know, suddenly, uh, I'm, you know, it's made it possible for software people like me and, uh, to, you know, suddenly have a much wider range of, of interfaces to, uh, to the outside.

**Trammell Hudson:** Yeah. No, that's, that's a good point too. And so is that like one of the first steps of your project is to kind of get it from the hardware world into the software world?

**Trammell Hudson:** I think so. I think once, once we have things in bits, uh, you know, we can throw, we have a lot of really great tools for pulling them apart, for looking at them, for analyzing them. Um, but yeah, when we're dealing with, uh, with analog signals on the wire, it's, it's a lot harder. Um, yeah. Uh, although, you know, I would, I would, uh, definitely not give up my, my physical oscilloscope. The, the ability to look at a, at a trace and say, ah, I see what's happening. And it's right.

**Trammell Hudson:** Right. Um, it's sanity check really.

**Trammell Hudson:** Exactly. Exactly. Um, you know, I recently had with the spice by project, we were having a problem where we were getting some, some really weird results. And it turns out that if you have multiple things, multiple, uh, uh, drivers on, on that bus, you don't get a digital waveform anymore. But the, uh, the digital inputs are trying to make sense of it. Um, and, you know, it's, um, uh, being able to look at it on the, on the oscilloscope and say, ah, you know, this is clearly multiple digital signals being, uh, added together and mushed together.

**Trammell Hudson:** Um, you know, you see like half, you see like half, half signals and stuff like that. You see like, uh, you know, blips and.

**Speaker ?:** Exactly.

**Trammell Hudson:** So that saves us a huge amount of debugging. Um, or saved me a huge amount of debugging to be able to, uh, look at that and realize that it's not a problem in my software. You know, the problem, the problem is somewhere else.

**Trammell Hudson:** Right. Yeah. It's like, uh, yeah, maybe garbage in garbage out, but where's that garbage coming from? You need a garbage inspector. Yeah. Yeah. Well, you mentioned, uh, you mentioned scopes. Um, you also have played around with, uh, vector stuff and vector is part of old oscilloscopes, but also video games and stuff like that. What was, what was your, uh, interest with that?

**Trammell Hudson:** So that definitely overlaps with the, um, you know, with, with the retrocomputing side of things. Uh, I, I really have a affection for the, um, both the, the aesthetics of, of the, uh, the vector games. And, uh, also the, uh, the simplicity of a lot of them that, uh, growing up with, um, with, uh, you know, the, the, the Pac-Man and Asteroids era coin op games. Uh, I always felt that, oh, I could write that, you know, and, and I think it's, it's very empowering for, um, you know, as a child to, to, to realize that these, these games were written by very small teams of people. In some cases by individuals.

**Trammell Hudson:** And in some cases in hardware.

**Trammell Hudson:** Yeah, in a lot of cases in hardware. You know, compared to, you know, if you're, if you're facing a, uh, modern, a triple A game these days that has a hundred million dollar budget and a team of thousands working on it. You know, it's, it's a little, that it's a little more intimidating to think about trying to, uh, to build your own version. So, yeah, I have this, this, you know, nostalgia for, uh, for, for these vector games for sort of the simpler, uh, versions of them. And, uh, I've never felt that the, the, uh, LCDs give quite the same feel of the, uh, the, the actual, uh, so the, um, the vector displays. Uh, unfortunately there are people aren't making CRTs anymore. And a lot of the electronics that were being used to drive the, uh, vector, uh, CRTs have, have failed. Uh, so I, I built a project, um, uh, that could generate, uh, analog vectors with some, uh, some dual DACs. And this is definitely a case of, uh, throwing more hardware at it. Um, that probably would have been easier if I actually knew how to do any op amp and analog work.

**Trammell Hudson:** But still, that's, that's great. I mean, like, that's, that's the basis of modern computing. I think it's just, you know, Silicon's cheaper. Why not do it?

**Trammell Hudson:** Yeah, exactly. Just, uh, do it in software. Uh, and then I hacked up, uh, the, uh, MAME emulator to be able to output the, um, uh, the starting endpoints of the, uh, the vectors. Uh, MAME is, uh, is emulating the, the original hardware, uh, that the, the, the cabinets were running on. So it actually gets the, for most of the vector games, it gets a, uh, 10 or a 12 bit, uh, XY coordinate, uh, to draw to. So, uh, I hacked up, hacked up MAME to print those out to the serial port that feeds into a, uh, into a TNC microcontroller that then drives some DACs, uh, to, uh, to generate those, uh, those vectors. And the games are really playable and they're really, uh, a lot of fun to see in that, um, you know, in, on the original sort of displays.

**Trammell Hudson:** Well, so we've had, uh, a past guest, uh, Todd Bailey, another, uh, New Yorker, uh, talk about his, uh, vector stuff as well. And one of the things he mentioned was like the, the line hops is like a hard thing. How did you, so did you have to do something in the MAME to, to, uh, to redraw the line segments so that they didn't like skew and overlap and stuff like that?

**Trammell Hudson:** So yeah, Todd's, uh, VEC 9 game is absolutely beautiful. Uh, you know, I got to play it at Maker Faire a few years ago and it's, it's a really stunning, uh, uh, piece of work. Um, I think he said it's the, the first vector game written or first new vector game in, in, uh, in a few decades. Um, it's really a lot of fun. So there are, uh, uh, there are a lot of issues that you run into with, um, with the fact that, uh, CRTs don't move instantaneously. Um, especially, uh, there are two different types of CRTs that I know of. There's the, uh, things like oscilloscopes use an electrostatic deflection and they can move at, um, you know, tens or hundreds of megahertz to, um, to move the beam around.

**Trammell Hudson:** And that's just because you're, you're driving an electric field basically to, to influence the E-beam. Is that kind of the idea?

**Trammell Hudson:** I believe so. Um, again, not an electrical engineer. I'm, I think we're just going to say you're close enough travel.

**Trammell Hudson:** Come on.

**Trammell Hudson:** And the, the other thing is the, if you, if you open up an old CRT oscilloscope, the tube is like half a meter deep, um, and still only has, uh, you know, 10 centimeters of deflection. So it's having to deflect over a much, much smaller arc, but the, um, the, the big vector displays are almost all, uh, magnetic deflection, which gives them a much, much wider, um, uh, angle that they can deflect to. But the, uh, the, the magnetic coils almost have inertia that you can't, you can't move them in their, their, uh, state instantaneously. So you have to, uh, in your vector generation, you have to essentially model that. So if you want to move the beam quickly from point A to point B, uh, you can set the voltage to the new value, but then you have to wait for the beam to actually get there. So, uh, in the, in the firmware for, um, uh, for, for my vector generator, it has some, some, uh, uh, tunable parameters for that sort of thing. So that you can ensure that your corners, uh, stay sharp and, uh, that your, um, uh, that the lines started at the right point rather than starting somewhere along the line.

**Trammell Hudson:** So, so you're saying that the greater deflections needed just because the screens are bigger. Is it, is that right?

**Trammell Hudson:** Or yeah, it's, it's, it's both that they're, they're not as deep because nobody wants a, a three or four meter deep, uh, uh, CRT. Yeah. I don't even know if you could make manufacture such a thing. Right. Um, right.

**Trammell Hudson:** You need like a, one of those, uh, what's that, uh, that glass shape. That's like a, you know, a glass drop. Um, yes. Yeah. Yeah.

**Trammell Hudson:** Something just extends out to infinity. Um, uh, yeah, they, they want larger CRTs. They don't want them to be as deep. Um, so as a result, uh, the magnetic deflection is a much more popular thing to do. And, uh, the other thing that, uh, that I haven't actually looked into, um, but a lot of the, uh, a lot of the, the modern, excuse me, a lot of the, uh, the, uh, the later vector games had color CRTs. So they could actually do, uh, different, they could do, uh, RGB, um, uh, colors for the lines. So like the, uh, the star Wars, uh, vector game is, is in color for instance.

**Trammell Hudson:** Yeah. And you have some, I mean, we're going to be linking all of these projects, of course, almost everything we've talked about, I think here today has a page for it. So people can definitely go and check out all this stuff, but, uh, yeah, the, the color, um, the, the, the, the tie fighter game is especially nostalgic for me. You know, that's awesome. Yeah.

**Trammell Hudson:** And, uh, there was a fun, uh, I had a fun write up on this in, um, in, uh, Travis Goodspeed's, uh, journal, um, uh, a year or two ago. And I think, uh, through the magic of their, uh, polyglot file formats that if you load it as an, as an animated image, uh, you get the, uh, uh, uh, replica of the, uh, the tie fighters, uh, um, racing across the screen.

**Trammell Hudson:** That's really cool. Well, let's see. So, okay. So we've talked about a lot of the stuff on here, but not everything, of course. Um, you've also reverse engineered robots. I thought that was kind of interesting. Uh, what was, what was the deal? And a lot of this stuff I should mention too, is, is, is coming through, uh, uh, NYC resistor as well, which you were a prominent member.

**Trammell Hudson:** So when I lived in New York, uh, we were, uh, I was at resistor, you know, three or four nights a week and most weekends. It was really, uh, you know, uh, sort of like the living room. Um, for a lot of us in New York, we don't have, none of us had huge apartments. So having a shared space for, for tools and projects was, uh, absolutely a necessity. And resistor was a, a, a wonderful, uh, welcoming place, uh, a very diverse and inclusive set of members. And what I really love about resistor is the, the mix of, uh, artists and engineers and fashion and music and, uh, textiles and paper crafts. And, you know, the, the, the view of technology, uh, uh, was just, you know, went across pretty much everything that it wasn't just people doing computer security or just people doing 3d printing. It was a little bit of everything. Um, so yeah, so, uh, somehow, uh, ended up with a set of, uh, Puma robot arms that had been removed from their factory with a set of, uh, um, uh, bowl cutters. So the no wiring harnesses, no motor controllers, just, you know, just, uh, uh, some, yeah, some short pigtails. Uh, and as a fun project, I, um, uh, with spent some, some hours with the multimeter, just, uh, doing continuity to figure out what was wired to what and, uh, built a, uh, an open source library to do the inverse kinematics for the, uh, for the six degree of freedom arms. Um, also just to try to understand a little bit better, uh, how, how to interface with them. Um, they, they're relatively high precision, um, and, uh, uh, relatively powerful. Um, so we had a fun project at my office where we built a, uh, shuffleboard attachment for them and then, uh, uh, invited, uh, some of our colleagues to build, uh, their own AIs to play, uh, tabletop shuffleboard with, uh, with the robots.

**Trammell Hudson:** And, uh, you know, I'm sure they're, they're no better than the, you know, the drunk, uh, bar denizens that are normally, uh, playing shuffleboard.

**Trammell Hudson:** Yeah, they, they, they were slightly better. Um, but the, uh, repeatability was really hard in shuffleboard that, um, uh, I think a lot of it comes to reading the, um, the sawdust on the table and the, uh, they, they, they didn't have a view of that. They only had a view of the, uh, the, um, uh, the, the puck configuration. So with that, um, with that limitation, they still did pretty well, but, uh, you know, a good, a good human was able to, to beat them. Unfortunately, that's good.

**Trammell Hudson:** No, no, no. It's okay. We're okay with, I think we, we have a limited time span for humans beating robots at anything. Let's just revel in it for now.

**Trammell Hudson:** You know, yes. Uh, when, uh, when alpha goes, which is over to a shuffleboard and ping pong, then, then we'll, uh, yeah.

**Trammell Hudson:** Oh yeah. Yeah. It's all over. So you, and you had mentioned, you'd written about the, um, the reverse engineering process of that. I was interested how you said you use the scope on the, uh, on the lines to actually sense the quadricer decoding. Could you explain that a little bit?

**Trammell Hudson:** Unfortunately, they didn't come with any data sheets. So what we had were just a bunch of wires coming out. Um, so with the, with the multimeter, we were able to find the continuity and, uh, we identified, um, the, uh, the DC motors pretty easily. And then we also identified for the quadrature encoders, uh, which, which four wires they, they were. And we knew that they would have a power ground and then sort of a, an A and a B, uh, output. Um, so we made a, uh, uh, uh, a good guess as to which was which, um, luckily did not blow up any with, uh, reverse, uh, reverse polarity. Um, and, uh, we're able to identify that they were, uh, you know, that we had to put, uh, that first it looked like there was no signal coming out of the, um, uh, the A and B output lines. Uh, and we realized that we needed to put external pull-ups and that they were being pulled down by the, by the encoder. And a lot of this came from sort of, you know, having seen a quadrature encoder before having some ideas about what is it likely to be doing? Um, and a lot of this reverse engineering just comes down to that sort of, you know, making guesses about, uh, you know, how could this work? What, what are the likely ways that it could work and, you know, um, and then trying things, uh, uh, you know, with four wires, there are like, uh, 16 ways that it could be wired up and hopefully only one of them causes things to blow up and, uh, hopefully we don't pick that one. That's good.

**Trammell Hudson:** That's good. I mean, I, I guess the, the thing I was wondering about too, is like, so, you know, I haven't done much with motors. Um, just even thinking that there was like an encoder on board and like understanding that and looking at an escope is interesting, just kind of, and, and like the encoder itself, like, uh, I don't know if it was Hall effect or if it was like a optical or how it was actually being encoded, but just thinking that like there would be one on there, you know, I just don't work with robots. So I, I don't know, but like, that seems like a, that's a smart thing to, to understand there and, and thinking about that and pumping that into a system.

**Trammell Hudson:** And the, the, the thought was these things need a higher repeatability and trying to run open loop with a DC motor is just not going to be, uh, very accurate. Um, you know, it's not going to give it that repeatability. So we figured there's probably going to be some sort of encoder. And, uh, when we disassembled, um, part of the, uh, uh, the motor housing and we saw that the motors had shafts coming out of both the front and the rear where the front, the front went into a gearbox that then drove the, uh, the, the, the arm mechanism. And then out the rear went into a, uh, uh, kind of light duty plastic box of some sort. So that, that, that was a pretty good hint that there, there's something in there that's probably doing some sort of, uh, some sort of counting or encoding. Um, and, uh, the, the, one, one of the issues we ran into is, uh, a lot of the, the servo controllers, the DC motor controllers, uh, weren't well set up to handle the quad share input. So, uh, like a lot of things ended up building a, uh, a small microcontroller based system that would do some translation layers, uh, on those pulses into counts that we could then feed into, um, into a closed loop servo controller.

**Trammell Hudson:** Put it back into software and the realm that will, uh, make it backable. Exactly. That's good.

**Trammell Hudson:** That move it to somewhere we can do, do our own PID and, uh, uh, you know, tune it ourselves.

**Trammell Hudson:** Well, this all kind of rolls up together to the fact that you, the thing we haven't really, I guess we've kind of mentioned it, but you do, you do security research. That's like your, your gig, right?

**Trammell Hudson:** That's my, uh, my day job when, when I'm, when I'm not, uh, taking other things apart, I take things apart for, um, uh, to try to figure out, uh, where are the security vulnerabilities and what do we need to work with? Um, where can we work with the vendors to try to, uh, you know, improve, uh, uh, the laptops and the servers that, that we depend on.

**Trammell Hudson:** Right. And you, so you've done, uh, you published about some of it on your site about, uh, the YubiKey and things like that. But, um, what is your, uh, I'm always kind of sensitive. I don't know how much security people are allowed to want to talk about, but, uh, what are you allowed to talk about in the security world and the things that you work on?

**Trammell Hudson:** I've been really lucky that, uh, most of the work that I've done in the security spaces, uh, has been in, in, has ended up in the open. Uh, so I've been able to present at, uh, CCC and, uh, DEF CON and events like that about, about this work. Um, the, the one that, uh, that sort of got me into that field was a few years ago. I found a, uh, a firmware vulnerability in MacBooks that allowed someone with, uh, access to the Thunderbolt port to, uh, flash their own firmware into the, uh, the MacBook main board.

**Trammell Hudson:** It's kind of a big deal. Kind of a big deal.

**Trammell Hudson:** Um, yeah, uh, this was, uh, because it was trendy at the time, we gave it a fun name. We called it a Thunderstrike since it came into the Thunderbolt port. And, uh, this, it, uh, it got a lot of press and, uh, in a lot of ways, uh, I think brought, uh, firmware, uh, vulnerabilities, um, into, you know, much, um, much more, uh, uh, well-known, um, in, in the community. The, the big problem is that a lot of folks have always assumed, oh, hard, if, if, if an adversary has hands on the hardware, it's game over. And I think that's a, um, a much too limited sort of view. I think that it's possible to have threat models that allow adversaries to have either temporary hands-on or perhaps even more extended time with it. And we can still possibly, uh, you know, have some faith that the systems will, will be okay. Um, and part of that is, is sort of demonstrating here are places where we have problems that we need to fix. Um, and, uh, you know, Apple, uh, took the Thunderstrike vulnerability very seriously. They released patches for eight years worth of hardware, which is just absolutely amazing. Right. Um, right.

**Trammell Hudson:** That's no small task. That's a lot of regression and testing and making sure it doesn't bork. Yeah, exactly.

**Trammell Hudson:** Um, so after that one, um, uh, I've also shifted into more trying to think about how do we build more secure systems? So I've been working with the, the core boot community on, uh, open firmware for these machines. And then also, uh, helped start a project called Linux boot, where we're trying to replace the proprietary firmware in, uh, in servers and some laptops, uh, with Linux, which, you know, it is a large amount of code, but it's a fairly well tested and fairly, uh, widely understood code base. So rather than having, you know, uh, a few tens of people at some small firms doing a firmware development, this lets us take advantage of the fact that everyone is looking for security vulnerabilities in Linux. And, uh, typically when they, they're found they're patched relatively quickly. Um, the other big thing that we, we like about, uh, open source firmware is it means it's possible for people to build their own versions, either for research or for customization, but also to patch the vulnerabilities on their own schedule. You know, a lot of this hardware never, ever sees any firmware updates, uh, because, you know, once the, once, once the system's sold, most of the OEMs are done with it. Uh, but if you can build your own firmware, you can patch, uh, uh, firmware vulnerabilities and, uh, the community can also then take over abandoned hardware and continue to support it. Um, so if, if a system is important enough to you, you can either do it yourself or you can find people who might be able to help you out with it.

**Trammell Hudson:** Yeah. So could you give a, what the, so you had said like tens or dozens of multiple dozens of people that are doing it. When you speak about that, you mean like internally, they'd be writing custom firmware for boot imaging and stuff like that.

**Trammell Hudson:** Uh, there's a, uh, there's, there's only a handful of companies called, uh, independent BIOS vendors that, that make most of what people think of as, you know, uh, as the BIOS, the UEFI, uh, for their, for their computers. Um, and the bulk of the code is actually coming from, uh, from Intel's, uh, EDK2 reference implementation for UEFI that the, uh, uh, in, in one of my talks, I have a chart showing, you know, the, the bulk of the code comes from that. The device manufacturers will pay the independent BIOS vendors to port, um, that reference implementation to their new, uh, servers or laptops. And then the OEMs will, uh, do some amount of customization on top of, of that when they buy it from the, from the ODMs. Um, so this means that, you know, any changes need, uh, if there's a security fix, it might have to go through four different companies before it actually reaches the end user.

**Trammell Hudson:** Yeah. That's, that's, uh, that's a little, that's unlikely to be as secure or as helpful. So then, so what would be the, so the alternative is this Linux thing that's on, on there instead then, and then how does, how does that look different for a OEM? They would basically just be able to build it and load it on there or, or is this meant as an end device or sorry, an end replacement for the end user, um, that they could then load on to something that they've already got as well.

**Trammell Hudson:** Well, the vision of the Linux boot project, uh, is that the OEMs will, uh, will do the port themselves and that they'll sell machines with this, uh, with, you know, either core boot or Linux boot, uh, firmware, uh, built into it where the, where the end customer who now owns the computer, uh, has the, the freedom to modify it if, if they want to. Um, in a lot of ways, uh, I think this is very similar to the, um, uh, the Unix wars of the, uh, the 1980s and nineties where all of the major manufacturers, uh, frequently made their own CPUs. They also then made their own versions of Unix and they were all incompatible in, in vague ways with their own sets of security vulnerabilities. Yes. You had the HP UX on the PA risk hardware. You had Solaris on the spark hardware. You had, uh, AIX on the, the power hardware. Um, and then pretty much out of nowhere, uh, Linux came about and took over and, uh, very quickly, uh, the operating system became, um, no longer a distinguishing feature for the, uh, for the OEMs that they were now competing on making better commodity hardware that ran Linux well. And I hope that a similar sort of dynamic will play out in the firmware space that the, uh, all of these customized, um, you know, value added, uh, UAFI implementations will end up becoming legacy. And the, uh, the OEMs can focus on, uh, using the, uh, the common, uh, Linux boot or core boot, uh, firmware and focused on just making better, uh, systems that run that well.

**Trammell Hudson:** Do they see it, their value add as something that is like competitive advantage? Like, are they resistant to this sort of thing?

**Trammell Hudson:** There's a lot of, uh, sort of not invented here, uh, going on with it. Yes, that they do think that they, that they're providing some value, um, from the view of a large enterprise customers, it's, uh, it, it sometimes is negative value because it's, it's essentially a vendor lock-in that if you end up having to build your procedures and your systems, um, you know, customized to, uh, to some vendors specific, uh, firmware implementation, it makes it much, much harder to, uh, to migrate to other vendors.

**Trammell Hudson:** And yeah, I can imagine the vendors like that then too, cause they, they want lock-in and end users don't. So, yeah, this is, uh, that's fascinating. How long is, how long is the, uh, the Linux, Linux boot project been going on?

**Trammell Hudson:** I guess we're Linux boots in about, uh, going into its second year. Um, I gave a talk about it at, uh, uh, I think 34 C3, losing track.

**Trammell Hudson:** Um, yeah, that's right. Give enough talks and they all start to blur together.

**Trammell Hudson:** Uh, and this is, uh, has some, some backing from, um, the folks at, uh, Google and Facebook who are, who deploy hundreds of thousands of machines. So they're very interested in being able to control the firmware on those machines.

**Trammell Hudson:** Yeah, I could add, yeah, with, with very large security, uh, uh, implications if, if things go wrong. So I can imagine they would be interested in that. And there's a bunch of bright people there too. So, uh, so how close, I guess, are you, are you, where are you in the life cycle of, uh, handing off the repo keys? Are you, have you already done this or?

**Trammell Hudson:** Well, uh, since, uh, since we have these, uh, uh, these large contributors from, um, from the hyperscalers, uh, I luckily don't have to, uh, do very much anymore that there are people doing code reviews, there are people doing, uh, documentation, there are people writing deployment guides. And, uh, I just get to hang out in the Slack channel and, and talk with, uh, really bright people about firmware things.

**Trammell Hudson:** So what is, so what's next then? What's the next, uh, so you'd mentioned you have, you'd mentioned one new project. I've already forgot what it is. We've had enough top project talks here, but what are you, what are you working on these days that you're interested, that you're excited about?

**Trammell Hudson:** So I'm right now working on extending, uh, uh, spy spy to handle some more different flash devices. Um, starting on the security front, I'm looking more at, uh, enclaves, uh, specifically the, uh, AMD SEV and Intel SGX, uh, you know, from the security perspective of what are the risks of moving, uh, confidential computing into these things. Um, uh, I'm excited about the, uh, some of the, the community support for, um, uh, Linux boot on some, uh, some super micro, uh, servers along with, uh, micro BMC, which means that these, these machines will now boot, um, almost entirely with, uh, with, uh, free software, uh, from the, the BMC to the X86. That's cool. I think what else is going on. Um, and then the, uh, the thing that I'm currently working on, hoping to put together a guide is how to build your own, uh, custom firmware for these Ikea lamps. That might be my, my next, uh, maybe my next, uh, talk at Congress or, or somewhere else.

**Trammell Hudson:** I think that's what you had mentioned earlier too. So that's good. And, uh, and you are in Amsterdam now, so you no longer are in New York. You, uh, you, you've hopped the pond. Yeah.

**Trammell Hudson:** So as of, uh, as of April, I'm now a full time in Amsterdam and, uh, really enjoying it. Um, we, we tell folks it's the new New York.

**Trammell Hudson:** It's, uh, that's great. Cause New York is new Amsterdam. Is that the idea?

**Trammell Hudson:** Exactly.

**Trammell Hudson:** Yeah. So new, new, new Amsterdam. It folds back eventually.

**Trammell Hudson:** Yeah. And there's, there's a really wonderful, uh, uh, tech and art, uh, scene here. Um, uh, this Friday, there's a, uh, fun, uh, live coding, uh, music and visuals event that we're going to. Um, and, uh, you know, it's, it's, it's really a wonderful place to be.

**Trammell Hudson:** I mean, I'm just jealous when you post pictures about, you know, working on the train and biking and stuff like that. So more lifestyle jealousy for me than, but the other, the scene is good too. That's great.

**Trammell Hudson:** Yeah. Well, the, the train, uh, I'm trying to, uh, trying to reduce my, my carbon footprint a bit that I've flown, um, uh, far too many hundreds of thousands of miles in my life. So I'm, uh, trying to go, uh, just via the train, uh, had a really fun, had three conferences in three different countries, you know, two weeks and did that all via, uh, the train, night train and ferries. And, uh, that worked out really well.

**Trammell Hudson:** Yeah. That's awesome. Yeah. That's a flying thing is that's on my list too. Uh, where can people find you online? How do they, uh, get in contact with you?

**Trammell Hudson:** So, uh, you can see the projects like you mentioned on trmm.net. Uh, I'm somewhat active on Twitter, uh, QRS, uh, also on Mastodon QRS at Mastodon.social. Um, and, uh, yeah, the website has more ways to get in touch with me.

**Trammell Hudson:** Awesome. Awesome. Well, Trammell, thank you so much for talking about all your projects here. I'm looking forward to seeing it future conferences and seeing, seeing all the other things that you put on your website. It's really great to really good, great to see the things that you've done.

**Trammell Hudson:** Chris, it's been wonderful chatting with you and, uh, really had a lot of fun talking, uh, about all these projects. It's been a fun, I love documenting them and I'm glad, uh, I'm really glad that, that, uh, you enjoyed reading about them.

**Trammell Hudson:** All right. Well, thanks. And we'll talk to you soon.

**Trammell Hudson:** Okay. Take care.

**Trammell Hudson:** Once again, we'd like to thank our sponsor for this episode, Roden Schwartz, a leading manufacturer of value instruments designed to help you maximize your bench's performance for everyday applications. They just announced an industry first complete solutions with all the upgrades upfront for one price. Now through December 31st, 2019, save up to $10,000 on Roden Schwartz solution packages. They come with fully loaded test and measurement instruments right from the start. When you invest in Roden Schwartz products, you get the highest quality engineering, plus all the bandwidth, channels, inputs, memory interfaces, and signal generation you'll ever need. Learn more about Roden Schwartz value instruments and this limited time promotion at askanengineer.us. That's askanengineer.us.

**Speaker ?:** Roden Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf Pf
