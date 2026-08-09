---
episode: 362
title: Secret Squirrel
url: https://theamphour.com/362-secret-squirrel/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released October 1st, 2017. Episode 362. Secret Squirrel.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** How's the new job going?

**Chris Gammell:** It's going great, man. I've been... I mean, I don't know. I went to Maker Faire over the weekend. And I don't know if that's work.

**Dave Jones:** Which Maker Faire? Sorry, I just...

**Chris Gammell:** I went to the New York Maker Faire. That's true. I felt bad I missed Milwaukee.

**Dave Jones:** Isn't that huge? You don't sound, oh, I went to Maker Faire. Isn't it supposed to be ginormous?

**Chris Gammell:** It's big. Oh, it's nice. I mean, yeah, it's great. But what I was saying is, like, I don't know if that's work. That's what I'm really getting at. You know what I mean? Right. I probably would have been there anyways, but...

**Dave Jones:** Right.

**Chris Gammell:** Yeah. But I was talking to people for...

**Dave Jones:** So you officially went there for work?

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Oh, so do you guys have a stand or something or what?

**Chris Gammell:** No, no. Right. Okay. I don't like doing that. You've had to do that in the past, right?

**Dave Jones:** Right. But did they send you there to walk around in a T-shirt, holding a placard or something or... Yeah, sandwich board. Sandwich board, yeah, yeah.

**Chris Gammell:** That's a good idea. But no, I was just there to talk to people, you know. Right. Yeah.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah.

**Dave Jones:** Okay, cool.

**Chris Gammell:** Yeah, so it was good. I mean, it was good. And actually, I want to announce too, I will be at Open Hardware Summit, I found out. So I'll be out there as well. Oh, okay. Excellent.

**Dave Jones:** Is the company sponsoring that or...?

**Chris Gammell:** Yeah. Yeah, we're helping sponsor that. Oh, okay. So, it's good. It's, you know, everything's great. I mean... Excellent. I don't know. I'm still learning, learning a lot.

**Dave Jones:** Learning, learning, learning. Actually, I looked at you, tweeted like a kit or something that you can get. It's like, it's free or something? You'll send it for the cost of postage or...? Yeah, the sim. Something. Right. Okay. That actually looked interesting. I thought, oh, maybe you should like have one of those sitting around just so I can...

**Chris Gammell:** Oh, yeah. Well, you know... You know? I mean, we're buddies. I'll send you stuff.

**Dave Jones:** Sweet. Send it in the mailbag, you'll get free publicity. Right. Exactly. Yeah, exactly.

**Chris Gammell:** You know how the game works. Of course. Right. I know which email address to bug. Dave actually reads my email sometimes. Yeah, but no, it's all good. I mean, like, I don't know. Like, this is a... I think the interesting thing is, I think the thing that's interesting is that my title is like developer advocate or developer relations or something like that, which wasn't really ever... I mean, that's a software thing, really. Like, that's a software... Like, I know people that have done that for Software World. Yep. But that's... But then again, I think about it. Some people do that. Usually, it's like FAEs are kind of like that same role, so...

**Dave Jones:** They're basically hardware evangelists or whatnot.

**Chris Gammell:** Yeah, exactly. They're kind of showing that stuff up, so... I'm looking forward to it. I'm supposed to... I've got a couple of boards that I'll be making, stuff like that. You know, we use, like, U-Blocks modules. They're real simple in terms of, like... Right. The actual, like, construction of circuits. It's mostly just doing breakout stuff, but I'll be doing those soon. I'm looking forward to that stuff. Got it. So... Yeah.

**Dave Jones:** So you'll be, like... So it's actually quite... It's not too dissimilar to your old job. You're still gallobanting around the country going to be in the face at shows and whatnot, right?

**Chris Gammell:** Yeah. Yeah, yeah. Yep. I'm a face. A face, not the face.

**Dave Jones:** Oh, okay. Oh, there's other people in the company who do a similar thing?

**Chris Gammell:** Yeah. Yeah, exactly.

**Dave Jones:** Oh, okay. Right. Yep.

**Chris Gammell:** So, yeah. It's all going good. Groovy. Mm-hmm. Some people will kill for... Some people

**Dave Jones:** will kill for a gig like that, you know? Just, like, bumming around at hardware conferences and whatnot. Make affairs. I do some work. I do some work, Dave. Right. Okay.

**Chris Gammell:** A little bit. Just a little. But, yeah, it's going great. What have you been up to?

**Dave Jones:** Well, I have... Hang on. Have you been, like, booting up the hardware and actually playing with it? Yeah. Because I presume before you joined the company, you hadn't played with this stuff before.

**Chris Gammell:** I had done a little bit, but, yeah, this is booting up some of the hardware. I found out the question that you were asking about the sleep currents. You were asking about that. Oh, yeah. Right. It's actually half a milliamp, which is, like, seems high, but with cell modems, it's not great. So, there's, like, a micro and cell modem on board, so...

**Dave Jones:** Okay. So, can we give a ballpark for a AA battery-powered... Oh, I did that. Do that, like, transmit in every minute or something, you know? So, it's 5,000 hours. 5,000? 5,000?

**Chris Gammell:** So, it's 5,000 hours if it slept the whole time, but it would be...

**Dave Jones:** Oh, okay. On what? A set of AA's? What batteries are you talking about?

**Chris Gammell:** Yeah, right. So, a AA, I looked that up the other day. It's 2450 milliamp hours in a AA.

**Dave Jones:** Right. Okay. Right.

**Chris Gammell:** So, you do that math at, like, half a milliamp. I think it's, yeah, you double that pretty much to 5,000 hours.

**Dave Jones:** Well, you've got to work in power when you're talking about it because you probably have to boost it up. Right.

**Chris Gammell:** But this is also without transmitting, so that doesn't really count here. Okay. Right.

**Dave Jones:** No, no, no, it doesn't. I mean, the entire product has to be useful. It's got to transmit.

**Chris Gammell:** Yeah, right.

**Dave Jones:** But it depends on the application. Some applications are interrupt, driven by a sensor, and only transmit when, you know, somebody opens the door of your shed or something, you know?

**Chris Gammell:** Right. Right.

**Dave Jones:** Right?

**Chris Gammell:** Well, and I was asking around about that, too, and, like, doing, like, you know, like, so you've probably done this before, where it's like, okay, your micro doesn't get as low as you want it to. You could go and just cut off the power rail to the whole thing, right? Oh, you could. And so, like, have a supervisory circuit. If you were really hurting for it, right, you could set up a supervisory circuit. You could then cut off the power rail to the entire module.

**Dave Jones:** If you're incredibly desperate, but micros are so low power these days, it doesn't. You don't. It's almost made those supervisory type stuff redundant and power switching and stuff like that.

**Chris Gammell:** Sure. Right. That's pretty much pulled into the circuit. Yeah. Yeah. Yep. Yeah. It's not lost on me, though, that, like, you know, more and more of the stuff that, I mean, this is the trend we've been seeing for a long time, right, of, like, more stuff gets pulled into modules, stuff like that. It's just that, so, like, I was talking about the top. Like, the fact that I'm just going to be doing breakouts for modules, it's not like I'm designing circuits at that point. Right. It's basically, you know, Lego blocks. Yeah. Yeah. Exactly. So, it's interesting. But what really is, it's overall, right? So, not just looking at what I'm doing, but just in general, too. The thing that I keep hearing over and over and over again is, you know, from lots of people, it's like, I don't care about the circuit. You know, like, I love the circuits. You love the circuits. We all love the circuits, right? But most people, they don't care. They just want to get that thing done. You know? Exactly.

**Dave Jones:** They want to build their widget.

**Chris Gammell:** Right. Exactly. They want to know that the shed door's open, like you mentioned, right?

**Dave Jones:** Yep. They want their widget to tweet.

**Chris Gammell:** Right. And it's like, you know, we love the circuit stuff, and I still do, and, you know, like, all that. But it's interesting, and it's like seeing how that stuff works at a low level. But that takes a lot longer. And, like, you think about, like, so, like, the Jim Williams app notes. Like, I look at that stuff. He's got, what's the one with the thermocouples. You know what I'm talking about? He's got, like, this one gorgeous app note. They're all gorgeous. What are you talking about? I know. That's true. But the one that I always think of is the app note 28, right? So he's got, like, he's got, like, a push-pull going into a transformer, and it's all isolated, and then he actually has code at the end of it. I'm sure we've mentioned it here on the show before. But, like, you do all this stuff, and now, like, literally these days, I used to use a chip that was just all this stuff in one. You know, the thermocouple's linear. It's basically, plop this thing down, give it some power, read the registers, you're done. Right? And it's insane. So, and then, like, so, what do we do here? You know, like, but most people just care about getting a temperature. So, the art of this is lost. But... Quite possibly, yes. Well, I mean, like, the art of this, the circuitry is the art, right? That's what it looks like. But at the end of the day, most people don't give a crap. They just, they just want the temperature. Yep. So...

**Dave Jones:** And everything's a module. You know, everything's available as a module. Oh, yeah. These days. You can buy just, yep. It's just nuts. Yeah. Well, I mean, we were talking about board

**Chris Gammell:** modules last time, right? We were talking about those power, the LTE, 3780, or whatever that was. Yep. Yep. Yeah. So... Which I looked at, by the way,

**Dave Jones:** because we're working on the micro supply again. Oh, nice. So, we're going through all sorts of chips again. Oh, yeah? Any others pop out? That one? How's it stack up? Oh, yeah, they did. I won't say. We're having a look at several others. Well, that's the other thing, though.

