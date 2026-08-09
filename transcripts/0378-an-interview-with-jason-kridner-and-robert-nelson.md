---
episode: 378
title: An Interview with Jason Kridner and Robert Nelson
url: https://theamphour.com/378-an-interview-with-jason-kridner-and-robert-nelson/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released February 4th, 2018. Episode 378. An interview with Jason Kreidner and Robert Nelson. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Jason Kridner And Robert:** And this is Robert. Robert Nelson from DigiKey. And Jason Kreidner of Texas Instruments and BeagleBoard.org.

**Chris Gammell:** Welcome, Beaglers. How are you guys doing? Excellent. Great. Nice to talk to you. Jason is a past guest. That was, God, a long time ago. I think in the double digits of the Amp Hour. So it's been too long since we've talked to Jason on the show. Obviously, we've talked since then. And Robert, I think you're our first DigiKey guest. We have first live DigiKey guest. Do we have some dead ones? Ooh, it's Twitters. All right. Okay. Cool. Yeah, so welcome. Today we're going to be obviously talking about the BeagleBoard project. Is that the right thing to say? The BeagleBoard project? Is it still BeagleBoard.org? I see that stuff everywhere. What do we call it these days?

**Jason Kridner And Robert:** So we're both board members at the BeagleBoard.org Foundation. The community, I guess, would be called BeagleBoard.org since that's the website and BeagleBoard community. But people call it BeagleBone a lot because that's the most popular board.

**Chris Gammell:** Oh, true. Yep. Okay. Cool. Well, that's great. And we were talking before the show too, and we are coming up quickly on the 10-year mark of Beagles, which is pretty crazy to think about, actually. Isn't it? Yeah.

**Jason Kridner And Robert:** It's pretty exciting to me.

**Chris Gammell:** Okay. So what are in the plans for the 10-year mark? Plans? Plans. I mean, come on. You got to have some like celebrations or, you know, like a birthday confetti, you know, cake. I don't know.

**Jason Kridner And Robert:** We've done cake in the past. It's, you know, I think that we don't know what we're going to do yet, honestly.

**Chris Gammell:** Puppies for everyone, maybe. You know, like how about that? Yeah, just... You get a Beagle and you get a Beagle.

**Jason Kridner And Robert:** I love it.

**Chris Gammell:** Yeah. A little messy. A little messy.

**Jason Kridner And Robert:** Don't do it WKRP style, no throwing them out the helicopter.

**Chris Gammell:** Right. Right. Well, okay. So we've talked to Jason before. Obviously, people can go listen to that one. Let's get a little bit about Robert, especially because you're, you know, so you're working at DigiKey, but you're also on the Beagle board board. The Beagle board board. Yeah, the board of the Beagles. Okay. Yes. So why don't we get a little bit of background on you? So what is your story? How did you get into this all?

**Dave Jones:** Ah, for me, it just started on when TI announced the product and we actually advertised it in Thiefer Falls at the local radio station. So I picked up the first board and I noticed it was running in Angstrom at the time and like, I don't like this. And so I ported Debian to it. And then a couple of days later, I went in the mail and was like, hey, here's how I get Debian on this board. And 10 years later, look what happened.

**Chris Gammell:** Yep. Stuck with it ever since. So what was, you said it was Angstrom to start with. I, I'm trying to think, I was trying to think back of like the first time I saw a Beagle board was probably one of the early ones, but that was like, what was that first one too? It was like pretty, it was like 150 bucks and it was a bigger processor, right?

**Dave Jones:** Yeah, it was 150 bucks. It had 128 megs of SD-REB and I think 128 megs of NAND. And the guys at Angstrom got all that to fit on there, including a desktop. So it was very well done.

**Chris Gammell:** That's cool.

**Jason Kridner And Robert:** Yeah, the first, the first distro we actually brought up on the original Beagle board was Mamo, which I think most people remember, but it was the operating system. It was Debian packaged base, but it was cross built into this crazy tool called Scratchbox. And, but it was for those, the, the tablets for these Nokia tablet devices, Linux based tablet devices.

**Chris Gammell:** Okay. Kind of like how all of like all the all winter parts are going on everything these days and they're super cheap. It's, this was targeting for the tablets as well, right?

**Jason Kridner And Robert:** Yeah. So the one of the, the, the, the same processor, the OMAP three processor that was used on the original Beagle board was also used in the, the Nokia N900 tablet. Okay. So that was the first, that was the first one. Everybody remembers that one, huh? Who's Nokia? No. Right. Exactly. Only the, you know, at the time the world's biggest, you know, mobile phone maker, but you know. Right. Oh, how the greats have fallen. Things change, right? So we, and then I, I started playing with Gen2, which was my favorite Linux distribution. I like, cause everything builds from source. I know I can always continue to move forward with, with that.

**Chris Gammell:** Right. What a friendly open source way to do things, right?

**Jason Kridner And Robert:** You know, friendly is, you know, friendly for what, right? Yeah. Noobs. Come on. Well, noobs are very important. And being friendly to noobs is extremely important. And I think it, you know, comes to respecting people that are experienced as well. If you're nice to noobs, then, you know, it's an easy on-ramp for experienced people. But sometimes what people want to do, um, can't be easy when you try to oversimplify things. And sure. I do agree with that.

**Chris Gammell:** Although we will get into that some of the future plans. So that'll be an interesting contrast as well, I think. Uh, so what does it take to, I mean, I, I have to just kind of plead stupidity here. Um, as I often do, but like if, if one is going to target a, so it's like a, you see a new board, it's got angstrom on it. You're like, I want to put Debbie on it, Debbie on it. Like what is, what is, what is the steps you have to take in that case, Robert?

**Dave Jones:** In that case, I had to figure out how to build a root file system from Debbie. Okay. And at the time, uh, I think D bootstrap was existed. I just didn't know about it. So I started with, sorry, what I'm going to probably stop you a couple of times here, but what is, what does that mean? So D bootstrap is an internal tool in the Debian system that allows you to, um, generate a base image from a set of optional options. So it's a very, very complex tool. Okay.

**Jason Kridner And Robert:** At the time, um, you know, way, way back this time, um, Debian wasn't really built, um, for cross compiling and there weren't powerful enough arm systems. To actually natively build all of the arm packages. Um, interesting.

**Chris Gammell:** Okay.

**Jason Kridner And Robert:** You know, Debian, Debian was a little bit different. Debian got to arm much faster than Ubuntu did because, you know, they were targeting embedded devices much earlier, but it was just, you know, the very limited number of packages that you could really cross compile. Did you cross compile everything, Robert?

**Dave Jones:** Uh, at the time, uh, I like, I natively built all the kernels, even on the 120 megabyte, um, uh, original Beagle. So it only took about six hours to build like a 2.6.28 kernel.

**Chris Gammell:** So that means that it was actually being built on the device itself versus.

**Dave Jones:** At the same time, I was testing the stability of the device. So that kind of came in handy. It's like, if it survives a six hour build, it's got to be good, right?

**Jason Kridner And Robert:** But how many, how many packages did you have in your root file system? If you were, were you natively building the packages too?

**Dave Jones:** Um, at that time I wasn't rebuilding the packages. So it was just the kernel at that time. Okay.

**Jason Kridner And Robert:** There was enough arm HF packages or, I guess it wouldn't have been arm HF at that time.

**Dave Jones:** It was even worse. It was etch, which was arm, which was E-A-B-I-3. Yeah.

**Chris Gammell:** I'm going to have so many links to try and find, uh, for people too. So I'm going to be kind of on the outside here, I think. I'm sure these two could, you know, could talk all the time about that for hours about this stuff too. Uh, okay. So, so I guess one of the things that I always wondered about, like, so say, say I have a brand new, so, uh, maybe not the risk fee, but like, just say there's a new chip, the XYZ chip that comes out tomorrow. Right. And I want to go do what you did. So the XYZ chip has Angstrom on it and I'm going to go put Debian on it. How is it that, like, the, that the whole system even knows what's available within that processor? Is it like there's, there's like, uh, there's libraries that are already built from the vendor that, that gets pulled in?

**Jason Kridner And Robert:** The power of the Linux kernel is power of mainline.

**Chris Gammell:** Again, I'm going to, again, I'm going to, uh, you know, plead ignorance on this stuff because I guess I don't quite understand that either. You know, like, so the power of the Linux kernel, sure.

**Jason Kridner And Robert:** But that's meant to abstract all the hardware. Um, you know, it doesn't. Um, but, uh, it does a, a pretty good job of abstracting all the hardware. So if, um, a package needs to write to a display or, you know, read, uh, um, you know, something off of I squared C, you know, read a keyboard, um, you know, have a network, you know, send, send packets over a network device. The Linux kernel handles all that. So the first part is, um, well, the first part's actually the bootloader. So you have to get a bootloader up that knows how to load the Linux kernel. And then you have to have a Linux kernel that will run on that architecture board.

**Chris Gammell:** Um, so who writes that piece that's from the, so it's because you need to rewrite the kernel. Cause I know this is what Robert does now too, is like some of the kernel stuff, but like the, the, to, for the kernel to understand what is actually available there, there needs to be some kind of like interface. Right. Or someone has to write that. Is it just drivers or is it other stuff or what is it?

**Dave Jones:** It's a lot of low level drivers. And a lot of times it starts with either just a serial port that magically works or you have a JTEC that you can plug in.

**Chris Gammell:** Okay.

**Dave Jones:** And a lot of times it's just, you have to find something similar. It's like, okay, what do we change between these boards? And you kind of poke around until you get something booted. And usually once you get the console, you're, you're golden. You can start doing a lot of stuff.

**Jason Kridner And Robert:** And we're assuming we're already on the CPU architecture at that point. Right. Cause there's, if you're talking about risk five versus, you know, arm. Right. Versus arm seven or whatever. Yeah. Right, right, right, right.

**Chris Gammell:** Yeah. Right. So, okay. So that's, that's another piece then is the, so what is the architecture piece then? So like, you know, first you need a compiler.

**Jason Kridner And Robert:** And for Linux, you need the GCC compiler. You can, at least for upstream, you can compile the Linux kernel with, with other compilers like LVM or a number of different commercial compilers. And a lot of times you bootstrap them with some type of commercial compiler. But then you need, you need, you need some compiler support for back. So back in the early days of Beagle getting the, the, the, the compiler support into mainline GCC for the arm B7 architecture was actually a big part of, of, of what we were doing. Um, we, we paved the way, um, for a lot of people with what we did with, with, with Beagle. Um, yeah. Cause.

**Chris Gammell:** Right. Cause it's these projects that, you know, like why would, why would commercial companies care about it? They're like, they're not seeing any direct benefit of it. Right. And it's like probably some off brand or smaller architectures. Right. I mean, if you're targeting a tablet type stuff.

**Dave Jones:** Yeah. At the time, Nokia helped out big time too, because they run the same architecture on their phones. They needed GCC cause their OS was, it was based on Linux. And so they needed it too. And they were, they had product to move.

**Jason Kridner And Robert:** And they had a great, they had a great community. Um, the Mamo community was really strong. Um, and we just poached it. Yeah.

**Dave Jones:** Especially if they're in the eight 50 phones. I mean, it was one of the first tablet phones that was like a tablet, but a phone in the nineties.

**Jason Kridner And Robert:** And you can actually run your own code on your phone. Um, and you weren't, you weren't locked out and you talk about a way to get the geeks involved. Right.

**Dave Jones:** I mean, like, well, even today on the mailing list, people are still porting kernels to the N900 series. So that was a single core phone that came out early two thousands and they're still pushing mainline.

**Jason Kridner And Robert:** And there've been a number of open phones that have been built based on the, the, the Beagle board that are still supported. And, um, you know, we have folks that continue to do kernel development because of that. Um, so it's, um, the, the, the golden delicious one comes to mind. The, the, the open Moco.

**Chris Gammell:** I remember open Moco. Yeah. I remember, I remember one of my old coworkers was super excited about it. And then it just kind of, it didn't disappear, but obviously, but it's just, it, it didn't, it didn't get, you know, the hype obviously went.

**Dave Jones:** It just took them a long time to get everything done.

**Chris Gammell:** Well, there's, there's a lot to do.

**Dave Jones:** I think at one point there was adapter for the Beagle board, uh, XM.

**Jason Kridner And Robert:** They had actually plugged into the phone. Yep. It was this monstrosity, but they, they've moved on since then. They're still using, um, uh, you know, they've, they're still using a derivative of that.

**Chris Gammell:** So, and, and when you say Beagle, or Beagle board rather, that's the, the old Ford factory, I'm trying to remember. It was like, what, like three or three or four inches?

**Jason Kridner And Robert:** The original, I think, was 3.1 by 3.0, uh, inches. Okay. In inches. And then the, the XM was three, three and a quarter by three and a quarter. Uh-huh. Um, we had a little bit bigger cause we put a four port USB hub and, and ethernet, the hub based, USB hub based ethernet. Ugh.

**Chris Gammell:** Well, there's been this continued convergence too, right? So like, as more people came from the Arduino system, wanted more power there. Obviously the, the size of the parts have all been, uh, shrinking. You guys have been pulling off, you know, certain peripherals over time as well. And adding more. Because I remember like the first one. Well, yeah, adding more too. But I just mean that like, I remember the number of ports in the first one, it was like more like a, like a mini ATX computer than it was like a, like what it is today. Right. Or like the, well, we'll get to it's pocket beagle. Right. So like, so like those two different things are obviously your stuff is all shrunk and the other stuff has, has blossomed in terms of, you know, processing power, but it's, they're starting to kind of converge in the middle. Yeah.

**Jason Kridner And Robert:** And we still kind of do both sides. We've got a, a bigger board. What's the X-15, bigger board X-15 still kind of doing the, the more of like that. Um. The high end. Desktop computer replacement. Yeah. Uh, what's that like four and a quarter or something square? I don't remember. Okay. I'm looking at one, but I don't know exactly how big it is.

**Chris Gammell:** Right. It's like commercial, but it's like a, you know, like a commercial computer that people might want to write or borrow code for or whatever. So. Yeah. But let's get back to the, uh, the compilation stuff too, because that's interesting. So, um, okay. So you're at that point where you've, so now you've, you have the kernel, uh, you have these, uh, the compiler, like you said. What, what next? Is it like, you're like, so then the kernel's like, well, I don't work with A, B and C that the drive, the display driver. I'm never going to talk to that thing. I'll never talk to the USB. So you, is it like at that point you start kind of going down the list or. Yeah.

**Dave Jones:** We start going down the list of like what you need first. And it's like, what do I really want from this project? And you, you try to get that thing working first for you.

**Jason Kridner And Robert:** Well, now most of the, so we've got so much working now and sort of a baseline that when people do derivatives of a beagle bone, right. For the most part, all they have to do is write this configuration text file called the device tree and, and they've got a new board.

**Chris Gammell:** And so that would just be like adding on. So I, I want to add a new chip on there. It's on the spy bus or something. Basically just need to change the device tree to add that new chip on the spy bus or.

