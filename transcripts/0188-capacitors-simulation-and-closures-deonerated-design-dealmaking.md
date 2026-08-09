---
episode: 188
title: Capacitors, Simulation and Closures - Deonerated Design Dealmaking
url: https://theamphour.com/188-capacitors-simulation-and-closures-deonerated-design-dealmaking/
---

**SPEAKER_01:** This is the F.R. Podcast, recorded March 10th, 2014. Episode 188, Dehonorated, Design, Dealmaking.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Who currently resides in the beautiful state of Florida.

**Chris Gammell:** The craziest. Do you ever see the stories, the news stories for Florida? There's some crazy shit that happens out here.

**Speaker ?:** I know.

**Chris Gammell:** There's a new late night talk show that me and my wife love, Seth Meyers, the guy that used to be on SNL. And he has a segment called Fake or Florida? Because all the news stories sound crazy.

**Dave Jones:** I can picture what that is, yep. Yeah, yeah. Right.

**Chris Gammell:** But yeah, I'm back in sunshine for a week or so. Right. And currently residing in an Airbnb location.

**Dave Jones:** On Wi-Fi, so yeah, this could go to crap, folks. Yeah. I hated, I flew into Florida once. Oh, man. I just wanted to get the hell out of there. Oh, man. Because of the... Well, for one thing, I thought I had arrived in Mexico. You know, all the signs were in bloody Spanish, you know. Oh, yeah, yeah.

**Chris Gammell:** There's a large Cuban population down here as well. Yeah, I know. It's huge. So that contributes to that.

**Dave Jones:** Yeah, but I flew into the airport and I went, did we arrive in Mexico by mistake? I mean...

**Chris Gammell:** Well, it's not the worst thing. I guess you don't drink tequila, so that's not the worst thing if you drank tequila. What, you were in, like, for Disney World or something? Is that why you were here?

**Dave Jones:** It was a stopover to get to Orlando, so...

**Chris Gammell:** Yeah, right, right.

**Dave Jones:** Yep, so we stayed a night. Which is also in Florida, yeah. Oh, well, yeah, well, it is, but yeah, then we hopped flying from Miami to Orlando, yeah. Oh, yeah. So, yep.

**Chris Gammell:** Yeah, yeah, it's an interesting state. It's just nice. I mean, you know, compare this to Cleveland. I think if I can make this part of my regular shtick to get the heck out of Dodge for two months a year, you know, that would be... Right. That would be a good thing. It would keep me sane. I like Cleveland, I really do, but you can't beat sunshine sometimes. Yeah, well, yeah, it's just, you know, it's zero degrees sometimes, so...

**Dave Jones:** At least we're not Detroit.

**Chris Gammell:** At least we're not Detroit. Yes. I haven't done that for a long.

**Dave Jones:** So you're, like, living the same lifestyle as I am now, where your wife has suddenly realized, oh, you don't have to go to work. You can... We can do anything we like. So she...

**Chris Gammell:** Yeah, right, right.

**Dave Jones:** Packed the bags and dragged you off to Florida.

**Chris Gammell:** Yeah, yeah, that works well until you realize that you can't go out to eat every night, like on vacation. So that's a slow adjustment. Why? It's expensive to go out every night. Oh, right, okay, right. I'm a cheapskate.

**SPEAKER_01:** Right, yeah, yeah.

**Chris Gammell:** I drink beer. I drink a lot of beer when I go out to eat. I don't know, but obviously you don't. No. Yeah, that adds to the wallet and the waistline. So those two things are no good. So...

**Dave Jones:** I just got back from the Hunter Valley, which is a wine region. I saw that.

**Chris Gammell:** I saw your tweet pictures. Yep. How was that?

**Dave Jones:** Oh, yeah. It was good. We drove up there and stayed a night up in the Hunter Valley. Very nice. That's nice. Yeah. Australia makes great wine.

**Chris Gammell:** Not as good as New Zealand, in my opinion. New Zealand is better. Oh, okay. Aussie wines are okay. There you go. Go Kiwis. Yeah.

**Dave Jones:** I think you'll find in the international circles that's not right. Everyone values Australian wine more. I think you are talking about your ass. Yep. Yeah. Nothing new here, folks. Yeah.

**Chris Gammell:** Business as usual. Yeah. Well, you know. It goes both ways. So what's going on electronics-wise for you? I saw you're testing boards. You've got tons of boards going out, huh?

**Dave Jones:** Yeah. Testing boards. That's just sucking up all my time. It really is. And, yeah. But, yeah, I was surprised at how quickly I could test these suckers. Yeah, that was fast. Once you get a jig that, you know, 17 seconds per board, that's three different modes, that's flipping switches, that's handling stuff, that's moving panels around. You know, that's pretty quick.

**Chris Gammell:** It's pretty quick. It is definitely quick. I've had, so for analogs, obviously that is an analog test. But for analog stuff, I've had tests that go, you know, 20 minutes, you've got to do warm-up. Of course. Yeah, yeah. You know, you could pre-warm-up sometimes, but then you have to step and settle and step and settle with, like, multiple channels and stuff like that. Yeah. So, yeah, 17 seconds is really, really good. It is really quick. So people should check out that video. It's a good video. And that's why you made that video about the, what was it, the current source, the 1A current source?

**Dave Jones:** The current sources. Yeah, I've done actually two videos on those showing two different types of current sources. So, yeah, I've got to pack and ship those. I've got to do documentation for that as well. So that's today's task, hopefully. And then I've got to order more parts. And then I have to go to the post office again and ship more parts. And, oh, man. It just never ends. So sorry, folks, that I haven't been doing a lot of videos recently. Yeah, it's just been sucking a lot of my time and family stuff as well. So it all adds up to you get nothing done.

**Chris Gammell:** Right. Well, it's, you know, a major own job, really, right? I mean, at least you enjoy it, though, right? No, exactly. That's important. It's good. No.

**Dave Jones:** And somebody, interesting, following on on the testing thread, somebody on YouTube or somewhere commented that, oh, why don't it be a good thing for like a flying probe tester? Why don't you do a flying probe, you know, at the manufacturer, you know, at the manufacturers, the assemblers often have these flying probe testers. And that, well, they're expensive. But if they have it, right, then it makes it, wouldn't it make sense to stick the board in the flying probe tester? And, well, you know, in theory, yes, in practice, not that easy because, A, the machines are expensive. So they usually don't have a lot of them, right? You know, assembly houses might only have one, you know, they've got one flying probe tester. And so that becomes a bottleneck. And you've got to physically, like, lift up the hood, put the, you know, take out the panel, put the panel in. And, you know, and by the time you do that, it's almost, you know, the same time as my little jig with, you know, the human sitting there and, you know, testing around. And I can build multiple jigs. That's the thing. Right. To then operate in parallel. So I can have, you know, I've worked at assembly houses where I've designed, you know, 20 different production jigs, all identical. And then they have 20 operators sitting there all testing them, you know. You know, so it's a massively paralleled thing. And if you do with flying probe testers, well, it becomes like a bottleneck. So that's flying probe testers.

**Chris Gammell:** I always think, I think of flying probe too for, like, high complexity stuff where you have, you know, a wide range of voltage you're testing. You know, like you have, what, three tests on there?

**Dave Jones:** I have three tests on three ranges, yeah.

**Chris Gammell:** Yeah. So that's not, I mean, that's not a small amount of tests, but it's pass fail as well. I think flying probe, I think, you know, testing multiple connections, you're testing shorts, you're testing opens. You know, it's just, it's probably, what, 20 plus tests for really making sense for a flying probe machine? No, I think so, yeah.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Yeah, I mean, so that would be what I would think about is just the complexity side of things. But, you know, it still, it could work, you know, but I think you're just going to pay more for it. Oh, of course. Yeah, yeah. I think that's what comes down to it.

**Dave Jones:** No, and mostly it always, it's always better to do a purpose design jig for the job. You know, that's what it almost always comes down to.

**Chris Gammell:** Yeah, well, yeah, I think really depending on complexity, that's what I would go with is complexity-wise. But I think in your case, you definitely made the right decision, especially because you were able to modify what, you know, you're not even making a custom, you're making a modified of your actual design, which is even better. So that's great.

**Dave Jones:** Yeah, it's too easy. I whipped those boards up, you know, in a few hours, you know, it was nothing. And then send them off for manufacture and, you know, yeah. No, too easy. And you can get caught in that cycle of trying to really get every last second optimized out of your testing. And sometimes it's just not worth it because, as I mentioned in the video, it actually takes longer to pack, to wrap and pack the boards than it does to actually test them. So why dick around, you know, trying to optimize a few seconds out of your test? You know, as long as you get it down to a certain point, that's, you know, good enough.

**Chris Gammell:** Now, do you regret the decision to pack and ship all that stuff yourself? Because I actually made a decision. I made a decision this week to offload all that stuff personally. You did. And I actually referenced you. Do you still think that's a good decision?

