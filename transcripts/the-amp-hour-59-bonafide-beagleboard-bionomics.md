---
episode: 59
title: An Interview with Jeff Keyzer and Jason Kridner - Bonafide BeagleBoard Bionomics
url: https://theamphour.com/the-amp-hour-59-bonafide-beagleboard-bionomics/
---

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog. And I'm Chris Gammell from Chris Gammell's Analog Life.

**Jeff Kaiser:** And this is Jeff Kaiser from MightyOhm.com. And Jason Kreidner of Texas Instruments and BeagleBoard.org. Wow. Hey, guys.

**Chris Gammell:** Full house.

**Jeff Kaiser:** Full house. Yeah. Full house.

**Chris Gammell:** Chris invited every band his dog this week, I think.

**Dave Jones:** Dogs are upstairs. They're not coming down. Although the BeagleBoard, I guess the BeagleBoard's got a dog as a logo, right?

**Chris Gammell:** Oh, right. Yes, it does. Welcome back, Jeff. Of the... Thank you. What the third... What have you been described as? The third wheel of...

**Ed McMahon:** The Ed McMahon.

**Chris Gammell:** The...

**Ed McMahon:** Well, the Ed McMahon. Yeah, you know, I... I'd like to take issue with the Ed McMahon. Ah, whatever. I listened to the show last week, you know, and... I was a little bit... I feel like I'm a little better than that. I'm a little better than... Ed McMahon's awesome. Ed McMahon. No, but I actually contribute some technical content to the show. I add value more than just, yes. Yes, sir. That is correct, sir. But I... But I did... I definitely cracked up. I thought it was... It was funny. But come on.

**Jeff Kaiser:** Okay.

**Speaker ?:** Okay.

**Chris Gammell:** And we have Jason Krittner in the house. Welcome, Jason. Thanks for joining us.

**Jeff Kaiser:** Thank you very much. Is it Krittner or Kridner?

**Chris Gammell:** I don't know if we've ever gotten that right.

**Jeff Kaiser:** It's Krittner. It's one of those... It's a German last name. It's one of those things where... It's the Germans. Yeah, yeah. Crazy Germans. Those pesky Germans, yeah. Whenever they came over to the United States, somebody dropped the E out, so...

**Dave Jones:** Ah, yeah. So it was actually immigration officials. That was the problem. Right.

**Jeff Kaiser:** Yeah, yeah. It was crazy Americans. Crazy somebody.

**Ed McMahon:** Yep. But then they saved you from a life of being Kridner, right? Right. Because that's probably how most Americans would have...

**Jeff Kaiser:** It probably did save that, yeah. Because that... Yeah. Yeah. The E did come before the I.

**Ed McMahon:** Except after C. Ah, yeah. Yep. Well, welcome to the show.

**Jeff Kaiser:** Thank you very much. Very excited to be here.

**Ed McMahon:** We've met before, Jason, right? We met at the Maker Faire this year. We did. And I took one of your classes a long time ago at ESC in the Bay Area. So it was a good class. Yes. I'm glad to hear that.

**Jeff Kaiser:** We're going back to Boston later this month, giving some more hands-on classes with the BeagleBoard and doing some more actual interfacing up to electronics. So instead of just more software, it's actually going to be a little bit more interfacing stuff.

**Dave Jones:** Cool. And that's actually how I met Jason, too. I was sitting in a class, and I think I made some snarky remark on Twitter. And Jason took offense, and we met up, and I apologized. Excellent. The rest was history.

**Chris Gammell:** I feel left out here. I haven't met anyone.

**Jeff Kaiser:** Well? Just haven't made enough snarky remarks on Twitter, apparently. Oh, yeah, right. Right.

**Chris Gammell:** Yeah, it's not that 12,000 miles of emotion between us.

**Dave Jones:** So, Jason, how about for the uninitiated? What is BeagleBoard Project? I mean, we've mentioned it on this show before, but just anyone who hasn't heard about it, or maybe you can give us a quick rundown and how it relates to TI and everything else you do.

**Jeff Kaiser:** Yeah, there's a lot of different ways to come at describing it. For the uninitiated, I usually try to describe it as essentially taking the guts of a cell phone and opening it up so that other people can hack on it and make it into what they want. So, you know, the cell phone processors these days are really powerful. Low power, you can do all sorts of crazy things, or it's all sorts of software on it. And the BeagleBoard just sort of blends that world of, you know, embedded electronics and makes it look like a computer so that people who maybe aren't that familiar with doing embedded development can just sort of ease into it from, you know, desktop sort of computer development environment.

**Ed McMahon:** Okay. And if I can ask, where did the name BeagleBoard come from?

**Jeff Kaiser:** Gerald has a beagle. He's a fan of beagles. Underdog, you know, is a beagle. That's the most important thing to remember. Oh, I see. Cool. It's an internal codename. You know how those things stick around. Yeah. Oh, yeah.

**Dave Jones:** Yeah. They're fun to come up with, too. I love coming up with codenames. Come up with some ridiculous stuff.

**Ed McMahon:** So people take this, the BeagleBoard, which I've played a bit with. I've never really gotten heavy into BeagleBoard development, but I've kind of messed around with it. You know, I took the class. The class was cool. You got to run Android on it. You got to run some kind of Linux. I can't remember now. Probably Angstrom.

**Dave Jones:** Angstrom, that's it, yeah.

**Ed McMahon:** Angstrom, yeah. It was Angstrom. And I think there were a couple other things. But maybe for the benefit of me and also our listeners, what are some of the most, or like, what are some of your favorite things that people have done with the BeagleBoard? Aside from give TI a lot of money.

**Jeff Kaiser:** There's been a lot of cool robotic stuff. I think that's where you see most of the projects coming out, doing vision stuff. These autonomous drones. So you see these flying vehicles that go around and recognize objects and actually build out 3D maps. And people put connects on these things. And they run LibFreenect. And they can take in all that data from their connect. And they'll build 3D maps and recognize people's faces. There's build robots that will dance with you. And, you know, those sort of crazy things.

**Chris Gammell:** So is anyone using it to flash an LED? Or am I just too old-fashioned?

**Jeff Kaiser:** So most of the time now when we start a class, you know, I do the here's how to flash an LED exercise. It's a little bit different than, you know, the Arduino Blink. Right. Yeah.

**Chris Gammell:** Because there's quite a lot of people who actually compare it to the Arduino. And they say, well, it's just a more powerful version of the Arduino, really. Because what is actually the hardware processor?

**Jeff Kaiser:** It's totally different.

**Chris Gammell:** The hardware processor. What's that? Sorry, what is? The actual hardware processor used in it. Which one is it?

**Dave Jones:** Yeah, maybe historically if you could tell us too. I mean, like what did it start out as? Because it's changed, right? Yeah.

**Jeff Kaiser:** Oh, it has changed, has it? Okay. Well, yeah, it started out as an OMAP 3 processor, which is the, you know, that brand comes from the cell phone product line for TI. And I don't know if you've heard the DaVinci brand.

**Chris Gammell:** Yes. Yeah, that's the DSP stuff, right?

**Jeff Kaiser:** Video processors with the DSPs. And, you know, really if you look in the guts of the chip, it's the same stuff. But the new one, the Beelboard XM is actually a DaVinci DM3730, but it's still the same guts as an OMAP 3630.

**Chris Gammell:** Right. So it's basically an OMAP processor. And it's in a similar form factor to the Arduino, really. It's just a bare board, right? Is that how it's still sold? I haven't kept up to date on the BeagleBoard market. I'm sorry.

**Jeff Kaiser:** Well, the BeagleBoard includes USB host ports on it, so that's kind of different. Instead of just, you know, being a, you know, bunch of pins to go out and do, you know, direct drive sort of expansion, it's more focused on, you know, expanding with computer peripherals. Although there is an expansion header on there, you know, it's not as extensive. It's only, a lot of it's 1.8 volt. Right. So a lot of the stuff that you would buy off the shelf to try to extend it, you know, you're going to need to add on level shifters. And that becomes a pain in the butt, right?

**Ed McMahon:** Yeah.

**Jeff Kaiser:** Yeah, it does.

**Ed McMahon:** Well, but I think to answer Dave's question, though, you know, it's a bare board. It doesn't come with an enclosure. But unlike the Arduino, it has an HDMI port, right? Right. So you can turn it into a PC. No, the Arduino does not have an HDMI port. But one of the coolest things about the BeagleBoard, I think, is that with only a couple, it's kind of like the Mac Mini of embedded boards, because you just add a keyboard and a mouse with USB, and you can connect a monitor to it with HDMI. And it even has audio output, right? I mean, it's like a, it's almost like a PC, like a single board computer. It's got all the IO just right there.

**Jeff Kaiser:** It is a full computer, right? You can run, you know, Ubuntu Linux, you know, which is the most popular Linux distribution out there. You can just download an SD card image and just pop it on and just go, right? It's a Linux desktop computer. So there you go. But it is still low power, and you can still get to all those IO pins, and you can get to, you know, the single line commands that help you toggle LEDs and, you know, control switches through your house and stuff. Or you can just drop on, you know, four Arduinos if you want on the USB ports.

**Chris Gammell:** So that's the ultimate way to describe it, really. It's just a single board computer.

