---
episode: 177
title: Discussing Innovation and the Future with Mike Ossmann - Fiesty Festivus Futurology
url: https://theamphour.com/177-discussing-innovation-and-the-future-with-mike-ossmann-fiesty-festivus-futurology/
---

**SPEAKER_01:** This episode of the Amp Hour is brought to you by Contextual Electronics. Do you find yourself struggling to get started designing your own hardware? Do you understand some of the basics of electronic theory, but don't feel confident enough to start designing your own boards? Contextual Electronics is an eight-week program that teaches you how to combine the theory and the practical side of electronics into a finished product. You'll work with your peers to learn all about electronics design and PCB layout. To learn more about the course and to sign up for Session 1A starting in January of 2014, go to ContextualElectronics.com. This is the Amp Hour Podcast, recorded on December 23, 2013. Episode 177, Feisty Festivus Futurology.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Michael Ossman of Grayscott Gadgets. Woo-hoo! Mike, thanks for joining us again. Thanks for having me again. It's great to be here. It's a Festivus miracle that you're back. It is.

**SPEAKER_01:** Happy Festivus, everyone, by the way. Happy Festivus. It's the 23rd where me and Mike are, and Dave's celebrating Christmas Eve right now, but the time difference is no matter for Festivus. Festivus can expand into your entire year. It's a way of life, really.

**Dave Jones:** See, I can't believe I didn't know about this. Festivus.

**Chris Gammell:** Do you have your Festivus poll, Dave?

**Dave Jones:** I'm sure I can erect one out of multimeters or something like that.

**SPEAKER_01:** It's got to be aluminum. That's the key.

**Dave Jones:** Oh, right. It's got to be right. Okay. Right. Okay.

**Chris Gammell:** Should I sort something out? Something about the strength to weight ratio.

**SPEAKER_01:** Yeah. Right. Yeah, and so we'll be airing grievances later. That's obviously a Festivus tradition. We cannot be in the same place for the feats of strength where we would battle it out in the front yard, but if people haven't seen it.

**Chris Gammell:** I think we all know who would win.

**SPEAKER_01:** I got about like five inches on Dave, so I'm just saying, you know. I don't care how much he works out. All right.

**Dave Jones:** You're toast, dude.

**SPEAKER_01:** He's an old man. He's an old man. Look at this guy. Yeah.

**Dave Jones:** Oh, dearie.

**SPEAKER_01:** Well, Mike, welcome back, man. It's good to have you back. Thanks a lot. It's exciting to be here again.

**Dave Jones:** Obviously, nothing better to do being a nerd on Christmas Eve.

**Chris Gammell:** That is an excellent point.

**Dave Jones:** Well, it's not yet Christmas Eve yet, is it?

**Chris Gammell:** No, but it's close enough.

**Dave Jones:** It's close. Yeah.

**SPEAKER_01:** Are you guys taking – I mean, how much – I guess you guys are both self-employed, so it's a little different, but how much time are you taking off, I mean, as self-employed people?

**Dave Jones:** Me? I'm – well, I'm shooting a mailbag after this before I head to my Rello's Christmas Eve party, so I'm struggling to get that done, and I'll be back on Boxing Day probably.

**Chris Gammell:** Yeah. Yeah, about the same here, like maybe a day and a half off.

**Dave Jones:** Yep.

**SPEAKER_01:** See, I took like two weeks off, but yeah, I mean, I'm going to be working at home. It's just, you know, my second job effectively. Right. Yeah. Contextual Electronics launched. Right. That's all up and running.

**Dave Jones:** So, how long did that take from go to woe?

**SPEAKER_01:** Six months. Six months, right. Only six months, guys. Yeah.

**Dave Jones:** Yeah, but how many hundreds of videos have you shot? Yeah, like 150 or so. Wow. Yeah. Exactly. Yeah, wow. That's a lot.

**SPEAKER_01:** Yeah, so that's up and running, and people started signing up. It was surprising. I saw like an email I got, and I'm like, hey, someone actually signed up. This is awesome. All right. One. We got one. No, we got like 10 or 15 so far, so that's good.

**Dave Jones:** It reminds me of the Ghostbusters scene, you know. We got one! She rings the buzzer and I slide down the fire poles.

**SPEAKER_01:** Yeah, that sounds about right, yeah. I was running around my house like that yesterday. No fire pole yet, of course. All right. Yet. Yeah. Right, exactly.

**Dave Jones:** That is one of my dreams, is to own a house with a fire pole. I kid you not. I think I've mentioned this before on the show.

**SPEAKER_01:** I think you might have. I saw this amazing post of a guy, I think it was in the Netherlands. He took an old water tower and he converted it into a house. And the number one question was like, how did you not put a slide or a fire pole? Yeah. Or anything like that? I mean, if you've got any kind of height in your house, you have to do it. I know. Totally. As long as you don't hit like, what's it called? Terminal velocity on the pole. Terminal velocity coming down the pole, right? Yeah. I mean, Mike, you should do that all the way down the mountain, right? I mean, you're up in the mountains, right? Absolutely. Absolutely. Yeah. Like zipline or fireman pole or something. I should have a zipline. Yeah.

**Chris Gammell:** I really, actually, my lab has a little balcony. Oh. And it looks out across the street towards the soup shop. Wow. Where I go to lunch like all the time. Yeah. So, like, I keep thinking I should have a zipline there either for myself or for soup. Like, they could just send a bucket of soup over a pulley.

**SPEAKER_01:** Yeah, right. But they're, like, at a lower elevation, so it would have to be, like, rocket-propelled soup, right, to, like, kind of get back up the zipline. Yeah. No problem.

**Dave Jones:** Yeah. It'd be one of those rope-crawling robots, you know, that just has two wheels on it that actually pinch the rope and then just pulls us up and down the rope. Easy.

**SPEAKER_01:** There you go. I like it. Sounds like another Kickstarter project for you. Speaking of, how are your various Kickstarter projects going so far? Mine? I mean, I guess the latest one is 8HackRF, right?

**Chris Gammell:** Yeah. It's going pretty well. I'm a little behind on it, but I actually am, like, minutes of work away from releasing my design and manufacturing for the pilot run. Wow. So, that's exciting. And Dave's going like gangbusters, too. Yeah.

**Dave Jones:** Mine's well oversubscribed. And I risk getting into that, you know, the, what is it? The pit of doom? Pit of...

**SPEAKER_01:** Despair. Pit of despair.

**Dave Jones:** The pit of despair, yes. Where I've got to... Not quite, because this is my full-time job already. So, you know, it's not like... Right. So, that's not too bad. But from the aspect of, you know, having to buy certain rules. So, rules of components, for example. Like, if I sell 1,001 units, right? See, I don't care about the money. I'm just looking at the number of units I have to manufacture. Everyone's focusing on the money. Oh, you're going to hit 100,000. Who cares?

**SPEAKER_01:** Right.

**Dave Jones:** I don't care. I'm just looking at the number of units, right?

**SPEAKER_01:** And so, what are you at right now? What are you... Oh, 881.

**Dave Jones:** Oh, 880-something.

**SPEAKER_01:** But backers doesn't correlate, right? I mean, it's... People might buy two.

**Dave Jones:** No, it doesn't necessarily correlate. And because I'm now allowing multiple... You know, people can pay extra for multiple units. And Kickstarter doesn't support that. Right. Which is a pain in the ass. So, I'm actually unsure of exactly how many, unless I go in there and manually add them all up. I don't know. So, I've just got to, like, guesstimate. But anyway, if I have to manufacture... If I sell 1,000 of one of these things, then I have to buy an extra reel of 1,000 components at $4 a pop just to, you know, just to get that extra unit. Because these parts, you can't buy one-off. Oh, right. So, you know, they're just not in stock as a one-off quantity kind of thing. So, yeah.

**Chris Gammell:** Well, you're going to make some more and continue selling this design after Kickstarter, right?

**Dave Jones:** Oh, yeah. Yeah, exactly. I plan on making more. But, yeah, there's always that awkward, you know, number. Oh, look, I've got to, you know, buy a reel of, with, you know, 3,000 parts on it. But I'm only going to make 1,200 or 1,500 units, you know?

**SPEAKER_01:** Yeah.

**Dave Jones:** And it's... Yeah.

**SPEAKER_01:** That'd be an interesting business opportunity, too, if, like, someone came in and they said, okay, well, if one Kickstarter is successful at this, there's likely going to be other ones that are successful at this, right? So, you think about, like, that, how a lot of the Kickstarters have, like, a Bluetooth low-energy chip on it, right? It's like, you go out and you offer, you're like, all right, I'll buy all the reels of parts and I'll sell you, you know. So, basically, any other brokerage firm does it with electronic components. But it's, like, targeted towards Kickstarter, you know?

