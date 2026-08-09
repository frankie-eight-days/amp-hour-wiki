---
episode: 145
title: PCB Mills, SDR and Oscilloscopes - Flaunting Furbelow Fanciness
url: https://theamphour.com/the-amp-hour-145-flaunting-furbelow-fanciness/
---

**Chris Gammell:** This episode of the Amp Hour is sponsored by Club Jameco, part of Jameco Electronics. Have you ever wanted to sell a kit you dreamed up? Do you have an idea for a new project you're working on and you think others would like working on it as well? Club Jameco allows you to upload your kit ideas and start selling to your peers. You can earn up to 10% on every approved kit that you sell. Additionally, if you submit an approved product brief, you will get a coupon code for 10% off your next order at jameco.com. To learn more and to see the chosen kit of the week, go to clubjameco.com slash theamphour. This is the Amp Hour Podcast. Recorded May 14th, 2013. Episode 145. Flaunting. Furbelow. Fanciness.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Chris Gammell's Analog Life.

**Chris Gammell:** Who is no longer shirtless. No, I have a shirt. I have four shirts, actually. I have more shirts than anyone.

**Dave Jones:** Four? You bought four. Four?

**Chris Gammell:** Well, no, I have the early prints of the new colors that should be coming soon. So I bit the bullet and took one for the team. And I have all of the available shirts so far.

**Dave Jones:** And of course, folks, we're talking about the Amp Hour t-shirts.

**Chris Gammell:** Amp Hour t-shirt.

**Dave Jones:** Which, if you don't have an ordered one, you missed it.

**Chris Gammell:** Well, they missed the good pricing on it, basically. We'll have the Printfection store up soon. Right. Possibly this week, actually.

**Dave Jones:** Where are you getting those samples from? Are you getting them from Teespring or are you getting them from Printfection? No, no, Printfection.

**Chris Gammell:** Printfection is the... That'll be our... You know, if people want to buy at any point, basically, it's like an on-demand service.

**Dave Jones:** Yeah, but it costs more than the campaign. Yeah. So what's the quality of the campaign, the Teespring shirt like?

**Chris Gammell:** Oh, Teespring's awesome. Is it good? Actually, I've got it right here. It looks kind of weird because of the different... You know, like the kind of... The Warren effect. Right. But... Oh, yes.

**Dave Jones:** Because that's hand... It's hand-drawn, kind of worn look. Yeah. Right? To the image. That's... Right.

**Chris Gammell:** But if you step back one step, it looks quite good, I think. So...

**Dave Jones:** Ah, right. Okay. Cool. Yeah. I haven't got mine yet, being in the back water here.

**Chris Gammell:** Right. Yeah, you'll probably get yours this coming week. So... Yeah. Lots of fun, though. And people have been sending pictures on Twitter and elsewhere, and that's really great. I've been trying to retweet all of them. So thanks to everyone who posts pictures, it's... I mean, it's not the main point, but it is, you know, it's helpful for the show to, you know, people showing their support. We really appreciate that. So that's really cool. Absolutely. And making people jealous, because the shirt does look pretty sweet, I think. I mean... Yeah. I think it's pretty awesome. Yeah.

**Dave Jones:** Haven't got mine yet. I'm jealous.

**Chris Gammell:** Yeah.

**Dave Jones:** Ah.

**Chris Gammell:** Yep. Yeah. Well, t-shirts are fun. And we'll do more in the future. So it's not the last one. But we'll give it a break for a little while. Yeah, I think so. You've had your fun with t-shirts, too, so...

**Dave Jones:** I've had my t-shirts, yeah. They're both finished. They're both complete runs. Yep. And so everyone will be getting those in the coming weeks, including me. I still don't have one myself.

**Chris Gammell:** Oh, yeah. Yeah.

**Dave Jones:** Sob.

**Chris Gammell:** Yep. Well, and we can wear them, well, at least in the States. Next weekend is Hamvention in Dayton. Yep. And then Maker Faire out in California. So hopefully...

**Dave Jones:** So if you're wearing a... Is there like a secret handshake to go along with the t-shirt? So if you see another person wearing the t-shirt, you do the secret Ampower handshake?

**Chris Gammell:** You look down at the ground and kind of mumble something. That's what... Yeah. That's what I would do.

**Dave Jones:** Like a nod. You know, you walk past and... You know, that nod. You give someone... Yeah. Yeah. Someone wearing the same t-shirt as you.

**Chris Gammell:** That's the downside.

**Dave Jones:** But we will be... Can you get a photo? Can you get everyone to coordinate who's wearing an Ampower t-shirt at the one location at the Hamvention and get a group photo?

**Chris Gammell:** Oh, that'd be great. Yeah. We'll try and do that. So we're going to have a meetup at the Hamvention. So definitely I'll get photos there. Oh, okay. Well, there you go. Yeah.

**Dave Jones:** Turn up at the meetup.

**Chris Gammell:** If people are going to that, it's 6.30 on Saturday night at a place called City Pub, a little bit south of the city. But hopefully it should be easy. City Pub? City Pub. Is it actually a pub? It's a gastropub. It's like good food and stuff. So... All right. And Kent Lundberg, Dr. Analog will be there. Or hopefully be there. I think... Or maybe he won't be at the meetup, but he'll be at the convention. But then Greg Charvat will be there. And then I'm not sure if any other former guests will be there, but definitely lots of other listeners. So if anyone else is listening and hasn't let me know yet, I'd love to know if you're going to be there. I'll be on Twitter probably posting pictures and taking video. Live updating. Yep. Yeah. Yep.

**Dave Jones:** And then turn up for the group photo.

**Chris Gammell:** Yeah, definitely. That'd be cool. I'm excited. It's... You're going...

**Dave Jones:** You're so excited. You're going internally berserk. I can hear it.

**Chris Gammell:** Internally berserk. Yep. Yep. I don't know. I see all this press for Maker Faire, too. It seems like there's going to be a lot of good stuff in Maker Faire, too.

**Dave Jones:** And that's on the same time, isn't it? Same... Yeah. Right. It's on the same weekend.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Right.

**Chris Gammell:** So, eh, got to choose sometimes, but we'll see how...

**Dave Jones:** Which, uh, fair is this? Which...

**Chris Gammell:** Maker Faire? Where's it at? California. San Mateo. Ah. Oh, right.

**Dave Jones:** That's the big one, right? That's the biggest one. Yep.

**Chris Gammell:** Yep, yep, yep. And, yeah, people said that, you know, Jeff said he'll be out. The Jeff Kaiser will be out there.

**Dave Jones:** Yeah, he's got some new project he's showing off. Another Geiger counter thing, which pulsates, leads pulsate or something. Yeah.

**Chris Gammell:** Jerry said she's going to be there showing stuff off. So, I think, yeah, a lot of people. Cool. A lot of past and future guests, hopefully. So, good stuff. Very exciting time.

**Dave Jones:** Once again, eh, I won't be there.

**Chris Gammell:** No.

**Dave Jones:** No.

**Chris Gammell:** Sorry. Throw your own Sydney party, man. You gotta... Yeah. You guys have Maker Faires and stuff now, so that's good.

**Dave Jones:** Well, yeah, there's been two. One was in Melbourne. Yeah. And one was in, which I didn't go to, and one was in Adelaide, which I wasn't allowed to go to.

**Chris Gammell:** Wasn't allowed to go to? In lockdown? Come on, dude. You're married? Oh, yeah. Well... You know what it's like. She's letting me go to Hamvention, so... I don't know, man. Right.

**Dave Jones:** How far is it to Hamvention? You just drive, right?

**Chris Gammell:** Yeah, it's only three hours. Yeah.

**Dave Jones:** Ah, pfft. Yep.

**Chris Gammell:** Yep. And speaking of Hamvention, I was talking to Mr. Kaiser the other day, and he said he's gonna be on the show soon to set you straight on ham radio. Apparently, I'm not doing a good enough job on the benefits. He said he's gonna convince you to get your technician's license, too. No. I was skeptical, but you know, never know. You never know.

**Dave Jones:** And then what am I gonna do with it? I'm just gonna end up like you. Just a poser with a call sign. Hey. Hey, now. I have two radios now. And a cheap Chinese handheld radio.

**Chris Gammell:** I have two cheap Chinese radios. I got a software-defined radio, too. Did I tell you about that? Even worse, isn't it? No, it's cool. It's really cool. It's one of the... This is a great one. I actually learned about this from Matt Richardson's video on software-defined radio. He talked about... He shows the... It's actually... I think this would have been a good thing to get first, because you don't actually need a call sign, either. You don't need a license to get one, actually. No, of course.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, because you're just receiving.

**Dave Jones:** Yeah, but you aren't transmitting. You're just receiving.

**Chris Gammell:** Right, but see... Okay, so here's the thing. And this is... So this is an important thing, I think. So people that are out there who are interested in radio or anything else like that, I've taken, you know, signals courses, everything like that. I remember there's been, like, discrete points in my life where I've taken courses, you know, but it just didn't click, you know? Like, Fourier transforms. That took me, like, probably two months of actually doing the math before it actually clicked. That's how pathetic it was. I mean, like, it was that bad. And then it clicked, and it was like, oh, hell yeah. And then, like, you know, I actually had, like, you know, I had a co-op that used those a lot and everything. And, you know, it was good after that. But I'm just saying, like, you know, having that kind of context is really important. And that's why I really like this software-defined radio thing because it is basically the perfect way to illustrate bandwidth. Like, it's not a great radio. I mean, I know that. It's very wideband. You know, you can go from, like, I think it's like 200 megahertz up to, like, 1.2 gigahertz or something. But it's cool. I mean, you can – actually, it's probably lower than that because you can get broadcast stuff like broadcast FM. And you can see it, you know. That's the best part. You actually can see, you know, like, learning about, like, FM, frequency modulated signals, like, on a radio. It's, like, really hard to conceptualize at first. But once you see it on this SDR screen with, like, a – what is it called? I forget what it is. C-sharp script or something like that. Basically, it allows – it actually takes the input data and then it visualizes it for you. Right. Those two things together, nothing – I just wish I would have had that about, you know, 10 years ago. 10 years ago. Jesus. When I was a boy. Yeah, right? When I was a student. I just wish I would have had it. So that's why I like it. It's 20 bucks. I'll post a link to it.

