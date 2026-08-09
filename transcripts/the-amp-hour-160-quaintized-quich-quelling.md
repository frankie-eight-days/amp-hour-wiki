---
episode: 160
title: Troubleshooting, PCBs and LEDs - Quaintized Quich Quelling
url: https://theamphour.com/the-amp-hour-160-quaintized-quich-quelling/
---

**Chris Gammell:** This is The Amp Hour Podcast. Recorded August 26th, 2013. Episode 160. Queen Ties. Quitch. Quelling.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEVBlog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life. What's up, nerd? Hello, David. I'm glad to hear you're not... What's the word? Dead? Dead? Yeah, I think it's the word. Yeah.

**Dave Jones:** Yeah, I have... Well, I'm probably going to sound absolute crap this show. Yeah, you're gross. Yeah, sorry, folks. I do have my trigger finger on the mute button. So, I'm not good. If you didn't know, I've... Yeah, I've had a nasty virus for the last couple of weeks, which has pretty much stopped me from doing everything, really.

**Chris Gammell:** And that, ladies and gentlemen, is why you shouldn't have children.

**Dave Jones:** Right, yes.

**Chris Gammell:** This is what we were talking about before the show, is that, you know, like you start having kids, and the kids meet other kids, and they're all germ factories and everything, and it's a bad time for virus time. It's not pretty. You know what? Your immune system is getting such a workout right now, it's unbelievable.

**Dave Jones:** I know.

**Chris Gammell:** It's just nature trying to knock you off, man.

**Dave Jones:** Right, yeah, I know. Survival of the fittest and all that.

**Chris Gammell:** Yeah. Make some room for other electronics people, huh?

**Dave Jones:** Come on, Darwin. Come on, take me, you bastard. Bring it on.

**Chris Gammell:** Bring it on. Come on. I'm glad you're alive. That's good. You know, the same thing happens at work. Thank you very much. Usually I get the secondhand effect. All the people, like, have kids. They come into work still, for whatever reason that happens to me. Of course, yep. And then, of course, I get it from them. And the green grass grows all around, all around. Yep.

**Dave Jones:** Well, that's one of the, you know, things. Like, you don't want to think that, you don't want them, you don't want your employer to think that you're, oh, just chucking a sickie, as we call it here.

**Chris Gammell:** Right.

**Dave Jones:** You know? And, you know, because, oh, I've got a runny nose, you know? Oh, I don't want to chuck a sickie just for that. You know, you want to save it for, you know. I don't know, when the Super Bowl's on or something, right? I don't know. What do you yanks care about? I don't know. Like, a big day. You know? Right on.

**Chris Gammell:** Not the Super Bowl for me, but.

**Dave Jones:** Right. Okay.

**Chris Gammell:** Maybe, like, a Friday night. I don't know. Yeah, something like that. Don't want to come out on a Friday.

**Dave Jones:** Yeah, I'll get a long weekend. Monday morning. Usually. Yeah. Yeah. Yeah. You know? If you've got Monday off, oh, yeah, I'll chuck a sickie on Friday, you know? Yeah. And chuck a sickie. Chuck a sickie, that's it. So, you don't want them to think that you're chucking a sickie, but you don't want to, you know. But you shouldn't go in, because it just, like, you're actually trying to do good for the company, but at the same time, you're doing bad.

**Chris Gammell:** Yeah. Oh, yeah. Every time, too.

**Dave Jones:** Because you just go in and give it to everyone else.

**Chris Gammell:** Well, and there's pressure to do it, too. Like, I mean, I remember someone in my office. Yeah. He was, like, on death's door, you know? He's, like, hacking up wrong all the time. And it's, like, you've got to figure at a certain point, if you're important enough in a company, you know, if you're making these decisions under the influence of, like, you know, Sudafed and all this other stuff. Like, I've been pretty messed up on just over-the-counter drugs before. Plus, you know, like, my head's all congested. Like, that is just not, that's not a good place to be in. Like, you were just going to make mistakes then.

**Dave Jones:** Yep.

**Chris Gammell:** Exactly. So that's, but you're right. The workplace culture is definitely like that. I mean, it's like, don't be a baby kind of thing. You know, like that whole mantra, but it's a mess.

**Dave Jones:** Yeah. Yeah. Is it different now?

**Chris Gammell:** I think we talked about, is it different now? Yeah. I mean, like, you're your own boss, so.

**Dave Jones:** Oh, me? Oh, yeah. Yeah, kind of. Well, no. Yes and no, right?

**Chris Gammell:** Yeah.

**Dave Jones:** Yes, in that I still feel pressure. Oh, I've got to churn out some videos. So I churned out a couple, right? Even though I was, you know, and they were pretty crap, right? But anyway, I've got a couple out there. And, yeah, I, so yes, I felt some pressure to continue to actually produce stuff.

**Chris Gammell:** Yeah.

**Dave Jones:** So when I, I shouldn't have, I just like, should have just said, bugger it. I'm taking a, well, I didn't know it would take two weeks, right? I thought it'd only be like a week tops. Yeah. Because that was the rumor going around that this, you know, virus that everyone was getting was like one of these five day viruses, you know? It wasn't over in a couple of days. So I thought, okay, it'll be a week, you know? And, but no, this is now the third week and I'm still not, not a hundred percent. Yikes. You don't want to see what's coming out of my.

**Chris Gammell:** No, I don't. My lungs. I don't want to hear about it either. No one, no one wants to know about this, Dave. No. Okay. Right. It's like extreme social media oversharing. Yeah, exactly.

**Dave Jones:** Check out a photo of the one that just came out. Look at this.

**Chris Gammell:** Oh God.

**Dave Jones:** Yeah. I know. It's pretty bad.

**Chris Gammell:** Anyway. So you've been able to keep up with news while you're laying on the couch moaning and, you know, trying to feel better or is this more of a.

**Dave Jones:** No, that's all I was doing. Lying on the couch moaning, trying to feel better.

**Chris Gammell:** Yeah.

**Dave Jones:** Did anything exciting happen? Well, I've. Oh. Been near death?

**Chris Gammell:** Not too much, I guess. I mean, only like 40 stories on Reddit and such. But a lot of these, a lot of these are timeless, you know, a lot of timeless electronics news.

**Dave Jones:** Yeah. There you go. Hmm. Hey. I did my first crowdsourcing.

**Chris Gammell:** Oh yeah. Yeah. We haven't talked about that yet, have we?

**Dave Jones:** No, we haven't. So we haven't talked about anything yet except what color of stuff I'm coughing up.

**Chris Gammell:** Yes. Anyways, how's crowdsourcing? So what did it end up at? I mean, this is for like a PCB ruler too.

**Dave Jones:** This is for a PCB ruler. You know, and I didn't want to do it. You know, I didn't want to make any more of these rulers, but I just made 500 for the Open Hardware Summit, right? So if you go into the Open Hardware Summit, you'll get one before anyone else. I think. When's the Open Hardware Summit?

**Chris Gammell:** That is September 5th.

**Dave Jones:** Oh, okay. Then you, yeah, you'll likely get them before anyone else. They will be in the goodie bag. I've just had word that they'd be delivered by the FedEx truck. So, yeah, there you go. They should be there anyway. Okay. And so, yeah, I thought, no, you know, I, you know, I didn't want to make any more of these rulers, too much hassle, but people kept asking me, right? Can we have the ruler? And, you know. Oh, had to hit my mute button there. Sorry. Oh. And this will go on all show. I should have sat this one out too. Anyway, you know, because like these things don't cost much, right? And when something doesn't cost much to actually make, usually, you know, there's no point doing it because all the hassle and expenses all in the shipping and the logistics and everything else, right? You know.

