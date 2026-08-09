---
episode: 512
title: Design For Longevity
url: https://theamphour.com/512-design-for-longevity/
---

**Chris Gammell:** This is The Amp Hour Podcast, released October 11th, 2020. Episode 512, Design for Longevity.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EAV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. What's up, nerd? Hello, nerd. How goes it? I was like the middle of reading a tweet. I should have not been reading one of your tweets as I'm about to start talking to you. Millennials, you know, millennials.

**Dave Jones:** Yeah, tension span of a gnat. Yeah. Oh, boy. Anyway, so yes, what were you going to say? You weren't. You were just mumbling.

**Chris Gammell:** This tweet of yours is dumb. What tweet? No, I don't know. Every tweet of mine is dumb. Now, let's see. One of my tweets, I don't know if you saw my troubleshooting setup. Did you see that thing? I've got a new remote debugging setup.

**Dave Jones:** Oh, yes, a remote thing. I love, yeah, I retweeted somebody's comment who, gee, this is a show we're just going to, we're scraping the barrel, aren't we? This is typical. No, no, no, no, no, no, no, no, no, no, no, no, no, no.

**Chris Gammell:** Hey, hey, hey, hey, this is just recapping our life, which happens to also coincide with our tweets.

**Dave Jones:** With Twitter. God, we're pathetic. We need to get off that platform.

**Chris Gammell:** It's social media, Dave. It's, yeah, yes, I agree with that. You know.

**Dave Jones:** We should just, we should just ditch it.

**Chris Gammell:** Anywho, I'm just recording my life and then talking about it here.

**Dave Jones:** All right. Anyway, somebody mentioned the comment of the day, comment of the week, was that looking at a LED and LED, people hate it when I call it LED, looking at an LED through a webcam, you can think of that as a giant opto coupler.

**Chris Gammell:** And yeah, I agree. That's great. Yeah, that's awesome.

**Dave Jones:** Yep.

**Chris Gammell:** So for a little background, I have been setting up a troubleshooting setup for someone that's helped me write some firmware. And I was like, well, how the hell am I going to get them to like hard reset, you know, so they're writing firmware.

**Dave Jones:** Remote troubleshooting, right.

**Chris Gammell:** Yeah, remote troubleshooting, whatever. So I'm using an analog discovery too, which I've talked about on here before, I'm a big fan of. And basically monitoring some rails, powering, powering the thing on via the 82. And then also have a webcam on there, like you talked about, basically to watch if the LEDs are blinking. And then there's like a J-Link plugged in to actually do the troubleshooting, things like that.

**Dave Jones:** So can they access those debugger tools remotely?

**Chris Gammell:** Yeah. Yeah. I mean, it's just a VNC type of setup.

**Dave Jones:** How does that happen?

**Chris Gammell:** They log in and then they have access to Eclipse and tools and all the other things.

**Dave Jones:** Is that a remote desktop thing? Do they take control of your computer? Yeah, exactly.

**Chris Gammell:** VNC is like a remote desktop.

**Dave Jones:** Oh, okay. Got it. Right. I thought there was some clever portal that you could, you know, serial link it or something, you know, to the other person. Yeah. But yeah, it's easy. There probably is. Leave it in the comments down below if you know. Yeah. But it's easier just to allow someone to remote desktop into your computer and, you know.

**Chris Gammell:** I was talking to a friend about this too. And it's like, this is a common problem. Like, say you had like a test stand halfway across the world, right? You need to log in. You want to be able to see things. This is probably not the way to do it because it's still very graphically based. But yeah, like something where it was just, you know, like an X terminal or X, is it X terminal? Whatever it is. Like the window viewer in Linux, you know, so you're just porting commands over the text interface and then you're rendering locally instead of like pulling the entire screen capture, you know, screen like, you know, frame by frame by frame. That's kind of how like I think some of the, maybe not BNC, but I think some of the other ones, they actually do. Like if you're like screen sharing on Zoom or something, it's literally just like grabbing your screen and sending that over.

**Dave Jones:** And send it over. Yep.

**Chris Gammell:** Yeah. And then, you know, it's like, oh, okay. Your mouse is currently at, you know, 400, 600, and now it's got 500, 600, and 600, 600, you know, it's like stepping across. So it's not as good, but this is, yeah, this is a kludge. I mean, it's fine. Kludge? Yeah, kludge, you know. Kludge. I say kludge. Kludge.

**Dave Jones:** What's this kludge rubbish?

**Chris Gammell:** I don't know. Kludge.

**Dave Jones:** I always say it. Okay. Kludge.

**Chris Gammell:** And yeah, so it's pretty cool. The goal is eventually, so like the board is the thing I've been talking about on here, the ABC board. It actually has the Raspberry Pi, like it is like a hat. And the thought is like eventually I could just plug it into a Pi and then, you know, it has a serial interface to the NRF chip on board. It's got an OCD interface to program it. I could maybe get a camera, you know, like a Raspberry Pi camera and monitor it like that too. Another friend had said they did something similar. You wouldn't have like the voltage monitoring as easy as it is otherwise with like a, you know, analog discovery. But I guess you could try and, you know, script it or something like that. So, yeah. I don't know. It's kind of cool. It's probably like overdone for like, you know, if I'm not doing like, you know, five devices at a time. But for my friend helping me write firmware, like, yeah, that part's great.

**Dave Jones:** Terrific. Have you ever tried to do PCB design over remote desktop? I have not. Oh. Why would you do that? Just because like licensing? Because I've had to do it for when I worked at Altium, you know, because I was working from home and I can't, the restriction it was because all of our stuff was over there and it was too, I can't remember why, but I was doing it over remote desktop. I was running Altium Designer over remote desktop. So it was running. So the software was running. I think it was because all of the, because all of our libraries are integrated with the network and everything. Right. So it was all like, you know, so I couldn't just copy the project locally, work on it or I could, but then it was like harder. So it was just like probably less pain just to, you know, like I wasn't laying out a complete board, like, but I was like finalizing a, a design or something like that. Sure.

**Chris Gammell:** Like scrolling around and like trying to, and it's very visual, right? Yeah.

**Dave Jones:** Oh yeah. Yeah. It's a very visual thing. And as you said before, like it's simply capturing a screen every like five times a second or something or three times a second. It's so slow. I can't remember what remote desktop software we're using. It's not like, you know, this was 12, 13 years ago. So remote desktop technology wasn't as good as it is now. Right.

**Chris Gammell:** Right. And it's still not great now. No, it's still not great now. How far was, was it going? Was it like, was it in the same country? Was it in Australia still?

**Dave Jones:** Oh yeah. Yeah. It was in Sydney. Yeah. So it was going from Sydney to Sydney. So it wasn't too bad. So there wasn't, but you know, it was, I was only getting like a couple of frames per second updating. So trying to lay out a board with, you know, like five times per second updating or something is like, Oh, it's, it was slow, but.

**Chris Gammell:** Test your patience for sure.

**Dave Jones:** Yeah. But I had to, and it was over Christmas, I think, you know, so it was like, Oh my God. Oh, it was. Yep. But it was the only way to get the job done. So we did it, but geez, it was, it was painful, but it actually worked. I was able to do it and you kind of got used to it, but you kind of got used to the torture of, you know, placing trace, waiting. Yeah. Place, trace, wait. You know, it's like. Step, pause, step, pause. Yeah.

**Chris Gammell:** Yeah. Totally. Wow.

**Dave Jones:** Yep. Oh, it was. Yep.

**Chris Gammell:** I didn't, I didn't have to do that, but one of the worst academic experiences I've ever had was like, I was in a class. So this is, you know, college days. I think it was a analog circuit design class, but it was on a chip. And so it was like a combination of things. Like we were remote desktoping. It was the first time I had ever used a Unix based system. Right. It's a Unix system. I know this. And it was remote. It was that X, X windows or X server, whatever. Yeah. Right. And, and then it was when you, even then when you finally got in there, it was, it was a cadence design tool or something like that. It was like Leonardo or something like that. Right. One of the, one of the chip design tools. And that, you know, you could be sitting next to the creator of the software and it would be the most obtuse piece of software you've ever used. And like, you're trying to like piece all these things together. And I just remember, I remember like viscerally remember that, like freak out two in the morning, like, why is nothing working? You know, just like, just like screaming at my computer. And of course, you know, it was, that was like 2003, 2004. And so we had a great network on campus, but I just didn't know what was going on. So I remember like trudging to the, to the lab at like two in the morning and just like, I'm like, I can't do this. I'm not in front of the computer. And so I sat down there. It was the worst experience. And, and that's why I'm not a chip designer. Not because I'm terrible at it.

**Dave Jones:** Oh, can we, uh, speaking of like terrible experiences like that, can we talk about possibly the most obtuse PCB design software in history?

**Chris Gammell:** Yes. This is, this is something.

**Dave Jones:** This is really something. Somebody, I can't call up the link because I, I need my, I thought, no, I need four. I, I, four of my two-step authentication. To get into my own forum. Oh no.

**Chris Gammell:** Oh no. Anyway. You can view it with your, with your not logged in. So.

**Dave Jones:** Yeah, I can, but it's not letting me actually.

**Chris Gammell:** Just open a incognito window, you know?

**Dave Jones:** Yeah. Nah, it's, nah, it's, ah, shift.

**Chris Gammell:** It found the spammer. It found the spammer.

**Dave Jones:** Yep. Another browser. Another browser. Here we go. Oh no, it's still doing it in another browser. Cause I must have cookies enabled. Oh, bloody cookies.

**Chris Gammell:** This is why you do a incognito. Control, shift, N.