**Dave Jones:** Yeah, this is one – just one – if you don't know what he's talking about, just one of these 20 buck USB dongle. Yeah, they're meant for, like, digital TV. Right. For, like, watching TV. Yeah, designed for digital TV.

**Chris Gammell:** Right. And I don't know if I'm going to ever use it for that. But, you know, more important, though, is actually seeing – because it shows – and it shows the spectrum over time, too. That's another really great thing. You know, like, seeing those two things together, I just wish I would have had it before. So now I do. Awesome. It helped me verify that I wasn't going crazy. You know, like, the spectrum is actually, like, really, really barren around here because I'm out in the boonies. Okay. I'm in the suburbs of Cleveland. And so there's, like, you know, my crappy Chinese radio, as you say it. It can only go so far. And so if there's no repeaters in the area and I can't pick up, like, you know, like, long-distance stuff, then, you know, I'm kind of SOL. You know, I just – I'm just kind of sitting here, like, I don't know – there's no way to troubleshoot at that point, right? You know, like, there's no –

**Dave Jones:** And just talking into the ether.

**Chris Gammell:** Yeah, exactly. Hello?

**Dave Jones:** Anybody?

**Chris Gammell:** Yeah.

**Dave Jones:** Anybody out there?

**Chris Gammell:** Yeah, and that's what it was like at first. And then I got this SDR thing, the software-defined radio, and then I could actually see it. And then if I missed a transmission from someone, I could see that, oh, there was something there a minute ago. You know, I could actually, you know, then wait for it to come back. So it's cool.

**Dave Jones:** What just popped in my head then? Sorry, totally non-sequitur – not – what did I say?

**Chris Gammell:** Non-sequitur?

**Dave Jones:** Yes. That's it. That's what I meant to say if that's not what I actually said.

**Chris Gammell:** No, you didn't say that at all. It's okay.

**Dave Jones:** That reminds me of the NASA video of Commander Hatfield is his name. Yeah, Chris Hatfield. He's up on the International Space – yeah, you've seen it, right? Yes. I'm sure. I watched it this morning. Yes, he sings – yeah, David Bowie's a space –

**Chris Gammell:** You mean David Jones?

**Dave Jones:** Oddity. Yes, David Jones.

**Chris Gammell:** David Jones, yes. That's the real name. Yeah. Right.

**Dave Jones:** David, which you didn't know until I told you.

**Chris Gammell:** No, I didn't. You're right.

**Dave Jones:** I can't believe it. You big muso, you.

**Chris Gammell:** Yeah, well, not that big apparently. Well, you're supposed to. You had a band. Yeah, yeah, I'm supposed to, right. Well, I – You had T-shirts and everything. I focus on the music. I focus on the music, man. You know? Right.

**Dave Jones:** Anyway, it's awesome. You've got to watch it. Yeah, it was really well done. Yeah, it's great.

**Chris Gammell:** Yeah, Tim –

**Dave Jones:** Why someone hasn't done that before? Well, you've got to actually sing. You know, you've got to be able to actually hold a note, which he can, I think. It's quite good. It's very well produced, too. It is, right. Anyway, he's up in the International Space Station, and he's singing David Bowie's Space Oddity. It's fantastic.

**Chris Gammell:** I didn't realize he was Canadian. I learned that today. I just, you know, make horrible yank assumptions, right? I'm just like, oh, yank assumptions.

**Speaker ?:** Yeah, of course.

**Chris Gammell:** He's an astronaut, right? If he's not a cosmonaut, he's an astronaut, and he's a U.S. guy, right? And it's like, no, that's not true, so.

**Dave Jones:** Yeah, it's the ultimate insult, especially like tourists come here, you know, and you hear them speak with a, you know, what sounds like a yank accent, but then you go, oh, you're Canadian, aren't you? And they go, oh, yes, thank you. Thank you for not –

**Chris Gammell:** Finally someone got it.

**Dave Jones:** For not thinking I was a bloody American.

**Chris Gammell:** Yeah, well.

**Dave Jones:** Yeah, they're so thankful. Oh, well.

**Chris Gammell:** It's the ultimate insult. Whatever. Whatever. I'll take my lottery winnings and be elsewhere. Boy.

**Dave Jones:** All right. What else? Well, I cannot – speaking of America, I cannot apparently do the Cleveland – at least we're not Detroit.

**Chris Gammell:** No, you can't. Well, some people say you can, but no. Right. I think Detroit has passed us an awesomeness, irrespective of the awesomeness of – It may have, yes. It may have. Recent events in Cleveland and some of the characters involved with that.

**Dave Jones:** Ah, right, yeah. Well, what does Detroit have to offer, Chris? Tell us about –

**Chris Gammell:** A 10-foot tall RoboCop statue. How can you beat that?

**Dave Jones:** Get along with that police state mentality. Yeah. Oh, yeah. All right. So it'll become a symbol of all the right-winger, you know, and others. No. No. It'll be –

**Chris Gammell:** It is a symbol of a crappy 80s movie held in Detroit.

**Dave Jones:** They'll be shooting at it with their assault rifles from 1,000 meters away, you know.

**Chris Gammell:** Shouldn't have brought it up. Yeah. Sorry.

**Dave Jones:** Anyway, it's very cool. It's like – It is cool. How tall is it?

**Chris Gammell:** 10 feet or what? Three and a quarter meters? Whatever that would be. Looks more than that.

**Dave Jones:** Oh, yeah, maybe. The guy standing next to it is probably six. Yeah. Right. Okay.

**Chris Gammell:** Yeah. All right. Very cool. Yeah. Kickstarter campaign. Yeah. Yeah, just because you like saying that so much, you know. We wish we were Detroit. I don't know. The tech scene up there, too. I mean, like, I see a lot of stuff about, you know, just Detroit tech coming back and stuff, too, you know. Obviously, they've still got the auto industry. There's no denying that, you know.

**Dave Jones:** There's something left there, anyway. I don't know. Oh, I think the significant is still there.

**Chris Gammell:** No. I mean, they manufacture – Sorry.

**Dave Jones:** I just insulted all Detroitians, didn't I?

**Chris Gammell:** Detroitians? What the hell do they call themselves? Detroiters. Detroiters?

**Dave Jones:** All right.

**Chris Gammell:** Detroit residents? You know what they call themselves? Canadians. Yeah, right.

**Dave Jones:** Of course, I'm from Canada. What do Clevelandites call themselves? Do they call themselves Clevelandites? Clevelanders. Okay. Yeah. Right.

**Chris Gammell:** Clevelanders call ourselves Canadians.

**Dave Jones:** Right.

**Chris Gammell:** Yeah, from Canada. Eh?

**Dave Jones:** I don't know what we call ourselves in Sydney. I guess we call ourselves Sydneysiders. Oh, that's kind of cool. Nothing else springs to mind. I don't know. Yeah. No. Sydney. Sydney. At least we're not Melbourne. Oh, boy. Anyway, this is very cool. Yep. Yeah. 12-foot high Robocop statue. I think it looks great. Like, it's just like all 3D printed or something, like a wax casting or something. They're going to make a bronze. It's just the casting that they're going to do the bronze thing. But when they bronze this, I don't know, how does the bronze casting work? Is this like the internal mold that's actually destroyed when you bronze cast it? I don't know. Because it seems a shame. It's fantastic. It's fantastic. Well, it depends what they made it.

**Chris Gammell:** I don't know what they made it out of.

**Dave Jones:** Well, here we go. Made from foam, wax, clay, and steel.

**Chris Gammell:** Oh.

**Dave Jones:** There you go.

**Chris Gammell:** And yeah, they'll probably create a relief for that then. Because some of the ones... So I know very little about molds as yet in my machining journey. But the one that's really easy is like if you do wax, then you basically encase that in sand. And then you pour liquid metal into that. And it just evacuates the wax, basically. Oh, okay. Got it. Lost investment casting, I think it's called.

**Dave Jones:** Right. Yeah, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. But what happens to the wax? It doesn't just magically vaporize, does it?

**Chris Gammell:** No, it flows out, basically. It gets displaced.

**Dave Jones:** Oh, it flows out, right. Yeah. Okay. Right, it just comes out as a bubbly ooze at the top or something.

**Chris Gammell:** Yeah, right, right.

**Dave Jones:** Right.

**Chris Gammell:** Yeah, and there's some intense videos. Like people will do... There's a couple of hackerspaces around that'll do... They'll actually smelt the aluminum. And then they'll actually... You know, they'll do like multiple setups at once. And then they'll pour them all. And it's very impressive to see. Yeah. Aluminium. That's not smelting? Oh, oh, oh. Gotcha. Gotcha.

**Dave Jones:** Get it right. Aluminium. Right, sorry. Right. Bloody yanks. Yeah. Rest of the world says aluminium. Okay. Enjoy that. Unbelievable.

**Chris Gammell:** Next. Well, speaking... I want to mention one more thing in Detroit. I don't know if it's actually Detroit. No. It's definitely Michigan, though. There's these great videos from the Geek Group. Oh, it's actually Grand Rapids. So that's not Detroit. Right. Not even close. But it is Michigan. And the Geek Group... Have you ever seen these videos before? No. Yeah. Tell us about them. I had found them from machining stuff. They're really well-sponsored. They have, like, you know, great Tormac-sponsored everything, basically. But really, really awesome videos for machining and even some electronic stuff, some Tesla coil stuff. And they're just... It looks like they're going, like, really pro. I mean, that's more geeky from the video side. But they make some really great videos. And I highly recommend their YouTube channel. So just another... You know, they're kind of like a tech shop but focused on making videos and educating and stuff. So really cool.

**Dave Jones:** I'll have to subscribe.

**Chris Gammell:** Yeah. You will. Better. Awesome. Yeah. So, speaking of...

**Dave Jones:** We've got another retro video.

**Chris Gammell:** Oh, yeah. Yeah.

**Dave Jones:** Retro video time, folks. Did you watch this one? Retro video of the week.

**Speaker ?:** Yeah.

**Dave Jones:** It's great. Yeah. Board Scope. No, what is it? It's a...

**Speaker ?:** It is...

**Dave Jones:** Cadnetics from the 80s.

**Chris Gammell:** Right. So it's... If people remember Dasics... So it was Daisy and Cadnetics. They merged and they became Dasics. And I've actually... I've had to deal with the aftermath. That's bad. I'm sorry. Oh, I know. Yeah.