**Jason Kridner And Robert:** Yeah. Or yeah. Or even on chip peripherals, you know, a different derivative of a similar processor, but it's got different on chip peripherals. Yeah. If you're adding something to a spy bus, exactly. You just specify what you've connected to that spy bus in the device tree. And I think like of the, cause how many different, there's like 20 different beagle bones now, Robert. Do you know how many we have out there?

**Dave Jones:** There's a lot there. There's at least 10 to 20 derivatives. There's 10 or 20 direct copies of a different name. There's tweaks.

**Jason Kridner And Robert:** So some with wifi on board, some with spy flash on board, some, you know, with different, you know, long distance radios or. Yeah. There's a, there's a number of them with different speed, ethernets, different.

**Chris Gammell:** So what makes a beagle bone, a beagle, or beagle board, a beagle board, I suppose. What, what is, what is that? You know, what is, what, what makes it qualify now?

**Jason Kridner And Robert:** Is it just using the package? There's obviously the trademark. Well, obviously. Jeez, Jason, come on. But I think it's really just from a, from a technical standpoint, it's just the ones using the AM, the TI AM35 processors, 335X processors, kind of the base for it being a beagle bone where all you have to do is kind of change the device tree. But really just interacting with, with Robert mostly just to try to make sure that when, when he creates.

**Chris Gammell:** He gives you the thumbs up. He, he is the beagle maker.

**Jason Kridner And Robert:** When it, when it, when it, if you want to run his distro images, right, then there's stuff that you have to make sure that you've got things going into his package build so that it'll boot up and run on your board so that we can all run the same images. Right.

**Chris Gammell:** Well, I guess, so that's another question then too. So, so you mentioned the AM35XX, right? So that's like, that's the, the TI part that's on all these things. And now the, uh, uh, what's there called Octavos packaging those into their thing as well. So it kind of pulls more in and we'll talk about that. But if, if I was going to like try and port the beagle image to something new, right, how, what would be a close, a close thing? Obviously there'd be a lot of, a lot of wailing and gnashing of teeth, but like, what would it take then to actually go and do that same thing?

**Dave Jones:** Uh, the biggest thing, as long as, uh, you got Uboot working and the kernel, we could pretty much package it all in the same image.

**Chris Gammell:** Really? Okay. And so when you say it's in the same image then, so like moving forwards, if I download the image tomorrow and it's got, uh, support for a new board, like Jason's stuff. So Jason makes a new board, you update the image. I download the new image tomorrow. Does that mean it's going to still keep running my stuff, but then it'll also start running Jason's stuff?

**Dave Jones:** Yep. As long as a couple of requisites are made. Uh, okay. We're very lucky with the, how configurable Uboot is right now. So as long as it's an AM335 target, doesn't matter what variant it is or what it is, uh, it can all boot off the same image. But now.

**Chris Gammell:** Oh, so I was actually saying like outside the AM335.

**Dave Jones:** So outside the AM335, um, we generate for an AM5 variants, the Beagle X15. Right. We still generate for the OMAP 36, which is a BeagleBoard XM. And that'll also work on the original Beagle. Okay. And with a bootloader change, that'll actually work with the old PandaBoard too, which.

**Chris Gammell:** Oh, cool. Okay.

**Dave Jones:** Those are kind of getting hard to find nowadays.

**Jason Kridner And Robert:** But if you, if you change, if you, if you, if you need a bootloader change where the bootloader itself has to change, you essentially have to pass, patch the disc image with a different bootloader. We can't just like boot off of the exact same, the exact same SD card image.

**Chris Gammell:** Right. Okay. Yeah. And it's almost, it's almost like feels like, like a family tree almost right within, you know, within the immediate family and then the extended family. And then, and then maybe you're the neighbor to this family or something. You know what I mean? Like it's, there's, there's a wide variety of what you could do, but obviously being closest to the center of that family tree, you're going to have the easiest time and making a new image or trying a new thing. Like, cause I, I have to imagine, and I'd like to get in this, into this later too, is the, you know, as people are designing these things into, uh, you know, like commercial products or just, you know, I, I think industrial stuff is a, it's a great target for this stuff. Um, this is a real concern, right? I mean, like I, if I go and take a new chip, put it down on a board, I have a bunch of new peripherals that are not in any other Beagle, uh, Beagle product of any type. Uh, then I want to make my own thing, but I also want to, any future improvements that y'all are making, you know, I want to be able to pull that into my new image as well. And I have to kind of maintain that over time. Right.

**Jason Kridner And Robert:** Yeah. The biggest challenge is if you don't submit the patches that, that you're making, um, somehow back, um, if you want to be able to move to the new images, you have to, to, to reapply your changes. Um, uh, that's, that's the, the biggest challenge is like, Oh, you want to update, you know, move to the latest image and just run it. Well, if you didn't either isolate your changes, so they just load on top, um, or submit them to, you know, preferably the, um, Linux mainline or U boot mainline. Um, you know, we won't pick them up now. If you, if you get them in the mainline, we'll pull them down into our images. Um, we're always, um, you know, tracking the, the latest Linux kernels. Right. So we've got, um, like the stuff we're doing on a regular basis is on the 414 kernel. Um, so I don't, is, is 415 out yet? Yep.

**Dave Jones:** 415 went out this morning and, uh, and 416 already opened up. So.

**Jason Kridner And Robert:** Okay.

**Dave Jones:** Yeah. Well, we do a lot of back ports. So right now we got three main kernels we're working on 4, 4, 4, 9 and 4, 14. Wow. Yeah. The goal was a transition of 4, 9 pretty quickly, but the 4, 4 is just too darn stable. Oh, got it. Okay. And so.

**Chris Gammell:** Yeah. Yeah. That's interesting. So, I mean, like, so, and, and maybe for people that have never people, me, uh, people and people like me, uh, so like if I wanted to go and start compiling my own stuff tomorrow, right. To make my own image tomorrow for a new, maybe not even for a new thing. Just, I want to go try out. I want to go try it out. I want to go see if I can just do this. Where do I start?

**Jason Kridner And Robert:** Um, buy a BeagleBoard X 15. Because you need a nice, fast arm target, arm system to do your building on. So, um, rather than trying to do, figure out how to cross compile it, go buy yourself a nice BeagleBoard X 15 and then download the, um, github.com slash BeagleBoard slash image dash builder, which is a repo that Robert maintains that has all of his scripts that he used for building the images. So you run that script. It actually spits out a disk image, um, or about 10 of them. I think I don't remember how many, um, well, depending on what script you run, but, um, and then, um, and then try booting that image and then start changing the script to, to, to, yeah. Make it do different things. But it's all just pulling from the mainline Debian repos. And then a set of repos that Robert maintains with various customizations.

**Chris Gammell:** And so when, when you say like, so the cross compiler thing then you're talking about is it's easier to build on the system it's on because it's already targeted at all the things you need to have all the peripherals, whatever.

**Jason Kridner And Robert:** It's all these different packages have, um, the, a lot of them build in a way that kind of probes the system that's running on. So it needs to be running on something kind of that looks pretty similar in terms of architecture. Um, uh, all these other, um, there's a lot of fancy systems like the Octo project, um, that, uh, try to fix all that. It turns out for all these packages, it's a lot of work to fix all these packages to,

**Chris Gammell:** to build, to actually work and make it look like something else when you can just run it on the thing you're running on. Yeah.

**Jason Kridner And Robert:** And, and that's, that's why we, we made the, the, the shift. There's the arm systems are fast enough. Um, we'll just assume that we can, can build natively and try to move quickly as possible without having to try to fix all these path, uh, packages. Now there's a lot of other reasons why, um, Yocto is great in doing all this fixing, you know, provide some, some proof point, you know, that you kind of own your own destiny a little bit, but I think our shared destiny is large enough with the Debian world that, uh, we can have a lot of fun stuff going on.

**Chris Gammell:** Right. Cause then you start to pull in other software tools that are available. A lot of the people that are getting used to a bunch, not getting used to, but are regularly using Ubuntu. It's just such a, that's such a big project these days too, that it's, you know, you get a lot of that crossover. Yeah.

**Jason Kridner And Robert:** And if you want to, if you, if you want to cut and paste stack exchange messages, you know, post. Ah, you know me well. So for the cut and pasters, this is the way to go.

**Chris Gammell:** And so Robert, what are those, I mean, what, what do those scripts look like? Are they, didn't see, I guess I don't even know. I'm so out of my element guys. It's mostly in bash. Okay. Bash. Yeah. That makes more sense. I'm so out of my element. Sorry. Yeah. Is it like code or? It's a very C like bash. Are there resistors involved? You know, we do hardware too. I know. We'll get to that. We'll get to that.

**Dave Jones:** It's essentially a thousand line bash script file. They're all terminal commands. So. Okay. So it just scripted terminal.

**Chris Gammell:** So I could type them in one by one, you're saying. Yeah. If I really wanted to learn. You could.

**Dave Jones:** Or you could just put the minus X at the top and then run it and it'll shove you all the commands it's doing. It's probably better. Yeah. Yeah. Okay. But it's just, it's just a script to automate, run in, deboot scrap and a bunch of other scripts that we do. So it's just to make your life easier.

**Chris Gammell:** I mean, are people doing this? I guess that's another important question. Is it like, is it worthwhile for people to think to do this? I suppose.

**Dave Jones:** Other than the learning. We do have some people doing it and they do ship images based off of it. So I've got a lot of patches over the years from people like, well, I tried this with this and this is a workaround I needed.

**Chris Gammell:** Again, I think the custom hardware thing, like, you know, and especially if it's succeeding, right? I mean, if your project's doing well, the Beagle project rather, it's like, you know, it's putting tendrils in all these parts of the electronics economy and, you know, shipping more parts. That's what TI wants to and yada, yada, yada. That's like, yay, open hardware. So yeah, that's good. But then this is kind of that other piece that I think I usually don't think about, right? It's like, oh, of course it would work, but this would scare me off, to be honest. That's good.

**Jason Kridner And Robert:** You shouldn't have to do it, though. Hopefully this is not the... For you doing... You know, you decide you want to make your own computer. All the problems that you brought up shouldn't be the ones that scare you off from, should I go and build my own computer? You know? What should scare me off, Jason? Well, I think if... So you make hardware, huh? So, you know, you should have some idea of what signal integrity means, you know, some idea of, you know, match trace links, you know, that done something with microcontrollers before. Sure. But if you've made microcontroller-based computers, you should be able to use something like the SIP that's on the Pocket Beagle to go and make your own Linux computer. And if you don't want Linux, don't use Linux, but you could use Linux. Differential trace is now available in KiCad, you know? Yeah. Yeah. It's in KiCad. It's in Eagle. I know. It's in Upverter, too, although we haven't actually verified the Upverter version. Womp womp. Womp womp.

**Dave Jones:** It could be hand-soldered.

**Chris Gammell:** Yeah, that's true.

**Dave Jones:** Yep. Yep. Cool. There's a good YouTube video and showing how to do it. Nice.

**Chris Gammell:** Nice. All right. Well, let's get into this. I mean, like, so, obviously, you know, I'm talking about putting stuff on boards. I've thought about it now because of the Pocket Beagle. You know, like, there's the new part from Octavo. I think it's a great, you know, little part. It's got a better BGA, a more accessible BGA. So, what are you seeing with that? Well, first off, what is Pocket Beagle? Because I mentioned it a couple times, but I talk too fast.

**Jason Kridner And Robert:** I have known to have a little fetish for mint tins. Yeah. So, the original Beagle bone fit inside of a standard mint tin. Can't say Altoids tins. I can say it. Yeah. Try not to. That's right. And so, Altoids also makes the Smalls. I'll go ahead and, since you cracked that one open. Oh, right. I said it first. Yeah, right. But the Altoids Smalls mint tin, the Pocket Beagle is in that shape. Because we can. Right. Right.

**Chris Gammell:** I always do bring up, I'm like, it is metal and this is electronics.

**Jason Kridner And Robert:** But it's perfect for storage while it's not powered. Right. Right. Right. Right. Yes. You can generate some static. But it's also not too hard to put some insulating material on the inside of it and take a Dremel and cut out openings and actually run it safely.

**Chris Gammell:** This sounds super convenient. Super convenient.

**Jason Kridner And Robert:** It's a survival tool, right? It's a...

**Chris Gammell:** I think, you know what I think? I think it's a great constraint. Engineering needs constraints and that's one of them. And I think that the new one with the mini tin too, I think, yeah, it's a great constraint. Now, I mentioned, you know, I warned you before the show, I was going to take you to task a little bit about this. But why don't the headers fit next to the part? Because you haven't used the right headers yet. Which I was excited to hear. I was excited to hear that. So, you're going to send me a link to these headers? Is that right? Sure. So, what are they? Like narrower headers?

**Jason Kridner And Robert:** So, right now, and Robert may have some updates on it. Right now, the headers that I know fit are actually single row headers. And you can take single row headers and just put, you know, two on each side. And they fit neatly flat, you know, so you don't have to have them, you know, sticking up. Robert doesn't seem to mind using the longer leads in order to get up above.

**Chris Gammell:** All the ones that can, like, plug below it. Yeah. You know, like that.

**Jason Kridner And Robert:** Yeah. Yeah. Yeah. If you want to put the female headers on top, you can use the single row female headers. And they work great. But, yeah, you have to put four of them on there. Two on each side.

**Chris Gammell:** Yeah. So, if people don't know what I'm talking about here, it's actually that if you use a double row, what is it, 2x18? 2x18, I think. Yeah. Double row, the thickness of the plastic runs just into the edge of the Octavo SIP, which is, it's super close. But like Jason said, you can fit stuff in there. My solution was actually just to put them upside down. So, I put them on the bottom side of the board, and then I put male headers on the board that I was building.

**Dave Jones:** Or a belt sander works great, too.

**Chris Gammell:** There's an engineer right there.

**Dave Jones:** You just need to take a millimeter off of it, so.

**Chris Gammell:** That's right. Right. I was thinking about doing that and just selling those, you know, just like a little cutout, like a small cutout, you know. Just machining it. Instead of a little jig, machining it out.

**Jason Kridner And Robert:** I just can't figure out why all of the double row headers are at least five millimeters wide, whereas we can find the single row headers smaller than two and a half millimeters wide.

**Chris Gammell:** And they're all. I mean, if there's anyone in a connector company, we're talking about a pure opportunity here. Obviously, the Pocket Beagle is a $25 little powerhouse, so you could sell at least 100 of these things if you make new. I said at least. Who knows? The sky's the limit, guys. We need two of them, so 200.

**Dave Jones:** Oh, there you go. Yeah, for some reason, all the dual row plastic ones are, they're wider than they say in the spec. So, single row ones aren't.

**Chris Gammell:** Interesting.

**Dave Jones:** Okay. They all went that direction.

**Chris Gammell:** Maybe just for stability? I don't know, shooting in the plastic or something.

**Dave Jones:** Old bulbs?

