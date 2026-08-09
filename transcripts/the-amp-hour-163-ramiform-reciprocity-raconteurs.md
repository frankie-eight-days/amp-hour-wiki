---
episode: 163
title: Interview with the Upverter Founders - Ramiform Reciprocity Raconteurs
url: https://theamphour.com/the-amp-hour-163-ramiform-reciprocity-raconteurs/
---

**Chris Gammell:** This is The Amp Hour Podcast, recorded September 16th, 2013. Episode 163, with the founders of Upverter, Ramiform, Reciprocity, Racontours.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEVBlog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life.

**SPEAKER_01:** Zach Homet of Upverter. Stephen Hamer of Upverter also. Michael Woodworth of Upverter.

**Dave Jones:** What are the odds of having all three people, all three guests from Upverter? Dave, we're surrounded. Worse than that, we're surrounded by Canadians.

**Chris Gammell:** Oh, man. I grew up surrounded by Canadians, so I'm not used to it. You're welcome. The poutine was delicious.

**Dave Jones:** Thank you very much for coming on, guys. Well, thanks for having us. They forgot to give their title, so I will do it for them. Zach is the founder and CEO. Steve is the – is it Steve or Stephen? I go by both. All right, Steve it is. Shorter. Founder and CTO. And Michael is a founder and CIO.

**Chris Gammell:** CIO. What's a CIO? That's a made-up title. Oh, okay. We needed a C in there somewhere. We wanted it to be technical.

**SPEAKER_03:** You know, so we just started going for it.

**Dave Jones:** CIO is Information Officer, is it not?

**Chris Gammell:** It is, yeah. Oh, is it like IT type stuff? Like the actual back-end webby stuff?

**SPEAKER_03:** I do very little of that these days, actually. Okay.

**Chris Gammell:** But yes, that is generally what an IT person does. But you tell people what they should be doing, right? That's called management.

**SPEAKER_03:** Yeah, well, some days. Some days I tell them what they should be doing. They do whatever they want anyways.

**Chris Gammell:** Right, yeah. Well.

**SPEAKER_03:** Mike is actually – Mike's actually heading up our sales lately. Oh. Oh, okay. And trying to figure out how we make money.

**Dave Jones:** Oh, yeah. From all the stuff we've built. One of those trivial things like, yeah, making money and eating.

**Chris Gammell:** Yes. Not just ramen, right? Yeah, startup life and all that. Yes. So who wants to give us the overview of people that have not heard of Upverter yet, who obviously haven't heard the show because we've talked about Upverter as well?

**SPEAKER_03:** Sure. Yeah, I can do that. Okay. So at like the super, super, super simplest, Upverter is a – it's a multiplayer CAD tool in the web browser. And so it's a tool for designing electronics. It lives in the web browser. It's built on top of HTML5 and JavaScript. And it lets you design circuit boards. There's a bunch of kind of cool community stuff and reuse stuff and collaboration stuff that we've baked in. But at the end of the day, we're just trying to build a better CAD tool.

**Chris Gammell:** Cool. Yeah. So CAD is not trivial to build a – so why did you say we were just – you know, screw it. We're going to start over and make an entire CAD tool, whereas maybe others were starting with existing CAD tools and like why did you decide to actually build the entire CAD tool?

**SPEAKER_03:** So we kind of started by trying to build it on top of other people's stuff. We looked really hard at GEDA. We looked a little bit at Cadence and a little bit at Altium and tried to, you know, like build version control for them. Like if you could build Git for hardware stuff or take Git, right? Like don't even rebuild Git. Just take Git and make it work better on those files instead of having to build your whole own tool. Or, you know, GEDA if we could take it because it's open source. Clean it up a little bit and jam it into a web browser. And we looked at all of that. And it goes way, way, way back to like our earliest days, so like three years ago. And it was – we were in my parents' basement in like a little tiny farm town in Ontario. And we were trying to jam GEDA into the web browser. It was a nightmare. And, you know, we generally failed. And Steve can talk a bunch more about that than I can. But like we totally failed to do it. And that was why we ended up building our own.

**Dave Jones:** So was it a start-up from day one or were you just sort of, you know, bumming around with this on the weekends?

**SPEAKER_03:** So we were college roommates. That's kind of our story. That's how we met. So we were in the same dorm room at the University of Waterloo like nine years ago, guys. Is that right? Yeah. And so we met. We were in the same class together. We all kind of like failed school together and, you know, tried to figure out engineering together. And we were all kind of startup curious. And so after school, we'd all kind of gone our separate ways and we got back together, kind of got the band back together. And we were going to start a startup. And we looked at some hardware stuff. We had good ideas about how to do better radar for like pirate ships and how to do better, you know, better Dropbox and better. Oh, God. What was the other one? We were doing like a home phone kind of device. And there was like some currency stuff like way before the Bitcoin days. And we were looking at all this stuff. And one that was like really near and dear to our hearts was just like how painful it was to design hardware, let alone share hardware, let alone get it manufactured. And it just it ended up kind of bubbling up to the top.

**Chris Gammell:** Can you radar for pirate ships? Can we? Can we? All right. All right. All right. We're going to let that sit on the table. I don't know.

**SPEAKER_01:** I want to clarify. We probably had good ideas of what we'd like to do on the marketing side of that. I'm not sure we actually had any idea how to build it.

**SPEAKER_03:** We had a logo picked out, a slogan, we protect your booty.

**Chris Gammell:** That's lots of booty jokes, right?

**SPEAKER_03:** Yeah. Lots of booty jokes going around. So is this implementation? Kind of weak.

**Chris Gammell:** So were these marketing meetings at the bar? Is that kind of a thing?

**SPEAKER_01:** We were a little hungover actually still. All right. We thought it was a great idea.

**SPEAKER_03:** If we knew anything about radar or flying things or pirates, we probably would have done it.

**Chris Gammell:** All right. But instead we got up for it. So that's a decent trade. I like that. And if your customers don't like you, they kill you.

**Dave Jones:** Yes. Yes. Yes. Yes. Not a good business to be in, I suspect.

**SPEAKER_03:** It's very binary. Right. Kind of like startups generally. Yeah. You know, dying means something different.

**Dave Jones:** Dying means you wipe your hands and you've lost someone else's money and then you move on to the next idea. Right. Yeah.

**SPEAKER_03:** Right.

**Dave Jones:** Are you guys using someone else's money?

**SPEAKER_03:** We are.

**Dave Jones:** Oh, excellent.

**SPEAKER_03:** So when we, yes, lots of it.

**Dave Jones:** Tell us the backstory of this. Like, you know, because we're always interested in the funding of, you know, startups like this. How long did you spend, you know, using your own money? And then how did you come across real money? Yeah. So magic money.

**SPEAKER_03:** So when we started Upforter, I was the degenerate addition to the team. Steve had a bit of personal money saved up and Mike had a bit of personal money saved up. And I had a bunch of student debt. And so I was kind of the anchor in the whole money thing to start with. But my parents were pretty great about it. They put us up for free and they loaned us a little bit of money so that I could, you know, pay my student bills and keep us alive for a little while. Stevie put in his personal money. Mikey put in his personal money. And that all lasted us about four months. And that was the first four months of the company. And I can remember sitting down and, like, looking at the books and being like, we get four months. This is amazing. Like, four months is so much time. Zach was going to have the first version fully working and sold in four months.

**Speaker ?:** Oh, yeah.

**SPEAKER_03:** Absolutely. He guaranteed it. It was profitable by then. So Zach was the hardware guy to start with? Is that right?

**Speaker ?:** Yeah.

**SPEAKER_03:** Yeah. I was the hardware guy. But, yeah. So we eked along for kind of our first four months. So we started the company in August. By November, we had our first kind of promises of angel money. And it was from friends. It was, like, guys that we knew that were angel investors but that were friends of ours. And then in late December, we got into Y Combinator. And so that brought in about $20,000 in funding. So at that point, we probably had, I don't know, $35,000 maybe in outside money and probably about $40,000 in personal money. So we were about at the break-even point there.

**Dave Jones:** And how long does that sort of money last? Three guys. Was it only three at the time? Yeah.

**SPEAKER_03:** It was just the three of us. And we weren't spending any money at all. It's for food, pretty much. We were really lean. Yeah, exactly. And coffee, right?

**Dave Jones:** Peter and Joel Kola. Yeah, you're right.

**SPEAKER_03:** So at that point, we probably had, like, six months worth of money if we wanted to take our time with it. But then we raised our first kind of real money. And it was from one of Yuri Milner's funds as part of what we were doing in Y Combinator. It was another $150,000. And then at the end of YC, we did Demo Day. We raised total. So, like, if I roll everything up at the end of Y Combinator, we had $450,000 in external money. And that was enough. Like, at the time, that was enough for 12 months. Like, we looked at it. We wanted to hire some people. We kind of knew what we wanted to do with the money. And it was, like, perfect. We got a year. And we didn't do nearly what we wanted to do in that first year. Like, it took us way longer. And we got really lucky. And we brought on a little bit more money along the way. But we were able to take that $450,000 and use it for all three years of the company's life up until, like, two months ago. So, all told, in June, we had only raised $650,000, give or take. And that had lasted us three years. So, we got three years out of $650,000. And then just recently, and we haven't announced this publicly yet, but just recently we closed another big round. Yeah. We just raised another big round of money. Excellent. And so, it's our official seed round. So, it's, like, officially our first venture capital money. So, we've graduated from angels to VCs. And that closed in the middle of June. Well, congratulations.

**Dave Jones:** What's the difference between angels and VCs, really?

**SPEAKER_03:** So, nothing. It's the size of the checks they write. Angels tend to be more useful. VCs tend to write bigger checks. And so, it's what do you need? Do you need people that are useful or do you need people that write big checks?

**Dave Jones:** And do VCs, I assume that VCs also expect a larger return quicker than angel investors, potentially?

**SPEAKER_03:** So, most of our angels, like, and we're very, very blessed with a lot of the angel investors we have. Most of these guys don't know anything about what we're trying to do. They don't know why we're trying to do it. They just, you know, they believe in us. They, you know, they believe in the collaboration of the collaborative economy. They believe that the world of atoms is going to look a lot like the world of bits given enough time. And that we're, you know, we're somewhere in there. And so, they, you know, they get all that. And they want to help. And they like who we are. And they like the story. And, you know, and at some point, three or four years ago, somebody gave them a check. And that's why they can write checks.

**Dave Jones:** Ah, right.

**SPEAKER_03:** And so, like, so there's a lot of pay it forward. And there's, you know, and we look for angel investors that help us with things that we're really bad at. So, like, we try and bring on angel investors that have, like, sales skills because we're terrible at that. And, you know, or marketing.

**Chris Gammell:** Someone who's just insulted at that mixed company.

**SPEAKER_03:** Or I've only bought it, you know, three weeks. How do you know how terrible I am? That's true. That's very true. Give it a chance. But, like, and then, but, like, at some point, at some point, you, the angel investors, like, they don't really expect a return per se. Like, they, you know, they want their whole portfolio to return. They, you know, they're not doing it to, like, to dispose of money. They're doing it because they want to make more money. But they're doing it for a lot of other reasons. VCs are only doing it to make money. Right. And that's, so, like, that's the really big difference between the two is you're working with somebody whose job is investing versus somebody whose hobby is investing.

**Chris Gammell:** Got it. Interesting.

**Dave Jones:** What about the, uh. Did any of you.

**SPEAKER_03:** Oh.