**Dave Jones:** Great. So, we can spam everyone like I got. I'm sure you got this, Mike, right? When you run a Kickstarter campaign, all the vultures, you start getting all these emails. Oh, yeah. I've got, like, you know, seven or eight of them already. And my campaign's still got a week left. And from, you know, companies offering, you know, to, you know, media exposure for your campaign to make it go gangbusters and all this sort of crap. And then people come in with, oh, the Kickstarter, telling you about how horrible the Kickstarter fulfillment tools are. So, we happen to offer this fantastic fulfillment tool because we went through the pain of Kickstarter. And so, you know, we know what it's like. And here we go. Just give us an extra percent or two of your, you know. The usual. Yeah. There's all these companies. And they just spam every single Kickstarter. I'm sure they spam them, right? I'm sure they, you know, there's far too many out there to go and deliberately target. So, they've probably got some tool that automatically harvests my contact details off the Kickstarter. Yeah. Exactly. Unbelievable.

**SPEAKER_01:** I guess it's a good one to have, right? It means, oh, you're too successful. Well, yeah.

**Dave Jones:** But, yeah, but as you were talking about, right, a lot of these people claim to have come from the, you know, they did a Kickstarter and had this horrible experience. And now they're offering a service to help others, you know, and they're doing it by way of spam, you know. Thank you very much. And I thinly veiled as a personal email.

**SPEAKER_01:** You should start another service that prevents spam for other Kickstarter people based on your experience. Yeah, that's a, and I only take half a percent, yeah. Genius. Exactly, yeah. It's a market at work, folks.

**Dave Jones:** So, you got hit with the same thing, Mike?

**Chris Gammell:** Oh, yeah. Backer management and manufacturing.

**Dave Jones:** Yep.

**Chris Gammell:** Those are probably the biggest ones.

**Dave Jones:** Yeah, yeah.

**SPEAKER_01:** See, now, you're interesting because you have a dual effect there, too, because you had a, you know, I guess it was earlier on with the Uber Tooth 1, but then you had a much higher level one later. Right. So, was there a different effect?

**Chris Gammell:** Oh, huge difference. Because Uber Tooth was almost three years ago. So, it was kind of in the early days of Kickstarter, and there wasn't as much, it wasn't as well known, there wasn't as much public exposure, and there weren't so many vultures around the whole thing.

**SPEAKER_01:** Yeah.

**Chris Gammell:** I did get one or two messages or emails occasionally, you know, one or two a week, maybe, during that time that were mostly related to manufacturing. Right. At the most, that's what I got, like, maybe one a week or so. Did you get the ones from China? Oh, yeah.

**SPEAKER_01:** The China ones where they're like, dear sir, I am Bluetooth, please send us files for Bluetooth.

**Dave Jones:** I am happy, one low company. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** We manufacture product.

**Chris Gammell:** But, yeah, when I did HackRF a couple years later, it was a world of difference, you know, it was ten times as much of that stuff. Huh. Yeah. And more specialized Kickstarter-related things. Yeah, right, right. It wasn't just, we'll help you manufacture, it was, we specialize in helping Kickstarter creators. Huh. Right.

**Dave Jones:** And tell me, how horrible is this Kickstarter survey slash fulfillment slash address management system going to be, or should I not ask?

**Chris Gammell:** So, I haven't really looked at it since the UberTooth days, really, because I haven't done a, I haven't actually collected shipping addresses for HackRF yet.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** Because there's really no point in collecting that stuff until you're ready to ship.

**Dave Jones:** Until the last minute, yeah, yeah. Of course.

**Chris Gammell:** Because otherwise, then you have to feel people's change of address and stuff like that. So, for the most part, back in the UberTooth days, it was pretty crude, but usable. So, you basically, you had the opportunity to give your backers a survey, which you could customize, so you could get them to answer whatever fields you need, like their address, for example.

**Dave Jones:** You would think that'd be like default given, like why you have to do it as a survey is beyond me. It's just nuts.

**Chris Gammell:** Right. And I'm not actually sure that's still the case. I think it is. Some things are different.

**Dave Jones:** Well, some people are, yeah. A lot of people have been emailing them and telling me that's the case, you know.

**Chris Gammell:** And it wasn't too bad. I mean, I had, I had to ship units for UberTooth and, you know, 500 is, is a lot.

**Dave Jones:** Yeah, but it's doable.

**Chris Gammell:** But it's doable, you know, it, I did use, I did use a, a postal service, a third party postal service application that, that I could like import a database full or a CSV file full of, and it would validate them all for me. And that, that was very helpful, but getting that software to work well was a completely different challenge.

**Dave Jones:** Right. Yep. So I've got a lot to look forward to. Yeah. Oh boy. As long as I can get all the addresses out into an Excel spreadsheet, I'm probably happy. You know, that's kind of, and, and then be able to sort them into, you know, how many, you know, who wants how many and, you know, what level they got and stuff like that.

**Chris Gammell:** So, yeah. And you're probably going to have a huge percentage of international.

**Dave Jones:** Oh, most of mine is international always. Oh, really? Oh yeah. All of mine is always like 90, 95% is international. Yeah.

**Chris Gammell:** Mine have, might have been like maybe 30 to 40% international.

**Dave Jones:** Yeah.

**Chris Gammell:** Cause you, you're in the States, right? That's the benefit of being in the States.

**Dave Jones:** Yeah. That's right. Like probably 30, 35% of my, uh, sales always come from the U S. You know, that's yeah.

**SPEAKER_01:** So enjoy hanging out at the post office in the new year, man. That's fine. Yeah, exactly. Yeah. That sucks.

**Dave Jones:** Well, I've, I've only promised to send the two, the first 200 personally. After that, all bets are off, you know? Oh yeah. So yeah. Yeah. Yeah. Boy. But once again, and one, you know, as I said, it kind of, you know, that pit of despair kind of thing, as you said, Michael, you know, 500 is probably, you know, in the ballpark of, you know, like something, something you just, it's not too hard to do yourself and it's probably not worthwhile paying someone to do and, and logistically handling it and manage them, managing them and all that. So you just end up doing it yourself. But when you get to say a thousand or, you know, 1500 or something like that, it's that awkward thing where it's, yeah, it's not quite enough for a mailing house to bend over backwards for you, but it's. Right.

**Chris Gammell:** But it's a heck of a lot of work to get all those shipments out.

**Dave Jones:** More than enough to do yourself. Yeah. Exactly. So yes. Anyway. Yeah. My experience with Kickstarter has not been good. No. So far. It's so inflexible. I tell you what, I, I, I just found out and just tweeted, of course, as I do, that they can't change your address. Sorry. They can't change your bank details after you launch the campaign.

**SPEAKER_01:** Yeah. It's weird. I kept trying to get Dave to like change it over to my bank account. He's like, no, I don't know why you would want to do that.

**Dave Jones:** And that's what I tried to do.

**SPEAKER_01:** Yeah.

**Dave Jones:** It's no. And they, they, they confirmed. I've now, I've now got a, um, one of my fans works for Kickstarter and he's one of the support people. So, you know, I get a bit more personalized service, I guess, than most, um, Kickstarter backers. No, he, he went and checked. And, and no, you, you, this, this system does not allow it. You cannot change your bank details. Well. After you launch that campaign. It's horrible.

**Chris Gammell:** I hope you have valid bank details. Yeah. Well, yeah, exactly.

**Dave Jones:** A lot of things. Well, because see, I'm switching come 1st of January. I'm now a proprietary limited company. I'm a corporation.

**SPEAKER_01:** Oh, he said it on the show now. Oh, he's a, yes. Dave is a business. I'm not a business man. I'm a business man. To quote Jay-Z. That's right, folks. I'm hip. At least I read hip things online. I have no idea who Jay-Z is. Oh, Jay, really?

**Dave Jones:** No, no idea. He's like the most popular rapper in the world.

**SPEAKER_01:** Come on.

**Dave Jones:** No, sorry. No, like I've heard of him, but no, I wouldn't know him if I sat on him. I'm going to send you some links for Christmas.

**SPEAKER_01:** I'm going to send you some links.

**Dave Jones:** All right.

**SPEAKER_01:** Listen to some new music. Yeah. But that's great. Yeah, you're a business now. That's great.

**Dave Jones:** Yeah. But it's all new bank accounts, and I can't change anything. It's ridiculous. Oh, whatever. You're fine. You're fine. You're a bloody Kickstarter.

**SPEAKER_01:** You'll be fine.

**Dave Jones:** And you can't even change that. Hang on. Here's another rant. You can't even. They don't even support line feeds, freaking line feeds, in the fields for the perks. You know the perks on the left-hand side, right? Yeah. Michael knows what I'm talking about, right?

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Like, you can't even put, like, can't even start a new line. The text just is one whole sentence. Like, it doesn't allow any formatting. It's ridiculous. What, are we back in bloody 1960s IBM mainframes?

**SPEAKER_01:** Sounds like it.

**Dave Jones:** Give me a break.

**SPEAKER_01:** You know, you're not there for the, you're there for the marketplace. You're not there for the technology. Yeah. And that's what it comes down to.

