---
episode: 354
title: A Meeting Of The Davids
url: https://theamphour.com/354-a-meeting-of-the-davids/
---

**Dave Jones:** This is The Amp Hour Podcast, released August 7th, 2017. Episode 354, A Meeting of the Davids. Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**David:** And I'm David from the EEV blog.

**Dave Jones:** David? Not Dave.

**David:** Not Dave, right. The other David. Yeah, I'm not Dave too. That would mean I was like a sequel.

**Dave Jones:** Yes. But you're commonly known as David too.

**David:** But I'm not like the second production of Dave. No. I'm a totally separate instantiation of Dave.

**Dave Jones:** What have I got on my website? I've got younger, better looking and less jaded.

**David:** Oh, thank you. I didn't know that.

**Dave Jones:** Yeah, it's on the website. There's a photo of you. Oh, he's checking it out.

**David:** Yeah, I've got to look at this. Right.

**Dave Jones:** Anyway, our esteemed regular co-host, Christopher J. Gamble, is absent again. Gallibanting around the country somewhere. Yankee land. We're sitting here. If this sounds a little bit different, we apologise because we're in the same office here. And it's actually quite, you might think, oh, being in the same location is easy to record. Because normally we use mumble to record with guests and record with each other on the other side of the world. But you might think it's easy being in the same office. It's not. We tried with the two microphones and it sucks ass. Because it's very difficult to acoustically decouple both microphones. So when you speak on the other side of the room, it's, you know.

**David:** Yeah. And then when the audio gets resolved later.

**Dave Jones:** We use a program which automatically amplifies and levels it and stuff like that. And it doesn't know the difference between you speaking in the background and me speaking in the foreground. And it amplifies it. It's just horrible. Noise gates and all those other audio things. So we decided to sit side by side. So we're practically rubbing shoulders. And we're talking in the same mic.

**David:** Yeah. I hope it's okay.

**Dave Jones:** Anyway, we'll find out. So what are you up to, David, too, at the moment? Are you allowed to say your, yes, we're allowed to say your full name. It's on the website.

**David:** Yeah, it's on the website. David Ledger. And some guy, like, doxed me.

**Dave Jones:** And some guy doxed you.

**David:** I actually know who it is. Right. But I'm going to not do it to you.

**Dave Jones:** Is it one of your uni friends?

**David:** I don't know.

**Dave Jones:** Right. Just some random.

**David:** It was really abrupt. It was like, this is his name. It's like, why? It's like, firstly, no one cares. Secondly, I'm commenting under my name. Right. Okay.

**Dave Jones:** Right. So this was on a video somewhere, was it? Yeah. Right.

**David:** Yeah, it was really weird.

**Dave Jones:** Somebody just said, his real name is David Ledger.

**David:** It's like, well, thanks. That was pointless. Yeah.

**Dave Jones:** So what are you walking on at the moment?

**David:** The multimeter.

**Dave Jones:** The multimeter app. Tell us about the drama. Tell us about the development. Is this your first time developing an app, per se?

**David:** The first time developing on Android.

**Dave Jones:** Developing on Android. Right. Okay. Yeah. Right. Well, what other platforms?

**David:** Basically, in high school, with even Windows Mobile, I was making apps.

**Dave Jones:** Because you're a Microsoft fanboy. Well, yeah. So you're a Windows phone fanboy.

**David:** Well, Windows Mobile was good because it was exactly the same library for the phone as it was the computer. Right. So I had a...

**Dave Jones:** Oh, of course. It's Microsoft Windows. It's running Windows, right? Yeah.

**David:** Yeah. So I don't really care for the platform, but I do care for the library that it has. And the commonness. You've seen me develop Windows Phone for the app. Yeah, yeah. And that came together basically flawlessly. Oh, yeah, yeah.

**Dave Jones:** Of course. It works. No glitches. Yeah.

**David:** No library inconsistencies. It was fine. But as soon as you get to Android, you get all these weird things. Like Android has some strange issues with BLE. Yeah.

**Dave Jones:** Oh, BLE's been a pain. We'll talk about that afterwards, BLE. But yeah, yeah, go on.

**David:** Yeah. Like Android 4.3 or something has an issue where it just closes the app because of a BLE thing. And it's nothing to do with the app. Right. So you have to like, kind of like, there's not really a workaround on 4.3. Right. But there are on other.

**Dave Jones:** Oh, on later versions. On later versions. What's the latest version of Android?

**David:** What is it, like 7 or something?

**Dave Jones:** 4.7 or something.

**David:** Yeah, yeah. Android. No, it's way up there now. Oh, is it? Yeah. Version.

**Dave Jones:** I don't think there are 5 yet, are they? 8. 8? Oh, right. Oh, well. We're way behind. Okay. Yeah, yeah. Yeah.

**David:** Yeah, so it will work fine on that. Yep. But Android 4.3 doesn't even support, you know, multiple simultaneous BLE devices. Right. Although it actually should. But it is behaving weirdly when you put a second adapter, even though it behaves perfectly fine in Android 7, 8, 6. Yep. Yep.

**Dave Jones:** Pain in the butt.

**David:** Yep.

**Dave Jones:** And so cross-platform development, is it possible? Like, true, I'm talking like the same code and just hit a button and it goes, compiles Windows, Android, iPhone, Linux, and Mac.

**David:** So Linux is the tough boat because, you know, there's lots of different distros of Linux.

**Speaker ?:** Yeah, yeah, yeah.

**Dave Jones:** Distros, sorry. That's the lingo. Yeah.

**David:** For the most part, you know, it's going to be the same, but there's little things with, you know, there's just little things you have to be aware of. And that makes it difficult. The only differences with our app at the moment are the BLE implementation for each device and the touchscreen implementation. Got it.

**Dave Jones:** Of course. The interface, the user interface is going to be different.

**David:** Yeah. On different platforms. Basically, the hardware layer is different, but everything else is the same code. Got it. There's no...

**Dave Jones:** Yep.

**David:** Yeah.

**Dave Jones:** And that's what you're shooting for though, right? Is basically, you're trying to have a common code base across all of them.

**David:** Yeah. Kind of like, it's two things. It's like more maintainable. And as you upgrade one platform, as long as you're not changing the hardware layer, like the interface layer with the hardware, then, you know, any upgrades propagate to all platforms.

**Dave Jones:** Right.

**David:** Which is great. Got it. I mean, what more could you want?

**Dave Jones:** There are... I asked this, or I mentioned it or something on Twitter or somewhere or forum or somewhere. And most people who were app developers just said, yeah, most people just give up on true platform thing. And they just have, like a lot of the code is common, of course. Yeah. But they just have separate compiled code bases for each platform. It's just easier in the end.

**David:** Yeah.

**Dave Jones:** They reckon. But you're persevering. I thought, I don't know. It's...

**David:** As soon as I got past that initial, like, two-week hurdle of, like, what the hell is up with Android at the moment. Yep. Like...

**Dave Jones:** So there was a couple of weeks hurdle there, wasn't there, at least.

**David:** Yeah, yeah.

**Dave Jones:** And this is what you work in full-time on it, pretty much.

**David:** Well, no. Was it? So I was doing, like, you know, odd things here and there. Oh, yeah, yeah. You know, about two days a week. So it was about three days a week for... Yep. ...for two weeks. Right. So... But those three days were pretty, like, full-time, maybe a little above. Yep. So...

**Dave Jones:** And then we hit the problem with BLE. Yes. So... What happened on BLE? I didn't... It's better if you explain it.

**David:** So there are... Well, no, hang on. What types of Bluetooth?

**Dave Jones:** Wait, we'll explain that. I... Back when I specified the multimeter, we got the... You know, I want... Yeah, we want to add Bluetooth to it. And the manufacturer went, yeah, sure, we'll add Bluetooth, you know, and we'll just use an off-the-shelf module. I went, great, you know, thumbs up. No problem whatsoever. And they... You know, it came back and they had this... What is it? The BLE 112, the Blue Gigger. And I thought, yeah, I've heard of that. We've even had the BLE guys on the podcast. It's a reputable module. No worries. It's got... Yeah, it's a nice module. It's got great industry support. It's one of the most popular. Not a problem. So we didn't... I didn't give it a second thought. And then...

**David:** The module, per se, wasn't the problem. No. It's the whole technology.

**Dave Jones:** The choice of BLE over Bluetooth 4.

**David:** Yes.

**Dave Jones:** Because Bluetooth 4 is... Bluetooth was originally, I believe, designed to be a serial port replacement. A wireless serial port replacement. And so it has good support for implementing serial ports. Right?

**David:** Yeah, yeah. So BLE... But BLE doesn't. 4.0 has the ability to act just like a COM port.

**Dave Jones:** Yeah.

**David:** But BLE...

**Dave Jones:** Which is what we had in mind for the multimeter. We wanted it to just... So that anyone... So you didn't even need to run an app. You could just have a terminal interface, if you want, and talk to COM port 4, you know, and bingo. There's your data.

**David:** Yeah. But not so much. So it was actually really misleading. So we had this thing called the cable replacement mode.

**Dave Jones:** Yes.

**David:** And you're like, serial cable. Because it does replace a serial cable. Yep. And it acts like a serial port, but it's not supported in, you know... The Bluetooth drivers. No. Yeah.