**Dave Jones:** Go ahead. I got in first. You go ahead. Did any of you have any fear of taking other people's money? See, I am the type of person who probably couldn't, like, that would keep me awake at night knowing that I'm burning someone else's money. That would just, I don't know. I don't think I could handle it. Did you guys have any fear? No, we'll take it. Thank you very much. Woo-hoo.

**SPEAKER_01:** Oh, certainly. And the friends and family money was. That'd be tough. Always the most stressful, right? It's people that you know and talk with all the time. And with the family, at least, they're not in the same position as the angels. You know that they don't have many millions of dollars squirreled away somewhere. They're doing this because they believe in you. So, yeah. Yeah. No, I think we all had a bit of that.

**Dave Jones:** Had? So you don't have it anymore? Still do. There's no more fear.

**SPEAKER_03:** It's all over. So, like, you know, I think I agree. I think I agree with Steve. Like, we took money from friends and family. And it was a really torn decision, right? Right. It's like you take the money because if you don't take the money, this thing's going to die and you want this thing to live. But at the same time, you're taking money from people who you know their life will be worse if you lose that money. Got it. Right? Like, you know that their quality of living is going down because of what you're doing in the short term and potentially in the long term. Right? And the payoff's really not that great for friends and family. Like, it's non-zero. But they're not.

**Dave Jones:** No, they're not going to become instant millionaires.

**SPEAKER_03:** Right. They're coming in early for small amounts of money, right? So, it's like, you know, they maybe 100x their money but it's not going to change their world because they only put in $10,000. So, I don't know. So, there's that. But, like, taking money from institutional investors and angel investors, not really. Like, you know, these guys, they become your friends. Like, and, you know, and you want to give them a return because you like them. But it's not. I don't know. Like, if we blew up and ran out, I think most of these guys would write us a check to do something else. Right. Like, they still, you know, like, they believe in us. They know that we're not, you know, they know that we're not taking it to the casino or, like, something like that. Right. You know? Yeah, yeah. So, it's, you know, I don't know. That's kind of where I'm at on it. Mikey, what do you think? I certainly had. I guess I still do a little bit. It's less now than I used to. I think it's one of the things that drives us a lot, though. It's that you're playing with other people's money. There's responsibility with that. I think it's made us work really hard. But that's a decision.

**Dave Jones:** Oh, sorry. That's a decision you've got to make up front when you do something like this that doesn't have an immediate profit return. So, you can't bootstrap yourself. There's a, you know, this is a non-bootstrappable kind of business you guys are in. Yeah. Or wasn't. Kind of, you know, for the first.

**SPEAKER_03:** Yeah, I mean, the amount of time it takes to build something like this. And we've been working at it full time. And so, you would never, well, eventually you will get to something. The problem is somebody's going to beat you to it if you're not full time on it. And, well, hopefully. Well, and it's even more than full time, right? Because you've got to, like, over-invest. We've been, like, our sales are effectively zero. It's been three years. And we've been an average of seven people, right? So, like, run that payroll. Yeah. And, you know, you're at a million dollars paid up front for a thing that doesn't make any money. Which is, like, and you just, you know, so we couldn't, we could never invest a million dollars of personal wealth in this kind of thing. Like, we just, none of us had any money. But, so, like, it is the kind of thing that needs to be, like, it is venture capital in the sense of, of it is an exploratory venture, right? Like, it is, you know, nobody knows if this is going to make money, but we're going to put money down. Because if it does, it's probably going to make lots of money.

**Chris Gammell:** Right. Well, that's, it seems like it makes the, I mean, if you guys decided you wanted to do it anyways, then that's, makes the decision to take money easier then, right? It's like, well, we do it or we take it, we don't. You know, let's just go.

**Dave Jones:** I guess it comes down to the mindset of the person as well, because I'm a bootstrap kind of guy. I've always, you know, ever since I was a teenager doing kits, I've always gone, oh, okay, I can put my own money in to build 10 kits. And I sell those 10 kits, I make a profit, I use that profit to bootstrap, you know, the rest of the business kind of thing. It's just something that I'm risk averse, more risk averse kind of person. I like to see that immediate result, you know, that, that immediate, you know, oh, things are happening. Great. I'm making money in the first month.

**SPEAKER_01:** Yeah. And it's got feedback to it. It lets you do what you're doing.

**Chris Gammell:** This is more system based, it seems though, as well. The, you know, you need, you need a lot of the things to be right before people will buy into it. Right. I mean, like, if I have a CAD tool and it's like only, only the silkscreen part of it works, it's like, well, okay. It's interesting, but I'm not paying for that yet.

**Dave Jones:** That's you, it's tits on a ball. Yeah. Exactly.

**Chris Gammell:** It's like, all right, well, yeah. So I can see that as well, the system side of it. I wanted to ask though about the, so you guys are, I mean, you guys are working on a hardware centric company, right? You know, designing hardware in, you know, CAD tool. But you were at a startup accelerator thingy, the Ycom and your guys are all software. Was that like, like being strangers in a strange land or, I mean, obviously you were as Canadians anyways, but.

**SPEAKER_03:** So it, so actually the Canadian thing's interesting. It's, it's about 10% of YC. Really? Oh, cool. Yeah, it's, it's about right. Waterloo, actually, interesting enough, is one of the most represented universities in YC. Yeah. It's, it's pretty high on the list. But, so like, that wasn't bad. Like in our class alone, there were, I don't know, half a dozen Canadians maybe, including us. So, so like another three or four guys. But, but in terms of like the, like we build software, that is what we do all day. Like we, you know, our, our engineering team writes code and it's code for building hardware. But like we're, we're as much a software company as anybody else that was going through YC. That being said, like we went through YC at the same time as the Pebble guys. So like, you know, the very real hardware company in YC at the same time as Austin, there's been a ton of hardware companies since then. They're, they're really trying to get better at, at helping hardware companies. You know, PG has that mindset. So, you know, really not bad. And the advice is kind of the same, right? Build something that people want, find a way to distribute it, find a way to market it, you know, sell it. Like, you know, software or hardware, it's kind of the same.

**Dave Jones:** Now, with YCombinator, do they, they get you to move to Silicon Valley for a while, don't they?

**SPEAKER_03:** Mm-hmm.

**Dave Jones:** Do you guys do that?

**SPEAKER_03:** Yeah, we were there for six months. Yeah, we were in Mountain View for six months.

**Dave Jones:** Why, why is that? They want you, they want to closely track what you're doing or they think it's important for your enrichment or what?

**SPEAKER_03:** I would certainly think it's closer to the enrichment. I mean, there's a huge sense of community. Um, I, I completely understand now how important it was to be there and, and just be at, at the dinners every week. I mean, we showed up and if you didn't have something new and shiny to show, you were embarrassed. Right. Because everyone else had done something cool. And, you know, you got to talk with some amazing people. And so I, I think.

**SPEAKER_01:** You got to talk through your problems with people as well. And it was nice to, to be in a situation that other people had the same problems as you. Yeah. So, um, that was kind of nice because it, it can be isolating. Working on your own through some of these problems can be quite daunting. And, um, if you don't have somebody else going, oh yeah, well, we, we don't have any users either. And, oh yeah, things are breaking for us too. Um, I, it, it helps soften some of those pieces.

**SPEAKER_03:** Yeah. It's just, I guess, understanding that other people are going through the same thing and being able to walk in and talk to the YC guys, um, person in person and just go for a walk and chat about what's going on was incredibly helpful.

**Chris Gammell:** Um, so you guys are at YC you're, uh, you know, you got all spun up and everything. What about when you started taking it out into the world? I mean, so what was, what was the initial response? I mean, how have you seen it since and, and where do you guys see it going in the future?

**SPEAKER_03:** Yeah, sure. Uh, so when, when we first took it to the world was about, uh, it was about six months after YC. Um, and maybe a little less four months after YC. It was a fall, fall of 2011. Um, and like all naive founders, we thought that it was perfect. We thought we had done everything that we needed to do and it was all done. And, you know, we were gonna, we were gonna launch it and then go to the Caribbean and just wait for the paychecks. Right. My ties everywhere. And it was, and it was like, and, and I, I look back on it and, and I can hear the excuses that like we were telling each other about how done it was and how perfect it was. And like, and I can remember like all the things that didn't matter that are like the most important things in the world right now. And, and it just, and so, you know, like really nice, like good learning experience for us and all, you know, all of that kind of stuff. But, um, the general response was amazing. Like it was great for, for like a super half baked product. Um, you know, that, that was doing an interesting thing, but not doing it very well. The response was great. Um, you know, we got a ton of interest. Everybody thought, you know, what we were working on was really important and that was good. Um, and then usage was zero. Right. So like everybody sign up or show up or like poke around at and say, Oh, this is, you know, this is awesome. If only I needed something like this, or this is awesome. If only it worked.

**Dave Jones:** And if only it was fully formed, as Chris said before, right. If it does, if it's not a hundred percent people expect, and because an EDA tool is so critical, they expect it to work. Well, Dave, you know all about this, right?

**Chris Gammell:** You used to talk about when, when you had to use half baked, uh, Altium stuff as well, you know, just as development versions, it's, it's tough to use, right? It's because you expect certain, like if I had picked up a hammer and the head of the hammer's missing, it's like this thing, I'm not using this, right? It's like, that's just what you expect from your tools. You need your tools to be finished in order to use them properly. Yeah.

**SPEAKER_03:** And, and that was, that was what it was. Like we ran into that brick wall and I, you know, for a bunch of reasons, that was really great for us. Um, we knew, you know, like we knew what we had to do, but we also knew that it was a really, really long way away. Like that was kind of the reality check of how far we are. Um, we, you know, we looked at the bank balance and we had about a third as much money as we needed to get to what we thought it was going to take. Um, and, and that was like, that was without even baking in the fact that we were probably going to be way late on, on how long it was going to take us. And so we, I can, I can remember Steve, Mike, and I, like we, we had kind of a really sobering chat in November ish of 2011. And we sat down and it was like, okay, what do we, like, what do we do? Right. Cause like we got, I don't know, at that time we had maybe a hundred or $200,000 in the bank and it was like, so, you know, we can get, you know, four or five months out of this money and it's probably going to take us eight. Should we, should we go to Vegas? Should we, should we go? And it was like, what do you guys want to do? Do you want to be like, you know, do we port? Do we, you know, do we pivot? Do we become like a social gaming email bullshit startup? Like everybody else in the world? Oh man, he went there. Or do we, well, like, and we, we had the real, you know, do we call up all of our investors and ask for more money? Do we fold it up? Like give the money back and like start up, you know, start over, do something new. And we decided that the right move was for us to start working on layout and start working on simulation and start working on some of these things that we didn't have that we knew we needed. Um, and that we would figure it out.

**Dave Jones:** I can tell you now that you didn't need to, uh, do simulation.

**Chris Gammell:** I knew Dave was going to go there.

**Dave Jones:** PCB and schematic and yep. I wouldn't have spent a second on simulation, but Hey, that's just me.

**Chris Gammell:** Dave doesn't spend a second on simulation anyways.

**Dave Jones:** So, oh, well I do, but it's not an essential part of a functioning EDA tool in my opinion. Anyway, especially not at this level, you know,