**Chris Gammell:** Like, so, like, okay, so, like, now we're talking about this, right? So, you talk about, now you're, like, trying to be secretive about this stuff. I understand that. But at the same time, it's like, who gives a crap, right? It's more about, like, can you source it, you know? Oh, yeah, exactly. You know what I mean? It's like, it's all about, like, supply chain stuff and getting

**Dave Jones:** the... Well, in our case, it's like, will it actually do the job, right? Because there's no, right? You can't just go out and buy a chip that's a voltage and current adjustable power supply chip that does exactly what you want. It's super stable for all loads. Boom. Right? It doesn't actually exist. It should, but it doesn't, right? Yeah. That's why power supplies are all discrete design, you know? They're discrete op amps, transistors, you know? Because nobody does a really, you know, an off-the-shelf solution. Right. But there are some chips that we've found which may, which were designed for another purpose, which actually act very similar to what we want. So, we have to actually test. Like, in theory, they might work and do what we want, but we have to actually breadboard them up and try them. Right, right. I see what you mean. To see if we can press them into service for

**Chris Gammell:** what we want. Right. I've seen that in the past where it was, like, a... So, it was an output stage for a power supply, but then it was an AB, a class AB amplifier driver that was actually driving the transistors, right? And it's like, that's interesting, right? Because you're still, I mean, it's still pretty linear, right? But it's, you know, you're just, you're not driving AC signals anymore. You're just cranking those things on. You know, you're opening the taps and either from the positive rail or the negative rail and you're burning the rest on the heat sink. So... Yep. Yeah, it was, it... But that's the same kind of thing you're talking about, right?

**Dave Jones:** Got it. Yeah. So, that's going to be interesting to see if it pans out, you know? Because you look at these chips and sometimes the devil's in the detail and sometimes they've got simulation models and you try it out and you go, you know...

**Chris Gammell:** Yeah, right. Is it worth breadboarding? Is it worth making a breakout for it? That kind of thing.

**Dave Jones:** So, anyway, we've identified one or two chips, so...

**Chris Gammell:** I was going to say, how's the search going these days? Because I find that, you know, like the big searches like you're doing here, like these are like, these are like higher, overarching, you're like trying to find almost like an architecture and a chip and...

**Dave Jones:** It's hard. We, like, you couldn't do it. Like, we had to actually think, well, maybe what other kinds of chips might do similar stuff and we had to look at the other areas because you won't find it by Google searching. You've got to switch your brain on and know that, oh, these other types of chips do current limiting and they do voltage limiting and, well, they're in a totally different category. So, you won't find them if you go through the selection.

**Chris Gammell:** Are you doing motor drivers? Is that what you're doing? Are you using motor driver chips? You are, aren't you? No?

**Dave Jones:** No. Anyway, I'm not going to say. I'm going to keep it a mystery. Secret squirrel. Secret squirrel. Secret squirrel. People can, can that be the photo for today's

**Chris Gammell:** show? We can have a secret squirrel. Yeah, I think that's good. Secret squirrel.

**Dave Jones:** Yeah. So, yeah, it's like you go, like there are other categories of chips and some look not too bad. So, anyway.

**Chris Gammell:** And so, when you're searching though, are you searching, so like I've always been a big fan of like the application level side of things? So, you're looking almost like, so like you're like looking in automotive, but then you dive down, you look at then like.

**Dave Jones:** You've got to look, like the first thing you do in the data sheet is look at the top level thing. Does it have, say, current limiting, for example, right? And you go, oh, okay, it's

**Chris Gammell:** got current limiting. Are you reading the marketing pages, Dave? Oh, no.

**Dave Jones:** Well, yes, we do. But that's the way to filter because you literally have to look through almost every chip in the category. Yeah, that's true. Right? Sometimes. So, it's, you know, you've got to, like, you can't spend an hour reading each data sheet. You'd go insane. Right? So, you've just got to like, so we may have actually missed one or two by doing that.

**Chris Gammell:** This would be a good like wiki source. You know what I mean? Like, so we have like a wiki of like possible applications for each chip. You know what I mean? Like, that would be, that's something you should do. You can do it, man. Yeah, sure. I'll spend my valuable time doing that. You got an assistant. Have him do it. Right. Okay. Yep. Sorry. I didn't mean to call David an assistant. Don't let him hear him say that. Yeah. But I mean, like, that's, that would be something, like, I've always, I've always thought about this kind of stuff in the application space of like, you know, because especially like searching for it too, like searching for, so like, again, to go back to temperature, right? The thing about searching for temperature stuff, I mean, how many frigging ways are there to measure temperature? There's thermocouples, PT, not PTCs, RTDs, there's, there's all the infrared readers, the junctions.

**Dave Jones:** There's a regular P and silicon junction. Exactly. I mean, there's just so many different things. Yeah.

**Chris Gammell:** And the problem is that when you go and search on a lot of the sites that are out there, right? You search on a distributor site or something, you basically search for the part, right? And then the, so if you search for like, like thermocouple amplifier, then you're going to miss all of the, you know, the, the high level module chips that happen to include a thermo, you know, like a, you know, a higher level encapsulated thing, you know, this is always the problem that, that we run into, I think. So you should do that. You should do that. It's a big, it's a moneymaker. It's a moneymaker right there.

**Dave Jones:** You think it's very, right? I'll be rich and famous. Yeah. Right. Fortune and glory, kid. Yeah, right. Fortune and glory. Anyway, speaking of modules and everything else, we can segue into, well, there's more about what we were talking before we got sidetracked onto thermocouples.

**Chris Gammell:** Uh-huh.

**Dave Jones:** Segue into what I was doing this morning.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** And it's a bit retro.

**Chris Gammell:** Okay.

**Dave Jones:** I know you're not really a retro fan. Ah, sometimes. That's okay. You know. Anyway, this might ring a bell or it might what. What, what? I'm going to ask you a question. I'm throwing him, I haven't told him what I was doing this morning.

**Chris Gammell:** This is like a, this is like a game show now. All right.

**Dave Jones:** It is. It is. Should I ask it in the form of a question or?

**Chris Gammell:** No, just, let's go for it. What do we got?

**Dave Jones:** All right. All right. What, can you name a embedded PC standard before all this modern Arduino and Raspberry Pi rubbish came along?

**Chris Gammell:** PC-104.

**Dave Jones:** Oh, he nailed it. He nailed it. He's not a young whippersnapper.

**Chris Gammell:** No, we've also talked about that on the show before, I think. Right. Usually, I think you sometimes bring that up when you talk about Arduino, but my real thing is I remember there was, there was a trade rag that was just dedicated to that. Yeah. And I remember looking at it being like, what the hell is this? So anyways, why don't you explain what the hell this is? Because that's probably useful. Yeah.

**Dave Jones:** PC-104 is kind of, there is a consortium that set the standard, but I don't believe it was ever ratified by, you know, IEEE or whoever do standards. Right. But it's basically when, you know, in the eighties when, you know, everyone was using PCs, right? PCs took over the world and everything. And everyone wanted like industrial embedded solutions, you know, industrial embedded. And sure, you could go out and buy your own processor and you could buy your own memory and you could roll your own solution. But people thought, hey, why don't we come up with a PC in a very compact form factor that is designed for industrial embedded applications. So that's exactly what PC-104 is. It is a, I think it's 98 by 98 millimeter board. It's a standardized form.

**Chris Gammell:** By the way, if you don't know. What? The first 103 didn't work. The first 103. That's so lame. That was such a lame joke.

**Dave Jones:** It is. Do you know why it's called PC-104?

**Chris Gammell:** No, I don't.

**Dave Jones:** Because it has 104 pins. Oh, that makes so much more sense. Anyway, so it basically, yeah. So it's a standardized size. It's 90 by 96 millimeters. So the PC-104 standard in quote marks defines the outline of the board. It defines the mounting holes and it defines the board to board interconnect header pins. So they're 0.1 inch header pins and they're in the, and they're functionally equivalent to the old PC ISA bus. Right? You remember the old, so they're all available in an 8 or 16 bit version. And well, most of them used a 16 bit. And these pin headers, and you could stack the boards just like the Arduino boards and other ones can stack, you know, if you, so they've got the pin headers coming, the headers coming out the bottom of the board extending out. And then, so the male pins coming out the bottom and the female one on top and you can stack as many as you want.

**Chris Gammell:** Right. Just don't, don't, don't double dip on a pin, right? You'll, yeah.

**Dave Jones:** Right. Well, it's just, well, it's a standard ISA bus. So within the limits of sharing stuff on the ISA bus, I won't go into details, but that's basically what it is. So it's an Intel, usually an Intel processor. Back in the day, they were, you know, 8088s.

**Chris Gammell:** I'm looking at a PowerPC one on Wikipedia right now.

**Dave Jones:** Yeah, you can get, you can get different ones. And they still sell them these days, right? It started in the eighties. PC 104 standard was early nineties. I've, I was playing with a board this morning, which is an 80386SX board.

**Chris Gammell:** 80386, so it's a 386. It's a 386. Sorry, I was like, you said like 803. I'm like, what's an 803? Yeah.

**Dave Jones:** Right. Sorry. Sorry. 80386 or just a 386SX. The SX being the limited 16 bit bus version of the 32 bit

**Chris Gammell:** processor. See, I never did anything with 286, 386, 8486, anything except for use it as a computer.

**Dave Jones:** So, right. Okay.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** Yep. Yep. So yeah, back in the day, I was developing with PC 104. Oh, wow. Okay. And the good, and the good thing about it was it was a PC, right? So you're already familiar with the development environment. You could develop it on your desktop and it, it just ran.