**Dave Jones:** It's not supported at all.

**David:** And it doesn't... It's not like a plug-and-play, like, COM port. It's...

**Dave Jones:** Yeah. It's not a COM port like you can get on true Bluetooth. No. On Bluetooth 4. So the BLE implementation of a serial port using this cable replacement thing is just not the same. It doesn't implement the same at the driver level.

**David:** No.

**Dave Jones:** At the Windows driver level or the Android driver level or whatever. No.

**David:** BLE is a special snowflake. A special snowflake. I don't know who said that. Someone on the forum, maybe.

**Dave Jones:** Probably. Or I probably mentioned it. Special snowflake. Yeah.

**David:** Each BLE implementation is a special snowflake. Yep. We've got it kind of... It's relatively good now, but, like... Yes. Jeez, we went through...

**Dave Jones:** Oh, it was hell, wasn't it? Yeah. BLE is annoying. So, with hindsight, we wished we had chosen a Bluetooth module instead of BLE. Yes, BLE is lower power, but we've got four AA batteries in this thing. It probably wouldn't have mattered a huge amount anyway.

**David:** And the power... Like, they have the ability to turn off the whole module. Yes. So... Like, it would need to reconnect, but we could, you know...

**Dave Jones:** But it was too far down the track, because it was already at the test house being tested for the federal communications FCC requirements, and you can't just go change your Bluetooth module at the last minute.

**David:** Yes, so BLE it was.

**Dave Jones:** So, we stuck with BLE, but you managed to get it working in the end with multiple devices. We thought multiple devices may not be possible.

**David:** Yeah. So, actually, I thought Android was never going to be possible, because I'm testing on a 4.6 or something, like a...

**Speaker ?:** Yeah.

**David:** An old Android. 4.3, I think. Yeah. An old Android phone. And I thought, like, what the hell's wrong with my code? It's like... It's... There is... Like, you get to a point where you're like, there are no improvements to be made. Even... Like, there are obviously some, but like, no ones that would help it work. Right. I'm like, there's nothing that could block it, you know. Yep. And it just didn't. And as soon as you're connected to a new device, the old connection started behaving like the new one. So, you'd just get echoed.

**Dave Jones:** Oh, echoed data between... Oh, no.

**David:** Yeah, it was stupid.

**Dave Jones:** Oh.

**David:** So, how'd you fix it in the end? So, I moved to another library. Assuming the library was the problem. Right. And... Because usually it is. Yep. And, you know, even though the library I had at the time was buggy, and I assumed, like, you know, that was true for...

**Dave Jones:** And this is just a community library, or just one, some random dude's written on the internet, or what?

**David:** Uh, so, random dude.

**Dave Jones:** Random dude, right. Who's kind of, sort of, the official random dude?

**David:** No, just a random dude. Yeah, he's got a good license and, you know. Right, okay. Yeah.

**Dave Jones:** So, you just chose another library?

**David:** Yeah. And it worked? No.

**Dave Jones:** No. You had to tweak it?

**David:** Uh, no. So, Dave got a new phone. Dave got a new phone. Me?

**Dave Jones:** That's me, Dave. Yeah. Yes.

**David:** And before then, we had nothing really to see how it would behave on a later device. Oh, a later device, yep. So, when the new phone came in, I'm like, oh, can I grab your phone for a moment? Oh, I want to see how it goes. I didn't really expect Bluetooth to work, but I'm like, eh, it might. Might. Right. And it worked straight away.

**Dave Jones:** Wow. We're talking to two... Yep. We're talking to two different meters at once. Yeah. Sweet. So, in theory, there's no limit, right?

**David:** Um, I don't know. It'll probably have some... You haven't pushed it. Right. No, yeah. It'll... Android has some issues with, um...

**Dave Jones:** Does it store it in, like, an 8-bit variable and it's like, and you can only have 256 devices or something, or...

**David:** I don't know. I... Right. I don't know. That's at a... Right. Another layer of abstraction. Yep. Yeah. Got it.

**Dave Jones:** So, anyway, it's working and you wrote it all from scratch. Basically. So, yeah. Trial by fire. Yeah. Yeah. In app, in cross-platform app development. Yeah. It would have been much better if you weren't shooting for cross-platform, right? Um, I don't know. I assume it would have been easier. No, you don't think so?

**David:** I don't know, because then... We would definitely have versioning issues.

**Dave Jones:** Right.

**David:** Um, so I don't think it's been... I don't actually think it's been that bad. I... There was a lot to catch up on Android anyway.

**Dave Jones:** Got it.

**David:** Because it's very, very different the way it is. Yeah. So I would have had to do all that anyway. Um...

**Dave Jones:** So we haven't tried... So I don't know. Right. I don't know. So we haven't tried iPhone at the moment, because neither of us have an iPhone. So we haven't tried...

**David:** No, but all the code on the Android... All the library I'm using for the Android is portable to the...

**Dave Jones:** Right.

**David:** All the code... So it should work. So you're confident. Except for the touchscreen code.

**Dave Jones:** Confidence is high. I repeat. Confidence is high. Yeah, except for... Name the movie. Sorry.

**David:** Not a clue.

**Dave Jones:** Just movie quoting. War games. Sorry. I was right to know that.

**David:** Yeah, right. Dave was quoting it, like... When I first met him, he quoted quite a lot. Did I? Right. Yeah. Okay. And he's like, you've got to watch this movie. So I did.

**Dave Jones:** Yeah, yeah.

**David:** Yeah, I don't remember. Right. No.

**Dave Jones:** Right.

**David:** Yeah.

**Dave Jones:** So what tools did you use? You're using Visual Studio as the main code thingamabob. Yeah, that's the main compiler.

**David:** Yeah, that's the idea I'm working with. It's not the compiler. Oh, right. I use the Mono for Android. Mono compiler for Android and for...

**Dave Jones:** Right.

**David:** For iPhones and for Mac and for Linux, probably. Ah, right.

**Dave Jones:** So I thought Visual Studio could use its compiler, whatever that is, to speak. Mono is made by Microsoft. Oh, it is.

**David:** And a whole bunch of other people. Right. Okay. You know, it's a...

**Dave Jones:** Got it.

**David:** Yeah.

**Dave Jones:** Got it.

**David:** So...

**Dave Jones:** In theory, is it as simple as going, choosing the platforms you want, pressing compile, and they all spit out?

**David:** Yeah.

**Dave Jones:** That's... Yeah. That's the dream. That's the holy grail.

**David:** Yeah, it does that now. So we'll see how it goes with Mac.

**Dave Jones:** Well, we've only tested on Windows and Android at the moment. We haven't tested on Linux yet.

**David:** No. No. Oh, Mac. Well, Linux will be cross-platform, but it requires a recompilation of the OpenGL stuff.

**Dave Jones:** Okay.

**David:** Yeah.

**Dave Jones:** So Linux may be the special snowflake out of them.

**David:** Yes. Linux will be the most annoying.

**Dave Jones:** Okay. Yep.

**David:** There's nothing inherently wrong with it. Right. It's just like... Yep. That's the way it's going to be.

**Dave Jones:** Because we want this to be a desktop and a tablet app and a phone app. Yeah. We want the app to work across any sort of device, any platform.

**David:** Yeah. We've hit 60... What? Windows is... What are they sitting at now? 90? I don't know. I don't know. No idea. So we've hit that. Yeah. And we've got Android, which is the biggest platform for phones. Yep. And we've got... Windows Phone is just a side effect of Windows working. That just happens to be true.

**Dave Jones:** I hate iPhone-only apps.

**David:** Oh.

**Dave Jones:** Oh, it's like... Anyway.

**David:** Yeah.

**Dave Jones:** Somebody actually wrote one this morning. They just emailed me this morning and said, Hey, I've written an e-v-blog app which, you know, sorts all your videos and everything and it's available on iPhone. Do you mind if I release it? No, not a problem. As long as you don't, you know, say it's, you know, approved by me or whatever. You know, I'm not fussed. But yeah, it's iPhone-only. It's like I can't even test it.

**David:** It's like... It's like we wouldn't even know if it was slanderous. Like... No, exactly. It could be horrible.

**Dave Jones:** That's why I don't endorse it. If I haven't tried it.

**David:** It's got open. It... Yeah.

**Dave Jones:** So, Mac's annoying, isn't it? Tell us what you have to do to compile for Mac.

**David:** No, Mac's okay. No, no, but the... Oh, you mean... You mean the... Yes. The hardware dongle. I think... So, the residual, like, rivalry between Microsoft and Apple, like, carries over to app development. To develop for, like, an iPhone, you need to have a Mac.

**Dave Jones:** Yeah. You have to own a Mac.

**David:** Yeah. And it has to be... Like, Visual Studio lets you put it on the network and then it lets it work. Right. But, like...

**Dave Jones:** So, it works like a hardware dongle. It must be present on the network. Otherwise, it won't compile. I think it might compile.

**David:** I think it actually might perform the compilation on the Mac. I'm not really sure. Oh, right. Okay. It kind of happens automatically, but, like... Got it. Yeah. That's a... It doesn't work until you have one on the network. Yeah.

**Dave Jones:** Although, we're going to try a virtual cloud solution, aren't we? Isn't it? Like, virtual Mac or something? Some sort of cloud.

**David:** Virtual Mac.