**Dave Jones:** It's like, well... You're dealing with the aftermath of this?

**Chris Gammell:** I used to have to deal with the aftermath of it. It was like a former CAD system. And so basically... Legacy designs, huh? Yeah. Yeah. All we had was the Gerbers and everything else is... Right. You know, it's just like older CAD systems. You know, you just don't have the files anymore. Or they're... You know, they're only on tape. You know, it's... You just kind of... Well, seriously. I saw... Yeah, I know. Someone was telling me about cloud storage. Or I was reading an article or watching a video or something. They said almost all cloud storage, eventually, if you don't access the data long enough, it'll end up on tape.

**Dave Jones:** Yep. End up on tape. Didn't we mention that? Oh, no. That was Alan.

**Chris Gammell:** Of course. Duh.

**Dave Jones:** That was who... Yeah, duh. Of course. It was... Duh. That's right. I'm sorry.

**Chris Gammell:** Yeah.

**Dave Jones:** I thought it was.

**Chris Gammell:** Yeah. I knew it sounded familiar, right? So much happens week to week these days, you know?

**Dave Jones:** Anyway, this is very... This is... It goes for like 10 minutes. It does. This video. And I haven't watched it all, but yeah, it's 80s, folks. Say no more.

**Chris Gammell:** Yeah. Founded through... VHS. VHS. You know. Former guest Steve Leibson, he knew the guy that was in this, apparently one of the actors, quote unquote. But yeah, it's intense. It's a 10 minute marketing video. So which means that there was no YouTube, so there was no distribution of this. So that means that they probably... You know, you had to write into them and they sent you a tape. Yeah. Yeah. And then you sat down and watched it. Yep. It was not good, though. This makes Dave's production quality look like, you know, like multi-million dollar studios.

**Speaker ?:** Right.

**Dave Jones:** They've put a lot of effort... Like, they've hired a company. They've clearly, like, hired a video production company to, you know, do the whole thing. It's not like an in-house... I don't think it's like an in-house thing. No, I don't think so either. I think it's a... Yeah. It's a professional... Yep. And there's 80s haircuts in there. Oh, yeah. Yeah, that's fun spotting. There's a meeting room, boardroom, action, token. Yep. And then there's a token engineer. There's a token CAD engineer who's the only one with a college shirt without a tie. Yep.

**Chris Gammell:** You know? Well, you don't want it to get caught in anything, but it's...

**Dave Jones:** No, no, exactly. Yeah, you wouldn't want to get caught in the keyboard or something, right? That's the excuse, right?

**Chris Gammell:** Oh, I don't have to wear a tie. I don't have to get caught in something.

**Dave Jones:** Oh, that's hilarious.

**Chris Gammell:** I love it. I think the product was actually for... The one they're talking about in there is actually this simulation software for simulating board-level traces. And then they're showing, oh, well, we don't have time to debug these traces. And it's like, well, maybe you got these fat right-angle traces for dip packages and everything. It's like, oh, okay. Well, strike one. We can't go too fast or else we will fail in production.

**Chris Gammell:** Well, yeah. You know?

**Dave Jones:** I love the screenshots of the software. It's all very vector-like. Yeah. You know? There's no, like, solid renderings of solid colors and shapes and things like that, you know? Let alone, you know, a 3D image of the board or something like that. Yeah.

**Chris Gammell:** It looks like old AutoCAD, right? That's kind of like the look. Yeah, yeah. Top-block background. Yeah. I imagine it must have been really tough. That's all I can really think about it, you know? It's like...

**Dave Jones:** Well, it was. You know, I come from the days of, you know, Altium slash Protel, back when it was called Protel, for DOS 1.6.

**Chris Gammell:** Oh, wow. You know?

**Dave Jones:** Yeah. Yeah, this was back in, you know, the late 80s. I was... Oh, yeah. I was using that, yeah, in the late 80s. I was using Protel for DOS 1.6. When Altium first started. Yep. Ah, those were the days.

**Chris Gammell:** And then all the CAD people got really accustomed to the command line stuff, right? And then... Oh, yeah. They keep pulling that forward through all the generations.

**Dave Jones:** Even today, the Altium tool today still uses the same keyboard shortcuts as it did back in the late 80s. They all do.

**Chris Gammell:** I mean, it's the same people doing it, right? I mean, you've got 30-year-old board veterans who are like, if you get rid of this, I'll never buy your program again, you know? And, like, it's a dwindling number that are buying the program, so it's... Of course.

**Dave Jones:** Windows, right? Everyone knows Control-C, Control-V to copy, paste, and cut. Yeah, yeah, yeah. Control-X to cut. Where did that come from? That was old WordStar.

**Chris Gammell:** WordStar? I didn't know that.

**Dave Jones:** WordStar command sets way back. I'm sure it was. Please correct me if I'm wrong, but I'm reasonably certain that they were the old WordStar, you know, word processor that even predates DOS. You know, WordStar, I think, started on CPM-based systems, and they were using those keyboard shortcuts, and it was the de facto industry standard. So even keyboards would actually come marked on the keyboard with, you know, cut, copy, paste, you know? Oh, right, right, right.

**Chris Gammell:** Yeah, like on the lower end.

**Dave Jones:** On the lower part of the keys back when we had raised keyboards, you know, and they're actually full-stroke keyboards, you know?

**Chris Gammell:** Oh, yeah, the clickety-clackety. They still sell those some places. It's like the new typewriter is the clickety-clackety keyboard. There's one rule I have. It's do not start questioning IT stuff in public, you know? Like, it's just like, no, way too many people have way too many opinions about IT stuff. Right. Yeah. And I have far too few clues, you know? It's just I pass.

**Dave Jones:** Oh, goodness.

**Chris Gammell:** Correct me if I'm wrong. Oh, they will.

**Dave Jones:** Yes, exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** Happens every week.

**Chris Gammell:** Yep.

**Dave Jones:** All right. More U.S. stuff. What's this about the copyright reform bill?

**Chris Gammell:** Oh, yeah. Well, this is kind of a hopeful thing. I don't know if it's actually going to go through, but it's... It never does, does it? There's always... No, it never does. It never does. Well, the... You know, so like right now, if you crack open a cell phone... And this is kind of gadgety, so it's like, eh, you know, but... Right. You know, if you crack open a cell phone, it's...

**Dave Jones:** Secret police will be around with Robocop in tow and drag you away.

**Chris Gammell:** Or they'll fine you. But yeah, you know, like it's like a copyright thing right now just because it's built into the law that way. And it's... I mean, technically, I would assume that, you know, if they had the resources to do so, you know, like... You know, if you were unlocking firmware on a scope or something like that, then, you know, maybe it would be under the same provision, but... I'm sure it would be, yeah. No one goes after that kind of thing right now. It's just...

**Dave Jones:** No one gives a shit because it's not consumer, you know. Right.

**Chris Gammell:** Yeah. But if it's Apple or Samsung or something, then it's... Yeah, that's right.

**Chris Gammell:** It's huge. It's a mass market and there's tons of money in it. And it's worthwhile.

**Dave Jones:** And then you have those companies pressuring the politicians to... Right, yeah. Lock down on it, so...

**Chris Gammell:** Right, yeah. But let's not go in. Yeah, it's just interesting from a, you know, a free... You know, it's like a buying hardware thing. We've talked about that in the past, right? Yeah, yeah. But yeah. If I have a scope, do I have the right to unlock it? And it's like, well, you know, I believe last time we said, yeah, you do. It's yours.

**Dave Jones:** Yeah, because you bought it. You paid money for it. It's your lock. If they want to hide something in there, that's their risk.

**Chris Gammell:** Yeah. I actually started shopping for scopes recently. Oh, okay.

**Dave Jones:** Tell us about... Let's talk about that. Let's talk about some hardware.

**Chris Gammell:** Oh, yeah. So, for the first time...

**Dave Jones:** Which will segue into something.

**Chris Gammell:** Oh, yeah, yeah. We'll say. For the first time, though, I actually... I was like, you know, I was talking to my boss about it, and, you know, I don't want to spend too much, you know, like that kind of thing.

**Dave Jones:** Oh, this is for work. This isn't for hire.

**Chris Gammell:** Yeah, yeah. This is for work, yeah.

**Dave Jones:** Okay, well, let's talk about what requirements go into a scope for work. Yeah, I mean, so... And how hard it is to extract the money out of your boss, you know? Well, yeah, I mean... You usually end up buying a Rigol 1052E, right?

**Chris Gammell:** Well, yeah, and that's kind of the spectrum. It's like, you know, it's like I could go super low end. I don't have tons of needs, you know? Like, it's like I'm doing relatively low frequency analog stuff. That's what I've always done, you know? Like, that's...

**Dave Jones:** But you know you're spending someone else's money. You're spending the company money, so you want to...

**Chris Gammell:** Right, right. Well... Get the coolest toy you can. Maybe, but it's all about the path of least resistance in that case, right? In terms of, you know, it's like if you have to get more approvals, you know, if you cross a threshold, you have to get more approvals.

**Dave Jones:** Oh, the CapEx limit, it's called here. I don't know what they... Is it called there? It's the CapEx is capital expenditure. And most big companies will have... If it's over that limit, then it has to go get approved by... Right, yeah. I mean, even just from a... CEO or something.

**Chris Gammell:** Just from a general perspective, you know, it's like if it's more expensive, it's usually harder to get. I'm sure everyone listening to this understands that kind of thing. You know, you have to make a case for it as it gets more expensive. And so for the first time, you know, looking at, you know, high-end scope, not super high-end, but, you know, nice scopes, right? You know, Agilent, Tektronix, you know, like, Rody Schwartz and who's the other one? McCroy, right? Or whatever they're called now. You know, look at all those. And for the first time, I'm like, oh, because I can buy the low, quote-unquote, low-end one, right? That's one purchase. And then next year, oh, well, I need more bandwidth or I need this feature. You buy it one at a time. That is the first time I'm like, hell yeah. You know, it's just easier to get it in the door.

**Dave Jones:** Now you can understand why they're doing those upgrades.