**Jeff Kaiser:** Am I not wrong? Yeah, I think there are a lot of those out there, though.

**Chris Gammell:** Oh, yes, yes, there are. Well, how does this differ? Is it just because it's open source and it's, you know, I mean, how does it differ from another single board computer that has, seriously?

**Ed McMahon:** Just because it's open source, I think there's a lot in that statement. Oh, yeah, I know.

**Chris Gammell:** But it's just, it's an open source single board computer. That's the best way to describe it. How many of those are there? I think.

**Ed McMahon:** There's not very many of those on the market.

**Chris Gammell:** There's the Maximite, which we've talked about this a couple of weeks back. It's an open source single board computer. Cover the Penguino? No, it'll be now based on the Penguino platform using the PIC32, but it's a single board computer. It's got a basic interpreter built in. It's got monitor, keyboard. You just hook it up and it works. Bang, like a PC, a single board computer.

**Jeff Kaiser:** I think the community and the performance, right? So I think it can do a lot more than what you can do with a PIC32, and you're talking about a gigahertz on Cortex-A8. Oh, for sure. And running full Linux desktop distributions and just all the community that's around the BeagleBoard today. Just because it is a lot of performance at a low price.

**Dave Jones:** Yeah, the thing I always remember about some of those demos I've seen is the 3D stuff that BeagleBoards have done. When you actually do hook up a monitor, you can start doing 3D processing and all that other junk. And that just seemed, you know, whatever. It's just junk. It's simple, right? It's all that geeky software shit, right? Yeah. Blah, blah, blah.

**Ed McMahon:** I think it's pretty impressive. Of course it is. I mean, you're talking about a 1 gigahertz PC and like a, what, 4 by 4 inch package?

**Jeff Kaiser:** 3.25 by 3.25.

**Chris Gammell:** And how much power does it consume at its maximum frequency?

**Jeff Kaiser:** Yeah, about 2 watts if you're not, you know. Yeah. It depends on what you draw off of the USB host ports, right? So 2 watts for doing video at the same time as, you know, that's like sort of the high end of the processing. Everything on, but then you still have to add in. If you're adding a USB peripheral, it chews up a lot of power. Right. So 2 watts plus whatever you're drawing off of the USB host port.

**Chris Gammell:** So is it scalable back to, here I go again, I'm old fashioned. Is it scalable back to like 32 kilohertz so you can run the thing on the smell of an oily rag? Or is it a full bottle only?

**Jeff Kaiser:** It pretty much is. You run fast and shut down, right? It has very low standby currents.

**Chris Gammell:** Yeah, I'm not particularly talking about standby, but actually low operating frequencies. Is there low frequencies you can run it at? If you don't need all that processing grunt for most of the time, you can just, you know, run it at, you know, 32 kilohertz or megahertz or something.

**Jeff Kaiser:** No, no, the lowest you can get down to is like 300 megahertz. No.

**Dave Jones:** Can Dave switch up, hook up a light switch and do the clocking manually? That's what he really wants to know. Exactly. That's Dave's ultimate. Yeah, exactly. Set some dip switches. No, but there's a real benefit in that.

**Chris Gammell:** Because you can, you know, a lot of people, they don't particularly need all that processing power all of the time. You know, you might be doing something simple and you want to use as low a power as possible and then dynamically change the clock rate up to your one gigahertz when you want to process something seriously.

**Jeff Kaiser:** So it does have dynamic frequency and voltage scaling.

**Chris Gammell:** Yep.

**Jeff Kaiser:** But the thing is, is it only, you know, it can only go down so far. And then the thing is, is just run fast, go to sleep. And it has incredibly low sleep. You can cut all the power off to the CPU.

**Chris Gammell:** Yeah, but you can't do any processing when it's in sleep. That's what I'm talking about.

**Jeff Kaiser:** Well, you're done with all the processing by that time.

**Chris Gammell:** Well, no, you're not. Often you just want to do some.

**Jeff Kaiser:** Peripherals, you can leave peripherals going. Like if what you're doing is audio processing, you can actually leave an audio processing buffer that's going to move stuff into memory while the CPU is off. Okay, cool. Right. That's kind of cool. Yeah. So there's all sorts of, you know, peripheral stuff that you can leave on and have the CPU powered off.

**Chris Gammell:** Okay, that's pretty good. Still, sorry, I want to see low dynamic clock rates. Call me old-fashioned.

**Jeff Kaiser:** We'll work on that for you. Excellent.

**Chris Gammell:** Thank you very much. That's an official request of Texas Instruments. Now, what's the deal with TI selling the OMAP? Is that a, or selling the, what are they, yeah, they're spinning off OMAP, right? Are you allowed to talk about that? Can you deny the rumors?

**Jeff Kaiser:** I can deny the rumors because, you know, we've come out publicly and denied the rumors in each time.

**Dave Jones:** That makes it kind of easy.

**Jeff Kaiser:** Yeah. That makes it the easiest thing possible.

**Chris Gammell:** Excellent. So it was just some bad rumor started by Electronic. Who was the magazine? EA Times, was it Chris? Do we want to? Yeah. I think it was, yeah. Yeah.

**Dave Jones:** I mean, there was other forums. I didn't think they started that.

**Jeff Kaiser:** I thought it started from.

**Dave Jones:** Or they publicized it, yeah. That's right, because remember the Semi-Accurate, Dave? The Semi-Accurate website. And it lives up to its name.

**Jeff Kaiser:** Semi-Accurate started naming the companies that were buying OMAP out, supposedly. Really? Yeah.

**Dave Jones:** They were talking about Broadcom and Intel and everybody else, yeah.

**Jeff Kaiser:** Honestly, you know, since they know I talk so much, they don't tell me anything. Yeah. Absolutely.

**Chris Gammell:** Well, it's the same with me and Altium, right? I didn't know Altium were moving to China until they handed over my paycheck, you know, and said, bugger off. So I was walking the rumor mill with everybody else.

**Dave Jones:** Yeah. All right. Jason, I wanted to ask you about just kind of the, I guess the clientele would be the right word for that. Like, so BeagleBoard, open source, there's a lot of people interested in that. But is this kind of a way to get hardware people back into doing software? Is that kind of the people you see doing this? Or is this kind of the other way around seeing high-level software programmers trying to dive down into hardware?

**Jeff Kaiser:** For me personally, right, so it was high-level software people down into hardware. And I think our actual future vector here where we're going to try to head more is focus more on the hardware hackers and try to bring them up into some of the higher-level software. But certainly the initial BeagleBoard was focused on high-level software developers and enabling them to do stuff that was towards embedded. And that met my personal interest because I like JavaScript and really high-level coding and working on website stuff and website technology. And I've been an embedded hacker for forever. And I've always wanted to take a lot of this high-end web stuff, Node.js in particular nowadays, and put that into embedded hardware.

**Dave Jones:** Cool. All right. So when you say you're targeting the hardware hackers more, does that mean more expansion ports and everything else? Like trying to get more bits flipped and more interfacing to self-made peripherals, that kind of thing?

**Jeff Kaiser:** Exactly. So getting away from the 1.8-volt I.O., getting to 3.3-volt at least, a lot more pins for expansion. Yeah, just being a lot more friendly to adding on hardware. Okay.

**Dave Jones:** And so what's driving that kind of thing? I mean, is it just seeing the open-source hardware community? Is that kind of what it is? Or is it preference? Or what's doing it? Like who's driving this train? That's kind of what I'm asking.

**Jeff Kaiser:** So I look at a lot of the projects that are coming out and those things that are kind of the sexiest and most interesting and the things that I personally like to play with more. So to me, the BeagleBoard is pretty inexpensive, but it could be cheaper. And so I'm drawn by the allure of just everybody else in the industry of things like the Arduino. So going more towards that direction.

**Dave Jones:** Okay. So what do you think about like Raspberry Pi? That's like the new one that's coming out. That's pretty cheap and small.

**Chris Gammell:** Raspberry Pi?

**Dave Jones:** Yeah.

**Speaker ?:** What?

**Dave Jones:** Do you not know what it is, Dave? No, I don't know. I'm not up to date on food. Tasty dessert. Pie, P-I-I, not P-I-E. Best with ice cream.

**Jeff Kaiser:** Well, that makes it old man. Is it real? I mean, is it? I mean, apparently.

**Ed McMahon:** I think it's real. I think it's real. I don't actually know that much about it, but I've been seeing it. They've been on the web a bit, and they've got a site at raspberrypie.org. And they're going to be at the Maker Faire, so I'll be able to tell you more in a couple weeks.

**Dave Jones:** Oh, yeah. Jason, are you going to the next Maker Faire, too?

**Jeff Kaiser:** I think I'm going to miss it. Oh, okay. I was really looking forward to it, but it's just a bit going on, so. There you go.

**Chris Gammell:** Raspberry Pi, they bill themselves as an ARM Linux box for $25.

**Dave Jones:** Yeah. Which is an impressive billing if they get it, right? And I think they're on the way to doing it because they're demoing.

**Chris Gammell:** It's vaporware, is it, at the moment?

**Jeff Kaiser:** At the moment.

**Ed McMahon:** I think they've demonstrated some prototypes, but I don't think you can buy one yet.

**Dave Jones:** Yeah.