**Dave Jones:** Yep. Control, shift, N. That's what I'm doing now. Hey, here we go. Come on. You can do it.

**Chris Gammell:** Anyways, this is a, it's in what software, Dave?

**Dave Jones:** It's in LibreOfficeCalc. So it's in Excel, basically.

**Chris Gammell:** Yeah, it's Excel. Yeah.

**Dave Jones:** It's a PCB design software in Excel.

**Dave Jones:** Chris 42 on the EEV log forum gets credit for writing PCB design software in Excel.

**Chris Gammell:** To be fair. Like, so this is very similar. This is like very similar to the stuff I was just talking about. It's a chip design software. It's not that different. You know, if you go like open up like electric or all of these different things, like their unit cells and they're basically like, they're creating these different blocks and piecing them together. And you have to, the thing that always pissed me off about it is like, why is there no 3D view? This is creating some of the most advanced technological things in the world. I just want to like click and rotate it 3D and like look through it. Like that is the hardest part about chip design is that you're, you're looking at it. I remember because Dr. Darren Young, one of my not super favorite teachers at Case Western, very smart guy. But basically like he had us like sketching on graph paper to do this exact same thing. So if you imagine, I guess to paint a picture.

**Dave Jones:** So you would sketch your own 3D view?

**Chris Gammell:** No, no, no, no. To sketch your 2D view. There was never a 3D version. So, so just to explain what we're looking at here, Dave and I are looking at like a two, 200 by 100 grid of squares with spaced out with like gray spacing in between. So like, like Dave said, it's like an Excel cell that is basically colored blue or purple or gray or whatever. And then basically the idea is that you're designing this chip by, I guess this, oh, this is actually a PCB. Yeah.

**Dave Jones:** Yeah. It's, it's done by shorting cells together. So think of each individual cell in a spreadsheet as a bit of copper. And then you're sort of like shorting them together.

**Chris Gammell:** It's almost like Vero board. Like that's kind of a good way to think about it. Right. Is if you're like, like how, um, like great Scott, like he, he, he does when you Vero board, he actually shorts, he like drags solder across multiple Vero board holes.

**Dave Jones:** I think that's what it is. I don't think it's actually PCB. I think it might be. Yeah. It totally reminds me of a proto board.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** But, but that is actually a very similar kind of like look. So I got this wrong. I was thinking this was also chip stuff. This is, this is PCB. It looks very similar in a, in a chip design software. Yeah. At least the old stuff did. And, but there was never any 3d view. And so like literally this professor that I had, he made us do the same kind of thing, not in Excel. You had to do it in grid graph paper, you know, like one, one millimeter square grids or one centimeter square rather. And like, uh, and then you had to like draw it all in there with like colored pencils. And it was, no one ever rotated it though. You never saw how it was actually all connected together. You had to know that these things stack up and if you don't have that 3d view, much like people getting started with PCBs, it's very tough to visualize vias. One of my favorite things in, in KyCAD, the 3d viewer is actually to turn off the FR4 visualization and just look at the vias and look at how the tracks are all connected. I think that is like one of the most useful things if you're learning how to use a PCB software for the first time, because making that mental switch from lines on a screen, like literally lines on a Excel sheet to like, you know, what a trace looks like on a PCB. It's like, that's a really tough leap, I think.

**Dave Jones:** Yeah. Have you ever created a, uh, piece of B layout backwards?

**Chris Gammell:** Backwards, uh, define backwards.

**Dave Jones:** Back to front because I did this in a PCB class once because we had to, uh, you know, normally it's a two-step process to, uh, create the negative and, you know, and do all the stuff like that. And I went, Oh, bugger that. I can skip a step. I can skip a physical construction step. And if I actually lay everything out backwards.

**Chris Gammell:** So you, you basically laid out the negative space.

**Dave Jones:** I know. I know. I laid, I, I flick, I physically flipped the thing backwards so that it would. Yeah. So it laid, so pin one was like in the opposite direction and everything was, everything.

**Chris Gammell:** Oh no, I've never, I've never done that. That's, that's. Oh yeah.

**Dave Jones:** That was, um, yep. Yep. I, I, I thought I was being clever. How'd it work out? It worked.

**Chris Gammell:** Yeah, that's great. Yeah, that's great.

**Dave Jones:** And I skipped a production step.

**Chris Gammell:** How much time do you think it saved you versus how much time it cost you to actually mentally do that?

**Dave Jones:** Oh, it, it wasn't a big layout. So it was, it was, yeah, it was like more of a fabrication class than anything else. You know, it was, yeah. So yeah, it didn't take me long. I think we did a, what was it? It was a, uh, it was a stud finder.

**Chris Gammell:** Okay. So like a LC tank kind of thing.

**Dave Jones:** Oh yeah. No, you did it with a, uh, 4,000. It was a 4,000 series inverter or something. I think it was a 4,001 or something. I don't know. Anyway. Um, no, no, it was a 40, 40 and only worked. And the thing only worked with one brand of chip. You could, I seriously, it only worked with one brand of 40, 40. They were using a unique property of this one brand of 40, 40 chip.

**Chris Gammell:** Yeah. Yeah. It had to. Are we calling that working? Well, yeah.

**Dave Jones:** It's, I can't remember.

**Chris Gammell:** That's great.

**Dave Jones:** Oh my. Was it like, or it was an unbuffered version of the 40, 40. I don't think, um, uh, CMOS. Uh, it was, oh God, this is so many decades ago now. Yeah. I think you, you couldn't use the 40, 40 B because that was the B was the buffered version. I think you had to get the non-buffered version. No, no, no. The 40, 40 is a counter. What am I talking about? No, it was anyway. It was a 4,000 series CMOS chip. It's the decade.

**Chris Gammell:** It's the decade. Yeah.

**Dave Jones:** Because if you don't have a buffered 4,000 CMOS, you can actually use 4,000 CMOS as analog type devices if they're non-buffered.

**Chris Gammell:** Oh, interesting.

**Dave Jones:** Yes. Okay. So a few, many early designs in, in like the seventies, this is before you were born. A lot of the, uh, projects out there, they would, um, take advantage of some sort of like unusual analog properties of 4,000 series CMOS logic.

**Chris Gammell:** Oh. And yeah.

**Dave Jones:** Yeah. Because they're effectively just, you know, FETs. So you can sort of use them in an analog-y type way, but the buffered version. Yeah. It, that sort of made, it mucked up the whole analog-iness of it. So, so you couldn't use a, like a feedback elements and stuff like that to actually, you know, do things like that. So yeah.

**Chris Gammell:** That sounds like a good topic for a video, Dave.

**Dave Jones:** Yes, possibly. I might try and dig that up. I might try and dig up. You should.

**Chris Gammell:** I mean, that's interesting. Yeah. Yeah. Yeah.

**Dave Jones:** It's, it's absolutely fascinating. Like, you know, totally not recommended for any design whatsoever. It's an early hack. You know, it's a hack. Yeah. Yeah. Yeah. It's a hack. Yeah. Using 4,000 CMOS as a, yeah. Like I've done a video on, on like powering a chip through the IO pins. Oh yeah.

**Chris Gammell:** I've seen that one. Yep.

**Dave Jones:** Yep. Yep. And you know, you can do weird stuff like that. So yeah. Back in the old days. Let us know if you've ever built that into a product that was reliant upon, you know, some weird aspect of some, either some particular brand or one particular type of chip.

**Chris Gammell:** And let us know how many times your manufacturer engineer stabbed you.

**Dave Jones:** Oh, because you bought the wrong, you know, part. Oh no.

**Chris Gammell:** I'm just because it's like, you know, it's, it's on the precipice of failing all the time. Right. Yeah. If you can't source it or. Yeah.

**Dave Jones:** Yep. Anyway, good fun. Good times. And I'm sure this was good times for Chris. Um, so hats off to Chris for, um, not me. Yeah. No. Yeah. Other Chris, uh, Chris 42 for perseverance in. Wow.

**Chris Gammell:** That's something. Yeah.

**Dave Jones:** PCB design software in Excel. Okay. We'll see you now. Oh, that's great. That's great.

**Chris Gammell:** One of the cons that he lists is during the design process, you will destroy a minimum of three keyboards. Each one will be a first one attack of rage. The second one was in during footprint placement. And the third one will shatter when you try to run a macro and you'll get an error, which forced you to move a couple of times. That's good.

**Dave Jones:** Oh man. The things we did like, see, like I'm getting too old. I don't have time for shit anymore. Right. Whereas back, you know, back when I was a, back when I was a youngster, a young whipper staff, like I'd spend like months just working on some like pointless, absolutely pointless thing just because I could, you know, was it because you could though?

**Chris Gammell:** Or because there wasn't a better, like, was there a better alternative out there though?

**Dave Jones:** Oh, maybe. Yeah. Okay.

**Chris Gammell:** Like I could see. Okay. So you're looking at something like this, right? Like a, like a spreadsheet program like this. What I'm guessing is I didn't, I didn't read the entire thing, but it's, it's a power devices class. I'm guessing this was made at some point by a professor or a grad student. And it was just like, well, we're going to just keep doing it this way. Why, why the hell would we learn a PCB CAD program when we can just, you know, we want to learn the concept. And so we're just going to use Excel, right? Excel is still Excel just like it was in the nineties. And like, and, and I argue against it because I hate, hate that idea as does this other Chris apparently, but like, you know, from an educational standpoint, like, yeah, they're, they're lazy. They don't want to, they want to do anything fine, whatever. But like, if you have another opportunity, you know, especially as an individual, like, Ooh, screw this stuff. You know, like it's like, this is just not relevant to anything else too. I, I always kind of like chafe at that anyways. Like they, you know, like professors say like, Oh, well we can't possibly teach a CAD program because it'll instantly be obsolete. And it's like, well, yeah, but it's a little close. It's a little closer than Excel. No one, you're going to have to relearn a CAD program. You know, if you're an Altium user, you have to relearn, you know, how it's used every couple of years anyway, just because of how the conventions changed. But like, yeah, this is no, no one's ever going to use this. It's not even close, you know? Like, so yeah.