**Dave Jones:** Where you can rent, like, a Macintosh on the cloud for, like, a couple of bucks. Yeah. So bizarre.

**David:** Like...

**Dave Jones:** Just to solve this particular problem, right?

**David:** Someone's made a whole business out of...

**Dave Jones:** A business out of...

**David:** Out of this arbitrary, like...

**Dave Jones:** Yeah, yeah.

**David:** Restriction.

**Dave Jones:** And they probably make a great living from it. Yeah. Good on them. Yeah. Anyway, so that's... Yes. Let that be a lesson to you. I think we've mentioned this on the... I've talked about it before on the Amp Hour. Yes. Bluetooth instead of BLE. Yeah. BLE is great if you're running something from a coin cell and a... You know. You know, that you want to work for two years off a CR2032 or something. But, yeah.

**David:** Yeah, the...

**Dave Jones:** Bluetooth is better. Isn't there Bluetooth 5 coming out or something?

**David:** Is there?

**Dave Jones:** Ah, somebody mumbled something to me. Yeah.

**David:** What was that?

**Dave Jones:** That... Somebody, I think, on Twitter, I mentioned...

**David:** I feel like I might have said that.

**Dave Jones:** Yeah, you might have said it or something. And I don't even... And it will solve the problems between BLE and Bluetooth 4 or something, apparently.

**David:** Oh, it better.

**Dave Jones:** Bluetooth 5 explained on YouTube. There you go. Somebody's already done it.

**David:** It's totally a thing. Yeah. It is totally a thing. In the S8 galaxy.

**Dave Jones:** Oh, right. Okay. Promises twice the data transfer. Oh, I don't care about that. I just want shit to work as a serial... Like, you know, this latest, like, Galaxy 8 phone or whatever, and I still just want a bloody serial port. Just give me a serial port. Like... Oh, man. Yep. 300 board. I'd be happy, you know. 8 in 1, you know.

**David:** Enough to just turn an LED on.

**Dave Jones:** Yeah, exactly. No, no.

**David:** 300 LEDs on, right? Every second or whatever. It's word speed or whatever, yeah.

**Dave Jones:** Anyway. Yeah, so if people don't know, you work at the EEV blog full-time now. I do, yeah. You, like, turned down, like, a real job and everything to work at this...

**Speaker ?:** Yeah, too.

**Dave Jones:** To work at this... Work in this hole. Yeah. Well, at least I've got a window here. It's a real job. I'm doing it. It's a real job. He's doing shit. Doing the hardware stuff and some software stuff.

**Dave Jones:** And, yeah. You will get back onto projects, you know. Yeah. Because that's the idea, because I can't pay you to just make content.

**David:** No.

**Dave Jones:** Right? Because that doesn't, you know... Like, if people don't know... I've done videos on this. Like, even, like, a popular video might bring in $100 to $200 in ad revenue, right? You know, if it gets 100,000 views or whatever, yeah. You know, $150, $200 maybe. Yeah, and how long do those take you? And, yeah, exactly. Like, you can't pay somebody, like, you know. Yeah. Even if you're working at slave labor wages, it still wouldn't.

**David:** Well, our minimum wage, what is it, like, $21.50? So, $200 in 10 hours. You know, 20 bucks. Yeah, I know. To make a bit, like...

**Dave Jones:** 10 hours. Yeah. It just doesn't really pay to make content. So, the whole idea is to make projects. Yeah. So, unfortunately, there's, you know, things like the multimeter. A multimeter's a project, but it's just software. Yeah. At the moment, you're just working on software. Either you've been doing some hardware testing and stuff, but... Yeah.

**David:** I guess I'm as much of a software guy as a hardware guy. Yeah. Yes, you are. I'm happy to do.

**Dave Jones:** Yep.

**David:** Yeah.

**Dave Jones:** Yep. Can we talk about your new product coming out? Yeah. Is that not a thing? No, you can talk about it. Yeah. Well, I don't want to talk... I don't know anything about it. It's just a cute little board that he keeps waving around in my face going, look at this, look at this.

**David:** Yeah. So, over the last, like, I don't know how long, because ages, I've been working on a little product, and it's got... It's basically a data acquisition device.

**Dave Jones:** The size of a credit card?

**David:** Yeah. Yeah, yeah.

**Dave Jones:** It's the exact size of a credit card? That's what you're shooting for?

**David:** The actual board's smaller, but it's got a credit card. A case.

**Dave Jones:** A case, which is the size of a credit card?

**David:** Yeah.

**Dave Jones:** And literally the exact millimeter to millimeter dimensions?

**David:** Yeah, I think so, but they're not... How thick is it? They change country to country, though. Oh, right. Oh, do they? The business card sizes, yeah. Oh, credit cards change sizes. I had to decide.

**Dave Jones:** Oh, right. Did you choose the Australian one or what?

**David:** No, I picked the one that was the cleanest...

**Dave Jones:** ISO standard or something?

**David:** Anything with a decimal point. I was like, not that one.

**Dave Jones:** Right, not that one. Okay, yeah, yeah, yeah.

**David:** Because I like to be able to divide by two for a while.

**Dave Jones:** That's it, right, of course. Yeah. Good man.

**David:** Yeah.

**Dave Jones:** All right. So how... What's the thickness?

**David:** It's not the thickness of a credit card. No. Like all these things are like the size of a credit card. They're not. They're not. They're not the volume of a credit card. They're the footprint of a credit card.

**Dave Jones:** Yes, correct.

**David:** Yeah. So it's about... What was it? Like 18 millimeters, I think?

**Dave Jones:** Oh, that's... Yeah, that's pretty chunky.

**David:** Yeah, it's a chunky credit card. It's not something you put in your wallet. Yep.

**Dave Jones:** So it's a data acquisition thing designed primarily for the educational market?

**David:** And yeah, for academics, people doing robotics. Yeah.

**Dave Jones:** So not... Because it's high priced. It's not designed for the hobbyist, right?

**David:** Yeah. It's basically the device that... You know, academics can't afford to have a whole bunch of test equipment on their table. Right. Yeah. And they don't necessarily need, you know, standards class instruments.

**Dave Jones:** They just need acquisition. And that's why the NI Virtual Bench, the National Instruments Virtual... It's like $5,000. Yes. We've got it over there. Yeah, yeah, yeah. That's right. But it's got everything built into the one box. It's all the things. It sits on the desk.

**David:** Yeah. And it's actually... If you were to buy the things it has, it's a lot cheaper. Yep. You know, like, that's the logical, you know, oh, the NI thing. That's pretty good.

**Speaker ?:** Hmm.

**David:** But this is, you know, it's somewhat cheaper again. Yep. With... I think it's actually pretty similar specs. Oh, okay. Cool. In terms of acquisition stuff. But I got nothing compared to the... Right. Their software support is what you pay for.

**Dave Jones:** That's... I was going to say, that is... Like, the hardware almost doesn't matter. It's what's in the software... Yeah. ...that matters. And the educational material that goes behind it. So that's why a lot of companies like, you know, tech and, I was going to say Agilent, Keysight, put, you know, when they sell educational scopes, they don't just sell a scope at a cheap price. They sell their whole classroom learning kit that goes along with it. Yeah. Which is all the material, all the teaching material and everything else. Yeah. So the teachers just go, material. I can just give it to the... I don't have to write it. I can just give it to the students. Fantastic. My job done. I'll pay. Any cost you like for that, right? I mean, you've taught, right? Yeah. So, you know. Yeah.

**David:** So, you know, and that's... It's... The actual volume of these instruments, though, is also a problem. Right. So that doesn't solve that problem. Right. It's still pretty large for a hot desk.

**Dave Jones:** Right. Okay.

**David:** So a lot of universities, they're actually moving towards hot desks.

**Dave Jones:** Ah, interesting. Which, you know, now... For students.

**David:** For academics.

**Dave Jones:** Oh, for the academics. Okay. Right.

**David:** Which is really tough for a guy who needs tests. Yeah, yeah. Yeah, exactly. It's basically impossible. Wow. So, you know...

**Dave Jones:** Is this like a thing or is it just that you're unique as you're running out of space? But you've got your new... We've got 10 buildings or something. I know, exactly.

**David:** And there's a new building going up every year or something. Yeah, yeah, yeah. Like a large building.

**Speaker ?:** No.

**Dave Jones:** So it's not...

**David:** It's just a thing.

**Dave Jones:** It's a thing.

**David:** Yeah.

**Dave Jones:** It's a new philosophy thing. Just like open plan work... Like open plan work stations were a thing in the 90s.

**David:** Yeah, people convinced themselves it was a good idea. And it was the right thing by everyone without any real... Yeah, got it. Yeah.

**Dave Jones:** Without any real feedback from people.

**David:** No. Right. Nothing. Right. It was designed by a committee. I don't even know if it was. Like maybe that would have turned out better.

**Dave Jones:** Right. No, nothing. Generally nothing designed by a committee. It turns out well. Everyone knows that. Anyway, so yeah, hot desking. Wow. So you can pick up all your crap at the end of the day. Hence why you're a Microsoft Surface tablet thing. Hence why... Yeah. Because like it's a tiny form factor and you just pick it up and go. Yeah.

**David:** Yeah. I actually did have an office. I was one of the lucky people who got an office. But same thing applies. I was a student. I had to work wherever I was.