**Jeff Kaiser:** Interesting. So I want to know if you can really do it for $25. And I think it's an 800 megahertz ARM 11. Yeah, that's about us, Paige. So it's a third or less of the performance of a Beagle board.

**Dave Jones:** Okay.

**Chris Gammell:** Well, is it just going to be capable? Is it just going to be a chip on a board like the Arduino, or is it going to actually be what they claim, and it's going to be a Linux box, which means it's got to have like a, you know, it's got to have video out, and it's got to have, you know, keyboard and USB and all that sort of...

**Ed McMahon:** I think that's what they're pushing for.

**Chris Gammell:** Okay, for $25?

**Ed McMahon:** Based on the demos I've seen. Okay. It's like a little computer with an HDMI port and keyboard and mouse. They've got a video co-processor in there, apparently.

**Chris Gammell:** Well, the thing is, the HDMI doesn't cost you much on the hardware side these days to actually implement that. So, yeah, really, I can't see why they can't do it for $25. They wouldn't be making much on it, of course, but, you know.

**Jeff Kaiser:** Do we know who's behind it? Is Broadcom? Is this a Broadcom project?

**Ed McMahon:** I could swear that I saw a board that had Broadcom written on the printed circuit board last week. So, I actually don't know for sure, but I think there might be some connections there. Yeah, I definitely... Yeah, okay, so if you go to Raspberry Pi and you scroll down, there's an image of the top of the board, and it says right on it, Broadcom. Yeah, with the logo.

**Chris Gammell:** Well, I'll tell you what. The domain's at their giveaway. It's .org, not .com. So, they're... In fact, if you go to the About Us page, they say there is a UK-registered charity.

**Dave Jones:** Yeah.

**Chris Gammell:** There you go. That exists to promote the study of computer science and related topics, especially at the school level, and put the fun back into learning computing. Excellent. So, it looks like they're probably doing it for very little profit, just to cover expenses, probably. So, that's what you'd expect at that sort of price point, though. You know, you wouldn't be in it for the money, I'm sure.

**Dave Jones:** And there is a picture of it on the wiki page as well. Okay. So, a little bit more info about it on there. And it says 50 alpha boards were delivered in August. So, that was pretty recent. So, we'll see. That'll be interesting to see what actually pops out of that. But...

**Chris Gammell:** There you go. It's got a 700 megahertz ARM 11, 128 meg of SD RAM. Yeah. It's got a H.264 high-profile decode, 1080p, composite and HDMI video, USB 2, SD card.

**Dave Jones:** That's interesting.

**Chris Gammell:** And it's got an optional Ethernet controller and hub. So, that's optional.

**Jeff Kaiser:** There you go. Red has cost a little bit extra. I think they were talking about adding some of that for only $10, though. Maybe the Ethernet for $10.

**Dave Jones:** Yeah.

**Chris Gammell:** Possibly.

**Dave Jones:** That's interesting, though. It seems like it's kind of a stepping stone, like between the... So, like, Arduino, then Raspberry Pi, and then BeagleBoard still seems to be the heaviest hitter there on the top. It's dual-core still, Jason? Is that right?

**Jeff Kaiser:** Well, the BeagleBoard is a... It's an ARM plus DSP plus the 3D graphics. So, it's not a dual-core in the sense of symmetric multiprocess. It's a DSP processor there.

**Dave Jones:** Okay.

**Jeff Kaiser:** Which can do more than the ARM for certain tasks and, you know, for running Linux eTasks. You know, maybe it does less for you.

**Dave Jones:** Okay.

**Chris Gammell:** Now, what about this Microsoft Gadget Master? Worst name of the week award goes to Microsoft for the Gadget Master board, which they claim is taking on the big... No, no. The Gadgeteer.

**Dave Jones:** The Gadgeteer is the name of the site you're reading off of, Dave.

**Chris Gammell:** The name of the blog. Sorry. I'm looking at the webpage and it's got Gadget Master. Oh, well, yeah. Made a fool out of myself. The Microsoft Gadgeteer. Is that any better than the Gadget Master? No, not really. It still wins the shitty name of the week award. I'm sorry. Anyway, they claim it's taking on the BeagleBoard.

**Dave Jones:** So what's your feeling on that, Jason?

**Jeff Kaiser:** I'm very intrigued by this. It is an ARM 7, so we're, you know, orders of magnitude off here in performance, right? The BeagleBoard is tremendously higher performance. Mm-hmm. But the whole idea, I mean, the fact that it's this appealing now for large corporate interests really to try to get into this, you know, a game of appealing to hobbyists is incredibly interesting to me. And, you know, and I've experienced this inside TI now where when we started the BeagleBoard, it was, you know, kind of a skunkworks project, really. It was very much on the side, something that, you know, Gerald and I and, you know, Steve Kippish and Qasim Saeed Muhammad and, you know, we just kind of went off and tried to do this on our own. And now it's hard to make a move left or right without, you know, sort of everybody in TI saying, you know, what are you doing next with the BeagleBoard?

**Dave Jones:** And what sense? Because do you mean, like, they're worried about what it provides, like, to the company now or just because they're curious about what's coming next, like, the cool stuff that's happening next?

**Jeff Kaiser:** Well, it's just, it's been discovered just how great it is to appeal to hobbyists. And so, you know, everybody wants to sell their next chip, you know, appealing to the hobbyists. And that's, you know, hobbyists get the buzz out. They help solve problems.

**Chris Gammell:** And they give free marketing.

**Jeff Kaiser:** And they give tremendous amount of free marketing.

**Chris Gammell:** That's the bottom line for a big company like TI, let me tell you. I don't want to be cynical, of course, but...

**Dave Jones:** Oh, yes, you do. Dave, you operate on cynicism. That's like, you could, instead of running off the smell of an oily rag, you run off cynicism.

**Jeff Kaiser:** I think it's a good thing for all of us, though. People that want access to technology, you know, want to do cool things on our own to have, you know, the big guys interested in marketing to us, right? And, you know, when you see everybody doing it, it kind of levels out the playing field quite a bit. And, you know, I think we can kind of run the sniff test on the technology and, you know, and people's interests. And I think it all ends up helping us out. I think it's for the best.

**Chris Gammell:** Yeah. But I'm still correct. I think you're right. But everyone wins. It's a good thing.

**Jeff Kaiser:** Everybody's very much interested in the marketing aspect of reaching out to hobbyists.

**Chris Gammell:** So is this Gadgeteer open hardware? I don't see any mention of it.

**Jeff Kaiser:** I don't know.

**Chris Gammell:** Anyone know?

**Dave Jones:** No, do you really care?

**Chris Gammell:** Well, I, you know, if they say it's, if they're coming out with a client.

**Dave Jones:** Throw it back in your face, Steve.

**Chris Gammell:** Well, no, you should care. You should care. Because the correct response from you, Jason, from the, you know, what do you think about the Gadgeteer, is if it was open hardware, your correct response should have been, it's fantastic. That's the whole idea of open hardware. Woohoo! You know?

**Jeff Kaiser:** I just haven't found that much interesting about the hardware itself. Right. I'm very interested in the fact that Microsoft is, and the .NET micro framework is open software. Oh, is it?

**Chris Gammell:** Okay. I wasn't aware of that.

**Jeff Kaiser:** So there's actually a really interesting thing there. Yeah. Because you can take that .NET micro framework and implement that on all sorts of microcontrollers and use their tools, you know, to produce these systems. So I think that's actually an interesting, whether or not that form factor of the breakout board with all the pins and these, you know, all these little modules that you can slide onto it.

**Dave Jones:** It looks like the brainchild of Doc Ock. It does.

**Jeff Kaiser:** Oh, boy. So if the Doc Ock board is interesting to you, if you need that design, you know, that's why I'm not sure. I'm not sure that it matters too much if it's open hardware, because I don't know that I'd ever want to duplicate that thing.

**Dave Jones:** Yeah. Well, I think the plug-in modularity of it. I think it matters a lot. I mean, I like modularity. That's always a big thing for me. But, you know, there's always trade-offs. And in this case, it's how it looks. But, yeah, I mean, we'll have to talk to someone who actually has used it. I haven't used it, and I don't think any of you guys have either, right?

**Ed McMahon:** I don't have any interest in any .NET products.

**Dave Jones:** Not a big Microsoft-embedded kind of person, Jeff?

**Ed McMahon:** Mainly because I don't have any experience in that area. I don't see any evidence at all that this is open source, looking at their website.

**Chris Gammell:** In that case, we won't mention it again, then.

**Jeff Kaiser:** I did a five-minute search when it first came out to try to look for the hardware specs, and I really had a hard time finding them other than to figure out that it was an ARM7, and then I sort of lost interest.

**Chris Gammell:** So, as usual with Microsoft, is it too little, too late? Or they're playing catch-up, you know, and they're still goofing it up. They still don't get it, you know? Maybe. The whole idea is not actually appealing to hobbyists, but actually appealing with open hardware and all the information so people can build on it and things like that. If you have to buy the proprietary boards from Microsoft, well, you know, that's going to damper a lot of enthusiasm.

**Ed McMahon:** Yeah, and not only that, but I suspect that many of the development tools only run on Windows. Ah, I think that's kind of... You've got to appeal. The hackers are not all Windows types, right? Yeah. If you want to appeal to the enthusiast crowd, you really, really, really need to support all operating systems, is my thought.