**Dave Jones:** Yeah. Yeah, but come on. You can't even format text. It just makes you look like you're illiterate. You know, you can't even type a sentence because there's no, it's just, pisses me off. Can't help it.

**SPEAKER_01:** We'll. Sorry.

**Dave Jones:** End rant.

**SPEAKER_01:** Yeah. You'll have to focus on the electronics instead, I guess.

**Dave Jones:** Anyway, that's how I've been.

**SPEAKER_01:** That's good, man.

**Dave Jones:** Yeah.

**SPEAKER_01:** Your business.

**Dave Jones:** I scored a whole heap of shit at auction.

**SPEAKER_01:** Oh, yeah. Oh, yeah. That was a fun video.

**Dave Jones:** Yeah. Yeah. And of course, everyone comes in and says. Did you say that or not? A lot.

**SPEAKER_01:** Yeah.

**Dave Jones:** No, I didn't say, but it's a lot. You know, people think I got this shit for nothing. You know? Yeah. It's no, I paid a lot of money and everyone's going, oh, give it all away. Give it all away. I need an oscilloscope, you know? No, no. No, thanks.

**SPEAKER_01:** Yeah, no, no. That was not a, it was not a, it's not a giveaway. Oh, that was a picture you posted.

**Dave Jones:** I might give the odd one away, but, you know, geez.

**Chris Gammell:** That's right. I saw that picture you posted with a whole bunch of scopes and stuff. Yep. Yeah.

**Dave Jones:** Yep. So, yeah, I thought I'd be getting a bargain, see, because it wasn't on eBay and it was on, you know, it was through like a car and truck dealer, right? Who, you know, you wouldn't think they would, you know, get test equipment surplus, but hey, this time they happen to. Yeah. And, yeah, they normally sell cars and trucks and, you know, and you have to pay to register to bid. So, I thought, oh, that'll keep a lot of the tire kickers away, you know? And so, but nah, nah, these things don't go cheap. So. Yeah.

**SPEAKER_01:** You know, that stuff never really interests me, though. Like the whole like arbitrage type of stuff. Like, I mean, like, yes, it is electronic stuff and you obviously have to have that knowledge of what, you know, what is worth it to bid on versus not worth it to bid on, you know, like being, obviously being able to evaluate, you know, if something's working or not, that's important, like you were showing in your video. But, yeah, it's so much shipping. So much of electronics and like all this business crap is all shipping. It's just like, you know, logistic stuff is just so annoying. I don't, I don't like it.

**Dave Jones:** And shit hit the fan when, when I told everyone, you know, look, I'll be putting this stuff on eBay, but sorry, I'm not shipping outside the country. It's too much hassle. And all hell broke loose.

**SPEAKER_01:** Yeah.

**Dave Jones:** I got abused from every, you know, from here to Timbuktu.

**SPEAKER_01:** Well, you shouldn't live in Timbuktu. Why don't you do it?

**Dave Jones:** Why don't you offer blah, blah, blah.

**SPEAKER_01:** Yeah.

**Dave Jones:** It's like, no, it's just, no, I've been there. I've been shipping shit for 20, more than 20 years. And I know a pain in the ass when I see one. It's like, no, if there's no market in Australia, sure, I'll, you know, I'll sell it internationally. But if I can sell it here, I will.

**SPEAKER_01:** So, yeah. So, Mike, is that how you, you, we were talking a little bit before the show about, about labs and stuff. And you said you, you had recently, you got a lab about the same time as Dave. Is that how you got a lot of your gears, like on eBay and stuff? Obviously not from Australia, because Dave wouldn't ship it to you.

**Chris Gammell:** Yeah. You know, I actually don't have that much gear. Oh. I have a. As an RF guy, really? I know. Isn't that crazy? I mean, and some of the gear that I have is on loan from, from DARPA funding my, my projects. Oh. And I'm going to have to replace it when my projects are over.

**Dave Jones:** So. No, you won't. They'll just forget about it. Oh. Yeah. You're not going to be something. I don't know about that.

**Chris Gammell:** Just a line item, right? Yeah. Whatever. Auditing? What auditing? So like my, my own personal gear that I have is very limited and like ancient stuff that I found on Craigslist or whatever. Yeah. Hmm.

**Dave Jones:** Well, you don't need much to do, you know, ultimately, you know, it's just that most of, you know, well, a good lot of us hand, my, my, my hands up, are just gear freaks. We just love getting shit and equipping our lab, even if we don't use it. You know, it's, it's a sickness.

**SPEAKER_01:** The dreamscaping of that one day when you'll need that. Right. Yeah, exactly.

**Dave Jones:** Yeah. That nano volt generator I've got. Yeah. I need to generate nano volts, you know.

**Chris Gammell:** Yeah. Why wouldn't you? So actually I really need to do some shopping around. I need my own spectrum analyzer that, you know, at least goes to at least six gigahertz and I, I could really use an RF signal generator that goes that high and a bunch of stuff.

**SPEAKER_01:** Yeah. Are you, uh, remind me. From the last time you were on the show. Did you do SBIR? Because we were, we were actually chatting about that last week. Oh, right.

**Chris Gammell:** No, I, I didn't. Uh, the, the, the projects that I've had externally funded have been funded by the DARPA cyber fast track program.

**SPEAKER_01:** And what's that?

**Dave Jones:** Um, and it, that sounds very Terminator like. Yeah. Totally. Skynet like. Yeah. Yeah.

**Chris Gammell:** The cyber eliminator program. DARPA is the defense advanced research project agency. Uh, it's a part of the, uh, of the department of defense in the U S and they fund all kinds of research and development, uh, primarily merit military focused, but, um, but some of it's pretty broadly focused and, uh, it's really the, the organization. I think it used to be ARPA, which was kind of the creator of the internet. Yeah. Um.

**SPEAKER_01:** ARPA E.

**Chris Gammell:** Yeah.

**SPEAKER_01:** So. Oh no, that's sorry. That's the energy side of it. Sorry. You're right. Oh, okay. Yeah.

**Chris Gammell:** So that's kind of their claim to fame historically. Uh, you know, that little thing, the internet. Um, and, um, there was a program, there is a program that it's coming to a close called cyber fast track that was specifically designed to fund smaller projects in the information security community that are run by individuals or small businesses. Oh. And, um, it was a very popular project or program, I should say, within the security community for the year and a half or so that it was running. And, um, they funded, I think over, over a hundred projects. And, uh, I had, I had three actually. Wow. One of which was the original development of hack RF before commercializing it. And that, that project is the DARPA part of that project is completed. Um, and I have two other projects, cyber fast track projects that are still active, which is why I still have test equipment. Right.

**SPEAKER_01:** That's why the auditors aren't breaking down your door and grabbing your signal generator or signal analyzer. Right. Uh, yeah, that's great, man. Are you allowed to, are you allowed to tell us what those are or is that kind of like it? Oh yeah, sure.

**Chris Gammell:** Well, and, um, the cyber fast track program, um, includes, I mean, some of the projects that they fund may be proprietary or even secret. Uh, but, but, but my projects that I proposed are entirely open source. Um, and that's one of the cool things about the project or the whole program from my perspective is that I was able to propose these projects and say, you know, uh, like for hack RF, for example, I, I basically went to DARPA and said, you know, I, I would like to build this fairly sophisticated software defined radio and I'd like to prototype it and I'd like to build 500 of them and give them away for free. And I would like it to entirely be open source and publish absolutely everything produced by this project. And I'd like you to pay for it. And they said, yes. Sweet suckers.

**SPEAKER_01:** No, that's, that's great. That's, that's kind of sucker around. Uh, yeah. The other one's the, uh, the Daikon. Is that one of the other ones? Daisho. Is that something? Daisho, sorry.

**Chris Gammell:** Yeah. Daisho, uh, that we talked about last time, uh, FPGA based platform for a high speed communication system. Yeah, that's right. Uh, that is, uh, also a DARPA cyber fast track project. And, um, that's how I'm able to pay for, um, the people. Several people who are helping me with that project. And, um, and then I have a third project that's more of a, uh, kind of a pure theoretical project, uh, relating to error correcting codes and data encoding.

**SPEAKER_01:** Ooh, eye diagrams. Is that the one or? No, no, it's not. What am I thinking of? You're thinking even lower layer.

**Chris Gammell:** Like I'm, I'm looking at like, um, maybe, uh, Mac layer encodings. Okay. So it's, it's a.

**SPEAKER_01:** Oh, ECC is the stuff with like, I've, that's, that's the one with like DRAM where if it's like a cosmic ray hits it and then you kind of check it against the checksum or something like that and weird shit. Right.

**Chris Gammell:** So I got into studying error correcting codes through my work in software defined radio. And I ended up having some ideas related to, uh, security, uh, communication systems that could be affected by your selection of error correcting code. Um, so it's, it's a very, uh, it's a very theoretical project that doesn't really relate directly to the, to the physical layer. Uh, but it's kind of that first layer of bits on top of the physical layer and how you encode data within those bits. Huh? That's cool.

