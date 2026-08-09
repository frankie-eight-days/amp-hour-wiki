---
episode: 64
title: OSHW, Makerbot & Memristo - Maundering Memristor Mathematicaster
url: https://theamphour.com/the-amp-hour-64-maundering-memristor-mathematicaster/
---

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell from Chris Gammell's Analog Life. Episode number 64.

**Dave Jones:** Six four. Wow. Power of two.

**Chris Gammell:** You were much more excited about this one than I had. We've gone up another binary digit.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** We've flipped over to nine digits.

**Dave Jones:** Yeah.

**Chris Gammell:** Eight digits cannot contain the Amp Hour. Oh boy. Very exciting stuff. I'm sorry.

**Dave Jones:** I guess so. It didn't get me like it got you. I don't know why you were... I'm more of a power of ten kind of guy, I gotta say.

**Chris Gammell:** Well, yeah. All that analog rubbish, right?

**Dave Jones:** Yeah. I like decades.

**Chris Gammell:** Right. Because you've got ten fingers and ten toes and all that sort of stuff, you know.

**Dave Jones:** Right. And sometimes we go wonky and we'll throw in a 20 in there because of... Right. The decibel people, but... Right.

**Chris Gammell:** No, I prefer binary either sticking the finger up, middle finger up, or... Not. So, it's even zero or one.

**Dave Jones:** There you go. There you go. Sticking it to the man. Oh, yeah. Yeah, you're all about that, huh, Dave? Absolutely.

**Chris Gammell:** Why not? I think every engineer is. Isn't it in our trait to sort of stick it to the man? Tell it like it is?

**Dave Jones:** I guess. I'm not a very stick-it-to-the-man kind of guy myself.

**Chris Gammell:** No, you're not. You're a bit of a wuss, yeah. Yeah. We all know this.

**Dave Jones:** I'm not an Occupy Wall Street so much as an Occupy My Basement.

**Chris Gammell:** Right. And just let sleeping dogs lie, huh? Instead of poking them with a stick. Yeah. All right. Fair enough.

**Dave Jones:** It's sad. It's true.

**Chris Gammell:** All right. So, it's no big deal, huh? Episode 64.

**Dave Jones:** Not as much to me.

**Chris Gammell:** But it won't come around again until 128.

**Dave Jones:** Yeah. Sorry if I've been a little out of... I've been checking your math here, Dave. I don't think your bit counts right. Why? Nine bits? I don't think it's nine bits.

**Chris Gammell:** Well, from zero to 63 is... But because we didn't have the zero, you know, I'm counting the zero in there.

**Dave Jones:** One, two, four, eight, six, four, thirty-two, sixty-four. Yes. That's the eighth bit.

**Chris Gammell:** With eight bits, you can represent...

**Dave Jones:** No, that's the seventh bit.

**Chris Gammell:** Oh, sorry. Duh. What was I talking about?

**Dave Jones:** That's the seventh bit. There we go. Okay. So, we're good now. All right. Analog guy here. It didn't sound right, and I got all thrown off, and now I'm... I had to... Yeah. Yeah. Well, that's embarrassing. Eight bit, seventh bit. That's okay. It's okay to make mistakes, people. I'm okay with this. Are you okay with this?

**Speaker ?:** What?

**Dave Jones:** We caught it. It didn't ship, right?

**Chris Gammell:** Right. Okay. We can post-edit, can we?

**Dave Jones:** What the hell came over here? The product didn't ship. The product didn't ship. The episode's going out like, this is pure gold. This is... Right. Chris points back to this and says, hey, Dave, remember that ninth bit?

**Chris Gammell:** Where the hell did that come from?

**Dave Jones:** I don't know.

**Chris Gammell:** Man, I... Okay, that's fine. It must be too early in the morning.

**Dave Jones:** Oh, yeah, that's the real problem.

**Chris Gammell:** I didn't even think about it. I just popped it like it wasn't even on the list, and then I thought, oh, what can I add to the intro? Hey, 64, shit. And I don't know.

**Dave Jones:** 120. You think we'll make it to 128 with these kind of Chris corrections, me being a big butthole about correcting you? I don't know, man. I don't know.

**Chris Gammell:** I think we should start again.

**Dave Jones:** No, you're fine. People will love this. Believe me.

**Chris Gammell:** Man. They'll love it. That's just... Oh. Forehead slap. Hang on.

**Speaker ?:** Oh.

**Dave Jones:** That's good radio. That's good radio.

**Chris Gammell:** Yeah, it is.

**Dave Jones:** So what's going on? We have an update from last week. I mean, 64th episode, that's good, but you had some bad news from last week, huh?

**Chris Gammell:** Yeah. Like, I bragged that I was, what, hours away from...

**Dave Jones:** I think we cursed it.

**Chris Gammell:** ...sign... I know. I was supposed to be hours away from signing the... Putting down the deposit for my new place, and then it would have been mine, my new EEV blog, Nerd Cave slash lab, and no, it fell through. Instead of putting down the deposit, apparently this douchebag emailed... I'm going to call him out. Emailed the agent who we were going through and said, sorry, changed my mind, don't want to sell it anymore. Tough tits.

**Dave Jones:** I can't believe you're allowed to even do that, you know? You'd think at a certain point in a contract, it'd be like...

**Chris Gammell:** Well, there was nothing signed, so you don't, you know, there's no legal basis whatsoever. There's no legal recourse at all.

**Dave Jones:** And even if there was, then you'd have to get a lawyer involved, and yada, yada, yada.

**Chris Gammell:** No, it's just, yeah, it doesn't happen. So, yeah, he's just a douchebag in the story. Yeah. Sorry, man. I know. Yeah, so much for keeping your word these days.

**Dave Jones:** Yeah.

**Chris Gammell:** It's hopeless.

**Dave Jones:** Oh. So what's in the plans for the future? You still looking?

**Chris Gammell:** Yeah, still looking, but there's nothing out there at the moment. So, well, we had one other choice, but it was too far away. I did, like, you know, I actually rode my bike there and did a test ride, but it's like, it was at least a 15-minute ride each way, and by the time you get your cycling clothes on and you get there, and it's the middle of summer, and you've got to have a shower, because you're sweating like a pig, and it's, you know, it, eh. And as far as driving there, it's like the worst street within, you know, 30 kilometers. It is awful. Like, you just do not go during peak hours, you know. Oh, yeah. So there'd be like four hours a day that I wouldn't be able to drive there, you know, even if I wouldn't see.

**Dave Jones:** Oh, no, that's, yeah.

**Chris Gammell:** It'd be, ah.

**Dave Jones:** No.

**Chris Gammell:** So I had to turn that one down. It was really nice. I had views over the mountains, over the Blue Mountains, and, yeah, pretty schmick. Actually, the hard part was, is that when you've got those nice, you know, floor-to-ceiling windows in your office, you feel like as though you shouldn't put anything there, like you shouldn't put benches along there, or you shouldn't do anything, because you've got these lovely floor-to-ceiling windows, so why would you, you know, like pile stuff up in front of it? So then you instantly lose, you know, a whole wall. That's a good thing or a bad thing? It's a bad thing, that you actually lose space. So you need to get,

**Dave Jones:** you need to get a basement space like me and be a troll.

**Chris Gammell:** A troll. Well, that's the one I was going to get. You know, it was literally down on the bottom floor and you had to walk down the stairs and you turn around the corner and you're down in the dungeon, you know.

**Dave Jones:** There you go. Yeah. Turn the lights off. Oh boy.

**Chris Gammell:** Anyway.

**Dave Jones:** Do you work in the dark? I know it's people that work in the dark and I just, I don't get that.

**Chris Gammell:** No, I don't get it either.

**Dave Jones:** Some people like, like, they like real low, like lighting overhead, you know, they'll just have like a desk lamp or something like that. Ugh. It makes me want to fall asleep.

**Chris Gammell:** I do if I'm, I do if I'm reading at night. If I'm reading my Kindle at night, you know, I actually deliberately put flat batteries in my little reading light so it is dim, you know, otherwise it's too bright.

**Dave Jones:** Oh, right. So, I get that. I'm just saying that like, you know, I know some people at companies I've worked at where they prefer like a really dark sitting situation so that they, I don't know why, like if they get migraines or something, but then they need this really bright light so they can actually see the components on their board when they're doing soldering or just trying to, you know,

**Speaker ?:** work on something. Well,

**Chris Gammell:** that's why you want to have one of those magnified headlamps with the lights on it, you know.

**Dave Jones:** Yeah, but if that's your only light, that sucks. I don't know.