**Chris Gammell:** Yeah, and from that perspective, it's actually pretty brilliant. I mean, like, you know, it's just, I don't know if that was always the idea. I mean, I'm sure some of it is being able to offer multiple levels of scope with ease, you know, and actually price it to different levels. But from actually getting in the door kind of thing, you know, they should, hell, they should price it at a dollar, right? Yeah, yeah. One hertz scope for a dollar. Get it in the door. The scope is free, you know? Yeah, exactly. You get it in the door and then it's like, well, if you want to use it, go ahead and buy this $5,000 upgrade. Yeah. You know, it's like, well.

**Dave Jones:** Yeah, of course, these companies, the Agilence of the World and everyone else, they know that most of their purchases come from big organizations and they know how those companies work. Right. And you're pricing in support and everything else, right? And then all of the, yeah, and like, you know, all of the options will be magically under $1,000 or just under, right? Yeah, right. Because they know that that's the average, you know, petty cash limit or the average project budget limit for, you know, yeah, exactly. Yeah. So they, yeah. A lot of thoughts gone into it. Let me tell you. Tricky, tricky, tricky.

**Chris Gammell:** Yeah. So it's, you know, so I'm looking around. It's like, and like I said, I don't, I'm not doing super high end. I have not, not many needs. I think when I, when I look for scopes, I favor.

**Dave Jones:** Engineers always say this. I'm guilty of it myself, right? Engineers are like, we will try and get by with, you know, like, this is the thing, right? If you're given an unlimited budget, you'll go, oh, I'm not going to buy $100,000 oscilloscope, right? I'm going to, oh, I can get by with the $1,000 one. And you're just naturally frugal. Right, right. To your own detriment.

**Chris Gammell:** Exactly. You are punished for that sometimes. You lose budget when you don't, you lose it or lose it, right? I mean, that's how, that's how budgets work. And it's stupid. And that's, and that's priced into like scopes too.

**Dave Jones:** Because it goes against our frugal mentality. Exactly. It's, it's, it's ingrained in engineers that, oh yeah, yeah, I can get by on the $1,000 one. Oh, I don't need the $2,000 scope. I can get by, you know? Of course.

**Chris Gammell:** Yeah. And it's all, or I'll hack it, I'll hack it, right? You know, I'll be able to do, I'll shift it down in bandwidth or something, you know? And it's like, yeah, you could, you know? But yeah, like you said, it's, it's just kind of a detriment as our optimization, right? I mean, it's just, it's just how we think. And, and I think also, you know, we've talked about before, you know, people making the switch from engineering to like management or, you know, trying to move up in a corporate type of situation or start a company. Like, that's a tough thing. Which is your dream. But maybe, yeah. You know, but like, but needing to spend money on people, right? It's like, it's like the same kind of thing of, well, I could do it myself. I could hack, hack at a Linux server or I could hire an IT guy, right? And it's like, of course I should hire an IT guy. But, well, it seems like I could do it. There's tons of tutorials online, right? I mean, like, what is, what is the real value of my time? It's almost all about flight, Aaron. Yeah, exactly. Exactly. So it's, it's a, it's a sickness, but it's, it's, it's something we all, we all argue with. Now, I would be interested to know if there's any, if there's any spendthrift, you know, like, you know, they just love throwing money around kind of people out there because I, engineers wise, you know, like if it's like, you know, burning a hole in your corporate pocket kind of thing. I haven't met anyone like that yet. Maybe really experienced engineers who, who have been burned by, you know, not using it and then being like, well, I need it now. And then they say no. But other than that, I don't, I've never met anyone like that. So.

**Dave Jones:** Right. Yep. No, I, I always err on the side of frugalness. Yeah.

**Chris Gammell:** It's a sickness. Or you just have people send you scopes, right? Right. Yeah. Yeah.

**Dave Jones:** I'm getting two more now. Oh, nice. I'll look forward to that.

**Chris Gammell:** So what is, what is this you were talking about with you? You had something about alternate triggering on scopes now that we're talking about scopes.

**Dave Jones:** The segue in, should we mention our sponsor first? We're halfway through the show. Are we really halfway through it? We haven't talked about anything yet. We're halfway through. How my God. I know.

**Chris Gammell:** We've been 30 minutes, dude. Yes. We should mention our sponsor this week. It is Club Jameco. Once again, they have. They're back. They have not gotten sick of us yet. And they're expanding too. So, so Club Jameco was the site where you could submit your idea. You could submit your project and then they'll, you know, if they, if the. Do everything. Right. They'll, they'll do it. Well, it was, if it's voted up by the community, then, then they'll, you know, you work with the manufacturing engineers and they'll, you know, work on a kit with you. So that's been happening since they last advertised with us and they have a bunch of new kits, some of which we'll be talking about. But yeah, it's, you know, it's, it's, it's an expanding program. It seems pretty cool.

**Dave Jones:** And the kit of the week.

**Chris Gammell:** Yes. Kit of the week. Pretty cool. I've seen.

**Dave Jones:** Kit of the week isn't. Yeah. They are everywhere.

**Chris Gammell:** I, well, I've only seen them once before, but, but, well, in person.

**Dave Jones:** Everyone seems to make them in the cells, but I've never seen them as an actual kit for sale,

**Chris Gammell:** I don't think. Yeah. Right, right, right.

**Dave Jones:** So this is a, it's an eight by eight by eight lead cube.

**Chris Gammell:** Yes. In blue. In blue. Funky blue. Yeah. Right. Oh, I didn't think about that. Right. James K. Blue. Right. Yeah. Yeah. But yeah, so really nice build log, actually. This, and, and, and that's a really nice thing. I mean, there's the convenience of it being a kit, but the, the log is actually really, really well done. You know, multi-step process.

**Dave Jones:** You've got step-by-step photos and, because it is a complicated thing to build. Yeah. I mean, I've, I've heard people spending six months building their eight by eight by eight lead cube, you know. Really? Like, yeah, it's a, it's not a trivial thing to do.

**Chris Gammell:** And then the programming of it is really, it's really interesting too. I mean, just like seeing, seeing the visualization is obviously the, the ultimate end goal, but it's, it's really, you know, it's really cool. I like it a lot. I mean, I, I don't know, I'm not throwing many raves in my house, but if I did, I would definitely have enough LED cube. Right. You know, it'd be good for like parties and stuff like that, right? It's like. Oh yeah. Yeah, exactly. I think it's more for the build. That's the important thing. So. Right. And also a new thing since the last time James, Club James Co. sponsored us, if you do submit a, an approved project brief. So mostly just, you know, like making sure it's legit. You're not just sending in blank sheets of paper, but actually like an actual project brief. If you submit one, they'll send you a 10% off code for anything at James Co. So that's a nice offer they have going for us and we'll, we'll link to them. And it'll also be club James Co.com slash the amp hour as it was last time. Cool. Check it out. It's good stuff. Glad to have them back.

**Dave Jones:** Alternate trigger. Alternate trigger.

**Chris Gammell:** I'm, I'm trying to trigger alt trigger. Go ahead.

**Dave Jones:** You, what, you're trying to think the last time you ever used it. Yeah, exactly. And herein lies the question. Right. It's been talked about on the forum, the EV blog forum a few times. Okay.

**Chris Gammell:** Okay.

**Dave Jones:** You know, and you know, it, it varies from, I think Mike's chimed in on it and he said, oh no, I'd never bloody use it, you know? And, and guys like you can't think of the last time you used it. I probably can't think of the last time I've used it. And, and there's other people saying, oh no, the new Agilent scope is absolutely worthless because it doesn't have alternate trigger. Oh, interesting. Okay. Like I, so, yeah, those kind of things it's like, it's workflow sometimes though too, right?

**Chris Gammell:** I've had that before where it's like, so like an FPGA tool I was using once, I was like, there's no way to do this. There's no way to do it. And it's like, no, well you just have to back up and start from a different path, you know? It's just like, they just change the entire architecture of something and you just do it a different way now. You know, that's, that's usually what it comes down to in that, in those cases, I think.

**Dave Jones:** So I think I'm going to have to do a video on this today. I think I might do a quick video because alternate trigger, it's one of those, you know, lesser known things. Anyway, if you don't know what it is, basically a, an oscilloscope, as you know, has usually you, you can trigger off one channel, you know, you can choose channel one, channel two or external or line or TV sync or whatever type of triggering you want, but it's one trigger. And then if you've got, well, almost every oscilloscope is dual channel or four channel scope, right? So then all of your signals on each one of those two or four inputs have to sync up to that trigger. You've only got the one trigger point. So that means if you've got two, let's say you've got a two channel scope, you're feeding into one frequency, one signal at one megahertz and you're feeding the other one at 900 kilo or one megahertz at one hertz, 1.001 hertz, right? Right. Then I've shown this in a video that you'll end up with one, you'll end up with one waveform perfectly stable and triggered, right? And then the other one just drifting on your screen. Traveling, yeah. And if it's one hertz out in frequency, you'll see it travel at one hertz rate across your screen.

**Chris Gammell:** It's basically unusable if you want to catch anything. I think.

**Dave Jones:** Well, it's a fantastically useful feature if you're looking at clock drift and stuff like that, right? I've done videos on this, right? And that's actually a useful feature. You don't want to use alternate trigger, but what alternate trigger does is allows you to get a stable trace on channel one and channel two, regardless of whether or not the signals are in sync.

**Chris Gammell:** Yeah. Which is nice unless you get tricked by it, right?

**Dave Jones:** Unless you get tricked by it. Oh, look, they're both the same. They're both synchronized, you know? Yeah. It can actually be a trap for young players.

**Chris Gammell:** Yeah.

**Dave Jones:** And the question. Oh, go ahead. No, go.

**Speaker ?:** Nope.

**Dave Jones:** Go ahead.

**Chris Gammell:** No, no. After you. I obviously know nothing about this, so.

**Dave Jones:** Fine. And so the question remains, why don't modern scopes have this? And that is, that's the question on the forum. You know, most modern scopes, the DS, by the way, the bottom of the range DS-1052E, right? The $300 scope. It's got this alternate trigger. But you go by any, almost any high end or higher end scope, even the Rigol 2000 doesn't have it. Right? My Agilent's don't have it. Most scopes do not have it. And a lot of analog, a lot of older analog scopes don't have it either. So don't think it's just a digital scope phenomenon, for example. But yeah, the question is why?

**Chris Gammell:** Well, unfortunately, our former guest and friend, Alan Wolke, was right on the ball. So we actually have an answer. I don't know if you saw it.

