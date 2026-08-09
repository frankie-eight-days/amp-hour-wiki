---
episode: 591
title: Olive-a The World
url: https://theamphour.com/591-olive-a-the-world/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released May 30th, 2022. Episode 591. All over the world.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. What's up, nerd? Not much, man. I was watching your reverse calculation from Twitter. You looked at a part and a picture of a part, and then you went through and reverse calculated it. I enjoyed that.

**Dave Jones:** Oh, excellent. Oh, you watched the whole thing? Excellent. Yeah, it was only half an hour long. It was like somebody asked me a question on Twitter, for those who aren't aware, which happens a lot. I get a lot of questions on Twitter, which is good. And often, yeah, I'll just try. If I can, I'll just fire off an answer. But I thought, eh, this might make an interesting video because I had to do work to try and answer the question. So I thought, oh, I might as well press the record button.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? Yeah.

**Chris Gammell:** No, it was really good. It was really straight ahead analysis. I thought that was great, picking out the pin types and the shapes of different things. I won't spoil it for people.

**Dave Jones:** No, but I did guess wrong in the start of the video because for those who, because this is radio, someone posted a photo of a PCB, which had a little SOC 23.5 part on it and a couple of caps and inductors around it and stuff like that. And I guessed, well, it's easy to figure out that it's a voltage regulator, but which type is it? Is it a switch in or linear? And of course, it's a switching because there's an inductor right next to it. That's a dead giveaway. Yep. And then to figure out the pin out, I actually got the pin out wrong. So, yep. Because the- But you didn't have other stuff there, right? I didn't have all the information. And I did later on in the video. So I actually asked him on Twitter and he sent a bigger photo. So then, aha, yep. I guessed wrong. It was simply a guess. And well, I had a 50% chance. Yeah, take a shot. Yep. So anyway-

**Chris Gammell:** It's interesting as I look at circuits now, just kind of being able to- So I just pick up a random dev board on my bench. I mean, obviously, I know about this dev board. But kind of just seeing design patterns and seeing kind of how stuff is laid out and general shapes of things, it's definitely not intuitive at first. But as you have more experience, get older in the industry, it starts to make more sense. It becomes obvious.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** And most board designers, you know, any capable board designer is going to do a modular layout. So if you've got a switch-in regulator or a voltage regulator, it's going to be in the one, you know, all the components are going to be grouped together. So you'll find the inductors and the capacitors. And they have to be for like EMC and other performance reasons, right? You can't have your filter. You can't have your switch-in inductor on like the opposite side of the board to your switch-in regulator. It's not, you know, it's really going to be bad.

**Chris Gammell:** Yeah.

**Dave Jones:** But I guess if you're a beginning layout person, you might not know that. But yeah, it's just like you'll never see that on any sort of professional level board. So they're all grouped together. So you're able to just look, you're able to just glance at the board and go, yep, that's a switch-in regulator part of the circuit. Yep, that's like an op-amp-y kind of, you know, circuit and stuff like that. You're just able to tell by the grouping of components.

**Chris Gammell:** Yeah, and I find that like even things that I probably would have looked at 10 years ago and have been like, I don't know what I'm looking at right now, but like tag connect connectors, I feel like that's like one that's been more prominent now. And it's like, oh yeah, it's like, they look very confusing at first, but now it's like, oh yeah, I know what plug in there. I can figure that out. Just like stuff like that. I don't know. I get less and less scared of electronics each time I look at them. Right. It's a move in the right direction.

**Speaker ?:** Yeah.

**Dave Jones:** And that's what the video was for. I mean, obviously anyone with any decent amount of electronics, any hobbyist is going to know all this stuff, but you know, but getting to that point is that's who the video is for, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** So, yeah.

**Chris Gammell:** Yeah, totally. I think having as a skillset too of like, you're not going to always have the schematic, you know, like hopefully you don't. No, that's right. That's a best case scenario, but when you don't, then what? I think that's an important tool in the toolbox to be able to reverse engineer that sort of stuff. Yep.

**Dave Jones:** What would be more important though is if the manufacturers actually put the part number on the chip. SMD parts. Is there anything more frustrating? I don't know. Is there anything more frustrating than SMD component marking? I mean, anything that requires some database on some obscure website somewhere to even have a remote chance of figuring out what that freaking chip is. You know, it's just, oh God.

**Chris Gammell:** Well, and I feel like the ones that are like properly motivated, like the ones who are going to like go and actually rip stuff off, like they're going to figure it out. Like they're going to decap the chip and look at the die shots.

**Dave Jones:** If they really want to know what it is,

**Chris Gammell:** it's going to be. So why not just make it easy for everyone? I know. Just make it easy. I feel like this culture of like, oh, well, our secret sauce is super important. It's like, it's a switching regulator.

**Dave Jones:** It costs 10 cents. If any of our audience, like work at a chip manufacturer and know the history of why they continue to put obscure markings, like the one that I've had in my video, where is it? It's like it's A, like it's capital A, lowercase a, 1B3 or something, you know, weird like that, right? It's like five random letters of upper and lowercase. That absolutely tells you nothing. And the only, and of course, none of that is related to the part number. So all your parametric search engines on all your favorite sites or Google or anything, even the manufacturer's own parametric search on their own website will not let you search. Well, as far as I'm aware, is there? Is there any manufacturer that has, that allows you to put in the SMD partner, but then you'd have to know who the manufacturer is, right? Because there's no label.

**Chris Gammell:** They're too small to put the logo on. They're too small to put the label. At least like SOIC8, you can maybe pull off like a new tech logo.

**Dave Jones:** You can have two layers of, yeah, yeah. But I can understand SOT23s. I can understand where it originally comes from because SOT23s are ancient, right? We're going back to like 1980, kind of. So were they around in the late 70s? Oh, geez. Definitely around in the early 80s. Anyway, right? A long time ago.

**Chris Gammell:** 70s, it would have been like hot new technology. Right, yes, of course. Check this out.

**Dave Jones:** Yeah. Actually, yeah, I think they were. Anyway, at least 40 years old, right? Possibly even 45 year old package tech. I can understand back then is that, you know, trying to mark the chips, right? A little SOT23, the actual, you know, laser marking and stuff like that wasn't really a thing back then. So it'd be a silkscreen, you know, or however, you know, process they did it back then. And of course, you know, look, you could only put two letters on there or something, you know, because they couldn't make them that small if it wasn't laser etched and stuff like that.

**Chris Gammell:** Oh, because the fidelity of the SOT23.

**Dave Jones:** So, you know, and basically you SOT23 packages back then. There was none of this five pin or six pin rubbish that you get these days, right? It was a three pin or bust, right? So, you know, it'd only be a single transistor. It'd be a single diode or it'd be a dual diode and that's it. And typically they might have like a two letter code for, you know, is it a dual diode or, you know, something like that. And there were kind of sort of some standards for that. I think there still are or some manufacturers, you know, a lot of them follow the same code. Like if it's a dual diode or something, it'll have like, you know, BF or something on it. I don't know. Just pulling that out of my bum. But, you know, it'd be sort of standardized. So you will find this kind of stuff in a database, in an SMD code database. But yeah, now that they've got laser marking and everything, and you can put at least five letters on there, the one that we're talking about in this particular video, it had five characters on it, right? I mean, five characters is enough to put the part number, like not the full part number with the alphanumeric prefix, but it's certainly enough to put, you know, it's like 65, 420 or something, you know, like.

**Chris Gammell:** It's like halfway to a URL at that point, you know, you could really.

**Dave Jones:** I know. It's like, yeah, come on.

**Speaker ?:** Yeah.

**Chris Gammell:** Using like Unicode.

**Dave Jones:** So does anyone have any, yeah. Does anyone have any idea why? Why this is, you know, and it's never like, I don't expect parametric searches and of the, all the manufacturers or of all the suppliers and stuff like that to include SMD codes. I don't think that's ever going to happen. If it would have, it would have, if it was going to happen, it would have happened by now. So it's, yeah. I think we're just, yeah. Forever screwed to these weird ass bloody, there's got to be a reason for it, right? It's like internally. Okay. So you don't want the same number as some other manufacturer. You want, you know, your own unique thing, but it's not worth it. And like, you can't put your logo on there anyway. So like, and anyone else can copy it, like can copy your code as well. It's not like it's, you know, it's not like it's trademarked or anything. I mean, it's just, anyway, SMD codes.