**Chris Gammell:** It's just a lower, lower memory, lower, whatever, right?

**Dave Jones:** Yeah. You just had a limited amount of memory and, uh, you know.

**Chris Gammell:** Did you heat sync them usually or no?

**Dave Jones:** No, no, no. Cause these were like, I powered it up this morning and it only drew, uh, two watts or thereabouts when it was just idling. Um, you know, and, and when I plugged in the video card, it used an extra half a watt or something, you know, so they're pretty low powered. So it's on par with like a fully flat out Raspberry Pi at, you know, two, two and at, no, at more than several watts. Cause the Raspberry Pi can pull two amps or something at five volts. So that's 10 volts. Yeah. So, you know, yeah. No, so these things didn't need it. Well, the, the later ones might have need heat sinks, but you know, back when I was playing with them, they're all, you know, low power 386 SXs and stuff like that.

**Chris Gammell:** What were you, what were you using them for? So you were doing like, like, uh, like test fixtures and stuff or more?

**Dave Jones:** Mobile test jigs and things like that. Okay. So, you know, and it just made development easy.

**Chris Gammell:** Yeah.

**Dave Jones:** And, and of course you can get, uh, digital plugin boards for them. So you get digital IO, you could get relay IO, you could get, you know, eight port RS two 32s if you need a bunch of serial ports and all sorts of stuff.

**Chris Gammell:** This is going to sound stupid, but were you doing, were you running DOS programs or you were running, you weren't running full windows on there? No, no, no, DOS. Yeah. Okay. So you were, you were developing for DOS and then, and then you would just run it.

**Dave Jones:** Developing for DOS and just run a command line program, which yeah. Yep. So yeah. How quaint. How quaint, yes. But it, you know, but it was great because it was the same as the PC you used. So the development environment was.

**Chris Gammell:** I think it's going to be really interesting. Like, so like, as you know, as, as Sagan and Hux grow up, like if they're nerds, which, you know, we can only hope. Yeah. Right. We can, like they have a choice, uh, but like they're like Linux is going to be normal for them. Right. I mean, like, right.

**Dave Jones:** Yeah. Yeah. That's what's crazy. Like, but there was no Linux back then.

**Chris Gammell:** I mean, there were, well, there was like, there's Unix for sure, but maybe not Linux

**Dave Jones:** by the, I don't know the history of Linux, but not Linux as people know it today. Damn straight. Yeah. Right.

**Chris Gammell:** It wasn't, it wasn't included on a $35 computer that you got, you know, that like, it's fully functional. Uh, yeah. Right. I mean, like, isn't that, that's just, that's crazy to me.

**Chris Gammell:** So.

**Dave Jones:** Yep. Wow. That's yeah. Yeah. Back then you ran DOS or you ran, uh, what was it? The, uh, the Novell DOS, the Novell DOS version, which was a better version of, I can't yeah. Anyway. Um, and then there were other versions of other flavors of DOS, which were better designed for embedded ones. God, I can't remember the name now. It's been too long ago. Okay. Anyway, the fact is the, this PC one, I thought you can still buy, you know, sure. Yeah. Yeah. Yeah. Yeah. Right.

**Chris Gammell:** My buddy's in DOS, uh, defense stuff and they, they use it like a ton.

**Dave Jones:** So yeah. Yeah. Yeah. They use it a ton because it's a, it's a standard. It's been around for more than 25 years and you can still get the same board with the same 0.1 inch pin header ISA bus, except they use an Intel atom processor now. Right. Okay. You know, you can, right. Oh, you can still get the older ones. Sure.

**Chris Gammell:** Sure. But you get more power or you get more, uh, processing at lower power. Right.

**Dave Jones:** So yeah, yeah, yeah, exactly. So, you know, it's not a bad processor.

**Chris Gammell:** It's just that, uh, well, it was bad in a desktop. It's in a laptop as well. Like a little EEPCs. Remember those things? Right.

**Dave Jones:** Oh yes. Yes. I've had one. Yeah. I've got one of those.

**Chris Gammell:** What a piece of crap. Yeah. But it was game changing for the time. Yeah.

**Dave Jones:** Back, you know, for, for about a year there, that was a game changing product, the EEPC.

**Chris Gammell:** Right.

**Dave Jones:** Right. So yeah.

**Chris Gammell:** Yeah. So, uh, why is this a teardown? You just had one or are you actually developing one?

**Dave Jones:** No, I just had one. I found, I was looking for another development kit. So I opened my tub of development boards and I went, Hey, here's these old PC 104 boards. Nice. And I thought, will they still work? So yeah, that thing's going to work till the, till the, uh, you know, spoiler alert. I managed to, but, um, but the video, like I found the doc, the original documentation online for the board, right. For the main processor board. This one didn't have video built on. So I had a separate video card. So I plugged it on, but I couldn't find any documentation for the video card. So, so I had to probe it to get the pin outs of the, you know, and, and didn't, and didn't had just have a VGA connector on the side. Oh no, it had some.

**Chris Gammell:** Like, like solder your own wires.

**Dave Jones:** I had to, I had to chop a VGA lead and solder it on.

**Chris Gammell:** Got it. And everything. But you got it.

**Dave Jones:** I got, and it booted. Yeah.

**Chris Gammell:** Nice.

**Dave Jones:** You know, well, no, it gets to, you know, no operating system found. Press any key when ready. Oh, so it powers up. But yeah, yeah. It powers up.

**Chris Gammell:** So just go write some, go write some code. You'll be fine. Right? I mean.

**Dave Jones:** Well, no, well, you can't just write code. You've got to install an operating system to boot from. Now it comes with, and this will bring back memories for a lot of people. One of the, the disc on chip from M systems. Do you remember that?

**Chris Gammell:** No, no.

**Dave Jones:** Oh, where? Yes. We got him. Folks. That's not hard.

**Chris Gammell:** The PC 104 is just a lucky thing. And probably you mentioned it on here. That's why.

**Dave Jones:** Anyway, M, the M systems was with the company and the disc on chip was, it was a 28 pin dip chip and it was a complete flash based disc. It was like a solid state disc in a 28 pin dip package. And it changed the whole industry. It was like, holy shit, we don't need a hard drive to hook up to our embedded system.

**Chris Gammell:** Wait, but what was it? Is that SRAM? What was it? Or like.

**Dave Jones:** It was actually flash. It was very early flash.

**Chris Gammell:** Oh, really? Wait, really?

**Dave Jones:** Very early flash technology. Yes. Wow.

**Chris Gammell:** How much, how much memory?

**Dave Jones:** Oh, not much. Like eight meg or something. No. No, no, no. It wasn't gig. No, no. It was eight meg. Yeah. It sounds like a lot too. Eight to 32 meg.

**Chris Gammell:** It wasn't like battery backed SRAM or something like that?

**Dave Jones:** No, no, no, no. Okay. So this is. It was actually flash disc.

**Chris Gammell:** Was it, was it, was it, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh, uh,

**Dave Jones:** Oh, yeah. It, I, it's not, I don't think it's the modern version of.

**Chris Gammell:** Yeah. Yeah. It's not multi-layered and flash all that crap. That's. Yeah. It's. No, no.

**Dave Jones:** I think it's like, it was very early flash, uh, technology. So I'll send you the, uh, link. Here it is. USB, uh, blah, blah, blah. Um, anyway. Um. Disc on key.

**Chris Gammell:** What's disc on key? That's another one.

**Dave Jones:** Oh, disc on key. I don't know about that one. I was like disc on chip was the only one I really used. Yeah. Anyway. Yes. They were, they were from 16 meg upwards. So yeah, but there was plenty to run DOS and an app. I mean, DOS, DOS booted in, you know, a hundred K or something.

**Chris Gammell:** Oh really? Okay.

**Dave Jones:** Oh yeah. Yeah. Yeah. DOS was quite small. If you, especially some of the other flavors.

**Chris Gammell:** I bet this was not cheap.

**Dave Jones:** Oh no, no, no. These disc on chip things were expensive. They were like a premium product. Anyway, that, that died in 2007 when other things started. Oh, they became Sandisk. They, they, they got bought by Sandisk. Ah, they got bought by Sandisk. Yeah. Okay. Exactly. Yeah. So anyway, yeah, that was all the rage. So, so, but now like you, you, you take for granted these days that you can just plug in a USB key, right? These things don't have USB. I mean, who even does that anymore? Right. Well, USB wasn't even invented back then. Right. So this thing has like a floppy connector and in, in the box came a three and a half inch floppy drivers and stuff. Yeah. So I've got a, and an old style PS2 keyboard with the five pin ding connector. So I've got a bodger. I've not only got to find a PS2 keyboard. I've got a bodger, bodgered in from the PS2 to the five pin din. So I've got to make up an adapter cable. I'm not sure if I have one anymore.

**Chris Gammell:** What's din?

**Dave Jones:** Din's like dual in line, but a din connector, you know, the circular, circular din connector back in the day that used to connect to all the tape drives, the audio din connector.

**Chris Gammell:** Audio din. Is that the one that looks like a MIDI? Is it a MIDI thing?

**Dave Jones:** Yeah. Yeah. Okay. Yeah.

**Chris Gammell:** Five pin din. Yeah. That's what I think about is. Yeah. Yeah. That's a MIDI connector. Okay. That's what I think of. MIDI might be a little different, but that's what I think. Yes. Right. Okay.