**Dave Jones:** Didn't you have an office next to the Woz?

**David:** Yeah. No, where he was going to be allocated. Where he was going to be allocated. He never turned up. He never turned up. I never saw him.

**Dave Jones:** He was an adjunct professor at the University of Technology. He probably still is. I don't know. He probably still is. But you've never seen him.

**David:** No. I was really excited.

**Dave Jones:** Yeah, right.

**David:** I was like...

**Dave Jones:** Yeah, the Woz is next to me. Yeah. Yep. Cool. Maybe share a hot desk with the Woz.

**David:** No, he would definitely get an office.

**David:** He would get an office. He'd probably take my old office.

**Dave Jones:** Right.

**David:** It's like free now.

**Dave Jones:** Boot out this young whippersnapper.

**David:** Give it to an adjunct.

**Dave Jones:** Yeah. What is an adjunct professor?

**David:** I think it's one that isn't...

**Dave Jones:** Is it a very loosey-goosey definition?

**David:** Yeah, probably. All right. I think it means that they're not like a permanent staff.

**Dave Jones:** Yes.

**David:** They're like a professor, but...

**Dave Jones:** They just come and go as they...

**David:** It's like an honorary professor.

**Dave Jones:** Right.

**David:** That, you know, might come and...

**Dave Jones:** Yeah, come and... Might come occasionally and give a talk or give a lecture or whatnot.

**David:** Yeah. I'm not really sure. Adjunct professor...

**Dave Jones:** We're doing advanced stuff. Google in here, folks. Nope.

**David:** Don't know.

**Dave Jones:** Don't know.

**David:** That didn't help. Too hard. Yeah. Whatever. Yeah.

**Dave Jones:** So you didn't want to stay in academia? You wanted to get out into the real world? Because you had a pretty cushy job there. I did. It was great. It was cushy, but also you were like a one-man band too, weren't you?

**Speaker ?:** Yeah.

**David:** Yeah. Yeah, it was a great job. But, you know, like... I have nothing against being academic. You know, I'd be totally open to doing that at some point. But I think people should be not an academic before they teach.

**Dave Jones:** Right. Yes. Before they, like...

**Dave Jones:** It should be compulsory, I think.

**David:** Yeah. Yeah. And I would enforce that philosophy on myself. Right. Okay.

**Dave Jones:** Get out in the real world. Yeah. Not that the EV blog's a real world. But you have worked in the real world before. You have had a job before. Yeah. Yeah. Yeah. Yeah. Yep. And that was at a design house. Yeah.

**David:** Yeah. That was in Chatswood at the time.

**Dave Jones:** Right. Is that a...

**David:** It was actually where the other offer was.

**Dave Jones:** Oh, right. Yeah. Yes. That's right. Yeah. Do they... So you turned down a design house to come here. Yeah.

**David:** Is it... Great. That was a great job too. Oh, right. Really great people.

**Dave Jones:** Is it the stereotype of what I've heard of that they work your ass off? Oh, yeah. And the deadlines are ridiculous.

**David:** Yeah. Yeah. Yeah. Yeah. Definitely.

**Dave Jones:** So if you're not into stress... Yeah. Like, if you don't thrive on stress, don't work for a design house.

**David:** No. No. No.

**Dave Jones:** Is it because they promise ridiculous deadlines to the customer without asking the real engineers first? No.

**David:** That place was quite good about that. Right. Okay. You know, their deadlines were, I think, you know, pretty close to reasonable. Okay.

**Dave Jones:** So who would make the decision on the deadline? Would it be the poor schmuck who's got to do the job?

**David:** It was the CEO. Oh, right. Okay. But as far as I could, I was aware.

**Dave Jones:** But they usually have vast experience.

**David:** The CEO there is actually quite, you know, a decent design engineer themselves. Yeah. Yeah. Right. So, you know. Yeah. Yeah.

**Dave Jones:** They probably, most likely started the design house. It was just them. Yeah. Yeah. So, right. So they're so used to doing that. Yeah.

**David:** It was, if I remember right, it was them and, like, a youngster from UNSW. Right. Who ended up working there for, like, five years or something. And then he's.

**Dave Jones:** And then burnout.

**David:** Then they started their own business. Right. Okay. And now they think they're touring Europe or something. Oh, right. Yeah.

**Dave Jones:** Academia. So, it's not as bad as it sounds. Especially if you get tenure, right? That's what everyone's after.

**David:** Yeah. Yeah. I kind of like the idea. You kind of like the idea of a job for life. No, no. I like the opposite. Like, tenure is, like, you know, there's no pressure to achieve. I need a little bit of pressure. Right. Okay. Like, most people do. Yeah. You just need, like, just something.

**Dave Jones:** Well, we've mentioned this on The Amp Hour a million times. Fewer cushy is hard to. Engineers work. Engineers thrive on deadlines. We always make deadlines. Yeah. We're just brilliant at doing it somehow. Yeah. And that's what makes us an engineer instead of an academic, really. Yeah. We're given a project. Yeah.

**David:** Like, our second question after getting specs is, like, when do you need it?

**Dave Jones:** Yeah. Yeah. Yeah. Right. Yeah. All right. So, yes, he turned out a real job to work here. Thanks, folks. And anyway, let's go through some of the, we've got some random Reddit stuff, don't we? So, we'll just crap on about what's happening in the business. What was the, yes, Qualcomm. Yeah. I'm pretty sure we talked about this on the blog a few months back. The blog.

**David:** So, Qualcomm were acquiring NXP. I think it was through a shares kind of thing.

**Dave Jones:** Yeah.

**David:** Or some weird share buying thing. Yep. But it looks a bit sketchy at the moment because the European Commission are kind of investigating, I think, Qualcomm.

**Dave Jones:** So, is that why it's, or is it because it's the money, or a money situation, or is it just because of a legal investigation kind of thing?

**David:** Well, apparently the shareholders, it's two things. So, apparently the shareholders are looking for a higher value. Because they were like, that was not high enough.

**Dave Jones:** Right. Like, the...

**David:** NXP is pretty substantial. Oh, yeah. And, you know, Freescale, I think they own now. Yeah. They are Freescale now, too. So... What was the value?

**Dave Jones:** What was the... I don't know. You know, like 30 billion or something? I don't know. It's pretty hard. And I'm sure it would have been here. I'm sure it's not a couple of billion. Jeez, I'd buy it at a couple of billion.

**David:** Would you? Yeah. Yeah. I'll just...

**Dave Jones:** Go and get the money on Kickstarter. Yeah. Yeah, right.

**David:** What would that be as an investment for every one of your viewers? It wouldn't even be that... It would not be small.

**Dave Jones:** That would be hilarious if there was a tiny manufacturer somewhere and someone started a crowdfunding campaign to try and save them, you know?

**David:** Yeah. Yeah, so... Anyway.

**Dave Jones:** So, it may not go through.

**David:** No.

**Dave Jones:** It may be blocked or it may just fall through financially.

**David:** Like, it's probably just a big delay.

**Dave Jones:** Right, okay.

**David:** It's probably going to still happen, which... I think the people with the money always win. I really like NXP, so I hope they still stick to what they're doing. Right, yeah. And, you know, acquisitions can do whatever to a company. Yep. Like, where's FreeScale right now?

**Dave Jones:** I don't know.

**David:** NXP ate them.

**Dave Jones:** Like... There's been... Like, we could... Literally could not keep up on the amp hour. Every week we were doing a... At one point, doing a... You know, some companies bought another. And it was just... It was impossible. Somebody did a map. We posted a map once of it. Somebody actually tried to document who bought who. And it was just... Wow.

**David:** Is it monopolizing or enough? New groups coming in to stop that.

**Dave Jones:** It didn't look that... I don't think the... It didn't look that monopolistic to me. But every time you heard it, it felt like it was monopolistic. But it... I don't... I think the reality was less than you thought it was. So... Anyway.

**David:** On the note of monopolies. Yeah. Samsung has just surpassed Intel.

**Dave Jones:** Oh, it's the world's number one chip maker. That's right. It must be because Intel got out of the Internet of Things market. And they just collapsed. That was such a huge... It was such a huge market for them. It was a huge market for them.

**David:** It was a passion decision, not an economic one. Right. Totally. No.

**Dave Jones:** Just in sheer sales volume, right? It's sheer numbers, right? So it's not like money numbers. Yeah. So it's not volume or anything.

**David:** Like... I think it might be both. It might be both. Okay. Because... So their operating profit is $7.1 billion and the whole market's worth like $365 billion.

**Dave Jones:** Yeah.

**David:** Which is a pretty big market. So... I don't know. Has the market increased?

**Dave Jones:** Have they got like a pie chart of where Samsung get most of their money from? Like I... Like is it from... Is it from the memory? Is it... Or is that a...

**David:** Samsung have tentacles in everything.

**Dave Jones:** They have everything.

**David:** I think they have like even...

**Dave Jones:** Yep.

**David:** I'm pretty sure there's a mining like group.

**Dave Jones:** Samsung mining.

**David:** Yeah. Let me just fact check myself. Samsung mining for... Ad blocked.