**Chris Gammell:** You're going to have to, I don't know, with lasers at a certain point too, you could start to mark smaller and smaller stuff.

**Dave Jones:** You can make smaller and smaller stuff. Mark O4 or two resistors if you want it. Yeah, you can put two left. Actually, I have seen some SOT 23 packages with two layers of info, I think. I can't recall where, but I think I may have seen it. And it's, yeah, it's absolutely tight. Yeah.

**Chris Gammell:** That, jeez, I don't know. At least give us like an upcharge option for stuff, you know.

**Dave Jones:** Anyway, so the outcome of that video where I was trying to identify this part for this person who asked on Twitter, I found the pinout. Of course, you can work out the pinout. And then I found a couple of two or three chips that matched that pinout, but they're obviously not, well, they're definitely, we know they're not that particular brand and part number because usually, not always, as I showed in the video, there is a marking table, which the manufacturer, if you're lucky, in the data sheet, they'll put a marking table. They should. Any good manufacturer should. So they actually tell you what the SMD code is. But the only way to find that, maybe it might be searchable in Google. Maybe once or twice over the decades, I've like found the SMD code because it was like, it was in the PDF data sheet and Google has like indexed the PDF data sheet and that code happened to show up and, you know, but it's pretty rare that happens. So, yeah. But there was one data sheet from MaxLinear. MaxLinear. Yeah, I saw that one. Yeah, apparently they were bought by XR, apparently. And then XR, I don't know, XR. XR is really old school. That's before you were born.

**Chris Gammell:** Yeah, okay.

**Dave Jones:** XR, yep. Really old school, you know, 1970s chips come from XR. Lots of old school, he near jobbies, you know, and like analog to digital converters and stuff, you know, from XR. So anyway, yeah, that was, yeah. And that MaxLinear one did not have the SMD code in it. So I couldn't even check if it was the right code. It's like, oh, geez, thanks a lot. So, yeah, it's a struggle. So anyway.

**Chris Gammell:** I have a chip of the week, speaking of chips.

**Dave Jones:** Chip of the week, chip of the week. Yep, go for it.

**Chris Gammell:** Send me a link. This is actually on a off the shelf board that I'm using, but I hadn't actually seen, I'm just literally pulling data off this thing. So I'm not even like designing or anything like that. The SM351LT Honeywell sensing product. Basically, it's a, I think it's like a digital magnetic switch, you know, SOT23. Sorry, Dave.

**Dave Jones:** It's a three pin SOT23. Yep, old school. Yeah, that's right. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, a little position sensor. Is it a magnetic Hall effect thingy?

**Chris Gammell:** Yeah, it's like Hall effect, but it has, I think, a one wire or equivalent. Oh, no, I guess it is.

**Dave Jones:** It's a magneto resistive sensor.

**Chris Gammell:** Yeah. Yeah. Yeah. So it's like a silicon, silicon, what's it called? Hall effect.

**Dave Jones:** A silicon read switch, basically. Well, no, it's a digital read switch, right? Maybe a digital read switch.

**Chris Gammell:** Yeah, it's digital. Yeah, I guess it's got a push pull output. So yeah. Yeah, I guess it is a digital output. But yeah. Yeah. Pretty cool. Yep. Pretty neat little part. Doing a little, one of these off-the-shelf boards that I'm using, like an enclosed sensor board. It's got a, basically, you can move a magnet up to it, like a lot of those sensors for windows, you know, like an open-close. So like a traditional main switch.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Low power.

**Dave Jones:** Oh, yeah. Yeah, 360 nanoamps. Thank you very much for playing.

**Chris Gammell:** Yeah.

**Dave Jones:** Jesus. Yeah. You know? And it works down to 1.65 volts, too. Oh, yeah.

**Chris Gammell:** Yep.

**Dave Jones:** That's pretty schmick. Yep. That's definitely. Pretty cool, right? Yeah. Yeah.

**Chris Gammell:** Yeah. So definitely. Yeah, I mean, like hall effects are great. You know, people know them from a lot of, like, if you're doing encoders and stuff like that, they're great for that sort of thing. But this is more like, I'm just sitting there and I want to know when the magnet's close to me. And so a lot of, like, proximity detection and stuff like that. That's cool.

**Dave Jones:** Can you buy it?

**Chris Gammell:** You know, I didn't have to worry about that one. Right. Okay.

**Dave Jones:** It's just a cool tip. All right. Yeah. I totally agree. I love the data sheet. I'm looking at it. And it's actually got a photo of a ruler with the SOT23 package next to the ruler as if anyone doesn't know what a SOT23 package is. Like, oh, yeah. This weird ass SOT23. What is this? How big is it? I don't know. Is it an inch? Or is it? Come on. Come on. That's funny. Yeah. I don't know.

**Chris Gammell:** How does this even work, though? I guess it's like a... It must be like the magnetic field impact. It's showing like a...

**Dave Jones:** Magnetoresistive thing. I don't know. Is it some nanotech? I don't know how...

**Chris Gammell:** It's like maybe a small MEMS sensor or something.

**Dave Jones:** I would assume it's sort of MEMS-y, nano MEMS-y kind of. Yeah.

**Chris Gammell:** That's what's kind of crazy about it. Like, we don't really need to know.

**Dave Jones:** Oh, yeah. It's an internal block diagram. Yeah. Yeah. There you go. Yes, it is a push-pull output. It's got a flip-floppy. And it's got a threshold comparator. And yeah, the AMR, what's the... That's the sensor thing. It's like a bridge thing.

**Chris Gammell:** That's the magic. That's the magic.

**Dave Jones:** That's the magic secret sauce, right? Yeah. So, yeah.

**Chris Gammell:** Yeah, I imagine there was one thing here, so... Yep.

**Dave Jones:** And there's a clock counter decoder.

**Chris Gammell:** It's different than ASMR, of course. You know, like...

**Dave Jones:** The magnet is close. Hang on. You said at the start this was I2C. This is not I2C. This is just a... It's not I2C. No, it's digital, like you said. It's just a digital output. Yep. Yeah. Nice. Just does its job. I like simplicity. I like simplicity. There's a segue there, Chris. I'm going to see if you can... You can get it to something on the Reddit list.

**Chris Gammell:** Okay. Let me see. I can do this. Simplicity, simplicity, simplicity. You can do it.

**Dave Jones:** You can do it. You can do it, Chris.

**Chris Gammell:** Please make a dumb car.

**Dave Jones:** Yes. Yay. You got it.

**Chris Gammell:** This is a TechCrunch article. Op-ed. Oh, TechCrunch is down for me. Oh, no. It's up for me. But basically, it was a... Oh, yeah. No. There it goes. It's an op-ed basically saying... You know, this is actually a very similar argument to the tablet in a car thing. Do you remember that argument from way back in early Amp Hour days? I said, instead of giving me a smart console, let me slot in a tablet. Oh, slot in a tablet. Yeah, yeah.

**Dave Jones:** Right.

**Chris Gammell:** And then switch it out every two years so it's not pokey as hell. I don't know how... How is your Ionic? How is the infotainment system on your Ionic?

**Dave Jones:** It's meh. It's my official verdict. Meh. Yeah. It's like... It kind of does the job, but the mapping in it absolutely sucks ass. I'd much rather use Google Maps. And I think I can using Android Auto and stuff like that. But then you've got to plug it. Oh, yeah.

**Chris Gammell:** So I love Android Auto, the Apple Car Kit. Those are like... That is my jam. I haven't tried it, actually.

**Dave Jones:** I should actually try it. But my phone's got a dicky bloody USB cable, so it wouldn't freaking work anyway.

**Chris Gammell:** It does it over Bluetooth now, though. Oh, really? So the newest cars... Oh, right. Yeah, because I was like... I thought it was always the cables. And then I got into a rental... You know, these are like... The only time I see it is rental cars. My cars are always very old. And I got in a rental car, and I was hooked up to the Bluetooth, and it's like, hey, you want to fire up Android Auto? I was like, oh, oh, yeah. And so it's actually cranking a decent amount of data over there. Right. So then in that case, the little console computer is basically just a bigger screen for my phone. And Android Auto is great, and it updates, and the Apple Car Kit's great. It updates. You know, it gets all the daily updates. And that's what you really need. You know, like all these cars...