**Dave Jones:** Similar. Yeah. Circular ding connector.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Anyway. Yeah. So, yeah. So I've got to convert it to that just to get a keyboard running. And then I've got to read the documentation to figure out how to get DOS installed on the disc on chip. And then I might have to bodge in a three and a half inch floppy drive or something just to get this, you know, but anyway, it's fun. Yeah.

**Chris Gammell:** Yeah. Yeah. I mean, I guess when you tell me you're busy, I didn't think you were saying this stuff, but I mean, this is good content. I'm sure you're making a video about this, right? We're going to see this on video at some point. Yeah.

**Dave Jones:** I've already shot some video this morning. I haven't actually got the disc on chip working yet, but you know, I'm assuming, well, I assume that'll still work after 25 years, the disc on chip. Yeah. Chip. So, you know, but anyway.

**Chris Gammell:** Yeah. Well, here's a comparison point, some contrast to that. So BeagleBoard just released- Yeah, they released something new, didn't they? Some tiny thing? Right. And so the Pocket Beagle, right? That's right. Pocket Beagle. This actually, the Pocket Beagle already existed. So that was actually a project that was online. It was basically to fit in a smaller Altoids tin, which- Right. I still don't understand the Altoids thing personally, but-

**Dave Jones:** I don't understand the Altoids thing.

**Chris Gammell:** Because like, it's a metal thing, guys, you know? I know, it's just stupid. I don't get it. But the thing that's exciting about it, the reason that they, excuse me, the reason that they did it is that they shrunk down that Octavo system. Now- What's the Octavo system? I don't think we've talked about Octavo in the past, but that was basically, they had made a SOM, I think is the correct term. System on module? Yeah. I think it's a SOM. Maybe it's a SIM. Not a SIM. But anyways, it's basically they have- Oh, sorry. It's SIP. System in package, right?

**Dave Jones:** Oh, system in package. Right. Okay.

**Chris Gammell:** So, and that was already on. So that was like, if you look at like as the Beagle board was going through, I think that was on like the- it wasn't on the black, but it was on the Beagle board blue, I think, which is like the motor driver one.

**Dave Jones:** And the memory was integrated on top of the processor.

**Chris Gammell:** And the PMIC and the power management IC and a bunch of the passives and stuff like that.

**Dave Jones:** So now they're putting all, like they're putting like, is there power supplies in this module? Yeah. Yeah. It looks like there's power supplies in there, LDOs and everything, but it looks like a chip.

**Chris Gammell:** Right. The way for people to think about it is like, imagine you're just making a really tiny PCB and then you're just covering it in black goop, right? That's like the way to think about this SIP.

**Dave Jones:** That's basically what you're doing. That's basically what they're doing.

**Chris Gammell:** But the interesting- so the thing that I'm- and it's obviously much more complicated than that because you're actually making BGA bottoms and stuff like that. Obviously, this whole thing is a BGA. The thing that I was excited about is this Pocket Beagle is a- so it has this new SIP on it, the OSD335X-SM, right? So that's the new one. Yeah. But the thing that's exciting about that, there is an entire- this is literally Linux on a chip. So like that- Right. That is frigging crazy to me. And then I talked to Greg, one of the guys at Octavo. He said that with this board, or with this chip rather, it's got- so it's 256 BGA. It's got the three rows of BGA. I think it's- Yep. 0.8 millimeter pitch. I didn't actually see what the pitch was. Yeah, 0.8 millimeter. No, that's not right. 127 millimeter? That doesn't sound right. What is the pitch? But I don't know what the pitch is, but it's- The pitch is- It's workable.

**Dave Jones:** It is a 1.27 millimeter pitch. That's huge.

**Chris Gammell:** Oh, yeah. Okay. So, yeah. So wide pitch. Yeah. Oh, it is that. Right. Okay. So it's bigger. So most of the BGA's these days is 0.8, right? So that's like- Right. And smaller. Obviously, the 0.4 is really tough. So what Greg was saying, though, is you can escape all 256 pins with a 6 mil space and trace. You can escape all pins on the top layer, which is like- On the top layer. That's crazy. That's great. That's great. That's a big deal. So now you have a Linux chip that runs on a four-layer board.

**Dave Jones:** Boom. People don't realize what a big deal escaping BGA's is.

**Chris Gammell:** Right.

**Dave Jones:** Right?

**Chris Gammell:** Right. Exactly. You do, obviously, right? Yeah. Yeah.

**Dave Jones:** No, of course. That's why I'm saying. Right. Yeah. Right? Because it's an important thing because it forces you. If you choose a chip with a specific pin count and a specific pitch, that forces you into using a specific number-layered board. Right. Right.

**Chris Gammell:** You're going to have an eight-layer board or you're going to need to do like a 3-3 space trace. Right? And it's like, and that starts to get, that gets really expensive. And obviously, there's a lot of other design issues. You know, like, it's just, it's crazy.

**Dave Jones:** So this could go on a single-sided board. Sorry. I stand a double-sided board.

**Chris Gammell:** Well, it could, but you really should do a four-layer. Right? Why? So you can get a plane. So you can get a... Eh.

**Dave Jones:** Eh.

**Chris Gammell:** Oh, okay. Well, challenge accepted, I suppose.

**Dave Jones:** No, because it's got the integrated LDOs with the bypass caps inside the module. I'm looking at the photo now.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Right? So that should be okay. I think you can get away with this on a double-sided board.

**Chris Gammell:** Well, that's even more interesting. When I talked to him, he said it was four, but yeah, maybe. Maybe two would work. Eh. Yeah. Or maybe one. I mean, I don't... But either way, even at four, that's crazy, right? And so this is that same thing we were talking about at the beginning. It's like, just it's all getting pulled in. And so the other thing that I'm sure that you have thoughts about is the fact that you don't have to do any of the DDR routing, right? It's got DDR3 in there. You don't have to do any of the routing. No, no. That's crazy. So even Raspberry Pi has external memory. Wait, no. They do flip chip, don't they?

**Dave Jones:** But it doesn't matter. You can't get the Broadcom chip either way. No, they use external memory. The Raspberry Pi uses external.

**Chris Gammell:** Yeah. But it doesn't matter. You can't get those chips anyways. Right? So this is a purchasable chip. And that's pretty awesome.

**Dave Jones:** So what are all the pins? Are they just IOs?

**Chris Gammell:** I think so. Right. I don't know.

**Dave Jones:** Because it's a system on a chip, right? You said it. It runs Linux. So the pins must be like USB inputs, IOs, maybe Ethernet. Does it have like Ethernet Mac and stuff built in? Yeah. All that sort of jazz?

**Chris Gammell:** Yeah. It's got all that stuff.

**Dave Jones:** Oh, data sheet. Here we go.

**Chris Gammell:** Yeah. I mean, so onboard, it's got eight channel ADC at 12-bit. It's got DMA, two spy port. I mean, it's got everything the BeagleBone's got, right? Right. But the two cans, three I2C, two spies, six UARTs, 114 GPIO. I'm sure some of those are taken. That's nice. Yeah. Yeah. And I'm sure that some of these duplicate, right? So don't. Yeah. People should, you know, whatever. But then the USB 2 on the go. Right. What else? So like, you know. 2C, yeah. Yeah.

**Dave Jones:** But the Ethernet 10, 100, 1000.

**Speaker ?:** Yeah.

**Dave Jones:** Two port and switch. Oh, two port.

**Chris Gammell:** So here's the thing. Here's the thing. I have been seeing people, friends, family, you know, everyone, right? Your mom's using this. No, no. They're using, they're designing products with like, with BeagleBones and with Raspberry Pi's in them. And Raspberry Pi has a thing like this too, right? Raspberry Pi has a compute module and that's like, you can buy it as a DIM, like a SoDIM module. And that's a good step towards it, but you still couldn't buy the chip. And as far as I can tell, you'll never be able to buy a chip. Now you can go and do something like the chip, right? So that's the Next Thing Co. They have their boards and then they have that R, oh, the GR8, the great, which is like, it's a, I forget what the processor is. It's one of the cheap one, the MediaTek maybe. So it's the MediaTek processor and then it's a module breakout. And so again, you can buy the processor on a breakout and you can integrate that. And so that's probably close to this as well. You know, it's basically a similar kind of thing where it's not integrated in a package. So it's a little bit bigger, but still you could buy it and get it in your product, whatever. But like this, you need to be able to, so the thing I keep thinking.

**Dave Jones:** Can you buy it on DigiKey?

**Chris Gammell:** Yeah.

**Dave Jones:** Or Mouser?

**Chris Gammell:** Right, you can.

**Dave Jones:** Yes, you can.

**Chris Gammell:** Yeah. Or if you can't yet, you'll be able to. Which one are you talking about? The great?

**Dave Jones:** The Octavos system. Yeah, these things. The thing we've been talking about.

**Chris Gammell:** Yeah, you can buy these.

**Dave Jones:** Really? Yeah, I think so. I'm going to verify. Trust but verify.

**Chris Gammell:** That's fine. Yeah, on Mouser. There it is.

**Dave Jones:** I've got a dev board.

**Chris Gammell:** Where it's listed. Order now. Order now. I see a link. 293 can ship immediately. And you'll pay through the nose for them.

**Dave Jones:** I was just about to order some stuff from DigiKey. Maybe I should order some of these chips and do a little project with it.

