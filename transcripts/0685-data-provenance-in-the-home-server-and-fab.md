---
episode: 685
title: Data Provenance in the Home, Server, and Fab
url: https://theamphour.com/685-data-provenance-in-the-home-server-and-fab/
---

**Dave Jones:** This is The Amp Hour Podcast. Released December 23rd, 2024. Episode 685. Data provenance in the home, server, and fab.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** It's almost 2025.

**Chris Gammell:** It is.

**Dave Jones:** 2025. The 21st century. And you would think...

**Chris Gammell:** A quarter of the way through the 21st century, actually.

**Dave Jones:** Yes, well...

**Chris Gammell:** Yeah, yeah. Oh, man, we've got a lot to do, man.

**Dave Jones:** Well, one thing... One thing the human race has to do is bloody get... Technology to just work. Why can't technology just work?

**Chris Gammell:** Is this a human race problem, Dave? Or is this a Dave problem, Dave?

**Dave Jones:** No, this is just a human race technology problem. Shit never works. Nobody's ever invented a printer that just works.

**Chris Gammell:** Okay, I will agree with that, yeah. Yeah, we're still not there.

**Dave Jones:** No one's ever invented a video card that just works and doesn't have video card driver issues. Nobody has ever invented an operating system that, you know, doesn't do weird shit. And nobody's ever invented a bloody microphone that just works every time. Especially when combined with said operating system.

**Chris Gammell:** I know. It's a rough go. It's a rough go. Dave, we've had two days of Dave's mic issues. But we... I think it sounds great now, so...

**Dave Jones:** Yeah, well, I had to change PCs. My main PC that I record at is totally rooted for any audio stuff. It just... It works, but it makes me sound like absolute garbage. It's like tinny garbage, so...

**Chris Gammell:** Yeah, here we are. Here we are.

**Dave Jones:** Maybe we can edit in a sample of what it actually sounded like. Oh, I'll upload it on Twitter. And no, you can't just audio... See? You can't even just upload audio to Twitter. You have to do it as a video.

**Chris Gammell:** Just delete your Twitter account. It's probably the best...

**Dave Jones:** No, no, Twitter's fantastic, dude. You lost that bit big time.

**Chris Gammell:** Yeah, I didn't... I'm not losing, Dave. I'm not losing.

**Dave Jones:** Trust me, you are.

**Chris Gammell:** Okay.

**Dave Jones:** How's that Mastodon going for you? Those big numbers on Mastodon, huh?

**Chris Gammell:** I know. It's great. It actually has picked up for me, so I'm on there more. You know, it's just like workflow and life situation. 2025 is going to be the year for me... Well, I'm not going to make any broad sweeping things. The thing that I'd like to do more of is more self-hosting, more interesting, like kind of owning my own stack kind of things, right? So like...

**Dave Jones:** Right.

**Chris Gammell:** Hosting my own website, fine. It's not like I'm going to have a server in my house, so I'll probably still be on shared infrastructure, DigitalOcean or similar.

**Dave Jones:** Well, you've got to do it. You've got to go the whole hog.

**Chris Gammell:** I don't think so, because I... Come on. ...don't want to. That level of convenience is... I'm not going to buy a server. You know, like you still host it.

**Dave Jones:** I've been hosting my own video files for 13 years on my own server. It's not a problem.

**Chris Gammell:** Sure. But you have a penguin nerd, and you also have a server at a server farm, right? It's not in your closet at your house, right?

**Dave Jones:** No, it's not in the closet of my house, but I own it. I own the... Yeah, sure. I physically own three devices in a rack somewhere. Yeah, yeah, yeah. Yeah, yeah.

**Chris Gammell:** But that's just accounting. I don't really...

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. And it will. So I would like to do more of that.

**Dave Jones:** And it's also a bandwidth. It's a practical bandwidth issue. Yeah, no, it's...

**Chris Gammell:** I think that's actually a good move for you. But anyways, I'd like to learn more of that stuff. More about, you know... I don't know how deep down... There's a very deep rabbit hole. I'm sure a lot of our listeners are in the IT group, but just... Or in the IT... Sven... Persuasion, rather. And yeah, you know, there's... You could go as far as you want. There's like a whole subreddit called Homelab. I don't know if you've ever heard of that one. Nope. But like, you can... You can really overdo it. And I hope to not go that deep. But just like things like Docker containers and just like... So just recently I put... I just booted my system back up. We talked about it last time we recorded about Home Assistant. You said you were going to be doing some stuff. I was going to get my stuff back out of there.

**Dave Jones:** I thought about looking into it, yeah.

**Chris Gammell:** Oh, okay. Okay.

**Dave Jones:** Yeah, because everyone raves about it and goes, you know... But, you know... It's just another way to get my solar data out. That's basically it.

**Chris Gammell:** Oh, right. Yeah, that's right. That's what it was for. Yeah. Yeah. And so I got that... I booted up one of the machines I have here and I just... Running it as a Docker container. It's a little bit different for me. But pretty painless and yeah, that's great. So I'd like to do kind of more of that stuff. Host it on my local network and do that sort of thing. So we'll see how deep this rabbit hole goes.

**Dave Jones:** Eh, sounds a bit too complicated. I just like... I just don't want to dick around with stuff. I'm just too old to dick around with stuff anymore. Yeah, I used to love it when I was a young whippersnapper. Right? Yeah, I'd be building my own PCs and rolling my own shit. You know, coding in bloody assembly language and doing all the rest of it. Right? But yeah, nah. I'm just too old for that. I just want shit to work these days. Is that too much to ask?

**Chris Gammell:** Yeah. I mean, I think... I find one of the things is the... I find it's getting easier to get stuff booted up. So like I mentioned, the home assistant install, that was relatively painless. But then keeping it up. You know, like making sure it's working. And, you know, like does it come back automatically after power resets? And, you know, all that kind of stuff. Like that's... That feels more onerous. And like there's less infrastructure. They're like... Like when systems are like, you know, really bulletproof, it feels like there's always humans kind of restarting stuff in the background. And that's where I think I lean a little bit more heavily towards the... I wish this would just work like you're saying.

**Dave Jones:** Yeah, yeah. Exactly. I just...

**Chris Gammell:** Yeah.

**Dave Jones:** I just like... Like everyone says this, right? Every time I have the slightest issue with Windows or I mention Windows at all. Oh, why don't you move to Linux? Why don't you move to Linux? It's fantastic. Never had an issue. Yeah. There are... Yeah, no. No, you do. No, yeah, I know. It's bullshit because there are real people like yourself who use Linux, right? Sure.

**Chris Gammell:** Yeah.

**Dave Jones:** Pretty much almost exclusively these days. But you will... But you'll be honest with me and tell me it's not some utopia that just works.

**Chris Gammell:** No, yeah. I think the thing that would happen there is you'd get a little bit more used to like, oh, I know what this is. You know, like you kind of get more hardened against the things that are common. Yes. Whereas it might... On Windows, it might be kind of like below the surface, you know, and just like, oh, I guess I'll try reinstalling the program and see if that does it. You know what I mean? Yeah. Or I'll try rebooting the whole system. That sort of... Yeah, and I think it is... It's just more of like a expectations kind of game.

**Dave Jones:** Right.

**Chris Gammell:** Yeah.

**Dave Jones:** No. I'm done with it.

**Chris Gammell:** There are no... There are no like perfect systems. I think the best thing you could do is pay someone to fix your problems for you. Honestly, like that's the...

**Dave Jones:** That's what I do. I literally pay a full-time Penguin guy to take care of my... That's it. Yeah, that's it. Yeah, service stuff for me. Yeah?

**Chris Gammell:** Yeah. I just have no interest in learning that.

**Speaker ?:** He's the expert.

**Chris Gammell:** He's making it work.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. I have no interest whatsoever.

**Chris Gammell:** You figured it out.

**Dave Jones:** Yeah. Well, I was doing this the other day, right? I was trying to get an old laptop working, right? But it had like a version of Windows 10 Enterprise on it, right? Welcome to the Linus Tech Tips show. And yeah, right? So I wanted to get rid of that. But it had all that like corporate security shit on it, right? So I just wanted to nuke the thing. And, you know, so I was asking on X, you know, how, what's the easiest, best way to just nuke this and install a new version of Windows? And everyone's going, oh, you know, ultimately it came, a lot of people had complex stuff. And then they go, oh, just install, you know, install Windows 11 on a USB stick, plug it in, and you should be good to go. So I did that. Sure enough, I was good to go. But then it forced me into a Microsoft account. And then I'm, you know, so I'm trying to buy, so I asked on X again, how do I bypass this shit? I don't really want to log in. Even though I had no problems with it. I just like on principle didn't want to do it. You know, log into my Microsoft account just to load up Windows.