**Chris Gammell:** Oh, yeah. True. That could be it. They just, yeah. As they just wear down, they get wider and wider. That's very possible. Okay. So, what actually prompted the Pocket Beagle in the first place?

**Jason Kridner And Robert:** Well, the new SIP was a big part of it, getting it smaller. So, because we can. Okay. Yeah. So, there's a, for a lot of people doing teaching, they really, really care about having the lowest possible entry price. Uh-huh. So, we wanted to do something at a lower price point. I also wanted to do something, in some ways, a little bit more flexible for people, you know, building, you know, systems around it. You can, you don't need to put headers on these things. You can actually just solder them straight down to a board, like a module.

**Chris Gammell:** Yeah.

**Jason Kridner And Robert:** So, it makes that sort of thing simpler. There's less resources essentially used on the board because, you know, we just kind of break things out more basically. But for people doing training, they really care about the lowest possible entry point. I wanted to show off just how simple it is to make something around the SIP give us a starting point for building other things. Yeah. So, you know, we work with people doing different derivatives at different times for fun. Like the BeagleBone Blue uses the older SIP on there, the bigger SIP.

**Chris Gammell:** Oh, yeah.

**Jason Kridner And Robert:** Right, right. But we...

**Chris Gammell:** And that thing was kind of big. I mean, it's like, it like is imposing just because it takes up. I mean, obviously, it was as our table was getting started. It was one of their first chips or...

**Jason Kridner And Robert:** That was their first SIP. Yeah.

**Chris Gammell:** And, but it's just, you know, it's big, but it works great. And so, the Blue is the motor driver one? Is that right?

**Jason Kridner And Robert:** It's a full mobile robots, mobile robot controller. So, it's got the Wi-Fi and Bluetooth built in, but it's also got output for eight servo motors, including the six volt power rail for those. It's got a two cell lipo charger balancer over voltage protection. It's got four DC motor drivers. It's got CAN bus drivers on it. It's got, you know, the 10 axis inertial measurement unit, you know, compass, accelerometer, gyro.

**Chris Gammell:** For doing like an upright, upright balancing robot type thing.

**Jason Kridner And Robert:** Yeah, or drones, you know, quadcopters, hexcopters, octocopters. So, it actually runs RG pilot out of the box. Oh, wow. Okay. So, you know, building a drone out of it's pretty easy. If you want to build submarines, you know, yeah. There's... But it's got all that stuff shoved into one board and the SIP makes that possible. So, we have a fairly application specific and I think it's a pretty broad application when you talk about mobile robots.

**Chris Gammell:** Sure. And you would introduce me to one of the professors doing stuff with that. I forgot his name though. You would introduce me.

**Jason Kridner And Robert:** There's a number of them, but if you're talking about the one that was involved in defining and creating it, it's Tom Buley at UCSD, University of California, San Diego. So, they've been teaching robotics classes with the BeagleBone Black and an add-on board, which is now a standard BeagleBone.org product called the Robotics Cape. That's on its fourth generation and they've been teaching that for, you know, robotics for years and controls there. And now we just kind of integrated that all into one board with the BeagleBone Blue.

**Chris Gammell:** That's great. And so, and that's like at the, they are working at the Linux level, right? So, they're writing Python type stuff? You can, yeah.

**Jason Kridner And Robert:** If you want to use like ROS and Python, you know, we've got the balance code written in Python as an example. We've got Python and C examples for doing things like the balancing robot and turning the wheels, reading the quadrature encoders, you know, reading the different sensors on the board. But, yeah, so it's all done on top of Linux. There's a library that kind of abstracts the hardware and some of it actually does do some memory mapping. But we've been working with folks to try to get more of that into the Linux kernel rather than peeking and poking things in user space. Can you explain that more? Yeah, so the right way to do things in a Linux world is to actually make a Linux kernel driver such that the kernel driver supports the hardware. So, nothing in user space should be really touching the registers, you know, that, you know, control the peripherals that talk to it. It should all be done through drivers to be things, you know, for properly abstracted in a Linux world. So, what...

**Chris Gammell:** So, people do that though because it's faster if they want to get down faster or what?

**Jason Kridner And Robert:** It requires less understanding of the system. It's not necessarily faster or slower, right? It just means that there's less time spent doing integration. So, people bypass the Linux kernel and say, oh, I'm just going to memory map this peripheral. And, you know, they'll say it's faster. What they mean is that they were able to reach their timing goals in their project faster. Where, you know, they may think that it means faster, but it really just means that, you know, it takes extra time to try to figure out how to put things in the kernel nicely so that, you know, it can be maintained and the system architecture is right and it meets your performance goals. So, yeah, a lot of people in the community will just memory map a peripheral and use it that way. There's also... There's some firmware that comes... There's a firmware load that comes with the BeagleBone Blue to use the PRUs or the programmer real-time units to generate some additional hardware PWMs. Not hardware, but it makes it look like it's hardware PWMs because these microcontrollers are doing the pulse width modulation. And also doing things like for RGPilot, it reads like four different types of remote control protocols and does auto protocol detection. And so it can read all these different remotes. The default image also uses it for one of the quadrature encoders because I think we only have three hardware quadrature encoders. And so the fourth one is actually implemented in PRU software. Okay. And the PRUs in a lot of things, even stuff like the Lego Mindstorms, the EV3, there weren't enough... They uses another TI processor, the AM1808, and there weren't enough UARTs to talk to all the different things that it needs to talk to. And they use the PRUs to generate software UARTs. Okay.

**Chris Gammell:** Well, I'd love to talk about the PRUs, but step back one bit to the user space versus the other stuff. Sure. So, all right. I'm going to again show my ignorance here. But like, okay, someone wants to... This is going to sound stupid. Program a beagle bone. So like I'm in the world of microcontrollers all day. Anytime I'm programming anything, it's a microcontroller. So I'm writing code, it gets compiled down, it gets loaded into Flash, and then it runs from there into RAM, blah, blah, blah, blah, blah, right? But like, are people writing drivers regularly? What are they doing normally?

**Jason Kridner And Robert:** So I'm going to describe a board bring up and then talk about some other stuff. So like if I'm bringing up a new board based on the system and package like used in the beagle board, the beagle bone, like the pocket beagle. So I'll boot the Linux kernel and you would just get the Flash interface working or the UART working or something else. And I'll actually boot the Linux kernel. And then when I want to like test the connection, like test the I2C, there's actually command line utilities like probe I2C. And you can do a tremendous amount of like board level system debug and development just sitting there at the Linux command prompt. You don't actually need to write any, you know, code per se. You're just, you know, going to sysfs entries and like reading a GPIO, setting a GPIO line.

**Chris Gammell:** Right. And so, yeah, and Ken's, so Ken Shura, former guest, had a really good article about doing that with the pocket beagle, right? So he was just blinking an LED, doing it with sysfs, right? So like just basically reading and writing.

**Jason Kridner And Robert:** So, you know, you can create entire applications doing things just that way. But, you know, the nice part about new boards or new systems is it's just a way to actually make sure everything's working. And then if that's all the performance you need, just do that, right? Just do sysfs entries and stuff. But if you need more, then, you know, maybe you'd write a kernel driver. And a kernel driver is just a program that's linked against the kernel. And it can be dynamically linked and loaded. It's really not, and it has a certain API available to it. From embedded systems developer, there's not that much difference between a kernel driver and a program, right? You just, just how it gets linked and run. Well, saying that sounds easy. Yeah. Yeah. But a lot of people, you know, just, you know, they're writing Python scripts. And there's some libraries that you can use to do, you know, GPIO. And people, there's extensive libraries to talk to all sorts of spy devices through spy dev. But for the most part, the hardware that you want to talk to, there's so many different sensors that Linux already knows how to talk to. And you just have to tell it what's connected and where. And the Linux driver is already there.

**Chris Gammell:** So this wouldn't take, like, a rebuild like Robert was talking about?

**Dave Jones:** No. Take even less than this. Oh, really? Okay. A lot of times, it's just one or two lines in the device tree.

**Chris Gammell:** Okay. So maybe I'm not understanding what the device tree is then. I'm thinking of, like, the Windows hardware manager type thing. That sounds stupid, but yeah.

**Jason Kridner And Robert:** That's not a bad analogy, except you're using a text editor.

**Chris Gammell:** Right. Okay.

**Dave Jones:** Yeah. It's essentially just a configuration file. You have a bunch of nodes in there and leafs, and you have the I2C device. And, like, I have, at this address, I have this accelerometer. And it uses this pin for GPIO and this pin for reset. And so it's abstracted out very well.

**Chris Gammell:** And so, okay, so if there's a new device on the device tree like that, and it already knows how to talk to that because it's an I2C, or basically you don't have any user code yet, so it doesn't even matter. It just has to know that it's there.

**Jason Kridner And Robert:** The kernel knows how to talk to a lot of stuff that a lot of different types of devices, and you just have to tell them that it's there. Right. And then what it's going to look like, like, say you put a gyro on there or an accelerometer. Linux turns everything into files. Yes. So you'd have some virtual files that would have acceleration in the X, Y, and Z. And every time you want to know the acceleration in the X, Y, or Z, you just read those files.

**Chris Gammell:** Okay. That's cool. But the piece I guess I don't understand is, like, so I go to an accelerometer manufacturer website, right? And there's a bunch of registers there. Someone at some point had to write, that is the driver piece, right, where it's basically abstracting that register set and saying, you know, to get the reading in the X, it's at location, ABCD, whatever. And then it's going to push it into this file. That's what the driver's actually doing, right?

**Dave Jones:** Yeah. Correct. And there's a whole subsystem for that. It's called the IIO subsystem. And they got tons of accelerometers, gyros, tons of sensors. Really? Okay.

**Chris Gammell:** And just based on just shared knowledge over time?

**Dave Jones:** Exactly. I think it was originally written by analog devices because they wanted all their ADC devices to be well supported in the kernel. And over time, it's almost every single type of sensor has been pushed into the IIO.

**Jason Kridner And Robert:** So when somebody throws it on a phone or onto, you know, any sort of, you know, useful device, somebody's going to put a Linux kernel driver in there for it.

**Chris Gammell:** Oh, that's actually really nice. So I guess the reason that, I mean, because this, again, like the trends that I see is just this convergence. I mean, microcontrollers and, you know, Linux computers are, there's a whole lot of gray area these days. I mean, I know that the, what is it like the memory mapping is the, is that the difference these days for full-blown Linux or something like that?

**Jason Kridner And Robert:** You're talking about the memory management protection. Memory management, yeah. So there's, on, for full, full-blown Linux, there's usually, you're assuming the processor has a memory management unit, which, you know, ideally has protected memory, right? So there's a difference between the memory map for kernel mode versus user mode. And, you know, so that the user mode can't get to other user mode programs or to the memory for the kernel.

**Chris Gammell:** I can't overwrite, if my user program, I can't go overwrite the kernel's memory space and put it in the middle of nowhere, right?

**Jason Kridner And Robert:** Right. And for an embedded system, how much does that really matter? But, you know, are you really putting...

**Chris Gammell:** Well, I'm going to do it no matter what. So it's just about how hard I have to try, right? Right. I will put that processor in a bad place, no matter, no matter what. That is my promise to you.

**Jason Kridner And Robert:** Well, if you stay in user space, you'll be prevented from doing anything like that that would actually shut the system down in any meaningful way.

**Chris Gammell:** Okay. Okay. Okay. Cool. So that's good to know. So it sounds like the default is if you're running BeagleBoard distros, you probably have access to a whole crap load of peripherals and stuff like that, which is great. You just got to go mess with the device tree, like Robert was saying. But then you actually have to go and write code for either you're writing scripts like in Python or you're writing drivers if you don't already have the kernel drivers, right? Is there any other situations in there? Or is it just mostly scripting these days?

**Dave Jones:** Or the third, fixing a driver. Oh, well. Yeah. A lot of times there's drivers that are close or you have a new device. It has little tweaks that need to be made.

**Jason Kridner And Robert:** Yeah. I know that I ran into an OLED, a spy OLED that all the drivers were for like some Adafruit breakouts or some other breakouts that were different resolutions. So I had to read. I think there were like four or five different register settings that I had to actually change in the driver to get it to work at the micro electronica's 96 by 39 OLED.

**Chris Gammell:** And that's kind of like, so when I think about like writing like libraries for a microcontroller, that sounds like it's a very kind of crossover-y kind of thing with just more overhead for actually talking. Well, probably you're borrowing a lot of this, the code that's already there for interfacing back to the kernel. But like, it sounds like the same activity of like data sheet driver listing or register listing and then code that makes the part do what you want it to do.

**Dave Jones:** And it's a lot more structured too because you have so many other examples and so many other libraries inside the kernel that you have to deal with.

**Jason Kridner And Robert:** And if somebody wrote it for an all winner or, you know, the Raspberry Pi or whatnot, because it's all abstracted in Linux, we just use the code. Oh, really? Yeah, it just works. I mean, it's using the Spy driver, so it just works. Or, you know, yeah.

**Chris Gammell:** So it's like ad hoc standardization without the guarantee for standardization. Like as much as... Well, it's formalized standardization. It's got to work with the kernel, so that's what matters, huh?

**Jason Kridner And Robert:** Yeah, I mean, it's an established practice of collaboration, right? I mean, it's the most collaborative software project in the world. Well, I'm sorry, project in... I'm sorry, project... Most collaborative project in human existence.

**Chris Gammell:** Unless you're dealing with Linus and then you're... And then he's just angry.

**Jason Kridner And Robert:** But, you know, they're... Yeah. The Linux community as a whole is angry. It's just the joke. Just let that one go. Yeah. Let's just let that one go. All software developers in all walks of life are angry and... Grumpy. Grumpy in some way or another. Yeah.

**Chris Gammell:** I know. Hey, man, I'm an analog engineer. I've seen my share of grump.

**Dave Jones:** Yeah, but he hasn't yelled at the arm group for us in like six or seven years now. So we're good. You do.

**Chris Gammell:** You do, man. The arm people are good.

**Dave Jones:** Got it.

**Chris Gammell:** Okay. So I wanted to talk about the other stuff that's on there because this is the piece that I've been probably, you know, waiting 50 minutes to get into it. But I feel like this is the thing that, you know, I know Jason talks about a lot, but I don't think it's, it hasn't been highlighted on here enough, mostly because I don't know how to do anything with it, but there's the PRUs on there. So what are the PRUs? Is that my cue? Yeah. So they're... Evangelize, Jason. Evangelize.

**Jason Kridner And Robert:** They're 32-bit risk cores that are optimized for low latency. They're a zero-depth pipeline. So, you know, even something like a Cortex-M3 has a 3D pipeline. And so when you, they're ideally suited for creating software implementations of peripherals. So PRU stands for Programmable Real-Time Unit. And there's a whole subsystem around them. It's called the PRU ICSS or Industrial Control Subsystem. So it's... That sounds friendly. Yeah, isn't it? Got to love those TI acronyms. Yeah. Don't get me started on TI-15-4, but...

**Chris Gammell:** Whatever. Yeah.