**SPEAKER_01:** How's the, uh, how's the Dyshow going these days? So, so last time I saw Dyshow was when I was asking about the KiCADs stackup abilities, like how people did stackups for PCBs. And you referred me to, uh, I forget the person who's working on the Dyshow boards.

**Chris Gammell:** Uh, Jared Boone.

**SPEAKER_01:** Jared, right.

**Chris Gammell:** Yeah. Sharebrain Technologies. He's, he's the one, uh, he's done a lot of work for, for me. Uh, we've collaborated a lot on, on some of my projects and some of his projects and, and he's done work for me on the HackRF project and on Dyshow. Um, and he was the designer of the main board for Dyshow. Uh, so that, that was a, that was a beast of a board.

**SPEAKER_01:** Yeah, exactly. And that's exactly what I was going to say is that, so, uh, that actually inspired me for contextual electronics to put in a, a, an entire unit, a course unit about just kind of going out and looking at other people's, you know, because that's the nice thing about open source, right? He's like, you can, you can go and download this GitHub repo, pull it into your project. And I like, I opened it up and I'm just like, whoa, you know, it's an eight layer. It's this huge BGA part. And it's like all, I think it had like impedance matching for all the DRAM and stuff like that. Oh, it was, it was intense for, I mean, not, not for a lot of, I mean, like Dave, you're probably like, oh, whatever. No, yeah, no. Yeah. I used to do those times. It doesn't. Right. Exactly. But I mean, I was thinking for KiCat, I didn't even know a lot of that stuff was possible. Yeah.

**Chris Gammell:** It's not the kind of thing you find a lot of on GitHub. Right. Yeah, exactly.

**Dave Jones:** There's nothing wrong with KiCat. You can do the world's most complex board on there, but you know, there's no automated tools to help you. Right. Right. Exactly. That's the only difference.

**SPEAKER_01:** Yeah. Yeah. Right. And, and it, and it is supposed to be getting better. So one of the links we had on the, the show notes this week is I've actually been talking to the guys at CERN. Oh yeah. It's been, it's been crazy. Yeah. Uh, Javier, Javier, sorry. Uh, uh, from CERN, he's one of the guys that's been, uh, writing articles for E E Times and, uh, he's given some talks about it, but they had this great list of, of what they're actually planning on working on. Oh yeah. I saw that. Oh, H R W R.org, which is the, uh, the open hardware repository, but basically a whole list of, of stuff there. And then like, so obviously, you know, we've talked in the past about CERN getting into this, into the KiCad stuff. Uh, so there's a couple of interesting things here. First off, what they are planning is interesting. There's like 18 or 19 items about, you know, and a lot of them are low level things, but also, you know, in talking to them, I didn't realize that they're actually not, it's not anything official there yet. You know, they're kind of working on it to get it to that level where it's official. And that's, and that's interesting and also like, kind of like, oh, well, I thought it was already in the works, but. What do you, what do you mean by official?

**Dave Jones:** Yeah. I was going to say, how do you get official in the world of, you know, I think what it

**SPEAKER_01:** would be like if you, if you stop, if you stop buying licenses of other, other CAD programs, you know, that's when it's official, right?

**Chris Gammell:** Oh, you mean like official within CERN?

**SPEAKER_01:** Yeah. Okay. Exactly. Oh, right. Okay. Right. It's not their official tool. It's their tool of choice. Yeah. That's, and it probably is choice anyways, right? Because you're never going to force everyone in your, your, your organization. And another thing being that CERN is, is way bigger than I even knew. So, but you know, it's, it's, it's great. They're working on it. You know, the guys that are working on it is really cool. And this is a great list too of showing of a lot of the, the CAD. Obviously I have a very vested interest. Mike, you have a very vested interest in CAD. Yeah. Absolutely. So I'm, I'm really excited about this. And I told, I told those guys at CERN too, I'm like, you know, and we'll, we'll keep working on Dave, you know, we'll see someday, someday maybe.

**Dave Jones:** Well, it's, it's hard. You know, I've been using the same tool for 25 years. Right. And you know, like, and the other tools just can't touch it. Right. So like, you know, I mean, it's, it's, it's hard to make that break. It really is.

**SPEAKER_01:** It is. Right. And, and, and that's kind of the whole idea is like a lot of these suggestions here are, are a lot of the, the add-ons and the extra bits. Right. I mean, like I personally, I've only used Altium once or twice. I don't even know a lot of the things that are out there, but it's kind of like one of those things where you don't know you need it until you need it. Right. I mean, like, so like that Daisho board that, that Jared was working on has the impedance matching where it actually calculates the length that needs to be for this trace to get over to the, you know, to match, match impedances between differential lines and all that other stuff. Well, a lot of CAD packages, that's just, it's just built in. You say, okay, I'm going here to here, calculate it, and then do the little, the little squigglies. Right. But if it's... Serpentine traces. Yeah. Squigglies. That's what I said. Yeah. But I mean, you have to, if it's more manual than like Jared did, or there's scripting or something involved, that becomes more of a, you know, more of a process then instead of a... Right. Just a click and go.

**Chris Gammell:** Jared had a really cool process for that. Yeah. You know, within the limitations of what Kikad could do, he defined custom net classes. Oh, yeah. And so he assigned like, let's say he had 32 signals that he wanted to all be able to do. He assigned them all to a special net class. And then he wrote a script that would tell him, just like dump out on the command line, the length of every signal in that net class. So it was a semi-manual, semi-automated solution where he was using this script to measure his lines and then manually adding in the serpentine squigglies until they all matched up.

**SPEAKER_01:** Yeah. Right. Oh, so like a repetitive process where he kind of... Yeah. Yeah. Do it, check it, do it, check it.

**Chris Gammell:** But it was a lot faster than if he hadn't been able to automate that measurement part.

**SPEAKER_01:** Yeah. Right. Hmm. That's cool. But still, you know, that...

**Dave Jones:** I've done that in Altium before it had the, you know, real proper support for that sort of thing where it did it automatically. You know, I've... Yeah. It's sort of, you know, it could tell you the length of the trace and you just, you know, tweak it here and there and just, oh, shuffle it, just move. Oh, I need a couple of thousand more. I'll just, you know, drag this trace, you know, that way and stuff like that. So it was pretty easy.

**SPEAKER_01:** Oh, that's good. Yeah. The NetClasses stuff on KiCat is actually interesting because I didn't realize that's actually where a lot of the DRC stuff comes from as well. Mm-hmm. And it gives like those little guard band. I guess it's terrible to talk about versus showing it, but...

**Chris Gammell:** Personally, I haven't... Right. I haven't made good use of the NetClasses feature, I don't think. Yeah.

**SPEAKER_01:** I could send you a video. Yeah. Yeah. I should watch that. Yeah. Yeah, so...

**Dave Jones:** Chris, you can't just go giving it away.

**SPEAKER_01:** Oh, I can. I can do whatever the hell I want to, Dave. You can't just give your content away. I can do it. You do it, I can do it. All right?

**Dave Jones:** Yeah, but it's my business model. It's not your business model. Yeah, I know. I know.

**SPEAKER_01:** Speaking of...

**Dave Jones:** You're doomed never to make money on that venture. You just give it away. Ah, just, yeah, look, have a look. Yeah, whatever. No big deal. I'll just give it to you for free. Yeah. Yep. There's no friends in business.

**SPEAKER_01:** So, speaking of business and electronics and business models, did you see this kind of somewhat ridiculous article about Silicon Valley moving to Cleveland?

**Chris Gammell:** Moving to Cleveland.

**Dave Jones:** I haven't read it.

**SPEAKER_01:** So, someone who posted this, Thiliot posted this to our subreddit, but it kind of comes down to this interesting argument about what really defines innovation, right? I mean, so all of us are kind of in... We're not... None of us are in Silicon Valley, right? And some of our listeners probably are in Silicon Valley right now or Bay Area, whatever, or in other technology centers, you know, Research Triangle, New York, whatever, wherever these areas are. And it kind of comes to an interesting point about what really defines innovation in an area. And I ended up getting into it on Facebook with someone about, like, he's like, oh, this could never, ever happen outside of California. And, you know, it's just totally impossible that any innovation happens outside of California. And, of course, my red flag flies up. And I'm like, what are you talking about here? But, you know, but it's just about what actually defines innovation. And could all this stuff move to Cleveland in a day, right? If Google said, all right, well, we got a billion dollars. We're going to move everyone to Cleveland. We're willing to take the losses on the people that won't move to Cleveland. You know, even though they're not Detroit.

**Dave Jones:** Well, it's an interesting question. How do you define innovation? In the electronics industry, is it like, you know, guys like us, we're just using existing off-the-shelf parts to create new products. Is that defined as innovation? It depends on what level you want to define innovation as, you know? Whereas if you're developing new chips and techniques and technologies and process technologies and stuff like that, that's obviously innovation. But is this sort of stuff we're doing? Innovation? Just taking, you know, just designing a new, get a new idea, come up with a new product, but you're just using parts off, you know, from your local supplier? Yeah.