**Chris Gammell:** Your MSN live.com account. Oh, man.

**Dave Jones:** So then everyone starts giving me advice on do all this command line shit. So I start doing this command line shit, and it doesn't work, right? And then everyone goes, oh, no, you didn't forget to disconnect from the network first. You've got to do this command line thing to disconnect from the network thing before you do this command line thing. And it's like, oh, I just gave up and just inputted my Microsoft bloody account. And then, like, even a day later, I came in this morning, and people are still answering my X, question, right? Because it just sits there, and there's no way to market it.

**Chris Gammell:** That's a bit of a bike shed one, too. Like, there's a lot of people who have a lot of opinions about, like, everybody has a computer. Everybody has to deal with OS stuff. So it's like, and Windows is the most popular. So, like, that also means, yeah. Oh, my God.

**Dave Jones:** And people were throwing me the most obscure technical shit at me that I had known. Just do this. Like, and they're throwing words at me that I have no idea what they mean. Like, yeah. And I'm not a complete dummy, but, like, oh, God.

**Chris Gammell:** Would you like my suggestion, which I actually think is the right suggestion, is rip the hard drive out and put a new one in. That is the answer.

**Dave Jones:** Somebody did actually suggest that. But no, I didn't have to do that.

**Chris Gammell:** All of my upgrades, like, it is so easy these days. Like, and then the nice thing is, if you mess it up, oh, you know what? I can just go back to the other one.

**Dave Jones:** I put it back. Yeah, but I wanted to get it working then and there. Sure, of course, of course. But no, I just nuked the partition. I just nuked it. So, which is, you know, same thing.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Anyway. Well, okay.

**Chris Gammell:** So, this is interesting because it leads into one of the news stories from this little cycle we've been in. Obviously, the Raspberry Pi 5 has been released since we last spoke.

**Dave Jones:** The Raspberry, you're talking about the compute module?

**Chris Gammell:** Oh, compute module 5. Yes. Sorry. Thank you. Yes. The CM5 has come out. Any impact for you?

**Dave Jones:** No, I just set up a CM4. I just got that running, a CM4.

**Chris Gammell:** What was that for?

**Dave Jones:** I was going to use it to talk to my Enphase system. I was going to run Solar Assistant to talk to my Enphase system. But I don't know. I could install Home Assistant on it, maybe, something like that.

**Chris Gammell:** What is Solar Assistant? I've never heard of that.

**Dave Jones:** Solar Assistant is confusingly named similar to Home Assistant. Sure, yeah. I believe it's totally different, but they do talk to each other in some way. So, I don't know. Anyway, Solar Assistant is designed to work with a whole bunch of different solar inverters. So, it talks to them via their serial ports or whatnot. Okay. And then it just gives you nice graphical displays and it samples the data faster and, you know, it gives you a nice remote control panel interface and all sorts of niceties. Got it.

**Chris Gammell:** Like log into a web page sort of thing. Yeah. Yeah. That's great. Yeah.

**Dave Jones:** And I believe it works similar to Home Assistant in that you do it as a root thing on a Raspberry Pi or on a PC or something like that as a root-based operating. Like, it works raw, so it doesn't work on top of the OS. It's actually a raw. Oh, a bare metal. Or it's a bare metal is the word. Yep. It's a bare metal install. And, yeah, it's doing the job for me. So, but I'm currently running that on a Raspberry Pi 3, but I need a separate one because apparently you can't run, you can't get the same Home Assistant to talk to two different inverters. So, you've got to use literally a separate Home Assistant device to talk to two inverters and then the two Home Assistants talk to each other. So, it's kind of like physically separate hardware. Oh, okay. So, you can't just run two instances on the one bit of hardware, so to speak. So, you've got to, yeah. Yeah, yeah, yeah. So, it's weird. So, you know, if you've got more than one solar inverter, you've got to physically have one hardware, you know, PC actually for each one. Yeah. It's just weird. That's it. Yeah.

**Chris Gammell:** So, that's interesting. I was, so, like I said, I was just reinstalling my stuff and I had been asking around as well about how to do this and poking at some of the AI thingies. And I was, there's a thing called Proxmox, which is-

**Dave Jones:** Oh, I've heard of that.

**Chris Gammell:** Yeah. So, that's like a virtualization layer that you install kind of at the, just above the BIOS level. And then you can install, basically, in your case, I think what you would do is you'd create up like two virtual machines that are on top of that. Yes, got it. And then you'd have two solar assistant things that are plugged in.

**Dave Jones:** Yeah, running on the same hardware. Yep. Yep.

**Chris Gammell:** That's right. Yeah. Where does it, how does it actually talk to the solar hardware? Is it like isolated or not isolated?

**Dave Jones:** What do you mean isolated? Is it in-

**Chris Gammell:** So, like, is it like serial, just a straight serial connection? It's serial.

**Dave Jones:** It uses a serial. Oh, interesting. Yeah. Yep. Not like RS-45, nothing like that? No, no. Just uses an RS-232 serial cable. Interesting. Yeah. Okay.

**Chris Gammell:** Yeah. Cool. Yeah.

**Dave Jones:** Easy.

**Chris Gammell:** Well, that makes sense. I guess they probably isolate, I guess, on that side of things, like wherever the computer side is, they're probably isolating from the higher power.

**Dave Jones:** Or isolated to the actual- Oh, they would probably do it inside the inverter, I would suspect. They've just, like, got a electrically isolated IO, like RS-232 in there or something. I don't know.

**Chris Gammell:** Yeah. Anyway. Yeah. Yeah. So, yeah. It works fine. Okay. So, and you're trying to do this just to kind of visualize all this stuff and get it talking back to a centralized- Yeah.

**Dave Jones:** It gives me a nice panel interface because the inverter that I've got is just garbage. It's software. It just does not work. It is absolutely garbage.

**Chris Gammell:** Oh, yeah. Yeah. You know, I thought about our long-running conversation a while back about- Do you remember how we used to talk about-

**Dave Jones:** The chip printer.

**Chris Gammell:** Yeah. We did talk about the chip printer. This is not about the chip printer. This is about- I remember talking about, like, tablets that would slide into, like, the center consoles for cars. Do you remember talking about that way back in the day?

**Dave Jones:** Oh, yeah. Vaguely. Yeah.

**Chris Gammell:** Yeah. Yep. But this, I was thinking about it because that was completely solved. Like, I wasn't looking. I wasn't buying cars or anything like that. But that was completely solved by, like, Apple Car Kit and Android, what do they call it?

**Dave Jones:** Yes. Android Auto. Yeah.

**Chris Gammell:** Auto. That's it. Yeah. Yep. That solved the problem because it's basically, it's just like, oh, okay, well, your phone, it's just like a screen for that now. And, like, that's all I ever really wanted. I mean, as long as the car updates the Android Auto, of course.

**Dave Jones:** Mine didn't work the other day. Mine didn't work. Like, I actually plugged my phone in because my phone supports the, you know, the new Android Auto and it just didn't work properly. So, I don't know.

**Chris Gammell:** Oh, it plugs in for it. Interesting. Okay.

**Dave Jones:** Yes. Yes. It physically plugs in. Yes. Got it. It needs a USB connection. It can't do it over the Bluetooth.

**Chris Gammell:** Yeah. Mine does Wi-Fi.

**Dave Jones:** Oh. Oh. Wi-Fi. Okay. No. Yeah. I'm pretty sure mine doesn't have Wi-Fi.

**Chris Gammell:** It says it's Bluetooth, but then it sets up a Wi-Fi connection, I think, it's back hall because, like you said, it's, like, high bandwidth. Oh, yeah.

**Dave Jones:** It's very high bandwidth. Yeah. You wouldn't be able to do it over Bluetooth, I don't think.

**Speaker ?:** Hmm.

**Dave Jones:** No. So, yeah. Anyway, that just didn't work and I was, you know, too busy. I didn't want to pull over and try and troubleshoot the stupid thing, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** No. Yes. I would like to restart my car, please. Turn it off and on again. Yeah. Right. My God. Yeah. Yeah.

**Chris Gammell:** Well, back to the CM5 thing, I went to my source for all things on that, which is former guest of the show, Jeff Keerling. Yep. People don't watch his shows. Yeah.

**Dave Jones:** He's done a video. It's been showing up in my feed for, like, every day for, like, a week.

**Chris Gammell:** He's the go-to, man. YouTube's really flogging.

