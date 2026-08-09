---
episode: 219
title: Get Smart About Automation - Caducous Cyborg Concerns
url: https://theamphour.com/219-get-smart-about-automation-caducous-cyborg-concerns/
---

**Dave Jones:** This is The Amp Hour Podcast, recorded October 6th, 2014. Episode 219, Cautecus Cyborg Concerns.

**Dave Jones:** Welcome to The Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. Who is where this week? I'm in the office, talking into a shoe. In which office? In which state? In Pasadena, at the Supply Frame office, actually.

**Dave Jones:** Oh, there you go.

**Chris Gammell:** But yeah, I forgot a mic stand, so I happened to get a pair of sneakers in the mail, and now, well, I'll post a picture of my lovely setup.

**Dave Jones:** Go to theampower.com and you can see it. It's great.

**Chris Gammell:** Yeah. So, you know, sometimes you've got to MacGyver your situations. That's fine. Whatever. No big deal.

**Dave Jones:** It's cool. I can dig it. I almost wasn't here today. Oh, yeah? Why is it? Because my internet was down for like two and a half days. Oh, yeah. You've been saying that. What is that?

**Chris Gammell:** At the labby? They must be installing the Aussie broadband, finally.

**Dave Jones:** Yeah, right. Yeah.

**Chris Gammell:** So, how do you survive without internet at the lab? That's what I want to know.

**Dave Jones:** Well, I have to use my phone or tablet as a backup. The tablet's got its own 3G card, and I've got a separate plan for that, so I can use that as a backup. But we've talked about this before. It just sucks ass. You're so unproductive on a tablet, let alone a phone.

**Chris Gammell:** Right, right, right.

**Dave Jones:** You know, like, there's just so much I can't do on a tablet, or it's just so messy, I just don't want to do it. You know, like, I can't open things in multiple windows. I can't, just stuff like cutting, pasting, and dragging, and, you know, things you take for granted.

**Chris Gammell:** Everything's messed up. All your workflow is getting interrupted, yeah.

**Dave Jones:** Yeah, totally.

**Chris Gammell:** Well, so, like, I'm working on these websites now, right? And, like, we have to basically make tablet stuff, but then when it really comes down to it, like, like, I know that people are going to look at it on tablets, and they're definitely going to check to make sure it can be on tablets, but it's like, who's really going to be sitting there, like, in their living room on a tablet, unless they have no other option? Like, and that's the reason to do it, is if you don't have another option.

**Dave Jones:** Yeah, yeah, yeah, exactly.

**Chris Gammell:** It's, yeah, kind of ridiculous.

**Dave Jones:** No. Even when I go back home, and I'm limited to my notebook, heck, you know, my 17-inch screen notebook, right? I'm going, where's the separate screens? Where's the, you know? Like, it's just, yeah, it's just, isn't nearly as nice. So, yep. First world problems to the max, right? Yeah, first world problems, yeah, that's right, yeah. Because humans need to be productive.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, even if we do, we could be on the way out. Oh, you're going to that? I was going to actually go back. I'm going to that. Well, let's save it, let's save it. Anyway, what my internet problems were, yeah, broken fiber down the road, apparently. Oh, really? Okay. Yeah, yeah. I don't know if they automatically detect that sort of stuff, or whether or not, you know, they have to wait for someone to complain, and then if they get enough complaints, they go, oh, something might be wrong. And, yeah.

**Chris Gammell:** Well, they can, like, ping devices. I know they can, from, like, the central server, they can usually...

**Dave Jones:** Well, they can, whether or not they actively do it and then act upon it is another thing.

**Chris Gammell:** Oh, oh, right, right.

**Dave Jones:** But that's what I'm talking about, you know.

**Chris Gammell:** Yeah, I'd say you're probably, yeah, you're probably correct.

**Speaker ?:** Right.

**Chris Gammell:** Let's do that check-in on all of our customers we love so much. Yeah, right. Service first. Yeah.

**Dave Jones:** Oh, goodness.

**Chris Gammell:** So, I actually, I had a similar experiment slash experience this week on Saturday, Friday night. I tried doing layout on a plane. Did you see my write-up on that?

**Dave Jones:** No, I haven't.

**Chris Gammell:** Do tell.

**Dave Jones:** Is this the experiment? Oh, plane experiment. I thought you meant, like, a power plane experiment.

**Chris Gammell:** Oh, no, no, no.

**Dave Jones:** Right. That would make sense as well. Okay.

**Chris Gammell:** So, this was a plane experiment where I got on a plane. I was flying out here to L.A. And I was like, well, I wonder... How long does that take? That's, like, a four and a half hour flight. Okay. Yeah, it's a decent flight. So, like, four hours of usable time, right? Yep. Right. So, like, something could get done. Right. But, you know, I always, you know, whenever we talk about, like, online tools, it's always, it always comes down to, like, you know, well, what happens when you're not connected? And I'm pretty sure you and I always use the example of what happens if you're on a plane. And you want to do it. And so, I'm like, well, I should do this. So, I started writing, basically started a design and started getting into it and quickly realized that even... So, basically, to cut to the chase, people can read about it. You know, I wrote it all up. So, I was comparing KiCad or really, you know, fill in the blank, whatever tool you use that's installed on your local machine, like Altium or Eagle or whatever else. And then comparing, again, CircuitMaker, which is the new Altium tool we've talked about. Right. And then Upverter, really. And those three are being our client side, mixed client, and network, which would be the CircuitMaker. And then mostly network for Upverter because they actually do have a browser extension you can use. So, yeah, just kind of like comparing all those and where you get into trouble. And to cut to the chase, basically, all of them. For different reasons than you might think, though, because I don't know how you do design, but basically it's like even if you have a completely local tool, I personally am so dependent on being able to quickly look up data sheets online.

**Dave Jones:** Oh, of course. Yeah. Yeah, I made this point the other – well, maybe in the forum or the other week when we're talking about this is that there's two things you need to do. Basically, if you're doing a schematic and you're designing your product and you're doing the schematic, you need access to the internet anyway, basically. Because as we said, yeah, you've got to check data sheets. You're so tired there. You've got to download 3D models. You've got to do all sorts of jazz. Right. And stuff.

**Chris Gammell:** If you prep properly, you can get away with not doing it, but then that's not really using a new design. Oh, yeah, but nobody preps properly.

**Dave Jones:** No, exactly. No, no. That's not how it works. So, yeah. So, I was saying one of my suggestions was Outium, at least if you want to allow people to work locally, it has to be on the layout side of things. Because generally, once you download all your parts, you've done your schematic, you push it into your PCB tool and you start your layout, generally you don't need to access the net much when you're actually laying out a board. Right. So, you know. Yeah, exactly.

**Chris Gammell:** I mean, like if you push a new part in or something like that, but you can probably get away with a lot of stuff. Yeah, that's right. You've got to verify your footprints, stuff like that. But, you know, that is something too. Like you said, you know, if you're already done with the schematic, you can basically, you could go out and make sure that you have all of the data sheets there already. Yeah, yeah. Like I know in KiCat it at least has a field for the data sheet link, but you could just go and download it. I don't know. Are you in the – do you still download all of them or is Google your new data sheet repository?

**Dave Jones:** No, Google's my new data sheet repository. I don't keep data sheets on my computer. I keep manuals and things like that. Oh, okay. But not, you know, like service manuals and stuff. Like I generally keep them because they're often like a bit of a pain in the ass to download. You know, you might have to log into something or do something or other. So, I generally keep those local. But no, no.

**Chris Gammell:** If it's a data sheet, no, I just don't keep any. What about like the really big ones where it's like a micro user manual? Oh, yeah, yeah.

**Dave Jones:** If it's absolutely enormous, yes. You know, like if I'm working on a design and I've got an FPGA data sheet and it's, you know, 100 meg because it's got, you know, 400 pages in it, then yeah, yeah. Certainly, I'm going to keep that locally while I'm working on the project. Definitely.

**Chris Gammell:** And I guess we should check in now as well. Do you still print stuff out?

**Dave Jones:** Yes.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, I think that's... Oh, as in data sheets? Oh, yeah, yeah. It's handy. Yeah, paper. Yeah. And I have it sitting right here. You know, it's hard to beat that. But when you've got a multi-monitor set up, often you don't need to do that.

**Chris Gammell:** Oh, that's a good point. Yeah, you know, I think my rule lately has been if it has registers, at the very minimum, I'm printing out the registers and like anything, you know, A to Ds, DACs, that kind of thing, definitely just... I know I'm going to be flipping that stuff anyways. Anything with a register map, definitely have that in paper right next to me. Because that's... I mean, that's really... I think even on a screen, even if you have two screens, it's still not the same to me. Because, you know, you want to mark it up and stuff like that. So, I don't know.