**Chris Gammell:** Perhaps you don't understand low or high margin products, but go on.

**Dave Jones:** Well, high margin products, I know. But, yeah, like I've always said, I can't understand somebody on eBay who sells something for 50 cents. Oh, okay. I agree with that. And then ships it for free from China. It's like, it's just ridiculous, right? But anyway, so, but I had all these, you know, a whole bunch of people and somebody on the forum started a thread and I thought, oh, well, okay, look, I'll, you know, I'll do a couple of hundred. How hard can that be? You know, maybe a couple of hundred people will want them. So I did a little impromptu. I thought, oh, that'll be an opportunity to try this crowdsource funding thing too. Why not? You know, if it hits the target, then I'll get 500 boards made, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** And, and if it, and if it doesn't reach the target, oh, well, sorry, dudes, you know, I'm just, I just won't bother, you know, because you don't get the money. So yeah, it sounded like a neat thing. So I, you know, spontaneous spur of the moment thing. I just went and did a, a Possible campaign, which is the Australian website. Everyone keeps asking, why did I use Possible? Why not Indiegogo or Kickstarter? Because it's Australian. That's why.

**Chris Gammell:** Yeah.

**Dave Jones:** So anyway, you know, I wanted to support Australia. I can't use Kickstarter because I'm not American. Or Canadian. And.

**Chris Gammell:** Or UK or British.

**Dave Jones:** Or Canadian or, yeah, exactly. And Indiegogo, well, I don't, you know, everyone bitches about Indiegogo. So I thought I'd give the Australian mob a try and they've been good. Anyway, so, you know, I didn't bother doing a video or any of that crap, you know? I just put up, yeah, here's my rule if you want one pledge, you know, kind of, kind of thing. And, yeah, I woke up the next morning. I did it like a, you know, three o'clock in the afternoon or something. I woke up the next morning and I'd already cracked my target of 2,500 bucks. And 500, I think it was, you know, 500 odd boards or something. So in the first day.

**Speaker ?:** Yeah.

**Chris Gammell:** Very nice. So it ended up, what, 25K plus or no? What?

**Dave Jones:** 31,000.

**Chris Gammell:** 31,000. Something or other.

**Dave Jones:** 31,000. Something or other. Yeah. Which is, oh, sorry, I don't have the stats to hand, but it's 9,000, I think it's 9,700 boards. To 2,100 and something people.

**Chris Gammell:** Wow. That's a lot of people. Yeah.

**Dave Jones:** So that's a lot of people. That's a lot of, yep.

**Chris Gammell:** Well, that's great, man.

**Dave Jones:** Yeah. It just went crazy. So now, it's, you know.

**Chris Gammell:** Now you're a shipping depot.

**Dave Jones:** Now I'm a shipping conglomerate. Yeah. Right.

**Chris Gammell:** Which is the downside of any kind of online type of sales thing, right? You have to get good at shipping. Yeah, we've talked about that endlessly. Yep. Yep. Yep.

**Dave Jones:** Yep. And, you know, it was going to be, oh, okay, I could easily, you know, buy a couple of hundred stamps and ship a couple of hundred envelopes. Not a problem, right? Yeah. But now it's a couple of thousand. No, it's a totally different board game. And now I have to talk to mailing houses and things like that to try and optimize the process. Because, you know, it's gotten to the point where, you know, I was going to, like, I've got one of those label printers, you know, that can print out all the addresses. I've got all the addresses in a CSV file that I download from Possible and I can put them all in and print them all out. But then it takes extra time. But now you've got to consider all the optimization parts of doing this, right? It takes me an extra, I don't know, two, three seconds to peel off that sticker and put it on the envelope, right? Well, you want to optimize that out of the step. So now I'm looking to get, you know, a mailing house to print directly onto the envelopes. And then you go, well, I can't just do stamps now. I can't just go out and buy 2,000 stamps at $2.60 each and peel them off and stick them on the envelopes. Well, you want to optimize that too. So you want to get one of those franking machines or whatever they're called, you know. I'm not sure what they're called in the US, but you can get these official machines from the post office that will print the postage onto the envelope, you know. So, yeah. And then you pay the post office or the supplier of the machine and then, yeah, the money goes to the post office. And yeah, you don't have to physically put a stamp on there. It's designed for all that high volume mailing stuff. And yeah, so I've got to look into that. And I'm probably stuck between that point of, oh, you know, a couple of thousand might be too small a job for a lot of these mailing houses, right? You only want to send a couple of thousand. Oh, that's one off. Yeah. That's, you know, it's kind of like the, you know, you want to buy reels of components, right? You know, you just want one reel, you know, or half a reel. You know, it's sort of that weird, you know. So you've got to end up buying, so you end up buying from DigiKey and paying more than what you get it from your local supplier at if you bought 20 reels or something. So you just, yeah, I'm sort of stuck in that.

**Chris Gammell:** Yeah, that's tough, you know, the volume optimization stuff. Surely there's someone that will do it all for you. I'm sure you just have to hand over a chunk of cash. Oh, I'm sure.

**Dave Jones:** Yeah, it's just, yeah, I'm sure they'll take, they'll happily take my money and do it. It's just a matter of, yeah, whether or not it's worthwhile, right? So at the very least, I'm sure I could find somebody to do at least, you know, print my envelopes for me and maybe do the franking postage thing on there, you know, but they may not want to stuff them, right? Because they're used to using, you know, stuffing them with envelope, paper, you know, and using their automated folding machines and stuffing machines and all that sort of stuff. So, yeah, I don't know. It's all too hard.

**Chris Gammell:** That's okay. It's the curse of success, I suppose. Right. Yeah. Well, speaking of that, you're not the only crowdsourced game in town for PCBs. There's another one that's coming out from, is it Octopart that's doing it?

**Dave Jones:** Octopart, yes. They just emailed me this morning. Yeah. The CEO of Octopart, Sam. They can't be that huge if the CEO is personally telling me about it. So, I don't know how big they are. I have no idea. Your friend works at Octopart.

**Chris Gammell:** Yeah. Yeah. My friend Russell does. I think it's like 10 to 12 employees or so. I'm not sure how many exactly. No, I can't. Right. It's small, but I mean, they're powerful, right? I mean, Octopart's a nice search engine for, you know, search a lot of different sites and distributors and stuff. So, that's why I like them. And then CircuitHub, I'm a big fan of too. They use their API. And Octopart API is pretty cool. So, I like that.

**Dave Jones:** Cool.

**Chris Gammell:** Yeah.

**Dave Jones:** And can anyone get that API or is it like...

**Chris Gammell:** Yeah, I think so. I actually haven't... So, this was actually one of my ideas for Google Glass was to have a talking... Of course, I needed to learn how to actually integrate the API with all the Glass stuff. But to tap the side and say, okay, Glass, look up part, you know, ABC123.

**Dave Jones:** I was going to say, you could do it for a teardown. You could be staring at a part and you could look at the part number and you tap it and you go, tell me how much that part costs, you know?

