---
episode: 128
title: Layout, CAD & Raspberry Pi - Kedogenous Kinetic Knowledge
url: https://theamphour.com/the-amp-hour-128-kedogenous-kinetic-knowledge/
---

**Chris Gammell:** This episode of The Amp Hour is brought to you by Electronicsurplus.com. From vacuum tubes to semiconductors, Electronicsurplus offers a huge selection of current and legacy products that integrate into your next design. Electronicsurplus also specializes in hard-to-find replacement components and off-the-wall parts you can't find anywhere else, all offered at some of the lowest prices on the Internet. To learn more about Electronicsurplus and to support the show, go to theamphour.com slash es and you'll be whisked away to an online marketplace of weird and wonderful things. This is The Amp Hour Podcast. Recorded January 15th, 2013. Episode 128. Kedogenous Kinetic Knowledge.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**Dave Jones:** Hey, Chris.

**Chris Gammell:** Top of the morning, Dave, for you, I guess.

**Dave Jones:** Yeah, it is. Bottom of the eighth here. On the show? Well, no, it's 11.30 here. Yeah. I've got to get this out of the way. You know who I hate?

**Chris Gammell:** Who's that?

**Dave Jones:** The United States government.

**Chris Gammell:** I've heard that before.

**Dave Jones:** Here's another classic example of them screwing up the tech industry.

**Chris Gammell:** Oh, I know.

**Dave Jones:** Economic development and the tech industry. It pisses me off. You know what they've done?

**Chris Gammell:** Dave, you know, you've got to listen to Rolling Stones. You can't always get what you want, Dave. And I bet you didn't even sign that goddamn petition.

**Dave Jones:** I do. Well, I'm not. Am I allowed to? Well. I'm not a U.S. citizen.

**Chris Gammell:** I don't know if you're allowed to either.

**Dave Jones:** Anyway, folks, what I'm pissed off about is the United States government denied a petition from the people to build a Death Star.

**Chris Gammell:** Seriously?

**Dave Jones:** Yep.

**Chris Gammell:** How could they?

**Dave Jones:** Imagine the jobs it would have created. Imagine the electronics. Imagine the tech industry. I know.

**Chris Gammell:** You know that the controls for that Death Ray is, there's got to be some cool stuff in there, right?

**Dave Jones:** Well, there's a nice big handle that, you know, they move forward and powers up, you know. Yeah. Yeah.

**Chris Gammell:** You have to wear that funny helmet, right?

**Dave Jones:** That's got to be worth a couple of million bucks, you know, just that nice chrome-plated handle, you know. Yes. There was an official government petition. Apparently, you can go to the White House Gov website or something, and if you get, what is it, 35,000 signatures or something?

**Chris Gammell:** 25,000, I think.

**Dave Jones:** 25,000 signatures, which, you can get that on any forum these days, can't you? Anyway, somebody petitioned the government to, they wanted them to build a Death Star. I think it was actually 4chan.

**Chris Gammell:** I think it was like, this was actually just a bunch of trolling, and then, you know, they And then they did it.

**Dave Jones:** They got, yeah. It's fantastic.

**Chris Gammell:** Yeah, and I'm sure a lot of people out there have seen it before, but.

**Dave Jones:** Yeah, well, you know.

**Chris Gammell:** But the response is just, I mean, this is how you do the internet, right? I mean, this is the chief of science and space branch at the OMB, and. The OMB? The Office of Management and Budget. Basically, they kind of figure out how deep of crap we're in.

**Dave Jones:** Yeah, so this is one of the senior dudes at the White House, in the White House department who responded to this, right? Because they have to, by law, I think, once you get the number of signatures, they have to look at it. No, it's not law. They have to consider it. No, it's not law. It's just a promise, but. Right. But still. Oh, okay. Right. But still. Yeah. Mate, a promise. Promises as good as a law. Hold the bastards to it.

**Chris Gammell:** Yes. A promise is as good as a law, one coming from a politician.

**Dave Jones:** Yeah.

**Chris Gammell:** Oh, boy.

**Dave Jones:** And they officially responded. If you haven't seen it, please check it out. It's great. Yes.

**Chris Gammell:** We will link that in. It's very good. Lots of nerdy references. Lots of nice links. There was another one on there, though, that I liked even more. Oh. Do tell. There was one about actually, I mean, making the metric system an official, the official measurement system of the US.

**Dave Jones:** Oh, I saw you tweeted that. Yeah. Yeah.

**Chris Gammell:** And this is obviously a serious petition, right? Yeah. I guess this is a little more serious than the other one. Later, Josh Meyer on Twitter, he actually alerted me to the fact that it actually is the official measurement system of the United States.

**Dave Jones:** Right. I believe, yes. I think he's correct.

**Chris Gammell:** I didn't know that.

**Dave Jones:** Yeah. They just don't implement it.

**Chris Gammell:** Right. Exactly. It's more of a guideline.

**Dave Jones:** No, I think on food. Isn't food, doesn't food now have to come in grams? I think food by law, food is, oh, dual. Right. Okay.

**Chris Gammell:** Got it. Yeah. But yeah, there's actually, you know, we've been on metric since 1866, apparently. But, you know, it's not in all the, you know, the road signs aren't like that. Yeah. Right. You know, there's shades of gray for all this stuff, right? I mean, like.

**Dave Jones:** I'm sure we talked about this before, like 50 episodes back or something, and somebody pointed out that, yes, they are metric, or you guys are metric, and yeah, they just don't care.

**Chris Gammell:** Yeah, it bugs me. I don't know. Right. I still wish it would happen.

**Dave Jones:** Yeah.

**Chris Gammell:** It probably won't, but.

**Dave Jones:** I started laying out a board the other day. I used metric for traces.

**Chris Gammell:** Really?

**Dave Jones:** I don't know what, yeah, I don't know what possessed me to do that, because normally I only use metric for, you know, the physical dimension, like the physical stuff, like the board dimensions. Yeah. Well, the grid, you know, the grid often, because the, you know, SMD components are often a metric grid these days, some of them. And like whole sizes, you know, those sort of manufacturing things I always do in metric. But traces, I've always done traces in Imperial, you know, mills. You know, a standard, you know, a standard 10 mil trace, standard 10 thou trace. Yeah, but I decided, bugger it, I'll use 0.2 millimeter traces this time and see how it goes. I don't know. Well, I've done it before where I've been forced to because, I don't know, some anal retentive wanted me to do it for some reason, but.

**Chris Gammell:** What's the reason you do it the other way anyways? I mean, is it, what got you started on Imperial? Oh, it happens.

**Dave Jones:** I've been laying out boards with CAD software for, well, since before you were born, sonny. And I've always used Imperial. And it's just, you know, second nature to me. I know what a 10 thou track is, you know, a 0.2 millimeter track doesn't. Oh, yeah, yeah, yeah. I get that.

**Chris Gammell:** But I mean, what was the initial reason? Was it because the CAD programs didn't offer metric? Or I mean, you've been on metric most of your life, right?

**Dave Jones:** Well, you're talking back in the old days.

**Chris Gammell:** Yeah, yeah, yeah. Like how you got started on that.

**Dave Jones:** Everything was done in Imperial. Everything was done. Now, they did offer metric, but, you know, Imperial was just the given thing that you used. Everything you read, you know, all of the manufacturers, they gave you their manufacturing tolerances in Imperial. You know, we can do 8 thou track and space. So, that's what you set your limits to, you know?

**Chris Gammell:** Yeah, yeah, yeah. Okay.

**Dave Jones:** And that's still very common today. I'd say probably, oh, maybe a majority, I'm not sure, but, you know, it's probably half and half of the manufacturers out there will still specify their manufacturing tolerances in Imperial.

**Chris Gammell:** Yeah. Yeah, it's silly too because it's so arbitrary, right? It's like, yeah, they say 6 and 6, you know, space and trace, but, you know, you could just as easily say whatever the, what is the conversion, like 3.9 or something like that? So, it'd be like, you know, 23, you know, 23 space and trace kind of thing, you know, in millimeters. And it's like, okay, you know, I don't know.

**Dave Jones:** And, well, yeah, and like, and of course, 0.2 millimeters is around about 8 thou, you know, give or take a couple of, you know, third decimal places or something. So, you know, I don't know. Yeah. It's just, yeah. It's a lot of convention, you know. Yeah.

**Chris Gammell:** I guess old habits die hard. Yep. So, what made this time be different? Why? Oh, I just. Was it just a lark? I mean.

**Dave Jones:** I just thought, ah, what the heck, you know, just do it for fun, you know. Yeah.