**Dave Jones:** I still think it is a very good decision because, A, I still get to keep an eye on things, which I like to do. Okay. And, B, well, there are a couple of logistical reasons why I can't just give it all to MailerHouse and get them to send it. The first of all is that my Australia Post account, I have to deliver them to my local business, what they call a business hub here. So, and you can't just ship them there. So it's not like, you know, the assembler house can just, you know, take them to their local post office. That's not how it really works, you know. Gotcha, gotcha. And ultimately, me just printing out and applying the labels is such a small step in the scheme of things. I worked out even for 1,000, no, for the, yeah, for 1,800 boards or something, it's only like 10 hours work. It's like 10 hours work to print out labels and put and stick them on the already stuffed padded envelopes I'll get with the, you know, fully tested units already in there. So, you know.

**Chris Gammell:** So that's already in the labeled packages or in the actual packaging and stuff as well?

**Dave Jones:** It'll already be in the padded bag. The padded bag will be sealed and all I've got to do is print and stick on the labels. And there's, you know. And there's, once again, there's some logistical reasons why I can't just print out the labels and send them to them, send them to the assembly house or get them to print it. There's some logistical reasons with how the Australia Post system works and stuff like that, so.

**Chris Gammell:** Gotcha.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah, well, that's good then. But no, I see that. So I decided this week to offload all that stuff. Yes, you did. Partially, you know, I'll be honest. Partially out of, you know, just not being used to it. I don't ship stuff out very often.

**Speaker ?:** Yeah, yeah.

**Chris Gammell:** Of course. Yeah. And so ramping up my operation fast enough, I was worried about that. I did doddle a little bit. I've been known to doddle in the past. Yep.

**Dave Jones:** How many units are we talking about here? We're talking hundreds, right?

**Chris Gammell:** Yeah, hundreds. It's not thousands or anything. But it's, you know, international. I've never done international stuff before. Yeah, that gets tricky. Yep. So is that something you have to do then, or like customs, or how does that work?

**Dave Jones:** Oh, well, yeah. The new Australia Post system I've got in place, my new business account with them, the software that I'll log in with takes care of everything. So it prints out the customs forms and all that sort of jazz. Yep. So I suck in all the information in a database. Yeah. Yep.

**Chris Gammell:** Okay.

**Dave Jones:** So I do a little bit of pre-processing work on the database. And then once I've got that database sucked in, it's a pretty easy job to print out address labels and customs forms onto labels, which I just slap on the front and back of the padded envelope. Very nice.

**Chris Gammell:** Yeah. So that's kind of the point I was getting to is like, if eventually, you know, if this keeps going for contextual electronics and I keep shipping boards in the future, I could definitely, you know, realize some cost savings by doing all that stuff. I was pulling that logistics in-house, doing that kind of thing. But for now, the decision was let someone else do it and be done with it.

**Dave Jones:** And ultimately, it means more money in my pocket because, you know, if you hand everything over to someone, it's like we've talked about with the kits before, right? Yeah, you can go to your SparkFronts or your Artifruits or, you know, your whoever it is. And, yeah, they will produce your kit. They'll make the boards. They'll assemble them. They'll test them. They'll ship them. They'll do everything. And you get, what, 10%, 15% or something, you know? It's a small – I think it's about 15, isn't it?

**Chris Gammell:** You'll get like – Oh, I don't know. Yeah, 10 or 15. I never know.

**Dave Jones:** It's a small – it's the same as writing a book. You know, if you write a book, go through a normal publisher, you're only going to get 10, 15% of that retail price. So if the book sells for, you know, $100, you're only going to get $10, $15 per book. But if you self-published it and sold it for $100, well, you get, you know, if it costs $5 to print it, you get $95 profit. You know, there's a huge difference. Yeah, there's a huge difference in the profit margin.

**Chris Gammell:** Yeah, what it came down to for me was actually I talked to a friend about it and he mentioned – you know, he basically was talking about – we were talking about the cost differences of doing it myself as well. And he's like, well, calculate your hourly rate of like shipping and stuff.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** And that's when it really started to make sense of offloading that to someone else. It seems like in your case, because you have the optimized process, your hourly rate is still high enough that it makes sense to do it.

**Dave Jones:** Yes, I've done that calculation as well. And before I had this Australia Post system, no, it wasn't worth my while. But now I've spent a couple of months setting up this system. Yes, it's, you know, I still, you know, it's even at, you know, a couple of hundred dollars an hour or something, you know, which would typically be our hourly contract rates, right? You know?

**Chris Gammell:** I still haven't made a couple hundred. Right. Okay.

**Dave Jones:** Well, you should be charging, dude.

**Chris Gammell:** Okay. I'll start doing that, dude.

**Dave Jones:** Never work for less than three digits.

**Chris Gammell:** Yeah. I like that.

**Dave Jones:** No, seriously, as a professional in the industry, you know, if you're working for 50 bucks an hour or something, you're working too cheap. I agree with that. Or you're working in a commodity industry, I guess.

**Chris Gammell:** You think? So to speak. Yeah. You're saying that going less than three digits makes it a commodity industry?

**Dave Jones:** Well, it depends. A, it's going to depend on what country you're in and what industry you're in.

**Dave Jones:** Of course. Yeah, I think so. If you're in, if you, you know, if you have a service that somebody, you know, desperately wants, then you should be charging them, you know, three digits an hour and not two digits an hour. Yeah. But if your service is just like everyone else's, right? Right, right, right, right. And they've got 10 people to choose from, you know, then you're, well, you know, it's a different story, right? Yeah. So, no, but no, seriously, that's a typical electronics design engineers industry contract rate would be, you know, it's not $50 an hour, it's going to be $100 an hour.

**Chris Gammell:** Yeah, no, you said a couple hundred, that's what I was, that's what I was scoffing at.

**Dave Jones:** It could be for a more specialized thing.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? You know, look, if somebody came to me and said, you know, look, we want Dave Jones from the EEV blog.

**Chris Gammell:** The Dave Jones.

**Dave Jones:** The Dave Jones from the EEV blog. Well, like, they can't get anyone else, you know, they want me. So what am I going to do, charge them $50 an hour? Of course not. Right? I'm going to... That's true.

**Chris Gammell:** You know, yeah, yeah, that's, you know. That makes sense, pricing-wise, yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Exactly. So... I don't think many people ask for the Chris Gammell, so... Right. Not yet. Not yet, folks. You just wait.

**Dave Jones:** Oh, dear. But, you know, that's common, but that's going to be totally vary from industry to industry. And likewise, you can also get those rates if you're known to them and they trust you and they've used you, you know, and they trust that you're going to do the job. And somebody else is a big risk, right?

**Chris Gammell:** Right, yeah, there's no dither. There's no dither in there. They're not like, oh, he has to go teach himself this and charge us the hours for that. It's, he's done this, he can produce it. Yeah. Yeah. That makes sense.

**Dave Jones:** It's like I'm not going to pay, you know, a couple hundred bucks an hour to an assembly house, right? Because I can get any assembly house to do it, right? I'm going to pay, you know, 20, 30 bucks an hour, right? I'm going to pay that sort of, you know, minimum wage kind of price.

**Chris Gammell:** Yeah. Well, whatever you can get away with, right? That's just the economics of it. Well, you know.

**Dave Jones:** Yeah. Well, no, that's how assembly houses typically work. They will, you know, if you need an hour of your operator's time, I mentioned this in the video, they will charge you, well, you know, what they have to pay the operator plus, you know, company overhead and a bit of profit margin and all that sort of stuff.

**Chris Gammell:** Amortization and all that other crap. Yeah.

**Dave Jones:** All that sort of stuff, you know, that goes along with having employees in-house and all that sort of stuff. But they're not going to charge you, an assembly house isn't going to charge you a couple hundred bucks an hour for testing boards, right? That just doesn't happen.

**Chris Gammell:** Right, right. Unless they have the flying probe guy.

**Dave Jones:** Unless they have the world-famous assembler, Mr. Fuji. Yeah. I don't know.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Oh, dear. Yeah. Yep. So that's, yeah, that's how it works. But I'm sure we'll get lots of comments about, or everyone's, you know, different countries and, oh, God, a couple hundred bucks an hour is, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** A thousand times more than what I'd charge, you know. Well, yeah. Sorry, we can only talk about our own industry, our own part of the world, really.

**Chris Gammell:** Yeah. Well, speaking of pricing, what is this? So you've posted an article about competing with free last week. What is this all about, basically, that you can't compete with free?

**Dave Jones:** I did. Let me call it up again, because I forget it.

**Chris Gammell:** Dave's not paying to remember stuff, folks. Yeah.

**Dave Jones:** Well, you, hey, I didn't, you got me on early to the show, because it's daylight saving there, so I didn't have my last minute cram to, you know, last ten minute cram.

