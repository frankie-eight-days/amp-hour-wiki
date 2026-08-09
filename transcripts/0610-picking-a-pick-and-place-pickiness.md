---
episode: 610
title: Picking a Pick and Place Pickiness
url: https://theamphour.com/610-picking-a-pick-and-place-pickiness/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released November 20th, 2022. Episode 610. Picking a pick-and-place pickiness.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** Stop me. Please stop me. No, it's not what we were talking about just before the show. It's from buying a pick-and-place machine.

**Chris Gammell:** I knew that was it. Right.

**Dave Jones:** Okay.

**Chris Gammell:** Here's the thing. Okay.

**Dave Jones:** Okay.

**Chris Gammell:** Well, do you actually want me to stop you? Because I'm probably going to encourage you to. Right. Bastard.

**Dave Jones:** Here I am crying out for desperate help.

**Chris Gammell:** Yeah, I mean, it benefits me for you to have stuff to talk about. Right.

**Dave Jones:** Okay.

**Chris Gammell:** So what's the thinking? I mean, what's the.

**Dave Jones:** I don't know. I just got the, you know. Got the urge. Just got the urge yesterday. I thought, you know, look, my content's getting a bit stale. Maybe I just want, you know, freshened up. Maybe I could do like, yeah, some new content on pick-and-place stuff. And maybe I could do like a series perhaps. You know, I always plan these things, but they rarely come off. But, you know, the plan would be like maybe do an entire design from design through to actual production, in-house production, you know. I like it.

**Chris Gammell:** Yeah. Here's the problem. Like, where are you going to put all this stuff? Where am I going to put it? Yeah. Because, I mean, like picking places, even the small ones aren't that small. You know, like.

**Dave Jones:** But they're desktop ones. I'm talking about like a desktop one. I'm not talking about like a.

**Chris Gammell:** And that's what I mean. They'll take up a bit of room. They do.

**Dave Jones:** But have you seen my cleaning video of my bunker? I've got a lot of bench space in my bunker now. I've got a. I've got maybe, I don't know, four meters of bench space that could easily handle a pick-and-place machine, a thermal oven, a stencil area. You know, all that.

**Chris Gammell:** Yeah, you get, did you, well, we had, Saber was on the show talking about his vapor phase, the vapor phase one. That's the prosumer, prosumer vapor phase machine. That thing was, that's pretty cool. You get one of those too. How much? 5,000.

**Dave Jones:** Oh, okay. Yeah. That's kind of what I'd pay for the pick-and-place machine. So that's a bit pricey for a.

**Chris Gammell:** It's definitely pricey. But like, I don't know. Whenever I do, you know, even when I do hand pick-and-place. So this is like why I was excited to talk to him about it. Like, even when I do hand pick-and-place, the thing that always trips me up is bad reflow. Like, I could, you know, if you have good, you know, if you have decent paste application and if you have decent part placement, you know, even hand placement, solder paste takes care of the rest. Yeah, yeah, yeah. But if you have bad profile and like bad reflow. Bad soldering profile. Yeah.

**Dave Jones:** I just haven't done enough volume in-house to sort of, you know, it's always kind of worked for me.

**Chris Gammell:** Yeah. Like to dial it in. Right. Exactly. Yeah, yeah. It's always, it's always a fresh. You're always starting fresh. So that's like, you know, it's like you have to figure stuff out at the time of assembly.

**Dave Jones:** And it can change greatly. For those who don't know, the thermal mass of a PCB can change dramatically. Whether you've got a two-layer board, four-layer board, the amount of copper on there, the thermal relieves you've got to your pads and all sorts of, you know, the thickness of your copper. If you use, you know, one ounce or half ounce copper, you know, if you're doing a big power board or something. Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. I mean, yeah, there's a whole, there's a whole science to it. I mean, and, and really, I think the other thing too, is that like, even when you have a manufacturer engineer, that's like figuring out the profile over time, like they're figuring it out over time. They're not like, they are going to have a much better shot at it than you or I are going to.

**Dave Jones:** They'll have more knowledge off the top of their head about, oh yeah, this is a big full run.

**Chris Gammell:** Multiple runs. You just dial it in, you know, like you figure out, you know, you do, you do some test runs and then you figure out how the profile needs to change and you dial it in. It's like, yep.

**Dave Jones:** We had that once we were doing a trade show board and I've, I've done a video on it. It's that weird red shaped board with the curved things, you know, you, yeah, you've, you've probably seen it. And that was like, it was supposed to like, it was supposed to work. Right. So we had to, it was actually a proven design, but we just modified it. Right. So we modified the board. I actually modified it. So it was way thicker. So it was like a three and a half millimeter thick board or something. Right. It was like really thick. Right. It was an eight layer jobby from memory. Yeah. Just the sheer, like the thicker board and everything else. And I think we had increased copper or something on it. And so, you know, make it look more wanky and industrial kind of thing. Cause it was going on the trade show stand. And then we put it through our normal reflow process or our assembler did put it through the normal reflow process that we did for our near identical board, but was much thinner and everything tombstone. All the 0402s, they all tombstone. And it was like, Oh God, we had this dialed in, you know, and then we actually changed the thickness of the board. And, you know, I don't know, we report some, you know, ground planes or something. And no, it just all come a gutzer completely. And yeah, I had to manually rework all of those, like, you know, hours before the trade show or something. Oh God.

**Chris Gammell:** So I do want to, I do want to stay on the pick and place topic, but I do want to say as well that I just gave a talk at Supercon about the one engineer dev shop and, and this portion of it, of like the assembly at home.

**Dave Jones:** Yeah.

**Chris Gammell:** I was, I was tempted to not put it in as like a time saver kind of thing. Like, so like the whole talk was about like, Oh, well, you know, you can do so much more as one engineer dev shop. You can do the mechanical, you can do all the design, like all of the stuff that you can do. And the truth is you can do all this stuff, but I think this stuff slows you down. Honestly. I think if, if, if you really want to speed it up.

**Dave Jones:** It does. If you're doing in-house. Yeah.

**Chris Gammell:** Yeah. It's not super high. So like, so I think your case is a special case here.

**Dave Jones:** Oh, my, my, my case is totally special.

**Chris Gammell:** Yeah. Yeah. And I think, I think for the most, you know, like when I think about small dev shops or one person dev shops, like myself, like that most of the time it's not, it's, it's low margin work, right? Yeah.

**Dave Jones:** You're better off paying five bucks per board and just getting someone to assemble it for you. You know? Totally.

**Chris Gammell:** Yeah. I mean, yeah, a lot more than five bucks usually, but yeah. Yeah. Yeah.

**Dave Jones:** Mine was five bucks. I was, I was paying five bucks to get my micro current assembled here.

**Chris Gammell:** Okay. That's, that's pretty good.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** I, I usually don't see those kinds of prices. Right. Okay. Yeah. Yeah. Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** But for you, I think you're trying to showcase the process and.

**Dave Jones:** exactly. I'm making content. It's all, you know? Yeah. Yeah. Yeah. It's a totally different, totally different thing.

**Chris Gammell:** But I remember following an Aussie that was doing some board stuff. I don't know if they were in Sydney though.

**Dave Jones:** That was.

**Chris Gammell:** But it was like home lab.

**Dave Jones:** Unexpected maker. Yeah. Was that unexpected maker who had. All issues. I do follow him as well soon. Yeah. Charm high. He, he had a charm high pick and place and had. That's right. No end of problems. Then he switched to near then.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** But I didn't follow what happened after that.

**Chris Gammell:** Yep. Well, he makes a ton of boards too. That's not exactly. That's actually not who I was talking about. This is a bed shot. Okay. Did some like slightly more industrial type stuff. It wasn't stuff that was like smaller boards. These were like larger boards. Right. But, but I mean, is, is unexpected maker in, in Sydney or somewhere else?

**Dave Jones:** I don't know where he is actually.

**Chris Gammell:** Oh, okay.

**Dave Jones:** I don't know. He, he just got a new factory. I just watched his video before this show actually. Yeah. He's got a new, just a new, one of those, you know, big roller door industrial, you know, factory kind of spaces, 120 square meters downstairs with an additional floor, you know, one of those hesineen type floors above. So yeah. Yeah. He just rented that and good luck. Yep.

**Chris Gammell:** Yeah. So here's the, here's my usual thing. Like, I feel like most people that start out saying that they need a, need or want to pick in place. They, I feel like the, the duty cycle of like needing a pick in place is quite low. Right. So like, yeah, of course. Yeah. You know, like the most.

**Dave Jones:** You use it five times a year or something at most.

**Chris Gammell:** Yeah, exactly. Exactly. And so like, you know, you're going to use it more if you have it theoretically, but I feel like it's just like not, you know, you're not starting a manufacturing business. That's the time to really, if you were going to start a small manufacturing shop.