**Dave Jones:** So, do you actually have CircuitMaker? Did you use it on the plane?

**Chris Gammell:** No, sorry. That was an assumed behavior. So, I do not have that. Okay.

**Dave Jones:** So, your experience was based on how you used it at the stand?

**Chris Gammell:** Yeah, and from talking to them about it. Because they cleared up a lot of that stuff too. So, like asking about creating new parts, I asked them that directly. And they said that unless you have access to the... Because that uses Octopart API in the back end. Yeah, that's right. Just can you make it without having access to Octopart? They said you can't make a new component. I believe. Maybe I'm wrong on that. But because they tie them all to the Octopart data. Right. I don't think you can make a new component. Or maybe you can. You can update it later. Or maybe they should switch to that if that's the case. But, yeah.

**Dave Jones:** Hang on. Coming straight over the teletype here. This is breaking news. Evil Man Scientist Labs just tweeted a response to your shoe photo. And they said, whoa, you're making your own ASICs now. And then Nick replied, you win the internet. Everyone else go home.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Yeah, I will pay that. You're making your own ASICs. All right. Sorry. That's amazing. It's just a little live interjection there.

**Chris Gammell:** Oh, I love those guys.

**Dave Jones:** That's great. The show has degenerated into live tweets. That's right. Yeah. It's all downhill from here. Yeah. Oh, goodness. So, yeah. So, what's your conclusion?

**Chris Gammell:** So, the conclusion is, basically, you're pretty tied to the internet. I think, you know, the one thing I did think of, I thought I was going to have actual Wi-Fi, you know, like in-flight Wi-Fi, how they do that now. I thought that the plane I was on was going to have that. It actually only had TV. And I think that with that, a lot of the local tools you can kind of probably get around it. Because you could probably download, you know, the smaller data sheets as you need to. You can maybe browse around a little bit. It's not going to be reliable. And I think same thing with, like, so, if you have that, I think you'd probably actually be okay with all three. Because you could probably get the data sheets. You could probably hook into the OctaPart thing on CircuitMaker. And I think even some of the upvorder stuff is low bandwidth enough that you could probably click around, especially if you had the local app. But it's basically you need to prep if you want to do that kind of stuff. So, if you are getting on a plane, you need to prep. And that was part of my problem, too.

**Dave Jones:** You could spend quite a few hours prepping. Oh, of course. You know, I mean, so you could argue, well, what's the point? Why don't you just forget doing design on the plane? Do something else, you know? Right, exactly. Read the data sheet. Write emails. Yeah. You know, a book. If you're writing a book, write a book, you know? Right. I don't know.

**Chris Gammell:** Well, and I think that is kind of the practical thing. I think that you're right about the layout stuff, too. Like, if you're doing just layout, you know, that's always, like, where you're in the zone anyways. Yeah, yeah, of course. That's good. And if they can all do that, that's great. Because then it's like, you know, you're just in the zone. And then by the time you look up, you're there. You know, that's great.

**Dave Jones:** And you don't have to fiddle with the details. When you're doing layout, like, you know, layout is 80% placement and then, you know, 20% routing. So, you just place everything. You know, you're shuffling things around.

**Chris Gammell:** It's like solving a puzzle all day. It's great.

**Dave Jones:** Yeah, exactly. And you don't have to worry about the fine details. Oh, did I get that footprint right? Well, who cares? I can change it as a fix at the end, right? You know, it's not really going to affect my layout much unless I've completely screwed, like, flipped the pin out or something dumb like that. But, you know, generally that's not going to happen, right? So, you know, yeah. So, you're pretty safe. You know, laying out, you can probably do 90% of your board layout, you know, just standalone. And then, you know, the rest is a tidy up step. Actually, often I work like that. I don't fuss over the details at start. I go, no, I just want to solve the routing problem. You know, look, I've got, you know, five huge chips on this board. I need to figure out how they go, where to route them on the minimum number of layouts, et cetera, et cetera. Yeah, exactly.

**Chris Gammell:** You're kind of doing, like, exploratory, kind of just trying to problem solve based on space constraints. Yeah, I totally agree. And I think that kind of stuff is good.

**Dave Jones:** And do you need a real mouse for that? Because I find I need a real mouse for that. I can't use, like, a track pad. So it's like nothing.

**Chris Gammell:** Oh, definitely. Yeah. I actually, I usually bring, like, one of those, the extendable cord ones. Yeah. And then you have to have it on your leg, which kind of stinks. Like, I actually use my leg because, you know, I'm sitting coach, folks. I'm not. Right. Sorry. Sorry. Contextual electronics is not doing that well. And, yeah. So, I mean, it's still constrained like that, too. So I think what it really proves is that, you know, we use the plain example as a benchmark. It's a test. And it's probably not a valid test, really. That's what it really comes down to. Right. Yeah, probably not. Okay. So, you know, your mileage may vary. But I think. Yeah, of course. I think a lot of, I think an argument could be made that, you know, internet tools are going to get you there 95% of the time. Now, I also wrote in the article that, you know, if you're risk averse like I am, that 5% is going to, like, inevitably be the time when you're in production and, you know, on a deadline and your internet goes out or something like that. That's usually the real case. But, yeah, that's a risk people take, right?

**Dave Jones:** Yeah, if I'm going on a plane, I don't want to do layout on a plane. If I don't have the optimized tool for the job, it just continually pisses me off, you know? So, like, for me, the idea of prepping and then going on the plane and, you know, doing it on some freaking, you know, little cramped notebook with its, you know, 15 in with a tiny little mouse in my arms or at some weird angle.

**Chris Gammell:** Well, I think you may have spoiled yourself there, Dave. Oh, yeah.

**Dave Jones:** Well, no, totally, right? I'm trying to do a, you know, I like tools that work. Tools that don't, that are unoptimized or, you know, they just piss me off, really. So, I would rather do something else. I'd rather find, you know, there's always something I can do, always something else I can do apart from that. So, you know, I'm going to end up doing that, I think. Yeah, I can't imagine anything worse unless I absolutely, desperately had to, you know, for some reason. Right.

**Chris Gammell:** Well, and that's the kind of thing where you can't really even test that, right? How do you set up a test case?

**Dave Jones:** No, no, you just have to do it. No, you just get on it.

**Chris Gammell:** So, what I did is I strapped a bomb to my wife and it's going to go off in two days and I have to fly to meet her.

**Dave Jones:** And unless I design a circuit board by then, she's going to explode.

**Dave Jones:** Right.

**Chris Gammell:** Bad test, Chris.

**Dave Jones:** And we've just been flagged by the NSA, by the automated algorithms.

**Chris Gammell:** Bad test.

**Dave Jones:** All we need is the keywords White House and President and, oh, sorry. Hey, bingo. Bad test, Chris. Oh, goodness. Yep. Anyway. So, yeah. Let's not mention how Australia's getting the US like that now.

**Chris Gammell:** Oh, no, we don't need to get into that.

**Dave Jones:** Let's not go there. Yeah.

**Chris Gammell:** So, that was my experiment.

**Dave Jones:** So, right. Okay. Would you do it again? Would you lay up boards on a plane?

**Chris Gammell:** I'm going to try it on the way home, actually. I unfortunately booked a flight. I thought I was flying overnight. I looked again and it's like, oh, that's 11 a.m. I'm flying out, not 11 p.m. Oops. Ah, oops. Oh, well.

**Dave Jones:** Yeah, that's pesky a.m. p.m. indicators here. Yeah.

**Chris Gammell:** So, it's not just for the show. I book flights at the wrong time as well.

**Dave Jones:** Consistency is key.

**Chris Gammell:** That's right. That's right.

**Dave Jones:** Yep. Chris Gammell, ever reliable.

**Chris Gammell:** That's right. Man.

**Dave Jones:** Oh, goodness. Yeah. Hey, you want to know what I've been doing?

**Chris Gammell:** I do. What's new?

**Dave Jones:** Well, what's new will be new today, hopefully, if I get off my ass and finish it, because I couldn't finish it yesterday, is my latest video, which is about the white van speaker scam.

**Chris Gammell:** White van speaker? I've never heard of that before.

**Dave Jones:** You haven't heard of the white van speaker scam? Oh, well, I'll tell you all about it. Or you can watch my video. No, I'll tell you all about it.

**Chris Gammell:** Of course I will. I will.