**Chris Gammell:** I know. I know people like that. The first thing they do when they move into a new Dilbert cubicle is they stand on the chair, they get up and they, and they take, you know, they take a bulb out or a tube out of the lights above them, you know. Huh. That's crazy.

**Speaker ?:** So,

**Chris Gammell:** you know, well, it's at least half or they take both out and they rely on, because usually they're a dual tube thing. I don't know what it's like in the US, but in offices, they're usually,

**Dave Jones:** yeah, a dual tube. Not me. I don't do that. I want a fluorescent suntan. I want it to be so bright.

**Speaker ?:** Right.

**Chris Gammell:** To bounce off that pasty white skin.

**Dave Jones:** That's right. I need a tan, man. That nerdy skin. I want to glow green. That's how bad I want it, you know, because of the fluorescent, you know, the hue that's on it. Oh, yeah, that's what I need, you know.

**Chris Gammell:** I'm still thinking about the 64 bits, the 64. Don't worry about it, man. You goofed it again, 64 episodes.

**Dave Jones:** You'll be fine. You're fine. You're fine.

**Chris Gammell:** I'm devastated. It is just...

**Dave Jones:** I know, all this buildup, all these weeks, huh?

**Speaker ?:** Well,

**Chris Gammell:** I didn't even think about this morning. We were going through the show notes before this, and we didn't even, it wasn't even on here that this was episode 64. We mentioned it at the end of last week to each other. We said, oh, yeah, next week, 64. Yeah.

**Dave Jones:** I knew.

**Chris Gammell:** I just popped in there, blurred it out, and for some reason, I'm like, oh, oh.

**Dave Jones:** Career-ending move right there, Dave. You'll never work in radio. You'll never work in radio again. Right. Yeah, right.

**Chris Gammell:** Speaking of new offices and taking out flu-ray lights and all that sort of jazz, the Altium, while I was looking for offices to move into, up popped on the real estate website, the former, well, the former Altium Sydney headquarters where I used to work, and there it is.

**Dave Jones:** You just roller skate around there, you'd have enough room.

**Chris Gammell:** I know.

**Dave Jones:** You'd take the bike inside, right?

**Chris Gammell:** Exactly. It's a pretty darn big building. It was actually purpose-built for Altium. It was purpose-built to our specs, and, you know, so each, I've mentioned before, you know, each Dilbert cubicle has got like four one-gigbit Ethernet cables going to it. I don't know why, but that's, you know, and you can see photos of it. You can post a link. For the Internet of Things, Dave. For the Internet of Things, you know.

**Dave Jones:** You need to be able to hook up everything, right?

**Chris Gammell:** Yeah. I'm not sure if they'd gone on the Internet of Things fad when we built the building, maybe. Yeah. I don't know, but yeah. I'm not sure what fad they were in at the time. Anyway, they change fads every six months, you know. Yeah, but let's not go there. Anyway, you can see the abandoned office, and you can see there's a couple of people still working in there, and you can see the canteen which has been deserted. There's no more free food. Oh, sad. It's all gone. And you can see where I used to work, the back corner.

**Dave Jones:** Should be a historical landmark, right?

**Chris Gammell:** Right, yeah. Did some of my best work there. Not.

**Dave Jones:** Yeah.

**Chris Gammell:** Oh, boy. Anyway. And yeah, I just thought it was funny, and then somebody, commented on, was it Twitter, or YouTube, or somewhere? Anyway, no, the forum.

**Dave Jones:** God, got so many avenues. So many places to yell at Dave. Absolutely.

**Chris Gammell:** On the forum, somebody, sorry, I forgot your name, and excellent idea. Why don't they turn the abandoned Altium headquarters into a hackerspace? It'd be the world's biggest and coolest hackerspace. It'd be awesome.

**Dave Jones:** The biggest tax bill.

**Chris Gammell:** And I don't care about the practicality of it. It's just a cool idea. Yeah. I'm sorry. It's just awesome.

**Dave Jones:** Yeah.

**Chris Gammell:** You know, it's sitting there doing nothing. And it's, it's,

**Chris Gammell:** Shane, there must be, how many thousands of companies like this with space that's just, you know, not being used anymore because of the downturn in the economy and all that sort of stuff. You know, they might have to turn the lights out in half the building or something like that. Yeah. And there must be plenty of companies like that who have all this space available. And, you know, here, the, you know, the Melbourne hackerspace I went to, they've been trying for two years to find a space. You know, there's just gotta be.

**Dave Jones:** It's expensive though. Like all that, I mean, the practical side, right? The buzzkill Chris coming out is like, well, you gotta heat it, you gotta cool it, you gotta power it, you know, all that other junk and gotta maintain it.

**Chris Gammell:** Yeah, but, but all those things aside,

**Dave Jones:** I completely agree with you.

**Chris Gammell:** Yeah, right. Okay, all that practical shit aside and the liability and all that sort of stuff. Yeah, I mean,

**Dave Jones:** I've been in a hackerspace that was like, not heated in the winter because they couldn't afford it and that was not fun. Right. So, if I want to be shivering cold, I'll sit in my basement in the winter. Okay.

**Chris Gammell:** It kind of reminds me of gyms. It's a bit off topic, but it's something I'm into, you know, and I used to go to this gym which was just had a hot tin roof, you know, it was a tin, it was an upper floor but it didn't have air con, it had a couple of fans to circulate the heat. Yeah, that always helps.

**Speaker ?:** you know,

**Chris Gammell:** in the middle of winter. So, you know, I'd go there like, you know, seven o'clock on a Sunday morning and I'd do a class in the middle of winter and you're freezing your ass off, right? And then in the middle of summer, it'd be 40 plus degrees and here you are doing a cardio class and I'd lose two kilos of sweating one hour. Yeah, exactly. Two kilos. It's like, wow.

**Dave Jones:** I have no idea what that is.

**Chris Gammell:** Ah, right, times 2.2 for pounds. So, there you go. What is it? About 10 pounds. Right, okay.

**Dave Jones:** No, two, oh, five pounds. Yeah, 2.2.

**Chris Gammell:** Two times 2.2. So, yeah, so five pounds, my bad. Yeah. See,

**Dave Jones:** there's my math mistake for today, Dave. There you go. In an hour, if you work hard enough. You feel better? Oh,

**Chris Gammell:** boy. Anyway, I think it's a brilliant idea. Why can't we turn these unused technology office spaces into mass hacker labs? Maybe we should just do a, like an occupy kind of thing. We should just walk in there and occupy something. Oh,

**Dave Jones:** that's a great idea. Yeah.

**Chris Gammell:** It's brilliant. Why not?

**Dave Jones:** They can't afford electricity. They probably can't afford security guards.

**Chris Gammell:** They can't afford security guards or legal fees to prosecute. Let's just go occupy the building, you know? Yeah. Why not? I love it.

**Dave Jones:** That's good, man. I like it. I like it.

**Chris Gammell:** Well, they're doing that in the US, aren't they? With all these foreclosures, there's, you know, people, they actually go in, they occupy houses. They go back and they take, you know, we reclaim this house in the name of the community, you know, and they actually, and they're actually winning. They are able to do that, apparently.

**Dave Jones:** So. I had not heard about that. No. I'm going to go, I'm going to go steal my neighbor's house. There we go. Awesome. All right. All right. What else have we got? Well, we got a couple of shout outs this week. Speaking of labs, I saw a thing on EDN. Did you see this? Yeah, this is good. Yeah. They, so, you know, Jim Williams passed away. We talked about that on the show, but Paul Rako, you know, he knew, he knew Jim and he knew Bob Peace and he writes for EDN. And basically though, they, they're just taking the whole, Jim's entire bench piecemeal over to the, the computer history museum. So they, there's a picture of it on the, on the website too. It's brilliant. Yeah. And, and he just, he just basically, I don't know. I think they, I didn't, I didn't catch the exact syntax of it, but I thought it said that Jim actually donated and it was already wrapped. Like he already did all the wrapping. So basically they, you know, he had, he had just components all over his bench and we'll, we'll link in this story so you can check it out. Yep. The, the original picture, but you know, he would just have tons of components on his bench and he would, you know, it's just a junk pile. Basically he'd go over and he picks something out when he needs it.

**Dave Jones:** you know, he's probably got, you know, 10 grand and chips on his bench. Right. But he would just go and pick it out. And when he didn't need stuff, we'd throw it down. And then, so in moving this, they just shrunk wrapped the entire thing and then they moved it all. It was amazing.