**Chris Gammell:** Yeah. So, that was the idea I had initially. Right. And then, of course, contextual electronics has been eating my life. But, yeah. So, that was the idea was integrating Octopart's API for that kind of thing. And a lot of people do. You kind of see the API pop up here and there. But this is a reference PCB that Star Simpson, who did... She actually... Her and someone else did the teardown with SparkFun or, you know, via SparkFun for the Google Glass teardown. Right. Star and then Sam from Octopart. They designed this PCB together. And I had talked to Star about it a while back because I was always really frustrated with having, like, the scale of, you know, like, you know, you can kind of keep them in your mind but not necessarily, like, having it, like, snap decision kind of stuff of, all right, well, it's a SOT 23. Is that bigger or smaller than an S-O-I-C-8?

**Dave Jones:** You know, like... Yeah. Yep. Yep.

**Chris Gammell:** Yep. Yep. Yep. Yep. Yep.

**Chris Gammell:** All those things at once. What I always really, really wanted... And NXP did this. I'll try and link in the NXP document, too, because that was a good one. I think I might have mentioned it before. But NXP had a document where they showed a bunch of different footprints, but they didn't show the actual scale. What I've always wanted is, like, a zoomable document where it's, like, you started a big, like, you know... Right. Yeah, yeah. Quad, flat pack, 204, kind of huge, you know, 13x13mm kind of package. And then you just keep zooming in, and you get the same detail, but then you can actually compare them one to another. And I think, actually, KiCat actually does that, too. They have... It'll generate a PDF, and there's some CAD programs that'll sort of do this kind of thing, but it's never been as interactive as I wanted it to be. Yep. So having these kind of reference cards are great. So the layout actually has a whole bunch of different package types in the back. You can kind of see them from the image, but there are, you know, some BGAs, and then kind of working your way down to 0402s and MSOPs and TSOPs and all those lovely types that we all love.

**Dave Jones:** And it's actually a PCB. Right. With their... On the front is the resistor color code. Now, here's the kicker. Now, they're actually, because it's a PCB, they have to silkscreen all the different colors on the PCB. Yeah. And it's like, you know, the first thing you go is, well, why didn't you just print a card? You know, a regular, you know, card. It'll be infinitely cheaper, right? Yeah. But of course, it isn't as cool, because it's not made out of PCB material, right? But this makes it... Yeah. It's expensive to print that many different colors on there. Right.

**Chris Gammell:** And Star even said in the video that they're actually sending it to a different house just for silkscreening. Yeah. So that probably speaks to the, you know, the process that's necessary, because, damn.

**Dave Jones:** Yeah. No. I know. Not every manufacturer would, you know, give you 10 different colors to start with, let alone do it for you on the one board.

**Chris Gammell:** Yeah. Right. So, yeah. It's definitely going to look cool. And, you know, it's a good reference to have, too. You know, it's all about having that in your pocket, you know, kind of just being able to be able to pull it out when you need it and reference it.

**Dave Jones:** My only complaint was that it was a three-color resistor code, not a four-color.

**Chris Gammell:** Right. They left out tolerance, which I was thinking, too. And it was like... But I guess those are a little easier to memorize.

**Dave Jones:** Yeah. And the... Well, the five-banded one with the tolerance as well. Oh, you're talking about... Oh, okay. Gotcha. Yeah. I see. I would have split it into... I would have had two separate ones or something on there. But I don't know. But then you've got to squeeze it in and, you know.

**Chris Gammell:** Yeah. Well, I mean, it's cool for what it is, though. I mean, it is compact. So that's an interesting side of things.

**Dave Jones:** How thick is it? I don't think they say, do they?

**Chris Gammell:** No. I don't think so. But I would guess 62 mil. Whatever that is in metric. Sorry.

**Speaker ?:** Mil.

**Dave Jones:** Nobody does bloody... Hang on. I'll get my... Oh, your ruler.

**Chris Gammell:** Oh, this is useful. Yes. You know, I've seen these kind of, like, comparison boards before, too. Every time I see them, I love having them around. Because there was one I saw for... I had taken a picture of it a long time ago. I was digging through old pictures and I found it, actually, of someone doing, like, diode comparisons. Because they were getting down into, like, you know, like, SOT 523, SOT 923. Like, all these crazy small packages, you know. And then you start getting into the chip scale, 4-pin BGA type of things. Like, oh, it gets... That's when... That's, like, the zoomable document that I... That's what I really want, you know. But... Yeah. Yeah. It's tough. Especially... You know what the tough part is? Is having that comparison... Like, when you're on, like, a DigiKey or a Mouser or a Newark type of thing, you know. Like, being able to not just have that list and being able to pull it up, right? Like, so that script we talked about two weeks ago, that's really great for seeing, like, the different package types. But those are actually the same size when you compare them side to side, right? Yeah. So not having that scale reference is kind of tough for that kind of thing.

**Dave Jones:** Like, occasionally you get a... You can search by chip size, you know. It'll be 5x5 millimeters. Right. You know, and stuff like that.

**Chris Gammell:** Right, but that's... That's always the problem with parametric search, too. You can't just do it by, like, relative dimension, you know. Like, what you need is, like, kind of like the hand-wavy, you know, like, ah, about this much, but then this much. But then you're talking in millimeters, so it's like, oh. Bloody yikes. I know. Yeah. So you figure out with your little handy-dandy ruler there?

**Dave Jones:** Oh, right, 64. No, sorry, I didn't look it up.

**Chris Gammell:** You're not going to? No. You're not going to? Okay. 1.6.

**Dave Jones:** You're talking standard 1.6 millimeter? Sorry, I forgot what value you used. Yeah.

**Chris Gammell:** Yeah, I used that 62 mil, yeah.

**Dave Jones:** Yep.

**Chris Gammell:** Or thou, as you would. You like thou.

**Dave Jones:** Thou? I use them interchangeably. I know. I know. I know. I know. Even the same sentence. I'm, you know, hopeless. That's okay. It's all contextual. Don't know why.

**Chris Gammell:** Yeah, so this is a cool, it's a cool project, though. I like it.

**Dave Jones:** And yes, it's a crowdsource funded thing. And once again, they're using yet another crowdsource funded site. Yeah, crowdsupply. Yeah, crowdsupply.

**Chris Gammell:** Never heard of them.

**Dave Jones:** No. Never have I. I don't think. I don't know.

**Chris Gammell:** There's some where they're like, there's that one where you can actually do your own now. You can like put it, install it on your site. Oh, really? Yeah. I think it was the lock people. Remember that phone-enabled lock? I forget the name of it.

**Chris Gammell:** Lock-a-tron, maybe? Is that what it's called? I think it was Lockatron but there was one where like they kept getting rejected from Kickstarter and they're like screw this we'll just write our own it's like oh okay yeah a bunch of coders you know it's like that's you know it's pretty smart

**Dave Jones:** like a WordPress thing or something you just install it do you

**Chris Gammell:** yeah yeah it's just like it's just a you know a software package you install on a server so

**Dave Jones:** I don't know about that oh goodness well you know I guess

**Chris Gammell:** it's just a bidding software and then a payment back end right that's I won't say it's all Kickstarter is but you know those are the main components really then the community aspect yep I could probably write one you know whatever no big deal yeah right

**Dave Jones:** hey I forgot to mention you wonder what the shitty thing is and apparently this happens to a lot of people one of the downsides is is that PayPal shut PayPal shut you down

**Chris Gammell:** oh yeah yeah