**Dave Jones:** Well, see, I could sell boards. That's another thing. Right. I could like, oh yeah. I could come up with a little project every now and then and, and get it assembled and sell a couple hundred of them or something, you know.

**Chris Gammell:** And that's like.

**Dave Jones:** It's interesting.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** You make little IOT things, you know, you get really excited. Right.

**Dave Jones:** Yeah. And that makes, yeah. Yeah. And I see, see, that's the thing. Like if I had it, I might go, oh yeah, I could, you know, I could come up with constantly come up with little project ideas, you know, and then do a small batch run and then, you know, and then sell a hundred or two.

**Chris Gammell:** Yeah. You could send stuff out to Patreon backers, stuff like that. Yeah.

**Dave Jones:** Yeah. Yeah. Right. Stuff like that. So, you know, I can value that way. So totally possible.

**Chris Gammell:** I don't doubt that you could talk yourself into it. If you really want me to talk you out of it, I will talk you out of it.

**Dave Jones:** I can definitely talk myself into it.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Well, what are the, what are the prices of the things? Obviously you've done some research on it. So like, what are we looking at there?

**Dave Jones:** It was the Neoden YY1. This is a new release. I just put it on the Reddit list there. Okay. There's an EV blog forum that just came out. They just released it like in July, I think, but people didn't get their hands on it until very recently. So it's, it's brand spanking new. Even the manual.

**Chris Gammell:** Have you run your own pick and place before? Sorry? Have you ever done that? Have you ever run your own pick and place machine?

**Dave Jones:** No. No. Not as such.

**Chris Gammell:** So I run the Neoden 4 and it is some of the worst software I've ever used in my life.

**Dave Jones:** Right.

**Chris Gammell:** Like the hardware is not bad. Right. But the software is just abhorrent.

**Dave Jones:** I've heard that the Chinese software, it's all in Chinese or something.

**Chris Gammell:** It's all, it's not the, it's, you know, Chinese, not Chinese. It's just like, it's like bogus Windows software. Right. That's what it really came down to. You know, like I said, the hardware is okay, but it was really then the struggle that I had was like trying to dial it all in. Like, like.

**Dave Jones:** Right.

**Chris Gammell:** And like the opaqueness of what it actually, what actually each of the things was. Like, I think they'd expect that you maybe have a FAE or someone with knowledge about it. It's just like the, I, I personally, I had a really hard time dialing stuff in.

**Dave Jones:** Got it. Yeah.

**Chris Gammell:** So.

**Dave Jones:** Hmm. Interesting. Anyway, they have released, you're talking about prices. They have released the new Neoden YY1 and I can send you a link here. Basically under 3K with like 40 feeders.

**Chris Gammell:** With the feeders are built in.

**Dave Jones:** With the feeders are built in. Yes. They're, they're not removable, uh, cassette feeders. They're like, you know, yeah, they're, they're built in, but under 3K. Right. For, for a dual camera, dual head with automatic tool changer. Right. And it supports, you know, shaker tubes as well. And it supports, um, bulk feed in bulk placement and other stuff. You know, it's like, it looks really quite good. So, but once again, yes, there are one or two people on the EV blog forum who now actually have one. And there, I just watched a video just before this and yeah, like it only supported one fiducial. One.

**Chris Gammell:** Oh, really?

**Dave Jones:** Yeah.

**Chris Gammell:** Oh, really? One. So like if you're doing a panel, you will get one? Yes.

**Dave Jones:** So if you only do a panel, you only get one fiducial. So how it knows where the other corner is, I, you know, yeah, it's, you know.

**Chris Gammell:** Yeah. You know, that was another problem that I had with, so I, like I said, I use the Neodon four and it had like the rails and the rail. So like I panelize stuff and then like the calculation between like the panelized version versus the onboard version was like really weird. And I don't know. I'm sure a lot of it was operator error. No, no, no doubt about that. Right. Yeah. I, yeah.

**Dave Jones:** But the main takeaway from his video after he's, you know, done a few panels with it is that it's the, like, like the hardware is quite good and it works with the one fiducial and, you know, it, it's sort of, you know, it's, it seems to work okay. Except the fee, the tensioners that pull the tape back, they rely on a friction pull. So apparently it doesn't work properly with, it works fine with paper tape backed. Uh, reels, but it doesn't work fine with plastic backed reels, which are most of the ones I've

**Chris Gammell:** seen quite frankly. Yeah. That's like a lot of the diodes are in plastic. Yeah. Yeah.

**Dave Jones:** They've got the plastic wrap on top and apparently it slips and, and it gets jammed and gets wrapped around itself. Yes. And, you know, all that sort of, yeah. But there, there it is 20, it's on eBay. Don't even have to go to AliExpress. eBay, $28.99 US. And that includes like 43 feet, 45 feeders. Right. It's got two cameras and it's got like a hood over the top. So it looks quite professional. You know, it looks kind of like low end professional, um, which, which the Neoden brand is the, they're, they're sort of like, you know, the budget, like they do make big floor standing ones. Prosumer. Yeah. Sort of like prosumer.

**Chris Gammell:** These feeders are 3D printed. Do you see the seventh image on there? There's like a camera and then there's feeders next to it.

**Dave Jones:** Oh yeah, you're right. They do look 3D printed. Definitely FDM. Maybe that's the prototype. Maybe that's the prototype. That's interesting. Yeah. Well spotted. It does look 3D printed. Yeah.

**Chris Gammell:** I mean, 3D printing is cheap to do these days.

**Dave Jones:** Anyway, they are a name brand, right? This is a company that I've, I've seen them at, at, at the trade show here in Sydney. Right. They've even had a stand. Right. For, you know, like, yeah.

**Chris Gammell:** Well, maybe they were targeting you specifically, you know, like they're just following you on the internet.

**Dave Jones:** But anyway, like it's got automatic tool changer, you know, dual head, dual cameras, like, you know, and it's $28.99 US. Sure. It's a thousand bucks postage to Australia, but.

**Chris Gammell:** Yeah. What do you think the resale would be? Because I feel like that's the real thing is like, can you unload this thing if you wanted to?

**Dave Jones:** Oh yeah. Someone would buy it. I've, I've, I've actually got an eBay watch list for pick and place machines. So I, I've been watching all the pick and place machines that come up secondhand here in Australia and they always sell. So they seem to sell for quite decent prices. Like you can't pick one up cheap. Like. Yeah. It's pretty rare. So I don't know.

**Chris Gammell:** So.

**Dave Jones:** So, okay.

**Chris Gammell:** Well, how about this? So I got to hang out with Stephen Hawes, who does the lumen pick and place. That is a open source one.

**Dave Jones:** Yeah.

**Chris Gammell:** Lumen pick and place. And. Yeah.

**Dave Jones:** No, I, people have asked me this on Twitter. Why don't I just go for one of the open source pick and places? And it's like, like, I don't want to be making videos. Oh, assembled.

**Chris Gammell:** Assembled. Yeah. It's assembled.

**Dave Jones:** Okay. So this is a company based.

**Chris Gammell:** So the design is open source. And then you were shown. This is the.

**Dave Jones:** Opulo. Opulo. Yes. That's right. Right. Okay. I didn't know it was called lumen pick and place. Yeah.

**Chris Gammell:** The lumen, I think is the name of the actual.

**Dave Jones:** Yeah. Mike from Mike's electric stuff. He chimed in on Twitter and said that. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. The, the Opulo is now this lumen pick and place is now like the kind of like the best, like open source one you can get, but it's like open frame. Like where the hell. And I asked somebody in Twitter, where the hell are the feeders? Oh, they're in beta. You know, it's like, I don't want to be making videos about. Yeah.

**Chris Gammell:** I mean, I think it's kind of like buying a, buying a finished, finished or maybe like a prosumer 3d printer versus kind of more, a little closer to a point, maybe a little bit, you know? So I think, and I think Steven would probably say that he's trying to be kind of like a Prusa of, of picking places. Right. So it's still open source, but high quality, that sort of thing. And like, you know, I think the Prusa stuff in the 3d printing world, I think the Prusa stuff still stacks up as like high quality, high support, you know, like, you know, so one thing I look at personally, when I look at stuff, when I was looking at 3d printers, it was like, look, I don't, I don't need the highest end newest thing, best specs. I need most supported, most community, so that I can like, reliable, but I can go and ask a bunch of people, right? I don't want to be searching and run out of forum threads when I run into something. I want to, I, every time I have a problem, I want someone else to already have figured it out. That's my, that's my goal. I want to be trailing edge, you know, that sort of thing. You know, I think you won't get that with the Neodem stuff for sure.

**Dave Jones:** Well, no, there's Neodem forums. I think there's, they're quite popular.

**Chris Gammell:** I just mean, cause it's a newer product. That's, that's all I mean.