**Dave Jones:** Well, yeah, but when they came out with this, I remember, because we talked about it on the show when they came out with this, and they were showing videos, and obviously they had people that are very enthused about it, but it was already, you know, .NET programmers, and it was a venue for them to get down to hardware. Yeah. I'm not sure how much, you know, they're not necessarily... They're still abstracting a lot of it out of it, but at the end, what it shows up as is, you know, blinking an LED. There's that magic LED application, you know? Like, that's a big deal, especially for some of this working just in the software realm. So, I think that's really what they were targeting.

**Jeff Kaiser:** And I'm not so sure that the tools only work on... Well, maybe the Microsoft-provided tools only work on Windows, but, you know, the work of Miguel de Caza, I think that he's got a lot of this .NET stuff running on Linux.

**Dave Jones:** Oh, cool.

**Jeff Kaiser:** Excellent. I don't know. I think he gets a pretty rough time in the open source community, right? He's actually a pretty famous figure, but I think the fact that he's servicing all these Microsoft technologies you know, if the technology's there or not, I think Microsoft has been given such a bad rap for being closed. Even if they are really completely open, are they ever going to be given credit for it? I think it's one of the nice things about, you know, me working for a semiconductor vendor is, although, you know, some of the intentions here, you know, with the hardware platforms are questioned some, you know, whatever your software agenda is, you know, people don't question it, right? You just want all the software to run, so it makes it nice for me to be able to just play with whatever software I'd like. That is nice.

**Dave Jones:** Thanks. So let's hear about some more of those projects that you have seen. I mean, so some of these higher-level software projects that you've seen, Jason, can you run us through some more of those? I mean, maybe the best crossover of software onto hardware, that kind of thing?

**Jeff Kaiser:** Man, because it's running full Linux. I mean, it's kind of hard to say, you know, what's not running. I mean, there's just so much that's there, right? So if you like scripting languages, right, or you like Java, you know, the guys over at Bug Labs, you'll find them for sure, they're sponsoring that open hardware summit.

**Dave Jones:** Which Jeff will be at also, right? Yep.

**Jeff Kaiser:** Yeah. So those guys, you know, have this Java-based framework, and they're building off of OpenJDK, and they've got these great tools for, you know, controlling all these little add-on modules for their components, and they're based on the same, you know, fundamental building blocks as the BeagleBoard, and so there's a lot of sharing between those groups. And so if it's Java, it's a Python, is it Ruby, is it, you know, you can run Apache server if you want on your BeagleBoard, right? There's Qt or Qt or Qt, however you want to pronounce it, you know, for building GUIs. That's a really popular one, including the QML, that quick markup language. Are you guys really interested in software? I could go on about it.

**Chris Gammell:** No, all these weird names are just going whoosh straight over my head.

**Dave Jones:** I'd say I'm about 50% on those, yeah.

**Jeff Kaiser:** Game emulators. Actually, that's – so I got one of those iCades for my birthday recently. Yeah, you take an iPad and you put a – It's a box, right? It's a – Yeah, it's a box with a joystick and buttons.

**Chris Gammell:** It's a box that you actually slip your iPad into and it becomes an arcade machine. It's got like a joystick and everything on it. So you actually – so the iPad becomes the display, you know, so.

**Jeff Kaiser:** So I'm looking for the right LCD right now. I've actually found some pretty affordable 10-inch LCDs. But I'm going to turn my iCade into a – instead of putting an iPad in there, I'm just going to turn it into a permanent arcade machine. So this is my next project. Because you can run all these game emulators on the BeagleBorn.

**Chris Gammell:** So is that using MAME? Is that using a version of MAME?

**Jeff Kaiser:** You can run MAME. There's even, you know, Super Nintendo emulators. There's – yeah, there's all sorts of emulators out there.

**Dave Jones:** So nerdy possibilities are endless.

**Ed McMahon:** You know, it's interesting. One of the interesting things that I've seen about the BeagleBoard is if you go to ESC and you walk around, you'll see these assembly companies like Screaming Circuits. And these guys are using the BeagleBoard as advertising of like, look, we can build this, you know, and then they show the BeagleBoard. So it's kind of a cool thing because I think the BeagleBoard had, at least in the beginning, kind of a reputation of being difficult to assemble, right? Because the OMAP 3 has the stacked memory on top of the package, the package on package. And also I think it's a pretty fine pitch BGA, right?

**Jeff Kaiser:** It's 0.4 millimeter ball pitch. Pure Able.

**Chris Gammell:** Fine. Pure Able.

**Jeff Kaiser:** I knew that one at home. Laser drill B is –

**Ed McMahon:** But think of this. Oh my god. Awesome. You have this reference design of this really kind of difficult to build board. And now all these assembly houses can download the PCB drawings and can make PCBs and do their own assembly. And it kind of puts everyone in the same playing field, right? So I actually thought that was pretty interesting. And if you walk around ESC, you'll actually see BeagleBoards that companies have assembled. So it's kind of an interesting tangent, right? Because it's probably not something that anyone anticipated. But yet I've definitely seen this over the past couple of years at trade shows.

**Chris Gammell:** There's probably a niche market there just to mount the OMAP processor on a bloody dip conversion board, you know, that you can plug it into your breadboard.

**Jeff Kaiser:** I think that is a market on its own. Dead bugging it.

**Chris Gammell:** Dead bugging 1.4 millimeter pitch BGA.

**Jeff Kaiser:** So the most crazy board hack I've seen – somebody actually drilled a hole underneath to correct one of the balls, right? It was actually a short to power rail. They actually drilled out the ball underneath it and hooked a wire directly to the ball on the other side of the device.

**Dave Jones:** It's like 34-gauge wire, that kind of thing.

**Jeff Kaiser:** I do not know how this was even possible.

**Dave Jones:** Is it gold bond wire or something?

**Jeff Kaiser:** One of these coaxial things. I don't know how he did it. It was the most incredible thing I've ever seen.

**Dave Jones:** Do you have pictures of that somewhere? Maybe we could post them later.

**Jeff Kaiser:** Have you – You know, I haven't seen that board in a couple years now. I'll – so it was – yes. I'll see if Steve – Steve Beltram – I'm sorry, Scott Beltram. I'll have to ask him where that is.

**Dave Jones:** Okay. And that could be a fun segment on the Amp Hour too, just seeing crazy board hacks. Because people have done some crazy stuff before. I've only – I mean, I mess stuff up all the time. And then I give it to a technician and they're nice. They take pity on me. And then they use a 30-wire gauge. You know, they're snaking all around and everything.

**Ed McMahon:** You know, I – that's one of the things that in my career I've always taken pride in is that I almost always do my own hacks. And I think in RF design, it's much more common for design engineers to also be really good in the lab. Like, I used to do wire bonding and stuff like that to support experiments. And, you know, I never did die attach. And I never did any, like, BGA assembly or things like that because we didn't have that in what I was doing. But, you know, I actually would like to openly challenge the other members of the Amp Hour. We should do, like, a soldering competition. Oh, my God. Do you know how much coffee you drink? I think I can do pretty well. Well, I found that there is an optimum amount of coffee. If you don't drink any coffee, you're a little too brain dead to really function at all. Dave doesn't drink coffee at all. Dave doesn't drink coffee.

**Chris Gammell:** I don't drink – I've not touched a drop of coffee in my entire life.

**Ed McMahon:** If your system isn't expecting this coffee input, I think you have an advantage. But for those of us who are addicted, we have a certain threshold that we need to cross in order to function at all. But if you cross that threshold too far, then your hands move too much to be able to do delicate assembly. And this is a well-documented phenomenon.

**Chris Gammell:** I think my skills are automatically going to be superior because I don't drink coffee.

**Ed McMahon:** Well, you're making the assumption that we haven't adapted to our coffee.

**Chris Gammell:** Sorry, you guys just aren't as highly evolved as I am. I'm sorry. In the hardware skills there, in the soldering skills.

**Ed McMahon:** I challenge you to a duel. So whose equipment do we use for this challenge? I'll provide all the equipment. All right.

**Dave Jones:** Dave, just fly to Austin. Well, I'll fly to Austin. Jason, you can drive down. Yeah, I can make it Austin.

**Speaker ?:** Yeah.

**Ed McMahon:** That's true. We have two Texans on the show, right? Well, three if you count former Texans. Oh, yeah. So Dave is totally outnumbered by us Yanks.

**Chris Gammell:** Doesn't matter. I'm going to win anyway.

**Dave Jones:** I don't know if you can call it Texans Yanks, though. I think in non-ampire circles, you might get punched in the face for that one.

**Chris Gammell:** Right, or shot or something with one of those quick draws which everyone walks around the streets with, right? Of course, yeah.

**Ed McMahon:** I think I'm probably tolerated by Texans more than I am.

**Dave Jones:** So Jason's the only true Texan. I mean, Jason, do you have a pair of boots? I mean, let's hear all the stereotypes that you fit.

**Jeff Kaiser:** Well, my boots don't fit anymore. I've grown out of my boots.

**Chris Gammell:** Oh, no.

**Dave Jones:** True metaphor.

**Chris Gammell:** And have they got those little, what are those little wheels on the back of them? Spurs. Spurs. Spurs on the back of the boots.