**Dave Jones:** Yeah, you want it to be almost decoupled. That's, as you said, you want the tablet in there, so it's decoupled from the car, basically. Yeah. And if, you know, if it gets... You know, if it fails, or you want to get faster processing, you just, you know, use the tablet for some other thing and pop in a new one, you know?

**Chris Gammell:** Yeah. Yeah, totally. I think some of it is like, it's so tough. I mean, like, don't get me wrong. This is a very tough problem for the car makers out there, because you're sourcing a part, you're sourcing a set of parts, including displays that you're trying to make for like five to 10 years. You know, you need to have like the sourcing guarantees, and you're trying to be bleeding edge, but, you know, just cars take a long time to get built and, you know, get through production. And so you're almost by definition.

**Dave Jones:** And, right, the customer experience is important, right? Because if you make it so it's just slotted in, slot in your own one, it's like people get the car and you go, oh, well, where's the screen? Oh, no, you just slot in your own tablet, but I don't own a tablet. Or, oh, no, it's not compatible.

**Chris Gammell:** It's like you could source it, though. Like you could have a tablet that you give to the car owner. Yes, that's right. And you just switch it out later.

**Dave Jones:** You actually provide a standard. Yes, that'd be neat. How would you do that? Would you like, you know, yeah, but you see, you would have to standardize on a particular type, and then you'd have to rely on the manufacturer to keep, you know, if you slotted it in, right, it's got to get power somehow, right? So you've got to have some sort of standardized USB thing, and it's got to be in the right location, and it's got to be the, you know. And the tablet has to be the exact form factor.

**Chris Gammell:** Yeah. I mean, it doesn't have to be like a commercial tablet, though.

**Dave Jones:** Yeah, right. Okay.

**Chris Gammell:** But yeah, I think if you define a standard, though, right? So if Ford or GM or one of the big car makers said, you know what, we're just going to switch to the standardized form factor. What would happen is you'd get like, you'd get downward price pressure because you'd have secondary markets pop up around like upgraded screens. Absolutely. People would be able to figure out the connector. They'd be able to figure out that stuff. They'd want to do upgraded things, and then it would become an ecosystem because, surely because of volume, right? I mean, yeah. I agree. Yep. So I don't know. I think it's just some of it is humor. Some of it is true sourcing. I think there's actually some regulation stuff in there, too. Like, I imagine that if you're in an accident, you probably have to have like shadow proof glass or all this stuff that I'm sure they have to do testing around that stuff. So I know there's other restrictions in there.

**Dave Jones:** Well, the good thing about mine is mine has failed once on me, right? The big 10-inch or whatever touchscreen thing, right? It just went blank or it locked up or something, right? So you couldn't use it. You had to repower the car. Yeah, and it worked fine once it was repowered. But it's only ever happened once, and I couldn't actually reproduce it. Don't know why. But anyway, it did lock up. Apparently, Teslas do this all the time. But my one's only ever happened once in now 25,000 kilometers, 27,000 kilometers or something. So, you know, done a lot of driving, you know. But the car still worked because it's got the dedicated heads-up display, which still has all the required info, and you don't need that user interface to drive the car safely, right? So it's, you know.

**Chris Gammell:** Yeah, and I think that's really the thrust of this article, too, is like, look, you can make a car that has knobs and is drivable without having all the other stuff in there. I think the real, I mean, one of the problems is just that it's, you know, it all comes, you know, the user experience stuff that I, whenever I think of user experience, it's like, how are you designed? How is your software? And then how is your hardware keeping up? Out of those three, one is, you know, it's just going to age with the car. And so you have fewer and fewer resources compared to other expectations that people have, right? If they have a cell phone that's less than two years old and they have a car that's eight years old, almost by definition, and, you know, the time to build the car as well, you know, may have been two years in development. Now you're working on 10-year-old technology versus two, and just there's just a complete mismatch in terms of expectations and hardware. So it just becomes, I think, I look at, you know, my wife has a 2015 car, so that was probably designed in 2012. That's 10 years now. It's like, it's insane, you know? Yep. I think, I think I reload the GPS data if I was to use it with an SD card hidden somewhere underneath the center console. It's just like, oh, okay. Yeah.

**Dave Jones:** I've got a test equipment segue here. I'm trying to get you the link though, because I don't know if you've seen, you're probably not following on the EUV blog forum. Give me a second. Give me a second. I will actually find it.

**Chris Gammell:** You know, that's on me then, really. Yeah.

**Dave Jones:** Oh, totally. Yeah. Because you're not following on the...

**Chris Gammell:** Got to keep up with the latest. Yes. Yes, you do. On the EUV blog forum.

**Dave Jones:** There is. I will find it. I'll find it. I'm here. I'm going to get it.

**Chris Gammell:** Kind of hoping it's Sharia's latest. I actually, I started watching Sharia's latest.

**Dave Jones:** What's his latest one? I haven't seen it.

**Chris Gammell:** It was a teardown and test of SignalPath. I should have put it on the list, apparently. There we go. I got it. Oh, the 60 gigahertz Y gig phased array.

**Dave Jones:** Hell yeah. Oh, right. Yeah. I haven't watched that one. Yeah. Right.

**Chris Gammell:** Like, it's getting so crazy that like... No, it's getting so crazy. It's just like so far away from anything that I understand. I'm just like, oh yeah. Okay. It's like magic. Look. Hey, look. Magic. Show me, wizard Sharia.

**Dave Jones:** So, there you go. I sent you a link. You might have to... The image, you might have to actually click on the image to make it bigger.

**Chris Gammell:** Yeah. Yeah. Yep. Yep. You got it? What am I looking at here? Oh my gosh. What are you looking at? You're looking at a new oscilloscope from Tektronix. Seriously. That looks like a tablet with BNC connectors. Yeah.

**Dave Jones:** Yeah. See, I was not supposed to talk about this. But, of course, the nerds on the EAV blog forum found all the info. So, it has not been released yet. So, I'm not supposed to...

**Chris Gammell:** No hints from Dave. No hints from Dave.

**Dave Jones:** But people have found the data sheet. Like, it leaked out on Farnell's website or something. And so, everyone has all the photos, all the info, right? Yeah. Yeah. Yeah. So, I guess I'm allowed to talk about it now. You know.

**Chris Gammell:** Right? If not, Dave's just a series of bleeps right now.

**Dave Jones:** Right. Okay. Bleep, bleep, bleep, bleep. So, anyway, it's there. It's all on the EAV blog forum, right? So, it's all out there.

**Chris Gammell:** This is definitely... This isn't a real shot, though. This is a render. No. I'm definitely looking at a render. No. No.

**Dave Jones:** That's a real shot.

**Chris Gammell:** That's a real shot? Are you sure? It looks not real.

**Dave Jones:** That looks like a real shot to me. It could be.

**Chris Gammell:** Renders are so tough to figure out these days.

**Dave Jones:** I know. That's what it actually looks like. So, that... It wouldn't surprise me if that's a real shot. Because it actually looks like that. So, yeah. All right.

**Chris Gammell:** A little quick vote here, folks. You can go vote on the comment section. Is it a render? I think it is. Look at the shadows. The shadows are too perfect.

**Dave Jones:** Right. Shadows are too perfect.

**Chris Gammell:** If it is a product shot, it's a very, very nicely done product shot. Yes. I will say that.

**Dave Jones:** Yes.

**Chris Gammell:** Also, the screen looks totally fake. Right.

**Dave Jones:** But that's...

**Chris Gammell:** That's how perfect that sine wave is. I guess I could be superimposed, but... I have questions, Dave.

**Dave Jones:** That is... But that looks real to me. Because I physically have one here. And it does look like I could...

**Chris Gammell:** Mix company on... Mix the signal of skill scopes. Yeah.

**Dave Jones:** So, anyway. I've got... Yes. I've got a pre-release one here. It's so pre-release. I can... Maybe I can spoil this thing. Like... Well, some things are 3D printed. Let's just say that. Some things on my model are 3D printed.

**Chris Gammell:** Yes. Hey, that's great. Hey, kudos to Key... Tech Terranix, rather, for sending out 3D printed stuff like that. I think that's great. You got to trust the community.