**Jason Kridner And Robert:** Anyway, but it's an amazing little subsystem that can implement all sorts of industrial protocols, including such mundane protocols as, you know, RS-232s or, you know, UARTs, right? Right.

**Chris Gammell:** So that's the idea. It's like, it's spinning out there like a little widget that's just doing its thing, waiting for commands. You're not saying, go pull this thing. It's just sitting there doing the polling for you or doing the outputting for you or whatever. Exactly.

**Jason Kridner And Robert:** And some IO pins are actually register mapped and not even memory mapped, but actually, like in, I'm assuming I can talk like R30 and R31, you know, at that level of people's understanding of microcontrollers. But so one of the registers is actually directly mapped to the outputs and another one is directly mapped to the inputs. And so you can do XORing on a pin and you could actually do, there's, you know, zero overhead loops. So you could do, you know, read XOR right on registers in a zero overhead loop at 200 megahertz.

**Chris Gammell:** So it's like having like a, like having a logic gate pretty much right there, but it's all programmed, it's almost programmable logic, right?

**Jason Kridner And Robert:** Yeah. I mean, if, if what you want is, you know, a collection of XORs for some reason, yeah, you could, you could run a, you know, 200 megahertz XOR, right? So, you know, 10, 10, 10 nanoseconds, um, you know, from, from input to output, it's under 10 nanoseconds. It should be something probably more practically like six or seven nanoseconds.

**Chris Gammell:** That's yeah, that's pretty crazy. So, and, and like you're saying, like, so for the real time piece of like making it, so like reacting to system inputs or anything like that, it's yeah, it's just right there. It's already doing what you needed to do.

**Jason Kridner And Robert:** And, and you can just memory map them into the processor space to put the, so like the, um, so the, the, the arm processor can directly see the internal memory of the peer use. Um, and the peer use can write into the, um, the, let's call it L3, but like the, the, the on-chip peripherals, as well as the things like the, the DDR, right? So the peer use can actually write to the DDR and they can just.

**Chris Gammell:** Oh, for doing like a DMA type of thing?

**Jason Kridner And Robert:** Exactly. If you, you just, you know, if you want to do a, you know, pure software DMA, which is, uh, if you've heard of the, something, the Beagle logic project, it's a project that makes a 14 channel, a hundred mega sample per second logic analyzer. Um, it just, just using the peer use to do a soft DMA. Um, that's cool.

**Chris Gammell:** Yeah, that's great. And then like, uh, it uses SIG rock to, to actually analyze it, right? It does. Yeah. Yeah. Yeah. So it's a nice little, nice little system. Is that Kumar Abhishek doing that? That's the one.

**Jason Kridner And Robert:** Yeah.

**Chris Gammell:** That's cool. No, it's a cool project. I remember seeing that.

**Jason Kridner And Robert:** So, but it's, it's a nice example of just how fast the, the, the peer use are, um, you know, just doing it in software. You could do the same thing with like a DMA, but, uh, you know, it's just, you know, interesting

**Chris Gammell:** to.

**Chris Gammell:** More flexible, more recompilable. Yeah. So, and that, and that gets to my question about it. So how does one actually do this? Cause I remember looking at it at one point and being, seeing something about Code Composer Studio and going, nope. And go the other way. Is that proper?

**Jason Kridner And Robert:** We shipped the C compiler on the boards actually in Robert's images.

**Chris Gammell:** Okay. So maybe, maybe I'm getting this, maybe I got that wrong then.

**Jason Kridner And Robert:** So. No, no, at one point, at one point, that's what it was. Um, you know, we, we kind of had to, to show the, the, the kind of legacy of this is, you know, you know, TI was, um, I, I always say TI like a third person, like it, like I don't work there, but, um, it kind of the, the. It's like an older brother that beats you up sometimes. The, the, the approach was, okay. The peer use, something we're going to use for supporting these industrial protocols and we'll provide firmware and we're the only ones that can program it. And, oh my gosh, this is just way too complicated for the real world. And, you know, for, for the, the, the, you know, other people. And so the, the coup I got was, um, we took the, the, the, the chapter that was originally written for the technical reference manual that had been removed after being kind of reviewed by managers and saying, okay, this is going to be too much, um, technical support. We don't want to have it out there. Um, that's fair. And yeah. And, and published it separately, you know, from, you know, on a, a BeagleBoard GitHub that, um, this is, this is the, the base technical information and don't call TI. Um, you know, here's a forum. Don't go out there than the forum. Yeah, exactly. We're mailing lists probably, right? Yeah. Um, and you know, it's, you know, this, this doesn't really exist. If you come and ask questions, you know, we're going to say that, um, anyway, the, what happened was, um, the community loved it. They started making all sorts of cool things out of it. And, um, um, you know, it's heard, I think a lot of us heard with the, some of the folks doing 3d printers, um, some of the, the cool MakerBot guys, um, back when MakerBot was cool. Um, no comment. And, um, uh, you know, they started doing stuff with it, you know, Trammell Hudson did

**Chris Gammell:** some really cool lighting stuff.

**Jason Kridner And Robert:** Um, and, um, you know, he, he's anyway, people started writing cool code for it. And, you know, eventually the, you know, powers that be said, you know what? Um, this seems to be working out pretty well. And, um, you know, so now it's an officially supported peripheral inside the processor.

**Chris Gammell:** So the, so you said, Robert, you have this in your, in your build now. So what does that actually mean?

**Dave Jones:** Uh, we actually support two versions of it because one of the problems was it became so successful with the old 3.8 kernel images that we still have to support the old way people were accessing it.

**Chris Gammell:** Oh no, do you have like a Python 2 versus Python 3 thing or what?

**Dave Jones:** Yeah. More like a Python 1 versus Python 6. Okay. Completely rewritten. Got it. Okay. Uh, four times.

**Chris Gammell:** Oh my God. Really? Okay. So. Yeah. So the two versions are the 3.8 and something else.

**Dave Jones:** Yeah. 3.8 is the one that was the most used by almost everyone. There was a version in 3.14 that was slightly different than 4.1 was even different. 4.4 was different again. And 4.9, they changed things. Okay. So, yeah.

**Chris Gammell:** Which, which of the two? So if someone was going to start today, which should they use? I mean, that's a better example.

**Dave Jones:** Um, if you have a project that is based off something else that someone has already done a huge library for, use the old 3.8 version. Okay. And we support that through all the kernels. If it's something newer that there's some projects exist or Jason's ported in it, use a new version.

**Jason Kridner And Robert:** It's not that hard to move the code. Um, there was, there's, there's the two different drivers that people really talk about are the, so we're not talking about the C compilers, but the drivers that people are used to talk between the processors. One's called UIO and the other one's called, um, remote proc. Um, and I think that, you know, Robert, I may be speaking about the wrong thing, but I think that that's one of the, the, the biggest differences they see between the older and the newer interfaces is which driver they're using. Uh, the, the newer one, actually the kernel loads the firmware rather than the, your, like a user space application loading the firmware on the PRUs. And that's the only hard requirement. A lot of people think of a lot of other features that are in the newer driver to, to message between the two and, you know, do some, what they call remote proc messaging or RP message. Um, and, and that requires, you know, a little bit of firmware on the PRU itself and kind of some understanding, but you can just use the new loader and then memory map the PRU and use it all the same way you're using it before. Just, you know, dump into some shared memory location, but most people don't understand that, um, you can still do that. And so they, they, they make the problem harder than it really is.

**Chris Gammell:** So 3.8 is referring to the kernel number. Is that right?

**Jason Kridner And Robert:** Yeah, correct.

**Chris Gammell:** So yeah, it's still there. So what, I don't, I don't get how that can work then. So I guess this kind of goes back to that early conversation. Like, so you said that it's currently on 4.14, now 15 today, but what, how does it still work with the 3.8? I don't, I don't get it.

**Dave Jones:** Oh, we still support 3.8. People are so used up with old code.

**Chris Gammell:** But, but what does that actually like, so what does that actually mean though? Like, so does that mean that they are, they have foregone all updates or is it like everything got, all of the new stuff got backported to the old stuff?

**Dave Jones:** So one of the things we do, the repo is we allow you to choose basically any kernel that you want and we almost never remove it.

**Chris Gammell:** Oh, there's a problem.

**Dave Jones:** Well, on one side, you can have a, yeah. Well, we want to make sure our users, if they have something built and then, well, Jesse goes into life, so they have to move the stretch. They could move to a different OS and still have the same kernel. See, okay.

**Chris Gammell:** This has always been confusing to me, stuff too. So, so now you're talking about distributions too, right? So like, so I'm on stretch currently, that's stretches the newest Debian for stuff, right? It's the newest stable. Yeah. And on a Raspberry Pi, I remember it gave me a whole crap load of issues with wifi. I know that. But, so I switched back to Jesse and, but that has nothing to do with the kernel though. You're saying that that's completely detached from the kernel.

**Dave Jones:** It's completely detached. And why? So you can run Jesse, Weezy, a stretch or Sid all on the 3.8 kernel. Why? So that way you. Why?

**Chris Gammell:** Why is this possible? So what, I guess maybe a better question though is, is what breaks? What breaks when you, when you don't, so when you go from 3.8 to 4.9, what actually, is it just like all the interfaces have changed or the memory locations or what?

**Dave Jones:** A lot of things in 3.8 end up going mainline, but at the same time, lots of things changed on mainline.

**Chris Gammell:** Maybe I need to have mainline. Mainline needs to be defined too.

**Jason Kridner And Robert:** What breaks is very specific to what you're trying to do. I mean, it's, it's, it's, I always try to tell people try to get, do anything you can to stay on the latest and just run with the community.

**Chris Gammell:** I feel like I should be like channeling Dave right now. I mean, like right now, Dave would be like, why? This is why I only use Windows. And you know, that's my worst Australian accent ever, which is a load of crap too, right? Because they obviously deal with this stuff too, but it's just, you know, it's hidden from all of us, but like, damn, this is a lot of stuff guys. I mean, like.

**Dave Jones:** Well, then a lot of times too, is someone will build a project based off something and they have, they wrote all the kernel interfaces, all the tweaks, they got it working. And then three years later, they need to upgrade the OS, but they have everything tied to the one kernel. So now they can easily see what's upgraded the OS and still build their old kernel with all the interfaces and they keep on buying our board.

**Chris Gammell:** And, oh, that's a good thing. That's not a bad, I thought you were going into a bad thing there. Yeah, it's a great thing. That's a good thing. Okay.

**Dave Jones:** So while it's complex that we have so many kernels available, it allows end companies and end users to have a more stable kernel that it'll always be there. We don't have to worry about changing kernels if we don't want to.

**Chris Gammell:** So the, if you, if you wanted to keep the same kernel, right? So let's say 3.8 is just the best kernel ever. You want to keep that. Why are people updating the distros then? What do you get? That's not in the kernel?

**Dave Jones:** Well, they want, they want the latest VLC media player. They want open SSH patches.

**Chris Gammell:** They want, I guess heart bleed is kind of a thing. Apache upgrades. Yeah. Yeah. Okay. So security, security would be a big one, but UI and UX and all that crap too, right? They want to run Python 3. Whoa. Let's, let's take her easy there. Uh, yeah. The world's going to break at some point just because of, just because of the rift. And I've only learned about it lately. I don't even, yeah. I don't have a dog in the race. Uh, okay. So that's really interesting. So what would then lead someone to go from, so now this person's on 3.8, they love 3.8, they've updated through all these different distributions over time. They get all these pretty, pretty, pretty updates on the other side of things. What would make them change? Is it just a hardware change?

**Dave Jones:** The biggest change is, um, if they want to run the pocket vehicle or the new blue or the black wireless or the green wireless, they need to run a newer kernel for the newer, uh, interfaces like wireless. Oh. We didn't, we didn't back port support for the wireless chip in the 3.8.

**Chris Gammell:** Okay.

**Dave Jones:** It's like, and what 3.8 will support what it did. We'll keep supporting it, but we're not going to back port newer stuff to it. Right. Just because of the overhead and headache of doing all that, right?

**Jason Kridner And Robert:** If you want to do something like mesh networking, I think you need at least 4.9 to do the 802.11s mesh networking with the big one blue.

**Chris Gammell:** So it feels like, so it feels like the kernel stuff you're talking about. If you want, if you want new hardware support, you have to update the kernel. If you want new software support, you have to update the distro. Is that fair? Yeah.

**Dave Jones:** That's a big, that's a good, um, generalization of it. Yeah. Cause the way Debian works is that, um, they'll stabilize everything together so that it works as one unified package and then lock it down. And then two years later you get all the updates and you do it again. Right.

**Chris Gammell:** Yes. I, I also have servers and I've seen that. Uh, yeah.

**Dave Jones:** It's stable for a reason.

**Chris Gammell:** Nothing changes for two years. Yeah. The game of the game for me. Yeah. Five years, five year packages.

**Jason Kridner And Robert:** But newer software systems like ROS, you know, like these different framework packages and stuff for your newer versions of Node.js. Right. Python, you know, some of these things you start having, you start getting libraries to get too old or other systems to get too old and you kind of have to make the leap to the next. Right. Distro image, distro version.

**Chris Gammell:** All right. So we got a little bit away from it, but let's go back to the PRU real quick. So, so now on the device, there is a compiler that allows me to write code for a PRU. Is that correct? Correct. How do I do that? Just see. So, you know, so, so it's like, but I'm saying, is it like a make file and like, is it like

**Jason Kridner And Robert:** that style of things or, um, a gist that I always point people to. If you go to beagleboard.org slash PRU and ignore all the old stuff in the beginning, go all the way down to the bottom. Um, I mean, the old stuff is interesting and informative, which is why it's still kind of first. But, um, if you scroll all the way down to the bottom, there's a single set, like with the, it's got a make file, um, with way too much in it, um, that you don't need, but, um, it's got a link or command file with way too much stuff in it that you don't need. And it's got some essentially a, uh, hello world application, which is, you know, toggling some, some GPIOs, um, ones through the on-chip peripheral bus and ones through the IO pins directly on the, the, the, um, the peer use. To me, that's a good place to get started, right? It's, it's a, it's a.

**Chris Gammell:** No. Well, yes, yes and no. I mean, so again, I'm going to be honest to you guys. Uh, I, I usually don't compile with make files. Like I'll do it if I got every command in front of me and someone's written the code already and I'll just need to hit make. Uh, but I don't do that really. So that's what I'm saying is like, that's where I start to fumble. So I guess I need another pointer towards, uh, another thing that shows me to do that.

**Jason Kridner And Robert:** You need to specify a link or command file because the peer use, um, you don't load with like a relocatable, um, you know, a relocatable binary, which is what you, uh, so you need to actually give it a, um, a memory map that, that says, okay, these things hard load here into memory. Um, and other than that, you're, you're pretty much just, just compiling it normally. So, um, you know, we could strip out and give you the single command line. That's, um, um, but you still need a link or command file.