**Jeff Kaiser:** Never had spurs for my boots.

**Chris Gammell:** No? And do you say howdy?

**Jeff Kaiser:** Jason's a cowboy cowboy. Yeah. Absolutely, I say howdy.

**Chris Gammell:** Is that a Texan thing? Or am I mistaken? It's a Texas thing.

**Jeff Kaiser:** It's also an Aggie thing. What's an Aggie? Yeah. What?

**Dave Jones:** I haven't heard Aggie before. Come on, Jake. You've got to educate Dave. Dave tells us all about the crazy Aussie-isms that he has.

**Jeff Kaiser:** Yeah, all the school stuff. I think it just gets boring quick. So I went to Texas A&M University. We're called the Aggies. Gig'em. Gig'em.

**Dave Jones:** Oh, right. Okay, so it's a school. It's the most ridiculous thing you'll ever see. It's like they're little city states within Texas. You know why? Because Texas is monstrous. It's just... Yeah.

**Chris Gammell:** It's not as big as Western Australia.

**Dave Jones:** That's true. Yeah, that's the middle of the world.

**Chris Gammell:** Yeah, sorry, Texas A&M. Texas is small fire. We've got hobby farms in Australia bigger than Texas.

**Jeff Kaiser:** That's a hot one. You can have them. Yeah.

**Ed McMahon:** Got a whole lot of nothing out there. Just like in Texas. If I can bring us way back to soldering, there's one thing that I wanted to maybe give, I guess it's like a shout out. I, this weekend over Labor Day, I invested in a new tool that has totally changed my life as an electronics professional. Do tell. All right. So, I bought, and I've wanted this for years, I bought a desoldering tool. And like, not, you know, the solder sucker that you push in and push the button. No. But I actually went out and I got a, I don't know if you say Hakko or Hakko? Hakko. Hakko. What's it? Hakko. Hakko?

**Chris Gammell:** Hakko desoldering, Hakko vacuum desoldering tool.

**Ed McMahon:** I bought a desoldering gun, a Hakko 808. Yep. And I walked into Fry's and they happened to have it and they had a decent price. And granted, it's more expensive than my soldering iron, but I had a 40 pin ZIF socket in my AVR Dragon, which is an AVR development tool. And the ZIF socket had gone bad for whatever reason. I think it was this ancient socket and I shouldn't have used it, but it stopped working. And I was in sweats because desoldering a 40 pin dip, I, I've soldered for a long time. And there are certain things that strike fear into my heart. And desoldering like large through hole packages is one of those things because you never, you never get it right. There's always like one lead that's hanging on. And it rips the pad off whenever you try to.

**Chris Gammell:** And you have to wiggle the pin, you know, you got to get in there. That's right. That's right.

**Ed McMahon:** So I, I said, screw it. I'm going to go. And I've always wanted to buy it.

**Jeff Kaiser:** That's what I do every time. Cut off every lead. No problem.

**Ed McMahon:** Yep. Exactly. I would have done that, but a ZIF socket is difficult. There's a lot of meat there to cut through. So I went out and I, I bought a desoldering tool, which I've always wanted. And in 20 minutes, the socket was out. The new one was in and I was done. That's 20 minutes. Well, including five minutes to plug in the tool. Five minutes to figure out how to use it.

**Chris Gammell:** It's just a second. Well, it probably takes. Jason's driving down right now.

**Ed McMahon:** It probably takes three to five seconds per pin, right? Wow, wow, wow. Because you heat it up, you push the button. Yep, it does. You wait.

**Chris Gammell:** Now, are you, are you one of those people who put it down on the bench and you, and come in vertically with the vacuum desoldering tool thinking, ha, I can defeat gravity with this thing?

**Ed McMahon:** No, no, no, no. I, I didn't think about that. Right. So I accidentally didn't do that, but I, I definitely went horizontally. Oh, you went horizontal. You didn't go upside down where you can add gravity to it. Yeah, you just go, all you do is go upside down.

**Jeff Kaiser:** You swirl that thing around three or four times in every pin.

**Chris Gammell:** You've got to be careful swirling it around because that can, that can, your actual, you can pad, your pad can lift off. Sure.

**Ed McMahon:** And I was, I was very worried about that, but I was very careful not to slam it up against the pad and I didn't have any problems.

**Chris Gammell:** Right. Well done.

**Dave Jones:** So how are we doing this, this soldering contest? Are we going to do like Google plus or I think we could do it through that. If we had like webpams.

**Ed McMahon:** I think it would require physical presence.

**Dave Jones:** I don't know, man. Google plus, I think we could do it. So we could have, you know, all of us could have a 40 pin ZIF or whatever the hell the challenge is. No, it can't be a piece of soldering.

**Jeff Kaiser:** No, we need something that shows electrical activity afterwards to verify the functionality.

**Dave Jones:** How about soldering a live line wire onto a, onto a switching module? No?

**Chris Gammell:** And you guys don't even do the same, same thing as we do. It's soldering over there, right? What the hell's that? It's soldering with an L.

**Dave Jones:** Soldering.

**Chris Gammell:** God, you can't even pronounce it correctly. How the hell are you going to win a contest? I don't know. Sorry.

**Jeff Kaiser:** Less talking, more soldering.

**Dave Jones:** Yeah.

**Chris Gammell:** My favorite programming language is solder.

**Dave Jones:** You might have a tough time with the legal board, I gotta say.

**Ed McMahon:** Yeah, that's right. That could be like the grand prizes you have to hand solder an OMAP 3 processor. Yeah, it's 0.4 millimeter.

**Chris Gammell:** I did a tutorial on 0.4 millimeter ball pitch BGAs. They're freaking evil. I was able to route out a three row one. If you've got a three row 0.4 millimeter pitch one, you can actually route it out and you can get it manufactured cheaply. But after that, as Jason mentioned, you've got to use those laser drilled vires really. You know, you've got, I think you could probably get away with a 0.2 millimeter drill or 0.15 millimeter or something if you're that game. But, oh man, that's evil stuff. That's crazy. I know. It's just nuts.

**Ed McMahon:** So guys, we're like 45 minutes into the show.

**Chris Gammell:** I know. Should we get on to some regular Amp Hour stuff?

**Jeff Kaiser:** I have been holding on to this one little bit of news that I wanted to share with you guys here. We really shouldn't take too much time on it. But we are planning on another BeagleBoard release. Is this breaking news? Breaking news. Off the teletype. All right. All right. So, yeah. The next version of the BeagleBoard is going to be coming out in the fourth quarter here. And it's going to be lower cost. It's going to be no DSP, no HDMI. It's going to be all this hardware experience. So I said we're headed in the direction. We're actually designing a board right now.

**Dave Jones:** Are you looking for input?

**Jeff Kaiser:** Yeah. Absolutely looking for input. How do people contact you? Well, the BeagleBoard mailing list is always a really great way to do so.

**Dave Jones:** Yeah. Or they can listen to BeagleCast. So that's something we should probably mention on here.

**Jeff Kaiser:** Oh, you know, but I'm still looking for another host at this point. I need somebody who can... Well, that's another thing to say.

**Dave Jones:** Yeah.

**Jeff Kaiser:** Yeah. Definitely looking for a host for BeagleCast.

**Dave Jones:** BeagleCast is a podcast radio show. Yeah. And we've mentioned it on here before once, I think. Oh, have we? Oh. Yes. I think so. There you go. Yeah.

**Jeff Kaiser:** I forgot an interview with Greg Crow Hartman and then never did another episode.

**Speaker ?:** Right.

**Jeff Kaiser:** So where did he go from there?

**Dave Jones:** Clint Cooley. I want to hear Clint Cooley on the show. Yeah. Got to do that. Speaking of Texans, right? Clint Cooley, if people don't know, Clint Cooley is one of the guys that helps manufacture the boards. I saw him at the Open Hardware Summit. And Clint's... I think I mentioned on the show before, he's got like one of the best accents ever. He's got like one of the thickest... Rock. It was East Texas, I think. He's just twanging all the way home. It's great. It's awesome. I love his accent. It's great. Brilliant. So fourth quarter, you said, is coming out. And any price idea? Like $80? $60?

**Jeff Kaiser:** Under $100? Okay. Well, I probably won't give any more guidance. But definitely under $100.

**Ed McMahon:** Okay. Wow. That's great. Because the BeagleBoard is about $150 right now, right?

**Jeff Kaiser:** Yeah. It's $150 for the XM with the 512 megabytes of RAM and $125 for the 256 megabytes of RAM version. It goes, I think, 720 megahertz.

**Chris Gammell:** You know what the crazy thing is? You can buy a mobile phone for half that cost and it's got all the shit in it. And with the OMAP processing.

**Ed McMahon:** Well, not if you paid retail for a mobile phone. That's true, yeah. You probably have to have a contract. Those are heavily subsidized. Those are heavily subsidized.

**Chris Gammell:** No, I'm sure you can buy a $70 mobile phone here in Australia.

**Dave Jones:** Like a clamshell? Like an older generation phone? Oh, yeah. Like a...

**Chris Gammell:** Yeah, I'm not talking about the touchscreen smartphone.

**Ed McMahon:** Well, think about the economies of scale. Yeah, I know. I mean, how many mobile... Just saying. If they start making 10 million BeagleBoards, then yeah, the price will probably drop through the floor. Yep.