**Dave Jones:** Yes. No. Yeah. They gave me a pre-release one. Now, obviously, it won't be 3D printed in the final version. Yeah. Right. It's obviously got to be injection mold. But, yeah. Yeah. Anyway. Anyway. So, yes. It is very cool. And it is kind of... You know, it's different. And I was not expecting it. And in, what, a couple of weeks, a week and a half or something like that, you'll be able to watch my first impressions video and unboxing video and stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** And I...

**Chris Gammell:** You're not going to get in trouble for this, are you? Because I don't want to have to cut all this stuff out.

**Dave Jones:** No. No. No. No. This is all on the forum. It's all on the forum. So, yep. All right. I've mentioned that I've got several videos hidden away. You can't find them unless you guess the URL, that random bunch of letters. So, good luck.

**Dave Jones:** The hash on YouTube. Anyway. So, the interesting segue with this, right, is why I brought it up. It wasn't on the list. I wasn't going to talk about it. But basically, yes, it is a touch tablet-y kind of scope. But it does have some real controls on the side, of course. But the whole idea is that this is similar to the 3, 4, 5, and 6 series tech. I don't know if you've used those, the new tech scopes, the 3, 4, 5, 6 series. No.

**Chris Gammell:** No, no. I think... Right. No. I have very old tech.

**Dave Jones:** Yeah. Right. Very old tech. No pun intended. All right. So, yeah. Basically, they've gone with this new sort of... I don't know how to explain the user interface. It's very tablet-y. Everything's sort of like it's got these modular little control things that pop up and disappear. And, you know, it's very... I don't know. Yeah.

**Chris Gammell:** It seems like they use the edge of the screen as almost like a beveled button display, but it's touch buttons. Is that a fair assessment?

**Dave Jones:** Maybe. Something like that. But, yeah. The point is, is that you can use it...

**Chris Gammell:** I'm going off a single photo here, so... Yeah. Yeah.

**Dave Jones:** So, the point is, is that you can use the scope completely via the touchscreen, right? You don't have to use the controls. And it's got a VNC remote networking screen interface so that all you need is you don't need to duplicate the controls.

**Chris Gammell:** Huh.

**Dave Jones:** So, you can remote control the scope by only having a mouse and the screen. Just like you do a remote control on somebody's computer, you can do the same for this, right? And you can do everything on the scope on the screen. You don't have to have the controls. And that's kind of...

**Chris Gammell:** You like or don't like? Because this is almost like... This is almost moving towards slapping a TFT on a headless unit. It kind of feels like that to me.

**Dave Jones:** Exactly. Exactly. And I like that concept. And they've stuck with that across... This is all their new gen scopes. So, now with this new 2 series...

**Chris Gammell:** New gen low end or new gen all the way up?

**Dave Jones:** All the way up. It's the same usability, the same interface from now the new 2 series right up to the 6 series. So, they're all the same. So, if you use the lowest end one, you can use the highest end one and vice versa.

**Chris Gammell:** So, you're basically paying for the upgrade on the capture chipset and front end low noise amplifiers. You're paying for that sort of stuff.

**Dave Jones:** So, any software improvements made in, say, the highest end 6 series, it can flow down to the 2 series.

**Chris Gammell:** Because it's a software thing. Yeah. I mean, you've got to imagine from a management perspective too. Like, if you have... Say you have two... Say one through six, right? You have six layers of scope based on different margin levels, whatever, manufacturing costs, whatever. I mean, you want to have a single unified interface if you can. So, that also it's very easy for someone who bought a two scope is like, oh, you know how to use the two scope? The six is great. All you have to do is give us $80,000 more. Right. Yeah.

**Dave Jones:** Exactly. So, yeah. And I...

**Chris Gammell:** We also take credit card.

**Dave Jones:** Yep. So, I just think that concept is interesting where, you know, as you said, it could be... They could actually make a completely headless unit with no controls whatsoever.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? Yeah. Right. And so, it's a pure tablet stove. It's a pure tablet stove.

**Chris Gammell:** I've seen that from the tech. I think the VNA... Maybe it was a key site. Like, there's one where, like, basically it's a, you know, take it with you VNA and it was like a 50 gigahertz VNA or something crazy high end. But it was like, yeah, there is no... It's just a front end with a high speed, you know...

**Dave Jones:** It's a complete headless unit. Yeah. Actually, tech do do this in some of the real high end stuff. And also, yeah, also a key site do headless units as well. And I'm sure I think LaCroix, basically all of the major ones do like a headless unit, I think.

**Chris Gammell:** Yeah.

**Dave Jones:** So...

**Chris Gammell:** One thing I think about with this stuff is, like, the hard part that I imagine is, like, the isolation. So, if I buy a scope and I plug it into my computer, you better be damn sure that you are optically isolated. Maybe not even optically, just isolated, right? It could be capacitive. It could be whatever. But I want many thousands of volts RMS isolation between my expensive computer and my expensive scope, which is supposed to be floating anyways. And so, okay. Well, no.

**Dave Jones:** Normal scopes aren't floating, though. Normal scopes are mains earth referenced. They're grounded.

**Chris Gammell:** Yes. Thank you. But... I just don't want it... I don't want my computer to be attached to it.

**Dave Jones:** That's the main thing. Well, yes. Because it's more robust. Basically, if you... Yeah. If you screw up something with your scope, it has a very low impedance path from those B and Cs to the mains earth, right? So, hopefully, you don't blow up your scope. You can just...

**Chris Gammell:** You can buy floating scopes as well, though. You can also buy isolated scopes.

**Dave Jones:** Most of them are not. And this new one is not. It is not a tablet. Yeah. Most portable scopes, they will be isolated. Some are isolated. Some aren't. This one is not. Because it can be used as a bench scope as well, right?

**Chris Gammell:** Yeah.

**Dave Jones:** And it comes with a big thumb screw terminal on the side so that you can ground that side. Oh, yeah.

**Chris Gammell:** Yeah. Oh, nice. So, the thing that I'm getting at, though, is if you do have something that's just completely headless and it's just crapping out data at USB 3 levels, now you're pushing that through an isolator, too. Like, that's got to be a super fancy isolator. You know, like, the speeds on that have to be crazy high.

**Dave Jones:** Well, there's two ways to do it, of course. You can do it on the front end. So, you can have a completely floating front end. Or you can do it on the digital side. And then all of your inputs are common together, but they're not mains earth reference to back to your computer via the USB. So, yeah, there's two ways to do that.

**Chris Gammell:** I'm sure they're thinking about it. I was just thinking the cost of, I don't know if you've looked at isolator costs, but they're just so crazy expensive.

**Dave Jones:** Yeah, yeah, yeah. The crazy expensive, especially the higher speed you want to go.

**Chris Gammell:** I guess at a certain point, you just skip doing, like, a, you know, a opto-based or even a capacitive-based. And you're like, you know what, I'm just going to put this into a serializer and you put it through a piece of fiber optic and you, like, hop a gap like that. You know, it's just crazy.

**Dave Jones:** It's nuts.

**Chris Gammell:** Bonkers.

**Dave Jones:** Anyway, yeah, that's very cool. How long until this is? I think early June, yeah. Yeah, it's a couple of weeks. I think June 7 or something. They've got a big announcement. You can go sign up for the live show when they actually release it and stuff like that.

**Chris Gammell:** SeaTac, don't worry. Dave is not only, you know, revealing some of your secrets on his forum, he's also helping promote it. So, you know, it's push and pull, push and pull.

**Dave Jones:** I did not reveal secrets. Everyone else did. It was like, it was like, I'm surprised.

**Chris Gammell:** Are you responsible for these secrets?

**Dave Jones:** I was just sitting there waiting, like, when is somebody going to, you know, a data sheet's going to leak somewhere, right? Because they have to send the data sheets ahead of time to all of the resellers and they have to put it on their website. And they, you know, and it just leaks into search engines everywhere.

**Chris Gammell:** The greatest argument against conspiracy theories ever is humans suck at keeping things secret.

**Dave Jones:** Yeah, yeah, exactly. But I did keep my end of the bargain. So it wasn't me who released it. So, yeah. Anyway, anyway, it's out there. Boy. Yeah. I'm sure they don't mind anyway. It's all part of the hype, right? So, and you're either going to go, wow, this is great. Or you're going to hate it and go, nah, nah, that's just absolutely no use to me.