**Chris Gammell:** Apparently that's how he moved his bench once. It's not the first time he's actually moved his bench. Oh, that's what I got wrong. Yeah. So this is how he did it last. Like they, they, they asked somebody, how did he move his bench last time? And they went, well, he just got out the shrink wrap and, and shrink wrapped the whole thing with components, with the project he was still working on all on the bench. And they just carried it. So they thought, oh yeah, that's how we can move it. Cause they were scratching their head. Apparently, you know, how the hell can we move Jim? Williams is benched to the computer history museum.

**Dave Jones:** Yeah.

**Chris Gammell:** You can't, it's got 10,000 components sitting on it.

**Dave Jones:** Yeah. You know, so here's my idea. I have an auxiliary idea. I like what they're doing. I think it definitely belongs in the computer history museum. Here's what I say though. I say shellac the whole thing, right? So the components are actually glued down. Right. And then what you do is you have, you turn it into a wishing well and people can bring their busted up components and they can flip it onto there and make a wish. Right. You know, there would be like the velvet ropes around it and then you flip a component and then it lands on there. You make a wish and then, you know, they can sweep off the components once a day or whenever they need to. And then it's still, it still looks like it's supposed to look right. Cause someone, some, some, some butthole would probably end up like throwing a transformer or something like that on there. And, and then, you know, it's like a, it's like a wishing well. It's a, it's, it's, it's a nice piece of lore, right? You flip your busted up resistors.

**Chris Gammell:** That is a brilliant idea. That is good.

**Dave Jones:** So if anyone knows the computer history museum, people tell them my idea. I don't charge royalties. They are welcome to have it. I got to say it's a, I want to go there. I want to, I want to pay my tributes to Jim Williams by flipping on, a couple of burned up transistors directly onto there.

**Chris Gammell:** That's great.

**Dave Jones:** The most charred ones I can get. Yeah. Yeah. So I thought that was great. So I'm, I'm glad they're doing that. And I'm glad Paul's, Paul's covering that, that story.

**Chris Gammell:** And apparently it's part of a, a, an exhibit honoring, um, uh, engineers at work. It's called, they're building an engineers at work exhibit. Yeah. Oh, it's going to open on October 15th. What's the date today? There you go. It's the 11th here. There you go. Yeah. All right. Over there. Yep. There you go. So it's opening this week.

**Dave Jones:** Yeah. Brilliant.

**Chris Gammell:** Yeah. So if you haven't been to the computer history museum, I've been there. It is really, really good. I did not get a chance to get over there. Oh man, you missed a really cool thing. So I was kind of busy, gotta say. Right. Anyway. Yeah. Yeah. I walked all the way from somewhere. I walked like an hour to get there. From somewhere, huh? Did you walk from? Yeah, somewhere. I don't know.

**Dave Jones:** Australia? Yeah.

**Chris Gammell:** Yeah. Somewhere in Silicon Valley. Yeah. Ah, well. Yeah, that's good. That's great.

**Dave Jones:** Another shout out is on the media side of things. I don't know if you've been watching these, the EE web, how they do interviews. Speaking of engineers of today.

**Speaker ?:** I have.

**Chris Gammell:** I've been on there.

**Dave Jones:** Yep. Have you? I didn't see yours on there. Yeah, I thought I thought.

**Chris Gammell:** Way, way, way back. Way back.

**Dave Jones:** Maybe they've already flipped pages. I saw mine, and I was going to link mine in. Yeah,

**Dave Jones:** No,

**Chris Gammell:** yeah, I'm there somewhere. Yeah. Yep.

**Dave Jones:** Huh. Yeah,

**Chris Gammell:** we've talked about it before.

**Dave Jones:** That's what I thought. Oh, there you are. Oh, they spelled David. That's why. Okay. Oh, right. Dave's on there. I'm on there. Jerry's on there. There's a bunch of people on there. Lemore's on there.

**Chris Gammell:** They've got a lot of people now. What is that? What? 50 or 100?

**Dave Jones:** 50 at least. Yeah. And you know, and they seem to keep getting better. I think people kind of go back and look at the other ones, and either that or they're getting more interesting people. But I'm really enjoying these a lot, and I think it's a great idea. I mean, so it's a great way to kind of informally meet people, and I highly encourage people to go through and just see what people write about. It's interesting seeing topics and trends through it. You know, like they always ask favorite book, and it's like, oh, okay, Art of Electronics, of course. Yeah, yeah, everyone of course. You know, like, yeah, that's right. But then there's a couple others in there, and I saw one that I really liked. Oh, I'm not gonna be able to find it now, but it's an audio power amplifier book, and it's just really good as a discrete amplifier book. You know, that's one that I have at work. And you know, you kind of just see verification of it. It's like, oh, okay, I'm not like totally off my base, you know, using this book that it's wrong. You know, it's nice to see that kind of thing, you know, and yeah. Yeah. So, lots of fun. I like it a lot, and I hope to keep doing it, so.

**Chris Gammell:** Well, I'm supposed to be in their Pulse, magazine too. They've got this mag, it's called Pulse, and it's really quite good. It's got some great articles and stuff in there. Yeah, I was supposed to be in it. This was like months ago, and they sent me the proof of it, you know, and I was, it featured my new project I'm working on, my scientific calculator watch, Mark II was in there, and yeah, I haven't seen it yet. so, I don't know, I think they do a lot of this stuff well ahead of time, and then they just schedule them out, so. Yeah, it's more like a,

**Dave Jones:** it's like somewhere between an online and a traditional publishing magazine. Yeah. So, yeah, it's tough.

**Chris Gammell:** They're doing a hell of a lot of work there, so, well done.

**Dave Jones:** Yeah, yeah, keep it up guys. It's great.

**Chris Gammell:** It's the only engineering portal, you know, in the quote marks, portal website, I find any good at all. All the others are shit, you know, like Element 14 and Design Spark, and all the other magazines try and be, you know, these portals, and they all suck. This is the only one I find that's actually, I would want to go back to.

**Dave Jones:** Yeah, like the format and everything. Yeah, yeah,

**Chris Gammell:** yeah, the format and they've got great, you know, they've got good technical articles and stuff. Yeah,

**Dave Jones:** I think it kind of suits, suits what you and I like. It's kind of WordPress like, and you know, it's standard like that. So, I agree. I think it's, it's definitely, it suits me the best. I like it the best, so.

**Chris Gammell:** Yeah. And they put a lot of work into actually getting good content on there. So, yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** I like it. Oh, cool. Keep it up, E-Well. We are hiring. Are they hiring? Are they?

**Dave Jones:** I don't know. Yes,

**Chris Gammell:** and yes, it looks like they are.

**Dave Jones:** There you go, Dave, get yourself a real job, hippie.

**Chris Gammell:** Oh, boy. Anyway.

**Dave Jones:** And, stick, yeah, right. This is actually a story from a couple weeks ago, but, there's, sticking in the media side of things, there's Sesame Street, actually.

**Chris Gammell:** Let's go to Sesame Street.

**Dave Jones:** Why not, right? They're, they're encouraging engineering on there, though. That's, it's great. I mean, there's a, there's a video and, it was actually suggested to us by Chris Felton, but, yeah, great, great use of, you know, a kid's platform to kind of promote engineering and stuff. So, I'm all about it. I think it's great. And we'll post a link to that too. It's a lot of fun.

**Chris Gammell:** Cool. Sesame Street. Love it. Yeah. Groucho was my, yeah, we got, I think Groucho was my favorite. Groucho? Yeah, is he the one in the trash can? Oh, yeah, yeah, Oscar the Grouch. Oscar the Grouch, yeah, right. Yeah. Not Groucho. Sorry. Apology to all Groucho Marx fans, you know.

**Dave Jones:** I'm sure his eyebrows are based off Groucho Marx. Right, okay.

**Chris Gammell:** Yes. Brilliant stuff. Yeah, anything that gets kids involved is fine by me.

**Dave Jones:** Yeah, yeah, I mean,

**Chris Gammell:** we're seeing a lot of, we were seeing a lot of, we were seeing a lot of Justin Bieber, and then, well, no.

**Dave Jones:** No.

**Chris Gammell:** Then it's a fail instantly.

**Dave Jones:** Definitely not, definitely not. And speaking of, you know, electronics for kids, there was actually another open source hardware company that, that, the fourth one got funding this week. I don't know if you saw that, Dave.

**Chris Gammell:** It did, I saw it, and Aya, is that a name? How do you pronounce the name? I believe it's Aya. I think that's how you say it. Aya. And, by the way, it's a girl, by the way, everyone out there, it's a girl, which is cool.

**Dave Jones:** Okay.

**Chris Gammell:** Well, no, it's just that it's not, you know, that usual in the industry, so it's cool.

**Dave Jones:** Fill in your bingo spots, folks. We, we have Dave going back into girls and engineering. There you go. Why? You don't like it? No, I think it's great. I just don't think it's, I don't think it's out of the ordinary these days. I mean, I think she's very talented.