**Chris Gammell:** Yeah, well, that's what I'm thinking, right? I mean, that's what's crazy about it. So, like, and I was talking to Jason. So, we've had Jason on the show in the past, and I'll link to that. And I asked him to come back on at some point, Jason Kreidner. But since we had him on way long ago, three years ago, they switched to doing, it's all Debian now. It's not running. So, it's just stock Debian, which Raspberry Pi also does. And so, like, okay. So, I'm obviously at a higher abstraction layer than I used to be, right? Obviously, I'm meeting a lot of people that are doing, you know, some heavy-duty processing. Maybe they even want to write with, you know, interpreted languages and stuff like that. And that's just the new reality we live in. Assuming you're working off of, you know, a big battery or you're plugged into the wall, then running Linux is fine, right? It's not great, but maybe, you know, maybe you want a display or maybe you want some of the other, you want, you know, security stuff in Linux. So, the next step is, like, being able to make something you can actually make. And if you can actually buy this stuff, that's a good step. So, that's all I'm saying.

**Dave Jones:** It's pretty sweet. It's got over 100 components integrated into the OnePack. I know. It's so crazy.

**Chris Gammell:** The other thing I learned, I kind of knew this actually already, is that, what's his name? Um, the guy who invented, so one of the founders of Octavo is the guy who did the speak and spell. Oh, really? Yeah, Gene Kranz. That's it. Yeah.

**Dave Jones:** Gene Kranz? Gene Kranz is the Apollo guy. Is it just the same name?

**Chris Gammell:** Wait, maybe it's a different name. It's a Gene someone.

**Dave Jones:** Right.

**Chris Gammell:** Wait, what Apollo guy?

**Dave Jones:** Gene Kranz. Come on. Famous. Sorry. Sorry. Maybe it's a different Gene. Sorry. He's the mission controller.

**Chris Gammell:** Everybody, everybody, you know, above 70 is named Gene, so. Right. Okay. Or Morty. Or Wally. Yeah. So, yeah. But anyways, one of the TI guys, these are all TI guys. These are all former TI people, so. Right. Yeah. So, that's exciting. Cool. So, in the news, I finally met Massimo from Arduino. Oh, right. Yes. Arduino. Arduino. Arduino. Arduino. Arduino. He's very nice.

**Dave Jones:** I thought you met him before. I probably shook his hand before. You interviewed him?

**Chris Gammell:** No. Right. Okay. No, I interviewed Eben, who's Raspberry Pi.

**Dave Jones:** Oh. Yeah. Okay. Right. Yeah.

**Chris Gammell:** I don't know. Yeah. But anyways, he's very nice. But they just released a bunch of new boards as well. After the shake-up.

**Dave Jones:** After the big buy-out. Yeah. Right. After the shake-up. Yep.

**Chris Gammell:** Yep. And it's interesting, too, because, like, so it's like these smaller modules. Now, it kind of looks like the Adafruit Feather format. It kind of looks similar to that.

**Dave Jones:** Right. I'll tell you what they should do. They should jump on this and release the Arduino form factor version of this chip. Oh, that's interesting. Like, Tevo systems and get support in the Arduino environment for it, maybe. Yeah, I guess. I don't know. I don't know. Boy, that's... It's probably overkill, but...

**Chris Gammell:** I was going to say, that's like using a howitzer to cut your lawn, man. It's like... Right. Yeah. I don't know.

**Dave Jones:** But, I mean... How much are those chips, by the way? 40 bucks. How much are they? They're not cheap.

**Chris Gammell:** 40 bucks. It's 40 bucks for one of them. Yeah. So, it's like, yeah. So, yeah. It's more expensive than a Raspberry Pi computer. Right. But, I think, you know, it's probably 20, 25 if you get it in volume kind of thing. But, you can get them in volume. That's the other thing. You know what I mean? Right. Yeah, yeah, yeah. These are the... This is just the message. And it's not for you, believe me. But, like... Right. Man, I just... I watch people do this and it's like, you know, you just see... You see two years into the future when they're like, oh, we can't buy any of the stuff we designed into our product. This is a product, man. Like, think about it. Oh, yeah. Yeah. Yeah. So, yeah. Exciting. Exciting. Gene... What did I say? I said Gene Krantz. It's actually Gene... You said Gene Krantz. Gene France. Huh. Right. Yeah. Speak and spell. Gene France and Gene Krantz. Got it. Sounds like the beginning of a joke. You know what else sounds like the beginning of a joke? Oh, God. What? I posted this and someone downloaded it on our subreddit. Two fish are in a tank. You ever heard that one before?

**Dave Jones:** No, I haven't.

**Chris Gammell:** But... Two fish are in a tank. One turns to the other and says, how the hell do you drive this thing? Right? You don't know that joke?

**Dave Jones:** No. No. No.

**Chris Gammell:** Yeah. It's wordplay, you know? No. But then there was a project where...

**Speaker ?:** Stupid.

**Chris Gammell:** No. Where a bunch of students built a fish actually driving a little robot with an aquarium on top of it. I thought it was clever. I'm full of dad jokes today.

**Dave Jones:** It'd be clever if it was monitoring where the fish was going visually and then the fish was actually controlling the thing. And that would have been...

**Chris Gammell:** Actually, it is. Oh, really? Yeah. Yeah.

**Dave Jones:** So the fish does actually control the robot? Yep. Right.

**Chris Gammell:** It's not doing it with vision, it's doing it with light detection. But yeah. Oh, right. Yeah. It uses the... It normalizes it and then... Right. Right. Yeah. Nerdy. It's good. It's good stuff. Oh, God.

**Dave Jones:** Okay. Very good. All right. Do we have anything on our list this week?

**Chris Gammell:** Well, that was on the list. Ah, right. Yeah. What was good here? You can tell we didn't prep this at all. No, we didn't really prep much. Much? I don't know. I had posted... So this is actually a fun project I saw in town. So Bart, who used to be at Instructables, he retired from there. And maybe I mentioned him on here before? That's right. But anyways, he just spends his time making robots now. And they're awesome. His buildlog.net, if people have never been on there. But he showed up at one of the meetups I do here. So there's a link to the post about this thing. It's called Pen Slash Laser Bot Controller. And so he shows up to this meetup that I do. It's at a bar. And we're all hanging out. And he's got this orange box. And it's 3D printed. And I'm like, Bart, what is that thing? He's like, check this out. He puts a coaster. He has a set of coasters with him. He puts a coaster into it. And it's got a roller. And so it kind of sucks the coaster in. And then it cuts out a design. It's a laser cutter. And then it pushes the coaster out the back. And he built this thing in a couple days. And it's just calm. That's cool. Man. So that's part of the story. The other part is that it broke while we were there. And so he's troubleshooting it while it's getting dark outside. And then he's got the hood open. But there's no interlock. And so I'm looking at what he's doing. And then the laser kicks on. I'm like, oh, my God, my eyes. But it's like a 2-watt laser. So no harm done, I suppose.

**Dave Jones:** No harm done from a 2-watt laser. OK. Was it 2-watt? Maybe it was less than 2-watt. I don't know. 2 watts is going to severely damage you.

**Chris Gammell:** I guess so. I mean, it was pointed down as well. It wasn't pointed out at me or anything. Yeah. That's a good one.

**Dave Jones:** Got it.

**Chris Gammell:** I don't know.

**Dave Jones:** What's this article about what working at Pebble taught me about building hardware? Oh, yeah. Have you read that? What's the takeaway? Is there a takeaway? Is there a TL deal?

**Chris Gammell:** Yeah. But it's the same old one. What? Hardware's hard? Hardware's hard. Yeah. All right. All right. Yeah. I mean, he talks about prototype early, of course. Duh. Yeah. And I should reference to... Oh, shit. What's his name? Oh, he was a case guy, too. I've already forgotten. We had a Pebble guy on the show.

**Speaker ?:** Damn it.

**Dave Jones:** Yeah.

**Chris Gammell:** Pebble, the amp hour. I feel bad now. I feel really bad. Andrew, I'm sorry. Andrew Whitty.

**Dave Jones:** We've done three on his shows. I know.

**Chris Gammell:** Yeah. But he's from my alma mater. I should have remembered. Anyways, Andrew Whitty, we had him on the show, and he was the CTO, and obviously Pebble is no more. They're all part of... What's it called?

**Dave Jones:** Yeah, they got sucked up for a song, didn't they?

**Chris Gammell:** I think so. Yeah. They're part of... What's the... Oh, Fitbit. Yeah, they're at Fitbit. Ah, Fitbit, right. Yeah, so some of them are still there. I think a lot of people got laid off, but... Yeah. Yeah. I mean, I don't know. Like, Pebble did a lot of things well. Like, they were one of the very early... They did Kickstarters very well. They did three Kickstarters. Yeah, yeah, yeah. Right? But he's talking about, you know, get to China if you're going to be building in China, obviously. Right? I mean, like... Yeah. I don't like this kind of stuff because it makes it feel like China's the only answer, but... All right. ...they're in the consumer space, so China's probably the only answer. Right?

**Dave Jones:** Well, my new meat has been made in South Korea. Thank you very much.

**Chris Gammell:** Yeah, but that's not the consumer space. That's what I'm saying, right? I mean, like... Right, okay. Right, and if you're in the industrial space, you could... I mean, like... Or if you're in the educational space, right? So, Adafruit's in, like, New York City, right? I mean, like... Right. And it's, like... It's all about, like, the margins about where you're going to manufacture. You know, it's more dependent on margin, I think, and what your expected stuff is. China's going to get you the margins that you need for consumer, but... Sure. Right? But you're probably not going to have enough volume to go there if you are industrial, so you should probably stick around locally. Got it. That's why I love industrial. It's just better. Yep.

**Dave Jones:** Yeah, it's a world of hurt, consumer. Like, you know... It really is. Like, it's great if you pull it off, but otherwise, it's going to be, like... It's going to be a world of hurt.