**Dave Jones:** It reminds me when Daewoo got into computers. I actually had a Daewoo computer. Hands up if you remember Daewoo. Like the big engineering... The big Korean. I think they were South Korean, weren't they? Yeah. I think... Yeah. And they were a big mining, you know, industrial company and they got into computers and then, you know, like... Yeah.

**David:** Well, you know, Daewoo were relatively large. Yep. But Samsung are 17% of South Korea's GDP. Yes. Yes.

**Dave Jones:** It's like... Yeah. It practically is South Korea.

**David:** Yeah. 17% of it. Yeah. The GDP at least. That's...

**Dave Jones:** That's enormous.

**David:** What's 20% is it? I'm getting mixed numbers here.

**Dave Jones:** No one would even come close in any other country.

**David:** Sure. As a percentage of GDP, I would think so.

**Dave Jones:** I...

**David:** Like... Oh, there's a... Oh, what was that? There's this... That Indian group. They make cars. They make...

**Dave Jones:** Oh, Tata or... Yeah, yeah. Is it Tata? Tata. Yeah. Tata. I went to the... I was in the Tata... Well, it wasn't the factory. It was like the Tata warehouse in the UK once. This was like... Tata movies. 17 years ago or something. Yeah. And... Oh, God. They were bad. Really? Those Tata's. Oh, my goodness. You have no idea. I'm going to try and find the largest US company.

**David:** Well, that... Isn't that Google? That's Alphabet. Oh, yeah. Of... That's Alphabet. Are they a trillion yet? Are they worth... I think they might be really close at this point.

**Dave Jones:** I don't know. Economy of the United States. No, I don't know. We could... 25 mega... US mega corporations.

**David:** So, Alphabet's currently...

**Dave Jones:** Has it got a percent of GDP? You would have to know what the GDP is and then calculate the percentage yourself, I'm sure. So, yep. Apparently, General Electric is the size of New Zealand in terms of GDP.

**David:** Wow.

**Dave Jones:** Yeah.

**David:** Yahoo's bigger than... I wonder if they're still bigger than Mongolia. Yahoo's bigger than Mongolia's GDP, apparently.

**Dave Jones:** And Walmart. If Walmart were a country, its revenues would make it on par with the GDP of the 25th largest economy in the world. Wow.

**David:** Well, what's Australia?

**Dave Jones:** I don't know, but we're bigger than New Zealand, I'm sure. Yeah, yeah.

**David:** Much.

**Dave Jones:** Mongolia's GDP. So, Yahoo are worth more, have more revenue than Mongolia.

**David:** That's really surprising.

**Dave Jones:** What? Where do Yahoo make their money? Nobody uses Yahoo.

**David:** Is Yahoo Answers still a thing?

**Dave Jones:** I don't know. Like, I still use Flickr. Or did they sell off Flickr? No, they turned it into a pay-only thing or something.

**David:** Is Tumblr a profitable thing? I don't know. That's Yahoo, right?

**Dave Jones:** But, yeah, I don't know. Yahoo is... I don't understand how Yahoo have ever made money. It's just... Yeah. I don't get it. Anyway, we could go through one of these infographic... Visa's bigger than Zimbabwe. Okay. Now we're getting into one of these, you know... eBay's bigger than Madagascar. Yeah, okay.

**David:** Amazon's the up-and-comer at the moment, I think.

**Dave Jones:** Oh, yes.

**David:** Jeff Bezos is now the richest dude in the world. I think that only lasted 10 days.

**Dave Jones:** Oh, did it? Okay. Yeah.

**David:** I don't know who... I think probably Bill Gates again.

**Dave Jones:** Yeah, but Bill Gates gave away $30 billion last year. Yeah. Is Bezos doing that stuff? I know. Well, he's funneling money into his rocket company, but apart from that... Yeah. Who's Con Anderson? Never heard of him.

**David:** Hmm. Hmm.

**Dave Jones:** Yeah. Anyway... No, Amazon.com is bigger than Kenya. $32 billion. $34 billion. Oh, man. There you go. So it's not as big as you think, but anyway. Hmm.

**David:** Yeah. So what do we have?

**Dave Jones:** No. Okay, this is Apple's bigger than... Apple's bigger than Ecuador, and Microsoft is bigger than Croatia. There you go.

**David:** Wow.

**Dave Jones:** Yeah. Costco is bigger than somebody else.

**David:** Sedan.

**Dave Jones:** Sedan. Wow. Wells Fargo, Angola. Oh, jeez. Wow. Speaking of Angola, I had the option to go to Angola at a former company I worked at.

**David:** Really? What were they doing there?

**Dave Jones:** I said, hey, Dave, do you want to... Oh, oil, you know, because I worked at an oil surveying company. Right, right, right. And Angola's an oil hotspot, you know. And Dave, do you want to go to Angola? It's, you know, it's completely safe. You'll have an armed guard the whole time. No thanks.

**David:** Yeah, like, does that make you feel less or more safe?

**Dave Jones:** Yeah, I know.

**David:** Is the armed guard safe? Yes, exactly. Do I have a guard guard?

**Dave Jones:** Have they paid that guard enough? Or will he determine that he can get more for ranciting me off than what he got paid by the company? Right. Does that happen? That happens. That would be... That actually does. What a trap. It does happen, yeah. Anyway, we're not here to talk countries and politics, are we?

**David:** I think, like, what was Freescale? So, back to, like, NXP stuff. So, NXP, that was, like, a 30-something billion deal. And Freescale was, like, 17 of that. Something. Or something. I don't know. Those Freescale... Freescale are pretty huge. Yeah.

**Dave Jones:** Still are. Are they still the number one? They were the number one. For automotives. Microcontroller manufacturer in the world because of the automotive market.

**David:** Yeah. Yes. I don't know if they still are. Yeah. And I don't know if they're now all NXP umbrella-ed.

**Dave Jones:** I don't know.

**David:** Yeah.

**Dave Jones:** I haven't followed. I just gave up trying. And in other news... Straight off the teletype. The Arduino war is over. We've talked about this before. How it was a battle of the two competing founders of Arduino. One, Federico Musto, who owned the trademark. And he owned the company Arduino AG, which owned the trademark. And then there's Massimo Banzi, who's the most well-known. He's the face and the, you know, generally considered the, you know, the founder of the Arduino thing. He was the chairman and CEO of Arduino, but not Arduino AG, which held the trademark. Anyway, they were supposed to form this corporation that merged the two together. And everyone got up in arms about it. And he's, apparently, Federico Musto has been bought out. So now, Hasimo Banzi owns 100% of Arduino AG, or him and his company own 100% of Arduino AG, and interned the trademark. So Federico Musto is Gonski. Wow. And a lot of people will say, well, don't let the door hit your ass on the way out. And let's, I don't know. Shouldn't really go any further. It's over. It's all done and dusted. So I'm not sure where the money came from. I'm not sure how much they paid him, or whether or not they've made offers to him in the past. I would presume they have back when, because these two companies were filing trademark lawsuits against each other. And they were battling that out for like a year or something. And, anyway, it's all done and dusted. Finally. Banzo beat Musto. It's all over. So, yep. Musto's gone.

**David:** Is this good or bad? I don't know.

**Dave Jones:** Most, you ask almost anyone, they'll say it's good. Because I don't know too many people who liked Musto. He just wasn't the, yeah. It's like, you know, he falsified his credentials and claimed he graduated from MIT, was it? I think. And, like, he didn't.

**David:** Wow. Can you just do that? You just claim you graduated from wherever.

**Dave Jones:** He's graduated from wherever. Wow. Anyway. How did he?

**David:** Wow.

**Dave Jones:** Anyway, there were a lot of people who didn't like that and didn't trust him. So, anyway, he's gone. He's gone. So, yep, it's all over. They all own the trademarks now. But, like, I don't know. So, I don't, like, will people go back to, there's a lot of people who did not support Arduino on principle because of the war and all that sort of stuff. Now that there's over, will people go back and become loyal and buy Arduino hardware again? I don't know. I won't. Right? No. Well. No. There's just, because there's so many clones out there that are cheaper. So, they have to make their money somewhere else, because it's probably not going to be in the hardware.

**David:** Do you think Arduino is still going to continue to expand? I think it's on the tail end of its...

**Dave Jones:** The software platform, yes, because the software platform is brilliant. Yes. Arduino practically has nothing to do with the hardware anymore. As the hardware platform. The hardware, it doesn't matter. It's the software platform that matters, and the software platform is brilliant.

**David:** Do you think the hardware platform is going to mean anything in five years?

**Dave Jones:** No, it won't, because people can write their own plug-ins for their own Arduino-compatible board for the Arduino environment. That's what Intel done and all those companies. They wrote the... I don't know. Is it called a plug-in? I don't know what the technical term is. But, yeah, you integrate it with the Arduino environment, and then, yes, the board... Arduino then has support for that board. Yeah. And it just handles everything in the background. All the compilers, all the nasty stuff just magically is taken care of for you.

**David:** How do you feel about those, like, there's the PC-combined Arduinos, so you get these little Raspberry Pi things with an integrated Arduino. I think... Doesn't that seem a bit redundant?

**Dave Jones:** It seems a bit redundant. That's the Latte Panda has that. It's not only that. There was another one. No, no. Yeah, there's other ones. Yeah. In fact, the Intel Atom has that. The Intel ones had that, didn't they? They had an Intel Atom plus an Arduino plus an AVR core in them or something? Or was that running in FPGA or something? I don't... Can't remember the exact details, but... Yeah, it seems... Well... It seems redundant. Like, from...