**Dave Jones:** Excellent.

**Chris Gammell:** Basically, he says because you can do single shot on a DSO, so you can actually analyze. Yes, you can. Right. So that's the idea, basically.

**Dave Jones:** No, that is the workaround. That's not the reason. That's the workaround. That's what everyone does. Yeah. A deep memory scope. Ah, it doesn't matter. Rat's ass. Just press stop. Just press the stop button. You've captured it. And boom, you've got the two waveforms, right? So what's the application then? That doesn't answer the question.

**Chris Gammell:** What's the application when you need it, when you couldn't do that? So you can...

**Dave Jones:** Well, the application is you want to view both stable waveforms. You've got two signals you want to do it. If you don't have a scope with alternate trigger, then you've got to use two different scopes.

**Chris Gammell:** Oh, so you're saying like over time, you want to watch them against each other. So if you like, we're looking for like a spike. Live. You want to watch it live. Right. You want to see if there was a spike on channel two, but it was traveling across. You couldn't catch it. Okay. I see. Well, Alan said he did post a video on this kind of thing. I haven't watched it yet because I just saw this comment. No, I haven't watched it either. But we'll post Alan's video about it. So it'll be a mystery until then. But yeah, that is a good point. I mean, it's always those catch things, you know, like those little run signals and all those other weird, you know, one-off kind of things that are hard to trigger on. That's the crappy stuff. You know, that's when you really get it. Get screwed, you know.

**Dave Jones:** Anyway, I think I know the answer why they don't have it is because it's complicated architecture. You've got to have entirely separate. Here we go. Yes, I happen to have the answer off the top of my head because, you know, it's pretty obvious, right? Because if you've got a four-channel scope and you have alternate triggering, you want stable waveforms on all four channels. You've got to have four trigger systems, right?

**Chris Gammell:** Yeah, but triggers are done in software these days, aren't they? Aren't they done in software?

**Dave Jones:** No, no, there's, well, you know, you've got to have a separate hardware system, a hardware trigger system for each one.

**Chris Gammell:** I mean, in analog, you definitely need separate hardware, but.

**Dave Jones:** There's still, you open up any modern scope and there's a whole section of the circuitry devoted to trigger. Huh. Okay?

**Chris Gammell:** Okay, yeah. I'll take your word for it. I haven't, I don't open scopes that often. Unlike some people here.

**Dave Jones:** Yeah, right. And then you get into the point where most scopes will only have a single horizontal time base, right?

**Chris Gammell:** Yeah.

**Dave Jones:** They've only got the one horizontal time base button. You can't display a one frequency on channel one at one hertz and a one megahertz signal on channel two, for example. Yeah. So there's yet another requirement on top of this alternate trigger. You'd have to have multiple sample memories and a lot of the time in modern scopes, the sample memory is shared and all that sort of stuff. So, you know, they don't have dual time bases and all that sort of stuff. So, you know, there's very, very few scopes on the market. I think one of the instec models, one of the older or relatively older instec models has all that. Now, you know, it has this capability, not only alternate trigger, but different horizontal rates for each channel. You can set your horizontal.

**Chris Gammell:** I think we're quickly running into Pareto principle right here, though. It's like, you know, how, or even more than that, you know, it's like, how many people need this and how often, right? Exactly. That's what it comes down to.

**Dave Jones:** And that's why modern scopes don't have it, because it's likely a trade-off between the complexity of the design of the scope and the need for people to actually do that. Because traditionally, if you want to view two entirely separate signals, you just use two scopes. Yeah. Right. If you're monitoring live two entirely separate, they've each got their own separate trigger, they've each got their own separate horizontal, well, you use two different scopes.

**Chris Gammell:** Right. And if you need to, you can feed a trigger to each one, right? I mean, you could sync them up in some way, but you don't need to, right?

**Dave Jones:** No. Well, the whole idea of this is that they're not synced.

**Chris Gammell:** These wave forms... You could send a pulse input, though, as a trigger, right? I mean, you could send something...

**Dave Jones:** Well, you could, but the whole idea is that these two wave forms aren't synchronizable in any way, either internal or external. So that's where the problem comes from. The problem is you've got two entirely different signals that aren't related in any way. There's no way you can synchronize them with an external pulse. There's nothing you can do, you know? And you want to view them independently. Well, two different scopes. Thank you very much. Well, I guess buy the cheap ones, huh? Well, yeah, exactly. Buy two cheap scopes or something. But that's the complexity because modern scopes are so fast. They have to have really fast update rates and waveform capture speed and all that sort of stuff. The complexity matters. And if you've got to design your scope to cater for different time base and different triggers for each one of your inputs, either two or four channels, wow. Yeah. You know, the complexity of the design of your scope's just gone through the roof. So I think that's what the scope companies have done. They've gone, well, it's such a niche need that, you know, we're not going to include it in the design of our ASIC chip. If you want to do it, buy a second scope.

**Chris Gammell:** If you need it, you'll really pay for it. Yeah.

**Dave Jones:** Yeah. Buy a second scope. Here you go. We'll sell you another one. Yes. Sir. Thank you very much.

**Chris Gammell:** 20% off too.

**Dave Jones:** So there you go. But if anyone has any further thoughts on this, please leave it in the comments. I'm sure we'll have some. That's the reason why you don't see it in modern scopes is because it's a compromise in the design.

**Chris Gammell:** Yep.

**Dave Jones:** Makes sense. We do talk tech sometimes on the air power.

**Chris Gammell:** Well, let's continue to because there's an interesting thing. So first we need to preface this with the disclaimer. This is one of Dave's advertisers, but it is a new company too.

**Dave Jones:** They are a new advertiser. They've just started like last week or something.

**Chris Gammell:** But regardless, I wanted to talk about this more than Dave did. So I think it's still interesting because it's actually tied to the story after that. But anyways, the tool is called PCBWeb.

**Dave Jones:** And yes, it's exactly what you think, folks.

**Chris Gammell:** Yeah, well, yeah, we'll get there.

**Dave Jones:** We've talked about this before. Online, it's a browser-based PCB tool. Yeah. Anyway, please, you're excited, Chris. Go.

**Chris Gammell:** Yeah, it's done by the people that do EE Web. That's the other thing, the Aspen Labs or whatever it is. I think they were bought by EE Web or something.

**Dave Jones:** They've been a longtime advertiser on that site. Gotcha. So we talked about them before, but they actually do a really good website. It's one of the few electronics sort of catch-all websites that I actually think is done quite well.

**Chris Gammell:** Yeah.

**Dave Jones:** We've talked about them.

**Chris Gammell:** I mean, it's kind of weird, right? I mean, this is kind of treading into new territory for us because we usually don't talk about like your advertisers. And when we advertise on this show, it's like we try and keep it separate. But at the same time, so this is really interesting, though, because they are the first, I think, first CAD program I've seen even. And not just an online CAD program where they have the DigiKey catalog built into the tool. And regardless of everything else.

**Dave Jones:** Schematic and footprint. And it looks like it's integrated really well. I'm curious to know, have you actually tried to get like an obscure footprint out of it?

**Chris Gammell:** No. I've done very high level stuff.

**Dave Jones:** Right. Okay.

**Chris Gammell:** I have tried it. I'm very... Yeah. It's...

**Dave Jones:** I have to say that Chris has tried this tool. I haven't tried it yet, but I have watched a demo video that the guys did for me. And it does look... I watched the video and I went, these guys look like they've done this right. Right. You know? Yeah. No, yeah. And it is. And you would agree. That was your sentiment as well.

**Chris Gammell:** Well, I'll get to that. But first I want to talk about the... So this is the first one that has a distributor built into it, right? And I haven't seen that anywhere else yet. And obviously DigiKeys was one of the biggest ones online.

**Dave Jones:** Well, Altium have the distributors built in.

**Chris Gammell:** Oh, they do? Okay. I've never seen that.

**Dave Jones:** Oh, yeah, yeah. But I'm not sure of the current state of it. I'm not sure if it's every part. I can't... I don't use the latest version of Altium. Okay. So do they have... It's been two years since I worked there, you know?

**Chris Gammell:** Yeah. Footprint and schematic symbol?

**Dave Jones:** Yes, they do. They were doing that, but it wasn't comprehensive last I looked. But I could be wrong now. Yeah. But no, it certainly doesn't look near... The Altium one last I played with it was not nearly as easy to use as this one looks. Right. Right. It's like you've got the DigiKey parametric search built right in there. Built right in. With all the drop-down boxes and... Right. And it's great. Or you can just type in the DigiKey part number and... Yeah.

**Chris Gammell:** Yeah. And so actually just clicking through now for like... I was thinking about connectors and some of the connectors are weird, right? So I just clicked a connector and it actually didn't have the footprint for that. So it's not completely comprehensive. Ah, there you go. Right. Right. But if it is, and I don't know anything about this whole thing, but if it starts building out where DigiKey starts offering that as a back-end service kind of thing, that... If... I think it's a given that they ultimately will.

**Dave Jones:** You think it's a win? I expect every CAD tool in five years' time will have complete DigiKey integration. If DigiKey aren't working on getting a footprint... Yeah. If DigiKey, Mouser...

**Chris Gammell:** Yeah. Farnell...

**Dave Jones:** And Mouser and everyone else in Element 14 aren't working on creating a footprint for every single library part... At least the default, right? ...that they're putting there. Yeah. At least a default or something like that. Then they're crazy because that is the killer app.

**Chris Gammell:** It is. Yeah. Right. And that's what I like about here. So obviously, I went really... I guess I should have started a little bit more realistic. I started with an LM324. It's like, of course they have a footprint for that. And it ended up being a dip part. Of course. It was just like the first one I typed in. Exactly. But, you know, so that alone is really, really cool. I really like that a lot. I've... You know, we talked to... I talked to Andrew Seddon from CircuitHub. That... So that's kind of a similar kind of thing where it's a Dropbox. You know, you can pull the footprint from there. So, you know, that could be eventually like, you know...