**Chris Gammell:** Well, I'm not saying that it's not, I'm not capable of, I can follow directions. I'm just saying that that's for someone like me, that's, that's, that's, it's a little outside my wheelhouse or at least comfort level. Right. I mean, and so, and you know, I've been doing this a long time. Uh, I've, I've been uncomfortable. I've done FPGA stuff. I've been uncomfortable. Uh, so I guess that's, that's what I'm really saying though. So that's, that's good to know though. So to get to the point where you want to use a PRU, you're going to be doing make files and all that stuff. You don't have to do make files.

**Jason Kridner And Robert:** I'll, I will give you the single command line. The, the, the only thing that's, that's kind of magic there is you need to specify a link or command file. Other than that, it's the same old stuff. You point to the include directory. Um, you, you, and.

**Chris Gammell:** So maybe I should step back even further. My experience is like IDEs. So like, that's what I, that's where I'm coming from. It's like IDE world. Right. So it's like, it's not that. And that's fine. Right. It's, it's fine. It's not. But I'm just saying that like, there's nothing out there that's like, well, this isn't an IDE. You're not going to have an IDE. Do you see the disconnect?

**Jason Kridner And Robert:** You know, it's, it's, it's ultimately it's a little hard to use Beagle without getting a little bit comfortable with the Linux command line.

**Chris Gammell:** I, I agree with that. And, uh, I think that's probably a good thing to do. Maybe, you know, someone needs to make a video course or maybe Chris will.

**Jason Kridner And Robert:** Well, we're about to make a whole video series. Um, so I say we, I actually mean, um, you know, beyond Webster and, and, uh, a group of people, there's a website called, uh, e dash a L e.org. And he's putting together a video series of, of, um, you know, training on getting started with Linux, including making some, um, uh, you know, some I squared C and SPI drivers. And, um, there's a whole series of, of really nice experts.

**Chris Gammell:** Um, well, I can say, I can say definitively that, you know, uh, you know, stodgy old programs that, you know, have, have improved quite a bit. Uh, having a video course can help a lot. So, KyCAD, that's a KyCAD reference, you know, uh, uh, but it does, I mean, it does help. Like, so just again, I, like, I think about it so much too, is like the, uh, it's like a momentum based thing, right? So it's like, I am from a momentum case, I am more than comfortable at least opening up a, you know, an IDE and being like, oh, okay. I've seen this kind of thing before. I can probably do this, but I see like the, the whole command line thing. And I'm like, eh, maybe not. Uh, okay, cool. So you follow these directions, you follow this, uh, this just for doing the coding, stuff like that. I guess, is it like just when, once you compile it, is it just up and running immediately?

**Jason Kridner And Robert:** So there's, you need to tell the kernel to load it. So you, you put the, the executables inside of lib firmware and you tell the kernel to load them and then it's running. Uh, and then when the kernel boots each time, it'll reload that firmware again and have it running.

**Chris Gammell:** Right. And so this is, and, and, and this is meant as like a, it's like a whirling dervish that's just writing, running code, reading, writing, doing whatever it needs to do. That's kind of what it's out there for.

**Jason Kridner And Robert:** It's, it's just totally, totally from the, from the main processor. Yeah.

**Chris Gammell:** So, so to actually get this in there then, so what is, so there's a compiler, so there's, there's a compiler sitting within the kernel and as well, that's also ready to do all this stuff. Like how does, how does that all work?

**Dave Jones:** So there's a compiler and user space from TI that we ship and that'll build a binary blob that the firmware loader will load into the PRU directly and it'll just basically run.

**Chris Gammell:** Okay.

**Dave Jones:** So it's all, yeah, the user space compiler will build it into a binary that just runs on the PRU.

**Chris Gammell:** Huh.

**Dave Jones:** There's more than one. Is that right? Yep. On this one, there is two. Okay. And I always got to think what chip it is because. Oh, this is the AM4 has four PRUs and the AM5 has four again. Okay.

**Chris Gammell:** Okay. And so this is, and we're saying this one, we're talking about the pocket beagle in this case.

**Dave Jones:** Yeah. I'm a pocket beagle. So, okay. So you have two PRUs to work with, so you can have two different binaries load and they just run independently.

**Chris Gammell:** And so, and so like when people are writing, so are there actual hardware drivers within there as well? Or is it just kind of like bit banging? So like, I think about it, one of the benefits of using a microcontroller is, or like a hard peripheral on a microcontroller is it kind of handles all that stuff that's out there, right? So there's a spy port, you write into a register, it shifts out those data, the data from that. Is this kind of taking that and saying, well, now you write the software to do the bit banging? Is that the idea?

**Dave Jones:** Exactly. You're writing the software to do your interfaces, to do your algorithms, to do what you need it to do. Okay.

**Chris Gammell:** And so it's, it's a general purpose. Right. So you lose some of the, the, the hands-off-ness of it, of a normal microcontroller, but you get the speed and whatever else you need to do.

**Dave Jones:** It's like you lose the specialization. Right.

**Chris Gammell:** But you can gain the flexibility, right?

**Dave Jones:** Exactly. Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** And that's where you can see so many unique things that people have done with it.

**Chris Gammell:** Well, so what are some of those things?

**Dave Jones:** Like the big ones with the 3D printer guys, when they're doing all the, the movement controls.

**Chris Gammell:** Oh, okay. So they're using like one of the four, the four PRU setups and doing like stepper controls? Exactly. Oh, wow.

**Dave Jones:** And then they got it tuned to what every instruction takes for how long. So they got, they know exactly how fast it is to move. Yeah.

**Chris Gammell:** Yeah. I remember I had a former coworker who was driving a huge ass, what are they called? Neo pixel display. And those have pretty finicky timing. And I remember he used, he liked using the PRUs for being able to shift out just the right precise timing on each, you know, each blip you needed to get to each, each individual pixel. And that was like a very good case of that too.

**Dave Jones:** Yeah. And then on Ken Sheriff's blog, he had an awesome case where he's using the PRU for that old computer for a network interface.

**Chris Gammell:** Oh, that's right. Yeah. Yeah. Okay. Network interface. That's crazy.

**Dave Jones:** It's like some archaic there's, you know, no one has this network controller again and he, he got it working.

**Chris Gammell:** Yeah. That's great. So, uh, I mean, so it sounds like, okay, so we were talking a little bit about the, um, the, the build process, is it starting to move towards, so is it just, that's it? That's all you get? Or is it, is it trying to, uh, did I remember you said something like there's going to be an interface on, on the Linux side that allows you to write the code there? Okay.

**Dave Jones:** So for the PRU, it's mostly about, uh, taking existing example, tweak it for what you need. Um, there's most of the time it's just a make file that you'd have to call to do it. Okay. And I know, I'm pretty sure in op source on our default images, we have a PRU software package folder. And I think a lot of the examples are in there. Oh, okay. It's been a while since I looked at those, but, and then otherwise we have our cloud nine IDE interface through the web browser that you can also access them through that. And, and so while it's not.

**Chris Gammell:** Sorry, what is, what is cloud nine?

**Dave Jones:** Cloud nine is just, uh, um, a web-based IDE that's now owned by Amazon. Um, it just allows, allows you to point and click and create files and a traditional IDE type environment, but through your web browser.

**Chris Gammell:** Oh, so I would be able to do that. So I could write, I could write code for the PRU and that thing now? Yep. Oh, okay.

**Dave Jones:** You can write, you can create text files. It supports multiple languages. Okay. I don't think there's a, uh, uh, semantic viewer for the PRU exactly, but like for C and Python, it'll show you interesting things as you type.

**Chris Gammell:** Oh, got it. Like just like the, the keyword highlighting stuff like that.

**Dave Jones:** Exactly. Okay. Function highlighting it.

**Chris Gammell:** Uh-huh. That's great. No, that's, that's actually really great. Okay. Uh, and I remember you said that the, there was going to be other, like kind of that gooey-fication of stuff, right? Yeah. Because that seems like, that seems like, uh, what that kind of is like the cloud nine idea.

**Dave Jones:** Uh, so for the, for the next generation for, we, we have the cloud, um, code red project integrated into the system now too.

**Chris Gammell:** Uh huh. And what is that?

**Dave Jones:** It has a lot of, it's basically like your Lego blocks where you can move modules around, connect them up, um, where each module does something different. So just, um, picking a web server, opening a file. Okay.

**Chris Gammell:** And so just kind of like. Nice drag and drop interface. Yeah. Like wiring it together kind of. And exactly. That's friendly. Uh, is it, can you do like actual interesting things with that? Or is it more just kind of simplicity for getting things started?

**Dave Jones:** Uh, we just integrated a package for talking to the IO directly. So you can move, uh, pins up and down, pull ups, pull downs. You can talk to serial ports, can interfaces, ethernet ports, ADCs.

**Chris Gammell:** So, so this is kind of building on that, the, the Linux kernel kind of access side of things. Is that right?

**Dave Jones:** Exactly. And it's going through Node.js. So there's a lot of power in there.

**Chris Gammell:** Uh, what, what is it doing? Sorry. I don't, I don't quite understand. Like, so it's using Node to like write to the kernel. Is that right?

**Dave Jones:** Uh, it's using Node.js to, um, make the GUI and it's basically just running JavaScript behind the scheme.

**Chris Gammell:** Okay. Okay. So, oh, I see. So there's a graphical element that then is paired with some kind of JavaScript, which then is what?

**Dave Jones:** Reached into your, through your browser. Okay.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** And then Node.js is very powerful and on servers and embedded systems allows you to do a lot of fun things.

**Chris Gammell:** Yeah. So I've heard about, I mean, I've done a little bit of stuff with it before, like at least used other people's code at least. And I know that like it's server and client. That's the thing I always hear. Uh, but like, so it's, I get that like you. You have those, the duopoly of like two things talking to each other, but like then on the server side, it must be talking down to the hardware, right?

**Speaker ?:** Yep.

**Dave Jones:** So how, so it has, it has hardware abstractions in there for different devices. Okay.

**Chris Gammell:** For IO. So the same thing of just like, it, it got compiled for whatever system it's on as well.

**Dave Jones:** And yeah, it got compiled native for what it's run, but, uh, otherwise it's, it's just running JavaScript on, in, on the outside.

**Chris Gammell:** Okay. Well, that's pretty cool. Um, I mean, now that I can write JavaScript either, but like it's nice that it's accessible. So that's, that's cool. Uh, yeah, that's great. So, uh, what, I'm sorry, I'm a little thrown off now. Uh, back to the PRUs. Yeah. Back to the PRUs.

**Dave Jones:** Back to the make files.

**Chris Gammell:** Right. Well, yeah, I guess so.

**Dave Jones:** And a lot of times for a lot of them, um, like the machine kit guys, they had a PRU library they kind of built and set up so that anyone that wanted to make a 3d printer, they just ran the binary and sent the right commands to it. And they never actually had to rebuild the PRU binary.

**Chris Gammell:** So the PRU, I mean, like more and more of this sounds to me like a, like a logic element, right? Like you make, essentially, you make the thing once and then you just kind of use the interface to it. You don't do anything else.

**Dave Jones:** Exactly.

**Chris Gammell:** Interesting.

**Dave Jones:** And for them, it was, it was basically they created a stepper element.

**Chris Gammell:** Uh huh. And then they would send like an API, like to, it acts like an API and you say, move to position XYZ and it just does it. Or, or I guess. Yep.

**Dave Jones:** They just gave it incremental, like move this. Yeah. Move this. And yeah, they had a big, uh, what's it called? Their hardware extraction layer where they just, they separate the PRU from the hardware that way they moved towards other boards and like.

**Chris Gammell:** Oh, that's a good idea. Right.

**Dave Jones:** And they also relied on the real time curl to take advantage of a lot of the, the, the accuracy of.

**Chris Gammell:** Yeah. Like the super micro stepping stuff and all that stuff they do. Right.

**Dave Jones:** Yeah. Cause you want to have a, when you have a laser printer, you pretty much want to make sure it gets to where it's supposed to go when it's supposed to go.

**Chris Gammell:** Well, you know, only if you want it to look like you want to print, you know?

**Dave Jones:** Yeah. But of course some of the machines, these guys are working like, you know, plasma torch and you want it to go where it's supposed to go when it's supposed to go.

**Chris Gammell:** Right. Right. Only if you want fingers. Yeah.

**Dave Jones:** Or if you don't want a hole in your wall. Right. Right. Exactly. It's sick or too long with the torch. Right.

**Chris Gammell:** Right. So, okay. So, so as I may have mentioned on the show, and I think, I think you and I have emailed about too, and Jason as well, who had to drop off here for a second. Um, the, I am actually working on a cape now. Right. So whatever we're on, pocket capes, is that the right term?

**Dave Jones:** Uh, I'll let you know tomorrow.

**Chris Gammell:** Okay. It changes weekly.

**Dave Jones:** Oh, okay.

**Chris Gammell:** Because we've already had them as big bone capes. And then before that they were, uh, yeah. Okay. So tiny, tiny board that plugs another tiny board. Uh, okay. So if I was going to interface with that thing then, right. Cause I'm only at the layer where it's just now starting to talk. So I'm talking to the serial port on that thing. I'm just going to have you troubleshoot my problem live on the radio here on the podcast.

**Dave Jones:** Sounds good. Great. Okay. So make sure the ground's connected to the serial. Yes. Thank you. RX and TX won't transmit if there's no ground linking them. Right.

**Chris Gammell:** Well, this is actually going to plug right on. So all the grounds are hooked up. I guarantee that. Oh, then you're set. You won't have to worry about that. Exactly. Well, RX and TX being backwards. I mean, you got to, you got to do that once. I think the only reason this is actually going to work is because I actually swapped RX and TX twice on the board by accident. Uh, so, you know.

**Dave Jones:** So you have, you have two jumpers set up to reverse them every time now.

**Chris Gammell:** Yeah. Yeah. Um, you know how it goes. It's a prototype. Yeah. Uh, so, okay. So I'm going to write to the serial port, serial port four, I think on the Beagle, pocket Beagle. So, um, I'm going to, uh, write to that. So I should just do that with Python then? Or, or should I take that down into the PRU? Or what should I do there?

**Dave Jones:** Um, whatever language you want to. Um, by default, um, most of the UARTs are set up, um, let's see, uh, UART four. I'm going to find the schematic again.

**Chris Gammell:** Okay.

**Dave Jones:** Um, so if in our table that we created that, uh, ship of every board, if it says UART out of the box, it will be a UART. If it's not a UART or spy or something else, you have to use the config pin tool to change that peripheral to a UART.

**Chris Gammell:** Config pin tool. Okay. That's good.

**Dave Jones:** So we have a tool that's in user space. It's called config pin. It allows you to change the pin mucks of every pin on the pocket beagle. Really?

**Chris Gammell:** Oh, I didn't actually know about that. That's good to know.

**Dave Jones:** Yeah. Cause one of the limitations of kernel drivers is that you, you enable a peripheral and set it up for a pin. It's locked in that mode.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** And so we have our own big patch that kind of undoes that where we have a default mode and then, well, say you want to change to something else. Well, we allow you to do that.