**Dave Jones:** for being too popular it's the curse of the crowdfunding campaign yeah because it looks

**Chris Gammell:** for some reason that looks like you're a money launderer for some reason yeah

**Dave Jones:** and of course they do it for your protection your protection right in quote marks even though money's coming into your account yep right they do it for your protection and yeah I ended up with like four and a half thousand transactions on my PayPal account

**Chris Gammell:** dang

**Dave Jones:** because because you get a transaction for every person who puts in and then possible I don't know how the others do it Kickstarter and all that but they take out an individual 5% transaction each time each time it goes in so for each person who who who said you're pledged you get two transactions on your PayPal account and sure enough and they actually warned me you know that yeah just be careful they may shut you down and sure enough they did PayPal shut me down and and I actually spoke to a human

**Chris Gammell:** yeah I saw that yeah

**Dave Jones:** yeah I actually I got their number here in Australia and I spoke to a human in a call center in India of course but

**Chris Gammell:** of course you know

**Dave Jones:** hey and they fixed my account in 10 minutes you know

**Chris Gammell:** well that's good unbelievable I was shocked online business can be dicey like that though you know like it's just crossing so many it's like doing like well like like you've complained about in the past right like dealing with components and and the US government like ITAR type stuff international trade and regulation stuff like that's that's just a mess right I mean like yeah

**Dave Jones:** yeah

**Chris Gammell:** and you know it's like anytime you cross a country border you have a whole new new set of speaking

**Dave Jones:** of which rules whole new set of yeah yeah my campaign was the most supported in the whole history of possible right it had the most number of supporters ever

**Chris Gammell:** okay I'm waiting for the rules part Dave

**Dave Jones:** yeah well the rules

**Chris Gammell:** allow me to toot my own horn a little more

**Dave Jones:** they it it actually broke their shipping engine right their shipping engine wasn't good enough so they had they've had to rewrite their shipping engine they've had to redo it

**Chris Gammell:** waiting waiting for the rules here David what what was you said speaking of rules your segue was

**Dave Jones:** speaking of well

**Chris Gammell:** they're not rules

**Dave Jones:** but no postage like mail it

**Chris Gammell:** Dave rules Dave rules

**Dave Jones:** oh goodness sake

**Chris Gammell:** speaking of rules Dave rules

**Dave Jones:** I'm the ruler of possible get it oh my god oh god okay no more bad yeah anyway so yes because and all the yanks complained of course because this is an Australian website they all complained that they didn't have a a postage field in there when you're filling out your address for city you know and all the yanks got up and up oh yeah yeah blah blah blah you know and apparently yeah they've had to go on and they've had to go and rewrite their shipping engine and and and my campaign showed up bugs in their csv download thing as well with all their fields for stuff like that so they've had to fix those bugs as well which nobody found before because nobody had used the Australian site to have so many overseas contributors before it just you know um yeah oops I broke it

**Chris Gammell:** you broke it man so I have a question about international stuff since we're talking about crossing lines I got in an argument uh this week with a friend about about internet hiring people internationally and I I think I already know where you come down on this kind of thing but what how do you how do you judge whether or not to hire someone like in country or overseas

**Dave Jones:** uh what do you mean actually so what I was doing is I was there there on a working visa or something what are you talking about

**Dave Jones:** no just like sending work

**Chris Gammell:** so like so I basically what happened was I was hiring someone for a task and I hired them based on you know the merit of their application and you know everything else and then I told my friend where this person was from and it was somewhere in Europe and and he's like well why don't you just hire someone in the US and I'm like because I don't I don't care right I mean like I care about the the quality of the work not where the person was born and I wonder about that because especially in electronics right I mean there is there is a nationalistic trend for that kind of stuff too right I mean he even called me out for saying like you know Chris you always talk about you know bringing manufacturing back to the States and you know Dave you talked about manufacturing in Australia right and we are nationalistic in that way but where do you really draw that line between like if you knew there was a good designer in India or China or you know Germany or England you know like how do you really make that decision right and I was just curious he he wanted us to talk about on the show and I'm like yeah I'll bring it up at least okay

**Dave Jones:** well let's talk about I guess how long is a piece of string which is a term you didn't know about

**Chris Gammell:** I know it now because of you yes

**Dave Jones:** you know it now yeah right let's be let's clarify this completely right is this person a US citizen

**Chris Gammell:** he is

**Dave Jones:** well what's the problem

**Chris Gammell:** oh wait is the friend or is the person I'm hiring

**Dave Jones:** no the person you're hiring no I said

**Chris Gammell:** they're they're they're European

**Dave Jones:** they're they're they're they're they're it's yeah it's all digital work it's all yeah right it's all digital work

**Chris Gammell:** okay right but I mean how do you draw that line right I mean because like like I said we've talked about manufacturing a lot with electronics right it's good and the point I made was with electronics with manufacturing the main benefit is not like the the the the nationalistic pride or anything like that it's having something there and being able to walk out to the floor or drive down the street and be like yeah no you put that part in the wrong friggin place fix it right now or you put that part in the right friggin place great job right I mean oh you gotta have both sides right

**Dave Jones:** or I'll break your legs you know yeah yeah

**Chris Gammell:** I mean yeah so that's that's what it was and it's like I just wonder what the limits of that are you know like because the reason I'm asking you is because you know you always try and source stuff locally so maybe what your thoughts are on that kind of thing

**Dave Jones:** well I'm a similar thing you the key word there was digital right it's all just digital remote work in that case I'm like who cares right like it it doesn't matter yeah you go for someone who you know if you know this person that they do good work use them you know I got no problems with that at all but yeah as you said when it comes down to local you know there's many reasons for having that local manufacturing and on that aspect I support the local manufacture of stuff

**Chris Gammell:** yeah

**Dave Jones:** and I you know and we can go into the whole you know it's you almost become a hypocrite because you're saying one thing and then you're saying another on one hand you're saying one thing on the other hand you're saying something else you know it's well yeah he was you know the world's not black and white like that

**Chris Gammell:** right and that's yeah exactly that's the point I got to as well and it's like you know he's like oh well you know if you build your if you build your business on low cost labor then you're going to be dependent on it and I'm like look I'm hiring someone in the UK first off this is not low cost labor this is talented labor right and that's what it ultimately comes down to is that in certain things it becomes purely meritocratic right you know like it's based on what they can do and not where they live I don't care I would rather pay someone a hundred dollars an hour to make a design well than to pay someone twenty dollars an hour and have to pay them for twenty extra hours to get the same stuff done right I mean like it's just that just seems like the right thing to me and then it got into all this like it wasn't like raw raw nationalism but it was just like oh you know like well don't you want to hire people locally and I I don't know I just I don't really care you know like right I'm kind of looking out for number one here

**Dave Jones:** once again I probably would give a preference for someone local but once again it comes back to the practical things like they'd be in the same time zone yeah that was a good point that he made yeah you know like yeah of course like if I had two identical people I know could do the job I'd probably pick the Australian person yeah right the local person from Sydney you know because well you know not due to some nationalistic pride just because it's just more practical or it may be if you know shit hits the fan then you know you can just go out and talk to them face to face