**David:** Because if they can write just any plug-in and then support the language... Like, they have their own little compiler back-end.

**Dave Jones:** Yeah, but you can't... Like, you can't, because the Arduino environment's designed for lower-level stuff. Like, it's not like you're going to be able to do this huge GUI interface using the Arduino environment. It's just... There might be the odd thing out there.

**David:** It's only for AVRs, though, right?

**Dave Jones:** No, no, no. It's for any platform.

**David:** Really?

**Dave Jones:** Yeah. Now, it's... Yeah, it started out as AVR, because that's Arduino when they made the first board. It was an AVR. It was an AVR. But then people decided, oh, we don't have to use an AVR if we just... ...integrate the compiler hidden behind the GUI interface. It doesn't matter. So then people started using PICs in there. Yeah. And then they started using ARMS.

**David:** There are PIC Arduinos.

**Dave Jones:** There are PIC Arduinos. Wow. It's called the PICduino, I think. There are PIC Arduinos. How do these things happen? I think that was one of the first. Wow. It was like, you know, somebody decided, I like the PIC32. So therefore, you know, the chip. What is it?

**David:** Oh, the thing called a chip.

**Dave Jones:** No, no. It's called the chip. Is it the chip? Do we know? What's the... Oh, who's the company? You know, you make all those educational kits. They do the... No. I'm talking out my arse. I should try and find it. Anyway, yeah, there's PIC1s and there's ARMS and there's other processors and stuff like that. So, ChipKit, ChipKit, if you search for ChipKit, it's the... Yes, that was the ChipKit. Oh, ChipKit.net now. Oh, anyway. Discontinue by Digilent, is it? No. It was from Digilent. No, no. They still make it. They've just got their own website now. And it's an Arduino clone which uses the PIC32 processor.

**David:** I never understood Arduino. You know, like, I guess I was too early to the bandwagon because, you know, like, I guess a lot of the old, like, the people who, you know, programmed on PICs and...

**Dave Jones:** Yeah, but it's not aimed at guys like you and me. Like, it's not...

**David:** Yeah, I know. Yeah, it's not at all.

**Dave Jones:** It's not aimed at us. I mean, who can write low-level microcode? No. It's just, you know, and figure out compilers and stuff like that. But, I don't know, but it's something to be said for just being able to, you know, use the write function or write to a pin and specify the pin. You don't have to set it up. You don't have to, you know...

**David:** It's true. A lot of the, like, the launchpad libraries, they do the same thing. Oh, yeah.

**Dave Jones:** No, there's nothing unique about... People think Arduino changed the world with this thing. Maybe, well, you could argue they did because it became popular, but they weren't the first.

**David:** Yeah, it was like the Apple of little microcontroller development boards.

**Dave Jones:** They were around since you were itching your daddy's pants. Yeah, they made them... ...being around.

**David:** They popularized it.

**Dave Jones:** They popularized it, yes. I mean, it's a fine platform, but like... Yep. No, and they rode the coattails of the open source and vice versa of the open source hardware movement. And once again, there's nothing new about open source hardware. No. In quote marks, you know, it's been around since day dot. Yeah.

**David:** Might not have been called that.

**Dave Jones:** No, no, it wasn't called that, right?

**David:** But the designs were freely available. Exactly. And everyone had them.

**Dave Jones:** And everyone had them. And, you know, and you could do anything you want with them and nobody complained. And, you know, and you're happy to reuse it and all that sort of jazz. Yeah. It just got more formal and structured and licensed and all that sort of stuff with the open source licenses. And yeah. So, anyway, the Arduino wall's over so we don't have to... Last time we'll talk about that. Yes. Anyway, still a great platform. Right. What else have we got?

**David:** Well, let's have a look.

**Dave Jones:** There's a self-balancing robot kit. You've been yapping on to me about...

**David:** I've made lots of these. These are great.

**Dave Jones:** These self-balancing robots. You said, oh, I can... Like, we'll just do a video in like 10 minutes of doing a...

**David:** I didn't say 10 minutes.

**Dave Jones:** Oh, well, you were pointing towards...

**David:** I reckon it would take about a day. Right. 3D printer, about a day.

**Dave Jones:** It always takes long. He's a young whippersnapper.

**David:** I'm an optimist.

**Dave Jones:** He's an optimist. It's a chronic disease. Yes, it's chronic... It'll take a day and I just roll my eyes every time he says it, you know. And, yeah. Yeah, a little self-balancing robot kit. Yeah, every maintenance dog's doing those. They're fun.

**David:** Self-balancing stuff's great. Yeah. It's one of the best platforms for control theory stuff.

**Dave Jones:** Oh, yeah. Yeah.

**David:** It's very, like... For sure. Past the linear region, which is just balancing right at the top when it's basically perfectly upright. It becomes really hairy. The algorithm... The maps behind the control... Like, the control theory becomes quite hairy. And, in fact, even, like, academic papers about this...

**Dave Jones:** Yeah.

**David:** They end up simplifying the model, for the most part, to a point where it's, like, basically unrecognizable.

**Dave Jones:** Right.

**David:** Beyond the point of stability. So, like... So, I always thought, like, when I read these, I'm like, why are you putting all this effort into this algorithm where you've just removed the second most significant part when it's unstable? Aren't you controlling it for instability?

**Dave Jones:** Right.

**David:** Like...

**Dave Jones:** Yep, yep.

**David:** So, you'll often see these things. If you push them, like, quite fast, they don't only, like... They don't just overcorrect. They totally flip out.

**Dave Jones:** Right.

**David:** Or, like, basically nothing because they don't have the response time. Yes, yes, exactly. Yeah.

**Dave Jones:** Well, the classic project is not a balancing robot. It's the ball-on-beam balancer. Yeah, and that's... That's, like, been going around for 50 years or something.

**David:** It's a substantially more simple mathematical model. I think it's, like, 7 on S squared is the whole model. Right. And that is a simplification. But that's okay because you never move it past, like, 10 degrees. Got it. And for anyone who's listening, like, if you don't move a sinusoid, it's basically a straight line, like a linear one, a line of gradient one across the X and Y intercept, the middle bit. Yep. And that's, like, a sine wave. Sine wave does the same thing. And so, you can just take this, like, approximation where a sine is a straight line. Yeah, yeah, right.

**Dave Jones:** At that point. Yeah.

**David:** It's from the series approximation. Right. So, if you look at the... Yes. ...the bloody series name. Taylor series or whatever.

**Dave Jones:** I was going to say Taylor series, yes. I think it's a Taylor series, isn't it? You're math boy. Come on. You're supposed to be math boy. I don't remember nouns good. He does actually have a genuine problem with nouns. It's, like, weird.

**David:** It's weird. Yeah.

**Dave Jones:** He's, like, completely weirdo.

**David:** Yeah, so you can represent... I'd be talking about... In a sine wave.

**Dave Jones:** You can represent... You can do it with the Taylor series.

**David:** Yeah. Right. Yeah, yeah, yeah. The McLaren series.

**Dave Jones:** Oh, there you go. Yeah. All right.

**David:** Sounds fast. Yeah.

**Dave Jones:** Anyway, yes, the ball on beam balancer. That just reminds me of Bob P's rip. Rip rap. People will get that rip rap.

**David:** Is it like rep rap, but rip rap? Rap.

**Dave Jones:** Robert A. P's.

**David:** What?

**Dave Jones:** He called him... Yeah, rap. That was his... He always signed his articles with rap at the end. Rap. Anyway. That was initial. So... And rip. Rest in peace. Bob P's. Anyway, yeah, he did a famous couple of articles on the ball on beam balancer, and he solved it using an analogue system, because he's an analogue guru, right, with a grey beard, and he stroked his beard and came up with a schematic and...

**David:** Yeah, you look at his schematic here. Dave's got it on the screen. And it's basically a... It's an integrator, a differentiator, just with an adder, basically. It's tuned to...

**Dave Jones:** If you can figure out Bob P's' schematics, they're famously... Um, what's the word?

**David:** Well, this is the proportional...

**Dave Jones:** I'm trying to look at the... You know...

**David:** So, when you have a differentiator like this, and they have this divider going into, like, a relatively...

**Dave Jones:** No one can see you pointing at the screen.

**David:** Oh, that is true.

**Dave Jones:** He thinks he's doing a screen capture tutorial.

**David:** This is going to go... This is... Yep. Sorry, listeners.

**Dave Jones:** Yep. Anyway, rap has labelled this. I'll put the photo up in the show notes. Anyway, yes, it is a differentiator circuit, and there's a derivative path feedback. There's two derivative paths. And, uh... Yes. Anyway, and then there's a servo system, which drives all that and feeds back in multiple weird and wonderful ways. And he tweaked his grey beard, and this is apparently the duck's gut's ball on beam balancer. None of that software rubbish.

**David:** Well, the software stuff can do the same thing.

**Dave Jones:** Yeah.

**David:** Software, that's bullshit. Yeah, that's cheating. In some ways, it can be kind of better.

**Dave Jones:** Nah.

