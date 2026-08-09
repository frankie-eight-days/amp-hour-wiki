---
episode: 154
title: Arduino, IndiGoGo and Hack-a-Day - Doodad Dealer Dancing
url: https://theamphour.com/the-amp-hour-154-doodad-dealer-dancing/
---

**Chris Gammell:** This episode of the Amp Hour is brought to you by NetBurner. Have you ever bought an embedded development kit that took a day or weeks to get to Hello World? Are there endless libraries requiring build after build? And do you find yourself banging on your desk, waiting for your application to compile and download, when all you want to do is test your code and get it out the door? NetBurner provides the easiest way to develop and deploy network-connected embedded devices. With a complete solution of hardware, software, and development tools, your prototype will be up and running in no time. For more info and a special listener offer, go to netburner.com slash theamphour. This is the Amp Hour Podcast. Recorded July 16th, 2013. Episode 154. Doodad. Dealer. Dancing.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life. What's up, nerd? Oh, I'm going to be... Hanging out with Amp Hour listeners without you.

**Dave Jones:** Yes. Heard about that. How dare you?

**Chris Gammell:** Well, sorry. You still have time to buy a ticket to New York City.

**Dave Jones:** Right, yeah. No worries. Sure I can swing that by the wife? Not a problem.

**Chris Gammell:** Yeah, just, you know, ask permission and hop on a plane and 40 short hours later...

**Dave Jones:** Well, I can just go and see you, honey. I'm going out for a bit, you know. Yeah. Just don't come a couple days. Yeah, exactly. I'm sure she won't even notice.

**Chris Gammell:** Yeah, exactly. Just tell her you're at the lab, right? 40, 50 hours flying later. Yeah. Yeah. Oh, that, right. Yeah.

**Dave Jones:** Call her up. Oh, it's a slight detour. Sorry. Yeah. Yeah.

**Chris Gammell:** We're going to be having a meet-up in New York City at a place called Swift Hibernian Lounge. I don't know what that means, but they have a place where we can hang out. They have food, they have beer, and they'll have a bunch of nerds influxing to their location.

**Dave Jones:** Have you got your own private room or something? No, just kind of like a back area. Or do you have to share it with the plebs?

**Chris Gammell:** Yeah, we have to share it with the plebs. All right. Yeah. The muggles. I'm not going to drop tons and tons of dough on a room when we can just kind of take over if there's enough people.

**Dave Jones:** Because you're already dropping tons and tons of dough on buying these stupid Google glasses and your plane ticket to New York, right?

**Chris Gammell:** Yeah. And I do have to say up front, I won't. So anyone who does show up and they ask me, I'm not going to actually have Google Glass. So if that's what you're going to expect, don't even bother. Ah, right. There you go. So that's the next day.

**Dave Jones:** No one's going to turn up now.

**Chris Gammell:** I know. Yeah. It's just me and other Amp Hour listeners. So sorry to disappoint in advance, but I don't know. Come have a beer. We'll toast Dave's distant memory. Not because he'll be dead or anything, but because he's very far away. Right. Oh.

**Dave Jones:** Goodness gracious.

**Chris Gammell:** Yeah. And we will be having a listening session as well. A what? A listening session. Like a CD release party or an album release party. We'll have that, except it will just be two hours of us laughing. Right. Did you know what I'm talking about? So there was this.

**Dave Jones:** Oh, the, yeah, you've done four minutes worth of laughing.

**Chris Gammell:** That actually wasn't me. It wasn't me, but it was. Oh, really?

**Dave Jones:** Oh, all right.

**Chris Gammell:** Somebody else mixed that, did they? Yeah. So I had posted, last week I had posted the Amp Hour minus the Amp Hour. It was just, I took it out of context where it was just Dave on one track and it was just me on another and just Jeff on another with just taking all the silence out and then, uh, uh, yeah. Oh, I forgot his name already. Sorry. Uh, Kai, I think he, uh, he, uh, actually did the hard work of cutting us all together and it's super, super, super creepy because it's just, it's just laughing too.

**Dave Jones:** You would think it was done in one take.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, it's yeah. Yeah.

**Chris Gammell:** It sounds like we're tripping balls basically. Um, but no, it was just a fancy editing.

**Dave Jones:** And there's some, uh, Kaiser in there as well.

**Chris Gammell:** Oh yeah. Yeah. Jeff's in there too.

**Dave Jones:** Jeez.

**Chris Gammell:** We haven't had him on for a long time, have we? The old third wheel. I know. Well, I've been trying to. Mr. I've, I've got a fancy job at Valve. I'm calling you out, Jeff Kaiser. I don't have time for the plebs anymore. Yeah. You know, it's tough because it's like, because time, time differences are a tough thing. It's tough for any organization, right? We are an organization, Dave. And, uh, when we, we should, we should see if he can come on now. We're, we're starting so late tonight, but, uh, yeah. Yeah. I mean, usually we're, we're starting, you know, where he's still at work because they work pretty late anyways. So it's a, yeah. What are you going to do?

**Dave Jones:** Oh, well. We'll get him on one day. Yeah, we'll get there. Shall we actually get onto some real news and crap? Because that's our slogan, right? Keep current.

**Chris Gammell:** Keep current, yeah.

**Dave Jones:** That's our tagline. Keep current.

**Chris Gammell:** Yes.

**Dave Jones:** The tagline, yes. Right. We don't really have a slogan, do we?

**Chris Gammell:** No. I don't know what the difference is.

**Dave Jones:** No. Neither do I. I don't know.

**Chris Gammell:** Yeah, we should, we should move on with, uh, we've gotten through the news, I guess, right? Not really. No? It's more news.

**Dave Jones:** Oh, we've gotten through the, the amp hour news. Right.

**Chris Gammell:** Right. Yeah. This show's gone well so far. Yeah. Oh, yeah.

**Dave Jones:** Well, the, this one got voted up the highest. I, uh, no, not, not, not quite. No. No, there's two more. Sorry, I haven't even sorted my Reddit things by, um, popularity. Yeah. Top. But anyway, one of the ones that get right up there, we'll get down the way, um, Hackaday. Yes.

**Chris Gammell:** Mentioned previously. Two weeks ago.

**Dave Jones:** The, the editors of, yeah, yeah, we did. Um, but now as it turns out, the editors of Hackaday, um, I assume they're the current paid editors, you know, who run the thing. Oh, yeah. Right, right, right. Um, yeah. They're, they're trying to raise funds to buy Hackaday, um, and, uh, form a non-profit to run it.

**Chris Gammell:** Lots of funds. Lots and lots of funds. Yeah.

**Dave Jones:** Well, we're talking half a million bucks, right? Right, right. So, you know, it's not, uh, it's not cheap. It's not, uh, chump change.

**Chris Gammell:** No.

**Dave Jones:** Five, five hundred and forty thousand dollar goal, and they're, they're up to eight thousand seven hundred so far. So they've got a long way to go. But there is 30 days left.

**Chris Gammell:** Right. It's tough.

**Chris Gammell:** I mean, it's like, there's not a whole lot of reason to want, uh, independent, but I mean, it would be a good thing, right? But it's not like everyone's like, oh, the ads are terrible there. You know, it's not like, it's not like they're popping up. Well, the ads are going to stay. Please wait 20 seconds. No, I know. No, I know. But they're not like, they're not like intrusive ads. You know what I mean? Like, that's, that's the downside. It's not like they're super oppressed. It's just like, it could be, you know, whoever they sell to.

**Dave Jones:** Well, they're saying, I think, that they might have to go to different forms of advertising and stuff to bring in more income to hire, you know, more editors and all that sort of jazz. Don't quote me on that. Right, right. Yeah. But, well, that was going to be the natural progression of the website anyway, you know, was that once, you know, it gets more and more popular, it needs more and more editors and, you know, more highly paid editors, I guess. Um, and yeah, and to do that, um, you need money. Right.

**Chris Gammell:** Well, this is just to buy it off the current owner though, too, Jason Gilcanis.

**Dave Jones:** Yeah, it's just to buy it off the current owner. Yeah. And then hopefully, and then they're hoping that the income stream will keep paying for the, um, because apparently it's not really making much money at the moment. Uh, the site, or it never has made a huge amount of money. It's sort of, you know, most of the money sort of goes into paying the editors and stuff like that. So.

**Chris Gammell:** Right.

**Dave Jones:** Yeah. Yeah. It's, uh, well, I wish them well.

**Chris Gammell:** I mean, uh, I suggest people that. Yeah. Same here. People donate. And, uh, I do like that they're doing the, uh, fixed funding thing. I keep seeing lots and lots of Indiegogo things. Yes, not the flexible. Oh. Flexible funding is just. Flexible funding. I know.

**Dave Jones:** Where you, if people don't know it's where, flexible is where even if you don't reach your target, you get the money anyway. So even if you don't end up with enough money to do the job, you still get the money. It's, it's lame. You know, it's. Right.

**Chris Gammell:** It's, it's good for some things, but it's a big sale, right? I mean, that's effectively what it is. Yeah.

