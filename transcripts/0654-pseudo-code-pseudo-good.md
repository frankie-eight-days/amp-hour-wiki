---
episode: 654
title: Pseudo Code...Pseudo Good
url: https://theamphour.com/654-pseudo-code-pseudo-good/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released December 18th, 2023. Episode 654. Pseudo code, pseudo good.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell, contextual electronics.

**Dave Jones:** Almost that time of the year again. CES. CES, that's it. Yep. Totally. Consumer electronics is what we're about here on the Amp Hour.

**Chris Gammell:** That's right. Which is usually what happens when I tell people that I have a podcast about electronics. They're like, oh, yeah, yeah. So like, you review phones?

**Dave Jones:** Phones, yeah, yeah, exactly.

**Chris Gammell:** No, you wouldn't want to know what phone I use. It's lame. Yeah, CES is coming. It's interesting with CES, too, because it's like CES is like this de facto. There's not many trade shows left in the U.S. You have the same problem in Australia. Yep. And it's just like, even though it is the consumer electronics show, it also becomes this de facto place to meet. And so I get asked by vendors all the time, like, oh, we're going to be at CES. You're there. And so it just becomes a place to go to, even if you're not a consumer person.

**Dave Jones:** I think that's the entire reason that they actually still go, that they still have them. Yeah, yeah. Right. Yep. Because everyone just gets to hang out every year, you know.

**Chris Gammell:** Yeah. And get COVID or flu or whatever, the RSV, all the local, yeah, the latest virus. I pretty much go to that. I've been twice, I think, and both times I got a real sick. No, really? It's Vegas, so I hate Vegas. All right. Yeah, just no fun. No fun at all.

**Dave Jones:** Don't want to know what you're getting up to, but okay. What happens in Vegas stays in Vegas, yeah? It doesn't. It actually comes home on the plane with you in that case, yeah.

**Chris Gammell:** In your lungs, yeah. Oh, boy. Yeah. And there are some good spots. I mean, there's like a startup-y area that's not terrible. And there's like some vendor areas too, but you have to walk through the super glitz of Intel's booth, which is like five stories tall, and they don't show anything there. Really? I mean, they do. They're like showing like, well, then they have like their latest silicon under glass, which is fine. Like, that doesn't really show me anything. And then it's like, here's some products this goes in, but it's, you know, for the size of the booth, it's insane. Like, the booth size to like relevant stuff ratio is very, very low. Very, very high, I suppose.

**Dave Jones:** There'll be one chip under a tiny bit of glass, and that's like the entire, yeah, right.

**Chris Gammell:** But they have to like basically be there as a presence. And this isn't just, I'm picking Intel, but it's Samsung and all the big companies too. And it's just like, there's just not a lot to see. Like, I want to go to a trade show and like see demos and see cool stuff. And this is like, come check out this car that has one of our chips in it. It's like, yeah, that's cool. Or maybe they have a, you know, these days it's almost certainly going to be like a machine vision or AI BS. So fine, whatever.

**Dave Jones:** One of the things I love is that you go to those shows and sometimes, like not always, this is what they should be doing. This is what Intel should be doing is they should have, you know, one of the layout or architecture guys there or something, you know, and you can go like, who do I talk to about the latest?

**Chris Gammell:** It's like a, you know, it's like a dunk tank. Yeah, right.

**Dave Jones:** And it's like, they should wear a shirt.

**Chris Gammell:** Like, oh, I designed this or something. You know, like, yeah.

**Dave Jones:** Ask me about routing. Ask me about chip routing, you know.

**Chris Gammell:** It's not about the engineers, Dave. You know that. I know that. Come on.

**Dave Jones:** Yeah, but that's what I want. That's what I want. Well, maybe not at CES, but I'd expect that at, you know, some other show.

**Chris Gammell:** And better worlds are better about that sort of thing. Yeah, yeah. That's happening. I have to whine a little bit. So trade show season is, you know, rounding up on us in 2024. I swear to God, every trade show that I go to is happening in April this year to the point where it's like, I'm going to skip some. Yeah. So I'm not sure how it all happened. But like back to back, like one. So like Embedded World is in Germany. Yeah. Like the second week of April. And then the next week, Embedded Open Source Summit, which is like many of the same people, not like all.

**Dave Jones:** Right. Yeah, of course.

**Chris Gammell:** But like, you know, Embedded is in the name of both. Of course. And it's in Seattle. So it's halfway across the world. Yeah. And it's like the next week. And so it's like you're home for a day. And it's like, oh God. So we'll see which one of those I go to.

**Dave Jones:** And you'll be going to all of them because that's your job really, isn't it? So.

**Chris Gammell:** Maybe. I don't know. Yeah, we'll see. You know. As is now known, I have a baby at home. So, you know. No, no.

**Dave Jones:** Well, I don't think they care about that. That's true. They don't. Yeah. No. No. Yeah. Yeah. Oh boy.

**Chris Gammell:** Well, so I will keep an eye out for me on one of those two, at least. Right. Yeah.

**Dave Jones:** Got it. All right. Well, enough of that consumer electronics rubbish. Don't talk about that. Yeah. Yeah. Yeah. What else we got? What we can talk about is engineering. I love.

**Chris Gammell:** Whoa.

**Dave Jones:** Whoa. Whoa. That's extreme. Calling out bad engineering.

**Chris Gammell:** Oh, where are you going with this?

**Dave Jones:** Where am I going with this? I'm going smarter every day. Have you seen.

**Chris Gammell:** Destin?

**Dave Jones:** Have you seen his latest video?

**Chris Gammell:** The NASA one?

**Dave Jones:** Yeah.

**Chris Gammell:** I didn't watch it. No. Okay. He said NASA was wrong or something like that. I just thought. Well, yeah.

**Dave Jones:** I've got a summary. I will now paste you the summary on my Twitter. See, you don't watch Twitter. You don't do Twitter anymore. So there you go. I've got a summary of his video. Not in order. But basically, we'll definitely link it in down below. You have to watch it. And it was like, what's it titled? The video. I was scared to say this to NASA. But I said it anyway. Basically, he was invited to this, like, really important, conference where all the movers and shakers in the space industry are there. Like, you know, like the who's who. And he got invited to give a presentation at this. And he went, oh, here's my chance. Here's my, should I do it? Should I do it? Whereas he doesn't, basically, he doesn't think that the new space launch system, the, um, the Artemis, uh, program is doing the right thing. He thinks they're making a bunch of fundamental mistakes. And he very politely in his very polite way called him out on it. Like, and they're in the audience and they're sitting in the audience and he's like.

**Chris Gammell:** Yeah. Speaking truth to power. Huh? Oh, wow. Yeah.

**Dave Jones:** And he's, he's, he's, one of his main points was that basically during the. Uh, polo program, like they went to like, you know, they landed on the moon. They, they, they had six out six for zero. Right. So they, they're six out of six missions landed on the moon. Right. Well, Apollo 13 didn't make it, but they made it back. Right. Anyway, because they had a fault, but all the landings that they actually attempted, they. Yeah. A hundred percent success rate. And then, uh, they, they wrote this document, what made Apollo a success. And it's a technical blueprint of how they succeeded in this. And he's basically saying, you guys have not read this, have you? And it's like, oh, burn like because they're making, he thinks they're making all these fundamental. Mistakes and all these choices are not driven by engineering. This is what he's getting down to. The choices that they're making are not driven by the engineering constraints of the mission. They're driven by the politics of the mission. And he thinks that they're des absolutely des, well, destined, get it. They're destined. Yeah. I get it. Yeah. I'm here all week. Destin. Um, Destin. They're dead. He didn't say that, but he's like, he's warning them. He's worried. He's worried. He is worried for the safety of the crew. Yes. He's, he's genuinely worried.

**Chris Gammell:** I mean, we're all cheering for this, right? Oh yeah. No, we totally want it. I want people to go back to the moon. Like, that's awesome.

**Dave Jones:** Right. I'm, yeah. I'm totally rooting for it. Right.

**Chris Gammell:** Let alone like, like averting disaster. Yeah. Yeah.