**Chris Gammell:** We could, like, put on some girl from Ipanema. Please hold while Dave reads the list. Dear Eddie.

**Dave Jones:** It's an article from Tech Dirt from someone called Mike Masnick, and I can't remember. Somebody tweeted it or something. I don't know. Found it somewhere. Anyway, saying you can't compete with free is saying you can't compete, period. And the article, basically, I'm probably paraphrasing here, because I haven't read it, but basically, if you're in an industry where, I think he gives the example of, let's say you have to build, you know, a million iPhones, and you've got to put $100 million into building the factory, right? Or you've got to build some wafers or something. Then it makes no difference what that initial outlay is, whether it's $100 million or whether it's free. If you can't, you know, compete in the market and make your money elsewhere, then you shouldn't be in business. That's, I need to read the article more.

**Chris Gammell:** Sorry, you've caught me on the spot. The way I remember it is, it's partially a discussion of sunk costs, which is what you're mentioning there. Sunk costs, yep. Yeah. The other discussion is about marginal value. And basically, so like for digital distribution, it's...

**Dave Jones:** That's what they're talking about. Digital distribution versus shipping a real product.

**Chris Gammell:** Yeah. Right. But I think that's an interesting... I think this kind of brings up interesting stuff for hardware, because there's two things. One, it's very tangible to talk about price for hardware, right? We can go out, we can look at the cost of components, either, you know, in single quantity or in, you know, large quantity, and then add some kind of multiplier to it. But then there's also, there's a... There's that je ne sais quoi, right? You know, people pay more for Arduino because of brand and loyalty and stuff like that, and that's on top of the actual component cost. Because some people go over to China and produce an Arduino clone for $8, right? And they sell it for $8. They don't produce it, and they'll say, no, I still want to go pay $30 for Arduino. And I think that actually comes into it, the whole calculation of, you know, if you can't do free, you can't compete well, okay, but maybe if you can't do hardware plus multiplier, if that's your, you know, your free point for hardware, if you can't do that or above, then you can't compete, you know? I think it brings into different questions when it's with hardware.

**Dave Jones:** Yes, it does. Their example was the difference between making an automobile and making a movie, for example. You know, both have this upfront cost, but then you have to produce the car, right? And let's say the car costs $20,000 to make, and you only sell it for $20,000 because it's a cutthroat industry, well, you've made no profit. Right. And likewise with the movie, if you cost, you know, if it costs $100 million to make the movie, but then the distribution cost is free, because while people are downloading it, right, people can, you know, pirate and download it for free, then your profit is still zero. Right? So they're both identical cases. That's what the article is trying to get at. And, you know, it's all about that profit margin. And, well, either way, whatever industry you're in, whether it's automobiles, movies, or electronic hardware, you ultimately have to figure out how to make a profit.

**Chris Gammell:** Yeah. And if you can't... How to be as cutthroat as possible with still making a buck and being able to invest in the future, because that's what the profit really comes down to, in my opinion, is being able to turn around and then build the next revision, you know, build up your next factory or build up your next run of boards with that profit.

**Dave Jones:** That's why I went to the effort to set up all this distribution system, because, yeah, I can just outsource everything and make, you know, 10%, 15% per item. But, you know, it's like, it's like why, you know?

**Chris Gammell:** Right. That's true. Well, and if that, say you make another 15% on top of that, because you're bringing that shipping in-house, you can go take that and buy your next set of parts and build your next Kickstarter or whatever your next project is.

**Dave Jones:** And then you can take another holiday and go to Florida.

**Chris Gammell:** There you go. Yeah.

**Dave Jones:** Join me down here. And afford to actually eat out. Yeah, there you go.

**Chris Gammell:** I'm such a cheapskate. You have no idea. Oh, so am I.

**Dave Jones:** Oh, boy. I think we all are. I think it's inherent in engineers. Oh, hardware people.

**Chris Gammell:** I, you know, my wife looks at contextual electronics and she's like, she's like, you know, I can't believe it works because, you know, would you pay for it? And I'm like, no, I wouldn't. But, you know, I also went to school for it. And I like to think that I would if I, you know, I hadn't learned this stuff already. But, you know, I'm very appreciative of the people that are paying for it and participating. And so that's good. Oh, goodness. So speaking of things that can't compete, we should talk about former guests of ours that are now. Oh, probably without jobs. They've gone down the gurgler. We don't know. No, no, no.

**Dave Jones:** They've probably still got a job because they got bought out.

**Chris Gammell:** No, their IP got bought out. They didn't get bought out.

**Dave Jones:** Oh, their IP. Right. So even. Right. So they're it. Right. So they didn't go with the IP.

**Chris Gammell:** I don't. Maybe they did. I mean, maybe it was an acquihire, which is, you know, sometimes a thing. But so that's what they call it in like Silicon Valley. When like when Google buys a company for like, you know, five million dollars and it's like 20 people and it's not really, quote unquote, worth it. Right. So basically, that's where you're basically buying out the talent more than anything else.

**Dave Jones:** I got it. OK.

**Chris Gammell:** Yeah. So but the news here is that Silicon Labs, they basically bought out a bunch of the Touchstone Semiconductor IP, which is, you know, the Touchstone.

**Dave Jones:** Well, they bought all of it, didn't they? I think so. They bought it all lock, stock and barrel for five million bucks.

**Chris Gammell:** It says it says no, no, no, no. 70 analog products. That's what the thing is. 70 analog products. And it does list all of the types of stuff they sold. But it says one point five million dollars.

**Dave Jones:** Oh, sorry. One point five million. Yes. One point five million. That's nothing. I know. I know. That's the the venture capitalists put 20 at least 20 million dollars into Touchstone. Yeah.

**SPEAKER_01:** Right. So they get paid back first.

**Dave Jones:** Right. Right. Exactly. So this is, you know, fire sale price. This is, you know. Yeah. Yeah. Which makes me wonder. It's a bargain. It's a bargain.

**Chris Gammell:** Definitely. I mean, I think so. I mean, I think they, you know, I was I was thinking about, of course, after the fact, I was I was thinking about them the other day for a sensor project I'm doing is just, you know, like low power stuff is very important. But yeah, man, that's that's crazy. I mean, like, that's really cheap. Totally. We don't know the whole story. And we should we should say that up front. We don't know the whole story. No, no, we don't. We do know that Silicon Labs bought them. Silicon Labs also bought another of our former guests. Right. They bought a Gekko. Who's Gekko? Oh, they bought.

**Dave Jones:** Yeah. Yeah. Yes. The Gekko line of low power micros. Sorry. Yeah. I forget. Anyway, they had the tiny Gekko and the giant Gekko. Yeah. And all that sort of jazz.

**Chris Gammell:** Yeah. But yeah. So basically.

**Dave Jones:** They did. They bought them like at a decent price. I think. I think they sold that at a profit. I don't think they were going out of business and bought them at a fire sale price like they did with Touchstone. Yeah. Because that's what. That's the story with Touchstone is they basically went out of business. They went into receivership, you know, and they liquidated the assets or whatever. And they sold them off to the anyone, you know, probably the only bidder, you know, who bought them for pennies on the dollar, as they say. Right. In America.

**Chris Gammell:** Right. Where things go like this all the time. Yeah. And there was an article about this. I can't find it now. But someone had written about, it was basically like kind of like a rumor around Silicon Valley about Touchstone. Right. I think it was Steve Taramovic wrote about it. But basically hearing that, yeah, that they were going out.

**Dave Jones:** Yeah.

**Chris Gammell:** Can't really find it right now. Novich. So, yeah, it's just a shame, though. I mean, it's basically what Steve wrote about, though, is basically it's a tough world when it's everything is a fabulous model. Right. So Touchstone was doing fabulous. They were they had engineers, I think, here.

**Dave Jones:** The only thing they had was their IP. That was it.

**Chris Gammell:** Right. That was it.

**Dave Jones:** There was nothing else. You know, they probably were working out of rented offices. You know, I mean, they. I think they said that when they were on the show. They have people and their IP, you know. Yeah.

**Chris Gammell:** Right. Why wouldn't you do it out of rented offices?

**Dave Jones:** Exactly. They were probably even renting the licenses to the Cadence or whatever mental design tools to design the ICs. You know, they don't even buy those. You know, they rent those per month. You know.

**Chris Gammell:** Maybe. Yeah. Yeah. That's kind of weird. I've heard that sometimes they also for startups, they'll kind of gift them that with like a contract on the back end. Like, if you start making money, we're going to charge you out the ass kind of thing. Right. Yeah. Yeah.

**SPEAKER_01:** Right. Yeah.

**Chris Gammell:** But yeah. I mean, it really is a shame. It's because those guys that came on, you know, they were great. Like Brett and. Yeah.

**Dave Jones:** There's not many two new analog startups, you know.