**Chris Gammell:** I don't know. I can't even think about it. Like, some people like really get it, you know, obviously people on the forum are very clued into when there's releases and the latest and greatest in tech test equipment. I'm like, until I have like a credit card with enough budget on it from my employer or from myself that I'm like ready to buy, like everything else is just moot and just really going to be tempting to me. So I'm like, I don't, this is why I had to stop. I had to stop subscribing to camera gear reviews as well.

**Dave Jones:** Oh, right. Yes.

**Chris Gammell:** Oh, I need that new, the new camera. I'm like, what for? You sit in front of a webcam effectively. Exactly. Like you need to look any, you know, I have no needs. I'm not a filmmaker. I know this. Yep. Viscerally.

**Dave Jones:** Yep. Same here. I've, I've gone through phases like that. Oh, the latest camcorders come out. Whoa. Will I upgrade? It's like, oh God, no, I'm just shooting 1080p freaking video. It's fine. That's right. You know, it's like, yeah.

**Chris Gammell:** Some people go in the other direction though. So some people don't say, hey, I need the latest and greatest thing that I can buy. They say, hey, how do I build all this stuff myself? And I want to talk about this a little bit because there was a video I found. And it was probably three years old now, I think maybe more, but it was an EV conversion. And like, did you happen to watch this?

**Dave Jones:** I think I watched it years ago and I have watched some of it just, just before the show. Yeah.

**Chris Gammell:** Yeah. 2019. So it came out in 2019. It's basically a guy who he's reviewing his conversion after 10 years, which is super impressive. He did an EV and I'm watching this thing, just getting so anxious thinking about like the way he's talking about everything saying, oh yeah, you know, I just like have a little dial here and this is how I turn this on. And then I charge this. It's about 90 kilowatts and blah, blah, blah. And I'm just like, holy crap.

**Dave Jones:** Yeah. Yeah. And it's all custom, right? It's all custom stuff. It's all homebrew stuff. I used to work with someone like this and she actually built her own EV. And this was, this was way before this one in 2009, this would have been mid two thousands or something like that. And you know, that was like bleeding edge back then. Like there were, you know, yeah, it was incredible.

**Chris Gammell:** Yeah. Actually I met a tech engineer. Oh no, we had him on the show. Oh yeah. One of the guys, I forget his name now. Sorry. One of the techtronics engineers we had on the show at some point and he did an EV conversion as well. It was like a BMW. I don't remember. I'll look him up. But yeah, he was crazy too. I mean, like the thing is, I think the thing is the guy in this video, I didn't catch his name. What is it? E. Tischer. And the guy that we had on the show, who I've forgotten his name. They're wicked smart. I mean like these guys, you know, guys and gals like, they're just, they're so freaking smart that they're like, yeah, this is no problem, but I am not smart. And I'm so afraid. They're so, they're so passionate about this.

**Dave Jones:** It's like, I could do it, but I don't freaking want to because it scares the shit out of me. Right. Yeah. It's like, I just get the heebie-jeebies around, you know, huge energy battery packs. It just like, yeah.

**Chris Gammell:** I guess I asked our guest about it. I've already recorded with our guest next week, who was a little surprised. I'll tell you Dave after the show. Oh, okay. But I asked her about it too. It was just like, you know, she does a lot of projects and you know, I was just like, well, what do you dig into? And she's like, yeah, not that. And I'm like, yeah, me neither. Yeah. Yeah. You're just commiserating, you know?

**Dave Jones:** Yeah. Yeah. We're just total wusses, aren't we?

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** I'm okay with it. You know, I think some of it, I think what it comes down to, and I guess people will hear me say this next week too. Some of it is just maintenance, you know? Like I think about like, so Mr. Tischer here, the, the guy in the video, like that he must have like stories where he's just broken down on the side of the highway. Like there's just things happening, you know? And like, I can call someone when my car breaks down because there's, who do you call for this range of command? Yeah. No, you just, I guess you, you know, your tow truck guy and then you just take it home. You simply call the tow truck. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** I guess maybe it's not a big deal, but I'm just, I'm not at that risk level in my life right now.

**Speaker ?:** You're right.

**Dave Jones:** I totally agree. I'm just like, yeah, no, no, no, no, no, no, thanks. Oh boy. Yep. Yeah.

**Chris Gammell:** I'm sure there's some aspect of like power in there as well that I'm just not, uh, not, that is not a DIY portion that I will be, uh, spending my time on. I will tell you what I have been spending my time on, which is relearning free CAD.

**Dave Jones:** Oh, why?

**Chris Gammell:** Yeah. It turns out when you, uh, put it down for about three months, it is a very difficult program to come back to. Oh. So this is the, uh, CAD program.

**Dave Jones:** Yeah. I, I actually tried it once. Doesn't it have like a command line interface as well? It's kind of maybe, uh, maybe I'm using a very old version.

**Chris Gammell:** It does. That was not for me. If so.

**Dave Jones:** Uh, it was just, yeah, it was just not intuitive at all. I just like try. Everyone said, try free CAD. It's great. It's great. It's easy to use. Like I just went, no, no, I'm sorry. If I can't draw a freaking cube in an hour, no, it's not easy to use. You know, it's like, no. Yeah.

**Chris Gammell:** So, I mean, there are some things that I think I mentioned last, you know, I, this is now my like third time using it and, uh, you know, it went okay last time. I went through a lot of tutorials and I was able to build a case. Right. So that was my big thing last time. And I started from a really good Adafruit model. Right. So Adafruit publishes lots of step models of their cases. Really great. You know, community service. Awesome. That is a great place to start because it's like, you're starting from like a known shape and then you're just kind of mapping to that shape. Like that is.

**Dave Jones:** Yep. Yeah.

**Chris Gammell:** That is, that is the way to start. I think I, if I had to recommend other people, it'd be that because if you just start with a blank sheet of paper, it's like. It's, it's harder.

**Dave Jones:** Some packages are easier than others. Like I've done that. I've done like case designs for my watches and my watch projects and stuff like that. And some packages just like within 10, 15 minutes of using it, I've got a pretty fancy looking watch case out of them. Right. Others I'm sitting there for hours. Like, like a free cat. I'm sitting there for hours and I'm still scratching my head, figuring out how to do the most basic stuff. It's just, you know.

**Chris Gammell:** Oh yeah. And I think that's what it comes down to is like, it's one of those things where I think as I get older and grumpier, you know, and hang out with you more, uh, I think what it really comes down to is I just want one answer. And a lot of things try and sell themselves based on like, Oh, there are so many answers. Look at all these different ways you can do things. Like if I'm going to pick on other open source projects like Linux, they're like, Oh, look at all these different ways you can do things. I'm like, I don't care. Just tell me one way to do things. Yep. I don't want to dig into a forum post where people are like, Ooh, isn't it cool? You can do it this way and that way and this way and that way. And you know, no, it's not Chris. You can go and try all these different things that, you know, 2 PM on a Saturday.

**Dave Jones:** Nope. Well, no. How about one thing? So totally.

**Chris Gammell:** I would say that's my, uh, my, my complaint coming back to it. I think some of it is just new program, you know, like a new CAD for, I mean, honestly, I opened a KiCad recently.

**Dave Jones:** You want a dumb CAD program, just like you want a dumb car. You want a dumb CAD program. You want a dumb CAD program that just does simple stuff simply.

**Chris Gammell:** Yeah. Right. I will. I'll be a little vulnerable here in a moment of weakness, Dave.

**Dave Jones:** Yeah.

**Chris Gammell:** I, uh, I almost installed fusion 360 again.

**Dave Jones:** Oh, okay.

**Chris Gammell:** But I couldn't figure out how to do it in Linux.

**Dave Jones:** That's what saved you, huh?

**Chris Gammell:** Yeah. There's a, there's an install script in Linux that like helps you install it. And it's got like wine and you know, like a windows emulator and script.

**Dave Jones:** You lost me at script. Okay. I'm just like, no, no, no, no, no, no.

**Chris Gammell:** I'm sure it would have worked. And you know, don't get me wrong. I think fusion 360 is great. Other programs are great, but I've made the switch. And luckily I was prevented from going back. So, uh, dug my own hole and now I will sit in it. Thank you very much. And as a resolution of the story, I was able to model the very, very, very simple thing that I was trying to do. Yeah. So small, small win, small win. Cool. Well done. People show up at embedded world. They may get to see it. So come on out to embedded world. That's in Germany. That's the German one. Yeah. That's in Nuremberg. When is it again? Four weeks. Four weeks. All right. June 20th to 24th, I believe. It's enormous. Yeah. It's not as big as electronica, but still pretty big.