**Dave Jones:** Yeah. The algorithm's flogging that video until the cows come on.

**Chris Gammell:** He's so great. Yeah. Yeah. Totally agree. Yeah. I'm excited to try. I only, I have a CM, sorry, I have a Pi 5. I do not have a CM5 yet.

**Dave Jones:** I don't even have a Pi 5.

**Chris Gammell:** Okay. I have a Pi 5. I have a whim, but, like, the, you know, stupid dual mini micro HDMI connectors. Ugh. Right. Anyways. Yeah. I mean, it's fine. Good. I don't really need, like, it's getting to the point where they, so they just released the keyboard, too. Like, they're really cranking out products, which is great. I'm hoping in the new year we're supposed to talk to the Raspberry Pi team, so that's great. I'm excited to talk to them. But, uh, I, uh, I don't know where this is going. You know, like, some of these, like, the Pi 5 is far outstripping most of the old crap laptops they have laying around, which is, like, cool. Right, yes. Yeah, exactly. That's great. Yeah. But, like, I don't have, you know, you and I are not exactly what people would call capable software engineers, so, like, what are we going to run with it, you know? Exactly. I'm not running, like, dual K, 4K streams.

**Dave Jones:** Well, I've got a company that, buddy, keeps sending me these embedded, these little NUC type PCs. Oh, yeah. Right? So, I've got three of them now. I've got another one sitting in the mailbag. Sure, sure. And two of them, one of them's actually technically higher power than my main desktop editing PC.

**Chris Gammell:** Why are we, why didn't we use that for the audio today? Come on, man.

**Dave Jones:** Because it's not set up.

**Chris Gammell:** You should just set all three up, have a microphone attached to one, and then when everyone works that happen day, you know, we'll just use that.

**Dave Jones:** Exactly. Yeah. Multiple redundancy, yeah. Yeah, exactly. Yeah, well, I've got, I've got a ton of mics, so yeah, I can just set up dedicated.

**Chris Gammell:** Bingo. Just.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** People walk in and be like, are you, are you running a studio here? No, no, no. I'm just. No, I'm just. I'm bad at Windows.

**Dave Jones:** Well, the thing is, I've never had a problem like that before.

**Chris Gammell:** Oh, Dave, it's fine, man. Don't worry about it. Oh, man. No, it's pissing me off.

**Dave Jones:** And just know, I just know every time I'm going to talk about it, people are just going to be hounding me about freaking Linux.

**Chris Gammell:** Performance anxiety.

**Dave Jones:** Oh, man. It's just. Yep. Can't win. Anyway. So.

**Chris Gammell:** Yeah. So, Nux, I feel like the same thing, though. Like, they don't, I don't have a lot of use for them. Like, I have one now. That's running home assistant.

**Dave Jones:** Well, I actually took one home, right? Because I've got, like, three of them now. Sure, sure, sure. So, I took one home for the boy, right? Because he's got this old crappy. Calling the tax man. PC's, right? And I didn't pay for it.

**Chris Gammell:** I know. It was a gift in kind.

**Dave Jones:** And, yeah. So, I set that up for him. Look, like, he wants to play Minecraft, you know. Only that's pretty much all he uses the PC for. Yeah, no, he's nine.

**Chris Gammell:** It's a great use. Great use of it, yeah.

**Dave Jones:** Yeah, yeah, yeah. Exactly. And I set this up, and it's super fast and everything. It was getting, like, 60 frames per second or whatever. And, yeah, this is great. But then, this is the VBlog came along and went, no, it's got too many cords. There's cords everywhere because you've got to run, you know. And then I was using, like, a portable screen with it. So, and the portable screen had to have a power cord. It had to have a USB cord, which goes back to the cable and the keyboards and the mice. And, like, no, it was all too much. So, I had to get that laptop working that we talked about with the Windows 11 and that passes. No, it was just too messy. It was too messy. Wow. You got the veto. Yeah. You got the veto. Yeah. Just cables.

**Chris Gammell:** Yeah. You need that wireless power, man. Wireless power. Yep.

**Dave Jones:** Totally. Should invest in one of those Wi-Fi. One of those wireless power companies.

**Chris Gammell:** Yeah.

**Dave Jones:** Who are doing gangbusters.

**Chris Gammell:** Gangbusters.

**Dave Jones:** Yep. Ah, boy. I was thinking about doing a video going through every single debunk. I've, like, every company I've ever debunked and just seeing where they're at now.

**Chris Gammell:** No. No. Okay, I kind of like the where are they now. Yeah, yeah. That's kind of like the...

**Dave Jones:** Yes. Robin Leach. Robin Leach.

**Chris Gammell:** Lifestyles of the Broken Stupid.

**Dave Jones:** No, right. I don't really get... I kind of get that, but I've never really watched. Yeah.

**Chris Gammell:** No? Lifestyles of the Rich and Famous? Famous? No. No. Yeah. Sorry. Yeah, it was the old guy. Yeah. Where are they now? Before my time. It was mostly a pop culture reference, but... Okay. Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Speaking of famous people...

**Chris Gammell:** Speaking of famous people, our last episode, you talked to Lee Felsenstein. That's pretty cool.

**Dave Jones:** I did talk to Lee. That was awesome. Yeah. That went for over three hours. Unfortunately, this is another one where we have to bring up bloody audio.

**Chris Gammell:** No, we don't have to bring up audio.

**Dave Jones:** Yes, we do. Because, no. No, this brings up an interesting thing, because I did several polls on this. I did a poll on X, and I did a poll on my YouTube channel. I think I even did a poll on The Amp Hour Twitter feed, right? Okay. X feed. In that... Because I had to do a lot of audio processing on that. This took me many days to actually edit this three-hour video, because the audio was so bad, we're getting feedback anyway. It was really bad. Okay? It's the worst audio I've ever had to deal with. And so, because we usually level the audio when we're doing the Amp Hour. And we've... Yes, we usually level the audio. Yes, we. We. We. Our editor, who we don't have at the moment... You're talking to him. Yeah. Yes. Anyway. Yeah. So, we used to use this old program for, what, 12 years? We've used this program or something? No, no. Yeah.

**Chris Gammell:** It is now defunct. It is now... It is now... No new versions. No, they're emerging. It sits in my Dropbox, because I keep installing it in, like, one... Yep. Yep. Yep. In compatibility mode.

**Dave Jones:** Anyway, it's the Levelator by... Levelator! The Levelator! From a company called Conversations Network. I think they were, like, an old-school podcast thing or something. Yeah, I think they were. Anyway, they don't make it anymore. And it's magic. You drop in your file, it does noise reduction. It does proper leveling, not just compression, but proper leveling. You know? And it's just... It does wonders.

**Chris Gammell:** Yeah, it does look like a 10 megabyte executable instead of, like, a...

**Dave Jones:** Yeah, yeah. Yeah, it's great. It's just a single X in. 4,000 GPUs that are... Yep, yep.

**Chris Gammell:** ...that consume the Amazon rainforest worth of energy. Yeah. And it's been...

**Dave Jones:** Yeah, it's the most fantastic thing ever. Thanks, Adobe.

**Chris Gammell:** You're so awesome, Adobe. Yeah, yeah.

**Dave Jones:** But I found that that didn't work on my exported, edited audio, because there was too much background hiss. And, like, there were all sorts of weird artifacts in the Lee Felsenstein video. So I ran it through. I've also... I've got a license for RX-8, it's called. It's, like, one of these professional audio tools. And they've got a professional audio reduction thing in there. And I put it through that, and it sounded really great. So I exported that. And then I put it through the... Play of a Later thing. And I thought it sounded okay, given the source material. But then I got a whole bunch of comments from people after I released that video on my main channel. I got a whole bunch of comments from people saying, This sounds shit. This is unlistenable. I cannot listen to this. It is utter garbage. You know, and all sorts of things.

**Dave Jones:** Try harder. And it sounds fine, do you? Yeah, okay. There's a few audio issues with it, and it sounds fine. Anyway, so I re-edited another version that had no audio processing whatsoever. It was just the raw thing. And those people who were complaining said, Oh, that sounds much better. Huge improvement. So I thought, this is interesting. Because I think the noise reduction, the process one, sounded, you know, better overall. And so I did a poll. I did a poll. And it turns out that over on X, I think, over 55% of the people said that the original one sounded better. So it's interesting how people have different tastes in audio. I was just surprised. I expected there to be, you know, like 80% of people said that, you know, yeah, the process one sounded shit and the non-process one sounded fine. But no, no. It was like, no. So I don't know. People have these weird tastes in audio and they, you know, they could not listen to it. They physically could not listen to it. They couldn't listen to more than five minutes of it. It was that bad to them. Yet other people said, no, this is fantastic. And they listened to the whole three hours. So what the hell is going on with humans?