**Dave Jones:** I think the video is going to be released by the time this thing is released. Okay. Anyway, yeah, the white van speaker scam happens in a lot of countries, and basically what it is, is you're in a parking, you know, like a shopping center car park or something like that, right? And someone pulls up beside you in a white van, usually a white van, hence the name, right? The white van speaker scam. They go, hey, buddy, you want some cheap speakers? And they look all legitimate. You know, sometimes the van will have like proper signage on it, and they'll wear uniforms and, you know, if they want to sell the scam a bit more. And of course, you know, the person's intrigued, you know, like five out of 10 people will be intrigued. Oh, yeah, give me a look. You know, I can always say no, right? So they go out in the van, they've got all this, you know, supposedly high-end boutique audio gear in there that you've never heard of, right? They're brand names you've never heard of, okay? But they're eerily familiar because part of the scam is that the names will be very similar to someone or something that you've heard of, right? And I'll give you the example in a minute. And the, yeah. And so, but what the scam is is these products aren't empty boxes or whatever. So you do get gear that kind of, sort of works. And, but it is the cheapest, crappest, heapest shit you can possibly imagine. Stuff that wouldn't even be sold in bloody Walmart, right? Yeah, yeah. At Rock Bonnet, right? They're so bad. They don't meet safety standards. They don't meet any of their specs or performance standards, right? They're so garbage. And anyway, so they actually sell these. So they flog these things as high-end, you know, made in, designed in Germany and, you know, all that sort of, yeah. High-tech, boutique brand. And if you haven't heard of them, you're just not sophisticated enough. You know, that's, right. And they bring out all these fake brochures and hi-fi magazines, right? So they'll whip out this hi-fi magazine. Look at these wonderful reviews. Look at how fantastic this is. And it's all bogus, right? So anyway, they, and they claim, oh yeah, they cost $5,000 and we'll give them to you for $300, you know. And they're worth about $20, you know. And yeah, anyway, they make a huge living out of this. They make a big living.

**Chris Gammell:** Yeah, I mean, confidence scams always are, right?

**Dave Jones:** Yeah, confidence scams. Yeah, exactly. It's a white fan speaker scam. And by the time you actually get it home, and they come in glossy boxes and everything, by the time you get it home, turn it on, and it works usually, you know, and then you realize, well, that sounds shit, or that projector is garbage, or that, you know, or whatever. Then you realize that you've been had, you know, and it's all too late, and they use fake addresses, and the invoice is fake, and, you know, blah, blah, blah. Anyway, white vans, beware of people in white vans, folks.

**Chris Gammell:** There's a new white van, though, Dave. It's called Kickstarter.

**Dave Jones:** It's called Kickstarter.

**Chris Gammell:** Oh, boy. Yep.

**Dave Jones:** Anyway, I found a couple of these things in the dumpster, right?

**Chris Gammell:** Oh, really?

**Dave Jones:** Is that where they came from? And I had never heard of these things, right? I'd never heard of these brands, and so I posted a photo on Twitter, and everyone came back, ah, that's the white van speaker scam gear. And I went, beauty, I can open them up. So I'm doing teardowns of these if you want to see how shit they are inside.

**Chris Gammell:** Oh, that's awesome.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah, that's crazy. I mean, like, honestly, the scams don't change, right? I mean, like, I say Kickstarter, but I mean crowdfunding in general, right? Ones that are, like, super, super janky and promise the moon but don't do much. Like, oh, I don't know, a perpetual magnetic USB charger.

**Dave Jones:** That was, come on, that had to be a piss take. It must have been. That had to be.

**Chris Gammell:** Yeah.

**Dave Jones:** It was so bad, and it got approved.

**Chris Gammell:** Yeah.

**Dave Jones:** It got approved by, I can't believe, you know. Well, I can believe it, actually.

**Chris Gammell:** It's like people are starting to do, like, penetration testing of the security at Kickstarter.

**Speaker ?:** Right, yeah, yeah, I've done it.

**Dave Jones:** Right. Yep. And if that's the case, then, yes, well done. Well done. Right, right.

**Chris Gammell:** You'd think they'd start setting up, like, just, like, plain text filters for certain things.

**Dave Jones:** Right, yes. Just Tesla, perpetual motion, you know. Yeah, yeah, perpetual anything, right? Magnetic energy, you know.

**Chris Gammell:** Yeah, energy just in general. How about that? Just energy in general, right? Yeah. There was an interesting one as well. The Printier, which was another Kickstarter, they wrote about shutting down their production. And they are doing refunds and stuff.

**Dave Jones:** I saw this. So, my hat's off to them. Seriously, they admitted that they failed. And they couldn't do it. And they're going to refund everyone's money, no questions asked. Fantastic.

**Chris Gammell:** Yeah.

**Dave Jones:** Right? No, yeah. I mean, yeah, they're silly for not, right? They just didn't do their homework to begin with. Right? And that article we talked about a couple of weeks back about how a sub, like a $300 printer is impossible. Yeah. Right, right. You can't do it. Even a $500 is borderline impossible. Right? You can't do it. And they got basically caught in the same. In fact, the math is almost identical to what that, I think, to what that article pointed out. Right. You know, they needed like $1.2 million to make it viable. And they only got like $150,000. Right. Exactly.

**Dave Jones:** And it's just, yeah.

**Chris Gammell:** It's just the economies of scale. Like, even if you just take a high level look at it, you look at the, you know, just the injection pieces that they had. I mean, they were really nicely designed and everything. And like, it looks nice. But then it's all about mold costs and everything else.

**Dave Jones:** The mold costs alone would have eaten up most of their $170,000 they got or something. Yeah. You know? Because, yeah, it's a fancy looking product.

**Chris Gammell:** When Eric talked about that last week, that, you know, so they actually did talk, this printer talked to Dragon. And I was very impressed by that, though. Like, the fact that Dragon pushes that, the break-even point as the minimum funding goal. So that's...

**Dave Jones:** Well, this company went to Dragon. That's a fact, though. Once they realized... Well, no, I think it was during the Kickstarter campaign they realized they might be in a bit of trouble. And they, I think that's what they were saying. Oh, it doesn't? Okay. Well, anyway, yeah, they went to them and they just went, no, sorry, you know. Yeah. You didn't raise enough money. You can't do this.

**Dave Jones:** Yeah.

**Dave Jones:** Just can't do it.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. So...

**Chris Gammell:** Well, it is good that they were able to...

**Dave Jones:** Yep. And they're going to have to eat that loss. I mean, you know. Yeah, because there are a store loss there. It's not like they partially refund it. Yeah. I mean, you have to be willing to do that in this business. You have to be... If you fail, you have to be willing for it to come out of your pocket. To have it come out of the, you know, the people's pocket is just shameful. Right? Yeah. Yeah, I know that's the risk of Kickstarter. There'll be people out there screaming, oh, but, you know, that's what Kickstarter's all about. You know, raising money. If you're stupid enough to think that you're going to get all your money back, then, you know.

**Chris Gammell:** Straight. Yeah.

**Dave Jones:** Yeah. But, yeah, I... You know, and I kind of understand that sentiment, but, you know. Yeah. Well, it's just... Sometimes you just have to do the right thing. Otherwise, you can live with a ruined rep, right? Right. Yeah. And, you know... And there are some people who don't care. Oh, I don't care. You know, I don't care. I don't have a reputation, so who cares?

**Chris Gammell:** But, anyway. You will after that, yeah. Probably. Oh, goodness.

**Dave Jones:** Anyway.

**Chris Gammell:** Yeah, so, the... Speaking of money, did you... You see this one I posted about the new cost of a fab these days? Obviously, this is my former employer, so it caught my eye.

**Dave Jones:** Yes, it is. Fifteen billion?

**Chris Gammell:** Fifteen billion dollars for Samsung to build a new fab in its own home country, as well, so it's like they already have...

**Dave Jones:** So, they're building it in Seoul, are they?

**Chris Gammell:** Actually, it's not... South of Seoul. Yes. Sungtech. Suwon is the... Sungentech.

**Chris Gammell:** That's where the current one is, but they're moving it somewhere else.

**Dave Jones:** Fungtech, they're moving to. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm pronouncing that totally incorrectly. Right, right. Right. Well, South Korean listeners are laughing their ass off. Thank you. Right. You're welcome. Yeah.

**Chris Gammell:** I mean, it's crazy, though. It's just like seeing this stuff, you know, like... And then you look at the scale differences, right? I mean, so we're talking... That printier was, what, like 115,000, and that sounds like a lot, and then you go and look at something like this, where they're building out new chips, and it's just like...

**Dave Jones:** Well, what does 115,000 buy you in one of these fabs? I've set up production facilities before, and $115,000 buys you just as a comparison. That's in that entire printier project. That would buy you, you know, one custom jig, you know, barely. Yeah, right, right. Right? It's like... Yeah.

**Chris Gammell:** Yeah, manufacturers are expensive, yo.

**Dave Jones:** Yeah. I know. If you want to automate it and do it properly. Absolutely.