**Chris Gammell:** It's getting less out of the ordinary, I've got to admit. Yep.

**Dave Jones:** Right. It's not like, whoa, it's like, great work. Yeah. Yeah, I know. So anyways, yeah, she's, she got funding though, and it doesn't say how much, you know, we'll link directly to her website, but.

**Chris Gammell:** I get the suspicion that it's not much at all. Well,

**Dave Jones:** we don't, we don't know that, but.

**Chris Gammell:** Well, yeah, like it's not $10 million that they just gave to make a bot. You know, I, I don't think it's that level. I think it's not even close to that. I'd be even surprised if it was seven figures. Because, yeah. Maybe. I don't know. I don't know. Because, yeah, it's a neat little concept. They've got, they've got, got these little building blocks, which snap together with magnets and they form little, uh, educational circuits, you know? Yeah. And yeah, it's cool. There's a few different concepts out there that do a similar, um, sort of thing, but this one uses magnets or something. I'm not sure of the exact mechanism, but, uh, they're color coded too for, for hooking up as well. And yep. Color coded and all that sort of stuff, which is neat. Um, yeah. And, um, it's excellent that they got funding, but I've got a, I don't know.

**Dave Jones:** You don't know. What, what don't you know about Dave?

**Chris Gammell:** I'm just like, this is the fourth open source hardware company. That's got in some way, some sort of venture capital funding. Right. And this is, and this is by far the smallest of the lot, I think, um, in terms of scale and, uh, in probably in terms of money as well. Um, and in terms of potential market, you know, for this thing, it's very niche. Um, and you know, it's not, um, you know, it's not going to be a hundred million dollar company, for example, you know, it's not a hundred million dollars worth of business in little education. We should compare against,

**Dave Jones:** against the other ones too. So that's Chumbie is one. That's a Bung Hwan. Yeah,

**Chris Gammell:** Chumbie has big potential, right? Because it's an internet appliance, right? That people can have in their home. There's a massive market for that sort of thing. Um, and of, and of course the MakerBot as well, which has a potential massive market, you know? So. And can Dave name number three?

**Dave Jones:** I don't know if he can.

**Chris Gammell:** Uh, would be Bug Labs.

**Dave Jones:** Yeah, that's right. Bug Labs, who just signed a deal with Ford and a couple other people in Verizon, I think. So, so they're definitely already kind of big into the game too. So.

**Chris Gammell:** Yep. So yeah, yeah, they're all big potential. This is a,

**Speaker ?:** so,

**Chris Gammell:** you know, it's a cool concept, but it's much more niche. Um, so, and I've got a question, why, you know, why would you take funding? If you're, if you're, if you've bootstrapped yourself, which is the way all these companies work, right? All these startup, you know, garage, companies, open source hardware companies start, then you're already, you know, it's likely that you're not in debt. You don't need the money. Like, why would you take investment from someone?

**Dave Jones:** Well, maybe, I mean, maybe if, if you need a production run though, I mean, I think that there's, there's, if, if it's a smaller run thing, I mean, if it, if it is a smaller company too, I think that there's, you know, if you needed to get a big production run to get some economies of scale, then you can, you can justify taking, I think there's justification.

**Chris Gammell:** But you usually don't need to in these niche sort of applications. People will pay a premium because they know it's sort of niche. So. Maybe, I don't know. If this is playing in the educational space, it just might not be there. you make the more, you know, it's a bootstrapping thing. You know, you make this money that you can then invest in. You can then invest yourself in the future of the business. So in high volume manufacturing stuff. And it doesn't take that long to make, you know, $50,000 out of something. And then you can put that into tooling for some sort of thing. You know, it's. I can't plan to know.

**Dave Jones:** I don't know. I don't know.

**Chris Gammell:** I don't know the specific details. I'm more, I'm more talking in general now. So.

**Dave Jones:** Right.

**Chris Gammell:** Okay. So, you know,

**Dave Jones:** even if it was a larger, a larger enterprise, right. If it was a 50 person company to start with, right. That had bootstrapped. That's what you're really asking about. Why, why then? And there's actually, there's a, there's a link with breathe that.

**Chris Gammell:** Well, no, I'm talking about these one or two people companies.

**Dave Jones:** Oh, those. Well, I don't know. Maybe it's the.

**Chris Gammell:** Why wouldn't you just continue to bootstrap yourself and own everything? I, I don't know why you would take. I guess it depends on the money, right? If somebody comes along and says, here's a million bucks, but.

**Dave Jones:** And the terms too. I think the terms are another big thing, right?

**Chris Gammell:** Well, the terms are that we basically pretty much own your company. And if you don't produce, we screw you. That's. Yeah.

**Dave Jones:** That's venture capital. That's different than angel capital. This seems like it's very angel specific, right? Cause she calls out specific people. What's the difference? Angel investing is. Usually with a very low likelihood of getting the money back,

**Chris Gammell:** but they still want their money back and they still own. And what they still will own your company, right?

**Dave Jones:** Well,

**Chris Gammell:** the majority of it, I, I don't really see the distinction. I think they're pretty much the same thing. And the, you know, they're both wolves in a different clothing. Really?

**Dave Jones:** Hmm. I'm trying to find the, uh, the specific difference here, but right. That might take a while. Yeah.

**Chris Gammell:** I don't think there, I don't think there is when people give you money, they give you money because they expect a return on that money or that, the likelihood of a return. And if that looks like they're not going to get that return, well, that's when things turn, you know, nasty.

**Dave Jones:** I guess so.

**Chris Gammell:** You know, I, I can't see anyone coming along. Oh, I don't, oh, you failed. Oh, okay. I don't care to do whatever you want. I didn't really put the money in there for, you know, no, I don't think that's true though.

**Dave Jones:** Cause we've, we've even talked about on here before that, uh, the guy that was the, the creator of Gmail, he was a investor and he talked about how many things he invested in that he didn't expect any kind of return out of just because it was a high risk situation.

**Chris Gammell:** Right. So he effectively just bought, you know, I smell like a shares in the shares in that company or something, or, you know, he, he bought a stake in that company, but didn't want to have any say in how it was run or anything like that. Uh, I think you wanted to advise them, but yeah. Well, if you're an angel investor or if you're a, um, you know, one of these, uh, um, investment mobs, I guess it depends on how much you invest, right? If you don't get a controlling interest, you don't get a say, I guess that's what it comes down to. Right. Yeah. I could see that. Yeah. Right. So anyway,

**Dave Jones:** I don't know.

**Chris Gammell:** It seems to be a trend though.

**Dave Jones:** You're just, you're just asking about why people would take money.

**Chris Gammell:** Why people take the money and why they don't just continue to do it themselves. I,

**Dave Jones:** I don't know. I think, I think that's more of a one-off question. I, I think, I think in certain situations, I think you have to look at the bigger, the bigger situations, you know, like, I think there's significant costs that, you know, when you scale up that you would have to, you have to take on. And, uh, you know, Phil Terone did an interview with Bree about that. And basically it's like an inventory thing. You know, inventory is damn expensive. Yeah. Building out your, your, uh, your employees is expensive. Real estate's expensive. There's just a lot of really big costs that sometimes you can't take on without, without either a alone. And if you can't get a loan, then where you're going to go, you have to go to some kind of funding source and they're going to maybe take a, a bite out of your ass for, you know, for, you know, using that money, but there's, it's a calculated risk, right? So,

**Chris Gammell:** yep.

**Dave Jones:** I had a bigger question about, about that whole thing though. I asked it on the open hardware list and I really didn't get any responses. I mean, I got a response from Bree on, on, on their, their situation, at least in a roundabout way. It was basically, you know, if you're an open source hardware company, does it get written into the, into the contract? You know, is it like, okay, we are only going to be an open source hardware company or is it like, well, when it's convenient, it's going to be, we do what we need to. Now, the realist in me says it's going to be the second one, you know, if it, of course it is. If the business conditions change, then yeah, but it's just, it was just interesting to me. You know, Bree's response was, well, it's, we're, we're dedicated to being an open source hardware company. And I think that's kind of a, a de facto response. And I, I understand that. It's like, he's not going to say, he's not going to say.

**Chris Gammell:** That is not the legal response. That is not the legal response of that, of the contract they've got with them. I'm sure. No, it's,