**Dave Jones:** I know it's, yeah, it's, it's a pointless way. It's practically a waste of time.

**Chris Gammell:** Yeah. Yeah, exactly.

**Dave Jones:** It's, yeah. Yeah. It's, it reminds me of like, you know, when you do a microprocessor classes and stuff like that, I can remember they always use their own in-house designed, you know, platforms. No, no. They use their own in-house, you know, development kits and stuff.

**Chris Gammell:** It's like, Oh God. Yeah.

**Dave Jones:** You do realize you can just buy a development kit from Intel or whatever. It's like, you know, or a Zilog or something like that. And it's like they, you know, and it's some convoluted bloody development system. It's like, Oh God. It's once again, not, you know, no real relevance to out in the real world.

**Chris Gammell:** Right. And I think, I think again, that because they don't want to redevelop curriculum, that's fine.

**Dave Jones:** Oh yeah. Right. Yeah. But somebody had to develop that in the first place. Somebody had to go, right, well, we're not going to use this Zilog development kit. Nah, bugger that. We're going to develop our own.

**Chris Gammell:** Right. But at the time that probably was a decent idea, but again, it's probably just because it was 20 years ago and they're just still not updating it. You know, like I feel like so much of it is that the teaching part isn't rewarded. And so like, I would point people to the show with, so like, first off, Brock Lemares was one of my favorite teaching folks who's been on the show. So he's at Montana state and he does great like videos and stuff like that. But he, you know, even he kind of chafed a little bit at the idea of like redeveloping curriculum because it's really advanced. And it's really involved rather. And like, so like from that perspective, I get it. Like I am the same, but like, you know, from the, the, the consumer standpoint as a, as AKA the student, like that, that sucks. You know, like if you're like using a, you know, I think there's maybe some arguments for like these days of like, okay, you're going to use a PCB program, like put it in a container, you know, like put it in like a virtual box or something like that. And like, yeah, maybe you're running a, you know, a six 40 by four 80 window on your 4k screen at some point, but like, but it still works, you know? And it's like, I don't know. I just, I feel like like the preservation piece is almost as important as anything else. You know, that's, that's the hard part is yeah. Interfaces change. I get it. But like, yeah. Sometimes if you just like lock it all in and I'm sure there's still some people out

**Dave Jones:** there using like a ProTel for DOS, you know, probably yeah. Because like, you know, as you said, like in a six 40 by four 80 virtual windows window, you know, virtual window or whatever, you know, still, still running that.

**Dave Jones:** Yeah.

**Dave Jones:** I did a video on that, you know, actually get it. I found one of my old files. So I thought, Hey, can I load a 30 year old version of ProTel? I think 30. Yeah. It was, would have dated to the late eighties. Yeah. You know, 30 year old version of the software and it worked like it loaded in, it loaded up. It loaded my original files. I was able to play around with it. It was dog slow. Like I thought it'd be so super quick because, Oh, this is DOS. Right. And, you know, and geez, these machines are, you know, a thousand times more powerful than they were back then. And it was, no, it, it was really slow. Just the, you know, the painting algorithm of, you know, paint, like filling in all the scrapes are like going across, it's rastering across. Yeah. You can see it rastering across, actually rendering the screen. It was like, okay. It wasn't really that bad. I could not remember whether or not it was that. Like I can remember there was lag when I zoomed in, like, you know, zoomed in so that you zoomed into a pad so the pad would fill the entire screen. And it took time to draw that pad. Yeah. Right. You know? And it was like, yeah, you just take it for granted now with our GPUs that just fill in polygons or whatever, just bam, like that. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** And, but back then, no, it was individual pixels. It was like paint pixel X dot Y, you know, it was paint that it was, you know, calling up a routine that painted each individual pixel.

**Chris Gammell:** I do remember like really long start times on like the 386 computers that we had when I was a kid. Sorry if that makes people feel old. Sorry. I had 386 when I was a kid. 286. DOS booted up pretty quick. No. Well, we had really bad ones too. So there may be that.

**Dave Jones:** Windows 3.11 was pretty quick.

**Chris Gammell:** Okay.

**Dave Jones:** It's faster than modern PCs, I think.

**Chris Gammell:** Well, then I think about like my scope that takes like six minutes to boot up. Yeah. So it's all relative, right? And we're still waiting on, you know, like a phone takes a couple minutes to boot up. I think I get it. Like there's a ton of stuff to do. Which scope are you using? This is my MDO 3000. That thing takes a solid chunk of time. Yeah. Oh, there's your problem. Yeah. Yeah. Well, you know, bankers can't be choosers, Dave.

**Dave Jones:** No, I know. It's a, yeah, it's an awesomely powerful scope, but it's, it's not suited for practical everyday use, you know, just, oh, I just want to check away for them. Oh shit. I've got to wait five minutes for my power on and, you know, get it in the right mode.

**Chris Gammell:** I've been, I just, you know, when I'm using it, usually I'm in the depths and I'm having it on for a couple of days to try and chase down a problem. So.

**Dave Jones:** Right. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Of course.

**Chris Gammell:** I am doing a, so now that I, I've got this new Zephyr thing that I've been talking about on here, I do, I am doing that in a virtual machine. I, I got sick of it. I didn't want to do a boot. And I think I'm going to do that for other things too, because, so I had a client that was like on pause for like eight months and they came back and they're like, Hey, we're ready to start working. I'm like, cool, whatever. You know, I got all the board files. I got, everything works fine. And then I'm like, I completely wiped out their, the dev environment though. Like, and I should have, you know, like, and just because the computer, like my computer crashed and I had to like reinstall everything. And so now I'm going to go through it. And I remember like on Ubuntu specifically, it was a really, you know, so I really like simplicity studio. That's the, uh, Silicon labs, like EFM eight thing that I talked about. And like, I really, I really like it. It's actually cross-platform nice software built on, I think it's built on an eclipse. No built on, I don't know what it's built on. Yeah, it's built on eclipse. And like, but it was just like really wonky for like, it had some library weirdness and so, okay, fine, whatever. But like, if I would have had that in a machine, a virtual machine, I could have just like clicked a button and it would just come up as, you know, a virtual machine. And I, so from now on projects get their own virtual machine and storage is effectively free. And like the USB pass through, I was kind of worried about, but like that part is like rock solid. I've been using, uh, the VMware, whatever it's called, like the, not the server one, but the other one works workstation player. So yeah, it's, it's great. And yeah, now every, every customer gets their own, their own little virtual machine and we're off to the races. So got it. Yeah.

**Dave Jones:** Right. So you can just save that setup and it's ready, you know, it's always ready to go. Okay. Yeah. Right. See, cause I thought like dual boot was the duck's guts, wasn't it? But you're saying like virtual machine is, is more, if you can save configurations and things like that, if you, I can see big advantages in being able to save configurations and whatnot.

**Chris Gammell:** Yeah. Right. Yeah. And, and I mean, and you could have a windows one versus a, you know, like basically it's kind of platform independent at that point, you know, it's like, uh, the real problem with, so I have a dual, I'm, I am on a dual machine right now, uh, but all the graphics stuff is all messed up from NVIDIA. And so I don't know. I just like my Linux, the Linux side of the machine is just like totally messed up right now. So I'm like, all right, well, I, I can't, I don't have time for this right now. You know, like, it's just like, I don't want to keep dealing with that. So now I just stick in a virtual machine. Right. So cool. Yeah. Yeah. It works. I'll let, I'll let you know how it goes. I'm sure I'll have some, some choice words if it doesn't work. Right.

**Dave Jones:** Excellent.

**Chris Gammell:** So to go back to the, uh, educational thing, did you see the link about the Coursera courses? Yeah. Uh, no. University of Colorado Boulder. It's on the, it's on the, uh, Empire subreddit, but CU Boulder or University of Colorado Boulder. Oh, there it is. They are offering like a whole bunch of like IIoT classes that look pretty interesting, actually, you know, like 10 hours at a time or whatever, but like, or sorry, each, I guess those are the projects that are in there, but there's like 10 different courses and they're like 500 bucks each. So not, not cheap.

**Dave Jones:** I was going to say it said the whole course is $6,000.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Yankee box.

**Chris Gammell:** Yeah. But it's actually like towards, towards a master's degree if you want to. So like, Oh, okay. So you could take like a one, you could take a one off for like 500 bucks or you could like, you know, start, I think you have to actually apply into the other stuff, but I was just like, this is the most targeted program I've seen so far on this sort of thing. I've, I've been following, you know, I get the Coursera emails and this is, you know, this is the one that's, it's pretty close to, you know, industry style things. So that's kind of cool.

**Dave Jones:** Yeah. Cause no, I'm surprised that they're using a Coursera for this. Normally the universities offer them direct. Don't they?

**Chris Gammell:** That's a lot of them have do branded. So like edX is like, uh, that's like MITX and Harvard is, I think they're, I think it's like, there's a couple of big players, but.

**Dave Jones:** Right. Cause there's lots of online, uh, masters these days.