**Dave Jones:** It's a, yeah. But no, this is fixed, which means it's just like the Kickstarter fixed is like the Kickstarter thing. If you don't reach a target, no one gets charged and no one gets anything. Right. So it's all a bust, you know? Yep. Um, which in this case, like there's no point for them to, you know, if they get, you know, 300,000, then well, that's not enough money to buy, buy it. So, you know, yeah, it's not fair to take the money and, yeah. Well, sorry, we try, but we didn't reach our target, but thanks for the 300,000 anyway, you know? We'll be in the Bahamas. Yeah.

**Chris Gammell:** Which is what you expect people to say when they're, you know, doing flexible fundraising.

**Dave Jones:** Yes, of course. Right. Oh boy.

**Chris Gammell:** Which is, which is another link on our, uh. Yeah.

**Dave Jones:** Let's not go there yet. I haven't finished. Oh, you have more to talk about. Okay. Well. Cause this, I'm ready for this one. I wish them the best, but, um, yeah, my fear is that, you know, when you, when it's tried, something is tried to, when something is owned by the community and tried to be run as a nonprofit for the community, I, you know, I can picture there being lots of shit fights. Oh. Well, you know, you need to run it as a dictatorship. That's the only way it works. You know, these things often work, you know, somebody needs to be in charge and say, no, screw you. I'm making the decision. Bang. That's it. That is true. Whereas everyone who contributes, you know, if somebody pays their, you know, what are some of the levels here are 500 bucks, a thousand, 5,000. Right. If you want to link on their main website, you know, imagine if you paid your $5,000 or whatever, or your thousand or your 500, then you, you, you're going to want to have a say in it. Right. Yeah, maybe. Or you're going to think you want to have a say in it. You know? Right. So, but, oh, look, I gave you a thousand dollars and well, you're not taking my ideas seriously and, you know, and it just turns into a big...

**Chris Gammell:** Well, I don't know if that really has any validity here, because it's not like they say that you'll have any say, right?

**Dave Jones:** No, no, no, exactly. But, you know, still that, that won't stop people, you know, complaining and stuff like that. And anyway, I don't know. It's, yeah, it won't, I can't see it running as smoothly as they hope, but it'll still work.

**Chris Gammell:** Well, it's like, I mean, it's like, it's like any project, right? I mean, when you have, if you have four managers on a project, right, there's always, there's always bickering and everything else. Right. I mean, like, it's just, it's just the same kind of thing of some, sometimes having a decision maker is good. Sometimes it's bad. AKA Caesar. Well, that's what they want to do.

**Dave Jones:** They want to hire a chief, a chief editor. Right. So, oh, and by the way, this is not the only campaign. Somebody else set up their own campaign. Once again, on Indiegogo, I think that also they're trying to buy it as well. There's actually two competing campaigns. Oh, wow. If you have a look, they actually link to it. They, um, on the.

**Chris Gammell:** Oh, I didn't see that.

**Dave Jones:** Yeah. Yeah. On the Hackaday website, they actually link to, um, the competing campaign. Um, yeah. So yeah, there's this guy who, uh, I'm not sure who he is. I did watch a bit of the video, but he says, yeah, look, I want to, I'm passionate. I want to buy Hackaday and I'm looking for, I think he's looking for, you know, the 350,000 or something or something like that.

**Chris Gammell:** Um, well, Dave, you should start your own. I don't know if he's currently. You should start a buy Hackaday campaign. Well, I should start one too. Yeah. I should start one. Yeah. Yeah.

**Dave Jones:** Jump on the bandwagon. Yeah. Everyone's doing it. And the first to half a million bucks wins, you know? Exactly.

**Chris Gammell:** The amazing race. Yeah. Yeah, exactly.

**Dave Jones:** Uh, so yeah, it's interesting. Um, interesting developments. That's for sure.

**Chris Gammell:** Yeah. Right. Because the other option is just to say, well, uh, I guess we could just start another site that's like Hackaday. Right. Right. Just a big internet property. Yeah.

**Dave Jones:** Right. Oh boy. Yep. Anyway, should we get onto the turd? The turd. The crackpot product of the week. What, what, what, what, what segment did we used to have?

**Chris Gammell:** We're front loading the Indiegogo and crackpot stuff. Not that the Hackaday thing was, but this one upcoming is. And then we'll get to the electronic side of things. How about that? Right. Yep. Yeah. Let's, let's do it. Okay. So I saw this, I think it was Mike, uh, Mike Harrison that actually posted this. Yeah. Who sort of tweeted it, right? Pointed it out.

**Dave Jones:** He found it and everything? And he put it on the forum as well. Oh, he did. Yeah. Okay. Yeah. I think he put it on the forum first and then he had a tweet rant. Um, yeah, it's, uh, folks, hold onto your hats. It's called the TARC. The TARC. It's, it's promoted as the first thought phone. The world's first thought phone, a transistor free and electronics independent communications device. Um, yeah, it's, it, it gets worse. And then what you, right. It just goes down from there. I started out.

**Chris Gammell:** I'm like, okay, there must be something here, right? Maybe it's magnetic or no.

**Dave Jones:** No, no. Here we go. The TARC stands for thought attenuated resonance communicator and is powered from the electromagnetic fields surrounding the human body and is activated by bioelectrical effects.

**Chris Gammell:** Man, this is a goddamn rock.

**Dave Jones:** All right.

**Chris Gammell:** Let's be honest here.

**Dave Jones:** No, it's based on interdimensional technology. And here's where it gets better, folks. Yes. This guy says Paris Tosin is his name. Tosin. He's certainly having a good toss here. Let's be, that's for sure. He's a tosser. Um, he, he has claims that he has been in touch with interdimensional beings or races, right? It's called Stelen's science and crystalline engineering. And he reckons he's got some of the technology from these interdimensional beings to design this TARC device. Yes, it is that batshit crazy.

**Chris Gammell:** It's like, oh, I, I really, I mean, I feel bad. Like this is bordering on, it feels like it's bordering on like, you can't, you can't be this crazy, right?

**Dave Jones:** I mean, he's, he's after 15,000 bucks, not American Canadian, which is, I think it's Canadian. Close these days, but. Right. Yeah. 15,000 bucks Canadian, but he says that, oh, if he gets like, you know, a hundred thousand dollars, he'll improve the production capacity and he'll create professional packaging and logos. And, and if he gets quarter of a million bucks, he'll do more research and development for a second generation device. I, oh goodness. What can you say? I mean, it's.

**Chris Gammell:** I, yeah, it, I don't, I don't know, man. It has no operating system. It has no transistors, no battery to install. I, I mean, this is like beyond, I feel like this is, this is a, a front to the shonky product of the week. At least some other people try. They, they don't just mention that there's not transistors in it. It's like, oh, here's this dirt. It doesn't have transistors in it, you know? I don't know. It's just, it's just a laugh, you know? Like we really can't say much else about it. It is. It's hilarious. No.

**Dave Jones:** The thing is, it's probably not a deliberate scam as such. This guy probably genuinely believes this thing works and believes all the shit he's saying. I, you know? Yeah. Can he really? It wouldn't surprise me. Yes, yeah, people are this delusional. They are.

**Chris Gammell:** It's just like people that like believe in like crystals and all that other crap. Like, yeah. Yeah, yeah, yeah. Energy crystals. Exactly.

**Dave Jones:** It's a similar thing. This guy just, yeah, he, you know, he's been in touch with interdimensional races, you know? Interdimensional. You know? Well, people believe in this shit. I guess, yeah.

**Chris Gammell:** Everybody needs...

**Dave Jones:** People believe in imaginary stuff all the time. Take religion. Let's not go there. Let's not go there. I mean, like, right? Yeah. I mean, seriously, people believe that they can hear God talking to them or they can hear these interdimensional beings talking to them or whatever. And to them, it's as real as evidence-based stuff is to us. You know? They feel it. It's real. So, you know, I mean... Yeah.

**Chris Gammell:** The problem is he calls it a phone. Otherwise, we wouldn't have brought it up. Yeah. That's a... Yeah. All right. Let's move on.

**Dave Jones:** Anyway, it's hilarious, folks. Go on. Go on. Take a look. Next.

**Chris Gammell:** Yeah, next.

**Dave Jones:** Oh, boy.

**Chris Gammell:** I don't even know where to go from here.

**Dave Jones:** Well, we could go to... Hey, let's continue the Indiegogo theme. Oh, another one. You've put a very provocative title here. Oh, yeah. This one.

**Chris Gammell:** Yeah.

**Dave Jones:** Tell us about it. Okay. So, this is interesting, right?

**Chris Gammell:** So, this is someone who has written a couple books, or a book, and he's created a robot, and basically, his thesis is he works with non-profits, he volunteers, and he wants to lower the cost of hardware for beginners, right? So, he runs a non-profit, and he wants to be able to, instead of spending $25 per Arduino, he wants to sell them for nine.

**Dave Jones:** And... It's like the Raspberry Pi model, right? Which is exactly the same. Right. It's a non-profit organization who want to get hardware in people's hands for as little cost as possible.

**Chris Gammell:** And so, yeah, my provocative title was, are non-profits the bane of open source hardware, right? I mean, like, not to be, that sounds quite provocative, but it was just on a whim, but

**Dave Jones:** I mean, honestly, like, there is some truth to this, right?