**Dave Jones:** But, um, but, but then he said, um, basically Neil Armstrong and also the designer of the, you know how, um, he famously aborted from that, uh, lunar lander training vehicle thing. Right. They, they actually developed this lunar lander, you know, this spidery looking lunar lander thing to actually simulate landing in one six, uh, gravity. And he basically, um, you know, showed a video of where, uh, or, uh, linked to it that, um, where Neil Armstrong himself is saying, you are not going back to the moon unless you've trained on something like this. You are going to goof it up. It, cause it is like, and they're not doing it and they're not doing it. And, and then he interviewed the guy who actually, actually designed that lunar lander, the engineer who designed it. Yeah. I remember that. That was a while ago. Yeah. And he, yeah, he did a video interviewing him. That's, that's quite good. And he's saying the same thing. Like, you're not going to get back to the moon unless you build this trainer thing to train the astronauts. They're, they're not going to be able to do it. They're going to be hit with all these different sensations and they're just not going to, they're just going to come a gutter. Yeah.

**Chris Gammell:** Um, and it does make you wonder, like, you know, like, uh, I think in almost all assumptions for like, let's say sci-fi so that I don't get myself in trouble, but like all these sci-fi sci-fi futures, right? Near, near term futures. There's always like automation, but then like, I feel like the story points are always like, well, something's going to go wrong at some point. And then a human has to take over and then it becomes like a story of ingenuity and whatever. Exactly. And I think that kind of like, kind of plays into this too of like, well, if you're, if you have like muscle memory, like there are going to be some things that humans just can't do reaction times, whatever. But I think the, the reactivity of like two different scenarios and having different, um, different plans as well. Yeah, totally.

**Dave Jones:** Yeah, totally. And he, he actually goes to length on that in the video as well. He's talking about just the, uh, just the, uh, just escaping from the moon, right? Just the, the original Apollo lander had, I think five, is it in my notes here? Five or six different backup systems. Right. It's like, yeah, six, is it? Okay. Six different. Yeah. Yeah. I've got it here six different backup methods to launch if things failed and all of the Apollo astronauts have said this it's like, yeah, we had backups upon backups and upon backups. And apparently, um, they're not even using hypergolic fuels like they did on Apollo. What that means is you just slam the two fuels together and basic, uh, basic chemistry says they're going to explode and you're going to launch. Right. And they're not doing that. They're having all these pump systems and all the, I don't know what fuels they're using, but they're like, they're adding complexity. They're adding all these layers of complexity and not having nearly as many backup methods. Like, and, uh, yeah, it's, um, it's not good. Yeah. It's a little scary. That's all scary. And he says the near recto linear halo orbit, which, uh, is being used by the new, uh, Artemis mission, uh, which is basically a big ellipse, which takes them away from the moon. You know, it takes them like in close and then days like way away and stuff like that. And they've chosen, they reckon they've chosen this, uh, orbit, this, this particular orbit for comms reasons. And he's saying, yeah, nah, that's basically bullshit. They're choosing it for other political reasons. And they basically, they don't have, and that reduces the number of backups. It means he's something goes wrong when they're on the moon. Yeah. They're, they're stranded for two days until they can get back to match up and like all sorts of things can go wrong. And I hope it doesn't, but geez, you know, anyway, it was very brave of him. Yeah. That's good. Yeah. I'll have to watch that. Get up in front of, yeah. Yeah. And he, you know.

**Chris Gammell:** It's kind of interesting, like, of like, uh, how paranoid should you be? But it does seem like that would be.

**Dave Jones:** Well, you go into the moon. You got, I think you've got to be super paranoid. Right, right, right. And that, and that's why Apollo made six out of six landings. They stuck six out of six landings is because they were super paranoid and backups upon backups. And that's how, that's how Apollo 13 was saved and you know, all sorts of things. Cause they had so many options. Um, whereas this one, Artemis, it sounds like it's, yeah, no, it's like any, and he asked them, have you read this like guide written by the Apollo people, which is like how we succeeded. And like, no, no hands went up. Like nobody's actually read it. And apparently it's the blueprint for how you succeed landing on the moon. And it's like,

**Chris Gammell:** RTFM. Yeah.

**Dave Jones:** RTFM. Yeah. Yeah. Yeah.

**Dave Jones:** So anyway, I, you know, that was, that was pretty gutsy to do that. And I, I think it was, I think it was valuable. I think it was valuable because it, you know, if you do it, like you should be doing things for engineering reasons. You should be all of the, all the fundamental choices should be for engineering reasons, should not be for politics. So, yeah. Anyway, this is not the space YouTube channel, but yeah. Yeah. You'll have to, it's that long, unfortunately. So you can't like, it's over an hour long. So, you know,

**Chris Gammell:** I got a holiday coming up. I have a little time.

**Dave Jones:** Well, although, although I've got to say, you could probably skip the first 30 minutes. Cause he goes into like all these background and stuff like that. So you could probably skip to various points.

**Chris Gammell:** I just watch it three X speed, Dave. Yeah. Yeah. Yeah. Cool. Yeah. Yeah. Three.

**Dave Jones:** 20 minute video.

**Chris Gammell:** Three. Yeah. Yeah. What's your fastest you go? Three. I can do three.

**Dave Jones:** Two is probably the fastest.

**Chris Gammell:** Depends.

**Dave Jones:** I have got, it totally depends on the person. Yeah. Yeah.

**Dave Jones:** Like a really slow talk. I went two. Right.

**Chris Gammell:** Yeah. A really slow talk. Oh yeah. Yeah. Like a really slow talk. How about this? I can listen to Dave at least two. Right. I've gotten to like some of the late night shows that I watch. Yeah. I watch like their clips and stuff like that. Right. I can do this. I can do this three X. No problem.

**Dave Jones:** Really? Three X. Okay. Maybe.

**Chris Gammell:** And like you normalize to it. You really, I think the one of the things is you have to ramp your way up.

**Dave Jones:** Yeah.

**Chris Gammell:** But it's, it's amazing how your brain just. Oh yeah. I know. I'm sure people are listening to us right now. Yep. And it's. They've only got a half hour gym workout. Probably. Really slow. Yeah. Yeah. I mean, I listen to podcasts at least two X. I mean, I just. I can.

**Dave Jones:** Yep. Yeah. Well, my, I set mine as 1.5 is like pretty much. Unless I've got a, like a really fast talker and then I'm going, okay, I can set that, but down to 1.25 or something.

**Chris Gammell:** Yeah. Yeah. Yeah. So my, I mean, my wife and I talk about this. She really loves the armchair expert, which is a celebrity podcast sort of. I mean, Dak Shepherd is like, you know, he's an actor and he's got a podcast. No idea. But like, if you listen to him at one X speed, he sounds dumb. Oh, right. Okay. Yeah. He's not a dumb person. Got it. But he sounds dumb.

**Dave Jones:** He's just one of those slow, methodical talker.

**Chris Gammell:** No, it's not even that. It's just, I think it's honestly, it's just me. It's my brain. I've normalized to it. It might people who are probably like, yeah. I just think that it sounds, he sounds way. It's a different, it's a different podcast when you just listen to it slow.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Although I do.

**Chris Gammell:** There's someone out there nodding their head right now. They're like, yeah, Chris sounds really stupid at one X.

**Dave Jones:** Although I, if it's something important and I know I've got the time to do it, I do set it back to one. Because I find that I can like, especially if I'm doing something, you know, I'm outside, I'm working, I'm doing a task or something. I'll set it on one. I don't want that to be at one and a half. I sort of, you know, want to slow it back down to sort of, you know, just to let it sort of, you know, give my brain more time to process kind of thing. But yeah. Yep. I totally get it though.

**Chris Gammell:** I'm listening to a, I'm currently halfway through a book called Shogun. And it's about a narrative, like Japanese history. I don't know. Yeah. I guess, I don't know. I don't know anything about it other than like my friend recommended it. Okay. And it's great. And it's a 40 hour book. Right. If I don't go faster. It's like, wow. Yeah. That's, that's a lot of, that's a lot of commitment. Yeah. Yeah.

**Dave Jones:** Exactly. Yeah. Oh boy. Anyway. Yeah. Focus on engineering people. But unfortunately, you know, you've worked at, I'm sure you've worked at companies that have, you know, been not in, not necessarily engineering focused. So yeah.

**Chris Gammell:** There's the human element sneaks its way in and everything. Right. I mean, that's, that's how it goes. Yeah. Organizational problems.

**Speaker ?:** Hang on.

**Dave Jones:** The original post was deleted. The original post. Somebody deleted the post on Twitter. Was that Destin? I don't know. He hasn't, hasn't deleted it. Has he?

**Chris Gammell:** Maybe NASA got to him. Yeah.