**Chris Gammell:** Yeah. The human ear is actually really hard to model. You know, like in terms of like the log, the log behavior of like human listening and stuff like that. Yeah. But in terms of the personal taste. Yeah. I don't know. I, I feel like my ears are all like, do you ever listen to old, old recordings of things like old Elton John songs and stuff like that? Sure. It's just like, ah, it's so quiet. It's so quiet. You know, like my ears are so used to just like fully compressed, like hip hop music. Sunday, Sunday, Sunday. You know, it's just like.

**Dave Jones:** And the latest doof doof shit they play at the gym. You know, I'm doing a class at the gym and it's all doof doof doof doof. That's a different problem. That's just you being old. No, no.

**Chris Gammell:** That's just the music being shit these days, dude. Well, that's true. Yeah. Okay. Come on.

**Dave Jones:** Come on. You've got to agree. Yeah.

**Chris Gammell:** Yeah. But that doesn't impact your, your, your compression, like perception of compression. You're just saying, this is bad music. It's just bad music. It's shit. It's just garbage.

**Dave Jones:** You can't understand the lyrics. And it's just all...

**Chris Gammell:** That's why I don't go to the gym, Dave. It's really the only way to save yourself. Yeah.

**Dave Jones:** Anyway, bloody hell. This does segue nicely, though. It does. Yes, it does, indeed. Into the big interwebs thing of the week. Mendit Mark, fellow YouTuber, who I don't know. You probably didn't see this because you're not on X.

**Chris Gammell:** I have no idea what you're talking about.

**Dave Jones:** It's on the Reddit list, dude.

**Chris Gammell:** Yep. Okay. Which one is on the list?

**Dave Jones:** People... Chris just did announce to me before the show that he's quit Reddit.

**Chris Gammell:** No, I haven't quit Reddit. I'm avoiding Reddit. You're avoiding Reddit. And that includes our own subreddit. I'm still there right now. I'm not posting there. I'm posting stuff to my own forum because that's where I am. And yeah, I'm just... I'm living a healthy life, Dave. Come on, man.

**Dave Jones:** Well, actually, there's two audio-related things.

**Chris Gammell:** Is this the preamp repair thing? Is that what you're talking about?

**Dave Jones:** This is the preamp repair thing, yes. The £25,000 or £30,000 American bucks.

**Chris Gammell:** Freedom bucks, yeah.

**Dave Jones:** Freedom bucks. Preamp. Preamp repair. Apparently, I think the manufacturer actually sent it to him to repair, which is the odd thing about it. Anyway, he's a YouTuber who does excellent detailed reverse engineering repair videos on, I think, mostly audio type stuff. Anyway, he's really great at it. It's a fantastic video. You should go watch it.

**Chris Gammell:** We'll link it in. Yeah, check it out.

**Dave Jones:** And... But, well, the only place you can see it is on Odyssey because the manufacturer copyright struck it. They had his video taken down based on copyright because he reversed engineered it and drew his own schematic. And they didn't like the fact that they were showing inside this £25,000 preamp and it's built like just absolute garbage. You should see... You've got to see inside it. Just scroll through the video now and have a squeeze through. And it's just like these like home-etched boards or something with plastic standoffs. Oh, no. Sorry. You can't see it because you don't have the link to the Odyssey.

**Chris Gammell:** Oh, so the first one that's on there, that was taken down, you're saying?

**Dave Jones:** That was taken down. The video that's on our Reddit feed is him talking about the video being taken down. So he can't show any of the footage.

**Chris Gammell:** So there's no link out to Odyssey.

**Dave Jones:** No, there's no link out to Odyssey. I won't bother finding it now for you. Anyway, just picture the most home-brew-y kind of crappy multi-board point-to-point wiring standoff construction. Stacks on stacks. Stacks on stacks of these plastic standoffs which all broke off. And this is £25,000. So he showed this and he ultimately repaired the thing. And they copyright strike him even though there's... You know, it's a totally bogus claim.

**Chris Gammell:** Can you explain copyright strike? What does that mean?

**Dave Jones:** Copyright strike. It means basically YouTube have an automated copyright system. So you can flag a video if you think you're the copyright owner. You can flag a video as, no, this is against my... I own the copyright to something in that video. And usually you put like a timestamp of where the thing is. And YouTube's rules, I believe still are, that the video automatically gets taken down and you have to basically then take the person to court to get the video taken back. Or you've got to elevate it to a next legal step before you can get your video put back. So it's an automatic takedown process and people actually totally abuse this system to get videos they don't like taken down. In this particular case, the manufacturer didn't like that he showed inside their own product. Yeah, I get it. Which looks like total garbage and he drew circuits of how he thought the circuit worked and stuff like that. You know? Yeah. So it's a total abuse of the copyright system and it's easy to actually abuse. Same with the trademark as well. You can say, this video infringes my trademark and the video automatically gets taken down and you as the content creator have to then issue a legal challenge to that to get the video put back. So it's a really shitty process. Yeah. And a lot of videos have been falsely falsely taken down. Yeah. So yeah. It feels like

**Chris Gammell:** like how DMCA was used kind of weaponized against people. DMCA,

**Dave Jones:** weaponized DMCA. Yeah. It's the same thing. So, yep. Yep.

**Chris Gammell:** I found the link for Odyssey. I will put that in the show notes as well. Excellent. Excellent. Yep.

**Dave Jones:** Cool. Yeah. Anyway, our good friend Lewis Rossman did a video on it and he has agreed to reinstate the video on YouTube in full on his channel and he has the legal back in to take this guy to court if he tries to take it down again. So, good on you, Lewis. Lewis has agreed to put the video back up and then the guy can try and take on Lewis Rossman. Good luck because Lewis now has very substantial financial and legal backing for the stuff that he does.

**Dave Jones:** yep. Lewis is fighting the good fight. Yeah, it's great. Anyway, yeah, yeah, it's absolute bullshit how, you know, us content creators can just have our content removed based on a false claim and really to fight it you've got to have legal backing. You know, you've got to be willing to go see a lawyer and put money behind it, et cetera. So, yeah, yeah, really sucks. Anyway, thankfully that hasn't happened to me yet. where the verdict's still out on the one we talked about with the battery, you remember the, what was it, DCS Systems battery or something? Who they, yeah, that was the, yeah,

**Chris Gammell:** I know what you're talking about, the, the, the, like the solar, the solar battery.

**Dave Jones:** Yeah,

**Chris Gammell:** yeah, yeah. So,

**Dave Jones:** yeah, I believe the lawsuit's still out on that one, but yeah, he had to take that to court to actually let him actually, for those videos to stay up.

**Chris Gammell:** yeah. Yeah, that sucks.

**Dave Jones:** I'm, I'm sure he'll win it, but yeah, it costs a lot of money and the only winners are the lawyers. So, there you go. And a good friend, Unmanaged 615 has put up a, um, video about the Fairlight. You being a muso would know all about the Fairlight, wouldn't you? The Australian designed Fairlight. It was basically the first digital sampling system that completely changed the music industry.

**Chris Gammell:** Dave, I have no doubt that I could be completely out of it, but, uh, you saying the Australian, uh, you know, sampling thing, it was just like, oh, okay, well, you were, well, you need to watch the video

**Dave Jones:** then. It's on our, it's on our Reddit feed. If, if you can dare go to Reddit, you can watch it. Anyway, in the early 80s, um, yeah, this, well, it starts out in this, in 1980s, this Australian invention transformed music. So all of the, I guarantee all the songs you love from the 80s were that they would have sampling done on this Fairlight, uh, keyboard sampling system. And it was an Aussie guy who invented it.

**Chris Gammell:** It says Peter Gabriel.

**Dave Jones:** Yep.

**Chris Gammell:** That's the only name I recognize. No,

**Dave Jones:** no, there's countless. Okay.

**Chris Gammell:** Tell me some others.

**Dave Jones:** Oh, we didn't name them. And they, and they probably, if they had the music that actually required any sort of like sampling and over sampling and stuff like that, it was a, yeah, sound effects, odd sound effects and stuff. It was all done. Gabriel San Jacinto,

**Chris Gammell:** Kate Bush, Babushka, Patty Kingsland, the whale, Frankie goes to Hollywood. Relax. Okay. There's one.

**Dave Jones:** Right. It's one. He's fine. Relax.