**Dave Jones:** Right. Yep.

**Chris Gammell:** Yeah. And that electronica is later this year. I am wondering about what's going to happen later in the year. Like trade show wise. I'm really hoping Supercon comes back. The Hackaday Supercon. I hope they do that again. Yep. Electronica is this year. I'm sure that'll be insane.

**Dave Jones:** So what's happening in Germany with all the COF stuff? You know, all the masks and everything else and lockdowns and what's happening? I don't know. Yeah. I think it's more open than it had been.

**Chris Gammell:** I haven't seen, there haven't been any, like, I think there's no mask requirements. I think there's no travel requirements. I need to double check.

**Speaker ?:** Right.

**Chris Gammell:** But, uh, yep. Yeah. I'm already locked in to go. So it's like, well, you have to wear this beanie on your head in order to, you know, come into the here because it's a safe thing to do. I'll be like, okay, cool. I want to see people. You have to wear a full body suit. Right. All right. Well, it's not going to be flattering, but I'll do it. You know? Yeah.

**Dave Jones:** You have to wear a full body suit and, you know. Full body suit.

**Chris Gammell:** Oh man. Can you imagine walking around a conference like that? Oh.

**Dave Jones:** Dude, I've done an obstacle race in a bunny suit. You don't have to tell me about how uncomfortable that is. It almost passed out due to heat, you know, build up and exhaustion.

**Chris Gammell:** That's like a, yeah, that's like wearing a garbage bag basically. Yeah. Not great for ventilation. No, no. Not at all. Cut a hole under the armpits or something. That is not fun. Yeah.

**Dave Jones:** I can tell you.

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway, can we go back to cars again? Because we have been, uh, done a lot of cars. Sure. Stuff.

**Chris Gammell:** We are pretty into cars. Yeah. Yeah. We're pretty into cars.

**Dave Jones:** Yeah. We're total car dudes, aren't we? Yeah. Yeah. Yeah. Yeah. All right. Welcome to car talk. Well, yeah. At one point I used to change my own oil and fix my own car. I have my own service manual and stuff. That's when I owned my first car.

**Chris Gammell:** Does your car even have oil now? Like what happens with an EV and like lubrication?

**Dave Jones:** Uh, it has, um, it was no oil for the engine. Yeah. I'm sure there's like bearing grease for the wheels and the power steering. Like there's actually power steering fluid and stuff like that. Right. Yeah. Cause that's a hydraulic thing. Yeah. Yeah. It's, it's basically all the same. So you basically just don't have the engine. So you've got no oil for your, you know, to lubricate. For the room, room, make go part. Yeah, exactly. Yeah. So, yeah. Anyway. So yeah, it's, um, yeah. I used to fix my own car, but geez, I haven't done that for like 30 years. So yeah. Yep. Yep. All right. So cars, cars, hydrogen cars.

**Chris Gammell:** Oh, there's a new, yeah. Researchers.

**Dave Jones:** Australian researchers claim to have made a giant leap.

**Chris Gammell:** You know, you lost me at Australian researchers. Do they, you know, do they even do research in Australia? Of course we do. All the, all the experiments are upside down. I didn't just invert your results, dude. It's not a good point. Good point. Yeah. You got to turn the notebook upside down then too. Yeah.

**Dave Jones:** All right.

**Chris Gammell:** So, so what is, uh, what is the deal here? Cause this is a.

**Dave Jones:** Anyway, this is a video from undecided with Matt Farrell, who does like, uh, info tech videos, I guess you could call them. Right. And yeah, apparently he's done a lot of videos and anyway, somebody put it on the Reddit. So I thought we'd discuss it. And it's like, yeah, there's some new innovation that scientists did here in Australia that increases the electrolysis, you know, the process of actually generating the hydrogen and makes it more efficient. It's like, meh, hydrogen cars will never be a thing. I'm sorry. Yeah. It's just, there's too many practical problems. It's just not going to happen. So, you know, faffing around the edges of trying to make it more efficient is, is just, no, it's, you know, the fundamental problems of storage and transport and everything else are still there. Even if you solve the generation part of it.

**Chris Gammell:** Well, you need some electricity and some water, Dave. Come on.

**Dave Jones:** Just like, well, you use more power to generate it than you get out. So that's, that's kind of a problem. I don't know if this, I haven't watched the whole video, so I don't know the exact details, but I don't know if this actually fixes it and flips it to energy, net energy positive. I.e. you, it take, you get more energy out than it takes to, no, no, it can't. It can't. There's no, you know, the laws of physics, surely. I don't, yeah. Say that you can't put more energy in.

**Chris Gammell:** I don't really do physics, Dave.

**Dave Jones:** Right. But, but, but surely, because you've got to create the hydrogen, right? You've got to create it and it takes energy to create the hydrogen. Therefore, I don't think there's any, I think it would disobey the laws of physics if you've got more energy out than what you put in.

**Chris Gammell:** Right. So. You know, Dave, if there's only one thing that we know more than cars, it's physics. It's physics. Yeah, exactly.

**Dave Jones:** And chemistry and the periodic table. And yeah. Yeah. Yeah. But yeah, no, surely. I mean, obviously, you know, huge energy density with fossil fuels, of course, right? Oil. Because there was a lot of energy used to create it in the process of time and compaction of the earth and everything else, right? Which compressed it and, you know, which compressed all that leaf and letter.

**Chris Gammell:** And then conveyance bonds. Yep.

**Dave Jones:** So that was all free energy input, so to speak. Free energy. And then we just came along and sucked it out of the ground and went, hey, thank you very much in nature for all that energy input from the sun and the pressure of mass. Black mold. You know. Texas tea. Yep. Anyway. So, yeah. I don't know. Just know. For hydrogen cars. Just stop it. Just stop it. I think I saw a hydrogen car ad from Toyota. I think they're one of the few who are actually trying to do it. And I think I saw it in ad on TV, like, in the last six months or something. I went, why? I think technically you can buy, like, hydrogen. Like, you can actually buy them, I think. Yeah. Yeah. I think you can actually buy them. But, like, God, no. No, no, no, no, no, no. Stop it, please. I don't care about hydrogen breakthroughs. I just don't. You know. There's some niche applications.

**Chris Gammell:** But I do wonder about, like, okay, so say, you know, we're an electrified future, right? 20, 25 years from now, right? Mass EV adoption. Solar on every roof. All the crap that, you know, everybody hopes for. What do they do for construction equipment? Like, you know, I drive by construction sites and stuff like that. And just, like, man, the amount of energy to just drive a dump truck. You know, like, I don't. It's. The power output is, like, insane.

**Dave Jones:** Surprisingly not. Because they're very heavily geared ratio. Like, you might find that, like, one of those huge tractor. Once again, I'm not a tractor expert. Go figure. But, you know, like a big John Deere tractor or something is, like, only, like, a couple of hundred horsepower. Or something like that, right? You can get normal cars that have more horsepower. But it's just how they divide that down through to the wheels and the gear ratios and everything else. So they get massive amounts of torque and the giant wheels and everything, right? So it's not.

**Chris Gammell:** Let me use my mechanical engineering skills here, Dave. I believe the wheels on the bus go round and round. Round. Round and round. I've been learning this with my daughter. Yeah, I know. Yeah, yeah.

**Dave Jones:** Wheels on the bus go round and round. Round and round. Oh, God. We've got one of those things that we, one of those learning, you know, like it's a keyboard thing. And we had it in the car for years. And all we heard everywhere we go is the wheels on the bus. Oh, God.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Yep. Yep. You're going to get more of that.

**Chris Gammell:** Oh, they already are. Yeah. All the toys in our house also, like, are bilingual. They also speak Spanish. Oh, really? So I, yeah. Yeah. We'll be trying that. It's been interesting. Wow. And, yeah. So I know my ABCs in Spanish now. Mostly if I sing it, though. Right.

**Dave Jones:** You've got, if somebody talks to you on the street in Spanish, you're going to reply in song.