**Dave Jones:** They got him. They got him. Lizard people. Lizard people got him. No, no. It's still there. It's still there. So anyway. Highly, highly recommended. It's good. Yeah. And, and, and you can just sense the, you know, like the little hint of snark in that, like, like you guys are wrong. And like, yeah, you know, you're going to come a gutter and please don't kill the astronauts. Like, and he, and he does it for genuine reasons though. Like he genuinely cares, you know? And yeah, that's good. It's all good. Anyway.

**Chris Gammell:** Speaking of committing to things, I am committing to a new board rev on two boards before the end of the year. And, um, uh, you do realize it's the 18th running out of time. I know really it's just paying, paying the invoice before the end of the year and I'm going to get it made before the end of the year, but yeah, that's the, I don't know. We used to do that.

**Dave Jones:** I can remember making stuff just before Christmas and yep.

**Chris Gammell:** Yeah. What was the closest you shaved it? Board back?

**Dave Jones:** Well, we spun it in 24. We spun the board in 24 hours.

**Chris Gammell:** Yeah.

**Dave Jones:** Spun an eight layer board in 24 hours. It cost us, I don't know, two, $3,000 or something. Yeah. Yeah. Yeah. We spun the board in 24 hours. They just bump everyone else. They just like, if you pay enough money, they will bump all their other customers.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah, exactly. Although have an emergency, you know, there are companies that have like a dedicated line that they keep open for these emergency jobs. And, and, and they say they're bumping customers, but they're not actually, they're just spinning up their emergency line, you know? So, yep. Bet they'll charge you. I'm going to leg for it. But it's certainly possible. It is certainly possible. You can do it. Yep. Hmm. No, I can remember having to finish an entire, like we, we started a design on the 15th or something of, of December. And the trade show was like January 15th. So like we had to, yeah.

**Chris Gammell:** So like, at this point we're also like getting ahead of like new year's, Chinese new year's too. Right. So that's another thing that like a lot of people are planning around.

**Dave Jones:** So ordinarily like a month. Oh yeah. That sounds like a, you know, you can get stuff done in a month, but when it's over Christmas and new year's. Yeah, exactly. You know, like people disappear. Yeah. Yeah. And companies just vanish. Yeah. Yeah. Oh boy. Yes.

**Chris Gammell:** It is tougher and tougher to do those sorts of things.

**Dave Jones:** Yep. Ah, fun days, fun times.

**Chris Gammell:** Yeah. Trying to think there, there were some, like, there was one. Problem that came up that I thought was kind of interesting for here. Whereas like, it was one of those scenarios where like me and a coworker were like working through like all of these different options. It could be. And it just like, at the end of the day, it was just like, oh, well, we could just like not do what the problem is. I, it was, I'm trying to find the, the ticket that I filed for this sort of thing where it was really a silly problem. Uh, what was the end thing? Wasn't that one? Hmm. Nope. I'll find it. I'll find it here. I'll find it. But you know, like sometimes you just have like these, these issues where like you think, you know, you, you've set these constraints almost upon yourself, right? For like a board design. Right. Yeah. Oh, that's what it was. It was, uh, um, so I have an auxiliary modem attached to a microcontroller I'm using. Right. So I'm using an NRP 91 60. Yep. And then it's talking to an ESP 32 C3. Right. So that's a ESP wifi module in AT mode. And so.

**Dave Jones:** As in Hayes ATC, that's where my mind goes. When you say the word. Exactly.

**Chris Gammell:** Modem. No, it's exactly. Dave, that's exactly what it is. That's what's crazy. It's still a thing. I know. AT modems are still a thing. It's like, how are we still here?

**Dave Jones:** Hayes AT command set. You know, it's like. That's exactly right. Yes. Used to know that off by heart. Yeah. You know. Yeah. And it's, yeah. Yeah. Yeah. 300 board modem, you know. Yeah. 300 bits per second.

**Chris Gammell:** I'm shoving so much stuff into this design that it's just like, I'm out of iOS. Right. So then it starts to get into like, oh, well, you know, we could do a GPO expander. Yeah. Yeah. And all of these different problems and like all of these different things came up there. And so it, it also came down to the point where like, we, one of the other restrictions on the 9160 is that there's only four, you know, like all of these chipsets these days have these flexible peripheral sets. So, you know, you can have like, it could be a spy controller or it can be an I squared C controller or it can be a UART controller. Right. Right. So you could have up to four UARTs, but if you have four UARTs, that means you can't have any I squared C or any spy.

**Dave Jones:** Right.

**Chris Gammell:** So it's like, basically you choose which four you want to use because it's using, I think the same address space is one of the problems there.

**Dave Jones:** Oh, okay. Yeah. Cause I was going to ask about the physical, like, is it a, is an internal like routing thing or is it a, like, you know, with the peripheral routing, like, and they're in the same block, but then they use the same outputs in pins to the internal matrix. If you sort of know what I'm talking about. Right. Exactly. Yeah. Like the flexible fabric. Yeah. And then it gets routed to the pins you want and stuff like that. So that, yeah. Yeah. That's where my mind.

**Chris Gammell:** I'm not sure because it's like, they all have their own, they all have their own like addressable thing, but the real restriction is that it's like, um, you can have, you are zero one, two, three, or you can have spies or one, two, three, I squared C one, two, three, but you can't use the same base number more than once. And the other weird thing about it is like, and this is on the 9160 specifically, which is their cell modem. It's different than it is on their Bluetooth stuff. So it's like, okay, well, whatever. But like that, that's, that's like a weird thing. Yeah. That's probably just one of the, like those, some constraint they had on the silicon. Okay, fine. Whatever. And this is, so now it's just this thing you have to deal with. And thank goodness my coworker found these. Cause I would have just like happily been like, oh, look, we can have four of each. Yeah. Yep. And then, and then that's the one where you like, you know, you, you get, it's like, oh, nothing's working here. It's like, yeah, well you completely shoved way too much stuff onto this chip, Chris. Yeah. That's how I operate. Um, and so, yeah. And so I think the real thing in this case was like, we were running out of GPIO and we were also running out of UARTs to talk to the AT modem over UART. Right. And it's like, oh, well we could do, we could switch it into spy mode, but, but then there's no Zephyr driver for spy mode to talk to the ESP 32 AT modem. Fine. I guess we could write that, but that's like.

**Dave Jones:** Yeah. It's just another process.

**Chris Gammell:** Days, weeks, months, who knows. Right. I don't think it's worth it. And so the end, the end result was just like, oh, well the assumption that we had to use some of the pins from the board we were borrowing from is the real, that was ended up being like the assumption that I had not thought of. And so there's like a spy flash on board, but we're doing other spy stuff and it's just like, oh, well don't double up on your spy, spy buses. Just use the, the nature of a spy bus and add another CS pin. Yeah. Chips like pin. And, and now I freed up a bunch of IOs. I freed up a bunch of, um, yeah. Freed up another UART to talk to this thing. So yeah, that was, that was like a really clutch. That was my, my coworker Chris who figured that out. So that was super clutch. And, uh, yeah, that's going to make things a lot easier, which is really nice.

**Dave Jones:** Check, double check, triple check your capabilities of your devices. Don't just look at the top level banner spec. Oh, it's got four UARTs. Yeah. Great. And then you realize you can't use them all at the same time because they share. Yeah.

**Chris Gammell:** I mean, you either read it up front or you read it when you're on the bench at two in the morning, right? Those are your two choices.

**Dave Jones:** You know, it was like, Oh, after you've already bought your, uh, prototype board and you're two ways and you're two days away from the trade show. And yeah, yeah, yeah, yeah.

**Chris Gammell:** Well, uh, I, I am also cleaning up all of the memes that I put into this, uh, schematic and, uh, other stupid comments because I'm also going to be open sourcing it. And so I was like, Oh no, this isn't fit for consumption. Although I am keeping in the, uh, the top level image for the, uh, the sheet with all the power parts.

**Dave Jones:** I have, uh, Palpatine, you know, shooting lightning out of his fingers and ultimate power. Do it.

**Chris Gammell:** I'm keeping, I'm keeping that one in there, Dave. Right. Yes. That's good. Yeah. Yeah. It's good. Cool. Yeah. Yeah. Yeah. It's tough. You know, like reading data sheets is like, it is its own fine art, but it's even, I don't know. There's just so much, so many demons buried in those things, you know?

**Dave Jones:** Yeah. And they're not going to tell you at the top, are they? They're just not that courteous. Why are them? You know?