**Chris Gammell:** You know, I really want to take longer on this. I need to re-acclimate. I need to. Why don't you just switch over to a new CAD program too, Dave?

**Dave Jones:** Yeah. God. Did you? No. No, I didn't. No. Because I'm still working on the same bloody arse project I've been working on for years. Right, but you switched over, so why not at that point?

**Chris Gammell:** You might as well have switched.

**Dave Jones:** Well, yeah, but, ah. You know, but then you've reset all the work you've done. I've already got all the component libraries and everything, you know, in there and all done and all sorts of things all already done in the existing package. So to start from scratch again would be, yeah, a pain in the arse. It would be tough.

**Chris Gammell:** Yeah, you're right. Yep. You're right.

**Dave Jones:** And I still don't know the best one to choose because I haven't properly evaluated them.

**Chris Gammell:** Right. So, you know. Spend all your time complaining about how your project's not done.

**Dave Jones:** Well, I guess. Well, yeah, exactly. I guess the only, ironically though, the only good way to figure out which is the best package is to actually do a full project in it.

**Chris Gammell:** Oh, yeah. You just got to swear. You need to, I'd say the best way to learn a new package is to swear at it. If you're swearing at the PCB, you know, software you're using, then you're learning. If you're clicking along and, you know, in a groove, then you've learned. At least at a temporary state. But, yeah. If you're not swearing at it, you're not learning it. That's it. Oh, boy. Which, it's unfortunate. I've been doing that on the more theoretical side of things. I've been like back and forth on this grounding scheme I've been working on. And, man, I was just, I was screaming. I was literally screaming on Friday about it. And I spent all weekend reading about it. And, and, and actually there's, I should mention this. I mentioned it online before, but there's actually this really, really great analog devices book that's free online. And I'll put the link in the show notes. I might have to find it. I forget the guy's name. It's Hank something. But it's the, it's a linear circuit design book from analog devices. Cool. And, oh, yeah, linear circuit design handbook. And it's all available free online. And, and, you know, you can get a print copy for like 80 bucks. But, you know, if you're reading PDFs, I mean, like, it's killer. And it's all the, at first, at first when I found it, I thought, I thought I was finding like a secret stash.

**Dave Jones:** Yeah, right.

**Chris Gammell:** Like buried on analog devices site. But no, it's actually, there's actually a page that I can link in and, and they, they offer it all up for free. And it's great. It is really great. It's Hank Zumbelin. Published in 2008. Yeah. Oh, it's, it's really, really good. So as an analog person, I highly, highly recommend this book. It's a.

**Dave Jones:** Brilliant. So what's this ground thing you've been working on? Is this like a PCB grounding thing or is it a system grounding thing?

**Chris Gammell:** Well, it, it is, I mean, it's a system level on the PCB. So like multiple grounds, multiple rails kind of thing. And just kind of figuring out star ground and where current, you know, like, and that's what this book by Hank talks about too, is, you know, follow the current. That's the important thing. You know, you gotta, you know, I knew a lot of this stuff.

**Dave Jones:** Well, more important than that, current loop. That's, that's, yeah, yeah, yeah. That's the essential thing, current loops.

**Chris Gammell:** I guess that was implied in my statement, but yeah. Of course. When you're looking at grounding, obviously you're implying that it's gotta, it's gotta come back at some point too. I remember that too.

**Dave Jones:** Yeah, circuits have to complete the loop, you know, as you learn, you know, when you have a light bulb and a switch, it has to complete the circuit, yeah.

**Chris Gammell:** Right, right. Yeah, and when you got a ground plane, I mean, that's, that's the crazy thing about it, you know, like, when you got a ground plane, it's just a sheet of copper, right? But, hmm, a lot of times...

**Dave Jones:** But it has inductance too. Yeah, it has inductance. It has inductance, and that's why it will follow the, the current will follow the least inductive loop path. So current doesn't evenly flow across a PCB ground plane. That's right, that's right.

**Chris Gammell:** At, yeah. At high frequency, at DC it does. And that's, you have to watch out, because oftentimes they get higher frequencies that'll follow right underneath whatever trace you're sending the signal out at. But, um, I do a lot of lower, lower current stuff, but, uh, you know, a lot of that same stuff still applies. Not all of it, obviously, but, um, yeah, so it's been, you know, I've just been reading and banging my head against the book, well, not the book, I guess the screen, because it's a PDF. And, uh... Right. Yeah, it's a great book. And, you know, it's, it's hard to find a lot of this. You know, even, you know, I even reread your PDF, the, the, uh...

**Dave Jones:** Oh, the PCB design one. Yeah. Yeah.

**Chris Gammell:** You know, it's, like, when you're at that point where you're banging your head against something, you just kind of start grasping at whatever you can find.

**Dave Jones:** Hoping you can find a nugget of information that solves your problem, you know? Exactly, exactly. Yeah.

**Chris Gammell:** It's kind of, it's kind of manic, actually, you know, it's like, you'd probably end up missing a lot of good stuff in the end. Like, I guarantee if I reread the chapter I was reading on it, that it would, um...

**Dave Jones:** No, because... I would find new stuff. Yeah, exactly. Yeah. But because you're in such a frantic state, yep. Yeah. Yep, been there, done that. I tend to thrive under those conditions, though. My wife doesn't understand it. You know, I'll get so aggro and I'll start shouting at the screen and getting myself all worked up and she doesn't understand why I get so aggro. It's because, you know, my senses are more finely tuned at that point. You know, I work more efficiently when I'm angry and under pressure and...

**Chris Gammell:** Yeah. Well, and you're well-practiced at it, too, right? I mean, like... Yeah, yeah. That's just what work does to you, right? When you're under the gun, you know, and you've... Yep, yep. You just have to perform, then you've kind of developed a whole other set of working habits that might work better. Exactly. You might not be able to replicate when you're... Yeah. You know, like getting into the flow, right? You might not be in the flow... That's right. ...when you're not under pressure. Mm-hmm. But if you've got 10 hours to deliver, then you're going to be a lot more efficient with your time than 10 days.

**Dave Jones:** Your mind starts subconsciously focusing better, I think. Yeah. Rather than wandering all over the place if you know that you haven't got a deadline.

**Chris Gammell:** Oh, yeah. Yep. Oh, yeah. Nothing like a deadline to get you going. See, that's what you need. You know, Dave, I will gladly offer my yelling at you services for $200 an hour. Or you pay me $200 an hour, and I will tell you you need to finish something. I'm sure many of our listeners are off to that same service.

**Dave Jones:** What does that work out to, you know, how much per shout?

**Chris Gammell:** Per shout? Oh.

**Dave Jones:** Yeah.

**Chris Gammell:** About $350.

**Dave Jones:** So you can... What? How about I just pay you per shout, and then you can just randomly shout at me once a day or something like that? Hmm.

**Chris Gammell:** I guess that wouldn't work for the time change. There's a startup idea.

**Dave Jones:** Hey, that's going to be a startup.

**Chris Gammell:** Yeah, you know, there's people that do, like, they do, like, human interaction. Like, I remember hearing a story about some late 20s female who would come over to your house and cuddle with you. You know, like, she would, you know, it was not... It was strictly non-sexual, but it was, like, just, like, you know, human contact. It was a cuddle.

**Dave Jones:** Okay.

**Chris Gammell:** And it was, like, that's weird. And this would be, like, the other side of it, right? It's like hireadrillsergeant.com.

**Dave Jones:** Exactly. Oh, man.

**Chris Gammell:** You might have hit gold here, buddy. I could have. Yep.

**Dave Jones:** We'll find on Kickstarter shortly.

**Chris Gammell:** Yeah. Speaking of procrastinating, how's your board going? You were mentioning that before the show.

**Dave Jones:** Yeah. I started, I decided, after I tweeted, I think, after last Tuesday. You know, I'd done, like, three or four videos in a row or something. Three videos in three days or something. And I thought, bugger it. I'm going to take the rest of the week off and I'm going to work on my project. And that's pretty much what I did. You know, I've got other things to do, too, obviously, that always come along. But, yeah, generally, I spent pretty much three days working on my projects. I was pretty darn happy with that. I wasn't pleased with the, you know, I thought I'd probably have, you know, I'd have the board finished and stuff like that. And I'd be able to send it out. And, eh, no, I didn't, you know. But I got the schematic finished. I got a new bomb finished. And I got part of the board laid out. So, I was, you know.

**Chris Gammell:** Oh, yeah? At least starting. I mean, that's probably pretty good.

**Dave Jones:** Yeah, well, you know. Well, because you don't start with your whole board component placement. But you fix your major components in place that you want to. Okay, these are fixed. You know, your front panel controls and your battery and your other stuff. You know, physical connectors and stuff like that, all there. And then you start routing out little modular blocks. So, I routed out a couple of modular blocks and dragged them in. So, it's starting to take shape. Yeah?