**SPEAKER_03:** I think I'd agree with you, Dave on that one. We weren't, we didn't know at that time and we actually, and simulation is a funny one for us. One of the ways, one of the ways that we patched it, one of the ways that we made it work, um, and, and, and found the money to keep us alive was actually through a contract. Um, so the reason that we have simulation is that we, for a couple of semiconductor companies, we, we built a simulator and it had all, it had all the same properties as up ford, um, you know, it was in the cloud. It was collaborative, you know, it was multiplayer was, it was well distributed, all that kind of stuff, um, accessible over an API, but it was a simulator that ran in the cloud. And, and that, that brought in, uh, I don't know, maybe $30,000 worth of revenue. Um, that contract and that, and that kept us alive. It was, it, it, it bought us like a mark. Fair enough. It was, it was kind of one of those amazing blessings. And, and it's still like our simulation is still really half begged, but it, it kept the company alive. Okay. Fair cool. I want to defend simulation a little bit. Cause as its father. Yeah, exactly. Uh, so, so, so there's a little button in our, in our tool, which everyone thinks is simulation, but it's not like, that's like a one day add on to our simulation engine. And it doesn't work very well. And I apologize. Um, but like then the behind that, if you give us like a spice file, there's a really, really cool backend to it that if we never get around to building like an automated front end into the tool will be amazing.

**Dave Jones:** Got it. So you have to put, you have to know how to use it. It's not, you have to plug in that spice data into the backend manually to make it. Yes. Yeah. You have to give us the net list.

**SPEAKER_03:** We don't generate the net. So the weaknesses is the net list generation is terrible. Got it. And model generation is terrible for us.

**Chris Gammell:** Yeah. It's always tough with that kind of stuff in simulations anyways, you know, actually associating like, like I know Eagle pulls in like LT spice stuff, but then you have to still input all like, it doesn't actually, I don't think it actually does any associations between the part, the part type and the actual, uh, cat or spice file or I don't know.

**SPEAKER_03:** So I dream to solve that problem one day. I want you to put every like analog chip down and then we'll start talking about mixed signal, but every analog chip down and press simulate and it actually simulate what you want.

**Chris Gammell:** I wanted to do that. And then I wanted to actually simulate accurately and easily.

**Dave Jones:** There's companies like Altium that can't do it. Okay. Right. Their simulation tool sucks.

**Chris Gammell:** Well, that's the thing. It's easy. It's, it's easy to strap a spice engine on there. I mean, like spices is, is, has been around a long time, right? It's all text based and yeah, it's an open source. Yeah. And that's easy to bolt on there, but then the actual interfacing and doing it right. That's the tough part. But I think that, you know, some of the stuff you guys are doing, right. Kind of, kind of does feed into that. Well, like the, uh, like bill of materials stuff. I mean, so the actual association between, you know, what you're seeing on the page and then real stuff, right. Like a real actual, uh, unique part number, that's a difficult thing to do. And, and that's, that's what I, that's what I actually like about, about your tool is, is the ability to, to link that up on the backend to actually have these, you know, if I'm looking at an LM324, it's not just a generic one. It's the actual, it's actually the one from TI that is a dip part, right. I mean, like it's the actual part number and that, that kind of tied together.

**Dave Jones:** And that's the killer feature, right. In any modern EDA tool, that's where they're all going, you know, and they know it. That is, you know, that is the modern killer app for EDA is all that backend.

**SPEAKER_03:** The next step to that one that I'd really like, um, and that I certainly know we're working on is you put down the TI dip LM, you know, five, five, five, five, yeah. 324, whatever it is. Um, pick your, pick your chip. And then we can go and be like, well, the TI one's not orderable from where you're ordering the rest of your parts, but here are 10 equivalent parts from whoever else is making one. Would you like to order one of those instead?

**Chris Gammell:** Nope.

**Dave Jones:** And are you guys sucking, are you guys sucking this data automatically? Do you have agreements with the likes of DigiKey and Mouser and Element 14 and all those to suck in? Yeah. So we start up or are you just sneaking behind the scenes as what used to happen?

**SPEAKER_03:** It's a little bit of both. It's a little bit of both. Um, we, uh, we work very closely with Octopart, who's also a Y Combinator company. Um, and they, you know, uh, we, we, we, we beat them up as much as I think everybody else does for the data that they have and the quality of it. Um, but it's, it's, it's kind of the best publicly available API data that's out there. Um, and, and they're working to make it a lot better. And that's, that's a really good thing for both them and us. Um, but we also work with DigiKey and Arrow and Newark and Mouser, um, to get data more directly, um, from distributors. And then we're also working with the semiconductor guys. So we're working with TI and Freescale and a couple other, um, big semiconductor guys to get data directly from them. So it's, it's.

**Dave Jones:** As in pool data sheets directly.

**SPEAKER_03:** So more than data sheets. So like, uh, so not just the data sheets, but yeah, you got it. The, like the symbols, the footprints, the simulation models, the, like, give us the stuff that you used to generate the data sheet so that we can put it into our open source database. Let people collaborate on top of it and let people use it much more than anything else. So, so we're, we're kind of hitting it. We're hitting it from all angles and it's, it's, it's a messy problem and it's a, it's like a legitimate big data problem. Like you're talking about, you know, millions and millions of parts with, you know, some, sometimes tens, sometimes hundreds, sometimes even thousands of attributes. Um, you know, and some of those attributes are like a data sheet or a spice model and like they're not, they're not simple attributes. Right. So, um, so it's, it's a really big, messy problem. And then like, you want to de-duplicate all that data and you want to be able to do recommendations and alternates and all that kind of stuff. You want to have pricing information and you want that to be real time. And it's like, try and just like, it's a data management nightmare, but we, what I want is everyone to have the same format of data sheet. Yeah. So do we. Zach laughs at me every single time I say this, but it would be amazing.

**Chris Gammell:** It would be amazing. I agree.

**SPEAKER_03:** If, if that's the way it was.

**Chris Gammell:** So how's that, how's it going for you guys so far? Hey, Texas instruments. Hey, Intel. You know, let me tell you what you guys are doing wrong.

**Dave Jones:** I think you should have stuck with the pirate ship stuff. Yeah. Up further.

**Chris Gammell:** That's, that's our job is to tell these chip companies what they're doing wrong. And then they ignore us. You guys don't have to do this. It's fine.

**SPEAKER_03:** I don't mean that I think you should all have the same data sheet. Someday. Or I do. And they all say, yeah, they should all use our format. Someday. Someday it would be. So like, you know, one of, one of the dreams and it's, it's probably pretty far out, but one of the dreams is if you can build enough inertia just in both people and data and designs and, you know, all that kind of stuff. If you can have a place with enough inertia and, and it's both data and human inertia, like at some point those guys have to enter their data in Doppler instead of publishing PDF data sheets. And like, so if, if the total, like if the total flank, right, if the total guerrilla warfare run around flank of Up verder is better data sheets, like if that's all we accomplish, right, is that, is that data is a little bit more open and a little bit more public and a little bit easier to get and not in a stupid PDF, then I think we've done a really good thing.

**Dave Jones:** And it's someone else's money will spend. Yes. Yes.

**Chris Gammell:** Yes. See, I, I think that's, that's a, that's a very good call. The data, the data stuff is very important. And I, I'd be surprised if, if we don't actually start seeing that at these big companies, having people that are just kind of like the external data coordinator kind of thing, right? I mean, we see this, like, like I mentioned TI and, and, and Intel, right? Some of the big, biggest chip makers out there. I mean, they're all moving into open source, right? Intel just started the middle board. TI has been doing the BeagleBone and a couple others. And so I, I, I imagine that they see it's in their best interest. So I'm surprised that we don't actually hear about that yet, but maybe it is there behind the scenes and it's just kind of a latent thing, you know?

**SPEAKER_03:** So, so it is a little bit, it is a little bit. A couple of these guys have actually gone and, and figured out where the data came from in the first place and, and put it into some database inside of the company. And, and we've gotten onto a couple of calls lately that have been like super refreshing, right? It's like, we get onto a call with a semiconductor manufacturer and they say, yeah, we love, let me just dump the database and I'll email it over and you'll have everything you need. And it's like, what? I'm sorry. What?

**Chris Gammell:** Oh, just everything I wanted. That's fine. Okay. Yeah. Right.

**SPEAKER_03:** So it's happening, but like of the, of the 500 semiconductor manufacturers that matter and the like 25 that like really, really matter, you know, this is like 10%, right? It's like two or three of them. So it's, it's really early days.

**Chris Gammell:** Yeah. Well, keep fighting the good fights. We'll be, we'll be sitting over here drinking lemonade and loving it.

**Dave Jones:** Now the big, the big question is how do you shake the stigma of being a web based EDA tool?

**Chris Gammell:** Speaking of things we lob your way. Yeah. Since the inception. There's the hand grenade.

**Dave Jones:** It goes in because, well, yeah, quite frankly, you know, professional engineers like Chris, am I like, Chris is more into it now, but you know, we are very wary of web based being tied to the web. We just, you know, have this innate fear. You know what it is?

**Chris Gammell:** It's actually, it's just, everybody wants to make their boss happy, right? That's what it really comes down to. That's like what, I forget who was talking about that, but everybody wants to make their boss. I've never given a shit about my boss. Whatever. Yeah. You're an outlier, but everybody wants to make their boss happy, right? That's where your raise comes from. If I go to my boss, I know, and I say, look, look, this CAD tool is really great. I really want to use it. And then two months down the line, you know, our, our internet breaks or my computer, you know, something, something's wrong where I can't access it. It's not like that doesn't happen with CAD programs on my own computer, but it's just, it just is that stigma. Like Dave said, I mean, it's, you know, it's, I can't, I can't go to my boss and put my neck on the line for something that's so important. And, and so like, how do you get over that?

**Dave Jones:** Uh, so. And, sorry, may I quickly add in there that a lot of, you'd be surprised, a lot of engineering companies still do not allow internet on the desktop. I am not kidding. Yes. You know, there are. Yeah.

**SPEAKER_03:** Wow. So, so I've got, I've, I've got the very like polished, I tell it to PR type of bullshit people all day answer to this. And I'll give you that, but like Mikey, Mikey, Mikey spends most of his day on the phone with engineers fighting with this problem. So like, you know, you know, Mikey, you should chime in here with your answer. But like my, you know, like my two points on this, like really quick are like one, um, at some point it becomes more important, uh, to be able to collaborate and to be able to move faster and to be able to work with all of the other people in the ecosystem. And this, this happened in software a little bit and it took a long time. Like there was, there was a really long time where the right way to do software was like solid files, you know, on your desktop, you know, you maybe share them with your co-founder over like an, you know, a NAS or a, you know, an NFS share or whatever. Right. And we've moved to the world where it's way more important to use an open source library or, you know, some, something that's a whole lot of people have looked at and then glue it together and, and do that very collaboratively with your coworkers, even if that means doing it on the internet. Um, and you know, and, and, and I, I think there's a very good parallels between the value of software IP and the value of hardware IP. Um, like I, I, you know, I don't, there are some pieces of hardware that are probably worth more than some pieces of software and vice versa. But, um, so like there's that chunk of it too. Um, but then there's, there's also just the general transition towards the cloud and the fact that we've got a ton of people that spend every day trying to make sure that your files don't get broken into versus like how many guys at your workplace or on, you know, at home on your personal desktop computer are worried about the security of that computer. And like, you know, like it's very, very bad for us. If somebody gets somebody else's data inside of Upverger versus very, very bad for you. Right. So it's just like a, like we, we worry and, you know, care a lot about this problem and, you know, we encrypt and we compress and we use AWS and like, we're in all of the right places to try and address this. But that's the very like polished answer. That's like the, the, what we try to do corporately. But like Mikey, you talk, like you talk to engineers all the time. Tell like, what do you tell them? So I, wow. What do I actually tell them or what do we tell them for this?