**Chris Gammell:** I mean, companies run on margin, right? I mean, like, between the material cost and how much you sell it for is what you run your company on and use future R&D or stuff, right? And so, on the one hand, I'm very, very much for this, because, heck yeah, I want more kids to have access to Arduinos and everything else. On the other hand, you know, this basically runs right up against that, I don't even remember what the name of it was, though. The guy that took the replicator 2 says, this is an open source design, I'm taking it to China, it's going to be $700 cheaper, and no one funded it, right? And there was a lot of backlash against that. And it's like, man, if that guy...

**Dave Jones:** But he did... The difference is, he did it for commercial reasons, for profit. This guy is doing it for, you know, much better reasons. Right, right. You know, he's, you know, he has good intentions.

**Chris Gammell:** Yeah, exactly, exactly.

**Dave Jones:** Yeah, he's not in it to make a buck.

**Chris Gammell:** He's, you know, he's doing it for a good cause. Right, but... So, I guess the question is... Okay, so say this continues indefinitely, right? The question is, like, you know, if this becomes more widespread, like, personally, I don't know the finances of, like, a Raspberry Pi Foundation, right? But there must be a little bit of margin, or else, you know, the big distributors wouldn't have piled onto it and everything else as well, but...

**Dave Jones:** Oh, yeah, there's enough to cover their costs, and this guy would be the same, right? He's, you know, there'd be enough to cover... Well, I said margin, though.

**Chris Gammell:** So, margin is the difference, right? That's what you run your operations on, right? So, if you, you know, if you need to pay people, or, you know... And honestly, I think...

**Dave Jones:** Well, as the Raspberry Pi Foundation do, right? They've got quite a few... No, they don't, actually. You know, they've got quite a... No? Liz... I thought they had quite a few overheads.

**Chris Gammell:** Liz Upton, I believe, is the only employee of the Raspberry Pi Foundation. Oh, right. Full-time employee, I think. It may have changed since they've exploded in growth, but when I... Right. I think when I talked to Eben at Maker Faire last year, I think that Liz was the only one. Um... And she does a lot of... She does a lot of the outreach stuff and the social media, but then, you know, Eben still works, I believe, and then some of the other designers, they all still work, basically. It's all volunteer. That was... That's old information. I'm not sure if that's still true. And so, that's the question, though. Is that, like, does... You know, like, at that point, does... Does open source hardware, then, you know, is it a volunteer workforce, right? Or is there still a business model behind it, saying that, you know, you have to add some kind of... You just have to keep innovating, right? That's always what's talked about of, you know, if it's open source hardware, you have to keep making new stuff. But, I mean, this is just kind of where it clashes, right? I mean, you want to offer low-cost hardware to people so they get involved, but then you also want to be able to run businesses so they can, you know, keep operating.

**Dave Jones:** Like Arduino, so they can, you know, like, I'm sure nobody wants to put Arduino out of business, right? Right, right. Because they're the ones who started it all and deserve the fortune and glory.

**Chris Gammell:** Right, right. Of course.

**Dave Jones:** Right? But this could potentially, you know, I'm not saying it will, but, you know, it... You know, why would you buy a $25 or a $30... I don't know how much the genuine Arduino costs when you can get one of these non-profit boards for $9? Yeah. Like, and how does anyone else come into the market space?

**Chris Gammell:** Yeah.

**Dave Jones:** You know, I mean, you can't... Let's say somebody wanted to do, like, a similar to the Raspberry Pi, but, you know, some variant or something. Well, how do you compete on cost? You can't. Right? Because, you know, you can't sort of, you know, make a profit and compete with the Raspberry Pi price. And that's a similar thing going on here.

**Chris Gammell:** Right.

**Dave Jones:** And we should say, if you have a look at the project page, right, here's the sort of, you know, thingy. This guy is, like, he's adding nothing extra. It is a complete duplicate of the Arduino Leonardo. And he actually shows two photos side by side. And, like, they are identical. The component placement's absolutely identical. Everything's... Right.

**Chris Gammell:** He goes over the differences in the project as well. Yeah.

**Dave Jones:** Yeah. But what... Yeah. I haven't read all that. Oh, yeah.

**Chris Gammell:** It's just some component differences, mostly, like, a different connector, a different diode.

**Dave Jones:** Oh, yeah. But the layout is exactly the same and the functionality is exactly the same. When you look at the two boards side by side, it looks like he's just replaced the Arduino logo with his logo and that's it. You know? And it may be a font change, you know, with some of the labeling on the pins. But apart from that, all of the connectors are in an identical... You know, all of the components are identically laid out. Yeah. Yeah, definitely. You know, you could... Which is allowed. I mean, that is okay. Like, this... Of course. It's totally okay.

**Chris Gammell:** Again, this is just a discussion about the interesting... You know, this is just an interesting aspect. I mean, on one side, this is a function of open source hardware, right? I mean, it allows people to say, I forgo margin in order to allow open... Or, sorry, to allow non-profit kind of access, right?

**Dave Jones:** And that's why you have to support them. If you support open source hardware, you have to support them doing this.

**Chris Gammell:** I think maybe the thing that would help with this, too, is, like, if you think about wide-scale access to this kind of pricing, right, for a $9 board, eventually, you know, he's either going to... If a thousand people... Not a thousand. Say a hundred thousand people want a board at $9, right? That might be when you start running into... You know, for nine thousand... You know, maybe he says, I can't make a hundred thousand at $9. Maybe, you know, that's what it is. It's the volume and the hassle behind creating that many boards and the delivery of it. That becomes the limiting factor in the manufacturing, right? Because that margin isn't...

**Speaker ?:** Right.

**Dave Jones:** He would have to hire more people... Probably have to hire more people and, you know, do whatnot. And, you know, and then it becomes a full-on business and then, well, you can't run it as, you know, then the price has to go up. It's sort of one of those contradictory things, you know? You would think that the higher volume you go, the, you know, cheaper everything gets, but not necessarily so. You know, especially if... Is he like a one-man band?

**Chris Gammell:** It looks like it, yeah.

**Dave Jones:** Right. Then, yeah, you know, there are limits to what you can do yourself. So, yeah. Although, to be fair, I haven't watched the video yet. So, I don't know.

**Chris Gammell:** Well, what's our verdict? Good luck. I mean, good luck because at the base of it, he's trying to offer stuff for, you know, his heart's in the right place, it seems like. He's trying to offer low-cost hardware to non-profits. I think if I were him, you know, I'd ask for donations from, you know, commercial ventures or individuals and then, you know, give preference to non-profits, right? So, people that are, you know, go for schools first and that kind of thing. And, you know, just ask for it, right? You can't demand it, but...

**Dave Jones:** And here's the difference, right? If he was doing this for, if it wasn't non-profit, right, he would be slapped down just like the Tangibot guy. That's what it was. Tangibot.

**Chris Gammell:** I forgot. Yeah.

**Dave Jones:** Tangibot guy got, you know, slapped down because he didn't add anything. He didn't, you know, that's the general, you know, it sort of goes into my own unwritten rules of open source hardware, which not everyone agrees with, of course, and that's fine. But, you know, usually you've got, you know, you usually don't directly, absolutely rip off and compete against the original designer. That's just not kosher. You're legally allowed to do it, but, you know, like, as happened, as the evidence showed, the Tangibot guy didn't really get supported. He got, you know, basically slapped down for it.

**Chris Gammell:** He didn't get funded either.

**Dave Jones:** But in, yeah, so, but in this case, it looks like people are, it looks like he's going to reach his goal. I mean, he only wants 12 grand and it's already up to seven with 31 days less. It looks like he's going to balls it in, of course. And it looks like people have no problem because he's doing it for those reasons. You know, it's a non-profit. He's doing it for those, you know, for some very good reasons. So that's how he's getting away with it.

**Chris Gammell:** Definitely.

**Dave Jones:** And there's nothing wrong with that. That's fine. I support him too. But yes, it does sort of change the game. You know, I mean, once these, as your title said, you know, once these non-profit ones come in, well, who do you support? Do you support the, you know, when you go to buy an Arduino, who do you, you know, an Arduino compatible board? Who do you support? What, the original guys who founded it, but you pay, you know, three times as much or whatever, two or three times as much? Or do you support the cool non-profit guy and pay less? I mean, you know, like, it's sort of like a conflicting thing. I don't know. My brain's exploding. Who do I support? Yeah.

**Chris Gammell:** I think my instinct is that most people will go after price just because that's my instinct, but maybe it's not true for everybody.

**Dave Jones:** No, no, I can, no, I'd certainly support people who wanted to, you know, not buy from this non-profit thing and support the original designer because I'm a big fan of that. I'm a big fan of with my, you know, as I said in the unwritten rules, you know, you try and support the original designer as much as possible, you know, as a first rule, as a first rule of thumb, you support them. So, yeah. I don't know. It's a tough one.

**Chris Gammell:** Well, speaking of Arduino, we should mention former guest of the show, Mr. Jeremy Blum. Jeremy Blum? He just released a book on Arduino. He did? Yeah, it's good stuff. There may be a review on the back for me.

**Dave Jones:** Yeah, we've both seen it and it's good.