**Dave Jones:** Oh no, it's, no, this one is a brand new product. It's just hit the market. So it's like, yeah, no, I'd be figuring stuff out. Exactly. Yeah.

**Chris Gammell:** So, you know, it's, it's just all trade-offs. I think one of the other trade-offs that you would have to deal with is that, you know, I think over your layout career, you got accustomed to being able to design super tight, tolerant stuff. And I just don't think, you know, you know, but your microcurrent is also not like super tiny stuff. I just think you'd have to kind of scale up and buy, do larger, larger scale parts, basically.

**Dave Jones:** Oh yeah. That's totally, I, I'm all for that. It's fine. Yeah. Yeah. No, I'm, I'm still a 0402 only if I have to guy, you know, for like any, if I'm doing a commercial design or something, yeah, it's a totally different thing. Right. But yeah. You know. Yeah. Anyway, this new YY1 is supposed to go down to 0201. So. It doesn't.

**Chris Gammell:** I always, always step up one, one up from where they stay. Always step up one. Yeah. That's funny.

**Chris Gammell:** Because they, they're going to give you the specs for that. And it's like, yeah, they can do it, but you have to sit there and like dial it in and babysit it.

**Dave Jones:** Yeah. Yeah. Yeah.

**Chris Gammell:** Like the Neoden IV could quote unquote do 0402, but what they're saying is like, it has the tolerance to do 0402. Yes. Not that it has like absolute repeatability to do it, you know, and not at speed either. So it's like, yeah, if you like, you know, click refact, you know, get over the camera really, really dial that thing in. Like, yeah, it can all, it all, all of the tolerances stack up and you could do an 0402, but you're not going to have a good time at all.

**Dave Jones:** See now look, right. I'm looking at this Opulo one, this Lumen pick and place, right.

**Chris Gammell:** Sure.

**Dave Jones:** And I'm seeing that it's 1745 bucks us, right. That's only a thousand dollars less than this Neoden YY1. And if you have a look at them side by side, right. There's, there's no contest, right. There's no contest. It looks like a kid's toy, right. Compared to a commercial pick and place machine. And it doesn't have feeders. And it doesn't have feeders.

**Chris Gammell:** The thing that you don't, the thing that you don't see on any of these though, is software stack. That is just a.

**Dave Jones:** I know, but if it doesn't have feeders and it's the same bloody price, then I'm probably living, I'm willing to live with, you know, tricky to use dicky software, but you know, I mean, like, right.

**Chris Gammell:** Okay.

**Dave Jones:** You have to remember 45 feeders, right. 45 feeders.

**Chris Gammell:** I think the Lumen is a little too much of, it's more kit than you want to do. And that's fine. I think you should. More kit than I want to do.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** No, I've, I've basically, I still have a light placer, open source pick and place machine. Yeah. I haven't assembled.

**Chris Gammell:** You should just. Just do that. Yeah. Yeah. Yeah.

**Dave Jones:** Then I can just do videos on how I'm dicking around trying to get that work.

**Chris Gammell:** Yeah. Yeah. So you want to buy a tool.

**Dave Jones:** Their feeder does look very impressive. They've got this like do it yourself feeder design and it's got all the circuitry on there and it's got like, you know, presumably like motor in there, motor drive or something. Yeah. Yeah. It looks, looks really, you know.

**Chris Gammell:** Yeah. I mean, Steven does a bunch of YouTube stuff about, about this stuff. So I'll, I'll link that in as well.

**Dave Jones:** But I want to be doing, if I'm going to do this, I want to be doing videos on the viability of a pick and place machine for in, you know, in house production rather than doing a, rather than just, yeah. Rather than just dicking around trying to get some open source thing and some beta prototype feeders working.

**Chris Gammell:** You don't care about the openness so much as the. Yeah.

**Dave Jones:** I don't care. That's, that's totally fair. That's.

**Chris Gammell:** Yeah. I think that's. Yeah.

**Dave Jones:** I think my audience would, would rather see me use a low end commercial pick and place machine that they could potentially afford for their little garage set up. Right. And what are the real results from that rather than, oh, okay. Dave's playing around with this open source pick and place machine and, you know, like, yeah. So as much as I like it and hats off to them. It looks, you know.

**Chris Gammell:** It's great.

**Dave Jones:** It looks great, but it's just, I don't think any of the open source designs are for me. So for my particular.

**Chris Gammell:** Well, then I think, I think we should just push you forward here, Dave. I think you should buy one.

**Dave Jones:** You think I should just buy one and just.

**Chris Gammell:** I think so.

**Dave Jones:** See what the pain is. And then if it's too much pain, I just sell it. I just resell it on eBay. Yeah.

**Chris Gammell:** I mean, probably it sits in your basement for a while. I mean, I think that's probably the honest thing, you know.

**Dave Jones:** Yep. Yep. Well, I would have to once. You know, I'd have to come up with actual designs and boards first to test. Yeah.

**Chris Gammell:** But it's going to take a while to ship. So you could do that between.

**Dave Jones:** Oh, I could do it between. Yeah. Right.

**Chris Gammell:** So if it says it's going to ship probably December. Come on the slow boat from China. Right. Yeah. I can get the cheap.

**Dave Jones:** No. Oh, that's FedEx. A thousand bucks for FedEx international economy.

**Chris Gammell:** Nice. There you go.

**Dave Jones:** Yeah. Oh, there you go. That's their only option. That looks like. No, I can. No, I can have this sucker between the 7th of December and 16th of January. Sometime between that date. Yeah. Yeah. Yeah. Oh, boy.

**Chris Gammell:** Well, I do think that, you know, this versus jumping into something, you know, if you went and bought a full, you know, what are the quad machine or like one of the ones that are Yamaha or something. Yeah.

**Dave Jones:** Like an old second hand Yamaha jobby or something. Yeah. Yeah. But it's so huge. That's the problem. And they need like three phase power and, and they need shop air, you know, factory air

**Chris Gammell:** and, you know, like, like it's serious. Right. You don't want to start a board shop. I think that's the right thing.

**Dave Jones:** No, I just want something that sits on my bench. Yeah. Like, cause I actually have a bunker with a long bench on it and I want to sit on the bench and then I'll have that and a thermal oven, have it all set up there, a paste stencil area and then stencil it, pick and place machine, run it, thermal oven. And, you know, I don't want some big floor mounted thing.

**Chris Gammell:** I'm going to be an enabler then. I say you go for it.

**Dave Jones:** You reckon I go for it. Okay. Well, that's what I, I did a poll on Twitter and they said 80, I think 80% of people say go for it. Yeah. So, you know, I think everyone just wants to see me in pain. You know, they just want to see me freak out about how fiddly these things are.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Anyway, it could make for fun content.

**Chris Gammell:** So, yeah, I find that the, you know, another thing that always tripped me up when I was doing this. So the reason I had access to the Neatotin 4 is when I was at M Hub, they had one there. Yeah. Yeah. That's right. I don't remember why they bought, I don't know if I was. Yeah.

**Dave Jones:** I think you were, you said you were the only one who was using it or something.

**Chris Gammell:** There were, no, there were a couple of people using it. There were, it wasn't just me, but the stencil, I had a lot of problems with stencils as well. Like, I don't know if it's just like my method or something, but like, you know, you just really need to get things like super, super flat. And I never, I never did it properly. Cause like, especially if I was doing like single boards versus panelized boards and like, you know, like, so if you could do panelized, it's a little bit easier, but it's still not great. And I don't know.

**Dave Jones:** You need one of those XY solder paste prototype dispensers. Oh yeah.

**Chris Gammell:** Oh yeah. You really want to.

**Dave Jones:** So that you don't like their slows are wet week, but like you don't have to make stencils. You don't have to do anything. You just press the button and go. Yeah. Yeah. Yeah. Yeah. It basically just goes blob, blob, blob, moves, moves the motor blob, blob, blob. Yeah. They're great. I've, I've got a video of one of those on my channel way back. Altium bought one. Yeah. So yeah.

**Chris Gammell:** Yeah. I think for low run prototypes, those are, those are the right move, but they're also like 50 grand. So like.

**Dave Jones:** Oh, they're, they're quite pricey. I don't think there's any cheap versions available. Is there? I don't. Yeah. Never followed it, but yeah, I suspect not.

**Chris Gammell:** Well, yeah, this is great, man. All right. Go for it. So you want me to. Maybe I'll ship you some board designs. You can just make some of my stuff if you want.

**Dave Jones:** Right. Okay. I'm sure I'd have no shortage of, you know, like I can always download some open source design and then just run with that, you know, and then just build, you know. Oh, that's so fun.

**Chris Gammell:** I mean, I guess at first, you know, at first you're always going to just be doing like the, you know, the, the test designs where you're just like putting resistors in a circle. Yeah. Yeah. Totally.