**Chris Gammell:** We'll save some time here, man. Yeah. I mean, if someone listens to the show, they might call.

**SPEAKER_03:** So, so, so look, um, in, in most workplaces, somewhere along the line, you're using a SAS system of some kind, whether it's your contacts or your, you know, repo for your code or that there are, there are some that are completely locked down. But as it turns out, there aren't that many. Um, and electrical engineering is a little bit behind, but what we're like, as Zach said, so I go into that, we have a team of people and his, his polished one. Um, but the reality is, is that the internet's, you know, going to be, you know, I don't know if you've heard of it, but it's, it's going to be big. One of these days. Yes. Okay. Um, so, so the story I like to tell people and it kind of, this actually has very little to do with security, um, and the web, but I was talking to a guy, I forget what his name was. And he came, he came into the office and he was talking and he was at a hackathon that, that we sponsored, I think. And he hadn't heard of us before and he was using Eagle and his friend showed up and he said, look guys, you got, you got to try this up for her thing. And he's like, no, no, I'm in, I'm in hacking mode. And his friend's like, no, believe me, you got to try this up for her thing. And so he went online and he came to Toronto to come to the office to say hi after using it. And he came up to me and he's like, you know, we're doing this hackathon. And I sat down and I'm like, this is going to take me four or five hours to do, sat down and did the schematic in 10 minutes. And, and like, as things go, that's pretty awesome. And he was obviously doing something reasonably short. Like you're not talking an 18 month project, right? Yeah. This is a hackathon. But people need to try it out. And, and people are really busy trying to say, look, we can't do it because it's on the web and you're trying to make excuses. But if you go to your boss and say, look, it's going to take me a 10th of the time to build this and get it to market. I can assure you that they'll be talking really hard and thinking really hard about whether they're going to do that. Because the time, the amount of money it costs to have it, to employ your engineering team is huge.

**Chris Gammell:** Yeah. Yeah. That's a really good point. So what about the, so the back end of that then though? So, so I think that's, this is the point that we've always gotten to is the, you know, you guys have, have this very strong policy about, you know, that your data is yours and you're very open about that kind of stuff. But more of the, you know, even if it is 10 minutes or 10 days that I put into a project, you know, if I have it in KiCad, like I use, right? I know that in two weeks time, I can, I can go open it up and, and, and it's, it's still there. Right. Whereas, you know, if, if you guys shut down or yada, yada, yada, you know, like it's.

**Dave Jones:** You think that the pirate thing's a better idea and head in that direction. Yeah.

**Chris Gammell:** That, that would be, I might, I might.

**Dave Jones:** Then the whole thing implodes. So. And everyone's lost their data. Yeah.

**SPEAKER_03:** So, so I can, I can talk to that just a little bit. So when we, when we went through Y Combinator, one of our advisors. And so the way, the way YC works is they, they set you up with people who have gone through before and advisory group, people that you can call on, people that can help you. And we, we were very, very, very fortunate to get set up with Adam Wiggins from Heroku. Um, and so when we, when we launched the site, um, there was an initial, you know, initial very positive, but then there was like this 10% who were really passionate about the problem and passionate about the space and liked what we were working on. But we're really concerned about the bump in the night factor, right? Which is that we just disappear or that we fuck up something and we lose all the data on our servers or like all of that. Right. Um, and who owns the data, right? So they're going to enter all of this IP into this system. Like who owns that? Like, are, you know, are we going to take it and go and sell it in China? Like, you know, a bottom dollar or are we gonna, you know, like, are we going to try and honor the, you know, the value that people have put into that? And so I called up Adam and I said, Adam, what do I do? You must've had the same problem with Heroku when you guys launched. And he's like, we made a page. And so Heroku has a page of their promises to developers. Um, and, and we lifted it like verbatim and I'm like, I'm stealing it. Like I'm taking it. And so we stole the page verbatim and we posted it. And it's like, I think it's our promise. I think it's like upford.com slash our promise. And, and like, and you know, when we meant every word and I called up the lawyers and I like, and I said like, look, I'm posting this page. And I need you to update the terms of, of, of service so that this page is valid. Like I need, you know, like I, I, I don't want a world where, you know, people are using the product, they're bound to the terms of service. And then we've got this nice fluffy page, which helps us sell shit, but actually doesn't mean anything. So we're not happy. I think we got a visit from ours. Yeah. I think he came into the office and was like, really? So, so we have, so, so, you know, we fixed the terms of service and, you know, and then when Dropbox went through their whole debacle and, and, you know, we updated it again too, when that happened and GitHub went through a thing and we updated it again when that happened. So like, we've been really, really kind of responsive to all of this stuff happening in the ecosystem, but like on, just on, on, on the topic of, you know, where Mike, Steve and I stand on this, where the company stands on it, where our investors stand on it, where if I like, it's, we don't view it as IP that we necessarily own. It's, it's, we're, you know, we're a transit mechanism, right? It's IP that flows through us. It allows people to, to do things that they otherwise wouldn't be able to do. But we don't ever, we don't ever like sum up the value of the library or sum up the value of the repository. And it's like, yeah, cool. Let's go see how much we can get for this in like China. Um, like it's not, it's not ever really thought of like that. It, you know, it's not really an asset that we think of as portable. Like it, it only has value inside of Upburger and outside of that is, you know, it's just dead data. Um, so there's that side of it, but then there's, there's the, like, what happens if we go bump in the night factor? And Steve can talk about this. We've built a ton of systems just to, just to make sure that that never happens. We've tested them. Um, we've, we've gone bump in the night a couple of times and, and I don't think we've ever lost anything. Um, so like, so like it has happened. Like, I'm sure you meant not ever, right guys? Right, right, right. And, um, so like, so like there's that, but then there's also the fact that like we've, we've forward paid on our servers for a long time and, you know, and, and we have open formats and people can go download stuff. And like, if you ever, you know, like if you're ever worried, download your data, it comes in an open source file format. It's super documented. You can take that and turn it into anything. We also have an open source project on GitHub that will turn it into the formats that we're able to. And we're, you know, uh, half of our engineering team right now is working on taking more formats and turning them into Upburger and vice versa. And, you know, taking more Upburger and turning it into other people's formats. So, so like it's a, it's a really important thing for us.

**Chris Gammell:** That's good. I like that. So that's, that's a good answer.

**SPEAKER_01:** Yeah. So I, I mean, to, to, uh, on the kinds of things that Zach said about the data to us, we think that it only has a whole lot of value in Upburger. Um, it's not worth it for us to try and trap things in Upburger. Um, electrical engineering involves a lot of tools and we do have to play with other things. Um, and if we're not the right place for the work to happen, it totally makes sense for us to find ways for you to be able to get what is your data, um, and get it in a way that you can work with it. Um, there are a lot of tools that as part of the import export stuff that we're doing right now are incredibly hard to work with to try and actually get the things that you've put into it back out. Um, and that's, that's not something that we want to do. Um, if it makes more sense for you to go and work on a tool on your desktop, then go for it.

**Dave Jones:** Yeah, because that's one of the fears of engineers with their EDA tools as well. You know, you start with some simple designs and you're using Upverter and everything's working great. And then a design comes along, that's a showstopper, which Upverter just cannot handle.

**Chris Gammell:** I'm still waiting for that for a KiCad to be honest. Right.

**Dave Jones:** Yeah, exactly. Because you need this, you know, you need this 12 layer board with controlled impedance, blah, blah, blah, you know, or you need, you know, there's really something that the tool just can't handle or you find that, you know, nobody's tested it to the extreme limits before in terms of number of components and, and layers and complexity and all that sort of jazz. And, uh, that's the other fear. I mean, how do you handle that? What are your, you know, what's the biggest design for example? Like, you know, like I don't see anything on your website that's, uh, that shows you what the biggest design that somebody's worked on. Look, Hey, you can do a 12 layer board in Upverter and you can do this and that and with 10,000 parts.

**SPEAKER_01:** It's a little unfortunate that the, the biggest designs and the most impressive designs are private. Yeah. Yeah, exactly. Um, so, so it's stuff that we very much like to show off. Um, but it sounds like it's time for a design contest guys.

**Chris Gammell:** Yes. Yes. Yeah.

**SPEAKER_01:** Yes.

**Dave Jones:** It might be. So like the most complicated design wins.

**Chris Gammell:** Yeah.

**SPEAKER_03:** So, so yeah. So like Stevie said, there's, there's a lot of pretty cool stuff in there that's private. Like we're working with a couple of really big companies nowadays that have like hundreds or thousands of engineers. And so, you know, like I'll, I'll just float that out there as you can imagine the complexity. Um, if you've got a thousand engineers, some of it's probably pretty complex. Um, so you've got big companies like that using Upverter. We do. We do. And it's, it's a very recent development that's, that's in the last couple of months.

**Dave Jones:** I'm very surprised because I, well, because this comes down to where do you see your target market? Do you seriously think that you can win, you know, uh, be the tool at huge companies and actually replace the likes of Altium and Cadence and all that sort of stuff? Or do you go, well, we know that's not realistic, so we're not going to even bother aiming for that.

**SPEAKER_03:** So, so like the very, the very arrogant answer to that question is our target market. It is engineers. Um, and they, they, they come in all shapes and sizes and you know, some of them are in the basement and some of them are in big enterprises and a lot of them are in SMBs. Um, we know, we know that, that for the target market of engineers, um, we do collaboration, reuse, sharing, consumption, all, you know, all of, all of those words that we associate with our product, we do it better than anybody else by like orders of magnitude. Um, and so, you know, there's a data library collaboration kind of thing that we're very, very good at. Um, interoperability is a thing that we're historically been very bad at and we're trying to get good at. Um, and complexity is a thing that we've been very bad at historically and we're trying to get a little bit better at, but it's, it's lower on the priority list. So in terms of like, you know, in terms of how we view our market, we want to be the collaboration tool for all engineers, right? Like we want, we want to be that for everybody. Like, I don't care if, if the tool that you boot up on your desktop, when you get into work is Altium or Cadence or, you know, something really crazy and esoteric that like only you use, I don't care. Um, what I want to be for those users is, is collaboration. Um, I want to be reused. I want to be a data repository. I want to be where they work with other people. And that, you know, if, if that's all we were for all of those guys, then great. We've done, we've done our job. Um, for a lot of those users, we're also going to be the design tool that they use, but that's not a requirement. Like it was like Steve was saying, like, it's like tools, right? Like we don't want to sell, we don't want to sell the hammer that lets you do everything. Like that's not, that's not the goal, right? Like, like we're going to sell you a hammer. It's going to do a lot of things, but like every once in a while, you're going to need a screwdriver and you should go use a screwdriver. Like, I don't, I don't really want people trying to use the hammer to do things that a screwdriver is really good at. Um, so, but you know, like our, our equivalent of the screwdriver, the thing that we're really, really good at, which is really, really special focused is collaboration. So like, that's, that's like our big, big, big one that we care a lot about.

**Dave Jones:** Can you use your collaboration technology separate from your tool? So say if you're an Altium user, can they come to Upverter and go, right, I didn't give a toss about your CAD and I didn't give a toss about your PCB and schematic and simulator. All I want is your collaboration stuff. Can you plug that in to Altium?

**SPEAKER_03:** And so the answer today is kind of the, the, the answer, the answer that we're working towards is yes. So, um.

**Dave Jones:** Because I can see your future potentially being much bigger there than the tool itself, than the PCB and schematic tool itself.

**SPEAKER_03:** Yes. I think, yeah. Like GitHub is, right?