**Chris Gammell:** Right. It costs a fortune. Yeah, especially because, like, in... I mean, most of these chip fabs are all, like, full auto these days, too. You know, you set them up... Oh, yeah, totally. Yeah. They just go, you know, they just...

**Dave Jones:** Silicon in one out and, you know, tested chips out the other end, almost. Yeah.

**Chris Gammell:** Exactly.

**Dave Jones:** Who needs humans?

**Chris Gammell:** You know, the only reason I was there is when stuff went wrong, and it... Right, yeah, yeah. But it was, like, one person kind of... Like, I was, like, manning a lot of... Yeah. A lot of machines, basically. Not a lot. More people did it later. Yeah. But it's amazing when you get into the groove of it. It's just, like, it's all... Mm. It's all robots, man. So, it's just robots nonstop.

**Dave Jones:** It's robots all the way down.

**Chris Gammell:** Robots all the way down. Humans need not apply.

**Dave Jones:** Beautiful segue. Thank you.

**Chris Gammell:** So, yeah. So, there was this... It wasn't documented. It was, like, a YouTube video about...

**Dave Jones:** It's a YouTube video.

**Chris Gammell:** Yeah. Robots. And, uh... But, uh... My friend's had us to me, and... It's just about the coming...

**Dave Jones:** Apocalypse.

**Chris Gammell:** I don't know what. The robot apocalypse. The economic robotic apocalypse, right? It's probably not gonna be... They're not gonna eat... They're not gonna kill us and use us for robot fuel, but... They are probably gonna eat a lot of jobs. And, uh... And some of the explanations that the guy gives is actually a better... A better comparison than I had heard in the past, right?

**Dave Jones:** Well, this is what he does on this channel. This is, uh... CGP Grey. Yeah. I'm not sure what that stands for. But, anyway, this is basically the style of video he does, you know, explaining things. You know, in a sort of infomercial kind of way.

**Chris Gammell:** Kind of like Scott Jeriskel does. Curious Adventurer. Kind of like similar... Similar style to Scott. Yep.

**Speaker ?:** Yep.

**Dave Jones:** It's got this really annoying tune in the right-hand channel background.

**Dave Jones:** Oh! It bugs me. YouTube critique.

**Dave Jones:** Yes. From a fellow YouTube content producer. Oh, blah. I thought, like, is that my phone doing something weird? And I'm going, no, I know. And I actually hit pause. And, you know, sure enough, it was, you know, in the bloody... Embedded in there somewhere. It's just, oh! People embed subtle music backgrounds in their... ...in their video... ...in their voiceover videos. Yeah. It just bugs me. Yeah. Anyway. Sorry. Yeah. Fellow YouTube content producer.

**Chris Gammell:** So it's interesting, though, like, looking at this... And I think we probably talked about this before because I read a... There was a book by these two MIT economists and they write about it and... About very similar things, basically, about how... Not just robotics, but also just automation, right? If you just kind of look at automation as a larger topic... Right. ...it really starts to be all encompassing... Up-uncompassing. But, you know, like... We even think, like, as electronics designers, right? That, oh, well, nothing will ever take our jobs there. And it's like, well, wait a second. It already kind of has. It's just... It's not as active, right? Right. So I've talked about, like, in the analog side of things... It's not like someone's coming in and, you know, using an auto-router to put together circuits. What's actually happening is on the supply side... It's that chip companies want to make more money and grab more of the market. So they basically just start integrating more functions on silicon. That's the side... That's actually the automation side that actually affects... Yes. ...more electronics designers these days. Same thing for micros, right?

**Dave Jones:** Yeah, because any schmuck can come along... Any schmuck can schmick. Any schmuck can come along and follow the application note circuit, use Eagle to lay out a board. And bingo, they've got, you know, some advanced functionality doing bloody DSP and HDMI and all sorts of jazz. And they can sort of, you know, hack it together and make it work.

**Chris Gammell:** Right. Exactly.

**Dave Jones:** Whereas five, ten years ago, that was rocket science.

**Chris Gammell:** Right. And if you're used to... So like someone like you who always did like high-speed interconnects, right? And like needing to have really good impedance-controlled boards and stuff like that. Well, when that stuff moves on silicon because it's more efficient to do so... Exactly. ...well, you need fewer designers. And you can have schmucks like me that, you know, like it's just... Then the hard part just becomes...

**Dave Jones:** You can do high-speed USB and HDMI on a two-layer board, for goodness sake. Right? And make it work. If you keep the connector near enough to the bloody chip, that's all you need.

**Chris Gammell:** And that's an app note that you have... And then, you know, also with open-source hardware as well. I mean, these are all benefits as well. That's the weird thing. Oh, no, of course. It's like we're like, you know, frogs in a pot of boiling water or rapidly warming water. It's like no one's going to complain about it because it's beneficial, right? You know, you can make products faster and you can do more interesting things. I mean, but there is that weird economic component to it of like, oh, crap. Well, it used to take 10 people to design this thing and now it takes one. And it's way cheaper to do so. You know, that's crazy.

**Dave Jones:** Yeah, look, it's one of these doom and gloom videos, right? That how all our jobs are absolutely redundant now and robots have already taken over. We just don't know it yet. Blah, blah, blah, blah, blah, blah. And, well, you know, you can argue they're not half wrong, but it's not as apocalyptic as they make out. It's just crazy.

**Chris Gammell:** Yeah. I'm trying to find the name of this book as well that I was reading because it actually is quite good. What is it called? It's called The Coming... The Second Machine Age. Oh, yeah, that's the one. Ah, right. The Second Machine Age. That's the one I've mentioned on the show before. But, you know, basically between this video and the book and everything else I see about it, what it ultimately brings me to, like over and over again, the only thing that I really start to come to a conclusion of is there's two options in the future. One is have a hard time finding a job, or two is own the automation systems. Like that is it. So people listening, if you're looking for a career change or if you're looking to become wealthy in the future, like, you know, that, it's going to cause a greater divide, I think, as well. I mean, obviously, there's a very large economic argument here as well. And, but, you know, if you want to be...

**Dave Jones:** Or just go into the...

**Chris Gammell:** Yeah. If you want to be in charge, though, basically be the one who makes the automation systems. That's what it comes down to. And when I say automation, I don't mean home automation. I mean, like, you know, it could be software. It could be software and hardware. It could be hardware alone like robots. But anything that, you know, makes things easier, right? It could be industrial automation, right? This is like the jigs you talked about in manufacturing. That is technically automation, right? I mean, it's...

**Dave Jones:** Oh, somebody has to build and design the jigs, and robots aren't going to do that, you know? So...

**Chris Gammell:** Well, yeah, but basically... No, they're not.

**Dave Jones:** No, you're right. No, don't buy into the hot.

**Chris Gammell:** I'm not going to say that, Dave. But what I'm saying is the same kind of thing is going to happen, right? You could move it forward in the design cycle. You could move to the, you know, design for test or design for manufacturing where maybe you move it all to be on a JTAG chain, right? So maybe you don't need as many test points, right? You start to move in that direction, or everything moves on silicon, and it gets tested at the silicon level. That's going to be, like... I totally agree that, like, no... You're not going to have these super, you know, intricate tasks that are... Those are not going to go away, but they're going to get shifted forward in the design process. That's what electronics people are going to see, I think.

**Dave Jones:** Well, yeah. But then you move into the physical handling side of things. You still have to connect up your test points and, you know, and your jigs and do everything and the manual handling of the boards and how that optimizes and how that flows through your production process and all that sort of jazz, you know?

**Chris Gammell:** Yeah. I mean, there's... Maybe, yeah, but, like, okay, how about another example? Like, I'm not... Like you said, I'm not trying to be all doom and gloom here, but actually there are interesting examples here, too. I think he is, folks. Like how... So, like, how about the Intel Edison? We talked about that one before. But, like, that... Basically, they're... You know, that's basically designed to be a module that gets designed into a final product, right? From Intel. It's very fancy. And obviously...

**Dave Jones:** Yeah, but it's not going to be.

**Chris Gammell:** I know, right? But they're not the only one. Obviously, there's a lot of modules out there that's been for a long time. But, you know, like, basically...

**Dave Jones:** The laws of economics aren't going to change. Can we agree on that?

**Chris Gammell:** I can agree on that. Yes. I totally agree on that.

**Dave Jones:** Thank you. All right. So, therefore...

**Chris Gammell:** But what I'm saying is the changes we're going to see as electronics designers is going to be the shift towards, you know, modules and then eventually getting it all on silicon. That's the shift that's going to affect us the most, I think. It's not going to...

**Dave Jones:** Yeah, but there's nothing that's not already here.