**Chris Gammell:** You stick into two layers?

**Dave Jones:** Oh, yeah. Yeah, of course.

**Chris Gammell:** Always. Yeah, I guess. Yep. Well, not always. I mean, not always, right? Well, no. For hobby and stuff. Yeah, because of cost.

**Dave Jones:** But for a simple power supply project, it doesn't need to go four layers. If I've gone four layers, I've failed. As a layout guy, you know, if I have to go to four layers for such a design, that's, you know, a complete cop out and failure. So, yep. Not going to happen.

**Chris Gammell:** So, do you not do, you don't do like power, obviously you don't do power planes or ground planes or anything like that. But do you do like pours on the top planes? Top and bottom?

**Dave Jones:** Oh, yeah, yeah. Well, that's right. I will try and lay out everything on one side. I've talked about this before. I've even done video on it. Like a time lapse video of me laying out a board doing this. And, yeah, I'll try and route everything on the one layer. So, I'll do it as a one-sided layout first. That's probably the key to doing a good double-sided layout is to lay it out as if it's a single-sided board first. And then, at the end, you know, generally, if you're lucky, you'll be left with just a few power traces and stuff like that, which you can run on the bottom. But then, generally, you'll be left with a huge, big ground plane on the bottom.

**Chris Gammell:** Yeah.

**Dave Jones:** Generally. Or on the top as well, and then you can stitch it together and it floods, you know. Yeah. And, yeah. So, that's how I'll generally try and lay it out.

**Chris Gammell:** See, I understand the two-layer thing, but I still, I don't like just the floods. Because I see people who do that, and then, like, I look at the actual floods, and it's like, well, it gets all chopped up. You get these little islands of, like, nothingness. Oh, yeah, no.

**Dave Jones:** I've got auto, my software automatically removes, you know, islands. Yeah. Under a certain size and stuff like that. But, yeah, no, I'll generally, I won't just fill in copper for the sake of it, but on the bottom side, I will. You know. Right.

**Chris Gammell:** Well, I didn't figure you would, but.

**Dave Jones:** Yeah, right.

**Chris Gammell:** You know. I see that. I see that even on, like, dev boards and stuff like that. And I'm like, really? Like, why? Yeah. And maybe it's just a time thing, or maybe they're just giving it to the new people, but.

**Dave Jones:** Yeah.

**Chris Gammell:** I say as the new person, you know. Right.

**Dave Jones:** Yeah, yeah. Well, sometimes you have to. Sometimes there's reasons to do it. Like, if you're doing a really large board, you can get warpage if you've got excess, you know, plain copper on one side and stuff like that. Yeah. Right. Yeah, you've got to think about that sort of thing. But, you know, the boards I'm working on, you know, just six inches by two inches or something. So.

**Chris Gammell:** There it is with that Imperial again. Man, you'll never make it in America. Sorry. Oh. Yeah. So you were mentioning that the layout took a good chunk of that time. What was the issue there? Or not the layout, the schematic.

**Dave Jones:** No, the schematic. Oh, just, you know, new bomb items. You know, I'm changing the design a little bit. Oh, this DC to DC converter is not available anymore. Oh, it was available two months ago. Oh, and the one that wasn't available two months ago is now available. Oh, I'll reuse that one. So I changed my DC to DC converter chip. I changed my charger chip because I wanted higher current. And, you know, so then you go through that whole iterative process of doing the whole bomb thing and, you know, finding alternatives, finding the lowest cost and availability. And so, yeah, I spent, you know, two days just dicking around. Yep. You know, on DigiKey and mouse are trying to find suitable parts, really.

**Chris Gammell:** Yeah. It's the thing I hate about that is like you can. I feel like, for me at least, I can do it so out of my element where I'll, you know, I'll go for like two days and I'll do the same thing where, okay, I need to find a new DC to DC converter. And then I find one, I implement it. And then I look at the schematic and I realize, oh, I didn't need a DC to DC converter at all or something, you know, like something stupid like that. Yeah, yeah, yeah. Right. Yeah, exactly. I'm going to change this thing over here and now I don't need a DC to DC converter at all. Exactly. You know, like that kind of thing. Yep. It's just, there's so much churn. It's very, there's no getting around it, but.

**Dave Jones:** Well, sometimes you can just say, right, that's enough is enough. It's kind of sort of going to work and I don't care. And sometimes that's all you need. You know, if you're just doing a one-off test jig or something, you don't give a toss about that sort of stuff. You just want something to hack together, something that works. Right. Right. But no, this is different, right? This is a project I'm putting quite a bit of little, you know, quite a bit of pride into and, you know, stuff like that. And I just like, and I enjoy doing that. Yeah. Well, I've done like 15 videos on it, right? Yeah. So, I'm not kidding. I think it's 15 or 16 videos. Oh, really? Well. Both the designs, yeah. So, that's a lot. Oh, boy.

**Chris Gammell:** Well, I think.

**Dave Jones:** And one of the interesting things I found, though, I tweeted this one as well, is that I ended up, like, the design has like over 60 resistors.

**Chris Gammell:** Is that a lot for you? It's a lot for you.

**Dave Jones:** Yeah, I know. It's a lot. Right? That's a lot for you. It's a power supply, honestly.

**Chris Gammell:** I've got a design with like 600 resistors. Oh, yeah, I know.

**Dave Jones:** Well, yeah. I've done that, too.

**Chris Gammell:** So, switch to 402. What's your problem, you know? No big deal. Come on. What's the big deal?

**Dave Jones:** But I, you know, it's just, where do they all go? You just need, you know, you think, oh, everything's in chips these days, right? But no. No, no, no, no. It's just, yeah, this simple.

**Chris Gammell:** Everything's in chips these days, including firmware, which can, not our firmware, but I guess logic that can be set by resistors. You know, before you would have to have a FPGA to talk to it in order to set those same parameters. But now they just pull it internally and they say, well, just set a resistor and we'll figure out the rest. Yep. Yeah.

**Dave Jones:** But, you know, every time you drive a transistor, you need a resistor. You know, if it's an open collector, you need a pull-up, you know. If you want to do a little RC filter, you know, two-stage, well, there's a couple of resistors, you know. Well, if you need some voltage dividers, there's more resistors.

**Chris Gammell:** Yep. Well, just thank your lucky stars. They're cheap, man. And stay away from the precision ones. You'll be fine. Yeah, I have.

**Dave Jones:** All just standard 1% stuff. And I switched back from 0603 to 0805. Oh, wimpy. I just wanted them to look big and chunky, you know. Yeah.

**Chris Gammell:** I guess it's friendlier for kit stuff.

**Dave Jones:** Well, it's friendlier for, yeah, if people want to hack it, you know. If people want to get in there and change the values, it's, you know, it's just nicer, I think. So, although ordinarily I'd probably choose 0603 would be my standard part these days. That'd be my standard size.

**Chris Gammell:** I think that's kind of to the point where, I mean, not the majority of stock, but I'd say if you were looking at a distribution, I mean, you'd be in very safe territory with 0603 for the next. Oh, yeah. Yep. Yep. Yep. For sure. 10 years? Maybe that's a stretch. I don't know. Yeah. Five years at least.

**Dave Jones:** Anyway.

**Chris Gammell:** But, yeah.

**Dave Jones:** That's enough of my power supply project.

**Chris Gammell:** If I've got any fancy resistors, I make sure they're, you can't get any fanciness in 0402.

**Dave Jones:** Oh, no. You'd want a damn good reason.

**Chris Gammell:** Right. Exactly. Yeah.

**Dave Jones:** Like you design a mobile phone or something or a hearing aid or, you know.

**Chris Gammell:** Oh, you're doing mobile phones or hearing aids. You're going 0201s or 0105.

**Dave Jones:** Yeah. That's what I'm talking about. If you're going better than 0402s.

**Chris Gammell:** Oh, no.

**Dave Jones:** And here we are talking imperial. That's true. Why don't we talk metric? See, I don't even know the metric ones. That's why I've got my little PCB ruler here, you know, that I gave out at the trade show. It's got the, like a 0805, here we go, is a 2012, and an 0603 is a 1608, and an 0402 is a, you know, a 1005. It's like, I don't know those metric ones off the top of my head. I'm slowly learning them, but it's, you know.

**Chris Gammell:** It would be easier for, you know, talking about when you get really small, right? Instead of saying 010, whatever you say, 0.5 or, you know, 0.05 or whatever. I don't even know how people, I never touch them, so I don't even know how people say them.