**Chris Gammell:** Yeah. So, it was cool. I'm excited for him, you know. That's a smart dude. Obviously, he's graduated now. And it's through. Yeah.

**Dave Jones:** And it's through like Wiley. It's through one of the big publishers. It's not like a no-starch also. Right. It's not through one of the smaller publishers. It's a big-ass publisher. Yeah. So, it's good stuff. Yep. Good on him. We'll have to link it in to the notes if you want to get it. Yep. Isn't there a discount or something that people can get?

**Chris Gammell:** I don't know. But there is a bunch of videos, at the very least.

**Dave Jones:** Right. Yeah, he's done a bunch of videos. Well, that's where it came from because he originally did all those Arduino videos for Element 14, you know. And I think that's where a lot of the material came from. So, it makes sense. You know, a lot of the material was already done kind of thing. So, just like John Boxall, who's from Australia. Oh, that's right. He's writing a book now too, right? Yeah, he's done the Arduino book as well. And it's very good. I've physically got a copy here. And, yeah, it's awesome as well. And once again, he, you know, had done all these Arduino tutorials on his website and sort of, you know, that sort of all flowed into the book.

**Chris Gammell:** Yeah, it's interesting because the books seem like they, you know, they don't seem like it. They do take a long time to make. But it seems like it still offers a marketplace, you know, like that just, I don't know why you'd think the internet would still be the ultimate marketplace these days. But I guess it just gives validity and, you know, being on a bookshelf is nice and having like a paper reference and everything. Because you think about it, like if you're doing online tutorials or video tutorials and you end up just making a book that becomes an e-book, that's less valuable, right? It's like, oh, I'll just go to a website. Yeah, that's right. Yeah. But it's, I guess, I guess the dead tree version is cool to have in hand.

**Dave Jones:** We support dead trees here on the air power.

**Speaker ?:** We do.

**Chris Gammell:** We're old school. I'm getting older.

**Dave Jones:** Well, we support, well, I support, you know, sustainable forests and trees chopping down. You know, let's not chop down virgin rainforests just to print our books and our data books and stuff.

**Chris Gammell:** When's the last time you saw a printed data book, Dave? No, I know.

**Dave Jones:** Does anyone actually still have them? Does anyone still offer them?

**Chris Gammell:** I don't think so. Like, I mean, I guess I get catalogs. Like, I still get catalogs and, you know, you always get that awkward moment where I don't want to like, you know, I talk to vendors and they kind of like, they're like smiling and they hand over their catalog and I'm like, what do you give me that for? What is this? 1992? Come on. But, I mean, some people still want it, right? That's why they do it and they just assume that, you know, oh, guy that works in analog, of course he wants it. Definitely connectors. Connectors are still a big thing for me.

**Dave Jones:** Right.

**Chris Gammell:** Still, no one still has, I thought DigiKey had it with their digital, or their visual catalog. Right.

**Dave Jones:** It's just not the same, is it?

**Chris Gammell:** No, it's not very good at all, actually. I mean, now that I've dug into it for a while, maybe they're still improving it, but the, what's it called? They call it like their visual catalog. They call it something else.

**Dave Jones:** Yeah, something, I don't know, something like that. I am responsible for that, I think, for getting DigiCandy. Oh, yeah? Well, I'm taking credit for it anyway. Oh, you're taking credit for that, Dave? Yeah, I'm sure no one's ever thought of that for it. Yeah, I'm taking credit for that. Dynamic catalog, it's called. Stitching the paper catalog. It's such a good idea, right?

**Chris Gammell:** I mean, and I've talked about this for a long time, as well, as Dave has, apparently, but honestly, the only thing that it really matters for is connectors, right? I mean, I personally think that connectors are the big ones, and even still, like, you know, you need that flippability, you know what I mean? I think I mentioned before on the show.

**Chris Gammell:** You need to, yeah, yeah. The best way to do it still is Google image search, in my opinion. Type in what you think you need. I need an RJ45, and then just start scrolling.

**Dave Jones:** And hit that image tab, yep.

**Chris Gammell:** And just hope you have the right search term or that someone caught it. Yeah, that's it. Yep. Yeah, I've... It's tough, though, too. I mean, like, because then if you start getting... Like, I'm looking at, like, backplane connectors on this catalog right now, right? This DigiKey catalog. And it's like, all right. But, I mean, there's just so many, you know? Like, how do you start filtering? And, ugh.

**Dave Jones:** You've got to be careful with Google image search. Like, I highly recommend not searching for wire strippers. Strippers. Yep. Or, you know, you've got to be careful with, you know, using the words female. Milded Island. Right.

**Chris Gammell:** Female-male connection. Milded. Yeah, exactly. Mating. Mating connectors. We're really mature here on the Amp Hour. Definitely turn safe search on, though, if you're going to do the Google image search thing. Right. Yeah, that's a... That's a killer thing. We're trying to get more into the Google search thingy again with the... We're putting all our episodes on the YouTubes. The YouTubes. That's right. Yeah.

**Dave Jones:** The YouTubes. Yeah. We finally have found an easy way to upload all our episodes on there. So we plan... Do we plan on doing all of them?

**Chris Gammell:** Yeah, it'll take a little time. Because you're the poor spuckin'. Yeah, we'll get them up there. Yep. And it was actually Kai that did it that... The one who did... He uploaded the Amp Hour minus the Amp Hour, and that actually alerted me to this service. So... Pretty cool. It was nice of him to do that. Yeah.

**Dave Jones:** It just auto... You feed in the image, you feed in the MP3, and it automatically uploads to your YouTube channel. Yeah. It's like easy peasy. Yep. Good.

**Chris Gammell:** You know what's not easy? All right, so we... What? Uh, these new parts, these new... These new micros. Oh, come on. What? Have you seen these new Pic 12 8-bit, good lord, tiny small things?

**Dave Jones:** They've been around forever, these little...

**Chris Gammell:** I know, but... Ultra miniature things. I know, and yeah, I know, packages... It's basically the same size as, like, a BGA, but, like... I don't know. It just... It bugs me. Get over it. It bugs me.

**Dave Jones:** Well, you can still buy them as an SL 8-bit if you want. Yeah, well, no. What packet is... Does this new variant only come in? Yeah, this is... What do they call it? Yeah, yeah.

**Chris Gammell:** It's a... I don't even see the... That's the other thing. Like, it's not like... It looks like a QFN. Oh, it's a UDFN. I'm guessing that's micro-DFN, and they just call it U. Yeah. Ultra fiddly. 2x3 micro... No, millimeters, rather.

**Dave Jones:** So, what does UDFN stand for? Ultra fiddly... Dicky.

**Chris Gammell:** I was gonna say... I said micro-D... U being micro, probably. Like, a mu symbol. All right. UDFN. I don't... What's DFN? That's a... I can't remember. It's like the flat package with the... Yeah, yeah, yeah. Oh, flat, no leads. That's the FN. Yes. Dual flat, no leads, maybe?

**Dave Jones:** Yeah, something like that. Yeah, I know. They're a pain in the ass. I always forget... Whenever I do that... If it's something that small, they're useful. I mean, the thing about microchip is they have 20 million variants. Yeah, they do. So, you know, choose your poison. Not a problem.

**Chris Gammell:** You know, the thing with these DFNs, though, I always forget to, like... The key, I think, is bringing out... Is, like, modifying the footprint. Because if you don't bring the footprint out past the edge of the package, even though they tell you not to, you're never... Like, at least at prototyping, you're never going to get it on the board, you know? You need to be able to actually apply heat to a pad from external to the chip. Because if you're just doing hot air, it's just... I don't know. At least with... At least with a ball grid, you can get some air under there, you know? Like, and you have a chance. Right. These things... Nothing. Especially with that big, fat pad on the bottom, you know?

**Dave Jones:** Well, the big, fat pad actually helps. I've done a video of how you can actually solder through the pad, use the bottom pad as a thermal heat transfer. So you put vias underneath the pads, and then you actually solder from the bottom side of the board. And then I've showed a video where the heat actually spreads from that pad through the die, up the bond wires, and then onto the pads themselves.

**Chris Gammell:** That sounds healthy.

**Dave Jones:** Yeah, I know. Just heat the shit out of your... It's not the best way to do it.

**Chris Gammell:** Out of your 30 micron gold bond wires. I'm sure everything will go great.

**Dave Jones:** I tell you... Yeah, it's... It works, and it is a way to do it. You've just got to be careful.

**Chris Gammell:** Yeah, you know what the lifesaver is, I think? Is... And I think it was Curious Adventure videos, or someone else was showing... I was watching a video about soldering leadless packages and stuff like that, real tiny stuff. Right. Board preheaters have changed my life.

**Dave Jones:** Do you have one of these?

**Chris Gammell:** Right, yes.

**Dave Jones:** No, I don't have one. We used to have them at work. I got a cheap one. I think it's... Yeah, you can get them cheap these days. It's $30 or something, can't you?

**Chris Gammell:** Oh, maybe $30. I don't know. I got the hot air... I was talking to Jeff Kaiser about it, actually. I think he said not to get quartz, so I definitely steered away from quartz, where it's like the little... It's like an IR heater, because that can scorch your board. But this is basically... It's just basically like a hot air gun, you know, on the bottom of the board.