**Dave Jones:** It wouldn't surprise me at all if in five years time we find Upverter no longer even bothers offering a PCB and schematic tool. Or they just do for hobbyists or something like that. It's a.

**SPEAKER_01:** Yeah.

**Dave Jones:** Central hub for.

**SPEAKER_01:** So review is where we're starting on that right now.

**Dave Jones:** Right.

**SPEAKER_01:** Yeah. Um, and it's, it's an easier problem than some of the, uh, edits and allowing two people to sync directly together, but we're building in that direction.

**Chris Gammell:** Okay. I love, I love the, the review tool. Like honestly, when, when that came out, that was actually, that was the turning point for me. That's when I was said, that's when I was like, okay, I really need to give this a look. You know, obviously me and Dave may have said, uh, you know, uh, web based tool, yada, yada, yada. I'm sure you could go back in our archives and hear one or two.

**Dave Jones:** Well, it was just a web based tool. Right. And it was.

**Chris Gammell:** But honestly, the, the, the design, the design review tool, that is, that is a problem that was begging to be solved. And, and, you know, you guys are very well on the way to solving it, I think. And that, that is, that is very impressive. More so than, than the other like CAD or a web based, you know, like the schematic only tools, you know, when they were just doing that kind of stuff in the browser. It's like, okay, yeah, I like that, but I don't want to have to operate between the two. So that's kind of moving to what Dave's saying as well.

**Dave Jones:** Can you explain this, um, review tool? Cause I, I haven't used Upvert apart from just a quick play when we used it, when we talked about it way back. Can you guys explain this, uh, verification?

**SPEAKER_03:** Absolutely. Uh, Stevie, Stevie, get in on this. Steve built it.

**SPEAKER_01:** Oh, there you go. Sure. Um, so the, uh, where we're coming at from that, um, uh, we do code review, um, internally for all of our software stuff. Um, every, every line of code that gets written gets reviewed, um, cause it's easy to make mistakes. Um, and hardware review happens as well. Um, and the, uh, experience that we're used to going through that is that somebody prints out a PDF and passes it around and everybody gets their highlighter out and goes and highlights up the documents. Then you get in a conference room somewhere and try and merge all of the highlights together. And then you get that, yeah, one piece, that one piece of paper to the designer and have him reenter all of it. And you repeat this process a couple of times. And it's so frustrating that you've got these computerized tools and you, you have very powerful computers and you just can't use them for the review portion of it. Um, so, uh, the design review portions, uh, that we have, it's, it's ideally suited for the web. Um, it's someplace that multiple people can work on the single canonical review. You don't have that merge step. Everybody can see what's going on. And then even being able to see what's changed revision to revision, uh, is quite easy there too. So, um, you can start with a design in Upverter or you can import designs from other places.

**Dave Jones:** Um, that's where that was going to be my question. Can I import my Altium project in there and just use your verification? Absolutely. Your tool. Oh, absolutely. Cause I was going to say there is a startup, a separate startup right there. Just in that.

**SPEAKER_03:** Fucking sales guys. Um, so, so yes, uh, just further to that point, Dave, the number of separate startups that we've stumbled across building Upverter, like the number of different startups that we should be instead of just being one. It's insane. It's insane. But it's endless. Oh God. So, so Adam, and I talked about Adam earlier, but like when we, when we sat down with Adam, I don't know, we were like a week or two into YC. It was really early, but we sat down with Adam and Adam's like, it's really good to have a fertile ecosystem to be building in. Like it's really good to have a fertile problem space, but you got to pick one. And, and it's kind of been our perpetual problem of, of being in a world where so much is broken and, and having good ideas for how to fix it all. But, but just not like if I had a hundred times as many people, like we, we would still not be able to fix it all. So it's, it's, it's a big broken space, but, but yeah, totally, totally agree. It could be, it could be a problem all onto itself.

**Dave Jones:** Cool. Glad to know I'm not alone. In that thinking.

**Chris Gammell:** So what about the, I mean, so, so you get through the design review and, and like I said, that's one of my favorite things about this. You know, what about the, the backend or I noticed actually since the last time I was looked at when we did the review to get, or that, that activity tracker, that, that session, online design session thing. I didn't notice actually the ordering side of things where you can actually, it's like one click order now as well. Or what is that?

**SPEAKER_03:** Yeah, absolutely. Absolutely. Um, so we do, we work with partners to do a PCP, PCB, uh, manufacturing and we hook up with DigiKey, um, to do bomb ordering. So like you press order and we'll have it shipped to you. And, and we have this like neat slider and, and it took us a long time to figure this out and confuses everyone. So it is like my favorite feature that no one can figure out. Oh, it's the worst. It is the best and the worst, but, but you, there's like a long time versus like I want it as soon as possible. And, and the amount of money you pay is depending on how quickly you want it essentially. Yeah. So, so for most, for most, uh, circuit board manufacturing, the defining characteristic is actually like a turnaround time. Um, and, and not the complexity of the board or what geography it gets made in or anything like that. It's just like, you know, or even the number of holes or layers or anything. It's just how quick do you want it? Like if you want it tomorrow, it's going to cost a lot of money. If you want it in a week, it's going to be, you know, mediocrely priced. If you don't care when it shows up, like it's going to be cheap, but like, that's it. You can get a crazy, crazy complex board in two months for almost no money. Um, and so it's so, so, you know, and what Mike's talking about was our attempt at allowing users to tell us whether or not they were price sensitive or time sensitive. And, and, and that, that's, that's it. And so we gave them a slider and it's, it's, it's the slider of like, how much do you look like a business or how much do you look like a guy in your basement?

**Chris Gammell:** Right. Yeah. And so people can't see this too. It's at the, so you go down, uh, like find a finished project. Cause I actually don't have any finished projects, but if you go to the bottom of the bill of materials, like scroll over to the bottom, then there's an order button there. Yep.

**SPEAKER_03:** So that's, uh, and it actually, and it works really well. Um, it, for, for the users that have used it, it's, uh, you know, it's, it's still in early days of deployment, that feature, but it, um, but it, like we place, so whenever you place an order, we place between one and three orders with, with manufacturers, assemblers, and suppliers. Um, and we, we get everything drop shipped to the right places. Um, you know, if it needs to get assembled, everything goes to an assembler and they assemble it. If it doesn't, then you just get two boxes in the mail, right? You get a box with PCBs and you get a box with parts. Um, and, and that's, that's all it does. Huh.

**Chris Gammell:** And then I see you guys also offer, this is interesting too, because you offer design verification, parts verification, and then like you said, assembly, but then also you could be offered routing as like PCB layout as well. Right?

**SPEAKER_03:** Yeah. So that, that, um, that was an experiment, um, that we're, that we're continuing to run. And then it was an experiment into whether or not people wanted to just do a schematic and then pay to have a board that was laid out delivered. So, you know, like what, what would you pay to have a board auto routed if you knew that the router was not a computer, but a person?

**Chris Gammell:** So, so this is an interesting experiment. Yeah.

**SPEAKER_03:** So it's just, it's slow auto routing. We work with, um, we work with double E's in India to do the routing. Um, and, and so, you know, you pay for auto routing and they, you know, they route the board for you. Um, and, and they're, you know, they're, they're as good as a mediocre double E would be. So if you're less than, if you're less than or equal to that, right. You know, it saves you time, right. If you, if you're, you know, if you're better than that, maybe you want to check the board before it goes to manufacturing. It depends on, depends on how hard it is, but, um, but that's it. And it was, it was an experiment. Um, we've had very, very, very few users use it.

**Chris Gammell:** Yeah. So let me ask you about this then. Uh, so with, with, uh, you know, offering that kind of layout service like that, who is your target audience? I mean, is it, are you, are you looking to get software people? Is that kind of, so you're looking for software people that are interested in hardware or are you actually looking for?

**SPEAKER_03:** So a big, a big question we were trying to answer with that feature was, do we need to build an auto router? Um, no, and, and, and no, the answer is always no. Right.

**Dave Jones:** Right. Don't waste it. No. Rock solid. You know what the problem with that is?

**Chris Gammell:** It's a software engineer's wet dream to build an auto router, right? It's just, it's just like a math.

**SPEAKER_03:** Friends auto route. Exactly. That's right.

**Chris Gammell:** There's a good t-shirt right there.

**SPEAKER_03:** Yep. So, but, so, but that was, that was one of the things that we were trying to answer. And then another one is, is, so it's, it's funny. The market, the market of, of hardware has, has had a new entrant recently, which is people who know nothing about hardware, who, who can't work on a PCB, but who, who know at least what chips they want, right? They know what kind of functionality they want a board to have. They can probably hook up a schematic, but then they're super lost for the rest of the process. And, and so part of it was to see if Upverter was a good, you know, a good tool for that audience. Like our, our schematic tool is, is, is much, much more sophisticated than our layout tool. You know, our schematic tool competes with anybody's, um, our, you know, our layout tool still has some work to be done on it. Could we, you know, could we replace our layout tool with a button and, and a place to enter your credit card number? Like that was, that was really the big test on that. And the result? Uh, and the result has been minimal usage. Like the result has been not, not a lot of people are looking for that service or at least, sorry, I should qualify that. Not a lot of people who know what Upverter is and have invested time in using Upverter want that feature. So.

**Dave Jones:** So it may not be a definitive answer. Yeah.

**SPEAKER_03:** Yeah. Yeah.

**Dave Jones:** Right.

**SPEAKER_03:** I think we've also got it hidden away, um, a little ways. Yeah. You have to press the order button and most of the time people don't find out about it until after they've ordered their first port. Yes.

**Dave Jones:** So you guys don't go around advertising the fact that, Hey, if you know jack all about a PCB, then we're the tool for you. Yeah. It's a bad market, right?

**SPEAKER_03:** So it, you know, it. The know nothing, pet company. It's actually, it's, it's actually, it's so it's amazing. And I, I, I will jump in on that. So like, because of how we started and because of how we got to where we are today, one of the biggest things that we fight against with our marketing nowadays is the fact that we're associated with being a hobbyist tool. And we're associated with being a hobbyist tool because we launched the tool like a year after we started the company. And, and, and, you know, it wasn't because we wanted to be a hobbyist tool. It wasn't because like, that was the market that we set our sights on when we started the company. It was none of those things. It was, it was that we launched the company and it was a year old and it was Steve, Mike and I in a basement for most of that time. Right. So, you know, it looked like a hobbyist tool. It looked like three guys in a basement built it.

**Chris Gammell:** Well, it was free. I mean, I mean, nothing, nothing against that. Right. I mean, like, but it was free and that draws in a certain crowd.

**SPEAKER_03:** It does. And, and so, so it's funny. So like, so it's one of these marketing things that we contend with that we're like, we're trying to change the paradigm around design. We're trying to make it easier. But if you go tell them the world that like you got this crazy, easy engineering tool, like no engineer that thinks he's serious wants to use it. Right. It's like, I don't want easy. I want the hardest fucking tool in the world. Right. Cause I'm, cause I'm bad-ass and I'm an engineer. And that's like, that's what I am. And it's just so like, so, you know, like we tell people we have a better way and they're like, no, I want a harder way. Right. I want to be more intense. And it's why you wanted to do it in C. Right. Right. But it's, so it's a problem. And, and it's a thing we, it's a thing we run into a lot on, on our marketing.

**Dave Jones:** Yeah. Your competition wouldn't help in that respect. Cause no, correct me if I'm wrong, but almost, well, every, uh, web based.

**SPEAKER_01:** Yes.