**Dave Jones:** That's it. Yep. Boring as anyway, there you go. Well, speaking of PCBs, did you know that mushroom skins are going to replace fiberglass?

**Chris Gammell:** Oh, I had, is this, did you point this? Oh my gosh.

**Dave Jones:** This was sent to me by Mrs. EEV blog. So you can blame Mrs.

**Chris Gammell:** EEV blog. Mrs. EEV blog. What the hell are you talking about?

**Dave Jones:** I don't know where the hell she got it from, but it's in a day of one. And Anthropocene magazine. Anthropocene magazine.org or something. Mushroom skins could be the secret.

**Chris Gammell:** That's the era we are living in, Dave, is the Anthropocene. The era of humans. Yes. By the way, the Anthropocene Reviewed is a John Green book. You know, the Vlogbrothers are like a YouTube channel and John Green is one of those. Yeah, right.

**Dave Jones:** I know of them. Yeah.

**Chris Gammell:** Yeah. And John Green wrote this book called the Anthropocene Reviewed, where he just does like Yelp reviews on stuff in the Anthropocene, like Yeast and Diet Dr. Pepper. And it's very enjoyable. I enjoy it. It's a great book. So highly, highly recommended. Oh, by the way, speaking of books, I finished the book. Did you finish the book yet? Kathy's book? No.

**Dave Jones:** Oh, sorry. No, no. I'm still, I'm all, I'm close. I'm getting close. I'm getting close.

**Chris Gammell:** I'm already halfway through another book on the grid, man. So you better, you better hurry up. I got stuff to talk to you about with that. Yep. Fantastic book and really good interview. So I enjoyed the heck out of that.

**Dave Jones:** Yep. It's good fun. Totally agree.

**Chris Gammell:** Okay. So mushrooms. What the hell?

**Dave Jones:** Mushrooms. Apparently there are 140,000 tons of electronic waste every single day. Yeah. And this won't go jack towards lowering that. Like, you know, it's like, come on. Like, anyway, yeah, they've got these mushroom skins and they mix them with something and they reckon they've sold it on them. And yay, we're going to.

**Chris Gammell:** I think this is the kind of thing where like you had like one grad student who did it. Yeah, exactly. And if we just extended it to.

**Dave Jones:** Oh, it instantly works straight to Kickstarter, you know, like straight to, you know, start engine. You know, I'm about to do. I, in fact, I'm behind the eight ball on a ton of videos at the moment. I've actually got several half shot videos, which is quite rare for me. And one of them is going to be, can we do a side tangent here onto start engine is one of those.

**Chris Gammell:** You're nothing if not side tangents, Dave.

**Dave Jones:** I built my channel on it.

**Chris Gammell:** That's right.

**Dave Jones:** Yeah. Start engine, if you don't know, is an equity crowdfunding site. So instead of getting a product like you do on Kickstarter, Indiegogo, you buy shares in a couple of shares in quote marks, ones that aren't listed anywhere. So you can't sell them to anyone. And I'm looking at, I was just going to do like a debunking video of one thing on start engine. And then I'm looking through start engine. I'm going, all these are shit. All these tech products on here are absolutely shit. And then I've got a page, some either wide article or something, which shows the greatest success stories on start engine. Right. Or something, you know, the biggest equity crowdfunding ones. And it's like, oh yeah, we made 300% return. And it's like, well, 99% of them are going to fail. And the 1% that wins doesn't pay back that much. It's like, you got it. Like you're guaranteed to lose. Do not invest in any of these companies on start engine.

**Chris Gammell:** Just do not do it. I mean, that's kind of, that's like right on the hairy edge of like what you're actually allowed to quote unquote invest in, you know, like there's. Oh yeah.

**Dave Jones:** Well, no, because you're deemed to be a professional investor. When you invest in these things, which means the laws don't apply, you know, or lesser laws apply.

**Chris Gammell:** Well, usually it's like, you have to have some like liquidity numbers that are like really insane though. Like $10 million liquid or something. No, no, no.

**Dave Jones:** The thing about start engine is you can invest with like a couple hundred. Oh yeah.

**Chris Gammell:** I meant, I meant in the normal case.

**Dave Jones:** Oh yeah. In the, in the normal case. Yeah. You need like the millions. Yeah.

**Chris Gammell:** Which, you know, is, is limiting and you know, it's a closed garden, walled garden. Yeah.

**Dave Jones:** I think here in Australia, it's called a sophisticated investor. If you're deemed, yeah. If you've got a couple of million dollars to throw around, you're deemed a sophisticated investor. And that means that you can't sue anyone if they try and con you or something because you should know better basically. Yeah. The laws are different.

**Chris Gammell:** They will try and con you. Yeah.

**Dave Jones:** And I'm looking at all these projects and they're all shit. They've all got 99, you know, 99% chance of failing. You know, it's just.

**Chris Gammell:** I mean, you could put one of your future circuit boards on there, Dave. I wouldn't, I wouldn't speak out against it too much.

**Dave Jones:** No, no, it's just bullshit. No, you're buying shares in somebody's. You're just paying somebody's wages for five years until the company folds and then they do another one. You know, that's how it works. And you can make a grift. You can grift for your entire career off this, just starting out companies and getting equity crowdfunding on StartEngine. Unbelievable. Anyway, avoid at all costs. Today's advice here on the Amp Hour.

**Chris Gammell:** Yes.

**Dave Jones:** We will take donations because we've saved you from all that loss. So we only ask for 1% of the money that you were going to put into all of these scams. Anyway, mushroom PCBs, yeah, nah. I don't think. That's just bullshit. No, yeah, nah.

**Chris Gammell:** I think there is room for organics in PCB production, but I don't know. It's probably going to be modified.

**Dave Jones:** Yeah, nah, there's so many exotic PCB materials these days. There's one for everything. But if you're going to toss it out, like the actual fiberglass resin is the least of your problems. You know, you've got all the bloody components and the solder and the, you know, the copper and the, like, you know, come on. Seriously?

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** I'm thinking you can solve the world's problems by, oh, yeah, I've just got the, I'm just going to replace the FR4, you know. No.

**Speaker ?:** No.

**Dave Jones:** Dreaming. Tell them they're dreaming.

**Chris Gammell:** I think you need to tell your wife she's dreaming.

**Dave Jones:** Yeah. Anyway, she sent it to me because she sends me interesting links if they pop up on her science-y feed, you know, thing, whatever. Yeah. She's into the science-y feed stuff. Anyway, yeah, I got a heat pump.

**Chris Gammell:** Heat pump. We talked about that last time. I'm looking through a list of what else. Yeah, I remember we.

**Dave Jones:** Yeah, but I've actually got it installed.

**Chris Gammell:** Oh, yeah. Okay. How'd the numbers work out?

**Dave Jones:** I have the whiteboard video right here and it chewed more than I expected. So I'm a bit disappointing. I've done it. I actually did a whiteboard.

**Chris Gammell:** Use more power than you thought?

**Dave Jones:** Yeah, yeah. It used more, yes, it used more energy, not power. It actually used the amount of power which I expected, which is around about one kilowatt, but energy. Yeah, I did the calculations that it would only take, look at the whiteboard here, 1.7 kilowatt hours per day. I'm getting two and a half to three kilowatt hours per day. So not quite double, but significantly more than I was expecting.

**Chris Gammell:** Yeah, so longer payback period than your, that's the net net from that.

**Dave Jones:** Yes, exactly. Well, no, no. Actually, the payback period is basically the same because we've got so much excess solar energy that it doesn't really matter. It's not a big deal. Like, yes, it's using more, which means we potentially have less to sell back to the grid at a pittance and we have less to store if we get a battery solution, when and if we get a battery solution. But no, it actually doesn't affect the payback period, surprisingly, because we have the excess solar. So it only comes on during the day. It doesn't matter that it takes double, really.

**Chris Gammell:** I am confused. It's because you're replacing the poor power rates being given to you when you're selling back into the grid. But that's basically the answer. Yeah, we're basically making money from everything that you're not selling.

**Dave Jones:** Seven cents per kilowatt hour and we're using that instead. Yeah, okay. But I sort of round that down to zero because it's almost a pittance.

**Chris Gammell:** Yeah, I see what you mean.

**Dave Jones:** Because the whole concept of doing this is to use the excess solar. Yeah, totally. Because we want to be kind of like self-sufficient kind of thing. We want to, as far as energy goes, and we want to switch off our gas entirely. Totally. Yeah, that's great.

**Chris Gammell:** So I mentioned I'm reading another book about the grid. And I kind of had this kind of in mind, but not really. We've talked about it on the show a little bit too. But I guess I didn't quite realize just the impact of the consistent versus the peaky power of wind and solar and stuff like that. And it's interesting reading this book too because the tone feels kind of like anti-renewables sort of. And it's more from the perspective of the grid operators and stuff like that. Oh, yeah. I guess I've never really seen it. I haven't seen it from that perspective before.