**Chris Gammell:** yeah and really it started as like this it seemed like it was nationalistic to start with but it did evolve into this all these other arguments that actually did come up at one point or another but you know it's just it's interesting because it's it's just the reality that we live in these days right I'm sure that some of our listeners out there you know I think about like people who are consultants you know you can get if you're if you're especially if you're a specialist in some area or you you know you find a group of people that say you're working with like you know you're really good with quadcopters or something like that right if you have one if you're a consultant in one area and a group of people get to know you those same group of people is going to keep calling you and people you know competitors and others just because you get a reputation and that's a really good thing for a business right but it's it's just it's not going to it's not always going to be that that same company that calls you is going to be down the road they might be you know next continent over so it's just right the reality of living in internet age I guess

**Dave Jones:** well that's a thing when I was a boy

**Chris Gammell:** you know

**Dave Jones:** this thing wasn't even an option geez be thankful you've got the option these days to do this sort of stuff back when you know phone calls cost you know a hundred bucks for ten minutes and international phone call was a hundred bucks for ten minutes and there was no internet and you know I mean these sort of things just you know geez you wouldn't even work with somebody interstate back then that was a big deal right that was a big deal because yeah oh you'd have to do an interstate phone call that costs a lot of money you know that costs more than just your local it was a big deal back then seriously

**Chris Gammell:** see now I guess the real question then is though like you know there's a lot of churn in that case right because there's a lot of manufacturing inefficiencies and everything like that but then I wonder about you know as we move into like an age of robots there's an article on the subreddit about like robots and stuff and just like you know like robots are potentially a threat towards certain jobs but usually the idea is that other jobs open up but I wonder about that as a as just a you know if you think about each small area of you know a country or region being like trying different things eventually the the best process is going to pop out of that right right and so I wonder I wonder if like some of this lack of churn and waste actually you know obviously we talked to Eric last week about you know like less waste but you know like having having that waste as just kind of like a development lab in a manufacturing environment right like company A does it this way but down the road company B does it that way and then because company B can get it done a little bit faster it becomes like a survival of the fittest right like you talked about right of course

**Dave Jones:** Darwin always wins folks yes right

**Chris Gammell:** yeah oh dearity

**Dave Jones:** meh

**Chris Gammell:** meh all right

**Dave Jones:** meh

**Chris Gammell:** meh

**Dave Jones:** meh I'm just you know yeah I I don't see the argument here really I just okay use use whoever you want to use

**Chris Gammell:** okay I will

**Dave Jones:** because ultimately that's what people are going to do anyway

**Chris Gammell:** yeah

**Dave Jones:** you know you can't well I know you can try and mandate this by law right and a lot of countries do that right x amount of you know x amount of you know x amount of your project this government project must be supplied by you know Australian suppliers

**Chris Gammell:** right yeah

**Dave Jones:** or whatever that's that's very common especially in the military and other big you know industrial kind of things that the government give a toss about

**Chris Gammell:** right

**Dave Jones:** so and even in the US right you guys have lots of state-based rivalry right like oh all the jobs must stay in the state and all that sort of jazz

**Chris Gammell:** sometimes yeah yeah there's like government contracts and all that crap like politicians fighting to bring stuff back but that's that's a mess that's yeah that's no good right once again

**Dave Jones:** next goodness hey that's stupid come on finish the crowdsource funding crap that's stupid Ubuntu Edge thing's not gonna hit its target

**Chris Gammell:** oh yeah even though they got 11 million dollars pledged yeah

**Dave Jones:** 32 million bucks they're like 20 million bucks short with two days left or something whoop-dee-doo

**Chris Gammell:** yeah I'm not I'm not too surprised let's not mention this kind of stuff right it's like oh well well if you want to go the other direction if you do want to instead of giving up money in order to buy something you could offer up something that other people might want to buy and you can get paid for it also known as companies stop doing R&D and instead try and crowdsource designs so Samsung is currently running a contest for up to $10,000 basically if you integrate a flexible screen you can get up to 10 grand for it and of course it's all voting and everything else and the usual contest crap but I don't know I don't think anything would actually ever come out of this you know like it's like yeah you might get some ideas but I think there's something to be said about the designer ethic you know like not the ethic even just like the having smaller people the smaller teams that actually design stuff versus crowdsourcing on ideas sometimes just doesn't doesn't strike me the right way

**Dave Jones:** what are the terms and conditions of this thing like what happened do you sign over your rights what is the

**Chris Gammell:** oh yeah let's see official rules there we go yeah but I mean come on these things are always especially the bigger company you get the rules are always like we own you we own your idea everything you do for the rest of your life of course that's hyperbole but uh you know and then like if you're not in an eligible state they basically when you have a lawyer actually look at the the contest rules

**Dave Jones:** your lawyer has a has a heart attack they do

**Chris Gammell:** yeah oh yeah yeah you gotta have something small and stupid and done done quickly and shoddily like the 555 contest right that's the only way it's ever fun and not for the people that put it together oh boy

**Dave Jones:** yeah they don't get much bigger than samsung so yeah i'm sure they've got this thing

**Chris Gammell:** oh yeah this is a so legally 11 page document on how to uh

**Dave Jones:** yeah yeah oh goodness yeah

**Speaker ?:** yeah

**Dave Jones:** fail yep that's a fail

**Chris Gammell:** so uh what have you been working on in the lab anything lately is uh mostly uh cough circuits cough circuits

**Dave Jones:** no that's no nothing nothing just you know moping around the house i've hardly even been to the lab jeez i don't know if it still works you know i get back there and there's cobwebs and everything

**Chris Gammell:** turn lights on even you know the light bulbs pop they flicker

**Dave Jones:** and just die oh boy i've been in

**Chris Gammell:** the throes of troubleshooting lately and i had possibly i don't know how much of the details i can talk about it but i had one of the so it's work obviously yes it's work it's uh it's one of the most frustrating problems i've ever had before today you know

**Dave Jones:** is it analog or digital

**Chris Gammell:** uh it ended up being both actually um but you know you know like the phrase uh the mark of an insane man is to do the same thing over and over again

**Dave Jones:** over and expect different results

**Chris Gammell:** and expect different results right well i got into a situation today where i was forced i ran out of other options i was forced into insanity today and it turned out

**Dave Jones:** just keep pushing the button monkey style i know work work work work

**Chris Gammell:** what it ended up being what so like the the the situation at least was i i was i had these pluggable units right and between unit a and unit or sorry there's base a and base b that i was plugging into it would work in base a and it wouldn't work in base b oh and so oh my god it was the worst thing i've ever i not the worst thing that's that's that's a lot i've had problems that went on for you know two and a half weeks with that kind of insanity but yeah this is this is a single day thing but yeah that same kind of thing of of you know like it works here it doesn't work here it's the same thing what the hell's going and honestly the difference was like it seemed like it was geographically based so of course my mind started racing to all these different things i'm like oh are there like magnetic fields over here oh is there like is it is it like a weird a weird weird ground plane that it's attached to or like what's going on here right and it was of course it was nothing like that but

**Dave Jones:** uh right no that's right

**Chris Gammell:** yep what was what was the one that you've experienced in the

**Dave Jones:** past oh i've had ones where you know a similar thing like oh it would work in chassis a and it wouldn't work in chassis b right and it turns out that you know marginal uh marginal uh capacitive loading differences between the builds in the two units you know like it was so on the design was so on the edge that it would work in one and not in the other yeah and and yeah as you say you move it around and that would sort of like jiggle the internal stuff and it sometimes work and sometimes wouldn't and oh you know and it changed slightly changed with temperature and and of course if you put it in this corner of the room that that's that that's under the air conditioning outlet yeah so you get no you know half a degree cooler in that side of the room and that's enough to cause it to you know and then you start being technical minded you start thinking of the most complex reason possible of course you're right you know and then that just leads you down so many garden paths it's just ridiculous