**Dave Jones:** That actually mounts on the bench. It sits on your bench, and you put the board over the top, and it hits the bottom of the board.

**Speaker ?:** Yeah, yeah, yeah.

**Dave Jones:** Then you just get a little clamp.

**Chris Gammell:** You hold it over top, and man, that... Oh, it's killer. It's just... Any kind of... You know, like everybody's experienced that before, where you're like... You're soldering, you're just holding a hot air pencil over top of the, you know, a copper pour. Yep, swirling it around. Yeah, and you're just opening it. Oh, God. Yeah. And then you move it for a second, and you see the solder start to flow, and then you're like, oh, crap, I missed it.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Oh, God.

**Dave Jones:** Yeah. Well, see, yeah, this is the proper way to do it. This is a professional way to do it. You preheat your board. Just like it goes through a reflow oven, you know? It has a thermal profile. Thermal profile. You know? This is a poor man's... Yeah. Yeah. And then a lot of flux. It actually preheats it all.

**Chris Gammell:** That was the other thing that... Oh, flux is everything. I know. Well, you know, that was a big problem for me for a long time. I did not appreciate the flux. I was totally fluxed. There you go. Yep. Like a joke.

**Dave Jones:** We should talk about our sponsor.

**Chris Gammell:** Yeah, it's pretty bad. For this week.

**Dave Jones:** We should, because we're halfway through. We're more than halfway through. Yes. Too much Indiegogo crap.

**Chris Gammell:** Sorry. Sorry, guys. Happiest. So, Netburner has once again, they've come back despite our... Well, we didn't do too bad last time. But they still have good products that you can use to get up and running quickly for your Ethernet solutions. If you need Ethernet in your project and you need to be able to prototype, you can actually get these boards. You can prototype with them quickly. Get up and running in less than a day. And you can actually then pull this whole module onto your board. So, you can actually plug it in and go.

**Dave Jones:** Yeah. Embedded in your product and it's all done for you.

**Chris Gammell:** Exactly.

**Dave Jones:** Yeah. Why anyone would dick around? Unless you're manufacturing 100,000 of something. Right. You know? Yeah. Why would you dick around trying to do it yourself? You know? It's just... Oh, man.

**Chris Gammell:** Well, and especially if you're already in the same kind of product families. If you're used to... You know, if you know that you're a cold fire house because a lot of the Netburner boards are cold fire based. I mean... Which is pretty standard. Especially in industrial space, medical space. Oh, yeah. So, like, basically, they're just giving you a dev kit, effectively, that you can take and start running. It's just not from cold fire. It's from Netburner. So, you get all the auxiliary benefits of having, you know, tailored packages to get up and running quickly. Yep. But, yeah. Cool. Cool.

**Dave Jones:** And they have a proverbial buttload of products. I do.

**Chris Gammell:** We were looking at this before the show. It's... It's...

**Dave Jones:** There's, like, dozens and dozens of each different type tailored to every possible solution. Yeah.

**Chris Gammell:** And if listeners are interested, you can actually... They're giving Amp Hour listeners 20% off dev kits. The one that they sent us is actually a Mod 54415. That's the plug-in board. And then the common board that it plugs into is a Mod Dev 70 board. And basically, you can hook up to it with serial, you can hook up with USB, and then you can toggle, you know, a lot of stuff and get an easy interface so that you can get up and running. So... Straight on the web. Yep. Right under the web. And it's all royalty-free. So that's nice, too. And it's got RTOS built in. You know, the usual stuff for a... Anytime you have, like, an Ethernet or USB stack, you usually need an RTOS in there. And Lord knows I'm not going to write one. So...

**Dave Jones:** No, exactly. I'm not going to spend six months sticking around. No, thanks. I'll just plug in one of these. Much easier. Save your sanity.

**Chris Gammell:** So, thank you to Netburner for sponsoring the show this week. They continue to be awesome. Thank you very much. Check them out. All right. What else do we have to talk about? Anything? Should we just shut it down now? Just call it a day?

**Dave Jones:** Aren't there another 10 Indiegogo projects? No.

**Chris Gammell:** Oh, God.

**Dave Jones:** Indiegogo seems to be the rage now. Everyone's sort of moving away from Kickstarter because, oh, it's too rigid. Oh, I can't get flexible funding, you know. Yeah. Anyway, let's not go there.

**Chris Gammell:** Yeah. Well, speaking of rigid, so there was a ruling that was just handed down from a ruling body. The ARRL actually just rejected a petition to encrypt data communications. Did you hear about that at all? No. Did it help? So, basically, someone petitioned them saying that, you know, we're entering a new age of data and we need to be able to encrypt our radio communication, you know, on different radio bands. Right. To stop the NSA snooping on us, right? Right. And that is kind of the... They didn't actually ever state that, as far as I can tell. Right. Right. But that was definitely the undertone and, obviously, the timing was way too coincidental. Right. But, you know, the basis of amateur radio is that everyone can listen in, you know, you can... And it is self-policing. That's kind of the thing, right? Same thing with, like, open source hardware, right? It's self-policing, you know, because there's just not resources in order to be able to have some kind of third party that can watch over and say, hey, you're doing this wrong, you know, you're in trouble, that kind of thing. It has to be, you know, community. And so they said, no, yeah, you... If it needs to be encrypted, it probably shouldn't be amateur. That's basically the idea. Right. Okay. And it's good.

**Dave Jones:** Why do they have a say in it anyway? Why do they...

**Chris Gammell:** Why does who?

**Dave Jones:** The Amateur Radio Relay League.

**Chris Gammell:** Why do they... Well, it's actually the FCC. I mean, the FCC is...

**Dave Jones:** Oh, right. Oh, it's the FCC. Right. Okay.

**Chris Gammell:** Right. But it's... The ARRL is pretty...

**Dave Jones:** So how are the ARRL involved?

**Chris Gammell:** It's a third party organization, but it's just... I mean, they're... Basically, as it was explained to me, and people I'm sure will correct me if I'm wrong, especially ham radio stuff. I think it's basically whatever the ARRL says the FCC goes along with, basically because it's that self-policing and stuff. I mean, it's a lot of the same people, too, you know?

**Dave Jones:** And they didn't support it. The ARRL gave it the thumbs down.

**Chris Gammell:** Exactly. And, you know, another reason, too, is that, you know, a big function of amateur radio is for emergency communications and everything else, and it's like... Right. At the times when you need it the most, you don't want that stuff encrypted. You don't want to mess with all that stuff, so they said...

**Dave Jones:** Yeah, you want to be able to make a transmitter out of a couple of transistors and an old teapot, you know?

**Chris Gammell:** Yes. Right. That sounds like a heck of a product.

**Dave Jones:** Or a project, rather. Well, that segues us nicely. Oh, yeah? To what? Yeah, it does. There's one on the thing. Are you a little teapot short and stout, Dave? Oh, boy. Flying teapot.

**Chris Gammell:** Flying teapot.

**Dave Jones:** Bertrand Russell's famous flying teapot.

**Chris Gammell:** That's a philosophical argument, right?

**Dave Jones:** Orbiting, yeah, philosophical argument. Yeah. Teapot orbiting Mars. You can't prove it or whatever? Yeah, you can't prove it's not there. Yeah.

**Chris Gammell:** Is there really a segue or no?

**Dave Jones:** Yes, there is, because there's a new ad hoc Wi-Fi network-y thing to use during disaster recovery thing. Oh, God, it's an Indiegogo. Oh, I didn't see this. Yeah, sorry. Another one. Jeez. It's on the list. It's an Indiegogo. Yeah, it's called the Speak Freely. Yeah. The Speak Freely. And, yes, it's, well, yeah, there's nothing new here. I think a lot of people have been working on this. It's like in disasters, you know, the GSM network goes down, the whatever, you know, the mobile phone network, cellular network for you yanks. Yeah. It goes down. And, you know, everyone's, you know, the seven billion mobile phones on the planet are useless, right? So they're getting them to talk together with Wi-Fi and stuff like that. But, you know, Wi-Fi point to point.

**Chris Gammell:** Yeah, I was going to say, Wi-Fi is terrible for that kind of thing, isn't it?

**Dave Jones:** And it's limited to, what, 100 metres? You know, like, if it's Wi-Fi, it's like 100. Like, you could see the person. Why don't you walk over them and talk to them? Say hi. You know, if it's 100 metres away. Well, I haven't watched the video. I haven't watched it in depth and know how it works or if they have repeaters or anything like that. Well, they must. Yeah. Not exactly. Well, yeah, yeah, they have to. Otherwise, it's useless, right? If you don't have repeaters that can sort of, you know, if you can't talk to someone 10 kilometres away, then what's the point?

**Chris Gammell:** Yeah.

**Dave Jones:** You know? So I'm sure it must do that. Anyway, there's lots of... And there's people working on the other aspect, like a mobile, like an ad hoc GSM transmitter repeater type thing. So they use the GSM functionality instead of the Wi-Fi functionality. Yeah. You know, there's pros and cons both ways. Yeah. The Wi-Fi one is like it's just an app, basically. So you don't have to get it certified and all that sort of jazz, I guess. Whereas if you go, you know, if you try and manufacture some sort of, you know, GSM cellular transmitter repeater thing, you know, you're just going to get slapped down silly by the government. Government. Government. Yeah. Government. Yeah. So, yeah. Anyway, check it out.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Whatever. Can we say that we're not going to do another Indiegogo? I don't know. They snuck up on us there. I don't know. They just pop up. Yeah. They just keep, you know, they just keep popping up.