**SPEAKER_01:** Yeah, well, that's one aspect of it. I think the bigger thing, though, is it more about the network effect of like, okay, so you have, you know, say there's 10 people in Cleveland, there's 10 people in, you know, the hills of Colorado where Mike lives, and there's 10 people in Sydney where you live, Dave, right? And then there's 1,000 people in Silicon Valley, right? All interested in the exact same thing. I think the place with 1,000 people is going to have the net effect, right? But the question there is then, outside of that 1,000 people, what are some of the other benefits that are there? And I think the assertion that I have is that there are other interesting things that are there, you know, like mindset and everything else like that. But ultimately, it's all about the number of people there, and possibly also the money that's there.

**Chris Gammell:** Yeah.

**Dave Jones:** It's the back-in money, and stuff like that. But once again, it comes back to what sort of stuff you're working on. If you're just working on developing products that you just buy the parts from DigiKey or whatever, and you get your boards, and you know, you can do that anywhere in the world, right? There's no, you know, there's nothing unique to, you know, Silicon Valley that makes that easier. You're still going to order your chips from DigiKey, which comes from bloody, you know, whatever state there. North Dakota, yeah. Yeah.

**Chris Gammell:** I think instead of moving to Cleveland, Silicon Valley is moving to the internet. Right. Or the whole world. Yeah, exactly.

**SPEAKER_01:** Yeah, right.

**Dave Jones:** And then if you want to do production, well, you're going to, you know, most likely do it in China in 90% of the cases, right? So, you know, I mean, Silicon Valley, the only thing going for it is, as you said, you know, that networking and the availability of money and all these, you know, it seems every week there's a new sort of, you know, seminary type, you know, angel funding, investing, what's the word?

**SPEAKER_01:** Oh, like Accelerator? There you go.

**Dave Jones:** Yeah. Accelerator type conference, right? We don't even have those in Australia. They just don't exist for hardware.

**SPEAKER_01:** Right.

**Dave Jones:** Although there might be some news on that front soon, but I won't.

**SPEAKER_01:** Oh, yeah. Well, now we know there will be folks. But he can't say what it is. That's the secret. Ooh.

**Chris Gammell:** I think the article, the author of this article put Cleveland in the title just because he wanted it to be mentioned on the Amp Hour.

**SPEAKER_01:** That's probably, that's probably exactly what it was. Yeah. That must be it. Yeah. No, he mentions too, he mentions, you know, Buffalo, Pittsburgh, a lot of the other places where there's, you know, it's always based around strong university settings and stuff like that. And, you know, that's somewhat some of it. I think it's more, I mean, if I was going to create, pick a town or a place that was going to, you know, and the characteristics that had that, it would be people that are young, they're hungry, they're stupid. But then, you know, then there's other factors, right? There's people that are willing to, the fun to take risk on the young and the stupid, right? And the point I made is that, you know, like I compared it against like Rome, right? I mean, Rome used to be like this super advanced and it was the center of a lot of different things there, right? Like Silicon Valley was and still is in many ways, right? But eventually the weight of the institution ends up weighing it down, right? I mean, like, you know, if you have all, oh, Sand Hill Road, you have to go to Sand Hill Road. It's like, well, maybe you don't in the future, right? I mean, like maybe funding isn't that important anymore and all this other stuff. You know, eventually it stops being as important and it can get distributed away from these locations, right? And all of this really comes from this argument about really this whole article started because there's all this strife in Silicon Valley and San Francisco about the, you know, the cost of rent, right? That's really what it comes down to, which is its own silliness. But yeah, I mean, I think just-

**Dave Jones:** Well, is that a detriment? Because you have to, you're almost, because it's so expensive to do work there, you have to sort of take all this venture capital funding, sort of like a vicious circle.

**SPEAKER_01:** Oh, yeah, that's an interesting point. I mean, yeah, if you're going to pay your employees, you know, they have to live in the area and they don't want to commute for hours on end, then yeah, you do have to pay them more and that ends up driving your costs up. But then all the other costs, right? So now people, I mean, people are always the biggest expense in any kind of like startup type thing. But, you know, parts are another big one for hardware, right? So parts are the same cost in Silicon Valley as they are in Cleveland or Sydney or Colorado as well. Exactly. Yep. So yeah, it's an interesting point. We'll see. I mean, I think it's just kind of in its infancy because there's, because it, I mean, it's not like it's been like this for 50 years. It's more like 10 years, right? I mean, like DigiKeyMiles or all the online distributors have been like that for 10 years or so, right? And even China has only been, has only been manufacturing like they have for about 10 years or so in the capacity they have. Right. So I think it's going to, it's going to take a little bit longer to shake out, but.

**Chris Gammell:** Well, I think manufacturing is a really good point because I mean, didn't they used to manufacture a lot of stuff in the Silicon Valley? Yeah. Like back in the seventies.

**SPEAKER_01:** And. Yeah. Yeah. Last time I was in Silicon Valley, actually when Jeff Kaiser was driving me around Silicon Valley, he pointed, he pointed to like a bill, an office building. He's like, and that's where National Semiconductor used to be. And now it's a brown site. Right. Yeah.

**Dave Jones:** A brown site?

**SPEAKER_01:** What's it? It's a brown, brown field. It's a brown field. So it's like a. What's a brown field? A formal, former industrial chemical place that got the groundwater, the ground got contaminated and it got like classified. Ah, so it's abandoned now. Yeah. It's like a super, super fun site kind of thing.

**Dave Jones:** So you can't do anything on it anymore.

**SPEAKER_01:** I think they built an office building over top of it, but. Oh, okay. That's me. Right. But you wouldn't farm there. I'll tell you that.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Yeah. So I wonder if, if it's maybe once manufacturing leaves, is there just a long, slow decline that you would expect in a place like that?

**Dave Jones:** But it's coming back with all the talk of insuring, onsuring or resuring or whatever the term they want to use. I mean, a lot of it's coming back.

**Chris Gammell:** But are the people who are trying to build more manufacturing capacity in the US, are they doing that in high rent districts? Right.

**Speaker ?:** Yeah.

**Chris Gammell:** Right. Or are they doing it in like East Texas?

**SPEAKER_01:** Alabama or something. Right. Yeah. Low costs. No union states. I mean, I think, honestly, I think a lot of it still comes down to talent pools. Right. We talked about this last week with the silicon stuff. You know, a lot of the silicon, where silicon's made is still based around where a lot of the talent is. And, and because why, you wouldn't, you wouldn't build a fab in, you know, the Northwest Territory, or not Northwest, Yukon Territories up in Canada, right? Because first off, no one lives up there. And second off, even the people that do live up there, they're not silicon experts, right? I mean, you go where the talent is. Right. And, and I think that this ends up being the same argument.

**Dave Jones:** That's always the case because nobody wants, you know, nobody's in, in this white collar, you know, industry is that desperate for their job that they're willing to uproot and move their entire family and lifestyle.

**SPEAKER_01:** Right. Yeah. Well, and I think it's interesting too, because I mean, both of you guys, I mean, so Dave, you're, you're in the city at least, but I mean, Mike, you're out in the mountains. I mean, like you're working relatively remotely, right?

**Chris Gammell:** Yeah. I'm, I'm like a 50, 60 minute drive from downtown Denver. Yeah.

**Dave Jones:** Well, I am in the suburbs. I'm a 30 minute drive from the city. That's true.

**SPEAKER_01:** Sydney, Sydney traffic, right? Yeah. Yeah. But it ultimately comes down to like how, how close you're to an airport, right? If you need to actually travel to a business meeting, right? And if you're flying, you know, anywhere from three hours to 24 hours in Dave's case, you know, it's like, you know, that, that hour drive to the airport doesn't matter at that point. And so it's like, you know, at a certain point and plus with like Skype and Google Hangouts and everything else, it's like a lot of the stuff doesn't matter as much as it used to. Yeah. So it's more about who can, who can outfit, you know, in this case of hardware, it's who can outfit their lab, right? Like Mike's going through and Dave, obviously you've done a lot of that. You know, can you have the equipment you need and then can you interface with manufacturing in some way that actually allows your, your product to be made or, you know, can you find a talent locally that allows you to keep making whatever you're making?

**Dave Jones:** I think it all comes down to money as it always does. If you can get the money, you can do your thing anyway. And the talent, of course, money and talent. Money and talent. But, you know, usually if we're talking small startups, it's usually, you know, I can either a single person or a couple of people who are already sort of living and probably working in close proximity to each other, really. Squalor. So. Yeah. In their mom's basement. Yeah.