**Dave Jones:** The grid operators don't like renewables. Renewable energy stuff on the grid because they're intermittent. They don't like intermittent. Intermittent.

**Chris Gammell:** Yeah, they want consistent. They want consistency.

**Dave Jones:** They want that nuclear power or that coal plant to pump out.

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Consistent amount of power. So then they can, you know, because they've actually got, they've, you know, developed technology. They know how much power people take during the day on average and stuff like that. So they ramp, you know, they know how to ramp things up and down slowly. But then when all of a sudden, you know, all of your solar vanishes because, you know, you've got a bad day, which you didn't actually predict or something, you know. But they've got a tie. And now they have to tie bloody, you know, forecasts of weather into, you know, weather is not that predictable. You know, it's not that great. Now they have to factor that into their energy calculations, not just use, you know, on average, people are pretty predictable, right? People go about their daily lives pretty consistently. So they all, you know, come home from work and they switch on their appliances and they flush their toilet and they, you know. It isn't just a power grid. It's a water grid, right? Sure, sure, sure. As well. It's a sewage and everything, right? They know people are very, very predictable. Well, in fact, the sewage system, because this is one of, this is EEV blog, comes from the sewer industry. She's worked on this kind of stuff as a water, as a Sydney water scientist, you know. Anyway, yeah, sewage, right? They know when people are going to flush toilets because it's during the ad breaks, right? It's during the ad breaks, yeah. Ad breaks of major sporting events, right? No way. Yes, if the football grand final's on, they know that that capacity's coming during the halftime thing or during an ad break. Yeah, they know it's actually coming. Right, right. And they can actually.

**Chris Gammell:** Yeah, because the other thing people are doing when football games are on is drinking beer and eating food.

**Dave Jones:** And it's, yeah, they can actually predict all this stuff. And yeah, so humans are very, humans load-wise on the power grid are pretty predictable, you know, on a daily cycle basis and weekly.

**Chris Gammell:** The interesting thing was they were giving an example of like, so this is US focused because I don't, it's just a book that I was recommended. But they were giving an example in the Pacific Northwest where there was like a, there's like a wind turbine that's in a valley. So like when, when the wind's blowing really hard, but in May, when the ground is really soaked with water, like everything's just completely soaked with water. And so all the, all the hydro, which is in the area is also trying to do that, like trying to, they're trying to run that and balance the water at the top of the dam versus the bottom. Or, and like they said, like the trade-offs are like, they can't, they can't dump the grid power and they can't just shut off the water because it'll overflow and it'll destroy all the towns. And also at the same time, there's like, it was like salmon run. So they couldn't, because of like, because of the fishing, they also couldn't like mess with the fishing. And it's just like, holy crap. It sounds, it's, it sounds stressful.

**Dave Jones:** Environmental flows, they're called. Yes. They have to do these environmental flows. Crazy. They have to release X amount of water, you know, and they, they can't be more or less. And, you know.

**Chris Gammell:** One is just from the, I mean, it's basically the capacity that they can plan for a lot of it, right? Like they know that the water is going to be high. They know that the fish are running. But like, you can't know when the wind's blowing then. And then you think they're also in, you know, another, another downside is that they're in the Pacific Northwest. So, you know, they're kind of like tucked up in the corner. So it's not like you have the grid going off in all directions. You only have it going off in a couple of directions, you know, a limited number of directions. And so you don't have as many power outlets as well to like, so then you basically are limited by the capacity of the lines going to that location. It's just like, whoa, that's like, that'll just overload. It'll just, it'll just be a bad time. So yeah, apparently they called, called the wind operators and begged them to turn off the turbines. Basically that was, that was the solution. Spoilers. Sorry.

**Dave Jones:** Oh boy. Well, I'll tell you what, I've been changing my thinking on this recently. Yeah. I've, I've never been, cause we don't have any sort of nuclear power here in Australia. Right. And where, and we've got a lot of coal, right. There's a lot of coal and, but we've got huge amounts of solar. We've got quite a lot of wind as well. In fact, we've got the largest home solar uptake in the world. I think home solar uptake in the world, I think one of the largest, but I'm, you know, I've, we don't have nuclear power here, but I've always been the opinion. I was, you know, years ago, I was like, eh, we can probably all get it from renewables. You know, we've got tons of geothermal. We've got, you know, tidal, we've got everything. And I've, you know, I've gone into the numbers. I've read reports and everything that, yeah, we can do this. We can go like a hundred percent renewable energy. And now I'm thinking, nah, I think nuclear is our only way forward. Yeah. I mean. I'm now starting, like I've, I've, I've never been anti-nuclear, but it's, you know, because we don't have them and it takes 10 years to ramp up. We don't even have the expertise here in the country. And it's like, you know, it's always been, you know, some far flung future thing. And I, I didn't care if we went nuclear, but now I think it's, I, I'm not seeing a way out of it. Really. I, I think we probably need to bite the bullet and.

**Chris Gammell:** Yeah. I think. Go for nuclear energy. Well, when you think about like base load, right. That's really what it comes down to.

**Dave Jones:** That's where the rubber hits the road is the nuclear base load.

**Chris Gammell:** And we've got so much uranium. The other option. The other option is basically to figure out some kind of storage mechanism. And everything I've seen has been like a grid level storage. It's just like not there.

**Dave Jones:** Well, I thought, you know, thermal salt, you know, salt storage would be big, you know, thermal, you know, I was like a 10 years ago. I thought this, this would be the future, you know, but I'm, I'm just seeing them fail. And I'm just, you know, seeing too many problems with the solar and the wind.

**Chris Gammell:** I just, yeah. I feel like the scale of it is very different than like, if you're consuming something like, like uranium or like, I mean, like a coal or, you know, patrolling products generally, like, it's just the logistics of, of transporting like non-active or, you know, active, but not, but not reactive materials at the, at the time of transport is like, that's a lot easier than like building out the scale of like containing thermal, you know, like thermal salts and stuff like that. It's just, it just seems like it's just a really, really tough problem. So I don't, I don't, yeah. I don't see what it is personally. You know, like, I don't, I don't know when I think about like the battery bank kind of thing of storage.

**Dave Jones:** Like, yeah, no, the battery storage thing. And that's bullshit. No, it's, it's, it's good for sure.

**Chris Gammell:** Pumping water up a hill as a battery kind of concept as well. Like even that.

**Dave Jones:** Oh, dams are great. Dams are great. If you have the environmental.

**Chris Gammell:** You don't have it.

**Dave Jones:** You know, if you have the environmental thing to do it. Yeah. Right. You know, and, uh, pumped storage as well. Pump storage, you know, pump dam storage. Fantastic. Fantastic. But you've got to have the environment to do it.

**Chris Gammell:** Yes, exactly. Yeah. You know, and a lot of, at least in the U S there's a lot of flat areas and. Yeah. Same here. You know, you've got it. Yeah, exactly. And there's a lot of places without water that are also, you know, like, so yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** It's a tough.

**Dave Jones:** I don't know. I'm.

**Chris Gammell:** So I met at Supercon. I met, uh, well, one of my friends, uh, longtime friends, uh, was on, uh, was working on fusion. I think I mentioned that on the show before. And.

**Dave Jones:** Yep. And it's only 20 years away.

**Chris Gammell:** Only 20 years away. But another one was working at fission, but a portable fission company basically. So like a one megawatt generator with like fission built into like a shipping container. And so like.

**Dave Jones:** There's a lot of talk about those now.

**Chris Gammell:** Yeah. I think that's, I think that's really interesting. I think. Yeah.

**Dave Jones:** There's a future for that. If they can, you know. Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Totally.

**Chris Gammell:** The founder of that is a former coworker of mine of the company that this person was working for. And so I can see if I can get him on the show at some point. He's. Cool. He's a interesting character. I, I, I, I don't even know where you'd start. Honestly. Like if you like wanted to start a fission company today, like.

**Dave Jones:** Right.

**Chris Gammell:** Do you have to get permitted? I don't know. Like.

**Dave Jones:** I have no idea. You've got to have, you know, some background in the industry. Like it's not like we could just suddenly start it. I think, you know, you've got to have.

**Chris Gammell:** Maybe.

**Dave Jones:** Some sort of universe. You know, it's got to be like a spinoff from a university research or something. I don't know. Something like that. Perhaps. Maybe. Yeah. Not ruling. I'm sure you could. If you really wanted to. But. Yeah. I don't know. You have to have something novel. You know, you've got to have like a novel nuclear. Tech. And.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yep. Yeah. I think the scale down is probably the potential. Novelty. That sort of thing.