**Dave Jones:** CAD tool. And there's a lot out there, be they schematic only or, you know, there's just like in the last two years, they've just exploded. It looks like every man, these dogs do it. Yes. A CAD web based tool startup. And, uh, and they're all, yeah. Hobbyist level. They're all, so that's the association. Oh, it's a web CAD tool. Yes. It must be for hobbyists. Oh yeah.

**Chris Gammell:** I came up with the acronym for that actually. I forgot what I, what's that? I forgot what it was yet. And I think it was like yet another browser based. Yes. Oh yeah. Yet another schematic tool on the web. Y A S T O T W. So it goes off the tongue.

**SPEAKER_03:** It's a, yeah. So like it's, it's a big problem is, is that we're associated with a market, which is generally pretty Mickey mouse, right? It's, it's a lot of, it's a lot of obvious stuff. It's not, you know, you can't do anything real, right? It's a toy. And, you know, and like most, actually most of our competitors that, that like, that's their tagline, right? Their tagline is it's not a toy. And it's like, and it's like, well, but it is. So it's, you know, it is, it is a big problem. And it's, so it's, it's the problem with tools. So like you build a, you build a new tool for almost any market. And, and because of the, because of the development path, you're going to be seen as a toy for a really long time. And so that's, that's a problem. But it's also, you know, it's the platform shift to the web. Like nothing real happens on the web, right? Like, well, you know, we're only just, we're only just entering the part of the part of the internet where actual real work gets done on the internet. So like that, you know, that's a big, like, how long is it taking Google docs? Right. So like Google docs versus word, that's been like a 10 year battle. So like, when, so, you know, so like, and, and, and now, you know, at, at Upverter, I think we probably use Google docs 90% of the time, but like that took a really long time, right? Like that was, yeah. So, you know, so there's a lot of stigma around web-based stuff and, and just that, that general development pattern. And, and it doesn't help that we have, so we have 25 competitors that I track. And I, you know, I track them on a regular basis and it used to be two, right? Like it was, you know, like we started the company three years ago and it was zero and, you know, about 18 months later, it was two. And then in the last 18 months it's gone to 25. And so there's a ton, there's a ton of energy, there's a ton of investment, there's a ton of people, there's a ton of stuff going on, but like, it's probably, you know, it's probably still three years away from a real market. Right. And that's like, that's the, like.

**Dave Jones:** I would think so. Right.

**SPEAKER_03:** And that's the really, really, really optimistic view. So, you know, so it's a problem. And, and they, you know, and they, they hurt us as much as they help us. Right. They, they make it a market that people are aware of, but they associate it with, you know, with, with the stuff that, you know, academics are building.

**Dave Jones:** It doesn't help the fact that they're like all entirely free tools as well. So you guys to essentially compete, have to have that free model. And by doing that, that sort of drags your brand down to their level. Yes.

**SPEAKER_03:** So it's, so I, I like the fact that we have it so that hobbyists can use it for free for open source hardware. Like that's a personal, like, I, I wish I like had this tool when I was doing things. I was building hardware. I wanted this tool and I couldn't afford to buy it at that time. Which is why we do it. Right. Like that, like that Steve, Mike and I, like we, you know, we, we wanted to build like radar for pirate ships. Right. Like we, it's not going to design itself. Right. We're hardware nerds. Like, and there was no way that we wanted to do that and pay money to somebody, you know, especially, especially if it was going to be like an open source public community kind of thing. Right. Like, you know, we understand that people build IP that they value and they want to keep private. And that's why we charge the money. But we also really understand that the only way the world gets better is through open source. And so anything we can do to encourage that to happen, it's amazing.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. So that's where you've drawn the line. You've differentiated your free product from your paid professional product in terms of one is you can only do open stuff on the free tool. Yes. And the professional tool is you can do all your private, much private stuff as you want.

**SPEAKER_03:** And so it's the same tool, right? So the tool's the same in both cases. Yeah. We don't, we don't limit you in terms of features or complexity or anything else. Like if you, if you want to build like a super badass server in your basement and you're willing to open source that with the world, like power to you, we will help you. We will do everything we can to empower you and we won't charge you a dime. But you know, if you're going to do that and you're going to keep it private from the rest of the community, we're going to charge you money.

**Dave Jones:** Yep. What, like, do you guys force people to use a particular open source license or how does that? Any license you want. Right. But then, but by default, all of, if you choose the free tool, all of your stuff is available for download. So it's, it's by anyone.

**SPEAKER_03:** We do not enforce the license. Yeah. So it's public, it's public, but we don't enforce the license. So the, the reason for that is we, we don't want to be like, uh, IP lawyers. Like that's not the play. The play is not like a guerrilla warfare attack to be IP lawyers. It's, so we give you an ability to express which license your content is under. I was going to say that's important. We don't, we don't actually enforce it or track it. Like if somebody forks your product and makes it private and then continues to develop on top of that, we don't actually do anything to stop them. And it's not, you know, it's not that we hate people doing public stuff or anything like that. It's just that the complexity problem of tracking that is impossible. Of course. It's just an impossible problem.

**Dave Jones:** No, I wouldn't bother. Yep. No, you can't do it.

**SPEAKER_01:** So I guess since we're on open source hardware, uh, segue.

**SPEAKER_03:** Um, what I'm really excited about is the idea, uh, of having hardware libraries. So the equivalent of what we have in software, but you can add your power supply into, into a design. You can just pick somebody else's power supply and stick it in. And there's 120 volts in one side and five volts out the other.

**Dave Jones:** Groan. Oh no. Altium tried this concept and it's just flawed. Why? Because, uh, the, the whole Altium idea behind this was that nobody would ever, you know, 99% of the market would never have to design anything custom ever again. You know, all you'd have to do is build these building blocks. Well, that's this, they were serious about this. Right. And, and then, you know, and then, you know, the majority of people would not have to design much custom. If anything, they choose all these blocks off and in the real world, it just leaves the crappy designs and, you know, it, it, it's not very practical in the real world. So I'm sorry.

**Chris Gammell:** I would agree. I would agree.

**Dave Jones:** Well, yep. Yep. There you go.

**SPEAKER_03:** He agrees. I don't. Well, I mean, I should argue it. So, but, so, so, but I think, think of, uh, you starting out into electronics. I did not have.

**Dave Jones:** Oh, that's totally different ballgame. Totally different ballgame.

**SPEAKER_03:** We're not going to go in and Lego together, uh, you know, uh, cell phone, right? Right. I'm not suggesting that. Wait a second. So, so actually, actually, actually, actually, actually, actually, I'm going to jump in on this one. So, um, uh, I was just like, yeah, full, full, no, no, no, no, no, no, no, no, no. Full stop. Full stop. It's not going to happen. Jack has strong opinions on this one. Yeah. So, so, so I, so I was on the phone, I was on the phone with TI the other day. And TI is like a super, super vertical business. Right. So like you've got the, you know, the guys that work on sensors don't talk to anybody else in the company. Right. The guys that work on processors saying like, and you just like in all of these crazy vertical, crazy, crazy vertical businesses. And so they do reference designs for all of their chips. And so if I'm doing a reference design for my chip, I have to figure out how to hook it up to power and hook it. And I got to go figure out from the TI catalog, what the chips that I have to hook this up to are. Right. So I like, I go flip it out of the chip and then I got to figure out what the reference design is. And I got to take that reference design. I got to drop it into my design. I got to tweak it as I see fit. And, and so I become a designer of all of these TI parts around the one at the core, around the one that I'm actually trying to hook up and build a reference design for. So like the very first use case that I see for what Mike's talking about and, and, and what Mike's talking about, like, I believe in ideologically, and I think we're going to get there and I don't know what that's going to look like, but you know, let's just, we'll just, we'll just put that out there. But in the short term, what it's going to look like is people inside of large companies that are working on designs or people that don't know what they don't know can drop in a reference design instead of a chip. And, and, and it's, it's just that it's that iteration speed. And I, you know, like, and we're not, you know, we're not giving anybody a guarantee that it's going to work or anything like that. What we're giving them is a guarantee that they're going to get a product out the door faster. And that might not work.

**Dave Jones:** I don't agree with product out the door. I agree. It's very useful.

**SPEAKER_03:** They'll get a prototype faster.

**Dave Jones:** They will get a prototype that they can play around with. That's what I agree with.

**SPEAKER_03:** And I think that's version one. And I don't like, and, and, and so like the experiment. So as, as much as the like Indian auto routers is an experiment that we're running, what Mike's talking about is another experiment that we're running into whether or not there is a parallel for software libraries inside of hardware. And, you know, the answer might be no, like the answer might be no, sorry, doesn't exist. But the answer also might be that, Hey, you just saved, you know, half of your design cycle.

**Chris Gammell:** So it's, it's, what's interesting about it is, is that obviously the free aspect of it, right? So we've talked, I think there was someone we talked about in the past on the show that was talking about like, okay, well you design a block and then you charge someone five bucks for it. Right. And it's like, as soon as you put a dollar transactional cost on that, that's no way. But, you know, if it's all open, you know, especially if it's vendor driven, right, where they're, they're already giving away these reference designs anyway. So I have to take this design and then pull it into my CAD software and, you know, like recreate it and there's potential for error, that kind of thing. All right. Yeah. I could, I could see that much more likely than, than, you know, someone trying to sell me an IP block. I don't know if that's what it was like in alternative, the selling stuff.

**SPEAKER_03:** Internally, we talked about a marketplace and I think, yeah. I think, noob. So, so it did, it did come up, but like, it was a pretty close, like it was a pretty short conversation between us. So the, like the, the logic on the marketplace side of things is, is, is if, if you give people a way to monetize work that they would otherwise not believe has value, you've done a very bad thing for the world. Right. Can you explain that more? So, so it's, it's this idea that I have to do a bunch of work to accomplish a goal. Most of that work is not special to me. Right. Most of that work could be open sourced with the world. Most of that work, if I didn't have, like if I could borrow somebody else's stuff, I would. Right. So this is, you know, this is, I'm building, I'm building open SSL, right. Or I'm building a web server or whatever. Right. The web server is not the important thing. That's not the thing that I did that I built that was special. Right. Especially at UpFerver. You know, like we've built a hundred and I don't know, we use a hundred pieces of open source, something like that to build our product. All right. So it's like, you know, and, and, and I saw this really, like I used to work for a telecommunications company. I was the signal integrity guy. That was what I did there. And, and our software team used hundreds of pieces of open source and our hardware team built, used zero. And most of what we built on the hardware team was not special. It was not things that we were the first person to build. It was not things that we even knew how to build. It wasn't things that we were the ones that knew the most about, but we had to build them. And those are all things that could have been open source. Those were all things that we could have given away. Um, and it would have made the world better. And not only that, if there were things that already existed in the world, there were things that we could have taken from. So, um, so when we talk about the marketplace problem, it's, it's, if, if you give people a way to sell something that they're going to do anyways, they're going to keep it private and they're going to offer it for sale. They're not going to give it away to the world, even though they should. And, and so you've taken this rising tide that was possible and you've killed it. Right. Like you put a drain pipe underneath. Yeah. And it's just like, and it was like, it was entirely possible for a bunch of people to not give a shit about this IP that they built and share it with the world and make the world better for everybody. But then you put a price tag on it. Right. And you, you made them choose the price of zero instead of forcing it to be zero. And, and that's a really bad thing. And, and it is so like, and that's our logic behind, like, that's why we don't have. So it's the same reason we don't have a marketplace for kits, right? It's the same reason we don't have a marketplace for people to design things inside of Upverter and then try and sell them. Right. Is we want people to go on to Upverter and find IP that is unrestricted, that they can take, that they can build on top of, that they can copy, that they can, you know, and, and, and we want them to attribute it back to the editor and we want good things to come out of that. Um, you know, it's not cause we're evil people that we do it, but it's just, it's, it's that idea that as soon as you can sell a kit on Upverter, you begin to lock up that IP that should have been free in the first place. And that's a really bad, that slows it all down.