**Chris Gammell:** Right. Yeah. And I guess that's what it really. It really questions, what the question is, is like, is this a sign of, you know, this point in history or is this a sign of, you know, for the rest of time that like that analog startups are very difficult to do because you don't have that IP?

**Dave Jones:** Well, we've talked about this, right? The problem is nobody wants to buy your parts unless you're a big manufacturer. If I'm, if I'm working for a company, my ass is on the line when I choose, when I spec in your parts into that design.

**Chris Gammell:** Yeah.

**Dave Jones:** And unless I absolutely have to, I'm going to go with the big vendor. You know, I mean, that's just the way it is. Right. Yeah.

**Chris Gammell:** That you're buying, you're buying the name and the, and the guarantee behind it. Yeah. You feel like a Tommy boy.

**Dave Jones:** That product's still got to be manufactured in five years time. You know, I mean, that's a, that's, that's a big deal. So. Yeah. So what we're saying is that engineers are tight asses and scared shitless.

**Chris Gammell:** That's. Yeah. Right. Yeah. We're really tight. We're coming off good here, man.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Yeah. It's, it's a tough world out there. So, well, I wish the best to all those guys. Hopefully they, they land on the feet. I think they're, I mean, they were really talented guys. I'm sure that they're, you know, all of them will be able to, it's not like analog designers are in short supply or are not sought after. Right. So they, I'm sure they're all going to do just fine, but.

**Dave Jones:** They'll probably do another startup. Hey, if there's money to be had, you know, use someone else's money. Hey, I don't think they use their own money. They use some, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** That's the thing to do, isn't it? If you can get someone else's money to play with, well, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** Why play with your own? Screw that.

**Chris Gammell:** Yep. Speaking of failure, we have another on the failure. I think one that probably deserves it a lot more. Radio Shack is closing 1100 stores. I haven't heard this. And no one said they were surprised. Right. So 1100 stores. I think they had about 5,000 worldwide or so. So, but, yeah, man. No one's surprised at all. Deerity.

**Dave Jones:** So what are Radio Shack these days? I heard they were getting back into components and stuff. Yeah. But they just went into consumer mobile phones and crap, did they?

**Chris Gammell:** Yeah. Well, that was a long time. I mean, people probably all saw it. Of course. I mean, do they have Radio Shack in Australia at all or no?

**Dave Jones:** So, yes, they were acquired by Dick Smith who are gone the same way as well. They were like, you know.

**Chris Gammell:** Yeah. I mean, it's so niche. It's just like, you know, how can you possibly have a, you know, unless you have a store in Silicon Valley, it's like, okay, well, sorry, the store in, you know, the middle of Cleveland is not going to be doing nearly as well as other places, you know, especially when there's other options online.

**Dave Jones:** Well, here, I don't know about you guys, but, you know, you can go into your local, your local, there's these, what are they, you know, general goods stores and they'll sell, you know, white goods and they'll sell you electronic products and stuff like that. And really they, you know, you can't compete with their buying prices and stuff like that. So the little Tandy store, you know, usually they Tandy as we call them here, not Radio Shack, you know, that, that little, it's usually like quite a small store, you know, and they usually can't sort of compete on that price and stuff like that. So, you know, that's right. Yeah.

**Chris Gammell:** And that's what they've all kind of, yeah, there's like the state side is like Best Buy. Like, I think that's what you were talking about. Best Buy. Yep. Yeah. Yeah. Formally Circuit City. Those all, then they're all going down because of Amazon and everything else, just the web kind of eats everyone's margins. But, you know, Radio Shack was trying to get back into stuff, you know, they started carrying Arduino stuff, stuff from the maker shed and all that kind of stuff. But even when I, I went into a couple of, you know, whenever I saw one, I'd pop in and just see what they had for that kind of stuff, see if they had any, any new kits or anything like that. They always kind of had limited selection too. And, and so I was always wondering, you know, if you're going to go for it, you got to really go for it. And yeah, exactly.

**Dave Jones:** You've got to become a, you know, huge retailer of that sort of product, you know, and carry everything.

**Chris Gammell:** And even then, I, I just, I question how big the market would be when there are so many options online. You're not offering like a huge discount to them. So, but the one that I have been interested in. So, um, last week when we talked or two weeks ago, when we talked about BeagleBone Black and how they're like kind of out of stock around the world. Yeah. Uh, I actually found one, I found like three or four of them at a place called Micro Center, which is a computer store. And it's kind of like this big computer center. There's a bunch in Ohio and elsewhere.

**Dave Jones:** Quick, flip them for a profit.

**Chris Gammell:** Yeah. Well, that, I mean, they were five bucks premiums of what they're listed for online, but, um, you know, probably shipping wise.

**Dave Jones:** You can still flip them for a profit at eBay, you know.

**Chris Gammell:** Yeah. Right. Uh, so yeah. And, you know, like they basically though, they have a whole section now where it's not just, it's not just, uh, uh, it wasn't just BeagleBone. It was also, um, uh, Adafruit, uh, SparkFun, Make, basically, uh, uh, Tiny Circus, who's a local guy. They're all around. They were like, they had a whole section there. So I, I think that's kind of where I would see stuff going. And I know that people in California, there's like fries and stuff like that. So there still will be stuff around, but it's, it's going to be, it's going to be difficult. I think, I think really they're going to end up being like storefronts for distributors like Adafruit and SparkFun and people like that. Sure. If at the best case scenario. Yep.

**Dave Jones:** Oh boy.

**Chris Gammell:** Oh well. End of an era. Just another one.

**Dave Jones:** No, exactly. It's the same thing happened here 20 years ago, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** And, uh, well, and that's the thing I don't know about there, but here it was right. You know, the local electronic stores like Dick Smith and Radio Shack stopped selling electronic parts like 20 plus years ago. Right. It's 20 years ago. Yet even just five years ago, people were going, Oh, they're not selling it like they used to. You know, it's like, dude, it was 20 years ago. 30 even like, you know, Oh man. Yeah. And you, you know, people just have no sense of time. That's the thing. Like our local Dick Smith, right? Store, which was a famous part store here operated by a famous guy, Dick Smith, who should we should have on the show sometime. He's an interesting character. If we could ever get him. And anyway, you know, everyone keeps complaining. Oh, Dick Smith went downhill when he sold, when he sold it to Woolworths, which is a big, uh, food chain here, right? He sold off the, he's all his stores. And, you know, everyone said that for like 20 years. Oh, it was never the same since he sold it off. And dude, you do realize he sold it in 1982, right? And it's like, they have no sense of time. No. I don't think you have sense of time either.

**Chris Gammell:** That's 31 years ago, man. That's not 20 years ago.

**Dave Jones:** People were still saying this in the mid 2000s, right? Oh, you know, when Dick Smith sold it, it went downhill, you know, so much better five years ago, you know, it's like, you idiot. People have no sense of time. I love it. I love it. There's an article on panelization.

**Chris Gammell:** Yeah. How to panelize your boards. That's interesting. So you've done a lot of this stuff before as well. Yeah, I've done a lot of videos like this. Yeah. Yep. I think that's, I mean, it still kind of scares me a little bit. I've always had other people to do that for me. So, you know, it's.

**Dave Jones:** Well, that's very common. You know, some companies will not panelize their own boards. They'll just send it off to the assembler. They will panelize it. You know, they'll organize, you know, and do it and get the boards manufactured and all that sort of jazz and take care of all that sort of thing. But no, I always panelize my own boards. It's like, screw you. I don't want you doing something wrong. You know, I want, I want to do it exactly how I want.

**Chris Gammell:** Have you had it go wrong before?

**Dave Jones:** Oh, well, I did. It, it, I showed it in a video just not that long ago where I let PCB, oh, what's the name? The European German PCB tool.

**Chris Gammell:** Oh, a Euro?

**Dave Jones:** Yeah. PCB tool. PCB tool or something in Europe. Yeah. Anyway, they wanted to, they, they shipped me the thermal oven that I've got here, right?

**Chris Gammell:** Oh, yeah, yeah, yeah. That's right.

**Dave Jones:** And, and, and they sent it and I sent them the board. I thought they were just going to ship me one board, right? So, but they go, no, we'll, we'll panelize it for you. Do you want my panel file? I'll give them you my, but no, no, no, no. We'll panelize it. And they, so they sent me the panel and of course the, the tabs are in the wrong spot. Oh, that's right. Yeah. And, and you, when you break it out, because it's, my board's a nice front panel, right? That's right. So it's got to look good. So it's, you know, the tabs have to be in the corners, not on the sides of the board. And they, they just, when you cut them out, they leave little, little burrs sticking out of your side of the board. And it's fine if your board's going to be sitting inside a box inside your product. But, you know, when it's a front panel, it's a, you know, it's a lot different.

**Chris Gammell:** Yeah, definitely.

**Dave Jones:** So, yep.