**David:** Because you can't... There's certain things you can't do. I think it's called a... I think it's called a bang-bang controller, actually. But that's... You can have your simplified control model of something broken into different sections of a control model. So, you know, it's not just the straight line. Now you're approximating... What is this?

**Dave Jones:** I don't know. We're looking at some girl group video. What are you Googling there, David?

**David:** I'm trying to... Yeah, it's a bang-bang control. So you can basically swap between...

**Dave Jones:** Don't Google bang-bang, folks. Let's go.

**David:** Yeah, that was a... Had a bit of a moment. Right. Dave's freaking out. Like, what's on the screen? I'm not even looking.

**Dave Jones:** Like trying to Google stripper. You know, I need a pair of wire strippers, you know? Like... Yeah. Anyway. Yeah. Bang-bang control. There's a Wikipedia... Of course there's a Wikipedia page for bang-bang control.

**David:** It's basically one of the most simple control algorithms in existence. But it basically means you just swap between control algorithms or just turn it off and on with hysteresis.

**Dave Jones:** Right.

**David:** Which is the typical one.

**Dave Jones:** Kind of the... That's the... That's the Heath Robinson approach, is it? To bang-bang control.

**David:** Yeah. They're like very, very simple. But, you know, like that's super, super simple and fast to do in software. But it's... You know, you need like comparators and, you know, you need like... Right. Analog muxes to do that kind of thing. Right. It's much simpler in software. Got it. Yeah.

**Dave Jones:** Yep. My favourite programming language is still solder.

**David:** Did you say solder?

**Dave Jones:** Solder. Yeah.

**David:** I wonder if that's an actual... I know what you mean, but I wonder if that's an actual programming language. Of course. It's called solder. Yeah. It is. It is solder programming language. No, it's not. It's Bob Pease. Oh, you Bob Pease got me. You've been peased. I have. He got me.

**Dave Jones:** Well done. Young whippersnappers.

**David:** I don't know this man.

**Dave Jones:** You don't know Bob Pease. Oh. Join me in the chant. We are not worthy. We are not worthy. We are not worthy. Is that him? That's Bob Pease. No, that's not him. That's from the... That's from... That's from the... Wayne's World.

**David:** Yeah. No, no. We did that originally with the Horowitz and Hill book. Oh, yes. Yes.

**Dave Jones:** That's right. The Horowitz and Hill book. Yes. We did a fun video. Yeah. With the 2001 Space Odyssey. Yeah. No, that's Bob Pease. He's the ultimate greybeard. Yep.

**David:** Well, I...

**Dave Jones:** I will educate this young whippersnapper. It's okay, folks.

**David:** If he's into control theory, I like him.

**Dave Jones:** Ah, he's into everything.

**David:** Yeah.

**Dave Jones:** Guru.

**David:** Control theory is the best.

**Dave Jones:** He's the czar of bandgaps.

**David:** The czar of bandgaps. How does one be a czar?

**Dave Jones:** He was given the title czar of bandgaps at National Semiconductor. He worked at National Semiconductor. He was the czar of bandgaps. Google it. Google czar of bandgaps.

**David:** I have to look up definition of czar.

**Dave Jones:** Oh, czar? Come on. Aren't you into your Russian history?

**David:** No, I just don't think it... Is he Russian?

**Dave Jones:** No, he's not.

**David:** I don't think he is. I'm not getting anything but...

**Dave Jones:** Certainly doesn't have a Russian accent. No, czar. T-S-A-R. Oh. Because, yeah, I was playing... What's that game? Bald? No. Some people spell it Z as well.

**David:** Because czar is short for pizza. Right. So to me, you were saying... Come on, Google it. The pizza of bandgaps. So I'm like, I don't know what this means.

**Dave Jones:** Oh, czar. Yes. I can't say it. As in a Russian czar. Yeah, yeah, yeah, yeah. You know, some people spell it C-Z-A-R. Some people say T-S-A-R. Whatever. Yeah, yeah. Anyway, if we go to Google Images for the czar of bandgaps... There he is, czar of bandgaps.

**David:** How did they get him to do that? Someone has got him to go in full dress. There we go. Look at this.

**Dave Jones:** Look at this. Yeah. A Russian czar. That's it. C-Z-A-R of bandgaps. Classic P's.

**David:** Was he a character within the company?

**Dave Jones:** Oh, yeah. He was a character within the entire industry. He used to write a column in the electronic design magazine.

**David:** Was it especially... What's all this? Was he especially novel or especially charismatic or both?

**Dave Jones:** Oh, both. He was eccentric, you know. And, yeah. Yeah. As all good... Wise old greybeards are. And, yeah, no. He was... Yeah. He was famous.

**David:** Wow.

**Dave Jones:** Yep. You young whippersnappers. Anyway. Anyway, he's got a whole... He's got a whole story about how he became the czar of bandgaps. See? There's rap. Robert A. Pears. See? There you go. He's learning, folks. He's learning.

**David:** I heard there was, like, a big fad with three-letter initials because of old computer database systems. What? So, apparently, like... Yeah. Computerphile, the channel was talking about it. Yeah. How you often see greybeards, like, signing off with three-letter initials. Ah, interesting. And, apparently, like, that was their little tag on their computer system.

**Dave Jones:** Ah.

**David:** Is that what that is?

**Dave Jones:** No. That's just his initials of his name. No, I don't know. Because he was anti-computer. Was he? He was anti-computer, anti-simulator. None of this simulator rubbish.

**David:** Hence the analog controller.

**Dave Jones:** Oh, he's... Yeah, yeah, yeah. Of course. Yeah, yeah. He was totally against, you know. Yep. And he did articles debunking fuzzy logic at the time. Fuzzy logic was all the rage back in the, what, 90s or something? Early, late 80s, early 90s?

**David:** That just... People just stopped talking about it.

**Dave Jones:** I think they stopped talking. Or did it morph into another name? I don't know. What happened to... What happened to fuzzy logic? What happened to it? It was, like, everyone thought this was the... This is the artificial intelligence of the future. We've figured it out. It's fuzzy logic. And, like... Like, I think it just died in the arse.

**David:** I guess it's, like, there's derivative concepts. Right. Maybe...

**Dave Jones:** Oh, yeah, for sure.

**David:** So...

**Dave Jones:** For sure. Artificial intelligence. Fuzzy logic explained. Like, yeah, but I've never heard anyone use the term for the last, probably, 15 years.

**David:** Yeah, it's... It's...

**Dave Jones:** Nah, it's Gonski. What happened to fuzzy logic? This makes great radio. Googling always. Whatever happened to fuzzy logic? E times 2012. Here we go. Quora. It's also on that Quora. What is that website? It's a question and answers website, isn't it? Quora?

**David:** Do they just database... I don't know. ...things? Or do they actually have a film?

**Dave Jones:** I think they have humans on there who reply. So, you know... In many fields, this approach is still widely used. For example, in robotics, there's a great number of projects based on fuzzy logic. You can blah, blah, blah, blah, blah. Blah, blah, blah, blah. No. No. Back in the 1980s, I was getting excited. The father of... Lotfali Zadi. Am I pronouncing that correctly? Lotfali Zadi is the father of fuzzy logic, having done most of the mathematical groundwork. Wow. He was born in Azbekajan in Russia in 1921. There you go. Outstanding mathematician.

**David:** So, it's control theory.

**Dave Jones:** Yeah. I won't even speak to pretend I know a thing about fuzzy logic.

**David:** Well, the guy you were talking about used it for a doubly inverted pendulum.

**Dave Jones:** Oh, right. Okay. Right.

**David:** I think.

**Dave Jones:** Yeah. All right. So, it was probably that. But, yeah, it was going to be the saviour of artificial intelligence. You know, like humanoid robots. Like we were promised from the 1980s. By 2000, we'll all have a home humanoid robot. You know.

**David:** I don't want a home. I don't want a robot.

**Dave Jones:** Do you want a robot? No. No, I don't really want a robot. No. I'd just end up kicking it.

**David:** It got in my way. It would just be annoying. Yeah. Like.

**Dave Jones:** It's like stupid things.

**David:** Even if it did all the stuff for you. I don't want to be like a slug. Like, just like. Do things for me. Like. Like. What's the point of that? Like. I'll be like. Not Jabba the Hutt. Is that right? Is that the giant slug guy?

**Dave Jones:** Yeah. Jabba the Hutt.

**David:** Jabba the Hutt. Thank you. I said it wrong.

**Dave Jones:** Yep. Jabba the. Yeah. It's not Jabba. Jabba.

**David:** Yeah. Yeah. Yeah. I don't want to be like that. That's what the robotics future is. We're all going to be. That's what. You know. His race clearly invented robotics.

**Dave Jones:** Well, isn't that. Isn't that the. What's that animated WALL-E thing? Is that the. Oh, yeah. WALL-E. WALL-E movie. Aren't they all like on spaceships and they're all just like so fat they can't move? Yeah.

**David:** They have assistive wheelchairs.

**Dave Jones:** Right.

**David:** Yeah. Right.

**Dave Jones:** Ah. The future.

**David:** Don't think that's it. Like. I don't see a market for it. I think enough people would just be like nah. That sucks.

**Dave Jones:** Yeah.

**David:** I hope there's not a market for that because. Yeah. I don't see. Because. I don't know. They can be slug people yet will be the incompetitive. Like. Will be not competitive. Like.