**Chris Gammell:** well yeah and I started like looking at the layout and everything you know and I looked at like your mind just goes yeah you're right your mind goes everywhere right I mean like yeah like I started and especially especially with like analog problems you know like you think about temperature you think about you know just like vibrational type stuff you know like the what's it called the microphonic effect or whatever that is yeah

**Dave Jones:** yeah in your surface mount caps yeah yeah if you actually you know all you got to do is put your coffee you know sometimes you would have a fault where you put your coffee mug down on the table and that would cause it to trigger you know because there's a little microphonic effect going through to your board right and you want to talk

**Chris Gammell:** about exercise and insanity when you walk by someone's cube and you just see them tapping on their desk

**Dave Jones:** right

**Chris Gammell:** like uh bill are you are you okay I just gotta get it I gotta get it to happen again and it all

**Dave Jones:** comes down to base you know and it all comes down to some fundamental theory like you know when when I had that problem with the static discharge from the chair right every time I got up from my chair oh yeah would cause and you know electrostatic impulse which would then be picked up by the circuit which would you know cause it to trigger an hour later or do get into mode which then causes an error an hour later so you wouldn't correlate the two

**Chris Gammell:** you know

**Dave Jones:** yes you wouldn't correlate the two you know because it's a long term data logger so you wouldn't you know so you can't possibly correlate the two it's just next to impossible you know and just weird things like that

**Chris Gammell:** yeah

**Dave Jones:** I've had tons of those weird electromechanical you know vibrational temperature shock all sorts of you know yeah

**Chris Gammell:** I think the thing that I really like doing and actually what ended up helping me today is following the current I mean obviously that's a pretty common thing but maybe for the younger people out there but just being able to do like voltage stack ups so you know that there's one amp of current flowing in this 10 ohm resistor and it's like okay you know there better be 10 volts at the top of that resistor or else something's wrong right it's you know it's getting diverted somewhere like that that has almost you know usually there's some component of that in the analog side of things you know at least DC analog right because you start getting into high frequency AC stuff and then your cap starts shunning stuff away but you know like that method usually helps me maintain sanity that's the important thing thou shalt test

**Dave Jones:** voltages yeah

**Chris Gammell:** well yeah you always talk about rails but yeah the stack up is what really you know and writing you know having papers still you know hey yeah yeah

**Dave Jones:** writing stuff down yeah

**Chris Gammell:** writing the stack up on your schematic too that that'll save your I feel like I could have gone bald at every amount of hair I was ripping out so right did you solve it I did solve it yes it was a hard fun

**Chris Gammell:** tell us

**Dave Jones:** what the

**Chris Gammell:** well it was the voltage stack up that's what I can tell you

**Dave Jones:** oh it was okay yeah

**Chris Gammell:** but what was

**Dave Jones:** causing it what was

**Chris Gammell:** bad assumptions really so like current was flowing somewhere that I didn't think would be flowing and it was flowing in different modes effectively so

**Dave Jones:** okay so this is a new design issue is it yeah right okay

**Chris Gammell:** right

**Dave Jones:** right and this is what the first time you built the prototype is it

**Chris Gammell:** yeah yep

**Dave Jones:** right and you didn't simulate it

**Chris Gammell:** I did simulate it but I changed stuff last minute that's another thing right when you start getting into changes like you know that's another thing that I've been noticing a lot lately too you know as you get as you get towards like release dates and stuff like that you can kind of sense that tension like you know I always had these very friendly you know interaction with my co-workers always but man it's like that palpable edge that people start getting towards you know it's like you can tell as you get towards dates it just starts to get different and it's like I don't fault anyone for it right it's just always yeah everybody's got their own thing to do and it's just human nature right but that's when you really make the crazy mistakes because you're like we'll just try this no no try this try this just try anything just try everything that's oh goodness that's when it really gets bad and you can never prepare for that stuff either right I mean it's not like you're sitting at the beginning of a project you know a year beforehand being like well I'm probably going to freak out in about 12 months I probably won't have thought of the following things and I'll probably freak out so it's tough to deal with goodness I'm amazed by things like this do you see this backscatter communications thing like think about I think about things that are difficult to test and difficult to work with and then this backscatter method of communicating it's just like how do you test this shit

**Dave Jones:** you just write it and it works or it doesn't you know you just write your code and does it work or it doesn't you know it's first hat if it doesn't work well how do you start troubleshooting it

**Chris Gammell:** yeah so what this is though it was so it was dangerous prototypes who posted about this but it's actually people from the University of Washington basically the idea is you have an antenna and then a PCB that's attached and then by either absorbing or reflecting ambient RF signals like you know a TV station so you might pick a certain frequency yeah the resonant frequency whatever your antenna is you can basically transmit information and so the demo they show is like swiping your finger across like a cap touch pad or whatever and then being able to translate that you know on or off characteristic to the little widget next to it both of which don't have batteries

**Dave Jones:** and both yeah both widgets don't have batteries they're just getting the parasitic power from the

**Chris Gammell:** right but it's actually yeah and then

**Dave Jones:** modulating that

**Chris Gammell:** right well yeah it's yeah the modulation being like I'm going to steal all of the localized RF or I'm going to just reflect it that's kind of the idea yep and uh the only thing I didn't get about this demo was that they showed uh like an RFID type of demo where they they transferred quote unquote money from one device to another but in that case I think you would need enough uh power to power something that actually would be able to control you know like your bit swapping because if you're going to translate okay Dave I'm giving you you know five Australian crazy Aussie bucks uh I need to know what the actual bit pattern is to to make that transfer right and it's like see then you'd have to power the thing that well does that bit flipping right

**Dave Jones:** well here comes the you know the crux of this thing what use is it right

**Chris Gammell:** yeah

**Dave Jones:** it's like you know yeah it's great okay fantastic novel terrific you know golf clap okay everyone applaud them yay and you know fantastic for doing this but then like what's the practical application

**Chris Gammell:** well I don't think they're at that stage I mean this is this is a paper really

**Dave Jones:** because you have to rely on some sort of potentially intermittent ambient signal it's just stupid just put a battery in the thing like you know I mean seriously it's you know yes it's novel but who would rely on this technology under what circumstances would you rely on using on there being this ambient

**Chris Gammell:** condition it's from like a swath of spectrum though Dave I think it's like there's always there's always energy in the spectrum that's the idea oh

**Dave Jones:** come on no it's just got a fail written all over

**Chris Gammell:** this is this is an academic exercise

**Dave Jones:** exactly it's an academic exercise

**Chris Gammell:** yeah

**Dave Jones:** when the you know as you said like the power is so low and the amounts of data are so low but then you've got to do some processing on data like you know you may as well you can power these things for a year on a coin cell battery anyway so why not just do that

**Chris Gammell:** right

**Dave Jones:** you know and then avoid and then avoid all the any potential issues with the back scattering and ambient signal I mean it's just it's pointless is anyone else with me I mean I'm sure there's a couple people with you it was novel when I saw it too but yeah it's novel yeah that's a good way to say it it's novel but that's where it's going to stay right

**Chris Gammell:** well maybe you never know what this kind of stuff you know