**Chris Gammell:** Well, that's, that's a good thing to know. I mean, I, like I said, it's not something I do very often. So it's, it's good to have this kind of information. I think it's probably just something you got to, you got to, got to try it out and, and, you know, fail once or twice and eat the tooling, you know. Right.

**Dave Jones:** And they're only showing you one type of breakout tab here too. Well, you know, people, they go under a lot of different names, breakout tabs, mouse bites. Some people call them because they look like a mouse that's sort of bitten out a few holes. And, but they're only showing you one type. They don't show the, the round type. They don't show you the indented type. They don't show you, you know, there's more than one way to skin it than to skin a breakout tab. Yeah.

**Chris Gammell:** Yeah. Certainly.

**Dave Jones:** And then you can do a combination of V grooving and route breakout tabs on your board as well, depending on sorts of things. I did that for my previous microcurrent. It'd be half V grooved and half routed out, you know, because I wanted nice smooth edges on one side and the top and the bottom I did as V groove. So, you know, so you at least get nice, you know, smooth edges on your sides and stuff like, you know. So, yeah. So it's important if you care about what your board actually looks like, you know.

**Chris Gammell:** Right. Right.

**Dave Jones:** Yep.

**Chris Gammell:** Man, that's crazy. Well, how about we move from the physical to the not so physical and we talk about simulation. Do we have to talk about simulation? We do have to.

**Dave Jones:** We're talking about real hardware, electronics here.

**Chris Gammell:** We have to talk about two. These are relevant things, I think. So first off is that analog devices is actually killing multi-sim, which probably doesn't affect any people. I don't know if you've ever used it.

**Dave Jones:** I may have fired it up once, but no, I've never used it in anger.

**Chris Gammell:** Yeah. It was kind of weird. I mean, it was based on national instruments, actually. So it was always weird to me. I think some people, when they got into the flow, they liked it. But, like, instead of, like, having, like, a probe point, like an LT splice where you click on a line and it kind of shows you a signal, you actually put in, like, an actual, like, a DMM. And then you run two leads to it, right? Or, you know, a scope. Right.

**Dave Jones:** It's that visual kind of thing. Yeah, exactly.

**Chris Gammell:** And basically, I'm guessing, you know, this is an announcement that came out from Analog a couple days ago. So, but basically, I'm guessing this is just cost-cutting on their part and not enough people were using it. But, yeah, you know, whatever. I'm not shedding any tears over it, but I'm sure it's, you know, but this could be quite disruptive if you were, you know, if you buy into this kind of stuff. This is almost an argument. It's like sometimes you should pay for tools if you want to try and guarantee that you, you know, you could get access to it. Obviously, nothing's guaranteed, but...

**Dave Jones:** Hang on. What's going on? I thought multi-SIM was National Instruments.

**Chris Gammell:** It is. It is. So, they licensed Analog Devices, licensed it from National Instruments. Right. And then they gave it to people for free. So, you can still, I guess you can still buy it from NI. Right.

**Dave Jones:** Yes, of course. Yeah.

**Chris Gammell:** Yeah. So, I guess that's not as big a deal, but... Okay. Right.

**Dave Jones:** And what, it only supported the Analog Devices parts? Is that the thing? They have, yeah, they have like special bits in there.

**Chris Gammell:** They bought, they built in like their components so that you, they were like native, basically. You drop in, AD, whatever, you know, op amp or whatever. So, yeah, that... Got it. I mean, that is a nice thing to have.

**Dave Jones:** So, what's their reason for discontinuing?

**Chris Gammell:** Basically...

**Dave Jones:** It wasn't worth it. No one was using it. The bean counters came in. Because I'm sure, you know, they've got to pay National Instruments, right? Right, exactly. So, that shows up on the budget each month.

**Chris Gammell:** Yeah. You know? Right. Yeah, and that's true. And interestingly, I learned about...

**Speaker ?:** Oh, there we go.

**Chris Gammell:** What was that?

**Dave Jones:** We will now shift our resources towards supporting more Spice software programs. Okay. Right. Oh, I didn't see that. It sounds like they were getting too many complaints that, oh, your Spice models only work with your stupid... Or I optimize for your stupid free version of multi-sim. I don't want to use that. I want to use LTSpice or I want to use blah, blah.

**Chris Gammell:** See, but I think... And multi-sim is built on top of... I mean, there's a Spice engine in there at least, but... Oh, of course. Yeah, of course. Maybe it's tough to get this... I always have a problem with that anyways, trying to get the stupid external models to start working. You know, like the sub-circuits trying to work in the Sims.

**Dave Jones:** Yeah, that's always a bit of a pain. Yeah.

**Chris Gammell:** But that's... Yeah, so this one is just... Analog devices is canceling it. That's no big deal. All right. Yep. I actually learned... Did you know that TINA, like TI's... Right.

**Dave Jones:** Yeah, TINA or whatever it's called.

**Chris Gammell:** Spice program. It's actually not licensed for... It's only licensed for commercial use. You actually can't use it in an academic context.

**Dave Jones:** What?

**Chris Gammell:** Yeah, it's really weird.

**Dave Jones:** What sort of ass about system is that?

**Chris Gammell:** I don't know. It's basically... It's the same kind of thing where like... You know, these companies aren't building their own Spice simulators. And basically, they go out and they buy someone who built a Spice... You know, because Spice... The Spice engine is actually open source, right? So someone built something...

**Speaker ?:** Oh, yeah.

**Chris Gammell:** Yeah, of course. ...on top of it. And then either these companies go out and they buy it... They buy the people that did it. Or they... You know, they license it. And in this case, that one wasn't licensed. And... Yeah. So, you know. Screw TI. That's all I got to say. Well, if you're in an academic context, of course. Yeah. And commercial, it's like... It's no problem. It's like you can do it, no problem. But it's...

**Dave Jones:** No, it's just us about. It's just dumb.

**Chris Gammell:** I agree. You'd think it would be the other way around, right? Usually it would be like... Yeah, of course.

**Dave Jones:** That's how it usually works. Yeah. This is for non-commercial use, you know?

**Chris Gammell:** Right, right. Yeah. So, it's kind of weird. But whatever. Unbelievable. We... In the same vein, we will be having... Oh, crap. I can't find his name now, of course. The guy that tours around doing LTSpice. I think the guy that runs Switchercad. I think the one that Linear Tech bought, he'll be on the show in April, actually. So, I forget his name now. Excellent. But we will be talking tons of Spice, and we'll talk about that in a month or so. Terrific.

**Dave Jones:** Because I think he's the only guy who writes that LTSpice. Oh, really? Because he maintains it. Oh, wow. Yeah, I think that's it. I think it's him.

**Chris Gammell:** Well, that's even more impressive. I freaking love LTSpice.

**Dave Jones:** Or it was at one point. I don't know. Maybe it's getting too popular now that they might have dedicated, oh, an extra person. Part-time.

**Chris Gammell:** It's Mike Englehart is his name. So, we'll have Mike on the show in April. So, that'll be... We'll have lots of good questions for him at that point, I'm sure. Yeah. Yeah. So, oh, well. One down. LTSpice is still around. I'm happy. Yeah, exactly.

**Dave Jones:** But that's my simulator of choice these days.

**Chris Gammell:** I did. I think... I mean, come on. Who does... Unless you're using, like, a commercial P-Spice, you know, you're actually... If you're at the system level, like... Man. Did you know you could rebind the keys in LTSpice? The hot keys? Yeah. No. You know they have those funky-ass hot keys with, like, F2, F3. F3 is, like, trace. And then F4 is label. F5 is copy. Or delete. F6 is copy. You can rebind those. You can control C is copy now. I didn't know about that. You can change all of the hot keys. Yeah. Sweet. I know. That's awesome.

**Dave Jones:** I just never bothered.

**Chris Gammell:** I know. I didn't even know it was possible. I've... You know, because, like, you... You know how it is with, like, tons of programs like that. You know, like, so much... Even though we're hardware people, so much of our stuff is still software-based, right? We're doing spreadsheets. We're doing, you know, part searches online. We're doing CAD stuff. It's still computer-based. And, you know, you switch from a CAD program to a SPICE program, and your fingers are just all messed up. You know, it's like, oh, what button do I hit again? Yeah, yeah. You know, it's just... Even...

**Dave Jones:** What I'm doing... I'm sick of going from the lab here to home and having a different keyboard. So I'm now standardizing on my keyboards across all my machines.

**Chris Gammell:** Ah, that's smart.

**Dave Jones:** I'm getting the same wireless keyboard for all... I'm just sick of it. Because my notebook here that I'm recording this thing on is, like, you know, the function keys, you've got to actually hold down the function button and then press F3. You know, it's just stupid. Oh, no.

**Chris Gammell:** I hate that. Right? Yeah.

**Dave Jones:** Bloody notebook.