**Chris Gammell:** I mean, I'm growing my business to the point where I now have half a dozen contractors, one of whom is full time, but none of, none of us live in the same place. Hmm. And, you know, two of them are in different countries. And it's, I think it's a really exciting way to, to do things, to operate because I'm able to hire really whoever I want, no matter where they live in the world and they can work. They don't have to move. Um, and I can provide them work and hopefully in the longterm provide them, you know, sustained employment doing open source hardware and that kind of stuff. And, uh, um, you know, and of course I use contract manufacturers and I sell everything that I sell through resellers. So that's, you know, the retail side is kind of outsourced and the manufacturing is outsourced and I just get to focus on the technology and, and the people and getting people to do more fun projects.

**SPEAKER_01:** Yeah.

**Dave Jones:** And all of your smart businesses are doing that. I mean, you'd be an idiot, right? If you've got the funding and, you know, and you've got a, you know, you've got the people to do it, right? You'd be crazy to just, you know, pick up and move all of that to Silicon Valley because you think that's where the action is in quote marks, you know? I mean, why? What's the advantage? If you've got the money and you've got the people, if in this case, it could be, you know, people spread around the planet and if that works effectively, why would you, you know?

**SPEAKER_01:** Yeah. That's a great question.

**Dave Jones:** A lot of people, a lot of, a lot of companies do, a lot of startups think, oh yeah, we have to do that. We have to be embedded in the culture over there. It's bullshit. You know?

**SPEAKER_01:** So, you know, I feel like we should also stop and pause and say, we're not there. So maybe we don't understand something about it. Right. I mean, like, honestly.

**Dave Jones:** No, but it's just, it's just a distraction. I think if you've got the money and the people just head down, bum up, go and do your job.

**SPEAKER_01:** No, I think the people, the people in that case is really the big thing because it's like, I think a lot of people go there because it's like, well, I need the best talent. I need the brightest minds, that kind of thing. But I think increasingly, you know, we see this in the U.S. as like a, in a more general case, even outside of Silicon Valley, right? Like a lot of people used to immigrate to the United States to go to college and stuff like that. And they'd stay here and start companies and stuff like that. Now they're just going back to where they came from. And, you know, for better or worse, right? I mean, a lot of immigration policy and stuff in there as well that affects that. But, you know, that's a net negative, at least for the U.S., because then there's less people building companies here. And if you're local and you can get the talent locally, then that's, yeah, you're right. That's all that matters. Oh, sure. Yeah. It's just about, you know, if you feel like you need to get to Silicon Valley to get talent, then, okay, yeah, you'll go there and you'll fight for it and you'll reward people handsomely for it and hope they stick around. But, yeah, it's interesting. I mean, you guys are much closer to this than I am. So, I mean, Mike, you're building up. You got six people in now, you said? Yeah. Wow. But most of them... Dave won't even hire one. Most of them are...

**Dave Jones:** No, I don't even hire... Well, you know, techno, I've got, you know, contract assemblers and stuff like that. That's true, yeah. Yeah. I'm not in a position where I need contract designers or contract video editors or anything like that.

**SPEAKER_01:** Right, right, of course. Right.

**Dave Jones:** But it may eventually come to that, you know, a few years down the track. I may, you know, have so many projects on the boil that, you know...

**SPEAKER_01:** Hmm.

**Dave Jones:** I don't know.

**SPEAKER_01:** You should move to Cleveland, man. There's tons of good... Yeah, it's where all the action is. Yeah, it's all the action.

**Dave Jones:** Did you ever think that the person who wrote that article maybe picked Cleveland as a joke?

**SPEAKER_01:** That was my initial thought, yeah.

**Dave Jones:** Because it's like, what's the shittiest area I can possibly move into? No, he explains it. Hey, Cleveland! No, he explains it.

**SPEAKER_01:** He just says, you know, like Rust Belt cities, right? Like Cleveland and low cost...

**Dave Jones:** Rust Belt? What does that mean?

**SPEAKER_01:** Yeah, Rust Belt. So, like, people that, like, used to be steel manufacturers, like Buffalo... Right. Where I grew up. Pittsburgh, where I was born. Cleveland. I'm basically made of rust. But all of the old, like, industrial places that were based around, you know, waterways, right? So, like, the St. Louis Seaway that went down to the Great Lakes, and then there was all the shipping based on that. Right. Okay. And then, basically, it all went away when, I think, what, 70s, 80s kind of timeframe, and all these factories just rusted, and so did the people.

**Dave Jones:** Right, and everything was made in Japan and... Right.

**SPEAKER_01:** Exactly. Yep. Yeah. So, yeah. I don't know if you picked it for a comical reason, but... Right. It is fun to make fun of, isn't it, David? It is. Yeah.

**Dave Jones:** At least we're not Detroit.

**SPEAKER_01:** You know, you haven't been here, so don't make fun of it yet.

**Dave Jones:** No, all right. No. Yeah. Sorry. Well, you haven't been to Sydney. Is that our New Year's resolution?

**SPEAKER_01:** I don't know. 2014? Mike, you ever been out to Sydney? I have not. I haven't been to Australia yet. Oh, well. Might be the year, man. We should all have a powwow out in Sydney or something. It's so expensive. Oh, it's so expensive. Traveling out there.

**Dave Jones:** Did we mention that the Kickstarter idea we had? I don't know if we did. I don't know. Like, after a show a couple of months back, we had this idea that we would do a Kickstarter and just, you know, fund a road trip or something like that, you know?

**SPEAKER_01:** Yeah. Well, no, it was based on... So, you were talking... So, Dave always... So, Dave obviously has a young son, and it's a big time investment to fly... Oh, sure. For me and Mike to fly over to Australia or Australia to fly over to here, right? I mean, like, that's at least 30, 40 hours worth of time travel and... And not time travel, but travel. And, you know, just getting acclimated to the time difference. And so, Dave says he wants to stay for a couple weeks, and that makes sense. You want to be somewhere for a couple weeks to acclimate and be able to do that. Well, the whole idea was, if Dave's going to come here for a conference, he's not going to stay for two days. He wants to stay for a long time. No, yeah. And so, we were talking about, you know, renting an RV and basically driving around the whole western side of the states and, you know, doing a bunch of videos and...

**Chris Gammell:** Definitely. So, it was...

**SPEAKER_01:** Yeah, Amp Hour across America. That's right. Exactly. You know, we'll stop in Colorado, right? We'll drive the RV up to Mike's house and... You bet. Hang out in his lab.

**Dave Jones:** And then we had the argument whether or not we should get the manufacturers to fund it or something. And I go, look, we'll come and visit your fab if you, you know, we'll log your lab if you fund this part of the trip. That's right. Or something like that. Or whether or not we should keep the corporate whores out of it and get the viewers to back us. That would be us. And then we, you know, and then I suggested, well, you should come here and we'll do a road trip to Australia. And then you said, no, well, that's just, it just appears, you know, Chris bludgeoning a free ride to Australia. Exactly.

**SPEAKER_01:** Exactly. Yeah. What is there to see out there other than beautiful beaches, right? Yeah. The EV blog lab.

**Dave Jones:** No. Yeah. The expansive EV blog lab. Yeah. So, Mike, I want to... I haven't had anyone take my $2,500 option yet. Oh, no.

**SPEAKER_01:** Oh. On Kickstarter. Yeah.

**Dave Jones:** Pretty disappointed.

**SPEAKER_01:** There's still time. There's still a week, folks. There's still a week. It's true. Mike, I was going to ask you about, so you are pretty prolific with going to conferences and stuff like that. Yeah. What's on your plate for 2014?

**Chris Gammell:** Well, I'm definitely doing ShmooCon in January. And that's a... What is ShmooCon? ShmooCon is an information security conference in Washington, D.C. So, I actually have a talk there with Dominic Spill on our unambiguous encapsulation project, which is the error correcting code project that I was talking about earlier. And after that, I think my next firm thing is Troopers, which is a small conference in Heidelberg, Germany. And I'm teaching my SDR class there.

**SPEAKER_01:** Oh, is that the first one?

**Chris Gammell:** No. Well, I've done several. In fact, I've done classes at Troopers before. Oh, it's the videos. It's the videos that are new.

**SPEAKER_01:** The videos are the big ones, right?

**Chris Gammell:** And those are... I haven't done much work on those yet. Because I've... We'll talk after the recording. Well, I've been trying to get my design finished for Pack RF and get it manufactured. And so, now that I'm getting that out the door today, I'm hoping to have some more time over the next couple of weeks to get rolling on those videos.

**SPEAKER_01:** Cool. That's great, man. So, Troopers is... So, you're going to Germany? You're going to... You said D.C.? D.C., yeah.

**Chris Gammell:** Yeah? And then, you know, I haven't planned too much of the year yet, but I think I'm going to make it to Hamvention this year. Ooh, Dayton. Yeah, are you going to Dayton? Oh, okay.

**SPEAKER_01:** I don't know. If you're there, I might have to go. But... So, the problem is, Dayton, the Hamvention, them and Maker Faire are solidly chosen... They've chosen the exact same weekend. Yes. Each and every year. All right. So, I think it's like the second or third weekend of May. And, uh...