**Chris Gammell:** Yeah.

**Dave Jones:** We can talk about a crashed airliner.

**Chris Gammell:** No. That's.

**Dave Jones:** No. No. No.

**Chris Gammell:** No.

**Dave Jones:** What do you get seven votes? No.

**Chris Gammell:** I don't care. I shouldn't say that on air. It's a dictatorship. I know. It is a dictatorship, folks.

**Dave Jones:** It's not a democracy. We'll talk about what we damn well like. We rule us two kings. Regardless of what everyone says.

**Chris Gammell:** I don't know. What have you been working on lately, man? What have you been, what have you been making? Anything?

**Dave Jones:** Nothing. Because I just did a five-hour live show. You did a live show. Yeah. That's right. Well, I only do them like every hundred or something. So, I did four hours for the 400th show. So, I thought, oh, yeah, I'll do five hours. Are you hit 500? 500. Yeah. Well, I'm pretty close to it. Yeah? Well, officially, but I'm like way over. I'm like 520 videos or something. If you actually look at how many I've uploaded. Yeah. Because some I didn't number. Some have been multiple parts. Blah, blah, blah. So, yep. So, it's a bit arbitrary, you know.

**Chris Gammell:** I've been dealing with vendors again. I'm doing the vendor dance again. Kind of like what Jerry talked about when she was just entering the vendor dance. I'm nearing the end of my tango.

**Dave Jones:** Everyone's bingo she's full by now, surely.

**Chris Gammell:** What? Mentioning Jerry?

**Dave Jones:** No. Mentioning the bloody, you know, the dance.

**Chris Gammell:** The dance? We should play music. Tango music.

**Dave Jones:** You're all the musician.

**Chris Gammell:** You've got live hardware there, don't you?

**Dave Jones:** Oh, yeah. They can't play it.

**Chris Gammell:** Rattle off something on the piano or something. Yeah, but the... It's funny to get to the point where I'm like, I'm like able to say more confidently how many I'm making. And I tell you, it never ceases to amaze me. Like when you have some volume and when, you know, like when you start speaking more freely about it because you're more confident about, oh, well.

**Dave Jones:** Right.

**Chris Gammell:** You know, I thought it was going to be a hundred and now it's going to be a thousand.

**Dave Jones:** And she didn't want to lie. Right. And she didn't want to lie.

**Chris Gammell:** Right. And of course, everybody just says, well, you should just lie. But no, I don't like lying either. Yeah, yeah, yeah. That's right. But it's amazing how nice everyone gets. Right. Money. Money. Money. Money. Money. Money. Money. Yeah. Money does make the world go round, apparently. And, you know, unless you're a non-profit doing an Indie Dago campaign. Oh, of course. Right. Yeah. Well, come on. Don't make fun. We shouldn't make fun of them. No, definitely not. But, you know. No, it's good.

**Dave Jones:** You know, the world does. That's what I'm saying. The world doesn't always revolve around money.

**Chris Gammell:** Oh, right. Yeah, that's true. Yeah, you're right. Yeah. Right. But you know what? For certain things, it does. Especially certain things like, you know, in supply chain stuff, right? I mean, like, supply chains move based on money, you know? Like, they just... I can't even imagine the next step up, you know? Like, I'm not doing anything crazy, but, like, you know, moving up into, like, automotive or, you know, consumer level, like, million, couple million pieces of, you know, a certain micro or something, you know? Like, I've never gotten that high before.

**Dave Jones:** I've gotten as high as a couple hundred thousand.

**Chris Gammell:** Okay. Like, single year? Mm-hmm. A couple hundred thousand? Yeah. Yeah. Oh. See, now, I would be interested to hear from people about that, too, because I'm sure that, you know, we've asked in the past about people that are in the consumer space, right? And we've had, I think, like, 15% of the audience or so said they were in the consumer space. And I assume that there's some percentage of that, then, that's actually working on large-scale products. Mm-hmm. And it's just got to be a different game, right? I mean, like, because I know that there's salespeople that are dedicated just to one company, right? I've heard about that before. Oh, yeah. Yes. Yes, absolutely. Multiple salespeople, which blows my mind.

**Dave Jones:** If you're an Apple of the world, yeah, you'll have multiple people handling your account. Right. Just dedicated to your account, you know? They're at your beck and call. They're on your speed dial, you know? Yeah. And as you said, like, on the flip side, you said, oh, people get very nice, right? Yeah. When those sort of volumes happen. Yes, they do. But then they could also get incredibly gnarky if you don't give them the design win. Right. You know, is the industry term, you know? They're all after the design win. Or sockets. You ever hear that one? Yeah, yeah. Where they talk about winning sockets? Oh, that bugs me for some reason.

**Chris Gammell:** Yeah. I know what it comes from.

**Dave Jones:** Every semiconductor manufacturer wants to get that socket or that design.

**Chris Gammell:** Or get every socket. That's what they talk about, right? We want to get every socket. Yeah. Yeah, okay. Well, you know, make some stuff I actually want to use this time. Yeah.

**Dave Jones:** And if they don't get the design win, and they've put a lot of work into their, into, you know, a lot of time and effort and free gifts and everything else trying to woo you to use their product. Right. And if you don't go with them, they can get real gnarky. Yeah.

**Chris Gammell:** Free gifts within reason, of course, right? You know, samples and, you know, less than $25 or whatever. Do they have that there? And they take you out for lunch and they give you, sorry? Do you guys have, like, because, like, in the States, we have, like, Sarbanes-Oxley and other, like, regulations based on, you know, how much gifts you can take. And then there's always corporate governance on, you know, if, you know, vendors can give you...

**Dave Jones:** Oh, I'm not sure. There probably are at the high end of things, as you know, if you're a public company or something, if you're a shareholder or, you know, if you're on the board or something like that. I think there might be. But down at our us grunt level, no. Yeah.

**Chris Gammell:** Yeah, I guess that's what they want to really give you anyways. Yep.

**Dave Jones:** Yeah. And they woo you and they take you out for free lunch and they, you know... Right. ...give you all sorts of freebies and they offer all sorts of support and...

**Chris Gammell:** See, the support is the main thing for me. I mean, so I was on the Toymakers chat the other night and you stopped in there, too. We were talking about it. And it's just, like, the thing that really matters is the support, ultimately, right? I mean, like, yeah, sure, getting a dev board is nice, right? But honestly, most of the time, I'd rather just pony up the dough, you know, and pay for a dev board if no one's going to bug me about it, right? I'd rather... Yeah.

**Dave Jones:** Well, that's the thing. The support comes... It's a two-way... You know, it can be a two-way street there. You can get support where, you know, they only support you when you need it. And the other aspect is, no, they keep hassling you.

**Chris Gammell:** Yeah, right.

**Dave Jones:** You know, we talked about this. Oh, they phone you up every day. Can we help you? Can we help you? No! Go away! Bugger off!

**Chris Gammell:** I try and do your impression of that when... Because you do that in your promo video, right?

**Dave Jones:** No! Yeah, yeah, yeah. I've got the... I'm a professional design engineer! No! Engineer. I don't need component advice from a... Right, yeah. I don't need design advice from a component supplier. Yeah. That's what I scream in the video. Right, right.

**Chris Gammell:** Yep. My accent's terrible.

**Dave Jones:** And, well, see, that's the thing, right? They all come in, and they're all nice, and they offer you... You know, they're... You know, oh, look... They want to help. Come on, give them credit. Yeah, they do want to help, right? But the thing is, it comes down to a practical thing. It's like, you know, look, there's no way that I could possibly explain all of my technical requirements to you. It'd take a month.

**Chris Gammell:** Right.

**Dave Jones:** You know, heck, it took me two months to write the design spec for this product, and you want me to... You know, like, you can't help. You're more of a hindrance than...

**Chris Gammell:** Yeah.

**Dave Jones:** You know, like... So, yeah, I... You know, you've just got to be careful. You can spend more time getting help than actually just saying, no, thanks. Look, I don't need it. Yeah. You know, it's... Yeah.

**Chris Gammell:** Yeah, that's tough, too, because, you know, it's not just one vendor as well, right? If you're working with five vendors, you've got to tell that story five times. You've got to keep straight who you told what and who you're allowed to tell what and everything. It's just...

**Dave Jones:** Yeah, and they want to come and meet you. Oh, look, let's come and sit down and have, you know, spend the whole afternoon, and you can explain all of your technical details. I don't have time to do that. It's like, you know...

**Chris Gammell:** Yeah.

**Dave Jones:** And as you said, if you get five people all wanting to do the same thing, you can, you know...

**Chris Gammell:** Yeah.

**Dave Jones:** Suck away all your time just trying to keep them up to date with your technical requirements. And it's like, no, it's...