**Chris Gammell:** And, and you're not saying any pin. You're saying like the predefined pins of where you see the pin outs and you, there's different there's like eight or nine functions per pin, right? Yeah, exactly. So it's not like a cross hatch where you can make any pin into anything else.

**Dave Jones:** Yeah. We're not moving pins around. It's each pin has about eight functions and we allow you to individually change them.

**Chris Gammell:** Okay.

**Dave Jones:** That's great. No, that's, that's actually really useful. So that's one of the questions a lot of people end up running. It's like, I want to use this UART. So the first thing is make sure it's actually in UART mode. Aha. Okay. And then once it's UART mode, just talk to it through dev TTY. In your case, UART four would be O4 or S4.

**Chris Gammell:** Huh. Okay.

**Dave Jones:** And this talk to us through Python through the UART library.

**Chris Gammell:** Okay. That sounds pretty simple then. That's what a great test case. I will just send you my code. You can help me troubleshoot it. Great. Awesome.

**Dave Jones:** And one of the crazy things you could actually do with this config pin library is you could actually hook up a UART and I squared C or spy to the same pin. Put it in UART mode. Talk to the UART device. Put it back to spy mode. Talk to the spy device.

**Chris Gammell:** Really? That sounds like a bad idea. Doesn't it?

**Dave Jones:** That was kind of, it's a bad idea. Yeah. Yeah. But that's kind of the idea that went, let's try this and do this. Yeah. And it works. So that's the way it's wired.

**Chris Gammell:** I mean, I guess it's just to a, if you send like a serial command to an I squared C, you're not going to have as many pins. Well, you might have as many pins, but it's just going to look like garbage, right? So. Yes. It looks like garbage. Yeah. So that's the idea is as long as your part doesn't care. And normally no one would ever do that. Right. As long as it, you know, your part doesn't have a self-destruct mode when it sees like bad data, you're probably okay. Right. Yeah.

**Dave Jones:** And so that's the way the Configure Pin was rich. And it's like, well, all the profiles are enabled and we have control of all the pin functions at the end. So leave them enabled and just change it on the fly.

**Chris Gammell:** That sounds kind of, yeah. That, yeah. I mean, I feel like I'd like a million monkeys on a million typewriters kind of problem. Like if you send the right, if you send the right bit patterns enough times, you might put it in a bad state. Like a, yeah. But okay. But you could.

**Dave Jones:** But for new users, it's kind of nice because they don't have to recompile the device tree or configuration or change anything. They just log into the user space. Oh, a Config Pin, I want to pull up here.

**Chris Gammell:** That is, that is actually pretty nice. Okay, cool. I also assume that would be a big headache, but. Yeah, it's a huge headache. Right. Okay. But is there a, is there a way to visualize what it's actually set as right now? Is it just like you can go do a display of what's actually set to what?

**Dave Jones:** Yeah, Config Pin has like a list and a query. You can do a list for all the options for every pin.

**Chris Gammell:** Okay.

**Dave Jones:** And it has a queue, which for query tells you what mode it's in.

**Chris Gammell:** Okay.

**Dave Jones:** One of the problems is when it's in the default mode, it'll actually say default. And then you have to look at the device tree. Oh, a default for this pin meant your.

**Chris Gammell:** Got it. Okay. Well, you can look at the pin out for the main pin diagram, right? That's like the default.

**Dave Jones:** Yeah.

**Chris Gammell:** So it's not 99% useful. It'll get you mostly there. I mean, if I'm, if I've got, you know, RX and TX going to the right pins on the right part of the processor, I'm usually doing pretty good. So. Yeah. Okay.

**Dave Jones:** So just to make sure they're in the right mode and then basically use any, any UART library. Any UART library. Yep. Whether it's Python or Node.js or C. Interesting.

**Chris Gammell:** Okay. So I guess I'm still stuck on this piece. So if I was going to write, so I get the Python piece now, right? So that's running basically a script on the device, right? It's just going and it's basically doing what you're talking about. It's like writing to a file or, you know, pulling from a file or, you know, manipulating strings in memory or whatever. Right. That's, that's what I get. Because you're just, you're just opening a file and then you're just sending data to it and pull data from it. Yeah. That, that makes sense to me. I, I, I'm, I finally got my head around that with the, like moving into the Python world. That's great. The thing that, so you're saying writing C though. So if I was going to write C for this, then what? I, I do the same thing where I, I compile it down and put it in the right memory space or I guess that that's the piece I don't understand. Cause like, again, because my flow has always been like an IDE where it gets, you know, executable at the end. You'd go and load that on your part and then it's got, you know, stuff to do things, you know? Yep.

**Dave Jones:** Well, in C, you're just going to, you're basically going to F open the file because it's still a folder in a file. Right. And so in C, you're going to open it up, set up the right, uh, uh, IO values for control registers.

**Chris Gammell:** But again, I guess the piece I don't understand is like, where is that? I mean, I know that this is happening for the other languages behind the scenes.

**Dave Jones:** So like. It's behind the scenes of Linux. Right. And so the Linux driver and the kernel is taking care of all the low level stuff. And so it has a unified API that everyone else just using to talk to the UR. Right.

**Chris Gammell:** But like, so now the user code, if I'm writing the user code in C and it's getting compiled down, where is that going?

**Dave Jones:** Yeah. It's just using the regular library. And then.

**Chris Gammell:** It's using the regular library. Yeah.

**Dave Jones:** But just basically running on target as is like a regular application. Huh. It doesn't need to know, um, what processor you're on or what architecture. That's crazy. It's just generic C for talking to a serial port in Linux. And so if you have it working on an x86 desktop. I know. That same application will work rebuilt on ARM.

**Chris Gammell:** See, I think, I think what this all brings, brings to a point for me is just how little I understand computers. Like, you know, like the full blown computer thing. Like I'm getting more comfortable over time with microcontrollers, but damn, there's just so much going on with computers.

**Dave Jones:** Yep. There's so many abstractions going on and it hides all the hard stuff from you.

**Chris Gammell:** Right. I think I'd rather see the hard stuff at a certain point, you know, it's like, I'd just rather get in there and, you know, peek and poke at some registers.

**Dave Jones:** And we tell people, you can do that if you want, but it's, it's hard to maintain and hard to move forward. I mean, you can make an application that it's poking a bunch of stuff, but then a couple of years down the road, how do you move it to the new OS or the new changes? Right.

**Chris Gammell:** Right. You're stuck. And, well, I think the other thing that, you know, we were talking about before too, is the portability and sorry, the distributed, distributed nature of it all. Right. So like I might be able to get it to work, but it doesn't mean if I sent you the code, you'd be able to get it to work because we might be on different systems. We might, you know, have different stuff going on, whatever. Like that's, that's the piece I think where that's the real power that comes in. Obviously there's, you know, there's, it's never going to be purely, uh, you know, it's not going to work on everything, but it's going to work on some things and, or it's going to be close to work on most. Yeah. Right. Right. Which is, that's really cool. And you don't hear about that much. I don't hear about that much at least, uh, you know, like, you know, you hear about like, oh, like modularity and all this stuff and like, oh, wouldn't it be great if everything works together, but it's kind of already there sort of, you know? So yeah. That's great.

**Dave Jones:** And the, and of course the way that Linux usually works too, is if a serial program that was built like 10 years ago worked, you can rebuild it today and usually it'll work again too. Right.

**Chris Gammell:** That is, that is actually really, yeah, that is true. I think that people underestimate the, that piece of it.

**Dave Jones:** Yeah. That was what, that's one of the big goals of Linus was that we're not going to break user space applications. It might be a bad API at one point, but you know, we'll change all the kernel code all the time, but we're not going to break people's applications on the end. And has that delivered or no?

**Chris Gammell:** It's pretty much delivered. Okay. That's good. That's good. Like, like I said, Jason, unfortunately had to drop off, but I did, I did have some questions about like just the future. Like what is, what is the future of the project? I, I, you know, you're a board member, you know, this stuff too. Like where, where's this all going?

**Dave Jones:** I think we're just going to keep on getting smaller and smaller devices that are getting more and more powerful.

**Chris Gammell:** Really? Okay.

**Dave Jones:** If you look at where we've headed, you know, the original Beagle was a 600 megahertz chip, then yay big. That's good.

**Chris Gammell:** That's good.

**Chris Gammell:** I mean, I think cheaper helps too. I mean, like obviously having, having like, so I've, I've, I've talked to people, like I said, in the industrial space, I think that, you know, making, making Linux more available in terms of just the UI and, you know, people just expect UI these days. But yeah.

**Dave Jones:** You gotta remember Linux is just the kernel. It's not the, it's not the GUI. Right.

**Chris Gammell:** But it enables more people to develop code and UI elements for it, right?

**Dave Jones:** Yeah. Because there'll always be something else on top to show the GUI, whether that's Wayland, whether that's X or whatever, the next generation, whatever comes out.

**Chris Gammell:** I don't know any of those things, but I guess these are, is it like QT and WX and stuff like that too? Or is that what X is? I guess X windows. Yeah.

**Dave Jones:** Yeah. X is your standard X windows. Wayland is what everyone's thinking that will replace X someday. Got it.

**Chris Gammell:** Okay.

**Dave Jones:** But a lot of the times for a lot of our embedded systems, we don't actually have a display to work with. Oh really?

**Chris Gammell:** Okay.

**Dave Jones:** It's like on the Pocket Beagle, you want to have a display on there. You have to connect a SPI or an I2C. That's where having like a display, like an embedded web server makes more sense with Node.js. Because you don't have a GUI on the Pocket Beagle, but yet you can log into it on the web server and create your own GUI through the browser. Right.

**Chris Gammell:** Right. Right.

**Dave Jones:** Right. Right.

**Chris Gammell:** And that's actually how, that took me a while. So I was following Ken's tutorial. And at first I was like, where the hell? And so like you plug it in, it shows up as a network device, like through USB, which is cool. It shows up like an Ethernet port, like a virtual Ethernet port. That's cool. And I was like, now what? What do I do? And I was like, oh yeah, it's like a web page. Okay. That makes sense.

**Dave Jones:** And you just log into it and then magically, wait, where does ID come from? Right.

**Chris Gammell:** Right.

**Dave Jones:** It's like it was in there the whole time hiding.

**Chris Gammell:** Right. Exactly. It's like a whole package of stuff. So actually that's a, that's a good segue too. So if I want it, so I think one of the things I was struggling with, and I think Ken mentions this in his tutorial too, is like, so there's no wifi, there's no connectivity on it at all actually, on the Pocket Beagle specifically. So doing updates and stuff like that is a little problematic.

**Dave Jones:** So yeah, on the Pocket Beagle, there is no Ethernet port by default. There's no wifi by default. There's no, there's nothing to get out of the, by default. Right.

**Chris Gammell:** Absolute low cost. Right. Yeah.

**Dave Jones:** So what we have set up is it's an Ethernet gadget and it was kind of intended where you'd plug it in and then you can talk point to point. And the problems exist is what OS are you running and how do you have your network set up? Okay. And there's some things we can't detect. We can't say, oh, you're running Mac. Oh, do this option. You're running Windows. Do this option. You're running Linux. Do this option. And so there's a, there's a little bit of setup that everyone has to do based on their systems. I know for Windows and ICS, all you have to do, if you use the serial port instead of the Ethernet port, if you just have DH client and then USB zero, it should connect in and your ICS will work. On Linux, you just have to do SRoute. And then I still have a plugin to my Mac, so I can't tell you how to do that one, but Jason could. Okay.

**Chris Gammell:** All right. So, so the idea is just, but it's just sharing. So I, on a host computer, I'm sharing the network. Exactly.

**Dave Jones:** You're just sharing the network and then you got to forward the gateway. Usually we just throw 888 for Google's DNS and then things magically start working.

**Chris Gammell:** Okay. Well, that's good. Yeah. I mean, I guess the main thing that I think about is that usually anytime I get a new distro, I mean, I know that this is not necessarily the case if I'm downloading the latest image and burning it to an SD and putting it in the thing. But like in the normal case, I would think it's like, I want to go and update and get all the security patches and whatever I want to do. Right.

**Dave Jones:** Yeah. And one of the things we do is all images do that by default. When you plug it in, you'll have three USB drives show up. You'll have a USB flash, which used to have the driver's windows before we figured out a way to around that. It has some documentation and some links. It has a USB serial port so you can log in as a serial and then the USB ethernet.

**Chris Gammell:** And that's all through the same micro USB.

**Dave Jones:** Yep. All through the same micro. And we've kept that going for like five or six years. That's been the default. Those three interfaces will always show up.

**Chris Gammell:** That's great. And then how much of the file system is actually visible via the USB flash?

**Dave Jones:** See, the USB flash is actually a fake image. Okay. There's actually an image file on the drive that we point to it. So you're actually looking at like a 32 megabyte image file.

**Chris Gammell:** Is it just like a transfer area or what is it for? Is it just for the...

**Dave Jones:** It was just for documentations and for Windows drivers back when we needed Windows drivers.

**Chris Gammell:** Oh, I get it. Okay. Okay.

**Dave Jones:** Yeah. We had one of our buddies that's done a lot for the organization, David. He figured out a couple of magic strings that we'd shove into the USB driver. Then Windows would, hey, this is registered.

**Chris Gammell:** Oh, nice. Okay.

**Dave Jones:** You don't have to have a key and a license to hack for Windows drivers. So... Hack it. Yes. We've since moved to that. And he pushed it all mainline. Here's the magic code you need for this driver to... For Windows to detect an RDNS driver. Nice.

**Chris Gammell:** Okay.

**Dave Jones:** Sadly, it doesn't work on Mac.

**Chris Gammell:** That's...

**Dave Jones:** I'm finding that...

**Chris Gammell:** I've been through some struggles lately. So yeah, I know how that goes.

**Dave Jones:** But so if you plug in the Pocket Beagle to a Linux OS, you're like, why is there two Ethernet ports? Well, turns out Mac recognizes one, Windows recognizes the other. Oh, really? Okay. All right.

**Chris Gammell:** So Linux people get both. Okay. So the idea though is, so there's that Ethernet and basically I just have to pass, I just have to time my Ethernet to that, my host Ethernet to that device Ethernet.

**Dave Jones:** Yeah. And the way we have it set up is the Pocket Beagle is actually a DHCP client. So when you plug it in, it'll tell the other PC and it'll give it an IP address. So the IP should, in like 95% of the cases, come up. And then you should be able to at least IP talk to each other. Then it's mostly just talking about changing the routing and set up the gateway.

**Chris Gammell:** Cool.

**Dave Jones:** But yeah, that would be a nice project if we could figure out, hey, we have a Windows. ICS is enabled. Do this by default.

**Chris Gammell:** What are you saying? What is ICS? Sorry.

**Dave Jones:** Internet connection sharing.

**Chris Gammell:** Okay.

**Dave Jones:** So in the Windows world, it's how they do it to share Internet.

**Chris Gammell:** Okay.

**Dave Jones:** So it'd be a nice project if someone to figure out, hey, figure a way to detect that by just plugging the USB port in.