**Chris Gammell:** Go to it. It's in the, it's one of the plot points in Zoolander where, they keep putting that, they keep putting that record on when Derek Zoolander is meant to kill someone.

**Dave Jones:** Oh, I haven't watched that in forever. I have to re, re watch that. Cause the memes are great. Yeah. The memes from that are great.

**Chris Gammell:** I think that actually might be the biggest song of this, from this list of, not, not huge, but yeah, I can see it. Oh, Def Leppard's in there. Okay. Liza Minnelli, Britney Spears. Britney Spears.

**Dave Jones:** Right.

**Chris Gammell:** Okay.

**Dave Jones:** Oh, okay. Right. Yeah. Anyway, tons of them. It's an absolute, it revolutionized the music industry. Absolutely revolutionized it. Um, and it was originally, um, well, it kind of, um, looking at the Wikipedia page, it originally was a construction project, um, in, uh, electronics today. Um, so like that,

**Chris Gammell:** I thought you, okay, got it.

**Dave Jones:** Like in the seventies. And then he hired Peter Vogel, the guy who did that hired Peter Vogel to actually design, uh, this fairlight thing. So he's now famous in the industry for base, basically venting, inventing music sampling. So, yeah. And it had like really cool spectrum display. Like it actually hooked up to a, uh, screen and you could like view all the waveforms and spectrums. And like, it was really, really cool stuff. So now it's absolutely trivial. Right. But back then,

**Chris Gammell:** right, right, right. Yeah. It's like an iPhone.

**Dave Jones:** You can do it on a Raspberry Pi compute module, you know, and a thousand times better, you know, right. And, uh, yeah. Anyway, I, I tried to get, um, Peter on the, I tried to get an interview with Peter, but he didn't get back to me. So he's here in Sydney. I think he's up in the blue mountains somewhere. Um, he's around still. And I was going to want to do an interview with him talking about the old fairlight design, but unfortunately didn't get back to me. So,

**Chris Gammell:** okay. Well,

**Dave Jones:** anyway, keep trying, keep trying. I'm surprised you haven't heard of the fairlight.

**Chris Gammell:** I,

**Dave Jones:** I'm, I'm real, as a, as a muse, I'm very, even a modern one, I'm very surprised.

**Chris Gammell:** I, I have, uh, specifically avoided all things synthesizer. Uh,

**Dave Jones:** okay. Right.

**Chris Gammell:** I, I was, uh, posted on Mastodon as, you know, as I have been doing now, but, uh, I've been like, you know, watching a bunch of woodworking videos, which is like the worst idea. Because there's, there's no, there's no other hobby. That's just like, Oh, did you have some money that you didn't, you wanted to spend and just like throw down a hole on tools? Like, okay, great. Yeah. Woodworking, woodworking is for you. but someone pointed out that buying synthesizers is actually a very similar.

**Dave Jones:** Oh, okay. Enterprise.

**Chris Gammell:** Just because it's like there's the variety and like the, Oh, well, don't I need that hyper specific one other tool to do that one thing? Yep. You know, that one time. Yeah. That's, I think.

**Dave Jones:** I gave an old, I gave away an old Yamaha. I think I might've found in the dumpster and all Yamaha, um, or, no, I might've sold it. Yeah. Yeah. I sold it. Um, and then I found in dumpster, Oh, Yamaha synthesizer thing. It was quite, you know, it was one of like the, you know, fairly high end ones, I think. Um, but I have no use for it and it's, and it's enormous, you know,

**Chris Gammell:** I don't need to take enough space and stuff like that.

**Dave Jones:** And the guy who came to, um, get it, he actually came to my house to get it. He actually collects these things and he's got an entire collection of Yamahas. He specializes in actually collecting Yamaha synthesizers. And, and he, and he didn't have this one. Why couldn't he have collected miniatures? Yeah, exactly. Yeah. It had to be frigging keyboards.

**Speaker ?:** Yep.

**Dave Jones:** Oh man. So yeah. Yeah. Yeah. He was, he was very pleased to get it. Um, and, and it had some issues, so he was going to fix it and you know, what, you know, yeah. So yeah, people get obsessed.

**Chris Gammell:** I used to have some vintage keyboards around.

**Dave Jones:** It's right. Okay.

**Chris Gammell:** You know, it's easy to pick them up and you know, they're fun to fix too, but they're,

**Dave Jones:** they're bulky,

**Chris Gammell:** you know,

**Dave Jones:** definitely.

**Chris Gammell:** No matter how many synthesizers or electric pianos or really anything I fix, I'm still not good at playing the piano. So nothing really fixes that.

**Dave Jones:** Wait until you get to, um, guitar effects pedals.

**Chris Gammell:** Oh yeah. Yeah. Well, like Fran. Yeah. Yeah. Yeah. That's, that's, I think that's, that's probably a good crossover between the two. Yeah, exactly. Except those are more portable. That's what I'm saying. You know, like you can really. Yeah.

**Dave Jones:** Yeah. Yeah. But you get addicted. Oh, this one has a slightly different twang to this one, you know? Right.

**Dave Jones:** Right.

**Dave Jones:** Right.

**Chris Gammell:** But none of those, I used to have those back in my music days too. Right. But again, nothing actually makes you go to guitar. That's the downside. Okay. Yeah.

**Dave Jones:** Oh boy. Anyway. Yeah. Fairlight. Anyway, very cool. So I'm going to actually watch that. It's a doc. It's an 18 minute documentary. You can watch 18 minutes. Okay.

**Chris Gammell:** I'll do it. Yeah.

**Dave Jones:** Excellent.

**Chris Gammell:** I'll do it for you.

**Dave Jones:** Thank you very much. Yep.

**Chris Gammell:** Uh, I think things they will be making documentaries about someday, but, um, I think it'll be boring, uh, is about the, the current strife happening at Intel. Uh, that was.

**Dave Jones:** This strife.

**Chris Gammell:** Well, yeah. Pat Gelsinger, uh, resigned, uh, retired. Technically the CEO of Intel. Uh,

**Dave Jones:** and if I follow, bloody Intel, I don't care. Well,

**Chris Gammell:** I think it's a big deal because Intel has been kind of going down the shitter. Uh, well, that,

**Dave Jones:** that I've kind of heard. Um, yeah, right. Um,

**Chris Gammell:** they have been, you know, what's interesting about it is that they keep talking about, remember how like my prediction on here for years and years and years and years was like, ah, I bet they're going to get into the foundry business. And then eventually it was like, oh, they're getting into the foundry business. And now they want to get back in. Gelsinger puts, gets pushed out because they're so bad at the foundry business. It's like, oh, okay. Um, yeah. Yeah.

**Dave Jones:** But aren't they, aren't they building new foundries? Didn't they just get some new uncle, uncle sandbox to.

**Chris Gammell:** They did. Well, yes. Um, and I don't think they're giving up the foundry business, like, but like foundry, not the foundry, like, uh, not the actual fab, right? Like they are building new fabs, but the foundry business being like making, so basically like being a dominant process player, right? So like TSMC is a, is a foundry where they will, you show up, you buy their, you know, capability and they will make the top notch stuff. That is if they can squeeze you in after NVIDIA. Yeah. Right. Right. And it's like, okay, uh, they are foundry. They're the best example of a foundry. Samsung has some foundry capabilities, but they, that's not their main focus. Uh, AMD really, they spun off, they spun off global foundries, which is still an operation. Yeah. And many of the things that are around, even the ones that are like Skywater, the Skywater PDK that runs with the, I forget the name of the, the fab that's up North that runs all the open source stuff. That's also a foundry where it's, you know, you're basically fabulous chip companies are coming to you and doing that sort of thing. So like Intel started to get into that as opposed to famously for, you know, most of their existence was like, okay, we're doing our own thing. We're keeping all of our stuff secret. We're, you know, all of our, all of the best process stuff goes to us because we're bleeding edge and they've just fallen behind on all things. So like there are some documentaries out there about Intel and really just a lot of news stories about it. But the big story is that now their, their leader, uh, he, he gone, uh, and, uh, and now they have, uh, done the thing that really shows, uh, they have no idea what they're going to do, which is appointing dual CEOs, which means there's no CEO. That's, that's, that's always my take on that thing. It's like, Oh, dual CEOs. You mean you couldn't decide, or there was a fight in the boardroom?

**Dave Jones:** Yeah, right.

**Chris Gammell:** Who cares? But that means you guys don't have a leader right now because boy, even if they, they're both up on stage, they are, they, they, the knives, knives are out. You know what I mean?

**Dave Jones:** Right.

**Chris Gammell:** They are ready. They are ready to pounce.