**Dave Jones:** it's do whatever we need to, to make money, which is understandable. It's a business, right? Yeah. At a certain point, it transfers from an open source hardware, I think is a viable business model. I'm not sure how scalable it is. You know, I don't know if a billion dollar company could, but I think it is very viable, at least in the stages that those three companies aren't. And hopefully, you know, Aya does as well. But yeah, it's interesting to me. It'll be interesting as they get bigger and bigger too. And, you know, as even we've talked about Adafruit and SparkFun and those other ones that as they get bigger, you know, their dedication to open source as well. I mean, I, I don't question it. It's just how it's going to play out. That's the main thing.

**Chris Gammell:** Well, I've already made a guess at that in my, my video I did on the, uh, Paykabot, uh, funding thing.

**Dave Jones:** And I predicted that within several years,

**Chris Gammell:** they will, they will simply not be, they, they will stop selling kits that I, I reckon that's almost a given. They will eventually stop selling kits. And once you stop selling kits, there's no point making it open hardware really, because you know, it's, it's going to require advanced custom parts and nobody's going to be able to, build it themselves anymore or modify it or something like that. So they'll just, you know, they might call it open hardware because, oh yeah, technically the plans for various things might be out there, but nobody's going to build upon it because it'll just be so complex that, you know,

**Dave Jones:** Are you saying from a complexity standpoint, not a, not a complexity standpoint,

**Chris Gammell:** once you get to a certain, a certain complexity, it's, you know, you could almost argue that it's almost pointless being open source, um, hardware, because people are only going to use the build up product. And, but it's good from the fact that it's in, in terms of like this software and the interfaces are open so that you can build, you know, you know, you can talk to it with different software products or add ons or something like that, perhaps. But yeah, it's, um, but in terms of the physical hardware build itself, you know, it's just no point being open hardware anymore. I don't think. So anyway, I predict that they'll stop selling kits for starters. And, um, yeah, they, and if it goes mainstream, well, nobody will care. Like if you've got regular engineers buying this thing or even regular consumers, which I'm sure is one of their ultimate goals is to get, you know, is to make this a consumer item that people have in their home. Right. People will go, huh? Open hardware. What's that? I don't care. It's just a thing which doesn't matter in the consumer industry. Really. So, um, you know, there's, there's no selling advantage to that as far as the consumer is concerned. And you could argue even technical consumers, a lot won't care. They just care. I want to buy something that works. End of story. You know?

**Dave Jones:** Yeah.

**Chris Gammell:** Anyway, it's a complex, messy, muddy business. And very case specific.

**Dave Jones:** I agree.

**Chris Gammell:** I don't know. Have we talked enough about open hardware?

**Dave Jones:** I think so. Yeah.

**Chris Gammell:** We weren't supposed to, right? Because we're trying to wean ourselves off.

**Dave Jones:** I don't, it's, it's intriguing to me. I don't know. It's, it keeps coming up. I think it's in, it's in the stuff that I read. And I think that's in the stuff that you read. Yeah. And, uh, yeah. So it's in the forefront of my mind. I mean, it's, I'm, I'm very intrigued by, I, I, I'm sorry if people out there aren't, aren't interested in it, you know, but I think it, I think it's a significant upcoming force in electronics today. If you know, like it or not, I think maybe not, maybe not the highest end electronics, but, um, yeah, I think, I think it, I think there's a, I think it's a, a growing force and it's, it's something, it's something to talk about. So,

**Chris Gammell:** yeah. It, well, it's good in that if it just leads to all products, especially consumer products being more open, not necessarily in terms of,

**Chris Gammell:** here's the, you know, here's the, uh, Gerber files and the CAD files for your latest mobile phone. Right. But it just in terms of, you know, just the, the software interface so that you can talk to the thing or do something simple like that, you know, so, so that you can hack it. Um, yeah. So, yeah. Yeah. Yeah. Open.

**Dave Jones:** Yeah. Open, open ecosystems are good for, for that kind of development,

**Chris Gammell:** but it's just open product. Cause you know, uh, open hardware, you know, there's, there's a concept of, Oh no, we're going to talk about it.

**Dave Jones:** no.

**Chris Gammell:** I know. I got to stop myself. I physically pull myself away. Yeah. All right. I'll, I'll stop now. I was going to go off another tangent,

**Dave Jones:** but yeah.

**Speaker ?:** Okay.

**Chris Gammell:** Please find another topic.

**Dave Jones:** Okay. How about the other direction? Let's go, let's go really big. Let's go not so small and open source. How about, how about really big and, and unbelievably, uh, massive and hard to fathom. So, uh, surprise me. David Manners is a guy that writes for, uh, uh, electronics weekly. And, and he's basically talking about the, the, the fab side of things, you know, like how, how is all this stuff?

**Chris Gammell:** We got chip fabs again. Bingo. Sorry. You know where it's going to lead.

**Dave Jones:** I'm not going to get to that. All right. But basically he's saying that the leading edge side of things, like, you know, like being the first to, God, they're running out of nanometers. Right. But like, you know, the first to 10 nanometers, right. Once you get there that, because it's so difficult to get there now, the chip companies will have an advantage for many, many years. So, eh, maybe I'll get there. Uh, you know, so basically it'll be harder to get certain types of chips, you know, like they're, the biggest stuff will be made by the biggest vendors. You know, Samsung will make all your memory Intel, make all your processors, microchip will make all your, your, you know, microcontrollers or, you know,

**Chris Gammell:** that currently how it works.

**Dave Jones:** Well, yeah, but what about, I mean, if, if there's any kind of new entrance to the market, it means get used to your brands and, and make friends with your FAEs, I guess. Right. I mean like, cause they're not going to go away. I mean, cause there's not any other options, right? To the point where there's not even like, you know, they talk about fabulous models and how, oh, all these companies coming up in China and India and it's, well, no, that's not going to happen either because there'll be no fabulous capacity. There won't be enough because the Samsung's and the, I guess Intel and Samsung have their own fabs, but you know, the microchips of the world or other people who don't have their own fabs and use. They have their own fabs. No, they do too. Okay. So other foundry list models, other people without foundries, right? Or without, without fabs. Fabulous companies. The fab, the fabulous companies basically will be buying up capacity so soon in these foundries that no one will be able to get in because they'll be buying it based on future projections. So I don't know. I thought it was really interesting idea. Like the fact that people are going to get the chip companies are going to get locked out because it'll be such, so hard to, you know, they'll, they'll plan it so much because the stuff's so expensive in the first place, all this equipment and the build out and everything. So that's the other, I guess that's the other side of things. I don't know.

**Chris Gammell:** So the heading of it is no more cheap wafers.

**Dave Jones:** Right. And because of that. Yeah. Because, you know, once you have control of a node, you know, if, if you're to 10 nanometers first, right? If Intel gets to 10 nanometers first and it takes them $10 billion to build a new fab, like they're doing in, in New York or 5 billion in that case, and they make this 10 nanometer ship and no one can touch them for 10 years, for three years. Right. They're going to charge you $400 for that chip and there's nothing you can do about it. Right. Yeah,

**Chris Gammell:** of course.

**Dave Jones:** Yeah. So, so then the economics might pay, play towards something else, which I won't mention. I won't mention it here. Maybe I'll mention it offline somewhere, but, uh, yeah.

**Chris Gammell:** 10 nanometers at home, folks. Chris says it's possible.

**Dave Jones:** Yeah. Jeez. So if you have chips, then what, what else could you do? You could do a contest, right, Dave? It's a horrible segue.

**Dave Jones:** you could. That was a horrible segue. It was just disastrous. Uh, yeah, TI is having a contest. You want to talk about this?

**Chris Gammell:** Another contest, TI, um, what, you've got to use three TI analog ICs? Uh, yes, there was two analog ICs and a processor.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** And it's for a senior project only. I was kind of disappointed they did this.

**Chris Gammell:** Hang on. It's an analog design contest, right?

**Dave Jones:** Yeah.

**Chris Gammell:** Yet you're allowed to use a TI processor. What? Come on. Yeah. Give me a break.

**Dave Jones:** Yeah. I mean, the, the, the realist, this isn't even a realist anymore. This is a pessimist in me. The pessimist in me says, this is all just a huge ploy for recruiting because they say it's only college seniors. It's only for senior project. And you have to be at an, an ABET accredited university. Right?

**Chris Gammell:** Right.

**Dave Jones:** Yeah. And it's like, if they really wanted to do a design contest, they'd open it up to anyone. Uh huh.

**Chris Gammell:** They're ticking all the boxes for the fun, sucking, you know, graduates through the funnel.

**Dave Jones:** Right. And so, yeah, that's, yeah, that's the, that's the pessimist in me, but.

**Chris Gammell:** And they're linked to all these other universities on the page.

**Dave Jones:** Oh, they do? Oh yeah. Yeah.

**Chris Gammell:** Look, down the right hand side there.