**Chris Gammell:** Yeah, it kind of comes down to trust, you know, like, because, honestly, I've felt the urge before with certain big vendors to just be like, screw it, you know, like, you have everything I need, you know, like, just design this stuff for me. Like, not like I really want to do that, but like, you know, when you're in a time crunch and they're offering that, like, there's always that... I think that's what they're really hoping for. You know, they really want you to just be like, just do it, you know, just, you know, either because you're a software person and you need help with hardware or...

**Dave Jones:** Yeah, I've done that. We've had people, you know, like complex stuff like FPGAs, for example, you know, and if you're not very good at FPGAs, you know, you might be able to bum your way through it. But then if the distributor comes along and goes, look, oh, we have a really great apps, you know, field applications engineer who's a whiz at FPGAs and he'll do it for you. Yeah. You know, then, you know, your eyes sort of start lighting up and go...

**Chris Gammell:** Yeah, yeah, because you just think about all the other stuff you have to do, right? And, you know, and that's what they don't teach you in school, right? That is... That bugged me a lot, right? Because when I came out of school, I thought about, you know, I was like, oh, I'm just going to do everything, right? Because it's interesting and I want to learn stuff. And at the end of the day, sometimes you just don't get to. And that part sucks. That's right. But also, you know, sometimes you just need to get stuff done, right? If you want to get a product out the door, if you're focused on getting your product done, which in my opinion is more important than ego, even though I've fought with my own ego a lot, you know, like your mindset changes, you know? It's just, no, just get it done. It doesn't matter if it's perfect. It just needs to be done. And sometimes that is, you know, working with a vendor to have a prefab solution. Yeah, it's a little boring, but boring is, if it works, you know?

**Dave Jones:** Well, hi, welcome to the world of engineering. Yeah, and product development, right? I spent my whole entire career doing boring. Yeah, yeah.

**Chris Gammell:** That's development versus research, right? That's the D to the R, right? And that sucks sometimes. Sometimes development blows. But sometimes then you get to, you know...

**Dave Jones:** Oh, there's some fun. There's some fun stuff in there, but generally, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** I mean, you can spend... There are people who spend their entire career and they do nothing exciting at all. They do nothing new. They just spend their whole career, you know, grinding, you know, on the treadmill, just grinding out stuff.

**Chris Gammell:** Yep. This component's absolutely... Change it out. Yeah. This component's absolutely... Change it out. Yeah. Well, yeah, and so like I was saying, though, like, sometimes it feels like the urge is there to just kind of, like, go all in, right? But you can't, right? You know, like, so say I want to go with just one vendor. They have all the chips I need. I'm just going to buy them all from them and get good pricing because it's a package or whatever, right? Like, that could bite you in the ass the next day, right? Because they say, oh, you're only buying from us? Well, guess what? The price just changed, you know? But it's the same kind of thing, right? Like, any kind of system, right? Like, picking a distributor, right? Sometimes you don't have a choice. You just have to go all in because of time constraints, you know? Yep. Or picking a PCB package, right? Like, that is a big decision, right? And once you go, you know, if you pick Altium, you got to go all in. You got to learn everything about it because you're not going to change that for 10 years, right? No, that's right. Because the transaction cost of switching away from it is super high because all your stuff is already in that, right? And they all know that, right? So these are the kind of things you have to decide. And it sucks sometimes. Oh, boy. Speaking of PCB softwares. So, one that I've been resisting because of what we've talked about previously is online, you know, online-only schematic. Right. Or layout programs and everything. But I thought Upverter has a very interesting selling point now. something that I think should be called out and praised. They have forking. So you can say, fork it. I'm just going to do it. So basically, you know, open source projects, right? So you upload your design for the microcurrent, right? Is that open source hardware? Yes, it is. Yeah. So that's open source hardware. You upload the design files, right? So that includes the schematic. It includes the layout. And it includes, I think, maybe there's even bomb backend stuff, right? On the actual features that they offer. And then basically, much like GitHub, right? Basically, this is an implementation of GitHub forking into hardware. So then I see, oh, Dave's got his microcurrent up there. I'm going to make microcurrent Gammel version. And so I hit fork, right? And then I could take it and start, you know, it's a whole new project. And then just start cranking on it. And basically, you can have derivative projects all over the place. And I'm not sure about reintegration, but that would be the ultimate idea, would be to actually be able to...

**Dave Jones:** Well, I assume it doesn't re... Yeah, assume it doesn't reintegrate or that's not terribly easy, I can imagine. Yeah, that would be the hard part. But that would... Well, you can't do it at the PCB level, you know? Right.

**Chris Gammell:** That's ultimately what GitHub is good at, right? Because then you actually pull the forks back in and then I...

**Dave Jones:** Yeah, code is a different beast. Yeah. You know, hardware is a different beast to code. Right. Really. Yeah.

**Chris Gammell:** And so they've also been featuring stuff too. And that's cool too, right? I mean, like they actually have been featuring projects for... Yep. ...that you can take and just fork, which is cool because you want to just... Awesome. Yeah, yeah. Oh, that's cool. I like that. Click, go, I'm going to build it, right? And I think what their idea is is that ultimately Upverter is going to be like, oh, hey, you want to buy the components? Buy them through us. And then, you know, like you can just click by a board, comes assembled. Right. I think that's what everybody's going towards with online. That's the promise of online. And it's tempting. It is oh so tempting. It is.

**Dave Jones:** It is tempting.

**Chris Gammell:** Waste of trap. It's in there, man. I don't know. Upverter's got another vote in their column because they, I think their export, they had like an export thing on their site. Okay. Where I think they can export to a bunch of different formats now too. Can they import? I don't. One of the two isn't there yet.

**Dave Jones:** Right.

**Chris Gammell:** It's kind of important. It is. Where is it? Because they just changed their site around too. I don't know. But, so, I like what they're doing. But, it's still, I'm still, no, I'm not there yet. I don't know about you. You're still nervous. I'm still very nervous.

**Dave Jones:** No, I'm still nervous. No. Yeah. I don't think I could commit to an online tool. You know, and. I'm not sure if I could do it. I'm too old school.

**Chris Gammell:** Yeah. And I think they said some, I mean, some of the, so I think some of their features are, some of their code is open source. But I'm sure not all of it is. But man, if it got to the point where like, all their code is open source, and then I could compile something for a local build, so that I, in the event of failure, I could, you know, run it locally. Right. That, maybe they're getting there. But, keep going guys. You'll get there. I think. It's.

**Dave Jones:** Well, there's always going to be a subset of people who are going to want to use it. Of course. There's always going to be a bunch of professionals who just will flat out refuse it. Yeah. For very good reasons, you know. Yeah. So, yeah, no, you can't be all things to all people. Right. It's impossible.

**Chris Gammell:** Right, right. And, I mean, open source alone is, you know, a strong point for them. Because if you're doing all your design out in the open anyways, why not, right? It's basically Upward is trying to be GitHub for. Yep. For. Right. For. Hardware. Hardware. Thank you. Hardware. That's what we do. You think? Oh, some days.

**Dave Jones:** Can we speak and can we talk some hardware now? How about a chip of the week?

**Chris Gammell:** Ooh, yes. Go ahead. So, this is one you found, but I had seen it mentioned as well.

**Dave Jones:** Yes, it's the new, well, we've done it before. You know, it's the new LT. There's a new version on the LT3080 series.

**Chris Gammell:** Yeah.

**Dave Jones:** Voltage regulator. And it's the LT3081. And, yes, just like the LT, it's sort of a big improvement on the LT3080, which has had some dye issue, which has had some design issues. Yeah. So, I'm not sure if this one has a similar thing. It could do.

**Chris Gammell:** And this was in your planned power project? Is that right?

**Dave Jones:** This is in my micro supply. Yes, I was using the LT3080, which I may have to go away from because I don't have a good vibe anymore. And there are workarounds to the issues that they're having with the silicon in there. But, yeah.

**Chris Gammell:** Which you wouldn't think there'd be a lot of silicon problems. Like, it's...

**Dave Jones:** No, it's a regulator. It looks pretty, yeah.

**Chris Gammell:** It's an op-amp and a couple transistors. But not like I know what the hell I'm doing.

**Dave Jones:** But then again, I'm trying to use it in a non-standard kind of way. But, you know. But still, anyway, no. Even a standard way, you can still... Using their example circuit, you can still kill it. You know, so that's pretty bad. Anyway, this LT3081, it's an expanded version of that. So not only is it a sort of a low drop-out, go-down-to-zero-volts regulator, the voltage output is set by a single resistor because there's a constant current output and then it's just got the typical feedback circuit with the op-amp and the pass transistor. It's, you know, not only is it that, so it's still the LT3081 in that respect, but it has a current monitor built in as well, which is really groovy. And it's a voltage and it's a current output. So once again, single resistor, you can scale the output voltage to anything you want because you just change the resistor value on the monitor pin, on the current monitor pin. And yeah, so you don't need a separate current monitor chip like I'm using in my supply design. And on top of that, it's also got a die temperature output as well. Once again, set via a single external resistor, it sets the voltage range. So great, you can scale it. The great thing about using these external resistors is that you can set your current range to whatever supply you're using and whatever the input range of your analog to digital converter is. You know, usually inside your micro or whatever and it's, you know, you can just scale it. It's great. You don't have to dick around with, you know, external op amps and voltage dividers to scale at all. Yeah. Yeah. It's just choose the correct value resistor. That's it. Right.