**Chris Gammell:** Yeah. So. Yeah. And this is saying master track. And so it's all like, you know, BS, whatever. That's what I really come. I wonder about this stuff though. Like I would really curious to hear from people, like if you were hiring someone and you see this on someone's resume, like you can go check it out, but like, it's not like, Oh, they have a master's degree from CU Boulder, which, you know. Good school, whatever. But like, does it have the same impact? That's, that's ultimately what it comes down to. At the end of the day, that's all that matters is like, can it get you a job?

**Dave Jones:** I wouldn't care because once you've got experience, your qualifications go down the bottom of your resume.

**Chris Gammell:** Totally. But I'm just saying it's not you or me as hiring people. I think it's more also like institutional type of things. Right. So like, would this get you past the HR to say like, Oh yeah, I've got some master, you know, I've got a master's degree or whatever, or.

**Dave Jones:** I think it would because they're, they're, they're checkbox tickers. Right. So do you have a master's degree? Tick. And if you can legitimately show, they don't care what quality of master's degree.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. They don't care. As long as you meet that tick box and check, that's it. Then your resume gets passed, passed to the next level. Yeah. So yeah, I think it would.

**Chris Gammell:** Yeah. I think it depends where you are in your career, of course, as well.

**Dave Jones:** You know, even, even one of those like non-accredited non-university masters in quote marks, right. That, that would get you through the tick box.

**Chris Gammell:** Uncle Bill's master's program. Yeah.

**Dave Jones:** Uncle Bill's master's, you know, or whatever. But like, I'm sure, you know, we could give examples of, I'm sure you've heard of them. You know, they, they try to give themselves like industry sounding names, you know, like the.

**Chris Gammell:** Like contextual electronics.

**Dave Jones:** Yeah. Contextual electronics. Yeah. And, but they will, they will get you through the checkbox. I'm pretty sure. Let me know if you, if you've got one of those sort of non-accredited, you know, I'm, I'm talking like non-Sydney Accord, non-Washington Accord kind of. What does that mean? Accredited thing. And they, they are the international standard, right? So if you're, if your qualification, if you want your qualifications to be recognized in other countries, right? Most countries are signatories to these accords. So there's the Sydney Accord, the Washington Accord, and the, what's the other one? I've, I've, I've done a video on this and, and the, and these accords are ratified by the various international bodies, right? In various countries. So here it'd be the Institute of Engineers, you know, or Engineers Australia or whatever. And if your, if your degree meets a certain standard, whether it's a master's or bachelor's or a diploma or whatever, you know, two, three or four or five year degree or whatever, it meets one of these accords. Then technically you can move to another country. It's internationally recognized. You can join the local, you know, engineering. So I could go to the U S in Colorado or somewhere and I could get accredited as a, you know, as a, a professional engineer there. If I meet a certain accord.

**Chris Gammell:** Okay. Yeah. Yeah.

**Dave Jones:** Right. And, and some of these things will claim that they're, they'll use wording. You got to be careful. They'll use wording like, uh, you know, we're not accredited, but they'll use a real sneaky wording like we're equivalent to the Sydney Accord or whatever, you know, but they're not actually accredited, you know, they're not officially accredited. So you got to be careful.

**Chris Gammell:** Arduino compatible header.

**Dave Jones:** Yeah. Arduino compatible. Sydney Accord compatible.

**Chris Gammell:** Yeah. Right. Right. Right. Right.

**Dave Jones:** So yeah. Anyway. So that's, yes. So the proper ones will be accredited. Um, and this is, it was talked about recently on the forum. Somebody asked, Oh, is this degree, is this a three year degree I'm doing? Is this equivalent to a four year? And, you know, we're going through all the various things that are actually related. To that very, the various technical things. And the bottom line is, no, it wasn't because it wasn't an, it didn't meet the certain accord that you needed to be internationally recognized as a four year degree. So yeah, you have to be careful. Well, that's, I know it's forward is bad shit.

**Chris Gammell:** No, no, I was laughing because like, cause I was scrolling down for the new thing and you made that noise and I had just scrolled past a picture of Kermit and I was like, Oh, that sounds like Kermit.

**Dave Jones:** Anyway, I've done a video number 1175, how to become a professional engineer. And it talks about all the accords and things like that. So I got it. Okay, cool. Yep.

**Chris Gammell:** That's great. That's great. Well, I, like I said, I, I'm mostly interested in if people are actually taking these things, you know, like at the end of the day, that's like some of the, the knowledge is interesting, but like, I don't really have any good way to know how good these classes are. Like some of the stuff they mentioned too, is like, like modeling and debugging embedded systems is like system C it's like, Oh, okay. Well, yeah, I'm sure that that's useful in some places, but like, is that directly applicable to anything I need? No, probably not. And like, same thing with like, you know, using, uh, I don't know the, I think they were using a bunch of, uh, P sock type stuff. It's like, Oh, P socks cool, but I'm not, they're so expensive. I'm not, I'm not, I'm not using them these days, you know, like it's just, and so like how practical is this? If I wanted to go and take something like this, you know? So generally curious.

**Dave Jones:** Yeah, really. You know, it's not something you can do on a whim, right? This is very expensive, you know, unless you use a cash to throw away, you know, you've got to be serious. It's because generally speaking, it doesn't like, it's like, it's okay. If you list, Oh, I've done a couple of little short courses on your resume or whatever, but yeah, it shows that you're, you know, you're actually, actually proactive and learning stuff on your own. Yeah. Yeah. Um, but generally it's like kind of meh, you know, it's not as, as is most of these. Oh, once I said, once you've got experience, everyone looking at anyone, any engineering person looking at your resume just goes meh at, at, at any formal experience. Oh yeah. Got a degree, meh, done this course, meh, you know, it's like, what have you done? That's all I care about.

**Chris Gammell:** It would make sense if like, it was, uh, you know, it was like leading edge technology. You couldn't find anywhere else like that, that, that could like, so say you were like doing like, like a machine vision thing and like, you just can't, you know, go and pick it up and do a thing. Yeah. Like, yeah, of course might make sense for that. Oh yeah. Yeah. Yeah.

**Dave Jones:** Absolutely.

**Chris Gammell:** Okay. I want to go build a blinky board. It's like, well, there's, there's lots of ways to do that. That there's not a $500 course, you know?

**Dave Jones:** Yes. If you're going for a, yeah, as I said, let's say you're going for a vision engineering job or something, you know, they need someone specific vision engineering experience. Having that you would then, this is why you tailor your resume for each job, right? Don't just send your standard resume to each job, right? You look at the things that they're after and then you highlight those. And I'd put, I would then move that right to the top of my resume, right? If I've done a short course on some course online or at some university, you know, just one, one little class that's done vision systems, right? I'd put that as a key highlight right at the top of my resume. Yeah. Right. I would definitely do that. You wouldn't bury it away down the bottom like you would for, you know, some other, you're going for some other power supply job. They don't care that you've done a vision engineering course.

**Chris Gammell:** Well, what if you're trying to, what if you're trying to remotely troubleshoot it though, Dave?

**Dave Jones:** What's that got to do with it?

**Chris Gammell:** Well, you set up your vision system to do your remote troubleshooting. Come on.

**Dave Jones:** Oh boy. Anyway.

**Chris Gammell:** Yep.

**Dave Jones:** Dublin Accord is the other one.

**Chris Gammell:** Dublin. Dublin.

**Dave Jones:** Washington, Sydney, and Dublin are the three accords. Mental block.

**Chris Gammell:** Yep. Yep. Anyway. Someone had asked on the forum for some guidance. Again, student, this is a very student centric kind of thing or school centric thing.

**Dave Jones:** Which forum are you talking about?

**Chris Gammell:** This is on the subrouter rather guidance for electrical engineering students.

**Dave Jones:** Oh, okay. Yes. Well, that's not a forum. Reddit's not a forum, is it? Reddit's Reddit.

**Chris Gammell:** Reddit's the front page of the internet, Dave. That's what they say. Ugh. Right. Yeah. Gross.

**Dave Jones:** Isn't it like going down the toilet, Reddit or something? I don't know. I don't use it really. I don't, yeah. I don't.

**Chris Gammell:** I try not to too much. It's snuck back in my life, unfortunately. Oh, right. Okay. Like caffeine, it is snuck back in my life. They both are very addictive. Who's? So this is Pablo, the ghost beater.

**Dave Jones:** Obviously. Yep.

**Chris Gammell:** Yeah. Handles being what they are. Let's see. As you know, the curriculum is extremely challenging. Yep. And we have doubts. Yep. Did you or Dave ever struggle like this with the understanding, the fundamental of the core? Sorry. Whether fundamental understanding of the core concepts is as strong as it should be. So I should have read this beforehand.

**Dave Jones:** Yeah, we should have. The curriculum is right. He's doing a BS in electrical engineering. The curriculum is extremely challenging. Yes, it is. And I'm sure it's to do with, it's not to do with the electronics part of it. It's to do with the maths and the physics. It's the maths and the physics. And I always hated it. It was like, oh God, you know, it was like, yeah, it was, it was just not my thing. It was just, oh, yep. Yes. So we did. Everyone struggles with that. Unless you're a math nerd. Yeah. Some people love the math and like, that's great. Great. Excellent. If you love them, if you, if that's your bread and butter and engineering degree is probably going to be a piece of cake for you. Right.

**Chris Gammell:** I would agree with that.

**Dave Jones:** Yep. Yep.