**Dave Jones:** maybe oh yeah maybe

**Chris Gammell:** yeah

**Dave Jones:** no but any technology which relies on you know random ambient stuff is just it's just going to fail okay so I

**Chris Gammell:** would say definitely if it was you know talking about like energy harvesting for that kind of like that's always crap

**Dave Jones:** of course you know like

**Chris Gammell:** RF energy harvesting is like what are you guys doing here you know

**Dave Jones:** well no there's a couple of niche applications where it's useful

**Chris Gammell:** maybe there's a couple

**Dave Jones:** of niche applications right yeah if you're in

**Chris Gammell:** a really high high RF density area you know I think that would be maybe but yeah dearity anyway all right well we don't really know what's going on there anyway so let's let's just leave that for now speaking of other things that I don't understand or I did not understand I thought this was brilliant so remember those movies or YouTube videos a while back where it was like an LED circuit and the guy would like flip switches and the LEDs would turn on well he finally posted all of his schematics not like people guessing at him like a lot of people got him right but he posted all of his schematics and they are brilliant how he actually did it I mean like he's bypassing stuff with a lot of inductors he actually had like signal generators inside the battery stuff oh it was I just I love this kind of stuff it's first off I hate puzzles I mean I know that like that's very anti-engineer but I just want the answer normally yeah exactly there's

**Dave Jones:** more elegance in the answer than trying to figure out the solution sometimes

**Chris Gammell:** I can appreciate it without bashing my head into the wall but that's why I'm not a researcher right I know this that's right that's right so but yeah these are really really fun I mean like just just like how he was the mystery behind it and everything so he's he's posted all of his LED stuff it's it's a lot of fun very cool yeah so

**Dave Jones:** he's bypassing leads with inductors and diodes yeah a lot of that kind of stuff capacitors and yeah

**Chris Gammell:** it is a little more complicated than I thought it would be I will say that right I know I

**Dave Jones:** expected there to be this complexity in there yeah you know and there's more once again there's more than one way to skin a cat here you know he's done it all you know RF trap kind of so to speak or you know frequency trapping kind of analog method but there you know there's other ways to do it as well yeah so yeah no neat another neat

**Chris Gammell:** project that I don't know how much press it got but this is Todd someone I know actually from locally but I really love this project so Todd Bailey and a couple of his friends they took old CRT vector monitors do you know what a vector difference is between a vector monitor and a normal monitor a vector

**Dave Jones:** monitor they come from the TV days are we talking about TV vector

**Chris Gammell:** monitors I believe so I think the way he explains to me is that like it doesn't have the raster already built into the set so basically you have to drive it to all the different locations from like oh right oh we're just talking about

**Dave Jones:** a vector right now I'm thinking of something else sorry so it's kind

**Chris Gammell:** of like it's like an oscilloscope effectively like that kind of screen but like much bigger and so him and some friends they they basically it was a FPGA project that so they built a driver for this vector monitor and then they wrote this old school asteroids demo for it yeah this is actually a couple weeks old now but yeah that the and the demo is just like really awesome you know it's like old school graphics and everything but then if you actually dig down into the tech I got I mean I've talked to Todd a lot about it too if you dig down into the tech you know like it's a lot of really cool you know driving mechanisms and like all the all the logic behind it then he actually drove you actually built the driver boards and everything so definitely a cool product project to check out if you like you know FPGA is interface and analog and of course right there you got my attention so yeah and of

**Dave Jones:** course yeah everyone you know a lot of people have a vector scope they have an oscilloscope you know which can be pressed into service often for that sort of thing but yeah I mean this comes from the old Vectrex you remember the Vectrex game back in that night this is before you were born anyway the Vectrex was a vector graphics based video game system and a lot of the arcade nerds out there will know what I'm talking about and yeah and it did that you know it actually drew a ship as a triangle you know on the screen rather than you know dots and a raster based system as all the other video games were back then this one actually did it using vectors and it's called the Vectrex Google it my son I shall there you go yeah I always wonder why I remember seeing one of those in the local shopping center back in the 80s and lusting after that you know so I just thought it was incredible yeah yeah

**Chris Gammell:** yeah this old I mean like and this this looks like it I mean like it just kind of shows like how hard it was to build this stuff back in the day too because I mean obviously Todd's doing this with an FPGA but like think about doing with discrete logic and everything too and it just it gets crazy so yeah it's a and a lot of high you know high speed high speed DACs and op amps and everything too lots of awesomeness so got it oh what else what else what else

**Dave Jones:** you're involved in a meetup

**Chris Gammell:** I am me and Cleveland meetup yes and I didn't mean to mention that to everyone so thank you so we're we co-opted a potential amp hour tagline we we're calling it charged conversation oh dearie yes so if people are in the Cleveland area or if you're coming through Cleveland or if you want to start your own I mean I don't care if you if you start one in Sydney perhaps or you know the Silicon Valley basically it's just going to be people you know drinking beers talking circuits that's kind of the idea so hopefully hopefully it works and beer is optional of course but you know hanging out getting to know people in the local area that's that's a a really important thing because I've kind of I've kind of been realizing like as I sit in the back and my my cave you know I hate right I interact with my co-workers but it's not that often and it's like I know that like the engineer you know stereotype but sometimes I just you know I want to bounce ideas off of people that's that's the real value I think of I mean having co-workers is nice from a social aspect but man like there's nothing better than like being able to bounce an idea off someone just even talk out your problems right I mean obviously I could do it once a week you know like and that's that's just a really nice thing to have so having that in a in a meetup capacities is good too you know once a month get together and hanging out and talk about projects and stuff I thought about

**Dave Jones:** doing that as well because yeah I am yeah one of your stereotypical anti-social engineers yeah you know I just don't like you know hanging out with other humans really you

**Chris Gammell:** should start a charge conversation group in Sydney we can we can just make it the name could be like a you know and then there could be one in New York and one in LA and you know

**Dave Jones:** well I already have this thing called the EV blog if you haven't heard about that you know I can use that brand

**Chris Gammell:** yeah but you can't well maybe you could have EV blog meetups elsewhere but uh anyway uh I guess you could

**Dave Jones:** do that you think amp hour meetups are superior to EV blog meetups no I'm

**Chris Gammell:** not calling it an amp hour meetup I'm just saying it's it's called the charge conversation meetup with MJ Lorton and the amp hour so that's why because we couldn't call it just one because it's me and Martin ah right of

**Dave Jones:** course of course I got to hang out

**Chris Gammell:** with Martin again and uh you know he

**Dave Jones:** says hi cool yeah because he's he's got oh thank you yeah say hi back

**Chris Gammell:** yep it's it's good to know other humans in the area actually I got to hang out with Dale Doherty too he was uh he came through town for uh the editor make or publisher make um no there you go yeah real nice guy so it was that's good I'd like getting to know people like that so well I'm I'm

**Dave Jones:** having a visitor this Friday somebody's dropping by the lap oh really yeah yeah yank yeah he's coming over here nice so he thought oh yeah turn on the camera drop by you know I'm yeah very cool yeah why not you know don't uh don't get him sick right yeah yeah might not be good um yeah but he's like my second visitor to the lab in like two years you know well it's

**Chris Gammell:** not like you have like a sign on the door

**Dave Jones:** like stop on no they yeah exactly I'm