**Chris Gammell:** Right. You're right. Yeah. But you said it's an economic argument, and I'm agreeing about that, basically. Right? If you... So, say you're a company, and you've got 10 engineers, you know, hardware, software, firmware, whatever, right? If you can now move from, you know, the mix being 333, right? Because I saw this right at my last job, actually. Right. It used to be, you know, out of those 10 engineers, it used to be five or six of them were hardware engineers, right? And you had... Yeah.

**Dave Jones:** Now you get away with one or two.

**Chris Gammell:** ...three firmware and one software. And then the shift became one hardware engineer, four firmware people, and, you know, five software, right? And it just shifts towards software. Because it's, you know, you can change it over time, you can update the firmware, but then you can also, you know, you can write more interesting stuff on top of the software. And it's just like, that is more economical, I think. I mean, maybe even to the point where some companies are going to go and just drop the hardware guy entirely and just go buy off-the-shelf hardware, right? So...

**Dave Jones:** Right. Now, this brings up, I can... We can actually get figures from a company that does this sort of thing. SparkFun have published a nice little infographic here, as much as I hate infographics, this one works quite well, showing how much time their people spend on what particular parts of getting a product to market.

**Chris Gammell:** Yep. And so this is a...

**Dave Jones:** Guess what the biggest one is? It's a... So it's a big rotating pie chart, right? Yeah.

**Chris Gammell:** And this is from Mike, who's been on the show. Mike Horner's on the show. Yep. And so the rest of the engineering team has as well, so...

**Dave Jones:** Right. So this is a nice little pie chart showing the breakdown of where all their engineers and product developers spend their time.

**Dave Jones:** Yeah.

**Dave Jones:** And we'll post this in... Yeah. We'll post this. So check... Go over to theairpower.com. Check it out. And guess where they spend their most time? Come on at home. You have to...

**Chris Gammell:** I was going to say, I'm looking at it. So it doesn't... I know.

**Dave Jones:** So we'll give people five, four, three, two, one. Documentation. Yeah. 20% of their time is the biggest one. Writing libraries is 15%. Yep.

**Chris Gammell:** And just like other stuff is 20%, right? Are there...

**Dave Jones:** Where's 20% other stuff?

**Chris Gammell:** Well, it's meetings is 10 and miscellaneous 10, so...

**Dave Jones:** Oh, miscellaneous 10. Right. But revising and reworking prototypes is 10%. Board design is 2.5%. Breadboarding is 2.5%. Firmware is only 5%. A lot of people think, oh, it's all in the firmware. No. 5% of their time. Writing libraries takes three times the amount of effort as firmware. And that's not surprising because once you've got... Writing libraries is hard, but once you've done it, the firmware becomes easy. Right? Right. Yeah.

**Chris Gammell:** Well, and that's the point of doing it is you get reuse and you start to... Yeah, yeah, yeah. Of course. You get gains. You get gains, yeah. Yeah.

**Dave Jones:** Once you've written the library, you get those gains in your firmware. So that's why... And then example code, 5%. Learning, 5%. Making projects, 10%. Exploring, 5%. So, yeah. Like, you know, documentation is the biggest part of it.

**Chris Gammell:** Right. And this is why we run out of things to talk about, folks, because hardware is only, what, like 15% there? Yeah.

**Dave Jones:** Yeah, like total or something. Yeah, that's right.

**Chris Gammell:** Which is the Kickstarter percentage, Dave? That's what, yeah. Right. We should respond with our own. Or if anyone wants to turn the amp hour bingo into a revolving wheel of this thing, right? Right. And a lot of it would be not fun as well. Yeah. Oh, goodness. Yeah. This is really great, though. I mean, and it is true. You know, like the... I think the thing that actually isn't on here... I mean, it's probably rolled in the other ones, but like sourcing, right? So sourcing parts. Right. Maybe that's less so for them because they have a library already set up or they have like a standard part library they're doing. But, you know, that, at least for me, like that, like finding new parts, sourcing new parts. Yep. You know, like actually going out and buying them, opening packaging, organizing all that crap. That, especially for prototype type stuff, that's a huge part of it.

**Dave Jones:** Well, you can argue that... Well, yeah. But you can argue that SparkFun don't really do finished products as such. They do more development boards and stuff, which are easier than... You know, they're much less complex and more specific than a generic product, you know, than actually designing a finished product.

**Chris Gammell:** Oh, maybe. I think a lot of the same stuff is... I mean, like, what is it? Plastic on top. I mean, like, I don't know. Like, a lot of that stuff... Like, if it's just breakup boards, that's one thing. But I think development boards definitely has, you know, a breakup or development board that has 100 components. Oh, yeah, but it does.

**Dave Jones:** But it's not the same as a finished product where you're, you know, where you're aiming to, okay, we're going to make 10,000. They don't care. They do, though.

**Chris Gammell:** They know that they're only... They have to make even more than a lot of people out there do because they actually produce this stuff. So I think, though, that, you know, they have sourcing people as well, which can help. It could be crappy as well. I mean, having, you know, having that divide between engineering and sourcing can be miserable as well. So, yeah, I don't know.

**Dave Jones:** Anyway, that's an interesting little pie chart. Yeah. So, but yeah, I think it's skewed towards that. Well, it's obviously skewed towards their style of what products in quote marks that they actually produce. Yes. Whereas if you're working on like a real consumer level product, it will be different, you know. Yeah. So, yeah.

**Chris Gammell:** Yeah. If I had to like quickly break down my past stuff, it's like 30% corporate garbage, 30% shopping and or meeting with vendors, you know, 10% designing and testing and retesting hardware. Right. And then like, what I leave out, like 20%, I don't know, 20% sitting in meetings. I guess that's corporate garbage as well. Yep.

**Dave Jones:** I'm glad I don't have to sit in meetings anymore.

**Chris Gammell:** Jeez. You got one per week, man. Terrible. Oh, yeah. This. Yeah. The best meeting you've ever been in. So, speaking of sourcing parts though.

**Dave Jones:** Well, hang on. I didn't tell you. Hang on. I didn't tell you about my solution to the coming robot apocalypse. Oh, yeah. I want to hear this. What I'm doing to avoid that. Okay. I've simply moved into the entertainment business. No, no robot's going to compete in there.

**Chris Gammell:** I don't know, man. They did talk about, in that video, they talked about robots writing articles, not necessarily entertaining articles.

**Dave Jones:** Yeah, and they're shit.

**Chris Gammell:** And nobody wants to read them. Well, yeah, you're right. I mean, but they cover the creative side of things though too. I mean, like, I agree that like right now it's going to be whatever, but.

**Dave Jones:** No, no. I'm sorry. They're still going to be full of shit. No.

**Dave Jones:** Right now.

**Dave Jones:** I mean, that's always what it is, Dave. No, no. Well, that's always. Well, that's always. That's the fear mongering of this. Yeah, I'm drawing a light in the sand. Yeah. They're not going to be bloody creative. You know, they're not going to be creative enough. I don't, you know, you can always go, oh, yeah, in the future and you can, you know, extrapolate things. And it's like, no, I'm sorry. There's huge thresholds there that have to be overcome before, you know, they become so intelligent that they can actually, you know, not only do art, for example, or do comedy, but explain why they're doing it and how and all that sort of shit. It's just, no. I'm sorry. Humans are always going to win.

**Chris Gammell:** Okay.

**Dave Jones:** I will predict. Not in my lifetime. Not in my lifetime.

**Chris Gammell:** Right. Because the robots are going to take you out, man. Get rid of the influencers first.

**Dave Jones:** Actually, I will even predict not in Sagan's lifetime. Yeah. Will, you know, so I'm talking like the next, you know, 80, 80, 80, 100 years. Right. I'm talking, so let's round it up to the next 100 years. Yeah. Yep. Well, let's round it up to the next 100 years then that computers will not, robots will not be as creative like this. I don't know, man.

**Chris Gammell:** I would pull out an exponential chart right now, even though he's a crazy nut job.

**Dave Jones:** Well, I'll shove it right back up his behind.

**Chris Gammell:** Yeah. He's a little crazy. Because I think he's wrong. Yeah. Exactly. I think he's pretty spot on with the exponential growth side of things. So it doesn't make him right on all things. No, of course not. But I think that that's correct. I think that our ability to see the future is so limited by predictions of linear growth. Yeah. Then again, I really don't know about the creative side of things. And I'll tell you this. I don't want a robotic Dave out there. Right. This one's bad enough, folks.

**Dave Jones:** Yeah, exactly. Some people say, I am a Dave bot. I just keep coming out with the same shit every time.

**Chris Gammell:** Believe me, they'll never figure out how to program an Aussie accent into a robot.

**Dave Jones:** Take the classic example of the game of chess. Right? That's always been the benchmark intelligent test of when computers would get more smarter than humans. Right? Could they beat a human at chess? And currently, yeah, they're kind of sort of able to beat a human at chess.