**Chris Gammell:** And I think like, honestly, I think the, so when I think about like the, the learning process in general and like how long it took, took me specifically, not other people, me specifically to get to like the point of like actual, like, like light bulb turn on understanding. It took years sometimes. Like it really did. And like so much of it, unfortunately with, with education systems, it's so much of it is the focus is on getting through it and getting to the grade and like, you know, getting to the next thing and not flunking out. And it's like, you know, there's some practical stuff in there that sucks. And that's where the struggle comes in. I think, you know, you have to pass calculus too, you have to, you know, do this, you have to do that. And it's like, but really you're there for the, the understanding. And if you can try and pair the actual, like, like men, it's all about mental models for me, like being able to visualize a thing and then reconstruct it. So I think about things like my physics of semiconductor class. I think I've said on here before, I wish I could take it now because like now that I actually have mental models built up around like just how, how a diode or an led works. Right. And then like thinking about like, Oh, talking about what was that?

**Dave Jones:** Are you saying it needs to be contextual?

**Chris Gammell:** Oh, nice. Yes. Yes. I am good. Yes. But like thinking about that and like thinking about like, like the, the carriers and things like that and like the math of it all, that's when it all makes sense. Once you've used an led enough to be like, Oh, why is it 0.7 volts? And then you like go and you look at the physics and you look at like all the materials and like the electron, the electrons specifically that like how that stuff builds up and the voltages that builds up. It's like, Oh, that is, that is frigging interesting.

**Dave Jones:** Well, it's not to everyone. I'm sorry. It's like, yeah, too. No, it's seriously not interesting to everyone.

**Chris Gammell:** Well, I just mean like there are a lot of engineers who could not give a shit from, from the top down. It's much more interesting because you know, at the end of the day, it's an led turning on versus the bottom up where it's just like, Oh, equation. Oh, equation. Oh, equation. What, what the hell am I doing this for? It doesn't make any sense. I'm doing this for the grade. And then at the end, yeah, I guess the led maybe lit up. Who knows? Like I'm still stuck in the math over here. Like, you know, so, uh, yep.

**Dave Jones:** You would, I would like to think that any engineer would find that interesting.

**Dave Jones:** Well, yeah.

**Dave Jones:** But any, any true engineer would find, you know, once they realize all this sort of stuff, they would go, Oh yeah, that's interesting. But, uh, you know, unfortunately there's a lot that just don't care. And, uh, and you can still be a good, a great engineer without caring about that sort of stuff, without finding that sort of stuff interesting. Yeah.

**Chris Gammell:** Like you can be attentive to detail and care about your job and all those other things, but okay. Yeah. I see.

**Dave Jones:** Yeah. Because of course, engineering is more of an apply. Engineering is an applied science, right? That is literally what engineering is. It is applied science. You apply it in a practical way. It's very, you know, not that often do you have to go back to, you know, basic physics principles and things like that.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. As, as, as I said before, you can be an electronics design engineer, go your entire career without solving an integral or without going back to basic physics, you can have a, you know, your entire career without having to do that. But others, I don't know, you might find yourself in a field where no, you are dealing with that physics on a daily basis. Right.

**Chris Gammell:** That's right. Yeah. Yeah. I think it, it depends. It depends on which, which, you know, which rabbit hole you dive down. Right. I mean, if you're, if you're building the spice programs, if you're a Mike Englehart and you're, you know, building the spice programs, like, yeah, you better know your math and your physics and your, you know, your programming really well. Right. If you're, you know, making, you know, if you're applying.

**Dave Jones:** Well, that's, that's almost pure math. That's, that's not physics. That's almost like you'd need a degree in pure maths to do a simulate right simulation software. Perhaps I would be guessing that you wouldn't actually get into the physics of it unless you're modeling things like, you know, the thermal properties of components. Like you're building a model for how a, how a semiconductor changes based on temperature and things like that for your Monte Carlo analysis, for your thermal Monte Carlo stuff. And, you know, all that sort of goody, goody stuff. But, um, I don't know how many people out there have written. Well, we have haven't had a guest on the show. Who's written.

**Chris Gammell:** That's right. Yeah. Right.

**Dave Jones:** Simulation software, but there's not many, there's not many out there. Yeah. Oh boy.

**Chris Gammell:** And then when I think about the, you know, the other things that I've done in engineering though, like as much as, you know, knowing the physics might be in, you know, a very important thing. Like some of the better engineers I knew were the ones who were like, were building engine, building relationships with like FAEs and salespeople and like understanding how to get early information and how to like navigate meetings and how to like construct project schedules. And, you know, like engineering is just so broad that it's, you know, you gotta, you gotta be well-rounded in some ways like that. Like, you know, around here we like electronics, of course. But like some of those other soft things help as well. And as much as I, I don't particularly think that, you know, the university system do a great job with that. They tried, uh, at least for me. Right. But I don't think it was like, I don't think me taking three semesters of Japanese ended up helping me.

**Dave Jones:** Right. Uh, with any of my class stuff, you know, it was, it was the thing to do in the eighties because Japan, you know, all the best stuff's made in Japan, right? Back in the eighties.

**Chris Gammell:** That's right. That's right. Yeah. And, or, or the early two thousands, apparently I was a little behind the curve, you know?

**Dave Jones:** Right. That was still a carry. I think that was still a course, uh, carry on from the eighties, just like using an old dev tool.

**Chris Gammell:** Yeah. Uh, well it did actually. So when I was watching this PS five teardown the, um, so this is a link that's on the, uh, the subreddit as well. There's a PlayStation five teardown from an engineer at Sony. And he's like just talking in Japanese the whole time. And it's like, Oh, I remember like listening to a lunch in Japanese. I don't, I don't understand anything these days, of course, but I always liked the sound of Japanese. So, and it is a great, have you seen this thing? The PS five teardown?

**Dave Jones:** No, no, I haven't. I didn't even know it was physically. Is it actually released yet?

**Chris Gammell:** I don't know. I didn't think it was. I think it's maybe pre-order, but I don't really, I don't play games. So who did the teardown? Who got one? It's it's no, no, it's Sony did it.

**Dave Jones:** Oh, Sony did it.

**Chris Gammell:** Yeah. That's what's interesting. It's on the PlayStation YouTube channel. Yeah.

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** I'm going to take it all the way apart though. And it's, it is beautifully built. I mean, who takes it apart?

**Dave Jones:** Is it one of their engineers or is it?

**Chris Gammell:** I think so. So I don't know. They don't say who it is. I don't think they do. All right. But yeah, he's just, you know, explaining the whole time. It's a brilliant idea actually, you know, from like a, I had not seen this of like a company tearing down their own thing like this, but it's like, right. They know it's going to happen anyway. So why wouldn't you, you know, it's great.

**Dave Jones:** Yeah, of course. I don't know. That's totally getting ahead of the curve. Why not? And I'm sure it's got huge production values, right? Sure. It's got nice, nice production values.

**Chris Gammell:** Beautifully done. Like the. Oh, here we go.

**Dave Jones:** No, it's a, oh, Yasuhiro Utturi, the vice president of the mechanical design department, hardware design division. So yeah, they've got one of their heads.

**Chris Gammell:** The case design on this thing is amazing. So it's like all built around the fan system and it looks like two pieces of paper kind of folded over. Like it almost looks like a book that's being peeled apart, but the whole center thing, you like.

**Dave Jones:** Oh, okay. So it's mostly about the mechanical aspects of it. That's why they've got the vice president of mechanical. Yes. That's sort of like, right. Rather than a. One of us.

**Chris Gammell:** I mean, they, they, they point out one of us, one of us. Yep. So yeah, I mean, they point out like, they have like notations of like what everything is, but yeah, they don't, you know, it's not like deep dive and anything, but also at the same time, like, you know, it's an AMD Ryzen processor on there. It's like, what are they going to do? Like, you know, peel that thing back and like, look at the silicon. Not really. So, I mean, the heat sink though is massive. It's awesome. So.

**Dave Jones:** Right. Oh yeah. It's just, it's just all a pure mechanical and it looks like, like thermals and physical construction tear down. They don't really go into. Yeah. I guess so.

**Chris Gammell:** But I mean, like, I don't know. It's just a computer really.

**Dave Jones:** Oh yeah. Show on the board. There you go.

**Chris Gammell:** You know, it's a fancy, fancy desktop. Yeah.

**Dave Jones:** CPU is eight core. Oh, okay. AMD Ryzen Zen 2. Okay. Whatever the hell Zen 2 is. I don't keep track of those things.

**Chris Gammell:** It is one of the newer graphics lines from AMD.

**Dave Jones:** Yes, of course.

**Chris Gammell:** I guess.

**Dave Jones:** I don't know. Yeah. Big chunky copper on the board. I'd love to see big chunky exposed copper. Yeah. It always gets me excited.

**Chris Gammell:** Yeah, no, it's beautiful looking products.

**Dave Jones:** All right. Can we get back to the question? Because Pablo. Yes. Pablo the ghost beater had a question specifically for me. Oh yeah. Which is an interesting question. Lifting the curtain here.

**Chris Gammell:** This is a little, this is a little, you know, it's a little hero worshipy, you know.

**Dave Jones:** Hero worshipy. The question is also a question for Dave. We know you are on, you are an off the cuff, a cusp, off the cuff. I like to say off the cusp YouTuber for the most part. Pretty much. That's no entirely. Almost. Okay.

**Chris Gammell:** No, I'd say your fundamental Friday things were used to be, you know, prepared.

**Dave Jones:** Well, no, not really. No, I'll go into that. But sometimes the knowledge and details you have about a particular subject are incredible. Do you spend time ramping back up on the video subject matter?

**Chris Gammell:** Jeez, Dave. Why did you want to read this, Dave?