**Chris Gammell:** sure you'd have some more if you if you offered so it's uh right yeah don't worry folks Dave will do a meetup eventually he was really excited when we started talking about this idea at the beginning and then of course he got sick so he'll he'll come around eventually and then he'll be like oh I've always wanted to do this kind of thing like he always does I've always talked about doing a radio show with some nerd from Cleveland oh I've always talked about doing crowdsourcing yada yada yada sure Dave we all believe you yeah speaking of meetup so uh I am still working on the venue but we will be having one in at the open horse open source hardware summit summit yes the open horse the open horse summit is down the road it's a uh equestrian uh dissection group but uh the open source hardware summit uh will be we'll be in Boston and we'll be having a meetup uh I've already set up a tour of uh I talked to the guys at Bolt the the hardware accelerator there so we will be getting a tour Thursday night but we'll be having an event around that as well and uh yeah looking forward to it hopefully a lot of people that are going will be able to hang out like we talked to uh some of the folks from spark funnel be there and everything so right excited about that definitely will be you know making fun of Dave for not flying overseas for that kind of thing

**Dave Jones:** have you finished the amp hour swag yeah

**Chris Gammell:** oh yeah it's all done

**Dave Jones:** it's all done I see I haven't seen it folks so if it sucks ass it's all me it had nothing to do with me yep it's all

**Chris Gammell:** me that's right and if it's awesome it's it's all me right it'll probably just be meh yeah right okay yeah oh goodness

**Dave Jones:** sake yeah yeah so there is amp hour swag and there's eev blog swag in the yeah open hardware summit bag yeah and I saw

**Chris Gammell:** uh actually uh where I met Dale down in Akron at uh tiny circuits um they're gonna have a board in there too so there will be at least three PCBs inside the bag which I think is more than they've had in any other beers which is was surprising to me and Dave when we were

**Dave Jones:** talking about that that is very surprising yeah so yeah I thought you know because they're cheap and they're easy to do and they're durable and they're fun and yeah and you can do lots of useful things with them so yeah I'm surprised there's not more I'm surprised the bag isn't filled with

**Chris Gammell:** PCBs right yeah I'm sure they will be eventually yeah after we pioneered the way of course yeah yeah let's see anything else on the list that you

**Dave Jones:** want to talk about oh bloody hell I don't know well it's largest antenna yeah what about

**Chris Gammell:** that uh that quad Kickstarter you see that thing there's actually a new uh so like as it's like an off-the-shelf Kickstarter but it's already hackable and everything or it's already it's an off-the-shelf quadcopter rather sorry all right okay yeah so I was thinking about you for that because of your canyoning idea yeah it's

**Dave Jones:** gotten to the point where yeah we've bumbled around on our canyon copter idea so long it's like well there's no point doing it yourself anymore you just buy the off-the-shelf bits and there's your solution you know and maybe some code you know whack on some sensors and some code but the physical aspect of it you know there's so many people doing so many of these things yeah right off the shelf now it's you know they just work you know yeah so and that drives the price

**Chris Gammell:** down of course it's like you know 3d printers as well you know that drives the price down it gives more variety you can make them hackable and everything and and the thing that's always an interesting to me about that kind of stuff is that you know like most people don't care about any of this stuff under the hood I mean not not like our people right now not like the people listening to this but if you're still into the public at large they don't want they don't want the fiddly bits they don't want the early adapter stuff they want the application layer stuff right they want they want what you're trying to do with that kind of thing of I want a quad copy that flies in canyons right so if you just write the software that makes it navigate canyons and put some floaties on it like you talked about and some waterproof cameras like that adds enough value that that becomes an entirely new product then and it's kind of crazy seeing that stuff from a you know from the maker perspective and kind of as as the maker movement grows up to that's going to keep happening I think of you know this different layers built on top of each other like ninja blocks right that was you know built on top of the beagle bone right most people don't care about the beagle bone but the ninja blocks is more is more of a compelling case and then you know maybe there's something else that actually maybe there's an appliance that integrates a ninja block in it right and eventually have to get cost out but it's interesting just seeing each of the layers kind of built on top of one

**Dave Jones:** another yep not like layers by 3d printers shock horror just want to print shit yeah they don't want to dick around with it right right you know and well yeah they're not quite there yet no you know but anyone who produces one that just works regardless of how you know how you don't maintain it yeah and it just continues to work and work and work no matter how much you abuse it and not maintain it then well they're going to win this is actually

**Chris Gammell:** dave asking for a 3d printer folks if you couldn't tell yes that actually works yeah exactly yeah yeah and uh you know and then early adopters kind of yell about it and it's that's okay we've been in the yelling group as well right oh boy all right so reminds me

**Dave Jones:** i've got to um finish making well i've got to start sorry making my uh thing for

**Chris Gammell:** the sydney maker fair oh yeah did we ever have enough guesses on that i stopped watching the thread we actually

**Dave Jones:** did post a thread about it there's yeah there's a thread there a couple of dozen that sorry a few pages of guesses so i won't say if anyone's right or wrong yet we'll leave it until the end yeah the person wins all right maybe we'll see that's if i can actually get it

**Chris Gammell:** built yeah well that's sad too let's try try and get healthy first uh next week on the amp hour we will have michael osman of hack rf and the ubertooth project uh both of which have uh well hack rf or hack rf is still in process it'll actually be the funding campaign will end the day of when when our recording's released so if you're interested in that look at that first because you won't be able to listen to our show and then be like oh that's so awesome i wish i saw it so definitely look at it first but you can also look at ubertooth is another thing that he worked on which was an open source uh bluetooth debugging kit that we actually did talk about in show 49 i believe um and it's a cool little project and it's still going it's all open source and everything so michael will be on here next week and we'll talk all about rf and sd that hack rf is an sdr excellent yep yep and he's crossed this four hundred thousand dollar uh threshold on his kickstarter so he has

**Dave Jones:** right so it's definitely no no no his

**Chris Gammell:** threshold was eighty thousand to make it is four hundred thousand with his was a stretch goal and now he's going to also release a two-day course that he does for software-defined radio so uh

**Dave Jones:** right okay we'll talk about it he's definitely met his original funding

**Chris Gammell:** goal oh yeah yeah he blew past that so awesome yes it's uh it's exciting it's uh it's gonna be it's gonna be good when

**Dave Jones:** can we see the first Chris Gammell crowdsource oh when i when i make

**Chris Gammell:** something that's worth crowdsourcing how about that dave right okay for now there's just contextual electronics that's

**Dave Jones:** not stopping anyone else yeah well that's

**Chris Gammell:** true uh uh but no contextual electronics is uh signups coming so that's i'm not doing i'm doing traditional you know sign up and then you pay me money and then we do a course together so i guess that's crowdsourcing in that you sign up early you sign you pay before you start uh right yeah but we'll have hardware by the end cool all right uh i guess we'll uh yeah feel better man yeah yeah try it i'm gonna go make not only add that i'm

**Dave Jones:** gonna go talk to mailing houses yeah bloody hell yep and that's

**Chris Gammell:** why i don't do crowdsourcing

**Dave Jones:** being successful sucks folks that's that's that's what we're saying yes

**Chris Gammell:** we're all we all really feel bad for

**Dave Jones:** you dave so yeah right thank you

**Chris Gammell:** yeah good all right man we'll see you next week

**Dave Jones:** bye you

**Chris Gammell:** whiny whiny whiny whiny whiny you

**Speaker ?:** you