**Chris Gammell:** Yeah. Yeah, no, that's really smart, actually. Like, the standardizing process type stuff. I mean, you think about, you know, those small changes, like, oh, crap. You know, back up, back up, back up. You're like, how much does that add up over time? You know, years at a time of doing that. It's like, you may be buying yourself a year. You might have just bought yourself a year retirement, my friend. Exactly. That's good.

**Dave Jones:** Ah, no, it all ultimately gets pissed away, anyway.

**Chris Gammell:** Well, yeah, you know, there's still the forum, so... Yeah. All right. There was another... Oh, so the other thing, speaking of TI slash formerly National Semiconductor, right, they bought them, Webbench now can do modification. So this was something that just came out today. I'm always... I always regret talking about press releases, but this is actually kind of important because, you know, that's kind of what... It seems like TI National is kind of going towards with the Webbench type stuff. I still never really liked the simulation side of things. I didn't think it was full simulation. So hopefully this is kind of actually... You know, you can actually go add in extra capacitors, add in extra inductors and stuff like that. And I can only assume that if they're doing that, they must have added a full SPICE engine, whereas before it felt very, you know, pre-packaged, like you have five different ways that you can run this and look at it. So, yeah, hopefully it's better.

**Dave Jones:** And speaking of that, hang on. There's a new online schematic program.

**Chris Gammell:** Oh, yeah? Which one?

**Dave Jones:** Schematics.com. It's from... It's from... It's from... It is. EE Web. And Hearst have, you know, the big advertising marketing. Oh, yeah. Yeah. Yeah. Who own, you know, tons of electronic marketing sites or something. Yeah. Yeah. They've teamed up to create schematics.com. It's another online collaborative schematic tool. Oh, whoa, whoa. Sorry, what was that? Right. I don't remember. Where am I?

**Chris Gammell:** Yeah.

**Dave Jones:** You know, how many of them are there now?

**Chris Gammell:** There's got to be at least 20.

**Dave Jones:** Yeah. I've lost count. So, I don't know. You know, go and check it out if you want.

**Chris Gammell:** What's the point of this then, Mr. Sinek?

**Dave Jones:** Well, it allows people to collaborate with their schematics. It allows you to share and collaborate on your schematics. I don't know.

**Chris Gammell:** Oh, so it's pretty like social, I guess, and you can embed it.

**Dave Jones:** It's social, and you can, I don't know, maybe you can thumb it up or something, you know?

**Chris Gammell:** Yeah, clone it. Yeah, okay, so they clone it.

**Dave Jones:** You can comment on it, and you can, you know.

**Chris Gammell:** Right, so this is very similar to like Upverter, in-browser type stuff.

**Dave Jones:** Yeah.

**Chris Gammell:** Open an editor. Make you sign in, of course. You can sign in with your social account. Yeah. And I'm sure then I could share it with people, and yes. Whatever happened, it's just email and crap.

**Dave Jones:** No, and I can't just open up the editor without signing in. I've got to sign in. Right. Well, you can view it, but you can't edit it. And you can add comments on each, and you can comment on the projects, and you can, you know. Meh.

**Chris Gammell:** Meh. You know. Well, I have to look into this just because if they can suck in Kaikad designs, I'm interested. If they can't, they can go take a flying leap. Right.

**Dave Jones:** I'm going out on a limb and going to suggest that no, they can't. I suspect it's their own thing.

**Chris Gammell:** Proprietary. Oh, that's weird.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. Oh, man. Yeah. Next. Well, everybody's got to make a choice, you know. Well, speaking of Kaikad, Adam Wolf, former guest of the show, is doing – so one of the big complaints about Kaikad, obviously, I have a very vested interest in Kaikad. I'm very interested in it. Of course. One of the admittedly crappiest parts of it, even though you said it wasn't that crappy, is that it's terrible on the Mac. You have to build it yourself, and it is really just a bad, bad experience. So you have to either run a VM running Windows or Ubuntu, whatever, which isn't the worst thing in the world. But basically, Adam is now running a nightly build for OSX, so you can go and pull that down and do that.

**Dave Jones:** I still don't like this nightly build business. I think somebody should take charge and go, this is the stable version, right? Yeah. This is the current stable version. Here it is for the next three months until we officially release, in quote marks, the next version. And sure, if you want to play with your daily build, go ahead. Here it is. But otherwise, here's the version that everyone is using at the moment, or the majority of people are using.

**Chris Gammell:** Well, I'm going to go ahead, and I'm going to release my idea, because ideas aren't worth anything, right? But I actually would benefit greatly from this. I think a great business model would be to take Kaikad, which I think is pretty decent for what it is, and it could use some work still.

**Dave Jones:** No, it is becoming the de facto standard, well, it is the de facto standard free PCB tool.

**Chris Gammell:** Yeah, I think so. It's gaining so much traction, yeah. I think if someone took it and they went Red Hat on it, so you know Red Hat?

**Dave Jones:** Yes, and they provide, which is providing a prepackaged thing with support and all that sort of jazz. Exactly. So is that the correct thing?

**Chris Gammell:** Yeah, so they also contribute back. So basically, CentOS, which is, they're on CentOS 6 now. That is an exact, someone from Linux-based is going to yell at me, but as far as I know, it is an exact clone of Red Hat Linux, basically, because of all the stuff that's already open source in there. Basically, that's how they feed it back to the community. So the idea would be, there would be Blue Hat, the Kaikad, you know, service group or whatever. Basically, they would take Kaikad, they would develop it, they would have these regular builds.

**Dave Jones:** Can we call it tinfoil hat?

**Chris Gammell:** Tinfoil hat, I like that. Okay. Yes! Tinfoil hat. And then basically, then they push that back out, right?

**Dave Jones:** Well, you know, tinfoils can conductive, right? That's right, they can be shielding, right? It's electronic, it's conductive, yeah.

**Chris Gammell:** I've wrapped up, you know, cabling in tinfoil before.

**Dave Jones:** Either that or copper-clad hat.

**Chris Gammell:** There you go. Yep. I like it, that's great.

**Dave Jones:** Yep, let's trademark that.

**Chris Gammell:** Yep, okay, well, dibs, dibsy. Dude, I came up with it. Yeah, I know, well, I'm saying dibs for you, the amp hour. Oh, right, dibs for the ever ride. Yeah, right, of course. You want to share, do you? Yeah, of course, right, yes. You think we're buddies here, right? We're going to do business partners, Dave, 50-50, of course. Yeah, no, that's great, though. So, yeah, basically, it'd be that idea. And I think there's, you know, obviously, I can't do this on my own, and I don't think I'd have time for it. Oh, and now it needs. Yeah. Yeah, you need a significant infrastructure. You need people to support it. You know, Red Hat has support technicians. They have, you know, people that go out and do installs and that kind of thing. They do it on a corporate level. Basically, it'd be all the stuff that, like, basically, like Altium does, but basically, without the proprietary backend. And it would just be, and then, but then it ends up benefiting the community as well. I mean, it's maybe not pure open source, as some people like, but whatever. It's good for me.

**Dave Jones:** And what's the business model? What, you pay 10 bucks? You pay 20 bucks? No, no, no, no. To download it? What do you?

**Chris Gammell:** No. Well, I mean, I don't know about how Red Hat works, but I know that, at least on an individual level, but I know Red Hat on a corporate level, it's like you pay, like, a site license. You pay 20,000 a year, but basically, you are guaranteed it's never, you know, if shit hits the fan, then basically, you know, it's all open source. Yeah, it's all open source, and you can find people for it. And basically, you kind of build a community around it. You're paying for the support. You're not paying for the actual software. Right, of course. Which is technically what you're usually doing anyways, but whatever.

**Dave Jones:** So, how would you support KCAD in this instance? How would you do it?

**Chris Gammell:** Oh, well, it's the same kind of thing. So, Red Hat will develop a version, you know, Red Hat 16 or whatever it is, and then they say, okay, and then this is also CentOS 6, and then they push that out, and then it goes in all the reposts.

**Dave Jones:** Right, so you're saying it would be a specific build of tinfoil hat slash copper clad hat.

**Chris Gammell:** Yeah, right, right. Yeah, exactly. That's the idea, and that's how it feeds back to the community. And then there's, you know, individual packages in there. At least, again, this is how I understand it. I could be very wrong, and I'm sure someone can let us know. They always do. They always do. They're good at that, yeah. But yeah, so I think that would be a great idea, and I think that would benefit a lot in the community. I mean, I think CERN jumping in is a good start as well, but I think, you know, having Profit Motive there as well also helps move the community forward.

**Dave Jones:** See, I would – that would probably really tip me over the edge to really wanting to start to use this thing. Oh, look, there's a company that's taking care of, you know, making sure it's all – this build is super stable, and everyone's using it, and I, you know.

**Chris Gammell:** Yeah. Well, I mean, Adam's a good start there, right?

**Dave Jones:** I don't want to go in and download the daily build and fart ass around, I mean.

**Chris Gammell:** Oh, right.