**Chris Gammell:** Yes, that's right. Actually, I was. Great stuff. On the toy aspect, you know, this is not like a new thing in the toy industry, but like we were gifted a bunch of secondhand toys. And it's fine. And one of them is like actually a bulldozer, speaking of construction equipment. Yeah. And it's like meant to be on a track. And on the underside, there is, there's actually eight tiny little buttons. And it's like basically as it drives over tracks.

**Dave Jones:** Oh, yes. It pushes the buttons. Yeah. I know those ones. Yeah.

**Chris Gammell:** So it's an eight, it's an eight bit encoding. Right. And then that triggers different, different sections of the ROM. And then it sings different little songs. It sings different.

**Dave Jones:** Yeah. Yeah. We had like a Thomas the Tank Engine thing. Yeah, exactly. That's the same thing. And then you hear the fat controller come on and, you know, this causes confusion and delay, you know, because it went over this part that triggers this part. Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. No, it's that. I mean, I just, toy designers, you know, like I think a lot of the tricks are the same, you know, like, but they're deployed in lots of very creative ways. And I'm, I'm always very impressed with toy design. I think it's. Yep. I don't know. I don't think I'd be good at it. I don't think, you know, like the. No, because you would be trying to use.

**Dave Jones:** You would be trying to use the chip of the week, which we have, which is the magnetic sensor, which, which costs like two bucks a pop or something, you know? And, and, you know, no, no, no, no. We want two pieces of metal. Oh my God. It was.

**Chris Gammell:** Yeah. It was a buck 63. Yeah.

**Dave Jones:** There you go. I called it. Right. I was near enough. And yeah. So no, you want two pieces of spring metal that just touch because you can, you can stamp those out for 0.01 cents each, you know? Yeah.

**Chris Gammell:** Yeah. And there's another, we have like a teapot as well. That's like, you know, lights up and it like does all the different actions when you like pour the tea and I'm like, oh, I bet it's got an accelerometer. No, no, no, no, no, no, no. Contact switch. Yeah. Contact switch, something like that, you know? Yep. Yeah. Yeah. I mean like big Clive, he takes apart like toys and like low cost stuff. And it's like. Yeah, it's cool. It's elegant, but it's never like that. It's never complex, right?

**Dave Jones:** It's never complex. And it's usually not that robust, you know? It's usually, you know, they make it as robust as it needs to be kind of. And then nothing more. It's not, it's not over-engineered, you know? It's price.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. It's built down. Yeah, exactly.

**Chris Gammell:** It's optimized for cost and volume and.

**Dave Jones:** Good stuff. Yep. You just got to get more of that.

**Chris Gammell:** I know. I wish I, I wish we wouldn't. How do you tell people that, yeah, we're, we're cool.

**Dave Jones:** You did the crime. You got to do the time.

**Chris Gammell:** All right.

**Dave Jones:** Yep. All right.

**Chris Gammell:** So back to the construction stuff. Do you think that it's just a matter of gearing?

**Dave Jones:** Yeah, I don't. I think, I think you might be surprised at like how little horsepower huge. You know, you'd think it might, oh, it's got to have like 5,000 horsepower or something. I think it might be. Yeah. Maybe the huge mining trucks and stuff do, but I think you might be surprised.

**Chris Gammell:** Just think of like a Mack truck, you know, like a diesel. Right. But like diesel engines, they have tons of torque, right? I mean, like, don't they have like lots of torque at the low end sort of thing? Isn't that what like people who know about trucks say? That's what all the gearing does, right? Yeah. Yeah. Dave, I'm really out of my element here.

**Dave Jones:** Okay. Here we go. Here we go. In, in, in 2014, this is the first thing on Google. In 2014, a Mack, a Mack truck, right? We just chose Mack trucks, right? Right. They have, they, they offer three engine series, 325 horsepower to 605 horsepower. So that is equivalent to a high performance sports car. Right. Right. It's nothing more. I guess. And that's a big Mack truck. Right. But they have like 6, you know, 2700 newton meters of torque. Right. You know, absolutely. Yeah. I guess that's the thing.

**Chris Gammell:** I don't, I don't know how horsepower translates to actual torque. Like that's a power. That's like a. Yeah. It's all the gearing.

**Dave Jones:** As I said, it's the.

**Chris Gammell:** Horsepower is such a dumb measure, isn't it?

**Dave Jones:** Oh, well, you know. Yeah.

**Chris Gammell:** Anyways. Yeah. I just think about like, okay, so now you have. So what I was really looking, when I was driving by the site, it was like, they were loading up a, they were like moving. They were doing earth moving. Right. So the, basically a backhoe was scooping up dirt, putting into a truck. And then that truck goes and deposits it at like a dump or something like that, or some central repository. And so like, just thinking about the, like the power output though, you would have to go and recharge that truck. You know, like just like the, I don't know, maybe it would just be about the charge capacity and, and how fast you could charge something like that. I would just think it would be very onerous versus plugging more diesel into a, into a truck and, and moving earth like that. You know, it's just like, it just seems like, uh, in the logistical sense, construction will be a very difficult thing for a non-carbon future, but maybe there's stuff out there that's already, you know, maybe Caterpillar and all of them, you know, who else does it? I don't know any other brands.

**Dave Jones:** Sorry, I don't remember any, uh, news coverage of any like big industrial machinery actually going fully electric, but I could be wrong. Maybe if we went out and searched it anyway, going back to the horsepower thing, John Deere tractors, I'm on the John Deere tractor website. So I know you're a big five E series fan boy of the five. Yeah, I know.

**Chris Gammell:** I love, I love, uh, yeah, those are. Yep.

**Dave Jones:** So we're, so we're talking 50 horsepower to 93 horsepower in the entire range. That's a bit like that's a John Deere tractor. Or if you go up to the big five R series, John Deere's 90 horsepower to 125 horsepower.

**Chris Gammell:** I just think that the torque is different than the horsepower.

**Dave Jones:** Yes, yes, yes, it is. It, it comes through differently. That's what I'm talking. It's the gear ratios and everything else. You know, it's, it's, it's how you transfer that horsepower through to the wheels and everything. And then you've got the giant wheels and everything helps, you know, and, and these things, you know, like they can't do over like 40 Ks an hour or something, you know. Yeah. Right. Exactly. Yeah. They're very low speed.

**Chris Gammell:** Yeah. I mean, there's a, so, you know, just preliminary Googling, you know, caterpillar, you know, they all have stuff about this, how we're going to move to an EV future. But like, I will, I will, what I actually, I should go on YouTube is actually the real thing. You know, they're talking about it in mining. It was like, actually that makes sense. If there's anything like underground, it should be electric, but anyway, what, what I'm talking

**Dave Jones:** about here, right. If you translate horsepower into kilowatts, right. Those lower end John Deere tractors are 37 kilowatts, seven 37 kilowatts. Right. That is not a big motor. Right. My, my, my, um, EV has 110 kilowatt motor in it. Right. So I, I can't see why it's not possible to convert tractors into fully electric. I don't know if anyone wants to tell us maybe the extra weight. Cause they're very low weight. People think tractors are heavy. They're not. They're really lightweight.

**Chris Gammell:** I was thinking about construction equipment, but yeah.

**Dave Jones:** Yeah, I know. But I'd start in from tractors and then we can work our way up, you know?

**Chris Gammell:** All right.

**Dave Jones:** Yes. Right. Yeah.

**Chris Gammell:** You work up to those monster, man.

**Dave Jones:** Oh, those big mining trucks and the big. Oh God. Those things are so cool. Yeah. I know. I know. So what a drive one. Yeah.

**Chris Gammell:** Yeah. There actually is a spot. Do you know, if you go to Vegas, you can actually go and like. Uh, you can go and drive construction equipment around and like just move dirt.

**Dave Jones:** Oh really?

**Chris Gammell:** Do you know? That's a thing. Yeah. Oh. Like you're like, you know, basically like a little kid. Yeah.

**Dave Jones:** It's one of those experience days, you know? It's one of those. Yeah. Yeah. Yeah. Yeah. You can go on. Yeah.

**Chris Gammell:** Yeah. So, you know. Okay. At least you find yourself in Vegas again.

**Dave Jones:** Right. I have to check out something like that's here. I would love to drive a train. I'd love to get like a train driving experience. I'm a train fan boy.

**Chris Gammell:** I know there's like a, there's train hobby groups.

**Dave Jones:** Yep.