**Dave Jones:** Oh, they're very useful, especially for emergencies and stuff like that. Like you can just like, you know, fly in like a shipping container and it powers the whole town. Yeah. You know, during a, you know, flood or some other, you know, emergency kind of thing. Yeah. They're very cool. So there is a lot of talk about these modular nuclear reactors, as they call them. Modular, I believe is the industry term for them. And yeah. So anyway.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. So I thought about trying to run a video on the numbers of nuclear, of going, of Australia going nuclear, but, oh, it seems to be a lot of work. So. Yeah. Yeah. I don't know. We'll see.

**Chris Gammell:** Well, I mentioned I met these folks at Supercon. I came back from that couple. That was like last week. Did you happen to see the badge?

**Dave Jones:** I saw it. I didn't see it in action. I saw it in.

**Chris Gammell:** It's.

**Dave Jones:** Yes. Okay. There it is. It's all lit up. I saw the post. The pre-con version of it.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. Were they posting about it? Yeah. Yeah. It was really interesting seeing how people interacted with it. And I was really scared of it at first. So if you don't know, this is a basically a four bit computer that was, you could. So it was actually a pick 24 in the back, but it was basically emulating like a four bit computer that you controlled. And then all of the registered states were shown on the front in LEDs.

**Dave Jones:** I didn't know it used punch cards.

**Chris Gammell:** So that's actually the link I sent you was, that was actually one of the badge competition hacks.

**Dave Jones:** Ah, right. Somebody did a punch card add on.

**Chris Gammell:** That's right. Yeah. So basically they put a, yeah, they were. Yeah. Because I think, uh, they, oh, they had a separate microcontroller. They'd like a separate Cortex M zero that had like a one mega sample, a multiplexed ADC. And so they use that to like super over sample with like LEDs as the, as the detector as well. That sort of thing. So, uh, yeah. So Zach and Ben built that thing. It was really cool. And that's one of the, one of the winning ones.

**Dave Jones:** Definitely.

**Chris Gammell:** But yeah, no, the actual badge itself, like there's a whole, uh, I'm hoping they'll sell more of these in the future. Cause like, if it's just a one and done kind of thing, it'd be kind of a shame.

**Dave Jones:** Maybe I can assemble one with my new pick and play. That's a classic example of assembling something with a pick and place machine. It's got like noise.

**Chris Gammell:** So they, they actually, they did that on site, uh, at the design lab where the conference was. So they had been building them for a couple of weeks.

**Dave Jones:** Right.

**Chris Gammell:** Uh, and there are, I think. Yeah. They were using a DOD for.

**Dave Jones:** Oh, okay. Right. Yeah.

**Chris Gammell:** Yeah. So it's, uh, it's really cool though. And so you can go and look at the, the links are kind of hard to find, but I think it's just hackaday.io slash badge. I'll, I'll see if I can find the link here, but it was, uh, yeah, it was really cool. Like I I've never really done, honestly, I'd never done assembly before, you know? Oh, really? Okay. Yeah. Yeah. I mean, I didn't need to. So why would I? Right.

**Dave Jones:** Yeah.

**Chris Gammell:** Yep. So I don't know. So, uh, that was really cool. Oh, it's hackaday.com slash badge. If you go to that and then there's like, uh, there's a design guy or there's a programming guide and there's a bunch of, uh, repositories you can do. You can like follow along and do look at other people's programs. There's an emulator. There's a nice, there's just a ton of stuff there. I learned a little bit of assembly.

**Dave Jones:** Huge amount of work's gone into that. That's off.

**Chris Gammell:** Oh yeah. Yeah. I think cause they had, it helped that they had three years to do this. Oh, okay.

**Dave Jones:** Oh, right. They've been working on for three years. I was going to say it's, it's a significant effort.

**Chris Gammell:** Oh, it's very, yeah. It's very significant. And Voya who designed the badge has been working on it a long time. My, my current coworker worked on some of the emulator stuff. There's multiple people that were working on. Oh yeah.

**Dave Jones:** It says in the article it goes back to 2019. Holy crap. Yeah.

**Chris Gammell:** Yeah. Cause this was supposed to be the 2020 badge. Oh, okay. And then pushed. So it was done, I think in 2020.

**Dave Jones:** Right. Right.

**Chris Gammell:** Yeah. Cool. So definitely worth reading about. It's, it's really neat. It's really neat. And I mean, what was your, what was your exposure to assembly? I mean, you, you must've had to do it back in the day, right?

**Dave Jones:** Yeah. I've done a 8086 assembly. I've done Z80 assembly. I've done a pick assembly. I've done a TI, some TI MSP, not MSP 430s. Some TI DSP 320.

**Chris Gammell:** Oh yeah.

**Dave Jones:** Assembly. And yeah. Yep. Haven't done it for a long time.

**Chris Gammell:** Affinity for it. Or no.

**Dave Jones:** I've done a video.

**Chris Gammell:** Some people like feel affinity for it.

**Dave Jones:** No, no, I've got no affinity for it. Like, no, not, not, not, not really. No, like I, I, I do. I think I would still enjoy it. If I'm just doing something like some little tight loop that I need to, you know, do, I think I, I would still get joy out of writing, you know, cause you can do mixed assembly and see now. Right.

**Chris Gammell:** Sure. Sure. Yeah.

**Dave Jones:** So yeah, you can just write a little, you know, just write a little routine that, you know, you've like hand optimized kind of thing. So I could, I could still appreciate that. But writing an entire thing in assembly, it's like, nah, like, you know, yeah. Silly.

**Chris Gammell:** Yeah. So there's, I will also link in the badge hack contest, which was the end of the weekend. So basically people work on this thing all weekend and then, and then they participate in the badge hack contest. Keen eyes. We'll see a familiar face on there with a joke entry.

**Dave Jones:** Okay.

**Chris Gammell:** Yeah. It was a lot of fun though. It was good. Awesome. Good weekend. Good conference.

**Dave Jones:** Excellent. Oh, so it was over the whole weekend. Was it?

**Chris Gammell:** Yeah. Yeah. It's like a Friday to Monday, Friday to Sunday kind of thing.

**Dave Jones:** Okay.

**Chris Gammell:** Right. And yeah. Got it. It's a, it was just, you know, like amazing to be back with people again too. Right. I mean, like this was the first, I'd been back to a conference before, but not like a, you know, hacker conference of this, this crowd. And yeah. Awesome. Yep. These are our people, Dave. These are our people. Yeah.

**Dave Jones:** I can dig it.

**Chris Gammell:** Yeah.

**Dave Jones:** All right. What else do we have on our list this week?

**Chris Gammell:** Let's try and have a Supercon Australia.

**Dave Jones:** Supercon Australia. Okay. I'll start it up. Yeah. I'll do it. Yeah. Yeah. Yeah. Sure. And 10 people will show up. Yeah.

**Chris Gammell:** You'll get some people. It's just, you know, not fun to run something like that.

**Dave Jones:** Yeah. No, I know. Like, like it's okay doing a meetup or something like that, but if you have to organize actual a conference with events and, you know, speakers and chairs and things, you know. Oh yeah. The chairs are the hard part. Yeah. Oh boy. No. Maybe I should get off my art. You know, like who else is going to do it, right? Who else in this country is going to do it?

**Chris Gammell:** I'm not going to do it.

**Dave Jones:** Oh boy. No, I would have to tee up a lot of people, you know, it'd have to be like a lot of people sort of like willing to go in on something like that to make it happen, you know?

**Chris Gammell:** Totally. Yep. Cool. All right. What else on the list? You had started on that. I don't know what else is on that list. We've, we've had a, uh, unmanaged one of our, our patron saint of, uh, adding stuff to the list has been great about adding stuff, but I haven't been great about reading stuff like usual.

**Dave Jones:** What has Ben Eder done on the RS two 32?

**Chris Gammell:** Basically reviewed the entire, like, uh, how it works. So that's pretty cool.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** I have had your speakers turned on for this entire time.

**Chris Gammell:** Like I've been coming out of the speakers.

**Dave Jones:** Yep. You've been coming out of the speakers. I've been listening through my earbuds, but apparently it's been coming out of the speakers as well. Cause I forgot to turn them off because my stupid monitor, the bloody focus, right? Bullshit. USB interface thing does not mute the speakers. When you plug in the damn earbuds. Like, like my road one.

**Chris Gammell:** It sounds like there's an electronics project right there.

**Dave Jones:** I've already gone through this. I have an entire EV blog forum thread about it somewhere. And yes, one of these days I'm going to get pissed off enough and I'm going to design my own USB audio microphone speakery interface.

**Chris Gammell:** Yeah. Yeah. The problem is that when you make your own board for that sort of thing, nobody to blame but yourself.

**Dave Jones:** But, uh, yeah, no, I, in fact, we've talked about this on the amp hour before how this product doesn't exist. The exact product I want does not exist.