**Dave Jones:** Yeah. I know there's certain schools too. Like, I think UT Dallas. Yeah. UT Dallas has like a really good, um, switching program. I've talked to people about that. You know, they have a lot of, a lot of like switch mode power supply, uh, chip designers come out of there. Okay. And like the guy that wrote the textbook on it, it consults for TI a lot. He works there. So I'm sure a lot of these schools are very built in, like RIT, Rochester Institute of Technology. I grew up an hour away from there. They have a, they have a micro, um, a micro lab. They have their own fab on, on campus. And like, it's like not just a research lab. It's like, you can go, work on chips is like a job there, I think. Yep. And, uh, so it's like that. Okay.

**Chris Gammell:** Yeah. And they're tied in with these universities. And if you're in a course at one of these universities, then, um, you, your, your group gets 200 bucks worth of free modules or something for the TI store. And I, yeah, come on. Yeah. So it's recruiting, but still,

**Dave Jones:** if you are there or you are a student and you want to show up some, you know, some other people, that's, that's good. I mean, it's whatever. It's still money into the, into the contest space. That's fun.

**Chris Gammell:** Right. Well, yeah. Don't give them any more promotion, right? Yeah. All right. You've got a thing you want to talk about, about what is the tipping point or where is the tipping point when you want to revise a product that you've already got in production. I mean, have you worked on release kind of products before Dave? Yes, I have.

**Dave Jones:** So, I mean, when, when do you usually decide, eh, let's start, let's start looking at this again. I mean, is it mostly just when you're told to?

**Chris Gammell:** I usually don't get to decide it. Yeah. I was going to say, I usually don't either. It's usually a factor that forces your hand. Um, generally speaking, you know, your hand either has to be enforced in,

**Chris Gammell:** and you, a competitor's come out with a competing product that's better.

**Speaker ?:** Oh yeah,

**Chris Gammell:** that's one. And you know, you're losing market share for some reason. Um, that would be a trigger for, um, actually revising a product. Um, yeah, sometimes it would be, oh, we need to make, you know, a new management comes in. We need to make more profit margin or something like that. So we need to slash two cents off the price of this product.

**Dave Jones:** Remove all capacitors.

**Chris Gammell:** Yeah. Take off all the capacitors until it stops working and then put the last one back. The old Japanese method of, uh,

**Dave Jones:** yeah,

**Chris Gammell:** designing circuits. Yeah. Yeah. Um, and, uh, yeah, I, you know, I mean, there's lots of these triggers.

**Dave Jones:** There's another big one, right? I mean, that's a huge trigger if your vendor says you can't get any more. Anyways, the, the thing that I thought was interesting is like, is like when, when do you actually go back though? And it, without any of those other factors, or even if you do, even if, even if you have the cost savings one, right? Say you have a product, you're only selling a hundred of a year and you have an op amp on there. That's 50 bucks. It's like, Oh, that's ridiculous. That's a $50 op amp. Yeah. But then you think about it. And if you, if you do 50% better, you only save what? Two, $2,500 in a year. And if, if you're, if your change takes more than 25 hours, right? In terms of, yeah,

**Chris Gammell:** I know you've just blown out your, it's unbelievable.

**Dave Jones:** So yeah, it's like, I just thought that was really, I mean, that's the kind of stuff I deal with a lot.

**Chris Gammell:** For small volume stuff. Yeah, exactly. I mean, you know, for like a hundred thousand dollar, you know, if you, if you're making a hundred thousand of something, you know, you can afford to spend a hundred thousand dollars in either time and, or, you know, engineering or anything, right. Or cost in tooling to actually reduce the price of that product by $1.

**Dave Jones:** Right. And that's what like a manufacturing engineer is.

**Chris Gammell:** It's a manufacturing engineering, you know, optimization thing. Yeah.

**Dave Jones:** And like big, big companies have like whole departments devoted to that. And it's, it's interesting that they have that. I mean, I don't think it would be very, I mean, trying to squeeze that last penny out is, I mean, it could make a big difference, right. That could make, you're a,

**Chris Gammell:** you're a component optimization engineer or you're a production optimization engineer. Yeah. I mean, yeah, I mean,

**Dave Jones:** that's the other side of things too. If you make it faster, right. If you make, if you, if you somehow figure out how to make it 10% faster than you can make 10% more in a year. And,

**Chris Gammell:** or engineer it for lower battery consumption or something, you know, or,

**Dave Jones:** right. Yeah.

**Chris Gammell:** There's, there's no easy answer to that one. But as you said, it's a, it basically comes down to, you know, time and effort cost versus cost versus your return on that investment. So is it worth it? Well, sometimes you have to, like if you're losing market share, you don't, you know, if you're about to go out of business, you don't care. You're going to, how much you spend, you're going to fix that sucker. Right. So, yeah,

**Dave Jones:** it's, it's also interesting from the point of view, I think of, of the actual design side of things. You know, I know guys that design really low volume products and, you know, they have no problem throwing in a $300 FPGA, right? It's just like, well, exactly. It's nothing. It's, it's faster for me to use, use the reference design and pay the $300 and pay the $400 for that other

**Chris Gammell:** $2,000 FPGA. Not exactly. No question at all, you know,

**Dave Jones:** exactly. I mean, it's just, it's just something you do. And, and I think, I think coming out of school, I definitely was like, whoa, I can't believe people pay that. Right. But on the other hand, if, if you look at the actual economics of it, it makes a lot of sense. It makes no difference. And that's, and that's why, that's why the chip manufacturers price it like that too. That's, that's why when you look at those data sheets, you're like, holy crap, you know?

**Chris Gammell:** Well, I've worked in the military side of things where sometimes you'll make one of something, you know, a grand total of one. So, you know, it doesn't matter how much it costs. Really. There's no, you know, there's no optimization to be done there. It's, yeah. Oh, no, you know, cost always matters. You know, if you can, you know, you, you wouldn't use a thousand dollar chip if you could use a hundred dollar chip, but.

**Dave Jones:** Right.

**Chris Gammell:** In, in the scheme of things, it's not going to matter. You know, if it's takes the same amount of time to end, to actually implement both of those, of course you're going to use a cheaper one, but. Right. Yep. Time to market can be a, or time to finish your project can be a much bigger driving factor than cost.

**Dave Jones:** Unless you're working for the military. Then no one gives a crap.

**Chris Gammell:** No one cares. You're a year late. Congratulations. Hey, hey, we'll award you another contract. You're only a year late. Wow. Break out the trumpets and the dancing girls. Yeah.

**Dave Jones:** Yep. And that's why it's hard to imagine. Like, so there's a, there was another news story this week too, about, uh, about India and that $35 tablet. It's the other, it's the other side of things. I mean, they, so it's actually a $45 tablet, right? But then India is going to subsidize it for, I think, uh, $10 per and they're going to sell, they're buying so however many and, uh, resell them to, to like rural areas for education, whatever. Yeah. But man, $45 for a tablet. Can you, I mean,

**Chris Gammell:** well, they might not be making anything on that. They might even be making for a lot, making a loss because it might be a political thing. I've talked about this. Well, no, they, before. they,

**Dave Jones:** no, they said the $10 is the loss that the government's taking. So it's a $35 tablet, but $10 is from the government paying that. So it's actually a $45 tablet.

**Chris Gammell:** So you're saying that the company is not actually, who makes it isn't actually making any money. There's no profit margin in it.

**Dave Jones:** I don't know about that. I mean, yeah, that, that, that's a good question.

**Chris Gammell:** You know, it might be a government owned company or government sponsored company or something like that. Because this is a very big political, it's more politics than it is engineering. And, and market driven. These countries work different to, you know, the apples of the world and things like that. So. Oh yeah. You were driven by profit and all the rest of it. Right. Yeah. Yeah.

**Dave Jones:** It's a great idea for teaching, right? I mean, there is, it is, it comes from a good place, I think. I mean, but yeah, you're right. I think you're right. It is, it is politics.

**Chris Gammell:** Because this made the news about, it was probably a year ago or something. I think that they were working on it and they were talking about it. And, uh, all the commentary at the time said, well, they can't, they can't make it for that price because they don't have their own LCD manufacturing industry. They don't have their own chip manufacturing industry. They have to buy all these parts from China, like everyone else. And China can't make it for that price. So how are India going to make it for that price? It's, you know, I, yeah, it wouldn't surprise me if it costs more than that to make. And, uh, and they're just pushing it in some way.

**Dave Jones:** Yeah, they have, they're holding it up in the picture here, but yeah, there's, there's no delivery yet, right? There's, there's no tablet in the hands of a child in rural India. Right. When that happens, yeah, that's a different story, but, uh, it's a great idea. I think, uh, I hope they, I hope they, they come through with it, but yeah. Their goal was, $10. Yeah, I know. That's ridiculous.