**Chris Gammell:** You know, a distributor buys them or something like that. And then they pull all that stuff in. I don't care how it's done. I really, really like this functionality, though. And I use older tools. And, you know, as I told... As I complained to Andrew, CircuitHub doesn't have KiCAD stuff yet. But, you know, like it's... So you're not... You know, getting 100% coverage is really, really tough. But I really, really, really like this app a lot. In whatever form it takes. So that alone is number one. I think that's really cool. And I think a lot of people will out there, too. Number two, though, like Dave said, is the CAD program in the browser is pretty nice. I mean, it's not like... It's still in a browser, right? That's... Strike one is it's in a browser. And I don't know the future plans, if they're going to break it out of the browser or something like that. I don't know anything about the plans with that stuff.

**Dave Jones:** It's possible. Yeah. The technology they've used, it is possible that they could potentially offer a standalone version. I believe, anyway. So, but... Okay. So, that'd be good. But it is browser-based.

**Chris Gammell:** Yeah. Yeah. But, again, you know, the tough part with all this kind of stuff and these, like, you know, quasi-closed ecosystems, it's like, well, it's good. I just... I need to know there's some chance that I'll be able to extract data at some point. Like, actually, I found out that Google actually lets you pull out all... I mean, this is old. I mean, I know that this actually happened for a while. But Google lets you pull out, like, all old YouTube videos and everything, too. Like, you can pull out all of your data of Google now. And, like, data portability, I think, is probably going to be a bigger deal in the future, too, as, you know, as everything goes to cloud apps. But it's tough, right? I mean, because I understand that businesses want to have, you know, profitable enterprises. They want to lock you in, right? Yeah. Yeah. It's like, I'd do the same thing. But at the same time, I don't want to deal with... I don't know. That's why I like KiCat. I mean, I don't even have to pay a license fee, right? I mean, I just... Right. You know, it's just an evolving project that, you know, like, I don't know.

**Dave Jones:** You want the best of both worlds. You want this really easy-to-use, killer... Yeah. For free. ...component integration. You want it all for free, and you want it completely open.

**Chris Gammell:** Yes. Right. Yeah. It's asking for too much for right now. But, you know, it's moving towards... It's making progress. So, but, you know, first impressions, it... I hate to say it, but it is a nice tool. I don't hate to say it. It is a nice tool.

**Dave Jones:** You were saying before the show, it is by far the best...

**Chris Gammell:** Yeah.

**Dave Jones:** ...web-based CAD tool you've tried.

**Chris Gammell:** And I haven't used them exhaustively. I've used Upverter. Upverter, I liked a lot. Yeah. Circuits.io, I've used a little bit. That's not bad either. I mean, like, they've got really... Everyone's got really good programmers working on this stuff. You know, the nice thing is, which I think we've mentioned in the past, is you're not carrying forward all this legacy stuff, right? I mean, you don't have... Mm-hmm. You know, you don't have type command line stuff that you have to build in, right? That's the benefit of it for, you know, in terms of lightweightness, right? Mm-hmm. You know, like Cadence and Altium, they're all carrying... Oh, yeah.

**Dave Jones:** They've got a lot... Yeah. There's like a million lines of load in... A million lines of code in Altium or something. Yeah. It's crazy.

**Chris Gammell:** So, that's tough. I mean, I don't envy that position. Working with, like, legacy stuff is tough like that. But, you know, it's... But there's downsides to the newer folks as well, because then you don't have the experience. So, it's a... I don't know. You just got to pick one and go with it, really.

**Dave Jones:** You're excited. I really... I watched the demo and I went, they've done this right. I really need to try this. But, yeah, as you say, I mean, it's a web-based tool. So, either you, you know, accept the limitations of that and potentially being locked in, or you don't. You know, I mean, it's up to...

**Chris Gammell:** Yeah.

**Dave Jones:** It's up to you. Yeah.

**Chris Gammell:** But, right. So, good start. Anyway, the functionality is cool. People should check it out. It's interesting. I mean, so... Yep.

**Dave Jones:** We'll post a link down there.

**Chris Gammell:** Yeah. So, interestingly, so, the other story, though, was about another browser-based tool, right? So, I don't think we've said anything... I think today might be the first time positive we've said anything about browser-based tools, right? Because, like, Tinkercad, right? That closed down.

**Dave Jones:** Well, we didn't say anything... Well, we didn't say anything positive... Well, we're not saying something positive about browser-based tools. We're saying something positive about the app itself.

**Chris Gammell:** That's true. Yeah, that's a good point. Yeah, because it's not like we're switching over to all browser-based tools right now, right? I mean, I'm not getting off my desktop yet, you know? It's like, maybe someday, but not yet. And I get all the arguments for it, too, right? People say, oh, well, it's, you know, instantly upgraded software. I get that.

**Dave Jones:** Yeah. See, I've moved over to that with, like, you know, Google Mail and, you know, Docs. Like, I do all my, you know, everything's, almost everything's a Google Doc and, you know, stuff like that. Well, not quite, actually, but, you know, yeah, I'm sort of half cloudy at the moment.

**Chris Gammell:** Right, yeah. Yeah, I think that I'm in a similar boat with that kind of thing. But it's not that kind of email stuff that I care about. It's the, again, you know, it's the legacy thing, right? It's like if I have an old design, right? We talked about Dayzix before and how I had to deal with that, you know? So if I have an old design, it's not necessarily, like, that the program updates or not even necessarily that the company could disappear overnight because that's also a possibility, like, with Cat Junkie. With Cat Junkie, no, with Tinkercad. You know, like, it's just – Yeah, they just went bust, right? There's just those two options. But it's actually that everything's working perfectly, but that when I pull up a file six months later after there's been three revisions, right, I had left something dormant. They say, oh, there's compatibility issues. Yeah, there's compatibility issues. That's the worst because you just – you don't know about it. You're not going to go and check every file once there's, you know, a background software push. And you're not going to know about it until you actually open that file up, right? It's just the nature of hardware. You can't pay attention to all your projects at once.

**Dave Jones:** And does this thing actually need the internet to run or can you download it and actually run it locally in your browser?

**Chris Gammell:** Oh.

**Dave Jones:** Because if you could do that, technically, then it's not a cloud tool, right? Because you can keep a copy of that existing browser. You can keep a copy of the downloaded file and run it locally. That's interesting. This could be a key question here. That is an interesting question. Because then it almost essentially is a desktop app then. It just happens to be running in a browser. So if it doesn't – the key point, does it need access to the internet live while you're laying out that board or not?

**Chris Gammell:** Yeah. Yeah, that is interesting because there's – I mean, there's stuff like that too. Like you mentioned Gmail for, you know, like a cloud-based app. But there's offline mode for Gmail now too where, you know, a cache is like the actual install with all the JavaScript or whatever the hell it runs on.

**Dave Jones:** Right.

**Chris Gammell:** Yeah, so you could maybe do the same kind of thing. But then I'm not sure about security. You know, sometimes people worry about security and stuff like that too. So I don't know how that works. But in terms of code, so there's another tool out there. We've talked previously about – I think TI had like a cloud-based compiler or something like that for like CC2000 boards – or C2000 rather. So one of their microcontrollers. And we kind of scoffed at it. It's like, well, why do you need that kind of thing? And I've seen a couple others here and there too. It's like – and you don't, right? I mean like there's no – unless you're doing supermassive compiles, right? For – and if you're doing a microcontroller, it's not going to be a supermassive compile. So, okay. Cool trick. And so I was in the midst of writing a similarly snarky comment today. I was reading about the Thingsquare, which is a cloud-based – it's like an Internet of Things kind of – bingo. Oh, cool. But, you know, it's like a mesh network kind of thing, right? So it's like you buy a piece of hardware, you talk to it, and then basically you can create little nodes all over the place and then they mesh together. So I was writing that similarly snarky comment and then I'm like, well, wait a second. You're already buying the hardware from them or the stack or whatever. If you're already in an ecosystem like that, that's when I think it finally makes sense. Right.

**Dave Jones:** I think.

**Chris Gammell:** Because at that point – I mean so the thing they talk about in this article is, okay, so we're this mesh network. We can – you can, you know, run your code in the cloud, right? And then you compile it and then it pushes it to all the devices. That's cool by itself but not necessary, right? You could just as easily compile it on a computer, push it to an IP address and it goes out, right? Yep. But the interesting thing is that it's just a convenience thing at that point, right? It's like, okay, I've got connected devices. I might as well do it in the cloud, you know?

**Dave Jones:** Right, right.

**Chris Gammell:** At that point, it actually becomes worthwhile, I think. So the thing Square missed is what their – that's what their mesh network is called. But yeah, I know.

**Dave Jones:** It's just that it really is, you know, a niche need. It's not going to be all things for all people. Like, it's just, you know.

**Chris Gammell:** Yeah. I don't know many software developers running on netbooks, you know. No.

**Dave Jones:** You know, this comes back to the whole Altium thing, you know. They bet the future of the company on the Internet of Things and, you know, every device on the planet, everything, every electronics designer is ever going to design is going to be cloud, you know, Internet of Things enabled. You know, it's just bullshit.

**Chris Gammell:** Yeah. Right? Yeah. If it is going to happen, it's going to be way slow. So, I think, still. I haven't seen any accelerating factors yet, but, you know, it's –

**Dave Jones:** Yeah, there's a need for stuff like this, but it's not, you know, it's niche. And it probably always will be.

**Chris Gammell:** And the downside of having, you know, net-connected type of stuff like this with, like, automatic firmware pushes is like in iRobot when they all get updated with, like, the malicious firmware and then they start attacking humans. Right. So, that's a thing, right? You never know.

**Dave Jones:** What happened to the three laws?

**Chris Gammell:** They overrode them. Overrode them. You didn't see iRobot?

**Dave Jones:** Yeah, I have. Oh, okay.

**Chris Gammell:** Yeah. Bloody.

**Dave Jones:** Nah, bloody internet of things. Jesus. Yeah.

**Chris Gammell:** There's another one, too. There's – when Ryan Brown was on – I think you weren't here that week when Ryan Brown was on the show.

**Dave Jones:** No, I don't think I was.

**Chris Gammell:** Yeah, it's another – some of the people he knows down in Austin, they're kicking off another similar kind of connected device thing.

**Dave Jones:** Yeah, devices. Yeah.

**Chris Gammell:** Yeah, so Sapphire OS. And, you know, it's interesting. It's another software layer, basically. A lot of them are using that same chipset. It looks like a lot of people are using the CC254X series. Yep, yep. Which I've got the kit for. It looks nice. I think we mentioned that last night, right? Or last time, rather. Yep.