**Dave Jones:** No, I don't touch them. I don't get that small.

**Chris Gammell:** No. That's definite. That is binocular, or microscope land. I don't like microscope land. I can't drink coffee at that point. Right. Yeah.

**Dave Jones:** Oh, boy. Anyway, so that's why I've got my PCB ruler here. It's handy. It's got the little conversion, you know. Because if I'm, you know, if I'm searching for a, and it's in a footprint library, then it might have just the metric number on it. You know, it doesn't have the imperial, you know, it doesn't say 0805.

**Chris Gammell:** Yeah.

**Dave Jones:** It's a pain in the ass. It says 2012. 2012.

**Chris Gammell:** It's too bad they don't do it the other way around, where, you know, like, if it's metric, you can do the other, like, 1220. You know, like, so you do the short side first. Because you see that reference sometimes. Oh, right. Some people do that, and I'm not sure why they do. But that would be, I feel like that would be a good way to delineate the two so you could tell them apart.

**Dave Jones:** Right. Okay. Yeah, yeah. Because some of them are identical. Like, there is like an 0402 in both ones, you know, and technically you don't know which one you're talking about.

**Chris Gammell:** Oh, good lord.

**Dave Jones:** So. That would be really small for metric. Oh, yeah, yeah, exactly. But, yeah, I think there is one that is an overlap between the two, and it's very confusing. Yeah.

**Chris Gammell:** That is confusing. Yeah, so I think people should switch them around. That would make it easier. Yep.

**Dave Jones:** Now, we were talking about Kickstarters before. And, um.

**Chris Gammell:** Uh, you mean like every last, every episode in the past 127? Yeah, exactly.

**Dave Jones:** But, no, yeah, let's talk about it again. Why not? Um, because you were a bit miffed. Oh, you felt a bit funny about this one. Yeah, it's not bad.

**Chris Gammell:** I mean, it's just weird. You know, it's. Well, tell us a story. So, there was one, I saw there was a post on probably Reddit or something like that. But, you know, there's a Kickstarter for a open hackable Linux plus ARM embedded GPIO module. And it's on like an SODIM. Yep. Is that what that is? It's like laptop memory. Yeah, it's an SODIM memory. Yep.

**Dave Jones:** Yeah. Not seen quite a few of those. But that's not what. You know, that's, that doesn't matter at all.

**Chris Gammell:** No, no. It's just. Tell us what bugs you. It's weird because it's, you know, you start the video. Okay, this looks like a cool little board. You open it up. And then. And. And it's. It's a company that's doing it. And it's like, oh, well. Why. Why is a company doing this? You know, like, I guess. Uh-huh. That's. That's my first reaction. Then the second reaction. Well, Peppa Watch was like a company. Weren't they? I mean, they were a company beforehand. So. My brain starts to go into like, well, where do you draw the line? And, you know, like it. In the end, it doesn't really matter. Because. Yep. I have no say in any of this anyways. But it's just. It's just interesting. And potentially dangerous. If, you know, because. There's 30 days to go left on this one. There's like 5,000 out of $30,000 gold. I'm not sure. They might make their gold. They might not. But. It's just more of a. You know. If this becomes more commonplace. If. If there are companies that start doing this kind of thing. It just dilutes it all. And. But at the same time. You know. Like you could miss out on something really cool. Right. There could be a company that like. Like say there's a bunch of engineers at Intel. And they get to go ahead to. You know. Make some. Open source processor. In the fab. Right. But they need. You know. A hundred grand to do so. That could be cool. So at the same time. You know. Like it's. I don't know. It's just so much a conflict.

**Dave Jones:** A lot of people may not know. Who this company is. If you haven't worked with LCDs before. Then you may not have heard of. Crystal fonts. America. Fonts. If that's how you. With a Z. If that's how you. Yeah. Pronounce it. I've used their LCD modules before. Right. They're a manufacturer. They're a US. I don't think they're manufacturing in the US. But anyway. Right. They're a. They're a manufacturer of LCD modules. And stuff like that. Quite. One of the big players. Right. So they're. I'm not sure what they're worth. But there are. You know. You can buy them at DigiKey. And you know. They're a major player.

**Chris Gammell:** The high. What's that? The high. Not aspect ratio. Darn it. What's it called? Where like the. Contrast ratio. They're like high contrast.

**Dave Jones:** The high contrast. Yeah. They make high quality LCDs. They don't make one hung low cheapies. They make. You know. These are the ones. You know. You know. They cost 10. You know. Bucks each. Where you can get them on eBay. For 50 cents. You know. Yeah. Yeah. So they make high spec LCDs. So it's a big company. But now they've decided to. Man. I don't know why. I haven't played the video. But yeah. I don't know. And then they're asking for like pledges as well. Like you know. You can pledge like. Just give them money. For just because they're cool. And they're developing this thing. You know. So you don't get anything in return. You just pledge.

**Chris Gammell:** Yeah. Yeah. Yeah. And that's okay. I mean. I don't know. I don't know.

**Dave Jones:** Well. The changing landscape of Kickstarter. But that's the other thing. A lot of people may not know. It's a big company. I haven't watched the video.

**Chris Gammell:** So I'm not sure if they do it. If you open the video. It becomes very apparent very quickly. When you have a round. Okay. When you have a group of techs sitting behind you. With the same name on their shirts. You know. And they say they're from the company. Right. Okay. They are upfront about it. And they are. And that's fine. Right.

**Dave Jones:** That's good.

**Chris Gammell:** And it was like a hobby project there.

**Dave Jones:** Why do they need to do it? Why don't they just do it? Because they're trying to get publicity. Right. Well. Maybe. Maybe not. It's a free publicity platform. Of course they are. Come on. You haven't seen the videos. You don't know. They don't need the money to do it. They do these every day of the week. They manufacture. Not just LCDs. But they do all these demo boards. To go with all these things. Right. Yeah. So they've got their own in-house group to do this.

**Chris Gammell:** But yes. I mean. Yes. I agree with all the things you just said. But. It doesn't. It doesn't seem like that up front. And that's the other thing that irks me about it. It's like. It's not like. It's not upfront about it. Like here's our new module. Right. They're not very obvious about it. But at the same time. Like that. That. Sneaking suspicion in my head. I'm just like. Oh. Is it? Is it? You know. You're kind of waiting for that other shoe to drop. And it's just like. Yeah. I don't know. Right. I just. Yeah. You know. I like Kickstarter. It's still fledgling. I think it's just. You know. I don't want to see it. Start going the other direction. Yet.

**Dave Jones:** Yeah. I don't. Yeah. I don't think I agree with it. Either. I. You know. If you're a big company. And you can afford to do it. You. Just do it off your own bat. I don't like you using Kickstarter. I. You know. If you're a one or two person company. Fine. Right. But. But they are not. I mean. This. You know. This is a big company. Crystal fonts. Right. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** So. I.

**Chris Gammell:** You know. I mean. Yeah. And they say it's like the engineers within the company. So that's okay. But then it's like. Yeah. Yeah. You guys do have money. So. So at that point. Exactly. Then you're just buying the boards. Which is against the new rules. So it's like. Yeah.

**Dave Jones:** Right. Okay. Yeah. Yeah. So I don't know. How did they get this through. Right. You. You're not allowed to just. Buy the boards. Right. And you're not allowed to do it to set up a company. Yeah. You're not allowed. There's all sorts of. Rules these days. So.

**Chris Gammell:** Yeah. Hmm. Well. On to another board that. We were a little. Skeptical of at the beginning. And holy crap. Has it showed the pants. Or. It showed us up. It beat the pants off of us. I guess. Or our predictions. Oh.

**Dave Jones:** We weren't skeptical. Were we? We just went. I was a little skeptical. Whatever. It's just another.

**Chris Gammell:** I was skeptical about their. Production schedule. People go back and listen.

**Dave Jones:** About their production schedule. And meeting the price point. Yeah. That's the only thing we were. I was. Skeptical about.

**Chris Gammell:** I was wrong. I'm on record. I mean. I'm wrong a lot. But this is another one. I'm wrong again. But yeah. Raspberry Pi. Bingo sheets folks. A million units. That's. That's crazy. That's awesome.

**Dave Jones:** Yeah. Just Farnell alone. Have sold half a million units.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Now this is the interesting thing. Right. It's supposed to be non-profit. Right. The whole idea of this thing from day one was non-profit. Am I correct?

**Chris Gammell:** It is non-profit. Yeah.

**Dave Jones:** Right. But you can't tell me Farnell's aren't making money on this.

**Chris Gammell:** Yeah. But the foundation that created and manages the design. Yeah. I mean. Yeah. I mean.