**Chris Gammell:** Well, yeah, they're not, I think that's the thing though. Like, I think one thing to remember about data sheets is they're written for, they're written as a contract of agreement between the company making it and the capabilities that are broadcast to their users. And so it's like, there's no real like requirement on ease of use. It's just about, no, it's all in there. And then it's up to you, the engineer to go and fill that out. And a lot of the, you know, I've talked to people who are like, oh yeah, I'm going to make a new, a new type of data sheet and like change the industry. It's like, no, you're not going to change that because there's just so much history and like, and just crap that's like layered in there. You know, it's just, yeah, it's just the way you've always done it. You know? Like, okay. Yeah.

**Dave Jones:** Yeah. But then like, yeah, people expect it to be in that form. If you try to do it, you know, differently, people would be going, what is this bullshit?

**Chris Gammell:** That's true. That's true. Yeah. Yeah. Yeah. Who moved, who moved, who moved the button? Yeah. That's the other problem. Exactly. Yeah.

**Dave Jones:** Engineers are creatures of habit. We are. We like using our favorite chip again and again, because we trust it. We like using our favorite manufacturer again and again. We trust us, our favorite supplier again and again, because we trust them, et cetera, et cetera. Yeah. And yep. Anyway. Speaking of chips.

**Chris Gammell:** Cheap as. I saw, I heard someone refer to cheapest chips on like NPR the other day. And I was like, oh, I know someone who says that. Cheap as chips. Go ahead. Yeah. That is not my one. Oh, that's what it was. It was about the dying fish and chip industry because of inflation costs in the UK, because that's a podcast you listen to. Okay. Yeah. And cheapest chips was the term. And I was like, oh, Dave says that.

**Dave Jones:** You don't actually think that's my term, do you?

**Chris Gammell:** No. No. I said, Dave says that. Not Dave came up with that.

**Dave Jones:** Okay. Right. Got it. Yeah. Cheap as chips. Yeah. That probably came from the UK. You know? Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. Yeah. As all. I mean, that's Australia is just discount UK, right? Right. Of course. No worries.

**Dave Jones:** Anyway. Okay.

**Chris Gammell:** Sorry. Chips. Real chips. Sorry. Real chips.

**Dave Jones:** This one is definitely not cheap, but I'd love to know the bomb cost. Actually, I put this on the forum. I'd love to know the unit cost. Siglent have a new oscilloscope. It's the SDS-7000A and it's like high end, like really high end. It's what is it? Is it eight gig or something? Right. And it's a 12 bit and it's eight bit at 12. Hang on. SDS-7000A Siglent. I better actually get the top level things. It's a four gig bandwidth, 12 bit ADC, right? So, you know, so it's getting up there, right? It's a 20 gig samples per second, right? Really high end big boy stuff. Right. And the thing is they developed a custom front end ASIC for it, which is an eight gig. Front end amplifier chip. And all the manufacturers that do this, Rygol have their new front end amplifier chip and it's used in everything from their four, four or 5,000 series right down to now the. 800 series for three, 300 bucks. Right. And they use the same front end chip.

**Chris Gammell:** They just cripple it.

**Dave Jones:** Yeah. They just, yeah. Because it's an eight hundred, that, that Rygol one is an 800 megahertz complete front end in a single chip.

**Chris Gammell:** Yeah.

**Dave Jones:** Like when I was a boy, right? A front end was a difficult thing to design at 20 megahertz. Right. And then, oh, you got a 50 megahertz one. Whoa. It's still as difficult, Dave. Yeah, right. It's still as difficult. Except that's all in a single chip now. Right. Yeah. Yeah. So all you need is a couple of relays on the front end, decoupling caps and, you know, Bob's your uncle. Right. It's got programmable gain amps in there. It's got all, you know, it's got all the good stuff. And, and yeah. So that's an 800 megahertz front end. So if you go and buy the a hundred megahertz scope, it's actually got an 800 megahertz front end bandwidth chip, capable chip in there. And it's exactly the same PCB layout. I've actually compared the layouts between the high end model with the 800 megahertz bandwidth and the a hundred megahertz model. And they're exactly the same. Right. So it's, yeah, it's a big, because the cheap is so cheap. The cheap is cheap as chips.

**Chris Gammell:** God.

**Dave Jones:** Because they designed it for, you know, once you design, that's the whole reason that you design NASIC. So that in volume, they're super cheap. Right. But, but this eight gig one, yeah, that's really high. That's like eight gig bandwidth, 12 bit dynamic range capable, you know, in, in entire front end. So that's a very impressive chip. So I'd love to know what the, for those who are into your process geometries and your chip manufacturer and everything, what would be the, the cost difference on an eight gig, uh, capable process, RFR process compared to an 800 megahertz capable process. I'd love to know what their unit cost is on those chips. Of course, they're not going to tell us. We can only ballpark estimate, I guess, but basically what I'm saying.

**Chris Gammell:** How do you know they're the different, how do you know they're the different, they're the, sorry. It's this, it is the same like markings on the chips as well.

**Dave Jones:** Oh yes. It's exactly the same markings on the Rigol one. Yes. I, I don't know. I don't, um, Siglent have released a new competitor to the Rigol 800, 900 series. That's just, just come out. I don't know the cost, but it's really cheap. It's like 400 bucks or something, 500 bucks. Um, I, I'm doubting that it uses this eight gigahertz bandwidth front end chip. I'm just, I, I just think that the unit cost is going to be way higher on this chip, but I could be wrong. I could be wrong. We, we could, in theory, start seeing bottom of the range scopes with an eight gig capable bandwidth front end in theory. Um, but you know, then, then you need pretty exotic PCB routing at eight gig. You know, you need exotic, you know, you need controlled impedance materials and, you know, stuff like that, you know, you start needing the fancy pantsy stuff. Uh, when you're talking about that, but which you don't need for the, for the Rigol 800 megahertz one, like you can do that standard FR4, just, you know, just your regular, you know, stuff. You can get your 800 meg on that. So you just control your routing, make it a bit tight and Bob's your uncle. All right. But anyway, I'd love to know the cost. And, um.

**Chris Gammell:** That's, that's, that's very far outside my peer range, Dave.

**Dave Jones:** I think it's, it's outside most engineers, um, pay range really. Capabilities. Yeah. Yeah. Totally. Wow. And it's low noise. It's 1.9. 10 volts per root Hertz. Like, you know, over the eight gig bandwidth, you know, for eight gig.

**Chris Gammell:** I would say root Hertz though at eight gig is quite a bit. Anyway. Yeah, exactly.

**Dave Jones:** That's why you've got to keep it low, you know? Yeah, that's true. That's true. Um, but yeah, no, it's, um, very impressive that, um, these, um, lower end, you know, you, you think of these as like third tier make, you know, Siglett and Rigol used to be like, who are they? You know? Yeah.

**Chris Gammell:** I feel like it's all, uh, innovative dilemma type stuff where that's like true, like bottom up kind of like, they started with the low, super, super low end. Yep. They built from brand value. They've moved their way up. They've funded their, they funded their own development sort of thing. And then, yep. Now they're playing in the same arena. Yeah. Yeah. Starting, starting to, starting to eat away at, at the, the big boys.

**Dave Jones:** Yeah. The, uh, big boys. And, um, yeah, there's talk on the EV blog forum about how dare Siglett release a scope of this bandwidth for this sort of price. That's just, that's, that's not on. That's always a part of it too. That's not on. You know, this is supposed to be a protected market. Don't you know about our carrying costs? Yeah. Right. Right. I know it's Siglett, Rigol, you know, um, Siglett and tech and, and, uh, Croy the road going, come on.

**Chris Gammell:** Well, the other crazy thing about that. So like, I always liken it to the auto industry too. And like, you know, and then what's going to happen too, is they're going to take some big swings. Like you see this in the auto industry too, where you're like some of the up and coming brands, they started with cheap, crappy cars and they've worked their way up in quality and reliability and all that other stuff too. And then they're like, you know what? We, we need to still stand out and we're willing to do it because we're, we're the new kid on the block. Yeah. And they take some big swings. It's like, Oh wow. Where did, where did that come from?

**Dave Jones:** I'm surprised it's been, you know, I mean, who's Polestar, you know? And they, they come out with this EV like, I've never heard of them. Like, geez, you know, and they just pop out of, you know, Aptera, you know, with their little light, all these companies just pop out of nowhere, you know, with their new cars. And it's like, Hmm, geez, you know, that's just something that we, you know, we, we spent so long, so many decades, you know, 50 years of all the same automakers really. And then all of a sudden.