**Dave Jones:** Hang on. I think I can see – yeah, yeah, there it goes past the office window here, the bandwagon. There it goes.

**Speaker ?:** Yep.

**Chris Gammell:** Nah, come on. People are interested in it. There is a lot of benefit to it. But the killer – you know, the killer thing with Internet of Things and everything else, yeah, of course people want, you know, like, connected stuff. But people don't want to pay for it, you know. They don't want to, you know, like – yeah, I want to connected –

**Dave Jones:** And they don't want the shit battery life when you get something that's Wi-Fi enabled, you know?

**Chris Gammell:** Yeah. Well, yeah. Well, and that's the thing, you know. Right. They're all moving to non – you know, because there's a bunch of different wireless standards. Wi-Fi is probably out of the question. Like we talked about last week, Bluetooth low energy is low bandwidth. Bluetooth is relatively high bandwidth if it has to be connected all the time. What else is there, like? Uh-huh. No. Polaris? Oh, there's a couple of others. Yeah, there's a couple of – Zigbee stuff, right?

**Dave Jones:** There's a few proprietary solutions as well and –

**Chris Gammell:** Yeah.

**Dave Jones:** You know. Eh. Blah.

**Chris Gammell:** I know. Two things you don't like. Internet of Things and RF. Blah.

**Dave Jones:** I didn't say I don't like IRF. I just don't do RF.

**Chris Gammell:** Right, right. Sure.

**Dave Jones:** Big difference, dude.

**Chris Gammell:** Yeah. It's – yeah. It feels a little bandwagon-y right now, but it doesn't feel like there's – you know, it – this – we're at the fragmentation stage, it feels like, right? There's lots of solutions. You know, there's – there is differentiation between them, but, you know, if you're a product designer trying to design it in, then, like, how do you decide? You know, it's like I want my stuff to talk to other stuff, but, you know, if I can't – you know, if I have to buy the same thing everybody else does, well, I better just wait. There's always that waiting period, you know, the wait and see who else is doing what. So, yeah. The good thing about both of these, so Sapphire and I believe both – and I think also the Thingsquare, they're both open source. So, kudos. Kudos on that.

**Dave Jones:** Oh, yeah.

**Chris Gammell:** That's cool.

**Dave Jones:** That's a good thing. Yeah.

**Chris Gammell:** What I want to see is, like, a, you know, a strategic merger, right? You know, like smash your IP together, you know? Like, that'd be cool, right? You don't really see that because there's a lot of little projects and people kind of doing that kind of thing. But making your little project into a bigger project and collaborating across, you know, distances and stuff, that's a tough thing to do, you know? Especially when you kind of get your eye on the prize, right? You know, maybe you want to get investment, you know, like that kind of thing. It's hard to do that kind of thing, but it could be worthwhile. So, think about it, guys. Some guy on a podcast said so.

**Dave Jones:** Right. Can we get back to some real hardware? Sure. What do you got? Real PCB shit. There's some PCB artwork. You put this on. What is the most amazing PCB artwork you've seen?

**Chris Gammell:** Oh, yeah.

**Dave Jones:** And there's some photos of some nice homemade artistic, you know, artwork shaped in all sorts of different things.

**Chris Gammell:** Yeah.

**Dave Jones:** I've kind of done stuff like that, but I'm not arty enough to actually pull it off, you know? Yeah. Yeah, because there's many different techniques you can use with PCB manufacturing to get lots of different colors and textures and layers and transparent, you know, leaving off solder mask and all sorts of things. You can get some really clever effects if you're smart enough just using the standard PCB manufacturing technique. Yeah.

**Chris Gammell:** Right, right, right. Yeah. It just comes down to where you cut out the Gerber, right? I mean, just leave a layer off and, yeah. Yeah. Put a partial.

**Dave Jones:** Just have to be clever. Yeah. You can do lots of really clever things, you know? You can do really colorful front panels and really artistic things with just basic PCB manufacturing, which I really like.

**Chris Gammell:** Yeah. Yeah. Well, I found this link from, because Lane from OSH Park is future guest of the Amp Hour, by the way, in I think three weeks. Ooh. Yeah. Yeah. Yeah. Um, so get your purple, purple PCB questions in later. Um. Right. Um. He was asking about mechanical examples because he's given a talk at, uh, I think at Maker Fair about mechanical stuff, right? And, and, and I think someone mentioned, you know, like how you use the mechanical aspect of the PCB as part of the case for the microcurrent. Yeah. And, um, I know Evil Mad Scientist, uh, labs, they, they use PCB material for their egg bot. Um. Mm-hmm. So, you know, just cool examples like that. And, and then someone posted this, this example. It's just, you know, there's a lot of cool stuff out there that I never really, you don't think about it as art, right? But, or even as mechanical. No, no, exactly. Yep. Kind of reimagine it.

**Dave Jones:** Yeah, I'm, I'm more into the using the PCB as the mechanical element rather than artistic sake, you know? Yeah. Because I, I'm, I'm not an artist, you know? I can't design some fancy whiz-bang shapes and all that sort of stuff. Yeah. I'm just not. Right. That way inclined. Yeah. Square box made out of PCBs. I've done, I've done the occasional curved corner, you know? Yeah. I'm getting fancy. Woo-hoo.

**Chris Gammell:** Yeah.

**Dave Jones:** You know?

**Chris Gammell:** A million machine. Yeah.

**Dave Jones:** I'm into novel manufacturing techniques like that. Like if you look at my micro watch, if you look at my micro calc, which is like a PCB sandwich done as a touch front panel. Yeah. Yeah. And, you know, there's, there's no case at all. It's just entire PCB and, you know, all that sort of stuff. And it's got cutouts for the batteries and, you know, things like that. So, yeah, I'm more into that side of things. Yeah. And, yeah. Because the great thing about, the great thing about using PCBs is because there's a cheap, established manufacturing industry out there for manufacturing your boards. Yeah. It's kind of a taste. So the limit is your imagination. Yeah. Exactly. Yeah. So it's your imagination what you can do with those Gerber layers, you know? Those Gerber files. And then, yeah, you can get those manufactured and, you know, you can build a product entirely with PCB and build it up in layers. You know, you could have 20 layers, 20 different boards and boom, you can build up your box and

**Chris Gammell:** Leaning, leaning tower of PCBs. Bees.

**Dave Jones:** Oh boy. Yeah. I've been to Pisa.

**Chris Gammell:** Oh yeah?

**Dave Jones:** Nice. Very nice little town. Liked it. Yeah. I've got the obligatory photo of me trying to hold up the, you know, big tower. Yeah.

**Chris Gammell:** So, right. It's original. You got to do it, right? It's the downside. Yeah, of course. You know, it's like, ah, well, okay. You know. Yeah.

**Dave Jones:** Yeah. And, you know, and there's a hundred other people there trying to get the same shot. Exactly. So you're trying to do it without getting anyone else in the background of you holding up the, yeah.

**Chris Gammell:** Well, if you were going to make your own PCB, you can actually, you know, you can mill your own PCBs at home. And that was another link that we had this week. Yeah, you could. But there's a Kickstarter campaign, actually, for a custom, not custom built, a specific built, I guess. It's only meant to be a PCB mill. And it's called the Other Mill.

**Dave Jones:** No, I thought it was, no. This is the one from the Hacker Lab.

**Chris Gammell:** Okay. There's somewhere. Other Fab, yeah.

**Dave Jones:** No, it can do other stuff, too. Okay. Yeah, primarily.

**Chris Gammell:** Sort of, yeah. I mean, okay. Yeah. I know, yes, you can do other things. But I mean, like, two inches, you can do two inches in the Z-axis. It's like, yes, you can engrave stuff. It's like, and that's actually, so, you know, I went through a lot of this research for the mill I got. But, and one of the really expensive ones, actually, is the Roland, which is part of the Roland TG-15 or something like that. And they're really expensive. They're polished. They're really nice. They're well-supported. Yeah. And they're part of the Fab Lab. So, like, the standard Fab Lab kit has, you know, a Roland cutter. It's got a ShopBot, a laser, an Epilog laser cutter, everything. So, it's well-supported like that. But, like, five grand for, you get, like, two vertical inches. Yeah, yeah, yeah. Oh, terrible. Maybe it's more of that.

**Dave Jones:** Well, the problem I have with it, yeah, it's a nice little Kickstarter project, but the build area is too small. Yeah, it's like four by five inches. It's like, oh, yeah, if that, yeah, it's tiny. So, like, oh, no, you know, I want to, you know, double that. Yeah.

**Chris Gammell:** And so, yeah, and that's the, so there was actually some really good conversation on this in the Amp Hour subreddit. You know, people were asking about this kind of thing. And it's like, yeah, you know, there is a very well-defined curve of, you know, if you want to pay for, you know, it's not features necessarily as much as size, right? There's rigidity in the actual axis and stuff. And I went through all this stuff. And actually, the, the, I can put the link in for what eventually got me to the mill that I got. You know, it's just, you know, you have to do a lot of research on that kind of thing. But, you know, it's a trade-off. And the price point on this thing isn't too bad. And it, it'll, it'll be.

**Dave Jones:** Oh, no, it's okay. Yeah. I would, I would probably be tempted to get one if it had a larger build area.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** It's, you know, I mean.

**Chris Gammell:** Right.

**Dave Jones:** Yeah, I think there's a good market out there for a really good, a really, you know, polished low-cost PCB milling machine.

**Chris Gammell:** Well, yeah. And that's, and that is another big, big benefit of this too, right? It's, it's, it's finished, right? I mean, like I had to put my mill together. I had to tram it. I had to, you know, I had to actually align and everything. Like if you don't want to do that stuff then, and you think you can get by with four by five PCBs and you have a need for fast stuff, then yeah, go for it, you know? But it's like.

**Dave Jones:** Yeah, of course. Yeah.

**Chris Gammell:** If you need to get past limitations. One thing is the software as well.

**Dave Jones:** The software is the other, how good is the software, you know, that, that drives this thing. That is the other thing. There's no point having great hardware if the software just sucks ass.

**Chris Gammell:** Yeah. So they, they talked about, there's a lot of components of a milling machine actually. There's a lot of different layers normally. I'm actually not sure about, oh, so they're using other cam. You know, like in, in most of this kind of stuff, you need like a CAD file, you need a cam file, which actually tells the cutter where to move like left and right, up and down. And then finally you need a translation program that takes that G code and then moves it to a stepper motor. Like, you know, like four steps this way, five steps that way, that kind of thing. And those are actually pulses.