**Jeff Kaiser:** Those HP touchpads...

**Chris Gammell:** Oh, they went crazy shit, didn't they?

**Jeff Kaiser:** Wish I'd... Man. I didn't get one. I really can't believe I didn't manage to get one of those.

**Chris Gammell:** It was sold out here in Australia in like an hour. People were tweeting, and if you weren't actually clued into Twitter, you missed out. And there were lines around the corner to buy these $99 bloody touchpads.

**Ed McMahon:** Unbelievable. I haven't seen the touchpad. And neither has anyone else. They all sold out. I mean, I haven't heard anything about it. All right.

**Chris Gammell:** Well, HP, right? You've heard about HP. They're selling their computer division. Did you listen to the Amp Hour, Jeff? I do know.

**Dave Jones:** Have you heard of the show, the Amp Hour?

**Ed McMahon:** They used to make really nice test equipment.

**Chris Gammell:** Right, yeah.

**Dave Jones:** Yeah, I've heard about that.

**Chris Gammell:** Anyway, they released this new touchpad, and within weeks of them releasing it, you know, it was released, you know, and nobody cared because it was just another touchpad computer, right? Me too. And then they cancelled it within like a week or two of actually releasing it. And then they had this big fire sale, $99. Clear it out.

**Jeff Kaiser:** Well, the crazy thing to me is that they bought Palm before doing this, right? Yeah, I know.

**Chris Gammell:** Exactly. How much did they pay for Palm? I'm sure they picked them up at a bargain price.

**Ed McMahon:** I think that proves that Palm is kind of cursed, right? Yeah. Palm was able to... It was a software to HP.

**Chris Gammell:** Palm was leader in its day, you know. It was number one.

**Ed McMahon:** I never liked Palm. I don't know. Never? I've had... I've owned two Palm Pilots in my life, and I hated both of them.

**Dave Jones:** Infrared beaming of contacts. That's what I always think of. Oh, God. Touchscreens that have to be recalibrated every 60 seconds. Oh, I miss them. I think I still have mine somewhere. I should pull it apart.

**Jeff Kaiser:** I think for the PEM software, I think that they really had it down. And for the WebOS stuff, if you didn't get a chance to play with it, I think they had the absolute best integration of contacts and calendars, right? So all your contacts show up...

**Chris Gammell:** That's what everyone says, yeah. This WebOS thing is the reason they bought it. And everyone says it's fantastic, you know. And it was a huge asset. But now they're looking to sell it. They're looking to spin it all off. Discard it. Toss it in the bin.

**Jeff Kaiser:** Yeah. I just want to figure out how to get a hold of all that software. I know a lot of it's open source. It's all built on top of open embedded, which is the same stuff that's used for the Yankstrom distribution. But it's... Yeah. It's just... It would be a shame to see it go to the way of the dustbin because there's actually some really incredible technology there.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, Phil Terrone, he writes for Make and he's part of Adafruit, too. And he always writes about, you know, if you're going to trash it, open source it. And he talked about the flip phone or the flip camera that Cisco bought. And then they trashed it and everything else. And I think it's a great idea, you know. It is. I think a lot of companies are against it because they say, well, you know, oh, it's proprietary technology. It's like, but why not just give it away? You're thrown in the bin, you dickhead. Yeah, exactly.

**Jeff Kaiser:** You're going to deny people. Chris and Dave officially asked Ari Joxy of HB on the Amp Hour. You made the official request.

**Chris Gammell:** I know that they listened, so, you know. There's a bingo word. That's a bingo item.

**Dave Jones:** So we should bring that up real quick. So I don't know if you guys saw the show or heard the show last week, but we actually had two people create Amp Hour Bingo. And now there's actually the AmpHourBingo.com. People who are listening along. I should have mentioned it at the beginning of the show. This thing, it reloads, like, Dave's dumb phrases and my dumb phrases. And basically, every time you hit reload, it's a new page. And then you actually click on it. It's got, like, JavaScript in there. So every time you click on a box, it turns green. And I don't know. It's awesome.

**Chris Gammell:** There should be, like, a prize for the person. If we had a live show, like, you know, we could be the first person to call in and shout, Bingo, we need a beagle board, you know. Yeah.

**Jeff Kaiser:** I'll donate a beagle board for that. Okay.

**Dave Jones:** All right. Yeah, we'll have to try and get something in there eventually.

**Chris Gammell:** Oh, awesome. We got taken to task again, Chris.

**Dave Jones:** Yes.

**Chris Gammell:** We got called out on the helicopter thing, which we made fun of last week. We did, yeah. And the guy who did it, Brad Huey, if I'm pronouncing the Huey correctly, he emailed us and said, no, it's not fake. You know, how, well, almost how dare you, you know.

**Dave Jones:** I think he was bordering on that, but it's okay. Yeah.

**Chris Gammell:** But he was quite polite and nice.

**Dave Jones:** Overlapping with him, I think. Yeah, yeah. And he was very, very kind about it and took it in stride. Yeah. Jeff and Jason, do you happen to see that video last week? Oh, yeah. Yeah, I saw the video. Yeah. It's down now, unfortunately. He took it down. He took it down.

**Chris Gammell:** Anyway, he says it's a... And he has his own corporate... Well, he calls it a corporation, the Huey Electric Copter Corporation.

**Dave Jones:** HueyCopter.com.

**Chris Gammell:** Yep. Yeah. And he's actually manufacturing... Manufacturing... Well, no, the goal is to ultimately manufacture this thing. So, this is real.

**Ed McMahon:** I hope he's not manufacturing the ones that were in the video.

**Chris Gammell:** The ones that dragged him down the driveway.

**Ed McMahon:** So, he's serious.

**Dave Jones:** He's doing more testing. Yeah, yeah. Yeah, this is serious shit.

**Chris Gammell:** I mean, this is... That's cool.

**Dave Jones:** So, power to it. And he said he's going to get us videos once he's got some better testing. So, we look forward to that. I can't wait. I can't wait to see it flying. I just hope that he stays safe.

**Ed McMahon:** Maybe Maker Faire 2012. Right, he'll fly it at Maker Faire and it crashes into the audience and chops off a thousand heads. No. He's got a parachute in or something. That would be badass. There's like waivers that can take care of that.

**Chris Gammell:** Yeah, exactly. Everyone signs a waiver as they come in the front gate. Amen.

**Dave Jones:** Do they really have to sign waivers for Maker Faire or no? No. I take it like those lame throwing swings and everything.

**Ed McMahon:** The people that are in it have to sign... Like, if you present something, you have to sign a waiver that I think says you're not going to do anything stupid. Oh, okay. So, I guess he'd have to sign that. But...

**Chris Gammell:** But I thought everything at Maker Faire is ultimately stupid in some way, shape, or form, isn't it? In traditional sense.

**Dave Jones:** Of stupid, you know? Non-standard is what you're trying to say, Dave?

**Chris Gammell:** Yeah, exactly. Yes. But it's, you know, it's silly. You know, there's lots of silly stuff there that's, you know, cool. But, you know... Dave just pissed off a bunch of people. You do something wild and creative and silly, you know? Silly is a better word. That's a lot of silly. In a good way. Yeah. In a good way. Breaking convention.

**Dave Jones:** Yeah. And speaking of breaking convention, I like this thing, too. Did you guys see Bill Porter? Did you know... Did you see this on Twitter?

**Chris Gammell:** No.

**Dave Jones:** No? So, he asked his girlfriend at the time to marry him via PCB order. I saw this. Through Dorkbot. It's awesome. Talk about non-traditional.

**Ed McMahon:** It was cute. And I'd like to see someone one-up that one by making the boards actually functional instead of just writing on the boards. Like it lights up.

**Chris Gammell:** The ring... If you don't know, we haven't said what it actually is. He basically asked his girlfriend, who's also a fellow electronics nerd, to marry him. But, you know, he actually etched it into a PCB and he actually did a little PCB ring. You know?

**Dave Jones:** He hijacked her PCB order from Neil's service.

**Chris Gammell:** Oh, right. I didn't read the details. Or PCB.lane.org.

**Dave Jones:** That I didn't see. He hijacked it. So, him and Neil worked on it. And, yeah. It's awesome. Right. Excellent.

**Chris Gammell:** Now, if you're going to do a PCB ring, okay, don't do it using breakout tabs. Actually, get it fully routed next time. Just a little tip there.

**Dave Jones:** There's a PCB tip from Dave, yeah.

**Chris Gammell:** And get the high-quality gold plate. Not that one-hung-low Chinese gold plate shit, right? Get the real, you know, get the real stuff. And get the edges gold plated as well. And two-ounce copper. Come on. Two-ounce copper. Get the inside and outside edges. You can do that on PCBs. You can specify it. Get the whole thing so it looks actually like. So, you can't see any fiberglass at all. You just, it's all gold. All around the whole thing.

**Jeff Kaiser:** Can you add a chip scale of 555 onto there somehow?

**Speaker ?:** Right.

**Ed McMahon:** And flash the lens, yeah. Oh, yeah. We just got another square.

**Dave Jones:** Mm-hmm.

**Ed McMahon:** Oh, just following along right now. I am now playing the show that I am also on, which is probably against some kind of code of that. But we already had that square with the Arduino earlier, so.