**Chris Gammell:** 10 bucks was their goal to get a, a color screen, uh, tablet. Um, I, obviously it's touch as well. You know, it's a, yeah, yeah, but I, come on, you know, there's only certain chips and certain LCDs and certain other things you can use in these devices. They, you can't just magically create them yourself. As you said about the, as we talked about before with the foundries and everything else, you know, you can't just go magically, make your own chips for next to nothing. Right. I mean, it just doesn't happen. Um, right. As far as I know, India has no, oh, very little component manufacturing industry. Um, so they're,

**Dave Jones:** they're on the fabulous side, but I think that's it right now. Yeah.

**Chris Gammell:** I don't think there might be fabs there, but they're owned. They might be owned by, you know, companies like TI or somebody else. So, yeah, yeah. I don't know. But if you do know more about that, um, and the ins and outs of the technical, uh, the, you know, the financial details and how they can build it for that price, or if they really are, let us know.

**Dave Jones:** Yeah. Definitely.

**Chris Gammell:** In the comments. Cause so, yeah, I, yeah, there's a width of bullshit in the air. Yeah. I can, I can smell something, you know, it's just sort of floating around. It's very, you know, it isn't a big mound of turd. It's just, it's just a, a hint with them. It's a tiny pile in the corner. Yeah. Right. Okay. Yeah.

**Dave Jones:** Speaking of potential piles of turd, uh, we saw another story in the news this week about, uh, memristors, uh, and how those are going to be started being made. It's a little bit between HP and Hynex. HP is the one who actually came up with the technology. And obviously there was a guy in the seventies that,

**Chris Gammell:** I thought IBM were, had a lot of input on memristor stuff, or am I mistaken?

**Dave Jones:** They might've had it in the beginning, but HP is the one who actually built it. And that's the picture you always see with that, the 17 lines crossing another, like a ridge basically.

**Chris Gammell:** Oh, I've got these EA time pop-up ads again.

**Dave Jones:** Oh, it's,

**Chris Gammell:** it's Texas instruments. You bastards are paying money to get these full page pop-up ads. Piss off. Skip. Oh,

**Dave Jones:** bloody hell. I couldn't tell you a single ad I've ever seen on there.

**Chris Gammell:** No. Not a single one. There you go.

**Dave Jones:** Maybe it's supposed to be subliminal.

**Chris Gammell:** Don't buy TI parts folks. Cause they pay for these bloody annoying pop-up ads.

**Dave Jones:** We're never getting advertisers. We're just pissed off TI as a sponsor. No, it's not going to happen. Is it? Never, ever. No, well, anyways. Yeah. So they say by 2013, they're going to have this stuff. And, uh, yeah, it's, it's, we'll see. I mean, that's kind of what I keep thinking, right? Right. We'll see it when we see it, but man, Oh, that's crazy. And they're talking about, they're talking about moving from starting with flash, replacing flash, and then eventually replacing DRAM. Yeah. Yeah. And then eventually replacing SRAM.

**Chris Gammell:** Yeah. Yeah. Sure. Yeah. And I've got a bridge to sell you, you know?

**Dave Jones:** Right. Right. Yeah. Um, it'll be interesting to see how much they charge for it when it starts out. I mean, like I'm not paying more. I mean, like flash. Well,

**Chris Gammell:** apparently they can charge all they want. Cause they've amassed 500 patents around the mem, mem, Rista. This is HP.

**Dave Jones:** Yeah, they have, but they haven't amassed the patents around patents. Why did I say patents? They haven't amassed the patents around, around flash. And if, you know, unless it's cheaper than flash, no one gives a crap. So that's going to be the thing they, they argue against. I mean, it's, I mean, there's other benefits.

**Chris Gammell:** It could be power. It could be, yeah,

**Dave Jones:** it's supposed to have like infinite race cycles or rights. Right. But we'll see. Now, the interesting thing that I think, I don't know about you, Dave, is the fact that there's a whole other set of math here. Have you looked at the, the wiki page at all? No, I haven't. Yeah. There's a whole, I mean, so the new mem, Rister. Simule. It's no longer. Okay. It's, it's right next to the other one you clicked on. Oh,

**Chris Gammell:** is it? Oh, right. Oh yeah. There it is. Yeah. Yeah. So theory, there's,

**Dave Jones:** there's basically, you know, V equals IR. That's, that's your resistive linear relationship, right?

**Chris Gammell:** Yep.

**Dave Jones:** But now it's the, let's see, the, it's a resistance dependent on the amount of charge that is passed between the two terminals. And that, and that amounts to a memory because there's, there's a time-based component there. So now it's V equals I times M of Q, right? M of Q being the, Yep. The M of, the memristriness, sort of.

**Chris Gammell:** Memristriness. Yes. Yeah. There's actually a term for it. Yeah. Yeah. It, it actually relates. That's what M stands for. It's the memristr of the resistor.

**Dave Jones:** Oh, the memristence. That's it. Yeah. The mem, the memristence or something like that. Yeah. And, and it's dependent on, on charge Q. And it's like the crazy thing about that. I don't, I don't know if this will ever push into a, a discreet, you know, you know, if you'll ever be able to get like a liter resistor or even a SMT type resistor, right? Or if you even want that because then it'd be a single cell of memory. But I mean, I guess you could use it for like a flip flop or something like that. Right. I mean, if you could chart a store, store a state in there. Right. But, um,

**Chris Gammell:** well, that's the whole idea between them building chips with it, building, you know, and competing with flash and everything like that.

**Dave Jones:** yeah. But the thing is like, this is, this is a whole, this is a whole new set of math. This is like, this is like, uh, you know, keeping up on, this is like the incarnate example of why you should keep up on the industry. You know, like there is a whole, new set of math here that, you know, granted if it, if it's like in the feedback of a, you know, op amp or something like that, I don't think you'd use it for that. But you know, if, if you, this is a whole new set of math. Like I've never seen this math before, Dave. I'm just scared. I don't know.

**Chris Gammell:** There's squiggly lines in there.

**Dave Jones:** All these squiggly lines. I don't get it. And it's like, oh, it's, it's, it's not going to be that big a deal. I mean, but, but like, that's a big, that's cool. I mean, like that, that's never happened to me before. I mean, I feel like there's, there's been a, you know, if, if you grew up in the sixties and, and you know, like you, you came in, like you started to learn how to code and everything else like that. And, but like there, that kind of stuff hasn't really happened in my lifetime so far. I mean, like, or in my professional lifetime, you know, I haven't had to like learn some paradigm changing, uh, you know, set of math. Right. Or, you know, like, right. Yeah. If tomorrow there was a biological, you know, electrical element. Right. And I had to learn about that. Right. That kind of thing has never really happened before. It's been more iterative kind of stuff. Yeah. True. And so this is for real.

**Chris Gammell:** I can't think of anything.

**Dave Jones:** What? In the amount of time I've been,

**Chris Gammell:** in, in our lifetime. Oh, even yours too, huh? That is fundamentally. Well,

**Dave Jones:** cause you're old,

**Chris Gammell:** man. You're old. I'm an old bastard. Oh yeah. But offhand, maybe, maybe there is, but I can't remember. Yeah. Like at the hardware level, right? That's the main thing. Like a big quantum change, like not quantum change, quantum small, right? A, um, you know, a huge.

**Dave Jones:** Cosmic change.

**Chris Gammell:** Well, cosmic change.

**Dave Jones:** Yeah. Yes. Um,

**Chris Gammell:** yeah. I can't remember. If you can think of something that's happened, you know, in the last 25, 30 years, then please.

**Dave Jones:** Yeah. I mean, it's, it's no,

**Chris Gammell:** it's interesting.

**Dave Jones:** Maybe like more like, maybe like object oriented type stuff in your lifetime. I mean, that kind of like,

**Chris Gammell:** there's been software. Yeah. The software, who gives a shit about software? This is an electronic show. I don't care about software.

**Dave Jones:** It matters at some levels. Yeah. It matters in my household. Did I tell you, uh, my, my now wife is learning Python.

**Chris Gammell:** Oh, right. Yeah.

**Dave Jones:** Yeah. Very exciting. I'm going to turn her into a nerd yet.

**Chris Gammell:** She'll be joining us on the amp hour. Will she?