**Chris Gammell:** Although they're different in the, in Aussie land than they are here. I'm like, I'm always confused when you're talking about brands and I'm like, who? And you're like, Oh, it's Ford. Right. Yeah. Yeah. Yeah. Right. Right. The Kings, but you're right. I mean, they, they, they haven't changed much. Right. I mean, right. Yeah. The market. Yes.

**Dave Jones:** Yeah. Yes. And, um, uh, there was a video which I saw pop up on my timeline, but I haven't, I didn't click on it, but the video title was why it's illegal for Toyota to sell cars. And it's like, they're talking about the sales channels, right? They're talking about all the existing companies, right? You don't go to, you don't buy a car. You don't buy a Ford from Ford. You don't buy a Toyota from Toyota. You buy them from dealerships.

**Chris Gammell:** Right. You buy them from like distributors.

**Dave Jones:** You buy them from dealerships and they might have Toyota dealership on it, but they're not owned by Toyota. Right. It's like, yeah, it's, um, and, and there might be an authorized service center. That direct model is, yeah, you know, that direct model is why Tesla got a lot of. Tesla got a lot of industry flack at the time. Cause they went, well, why do we have to sell through a deal? Why can't we just sell it direct on the website? Why can't you just move car and shopping cart? Boom. Like, right.

**Chris Gammell:** But that also has changed a lot of things too. And I wish it would. Cause I have to buy a car soon, I think, and I'm not. Oh, really?

**Dave Jones:** Why is your one, is it getting too old? Is it crapping out or. No, no, no. I just. Child expansion. Yeah. Child expansion. Yeah. Exactly. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. Yeah. You'll be, you'll be getting the, um, what is the car of choice for those with like five kids? What is it? The, um, the, uh, Kia Carnival. As soon as you get a Kia Carnival. Kia Carnival. Yes. The Kia Carnival is the celebrity car of choice for those with four or five kids. Yeah. The Kia Carnival.

**Chris Gammell:** Oh my gosh. That thing's a beast.

**Dave Jones:** Yeah. Yeah. It comes in different sizes. It is so big. Right. Yeah. It's a. Yeah.

**Chris Gammell:** Are they allowed to have that in the, in, in Australia? Yeah. That looks like.

**Dave Jones:** Yeah.

**Chris Gammell:** Wow. That is a really big car. Yeah. No, I, I always think of like. Yeah.

**Dave Jones:** I haven't heard of a Kia Carnival.

**Chris Gammell:** Minivan. No, I never have. Yeah. Okay. I'm not. That's the thing. I have my only, the only car I've ever owned. Uh, that I've ever bought rather. Uh, was in 2004. Right. That was it. Right. Okay. It died. I moved to Chicago. I didn't have a car there. And now I, you know. Yep. Yeah.

**Dave Jones:** Anyway. Yeah. So as soon as you hit the third kid, you start thinking about the Kia Carnival. I think that's the. Wow. Yeah. That's a big car. Well, there are bigger. Like, like you can buy a giant. They're beasts. You can buy a giant. You can buy a Winnebago. Mercedes Benz. I don't know the model name, but they sell a gigantic tank. Thing. I, I actually posted a photo of one of these.

**Chris Gammell:** I can't afford this on a podcast for salary.

**Dave Jones:** Salary. Exactly. And, um, I, you know, there's one gigantic beast parked down in the carport, underground car park. And I tweeted a photo of it once. And like, I was walking past it. And the first thing I thought of is you could convert that into a lab. It's like, like it was so enormous and boxy. And it's like, you could literally like, that's actually bigger than my old lab in the garage. You know, it's like, and you could actually convert it. And if I had the space, I would probably do like a van conversion. You know, I'd probably do like that. Yeah. That's what I'm talking about. Yeah. Lab van conversion. Yeah. Like a sprinter van or something. Yeah. Something like that. Yeah. But I've got nowhere to put it while the conversion happens, you know.

**Chris Gammell:** That's a deep, dark hole to go down. Yeah. I know. I would not recommend people go on YouTube and start looking at van life. Yeah.

**Dave Jones:** Van life videos. Yeah. Yeah. Yeah. Well, they're all hat now, aren't they? It was all the rage. Yeah. Just like tiny homes. Yeah. Yeah. Tiny homes were all the rage. Yeah. Yeah. Right. People were like, oh, COVID. Didn't you want a tiny home at one point? You were bragging that you wanted, you were desperately.

**Chris Gammell:** I didn't brag. Hey. It's not bragging. No, no, no. But you were like salivating.

**Dave Jones:** You were salivating over.

**Chris Gammell:** Salivating is maybe a better term. Yeah. And then, you know, you know, it cured me of it one day I was like in an airplane bathroom and I was like, I had problems turning around in there. Not because I was like, I got it. Yeah. Yeah. Of course. Because it's an airplane bathroom. Yeah. And then I was like, oh, right. This is what they want you to. This is like what it would be like. Yes. Like that. Yeah. Right. Okay. Really?

**Dave Jones:** That actually cured you.

**Chris Gammell:** It cured me instantly. Yeah.

**Dave Jones:** Oh, that's great. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Terrific.

**Chris Gammell:** A little bit of reality smacking you in the face.

**Dave Jones:** Reality. And then, and then kids happened. And that's another reality smack in the face. Yep. Yep. Oh boy. Yep.

**Chris Gammell:** It's fun, man. Come on. It's fun. Yeah.

**Dave Jones:** Of course it is.

**Chris Gammell:** I love it. Yeah. I love it. Yeah.

**Dave Jones:** But you know, it changes things. Like you have to be practical in, you know, you have to do more. Yeah.

**Chris Gammell:** The only thing constant is change. That is very correct. And speaking of, I will be reworking training in the new year. So I do training currently. Did I ever tell, I think I told you about training.

**Dave Jones:** As in training, this is conceptual electronics training you're talking about.

**Chris Gammell:** No, this is Goliath stuff. Oh, right. Okay. So I do, with my coworkers, I do Zephyr training. I train people for Zephyr. Yeah, right. Right. How to use Zephyr. And we've been on last week, last week, last time about Zephyr as well. And so the way I've been doing this is one thing I hate about training in general is that everybody brings a computer that's just like, I don't know. Like so Dave brings his Windows laptop. He brought out of, you know, he got out of the dumpster room. Yeah, exactly. It's just like, yeah, it's got somebody else's window XP on it. Okay. And then you're always starting from different problems and different spots. And that's one of the problems. And so one of the things that we worked on was this thing called Chasm. And it's basically like, it's called desktop. Desktop as a service, which is a stupid term. But basically it's like desktop and browser.

**Dave Jones:** I'm sure you've mentioned this before.

**Chris Gammell:** Yeah, I think I have. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Anyways, there's another solution. That's what I really wanted to get at here, which is what we're going to switch that to. And it's kind of interesting. So there's this thing called code spaces. And basically like when you wrote code, were you ever doing VS code stuff? Or are you still kind of like Eclipse ID type of things? Visual Studio. You did like that moon. Right. Yeah, VS code. Yeah, you were doing that stuff. And so this is like, so code spaces is part of GitHub. And there's other services that do this. Yeah, yeah, there's. But there's this new, not new, it's not new at all. But there's a way that basically you, you can set up a container. And so like all of your tool chain is completely pre-installed in there. And this is what we had done on the Chasm thing as well. So basically everything's kind of pre-installed. And in the past you were like logging in and viewing a desktop and then you're launching VS code within there. And so it just looked like you were on someone else's computer. It was like a, almost like a remote, remote terminal. This new one is basically now it's code spaces is similar, except it's like kind of more opaque to the user. And so it's basically like someone. So like I would send you a link. Like I can send you a link right now and it would have the tool chain pre-configured. Yeah. It would have all the code in there.

**Dave Jones:** We actually played around with it live once. Oh, you did? Yeah, yeah. Oh, nice. You sent me the link. Yeah, yeah. You sent me a link and I went in and we played around. It just worked. Oh, yeah, yeah, yeah, yeah.

**Chris Gammell:** Okay, right. Yeah. Right. And that was still Chasm. But this new one is the code spaces. Yeah. And it's crazy because it's like one of the things that's cool about it.

**Dave Jones:** And it's free, right? It's part of-