**Dave Jones:** Yeah.

**Chris Gammell:** So Intel, uh, no good news there, uh, except maybe things will change, uh, maybe some shakeups. So we'll see. Um,

**Dave Jones:** I've just stopped hearing anymore. Like modern processes are just so like,

**Chris Gammell:** yeah, it's the access we talked about,

**Dave Jones:** the,

**Chris Gammell:** the Pi five, right? It's like that times a gajillion, right? I mean like, yeah, it's not for us today. We are the, we are the,

**Dave Jones:** yeah, but so that some gamer kid can, can get an extra two frames per second on there. You know, they're going, Oh, this one's two frames per second better than this one. Oh, no,

**Chris Gammell:** I mean, there are, there is some very significant, uh, I think, uh, national security interest stuff. Oh, I'm sure.

**Dave Jones:** But you know, like that's a very limited market, you know?

**Chris Gammell:** No, no, no, no, no. I'm saying like, I'm saying like, uh, national security in, uh, and also like all the AI stuff really the big, the big thing. I think the thing that Pat Gelsinger will be remembered for, and this is me speaking, not having read too much about it is that basically he just like completely seated to Nvidia, right? Like they're there. So TSMC kind of blew them out of the water on the process side of things. Uh, arm kind of took over some of the server, not completely took over, but AMD is nipping at their heels, arms nipping at their heels. Risk five is growing like crazy. Although, you know, still a small share of the market, but you know, longer term, I feel like risk five is, is the jam. And it's just like X86 has continued to play in the pools they played in, especially the server market where they're going to be they, but they just, they seeded all GPU stuff. Okay. And, uh, and then all the other stuff, they just kind of lost on lots and lots of fronts. So I, I don't think he'll be, uh, you know, I don't think he'll be remembered well, unfortunately, like as, as I'm sure he's a fine person. I don't know him. Uh, but I, I think that like when people look at his tenure, I think, I think they're going to be like, whoa, you really crap the bed, you know? So, uh, yeah.

**Dave Jones:** Well, was it a matter of like, was it a matter of them crapping the bed or was it a matter of them not being in that market and that market suddenly became huge and all caught them by surprise kind of thing?

**Chris Gammell:** I mean, you could say that. They were never,

**Dave Jones:** they were never big in the GPU space, but they, they, well, they did have their, you know, GPUs that were embedded inside the, um, the Intel processors and they were pretty good actually, especially for video encoding and stuff like that. They, they were pretty good, but they were never a dedicated GPU maker, for example. Well, they, well, there is one, they, they, they had some obscure one. What was it? It was called, I don't know, some, was it edit? No, what was it? Not Edison. It was some weird named after some inventor or something. I don't know, something like that. Um, but yeah, they, but they were never really in that market. So can they be blamed for losing that market that they never had? Sure.

**Chris Gammell:** Look at, uh, the only real competition I feel like Nvidia has is AMD and that's also Intel's competition. So it's like possible that large scale processor makers could do that sort of thing. So like, yeah, you can, um, it doesn't really have any impact other than like, uh, this is a huge brand that just, they were like, yeah, it's just, you know, going away. Not going away. It's, it's losing relevance really is what it comes down to.

**Dave Jones:** I've heard, uh, rumblings that Nvidia, they're not on the rocks, but they might be being handed their hat as the leader in AI stuff because there's a lot of, yeah, because apparently there's a lot of,

**Chris Gammell:** on X is the whispers on X day. Is that what it is? Absolutely.

**Dave Jones:** Because, uh, the, because new, new research comes out all the time in that, um, new AI algorithms in quote marks, right? That new, new ways of doing things makes the Nvidia stuff red redundant. And by next year, they could be there. Massive AI, a GPU things might be redundant. So because, because they've found new ways to do that AI stuff in way simpler hardware, way simpler hardware. So they don't need these massive a hundred millimeter by a hundred millimeter freaking dies, right? To, you know, and that are worth, you know, $200,000 each for each chip or something, right? They've found the ways to do that AI processing in, in much simpler hardware.

**Chris Gammell:** And,

**Dave Jones:** and, and this research is coming out all the time. So I, I wouldn't bet on Nvidia.

**Chris Gammell:** I, uh,

**Dave Jones:** is what I'm saying.

**Chris Gammell:** Uh, okay.

**Dave Jones:** Okay. You think I'm going to be wrong? Fine.

**Chris Gammell:** I'm just relaying. If we get a time machine, I can go back like 15 years. Yeah. I'm going to, I'm going to bet on Nvidia. Uh, sure.

**Dave Jones:** But I'm saying like into the future.

**Chris Gammell:** Yeah. I mean, they're super. I'm saying,

**Dave Jones:** I'm not talking about next year. I'm talking about, you know, maybe in five years time or something, they could lose the edge because they, they,

**Speaker ?:** they,

**Dave Jones:** the reason that they have the edge is because at the moment they need to make these massively huge, expensive dyes, complicated dyes, right? To do all this AI shit, right? You've got a, and only like, and they've just like mastered that sort of niche in the market. Right. And that's why the new X AI center, right? Oh my God. That has like a hundred thousand. Right. And then why it's, it's the world's biggest AI center. Why can't I talk about it? Cause you don't like Elon Musk.

**Chris Gammell:** That's exactly right.

**Dave Jones:** Dude, get over it. Seriously.

**Chris Gammell:** It's, it's, it's just such a load of hype and like, Oh man, it's like, you're like on there and you're like, Hmm, I'd like, I'd like some more Elon hype, please.

**Chris Gammell:** Dude, it's not hype. It's a real freaking AI center. Have you seen the video of how they made the damn thing?

**Chris Gammell:** I have not. No.

**Chris Gammell:** Well, there you go.

**Chris Gammell:** Hmm.

**Speaker ?:** Okay.

**Chris Gammell:** Dude.

**Dave Jones:** Just, just lose the Elon derangement syndrome a bit. And you might actually, you know, it's no, anyway, they have one of the world's biggest AI centers, right? They just built the damn thing with like a hundred thousand Nvidia GPUs, right? It's a massive AI center. And if you can do, and if in five years time, you can do that same thing on your shoe phone because they found new optimized algorithm, you know, not, not quite. I'm kind of, you know, being a bit hyperbolic there, but you know what I mean? Right.

**Chris Gammell:** Hmm.

**Dave Jones:** These, a, a, a new algorithm, a, well, a new way of processing that someone, one comes up with might make those really high end AI GPUs redundant. So, or not, not redundant, but you, you're chewing all that power when you can do it in much simpler, much cheaper hardware in a few years time.

**Chris Gammell:** I think the, I think the software folks are going to keep finding new uses for this kind of stuff. So I, I'm not, I'm not too worried about that. right?

**Dave Jones:** Yeah, maybe, you know, you, you know, you can pivot to something else. You can pivot to using that hardware for something else. You don't have to use it for AI. I don't think, I think it has, you know, fairly generic use. You can simulate your nuclear weapons on it. I'm sure, you know? Um,

**Chris Gammell:** so just let me get this straight. So, so you said, everybody's talking about a YouTuber with a copyright strike and everybody knows about the X AI thing, but you didn't know the CEO of Intel had, had been forced out into retirement.

**Dave Jones:** Uh, no, didn't. Okay. Just didn't happen to show up in my feed. Just went,

**Chris Gammell:** got it, got it. Okay. Not in your feeds. Yeah.

**Speaker ?:** Yeah. Okay.

**Dave Jones:** Fine. Simply tell me who I should follow.

**Chris Gammell:** I think what we're really saying to each other is we need to go touch grass. That's what, that's what the kids are saying these days.

**Dave Jones:** Right. Oh boy. Well, I'm touching more grass than you did. I can assure you.

**Chris Gammell:** You probably are. Yeah. Yeah. Uh, I, my favorite thing, uh, from this whole reading about, about, uh, Gelsinger is, um, actually one of the past guests of the show, he posted about the news article and he said, uh, uh, when it said that Pat was retiring, he said, this is Luke Wren based on historical trends. I predict the number of Intel co-CEOs will double every two years.

**Dave Jones:** That's good. That's good. I like that. It, it actually needs a name that, uh, it's Renslaw. Oh, Renslaw. Okay. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Okay. Great.

**Chris Gammell:** Yeah. Oh man. It's so good. Okay.

**Dave Jones:** I, I, I will endeavor to find that and, uh, repost that. Yeah. Yeah. It's so good. That's great. Oh boy. Well, how long did the last CEO, like, Oh, the CEO just got, he was only there,

**Chris Gammell:** I think four years.