**Dave Jones:** You know. Yeah, maybe. Well, no. Look, if I was looking to change, yes, I'd probably change to KeyCat, right? But that would be a pain in the ass, right? That would be one of my gripes, would –

**Chris Gammell:** Oh, yeah. You would – you would – I'd say if you do it in about two to three years, you'd be in good shape, probably.

**Dave Jones:** You'd be, you know, in better shape than now. No, I expect – yeah, I expect this sort of thing's probably going to happen anyway, I think. It's going to get more away from the daily build thing to, you know, somebody will come in and go, you know, here is, you know, the – The build. Build 12, you know, and here it is. Everyone's using that.

**Chris Gammell:** 12.04, right? How Ubuntu does it.

**Dave Jones:** That's what it needs. I mean, you know, when you're on a forum asking for support, people are going to go, well, what build are you using? I don't know. I'm building using 13.1.3.2 dated 12th of December.

**Chris Gammell:** Yeah, right, right, right.

**Dave Jones:** What the frig? Yeah. And I compiled it myself, you know. Yeah. You know, it's like, how can I help you, right?

**Chris Gammell:** Right. No, yeah, that's very true. You need some kind of standard reference point there.

**Dave Jones:** You've got to have a reference point.

**Chris Gammell:** They have that now. I mean, so I'm on BZR4022, which is whatever that is. I don't know how it correlates to the time.

**Dave Jones:** I still think they're too frequent.

**Chris Gammell:** That's like only every three or four months.

**Dave Jones:** Oh, okay. Well, that's okay. Yeah. That's better. Right. Yeah. Okay.

**Chris Gammell:** But. Right. Okay. I'll stop complaining. So maybe we're getting there. Yeah, who knows? But if anyone ever wants to talk to me about that, of course, you know, give me a shout. We can talk the logistics of, you know, the idea, right, the Red Hat clone. Yep. And then we can talk to Dave about licensing his brilliant name. My name. Yep. Tin foil slash copper clad hat. Because, you know, ideas aren't worth anything unless, you know, it's a name. Of course. Right, Dave?

**Dave Jones:** Unless it's got a cool name. That's going to make or break it. I'm telling you.

**Chris Gammell:** That's right. Yep. First, we need a logo. Right. Yeah. Yeah, that's funny. Oh, boy. I do want to say one other thing about Webbench. You know, as much as I gripe about Webbench, I do like, have you ever seen their little circles? You can kind of see it on the pictures they have here. Yeah, they kind of do. They do like a comparison matrix where they do like switching speed versus cost. Oh, right. Or size versus, you know, switching speed, that kind of thing. And then they have different bubbles. And basically, it's just a way of viewing data. That is probably, that has always been my favorite thing about them. And my gripe has always been the simulation side of things. So, if any Webbench developers are listening, good job on the bubbles. I'd like to see more of that. I think that's a really great way of visualizing data. But, you know, hopefully I'll have to try out the actual schematic stuff now. Right. But the bubbles are very, I really do like those. The bubbles. You're easily immune. You're easily pleased. Oh, my God. Yeah. Yeah.

**Dave Jones:** Oh, goodness. Yeah. That's sad.

**Chris Gammell:** What about these, did you see this AVX app note from a while ago? No. The 80% of SMD capacitor failures are from automated production? Says who? Says AVX, the capacitor people.

**Dave Jones:** Oh, that says AVX, the capacitor. Well, they'd know, wouldn't they? Yeah. Yeah.

**Chris Gammell:** Basically, it's two things. It's one is like the actual compression from picking up the thing with a vacuum bit. And then the other is, you know, and then also putting it down. And forcing it down. Plomp. Yeah. Yeah. But then also, I think because of the stresses, once it actually then solders up, because of how it's placed, and if it's on glue and stuff like that, it starts to create these micro cracks. And then, you know, that basically causes some crazy, crazy failures.

**Dave Jones:** Because they're ceramic capacitors. Hello. Ceramic's brittle. You know? I mean, these sort of things.

**Chris Gammell:** Well, and plus they show, I mean, they show the, I always think it's interesting looking at how ceramic capacitors are made. Like, I always, you know, you think, oh, okay, it's like a little chip thingy. You know?

**Dave Jones:** They're phenomenal. They've got, you know, hundreds of layers in there, some of them. They're just crazy.

**Chris Gammell:** It's like a wafer cookie, right? Except the wafer is the dielectric, and then the cream of a wafer cookie would be like the conductive part, right? Or however it would work.

**Dave Jones:** And that's why these things are microphonic, right? Right, yeah. These ceramic capacitors are microphonic, because they're basically a piezo transducer. That's what they are. Yeah, right. So not only can they pick up sound, but they can emit sound as well. You can make these capacitors sing like a generic.

**Chris Gammell:** Yeah. I've had inductors sing like crazy, but maybe they were actually, was it the capacitors that were probably singing instead?

**Dave Jones:** You can do multi-layer ceramics as well. Huh. Very easily. Yep.

**Chris Gammell:** We should start like a little ceramic choir, you know?

**Dave Jones:** We actually used to do this in production. They weren't actually ceramic capacitors. We were making our own hydrophone ceramic transducers, but exactly the same concept, right? Yeah, right, right. They're actually manufactured the same way, except they're designed as underwater hydrophones. And one of our troubleshooting tools was to have a capacitor meter that gave out enough voltage at one or two kilohertz that actually made these capacitors sing. So you'd stick them. So you'd stick the meter on the end and you'd walk along and go in, you know, yep, I can hear that one. I can hear that one. Oh, this one's dead. There we go. Oh, you wanted to hear it. There's our culprit.

**Chris Gammell:** Because it's a hydrophone. Yeah, yeah.

**Dave Jones:** Yeah, you actually wanted to hear it. It was actually a troubleshooting technique to find a broken, you know, faulty wiring in the big hundred meter section. You'd go along and make these capacitors sing.

**Chris Gammell:** That's great. Yeah. Yeah. I mean, that's similar to how, you know, speakers can act as microphones, microphones can act as speakers. Yeah. Speakers. Yeah. They're not very efficient, but... No, definitely not. Although I did learn... Did you know that they did that on a Beatles album? They were talking about that on Innovation Hub, where, like, there was some... Like, they couldn't do it back in the day. They couldn't get the bass big enough. So they had, like, some huge six-foot speaker, which then they turned around and used as a microphone. And that was... Oh, really? Paperback writer. It was, you know, like that boom, boom, boom, boom, boom, boom.

**Dave Jones:** Oh, right. Yeah, yeah, yeah.

**Chris Gammell:** Like, that really heavy bass. Really? That was how they did it. Yeah, it was awesome. I'll link the show in. It was... Yeah, it was Innovation Hub did... They talked about the Beatles back in... ...on the 50th anniversary. Oh, it was awesome. Yeah. That's great. I love it. So, yeah.

**Dave Jones:** There's so many things that can go wrong with ceramic capacitors, folks. Multilayers ceramic capacitors. It's a wonder they work at all. Well, okay. So now let's talk about this a little bit. They've been manufactured. They've been abused by the pick-and-place machine. They've been thermally shocked. That's true, yeah. You know, to buggery. And then, oh, man. And then they've been stressed and pulled from the suction of the solder, the tension of the solder joints.

**Chris Gammell:** The surface tension, right? Yeah. Bloody hell. When are you designing in electrolytics these days? Are you doing them at all anymore? Because I usually just avoid them these days.

**Dave Jones:** I will. I try and avoid, but you can get, you know, if you have to, if you want a large amount of capacitance at a large-ish voltage, you know, sure, you can get, you know, your 10 or 100 microfarad multilayer cement capacitors. But they're, you know, their temp curves, right? Yeah. It's just awful. And they're very low voltage, you know. There might only be, you know, three, you can get, like, three-volt ones, you know. Oh, yeah.

**Chris Gammell:** For the super huge. Right, right, right. Yeah. Unless you're going, like, 2012 sizes and something crazy like that, right? You have to go huge. But, yeah, I mean, I guess I'm thinking more on, like, board level these days. I just, I don't find myself, because I talk to people about this in Contextual Electronics. They're like, oh, well, I found, you know, these electrolytics, and they're, like, these, you know, they're small electrolytics. And I'm like, eh, these days I just don't bother. You know, if it's anything, if it's below 50 volts, why bother? I just go ceramic.

**Dave Jones:** Well, you know, it depends. I mean, and the manufacturers are, the chip designers, the chip manufacturers are realizing this, especially with voltage regulation, right? Or, you know, all your switch mode converters and stuff like that. They need, you know, a minimum output capacitance, for example. But traditionally, some of them also had a minimum ESR of the capacitor. That's right. It couldn't be too low. And if you, oh, you went, oh, okay, this data sheet says it needs 10 microfarads minimum output capacitance. Aha! You know, these days you can buy a 10 microfarad ceramic cap, right? So you're whacking your ceramic cap and, oops, oops, it oscillates, because it's actually too low in ESR.