**Dave Jones:** They don't make money. But Farnell are making money on this.

**Chris Gammell:** That's not how non-profits work, Dave. I mean. There's servicing companies. Yeah. I know. Well. That help. You know.

**Dave Jones:** Yeah. Well. Okay. How about this? Like when the Red Cross is a promotion.

**Chris Gammell:** Like they do like a concert on TV. Right. And you donate $10 through your cell phone. Your cell phone is taking a cut of that. It's just a processing fee. I mean. Like. That doesn't really bug me. There's no. I have no problem with that. Yeah.

**Dave Jones:** Okay. I'm just mentioning the fact that it is non-profit. Farnell make quite a profit.

**Dave Jones:** Profit.

**Chris Gammell:** You don't know how much they make. They're a distributor. They don't make tons of money. Distributors don't make that much money, man. I mean. What? They don't. Oh, shit. You think they make a lot of money? Their margins are incredible. No way. Yes. Why? Maybe on the small stuff. The onesie twosies. How do you think DigiKey is worth a billion dollars? Because of the volume. They do tons of volume. So does Farnell. They all do just tons of volume. Like their margins are like. I remember looking at it. Because I remember. Oh, they can't bring. Okay. I looked at their annual report. And I think it was from Mauser. Right? Because they're owned by Berkshire Hathaway. Which is Warren Buffett's company. Right. And I'm a huge Warren Buffett fan. So I was like. Oh, Mauser's owned by Warren Buffett. That's really cool. And I was looking at. I think it was theirs. Their annual report. And it was like. Oh. You know. Our revenues are a billion dollars. Wow. That's great. And profits of like 50 million. Holy crap. Really? Like that means that you're. That's like. 5%. Yeah. Yeah. It's terrible. I mean not terrible. I mean you're still making money. But just think about the churn there. It's not that great.

**Dave Jones:** Yeah.

**Chris Gammell:** Right. Yep. So the cost of sales is really, really high. And you don't make a lot per unit. You know. I'd rather be Apple. Right? Where you're making 50% on every unit. Yeah.

**Dave Jones:** Their overheads are very large. Their service overheads are very large.

**Chris Gammell:** Right. Overheads are large. And you know. They're effectively an online grocery store for parts. Which is. Yes.

**Dave Jones:** Yep. Tough. Yeah. It's expensive to hold all that stock. And actually distribute it. You know. And warehouse it. And do whatever.

**Chris Gammell:** Yeah. Do you know. I think one of the reasons. In the states at least. There's actually a tax on inventory. If you hold inventory. You can be taxed.

**Dave Jones:** Oh really?

**Chris Gammell:** Yeah. It's weird.

**Dave Jones:** Well it's probably the same. Yeah. I think it's the same here. We have end of year stock sales. You know. I'm not sure how it works. Yeah. I don't give a toss about that stuff.

**Chris Gammell:** Yeah. Until they figure out you're holding a bunch of reels of parts. They'll come get you. Oh yeah. Reels of parts.

**Dave Jones:** I just. Nah. That's just bullshit. As if I'm going to count every. But no. Technically. Right. That's what you're supposed to do. You're supposed to count every single freaking resistor on the reel that you have left over at the end of the. And it's like bullshit. No. I'll just. Nah. I just ride off at the end of the year. And then. And it all evens out over two years. Right. It just. Well at that point.

**Chris Gammell:** It's worth more for you to just say. Well that's a whole reel. That thing costs $40 instead of maybe $30 because there's. I counted all the resistors on there. Yeah.

**Dave Jones:** It's just. Yeah. It's crazy.

**Chris Gammell:** Yeah. Well speaking of stock. We should. We should. We should mention our sponsor from this week.

**Dave Jones:** We have a new sponsor for this episode.

**Chris Gammell:** A new sponsor. And not only that. A Cleveland sponsor. How about that? Woohoo. Local. Yeah. Yeah. Well local for you.

**Dave Jones:** It's still 15,000 miles away from me.

**Chris Gammell:** That's true. Yeah. Yeah. It might be kind of tough for you too. Sorry metric.

**Dave Jones:** But we are talking American here. That's true.

**Chris Gammell:** So it's electronic surplus.com. It's a. Like I said. Local business here. They have an online store though. Dave and I were kind of poking through there earlier. Just kind of looking. I've looked. I've obviously been there before. They actually have a storefront that I've been to. But most of their stuff's online. And. Yeah. There's some cool stuff on here. A lot of older stuff. You know. But good for projects. Like I'm looking at the analog indicators and meters and stuff. And a lot of these things are kind of. They're one off. So. You know. But if you're. If you're making a project where you want to have a. You know. Analog indicator. You can go on here. And. You know. You can find something like that. And make it look.

**Dave Jones:** That's a good thing about these surplus stores. Is that. You know. Yeah. They sell these weird one off kind of things.

**Chris Gammell:** Right. Exactly.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. And so. You know. Like. I think a lot of their business too. Is about. Not just one offs. But like replacements. And stuff like that. So. You know. You kind of. See. See a wide range of stuff. You know. So you might see a switch on there. That's like. Oh. Why. Why is it like that? Oh. Okay. Well. That's for like a fridge or something. You know. That. That people. Yep. Might actually need. Exactly. But then there are also. You know. Transformers. There's transistors. Resistors. You know. There's a lot of great. A lot of good power resistors on here. Things like that. Just a lot of. It's just. It's like a. Online flea market almost. You know. Like. It's just.

**Dave Jones:** It's just a small category for high voltage capacitors.

**Chris Gammell:** Yeah. So. I. I. Encourage people to go check it out. If you go to the amp hour dot com slash ES. That'll actually take you there. And then. We also. Get credit for that. So we'll have that link in the show notes. But we really appreciate everybody supporting the show by. By going to check out their stuff. And. Yeah. Hope you enjoy it. There's some cool stuff on there. And definitely. You know. Poke around and see what you can find.

**Dave Jones:** I assume they only ship to like US. Their main markets are US. Right. They. Um. They probably aren't going to ship US a couple of. I think they'll ship it to you.

**Speaker ?:** You know.

**Dave Jones:** Five voltage caps to Australia. Well. They probably will. Yeah. They. They will. Postage is probably expensive for international stuff.

**Chris Gammell:** Right. Yeah. So. Especially if it's heavy. If it's a big heavy bit of surplus gear. You know. Yeah. Yeah.

**Dave Jones:** Postage costs ten times more than the unit does. That always sucks.

**Chris Gammell:** It does. Sometimes it's worth it though. Yeah. If you can find something really. You know. Kind of out there. And different. So. Like I said. People should poke around. See what they can find.

**Dave Jones:** Yep. Thank you very much. Electronicsurplus.com.

**Chris Gammell:** Yep.

**Dave Jones:** All right. Speaking of surplus gear. I scored. I think it's the first time ever on eBay. It'll be a tear down item. I got it for 99 cents. Really?

**Chris Gammell:** What'd you get?

**Dave Jones:** Yeah. Like. Like. Yeah. You. You.

**Dave Jones:** You always see these. You know. These eBay listings. You know. It starts out at 99 cents. But by the time everyone bids on it. You know.

**Chris Gammell:** A hundred bucks or whatever.

**Dave Jones:** But no. I actually got it. I was the only bidder. And I got it for 99 cents. I don't think that's ever happened to me.

**Chris Gammell:** So. So what is this wonderful piece of equipment you got?

**Dave Jones:** I'm not going to tell you. It'll be. It'll be. It'll be. Oh. It's a secret. You're going to tell me after the show though.

**Chris Gammell:** You better tell me. Hopefully today.

**Dave Jones:** Yeah. It's not that exciting. You know. It's a bit of old vintage 80s. Bit of. 80s development gear. Let's say. Okay.

**Chris Gammell:** Okay. Yep. I'm guessing. Actually. I don't know. In circuit emulator. That's what I'm guessing.

**Dave Jones:** All right. That's your guess. Boring. Yeah. Well that's the thing. Right. It. Like. Because I can't power it up. Well I could power it up. But it doesn't. It's not going to do anything. Right. Because I don't have. You know. The software for it comes on a. You know. Five and a quarter inch floppy. You know. And it's got a plug in DOS PC. A plug in ISA PC card. Oh God. Yeah. You know. I'd love to show you what's working.

**Chris Gammell:** For now we're just going to poke at all the parts. And see what's in there.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. That's. That's tough.

**Dave Jones:** And it's. You know. It's not going to be that exciting. Inside there's going to be a whole bunch of. You know. Dip. Parts I'm sure. You know. It'll just be. You know. Five or six boards of. Dip. Yeah. Because. That was the vintage. You know. Maybe it's got some SMD in there. But. Yeah. My. My guess would be. Dip. With all the doubles. The classic double sided. Dip. High density layouts. You remember all the boards.