**Chris Gammell:** It's free. Like it's basically like you have to pay for compute. So like I could send you a link and it would be, you could get like a couple hundred, you get like maybe like 50 to 100 hours of like compute time for free, I think. Oh, okay.

**Dave Jones:** Because it's all cloudy, right? So you've got to pay for the server time. Right.

**Chris Gammell:** Right. But then it's like if you're using like 100 hours or more and then you start paying, you know, a pretty reasonable cloud rate. And then it's like it's very much worth it, I think. You know, it's like if you're using it that much, you're basically getting value out of it. So, yeah. No, it's like this cool. And then you're- So the way it is like- So I would send you a link. You would click on this thing. You would then have this container in your GitHub account. Yeah. And then you'd have VS Code all configured with the code ready to go. And then it's like literally like run a command and you're already compiling. Mm-hmm. So like- And it's kind of like you can do the same thing. Like, you know, you hear about like continuous integration, continuous delivery. Like that's another thing that people do often for firmware stuff these days where it's like you and I might have- You and I might be compiling the same firmware on our computers. But if the tool chain is different or whatever, we might have a different binary. Well, now it's like we would be shipping that code off to be compiled on the cloud. And then we'd have a binary that's always the same. And now it's like also we get a copy of that same compiler on our GitHub account as well. So it's like you can always be sure that you have the same setup.

**Dave Jones:** Right. Very cool. That saves huge. Yeah.

**Chris Gammell:** It's, yeah. So many, so, so many problems.

**Dave Jones:** People have no idea. If you've never been in like a group workshop with all people working on a group workshop, like I'm not kidding. Half, half of the class, half the time is spent debugging problems with the setup. It's like, like half of it's wasted. Yeah. Every time, every time. Guaranteed. Somebody has a sound, puts their hand up. My system's not working. Oh, the driver's not in store properly. Oh, God. You know. Yep. Yeah. It's just a nightmare.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Yeah. Breathe in. Breathe out. Deep breaths.

**Chris Gammell:** Mm-hmm. Mm-hmm. I thought you were going to say about, I think you meant with the group workshop too, like about, so I've had it where, you know, you're making a final firmware image to like ship off. To someone else. And it's like, I've actually made the mistake where I've labeled it wrong at that stage after you've made it. And now it's like sitting in your local drive. Yeah, yeah. And you just label it wrong then.

**Dave Jones:** Yep, yep.

**Chris Gammell:** Like that's, that is a way to mess up a lot of stuff. You know, like.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah, yeah. You can really mess things up at that point. So, yeah. So this also kind of fixes that. So anyways, it's super cool. Check out Codespaces if you haven't done it. It's not, it's very big in other industries, right? In the software world, this is already like a well-known entity.

**Speaker ?:** Oh, yeah.

**Chris Gammell:** I'm sure it's huge. People are screaming at their real software people.

**Dave Jones:** Because both yourself and me are not real software people, you know. No. No. But my coworkers are. Right. Yep. Yeah.

**Chris Gammell:** No, it's really cool. It's going to be, it's going to be interesting. And I'm excited about that for the new year. Because. I don't know. Like, like, even to the point where, like, if you were, if I was working on, like, a test branch of some code. So I'm like, oh, I'm going to go and implement a new feature. And then I pull in, like, a new, like, library as well. Mm-hmm. I could just pull all that stuff in, including the library, send you a link, you boot this up, and it's got the library, the tool chain, everything that's updated to it. And then you try it just how I'm trying it. Yep. It's, yeah, that's pretty, pretty rad.

**Dave Jones:** Game changing. Yep.

**Chris Gammell:** Yeah. Yeah. Ah, code. I'll get good at it sometime, Dave.

**Dave Jones:** I don't think I'll ever be good at it. No. I'm just capable enough to sort of get myself into and out of trouble, you know.

**Chris Gammell:** I mean, you know, you did that, I enjoyed that CH32 V003 video you did. I thought that was great. All right.

**Dave Jones:** Oh, yeah. Yeah. That was all right.

**Chris Gammell:** I think it's still the, you know, you don't have the project. The project required, you know.

**Dave Jones:** You're right.

**Chris Gammell:** You don't have that.

**Dave Jones:** Yep.

**Chris Gammell:** You don't have that drive because you've got a deadline looming. What you need, sir, is a boss.

**Dave Jones:** I need a boss, a deadline.

**Chris Gammell:** Yeah.

**Dave Jones:** I need the wife to task me for a new electronics project. I need her to task me with an electronics project. Yeah, yeah, exactly.

**Speaker ?:** Right.

**Dave Jones:** Hug. Design this.

**Chris Gammell:** I'm actually going to be, I'm going to be tasking myself with this in the near, is home assistance stuff. Have you looked at home assistance?

**Dave Jones:** I hate home. I hate home automation shit. No. Why? No. No. What do you hate about it? I want a light switch, which I turn off and on. Damn it.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** I don't want lights. Although something, you know, although there's some things now, like I've got a new pool and it'd be nice to technically automate. Yeah, that's the kind of thing that I think about.

**Chris Gammell:** Yeah, yeah. Yeah, yeah, yeah. Right. Yeah. So like the, so we had Jeff Geerling on. We had Jeff Geerling on a couple weeks ago. It's all right. Yeah, I just dropped my really expensive wireless lapel mic. Oops. And Jeff was talking about this a little bit. He's done some videos about it too. But like, yeah, so basically it's like a, you install it on like Raspberry Pi or a local computer. And then it kind of sits there and it does your automation. Yeah. It can do it behind your firewall as well. So you don't have to go and talk out to Google servers or Apple or whatever. And then. Well, why the hell would you want to do that?

**Dave Jones:** If you're going to automate it, automate it locally for goodness sake.

**Chris Gammell:** Right. That's what I said I'm doing. So is that what you meant?

**Dave Jones:** Yeah. Right.

**Chris Gammell:** Yeah. Okay. Yeah. So you're saying I'm doing it right.

**Dave Jones:** Yes. Yes. Yeah. I know. I'm saying if I'm like, if people are going to automate their home, don't rely on that cloud rubbish.

**Chris Gammell:** Oh, I think that's easy use thing. Right. I mean, like if you were like, if you're like, you're like, you're like, I completely bought into the Apple ecosystem. I can see people being like, oh, well, I'm just going to buy the Apple this, the Apple that.

**Dave Jones:** Don't come crying on freaking Twitter when you're locked out of your house because you're, you know. Yeah. Sure. Sure.

**Chris Gammell:** Yeah. The ecosystem breaks or you've lost your keys or whatever. Yeah. Yeah. Totally. Totally. Yeah. But there's another thing called ESP home. And then you can basically write really easy automation. So if you wanted to make a, like a pump monitor for your pool. Yep. Right. And you could make like an ESP 32 current clamp monitor, write some, write a couple lines of YAML and then you're like done. And then it hooks right in.

**Dave Jones:** A few lines of what?

**Chris Gammell:** YAML. Y-A-M-L.

**Dave Jones:** What the hell is YAML? Is this a spinoff from YAML?

**Chris Gammell:** Yeah. That's what I said. That's exactly a joke. What the hell is YAML? No. YAML. It's like a yet another markup language, I believe.

**Dave Jones:** Oh, I was going to say it's yet another language. And it's literally in the name. Yeah. Yeah. It's literally in the name. Yeah. Yeah. So at least. Yeah.

**Chris Gammell:** It's pretty. I mean, it's basically like directives. So if you've ever seen like.

**Dave Jones:** It's pseudocode.

**Chris Gammell:** Docker lines. Yeah. That's a scripting.

**Dave Jones:** Everything's devolving back to pseudocode. Yeah.

**Chris Gammell:** I think that's right.

**Dave Jones:** Hands up in the comments. Does anyone do pseudocode? Do they actually teach pseudocode anymore? Because they used to teach pseudocode. You used to learn pseudocode. A bit out of school, Dave. Right now. Yeah. That's why I'm asking. You know, I haven't been in school for, you know. Yeah. Long time. Yeah.

**Chris Gammell:** I did visit Duke finally. I got to see some of the Duke facilities. Yeah. Okay. That's my. That's a local university where I live. So.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. Finally met someone from there.

**Dave Jones:** Right. I did a tour of the University of New South Wales. That was cool.

**Chris Gammell:** Oh, how did that go?

**Dave Jones:** Yeah. You can watch my tour video of their lab. They've got a lab there. Oh, I should have. Yeah.