**Dave Jones:** Do you have to, why if you're selling the kit, does it have to be locked up? Why can't you sell an open source hardware kit? This was somebody's question on Reddit, actually. DK Mac.

**SPEAKER_03:** So it doesn't, it doesn't from a manufacturing point of view. Um, but it's, it's where the money comes from in that question. So like our manufacturing service, um, we make about a 30% margin on for offering the service, but that's it. Like that's the only money. So if we were to, if we were to give people money for selling kits, um, like it would either come out of our cut or we would have to raise the price for the thing.

**Dave Jones:** And then you're, as soon as you're just the facilitator of the sale.

**SPEAKER_03:** Yes.

**Dave Jones:** Which is rather than, you know, you're like, like it has nothing to do with you, but you just have the ability there for people to.

**SPEAKER_03:** So, and that's what I'm talking about. When we become a facilitator of the sale, you've, you've, you've taken IP, which somebody otherwise would have posted publicly publicly on Upverter and, and they're now charging money for it.

**Dave Jones:** Um, no, but the information could still be available, but they've, but their particular collaboration and their particular design that includes all this open hardware stuff is where the value is.

**SPEAKER_03:** I, I, so, so I, I, I agree with you. Um, so I, I can, I can break down the mechanics of how it will work out, but it's one of those things where, so it's, it's open source and public on Upverter. They've got a price next to it. They get some cut of that price. So a user doesn't click the button. They click the download button. They upload it into a new repository. They, they order their own copy of it. Right. You know, they, they, they save themselves 20 bucks. The guy doesn't get any money. It's just, it's one of those mechanics that breaks down whatever way you slice it. And it's, it's not like, it's not that we don't want people to get paid for the work that they're doing. It's that we don't want them to not be public in exchange, in exchange for that, that profit for, you know, does that make sense? So like go post it on TV. It does. So go post it on TV.

**Dave Jones:** It's self-regulating. I think this sort of stuff is quite self-regulating in this free open source hardware. Mark, I mean, it comes down to one of the, one of the, you know, one of the unwritten rules I talk about is that you don't, you know, screw other people. And generally that's what happens.

**Chris Gammell:** Yeah, but then they become police people, right? I mean, they have to, they have to then police it. And it's, I, I, I, I am sorry with them, Dave. I think that's, I think they made the right call.

**SPEAKER_01:** So I think the stories that SparkFun tells about their, their experiences with open source are particularly telling of how that happens.

**Dave Jones:** In terms of the China copying their kits in three days.

**SPEAKER_01:** Yeah. Right. And just the, the frustrations that they have with that. Now, I, I very much appreciate what they're doing. I love SparkFun. They're fantastic. They, they are in a very, very difficult position and it is a constant uphill fight for them. I mean, they've got to stay on the edge or other people catch up.

**Chris Gammell:** Yeah.

**Dave Jones:** But they also have a very huge viable business. We're talking about a 15, $20 million turnover business or something. And they're going great guns and they survive because of their brand and because people like them and because of their value added services. I think the question is, if you were to break SparkFun. Those Chinese kits are not a threat. Yeah.

**SPEAKER_01:** Well, so if you were to break SparkFun up into the, so same size, but you were to break it up into say 200 individuals with kits, whether that could exist or not in the face of.

**Chris Gammell:** At the same, at the same level of 15 to 20 million distributed amongst 200,000 or 200 people you're saying. Yeah. Yeah. Yeah. That's an interesting question. Yeah. If you don't have the scale and the individual or and the brand name behind it, then do you have that same kind of power of market, right? I mean, that's. Okay. That's a bit.

**Dave Jones:** Well, it's interesting. I just think that there's, you know, the ability to offer that there and just let the market regulate itself. And you guys go, hey, we offer this ability to, you know, advertise and your kit or whatever. It's open source. And well, if you want to sell it, then you can.

**Chris Gammell:** I'm just impressed. They drew the line somewhere, Dave. I mean, they, they pull so much other stuff in there. You know, like a fair call. I won't beat them over the head. Layout. I won't beat them over the head for it. Yeah. Parts. No. So I can certainly understand. You finally found the line.

**SPEAKER_03:** I will dive in that, that, that a company that we're very close with, Tindy is doing a very, is doing a very good job of this, of allowing people to sell open source.

**Dave Jones:** Well, maybe you could tie into them and let them, like the data just flows into there and Bob's your uncle. Yes.

**SPEAKER_03:** And, and we, so, so Emil and I have, have talked about that at length and we're trying to figure out a good mechanic for that. But I, I think that, that might be what you're talking about is that, you know, uporder is a, you know, we're, we're a design tool and we're a workshop where you can get stuff ordered. But as soon as you want to store, you have to go to somebody else who runs the store.

**Dave Jones:** And that, that's a perfectly fine solution. Yeah.

**Chris Gammell:** Definitely.

**Dave Jones:** Absolutely.

**Chris Gammell:** And I think we'd be happy with that. Yeah.

**Dave Jones:** I think most people would be happy with that. So not a problem.

**SPEAKER_03:** And in addition, I think they're doing a very good job and I don't really want to build the tech to compete with somebody doing something good.

**Chris Gammell:** Right.

**Dave Jones:** Well, it's just another thing that requires your resources, right? The more things you try and, you know, the more things you try and bite off, the more you try and chew it once, the more strained your software resources are and you try and be a jack of all trades and, you know. Yeah. Yeah. That leads to problems. Only so many hours in the day.

**Chris Gammell:** And dollars in the bank.

**Dave Jones:** That's what I'm talking about, guys. No auto router. Yeah. Okay. No simulation. Just stick to the core stuff. Okay. Be the world's best online. You must resist the power of the dark side. There is something to be said for being the world's best X, you know, in this narrow little niche. So many companies fail. I won't name names. I'm out of them. I'm out of them. You know, try and be all things to all people. And it fails almost every time.

**Chris Gammell:** Yeah. Yeah. I really do like the fact that you guys, I mean, the focusing on sharing, that is your killer app for sure. I mean, like, you know, you guys said, your schematic tool is stronger than your layout tool. Well, you're working on both, obviously. But yeah, I mean, that is by far the killer app is the sharing. And then the backend stuff is coming up, I think, too. So that's what I'm excited about.

**Dave Jones:** As I said, in five years time, I can see them being more of that type of company than a CAD, EDA type company.

**Chris Gammell:** How do you guys feel about actual, I mean, you guys are tied into GitHub. At least you asked for my GitHub name and stuff. But what do you think about just storing crap on GitHub, like board files and stuff? Because I started doing that a lot lately.

**SPEAKER_03:** Yeah. So we know the GitHub guys quite well. Another of our mentors when we were going through the Y Combinator thing was actually the founders of GitHub. And we spent a lot of time with those guys trying to figure out, you know, what the difference between their world and our world was, what the difference, you know, between what should be in GitHub and what should be in OpTrader is. And we're good friends with them. Actually, a number of the people that we raised money from came from introductions from GitHub, which is kind of cool. So like, you know, we've got a good relationship with those guys. GitHub is incredibly good at linear text-based version control. Like that's what, you know, they've got an amazing front end built on top of the power of Git that is very good at those things. You know, OpTrader is very, very good at graph-based hardware type design file version and revision control. And so, you know, like not everything looks like either. But things that look like text-based linear version control problems should probably be in GitHub. Things that look like hardware should probably be in OpTrader. Things that, you know.

**Dave Jones:** Like, can you give examples?

**SPEAKER_03:** So schematics, layouts, you know, we're beginning to work on a broader set of the engineering world. But right now, schematics and layouts are the really big ones.

**Chris Gammell:** I can give a good example. Would be like, you guys actually track individual, because you're doing in the browser, you actually track individual, like, trace drawing between like, you know, resistor one and resistor two. Whereas when I actually do a capture in GitHub, it's going to be like, all right, I put down resistors one through ten and connected those all together because I don't want to track each individual one. But you guys actually track each individual thing.

**SPEAKER_03:** Yeah, you're also not going to be able to do like a merge or a diff in GitHub, right? Like, you're just going to, like, it's, you're doing version control, not source control in GitHub. Whereas, like, the parallel to source control in UpTrader is actually like, it's that action-based thing that you're talking about, right? Which is that you get, you get each snippet of a trace. You get each move of a part. You get each little change that everybody did. And you can take, you know, you can take that and diff it, merge it, figure out what people actually did. You can see what happened between versions instead of just picking a version and saying, I want version 27, right? Or I want to roll back to version 25, right? In UpTrader, you can actually see what all of that means. So you can do it very atomic and very, very, you know, individual revision based. So it's, you know, so like it's been built in a different way to solve a different problem. There are a lot of things that should still be stored in GitHub. But things that UpTrader is good at handling should obviously be stored in UpTrader.

**Dave Jones:** By the fact that you are logging, tracking, storing, recording every single movement the user makes, like you move a part one pixel, you know, in the schematic, you move a, you know, a part one pixel across or something like that. You guys track and record that. Does that, and in a large design, that could be millions of little, you know, and board layout and everything else. That could be millions of operations. Is that an issue in terms of storage of that amount of data?

**SPEAKER_01:** It's been an interesting challenge. It doesn't end up presenting a whole lot of problems, though. The little bits that you do, so the individual pokes and tweaks, end up getting all compressed down together into a single snapshot, right? The single state of the world right now.

**Dave Jones:** Oh, right. So you ultimately do a snapshot based thing.

**SPEAKER_01:** Oh, well, so yeah, we have the whole action stream and then to be able to work with it in a useful way, we have the state of the world right now. And that's what gets passed around.

**Chris Gammell:** Oh, interesting. Okay. So if I'm on state of the world 16, right, that only has the changes that I've done since state of the world 16, like loaded up, right? If I need to go back and see the changes of state of the world 15, then it's a whole different set of changes that actually progress me towards 16. Is that the idea?

**SPEAKER_01:** No, actually, the changes are from the last action, right? From the last click, here are the changes. But we can take that entire stream and merge it down into a single unit.

**Chris Gammell:** So does it, could I take a board that's completely finished and completely undo the entire thing and watch it be uncreated? Yes.

**SPEAKER_01:** Yep. You guys should make a video of that. On the project page, there is the timeline and you can play it backwards or forwards and see all of the little things, jump around. Like crisscross.

**Dave Jones:** By not only you, but other people who you are working on the same design with? Yes.

**SPEAKER_03:** Yeah. Or if it's public, anybody can go back and look at it.

**Dave Jones:** Right.

**SPEAKER_03:** So it's, so like, like Stevie was saying, so the, the snapshot is just like, it's, it's a data manageability thing. It's not actually a, it's not actually a feature of the tool. When you load up up further, you get your undo history from the last time you were editing. So like if the first thing you did, so you load up a project, the first thing you can do is a control Z and back up one action from the last time you loaded the tool. And, and that actually works. That's like a thing that you can do. Um, and so, so we've got your undo redo history for all the time.

**Dave Jones:** Excellent. We've been going for an hour and a half here guys. You've blown your amp hour. Do we have any, uh, last questions, Chris?