**Chris Gammell:** It's just like, there's gotta be so. If you go join like a train hobby group, you know, like there's a lot of people that are into trains.

**Dave Jones:** Oh yeah. Yeah. Totally.

**Chris Gammell:** You gotta really work your way up before you get to be. Oh yeah. Before you get the big iron stuff. You know? Oh, whoa, whoa, whoa, buddy. You can't just drive a train right away. You gotta learn how to do it. You know? Forwards. Shovel here. Backwards. Shovel this coal first for a week. You gotta stop. You know?

**Dave Jones:** Yeah. Yep. Cool bananas. All right. Well, do we have any last minute? Our NPR is almost up. Do we have a last dibs? Dregs? Do we have any dregs? You know, Intel. Do we care?

**Chris Gammell:** As a new CEO. Newish CEO. Oh, do they?

**Dave Jones:** They got a new CEO?

**Chris Gammell:** Nah, I mean newish. I think he's been there a couple, a year or two. Pat Gelsinger.

**Dave Jones:** Oh, and he's got a plan to fix Intel. How? To buy.

**Chris Gammell:** Probably getting a lot of Uncle Sam money, to be honest.

**Dave Jones:** Yeah. And or buying AMD or something. I don't know.

**Chris Gammell:** Yeah. That would be something.

**Dave Jones:** That'd pretty much do it, I think. That'd pretty much fix Intel would be to buy AMD.

**Chris Gammell:** Yep. Here's an interesting thing on a forum on, someone asked recently about their client wanted them to have knowledge of where every chip was manufactured on the board they designed.

**Dave Jones:** That's not uncommon for the stuff I've worked on. You have to know where the chips are sourced from. Would it be possible in 2022 though? Well, it depends how deep you want to go because when you get a chip, right, and it's made in Taiwan or something, it's not all made in Taiwan, right? The actual wafer silicon could come from somewhere in China. Yeah, that's in Japan. And then it's chopped up in Malaysia and then testing. It's chopped up in Malaysia and then it's tested in China and then it's packaged in China and then it's sent. It's all over the shop. That's why you often see in the data sheet manufactured in one or more of the following countries. You know, it's like, you know, and there's a reason for that.

**Chris Gammell:** I always see that, you know, that doesn't bother me for chips for some reason. It always bothers me for olive oil. What? It says, yeah, olive oil. Like if you look at like, not like high-end olive oil, like you look at high-end olive oil, it's like, oh, this is from Italy and you're going to pay for it.

**Dave Jones:** Right.

**Chris Gammell:** No, it's like you look at like medium to low-grade olive oil, it's like, this was possibly manufactured in Spain, Tunisia, Italy, you know, Brooklyn. I don't know.

**Dave Jones:** And it's all just mashed together in one big vat.

**Chris Gammell:** And like literally, yeah, it was like some dude just like, well, let's just mix it together until it tastes like not garbage. Right. Yeah. So, you know, olives from all over the world. Yeah. All of the world. Ah. Olive-verd the world. Ah.

**Dave Jones:** Ah. Yeah. Yeah. Olive-verd.

**Chris Gammell:** Here all week, folks.

**Dave Jones:** Yeah.

**Chris Gammell:** The world. You know, maybe writing a title slide right now. Oh, you're right. You're writing a title. Olive-verd the world. Yeah. Let's see. We've actually had other olive-based names for shows in the past. I don't remember why. I think it was about Olive Green. Maybe it is. Drab Green, maybe. Ah, Drab.

**Dave Jones:** Drab Olive.

**Chris Gammell:** Drab Olive. I think that was it. I think you brought that up.

**Dave Jones:** Drab Olive is the official military color.

**Chris Gammell:** Yes. Ah, yes.

**Dave Jones:** Yes.

**Chris Gammell:** Yep. Drab Olive. January 2020. There you go. June 2020.

**Dave Jones:** Yeah.

**Chris Gammell:** Two years ago.

**Dave Jones:** Oh, this seems like way further.

**Chris Gammell:** Yeah. So anyways, it would be very interesting to know that stuff, but then like, okay, so now you know this. Now what? You know like, I don't know. I don't know. Yeah. Does it matter? What are you going to do? Right? I mean like, I just, that's what I always come back to is just like, what are you going to do about it? You know? Okay. I only source chips from the US. Well.

**Dave Jones:** Well, that's what Intel are trying to do, right? Is that the plan to fix it? There's more local manufacturing, right? And as you said, it's going to come from Uncle Sam Buck. So you're paying for it. Right. So congratulations.

**Chris Gammell:** Yeah. And we talked about packaging coming back to the US as well and testing and. Right. And like, you know, that might end up, there might be alternative ecosystems and pathways to do that sort of thing. I just think on a long enough timeline with a thick enough NBA playbook, someone's going to go, pretty expensive to do this in the US. You US. Yeah.

**Dave Jones:** No. I can.

**Chris Gammell:** We should optimize everything in Malaysia. I can. I can do all the packaging and blah, blah, blah. And like, oh, man. Yeah. You can picture it.

**Dave Jones:** You can picture the cycle will continue. Right. Oh, totally. And I said, they'll bring everything back here. And then in 10 years time, when all the political craps died down. Oh, look at this. We're consolidating again. And now we're back to. Yeah, exactly. Yeah. And they'll outsource again. And it's just, you know, it's. Yeah. Yeah.

**Chris Gammell:** Yeah. Same old story. But it's like the universe.

**Dave Jones:** You know, it just expands, does the inflation, then contracts. And then it's the same universe over and over again.

**Chris Gammell:** Oh, yeah. Yeah. Yeah. I mean, what's really scary is that there's like a multiverse of Chris and Dave.

**Chris Gammell:** Of them all. Also doing this exact same show.

**Dave Jones:** Right.

**Chris Gammell:** You know? Yeah. And they all came up with all of the world.

**Dave Jones:** Right. In the title. No. No. There's. I reckon there's only three of those tops. I reckon there's only three of them tops. Come on.

**Chris Gammell:** Oh, man. So many movies and shows about multiverse stuff right now. It's getting a little tired. It is. It's like if there's a multiverse, how do I switch? Can I sign up for a different one? Is there like a. Is there a form I've got?

**Dave Jones:** I've got a title. The Oliveverse. That's pretty good.

**Chris Gammell:** I reckon that's pretty good. I think mine's a little better. But you know. We'll add to the list. We'll. You know. How about this? You're in charge. The Oliveverse. The art for the show. Gets to pick the name.

**Speaker ?:** Okay.

**Chris Gammell:** Right. All right. Yeah. All right.

**Dave Jones:** I'm probably not going to bother to do the art. Yeah. Sometimes you get lucky though. Sometimes. It'd be lame. It'd be like an olive falling into a black hole or something. You know. Yeah. Yeah.

**Chris Gammell:** Like the. Like the. The gravity well thing.

**Dave Jones:** Yeah. Yeah. Right.

**Chris Gammell:** I. This is completely stupid. Now the stupidest thing that I've said in the past hour about to. About to happen. I was thinking about a joke the other day. Where. You know how like. People talk about like small and medium businesses. Yep. And like. They're like SMBs. Yeah. And. I was thinking about like. If I'm in a meeting at some point in the future. And. Someone says. Oh. And like. You know. We're targeting the SMB for this. This new rollout. And I'd be like. Do you mean. Small to medium business. Or do you mean. Supermassive black hole. All right. Because like. You know. Like they discover the supermassive. Black hole at the center of our galaxy.

**Dave Jones:** Yep. Yes. Yes. Yes. They did.

**Chris Gammell:** Yep. I kept seeing SMB. And I'm like. Oh yeah. That's a good joke. Like.

**Dave Jones:** I've seen that around a lot. Yeah. Small medium. Yeah. Business. Yeah. Yeah. The government likes to trod out. So you'll see. SMBs man.

**Chris Gammell:** You gotta watch out. They can just suck you in. You know. Yeah. They just. They just.

**Dave Jones:** I don't think I'm an SMB. Because I'm a one man band. So. You know. I'm.

**Chris Gammell:** It's an OMB.

**Dave Jones:** It's an OMB. Yeah. Yep. No ampales up.

**Chris Gammell:** Yeah. We should go. Before I make any terrible jokes. More terrible jokes.

**Dave Jones:** Catch you next time. Bye.