**Dave Jones:** Oh, I doubt that. No, no, she still thinks we're nerds. Don't worry. Yeah. Oh boy. But yeah, I, I can't think, I mean, software, software aside. I mean, I don't know. I mean, like even, even if you look at like amplifiers, like op amps go back along, they go back into the tube days. Right. And, uh, you know, silicon is a big deal, right? That was a big deal. Um, maybe like silicon carbide or like the more exotic kinds of stuff, but it's not mainstream yet. We're like, you or I would need to, we would even learn that in a university classroom. Right. There's not like an intro class. It's like, okay, now we're going to sit down and learn about, you know, the, the GAN or GAN or silicon carbide or anything like that. So, yeah, I don't know. So this could, I mean, it could be a big deal. I mean, if it's, if it's going to happen this year. Well, it's got its own component symbol. That's pretty cool. Right. Yeah. There's a t-shirt, Dave, get on it.

**Chris Gammell:** Right. Okay. Only those in the know of mem, memristas. Oh, I could put, put the math on there too.

**Dave Jones:** You could. Yeah. You need some kind of snarky phrase. Right. Yeah.

**Chris Gammell:** But when you don't even understand your own t-shirt, that's when you're fucking.

**Dave Jones:** What does your t-shirt mean? I have no idea.

**Chris Gammell:** I have no idea.

**Dave Jones:** It's some new technology. Yeah. Right. I, I got this from HP. I got to say.

**Chris Gammell:** Boy. All right. Yeah. Done. Our amp hours up. Do we have time for, um, a, uh, shonky product or something else or, uh,

**Dave Jones:** history maybe. Yeah. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** How about, uh, here's a nerd history thing that I actually found after, after I, I found a different nerd history thing. Um, there's actually a site dedicated to the history of transistors. Speaking of, right. So maybe we could look on here and, and figure it out. It's kind of a, uh, shonking looking, looking site itself, but, uh, you know,

**Chris Gammell:** it's just a very HTML. It's very, yeah. It's like, yep.

**Dave Jones:** But it's interesting because there's a lot of, uh, articles about the actual inventors of these one-off parts that I don't think you would have ever learned about otherwise, you know, like, or maybe I'm just more likely it's, it's just, I don't know who they are in the industry. They, they probably are, are very well known, right? Because they're probably got their names on papers and everything. But, uh, but yeah, it's, it's really interesting. I got linked here from, uh, someone had posted a link. I think it was on Reddit actually. Yeah.

**Chris Gammell:** I've been to this site before. Yeah. Oh yeah. It's actually a transistor museum. Oh, there's like a physical one? Semiconductormuseum.com.

**Dave Jones:** There's, there's like a physical museum somewhere?

**Chris Gammell:** Yeah. They've got, well, if you scroll down, there's the transistor museum donations. People have donated old transistors to this transistor museum. Huh.

**Dave Jones:** I mean, it could just be that the guy running the site in his basement though, to be honest. Oh yeah,

**Chris Gammell:** I've got, of course. Yeah. I mean, like that's different than like the computer history museum, right? Yeah. Not the scale of the computer history museum. Right. Right.

**Dave Jones:** Right. But still pretty, I mean, pretty cool. Yeah. I don't know if any of these parts are like radioactive or something.

**Chris Gammell:** They've got a triple five there. They've got a 1971 vintage donated by Hans himself.

**Dave Jones:** Right. And that's how I got to the site. There's actually, so there's another great thing about this is there's oral histories throughout this, right? So basically they call these guys up and they did oral histories with them. And it was interesting because me and Jerry had actually talked about doing something similar to this at one point. Yeah. So I've thought about it as well. Yeah. I mean, there's just a lot of guys retiring and stuff like that. And it's, you don't want to lose it. So it's great. It's, it's fun to look through and, and, and the audio quality is, you know, I'm kind of a snob, but, uh, right. It's, it's, I really suck at audio lately, but, uh, we're getting a little better.

**Chris Gammell:** So it's a Skype equality, is it? Yeah.

**Dave Jones:** Skype or like a tape deck, you know, even that kind of thing. Okay. So, um, but yeah, it's great. Uh, so I, I highly, I highly recommend people go there and check it out. And, and there's a lot of, and, and even companies don't, don't exist today. I mean, national union, they got, so I think they got swallowed up and a lot of different, uh, Texas instruments are still around, obviously. Uh, Raytheon is still around, but they're doing less hardware or do they do more military hardware?

**Chris Gammell:** They're all, they're all military. Yep.

**Dave Jones:** Yeah. So yeah, it's, it's, it's really cool. I think. So check it out. Awesome.

**Chris Gammell:** I'm going to throw in a shonky product of the week cause it's been on you forever. We'll just piss it off. Bump it up. Yeah. Yep. Okay. It is the winner this week is the Ampelizer.

**Dave Jones:** Ampelizer. Ampelizer.com. Ampelizer. Ampelizer.

**Chris Gammell:** There, um, it's a capacitor in a box folks. Uh, we'll save you the, uh, uh, anyway, watch the video. It's a very commercial sort of TV, almost like TV kind of thing.

**Dave Jones:** Yeah. It's got like a royalty free music in the background.

**Chris Gammell:** And it's just 15 bucks a month, folks. You can't buy this thing outright. They, they will lease you this box.

**Dave Jones:** Yeah.

**Chris Gammell:** And, uh, yeah. And of course, yeah, as you can guess, um, it's one of these power factor correction boxes and you stick it on your wall next to your power box and it's a big capacitor and it, uh, supposedly saves you money.

**Dave Jones:** And we should explain why, why that's supposed to save you money. Now, if this was actually, if you were actually had a high power factor, right? Is that the right, the right term? Low power factor, a low power factor, right? So yeah, you want, you want a power factor of one, you know, right? You want one. So if you start moving away from that, your apparent power is different than your, Oh, I needed to restudy my F E book. Uh,

**Chris Gammell:** anyways, you get charged more. Yeah. Well, not in Australia. We don't, I, I believe we don't get charged for apparent power. Only commercial companies get charged for apparent power. So,

**Dave Jones:** right. It's free. So you don't need this, but, uh, maybe it's all those pool owners in the U S that's who they, uh, they advertise to. Yeah. Oh boy. So expensive. Yeah. It's, uh, shonky to the max. I mean, a cap, a bank of capacitors could, could be good. If you had like huge inductive motors running in your facility, right? Yeah. And you were, and you were being charged for it, but more than likely paying $15 a month is just donating to a company that needs to pay for some better music. Much like us. I mean, if people want to give us money, we need better music.

**Chris Gammell:** They, they take what's real, you know, they take a real engineering concept and a real problem. And they think that they can apply that solution to, you know, something else and it doesn't actually work. So yes, you know, this apparent power thing is a real problem. Um, but generally it's only applicable to, uh, to big commercial companies with big installations. So, yep. And you can buy these ones that plug into a PowerPoint. Of course, this is a big, like, this is quite a big one. It's, you know, a big box you mount on your wall near your switchboard. Um, so this is actually, you know, so this might do a little bit, um, but you can actually buy these commercial ones, which just plug into your PowerPoint, you know, it's like, and they've got a tiny little capacitor in them. And, uh, oh boy, they're, they're magic things. Capacitors, aren't they? They can give you free energy. They can, uh, improve the energy fuel efficiency of your car. They can lower your energy bill. They can, uh,

**Dave Jones:** according to this video too, they can save me the kilowatts.

**Chris Gammell:** No pun intended. Sorry.

**Dave Jones:** The kilowatts, as they kept saying in there,

**Chris Gammell:** the kilowatts. Yeah.

**Dave Jones:** Yeah. You got to save the kilowatts.

**Chris Gammell:** Yeah. It's all about the kilowatts. And they've got some funky graphics of how the electricity flows down the line from your power. Yeah. Yeah. Yeah. Anyway. Yes. And they've had, apparently, um, they, I think might even be actively taking down people who have posted this video on YouTube. Um, cause we had a link that was before several weeks ago that was shut down. So.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. They might be clamping down. Watch out. I didn't even know if it's still available. Maybe they have gone bust, but anyway, it's funny.

**Dave Jones:** Yeah.

**Chris Gammell:** Hmm. Give it a big thumbs down folks. When you view the video. So that's all of our amp hour, huh, Dave? Yeah. It's all gone. But if we had a capacitor, we'd magically get extra capacity.

**Dave Jones:** We can get 10% extra capacity. Yeah.

**Chris Gammell:** Easy for just $14.95 a month. Who do we write out the check to?

**Dave Jones:** Chris Gammell. Right.

**Chris Gammell:** Oh boy.

**Dave Jones:** Yeah.

**Chris Gammell:** We're way over. See you next week.

**Dave Jones:** Yeah. See you next week. You can't connect the dots looking forward. You can only connect them looking back. Thanks, Steve.

**Speaker ?:** Thank you.