**Chris Gammell:** Yeah. I... Well, neither of us have done it, so I don't know. We've...

**Dave Jones:** No, I mean, we've had Jerry on the show before, you know, talking about the... Sure, yeah. ...insane pressures of, you know, working on consumer toys, which is probably one of the worst.

**Chris Gammell:** Right, exactly. Talk about thin margins. Yeah. And we're supposed to actually talk to Jerry again, too. We had... I had messaged her about stuff, so we might have her back on soon. Um... Sweet. Uh... Get an update. But, yeah, I mean, most of the stuff that we cover is kind of... I mean, it's all over the place, right? We have, what, security people. We have, you know... Mm-hmm. I guess the interesting crossover one... I guess Juergen, when he was on here, he was the one who was doing... I think you weren't there for that, but he was the one doing hearing aid chips. Right, that's kind of... Okay. That's consumer in that it's widespread, it's kind of high volume, comparatively.

**Dave Jones:** Yeah, but they're high-priced. Right, yeah. Like, it's not like they're selling... It's not like you can buy a... Well, maybe you can buy a $10 hearing aid on eBay. I don't know. Yeah. But they're probably going to be crap.

**Chris Gammell:** Right, right. So... Yeah, so, I mean, I guess other people, like, so we've had Bunny on, we've had, uh... Zach from MakerBot. Uh... I guess we had Scott Miller on, right? So we had Scott Miller on. He did the, uh, Ruma stuff at iRobot. So, I mean, like, yeah, it's kind of all over the place, though. And it's even a bigger deal when it's like, like, how much is a watch going to cost, right? It's like, yeah, if you're Apple, you get to sell a $400 watch. But Pebble wasn't. Pebble was selling a $99 watch.

**Dave Jones:** Mm-hmm.

**Chris Gammell:** So... That's a good question, though. Right, Pebble was, like, always selling on the premise of, like, oh, well, we'll have this ecosystem where we make money on the back end of software.

**Dave Jones:** Right. Selling the app.

**Chris Gammell:** Has that worked for anyone? You know what I mean? Like, that's like, that's like the story of hardware startups. It's like, oh, well, we'll make it up in data, you know, at the end.

**Dave Jones:** Well, it worked, it famously worked for Apple, right?

**Chris Gammell:** Right, but they're Apple. They make a lot of money on hardware, too. I know, exactly.

**Dave Jones:** Yes, yes, they do. But only because they got to the point where they got so much cash from all the software and everything else that their hardware became better margins.

**Chris Gammell:** Right, they had the lock-in at that point, then they could...

**Dave Jones:** Yep.

**Chris Gammell:** Yeah, I don't know. I'm still looking through our guest list here. By the way, we have a... We do have a guest list. Yeah, you can get to the guest episodes if you go to, on theampire.com, if you go to For You and For Us, obviously those are the two choices, For You, and then go to guest episodes that'll list out all of the episodes. I'm not seeing many here, man. Yes. We don't really, we don't have many consumer people.

**Dave Jones:** Well, I'll just get to work on my micro watch again. Won't I?

**Chris Gammell:** Yeah.

**Dave Jones:** I'll make a consumer, I'll do a Kickstarter for our watch.

**Speaker ?:** Oh, yeah.

**Dave Jones:** Well... Jeez, that'll be novel, won't it?

**Chris Gammell:** Yes.

**Dave Jones:** Oh, man. I was very close to actually producing that, you know? To going ahead and actually producing that micro watch.

**Chris Gammell:** For... I mean, that's still for a pretty narrow audience, isn't it? Yeah, but... It's like for nerds?

**Dave Jones:** Before crowdfunding, yeah, it's for nerds. Yeah. But this was before crowdfunding even came along, you know? It just wasn't a thing, you know? I would have just sold it myself. Right, right. Yeah.

**Chris Gammell:** Yeah. I mean, what was... So, when you lied to vendors about how many you would use per year, what was your lie?

**Dave Jones:** 10,000, you know?

**Chris Gammell:** Oh, okay. That's still small potatoes.

**Dave Jones:** I sold quite a lot. Yeah, small potatoes.

**Chris Gammell:** Right. I mean, that's the thing. It's a lot. It's a lot to me, right? It's a lot in the industrial space. But for a consumer, that's nothing. You wouldn't get anyone's attention to that. No, no, no. Of course, yeah. Yeah, chump change. Seven figures of devices, right? Like, that's the... Yep. That's when you get the price breaks. So, yeah.

**Dave Jones:** Fair consumer. Anyway.

**Chris Gammell:** Yeah. So, go to China early, I think, is like the main lesson. Is like, go early. Get your hands on, right? Get out in the field. I was reading those... What's that? Steve Blank? He's like the startup guru guy that taught at Stanford. He's like the one who taught Eric Ries.

**Dave Jones:** How many startup gurus are there, right? Yeah, no, no.

**Chris Gammell:** But Eric Ries was in his class. Oh, so...

**Dave Jones:** Okay, so there's some uber startup nerd, is there? Right. Well, yeah.

**Chris Gammell:** I mean, like, but like, people, this is an actual example. Don't worry about that. I mean, like, yes, there's a lot of people that are like, oh, okay, buddy. But this is actually, like, he's legit, I think. Yeah. All right. But basically, he kind of talks about what Jerry talked about. And oh, actually, that's what Jerry... So, Jerry was the guy I couldn't remember a couple weeks ago. He's the one who did that industrial civionics, right? So, Jerry was from civionics, and he was talking about, like, you have to get out of the building, right? And he was the one who would help people. Remember, you and I were talking about, like, oh, like, Jerry should do a class teaching people about this, like, how to do product development stuff. And he was basically quoting a lot of Steve Blank stuff. Got it. And that's the idea. It's like, and this is what Eric McGofsky is saying, too, is that you just got to get out there and not only get out there and talk to your customers, but get out there and talk to your manufacturers. You need to get on the floor, right? And this is the stuff that Ian talks about. Ian, a dangerous prototype who lives in China now. And, like, you know, like, you just, you need to be near your stuff or else you're going to have, you're going to, you know, you're going to have no context. You're not going to know what they're doing. You're not going to have any way to control what's going on. So.

**Dave Jones:** Agreed.

**Chris Gammell:** I'm surprised you haven't been to South Korea yet, honestly.

**Dave Jones:** Oh, all right. No, yeah, exactly.

**Chris Gammell:** Is that going okay? Like, being remote?

**Dave Jones:** No, there's been issues.

**Chris Gammell:** Oh, okay. Yeah, I mean, like, right.

**Dave Jones:** But it's not production issues, really. It's more design issues. Okay. So, you know.

**Chris Gammell:** And I guess the difference, too, is that you didn't dictate the design from the beginning, right? You were helping modify an existing design of sorts?

**Dave Jones:** No, no, no. No, it was done from scratch.

**Chris Gammell:** Oh, really? Oh.

**Dave Jones:** Yeah. Yeah, it was done entirely from scratch. Yes.

**Chris Gammell:** Oh, color me impressed, sir.

**Dave Jones:** No, this is not based on any existing multimeter design at all. But, you know, obviously they take some building blocks, you know, like maybe. Sure, of course. Right, right, right. Yeah. But basically, no, it's entirely from scratch.

**Chris Gammell:** Okay. Yeah. Even like the molds and everything?

**Dave Jones:** Oh, yeah. Yeah.

**Chris Gammell:** Oof.

**Dave Jones:** Yep.

**Chris Gammell:** Wow. Fancy, fancy. I don't have to get me one of these. When is this coming out? Ever? No? Yeah?

**Dave Jones:** 21st of October will be the first 50 of them. I've ordered 50. Man. I've ordered 50. Like a pre, like an early run batch, you know.

**Chris Gammell:** See now, so you're talking about, like, so you are skipping both of the things I just said, right? You're not going to the facility and you're not talking to your customers. Let me, yeah. You are the customer, right? Yeah, exactly. So that's the difference there. But...

**Dave Jones:** Well, I know my customer base, right?

**Chris Gammell:** I mean, you are your customer base, right? Yes, basically. You're going for, like, the test nerd.

**Dave Jones:** Right.

**Chris Gammell:** So... Yes. Yeah.

**Dave Jones:** Exactly. So I like to think I know what I'm doing there.

**Chris Gammell:** I guarantee you what you do. I mean, like, you're probably going to be your harshest critic. Well, it's the internet. You're going to have some harsh critics, but... Yeah, exactly. But the not being on site, I mean, you have built some trust by, like, you private labeled some of the stuff, right?

**Dave Jones:** What do you mean private label?

**Chris Gammell:** Is this... Isn't this the ones that have the... What's the blue meter that I have? That's... Is it the same company or no?

**Dave Jones:** Oh, that's the Bryman. No, no, no. It's a different company. Oh. The Bryman one's just an existing model rebadged with mine.

**Chris Gammell:** I thought it was the same people. I'm sorry. Okay.

**Dave Jones:** No, no, no. Okay. Different company.

**Chris Gammell:** So, well, this might still all blow up in your face, right? That's it. Well, it could. It could. Well, you know. I mean, you've had some on-site stuff, right? You've had some devices in your hands, so...

**Dave Jones:** Oh, yeah, no. We've gone through... I've got 10 different prototypes, you know? Yeah. So, I can see what hardware they're actually producing. So, it's almost... Like, you know, they're contracted to sell it to me for a price. I know, like, they've been very... They're brilliant at giving me hardware. So, that's why I'm ordering 50 up front right now. Oh, yeah. Just so as like a test...

**Chris Gammell:** This is like a pilot run, yeah.