**Dave Jones:** Prior to shooting or is all of this knowledge just in your brain? Okay. Interesting. It depends on the video. Obviously, like if I'm doing a teardown video, for example, that's just stand by on the camera, press record, tear it down and my instant reaction and first comment as I tear it down.

**Chris Gammell:** Right. Yeah. Yeah.

**Dave Jones:** So I don't tear it down and sit there. Oh, this would be interesting to talk about and make notes and things like that. It's like, that's why I'll either miss things all the time or I'll rant on for 10 minutes about some, you know, obscure screw, right, in the thing. Because I don't know, I've got a story to tell. It just pops into my head. Right. It's stuff like that. So yes, all of my video, I don't do scripts at all. All of my videos are off the cuff. I'm sure you don't do scripts either, right, Chris, when you were doing your videos?

**Chris Gammell:** That's correct. Yep.

**Dave Jones:** Fundamental. Yeah. We just start yapping. For like something like a Fundamentals Friday video. Yes, I'll do some prep work. You know, if I'm doing the whiteboard video, I'll do some prep work just to make sure I'm not goofing something.

**Chris Gammell:** Right. Because I don't want to, you know, because it's... I'll usually like record it five times in the first four times or train wrecks. And the fifth time is like...

**Dave Jones:** Mine's pretty much the first time. Like often, I've done a video explaining this. My supporters have access to it. And like explaining my process and stuff like that. I will, like, I'm pretty much off the cuff. Like even though I've done some prep work beforehand for a Fundamentals Friday video, and I might have some, like I'll literally just have points. Like I'll go, oh yeah, I probably want to talk about it, you know, like a Post-it note with a couple of asterisk points on it. Right. Just so I don't skip a step pretty much. So I just outlined that. But I don't know what I'm going to say until I actually press record. Right. It just sort of comes out. And like you, I might have to do it maybe twice. You might do it about five times. Yeah, five times. Yeah. The shorter for me. Yeah. Or my former psychic, David, he used to do it 10 times. Right. Because he was like super paranoid about getting it all 100% absolutely perfect. Right. Whereas I don't care. It's like, eh, good enough. You know. And yeah, I think I got my point across, which is, so I'll make up some point that I'm trying to get across and I'll press record and then I'll start yapping. And if I think in real time, as I'm saying it, my brain's going thinking, is this right? Is this getting the point across in a reasonable way? And if not, I'll stop and I'll re-say it. I'll say it in a slightly different way, perhaps. Generally, like, you know, most of it's, yeah, it's all pretty much off the cuff and it's coming from my head. Although, you know, there's formulas that I won't remember. Right. There's details. There's math stuff. Right. Just like you. Like you said that you didn't like the maths. It wasn't your thing.

**Chris Gammell:** Right.

**Dave Jones:** Same here.

**Chris Gammell:** Still not. Yeah. Not past tense. Present tense as well.

**Dave Jones:** Like right now, if I asked you to solve a triple integral, would you be able to do it?

**Speaker ?:** No.

**Dave Jones:** No. See? Hold a gun to my head.

**Chris Gammell:** I still, I don't know how to do it.

**Dave Jones:** I still wouldn't be able to do it. Right. Yet, I learned that stuff. Right. And I have no idea. Right. I couldn't. Yeah. Hold a gun to my head. I could not do it. Right. Even the most, like, even some formulas you'd think are really fundamental. I've totally forgotten because I've never used them since I started them. Yeah. Yeah. It's an atrophy thing, right? Yeah. And yet other, like, I will remember the most obscure detail from a magazine article I read back in the 70s. Right. It's really weird, the stuff that sticks in my head.

**Chris Gammell:** Why do you think that? Is it something specific, like an image? Or is it because, like, the experience that you had around it? Like, what actually?

**Dave Jones:** Yeah. It's, you know, just me alone with my magazines. And that's all I had. So I was hyper-focused on it. And I can still picture me, you know, reading that magazine in my shed. You know? I can still visualize it. You know? I can, like. That's great. Yeah. It's, you know, it's weird. Yet I can't remember the formulas that I had to study for, you know? Because I just didn't care, you know? I was like, oh, shit. I've got to learn this crap to pass this.

**Chris Gammell:** Right. Right. Exactly. Just to get through it. Yeah.

**Dave Jones:** Exactly. And it didn't interest me. So it didn't stick in there. And so, yes. Yeah. A good lot of the stuff just pops out of my memory. It's like, this is why I've always said, because I've been, you know, a hobbyist since I was, like, five or six. Right? And then I was, like, by the time I went to formally study engineering, right, I like to think that I had, like, I had near it, like, I had probably, like, a decade before I studied engineering, I had a decade of this hobby experience, just, you know, reading and memorizing all this stuff, which I didn't really understand at the time.

**Chris Gammell:** Right. Yeah. Yeah. You'd, like, unwind it in your brain, right?

**Dave Jones:** Yeah. Like, you know, I'm 10 years old and I'm reading about, you know, there's something I don't really understand. I just know I love engineering. I love electronics and stuff. So I'm just, you know, absorbing all this stuff. And then when I go to learn it formally, boom, it just floods out. And it's like, oh, you know, it just pops out. Right? I'm the one who's always putting up my hand, you know, like answering the questions in the class because it just, boom, I just know it. It just, like, floods out later because my head's just full of all this stuff that when I went to formally learn it.

**Chris Gammell:** And it's been flooding out ever since, folks. It was flooding out ever since.

**Dave Jones:** Leaky tap. That's right. And, yeah. So even if you don't, even if you don't understand what you're learning at the time, it does, I find it always pops out later. Like, you know, oh, one little experience I had in a job 20 years ago, that'll just suddenly pop out in my mind. You know, when I'm talking about a board or, you know, I'm going through a teardown, I'm talking about a layout or whatever. Boom. Out it comes. This little obscure issue I had 20 years ago just pops out. And, you know, I'll waffle on for five or 10 minutes talking about that issue.

**Chris Gammell:** So I think that's a good point, though, like from a learning perspective, too, right? So to go back to the struggling and stuff like that, like so much of what we're talking, what Dave's talking about here, what we've been talking about is like pattern matching, right? That's what humans are really, really good at is like pattern matching. Yeah, the brain's great. And so some of it is just honestly getting exposure to it, struggling with it, you know, like Dave said, like sitting in your shed, memorizing things, but also like just kind of struggling with things, trying to figure out what's going on. And so I think one of the problems is that like, from my experience for like going into an undergrad program that was like electronics, I just didn't have any experience there, right? So Dave had all this stuff popping on his head. I was like, there's nothing here. You know, it's just all I had was the math to lean on. I didn't have anything else to contextualize against. And so like, that's, that's the problem. So that's why we always say, go and try and get some of that outside experience if you can, not just for, you know, contextualizing what's actually doing here, but also to just keep motivated, right? Make sure you honestly make sure you like it, right? That's, that's the other thing. I know some engineers that just don't like being engineers. And it's like, yeah, I know. If you figured out early enough, maybe you could switch to mechanical or, you know, business or whatever, whatever floats your boat, but like figure that out as soon as possible.

**Dave Jones:** That was my biggest shock. When I went to university, it was like, are you like, you know, meeting the other people it's like, Oh, like I'm super excited about electronics. Right. Nobody else gave a shit. Right. It was like, I'm talking like 95% plus did not care. It's like, why are you here? If you don't like it, if you don't care, why aren't you enthusiastic about it? It's like, wow, what a shock, you know? I think that's totally normal though.

**Chris Gammell:** I think that, you know, like for granted, the timing was not great, but like, you know, late nineties, like there was a resurgence of, you know, like there was all the opto stuff and like, so there was like programs that were popping up a lot and people were like, Oh, you can get really good jobs in engineering doing this kind of thing. Like, I would say that didn't influence me. Like, yeah, the money was an interesting thing, but you know, that, uh, some people are just doing it for that.

**Dave Jones:** And it's like that, that, Oh, they're doing it because their parents want them to study something. All their friends went into it. So they go, Oh, I don't know. Exactly. Yeah. I'm doing engineering.

**Chris Gammell:** I guess, you know, they'll shut my parents up. Figuring out if you actually like it is like one of the most important things. Cause if you do, right. If you get to really like it, like, like a young David L Jones did, right. You can get through the, like, you can get through that crap math, you know, like you're just like, Oh yeah, it's just the thing I have to do. And it's, you know, you might have a good reference point for, for the things that you find interesting outside of the math.

**Dave Jones:** So I find that there's vastly more distractions these days. Like back when I was a kid, right. Learning electronics, right. There was no other distractions.

**Chris Gammell:** So they didn't, they just had, did just had a Twitter. They didn't have Tik TOK. Is that what you're saying?

**Dave Jones:** Exactly. No interwebs, you know, like there was just, there was nothing. There was just me in my shed with my magazines. That was it. Right. That was it. That's why I read those things over and over and over and over again. And it was like, and that's why, like I will, uh, when I'm thinking about like when I'm doing a repair start, like I might tell a story, but that's not something that I, you know, I might go, Ooh, this is a trap for young players right here. That's not necessarily something I've been trapped. If that's because I re I read every serviceman column in electronics, Australia magazine, going right back to the 1970s. It's right. Even, even before that, I went back and read all of the, you know, all of the columns. So, you know, that, that had this, so the, these things will just pop out in my head, you know, 30, 20, 30 years.

**Chris Gammell:** Dave's just repackaging old material here, folks. Yeah, I'm just, yeah, exactly. It's like everything I've read. Aren't we all, I mean, even, even you and I right now, even right now we're repackaging old amp hours, right?