**Chris Gammell:** Yeah. And it'd probably be pretty simple as well. Right. It's like mostly just like a physical.

**Dave Jones:** It's mostly off the shelf. Like I wouldn't have to write any firmware for it. It'd all be off the shelf. Yeah. Yeah. You know, like you buy a Cirrus logic USB audio interface and the drivers are all there and it just does its thing, you know? So it's, you know, it's yeah. Yeah. So I probably wouldn't even have to write any firmware for it. I don't think.

**Chris Gammell:** Yeah. You know?

**Dave Jones:** Yeah. So yeah. Could all be like analoggy goodness. You know, it's got like a phantom voltage generator. It's got a microphone amp. It's got a, you know, a knob for volume control. It's got a jack, which you detect. And then you switch off the bloody... Audio outputs, which isn't much. And then have a compander, you know, a compressor expander thing for, you know, all that sort of jazz. And I have like a bar graph, you know, like a VU meter and stuff like that, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** Jeez. If only I could design electronics projects.

**Chris Gammell:** If only I had to... That is not the limiting factor, you know.

**Dave Jones:** No, it's time.

**Chris Gammell:** Yeah.

**Dave Jones:** It's totally not that I like the skills to do it. It's yeah. Yeah. Oh boy.

**Chris Gammell:** So here's an interesting thing that was posted on the subreddit. The WCH... So WCH has been putting... It's a Chinese silicon vendor. It's been putting out cheap and wild and wonderful parts. You know, there was one where like, there was like a crap ton of UARTS. I remember seeing something like that. It had like 10 UARTS or something like that. I was like, why do you have that? It's like super... Super specialized. Okay. Yeah. But now... So this is a Hexer article from a sub 10 cent RISC-V microcontroller. Show me. And it actually has... It actually has more pins. It has more pins. Hold it. Hold, please. It has more pins than the... What was that one that you talked about? The three cent microcontroller?

**Dave Jones:** Yes. The Paduk.

**Chris Gammell:** Paduk. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** So this looks a lot more like... This kind of looks like it's kind of trying to clone like a STM32 F030 sort of. Right. That's kind of the style of part that it looks like to me.

**Dave Jones:** Hmm.

**Chris Gammell:** But...

**Dave Jones:** I... Is... I'm going to have to do a video on this. Holy shit. Because my three cent microcontroller video, that was hugely popular. People love that. And I did like a series of it. I did like five videos or something on that.

**Chris Gammell:** And that was pin limited, right? That was like...

**Dave Jones:** Well, you can get ones from five pin SOT23, six pin SOT23 up to, you know, a SOT28 or something.

**Chris Gammell:** Oh, it did go up to that high. Yeah. Okay. I thought it was all sub 10 pin.

**Dave Jones:** Oh, no. No, no. You could get versions that went higher. Yeah. Yeah. And... So, I mean, this is... The million dollar question is, what is the development environment like?

**Chris Gammell:** Yeah. I mean, it's... Well, you know, so the... There's a GCC... It's not GCC. It's not GCC. Is it GCC? Yeah, it is. Yeah. Because there's like the ARM non-EABI. Right. Yeah.

**Dave Jones:** But does it have its own GUI? Does it like... What does it tie into? No, no, no, no. You're going to have to... Yeah. You have to roll your own, right? And sort of...

**Chris Gammell:** Yeah. But it's the sort of thing where like if you were in a... Say you were comfortable in a... Like a... What's it called? Environment. Like an Eclipse environment. Yeah, right. And you had that set up. Yeah. It's not going to be like vendor provided. Yeah. But if you had an Eclipse set up, you basically would like go into the Eclipse configuration and you would point it at a different GCC... Yes. Like version. Right. And it would be similar. It's not going to be perfect. No. But like it would be very similar. And it's like... Yes. I was very surprised that the first time I saw that happen, I'm like, oh, wow. It's just like you just changed the compiler and it's... Yeah, yeah. And you target a different device.

**Dave Jones:** Yeah. Yeah. It's just all the other stuff which goes into, you know, setting up all the IOs and doing all the other stuff that you know... Exactly. Yeah.

**Chris Gammell:** Configuration and all of the nice stuff that happens in like configurators and like people are used to like... Yes, that's right. ...STM32 Cube and stuff like that. It's like, no, you ain't getting that. Yeah, yeah. You're going to be twiddling some registers.

**Dave Jones:** Twiddling some registers in your header file to get your... Yeah. Yeah.

**Chris Gammell:** Yeah. Yeah. And I mean, it's, you know, so 16K flash, 2K SRAM, like not a ton of stuff, but still like...

**Dave Jones:** I think I'm going to order one of these and I'm going to do a thing. Do they have like a programmer? How do you program the... Can you buy like... See, because the thing with the Paduk one is that you can buy an actual programmer for it, right? So you can put the chip into the ZIF socket and you can program the chip or you can order them pre-programmed from the manufacturer.

**Chris Gammell:** I mean, if I had to guess, I would guess it has like an SWD, SW clock, you know, like a single wire debug kind of thing. That's how most of these things go. And then if you have a J-Link, it's just like, oh, I know what this is, you know?

**Dave Jones:** Yeah. Yeah. So you solder it to your board unprogrammed and then you have to have the header on there to program the thing.

**Chris Gammell:** That's a good question though.

**Dave Jones:** Which is kind of annoying for some products, you know, you just don't want to do that. You just want to order it, you know? Yeah. See, the reason you use the microchip, you know, PIC10 series or you use the 3Cent PUDUK one or something like that is because you can order it direct from the manufacturer. You just give them your hex file and in comes the reel of pre-programmed chips, right? They've got some magic automated production reel programmer or something. And, you know, and it doesn't cost you much more. You can order them from DigiKey program.

**Chris Gammell:** Yeah. Right?

**Dave Jones:** It's like, you know, that's like the, you know, that is a benefit. You don't have to dick around putting a header connector on your board and then programming each one and designing your test jig to, you know, program your, no, pain in the ass. Order them pre-programmed on the reel. That's what you want.

**Chris Gammell:** So it looks like there is a programmer, but the programmer honestly looks like it's just a USB to serial. Right. So I'm guessing there's a serial bootloader on there with like maybe a special pin that pulls down and then you.

**Dave Jones:** Well, I've gone to the website and it's all, oh no, it just automatically translated to English for me.

**Chris Gammell:** Yeah.

**Dave Jones:** Right.

**Chris Gammell:** Here's a, here's a link to the Tindy seller. So the Tindy seller has like a programmer.

**Dave Jones:** Oh, okay.

**Chris Gammell:** That's what they do in the hackster post. Yeah. It's interesting. I mean, like it's interesting that there, I like now that we've reached, I feel like three cents is kind of the bottom, you know. Oh yeah.

**Dave Jones:** That's yeah. Yeah. It's pretty much the bottom.

**Chris Gammell:** It's, it's, but, but now, you know, that we've reached the bottom and now that risk five is like even less IP in there, you know, like there's not, now there's actually like a pretty well-developed. There's a ISA that's open source and you know, there's processors that are targeting that ISA that are low cost or very, you know, no, no royalty, like going to arm sort of thing. It's just like, now this stuff is like down in the dirt as well. Like 32 bit processors, this cheaper is just, yeah, it's crazy.

**Dave Jones:** Yeah. That's, that's pretty nuts. What does it work at 48 meg? Yeah. Is it, is it single? I can't remember. Is the risk five, is it single cycle instruction? So do you get 48 MIPS from 48 megahertz?

**Chris Gammell:** I don't, I don't know if that would matter with, I don't know if the standard would say anything about that, right? That would probably be more specific to the, to the, not because remember that risk five defines the instruction set, not the instruction set, not how they implement it.

**Dave Jones:** Yeah. Right. Okay. Yeah.

**Chris Gammell:** So it would come down to how they, how they architected it.

**Dave Jones:** Yeah. Interesting.

**Chris Gammell:** I'm guessing somewhere in the data sheet says that. Yeah. Anyway. So anyways, this WCH as well is like, it's just, I just keep seeing more and more interesting parts pop out. They had a Bluetooth, they had a BLE part that was also really interesting and risk five based. And, you know, I just feel like there's, you know, this is kind of the, I feel like, you know, especially with all the restrictions that the U S is putting on, uh, China chip making and stuff like that. And like IP transfers and whatever. I just feel like risk five, risk five is happening everywhere. Right. Like I think I mentioned, I thought it would. Yeah. Yeah. But so it's going, it's going to all the major chip companies. I think they're going to be, they're going to adopt it. No doubt. I think, you know, just arm has a lot of sway still, and they have a lot of stuff in flight already that. Why would you cancel that if you've already paid for it sort of thing? Yeah. And you've paying for, and there's, and there's just a lot of expertise there. So like, I just think that's going to go on for, for a good long time. However, I think in stuff coming out of China, I think we're going to see tons and tons of risk five stuff. And it's just going to be really interesting. So I think that people that are understand, understand how the tool chains work and how to like, you know, how to access stuff like this, like super low costs, pretty interesting looking parts. You're just going to see more and more capable stuff coming out of China. I feel like, and that, so I think if you're good at the firmware stuff and comfortable in the risk five ecosystem, you know, that, and like understand some of the stuff under the hood, I think you're going to be really well prepared for all of the cool hardware coming out of China in that way.