**Dave Jones:** See, the people using this shouldn't have to give a rat's ass about that. They take the GERB file, they put it in and your board comes out.

**Chris Gammell:** Yeah. You're right.

**Dave Jones:** That's what I want. I don't, I don't want to dick around. I, I just, I got better things to do with my time than dick around trying to get, you know, this stupid machine working.

**Chris Gammell:** I think then this, this would be the kind of thing for you, right? And, and, and even, you know, I had used a custom built or not custom built, a specific built, you know, similar board cutter before where, you know, it was just, just a board cutter, nothing else. It wasn't meant to mill anything else. And, and even that still, you know, it's just, it's tough, you know? And there's still adjustment, right? I mean, you still have to adjust the, um, you know, so for milling boards, you don't necessarily use an end mill with like a flat, a flat end mill where it's, you know, like where you would use like on metal normally, usually use a V shape, basically a carver. So you actually have to set that depth then too, because then if you're using copper clad FR4, if you set it too deep, you end up cutting your traces or you, yeah, your traces end up being too narrow. And, uh, so that's kind of a fine artwork kind of thing too. Right. You have to learn that, mess it up a couple of times, but.

**Dave Jones:** But I don't want to do that. I want it to know. I want it to take care of everything. I want it to be intelligent and just produce my bloody Gerber file, you know?

**Chris Gammell:** Oh, well then what you should do is, uh, send it out to a cheap board fab and wait three weeks or.

**Dave Jones:** Exactly. Or copper.

**Chris Gammell:** I mean, honestly, copper etching is still like in terms of accuracy. I think, you know, if you, if you have a good process for, for copper etching, you're still going to win. I think.

**Dave Jones:** I've done like six, six at home. Yeah. You know, you can, you can get down to, you know. Right.

**Chris Gammell:** And it's tough to get six, six for, for, um, mechanical because you start to get.

**Dave Jones:** Oh, yeah, yeah. Yeah. Yeah.

**Chris Gammell:** You know, you get that rotational force on like a six mil trace, like whoo, or six mil space. Yeah.

**Dave Jones:** Oh no. And it tears it, it tears it straight off. Yeah. Yeah. No.

**Chris Gammell:** And then if you're, then when you're drilling Vias too, right? I mean, that's another tough thing. I think they showed drilling second or no, maybe it was someone else showing right second on Vias. You can't do that. That's as bad. You'll rip that trace right off. So. And then there's the other thing too, with like, if you're doing it, if you're doing a cut board at home, right. Or even if you're doing an edge board, you still have to connect the Vias yourself. That's always going to be a problem. You know, like I think, I think I was talking to Jeff Kaiser about the, uh, about a, uh, what's it called? LPKF. The, uh, that's a laser based one. Those are high end, right? But they have. Yes. They're high end. You pay 10, 20 grand for those.

**Dave Jones:** Yeah.

**Chris Gammell:** And, and I mean, it's nice, right? But again, it's, it's about, you know, what do you have a need for and how much time you're willing to spend if you don't want to pay for that need, right? Yes. You know, it's like, I still haven't actually used my MILF. I've only been doing metal and wood, so I haven't tried it for PCBs yet, but I should be able to eventually when I get to it. No.

**Dave Jones:** Like I, you know, I love getting back the real board, you know? Oh, yeah. That's like, you know, that's why I've never, you know, yeah, there's no, like you get the real board with the real solar mass, the real plate through everything, the, you know, the You get the funny silk screens that you put on there. Right, yeah. And you get to see the real finished product, you know? I mean, there's no beating that, and as you said, PCB manufacturing's a commodity these days, and, you know, I mean, there's less and less a market for these rapid prototyping Right. Things nowadays. Right. I mean, you know, especially at work, like, you know, we, we used to spin eight layer boards in 24 hours.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? Yeah. You know, I mean. But who cares, right? Yeah, right. Yeah. You'd pay a couple of thousand dollars. Who cares, right? You know? Yeah. Well, I didn't care. The shareholders cared in the end, but, you know, I mean. Right. But the engineer, no, I want my eight layer board tomorrow. Yeah.

**Chris Gammell:** But even that, you shouldn't care either, right? Because the justification should always be that if you're paying for an eight layer board overnight, it's like, you have a need for it, right? I mean, that's just.

**Dave Jones:** Exactly.

**Chris Gammell:** That is just the trade-off you have to make. That's the one thing that engineers are normally good at, actually. You know, like, you know how to make that calculation, and once you make it, you know, it's like, no, I need it, so I'm going to pay for it. It doesn't matter. At that point, the price tag is just a thing, you know? Yes. Yes, that's right. It's just a number on a page. It's just my boss's credit card. Who cares?

**Dave Jones:** Yeah. So are we quite bipolar in that way? Like, you know, yeah, I'll go out and spend, you know, three or four grand getting that eight layer board made overnight, and I can sleep well at night, but then I'll agonize over the scope I just bought and why I bought a, you know, a $1,000 scope instead of a $2,000 scope.

**Chris Gammell:** Right. Well, you know, I think the problem there is just analysis paralysis, right? I mean, like, think about how many scopes are available these days, right? There's at least four big ones, and then there's the smaller ones, and, you know, you could start optimizing for, you know, oh, well, Rigol has features, but there, you know, there might be less support, that kind of thing, just because it's an overseas company. And it's like, well, okay, yeah, you know, I could do this analysis all day long, right? Or I could, you know, pay for support and pay through the nose, that kind of thing. It's like, but if you had to buy a scope the next day, of course, it would just be like, no, I need this, go, done, fine, whatever. You know, it's...

**Dave Jones:** Oh, they've got it in stock at my local supplier. Exactly, exactly. Your decision factors are, you know, different. Exactly, exactly.

**Chris Gammell:** So that... No, I'm not going to say what I was going to say.

**Dave Jones:** Sometimes that comes down to part choice as well, you know? Yeah, exactly. You'll use a non-optimal part that you can get over a, you know, over a better part, which, you know, might have a questionable supplier, or that you can't get.

**Chris Gammell:** Exactly. Engineering brains are all about optimizing. That is, that's just what it is, right? I mean, like, and so if I could, if I could get it faster, and I need it, then yeah, whatever. No big deal.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** That's it for today's show.

**Chris Gammell:** That is it for today's show. No. Oh, no. We do, we do have a workbench. We do have a workbench. Two workbenches, actually, but... Oh. Quick, quick looks.

**Dave Jones:** Hong's Electronics.

**Chris Gammell:** Yes.

**Dave Jones:** Where is he? Yes, Hong's Electronics. Yeah. Jeremy, Jeremy Hong. Hey, Jeremy. Jeremy, he's a student at Wright State University, I guess.

**Chris Gammell:** I thought he was going to be coming to Cleveland because he has a case on his website, but yeah, he linked to something else, so...

**Dave Jones:** Anyway, he's got a cool-looking basement. I assume it's basement. It's all dark and dingy. Yeah, it looks basement-ish. Oh, I love it. And it looks like some real stuff happening in there. Awesome.

**Chris Gammell:** Very nice. Awesome, awesome workbench. Part organization looks like his MO. Very, very awesome.

**Dave Jones:** And he's got like half a square meter to actually move in. Yeah. So it's all... You know, it's great.

**Chris Gammell:** And a very prominently displayed fire extinguisher. Always a good idea.

**Dave Jones:** Oh, yes, yes. Got the fire extinguisher there. Fantastic. Yeah. Right there on the bench, right next to the scope. That's where you need it. Right next to the breadboard. That's the way to do it. Great. Great stuff. Yeah.

**Chris Gammell:** The other one was from HarryMJ, and at least on Twitter, or on Reddit, rather. I'm not sure, I mean, I'm not sure, Harry's last name. HarryMJ sounds kind of funny. But this is actually a really cool picture because it's from the Stanford solar car lab. And they've got... Ooh. And so he's got a couple pictures in here of the battery packs and everything. And the bench is actually really nice. They got one of the new Agilent source measure units, which is a pretty nice thing. Reflow ovens, welding stuff. I mean, not like the huge bench is very specific to the electronics needs, but yeah, cool stuff. Yeah. B2902. That's a cool source measure.

**Dave Jones:** And they actually drive the solar car into the shop, you know? Yeah.

**Chris Gammell:** Right.

**Dave Jones:** And if... So there's the solar car right behind the workbench, you know?

**Chris Gammell:** Right. It's great. And if you scroll down, of course, if you scroll all the way to the bottom, you did see that, right?

**Dave Jones:** Oh. Oh, there's a DeLorean in there. Yeah.

**Chris Gammell:** Great, Scott. That's not theirs, but yeah, I guess that's the benefit of being a solar car team is you get to play near awesome cars, so...

**Speaker ?:** Awesome.

**Chris Gammell:** All the, like, the... I'm sure Stanford labs are pretty well decked out, so that's pretty cool.

**Dave Jones:** Yep. I could imagine. Yeah, that's awesome.

**Chris Gammell:** Thanks to people for sending that stuff in.

**Dave Jones:** Workbench of the Week. Everyone loves Workbench of the Week, even though this is a radio show.

**Chris Gammell:** Yeah, yeah. Well, we always post links, so...

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. All right, cool. All right. Well, uh... That's it. I will report back next week from Hamvention, and we might have a Maker Faire attendee. We have a guest. We might. Yes. We're not sure yet, so... Might.

**Dave Jones:** Oh, okay. Right. Okay.

**Chris Gammell:** We'll see, but...

**Dave Jones:** Well, have fun. And make sure you get that group photo with all the APL t-shirts.

**Chris Gammell:** Yes, I will try my best, and I'll be taking lots of videos and hopefully out on the hunt for mullets and such, so... Yeah. I'm excited. Cool. Have fun. All right, man. Talk to you next week. See ya. This episode was sponsored by Club Jameco. Upload your project brief today, and if approved, you'll get a 10% off coupon. If chosen by the community, you'll make 10% off any kit sold without ever needing to buy or bag components. Go to clubjameco.com slash theamphour to find more details and to support the show.

**Speaker ?:** Go to clubjameco.com slash theamphour to find more details and to support the show.