**Dave Jones:** It's basically a pilot run, yeah.

**Chris Gammell:** Right. Are they tooled up to do this? I mean, like... Oh, yeah, yeah. So, this is like an acceptance test, almost. I always forget the names of the...

**Dave Jones:** Oh, it depends on who you talk to.

**Chris Gammell:** What names are you used? PTV. The verification testing. DVT. Design verification testing. DVT. PVT, right?

**Dave Jones:** Oh, that crap. It depends on who you are and who you work for and...

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. As to what acronym you use. Yeah.

**Chris Gammell:** But this is going to be like an early production verification.

**Dave Jones:** This will be the first... Basically, the first production run, pretty much.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, because they're setting up the proper SMD line, you know. Okay. Yeah. So, this will all be... Oh, yeah, yeah.

**Chris Gammell:** Yeah. This will actually be machine placed and... Oh, yeah, yeah, yeah. In theory, if all of the supply chain was in place for this and the parts are on order, you could say, yep, go.

**Dave Jones:** Yeah, yeah. No, well, in fact, the last couple of prototypes they sent me have been from the actual pick and place machine.

**Chris Gammell:** Oh, nice. Okay. Yeah. That's great. Yeah.

**Dave Jones:** So, they are practically finished products.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** Yeah. So, I know exactly what I'm getting. So, unless something goes wrong, I don't necessarily have to be in the factory because they're... You know, if anything goes wrong, the onus is on them. Right. But, of course, I'm the one who's actually promising these things by a certain date. So, you know, yeah, it'd be handy to go there, but, you know, it's South Korea.

**Chris Gammell:** Well, so I think this is a little bit different, too. So, like, this was like a partnership kind of that you were approached with, right?

**Dave Jones:** Well, I approached them and said, hey, because we're talking about other things, and I said, hey, I've always wanted to design my own multimeter, you know. And they went, oh, yeah, we could do that, you know, and just send us some specs and we'll give you a quote. So, I sent them some specs. They sent me a quote for a finished meter, and they came up with a concept of what it would look like. I told them what size I wanted and stuff, and, you know, and then, you know, a lot of to and throwing.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Over a lot of time and effort.

**Chris Gammell:** I mean, yeah, it has been going, what, more than a year, right? I mean, like... Yeah.

**Dave Jones:** But, like, it's not that I contracted them to do it. They basically said, yeah, we will do it, and we'll pay for everything.

**Chris Gammell:** Oh, wow. Okay. And, yeah, I haven't spent a cent on this. Yeah, that's different, people. Yeah.

**Dave Jones:** I, yeah, so this isn't traditional. I have not spent a cent on this, right? And they've been working on this for two years. Right.

**Chris Gammell:** Well, you gave, like, IP, right? Obviously, they benefit from brand and IP.

**Dave Jones:** That's what they wanted. Well, they wanted two things. One, they wanted to sell multimeters, of course, and they believe that with my, you know, my market, so to speak, I can sell quite a lot of multimeters, right? So they think they should make some money that way. Yeah. Right? So, assuming it's a winner, you know, it should sell quite well, hopefully. That's the, you know, that's a bit of risk on their part. And, well, that's a risk on their part.

**Chris Gammell:** Right. Yeah, because they're paying for tooling. I mean, they're going to own the tooling. They're going to own the...

**Dave Jones:** Well, that was part of the stipulation. They said, hey, we're paying for all this. Can we use the tooling for other non-competing products? And I went, yeah, fine. Yeah. You know. So they're going to... Right.

**Chris Gammell:** I mean, they just can't brand it with your name.

**Dave Jones:** Oh, no, they can't brand it with the name and they can't sell a competing multimeter in the same form factor.

**Chris Gammell:** Yeah.

**Dave Jones:** In, like, in the same case with the same tooling. But they can go sell, like, a power meter or some other meter that uses the exact same case with the four AA batteries and the, you know, whatnot. And so that's one thing they wanted from me, obviously, is to sell meters. The other thing they wanted is my expertise in the multimeter market. They wanted to learn stuff from me about designing multimeters so that their own products can get better. Like, not only in terms of features, but in terms of, you know, testing, debugging, you know, what stuff were, you know, and all that sort of stuff. So they've learned a lot from this as well. So that's what they're getting out of. And I'm sure that they're... That's why they want to maintain the firmware. They want to... Like, I asked them, look, hey, should we take the firmware off your hands? You know, should we maintain the firmware ourselves? And they said, no, we want to do it ourselves because we want to, you know, we want to develop code that we can use in other products and stuff. So, you know.

**Chris Gammell:** Okay. So it's like mutually beneficial. Mutually beneficial. Yes. That's great.

**Dave Jones:** It costs me nothing with almost no risk. Well, very little risk on my part and larger risk on their part, but hopefully a larger return for them. So...

**Chris Gammell:** Right. Yeah. Yeah. That sounds like a... Yeah, it's good. Well, as long as everybody abides by the contract, I'm sure it'll work out fine.

**Dave Jones:** Well, yeah. I mean, they've increased the price a few times because we've changed a few things. So it's more expensive than originally intended and stuff like that. And technically, I could just pull the plug, right? I could just pull the plug after a couple of years and they would probably go, well, we're going to sell it under our own brand. Yeah. Right. Because we've paid for it. Right.

**Chris Gammell:** Yep. Yep. Yep.

**Dave Jones:** So it'll happen one way or another.

**Chris Gammell:** Yeah. Yep.

**Dave Jones:** Not that I'm going to pull the plug.

**Chris Gammell:** No, at this point, why would you? Right.

**Dave Jones:** No. But technically, I could, you know.

**Chris Gammell:** Yeah. Well, I mean, that sounds like a sweet deal. It's a pretty good deal. That is to say, most people don't get that. No.

**Dave Jones:** See, that's why I've mentioned on previous episodes, that's why I'm not whipping them. Right. Right. Because I'm... You know, this is not my money on the line. It's theirs. Right. Well, and also, you don't really...

**Chris Gammell:** I mean, like, your timeline is somewhat, you know, fake. You know, like, you promised it, and then that's important. But it's not like, well, you know, I set it up, you know, like, all this PR campaign or something, right? Right. You're going to do a Kickstarter campaign when you're ready to go.

**Dave Jones:** I will do a Kickstarter very shortly. Yeah. Right.

**Chris Gammell:** Right.

**Dave Jones:** Yep. That's exciting. Not looking forward to that. No, it's kind of exciting, but it's a lot of work.

**Chris Gammell:** I don't know, man. You got to watch out. Do you know how to make videos?

**Dave Jones:** No, I don't know. Well, I don't know how to make good videos. I know how to make videos. Right.

**Chris Gammell:** I think it would be weird to see you in a produced, like, a highly, you know, polished...

**Dave Jones:** A highly produced video. It'd suck ass.

**Chris Gammell:** Yeah, that would be really weird. Yep. And be like, hello, I'm David Jones. Welcome to the multimeter factory. And then, like, harps play. Right, right. Brum, brum, brum, brum. I kind of want to see that now, but it wouldn't do well. Nah. Yeah.

**Dave Jones:** Anyway, so, yeah, that's the story of that.

**Chris Gammell:** Yeah. Well, we've, you know, we're talking about all the same things here, right? Like, if you're going to make a product, make sure you can build it, right? Find your...

**Dave Jones:** Oh, if you're paying for it, if your arse and money's on the line, then you want to be there.

**Chris Gammell:** Yeah. Right. Yeah, exactly. Right. And especially if it's consumer. Probably don't do consumer. That hurts. Yeah. Right? Yeah. Oh, wow. Okay.

**Dave Jones:** Well... But there are lower risk. Like, some products are much higher risk than others. You know, if you're just getting like a hat, you know, if you're just developing like a shield, you know, if your product's just a Raspberry Pi shield, which is a few parts on a board, right? The risk is, you know, much lower than something that has, you know, injection molded cases and complex test procedures and complex calibration procedures and, you know, complex stuff in the production environment and, you know, critical parts and et cetera, you know? Right.

**Chris Gammell:** Yeah.

**Dave Jones:** They're almost chalk and cheese.

**Chris Gammell:** It's almost like, like, you know how there's like the different layers of bombs, the material rather. Like, it's like the top line bomb, it's almost like we should have the amp hour law. Like, as the top line bomb number increases, the complexity of the product scales by square. Like, it's like a square law type thing.

**Dave Jones:** It's a square law. Yeah, right.

**Chris Gammell:** Yeah, yeah, yeah. It's like, oh, you're putting a screw into that PCB, right? You probably just got four times harder just for that one screw. You have a screw and a zip tie? Oh, sorry, you're at 8X now, you know?

**Dave Jones:** Like, well, we, the micro supply, which we're working on at the moment, we changed our, not our topology, but we changed what the product, like we changed sort of the top level spec of the product, the top level, how it, you know, the, what's, what am I saying?

**Chris Gammell:** Like the deliverables or the data sheet that you would write, that kind of thing?

**Dave Jones:** Like the feature set? Yeah, the feature set and the usability of the thing. Okay. Right? So totally unusable now. I'm not going to say what. Yeah, I'm not going to say what, but we basically, it's, it's, it's used differently to what, what we previously envisioned with the previous designs. And some of that was to like, were you? Right, right.

**Chris Gammell:** So, so like if I could conjecture, you were talking about battery powered before, so maybe you ripped the battery out or it was, you know, you changed the voltage range or you do, you know, some other big feature set type thing, right?

**Dave Jones:** You're getting warm. Yeah. Getting warm, right. Yeah. Right. No, it's, yeah, like it's stuff like that.