**Dave Jones:** Totally. That's where we're being, that's been our career for a decade now. That's right. Yeah. Repackaging old shit. Even, even for the second episode, we'll just rehash and shit from the first episode. Yeah. Why not? Right.

**Dave Jones:** It was, you know, yeah.

**Dave Jones:** It's telling stories.

**Chris Gammell:** Reduce, reuse. Okay.

**Dave Jones:** So yes, to answer Paul Pablo, the ghost beater's question is, um, it's partly, it's half and half, you know, there's a lot of shit up there. I don't know until I start talking and then it pops out.

**Chris Gammell:** Yep.

**Dave Jones:** And yep. Other things. Yeah. I might do some prep work, but no, I don't, I'm not like there's, there's other YouTubers out there who do, um, engineering videos and they'll do, you know, they will do a ton of prep work. So don't necessarily think that because your favorite YouTuber, you know, don't necessarily think that there's some, there's some super genius is what I'm saying is that they know every equation off the top there. They know everything off the top of their head. No, it's, um, there's a lot of YouTube. They will all admit that. Yeah. Google is your friend. Um, it's like, you know, totally. It's yeah. Yep. But even then I get things wrong, you know? Yeah. All right. Yep. So, uh, but I, I like to think that, you know, I'm knowledgeable enough that once I, like, I, I don't have to refresh much. I just got to go, Oh yeah. I remember that formula. Now I remember how that works. You know, it all just sort of like flows back in there. Right. It's all kind of, yeah, it flows back. It comes back pretty quickly. And, and then I, I will figure out my own way to explain it. Now that's why often like I will not do a tutorial video. Unless I can think of a, a different or better way to explain it than somebody else has done before. Right. If, if I'm just going to rehash somebody else's work, I'm not going to bother to do it. I'll just go, well, just go and, you know, buy this textbook or whatever, you know? So there you go. Thank you, Pablo. That's an interesting question.

**Chris Gammell:** Other places for Pablo to go and learn things. One thing is reference design. So I've been following this lately. This is when I posted about MPPT.

**Dave Jones:** This is maximum PowerPoint transfer for those who don't know.

**Chris Gammell:** Or tracking.

**Dave Jones:** I thought it was. Maximum PowerPoint. I didn't realize. Yeah. Once again, you know, it's one of those.

**Chris Gammell:** I, I didn't realize whenever I see these things, I always thought they were built into the chips, like, and like, like the actual charging chips. I thought they had to have everything in there, but I didn't realize that. So the chip that I'm using, the reason I found this is because it's actually the chip that I'm using on my board, my recent board, but it's got like a, a variable impedance input for like a solar panel. And so you can actually do MPPT using that. And it's got an ADC internally.

**Dave Jones:** Why, why are you, why, why are you using that?

**Chris Gammell:** On my board?

**Dave Jones:** I didn't think that was, yeah, the stuff that you're doing. I didn't think that was actually. Yeah.

**Chris Gammell:** So I wanted to, well, honestly, it was, it was kismet. It was because I was looking through the list of things that I wanted. And one of the things that I really wanted was a way to back power other stuff. This BQ25895 that I put on the board, it has a thing called PMID. I'm not sure that stands for, it's an acronym for something, but it's basically it's, it's like a high speed charge controller, right? It can do three volts to 3.4 to like 14 volt input. So it can take like solar panel or 12 volt battery inputs. And then it'll bucket down for battery charging. And then there's also just a system output. But the cool thing is then you can turn off battery charging and then instead back power something else like USB on the go. And so because I've made this into like a Raspberry Pi hat, I wanted to be able to go and power, back power that Raspberry Pi without a separate supply. And so the idea is that it's a solar panel input, charges the battery. You can turn that off and go and power the Pi using the solar panel. If you have it, you wouldn't be charging the battery at that time. But the idea then is the solar panel is just so you can have a solar panel to power this whole, this whole mess of a thing. And it had, it had said MPPT in like the, the digi key thing and like some of the marketing specs, but I couldn't find anything else. It turns out it's just this application note where MPPT is like this algorithm where you're basically trying, you know, you're doing, you're trying, you basically excite the solar cell and then you kind of back off and you see what it does. And then what you do is you actually ratchet the, the input impedance using a override squared C. And so this whole, this app note here is basically how to go and do that. So you have an internal ADC, you measure the voltage, you, uh, you see what the voltage is, you see what the current is. Those all measured internally. And then, and then you like step up to the next level, you change the impedance, you step up to the next level and you basically go until you, you know, go over the top of that MPPT curve and then you get the maximum. And then you can like just set this up as an algorithm. You know, the microcontroller controls this thing and, uh, set it up as an algorithm. And then you can get the maximum out of your solar cell. But then when the sun changes, you know, have throughout the day, you can rerun it all the time. I thought this was always built into the actual charger. And I thought it was actually built into this charger that I bought and designed in, but no, it's actually, it's just capable of, you can do that from a micro externally and then, uh, modulate the input to, to do that sort of thing. So kind of cool.

**Dave Jones:** There are specific MPPT chips that would do this internally, but yours wasn't one of them.

**Chris Gammell:** I forget what the part number was. I was talking to my, uh, Dave Young, actually, I was talking to him about, he's got a board that he designed, uh, for Voltaic, which is a solar panel manufacturer. And he designed a board for them that is like a reference design. And instead it has the BQ 24, six, five Oh, and that actually does have MPPT internally, but it's got a whole bunch of like external fats you have to use. And then, you know, there's like really, really beefy diode. And then it's got like really high leakage occurrence and stuff like that too. So it's really high powered and it's good for big systems, but it's not, it's not what I needed. So, so I can still do it, but it's, uh, yeah, anyway, so it was cool. I'm very excited about it. I got to write the algorithm, but that's neat. Yeah. And the app note teaches me. So like, that's, this is all going back to Pablo. You can go and learn this stuff from resources like this. Yeah. Yeah. App notes. Yeah. Love them.

**Dave Jones:** Yeah. Yeah. I'll get lots of inspiration from app notes and things like that. They're yeah. They're really cool.

**Chris Gammell:** Uh, there's also YouTube channels, of course. Uh, there's GitHub repos. Did you see the GitHub repo with the, uh, where is it? Someone built a one megahertz to six gigahertz USB based vector network analyzer. Like, holy crap. This thing's amazing. Yeah. Yeah. So it's a Spartan six on board. It's got all the hardware. It's his first attempt at a VNA, which is crazy. But, uh, you know, this could actually be like a candidate for a low cost VNA. We'll see.

**Dave Jones:** I thought there was a low cost. Isn't the nano VNA, the duck's guts? Everyone's.

**Chris Gammell:** Yes. But that only goes up to a gigahertz, I think. So.

**Dave Jones:** Oh, okay.

**Chris Gammell:** Like even getting to 2.4 gigahertz. Right. So if you need a VNA for like testing your antenna on your Bluetooth thingy or your wifi thingy, it's pretty expensive still. Uh, I think there might be one or two things. Oh, there's the one that, uh, Sharia reviewed. There's like a handheld one. That's from a China brand that I looked at.

**Dave Jones:** Right. Yes. I remember. It's just okay. Was that his conclusion? That? Yeah.

**Chris Gammell:** It's just okay. That was pretty much his conclusion. I'll link that into it. It was, it was a great review, of course. Right. The Sharia, but, um.

**Dave Jones:** Oh, yeah, of course. No. Yeah. Very in depth.

**Chris Gammell:** It's called Deep Ace at the Deep Trace. Deep Ace. I forget. I think it's Deep Ace. Um, uh, but it's a handheld, which is cool. And, uh, but not probably not what you want. You know, if you need like really good, uh, dynamic range, that's not it. But if you need handheld, then it's great. You know, that's my summary of the summary. You know, just a remix.

**Dave Jones:** Speaking of battery charging, speaking of battery charging, can we talk quickly about my electric car?

**Chris Gammell:** What about it?

**Dave Jones:** Because I fast charged it for the first time the other day.

**Chris Gammell:** I thought you were going to talk about something else. What? The, uh.

**Dave Jones:** Well, what do you think I was going to talk about?

**Chris Gammell:** That photo you sent me. The wanker plates.

**Dave Jones:** Oh, right. No. Okay.

**Dave Jones:** Let's not talk about that. All right. Nope. Okay. Nope. Charging. Charging the electric vehicle. Fast charging. Right. I was, yeah, fast charged it for the first time. So I went and plugged into an Australian designed and manufactured. Thank you very much. Tritium charger. Um, I, hopefully, um, I'm going to ask them to maybe. Oh, great. Yeah. Episode. Yeah. That'd be nice. And, uh, yeah. So they, um, have these 50, 50 kilowatt chargers, right? 50 kilowatt capable. They might make bigger ones, but anyway, our national roads and motor association, they've installed these free super DC fast chargers around, you know, in various locations around. So, so I went to use one and I thought, oh, great. I can charge at 50 kilowatts. And I knew that my car could do a 50 kilowatt charging. That was like the maximum it'd charge at. Right. And, uh, if, if you don't know, there's basically three levels for the Hyundai Ionic. There's the 2.4 kilowatt or 2.2 kilowatt, which is your standard 240 volt wall outlet. Right. And then there's a seven kilowatts, which is single phase AC charging. It won't do three phase charging, which would be 22 kilowatts. Unfortunately, it won't do that, but then it'll do DC fast charging, which is up to 50 kilowatts. So I thought, okay, this is a 50 kilowatt station. Nobody else is using it. Like there's two of them there. Nobody else is using it. Cause there's not many electric cars in Australia. No one else is using it. So I should be able to get the full 50 kilowatts. So I plug it in and I go look at the display on the, on the dash. And it says 25 kilowatts. Now what the hell's going on? And, uh, and I'm, I'll send you the link here.