**Chris Gammell:** Like all the right angles.

**Dave Jones:** From all the right angles. And this was when. Routing. You know. Auto routing. Actually worked. Because. You know. You would have. To make a system. Right. You didn't have one microcontroller. To do everything. You. You know. You. You had to build everything out of 7.4 series logic. Or whatever. Yeah. You know. If you're lucky. A couple of gate arrays. And. You know. Stuff like that. But you. You might have a hundred chips. And you. A hundred dip. You know. Dip chips. And you've got a line. And you put them all in line. Right. And so you put them in lines. And lines. And lines. All on your board like this. And then you go auto route.

**Speaker ?:** You know.

**Dave Jones:** And this was. It goes zooming.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And the auto routers. Because the speeds were so slow. We're only talking a couple of megahertz. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** And you might have a four layer board. Right. You know. You might have your ground plane in the middle. With your five volt rail. Or another 3.3 volt rubbish back then. Right. Right. It would be five volts.

**Dave Jones:** Yeah. And it would just route them. Because. You know. Because routing algorithms are quite efficient at doing those. Sort of. You know. Double sided. Layouts. You know. And so. So. You would specify the rules. Well. One layer all goes horizontal. And the other layer all goes vertical. Traces. So it would. You know. And. So it would give you. You know. 20 vias to get to the other side of the board. But it would get there. Right. And. Yeah.

**Chris Gammell:** And then you just start spouting RF energy all over the place. Oh yeah.

**Dave Jones:** Of course. Right. Oh God. It was only. You know. Yeah. Them edges. But you just didn't care back then. Right. Right. That's what they did. Because you had to make it work. There was no other way. Right. Yep. Yeah. How do you. Wow. How do you hand place and hand route and optimize a design with a hundred dip chips on it. Right. You don't. Right. Well. You can. You make the board bigger. Placement's also important.

**Chris Gammell:** Yeah.

**Dave Jones:** Well. Yeah. Exactly. But. You know. But you can't make the board infinitely big. And.

**Chris Gammell:** What about. One of those types of. There's like racks that were like that. Weren't there. Like. I forget the different.

**Dave Jones:** The Euro card. Well. The one U2. You kind of stuff. Yeah. And there's the big six. Six rack unit high. Yeah. Cards. And stuff like that. Yeah. So you would design things to fit on those big rack cards.

**Chris Gammell:** Wow.

**Dave Jones:** Yeah. And everything goes into a bus plane. You know. So that's how you design systems back then. And that's what's going to be inside this teardown.

**Chris Gammell:** Yeah.

**Dave Jones:** Is. You know. It's going to have a couple of boards slotting into a back plane. Because. You know. And each one will have like a hundred dip chips on it.

**Chris Gammell:** Wow.

**Dave Jones:** Yeah.

**Chris Gammell:** That's a.

**Dave Jones:** I'm sure. I don't even have to open it to know. That is nothing more than a leaded.

**Chris Gammell:** A leaded. Yeah. Finger poke waiting to happen. You know. Yeah. Oh man.

**Dave Jones:** But yeah. Those. Those were the days. And. Really? Yeah. You missed that? You don't miss that. Come on. Oh no. I don't. No. No. It's a pain in the ass.

**Chris Gammell:** Yeah.

**Dave Jones:** No. There's so much integration. Like these days. You know. You don't see all discrete TTL logic anymore. I don't want to. Everything's done in one big process. No. I don't want to either.

**Chris Gammell:** Give me that PGA any days. You know. Right.

**Dave Jones:** Yeah. Oh God. Oh boy.

**Chris Gammell:** There's actually. There's a link I put on the show. No. It's from. Actually a couple weeks ago now. I think some of this stuff is from before the new year. We kind of. We kind of missed a show. We took a little time off and stuff. But. There's this really cool post about. Reverse engineering in IC. And this guy. He basically etched off the top. And then he started kind of. He basically started. Moving down through the metal layers. And then he reverse engineered everything. And he actually drew out this. I'm always impressed by that.

**Dave Jones:** That is. Me too. Rocket science. Yeah. Oh yeah. That's a lot of tedious work.

**Chris Gammell:** Yeah. Exactly. And I remember like back in the day. I was trying to. You know. I did a lot of analog circuits in school. But we. I only had like one or two classes. In the actual analog IC design stuff. And. Oh man. I remember my teacher like. Had us like filling in graph paper. With like colored pencils. To try and like. You know. Like. Do like IC layout. Oh God. Yeah. Right. And like looking at this. I had these horrible memories flashing back to me. Oh. Just. You know. Since then I've worked in the chip industry. Oh boy. And. Yeah. And it is cool. You know. Like learning process stuff. I really highly encourage people to learn it. But when you start with graph paper. And colored pencils. Like. Yeah. Exactly. You know. That's like. That's like saying. That's like trying to teach someone programming. And this is how a lot of people teach programming. You know. It's like. Okay. We're going to start. With abstraction. You know. It's like. Like the worst. The worst possible. Place to start. Instead of. What. What the hell is memory? What is a bit? You know. Like. What is a bite?

**Dave Jones:** And then we're going to enter it all with dip switches on the front panel. And we're going to load the data bits into each address.

**Chris Gammell:** Yeah.

**Dave Jones:** Flip. Flip. Flip. Yeah. Altair like. And. Yeah. Well hey. You know. PCB layout. I used to use tape. I can remember. As a kid. Yeah. You would lay it out. With your light box. You would have a light box. And you'd have the tape. And you'd lay it out. And. Yeah. You would actually have it. You know. A roll of. A roll of tape. And you'd run it out by hand. So you could get all the smooth bends. And. You know. Stuff like that. And you had your exacto knife. And you'd cut the tape. And. You know. If you were. You know. You had often the. Pre. Printed. Stick down. IC pads. You know. So you go. I need a dip 16. So you'd go to your sheet of dip 16. You know. Dip 16 footprints. And you'd place it down. And then you'd roll. Your. Your roll of. Tape. From each. Each pad. Out. And you know. And if you had to. That's why. Rip up. And retry. Auto routing. Right. That's where the name comes from. Rip up. And retry. Because you would rip up the tape. In the old days. You would rip it up. And you'd go. Oh. I can kind of sort of reuse that. But it's just. Yeah. Thrilled in the beat. You know. Yeah. Exactly. And.

**Chris Gammell:** That makes me sick to my stomach. Thinking about doing that. That just sounds. I know. It's terrible.

**Dave Jones:** It's pretty painful. I don't. I'd never go back to that.

**Chris Gammell:** Oh. I know. And you know. But it's interesting to think about that. Right. You know. We. We. We talked earlier on the show today about. About. You know. Like learning. And you know. Banging your head against the wall when you're learning stuff. And we talked last time about. About learning as well. Um. About. What were we talking about last time? It was. No.

**Dave Jones:** I don't know. I can't remember what I had for breakfast. Yeah.

**Chris Gammell:** But someone. Someone submitted a link on the. On the show notes. Um. But basically. Uh. The Jope. Sended this. Sent this in. But basically. You know. The point is. There. There is no fast way around it. I think that's probably what we were talking about last time. There's no fast way to learn electronics. And there's actually this really great. This post by. Peter Norvig. Saying the same thing about programming. You know. There's all these like. Yep. Yep. Learn it in 21 days. And all these fast. Yeah. Right. You know. Fast ways to learn things. It's like you're really not learning it. He's saying. No. You should learn it in 10 years. You know. Like. Yeah. But I. I really did like the thing. The. The point that. That Peter Norvig makes in here. The thing. The. The. The number one way to figure out. Or to actually succeed in it. Is to get some friends. And then do it all together. Because then you keep encouraging each other. I mean. That helps now with the internet and stuff. Right. Yeah. But yeah. If you have people to. You know. Make it fun with. Then of course you're going to learn it. You know.

**Dave Jones:** Yeah.

**Chris Gammell:** So. It's. Yep.

**Dave Jones:** Ah. Takes a long time.

**Chris Gammell:** I will not be learning how to. How to. Reverse engineer. An IC. But I highly recommend other people do that. Right. It's. It's. It's. Or at least go look at this. This is. It's a cool. It's a cool. All right. Cool bunch of pictures. With all the hydrofluoric acid. Cutting down.

**Dave Jones:** Hey. Patent trolls.

**Chris Gammell:** Oh. Really. Yeah. I know. Yeah.

**Dave Jones:** They're suing a podcaster. Yeah. Next.