**Dave Jones:** Okay. Yeah. Well, that's long enough. I guess.

**Chris Gammell:** My, uh, my stuff is so out of date that I'm like, when was Andy Grove there? Like last time I heard about Andy Grove, him passing away. I'm like, okay. Oh God.

**Dave Jones:** 80s, you know?

**Chris Gammell:** Yeah. He was, yeah. The 90s for sure. Like he was like, he was the growth. Um, yeah.

**Dave Jones:** Right. He was the growth guy. Yeah. Right. Yeah.

**Chris Gammell:** Yep.

**Dave Jones:** But, um, but then again, you know, the whole industry has been turned on its head in the last four years. Right. Totally. Yeah. How, well, you can say AI really hit its straps when chat GPT was released. That when, that's when it became into the public consciousness. That's when there was a mad scramble for every man and his dog to put AI into everything. And, uh, you know, it's going to change the world, blah, blah, blah. And then a hundred, listen, a hundred companies suddenly appeared on the bloody Aztec thing with, you know, AI in their name or whatever. Um, and yeah, so that's only been what? Three years.

**Chris Gammell:** It's when was chat GPT?

**Dave Jones:** Yeah. Since I, I know chat GPT was around before that, you know, it was around for, you know, a year or two before that, but you know, when it actually hit the mainstream, when chat GPT three, I think it was came out and yeah,

**Chris Gammell:** sort of, yeah,

**Dave Jones:** it's, it's not that long ago. So, you know, you can't spin the Intel ship in a few years like that. I guess it's hard, but I guess, yeah, being in the industry, they should have seen. Yeah.

**Chris Gammell:** They were already behind though when that came up. Right. I mean, like, yeah.

**Speaker ?:** Yeah.

**Dave Jones:** All right.

**Speaker ?:** Yeah.

**Chris Gammell:** You know, actually one of my markers for like when, uh, that stuff started happening was I go back through Amp Hour art and like, you know, like the early stuff. I think the Fry guy one was the first time we did, um, that was the one. The 604 was October, 2022 was the first time we did AI art. All right. Yep. on the Amp Hour. So that's.

**Dave Jones:** And now we're doing all the time. Cause it's just so easy and great. Yeah. It's easy. It's generic. Yeah. Yeah. Yeah. It's fantastic.

**Chris Gammell:** It doesn't really have much impact for us, but I think that was the first one. So that was 20, that was October 22.

**Dave Jones:** Hmm.

**Chris Gammell:** So.

**Dave Jones:** Okay. There you go. Yeah. Yeah. So it's only been a couple of years.

**Speaker ?:** Yeah.

**Chris Gammell:** Well, let me tell you about some software that is going to change the world, Dave. as you can tell, I'm really, really.

**Dave Jones:** We're, we're terribly excited about software.

**Chris Gammell:** Free CAD version one is now available. Yes.

**Dave Jones:** I'm so excited. I'm going into. We're out of beta.

**Chris Gammell:** Unfortunately, it is still free CAD. Um, so.

**Dave Jones:** Yeah. I tried it like, Oh my God, we're talking at least six or seven years ago or something. Oh my God. And people raved about it and said, just try this. Oh my God. That was garbage.

**Chris Gammell:** Yeah. That's real rough. That's real rough.

**Dave Jones:** No.

**Chris Gammell:** The new stuff is better. Um, and it's less broken. You're definitely going to have to learn like the free CAD way. Right. And so are you doing any modeling these days? Like the parametric? I feel like my brain is still like based on fusion 360. So even though I guess that's fusion 360 from like five or six years ago. So like, uh, that's like my basis for things. And I don't think, I mean, free CAD has its own flavor style of doing things and it's, I still prefer the old fusion. I'm very forthcoming about that. I don't, I don't like, it's definitely a lot easier in the other way. Um, but, uh, well, well changing the, you know,

**Dave Jones:** if they change the UI and stuff, that does a lot. I can remember. Yeah. OBS, right? Everyone, every man, his dog uses OBS. Dave, why don't you use OBS? It was because when I first tried it, it was, you know, like a decade ago and OBS was garbage. The user interface was garbage. That's why I use XSplit. Right. And then OBS decided to actually copy the XSplit user interface, like completely, almost down to the pixel. They, they copied the XSplit user interface. And then when I came back after that, I went, oh yeah, OBS isn't too bad now because they copied the XSplit interface, but I just kept on using XSplit because I've been using it forever. It's like, you know, so yeah, things do change. And sometimes you just, you know, I think that does matter. I mean,

**Chris Gammell:** like you get hired someone to start doing like logo or icons and like more UI, UX type stuff too. It does matter. You know, it's like, it's a workflow tool that you're in there every day. It's basically like, you know, you pay a physical therapist to make sure you get a repetitive, repetitive, uh, injury to, you know, sort of things. Like, yeah, like bad UI is like a repetitive injury that you're, you know, accepting. I don't know. So anyways, there, uh, there is a blog post. There's a video that kind of shows some of the new stuff, which is great. Um, I'm hopeful. I'm going to use it regardless, but, uh,

**Dave Jones:** I, once again, it's one of those things where I want a tool that just works. That just work. Like I just want to do the simplest shift.

**Chris Gammell:** I would know, I would just know what that is in the mechanical space though, too.

**Dave Jones:** I will tell you what it is in the mechanical space. I used a machine shop, right? Back when I was designing my scientific calculator watch, right? I wanted to design my own custom case, right?

**Chris Gammell:** But is that because you knew it? Like,

**Dave Jones:** no, no, I downloaded it and it just let me do shit in the first couple of minutes of me using it. It was okay. I draw a drag here, draw a rectangle around these corners, do a cutout, you know, like it just worked. And I tried all these other CAD tools including free CAD and all bloody every CAD tool out there. And they were all just garbage. No, I had to watch a bloody two hour tutorial just to get a box with a hole in it. You know, no, it's bullshit. You know, and then on top of that, it gave me, and then you could analyze this, this e-machine shop software. Not only was it just intuitive for a dummy like me to use, but then it would tell me that, no, you cannot manufacture that because the in cutters, you know, the router bit's going to be too small, blah, blah, blah, you know, and it would highlight or it would do all these DLC kind of errors.

**Chris Gammell:** This is like a, this is from the actual manufacturer. Is that right?

**Dave Jones:** E-machine shop is a company that manufacture parts, but they also have their own software.

**Chris Gammell:** Ah, okay.

**Dave Jones:** Yeah. So I assume they're still going. E-machine shop.

**Chris Gammell:** Yeah,

**Dave Jones:** yeah. Yeah. And they've got their own, I assume they wrote it themselves, but yeah, they've, they've got their own, free 3d CAD software. It's like the mechanical equivalent of one of those online. PCB places that have their own software. What's their, this is like the JLC. The JLC have their own software, right? What's it called? Oh, yeah. The, the JLC PCB software, right. Which is free to use. And, and it's great if you're just doing the stuff, you know, maybe. Yeah.

**Chris Gammell:** And it's like the tech coupling to the manufacturing, actually. That is the benefit. Yes.

**Dave Jones:** And that is about, once again, this is, that's a benefit with the e-machine shop. So for you is that it ties into their manufacturing capabilities. So they know exactly what they're capable of manufacturing. And it just instantly told me that, you know, they can do it.

**Chris Gammell:** I'm trying it right now. I am not seeing what you're seeing. I'm trying the, the web version. Maybe you did the, Oh, okay.

**Dave Jones:** No, no, it was executable back when I did it. Um,

**Chris Gammell:** I can't figure out how to extrude. I probably shouldn't be doing this live. I should be. Yeah.

**Dave Jones:** Well, okay. Right. But yeah, but I,

**Chris Gammell:** yeah,

**Dave Jones:** but I, I figured it out in five minutes and I had this magical new scientific calculator watch case all done. And I was posting it on the calculator forums at the time and everything, everyone was going nuts. Cause I had all these 3d drawings in like hours of posting, you know, like, yeah, it was like, it was really cool.

**Chris Gammell:** So it's interesting. Like, I think it always comes down to those kinds of things too. It's like really, so, you know, respect. That's great. Like use the tool that works. Right. Yeah. Um, it, the interesting thing in that case is always, man, I cannot get this to work. I got to close this. This is not working for me. Um, uh, where, where does it run into stuff? So like, are you gonna have to reduce stuff at a certain point? Yeah.

**Dave Jones:** Yeah. Yeah. Yeah. Of course. But, but sometimes I don't want to get that complex, right. Just like somebody's doing a PCB. Don't they don't want to get anything more complex than the little, uh, do we know double-sided board, you know,