**Chris Gammell:** Last year, I didn't do either one because I had a third event on the same weekend.

**SPEAKER_01:** Oh, yeah. Okay. Well, uh... I have not decided which yet.

**Dave Jones:** Well, I've been invited to Hamvention. Oh.

**SPEAKER_01:** Yeah. Yeah.

**Dave Jones:** I have been invited to Hamvention.

**SPEAKER_01:** See, we could drive around the Midwest, Dave. I'm saying, you know, I got a Honda Civic that could... It could drive a little bit.

**Dave Jones:** You're the one who told me that I wouldn't like it. I shouldn't borrow it. I don't know. Mike, have you ever been to Hamvention before?

**SPEAKER_01:** I never have. Yeah.

**Chris Gammell:** Uh... The first, uh... The first amateur radio event I ever went to was in September, and it was a pretty small conference. Uh... The... The Digital Communications Conference.

**SPEAKER_01:** Oh, okay. Uh... Yeah. Hamvention... You know, I feel like part of it I might have missed out on. You know, I didn't do a lot of the... The conference-y... The talks and stuff like that. But, admittedly, I'm not very into Ham stuff still. Uh... So, there's that. It's, uh... You know, it's... It's... It's weird. It's weird. It's a weird culture kind of thing there. It's, you know, it's a lot of old guys. You know, like, a lot of old guys.

**Chris Gammell:** Yeah.

**SPEAKER_01:** And, uh... Greg was great. Greg Charvat was great to show me around out there. Oh, yeah. Him and all his buddies. Um... So, you know...

**Chris Gammell:** I had a really good time at the Digital Communications Conference, uh... In Seattle in September. It was only, um... I don't know, a little over 100 people. Like 150 people. Uh... Wow. Okay. But it was people who were focused on, uh... Digital Communications. And a lot of newer technology. Uh... So, people who are really innovating in the amateur radio community were there. And a lot of interesting talks. Really good discussions. Great people. Um... And, uh... Especially the... The taper... Or, sorry, tapper. The tapper folks, uh... Who were putting it on. Um... Mm-hmm. And they were the ones who really, um... Kind of convinced me to... To, uh... Put Hamvention on my calendar. Uh... So, I think I'm gonna go this year. The other thing that I'm really looking forward to this year is Tour Camp. Which... T-O-O-R Camp? Yes. Is that the one? Yes. Which is an every two years event. Um... Primary... Which is, uh... Put on by TourCon. Which is an information security conference. But Tour Camp kind of goes... Branches out beyond information security. There's a lot of hardware hacking. And, um... All kinds of fun stuff going on there.

**SPEAKER_01:** Is that like one of those ones like, uh... The... The... 29C3. I guess it'd be 30C3 this year. Where it's like they'd go and actually... Play with electronics out in the woods and stuff like that.

**Chris Gammell:** Yeah. Yeah. That's always so weird to me. 30C3 is coming up in a few days. Uh... But, uh... But they do, uh... That group and another group in Europe do a camp, uh... In the summers every other year. Huh. And so, uh...

**SPEAKER_01:** Yeah, camping plus electronics. I just never understood. I just never got it. It's a little strange, but... Yeah. It's a whole lot of fun. Yeah. Well, I mean, you go anyway... Like, again, with the employment side of things, right? It's all about the people, right? Mm-hmm. That's all that really matters. Exactly. And, and honestly, Maker Faire, too. It's all... Like, you know, like, a lot of it is... Some of it... Some... Or not a lot of it, but some of it's silly. But a lot of it is just, like, this huge concentration of people who are excited about the same things that you are. That is the reason to go to conferences and conventions and stuff like that. Absolutely.

**Chris Gammell:** And actually, a lot of the people... Like, all the people who do work for me are people that I've met at conferences. Oh, yeah? In fact, I think they have all been to tour camp in particular. Huh.

**SPEAKER_01:** So, go to tour camp, hunt Mike down, and give him your card, folks, and you will be able to... Or, you know, send him an email letter. Whiff like a dog. Yeah. Do you enjoy working on open source projects for no money?

**Dave Jones:** Then call now. 1-888. And you get a free used DARPA spectrum analyzer. That the goons will take back at any time.

**SPEAKER_01:** No, it's probably... It's good work. It's good work.

**Dave Jones:** Oh, boy.

**SPEAKER_01:** That's good travel, though. That's... You know, and it's weird, too. You know, I think you and I have talked about it offline before, about... It's interesting that a lot of the other fields that have a lot more conferences and stuff like that. I think about, you know, on the electronics side of things, there's... There used to be ESC, which is now... It used to be Design West, and I don't even know what it's called now. Yeah, I think it's still Design West. No, it was E-Live, maybe, or something like that. And then there's DesignCon, but then, like... Those are the two that I knew about. And then there's a bunch of, like, IEEE stuff. But that's kind of it. And then... But the IT security side of things, where a lot more people are getting into the hardware, it's interesting, but it's not... You know, it's not... It's more focused on the security side, and hardware is more of a... And here's how you do it.

**Chris Gammell:** Yeah, we have a great number and growing number of hardware neophytes in the security community. And, you know, we may not have as much experience, but we do have the benefit of getting together and sharing our knowledge a lot.

**SPEAKER_01:** Yeah, right. But that's powerful. That's really... That's important. So that's good. Dave, you should look for one of those out in Sydney, see if there's anything out there. And then Mike can go, too. I doubt it.

**Dave Jones:** Oh, no, yeah, there is... I bet, like, John Oxley would know about that kind of thing or something like that, right? Yeah, exactly. There was one in Canberra. It moves around. Yeah. There's a... Well, there's now a hardware contingent to this software conference. It's sort of like a spinoff. So, you know, all these... Yeah, because he was doing the LinuxCon thing or something like that, right? Yeah, LinuxCon is... Yeah, I think LinuxCon is... And there's a hardware aspect to that, which is getting quite big now. And it moves around the country every year. And, yep. Sounds good.

**Chris Gammell:** Yeah, there's also RuxCon in Melbourne. That's a security conference. RuxCon, like R-U-X? Yep. I haven't made it to RuxCon yet. But one of these years I will. I imagine. What is your...

**Dave Jones:** Is that a New Year's resolution?

**Chris Gammell:** Oh. Is he going to say it? No. Oh. Not because I don't want to go to RuxCon, but just because I don't make New Year's resolutions.

**SPEAKER_01:** Yeah. Yeah. My New Year's resolution is to get through the next year. Yeah. That's a pretty good one. Yeah. Yeah. Well, uh...

**Dave Jones:** Yeah, it's stupid, but as always, I've got plans. Yeah?

**SPEAKER_01:** What do you got planned, Dave? What is it?

**Dave Jones:** Oh, well, I want to clean up the shithole that is this lab. And, you know, and make it more manageable for me to... Make it more efficient and optimized for me to do my job. You know, like I want to have a dedicated photography bench, for example, where I can photograph stuff. I'm going to be getting, hopefully, a new video camera tool for teardowns. And stuff like that. I'm teeing up with a company to get me one of those. And, you know, so I'll have that dedicated and it'll have like a PC, dedicated PC with capture and everything else. And I can do live overlays, possibly, and all sorts of, you know, neat stuff like that. So, that's the idea. That's the plan.

**SPEAKER_01:** See, now, I always get caught up with that stuff when I'm like getting into the like, I guess the infrastructure side of things with like labs and stuff like that. It's so enticing because there's so much to be optimized. You know, it's like, oh, I could, you know, I could get this camera, that camera. I could do this lighting, that lighting. But ultimately, like, I got so deep into that when I started doing this contextual electronics stuff that it's like, it gets distracting at a certain point.

**Dave Jones:** Right.

**SPEAKER_01:** You know, like it can be really useful later on once you do get it set up. But it's like, I got so distracted with some of that stuff at first that it was very difficult for me. I'm sure that you've been doing the equipment stuff so long.

**Dave Jones:** Yeah. There's almost a pit of despair for setting up a lab and optimizing your process, isn't there? It's like, oh, it's too much effort to go to. But, you know, like so you end up not doing it or you do it half ass. You play around with it and dick around with it and you don't finish the job and properly put it in place. Yeah. Or you can go the whole hog and spend six months optimizing it. And then once you do, you're glad you did.

**SPEAKER_01:** Yeah. Well, I was even just saying, like, I just kept, I just kept like planning and planning and planning on doing this thing. And then it was like, oh, well, I should really just do the stuff that I want to use the lab for. You know, like, it's like. Right. I got to get past that planning stage or even the assembly stage.

**Dave Jones:** Well, what I want to do is try and, you know, add a bit more innovation to my videos. And also I want to produce more content on my blog as well, as in my, you know, text blog website. I want to produce some original content for that, not just video. Text. And stuff like that. How novel. Text. So 1960s. 1860s. And, you know. So anyway. Yeah. So I'll probably spend some of my Christmas break in quote marks, you know, cleaning up the lab and getting it ready for, you know, spending a bit more coin. Because there's always stuff to spend more money on.