**Chris Gammell:** It's fantastic. Buy decent resistors as well. Well, yeah. Yeah.

**Dave Jones:** Anyway, yeah. So it's got a temperature output, a die monitor temperature output. You can feed that back into your analog to digital inverter. And on top of that, yes, it's got the kitchen sink, folks. It's got current limit as well. Once again, set by a single feedback resistor. Yeah. Yeah. In there, which connects to the output, unfortunately. So it's not like you can adjust the current limit digitally. There's no easy way to do that unless you use an E-squared pot.

**Chris Gammell:** Right.

**Dave Jones:** But then E-squared pots have voltage limits. You know, they have maximum voltage limits. Oh, right, right, right. You're not going to use this thing up to 36 volts with an E-squared pot, you know. Well, it looks like it's floating, though.

**Chris Gammell:** It's floating on from the output to the iLim, so it looks like it might be okay.

**Dave Jones:** No, but then you've got the control pin and the reference and everything. Yeah. No, it doesn't. Yeah. No, been there. Okay. Looked at that. Even your high voltage, in quote marks, E-squared pots only go to 12 volts. See, I've never touched those. I've never... Ah, right. They're pretty handy. Yeah. For lots of uses, but...

**Chris Gammell:** They're never precise enough for me.

**Dave Jones:** I mean, like, they're okay for, like, stair-stepping kind of stuff. Yeah, I know. Yeah, they're pretty crude. You can get, you know... Your general one's, like, in 128-step, 256-step. Yeah. You can get, you know, like, 1,024-step. That's always drift stuff for me. I mean, like, yeah, the steps are okay,

**Chris Gammell:** but then, like, the driftiness... Yeah, pretty horrible in terms of drift. Yeah, yeah, yeah. And it's like, at that point, yeah. I don't know. Yeah. Get a DAC, you know? Yeah. Get a decent DAC.

**Dave Jones:** Yeah, yeah. Yeah, I know. Yeah, exactly. Because that's how most people use them, right? You know, 50-cent DAC.

**Chris Gammell:** They use actual DACs, or they use them as, like, a feedback for a DAC or something, you know, ad hoc DAC.

**Dave Jones:** They have lots of uses for setting, you know, crude volume and stuff like that, or, you know... Mm. You know, yeah, there's, you know, lots of reasons. But as you said, yeah, they are pretty crude in terms of their tolerance and specs and stuff, but... I way overdo it with precision stuff.

**Chris Gammell:** So, I don't know.

**Dave Jones:** Well, yeah, speaking of which, this is not... You might think this chip is magic, but, you know, there's no free lunch here, folks, I'm afraid. Well, an amp and a half. Oh. Well, no. Well, okay. It's an amp and a half. But you can parallel them up, right? But anyway, the thing is, right, you might think, oh, current limit in building, great. I can build a great precision current limited power supply out of this single chip. Wah, wah. Wah, wah, wah. No, go read the little asterisks and the thing, and it says, yeah, tolerance of 15% on the current limit. Right, right. Only 15%, you know. So, yeah, over temperature. So, hmm, trap for young players there. Yeah. That's why you can't take... You know, that's the thing. You look at the front page of this and you think it does everything. And you're racing and you spend, you know, all day thinking about what wonderful design you can do with it, and then you finally get down into the deep, dark detail of it. Oh, it's 15% tolerance.

**Chris Gammell:** You know, shit. Read your data sheets and then prototype, folks. That is important.

**Dave Jones:** So, it's good enough for crude... But it's designed for crude overload kind of thing. Yeah, right. Like, you know, where it's, oh, 200 milliamps is near enough, you know. Is it 200, 250? Eh, you know. Right.

**Chris Gammell:** And this is actually a question I asked today on the Reddit as well because it was actually separate from this, but it was just everything's getting current limiting or, you know, protection type stuff built into it. I think the one I posted, there was like an eFuse built into some TI part. And it's like, you know, our younger engineer is going to actually have a sense of, you know, needing to current limit, right? I mean, like, obviously they'll understand the flow of current, hopefully.

**Dave Jones:** And input protection and stuff like that. Yeah.

**Chris Gammell:** I mean, it's just everything is getting thrown in because it's a feature that can actually be sold. But until it's actually designed into everything, everything, you know, you need to worry about this. And if you just start expecting it's going to be there, well, you're going to blow up a lot of chips, right?

**Dave Jones:** Well, I'd say you're not going to have a career if you go around. That's true. You're not going to have a very long career if you go around expecting things to work instead of actually checking to see if they will work. Yeah. I'd say you're not going to make a good designer and you'll end up in management. Right.

**Chris Gammell:** I was comparing it to my... But the thing is, like, I was comparing it to EST, right? I mean, like, I don't really... I'm not very stringent about, like, you know, static mats or wearing a wrist strap or anything like that. I mean... None of us are. I know. But I'm just saying, like, that's much less of a concern than it used to be, right? I mean, everything has a diode built into it now. It actually shunned current away when you have a static spike, right? And... But it wasn't always like that. Where there was a point where... No, that's right. It... Back in the 70s, 80s? 80s, yeah. I mean, like, yeah, this old CMOS stuff, that stuff would just pop. And... And, you know, like... But eventually it got designed in everything and then people like me could just ignore it, right? And so the idea, I think, would be that eventually this kind of, you know, current limiting or something else might also get designed in. And then there might be other issues because of that. I'm just... I guess I answered my own question, but... Like usual. But, I don't know. It's just something to watch out for, I guess, if you're getting started, you know? You don't always trust the vendors to design it for you because it might not be precise enough or it might not work at all.

**Dave Jones:** As the LT3080 had issues, right? You think it's wonderful and you design it in and, no, you find little hidden traps everywhere.

**Chris Gammell:** Yeah. What's the price on those things? It's not good. I didn't see it.

**Dave Jones:** Oh, the LT3080, they aren't cheap. Come on, it's LT. Right, right, right. Or the Rolls-Royce of analog, you know? Yeah, like they're five bucks one off or something. I don't know. They're pretty expensive. Oh, yeah, yeah. These aren't... No, if you're after a low-cost solution, you wouldn't be dropping these LT regulators everywhere over your board. You know, you wouldn't have ten of them on there.

**Chris Gammell:** Yeah, this looks like it says 370, 470 in single quantity. Yeah, that's pretty rough. Duh.

**Dave Jones:** But, hey, if they do everything you need, then, you know, with no fuss. No fuss, no muss. We were talking about that before, right? Yeah. You know, you don't want to dick around, right? You just want to... That's true. Oh, look, this chip does everything I need and there's an application circuit which does exactly what I want. Bam. Put it in. No risk. No fuss. Thank you very much. I'll pay the three bucks, you know.

**Chris Gammell:** Well, that is the last thing we should bring up about this. That was an interesting thing that you pointed out on this data sheet, which I did not expect. They actually talk about Arduino on it, on like an LT.

**Dave Jones:** Oh, yes, they do.

**Chris Gammell:** On an LT data sheet, they're mentioning like Arduino monitored supply. And it's like, huh.

**Dave Jones:** Have they jumped the shark? Is this the beginning of the end? Every old graveyard out there is just groaning now.

**Chris Gammell:** I was going to say Jim Williams is rolling over in his grave probably, but... Yep. Although I was talking LT the other day. They said that they're putting some 8051 cores in some stuff. So, I don't know. Right. It's all... Yeah, maybe it is the beginning of the end. I don't know. Analog companies. Nothing's purely analog anymore. Chris is outmoded.

**Dave Jones:** But you're out of a job.

**Chris Gammell:** Just like we're out of time. Yes. Well, I'm going to go practice coding, I guess. Coding or marketing. I don't know.

**Dave Jones:** Well, you always wanted that MBA, didn't you? Oh, yeah.

**Chris Gammell:** Yeah, I've always talked about it in such great light. All right. Well, I'm off... Go and get one now. I'm off to study. And people can come quiz me about MBA stuff in New York City. So, be sure to let me know on the subreddit if you think you're going to make it out to this New York City meetup. I'd love to see everybody and hang out and have some... Have some...

**Dave Jones:** Hey, I could send my full-size cardboard cutout, Dave.

**Chris Gammell:** There you go. Yeah, man. Do it. All right. Well, I'll let you know all about it next week. Oh, and Jeff Roberg, applications engineer of Blue Giga and mentioned last week on the show for the Key Glove talking to Google Glass. He will be on the show talking to us about his Google Glass experience. I will have my Google Glass at that point. Sweet. But we'll talk about Bluetooth, and that's the real thing people should ask questions about on the subreddit.

**Dave Jones:** Fantastic.

**Chris Gammell:** All right. Talk to you then.

**Dave Jones:** See ya.

**Chris Gammell:** This episode was brought to you by NetBurner. NetBurner allows you to get your embedded network solution up and running quickly, so you can get your prototype or your final product out the door faster than any other solution available today. To hear more about the hardware, software, and friendly build environment, and to get a listener discount, go to netburner.com slash theammo. Thank you.