**Chris Gammell:** No, no, no, no. They beat humans every single time. They cover this in that second machine age as well. Every single time. No, no. Believe me. Every single time. But the interesting thing they talked about. Well, last I checked, it wasn't. No, yeah. It wasn't that good. Kasparov beat Deep Blue once. And then right after that, he...

**Dave Jones:** No, no. If yeah, but I've read thoroughly on the Kasparov incident. Right? And it turns out he just lost. He basically gave up. He basically gave up. He could have easily drawn that match and taken the championship. Right? And not lost. But he simply gave up because he was so stunned that it made this move that, you know, he just went, that's bullshit, they're cheating, you know, and he just... No, it was... There was a human factor. There was a psychology factor involved in there. Okay. And I'm saying, well, that's because some people say that's part of chess. Right?

**Chris Gammell:** I was going to say, if you get your opponent to quit, you win.

**Dave Jones:** No, but anyway, he was not thoroughly beat.

**Chris Gammell:** I'll reference Ender's game right here, you know? Okay. Right. I won the game.

**Dave Jones:** He was not thoroughly beat is the takeaway from that. He could have won that.

**Chris Gammell:** So, that aside, every time since, the computer keeps winning. So...

**Dave Jones:** Right. Anyway... But the point is... Okay, go ahead. No, no, no. I haven't finished my point. Okay. The point is, yeah, the computer might win, but the computer cannot explain how it wins. The computer cannot... It goes... It does it. It still does it by brute force. Right?

**Dave Jones:** Correct.

**Dave Jones:** Still does it by brute force. Okay? And that's the tell, right? That's the thing that tells me that all this prediction about, yeah, in 15, 20 years, computers will be smarter than humans. It's bullshit. Right? And they'll be creative and they'll do art and they'll do comedy and they'll do music. No. Bullshit.

**Chris Gammell:** Actually, this proves my point as well. Because they... So the second machine age talks about this, right? So they say, humans always lose the machines. However, humans plus a machine assistant will always beat the best machine in the world. Basically, the creativity of a human plus that. And so that actually proves my point of whoever owns...

**Dave Jones:** Because they don't have creativity. Right. That's what I'm getting at.

**Chris Gammell:** Whoever owns the automation and the robotics side of things, right? If there's human intelligence behind it, they are always going to win. So that's why my point is proven. Yeah.

**Dave Jones:** Totally.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** And you'll just find efficiencies. It's an economic argument. You'll always find efficiencies if you have this automation. Like, if you compare that versus having to hire 100 people to do something, if you have a robot, you're always going to win with the robot because of cost.

**Dave Jones:** Right.

**Chris Gammell:** So.

**Dave Jones:** Yep. And then cost aside, humans can always do an infinite more than robots. Yeah. The classic case is going to Mars, right? Why send humans to Mars? Why send robots instead of humans, right? Humans can do a thousand times more in the same time that a robot can do. Right. Right. Because they're there. They're able to go, whoa, what's that? Whoa, look at that shit. Let's do that. You know, they're able to just, you know, think on the spot. They're creative creatures. They're, you know, creative, inquisitive. They're, you know, all the stuff that makes a human.

**Chris Gammell:** It's not about reproducing. I always say it's not about reproducing information. It's about synthesizing information, right? That's ultimately what a human's good at or better at than computers, right? Yeah.

**Dave Jones:** And understanding new things that they haven't encountered before. Whereas computers, you know, unless they can have algorithms to learn that, it's just no. So you've got to know what the problem is.

**Chris Gammell:** Is that we mistake regular tasks as needing synthesis of information, whereas many more than we actually perceive are just repetitive type things. Yes.

**Dave Jones:** Oh, yeah. Yeah, totally. Like a lot of PCB layout is repetitive. Right. Exactly. I'll happily, you know, admit that. And that's why a good PCB designer will use an autorouter very selectively. It's like that combination, you know. It requires the human plus the autorouter.

**Chris Gammell:** I need a new t-shirt. I need a new t-shirt. Never trust the autorouter with everything.

**Dave Jones:** That'll be the next route.

**Chris Gammell:** Speaking of, I have a new t-shirt out, Dave. Did you see my new t-shirt?

**Dave Jones:** I have seen your new t-shirt. Yes.

**Chris Gammell:** Yes.

**Dave Jones:** I don't know. I have the odd question about that.

**Chris Gammell:** Yeah? What about?

**Dave Jones:** Well, you're talking DC only, you know. I mean, there's a bit of fuzziness there. But you do show a DC battery on it. Yes. So granted, it is that case. But what about the instantaneous case? It takes time for the electrons to get across. So when you flick that switch, you know, it's like, so you're not talking, you know.

**Chris Gammell:** Should I put it in the bottom, like, assume steady state? Should I cancel the t-spring? Assume steady state condition. Yeah, exactly.

**Dave Jones:** Assume in steady state condition.

**Chris Gammell:** Oh, my God. Okay. Yeah, maybe I'm going to add that to the back. I don't know. I don't want to cancel it now. But if the t-spring... It's getting a bit geeky now. If the t-spring... Oh, yeah. Now it's going to be geeky, Dave. Right, well... If the campaign fails, though, I'll definitely revise it with that.

**Dave Jones:** Right, because that will be the sole reason it fails, right? Right, right. Not because people don't need... Because everyone goes, that's just stupid.

**Chris Gammell:** People don't need another nerdy t-shirt, but yeah.

**Dave Jones:** Oh, goodness. Yeah. All the pedants coming out of the woodwork. Yeah.

**Chris Gammell:** So what I was mentioning before, though, with layout stuff, Octopart recently, they paired up with Seed Studio. Remember I had talked about the open parts library a while back? Right. Yep. So they paired up with them and a couple others. I think Adafruit and a few other open hardware companies and stuff like that. But basically, you know, trying to standardize this idea of, you know, a regular set of components and then having a couple comparisons for each one. So it looks good. I mean, I think that's a great idea, especially if you're moving into... Oh, I know Chris from Worthington as well, so another assembly house there. Right. It's a cool idea.

**Dave Jones:** And that's what Altium's moving into, too, because they're using the Octopart back end. So they'll ultimately, I guess, tie into all that. Or maybe they're doing their own thing. I'm not sure.

**Chris Gammell:** Proto Exchange, Tindy, Tempo Automation, Art Factory, Make Simply, Dragon, Electric Camp, Highway 1. Ooh, speaking of Electric Camp, I'm actually having... This should be out in time, but Brandon, who's on our show, he's going to be... I'm going to be... There's a meetup out in San Francisco, so if there's any San Francisco listeners, Brandon will be giving a talk about hacking sub-gigahertz RF and then tying into electric imp. And then there will also be a talk on reverse engineering file formats for CAD programs. So that's going to be fun. Awesome. Yeah. I'm excited about that one. Yeah. And Brandon, too. Excellent. Yeah. Sounds good. So, yeah, the Common Parts Library, I think this is going to be really cool. So definitely good stuff. They should keep it up. I think, yeah, there's, what, I think like 150 right now or 200. I'm not sure how many exact parts right now. But like we said last time we talked about this, you know, there's a good number of things on here. You could really make a lot of different things with this, basically. So very cool stuff.

**Dave Jones:** Totally. Yeah, I like it.

**Chris Gammell:** Yeah. What else? What else should we talk about?

**Dave Jones:** We've got... Yeah, we got time. Chip of the week. Chip of the week.

**Chris Gammell:** Oh, yeah? Which one?

**Dave Jones:** The Max 10. Max 10. Oh, yeah. The new FPGA. Which I was confused, right? Yeah, I've looked at it, right? I was confused because I go, well, Max, that's a CPLD, isn't it? Yeah, exactly. You know, I was like, oh, they've caught an FPGA. Apparently, they've always used it for a long time. They've used the FPGA fabric inside. But still, my old brain thinks, you know, associates Max, you know, the Altera Max series with the PLD. The Max 3000 and stuff like that. Yeah, yeah. Exactly. Yeah. It still associates that with the PLD. So, anyway, they've decided to call their new low-cost one the Max 10 instead of calling it the Cyclone 20 or something, you know. It's the...

**Chris Gammell:** Right, yeah. Yeah. Well, and you will be sad to know that I saw Mike Harrison tweet about this, Mike's Electric stuff. He said there are not any low-scale 10-ounce.

**Dave Jones:** Yes, I've seen that. So... Yep. No, of course there aren't.

**Chris Gammell:** Blah.

**Dave Jones:** They just don't give a shit.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** They don't give a shit. I've been asking for 15 years. They don't care. That is a shame, too, because... Every time I ask them, they tell me the same thing.