**Dave Jones:** There's always more toys to spend money on. And, you know, get it a bit more set up, optimized. Because I'm sick of having, every time I've got to do something, I've got to sweep all the shit aside that I've, you know, that just builds up. And, you know, I've got to cobble things together to get things working. It's like, you know, like if I wanted to go do a live show now, I'd have to go cobble it all together. Right? I'd have to go, where's my freaking webcam? Where's this? Where's that? I'd have to go cobble it all together. Right.

**SPEAKER_01:** Well, it's just like lab setups, right? Where it's like if you have three oscilloscopes, you're in good shape, right? Because you can just keep them wherever you need them until the project's done. But if you have one oscilloscope, you need to move it from project to project and set it up. And that's a difficult situation to be in. So I guess it's the same for video, huh?

**Dave Jones:** It's the same for producing content. Yep. It really is. Because I've got different types of content. You know, I've got teardowns, mailbags. I've got stuff where I, you know, shoot soldering and things like that. And, you know, and it's just, yeah. And they all have their own unique sort of tools and ways of doing that efficiently. Yeah. So it's almost as if you have to have a separate setup to do it efficiently for each type of video that you do.

**SPEAKER_01:** Yeah.

**Dave Jones:** You know, and yeah, it's not easy. Like the photography bench, for example. You know, just photographing stuff, right? You've got to have the right light. You've got to have the right background. You've got to have, you know, everything. And by the time you dig around, oh, where's my camera? Where's my macro lens? Where's my lights? Where's my, you know? Yeah. It's just a pain in the ass. Whereas if you've got a dedicated area where you can do that, you can just take your board over. Right. I'm going to, you know, photograph this professionally. Snap, snap, snap. You know, it's got the, yeah, bang. And it automatically sends it via Wi-Fi and uploads to your Flickr account and, you know, sort of does all that sort of jazz. Automation porn. Yeah. Yeah.

**SPEAKER_01:** Yep. I think my resolution for 2014, Jesus, is going to be making more stuff move. Ah. I'm really digging the moving.

**Dave Jones:** The whole robot thing. Yeah.

**SPEAKER_01:** I mean, I'm not at robot level yet, but.

**Dave Jones:** No, but it's, you know, yeah, shit turning around. Yeah.

**SPEAKER_01:** Yeah, exactly. Making stuff turn over and over. Stuff that's been happening for thousands of years. Not thousands, but tens of years. Yeah. I think that's going to be my focus for 2014.

**Dave Jones:** No. It's been happening for thousands of years. Haven't you seen the anti, I can never pronounce it, the anti-thikura mechanism? Oh, right. The anti-tithura mechanism, you know? The computer, yeah. Yeah, the computer, you know, all those automator. I saw a documentary recently about, you know, the 17th and 18th, 19th century obsession with all this autonomous mechanical, you know, toys.

**Chris Gammell:** Right.

**Dave Jones:** And things. They were such works of art, you know? Fantastic. I'll try and find the name of that doco because it was really good.

**SPEAKER_01:** Yeah, I won't be doing that.

**Dave Jones:** So it's not just a recent invention. That's what I'm saying. No, I won't be doing that.

**SPEAKER_01:** I'm going to try and move stuff with, like, stepper motors and stuff like that, you know?

**Dave Jones:** Yeah, it's all bloody software these days.

**SPEAKER_01:** Yeah, that's another one. I've got to do that, too. Hopeless. Yeah. Oh, yeah. Well, we'll get there in 2014. Are we going to do any more shows this year, Dave? I don't even know. Are we supposed to...

**Dave Jones:** I don't know. We haven't talked about it, have we? No. We'll see how the holidays go. We don't.

**SPEAKER_01:** Yeah.

**Dave Jones:** Yep. It's the same thing with this radio show, right? I've got to cobble... Oh, where's my mic? You know? Oh, I've got to clear my bench. You know, every time I've got to move everything to put my mic down in front of me and get all set up for the show. And it's like, oh, man, I do this every week. You would think I'd have a... Yeah, you would think that. ...really nice sort of, yeah. Nah. We'll just cobble together.

**SPEAKER_01:** Maybe next year, man. Maybe next year.

**Dave Jones:** All right.

**SPEAKER_01:** You'll have your own recording booth. Yeah, exactly. Any other plans for 2014 other than HackRF type stuff?

**Chris Gammell:** Oh, you know, I've got tons of projects going, but one thing I'm looking forward to that I haven't even confirmed yet if I'm going to do, but usually at the end of February, I go to Fairbanks, Alaska and carve some ice for a few days. So that'll be a good time. What?

**SPEAKER_01:** Yeah.

**Chris Gammell:** What is that?

**SPEAKER_01:** Carved for like chainsaws? Yeah, yeah. At the World Ice Start Championships. Really?

**Chris Gammell:** That's really interesting. Yeah, I have a buddy who lives there and we were friends in college. And then in recent years, we took up ice carving and we do that usually every year, but last year we skipped it. So hopefully this year we'll do it. And, you know, for a few days, my Twitter feed will cease to be about anything technical and be only about how cold it is and, you know, the pictures of ice. Yeah, 100 pound block of ice that I dropped on my foot and stuff like that.

**SPEAKER_01:** What have you made in the past? I'm actually, this is really cool. I like that.

**Chris Gammell:** So we're kind of different in that, for one thing, we're not professional ice carvers, unlike many of the competitors. But the other thing that's different about us is that we try to build mechanical ice sculptures entirely out of ice. Well, there you go. You should make this into Thurkertra computer. Yeah, something like that. Our dream is to one day build a working clock entirely out of ice, but we haven't gotten that complicated yet.

**SPEAKER_01:** Oh, man. That's intense, man. That's really cool. So what have you built in the past?

**Chris Gammell:** So our best success, I would say, was a pair of penguins that we carved. And they were like seven foot tall penguins. And it was this piece that had two penguins facing each other. And one was realistic. And the other was mechanical, like a clockwork penguin. Oh, like a steampunk, but ice punk instead. Yeah, something like that. And it had a big key on the front of it, like a wind-up toy. And if you walked up to it and turned the key, it made the head bop up and down.

**SPEAKER_01:** Oh, wow. So it's like a cam action kind of ice sculpture. Exactly.

**Chris Gammell:** Just a real simple mechanism with like a single axle or two axles and a cam.

**SPEAKER_01:** Still, doing it with ice is insane. That's crazy, man. It is insane. But it's fun. It's a lot of fun. Yeah. That's really cool. Well, yeah.

**Dave Jones:** See, Chris, this is called having a hobby outside. Yeah, right, right. I used to play music, whatever.

**SPEAKER_01:** That's really cool. So, well, yeah, man, we'll keep an eye out for that. That's a cool idea.

**Chris Gammell:** Wow. So hopefully, maybe the show will convince my carving partner, Lars, that we should do it this year.

**SPEAKER_01:** Yeah, send it to him. Lars, if you guys should like carve a microchip or something like that, like a Sigma Delta. Yeah, huge triple five or something. That'd be awesome. There you go. Yeah, that's gold. That's like a good angle to it, right? Totally. Yeah.

**Chris Gammell:** Yeah. We have some friends who often do biological-themed sculptures. And so they've done a lot of like micro, like the scale of things, like you're looking in a microscope, you know? Yeah, right, right, right. But nobody's done the man-made technical side of that.

**SPEAKER_01:** Oh, there you go. Maybe we shouldn't send it to him. Well, make sure just Lars listens to it, not anyone else. All you Fairbanks, Alaska's listeners, just keep your yap shut. If you're into ice carving like Mike is. Yeah, that's cool. All right, guys. Well, we should probably call it. Yep. We're getting down towards holidays. Yeah, pal's well and truly up there. Yes, it is.

**Dave Jones:** And we're all busy nerds.

**SPEAKER_01:** Must get back to it. Yeah, right. Back to the grindstone. Yeah. So, Mike, thanks for being on again. Thank you, guys, for having me. Back to RF. Thank you. Excited about that. That'll be good. Dave, have a good Kickstarter. No worries. A good Kickstarter. Festivus. Good Kickstarter and Festivus activities out there.

**Dave Jones:** I'm obsessed with this Festivus now.

**SPEAKER_01:** Oh, yeah, yeah. He's going to be posting about it on Twitter in the next hour or so. I think so. Absolutely. You could totally get a Seinfeld episode in before you go to this party you need to go to, so. I know.

**Dave Jones:** I'm sure it's on YouTube.

**SPEAKER_01:** Oh, yeah. There's got to be YouTube something out there, so. Yeah.

**Dave Jones:** All right.

**SPEAKER_01:** All right, guys. Well, we'll see you in the new year. All right, guys. And happy holidays to everyone out there. You too.

**Dave Jones:** Sweet. Catch you next time.

**SPEAKER_01:** See ya.

**SPEAKER_01:** Bye.

**Speaker ?:** Bye. Bye.