**Chris Gammell:** Because I should have done a tour video. Yeah. Okay.

**Dave Jones:** Exactly.

**Chris Gammell:** That was in the quantum thing, right? That was. Yeah.

**Dave Jones:** That was part of the quantum. I shot that on the same day. Oh, it was.

**Dave Jones:** Okay. Okay. So. Thanks for reminding me. I have to do part two of the quantum video. Got it. Yeah. Yeah. A bit of an editing nightmare. Okay. Because I had multiple cameras and they're all. Everything's unsynced and all the audio is unsynced on different. You know.

**Chris Gammell:** That's fun.

**Dave Jones:** Yeah. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. So hopefully I'll have some, you know, again, like software people who are into home assistant. They're going to be like, yeah, Chris, welcome to the party like 10 years ago. Yeah. All these things that I'm talking about.

**Dave Jones:** Exactly.

**Chris Gammell:** But I'm doing it now. So it's fun for me. And some people out there haven't heard about this stuff. Right. And also I know how to solder and maybe you don't.

**Chris Gammell:** Yeah. Also, I'm in charge here. I am the captain now.

**Dave Jones:** Well, if I am going to automate my pool stuff, I might look into this ESP home thing.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Because I don't like it's like, you know, because I don't keep up to date on a lot of stuff like you do because it's your job, you know, to keep up to date on all these platforms.

**Chris Gammell:** I mean, this is.

**Dave Jones:** What not.

**Chris Gammell:** But this is also like smart home stuff. Right. So it's different. Like it's consumer. It's open source. It's like, this is more like hobby level stuff that I would do for myself.

**Dave Jones:** Well, I used a smart home thing before. I was monitoring my lab temperature and then the server freaking just vanished one day. You know, it's like, it doesn't work anymore. It's like, oh God, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Give me a break.

**Chris Gammell:** You were doing that. You had it for, you had like a third party service for your solar, I remember as well. That's kind of.

**Dave Jones:** Yes.

**Chris Gammell:** Smart homie.

**Dave Jones:** It's a.

**Chris Gammell:** But that was like a standalone service.

**Dave Jones:** It's a monitoring system. It's their own. Yeah. It's a 4G based. It actually reports VAC via cellular and it reports the data back and logs it and all that sort of stuff. Yeah.

**Chris Gammell:** But you would just check that on like their webpage. It wasn't like tied into other stuff.

**Dave Jones:** No, it's not tied into. They don't actually make any other automated devices. It's just you. Yeah. You just log into their website or the app and you can, you know, see your consumption and monitor in real time and stuff like that. Handy. But it doesn't tie into anything, you know?

**Chris Gammell:** Yeah, exactly. I think that's what it comes down to is like how, how much you expect your users. So like in that case, like they're selling a standalone product and there's probably not a lot of incentive for them to be like, well, we have open APIs. If they don't have like a developer community or whatever. Yeah.

**Dave Jones:** No. Why would people care? Yeah. Yeah, exactly.

**Chris Gammell:** And so it doesn't really add anything for them.

**Dave Jones:** My zappy EV charges like that. It's like technically they do have an API, I think, but everyone bitches about it that it's not, although I haven't checked it in the last year, but you know, last I looked at it sort of like it was clunky or something like that. And it's like, and they don't like, they, they actually offer technically offer a product to do what I want, but it doesn't do what I want because it's, it's, it's actually designed to drive pumps, pumps directly. Like just a bare pump directly. I don't want to do that. All I want is for my, any excess solar, I want it to just switch a relay. That's all I want it to do. I want a little box, which said it, it no, like I've got the complete control solution. I've got a hub, which not, which can tie into other devices. And all I want is just a little relay output, like to just, just to trigger my heat pump, you know, to turn on and use excess solar or something like that. But they don't sell that product and it's not integrated to their zappy. It's like, if I was designing that EV zappy, I would have had a simple relay with a control output that says, well, if your EV is not charging, okay, you can use the energy for something else. And here's a relay contact. Boom. You know, but they didn't build that in, you know, it's like, so wait, tell me, tell me

**Chris Gammell:** again about the power routing stuff. So this is like your solar is overproducing.

**Dave Jones:** My solar is overproducing. So my zappy charger has current clamps. It can detect a difference in the car that I'm exporting current. Right. So I'm exporting power. Okay. You don't want to export power because you get to pay the pittance for it. I want to charge my EV with it. So as soon as it goes excess by a certain amount, it'll start charging your car if you've actually plugged it in. Right. And I'd also like it to.

**Chris Gammell:** Different problem. Yeah.

**Dave Jones:** And I'd also like it to do other things like to recharge my storage battery using excess. Yeah.

**Chris Gammell:** So you want like a, like a, like a logic diagram almost of like, yeah, if this, then that, that sort of thing almost.

**Dave Jones:** Yeah. Not even like it can already set, uh, priorities cause they sell like a specific heat pump. Uh, they spell a specific, they actually sell a specific pool heater thing, but it's designed to like drive the element directly. So they've got like the mains, you know, uh, you know, uh, SCR chopper thing for, for like driving the element at various, at different powers to match the excess solar power. And it's like, oh, I don't really want that. I just want to relay that just goes off and on. You know, it's like.

**Chris Gammell:** So you're going to then control your, your heater. You're going to turn on your heater. I would, I would switch on the heat pump. Yeah.

**Dave Jones:** I would. If we're using excess power. Is that right? Yep. But then you've got the problem hysteresis, right? What if it suddenly comes over cloudy for a few minutes? Do you want to keep switching your heat pump off and on? The answer is no, you don't. Cause it's not good for it to be chopping it a hundred times a day when it, when a cloud comes over. Right. So you want some hysteresis programmed into there so that it, you know, it comes on and stays on and then only will switch back off when it's truly dark or based on a timer or, you know, like based and like, like an all function. Like if you've got, yeah. Yeah. And if then else, you know, or yeah. Some sort of logic function so that if you've got excess solar and it's in this time.

**Chris Gammell:** Yeah.

**Dave Jones:** And it's in, and it's within this time window, then turn it on. And you know, but, uh, I don't know. And then you've got, uh, priorities. So you want to go, Oh, I need to charge my EV. I know. You know, I want to, I want my EV to have a priority today, please. But tomorrow I don't kind of thing. You know, it's like, it gets real messy.

**Chris Gammell:** I think this is one of the problems with, with smart home in general. Like, so smart home is kind of its own class of things. And, and there's like, so one, one problem is that it's multi-vendor, right? So like, it's, you might have Google, you might have Amazon, you might have, who knows what, you might have something you bought off of, you know, a marketplace somewhere. It might be something you built yourself, but like getting those things all to work together. It's like, there is no, basically the answer that Apple has for, I want my Apple speaker to talk to my door lock is like, make sure your door lock works with Apple because we are the 800 pound gorilla. Yes. Right. That is basically their solution. And it's like, if you don't work with us, you're not friends with us. Don't go away. Right. And it's like, I get it from a business perspective. That's fine. And it's not just Apple. I'm just picking on Apple. Fine. I think actually Stacy Higginbotham, when she, she, in like her last episode with Kevin of the IoT podcast, she was talking about this, like the frustration that she thought, she thought this was going to get better over the years that they did IoT podcast. Right. And it's legit. I mean, no, it is legitimate. Like basically it's like that it, that the control should have moved further up in the software stack. I think some of it did, but I think the problem is that there's just still, you know, there's still so much commerce involved. Yes. And that like, there's big companies jostling for position and thinking they're going to win everything. And there was no incentive to, to be like the most open. Right. There, there, there, they were disincentivized from that, I think. Like, and so what I'm excited about with home, home assistant is it's like, okay, well you can start to do some of this yourself and it may not be perfect. It's probably going to suck actually, but I think it's going to be like, at least I'll have some more agency. And that's all I really care about. Yeah. Yeah.

**Dave Jones:** Yeah. And, and, and I, I get this all the time. People, oh, why don't you just write a few lines of code and you can automate your heat pump with your EV. And it's like, it's, it's not the usage scenario is actually a lot more complicated than that. Unfortunately, it's not, you know, there's so many different scenarios that I want it to do something different in so many priorities.

**Chris Gammell:** So they're saying to like write it, write like a code for like a microcontroller to do that sort of thing.

**Dave Jones:** Well, it's, it's not just that it's how it's, it's not just the technical part of doing it, the technical part of doing it, you can do it. But the, but the part of. Yeah.