**Chris Gammell:** Well, and they talk about having an Arduino-compatible dev board and stuff like that, too, and it's just like... Especially if there's going to be low-end, you'd think, why not go really low-end? Why not, like... I don't know. I guess it's just how they position themselves.

**Dave Jones:** Well, there's no market. It shows how pathetically insignificant this Arduino market is to these chip manufacturers. It's nothing. It's chump change. Yeah, I know that.

**Chris Gammell:** I didn't mean actually developing for that.

**Dave Jones:** They're just including...

**Chris Gammell:** I just meant, like, the friendlier package type, you know, like, just as a signal.

**Dave Jones:** Yeah, no, well, that's what I'm talking about, right? The friendlier... There is no market. According to them, there is no market for it. This is all their reason. It's chump change market, and they simply are not interested. Yet, they'll happily throw on this Arduino bloody shield footprint, right? Just into the wank market, right? Well, I'm not even talking about that.

**Chris Gammell:** I'm just talking about, like, getting it into two-layer boards, right? That's all I really think about. I know, I know.

**Dave Jones:** But they claim there's no market for it.

**Chris Gammell:** I guess maybe that is a signal of, like, lower costs. Like, they don't want to, like, be perceived as, like, cheap stuff or... I don't know, but...

**Dave Jones:** No, no. They probably don't want to have the race to the bottom, right? Yeah, right, right. Because then, if it's only, you know, if it's a 20-pin quad, you know, huge-pitch quad flat pack, then they're going to... People are going to want it for a dollar, right? They're not going to pay 10 bucks for it. Because, ooh, I could buy a, you know, micro for, you know, a couple of bucks, right? And so, yeah, they're just not chasing that low end. It doesn't...

**Chris Gammell:** Yeah.

**Dave Jones:** Anyway. Yeah. I know.

**Chris Gammell:** Are you a Xilinx guy still, or are you a... I'll use whatever.

**Dave Jones:** Yeah. That's the best fit for the purpose. Gotcha.

**Chris Gammell:** Usually it comes down to tool change for most people. That's what I've seen.

**Dave Jones:** Yeah, it does, but, oh, but, you know, I'm... You know, I've used both. It makes no difference either way for me. Both.

**Chris Gammell:** There's only two. Well, both. I've used three.

**Dave Jones:** No, well, there's, you know, there's three or four of them, you know.

**Chris Gammell:** Yeah, there's four. That's the answer, Dave. There's four. Yeah, exactly. There might be another startup at some point.

**Dave Jones:** Yeah, but there's two big players who own 90% of the market. Yeah. The others fight over the 5% each, you know.

**Chris Gammell:** Yep, yep, yep.

**Dave Jones:** Crumbs, right. So, hmm. Anyway, the Max 10, yeah, blah, blah, blah. It's got a 12-bit ADC in it that probably only has eight effective bits, blah, blah, blah. Which is, you know, handy. Yeah. That's fine. Yep, yep. It supports DDR3, blah, blah, blah. It's got an internal RC oscillator, which is kind of handy if you just don't give a toss about, you know, hey, yeah, it's around about 20 megahertz. It doesn't have to be exactly. It's good enough. Right. Which is great, right? There's one less bomb item you have to worry about. You know?

**Chris Gammell:** Imagine that movie, Billy Madison. I imagine the chip being like that, where, like, the drunk guy wakes up. It's actually Norm MacDonald. And they go, what day is it? Uh, October? Right. It would be, like, using an RC clock as a real-time clock would be like that, you know?

**Dave Jones:** Right. Okay. Oh, you can get within a couple of percent.

**Chris Gammell:** I know, but I'm just saying, that's what I think of, right? You know, like, that's... You're right. Yeah. October?

**Dave Jones:** Yeah, right. Anyway.

**Chris Gammell:** So, I was at the... Speaking of chips, I was at the Hackaday 10th party this week, or weekend, rather. And there was one talk by Lost, the guy that does the badge for DEF CON. That was really cool and definitely worth watching. But the other guy that talked... Actually, the other guy that works on the badge was talking a lot about Propeller stuff. And I realized that we actually never mentioned a pretty interesting thing that kind of involves FPGAs as well. A while back, Propeller, or Parallax, they actually open-sourced their entire... They did. ...design. And we didn't mention that, so... I'm sure we did. I know we didn't, because someone yelled at me.

**Dave Jones:** Oh, right. Well, I mentioned it on Twitter.

**Chris Gammell:** Oh, yeah, yeah. I mean, I saw it there, too.

**Dave Jones:** I'm pretty sure I did. Or somebody, yeah, somebody yelled at me on Twitter because I forgot it, and then I yelled back. Yeah, that's what it was. Yeah, okay. Yeah.

**Chris Gammell:** Yeah, so it's really interesting, too, like, you know, that you don't really see that. I know... So they said open-sourced as well. I know that you could get an ARM Zero core. I'm not sure if it was actually... It might have been encrypted, though. But I remember you could get that and put that on FPGA. And there's a couple others you can get out there, you know, that... But I don't know if any of them are actually, like, open-source, open-source. Right.

**Dave Jones:** Right. So has anyone now taken that design and put it onto an FPGA?

**Chris Gammell:** Well, I bet they did. Oh, right. Okay. But, yeah. I don't know, though. And it's kind of weird, too, because they... So I had never really looked at the logic blocks and all the stuff that's actually internal to the chip before.

**Dave Jones:** Well, it's a multi-processor chip. It can do multiple things. And it's kind of pointless. It's like, why... If you get onto an FPGA, why put a soft core into it? Even if it... And it's a multi-core soft core. It's like, you know... Like, just buy the chip. Just use the damn chip. You know, like, why put it on an FPGA unless you have to integrate other stuff with it? It's like, I don't know. You just make a life hard for yourself.

**Chris Gammell:** So the times that I... I've used a couple of soft cores before. And really, it's like, because you have firmware resources, you're doing something in logic, you know, and you don't want to put a separate micro and have the memory interface and everything else. But even that, it's always been really messy.

**Dave Jones:** Yeah, I know. It gets messy. That's what I'm talking about.

**Chris Gammell:** Yeah. But I think... Why make it?

**Dave Jones:** I'd rather have separate tasks and put the effort into the PCB layout to actually do that than to put it into the FPGA.

**Chris Gammell:** Well, the other thing there, too, is sometimes you can get... You could... If you were in... I'm talking out my ass. I actually don't know. But the theory, I think, is that you could... If you could save money on a micro, you know... These days, it's so cheap that it's just like, well, yeah, just throw something on there.

**Dave Jones:** Exactly.

**Chris Gammell:** I think a lot...

**Dave Jones:** No, because FPGAs are not cheap, right? To get them a decent amount of logic core and everything you want, they are not cheap. Right. So you've got to have a good reason to use them. Yeah. And they're complex to use. The tools are complex. And, you know... So you've got to have either... It's got to be like a flexibility reason, a multi-processing, you know, hardware, you know... You've got 20 serial interfaces. Yeah. Okay.

**Chris Gammell:** That's the example I was thinking of. You know, like... And when you really, really need a lot of customized... You know, like you can't find it, so...

**Dave Jones:** Yeah. Yeah. That's right. Or you need 20 different micros to do the job. Okay. Well, you move to an FPGA. Fine.

**Chris Gammell:** Yeah. There's probably better ways to do if you need 10 to 20 micros, though. So, I mean, it's still interesting, though. I mean, I think the fact that Parallax did that, that they released it. And the reason they did is actually they're working on a second version of it. Now, what I didn't realize is that they have their own programming language. You can use C, but, like, there's also... Right. Spin is, like, the programming language. Yeah, that's right. Yeah, yeah. It's a high-level thing.

**Dave Jones:** Yep.

**Chris Gammell:** You kind of got to drink the Kool-Aid and jump into their... Right. Yeah, their thing. Their way of thinking. But I think that there's benefits to that. You know, thinking about, like, coprocessors and stuff like that for, like, robotics. I know a lot of people talk about Parallax stuff for robotics is good, so...

**Dave Jones:** It's probably the lab view of the microcontroller world, perhaps. The lab view?

**Chris Gammell:** What do you mean, like, because it's...

**Dave Jones:** Yeah. Yeah, because it's our own unique language, and it's... Yeah, well, it's not... Well, I think it's not far off that, isn't it? Or something? I don't know. Anyway, I haven't used it.

**Chris Gammell:** It looks like... I mean, Johnny Mac was talking about the Parallax stuff. It looks like Python-ish, you know? Okay, right. But kind of, like, shorter commands, so... All right. Yeah. It was very interesting. You know, all the talks that day were quite interesting, so... A lot of those are going online.

**Dave Jones:** Yep.

**Chris Gammell:** That's fun.