**Chris Gammell:** Oh. Yeah. Yeah.

**Dave Jones:** Yeah. They can come and sue us. Because we're on iTunes. Yeah. They could.

**Chris Gammell:** They won't. But they could. They could. Speaking of patent trolls. Thank you. There was a. There was an article talking about. What are they called? Shoot. Nathan Meervold's company. But basically. They're like a bunch of. They have. Oh. Here. Intellectual Ventures. You know. Nathan Meervold. Oh.

**Dave Jones:** That name just. That name just. Turns you off. Right at the start.

**Dave Jones:** Exactly. Intellectual Ventures. Inc. Yeah. So there was an article. About this.

**Chris Gammell:** Since we're talking about patents. They have like a thousand. Shell companies. In order to. Actually go after people. For patents. Or patents. As you say. Yep. Good lord.

**Dave Jones:** Right. So they threaten them. And if they sue back. Well they just shut down. The shelf company. Exactly. And no harm done. Yeah. Exactly.

**Chris Gammell:** Yep.

**Dave Jones:** And if they do it a thousand times. You'll get one or two people. That buy it. And pay up. Right. And it makes a worthwhile. Business. Unfortunately.

**Chris Gammell:** Bastards. You know. Someone. Someone mentioned in response to this. When you tweeted this link to me today. About this. Podcaster patenting thing. Something about like. Requiring a. A. Prototype. And like. A working model. Or something like that. Yeah. Was that used to be a thing? Yeah.

**Dave Jones:** I think. I don't know if it used. Yes. It used to be. I think. Back in the old days. Yes. They would reject your application. Unless you had a. Like. I'm talking the days of Einstein. Right. Yeah. Working at the patent office. I think. Yeah. Unless you had a. An invention. Um. They wouldn't. Uh. You know. A physical thing. They wouldn't actually patent that. But then. Yeah. All hell broke loose in the 70s. Or something. I think. And. Yep. Just went down the toilet. Yeah.

**Chris Gammell:** I'm sure it's tough with software. But.

**Dave Jones:** Oh. That reminds me of the young Einstein. Have you seen the movie. Young Einstein. No. I don't think I have. Oh. Dude. It is an Australian classic. It's an Australian movie. Australian really? About. Does he have an Australian accent? Yeah. Absolutely. It's an Australian. And. And. He. It's about. You know. Einstein. And how he invented. Well. Einstein. And how he invented rock and roll. And also. You know. It's a. It's a comedy. Oh. Okay. It's very cool. And I remember. You know. There's this scene. Where he goes into the patent office. And he. He. Tries to. Patent. EMC. Which is. E equals MC squared. Right. He actually came up with this formula. For. Formula for putting the bubbles in beer. Right. You will love this. Right. Oh yeah. Einstein invents the formula for putting bubbles in beer. And it's EMC. As he called it. E equals MC. And he walked into the patent office. And. I want to patent this. And. You can't patent a formula son. And anyway. It's hilarious. I'll have to get some YouTube clips.

**Dave Jones:** Yeah. Post them in. Or something. But young Einstein. Young Einstein. You'll love it.

**Chris Gammell:** Not to be confused with young Frankenstein. Right. No.

**Dave Jones:** Young Einstein. By. Yahoo Serious. Is the actor's name. That's his real name. Yahoo Serious.

**Chris Gammell:** Yahoo. Serious.

**Dave Jones:** Yahoo. As in Yahoo. The internet company. Yahoo. His real name is Yahoo Serious. Well. His real name is. I don't know. Greg Platt or something. But no. He changed his name formally. Right. No. He changed his name. You know. To Yahoo Serious. I'm sure it's on his. You know. Driver's license.

**Dave Jones:** Passport. Weird. And he made a few movies. Back in the 80s. And he was. Yeah. Famous for making these comedy. Movies. And anyway. Sorry. That just reminded me of that. I just wasted five minutes there.

**Chris Gammell:** That's okay man. I'm. I'm counting. I'm counting on the minutes right now. I'm. I'm counting on the minutes till the show's over. You know what.

**Dave Jones:** I thought you'd love it. Because it had beer. You know.

**Chris Gammell:** Oh yeah. Yes. I do love beer. Thank you Dave. Thank you for reminding everyone that I. I do love beer. I'm the only one too. It's weird. It's an. It's an addiction. Freak. You know. I really. Really. Enjoy having a beer. Because I don't pour it on the drain.

**Dave Jones:** Next. Come on. We've got like. You know. Less than. Oh like 10 minutes left or something. I know.

**Chris Gammell:** I'm counting on the minutes. If you go over. You know why. Yeah. Well. Why. Because my mill showed up.

**Dave Jones:** Oh yes. Yeah. Right. And it's sitting there in front of you. Just teasing you in the box. It is. It's like. Oh.

**Chris Gammell:** Stop talking to that Aussie. Just. Come over. Put this together. Yeah. Oh. I'm very excited. It's good. That's a stupid thing too. You know. It's like. It's like. I got it now. But it's going to be probably. You know. Another month before anything happens. You know. It's like any. It's like any electronics project.

**Dave Jones:** Does it. Yeah. Does it come fully assembled. Or do you. Does it come in bits. And you've got to. Do the IKEA thing.

**Speaker ?:** It's not like.

**Chris Gammell:** It's like. It's like. It's like two big pieces. And a bunch of littler pieces. But then I have to bolt. Like stepper motors onto it and stuff.

**Dave Jones:** Is this a. A Chinglish one. Is this a Chinese. No.

**Chris Gammell:** This is built in the USA. This is built in Arizona. Oh.

**Dave Jones:** Hey.

**Chris Gammell:** Yeah.

**Dave Jones:** For Uncle Sam himself.

**Chris Gammell:** Exactly. Wow. I think the controller. I'm not sure who makes Gecko. The controller is a Gecko. But. And that might be overseas. But the. The person who did all the integration and stuff. That was in Missouri. Missouri. If you're from this. If you're from there. Oh. Really. Yeah. It's Missouri. Yeah. Instead of Missouri. And. Wow. And. My friend's from St. Louis. But yeah. Yeah. Stateside. Yeah. Supporting. I guess it's local. I don't know. But yeah. It's exciting. You know. The other thing that's exciting about. To me about it though. Is. It's. It's. It's kind of like a 4A in a robotics. I know it's not really. But. You know. I've never really moved. I've never really moved anything with electronics before. You know. I've always done. Oh. Measuring stuff. And you know. Controlling. Yep. Controlling. You know. Yeah. Dac values and stuff like that. Outputs. Inputs. Yep. Communicating. That kind of thing. And so this is kind of the. I obviously didn't design the electronics. But.

**Dave Jones:** So you're going to like. Have a little cry. When the motor suddenly. Start. When you push a button. And the motor suddenly starts to move. You'll probably.

**Chris Gammell:** Oh yeah. I already did it on video. I'll post that video. I think that's so wonderful. Oh okay.

**Dave Jones:** Right. You haven't watched it yet. Oh yeah.

**Chris Gammell:** Yep. It's a good feeling. I didn't really do much. I mean that's the thing. Like. This is kind of my first. Like. Prosumer experience. I've never really spent. Like. This is not normal for me. I don't spend money like this usually. You know. I've never bought like three. I was going to say.

**Dave Jones:** How did you get this approved by. She must be obeyed.

**Chris Gammell:** Oh. Well. I'm going to be. Using it for various things around the house. Of course. Like. Yeah. I'll figure it out. It's okay. Your secret's safe with me. Yeah.

**Dave Jones:** And all our listeners.

**Chris Gammell:** 6,500 others. Yeah. But. You know. It'll be good.

**Dave Jones:** But. Yeah. It's cool.

**Chris Gammell:** Use it to cut circuit boards too. Everything else.

**Dave Jones:** Right. Yeah. But. I wish I had a separate area that I could. Do stuff like that in. I don't really. You have an office Dave. Yeah. I know. It's not really suited to. You know. Laves and mills and. PCB cutters and. Yeah. Etch tanks and all that sort of. You know. I guess so. It's not really suited to that.

**Chris Gammell:** I mean. You've got an air conditioner right. It's pulling air through somewhere. Does it event externally. That's all you need.

**Dave Jones:** Yeah. I'm sure it does. Well. I don't know. Maybe just recirculate.

**Chris Gammell:** Just bring in a smoke bomb. You'll figure it out real fast. Yeah. Right. Yeah. Like a lot of things. Like. I've used. I've used a PCB cutter before. That has like. A built in vacuum. Then it just goes through a filter. Right. And so it just. Yeah. Yeah. It pulls the. It pulls the dust off. And then it just pulls it through a. A vacuum. Yep. Hits the filter. And the air comes back out in the. Atmosphere. Same for a. A. What's it called? A. Still.