**Dave Jones:** I just can't see them being versatile enough. They just like. You know. Robotics. Yeah. I just can't. Like the. And by. By the foreseeable future. I mean. Like when Sagan. Like become. Like when Sagan turns 20 or whatever in 15 years. Yeah. Like. Like. There won't be. A home robot on the market. Like. I just don't see it.

**David:** Well I would bet there would be. I would. I would say there would be. Because. They're no. Like. For the most part. They're not programming systems with like. Hundreds of rules. While they have rules. They're mostly.

**Speaker ?:** Yeah.

**Dave Jones:** But what's the robot going to do?

**David:** Learn to learn.

**Dave Jones:** Yeah. But to do what? To do what? What function? Like you pay. You know. You might pay five grand for this robot. What's it going to do for you? Well. They had robots back in the 80s. And they brought your beer around. And they had a radio in them. So you can turn on a CD player.

**David:** Well it will definitely drive. Sorry. A tape drive. It will definitely drive most of. You know. It would be the driver for most people. Right?

**Dave Jones:** Oh. The cars. At the least. I still think there's a massive hurdle there. And I. I. Yeah. Forseeable future. I don't think it's going to be as popular as. Or near as. As close as people think it will be.

**David:** Well people will like. The families that have self-driving cars. This is how. It's inevitable. The families that have self-driving cars. Their children won't learn to drive. Right. So.

**Dave Jones:** Yeah but that's.

**David:** Then they will also get self-driving cars. And that's an exponential growth. From the family model.

**Dave Jones:** Once again. I use my boy Sagan as the example. Or even Huxley. Who's a couple of years younger. Four years younger. Right. When they grow up and learn to drive. They will learn to drive. There will not be. Like so. In 15 years. I'm calling it. Yeah. I think I've done this on the show before. I'm calling it. In 15 years. When Sagan's. Or Huxley's old enough to get his driver's license. It won't be redundant. Because of driverless cars.

**David:** Well my. Some of my. That is my prediction. Some of my friends. Yeah. You know. They've just decided not to buy a car.

**Dave Jones:** Right. I know. They're ready for self-driving. Yeah. Because. Yeah. But most of your friends are young university students. Living in the city. Right.

**David:** That's exactly the truth. Yeah. Yeah. But as more self-driving cars come into existence. The push for legislation to enforce them. Will get stronger and stronger. Yep. Because traffic for example. If you can have every car going flat out through intersections. Just cars weaving together.

**Dave Jones:** Yep.

**David:** Which is like possible. You know.

**Dave Jones:** Yeah. Yeah. Yeah. Of course. If they had 90% of driverless cars on the. Right.

**David:** Right. And they would have to have awareness. Every critical mass. They would have to have awareness of the non-self-driving cars. But like. As soon as you get that. Yeah. Legislators will be pushing for it. Because that's cheaper than upgrading infrastructure. Right.

**Dave Jones:** Yes. But I'm not going to.

**David:** Because it pushes the expense to the taxpayer.

**Dave Jones:** I'm debating the time period of getting there.

**David:** Yeah.

**Dave Jones:** I'm. People don't realise the pushback there will be on this tech.

**David:** Well there needs to be pushback. Like India's. I think blocking it at the moment.

**Dave Jones:** Right.

**David:** So they're blocking parts of this. Because it would disrupt their economy.

**Dave Jones:** But you said they need a pushback. But you're for it. No. No. I'm not.

**David:** I'm definitely against it. Oh right. Okay. I think it's going to happen.

**Dave Jones:** Right. But I'm definitely. What's your time frame prediction on it?

**David:** Oh. 10 years.

**Dave Jones:** Like as it becomes. See I don't think. There's no chance in hell it's going to happen in 10 years.

**David:** 10 years you'll start seeing them you know in car parks. You'll be like holy shit there's no one in that car.

**Dave Jones:** No.

**David:** And then it will start to become like this thing you become aware of.

**Dave Jones:** See I was doing this the other day right. I was driving in the underground car park here. I was like driving out right. And I was going how would a driverless car do this?

**David:** They already do.

**Dave Jones:** Right. Yeah but like. Okay. So there's no GPS reception. Right. So it doesn't know where it is.

**David:** But they don't need GPS reception. No. There's a mapping technology called SLAM and it's been around for the last 10 years.

**Dave Jones:** Yeah but what you've got to put the mapping hardware in the car park?

**David:** It already is. No. It's in the cars.

**Dave Jones:** It's in the cars. Right. Most self-driving. So it's all visual.

**David:** No.

**Dave Jones:** Then how does it do it?

**David:** So there's a few different ways. They have. Actually they have lots of sensors. They have radars. They also have a LiDAR. Most of them use about the same LiDAR too. Yeah but. It's great for that company.

**Dave Jones:** There's just so many. There's just almost an infinite number of combinations and permutations of car parks and back alleys and side streets that have no signs and this and that. And it's like I just can't see them. Yeah okay they might be able to go from where it knows from a pre-programmed a nice street onto the highway and then get there. They can do that now. Right. But when they when it encounters anything remotely troublesome I like it's just going to throw up its hands.

**David:** So actually we're already at I think level three for Aldi. Aldi have already reached level three autonomy. What's that? So that means you don't need the driver. Aldi will take on if there's an accident. Aldi I believe this means Aldi are like we'll take it. That's us. You know they think their car is safer to drive all the time than their driver.

**Dave Jones:** No no no but I'm talking about practicality of you know look I get like just trying to encounter situations that aren't that aren't predicted. They're not you know they just don't know how to do where a human does it with absolute ease.

**David:** See that's the thing though. In a split second. It doesn't work the way that old algorithms did. So basically it's a big AI. It's like not.

**Dave Jones:** Sure I understand that. It's not necessarily an AI. But until I see one drive.

**David:** It's learning. It's improving itself with you know day after day. Yeah. And those algorithms they don't actually have to encounter every scenario to understand how to react in every scenario. Yes I understand that. So you can map for example you can put a neural network on a transistor and it will start modelling it really great. And it will model sections that you didn't put it into.

**Dave Jones:** I'm still not convinced until I see one navigate a troublesome situation. It's just like anyway I'm calling definitely not 10 you're saying 10 years. I reckon 10 years. I'm calling bullshit on 10 years. I'm calling bullshit. Yep. Yep.

**David:** So. That's it. How do you feel about Sydney Olympic Park's automated cars now? So they're just bringing in automated cars for the actual park. They drive people around the park. Oh I didn't know. Avoiding obstacles. Avoiding people.

**Dave Jones:** In Sydney Olympic Park.

**David:** That's right.

**Dave Jones:** Yeah. What from venue to venue.

**David:** I believe so. Yeah.

**Dave Jones:** Jeez you wouldn't even need a car. You just need a golf buggy.

**David:** It is like.

**Dave Jones:** Yeah right. I was going to say. Sydney Olympic Park is like. Yeah but I can't imagine a more simplistic scenario than Sydney Olympic Park. If I was to choose. For those who you know have never been to Sydney and Sydney Olympic Park. It's the perfect test ground. It is the perfect. The streets are 20 lanes wide and there's hardly anyone there and it's and there's perfect GPS sky reception like you can get 20 zillion satellites.

**David:** But GPS is actually like. GPS is a tiny fraction of what they need. Yes. I know. They can probably have it off. Yep. Like to navigate because the slam mapping. Right. It maps with respect to maps they already have in their system. You know.

**Dave Jones:** Right. Right.

**David:** They don't need the GPS. They can basically figure out where they are without it. So in a car park they don't need GPS.

**Dave Jones:** Right. Well they can't get it.

**Speaker ?:** No.

**David:** No. They need to not need GPS. Right. Yeah.

**Dave Jones:** Instant. Yeah. I don't know. I think there's going to be more. Even if it's technically possible. I think there's going to be more pushback than what people think there will be.

**David:** Well our government's already letting it for the autonomous bus. That's a bus not a car.

**Dave Jones:** Where?

**David:** In Sydney Olympic Park.

**Dave Jones:** Oh right.

**David:** That's a bus.

**Dave Jones:** Yep.

**David:** And so. And it's not only that. It's like many other countries are already allowing it. Like I think California has some. Right. Quite a few things that allow it. I'll fact check myself.

**Dave Jones:** Nah it's alright. Anyway. That's enough of driverless cars. We've yapped on about that on the Amp Hour before. Our Amp Hour is up. David. Ah. See that was painless wasn't it?

**David:** No. Yeah. Yeah.

**Dave Jones:** And we didn't get through. He thought we'd go through the list and she like no. It never works. It never works.

**David:** You know apart from sitting on my keys this is pretty painless.

**Dave Jones:** Yeah.

**David:** Yeah.

**Dave Jones:** There you go. So thank you very much for filling in for Christopher J. Gamble.

**David:** No worries. Sorry audience.

**Dave Jones:** We were going to do this last week but you were sick.

**David:** Yeah. I still am a little.

**Dave Jones:** Yeah.

**David:** I don't think I'm contagious anymore. Don't give it to me.

**Dave Jones:** What are you sitting on my desk for? Bugger off. Alright.

**David:** When I think I'm contagious I stay away.

**Dave Jones:** Good man.

**David:** Yeah.

**Dave Jones:** Alright. Catch you next time.

**David:** Bye.