**Chris Gammell:** You know how relay works.

**Speaker ?:** Yeah, exactly.

**Dave Jones:** But the part of actually deciding what you want today, because your, my requirements on one day might be different to requirements on another day. Sometimes I want to prioritize my EV. Sometimes I want to prioritize the heat pump because the kids want to go. Swimming tomorrow. The wife wants to go swimming tomorrow. So I better heat that up today. And I bet, you know, but we do want to actually go somewhere in the EV and we've got all this and I want to charge my rechargeable, uh, you know, storage battery. And like, it's not that it's.

**Chris Gammell:** First off, first off, very first world problem you have. Oh yeah. I totally. Right. I can, I can, I can relate. Yeah, no, totally. It's like, it's fine.

**Dave Jones:** This is why I don't necessarily jump right into it and just people think I can just solve it by applying any one of these various technologies to it. But like, technically it kind of sort of can, but on an operational level, it's just so, there's so many different requirements and they're all, and they conflict sometimes. And like, how do you handle that? And like, you know, I'm almost better off just manually doing it, you know, just, oh, okay. Well, yeah. We need the heat pump tomorrow. We'll just switch it on. Flip the switch. Yep. Yep. Exactly.

**Chris Gammell:** Yeah. Yeah. Yeah. I think, I think some of this is also like a good analogy of like why you have layers of abstraction in the first place. Right. So like, like you should basically have some firmware that like just says, listen for signal, flip the relay. Right. You want it to have like, that's dead simple. It always works. You know, it works, whatever. And like the function is not going to be, but like, you wouldn't want to go and write like your scheduler logic in C for a microcontroller that like, then you're like changing on a daily basis. Exactly.

**Dave Jones:** Exactly. You're trying to handle these different things. It doesn't work. You have to have some high, huge higher level interface, like a button on the wall, like a mode selection switch on the wall that says priority. Sure. Yeah, exactly. Priority switch. You know, like. Right.

**Chris Gammell:** Or, or, I mean, like even that then, like, so now you have like a scheduler layer in software that's a step above, you know, you're talking to it over wifi or whatever. And you're, you're now at the layer where you're like writing software almost at a web level. And it's like, okay, now I can like handle schedules or, you know, take input from various other sources. It's kind of where I see that, that home assistant layer kind of living. Yeah. But then like, all right, Dave, I'm going to go out on a limb here. I'm going to, I'm going to go out on a big limb. I think there is a potential layer above that. That's AI that might actually potentially someday. We're not there yet. Someday have some use case up at that layer. We're not there because the other stuff's broken as shit too. Right. But like, but that's where, if it should ever live anywhere, it should live up there. Way in the way, way, way.

**Dave Jones:** The problem with AI at the moment is it just invents things. It just imagines things that aren't real. Exactly.

**Chris Gammell:** You know? Yeah, exactly. Did this, I've just figured out, Dave, that your, your kids want to go for a drive in your EV in your pool next Thursday, Thursday, Thursday day. Right? Yeah, exactly. And it thinks it's totally legit, you know? Yeah. Right. Oh boy.

**Dave Jones:** Yep. Yep. Yeah. AI is overrated. Yep.

**Chris Gammell:** It totally is. Yeah. I just, I was just talking to my lawyer brother-in-law about, he's, you know, a lawyer. And I was like, oh, how is, you know, I hear that like AI is coming to the lawyer space. He's like, yeah, no.

**Dave Jones:** No. And I'm like, oh, yeah.

**Chris Gammell:** That's how I feel too.

**Dave Jones:** There's something there. When it first came out, you're like, I was amazed. Like I've, I've changed my tune on AI. I thought when it first came out and it was doing this amazing, like, it's an amazing tool. It can be an amazing tool, like phenomenal tool, but people are then extrapolating that, oh, in 12 months time, it's going to be doing this. Oh, I see. And it's just, no, it's bullshit. And, and I've publicly made the claim on Twitter and I'll make it here as well, that general, like true general AI, right? That is the, you know, that's the AI that can actually, is I'm, I'm going to claim it'll never happen. Never happen. Never happen. No, no timeframe.

**Chris Gammell:** Oh man.

**Dave Jones:** No timeframe. We're true. There are a lot of people who will claim it, but I'm, I, I, I now think it's not going to happen.

**Chris Gammell:** I do agree with, I do agree with that. That's going to happen many times and there's going to be scares about it. And there's going to be like the guy that got fired from Google about like whistleblowing about like whatever.

**Dave Jones:** And then they'll find that it's no, it's just like a smarter niche. A hundred monkeys behind a curtain. Right. Right. Right. There'll be so many startups making billions of dollars and they'll go bankrupt because like when the curtains pulled back, there's, you know.

**Chris Gammell:** Do you know how expensive it is to buy a .ai domain? It's like they figured out that like, oh, you, cause you could fund, you could literally like right now you can, maybe not literally, not right now rather, maybe like a year ago, you could literally fundraise off the idea that you had a .ai domain name. Oh, really? Adding capabilities that are artificial intelligence.

**Dave Jones:** All right.

**Chris Gammell:** Dave, there is yet to be an AI that can save me from myself when I do a layout. Let me tell you, I don't care what they say. I can, I can mess anything up.

**Dave Jones:** Well, where's, where's a PCB routing AI? Where is it? Huh? Yeah. I was calling that.

**Chris Gammell:** I mean, you know, we've had, we had Sergey on here and it looks, it's a great stepping stone towards something. I'm excited about Quilter and other similar things, but it's just, it's a tool. It's a tool still. It's fine. And that's, and that's okay. Like it's still super valuable if it is a tool. Super valuable tool. It's just not AGI. I actually use AI as a tool.

**Dave Jones:** I use it a lot. Cool. You know?

**Chris Gammell:** But that's what I think we've been saying on here that it's going, it's going, I think it's going to go in that direction. That's fine if it does. Yep. Cool.

**Dave Jones:** So both you and I are saying don't invest in AI companies because most of them are probably going to be.

**Chris Gammell:** Don't invest in it. Well, don't worry about me. My money's tied up other places known as, known as bigger family. Right. I got to go buy this Kia Carnival. Holy shit. You got to buy a Kia Carnival. 11 seats. 11 seats. Who needs this? This is insane. You do soon.

**Dave Jones:** I don't.

**Chris Gammell:** This is, I'm done. I'm done. Done. Done. No, no, no 11. I mean, maybe if I need to like drive the other kids around. Yeah. Yeah.

**Dave Jones:** Because you build your lab in the back at the same time. You could multitask. Oh my gosh. You could multitask.

**Chris Gammell:** Yeah.

**Dave Jones:** You could work out of the back.

**Chris Gammell:** You could work out of the back. Yeah. Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Right.

**Dave Jones:** Just think of the possibilities. Oh God. Oh, this is so bad. Anyway, our amp hours up, but we should mention, because we have mentioned it on the show many years ago, Bunny Huang's Shenzhen Guide. There's a new addition to that. And it's written by Naomi Wu has updated that. So she is back kind of. Yes. Yes. So much as she's still around. She.

**Chris Gammell:** I hope she's okay. Yeah.

**Dave Jones:** Disappeared in quote marks.

**Chris Gammell:** She stuck her neck out and. Yeah. And she was.

**Dave Jones:** Yes. Chinese disappeared. Yeah. Yeah. Yeah. But no, she's. She has tweeted again and now she's written this. Well, she's like done the update to this book. So you can. It's.

**Chris Gammell:** It looks great. Yeah. Yeah. Yeah.

**Dave Jones:** It looks. Looks really good. They raised 40 grand of their 10 grand goal, but you can. There's view purchasing options. So if you missed out, obviously you did miss out on the crowd funder, but you can get it for 30 bucks and you can back it and we'll link it in down below. So, so yeah, if you're ever shopping in Shenzhen, you probably shouldn't go without getting this book, you know. Yes. I agree. Yep. Totally. I would not even hop on a plane there without getting this. Yeah. It's great. Anyway. Good to see that she's okay. And back. Kind of. Sort of. Even if. Yeah.

**Chris Gammell:** I hope we get to see more videos of hers. Yep. I miss her.

**Dave Jones:** Anyway. Yep. That's it.

**Chris Gammell:** All right. See you soon.

**Dave Jones:** I guess. Catch you next time.

**Chris Gammell:** We'll get AI to do that.

**Dave Jones:** Yeah. Right. Okay. Bye.

**Dave Jones:** Thank you.