**Chris Gammell:** Yeah. Yeah. That would be really nice. Yeah. If it's just, I mean, that's the thing. Like the magic of it just works is really nice. And it's really hard. It's really hard. Yeah, exactly. So one thing that I've realized is that I value time more than money these days. And one thing, so like, okay, so I was going through this whole thing with the HackRF, which is a great little device. But like, it was a shit show to get it set up, to be honest. I mean, like, I love it. And I got it finally. But it was a shit show. And it was because, though, it was because I was just not doing what most people do, right? Most people are like, well, I've got a Linux box. Let's plug it into that, right? I don't have that. I'm traveling with a Mac for work, and that's all I got. So I had to struggle with that. If someone was going to, best case scenario for them, what should they plug it into? Should they have a Linux box?

**Dave Jones:** For this board, right now, set up any of the three is fine.

**Chris Gammell:** But give me a best case. I mean, I agree that, like, usually that is the case. But, like, there's always a best case.

**Dave Jones:** Yeah. To get, if you just want a network set up where you can talk to point to point, the Linux is about the easiest right now. Okay. For getting it to the internet, if you already have Windows ICS enabled, it's only one command you have to do on the Pocket Beagle to get it connected. Okay. Whereas on Linux, it's like two commands.

**Chris Gammell:** That's what we're down to. Okay. It's like, how much do you really want to type? Yeah, well, you know. Sounds like I'm going to be doing it either way. So, okay. That's good to know, though. And I think, I mean, like, that's the other thing that's amazing about this price point, too. Now, again, this is within the realm of the, you know, the Pi Zero and the Raspberry Pi and stuff like that, too. But for the BeagleBone project, BeagleBoard project, right? This is the lowest price one yet. And so if people want to try this stuff out, and like I said, if you want to be able to put the damn chip anywhere else, you're just not going to do that with a Raspberry Pi. Even, you know, you might be able to buy a module or a memory or whatever they call those things, the compute modules. That's fine. But I'm saying if you want to put a chip on a board, this is the way forward, I think.

**Dave Jones:** Yep. And build your project around it.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** And we've done it before where people have made small changes and, you know, here's the 10-line kernel patch I need. Like, oh, I'll take it. And we just put it out in our default distro so their stuff is supported out of the box.

**Chris Gammell:** That's great. That's really great. Yeah. So I think that, like, that's – and so, like, this whole Pocket Beagle, the reason I'm so excited about it, because it's redesignable easily. It's cheap. And, yeah, I think that getting started is, you know, it's a little bit bumpy still. But I think it's – I mean, this thing only came out, what, like three or four months ago?

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** And it's kind of amazing to see all the new Pocket Beagles that have come out as far as – so they've taken the design, tweaked it here. I mean, it's – with the easier layout tools of Eagle and KiCad, it's – people have made derivatives a lot easier. Yeah.

**Chris Gammell:** Yeah. I mean, like, yeah. I thought – so I made a little cape thingy to plug in board, whatever. And, yeah, I just – I mean, like, even just grabbing the header, you know, like, there's no way you can be wrong – well, you can be wrong. But it's hard – it's a lot harder to be wrong when you're starting from the actual design files. And I just literally took the design files, ripped out all the other crap, and just kept the headers and the outline. It's like, well, not going to mess that up. You know, at least I know that I'm starting from that point, which is, you know, if you get that wrong, it's a bad – that's a bad day to start with, right? Yep. You know, jumping and cutting on your – on the connector side of things.

**Dave Jones:** And I think, like, a week or – a couple weeks after it was launched, there was already boards showing up on Tindy. It's like, well, I want USB. Here's my four-port hub design. Oh, nice. And so there's already mods being done on it. Right.

**Chris Gammell:** Well, there's money to be had, you know? Like, that's the thing. Like, that's – I am amazed by the low-cost – like, the low-cost ecosystems that pop up, right? Like, you know, Pi Zero, the Pocket Beagle, the ESP, just all the stuff around ESP. You know? It's just that – I mean, it's not always clean, and it's not easy, but damn, does it enable new things, you know?

**Dave Jones:** Yeah, especially, like, when the ESP first came out. It was kind of amazing, all the little hacks they were doing. Right. It's like, oh, then we've got a whole library to use now. Exactly. We can do everything. Now it runs a little. It's a couple hacks.

**Chris Gammell:** Right. It's like, how? But it's great. I mean, it's really great. I mean, that is the collaborative, internet-y thing, because people want to do more stuff with it, right? So, that's awesome.

**Dave Jones:** And what we try to do, especially with the foundation of the org, is that if people start doing cool things, we try to pull in their projects, their libraries, into the default image. It's like, this is awesome what you're doing. We want to show it by default.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** And that's one of the things that happened in the Node-RED, is we've been shipping Node-RED for a while. Someone made this awesome module. We're talking to the IELTS. Like, oh, we do that by default now, too. Nice. So, we pull it in and share it with everyone.

**Chris Gammell:** Well, and you keep talking about pulling this stuff in, too. So, is there a cost to it, in terms of just bits? I mean, or how much cost?

**Dave Jones:** For the longest time, our cost was it had to fit in two gigs of EMMC. Okay. And then we had four gig problem.

**Chris Gammell:** Okay.

**Dave Jones:** But now, with the Pocket Beagle, well, we're not going to run Xorg or Wayland, because we don't have a real display to connect to by default. So, we can shove more in and still fit in that four gig target.

**Chris Gammell:** Oh, so you're just saying because there's fewer peripherals, taking up that base space.

**Dave Jones:** Well, like Xorg in any GUI interface is big. Oh, I see. So, if we drop the GUI, our four gig images, we can fit a lot of other tools in there.

**Chris Gammell:** Okay.

**Dave Jones:** And then ship it. What is the four gig? Why is it four gigs? So, the BeagleBone Revision C is a four gig EMMC. And so, we kind of put that as the max size we'll ever make an image.

**Chris Gammell:** Okay. Which seems doable, right? Yeah. Have you run into it or no?

**Dave Jones:** Yeah, we can fill it up pretty fast. Okay. If we really wanted to. Okay. If we put every library that was ever created, yeah.

**Chris Gammell:** Okay. So, there is some cost to it, but you're saying that because these images for the Pocket Beagle, there's just more space to start with. So, what's a why not right now? Yep. Is there a process later to be like, well, we got to get rid of this thing?

**Dave Jones:** Well, the process is, does it still work?

**Chris Gammell:** Oh, okay. So, they kind of age out on their own.

**Dave Jones:** Yeah, kind of age out. Like, we've had a couple libraries that were tied to the 3.8 kernel that we don't use way to fault anymore. And it was only tied to that kernel. Got it. Interesting. And a lot of times, too, they're implemented in other softwares. Like, well, you just use this library instead.

**Chris Gammell:** Like, the functionality was done elsewhere?

**Dave Jones:** Yeah, it was a similar functionality. It just was a different name.

**Chris Gammell:** Oh, okay. Okay. So, to talk to a similar peripheral or something like that?

**Dave Jones:** Yep.

**Chris Gammell:** Okay.

**Dave Jones:** In this case, it was talking to the PRU in that version. Like, we had a better way to do it, so.

**Chris Gammell:** Okay. Yeah. Well, okay. So, you're at DigiKey, right? Yep. So, are you seeing people, I mean, not that you're, like, watching this like a hawk, but, I mean, y'all do sell these chips, right? So, like, obviously, people can go and buy these and plop them onto boards as well, right?

**Dave Jones:** Yep. And I see it from both sides. Like, it's like, buy this chip. They've already spun a board. Like, we have a problem. We can't get this talking. Like, so, I see on the debug side of the first couple PCB designs. Oh, interesting. Okay. It's like, we want to do this bring up. And that's why I see a lot of that. They get to you, huh? Yep. Right. Oh, yeah. Maybe we should say what you do at DigiKey, huh? Yeah. So, I'm an applications engineer there, and I just basically support customers.

**Chris Gammell:** Right. So, this kind of, like, is a merging of all your loves, huh? This is. Yep. Yep.

**Dave Jones:** It's like, I get to go home and play with what I do and go to work and do what I like to do.

**Chris Gammell:** Oh, man.

**Dave Jones:** It's kind of hard to separate work from home some days.

**Chris Gammell:** I know the feeling.

**Dave Jones:** The only difference is at home, I have more build farms. Right. So, what does a build farm look like for you? Oh, right now, it's 20 BeagleBone Blacks, about seven wand boards, six X-15s. What? Yeah.

**Chris Gammell:** What are you doing? You're just like, so are these, like, all just networks and just kind of kick them off and they do their thing or what?

**Dave Jones:** Well, the main thing that they're doing is, so, yeah, we haven't talked about it yet, but we do weekly images. So, when you go to BeagleBoard.org, it'll say latest image. It'll say, like, three months ago. Behind the scenes, we do it weekly.

**Chris Gammell:** Is that to do, like, is that, like, a continuous integration type thing or what?

**Dave Jones:** Exactly. We're doing continuous integration. We're doing kernel builds. So, we usually do two or three kernel builds a week per version. So, we get updates that come in from other customers, other users, from TI, and we just keep on integrating the kernel, all the package updates, and, yeah, lots of testing.

**Chris Gammell:** Is this really just that you're heating your house with all these, you know, small computers that are just crunching code all day? Is that the real plan here?

**Dave Jones:** No, that's what the crypto miners are for.

**Chris Gammell:** Right. I did hear someone talking about that. They're like, you know, I heat my house with electricity anyway, so why the hell not? You know, it's like, yeah. Exactly. Yeah.

**Dave Jones:** Well, when you live in the Northland, you know. Yeah. You've got to get warm somehow. When you have to open the window in the Northland to cool your systems in the winter.

**Chris Gammell:** Wait, seriously?

**Dave Jones:** Yeah. No.

**Chris Gammell:** The basement gets hot here. Holy crap. That's amazing. So, you aren't running, like, a cooling system up to the rest of the house or what? No, I just opened the window. But, I mean, like, why don't you use that heat?

**Dave Jones:** Like, you're paying for gas or no? Yeah, I pay for gas, but it's already heating up the house, but it's overheating the house. Whoa.

**Chris Gammell:** That's amazing. Wow. Oh, computing power, huh? Okay. So, what, I guess, what actually, like, determines, like, do you have a suite of tests then? How do you actually know if an image is good?

**Dave Jones:** So, one of the things that we do is long-term stability. We want to see how long a board will stay up, whether it's doing a load test or Wi-Fi. We want to make sure that even after a week that it's still up. Uh-huh. Because that's one of the things that we've always run into, that if it reboots before a week, there's something seriously wrong. If we usually get at least a week out of it, we know that when the end user gets it, it's going to last for days on end.

**Chris Gammell:** Right, right. So, it's like a bathtub curve kind of thing, right? It's like... Yeah.

**Dave Jones:** We've had some in the 4.4 that people have been running for a year and a half.

**Chris Gammell:** Oh, wow. Okay.

**Dave Jones:** And I had one here that was almost two years until the power went out for a day, and then my UPS has failed.

**Chris Gammell:** Oh, that's a shame.

**Dave Jones:** It's like, darn it, I lost my uptime. Right. It's like a really, really slow marathon. And when the Beagle first came out, that was one of the things I was doing. I was helping out the GCC guys by rebuilding GCC and running their test suite because I found that it would take the board three or four days to do it at 100% CPU usage. Oh, my God. While going over the network. So, it's like, if it stays up to do this test suite, it's doing pretty good. Yeah. It got to the point where it just never failed, so I stopped doing it.

**Chris Gammell:** Okay. And what does that mean with the test suite?

**Dave Jones:** So, GCC has a huge test suite where you build GCC, which takes about a day, and then you run the test suite, which takes about two days. And it runs through all the test cases, pass or fail, and in the end, you get a big list.

**Chris Gammell:** Okay. And at the beginning, it probably is a lot of fails, right? And then later on, it's... Yep.

**Dave Jones:** The way GCC works, it's almost like every bug they've ever had, they've made a test case for. Oh, wow. In the 30 or some years in existence. So, it's a massive test case. That's some baggage, huh?

**Speaker ?:** Yep.

**Dave Jones:** And so, if it survives that, you figure, well, it's going to survive your average user who just has it idling and taking a sensor reading every once in a while.

**Chris Gammell:** Okay. Yeah, no, that is a good test, huh? Okay.

**Dave Jones:** But nowadays, the problem is the boards are a little fast. The test suite's done in a day, so it's kind of worthless. Okay. Yeah. Don't you hate how you keep getting all this computing power? For multiple days.

**Chris Gammell:** For, like, cheap and awesomeness?

**Speaker ?:** Yep.

**Dave Jones:** It's like the test suite's too fast nowadays. Yeah.

**Chris Gammell:** It doesn't actually test anything. Right, right, right. Well, it probably heats up the house a little bit, right? Yeah.

**Dave Jones:** But the arm boards, they don't heat up the house very much. That's the problem. I don't know. They're so efficient. Yeah. We could have this big GPU heat up the whole room, but.

**Chris Gammell:** Yeah. So that was something I was going to ask Jason, too. Like I said, we're sad that he couldn't stay with us, but the, I mean, this chip's getting a little long in the tooth, isn't it?

**Dave Jones:** Yeah, it is. But with the PRU, it's still selling like a hot cake.

**Chris Gammell:** So it's just because of that? I mean, like, so I guess. That tells you how important it is, the PRU. Okay. So, but the ARM V7 is the main, what is the core in there?

**Dave Jones:** So, yeah, it's an ARM V7 and it's the Cortex-A8 version of the Cortex-F7.

**Chris Gammell:** Okay. So it's ARM V8.

**Dave Jones:** And that was the first. So the A8 came out first, the A9 came out second, and then they went crazy and created a whole bunch more parts. Yeah.

**Chris Gammell:** Right. Because I remember like A8, A9, it was like still like iPhone 4, 5, right? Like that's what it was using.

**Dave Jones:** Or you have to think about it. A8 was so Nokia days.

**Chris Gammell:** Oh, am I that far back?

**Dave Jones:** Nokia was the king of all cell phones. It was the OMAP 34 from TI.

**Chris Gammell:** Wait, I thought the A8, A9 was actually still around for a while as like a, as a consumer thing. Is that, is that, am I way behind the game here?

**Dave Jones:** Yeah. I think you can still find them. They're harder to find out. Okay. So most days they're all 64-bit.

**Chris Gammell:** Okay. So I'm full of crap then. So I don't know what I was thinking of with the Apple stuff, but okay. So what is an example number now then? Like what are they using these days?

**Dave Jones:** So the Apple ones are all 64-bit ones. I think the original iPhone was a Samsung Cortex. It was an A7, but it was, or was it an ARM 9? It might have been ARM 11. So even pre-Cortex.

**Chris Gammell:** See, this is the thing that's confusing to me. So there's an A9, but a V7, V8, V8. Yeah.