**Dave Jones:** There you go. There you go. And speaking of 555, because that's our favorite, another contest starting up. Dangerous Prototypes is having a 7400 Logic contest. So, I saw this through Embedded Eric's website. I don't know. It's going to be kind of broad, but kind of a cool idea for a contest. I don't know if you guys are.

**Chris Gammell:** You will hear more about me in this contest coming up shortly, perhaps. Oh, you're going to.

**Dave Jones:** Oh, okay. No questions there, I guess, huh?

**Jeff Kaiser:** Yep. Does that really have the same, I mean, I don't see it having the same possibilities to me as a 555 contest. I mean, I love playing with the 7400 Series Logic, but.

**Chris Gammell:** Well, I think it's got the same. Well, I think it's actually got more scope. More scope. That may actually be the Achilles heel of it. That's almost a bad thing. Yeah, I agree.

**Dave Jones:** I agree.

**Chris Gammell:** Yeah.

**Dave Jones:** Every time I try and, like, anytime I talk to, like, people who are running contests, I always say that's one thing that's good about, like, the best contests have limited scope. Because that's what engineers want. They want that challenge to try and squeeze it all in. Like, one of the suggestions we had was, like, a really small PIC microprocessor with, like, 1K of memory. Right? Something like that. That would be a great contest because you're so bounded in what you can do. So, anyone who's doing a contest, Jason, if you do a BeagleBoard contest, make sure you can only use, like, the RS-232 port or whatever it has on there. I'm sorry. I don't remember what the peripherals are. But, like, if you bound it, then you're going to get some really cool entries, you know?

**Ed McMahon:** Yeah, because it kind of levels the playing field a bit and makes it so that the entries are... You can appreciate that there was some ingenuity that went into each one. So, yeah. I agree.

**Jeff Kaiser:** How many logic gates can somebody use in this sort of contest?

**Chris Gammell:** There's no limit, I don't think. Yikes. Yeah, which is, you know... Yeah, I mean, you can build a crazed supercomputer with 7400 series logic if you want. Yeah, I want to see, like, a data general Nova.

**Jeff Kaiser:** That 32 kilohertz frequency you were looking for earlier.

**Chris Gammell:** Exactly. Finally. You can cut the damn thing and use a 4,000... And you're allowed to use 4,000 series CMOS as well. It's, like, all over the shop. Wow.

**Ed McMahon:** Yeah. Well, it'll be interesting to see what happens.

**Dave Jones:** You know what the best thing for this would be? It would be that you have to use the old data books, that you can't look anything up online. You have to look everything up through the data books. That would be a contest.

**Ed McMahon:** Yeah. First off, it has to be wire wrapped. Oh, there you go.

**Jeff Kaiser:** Well, make sure there's no 7474ers. Because that'll limit people. Everybody has to build their own flip-flops.

**Dave Jones:** Oh, that's good. Yeah, that's a good start. Yeah. Oh, boy. We don't make this a fighting contest yet. And so we should mention, too, if people are out there listening and do have things to donate, I think they're still looking for prizes. So it could be a cool contest. So definitely. I think I saw some other companies throwing in a BeagleBoard already, but maybe Jason will throw in another BeagleBoard or two.

**Chris Gammell:** Yep. They need some big players in the sponsorship stakes. At the moment, it's a bit slim pickings. But yes, they should. So all of you tight-ass, huge, multi-billion-dollar corporations out there, get off your ass and sponsor it.

**Dave Jones:** Yeah. Get in with the hobbyists. We hear that's the big thing now. Yeah, apparently. So in the last couple minutes here, Jeff, why don't you – so you were just at the Chaos Communications Camp. We were talking to you a little bit during that. You were out in the woods on Wi-Fi or something really nerdy like that, right?

**Ed McMahon:** Yeah, I had a heck of a time getting a good internet connection at various times during my Europe vacation because we were actually going to try to do a show while I was in Berlin. But the hotel that I was at had a horrible internet connection. It was hard to even do anything, much less stream audio. I had to talk to people and go outside. It's horrible. Well, I mean, it is challenging whenever you're traveling, but I would have done it if I could have made it work, but it just didn't work out. And I think I was pretty wiped out at that point anyway, so I wasn't about to go down to some cafe or something and try to – Talk to everyone while you're – Steal there.

**Dave Jones:** Yeah. Much of Germans staring at you.

**Ed McMahon:** Yeah. But anyway, yeah. I don't know if very many people know what Chaos Camp is. And I only know about it because Mitch Altman introduced me to it a couple years ago. But Chaos Communications Camp is a – it happens every four years. I don't know what the word for that is. It's every four yearly. Quatranurnal? Is it like biennial, triennial, quadennial?

**Dave Jones:** Maybe?

**Ed McMahon:** Okay. But anyway, it happens every four years. It just happened. It's just outside of Berlin. It's put on by the Chaos Computer Club, which is a really old-school hacking organization that's based in Berlin, I think. That's been around since the 70s, if I'm not mistaken. And the best way to describe it is it's sort of like Burning Man, except there's more computers and less nudity. So it's like a Burning Man for nerds and computer geeks. What's Burning Man? I'm sorry. Oh, I'm sorry. So, yeah, my comparison fails. Burning Man is an annual event that happens in the United States where these people – In the southwest, in the desert. Of course. In the desert where people go and –

**Jeff Kaiser:** The easy way to explain it to an Aussie is it's Saturday night in the Outback.

**Dave Jones:** Oh.

**Ed McMahon:** You set shit on fire, you drink a lot, and you get naked. Yeah, there's – exactly. Yep, right. And there's a lot of interesting light shows and stuff like that. People bring things that they build. And so this is the same thing. People build things.

**Chris Gammell:** Is this a young person thing or is it a – No. It doesn't sound like a family event, you know? No. Well, no.

**Ed McMahon:** So, chaos camp is interesting because I think it represents the part of the difference of European hacker culture versus what exists in the United States in that there's an extremely broad cross-section of age, occupation, personality, and there are families. So people actually bring their kids. And there's a whole section of the campsite. And if I didn't make this clear, this is camping. So you go –

**Dave Jones:** This is tent camping, not cabin camping? This is tent camping.

**Ed McMahon:** Yeah, okay. Some people bring, like, RVs. Like, crapping in the woods kind of camping, right? Actually, there are bathrooms and showers. Aw, come on. Well, come on. I mean, I only put up with a certain amount of camping. But think of this. You've got somewhere around 4,000 hackers, which in the European sense especially are professionals in the computer science, electrical engineering, et cetera, who basically are on summer vacation and want to have a good time. And so they go camping. And at the campsite, which is a former Soviet Air Force base, they have, like, extremely high-speed internet. There's a phone network. There's, like, any – there's electricity to your tent. So I brought a tent. No, no, no. To appreciate this, you have to see it. Might as well stay at a bloody hotel. It is the most awesome thing you've ever seen. Because think about it, temporarily, for four or five days, you are camped amidst over 3,000 other people who are bringing interesting electronics things. They've got their laptops. And the interesting thing is that hackerspaces all around Europe, if not the world, go to this thing, and they actually bring big stuff. So the people who can drive load up a truck with, like, a couch, you know, tables, chairs. There's, you know, there was a big tent that was brought by the folks from Metal Lab, which is in Vienna, not too far away, although it's at least a few hours' drive. They had a crepe-making robot that they brought that was actually making crepes all weekend. They had at least one MakerBot. There was a Rigol oscilloscope. They had a full electronics lab. And they also had a lounge area with, like, beanbags and stuff where you could just chill out and, you know, it's hard to describe. But I hope that I've captured at least part of the vibe of it. But the best part about it is that whenever the sun sets, it is the most unreal display of LEDs and lighting creations that you have ever seen in your life. So we had everything from LEDs everywhere, RGB LEDs everywhere doing, you know, crazy patterns to video projected onto trees in the distance projecting movies and stuff to someone had a RGB laser projector that was playing vector arcade games on the side of a building. There was everything. And, I mean, everything from the cool to the weird to the who knows. Like, it was really fascinating. And I took a few pictures that are on Flickr that give you, like, 1% of it because it really was impossible to see everything and take pictures of everything. But anyway.

**Dave Jones:** Is there any good place to see video on YouTube or anything like that?

**Ed McMahon:** There should be quite a bit on Flickr. If I can scare up some links, I will post them to the show notes. Okay. And I'll see what I can find. I mean, part of the issue is that it is a hacker conference and photography is discouraged. Of people. And so I didn't have my camera out all the time. But I did take pictures of some of the static art installations. And actually, one of the coolest things that I saw, which is not even that electronics related, was there were at least three video installations where they had digitized the scene that they were projecting onto. And then the projected visuals were mapped onto the 3D scene. Oh, cool. So you actually had stuff like line art tracing features in the scene that the projector was projected onto. And it kind of blew my mind, the sophistication. And I think people just do this in their spare time. You know, this was better visuals than I've ever seen anywhere in my life. Like totally jaw-dropping. And this goes on for like five days. I think we were there for five days. And it rained quite a bit. So we had some weather-related issues. But overall, it was... Water and electricity, right? Water and electricity. But I got to tell you, these guys know how to do it. They've been doing this for many years. And so they really know how to waterproof everything. All the lighting stood up to the rain and to the wind. But some of the highlights actually were... The program featured actually a special focus for some of the talks, which is a hacker space program. And Nick Farr, who's an American, I guess, advocate of the hacker scene, proposed a plan, which may seem a little bit ridiculous, but I think he was being serious. So he's proposing a hacker space program, which has three components. Wait, wait, wait. Hacker... Hackers in space. Hackers in space. Okay. That's right. So part one, he wants to build a global satellite internet network, which is censorship-free. So no government can turn off because it's satellite, right? Step two is he wants to put a hacker in orbit. And I think that includes hopefully getting them back. Details. And then step three is they want to put a hacker on the moon by 2034.