**Dave Jones:** I would much rather have a. You know. I'd much rather have like a. A workshop. You know. A mechanical workshop. Yeah. Like a vent of hood and stuff. Where I can do chemicals and stuff. And I can. You know. And I can open the roller door. And just let natural air flow through. And you know. All that sort of jazz.

**Chris Gammell:** Start pouring acid on the ground. And just. Yeah. Exactly. You know. Hitting birds with. Hitting birds with. Concrete. Ah who cares. You know.

**Dave Jones:** Yep.

**Chris Gammell:** Yep. Yep. Yeah. I'm jealous. You know. Like any project. It's. You know. There's startup time. And. It's tough. Right. I mean. Like even. Even when you get. You know. Dev boards back. Or you know. Like you. You know. When your power supply comes back. Right. Even though you've designed it. There's bound to be something that goes wrong. And. Oh. Of course. And getting to that. That LED turning on. Is. Is a big deal. You know. That's.

**Dave Jones:** It can be a pain in the ass sometimes. Yeah. It can take you a week. Just to. You know. Finally get the bloody LCD going.

**Chris Gammell:** Right. Exactly. So. Yeah. I'll get there eventually. And I'll videotape everything. That's. Cool. Hopefully people will learn. Something from my mistakes. Awesome. Yeah. Speaking of. Learning from others. There's a. There's a really big list. Of homebrew. RF circuit designs. That I wanted to point out. It's not like a new list. It's pretty old actually. But in terms of just like. Raw schematics. Available. Kind of awesome. And like. Like. Throughout the spectrum. I mean. 80 meters. 40 meters. 7 megahertz. You know. Like. I'm so out of practice. My amateur license. Those.

**Dave Jones:** Those. Those meters mean nothing to me. I know. I know. I don't know what the 40 meter band is. You know. Like.

**Chris Gammell:** 432 megahertz. Yeah. Exactly. I've. I've already lost all that stuff. So. But. If you're into that kind of thing. And plus. Just looking at these things is fun. You know. Like. Just looking at the actual schematics.

**Dave Jones:** I'm sure if people are that into it. They probably already know about it.

**Chris Gammell:** You're right. We probably shouldn't mention any links. On the rest of the amp hour ever again. Huh Dave. Right.

**Dave Jones:** Because.

**Chris Gammell:** The amp hour. If you're into it. You already know about it.

**Dave Jones:** Exactly. This show is pointless.

**Chris Gammell:** The amp hour. If you have to ask. You'll never know.

**Dave Jones:** Do we have a slogan? We don't have a slogan.

**Chris Gammell:** Ah. Dave and Chris yapping each other every week. Every other week. And then guests come on.

**Dave Jones:** You can come up with a real witty. Cool. Funny. That's not bad. I like that. Pointy and slogan.

**Chris Gammell:** I like that.

**Dave Jones:** People have been adding to the. Should we have a slogan contest?

**Chris Gammell:** Slogan contest. Well we need to put some. Some. Stuff where our mouth is. Some coin up as a. Yeah. I don't know about coin.

**Dave Jones:** Yeah. Now screw that. Yeah.

**Chris Gammell:** I could probably. Don't have any money to be human. But it might take a couple years. Right. I just send them a. You know. A block. And. Oh I cut that. Sure.

**Dave Jones:** Oh I could send them a microcurrent or something.

**Chris Gammell:** There you go. All right. There you go. We'll figure something else out. We'll. We'll come up with an amp hour party pack. I like this. I like this idea. Party pack. We should. We should come up with more things. You know. Off the cuff.

**Dave Jones:** A 10 pack of resistors. Score.

**Chris Gammell:** Exactly. Yeah. Just what I needed. 3.32 kiloohms. Awesome. Thanks Chris and Dave. This is great. And what a convenient size. 5 watt carbon film. Awesome. It'll fit in all my new projects. Okay. So. How are we going to do this? We're going to do a slogan contest. Should we just do it in the comment section? Or should we do an email?

**Dave Jones:** Oh bloody hell. I don't know. I haven't thought that far ahead.

**Chris Gammell:** How about we'll do slogan at the amp hour dot com. You send an email to that. We'll have it. Because that way it can be a blind test. And then we can have people vote on it later.

**Dave Jones:** Well then we're going to do work where we actually have to set up an email redirection.

**Chris Gammell:** Oh that's easy. Come on. That's fine. Slogan at the amp hour dot com. I will make sure that that's in the show notes.

**Dave Jones:** But then nobody gets to see it. No no no.

**Chris Gammell:** We'll put it up as a contest later once we know. You know. Because if. So what if Mr. Jeff Kaiser put up something right? Then you know it's from Jeff. And everyone's like. Oh Jeff's so great. Right. And then. Yeah right. You know. Like. There is. There's that bias. Right. So it should be. It should be blind. So. Right. Jeff is great. Come on. Jeff's great. We tried to get him on the show tonight. But he's busy or something.

**Dave Jones:** Well he must be. He's working at Valve. Yeah. Yeah. I think they will be in order to keep their mouths shut. Oh yeah.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Alright. Anything else for this week? The boys have stepped in. No. That's it. We just came up with the contest at the last minute there. I like that.

**Chris Gammell:** I like that too. You know. If you've got. If people have questions. It doesn't have to be limited. Just to. Q&A shows like last week. You can always send us an email. At the Amphour at gmail.com. And we definitely want questions for next week. When we are going to have. For the very first time. A CEO of a company. On the Amphour. Oh. Yeah. We could really. A CEO of a two person company. No. We're going to have to behave. So next week. The VP. The VP of engineering. And the CEO. Of Touchstone Semiconductor. Will be on the Amphour.

**Speaker ?:** Yep.

**Chris Gammell:** As long as our setup.

**Dave Jones:** So if you want to know anything about. Yeah. Starting up a semiconductor company.

**Chris Gammell:** Yeah. So they started up. What. It was like. Two. Three years ago now. But they were. They were a fabulous semiconductor. That do analog. So. If you got any questions about that. We'll have a. I'll put a post up on it. Later in the week. So you can ask questions. Directly on the site. And you can ask. On the. I'll put it up on Reddit as well. So you can. Awesome. Post questions. Either one. And please. Please do. Because. Otherwise. Me and Dave. Will start coming up with contests. And you know. We'll start giving away. Touchstone gear. Without them authorizing it. And I think. Yeah. Right. I don't know if CEOs. Go for that kind of thing. But it's really cool. I'm excited about it. So. Yeah. So next week.

**Dave Jones:** Oh. We'll just put them on the spot. Why don't we? Because CEOs love being put on the spot. They do. Yeah. So tell us about all your quarterly earnings. I'm surprised they haven't. Yeah. I'm surprised they haven't. Carefully vetted. You know. Usually. If we went to. You know. If we wanted to get the CEO of. You know. Intel or something on here. You know. It would have to pass through. Five lawyers first. And. You know. Yes. They've been very generous so far.

**Chris Gammell:** So. We'll see. We'll see.

**Dave Jones:** And then they would want all our questions vetted beforehand. And guarantee in writing that we wouldn't ask. About. You know. About their latest scandal or whatever. Yeah. So next week.

**Chris Gammell:** Touchstone Semiconductor. Yeah. In the meantime though. You can find us on Twitter. And email. And everything else.

**Dave Jones:** Yeah.

**Chris Gammell:** All right man.

**Dave Jones:** And if you've got any ideas for other CEOs you'd like to see on this prestigious. Here on this prestigious radio show. Yes. Then let us know. And we'll get them with our infinite power industry.

**Chris Gammell:** Clout. Clout I believe. Clout. Yes.

**Dave Jones:** That's the word I was looking for.

**Chris Gammell:** Yes.

**Dave Jones:** Yep.

**Chris Gammell:** All right. I'm sure we can get them.

**Dave Jones:** You name it. We can get them.

**Chris Gammell:** Yep.

**Dave Jones:** That should be our slogan. You name them. We get them.

**Chris Gammell:** Well we'll see if that's our slogan. Now we know who came up with that one.

**Dave Jones:** The Amp Hour. We will not be beaten on banter. No.

**Chris Gammell:** Or length of shows. We'll see you next week. Bye. This episode of The Amp Hour was sponsored by Electronicsurplus.com. Electronic Surplus not only has hard to find components to put into your next designs. They also buy old components. So whether you need to liquidate your inventory or need to restock those hard to find components, go to theamphour.com slash ES. administered administered administered administered administered administered administered administered

**Speaker ?:** administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered administered Outro Music