**Chris Gammell:** plug on times that the JLC software or, you know, equivalent from other manufacturers, right. It would have been,

**Dave Jones:** yeah, totally.

**Chris Gammell:** Cause like the tight coupling means you can't buy what doesn't exist. Like I try to do on my designs.

**Dave Jones:** All right.

**Chris Gammell:** Yeah.

**Dave Jones:** And yeah, it's, you know, there are, there's a market for those sorts of software. So I won't begrudge anyone's, Oh, you must go and use Altium or you must go and use, um, key cat or something like that. You know? No, if, if that works for you, great. Use it. Fantastic.

**Speaker ?:** Yep.

**Chris Gammell:** Yep.

**Dave Jones:** Yep.

**Chris Gammell:** I think we're racing towards key cat nine as well. So,

**Dave Jones:** Oh, there you go. Yeah. I haven't even used key cat eight yet.

**Chris Gammell:** Free cat one.

**Dave Jones:** All right.

**Chris Gammell:** You get nine. Yeah.

**Dave Jones:** Free cat. What?

**Chris Gammell:** It's 1.0. That's, that's why it's a big deal is because it's been a zero dot blank for years and years and years and years and years. So that's why it's a big deal. Cause it's like a first official supported version. Like that's, yeah. So it's like coming out of beta effectively, but it's really just like, it's like they're, they're grown up, you know, that's cool.

**Dave Jones:** Right. Oh,

**Speaker ?:** yeah.

**Dave Jones:** That reminds me. Oh, what, uh, DJ Delorey, DJ Delorey, who I, who I've met at a conference once. He was a, he was a similar background to me. He used to publish, uh, projects in the magazines, win, win contests, DJ Delorey, um, if you look at, I've got an interview with him, uh, way back.

**Chris Gammell:** That's maybe what I'm thinking. Yeah, that's what I'm thinking. Right. He,

**Dave Jones:** he, he actually wrote his own PCB software, which was, um, uh, oh, he was the major contributor to it. Um, what was it called? Oh God, I'm, I'm trying to look for it now. Do you, um, G, G E D A, G E D A.

**Chris Gammell:** Oh, okay. I know that one. Yes, yes, yes, yes.

**Dave Jones:** G E D A. He's, he was the main, I don't know if, if he actually started it or he was just became, he just become the main coder for G E D A, G E D A PCB, you know? And it's like, yeah, G E D A is an open source, um, thing. It's same as key cat. In fact, it probably would have been better than key cared back in the day. Um, so yeah, but key cat just took off and, you know, got lots of support and et cetera. And a poor, G E D A didn't. So anyway, um, yeah.

**Chris Gammell:** Yeah. I remember G E D A because, uh, uh, Wendell from evil man scientists, he was a big fan of it.

**Dave Jones:** Oh, was he? Okay. Right. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** There were a few people who were, you know, fanboys of, uh, G E D A, you know, cause it was open source back before open source was cool.

**Chris Gammell:** I remember they had a really good, uh, I used the, the Gerber tool from G E D A. That was a really good shirt. Oh, okay.

**Dave Jones:** Oh yes, it was. I think I may have used that at one point. Yeah, that's right. Yeah. Yeah. Yeah. They had a separate tool, right? That, that did Gerber's. Yeah. Yeah. Yeah. Anyway, hi, hi to DJ if he's listening. I'm not sure what he's doing these days, but, uh, yep. Yep. He's cool. And, uh, Jeter, I haven't heard of any, I haven't heard of Jeter in the last 10 years, maybe. So, yep. Yep. Yep. Yep. I think it just, yep. Died on the vine, so to speak. Yep. Sad, but you know, there can be only one.

**Chris Gammell:** Sure. Yeah.

**Dave Jones:** Well, there can be only one big open source one that's going to dominate. I think, I think with any tool like this, but no, you disagree.

**Chris Gammell:** Well, I guess it depends on the size of the industry, but like, look at like, I don't know, JavaScript projects and there's, you know, a bunch of massive projects, but maybe if you, if you do like the, the Venn diagram of like, uh, people who are good at writing C plus plus, people who want to work on tools and people who actually know how electronics works. Yeah. There's probably a pretty small group of people that are like, like that group of developers and like open source enthusiasts as well. Yeah. That's probably not big enough to support a ton of projects.

**Dave Jones:** Yeah. Got it.

**Chris Gammell:** Yeah.

**Dave Jones:** That's why I think key care became the dominant sort of, you know, and there are, you know, a few other open source ones out there, but yeah, it,

**Chris Gammell:** it just became because of me, Dave.

**Dave Jones:** Right.

**Chris Gammell:** Right. It's all you. It is not, but I'm very excited that many people are using it. That is, that is for damn sure.

**Dave Jones:** It's great that there is an open source option out there.

**Chris Gammell:** And they keep having conferences too, that I just hear about. Like there's a, okay.

**Dave Jones:** Right.

**Chris Gammell:** In China, there's actually a bunch of great talks. Yeah. They had one in Shenzhen. They had one in Germany. They had one. I don't think they've had one in the U S in a while. They had one in Spain last year. So I think they're doing kind of like a couple per year now, which is great.

**Dave Jones:** Is, uh, does anyone know, please let us know, does China still predominantly use Altium? Cause Altium used to just dominate China. It just like, they weren't paid for copies. They were almost all illegal copies, much to Altium's. In total disgust. But, uh, um, yeah, it was, it was just the package in all of China. It's like, if, if you had some farting gadget, you know, that was almost certainly designed in Altium, you know? Yep. Yep. So, yeah, it was just the thing. So that'd be very, and that's why, yeah, I mentioned that cause you know, they had a KK conference in China. Interesting.

**Chris Gammell:** Yeah. Yeah. There's a bunch of talks. I'll post a link to the YouTube channel. There's some good talks, a lot of them.

**Dave Jones:** Very interesting.

**Chris Gammell:** Yeah.

**Dave Jones:** All right.

**Chris Gammell:** Looking at, oh, so Dave mentioned I'm not on Reddit as much. I am posting stuff occasionally to the contextual electronics forum. That would be the place to look if people are interested.

**Dave Jones:** There's a contextual electronics forum?

**Chris Gammell:** Who knew? Who knew? Yeah. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** That's also where the consultants forum, if you've heard me talk about that. Oh, okay.

**Dave Jones:** Yes. Right. Oh, there's a sub, there's a subsection on there. There's a private section that is for consultants. Okay.

**Chris Gammell:** You can apply using a link on the front page of the consultant contextual forms. Cool. But I'm also posting just kind of articles live about our good friend Matt. Matt Venn is doing the zero to ASIC analog courses starting up. Right. There was an El Camtuf post. That was fun. Quick tell parts are going to be made in Ohio. Did you hear about that?

**Dave Jones:** Nope.

**Chris Gammell:** Yeah.

**Dave Jones:** You're all stomping ground.

**Chris Gammell:** Yeah. I don't know what part of Ohio. It's really interesting. Like they're because of, you know, who knows what tariffs are going to be in the new year. I'm sure we'll talk about those in depth as things change, but they're going to try and basically quick tell is actually like teaching the people in Ohio. how to build quick tell parts in Ohio. So they're like setting up a new manufacturing facility. It'll be truly us made, but with like Chinese IP and Qualcomm chipsets. And it's just like, Oh, this is a weird world. Interesting.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. Yeah. I'll, I'll get that into. Yeah.

**Dave Jones:** Awesome. Local manufacturing. Love it.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** I can see why you don't like Reddit anymore. My, my page is just filled with ads. Like every third one. It's almost like an ad.

**Chris Gammell:** Uh,

**Dave Jones:** like do those go away if you log in?

**Chris Gammell:** If you go to old. old.reddit.com is better. It's the old way of doing things.

**Dave Jones:** okay.

**Chris Gammell:** Yeah. And that works on all pages, I think. So. Okay. Yeah.

**Dave Jones:** All right. That's the old view. That's like, yeah.

**Chris Gammell:** Oh, if you're not logged in for sure. Yeah. Yeah.

**Dave Jones:** Okay. Right. Because I am using different machine at the moment. Yeah.

**Chris Gammell:** Yeah. All right. Well, yeah. Lots of other links there too. Thanks to unmanaged for posting stuff there. And, uh, we'll continue to do posting to multiple locations. If people have thoughts, you can always email us at feedback at the empire.com. And, uh, we'd love to hear from you.

**Dave Jones:** Awesome. Catch you next time.

**Chris Gammell:** See you soon. Bye.

**Speaker ?:** x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