**Chris Gammell:** I was going to say, would you like shouting? You're like, I want my money back for my free electricity.

**Dave Jones:** Oh, yes. It's in my video on my second channel. You can go see it. And I felt ripped off and, uh, here we go. I'll give it to you in the Zencaster chat. Okay. There it is. And 25 kilowatts. And then I hopped out and we're talking about it and stuff on camera. And then I went back in, checked it again. It's dropped down to 11 kilowatts. And I went, what the hell's going on here? I've ripped off. Like, is there, you know, where's the limit? Like I figured it was the car.

**Chris Gammell:** I got my free power, but it's not showing up fast enough.

**Dave Jones:** Yeah. I expect that. Like I'm using a 50 kilowatt charger. Why can I charge at 50 kilowatts? It's because I've got the new model. If you had the old model, it would. So Chris, take a look at these graphs and we'll provide a link down below. This is fascinating. They've shown the different models. The one in green. Have you got the graph there?

**Chris Gammell:** I have the graph. Yep.

**Dave Jones:** Okay. The one in green is the previous model, right? That's like the 2019 model with a 28 kilowatt hour pack, right? Mine's got a 38 kilowatt hour pack and both of them charging at 50 kilowatts. Mine will only charge at 50, you know, up almost 50 kilowatts up until 50% of the battery pack. So if it's above 50%, then they step it down. The bastards. Why?

**Chris Gammell:** It's because it's probably in voltage limit mode at that point.

**Dave Jones:** No, no, no, no. There, no. Take a look at the previous model.

**Chris Gammell:** Oh yeah, you're right.

**Dave Jones:** The previous model has a flat line right up until 80%, right? This one has the, the yellow one is my one. This is the new 2020 model. It's got steps. So at 50%, it deliberately steps down to about 35 kilowatts. Then at 60. So you don't think it's, what do you think it's for?

**Chris Gammell:** Like heat, heat then? Or what do you.

**Dave Jones:** It is for, it's for battery management. I think it's for pack management, longevity of the pack. Cause they're now offering eight year warranties on these packs. So I think they're being super cautious by going, probably wasn't a good idea to allow people to fast charge these things right up to 80%. So they've implemented this step algorithm and I was, and, and I happened to be just on the cusp of when it was 25 kilowatts. So I started charging at 74% battery and I was getting 25 kilowatts. And then by the time I stepped out of the car and then came back, it had dropped down to 11, which is, I was going into the next step phase of the charge. And this is only on this new model.

**Chris Gammell:** Do you think maybe they'll update it later though, with like firmware or something? Like if they figure out better characteristics?

**Dave Jones:** No, no, no. This is very deliberate. This is, this is a money saving thing.

**Chris Gammell:** This isn't, this isn't capability.

**Dave Jones:** No, no, no. This isn't capability. You can fast charge that pack right up to a hundred percent if you're damn well wanted.

**Chris Gammell:** But they want to, they want to save their money on, on, on the, uh, for, because of the, the warranty.

**Dave Jones:** They want to save it because they're offering eight year warranties on the pack. They don't want to suddenly find in seven years time that half of the cars out there because they've been DC fast charged a lot are all dying, you know, and they, and they have to pony up the replacement pack, which is going to cost them a fortune. So I think they're being super cautious. So whether or not that is a learned experience from the previous models or not, I don't think so. Cause the Ionic hasn't been out long enough for, I think there to be any issues with the packs. So it, it isn't like the leaf, which has been around for eight year, eight, nine, nine years now. Right. And a lot of those old leaf packs are dead, right. They'd a lot lost, you know, they've lost a crap ton of capacity and they've had to change a lot of those under warranty.

**Chris Gammell:** So they, and they started, they started at low capacity too. So then they're like, they're like, basically, Oh yeah. You can use this to drive on the block and come home and that's about it.

**Dave Jones:** And come home and that's it. Yeah. It's a, basically a novelty. If you buy an old, you know, 2012, 2014 leaf, it's like a novelty car. Yeah. Clown car.

**Dave Jones:** And anyway, it's, it's interesting. So yeah, I was like, I was puzzling. I knew the car was doing this, but I didn't. Yeah. Somebody's published a graph. And I think I might go out and get my own graph. I might discharge it to like 5%, go to one of these things, put a camera on it for, for an hour while it's charging from zero to a hundred percent. And we can possibly see this step.

**Chris Gammell:** Yeah.

**Dave Jones:** Step response. So. Yeah. This is interesting.

**Chris Gammell:** I mean, it is interesting following your, your stuff here. The, I mean, it's for you. It's, it's actually like how you get around. So like, I get, it's actually much more visceral for you, but like, I am digging the other stuff that you're doing with like the bus thing that I, if people haven't watched those bus videos that Dave did, I thought that was really, really cool. Like that. And just like, that is, I don't know the, the fact that it's like, it's just a bus, right? I mean, it's just like, it's just.

**Dave Jones:** Yeah. It's, it's, it's just a regular bus.

**Chris Gammell:** That is the greatest hope for me. Like when solar panels got cheap and it's just like, oh yeah, it's just like a good economic decision. When buses are just, you know, like they're all the maintenance costs are better and you know, it's less diesel and it's cheaper. And it's like, when it becomes like an economic decision, it's like, man, it's just like, it makes me feel like warm and fuzzy. Cause I'm like, there's no way that that's not going to be the answer now. You know what I mean? Like it's not like, oh, well.

**Dave Jones:** Right. It all comes down to economics. Nobody, you know, nobody really, when they, when, when the rubber hits the road, nobody really cares about the environment. When rubber hits the road, nobody really cares about 3000 people in Australia dying from air pollution due to vehicles every year. Right. You think COVID is a problem. Oh, keyword. I don't think this will get indexed. Yeah. No, more people. Die from Australia.

**Chris Gammell:** Let's just make that clear. Yeah.

**Dave Jones:** The U S in Australia. Anyway, air pollution problem, right. Which nobody gives a shit about, but when it comes, if it saves the money, you're damn right. They're going to do it.

**Chris Gammell:** It becomes a, it becomes a, like a non-political non like lifestyle issue. It's just literally just money. And like, oh man, I love that because the market, because for me it is, it is like a visceral thing. Like I want it to be like this. And like when the money lines up with it, it's like, oh, hell yes.

**Dave Jones:** Yep. Yeah. And like the other stuff you said too, it's clean.

**Chris Gammell:** It smells less. It, you know, like it's quieter. Like all these other things are great too, but once the money lines up, boom. Yes.

**Dave Jones:** Yep. That's the answer. That's it. It's done it. Yeah. It's done. So anyway, this is, I think this is a very interesting example. I'm going to have to dig up more data on this. And if I can, then I might, might do a video on it. This is preventative cost engineering. This is preventative. What would be the correct term? Design for longevity. It's preventative because they're designed for long, designed for product longevity. Yes. Yes. Because in this market, they've been forced, you know, when, you know, 20 years ago, if you bought a car, you were lucky to get like a one year warranty on it. Right. Like, you get three years on it. You know, it was a big step when they went from one to three year warranty. And then some manufacturers came out and went, oh, for a four year warranty, then five. And then it was seven. Right. And now it's like you, you buy a new car and.

**Chris Gammell:** New powertrain warranty has come for 10 years or 10,000 miles, 100,000 miles.

**Dave Jones:** And 10, 10 years. I know. Exactly. An eight year battery pack warranty. And that's gutsy. Right. That's ballsy when you don't have eight years worth of data on that. Actuarial nightmare.

**Chris Gammell:** Some actuarial is like sitting somewhere just like biting his nails, you know, just like peeing his pants.

**Dave Jones:** I know it's just like having convulsive fits because yeah, it's called up in the fetal position. Yep.

**Dave Jones:** And yeah, so I reckon they've deliberately implemented this really to be on the safe side. So I'd love to talk to the engineers responsible for coming up with this step-based algorithm and what their rationale behind that was. And I'm sure it is a hundred percent preventative long pack longevity because the biggest risk to an electric car battery pack or an electric bus or whatever it is, electric truck, is fast charging. That really damage it. If you fast charge every day, your pack's not going to last very long at all. And they actually warn you in the manual, you know, look, you can fast charge this, but don't do it all the time because you'll just, yeah, shorten your battery life. Guaranteed. So interesting. So cool. Sorry. We're way over our amp power capacity. We were designing for longevity this episode. Hey, that could be the name of this episode. Designing for longevity. Ah, yes. It always comes out, doesn't it? Name just presents itself.

**Chris Gammell:** All right. So Luigi on Twitter, he gave me a potential sign off. So I'm going to try it here today. You know how like I always say what you say and then I'm like, that's not what I'm supposed to say. Here we go though. You know, like when we, when we sign off, you know, like you always say like catch you next time. Catch you next time. Here we go. Ready?

**Dave Jones:** Yeah.

**Chris Gammell:** Thank you for listening. Okay. May all your blinkies shine brightly.

**Dave Jones:** Okay. Catch you next time. Bye.

**Chris Gammell:** This episode was produced by Analog Life LLC and brought to you today by our patrons. Join at patreon.com slash the amp power to get access to our private discord and discounts on amp power swag. A special thanks today to our corporate sponsor, Bino, makers of the Bino Nova.

**Speaker ?:** Thank you.