**Chris Gammell:** That's weird. Um.

**Dave Jones:** Because we only got the one question. Why did you phrase it like that? Oh, whatever.

**Chris Gammell:** I'm sorry, I don't remember what I said there. You're welcome. All right. All right. Um, you know, actually, do you guys have any stats on, uh, how much forking is actually happening here to, uh, to have another terribly phrased statement?

**SPEAKER_03:** It's, yeah, it's, it's, uh, it's tens of forks today, I think is what we're seeing. Um, okay. So, you know, for, for the last couple of years.

**Dave Jones:** And then what about how many, how many designs do you have? Yeah. How many total projects?

**SPEAKER_03:** 18,000, give or take.

**Dave Jones:** Wow. Wow. And over across how many users? What's the average users? It's like 11, 11 or 12,000 users. Right. So an average of like one ish, almost two, one ish, one point something projects.

**SPEAKER_03:** And it's, it's actually pretty chunky. Most of our users have one and then a couple have like a whole ton.

**Chris Gammell:** Yeah. Power distribution. Like Wikipedia. Of course.

**SPEAKER_01:** We also see a decent number of users, certainly in the last couple of months that don't have designs that they individually own. They're just there, uh, so that they can review other people's designs. Oh, okay.

**Chris Gammell:** Right. Yeah. And I bet that if that trend, like you said, is continuing with more people pulling in designs for reviews and stuff, that would definitely increase. Yeah. It's a good, uh...

**SPEAKER_01:** There are a lot of people that need to consume the design information that maybe don't need to be there as part of the composition.

**SPEAKER_03:** Yeah.

**SPEAKER_01:** Right.

**SPEAKER_03:** So there's also people working on the same project together. So one of them owns it. They have a team, uh, where one, the team owns it, but there are three or four people working on the project.

**Chris Gammell:** Yeah. Well, that's kind of like what, uh, Michael Ossman was talking about too, because he said, you know, for the HackRF stuff, it's like one per, or well, all the RF projects he does, one person does it and then they use GitHub for similarly pulling down designs and then reviewing them. And then, uh, they, they, I think they don't have the same kind of change mechanism, but at least for reviewing, you know, being able to see, look at this, this tag or this, uh, commit number. And that's, that's when you, that's how you review stuff. So it seems similar.

**Dave Jones:** Uh, do you have any stats on how many users can, can you see which users are just coming in to have a little play around with it and then bugger off and don't come back or yeah. And it's got any stats.

**SPEAKER_03:** It's a large percentage of our users. Yep. It's, uh.

**Dave Jones:** Right. Well, as you'd probably expect.

**SPEAKER_03:** So it's, it's, um, so one of the things that we did to try and facilitate that, cause we, we want users to be able to play with UpFurder and be able to get a feel for whether or not it does what they need, um, was, was we removed the requirement of being a user to using the editor. Um, so, so you can, you can use the editor as a guest nowadays. Um, so you can just go try it out. Like if you don't want to, like if you really don't want to give us your email address,

**Dave Jones:** sign up with your login and yeah. Right. You can just go kick the tires. That's very good.

**SPEAKER_03:** And actually, if somebody sends you a link to a public design, you can, you can load that design up. Um, you can't obviously edit their design, but you can load that design up and poke around inside of the editor environment. Um, you know, without making changes, without being a user. So we've, we've made a bunch of changes like that just to, just to facilitate that. We call them lurkers. Um, you know, facilitate the lurkers. Um, but it's, you know, it's, it is a large percentage of our user base, but it, it's, it's like any, uh, content network. Like we have a lot of parallels to, to most other content networks that there's a ton of people playing with stuff, um, you know, and not actually contributing back.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Do you, um, uh, who do you see as your major competitors at the moment? And where do you sit in the, I guess your market is the web based EDA tool market, right? Yeah.

**SPEAKER_03:** So I don't think that's who we're competing with. Right. Right.

**Dave Jones:** Right. Okay.

**SPEAKER_03:** So, um, so like we, we have, we have kind of three levels to that. So we compete with other collaboration tools, right? So, so GitHub, you know, so you put all your files in GitHub, uh, you know, you don't put them inside of anything. You just leave them in Dropbox or on an NFS server or, you know, or maybe you work alone. Right. So, you know, like, like we, we compete with, we compete with the old way of doing things, um, and with, and with other collaboration apps, which are less attuned to hardware. Um, we compete with other EDA software and that's as, that's as like an editor, right? So as a, as a content creation tool, we compete, you know, with other, with other content creation tools.

**Dave Jones:** Um, because that's what people are going to come in for. They're going to come in for your PCB and schematic and stay around. Yes. Yes.

**SPEAKER_03:** And that's, and that's where I would put, that's where I would put all of the other, that's where I'd put all of the other web-based tools is in that bracket.

**Dave Jones:** And that's where I'm saying, where do you stand in relation to the other online CAD tools? For example, ignoring the, the collaboration stuff, which you're very good at just in terms of the CAD. Yeah. Um, yeah.

**SPEAKER_03:** And so, and I will answer that just, um, the, the third bucket is as a data repository. Um, so it's, it's other places you can get data. Um, so, you know, so like Octopart for parts data, uh, uh, you know, DigiKey for parts data, uh, you know, and any of those other repository type things. Um, and then like in terms of how we compete with the other tools, uh, so the, the realer the tool, the better we do. Um, so like the, the realer, the editor capability or the realer, the collaboration, the better we compete. You know, if, if all you want to do is like a super simple, you know, RF, uh, you know, sorry, RC time delay, you know, simulation circuit lab, you know, do it, go for it. You know, they're, they're really, really, really good at that. Um, so like, you know, and, and they, you know, and, and I think, I don't know, they have 10 times as many users as us maybe. So like, and then, you know, they're, they're very, very good at RC circuits. Um, uh, the, you know, in, in terms of like the circuit site.io and the, you know, the other, the other actual like CAD tools, like where you would actually be able to lay out a circuit board or something like that. Um, I, I don't know numbers for most of the other guys, but just based on activity, um, you know, we're, we're maybe 10 or a hundred times more active than they are. Um, in terms of the big old desktop tools, like we, we don't make nearly the revenue that Altium makes. Um, you know, we're beginning to penetrate into Eagles market. Uh, you know, we, cadence is, is, is almost zero at this point. So, you know, like it's still really early days on, on the, you know, us versus desktop tools comparison. That was a very business answer. We're way better than Eagle.

**Dave Jones:** So did you guys, did you guys know Altium are going to come out with a low cost tool soon? Yes. Shortly. Yes. Yes. I think they're going to goof it up, but that's just my personal opinion.

**SPEAKER_03:** So I'm not sure the thing that's keeping people from using Altium is the cost.

**Dave Jones:** So I, Oh no, it certainly is.

**Chris Gammell:** It's the Australian-ness of it, isn't it? If that's what it is.

**Dave Jones:** No, they don't compete in the free, like, you know, they don't compete in the hobbyist, hacker, maker, one man band. I don't know if that, I also, they, they, they don't have a tool for that. Not paid.

**SPEAKER_03:** They do not. They don't, they don't have a tool that people pay money for. People certainly use it. Yeah. Yeah.

**Dave Jones:** Oh yeah. It's the de facto tool in China. Yes. But nobody buys it.

**SPEAKER_03:** Right. And that would, that would be, and I think that would be my argument for Altium across the board is, is that yes, some people pay a lot of money to use Altium. I'm not sure the price tag is what keeps the people who don't pay a lot of money from using Altium.

**Chris Gammell:** Right. Yeah. Hmm. So what about expansion for you guys going forwards? I mean, you guys, well, how about, how about for our audience? Are you hiring any project gurus, people that you need to come in and just build the, obviously you have a large contingency as your users, but you have maybe someone to build that 12 layer board.

**SPEAKER_03:** Yeah. So we, so we just actually, it's, it's, it's funny. You mentioned, we just hired our 12th guy. Um, and he's a, he's a double E. Um, and his whole job is to work with the community. Um, and, and, and just kind of generally support. We, we call the role customer success and it's like a super douche. It's like a super, I know, I know, right. It's like a super, it's a super douchebag title, but the, the, the job, like his job is to make our users more successful. Like if that's it. And if that means, if that means lay out a board for him, then he's going to lay out a board for him. If it means, you know, go enter a part in the library, he's going to go enter a part in the library. And so, so that's, you know, so, so we, we just hired him, but we're, we're looking for two more people right now. Um, and so that'll get us up to 14. Um, and then we'll probably. Two more to do one. So one software, one hardware. So the, the software is just, it's, it's, it's a reasonably generic software development role. And the hardware role is to support and work with Anand and the community at just, just helping our users and building cool shit.

**Dave Jones:** Right.

**SPEAKER_03:** Um, and so, so we're hiring for those two right now.

**Dave Jones:** And if people are interested, where can they send their? Jobs.

**SPEAKER_03:** Jobs at upvirtor.com.

**Dave Jones:** There you go. I'm sure you might get some. Cause we've had, we've had companies do this before on the show. Yeah. And they've been flooded. Yeah.

**Chris Gammell:** He had a whole bunch of people. So yeah, they've hired good people. You're welcome. Thank you. Thank you.

**Dave Jones:** No, no. Thank you. We don't charge. We've got a free and open source. That's awesome. Yeah.

**Chris Gammell:** That's awesome. We should fix that, Dave. Yeah, I know.

**Dave Jones:** We're not getting rich here, dude. I know. Right now. I know.

**Chris Gammell:** That's all right. We do it to talk to fun people. And it has been fun talking to you guys. Definitely keep up the good work. I like the sharing model, everything. That's definitely, you guys are doing a good job with that.

**Dave Jones:** And I'm going to have to actually try it for something.

**Chris Gammell:** I wouldn't hold your breath on that one, guys.

**SPEAKER_03:** Mike's going to make them. Mike's going to make them.

**Chris Gammell:** Mike's going to make them. Oh, yeah.

**Dave Jones:** We'll have a call, right? Like you said. I've been using Altium for 25 years. I'm a hard sell. Yeah, I bet.

**SPEAKER_03:** And we'll start you. We'll sell you off soft with design review. It's amazing. We'll get you in there. Okay. No problem.

**Chris Gammell:** That would be good for Dave to make videos with that. You know, like have the hangouts like we did. Yes. That would be a good thing.

**Dave Jones:** Well, see, a lot of people ask me that. Why don't you make a video on Altium or some other, you know, like tool that costs money? And I go, no, I'm only going to make videos on tools that have a free option. Right. You know, which you guys do. We do.

**SPEAKER_03:** And I'll just slide in here. Like what piece of software that's 25 years old can't be good, right? Right? Right? DOS. DOS, mate. Yeah. Cool. Go, Nick. Well, thank you so much for having us. This has been a lot of fun.

**Chris Gammell:** Yeah, it was great. It's great to have you guys on.

**SPEAKER_03:** Awesome show.

**Dave Jones:** Thanks a lot, guys. Thank you very much. It was a great insight into the whole startup thing again, which we love getting on here. We always get a slightly different perspective each time we do it. Yeah.

**Chris Gammell:** So everyone should check out Upverter.com and jobs at Upverter.com if you want to join the guys here. Thanks again, guys. Awesome.

**Dave Jones:** Thank you. Cheers. Thanks. All right, guys. See you. Bye. Bye. Bye.

**Dave Jones:** Bye.

**Speaker ?:** Bye. Bye. Bye. Bye. Bye. Bye. Bye. Bye. Thank you.