**Dave Jones:** I think that's probably the best thing they could have done, is open-sourced. That it will ensure the survival of it.

**Chris Gammell:** Yeah, well, and plus, it's just interesting for users to be able to dig in. Because otherwise, there's always risk going out of business. You know, like, you can just... You can actually go and look at the code then, and, you know, maybe that piques some interest into getting into chip design, that kind of thing, so... Yeah, it's...

**Dave Jones:** Or if it's scalable. Like, because this is already, like, a... I think it's like an 8-core processor or something, this Parallax thing. If you can sort of then... If they've done it, like, modular so that you can, like, expand that when you put it into an FPGA. Oh, you need 20 cores?

**Chris Gammell:** Yeah, they mentioned that.

**Dave Jones:** Sweet. Oh, the cogs. Oh, the cogs. Cogs, they call them. Yeah. Yeah, you can expand it out. Oh, you can just expand them. Yep. Ah, see? Now, that's clever.

**Chris Gammell:** See, the only thing I don't get about that, though, is that I thought that, like, they have interesting analog peripherals on the end of, like, the actual... Maybe it's the new one. Maybe that's what I was thinking of. But, like, they had interesting non-standard logic blocks.

**Dave Jones:** Yeah, which you can't get when you translate it to an FPGA.

**Chris Gammell:** Yeah, so if you have, like, an analog pin there, you can't do that on most FPGAs. No. No, that's right. I mean, obviously, I'm not... I don't know what I'm talking about here, but...

**Dave Jones:** No, but it's right. It's just the processor side of things. Yeah. Yeah. It's not the analog blocks. Yep.

**Chris Gammell:** Yeah, so... It's cool. I basically... I've come to the point where it's like, all right, I'll go look at that more. Right. Yeah. So...

**Dave Jones:** No, like, if I wanted to do parallel processing, I would certainly check it out.

**Chris Gammell:** Yeah.

**Dave Jones:** Otherwise, it's like, meh, I might as well stick to, you know, if I'm just doing my regular micro single task thing, I'm just going to stick with a little micro. Oh, yeah, simple.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? Yeah, of course.

**Chris Gammell:** Yeah. Are you... Do you use PIX on your stuff a lot?

**Dave Jones:** What did you use? I use both. Yeah. PIX, app bells. I'm not fussy. Yep. They're the two I mainly use.

**Chris Gammell:** Okay. Yeah. I've been looking at a new platform, trying to just try out new stuff, and I've never used a PIX before, so I'm interested in it, but... Right. ...not really sure where to go with that stuff. You know what I mean? Like, it's like, well... Yeah, yeah. I'm kind of choosing just because I want to try something different. It's not necessarily like I'm being forced into it. Right.

**Dave Jones:** Okay. Right. And I'll usually pick based on my requirements, right? I go, you know, I need to meet this price point, and I need these features, and, you know, pick... Yeah. ...and you just have a larger range of chips that suit your thing than the Atmels, right? The Atmels are sort of like, you know, yeah, everyone uses an AT8 Mega or something, right?

**Chris Gammell:** Yeah, AT8 Mega 328. Yeah.

**Dave Jones:** Right. Or something like that, right? So, whereas microchip have 10 times more range of chips... Right. ...to suit a specific niche thing, you know? And that can be... That has its good and its bad points in terms of longevity and availability and all that sort of jazz, but... Yeah.

**Chris Gammell:** Anyway. Yeah. Well, and that's another thing. Someone mentioned at this thing over the weekend is MP Lab is like the... I think that's the online thing or something like that, or there's like the development tools or something like that?

**Dave Jones:** No, it's totally changed since I've last used it. Okay. A lot of people complain about it now. Yeah. I haven't used it since the complaints have come out.

**Chris Gammell:** Yeah. Yeah, I don't know. And like there's other stuff out there too, like the embed. Like that's another one where it's like, I think that's actually online. Because, you know, we were talking about like the online CAD stuff, but then there's all these online compilers and, you know, IDEs and stuff like that. Yep. And that's, I mean, it's interesting to me, but again, it's like I don't really, you know, I'm used to like the download the IDE struggle with it for a long time. Yeah. I mean, you know.

**Dave Jones:** That's right. Install it and then figure out how all the projects work and all that. Yeah. Yeah. That's right.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Yeah. Yeah.

**Chris Gammell:** Same here. So it's just kind of like, you know, getting older. That's not stupid. I'm not that old. Exactly. But like, but you know, like just kind of as new stuff pops up and forcing myself to try it.

**Dave Jones:** Well, like if I had to use a new device, that would be compelling for me. If something had just a browser based compiler and it just worked or something, I might give it a go.

**Chris Gammell:** Just to try out the browser based, you mean?

**Dave Jones:** Well, no. Just because like I wanted to use that particular chip because it had the features of the price or whatever I wanted. And then if it had, but if I knew it had, you know, some complex compiler chain that I had to download and struggle with to get working, then I'm going to groan and go, oh, I don't think so. That's true. But if it's got something you really dumb ass user friendly, you know, browser based compiler or something that just works, then I'm going to go, hey, yeah, I'll use that. You know, because I'm not betting the farm. I just want to do a project, you know, I do it project from project, right?

**Chris Gammell:** Yeah. Project to project.

**Dave Jones:** And I don't care if I... Right.

**Chris Gammell:** And your long-term risk is not there as much either, right? You don't have to lock down your tool chain. Yeah, because I was thinking about that.

**Dave Jones:** I'm not committing my entire company to change to this architecture. Right.

**Chris Gammell:** Yeah, that definitely does change stuff. And like when I think about like trying out new chips, like that's kind of what's always guided me in the past. It's like, okay, well, I don't really have a choice, you know, unless you're doing it on your

**Chris Gammell:** Right. But, you know, it's like, okay, well, you're using microchip parts because everybody does it at your company or Freescale or whatever else, you know? Yep, that's right. And yeah, so I don't know. Yeah, same kind of thing for me. I'll have to try that out and see. I guess the benefit of that and what they're probably banking on is that like, you know, people like us or people that are coming into the industry as well, like if you don't know any better, you know, if you don't have these prior expectations, like, yeah, of course, you just kind of roll with it. If it works, it works. Cool. No big deal. Right. If it doesn't work, we can play the vampire.

**Dave Jones:** At the end of the day, that's all I care about. Does it work? Did it cause me any grief? Is it going to cause me any grief? Right. Yes or no?

**Chris Gammell:** And usually, and the other thing for that too is like, we won't know until later. You don't know until you try it and really get burned as you go to production. But yeah, I guess we'd have to depend on the kindness of strangers to let us know about that beforehand. Exactly. Yeah. Yeah. There was a bunch of stuff from, there was that ARM conference last week as well. So there's a bunch of new ARM stuff that got announced. But this, this Atmel one looks interesting as well. Like the, it's basically like a little embed basically. So I think it could, I think it could do the online stuff, but then it's got a radio on board and interesting things, I guess. I don't know. It says IOT. So I'm like, man, but I mean, like I, like I said, I am interested in trying some of these online, the online tools and you know, if I'm going to give the online CAD tools a try, I might as well try the online code tools. I definitely need more help with one than the other. So yeah.

**Dave Jones:** There you go. Yeah. That Atmel's an internet of things development platform. Yeah. You can see me doing the whoop-de-doo hand gesture right about now, twirling it around.

**Chris Gammell:** Yep. Yep. Exactly.

**Dave Jones:** Goodness gracious. Can we stop talking about that shit now? Sure.

**Chris Gammell:** Yeah. Anything else this week? We're actually kind of a...

**Dave Jones:** No, we're over time, dude. 10 minutes over time.

**Chris Gammell:** Yep. We've got things to do. Yeah, sure. Yeah. I have to go eat dinner. Actually, no. This, we should have brought up earlier, but there was a good article earlier this week, kind of like on the same vein as the 3D printer side of things, but basically talking about the differences. I think it was actually from Bolt. The Bolt guys wrote this, but basically how you can't be like Apple for manufacturing. And, you know, like the same assumptions do not apply to everyone. So that's... Right. That's definitely worth the read as well. You know, as people are getting into manufacturing things, if they haven't already, it's good to have those things in mind. So... Right. I think that's it from the list. Hopefully I didn't... I think we're done. Yeah.

**Dave Jones:** I'm going to go. Okay. Shoot some more video and hopefully my camera doesn't... Oh, yeah. ...screw up and not record the footage. That pissed me off. Time to build your own camera, man.

**Speaker ?:** Oh, man.

**Dave Jones:** Unbelievable. All right. Cool. Anyway. See ya.

**Chris Gammell:** Catch you next week. Bye.

**Speaker ?:** Bye. Bye. Bye. Bye.