**Chris Gammell:** That's how you, that's how you modulate schedule, right? I mean, that's what, if you want to, if you want to change your schedule, you change your feature set. And then, and this is again, to go back to, you know, what's his name? Steve Blank and Eric Reese and the whole lean startup thingy, right? If you, if you want to get something out faster, make it simpler. Because the truth is, most people are going to tell you it's a piece of shit either way. Yeah, exactly. And that's what you're really trying to get towards. That's the, basically, if you, if you were to summarize that book, it's put the crappiest thing you can into the market as fast as possible. Right. Because people are going to hate it no matter what. Exactly. Yeah.

**Dave Jones:** And that's what we're trying to do. That's good. Not only will it speed our time to market, it'll make it simpler. It'll make the housing simpler. It'll make compliance simpler. It'll make, you know, there's a lot of-

**Chris Gammell:** The problem is when, when you make it and you make the simplest thing you can and people love it. And then they say, and they say, never, ever, ever change it. You're like, oh, come on. Come on, this is crap. Yeah, right. Like, yeah, yeah, right. That's when you double the price. Yeah. And then, and then you make the next version.

**Dave Jones:** It's kind of like the mic, it's, it's like my microcurrent. Yeah. Right. That, that was never designed to be a mass produced product. It was designed to be an article for a magazine. Right, exactly. And a one-off for me. And oh yeah, okay, I'll sell a, I'll sell a couple hundred kits maybe. You know, eight, what, eight, nine years, nine years later, I'm still selling that damn thing. Yep.

**Chris Gammell:** What is on version two or three or something? I mean, like, you've changed a couple of things.

**Dave Jones:** Yeah, yeah, yeah. I did the microcurrent gold. I upgraded that. Oh, that's right. Basically, you know, but people just, I don't, I didn't expect that that form factor and that feature set to be popular.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, it's just what I needed at the time.

**Chris Gammell:** Right. Well, I mean, it's like, if you're making, if you're making good products though, and you, and you, and you have the capability to put a lot out, right? Yeah. It's almost like a throw, throw it at the wall and see what sticks, right? Obviously, you're still solving a problem. Right. But that obviously solves a problem. So, and that's what resonates with people. Yeah. Yeah. So.

**Dave Jones:** So, it didn't need anything more refined or better.

**Chris Gammell:** I mean, having a distribution method such as your face on camera doesn't hurt. Oh, right. But.

**Dave Jones:** Yeah.

**Chris Gammell:** But that's also a benefit, right? That's like a built-in marketing channel. So.

**Dave Jones:** True. But you've got to remember, ever since I've had the blog, right? I had the micro, I was selling the microcurrent before I started the blog. Right. Oh. And then after I started the blog, I actually discontinued it twice. Even though I was market effective, like I did videos on it and stuff. I actually discontinued it twice because the, you know, the interest dropped off. So, I said, oh, it just discontinued. And then all of a sudden, interest just comes out of nowhere. I get a hundred people emailing me, like out of nowhere. And I go, oh, okay, I'll do another one. And it leads to another one.

**Chris Gammell:** That's a great way to actually get people to order something, by the way, is to announce obsolescence. People will be like, oh, no, I need one.

**Dave Jones:** I was waiting. No, I need one. Yeah, yeah. And artificial scarcity, too. Yeah. Oh, yeah. Yeah, yeah, yeah.

**Chris Gammell:** Right. You put a counter next to it and 30 left, 29, 28.

**Dave Jones:** Ah, bye, bye, bye, bye, bye. Psychology 101.

**Chris Gammell:** Right, exactly. Suckers. Yeah. Yep.

**Dave Jones:** Oh, boy. Anyway, the joys of product development.

**Chris Gammell:** The amp hour is, well, not even the amp hour. It's really your stuff. I'm not making anything. Yeah, right. Yeah. The EEV block. For once, I've done a lot more than you. Yeah, hey, look at that. Yeah. I don't think for once. I think, yeah, it's been a slow burn, man. It's been a slow burn. Right, yeah, yeah. Yeah.

**Dave Jones:** I'm consistently slow burn. Right, yeah, that's right.

**Chris Gammell:** Dave is the tortoise of product development. Right. Yep. Well, that's it. Yes. For sure. Oh, one other thing. Usually, I said I wouldn't do this, but we've done it in the past. I've been doing it recently. Speaking of product development, Zach, former guest of the amp hour, Zach from Kickstarter, he has a new podcast, and it's about product development. Ah. Cool. So, it's called, it had a good name, too. I don't remember what it's called. Nope, that's not it. Respect to Zach Dunham. Where is it? The Prepared. That's a good podcast name.

**Dave Jones:** The Prepared? Yeah. It sounds like a prepper.

**Chris Gammell:** It sounds like a zombie prepper movie, kind of.

**Dave Jones:** It's a zombie prepper movie, yeah.

**Chris Gammell:** Yeah. But anyways, I think it's good. I like it. And he's...

**Dave Jones:** Why couldn't, not the prepared, because that implies people, why couldn't it be tech prepared or something? Yeah.

**Chris Gammell:** I think he's a little more design-minded than we are, Dave. Like, this is going to be...

**Dave Jones:** Production prepared.

**Chris Gammell:** This is going to be outside of our circle as well. Right. Okay. So, yeah. So, like, I'm looking at... He has one of the BioLite people on.

**Dave Jones:** Right.

**Chris Gammell:** Which is a cool little product. I was very unsure of that thing. I thought that was going to be snake oil. That's a cool little product. I don't know if you've seen it.

**Dave Jones:** BioLite.

**Chris Gammell:** It's like a camping stove that converts... I mean, it's really just a... It's like a... It's like you put twigs that are burning into this little chamber, and then it's just not a peltier.

**Dave Jones:** Maybe a peltier? Oh, God. No, but... It charges your bloody phone, and it... It does. I mean, like, that's... Makes your coffee. That's...

**Chris Gammell:** Not makes your coffee, but yeah. But... So, I thought the same thing at first, but then go... Watch AVE's teardown. So, AVE did a teardown of it, and he was... He actually did this... He did... He was hardening his as well. For some reason, they don't conformal coat it, and so he was... He hardened his design. He did conformal coating inside, and I was like, oh, man. That's going to stink up the room.

**Dave Jones:** Yeah, yeah, yeah. Oh, that stuff's awful. Yeah. Do that stuff outside, folks. Oh, definitely.

**Chris Gammell:** But AVE, you know, come on. He knows what he's doing. Sometimes. We love him. We love him. He's cool. Yeah. And it's a nice little product inside. I mean, it's cool. So... Okay. I don't know. I think it's a neat device. You know, you think about charging LEDs, stuff like that, like...

**Dave Jones:** Yeah. No, I just... Maybe I'm jaded, because I was approached by a company that's selling one of these things, and I had email discussions back and forth about with the head technical guy who's developing it there. It's like, yeah, like, it's designed for third world countries. You whack... It's got a peltier, and you whack it on a stove, and you fill it with water, and so it dissipates on the cool side, and it charges your phone and generates light and power and whatnot. And I'm just... I don't know. I'm so over those things.

**Chris Gammell:** There's nothing else, though. I mean, if you don't have sun... I mean, like, okay, say where I live in the Midwest, right? Like, you go camping, you got a lot more fire than you do sunlight. You know what I mean? Like, and lugging batteries around ain't always the best idea.

**Dave Jones:** Yeah, I know. I know. But they think, oh, it's got to take over the world, and it's like... No, no, no, no.

**Chris Gammell:** I think that's the big thing. I remember I had a friend that worked on an energy harvesting thing, and it was like... That's always the problem, is that the promises of the top-line specs, like we talked about, those are always just way out of line, right? They say they can do five watts or something. It's like, okay, like on the best day ever.

**Dave Jones:** On the best day ever, withholding your tongue at the right angle while farting Dixie at the same time.

**Chris Gammell:** Yeah, you can't... I mean, like, that's a bad way to spec products, but sometimes in crowded markets, that happens.

**Dave Jones:** It happens by rule, almost.

**Chris Gammell:** Yeah, that's true. It's a consumer product.

**Dave Jones:** Is there a market that is devoid of that? I don't think so.

**Chris Gammell:** Specksmanship? One-upsmanship? Yeah. Yeah.

**Dave Jones:** Yep. It's just everywhere.

**Chris Gammell:** Yep.

**Dave Jones:** I'll have one off this planet.

**Chris Gammell:** All right. Well, you at least get off the show for this week, so... All right.

**Dave Jones:** Thank you. Yes. I'm going back to my PC 104. Back to the old days. Yeah.

**Chris Gammell:** Back to the future. Cool. All right, man. I'll talk to you next week. Catch you next time.

**Dave Jones:** God, I loved this thing that Mike tweeted. Oh, yeah. Yeah. The salt shaker.

**Chris Gammell:** Oh, that's actually not that new, you know?

**Dave Jones:** Salt dispenser. Isn't it? But it just typifies the internet of shit. Yeah. Oh, yeah. You know, it's just... Yep. It's pretty good, right? The world's first interactive centerpiece and smart salt dispenser. I know. Because that's, yeah, what you freaking want. Right. You know, like...

**Chris Gammell:** That was... And the video is so painful to watch.

**Dave Jones:** Oh, I haven't watched the video. I don't think I could... Oh, it's so bad. Oh, really? Okay.

**Chris Gammell:** And even just the name. Smalt. It sounds like something that you wipe off your ass. I know. Oh, I got smalt all over me again.

**Dave Jones:** I got smalt all over me. Oh, man. Oh. Just shoot me now.