**Chris Gammell:** Right, right.

**Dave Jones:** Whereas if you use just a bloody old fart-ass electro in there, it'll work just fine.

**Chris Gammell:** Yeah, right, right, right. Well, yeah, that's very true.

**Dave Jones:** They've had to redesign them.

**Chris Gammell:** I think, well, I think a lot of the new switching regulators are kind of moving away from that, though. That's at least the trend I've seen, is that they all talk about ceramics.

**Dave Jones:** They all talk about ceramics now. So they're all specifically designed to be stable with ceramics these days.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Yeah. But if you use a switch mode converter that was designed 15 years ago, you know, hey, we didn't have these large-value ceramic capacitors back then. So it was never an issue.

**Chris Gammell:** Last time I ran into a singing inductor, it was exactly that issue, actually. It was bad compensation, and then the inductor ended up singing because of it. Yeah. It was crazy, because the load, basically the load was a problem. Yeah. That's funny. It's just the same problem.

**Dave Jones:** This is interesting. They're talking about the crushed surface area where the suction cup picks it up, and it's great. Yeah. This is a good article.

**Chris Gammell:** This is a very nice app note I highly recommend. I forget who. Someone linked it on Twitter.

**Dave Jones:** Because on the good pick-and-place machines, you can adjust how much force it puts them down with. Oh, yeah. So, you know, because some parts are very delicate, like these capacitors. Leads, for example, if you whack down leads too hard, you can damage them. So, they have to program their pick-and-place machine, you know, to treat these parts gently.

**Chris Gammell:** Yep.

**Dave Jones:** So, yeah, it's important.

**Chris Gammell:** Well, same thing with picks. You see this thing from Mike, Mike's electric stuff, Mike Harrison. Did you see this video?

**Dave Jones:** I've heard about it. I haven't actually opened it. They're sensitive.

**Chris Gammell:** So, basically, squeezing a pick can make the internal oscillator drift. Right. So, highly recommend checking that out. It's crazy to see that actually happen in real time. Awesome.

**Dave Jones:** But that's not surprising. That's inherent. Once you know, you go, oh, okay, that's not that surprising, I guess.

**Chris Gammell:** No? That's not surprising?

**Dave Jones:** Just like they'll vary, just like the internal RC oscillator will vary with everything. You know, you fart halfway across the room, it varies.

**Chris Gammell:** Yeah, that's true. Yeah.

**Dave Jones:** It's an RC oscillator. Yeah. Yeah. And, of course, physical pressure on a chip is going to, you know, might impact the die, you know? So, where they're trying, you know, they've got a large part of the die. Yeah. A large part of the die is working as the capacitor and is working as the, you know? So, yeah.

**Chris Gammell:** Yeah, man. That's crazy. There you go.

**Dave Jones:** But no, I hadn't heard of it before, but hey, yeah, seems obvious.

**Speaker ?:** Cool.

**Chris Gammell:** Seems obvious now that we've heard Mike talk about it. One thing that does not seem obvious is how many frigging ARM chips are in the world. How many billions? There are now 50 billion ARM power chips in the world. Is that all?

**Dave Jones:** I, you know, I'm not terribly surprised by that number.

**Chris Gammell:** 50 billion?

**Dave Jones:** If you said trillions, I'd go, oh, shit. You know, but no, billions. Because I know that they sell, you know, just like a couple of billion a year. Like, minute, like 10 billion a year or something. It's not surprising.

**Chris Gammell:** No, not that many. Maybe last year, but not the years before it. I mean, that's the thing. Like, it feels like it now, but it's like the RAMP was so slow. And then, you know, finally getting up to the point where it was. I don't think this stuff really ever would have happened.

**Dave Jones:** They've been in phones a long time.

**Chris Gammell:** No. No way. Like.

**Dave Jones:** Yeah. I mean, they've been in. You're falling into the Dick Smith trap we were talking about before. Oh, yeah? Thinking that it's a recent phenomenon. I don't think it is.

**Chris Gammell:** I'm going back here. Hold on. Hold on. Hold on. Okay. So.

**Dave Jones:** Is there a graph over time? Total units versus time.

**Chris Gammell:** No, there's no thing over time. But I'm looking at, like, the announcements when they started doing stuff. Right? So it's all about when you start seeing stuff. I think the phones are really it. Right? Because you could buy an ARM 9, you know, ARM 7, ARM 9 for a long time. Yeah. Right? ARM 6 was announced in 2001, it says here. You know, and basically ARM 9 is 2003. You know, you could buy these for a long time. But it wasn't until I think that the ARM stuff started getting into, you know, the ARM A series started getting into phones and tablets and stuff like that. And the fact that phones and tablets didn't come out until what? I mean, like, the iPhone was really the start of that kind of whole craze. Technically, you know.

**Dave Jones:** Yeah, but I'm telling you, that was quite a long time ago.

**Chris Gammell:** In the scheme of things. No way, man. I think it is. Maybe in the scheme of things. I don't know about that. But anywho, there are now. So, okay. So what? iPhone came out in 2006? Yeah? Yeah, which is eight years ago. Goddamn, that's eight years ago. Uh-huh. Okay. Yeah, well.

**Dave Jones:** And the iPhone wasn't the first to use an ARM chip.

**Chris Gammell:** No, that's definitely true, yeah. I mean, uh...

**Dave Jones:** Mm-hmm. Mm-hmm.

**Chris Gammell:** Mm-hmm. All right, whatever. See what I'm talking about? But still, 50 billion is quite a lot. I don't care what you say. That's a lot.

**SPEAKER_01:** True. I won't argue.

**Chris Gammell:** Yeah. So 50billion.com. There's a 50billionchips.com. Oh, there it is. There's a graph on this site. Uh, yeah. Yeah. So 10 billion were shipped last year, in 2013. All right. That's crazy.

**Speaker ?:** Yeah.

**Chris Gammell:** All right, well, congrats to those guys. They're gonna keep going. You know what the crazy thing about all that is? What? So I watched, like, their stock price and stuff like that, their price through the roof and stuff like that. They're still not making any money on that stuff. You know? Really? They're like, as far as I know, as far as the last time I read their financial report.

**Dave Jones:** How are they not making money? They're like a fabulous, they're just selling IP cores. How do you not make money?

**Chris Gammell:** How do you get people to put this thing in everything, Dave? Well, you make it cheap. You make it cheap. That's right.

**Dave Jones:** Yeah, but even one cent per thing is still a lot of money.

**Chris Gammell:** One cent per thing, I guess, would be, what, 50 billion? And so 50 billion times .01 would be, what, 500 million? Is that right? 500 million over 10. It's still a lot of money. Over, since 93. So if you start selling in 93, that means you're not actually making any money until the past couple years. So maybe they're making money now. Maybe I haven't read it recently enough. But, yeah.

**Dave Jones:** Well, they just ship 5 billion, right? And I know it's not like one cent per chip. It's like, you know, I think it's like tens of cents per chip.

**Chris Gammell:** No, no, no, no. Oh, tenths. Tenths with an H in there of cents. Yeah. Oh. Yeah, it's not much at all. But I think that stuff's all hidden, too.

**Dave Jones:** Well, they're doing shitty business, then.

**Chris Gammell:** Yeah.

**Dave Jones:** Again, we might be talking about our asses. Once they've locked everyone in.

**Chris Gammell:** Well, I think that's what's going to be interesting, right? Right? What happens in our own. And this is what I've been saying. I've been saying this for years now, right? Because I saw Freescale switch over, and you see everybody switch over because it seems to make a lot of sense, and people are clamoring for ARM. And then, shoop, the rug gets pulled out from under you. You want ARM? It'd be a darn shame for us to break your process there, buddy. Translation, break your legs. Yeah. Exactly. The old mob mentality. Yeah.

**Dave Jones:** You're all right. I love it.

**Chris Gammell:** We'll see. We'll see. And that's why I stay away from microprocessors. All right, man. Well, I think that's it. I've got to get back to vacationing. But next week, you know.

**Dave Jones:** Why is the wife in the corner sort of wagging the finger? Yeah.

**Chris Gammell:** She's tapping her foot. All right. Yeah. Yep. I get beers calling my name. So, yeah. Next week, we don't have a guest schedule yet, but we hopefully will in a day or two. And it'll be a nice surprise. Woo-hoo. All right, man. I'll see you then. Catch you next time.

**SPEAKER_00:** Before I decide to keep my business with your place, I'd have to come by and have a look at your new operation. Hey, I tell you what. You can take a good look at a butcher's ass by sticking your head up there. But wouldn't you rather take his word for it? What? I'm failing to make the connection here, son. No. I mean, you can get a good look at a T-bone by sticking your head up a butcher's ass. But then, no. It's got to be your bull. Wow. iTunes reviews. YouTube reviews.