**Jeff Kaiser:** And bring him back as well?

**Ed McMahon:** There were a lot of eye rolls during this. But, you know, I think really at the root of it, it's about motivating people to pursue space. Do what NASA's not doing right now. Exactly. Exactly. Yeah. Wow. That's right. So...

**Dave Jones:** And so we should mention, too, that you said hackers space program, right? We should also mention that four years ago, that actually is what kicked off the United States-based research, or I guess, upsurge in hackerspaces. Yes.

**Ed McMahon:** Absolutely. So the hackerspace movement in the United States was a direct result of Chaos Camp in 2007. And there were a bunch of people there that... Mitch came back and started noise bridge and everything else. That's right. That's right. That's right. And actually, Chris, if I can check off another bingo square, there were a lot of amateur radio. Or ham. Ham is, yeah. Or ham, as some people call it. And actually, one of the cool things is that there was a station put up by some of the guys from Vienna from Metalab. And they actually did two meters, so 140 megahertz moon bounce at the camp. Nice. So they had this huge dual Yagi antenna that they had driven to camp and set up over the week. And I understand that they didn't actually make a complete contact. They were heard by several stations around the world. And they also were able to copy part of a transmission that they later figured out was for them. So they had some challenges, but they had it like 90% working, at least. And they were allowing people to go over and check out their equipment. And I thought that was cool. I mean, because you think about so many people would say, well, I can't even do that at my house. These guys just set up at a campsite. Right.

**Dave Jones:** Moon bounce is usually doing like really low temperature electronics as well, right? Because it's so sensitive.

**Ed McMahon:** It depends. But yeah, I mean, they had some sensitive LNAs and stuff that were mounted on their antennas. But these guys actually didn't even have their ham licenses more than two years ago. So these are all like brand new hams who got their license just to do this kind of stuff. And they're moving much faster than, you know, I mean, they figured out how to do it and they set it up. And I have a feeling that next time they try, they'll be able to pull it off because it is a big challenge. They were aiming their antennas manually because they didn't have time to set up a rotator. And it was just cool to see these guys like with ropes out there eyeing the moon and trying to swing these antennas. It was totally like that. But if so, so that, that was really cool. But actually the thing that I was there for is I gave a two workshops on building a Geiger counter that I designed. And there's kind of a funny story, which I probably can't get too far into because we're running out of time.

**Dave Jones:** We're 10 minutes over.

**Ed McMahon:** Well, we can just, we can go out and remove some portions of the show, which were less

**Dave Jones:** interesting.

**Ed McMahon:** The long story short is that I designed a Geiger counter for, specifically for the conference because I wanted to be able to give workshops and provide something. There was a hardware hacking area where people could solder together kits. And I'm like, what do people want? You know, what do people, are they interested in right now? And radiation and sensing radiation seems like a big thing because of Fukushima, because of all this sensationalism about radiation exposure. And so one month before the conference, I decided I was going to do it. Two weeks later, I had a PCB designed out for fab. Two weeks after that, I had PCBs back. Three days before I left for Europe, I got all the parts, put them in the bags. And I flew it out there and 30 people built kits. Nobody had problems. It all went 100% to plan. And people were really excited about it. So if I can, I guess this is shameless self-promotion, but if anyone's interested in checking out these kits or building one of their own, I'm going to be at the New York Maker Faire in about two weeks. And I'll actually be selling kits. So it was a huge amount of fun. And I'm definitely going to go back to the next conference, which is actually in the Netherlands in two years. So they stagger them between the Netherlands and Germany. And the Dutch conference is actually just as much fun. I went to the one in 2009 called Hacking at Random. And it's similar, maybe a little bit smaller, but just as cool. So I highly recommend these Europe hacker conferences. They will absolutely inspire you and change your life. So yeah, it was great. It was awesome. It's great to be home. But I got to say, it was just totally awe-inspiring to go to one of these things. That's great, man.

**Dave Jones:** Sounds like, Dave, you should fly the other way and meet Jeff over there. Yeah, right. Jason, you should get TI to fly out there.

**Jeff Kaiser:** Sounds good. Somehow I've got to increase the interest in the Geiger counter world. That ought to justify it.

**Dave Jones:** Well, I think just the general hacking side of things, I think that, you know, just say we need to sell more Beagle boards in Europe.

**Chris Gammell:** Yeah, I mean, it's interesting. Specifically in the Netherlands.

**Ed McMahon:** Yeah, right. If you think about it, it's an interesting gateway into a lot of these people who are hackers are professionals during the day. And the interesting thing about Chaos Camp is that there's a lot of engineers that are there. And this is their idea of fun. And I think it's a great vacation because you basically spend a week camping in not the wilderness, but you're still kind of off the beaten path. You have all the creature comforts of, you know, your internet and your power and your computer. But you're in this intensely social environment. And the coolest thing was that you can walk around and I visited the tents of many hackerspaces in Europe that I'd never been to before. And after camp, whenever I was traveling through Europe, I got to actually go to the hackerspaces and I was graded with like so much enthusiasm. It was great. It was like I was instantly a friend of these people who I'd never met before. And you just get to see this cross-section of European hacker culture that's just, yeah, it's really amazing.

**Jeff Kaiser:** I think that same sort of thing happened at Maker Faire. I mean, I love going to Maker Faire. I think it's a wonderful environment. But there's no overnight camping. I mean, I'm kind of surprised they don't incorporate some things like that. And more, I mean, there's some pretty impressive art shows that actually happen at Maker Faire and the things that people do with the, you know, the mass of Tesla coils. Yeah.

**Ed McMahon:** I don't know. There's actually, there was some talk at camp that this should happen in the United States. And I wouldn't be surprised if in the next couple of years there is something. I think the closest event like this is TourCon, which I've never been to before. But the last one happened at an abandoned missile silo in the Pacific Northwest, I think. I didn't make it out. I don't think it's as hardware-centric as camp is. But camp has something for everyone. It's not just about hardware. It's just that it's so big that the hardware portion is enough for me to be occupied for a week. But yeah, I don't know. I'd like to see something like this. And I'd like to see the...

**Dave Jones:** If you guys like mosquitoes and blistering heat, we could have it in August in Ohio. I mean... Or blistering heat, we could have it anytime in Texas. So I'm just saying. We can have this happen. So, Jeff... All right, guys. I hate to be a killjoy, but we're 15 minutes over. Oh. Oh. The amp hour plus one quarter.

**Jeff Kaiser:** Can we mention that the Forced and Mems book? Just as a... Okay. Oh, okay. As a closing note. I saw one of the items on the show list was that Forced and Mems is... The books are now back at Radio Shack.

**Ed McMahon:** Mm-hmm. Yes. I didn't think they ever left Radio Shack.

**Dave Jones:** I haven't been to a Radio Shack in a long time, so...

**Ed McMahon:** I was at a Radio Shack last week, and there were quite a few... Forced and Mems books there. They had, like, different covers, so they look a little different than the old engineers' mini notebooks do. But, you know, I haven't been to Radio Shack much in the past 10 years, so maybe they did vanish for a time, but I didn't realize that they actually stopped carrying them completely.

**Chris Gammell:** They must have, because they made a big announcement that they're back, so...

**Ed McMahon:** There you go.

**Chris Gammell:** They were out of stock, but they just restocked. Maybe they just had all stock. Yeah, yeah, yeah. Okay.

**Ed McMahon:** That's right.

**Chris Gammell:** All right, guys.

**Ed McMahon:** Well, thanks for having me on the show.

**Jeff Kaiser:** I appreciate it.

**Chris Gammell:** Thank you very much, as usual, Jeff. And Jason, thank you very much.

**Jeff Kaiser:** Hey, thanks for having me on the show.

**Chris Gammell:** See ya. See ya, guys. Bye.

**Speaker ?:** Bye.

**Jeff Kaiser:** So the thing I didn't manage to mention on the show is the working name. Oh, okay. The names tend to stick on these boards and the working name for the next...

**Dave Jones:** Yeah, so this is like what we talked about earlier in the show with you get to make up, you know, like BeagleBoard, how it started with Gerald's Beagle and everything, right?

**Jeff Kaiser:** Yeah, and how the internal project names tend to stick. Well, the working name for the next BeagleBoard is the BeagleBoard Bone. So it's the treat for the BeagleBoard.

**Chris Gammell:** T.I. Bone Hardware Hackers.

**Dave Jones:** The marketing options are limitless.

**Chris Gammell:** Unbelievable.

**Dave Jones:** Spectacular.

**Chris Gammell:** BeagleBoard Bone.

**Jeff Kaiser:** You know, it's bad to the bone.