**Dave Jones:** Yep. Totally. This looks really good. I'm going to get, I'm going to auto one of these straight after this, and I'm going to get some chips.

**Chris Gammell:** First, first chip that can go onto your pick and place, Dave. Right.

**Dave Jones:** I can have this flash in like a thousand leads or something, you know?

**Chris Gammell:** Yeah. Yeah. Maybe. All right. The CH32V003.

**Dave Jones:** Chip of the week. Chip of the week.

**Chris Gammell:** Chip of the week. Yeah. The thing we haven't tried yet. Maybe we'll wait until you get it in hand and then, then, then it'll be chip of the week.

**Dave Jones:** Yeah. Right. Well, one of the things I like about it off the bat is that it works at both 3.3 and five volts.

**Chris Gammell:** And five. Yeah. That is interesting.

**Dave Jones:** There's a lot of stuff which doesn't work on five volts anymore. And that's like, you know, it's like a pain in the ass for some things. So it's got a 10 bit ADC. It's got no DAC.

**Chris Gammell:** I wouldn't expect. I feel like you don't see a DAC until you're up in the, you know, 50 cent plus range. It's got a DM8 controller. And even then, it's 80. It's got some hot band comparators.

**Dave Jones:** That's handy. How many PWMs? Does it have any PWMs? Doesn't have any PWMs. Really? Unless that's part of the timer. That might be part of the, uh.

**Chris Gammell:** Yeah. I think that sounds right. Yeah. There's only two timers though, right? Yeah.

**Dave Jones:** There's only one 16 bit advanced timer, one 16 bit general purpose timer. So there's two 16 bits jobbies. And there's two watchdog timers, one 32 bit system time-based timer. Yeah. But there's no PWM. So that's a bit disappointing. Unless you can get one of the 16 bit advanced timers I'm sure could possibly be. Yeah, I bet you could. Yeah. Yeah. Yeah. There you go. You might, I might have a new low cost thing because I can just picture the clickbait now, you know, five cent risk micro.

**Chris Gammell:** Five for five. The five for five. Yeah.

**Dave Jones:** Right. Oh boy. Yep. Uh, where's the, where's the site that actually sells the bear chips though?

**Chris Gammell:** The bear chips?

**Dave Jones:** You, I don't know. Can you like buy a reel of these things? Like. Oh, I'm sure you can. Sample. You can just get sample requests.

**Chris Gammell:** Probably somewhere, somewhere on wch.cn. Right. Okay. And I think you could probably go into like AliExpress and find stuff like this too.

**Dave Jones:** Right. Yeah. I'm sure. All right. Interesting. I shall do it. Well, our amp hour is up.

**Chris Gammell:** It is. It is. I'm going to go, uh, watch Twitter burn down. We'll see. We'll see if, if, and when that happens.

**Dave Jones:** All right. I have, I, I bet Chris before the show that it's not going to burn down. That doesn't mean it can't go down for a day.

**Chris Gammell:** How many, how many parts of these do you think? How many of these things do you think would be in a reel? Do you think there'd be a thousand parts in a reel for 10 cent parts? I could bet you a reel, a reel of CH32V003s.

**Dave Jones:** Well, it depends if you get in the SOP 8 or you get in the SOP 16.

**Chris Gammell:** That's good. You know, maybe how about that though? I'll, I'll bet you a thousand, a thousand of these parts.

**Dave Jones:** You'll bet me a reel. You'll bet me a reel of risk five processes.

**Chris Gammell:** Uh, no, we have to be very specific. That could get very expensive. I will bet you a hundred dollars. How about we just say it like that? A hundred bucks. A hundred bucks. Go towards whichever risk five processors you would like.

**Dave Jones:** A hundred bucks. How long does Twitter have to go down for before you win? How many days continuous that no one can use it? Oh man.

**Chris Gammell:** That's a good question.

**Dave Jones:** Cause I am, I am, I'm totally with it that it could go. I've seen Twitter go down before, right? It's not the first time, right? So I, I, I figure a day is not enough.

**Chris Gammell:** No.

**Dave Jones:** I figure a day is not enough.

**Chris Gammell:** I, I, I'm saying the whole shebang.

**Dave Jones:** So you're saying the whole shebang.

**Chris Gammell:** I'm saying the whole shebang. Okay.

**Dave Jones:** Done.

**Chris Gammell:** That Twitter, Twitter is sold for parts.

**Dave Jones:** Twitter is sold for parts.

**Chris Gammell:** Yeah.

**Dave Jones:** You think Musk will sell it. So, so if either of these things happen, you win. If Twitter like just vanishes and nobody can use it anymore, it's gone. Or Musk sells it.

**Chris Gammell:** I feel like there's something else where it's like, it's still there, but it's in zombie mode. So like everybody, I don't know how to like quantify that.

**Dave Jones:** Yeah. I, I know what you mean. Yeah. Like it's kind of like, it kind of just.

**Chris Gammell:** Like nobody goes there anymore. Cause it's just like a bunch of spam, you know, it's just like.

**Dave Jones:** That is not going to happen. Crypto spam sort of thing. I'm saying that's not going to happen.

**Chris Gammell:** You don't think that's going to happen?

**Dave Jones:** I think like, no, Twitter would literally have to stop working before people stop using it.

**Chris Gammell:** I think that, I think that's a possibility, Dave.

**Dave Jones:** Okay.

**Chris Gammell:** All right. I will put a line in the sand that within two months. Two months. Within two months, there will be a major exodus of Twitter or some other. Twitter users, you mean? Twitter users as a result. Yeah.

**Dave Jones:** As in everyone we follow, like a good majority of people we follow just are gone.

**Chris Gammell:** Just Gonski.

**Dave Jones:** Gonski. All right.

**Chris Gammell:** Because of that's, yeah. And I think that's, that's enough right there. So we should put a number on it. So it's measurable. It's hard. That's tough. Yeah. I know. It's tough.

**Dave Jones:** I know. It's hard. I'm sure we'll know it if we see it. Right. Yeah.

**Chris Gammell:** That's the kind of thing. Yeah.

**Dave Jones:** Can we have kind of like a handshake agreement that it's kind of like, we'll know it when we see it.

**Chris Gammell:** I think we'll know it when we see it. Okay. So let's just say the two month mark. Okay. So we're going to reevaluate in two months. Twitter's going to come a gutter.

**Dave Jones:** If it's come a gutter or not.

**Chris Gammell:** So middle of January, middle of January, Twitter's come a gutter. Yes or no. We could do a vote somewhere.

**Dave Jones:** I am voting no. Because there's nowhere else for people to go. We will not. There's nowhere else to, and no, Mastodon's not an option.

**Chris Gammell:** I don't know where I'm going to go, Dave. I'll tell you that much. I'm not. Oh, no. I'm not doing this joyously. This is all gallows humor.

**Dave Jones:** If it did go down, I don't know where I'd go either. Because I'm totally addicted to Twitter.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** That's why I'm saying people aren't going to leave. You might be right, man. The wheels would so have to be falling off the billy cart before people would leave. Because there's no other option. There's nowhere else to go. Where are you going to go? Facebook?

**Chris Gammell:** No. God, no.

**Dave Jones:** Right? Exactly. What am I?

**Chris Gammell:** 70?

**Dave Jones:** That's right. Right? There is no other option. That's why people are so addicted to this thing. It is the social media.

**Chris Gammell:** Of people that are addicted to it. You know? Like, I talked to my wife about it. She's just like, why don't you just stop using it? I was like, uh, no.

**Dave Jones:** Literally half of the media is stories about what's happening on Twitter every day.

**Chris Gammell:** Yeah. And most people are like, so what? I'm not on Twitter. But it's probably, most people listening to this are like, all right, David, Chris are just off on this thing. They're not going to shut up about it. So, sorry. All right. We're addicted. What can we say? We're junkies. Two months.

**Dave Jones:** Twitter comes a gutzer.

**Chris Gammell:** Yes.

**Dave Jones:** All right.

**Chris Gammell:** Or if it, if it does not come a gutzer, then I owe you a hundred dollars with risk five parts.

**Dave Jones:** All right. Done.

**Chris Gammell:** All right. See you then.

**Dave Jones:** Catch you next time. Bye.