**Dave Jones:** So the way ARM works is you'd always have the ARM-V architecture. So you had ARM-V1, ARM-V2, ARM-V3, ARM-V4. And so the ARM-V7 variant is where all the Cortex families came from. Okay. Whereas the ARM-V8 is now the new 64-bit stuff.

**Chris Gammell:** Okay.

**Dave Jones:** And so then before the Cortex came out, they had a couple of products. One was called the ARM-9, which is an ARM-V4.

**Chris Gammell:** Wait. Wait a second. There's an ARM-9, there's an A8, and a V7? Yeah. Who of those guys in England really wanted to say we're not? Oh, my God. I'm going to go over there and punch someone in the nose. What is with that naming? That's terrible.

**Dave Jones:** You've got to go on Wikipedia and look up ARM architecture. And I'll show you one number list. I will link people there.

**Chris Gammell:** Yes. Yep. Oh, my God. Okay. So that's really confusing. So what would mess up your world the most? Is it like the V7? So this is an ARM-V7-A8.

**Dave Jones:** Yep. So the biggest thing that messes with us is whether it's – so there's a revision of the core, too. So the original Beagles, when they came out 10 years ago, were R1-PXs. So they were revision 1, and I think there was a P2 variant, and a P3. And nowadays, they're all revision 3 P-something. Okay.

**Chris Gammell:** So wait, R1-PX was the original? Yep. And then now it's –

**Dave Jones:** That tells you it was the first revision.

**Chris Gammell:** Uh-huh.

**Dave Jones:** It was basically the first Cortex-A8 that ever came out, whereas the newer ones are like the third revision. So lots of bugs in the old stuff. Okay.

**Chris Gammell:** Well, you know.

**Dave Jones:** I mean, it happens. Surprisingly, one of those old bugs fixes Spectra in Meltdown for us.

**Chris Gammell:** Ha-ha. Take that, Intel. Yep. Yeah. Different kind of realm of things. But okay. That's good to know. I was actually listening. So people heard me floundering trying to talk about it last week. I then listened to Embedded, and they had someone on who actually knew what they were talking about. And that was much better. Oh, it was Exploding Lemur from Twitter. I forget. Nick, I think. But I'll link that as well, where they actually talked about it. So they talk about Spectra. And what is it? Spectra and – Spectra and – yeah. It's not Heartbleed. Meltdown. Meltdown. That's it. Yep.

**Dave Jones:** Yeah.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah, I think you teach a whole couple of graduate courses on that stuff now.

**Chris Gammell:** Yeah. Right. That's crazy.

**Dave Jones:** And people still don't know what's going on.

**Chris Gammell:** So this was a good explanation. So I will link people there. Okay. So you had to switch, though. So what happens then when it goes from R1 to R3? Is it like the compiler changes, or what changes here?

**Dave Jones:** Well, one of the big things that was happening in the ARM world, everything was getting recompiled for Thumb2, which is –

**Chris Gammell:** Wait. There's another number?

**Dave Jones:** Yes.

**Speaker ?:** Oh, no.

**Dave Jones:** Thumb2 allows more optimized code. It's both 16-bit and 32-bit instructions in the call stack. And R1 family had lots of thumb bugs, so.

**Chris Gammell:** Okay. And thumb versus Thumb2. God, their naming is terrible. It's really bad. Okay, so – They were having fun, though. You have an ARM processor or a thumb mode. Oh, okay. That's kind of clever. But like just the appending of numbers, that's the bad part. Yeah. Like why not call it fingernail? I don't know. Or pinky. Or, you know, anyways. Anyways, that's –

**Dave Jones:** If you look at the 64-bit stuff, it's now worse. They have ARMv8.1, ARMv8.2, ARMv8.3.

**Chris Gammell:** Yeah. That's crazy. Okay. So, you had to go and – so, when it went from Thumb2, what did you have to do then? Like, do you have to go and like recompile everything or what happens?

**Dave Jones:** For the kernel, we – there's a lot of changes we had to do. And we found out very quickly that Thumb2 broke a lot of stuff. Okay. So, that's one of the reasons why when you go to thebeagleboard.org, there's an XM image for the old Beagleboards. And then there's a bone image for these, for the newer stuff.

**Chris Gammell:** Okay.

**Dave Jones:** One of the big changes is that all the bone stuff for the Beaglebones have Thumb2 enabled by default.

**Chris Gammell:** So, why didn't XM take that on? Is it because it's just the processor is on board?

**Dave Jones:** The processor is on board and if we enabled it, we'd lose performance and other things would break. Whereas, the pocket beagles would handle it just fine. Okay.

**Chris Gammell:** Just because they're lower performance in the first place? Yeah.

**Speaker ?:** Okay.

**Dave Jones:** They could actually understand that instruction about problems. Oh. About worker runs. Okay. Okay.

**Chris Gammell:** Got it. Man, that's crazy.

**Dave Jones:** And that's one of the things we had to enable. It's like, okay, we have a single core, Cortex-A8. We have to enable Thumb2 because we need every performance we can get out of the core at this point.

**Chris Gammell:** Yeah. Yeah. So, I think this, I mean, this just really, really reinforces like just the layers and layers and layers of abstraction that happen. You know? There's just so much stuff that I don't have to think about, which is great. Like, really great. I never want to think about this ever. And you're a saint for doing this stuff. And Jason is too. That's what it goes. You know? Yeah.

**Dave Jones:** It's like, we try to make it as easy for everyone else. Like, it's just all the stuff to make it fast is enabled by default. Right.

**Chris Gammell:** That's great. So, Thumb2 broke a lot of stuff. You had to read. So, just go like bug fix at that point? Is that the idea?

**Dave Jones:** We basically separated the two. It's like. Oh, okay. So, we have Thumb2 enabled for this device. This device does not get it. Don't run these images.

**Chris Gammell:** Okay. And then, so, kind of going. Is this kernel stuff? And my brain is starting to slow down. And we should probably end the show soonish. But, okay. A lot of it is on the kernel side. Okay. So, like, that's what I'm wondering. It's like, so. So, when you said you broke a lot of stuff. Does it break the peripheral things too? Or just the internal, like, talking to. From one thing to another. That question may not have made sense.

**Dave Jones:** Oh, it's slow downs. And you get undefined instructions. And you get erratic behavior. So, yeah. Breakage. Lots of breakage.

**Chris Gammell:** But you fixed it. So, that's good.

**Dave Jones:** Yeah. We fixed it on the older parts. And, like, just don't run these images of that.

**Chris Gammell:** Okay. But, like you said. So, you said that these builds come out quarterly. So.

**Dave Jones:** Yep. So, we have two separate builds to go on. We have a monthly build for Jesse. Which we consider the old stable at this point. For stretch, we have builds every Sunday morning. And they get pushed out Sunday afternoon. So, every Monday you'll see me update a wiki page. Like, here's the latest images for this week.

**Chris Gammell:** Like, what it fixed. And what's new about it. Or whatever.

**Dave Jones:** Yeah. I don't bother showing what it fixes anymore. It's like, it's just a rebuild of all the new packages.

**Chris Gammell:** Yeah. Just use it and be happy.

**Dave Jones:** Don't ask questions. Yeah. And that's one of the things is, you know, people ask, well, how do I get net? You know, they want to get network connectivity to their Pocket Beagle to just update the software. It's like, just go to the website, download the latest version. You have it as an updated Sunday. Ah. It has all the kernel weeks fixes from the week. It has all the uBoot fixes from that week. Got it. And so, it's just continuously integrated. Okay. No, that's good to know. Our disconnect is how often we convert that weekly image to, hey, here's the latest image.

**Chris Gammell:** Right. So, and that's a good question, too. So, if someone's going to, a lot of people, if they're just thinking about doing this, what should they go and pull down as their first thing for the Pocket Beagle?

**Dave Jones:** So, the first thing that they need, all they need to do is just turn it on, the Pocket Beagle. But, I mean, which image, though?

**Chris Gammell:** Is it shipped with the...

**Dave Jones:** Oh, that's right. Because there's, yeah, I keep reading. There's no image by default. Right, right.

**Chris Gammell:** It's the SD card, right?

**Dave Jones:** Yeah. Because the older boards, you plug it in, it'll actually tell your website, go to this website, FQs. And then you go to that website, hey, there's a new image.

**Chris Gammell:** Right. So, they go, they grab an SD... I don't think it ships with an SD card, right? Yep, it doesn't ship with an SD card. Right.

**Dave Jones:** There's a good utility called etcher.io that is multi-platform. Yeah. Yeah. It's solved all the Win32 problems. It's solved the Windows, Linux, Mac is different. Yep. They're awesome guys at Resin. Yep. They also have their own image for the Beagle, too.

**Chris Gammell:** Oh, cool. Okay. Okay. So, it's best to start with the Jesse stable, though, or which one? Depends. Just give me one, man.

**Dave Jones:** I tell people to run Buster right now. Oh, God. Is that the newest one? That's the one that's going to be coming out in a year and a half from now.

**Chris Gammell:** No, no, no, no. Don't do... Okay. Never mind. Yeah. Don't listen to this guy. This is like... Yeah. This is like when you walk up to a Linux guru and you're like, hey, what is that interesting thing on your laptop? They're like, well, let me tell you. Let me tell you.

**Dave Jones:** This is the newest and greatest and you'll have it next year. Right.

**Chris Gammell:** Why don't you take a seat? And I'll show you how to do this from source. Exactly. Oh, my God. You can use flags. You can build it yourself. Okay. So I'm going to say the Jesse stable then?

**Dave Jones:** Yeah. Stretch stable is what we've been telling people to do right now. Okay. That's good. Because stretch is stable. Jesse, we're not going to do a lot of changes to it. It's kind of frozen. So if you have something that you don't want things to change, use Jesse.

**Chris Gammell:** Okay.

**Dave Jones:** And so the stretch, we're still backboarding things.

**Chris Gammell:** So the stretch stable though, what would be the default kernel to? Because now I know that's a different thing.

**Dave Jones:** Yeah. So in Jesse right now, we're shipping 4.4 by default. We're not going to change it ever. It's done. Yep. Stretch, we're at 4.9 right now. Okay. I'd like to get it to 4.14 in the next month or two.

**Chris Gammell:** Okay. That's good to know. And that will enable some of the, you said like the network connectivity stuff and maybe the mesh stuff, right?

**Dave Jones:** Yeah. The biggest thing is mesh networking is going to be better. Problems of Wi-Fi mesh, we don't have a good version of the WPA supplicant and the host AP package. Yes. To take full advantage of that, but the kernel is ready.

**Chris Gammell:** Cool. Cool. Okay. So last question. Where do people go to find other people to help answer questions?

**Dave Jones:** The easiest thing to do is just search BeagleBoard group into Google. There is this massive forum slash email list that has been going for 10 years. Okay. It's like Google groups or something? Yep. Google groups. It's the BeagleBoard project. Okay. Yeah. It's been going on for 10 years now. Tons of people have been on there. Flame Wars abound. Yeah. Flame Wars from every era.

**Chris Gammell:** Yeah. 10 years, man. That is very impressive, actually.

**Dave Jones:** There's a lot of historical stuff in there. You can go back and what was 2.6.11 like on the board? Right. I guess that's what's amazing to me, too. What was it like before, Thumb? What was it like before ARM optimizations?

**Chris Gammell:** There's your weekend plans right there, folks. I mean, come on. Go listen to all that stuff. That's great. Yeah.

**Dave Jones:** Make sure to bring out your pitchfork and magnifying glass to look at the arcade.

**Chris Gammell:** That's right. Oh, man. Yeah. And then use your historical stuff against you at some point, right? Yeah. Robert, you said this back in May of 2009. Yeah.

**Dave Jones:** And you'll see people that worked at Nokia, then people moved on to TI, then went to Trolltech, and then they moved back to TI, and then they went back to Intel. You can see people move all over the place to the email thread. Did you say Trolltech? Yeah. Trolltech. There were some Trolltech developers.

**Chris Gammell:** Then Nokia bought them. Trolltech is just perfect for an online discussion group, though. Well, that's why there's a troll group. That's great. Okay.

**Dave Jones:** Yeah. Because otherwise, there's the IRC channel, too. Okay. So that's good to know. Yeah. Beagle on Freenode. Okay. Beagle. Great. Of course, I'm never on there, but we'll let other people answer those questions.

**Chris Gammell:** IRC is its own beast. I recently had to go back on, and I'll probably be back off again. It's just one of those things, you know? Yeah. You have to go on everyone's phone.

**Dave Jones:** It's like we have Google Summer Code starting again, and I'll have to be on there again. Oh, yeah. Right. Take care of those students. Yep.

**Chris Gammell:** You're doing good work for that. You're doing good work for all this stuff. Like I said, I never would have gotten close with any of this stuff. So I feel personally enabled by all these projects that are out there. Like the fact that, you know, there's Linux computers that are running just a single circuit board is insane.

**Dave Jones:** Yeah. A single-sided circuit board in some cases.

**Chris Gammell:** That's true. Right.

**Dave Jones:** I'd still like to see someone actually do design where that Octavo chip, there is a way to do this one-sided board. That's right. Yeah, because it can escape and... It is set up for them, but I haven't seen anyone do it yet, so... Challenge accepted. It'd be a good one to see on one of the blog sites.

**Chris Gammell:** Right. You need to see it, and it needs to be like milled, right? It has to be available on Tindy. Right. Right. Exactly. Just wear it around your neck is like a talisman.

**Dave Jones:** You got to prove it works, and then you can prove you can make it, and we can buy it.

**Chris Gammell:** Right. What about you? Are you on the Twitters or anything like that?

**Dave Jones:** I'm mostly on the BeagleBoard groups, and then I'm hiding behind IRC. If you ask enough questions, eventually I'll answer.

**Chris Gammell:** Okay. So you're there, you're just... I'm usually hidden. Yeah. Okay. That's healthy. But no public-facing Twitter-type thing. No, I like to hide. Okay. I like to hide. You know what? You've got your server farm. You've got your whatever you called it, your build farm.

**Dave Jones:** Yeah. It's like they find me on GitHub. I get hundreds of emails a day, so it's like, I try to... Seriously?

**Chris Gammell:** Oh, I guess all the updates and everything.

**Dave Jones:** Yeah. It's like, hey, we need this. You broke this. Fix this.

**Chris Gammell:** Right. All right. Well, we will definitely post links. I will be posting links to all this stuff, everything I can figure out. I'm going to have to listen to this whole episode again, too, and be like, what were we talking about? Yeah.

**Dave Jones:** Because the good thing is we have a link somewhere for everything. Yeah.

**Chris Gammell:** The problem is we don't remember where it is. The core organization, right. Yeah.

**Dave Jones:** Yeah. Because when you have a 10-year-old project, you have links going everywhere. That's right.

**Chris Gammell:** Yeah. Well, Robert, thank you very much for being on the show. It was a pleasure talking to you. I'm sorry Jason had to go, but we enjoyed talking to him again, too. And we'd love to have you back sometime.

**Dave Jones:** That'd be awesome. Pleasure to talk to you guys, too.

**Chris Gammell:** Okay. Well, we'll talk to you soon.
