---
episode: 156
title: Tesla, FPGAs and DigiKey - Zesty Zippy Zynq
url: https://theamphour.com/the-amp-hour-156-zesty-zippy-zynq/
---

**Chris Gammell:** This episode of the Amp Hour is brought to you by NetBurner. Have you ever bought an embedded development kit that took a day or weeks to get to Hello World? Are there endless libraries requiring build after build? And do you find yourself banging on your desk, waiting for your application to compile and download, when all you want to do is test your code and get it out the door? NetBurner provides the easiest way to develop and deploy network-connected embedded devices. With a complete solution of hardware, software, and development tools, your prototype will be up and running in no time. For more info and a special listener offer, go to netburner.com slash theamphour. This is the Amp Hour Podcast, recorded July 29th, 2013. Episode 156, Zesty, Zippy, Zing.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life and Contextual Electronics.

**Dave Jones:** And contextual, burning the candle at both ends there.

**Chris Gammell:** Yeah, you know, I feel like I'm jinxing it again, you know what I mean? Like every time I start adding that to my intro, I go and stop doing something. So I should probably not say that. I'm sure listeners are like, yeah, sure, Chris, whatever.

**Dave Jones:** And you've got a free beta program. Free. Sorry, I can't do a good radio voice. Free. No, sorry. I don't have a radio voice. Why the hell I'm doing a radio show? I have no idea.

**Chris Gammell:** Yeah, yeah, the beta program is going to be free for people. And I don't know, it should be good. I mean, it's like, it'll be not as long as the regular program, but it'll be basically people telling me what I'm doing wrong early on. Right. And that's the trade for the free, because there will be some stuff that I'll probably say wrong. Hopefully it won't be wrong, but...

**Dave Jones:** Will you get those sponges who take the free program but don't give any feedback?

**Chris Gammell:** Oh, I'm trying to find people that aren't going to be like that, but I'm sure there will be a couple. How many people? You always have to play those numbers games, you know?

**Dave Jones:** Yeah, yeah. How many people are you going to get? Oh, 20 people. 20 people total. On the beta program. All right. Beta if you're in Australia, beta if you're in the US. Beta.

**Chris Gammell:** What? Beta. Beta? Beta? Beta? Beta? Beta is what you buy if you're buying a crappy car in Boston.

**Speaker ?:** Right.

**Chris Gammell:** What kind of car did you buy? I bought a beta.

**Dave Jones:** I haven't heard that with the term before. There you go.

**Chris Gammell:** What, like beater? You never heard of beater before? No. All right, fine. Speaking of Boston, we are... Yeah, right. We are sponsoring the Open Hardware Summit. We are. Which is in Boston. That's exciting.

**Dave Jones:** And you're going. You've got your plan together.

**Chris Gammell:** Yeah, I found out today that I will be going, and we'll probably have an Amp Hour meetup, and we'll all toast Dave from afar once again.

**Dave Jones:** I'll send you my cardboard cutout, and you can carry it around. That'd be great.

**Chris Gammell:** That would be... Well, you were just talking about possibly going to a conference via Skype at one point.

**Dave Jones:** No, yeah. Yeah, that's right.

**Chris Gammell:** I could carry you around, man.

**Dave Jones:** You could carry me around.

**Chris Gammell:** That would be creepy.

**Dave Jones:** Or I could embed a tablet in... I could replace the head of my cardboard cutout... Of the cardboard cutout, yeah. ...with a tablet, and then I could Skype the whole event. Oh, God, that'd be really creepy. Yeah. We could get one of those cheap, you know, $30 tablets or something.

**Chris Gammell:** Yeah, there you go.

**Dave Jones:** Graft it on. Yeah.

**Chris Gammell:** It's a low-budget telepresence. Yeah, exactly. It'd be like a tablet version of Weekend at Bernie's, you know? Right.

**Dave Jones:** Be tracking me around everywhere.

**Chris Gammell:** Yep. Great. Yeah, I'm looking forward to the summit. I mean, they start announcing some of the speakers and everything, and a lot of familiar names, but, you know, you go for the people. It's always about the people.

**Dave Jones:** Yeah, of course.

**Chris Gammell:** And that's what I'm pumped about.

**Dave Jones:** And I'm sponsoring it, too.

**Chris Gammell:** Oh, yeah, that's right. EEV blog.

**Dave Jones:** The EEV blog is also sponsoring it. Yep. Yes. So there'll be something in the bag.

**Chris Gammell:** That's right. The goodie bag.

**Dave Jones:** Goodie bag from both the EEV blog and The Amp Hour.

**Chris Gammell:** Yes. We've been brainstorming about that, and hopefully we don't do anything that everybody else is doing.

**Dave Jones:** Oh, it's highly original. You can probably guess what mine is, but, you know. Yeah, right. No hints. No hints. Oh, dear. Anyway, but we're trying to put something useful in there. I talked Chris into it. See, Chris.

**Chris Gammell:** Yeah, I was all about stickers.

**Dave Jones:** You wanted, like, a sticker. You wanted a sticker. I went, that's lame. They're stickers of shit. Stickers of shit.

**Chris Gammell:** They're a little lame, but you know what? They're also, you can, they're easy. You know what I mean? Not just for us, but also just for.

**Dave Jones:** Yeah, but they're easy and useless. People just toss them out. No. People like that stuff for laptops and everything. No, they don't. 95% of people are going to toss a sticker.

**Chris Gammell:** Maybe. I don't know. I put a Mighty Home sticker on my laptop that Jeff gave me. I've got Dangerous Prototypes one. I mean, I've got a small collection going. I'm sure people would like the Amp Hour sticker. There will be stickers in the future. It's just a matter of Dave didn't want to put them in this goodie bag, so.

**Dave Jones:** Let's take a Snap Amp Hour poll, shall we? Can we put a poll on our website? Do people want, do people use stickers that they get in these bags?

**Chris Gammell:** That is a Snap poll for sure.

**Dave Jones:** What do you want something useful? Oh, I can stick it on the forum. I can do polls on the forum easily.

**Chris Gammell:** There you go. Yeah.

**Dave Jones:** And I'll show you. All right. I'll show you that people don't want stickers. Stickers of life. Next thing you know, it'll be like a patch, you know? Like you sew on the arm, you know? It'll be like, what the hell do you do with that? It's great if you're a scout.

**Chris Gammell:** I mean, like some people like those. I think they're cool, but yeah, I agree. I don't really have anything I sew on to, but yeah, I like them. I saw Jaren, one of the guys that hung out with me in New York when I was getting glass. He actually took that patch and he gussied it up with some LEDs and stuff for one of those bring a hack dinners out in Maker Faire. All right. Cool. So that's one thing. You know, you can integrate them on other stuff. You could put stickers on your project. I'm just saying, swag bags are hit or miss on their own.

**Dave Jones:** But everyone else is going to put a bloody sticker in there.

**Chris Gammell:** Yeah, because it's easy. Exactly. Exactly.

**Dave Jones:** Chris is a lazy ass. That's what we're getting at here.

**Chris Gammell:** How about busy? Let's go with busy.

**Dave Jones:** And that's saying a lot because I set the benchmark for lazy ass. That's right. I knew well. Chris is worse.

**Chris Gammell:** Oh, boy. Yes, and we can see how lazy you are because you were riding around Sydney on some kind of little electric scooter to old school. I don't even know what this is. I saw a picture of it, but I had no idea what I was looking at. Wash your mouth out, son. This is a Sinclair C5. It looked like a... Is it like a go-kart? I mean, it's not a real car. Is it like a golf cart? What is this thing?

**Dave Jones:** It's basically a trike. It's a bike. It's a bike. It's actually got pedals. You actually pedal it, but it's got a motor assist. Binary motor assist on, off. There's no throttle on this thing. It's like you turn the motor on and it helps you go, basically.

**Chris Gammell:** So there's a lazy option?

**Dave Jones:** Well, there is a lazy option, but yeah, it's very underpowered. Well, it's got a 250-watt motor in it, or it's supposed to, but really, if there's any heel whatsoever, if there's any gradient at all... You're pedaling? Yeah, you're pedaling. Well, you pedal and use the motor at the same time, so it's not that hard, so you're not expending much energy. But yeah, it won't get you from a dead start to going on any sort of gradient with just the motor. If you just hit the motor button, it'll just sit there. But this is a simple... It'll just rev and... Yeah, it'll just...

**Chris Gammell:** Any kind of little scooter thing like that. Do you guys have power wheels over there? Do you have that? Like the little toy that kids can ride on? Power wheels, no? Power wheels. It's like part of my childhood. I was like supremely jealous of my friend down the street who had a little Jeep that... You know, it's just a little car battery and an electric motor, basically.

**Dave Jones:** Oh, God, no. We had nothing like that.

**Chris Gammell:** Terrible recharge cycles, so like you'd buy it and you'd get like 30 minutes of battery and then eventually it gets down to like five minutes of battery. Yeah, yeah, yeah.

**Dave Jones:** And then it's useless, yeah. Yeah. Yep.

**Chris Gammell:** So, yeah, that's what I always think of. Even with electric cars, I mean, I know that they're not anything like that, but it's just there's always that stigma in my mind of kind of as you're flooring the gas with a little plastic pedal, right? And you just kind of slow to a stop.

**Dave Jones:** But anyway, I'm going to rub your nose in it because this thing was designed by Lotus. Thank you very much.

**Chris Gammell:** Yeah, Lotus. All right. I mean, they're impressive vehicles, but they're ugly to me. I don't know. That doesn't really matter in the scheme of the electronics.

**Dave Jones:** I think this thing looks cute. I think this thing looks awesome. The Sinclair C5. It's great.

**Chris Gammell:** Okay, so the real test is, would you actually drive one of these around every day of your life?

**Dave Jones:** Oh, I could see myself doing it if I wasn't on really my... Like, I wouldn't drive one through the CBD of Sydney. You know, you would just get creamed. I mean, this thing has the nickname the Hedgehog for a reason. It's because people keep getting run over in it. You know, so... Yes. Oh, my God. No, well, it was so dangerous that they had to fit flagpoles to them, right? So that everyone on the road could see them, right? Because otherwise...

**Chris Gammell:** I have to send you this picture. Hold on. Hold on. Before we go any further, I have to send you a picture. All right. Oh, my God. I know people can't see it. I'll post it in the show notes. But there's a picture of a guy with a poncho that goes over the outside of the entire scooter. Oh, my God. So you ride one of these, huh? This is really cool, Dave.

**Dave Jones:** I was riding one of these puppies. Yep. Sinclair Seaford.

**Chris Gammell:** Oh, my God. Dude, they are great. They are great. This is the nerdiest little thing I've... Oh, it gets even better. Oh, yeah. Pictures from Europe. Sorry, people from Europe. I don't know. Some of these pictures are just like, yep, that's about what I... Oh, God. So many good pictures. So this came out in 85. I was two at the time.

**Dave Jones:** 1985, yep. And they folded in 1985. So, yeah. Before they did, they sold 12,000 of them. And this was the highest selling electric car in the world until 2010. Can you call this a car? Is that... Well, Clive Sinclair did, so that's good enough for everyone else.

**Chris Gammell:** All right.

**Dave Jones:** So it's a car.

**Chris Gammell:** Yeah. Sure.

**Dave Jones:** It's a personal transportation device, okay?

**Chris Gammell:** Okay. I'll go with that.

**Dave Jones:** Well, it's got a motor. It's got a little boot in the thing. You can drive it on the road. It's a car.

**Chris Gammell:** Kind of.

**Dave Jones:** Okay. You know, and it was built down a price. I mean, this sucker was only, I think, 399 pounds, right?

**Chris Gammell:** Oh, that's pretty impressive.

**Dave Jones:** Back in the day, which is like, even counting for inflation, it's probably less than like a thousand bucks, right?

**Chris Gammell:** Right.

**Dave Jones:** So this, you know...

**Chris Gammell:** So this is effectively like a sit-down segue. That's what it looks like to me.

**Dave Jones:** Yeah. Well, yeah, probably. Yeah.

**Chris Gammell:** Yeah. Okay.

**Dave Jones:** Yeah. It's a...

**Chris Gammell:** So why were you doing this? That's what I wanted to hear. Where did this opportunity come from?

**Dave Jones:** Well, somebody... Sorry, I can't... I forget who it is. Emailed me a link to an eBay auction, which had a Sinclair C5 on it. And these things are rare in this country, right? There's less than a handful. There's like a handful of these in the country, and we were riding two of them on the weekend. You know? It's like... It's not that many.

**Chris Gammell:** This is you and the wife? You guys... No, no.

**Dave Jones:** Me and Mal. My mate Mal. Fade. Yeah. So... Yeah. Anyway, he's got two of them. And the reason he got two of them is because somebody emailed me. One of my viewers emailed me this eBay auction. And I went, holy shit. It was 500 bucks. And holy shit, I really want this. It's so cool. But I knew I had nowhere to put it, right? And I actually did all the measurements. I went and measured the door to my lab. Yeah, try and get it through a door. And it wouldn't fit in the lab. I'd probably have to take it apart, take the wheels off and everything. And so it wouldn't fit through. So I thought, you know... And the wife wouldn't let me keep it at home, of course. But she actually gave the approval to... She thought, oh, this is so cute. I want a ride too.

**Speaker ?:** Oh my God.

**Dave Jones:** So I had approval to buy this thing. But in the end, I didn't. Because I knew it would just sit around and I wouldn't have time to devote to it. And everything. But with hindsight, I bloody well should have. Dude. Because it's an investment. I could have easily got my money back. I'm sure you could. They're so rare. I don't doubt that at all.

**Chris Gammell:** Yeah, I don't doubt that. But...

**Dave Jones:** Anyway, so I thought, well, if I'm not going to bid on it, I might as well tell my mate Mao, who's into electric cars. You know, he builds his own electric cars.

**Chris Gammell:** Yeah, right.

**Dave Jones:** And anyway, I think he bid on it, but it was outbid or something like that. Anyway, he didn't get it. But that piqued his interest in the Sinclair C5 and he found a guy who had actually imported two of them from the UK as part of his personal effects when he came over here. And this guy lives in an apartment now. And he said, look, if you can... I've got two of them. If you want to do them up, then you can actually... You can keep one. So he went, holy shit. Yeah, thank you very much. And so he's now got two Sinclair C5s, half of the number that are in this country. And yeah, so I just went to his place and we had a ride around and shot some video, of course, which will be going up today. Yeah, of course.

**Chris Gammell:** Yeah. Of course.

**Dave Jones:** Yeah. Well, that's good.

**Chris Gammell:** Yeah, I look forward to see what's inside this thing. I mean, because the... I mean, the interesting thing about electric vehicles to me is just... What? Nothing. Nothing? Nothing's interesting? I mean, I just... I think from the motors, the motors are interesting just because, you know, just because of the torque that you can get out of an electric motor. You know, obviously, this one didn't have a lot because it didn't have a big battery pack.

**Dave Jones:** Yeah, it's got a 250-watt motor. There's a motor, a gearbox, a relay that switches the motor off and on. And there is a complex little Gatorade chip in there that actually does the battery monitor and stuff like that. It does have a little heads-up display that tells you, you know, your battery and your motor torque and all that sort of stuff. But no, it's really bare bones, this thing. You know, it's no more advanced than any of the powered bikes you can buy these days. You know, like you can go on eBay for $300, you can buy a powered bike, you know, just a regular ride-on powered bicycle. And yeah, it's just a motor and a gearbox. That's it. Hooked onto an existing pedal drive chain. And that's it.

**Chris Gammell:** The batteries are still the impressive. Sealed, lead-acid, 12-volt. The thing that actually limits it is still the batteries, huh? Just because of the charge you need and everything.

**Dave Jones:** In this thing, it would be the battery and the motors. I mean, the motor's not hugely powerful and it only drives one wheel. And it's got a motor on one wheel and the brake on the other wheel. So if you keep your brake at the same time, it just veers to the right, you know?

**Chris Gammell:** Nice. You burn some serious rubber, huh? Yeah, that's it.

**Dave Jones:** And on the front, it's just got your regular brakes like you have on your bike. So, you know, one of those caliper brakes, are they? You know, those little pads, little bike caliper brake things. Yeah. But I like it, damn it.

**Chris Gammell:** Well, that's fine, man. I mean, you're allowed to do that. You're allowed to like it if you want to. See, I'm not sure. The reason I bring up the torque, though, is because we have other stuff on our list about transportation and stuff. And so there's an interesting teardown of an electric skateboard as well. And I think that's really interesting just because of the – I mean, you look at the compactness of it all. And that's where it really starts to get crazy because it's all contained underneath a skateboard. And it's – you know, it's –

**Dave Jones:** I almost got one of these. When I bought the lab, I thought, what options do I have for, you know, riding to the lab? You know, I've got my regular bicycle, right? And the other one was a skateboard. And then I got into looking at power skateboards. And then I was looking at, you know, electric bikes and stuff like that. And now I'm dreaming about driving my Sinclair C5 to the lab.

**Chris Gammell:** Yeah.

**Dave Jones:** But, yeah, these skateboards are great.

**Chris Gammell:** Yeah. Yeah. I mean, they actually were a Kickstarter project too, which is – I think I missed when these actually came out. But, you know, they actually did all custom electronics and everything. Yep. And it's – I'm just impressed that they can deliver that kind of power just from – I don't think they get a lot of battery life out of the thing.

**Dave Jones:** No, they're not huge.

**Chris Gammell:** Yeah.

**Dave Jones:** But, yeah, the reason I possibly wanted one of these skateboards is that, you know, it's so compact. Like, it's a board on – Yeah. It's like from – it's a board on wheels. Sorry, I had to quote back to the future there. Yeah. And, you know, so you can just – once you – you know, you can just hop on and off at any time. Yeah. And you can just pick it up and take it into the lab and it takes up, you know.

**Chris Gammell:** I mean, you just – it doesn't take up any room. It's fantastic. The thing that it has over the C5 is you don't look like a total dweeb. You put on your little poncho and you strap yourself in.

**Dave Jones:** You're like, hey, I'm going to work. Well, you'd have the same poncho problem with the skateboard if you're riding that, right? You would, but you know what? You'd look like even more of a dick because you're riding around with – you'd look like a penis on a skateboard.

**Chris Gammell:** No, you know what? You'd pick up the skateboard, you'd get on a bus and then you'd ride to work, right? Try doing that with a C5. No, you put on your little poncho. Exactly. You strap yourself in, you know, ambiguously gay duo style looking thing, you know? Yep. Yeah. Ace and Gary.

**Dave Jones:** That's what I'm tossing up at the moment. I'm tossing up between getting a folding electric bike, right? You know, one that you can fold up just because – yeah. Well, like most of the time, if I rode it to the lab, I'd just leave it down in the car park and just park in my parking spot, you know. Or one of these powered skateboards because they're just cool.

**Chris Gammell:** Yeah, it's cool. I mean, it's cool. I mean, it's very slick looking too. I mean, that's the other thing. So people should definitely check it out. It's all controlled by – I think it's controlled by Nunchuck like a Nintendo Wii style. And yeah, man, it's neat.

**Dave Jones:** Yeah. They weren't cheap though. They weren't cheap in this country. So, you know, you can pay like a thousand bucks for one of these, you know, powered skateboards. Some of them are really serious business. Yep. Yep. So anyway, I do – yeah, I'm going to – maybe I should do a poll. What sort of power transport should I get to go to the lab on? It's just cooler. How about your legs? You know?

**Chris Gammell:** How about your legs? You've thought about that? Walking, you know?

**Dave Jones:** Yeah. Yeah. I can do, but, you know. I just want to speed it up, you know? Well, it's the hills, you know? And that's the other thing, right? I live in the hills district here, right? So there are hills. So, you know. Yeah. I doubt that one of these powered skateboards would actually get me up the hill.

**Chris Gammell:** You know what you should do? You should just throw caution in the wind and just buy a Tesla and get it over with. Just buy one. Have it made in a robotic factory.

**Dave Jones:** I want one, dude. They are just so awesome.

**Speaker ?:** I know.

**Dave Jones:** I'm telling you, the future of cars is electric. Anyone who doesn't agree is wrong. I'm sorry. But, you know, you are wrong. You are going to lose.

**Chris Gammell:** I totally agree. And so this video is jaw-droppingly beautiful because it is a symphony of – it was wired, right? Yeah, wired.

**Dave Jones:** Hats off for the editing on the video. It's beautiful. Yeah.

**Chris Gammell:** Very, very nicely shot.

**Dave Jones:** And it only goes for five minutes, so.

**Chris Gammell:** Yeah. And the main actors, though, are the robots. And, you know, it's a nearly fully automated plan. I know there's a lot of people interaction still.

**Dave Jones:** There's 3,000 people who work there.

**Chris Gammell:** Right. But that's for cranking out a lot of cars, too. I mean, like – I mean, most car facilities are like that these days. I mean, it's not like this is just Tesla doing this. No, no. There is a significant amount of automation in the automotive industry. Oh, yeah. And it's amazing. Yep. Industrial robots are so cool. Yeah. I walk around –

**Dave Jones:** What I was impressed with, they do all the – like the entire body is aluminium, not aluminum, right? It's aluminium. Of course. And it looks like the entire body of the car is completely aluminium. They've got their own stamping and forming machines all in the factory. Yeah. So they show you these – Yeah. You know, go along – like they come in big rolls of the stuff and then they flatten it out. Yeah. Then they stamp it and mould it and press it. Yeah. Oh, and it just pops out and it's just magic. Yes. Oh. It really is.

**Chris Gammell:** It is a lot of fun to watch. Especially from a distance because it's not as noisy. You know, like manufacturing is still very dirty.

**Dave Jones:** If you go there, it'd be – Yeah. It'd be – Yeah.

**Chris Gammell:** And loud and – Yeah. It is a symphony, but it's still a violent symphony. You know, it's more like 1812 Overture than like, you know, Mozart. Yeah. Wait, who wrote 1812? That's – I don't remember. Sorry. Symphony fail. Oh, you. Did we talk about that new Ford prototyping thing last – or two weeks ago?

**Dave Jones:** Ford prototyping thing?

**Chris Gammell:** Yeah. So there was a thing – Since we were talking about the sheet metal here, there's this really cool thing from Ford where they took – you know, usually you have to – the sheet metal stamping like they show in this Tesla video. You know, the stamping is these huge, huge presses. You know, 50,000 – Yeah.

**Dave Jones:** Bam.

**Chris Gammell:** A pound press and stuff like that. But now there's this new tool from Ford where basically it's like on a gantry, like on a 3D printer. Instead of actually extruding plastic, what it does is it just – I think it heats either through a direct method of like applying like a heated tip or just from pressure. But basically it bends – it forms metal like just by – just one point at a time and then it moves this – the point around in a predetermined shape and it basically then deforms the metal, you know, step by step by step like a – Right. Oh, got it. Like a 3D printer basically. And it's amazing. I mean they're showing like –

**Dave Jones:** Would that give a smooth actual result? Yeah. I mean if you go over it enough, right?

**Chris Gammell:** It's just like machining, right? With machining you can do a rough pass, then you do like a –

**Dave Jones:** There's no way that can beat the speed of a huge stamped press though, surely.

**Chris Gammell:** No, no, no. This is for prototyping only.

**Dave Jones:** Oh, right, right. Okay.

**Chris Gammell:** It's because – but I mean it's just like doing PCBs, right? If you're trying to do a full-blown PCB with 12 layers, right, or just a – well, this is a bad example actually. But basically the idea is that the prototyping is so much faster just because you don't have to send it out. You don't have to – Yeah, yeah. You know, if there's a big mistake, you don't have to retool. It's just, you know, very custom type of thing.

**Dave Jones:** Mm-hmm.

**Chris Gammell:** So it's gorgeous watching this kind of stuff. You know what I like – The future's exciting.

**Dave Jones:** The most – the best thing I liked in that Tesla video was that robot that did three things, you know, three different things. Oh, yeah. It would install the seat, right? So it grabs the seat and then it twists and turns it so it puts it through the door and then it rotates it and puts it in place and anchors it down and everything. Yeah. And then the machine comes back out and changes its own tool head and then goes and installs the bloody windshield.

**Chris Gammell:** Yeah. You know? That's killer. It's really – it's amazing. It's fantastic. You know, these – It makes me wonder, like, you know, maybe robots are kind of the thing. We should start doing that.

**Dave Jones:** We should work on my motor drive skills, you know? But these things cost like a million bucks each, you know? These aren't cheap.

**Chris Gammell:** Well, yeah. Yeah, they're coming down, though. I mean, like – Are they? That's what we've talked about in the past with Baxter that – oh, it's a company out of Boston, Personal Robotics or something like that. I forget the name of the company. But it's that little red plastic-looking robot with a real, you know, kind-looking googly-eyed screen, basically. And it's the same kind of idea but, you know, very cost-reduced and made to be friendly. Basically, that's only $22,000. Rethink Robotics. That's the one.

**Dave Jones:** And that's chicken feed for a, you know, car manufacturing or an automated plant. That's like 22 grand. God, I can remember – you know, we would piss that away on one little, you know, tool in – Oh, yeah, pay that in the wire, man. Yeah, I know. Some of the factories I've worked in.

**Chris Gammell:** But it's not meant for that. That's meant for very low – I mean, these industrial robots are, you know, million-cycle, 10-million-cycle kind of machines. They're insane and awesome. I know.

**Dave Jones:** I can just watch that video. Actually, have you seen somebody linked in the comments there's a one-hour version of that video? It's not from Wired but it's one of those – it's that TV show, you know, that mega-building? That mega-building show? Yeah, I know what you mean. Yeah, there's a link to that. I'm not getting anything done tonight now. Well, neither am I. I'm going to have to watch it after this. Jeez. But, yeah, it goes for an hour. Yep, all about – Bromalist. Yep.

**Chris Gammell:** Damn.

**Dave Jones:** I know. So we'll have to link that one in as well and we can waste an hour of your day too, folks.

**Chris Gammell:** Yeah.

**Dave Jones:** Sorry. But it's an hour worth spent because it's just awesome.

**Chris Gammell:** Well, speaking of automation and things that will make your jaw drop, I have been alerted to a jaw-dropping tool.

**Dave Jones:** Warning, Will Robinson. Warning.

**Chris Gammell:** Yeah. Sorry. So this comes from Ben and he wrote this script. It's a – some people know what Greasemonkey is. It's like a script platform for Firefox and then there's a similar one for Chrome called Tampermonkey. And basically he wrote a script that refactors DigiKey. So, like, it takes – you know, you just do a DigiKey search, right? Many people use – a lot of people, listeners use DigiKey. And it takes it and they're arguably very crappy interface, you know, all text. Not super friendly. And it makes it awesome. Yeah.

**Dave Jones:** Now, warning folks, superlatives are coming. Yes, many superlatives. Because Chris just rattled off. Yeah, he just talked my head off. I'll find this before the show about, you know, how wonderful this thing is.

**Chris Gammell:** It's just, like, stuff that – it's one of those things where it's like, you know, first off, we've talked about it on the show before. And I'm not – we're not claiming any input on this. But, you know, just stuff that we've talked about before with, you know, trying to replicate catalog view type, you know, like leafing through a catalog and stuff like that. And just making it easier to use and everything. Like, everybody's used DigiKey before. And it's not super friendly. It's just the people are used to the convention of it.

**Dave Jones:** And it gets the job done. You just brute force it and it does the job, you know. Right. Yeah.

**Chris Gammell:** Yeah. So, you install the script and basically – so, then you search for something like LED, right? And then you get the billions and billions of results that they send back, right, with lots of different – you know, basically anything that mentions an LED. Even like, you know, like a RJ45 jack, right? That has LED mention in it. And you might actually want that for some reason. You might actually have been searching for that for whatever reason. But what you can do is then you can just mouse over – like I'm mousing over circular connectors housings, right? And it's just doing a preview of the first hundred images from that, from the search page. And it's just like, of course. And then as you dive down into the search results and stuff too, you can start – it gives you the previews again and you can actually get up to, I think, like, I don't know how many. But basically, you mouse over anything and it starts having preview windows and you can, like, knock out different columns of the search table for, you know, if you want to simplify your parametric search. And then as you dive down into an actual part, there's something called – well, first off, it does an auto loader of the data sheet too. So you don't actually have to download the data sheet. It will just preview it in the pane. And as you mouse over everything, it will like – so then there's the filter in reverse, which is probably my favorite thing here so far. And it actually allows you to like – so if you select something and you're like on a 0603 resistor and you like that it's a 2K resistor but you don't like any of the other specs there, you just click 2K and then it'll filter in reverse and it'll only show you all the 2Ks even outside of that search basically.

**Dave Jones:** That's one of the most annoying thing about DigiKey is you always have to go back multiple levels through your parametric search. You've got to hit the back button and you've got to remember how many times to go back. Yeah. And then you've got to go forward again. So you're always going back and forth, back and forth.

**Chris Gammell:** Right, right. And it's tough too, right? I mean, I think we've complained about DigiKey before but basically what we came to is that like they're a huge database with a, you know, daily operations. You're not just going to halt that stuff, right? You have to make incremental changes versus big changes for that kind of stuff. But in this case, it's just like overlaid over top of the database so who cares? And it's awesome. I mean, it's just stuff that you need, you know? Like it gives you – where was the other thing? There was something about like – oh, this is it. If you actually go to a search and then you mouse – oh, sorry. If it gives you like the parametric search list basically and then you mouse over stuff, it'll give you like pricing. Where is it? Yeah, so if you mouse over single quantity pricing, it'll just preview – it'll preview up to 1,000 price break type of stuff. Like stuff you're just doing anyways.

**Dave Jones:** Yep, yep, yep.

**Chris Gammell:** And then there's a cart too.

**Dave Jones:** Calm down, calm down, calm down. I know. I know.

**Chris Gammell:** I'm sorry. I'm sure that like people that are fans of Element 14 or Newark or, you know, Mauser or whatever, it's like, you know, a lot of people say, oh, well, other people have this. And it's like, yeah, that's cool. It's just, you know, I use DigiKey a lot and so that's why I go back there, you know? Yeah.

**Dave Jones:** You're just going to put this on a tablet and just go to bed and just fondle your DigiKey. Yes. Script, aren't you? I don't know if it would work on a tablet. And your wife's just going to look at you and roll her eyes. Roll her eyes. Yeah.

**Chris Gammell:** I guess it probably would work on a tablet because my phone has Chrome on it now. So I guess I could probably install this on my phone too. Oh, goodness. I don't know if the script stuff works on phones, but – Yeah, man. Dave hasn't had enough. I just got Dave to look at this right before the show. So he doesn't have many superlatives yet, but he'll get there. No, sorry. Yeah. Yep. So anyways, check it out. We'll have it in the show notes. And nice job to Ben. It's pretty killer. Yeah.

**Dave Jones:** Someone will end up buying him for a fortune. Speaking of which –

**Chris Gammell:** Yes. Which one? Hackaday.

**Dave Jones:** Hey, we've got some news. Follow up. Straight off the teletype. Da-da-da-da-da-da-da-da-da.

**Chris Gammell:** Yeah.

**Dave Jones:** Yes. Somebody did pony up and buy Hackaday.

**Chris Gammell:** Somebody. Yeah. Who was it, Dave? Come on. As if I had anything to do with it.

**Dave Jones:** I didn't have anything. They just happened to sponsor my forum as well. Yeah. Yes. Supply Frame, a.k.a. Nobody knows who Supply Frame – they're the finechips.com people. You know, everyone's used finechips, right? That awesome little, you know, supplier – Search box on the EV platform. Search box for multiple prices for multiple suppliers, right? So, yeah, which your script doesn't do. You're always being a script. That's true. Doesn't do magic like that when you try to find the cheapest part. Anyway, finechips.com, yes, they have bought Hackaday. Yeah. Yeah. Presumably for $450,000. We're not entirely sure, but that's kind of the price that – what's his name? What's the guy's name? Who owns Hackaday?

**Chris Gammell:** It is Jason. Jason. Calcanus. Yeah.

**Dave Jones:** Yes. Jason, yes. He threw that figure out there that he had a bid for $450,000 and several lower bids. So, more than one person bid on it, but Supply Frame got the deal, and it's signed, I presume, and they've all announced it. And, yep, Supply Frame are now the owners of Hackaday. And I couldn't think of anyone better, really. Yeah, it's great. You know, because they're very neutral. You know, they're very – that's why I loved it when they sponsored the forum because they're so neutral in everything. And they're, you know – because they don't have anything to sell, so to speak. They're, you know – like it's – Can you imagine what would happen if Element 14 bought them, right? It'd be like, you know, bye-bye Hackaday. So – That's nice to see, Dave. They would have just ruined it. No, well, you know, they've got their own – they work on, you know, they've got their own systems and their own ideas about how things work. Yeah, I know what you mean. You know, yeah. I mean, you know, that's just the way that they do things. And the way that Supply Frame do things is that they generally just don't touch it. They just want to put their little fine chip search box there and they want to, you know, put a couple of their ad network and they just want their name there and that's it. You know, and generally they'll go, well, look, we'll just, you know, fund you and hands off, you know. Plus they get it, I think. These guys get it, you know.

**Chris Gammell:** Well, they've only made one big mistake so far, so.

**Dave Jones:** What's that?

**Chris Gammell:** Didn't figure that one out, huh?

**Dave Jones:** No? Oh, sorry.

**Chris Gammell:** It's you. You were the... Oh, me?

**Dave Jones:** No, I still don't get it. It was a joke, Dave. Okay, thank you. I'll probably get it after the show and then I'll laugh. Yeah, because you're poking fun at me, but okay.

**Chris Gammell:** Right, yeah. Anyways, I'm glad they're going to be sticking around. And that's the main thing. As long as they're sticking around, I like Hackaday a lot, so. Yeah. Well, there you go. Good stuff.

**Dave Jones:** But I think Hackaday is a classic example where if nobody bought it, that crowdfunding campaign was not going to work. You know, that was never going to work.

**Chris Gammell:** No, I didn't think it was either.

**Dave Jones:** You know, that's the thing with a website like this that has no original content. It can just vanish overnight. Because if the editors just packed up and left and, you know, went for hackperday.com, started up hackperday, then I think most people would have left. You know? Yeah, probably. Did we talk about that the other week? Yeah, we did. But yeah, yeah, I think most people would have left, you know, and Hackaday would have just folded. So yeah, I think Jason's very lucky to get that, so.

**Chris Gammell:** Yeah. Good stuff, man.

**Dave Jones:** Good on him.

**Chris Gammell:** Well, what else we got this week? Man, we got their usual slew of crowdfunded projects, but. Yeah, right. But two, so a small trend that I've seen that I think is interesting from an electronics perspective, two different projects with the Xilinx zinc chip on it. Have you seen that chip at all? You looked at that?

**Dave Jones:** Well, I haven't really looked at any detail, so no. I won't talk out my ass on that.

**Chris Gammell:** Oh, yeah, well, we can do that. We can hang with that. I was really excited about this chip when it came out because it's kind of like the holy grail of, you know, like embedded processor plus flexible fabric plus everything else.

**Dave Jones:** It's a system on chip. It's a system on chip. Yeah, it's a kitchen sink, you know. So it's got an ARM processor with FPGA, you know, around it and it's got, you know. Yeah. And it's got, well, it's a dual, it's a dual ARM one gig processor, A9 processor. Yeah, the A9, you know. Right. And plus with FPGA fabric around it. I don't know what other goodness it's got in there, but yeah.

**Chris Gammell:** It's got, I think it depends on the model. You know how like usually the FPGAs have like a big bunch of models. Oh, of course, yeah. There's 20 different models, yeah. Like, so they have transmit, you know, the high speed service transmitters. Of course. They've got hard logic memory controllers for, you know, for use of the DDR2 and 3.

**Dave Jones:** I've got the block diagram up. It's got USB, it's got two USB, it's got two gigabit Ethernet, it's got SDIO, it's got two UARTs, two CANs, two I2C, two SPI. So it's got all your normal microcontroller type stuff. It's got RSA security built in. So, you know, it's got two analog to digital converters.

**Chris Gammell:** Yeah. The nice thing is that in reality, aside from the analog to digital converters, all of those things are possible in Fabric anyways because it's just an FPGA, right? I mean, you just did that video on FPGA. You did two videos on FPGAs, right? Yes. The other one was JTAG, right?

**Dave Jones:** The other was the JTAG, which was associated. Yeah, that's right. Yeah. Yeah.

**Chris Gammell:** So, yeah, people don't, you know, obviously go watch Dave's video on FPGAs. I actually watched that one, Dave. That was, you got one. Yeah. Excellent. Thank you very much.

**Dave Jones:** But yes, this, yeah, as you say, this could have been done. You can put all this stuff in a normal FPGA. It's just that this is the direction FPGAs are headed because it's more efficient silicon-wise to embed these hard modules in there. Yeah, it's so cheap to do that. Yeah, exactly.

**Chris Gammell:** From a logic perspective, right? Because you already have these blocks and other things. You just drop them in now. You know, they're just IP blocks that you drop in and verify and then you do it once. Yep. And it's tough, too, from a licensing perspective because ARM usually, you know, except for the very low-end stuff, I think there's a couple ARM cores that they'll license out to put into soft logic. Most of the time, they'll only work with bigger vendors to, you know, because you have to sign the... To do chips, yeah. Yeah, the big agreements and everything. So, yeah, it's pretty neat. I mean, like, it's a cool part. It's definitely pricey, I mean, but for everything that's in there, you know, it's... Was there... I don't have the block diagram up. Is there a DC to DC in there, too?

**Dave Jones:** There is no DC to DC that I can see. It's not shown in the block diagram, so no.

**Chris Gammell:** Which isn't too surprising, I guess, because...

**Dave Jones:** Well, no, because that's analog crap, right? And they don't, you know, they're...

**Chris Gammell:** Well, no, I've seen these... Dude, people are pulling in DC to DC converters now, too. You know, they'll leave the...

**Dave Jones:** They are into the... Yeah, yeah. Yeah, they'll... Well, yeah, because it's really...

**Speaker ?:** At least the controller.

**Dave Jones:** It's not really... Yeah, it's... You know, there's, like... There's just huge MOSFETs in there for switching, right? And, yeah, but they've got to have, like, op-amp in there, and, you know, for the feedback.

**Chris Gammell:** See, I think it depends on the vendor and the process, too. Like, so... Of course. What was the one process? So, there's a new process... Not a new process, but there's a process out there called BCD, which is bipolar, CMOS, and then DMOS. All... They can put them all in the same wafer now. And that's what's allowing, like, analog vendors to start putting, you know, like, crazy... They'll put, like, state... You know, either state machines in, or they're starting to roll in actual arm cores. Like, there's a couple... You know, with, like... They'll have an ADI... Or an A to D on there, rather. I was thinking of an ADI part. They'll have an A to D on there, and then it'll actually have, like, a Cortex-M3 on there, too, you know? So, you actually can do that kind of stuff.

**Dave Jones:** We're talking about smaller chips there. I mean, these FPGAs are still bleeding edge, right? Process technology. Right, right, right, right. So, they're very limited to what process technology they can use to get this thing. So, that's probably why they didn't incorporate it, because they can't. You know? Right.

**Chris Gammell:** And that's the same reason that, like, you won't have as good of an A to D on there as well, right? It's like a... Yeah, exactly. A to D on there and stuff. Like, you'll see that in a lot of processors, too. You know, they'll just throw in A to Ds, because they're just Sigma Delta, you know, small-time 12-bit A to Ds, because the process can handle it, and the noise level's acceptable enough that a 12-bit's not that big. I mean, it's a big deal still. It's not like I could just whip one up in my basement or anything. But, yeah, it's not like a 24-bit type of thing. You know, you actually have to do some kind of external FETs and stuff like that to actually get the lower noise process stuff.

**Dave Jones:** And I believe they don't have Flash, you know, they don't have the configuration memory built in as well, once again, like most FPGAs. Right. Well, the majority of FPGAs, you need the external chip, I think. Don't quote me on that. It does have a Flash controller built in, but that's not... Yeah, yeah, that's for, like, bigger... Yeah, that's the larger parts.

**Chris Gammell:** Because this is meant to run... You know, like, you're going to see people running, basically, like, Android or Linux, basically, on this thing, because it's set up as a...

**Dave Jones:** It's a system on chip.

**Chris Gammell:** Yeah, it's effectively a smartphone with FPGA bolted to it, you know? Yeah. It's all on the same thing.

**Dave Jones:** It's got two 1-gig processors in it. Holy crap, you know? Yeah. You know, it's got DSP and FPU engines, and... Yeah.

**Chris Gammell:** Holy goodness. Yeah.

**Dave Jones:** Yep.

**Chris Gammell:** And apparently it's a fan of RAP, because it has a Snoop control unit.

**Dave Jones:** I was going to say, my favorite module in there is the Snoop control unit.

**Chris Gammell:** Yeah, Snoop. Jeez, we're childish, aren't we? I just love Snoop Dogg, man. Or Snoop Lion now. Right, okay. What? Let's not get in. No, it's not getting in the music business. No, come on. Snoop Dogg has become Snoop Lion. Everybody knows this.

**Dave Jones:** I do not know this. And I still do not give a talk. So, yeah, let's move on.

**Chris Gammell:** So, back to the fact that the DC to DCs aren't on here. That's interesting, because, you know, I had predicted, or at least the trend I had been hearing about is that, you know, they'd been going to simpler rails, right? Where you'd have maybe like one or two, you'd have an IO power supply for these kind of things to actually power, you know, maybe 3.3 on the outputs of these things. And then you'd have a core voltage, just a single core voltage, like 1.5, and it can divide it down to all the different internal voltages and the DDR voltages that you need in order to actually use DDR RAM. But it doesn't really seem like that. No, no, it is. At least not with these fancy, fancy, you know, parts. Yep, sorry. I don't think any of the other... Sorry, the dream isn't there yet. Yeah, I don't think the vendors, the power supply vendors care, because they want to be like, you need eight DC to DC controllers in one chip, you know? Yeah. You need 16 different rails for your FPGA part? We can do it.

**Dave Jones:** Yeah, that's right.

**Chris Gammell:** Yeah.

**Dave Jones:** It sucks. And that's always a pain in the ass. I mean, you know, I've developed FPGA development hardware, of course. And, yeah, on some of the larger parts, the number of rails that you need is just ridiculous.

**Chris Gammell:** Yeah.

**Dave Jones:** It really is a pain in the ass. I didn't understand why that happens either. And they've got to be high current, so you've got to have like a switching regulator on each one.

**Chris Gammell:** Yeah. You know? Yeah, and then if you need like separate inductors for everything, that just starts, you know, you start putting inductors on board, you start ramping your cost and stuff too, and efficiency.

**Dave Jones:** The power supply is bigger than the system on chip. Just the inductors alone can be bigger than the entire FPGA. I'm not kidding.

**Chris Gammell:** Yeah.

**Dave Jones:** It's crazy.

**Chris Gammell:** Well, I think we talked about it on here. I think the reason that I was looking at a lot of the pulling DC to DCs on board and stuff was because I went to a conference at one point where they were talking about like the speed, the switching speed of these converters going up into like 30 megahertz, you know, kind of range. So you can get super, super small.

**Chris Gammell:** That gets hard on the magnetic side. Well, it gets hard on the leakage side, but the magnetics get super small.

**Dave Jones:** Well, the magnets become smaller, but yeah. Well, that's what I was getting at. Yeah, the leakage side of things.

**Chris Gammell:** The leakage and the switching losses go up a lot.

**Dave Jones:** Once you get to a megahertz, you start getting, you know, you start really having to pay attention. You know, once you get to a couple of megahertz, yeah, you really got to, you know, yeah. I don't know.

**Chris Gammell:** I've done a four megahertz switcher before. It wasn't too bad.

**Dave Jones:** Yeah, but you got to pay attention to what you're doing, especially if you want the best performance, you know. You can't just go pick a part out of your junk box willy nilly. No.

**Chris Gammell:** You're doing that a lot for, you know, big products these days, Dave? You're going just to the junk box? I think those days might be over.

**Dave Jones:** Yeah, I've got a 741 in my junk box. I'll use that in my leading edge project.

**Chris Gammell:** Yeah, I'll hook together my 555 boost like I did for Maker Faire last year. Right, yeah, yeah. I think I calculated it as 30% efficient. A lot of people love that kind of efficiency these days. Oh, yeah. And battery would really last. Yeah. So, yeah, these projects, though, that are using, actually using the zinc part, there's two, so there's two different projects. The first is interesting because it's a, it's claiming to be like a catch-all high-speed measurement platform. Right. Basically saying that, you know, they're putting external DAC, you know, high-speed DAC, high-speed ADC, and then the zinc, and basically, you know, saying that, I think there might be a front end in front of it, too. This is the, the red, oh, where is it? The red, I keep forgetting the name. Pataya or something? Pataya, yeah.

**Dave Jones:** Oh, right, yeah. Yeah. Yeah, I don't know how to pronounce that one either. Red. Right. Papaya or something. Not papaya. No? Oh.

**Chris Gammell:** How did I lose this link? Every time. Every time I lose this. There we go. Yeah, red Pataya. And so, yeah, they have, you know, a couple high-speed capture parts on there, basically. Right. And then, you know, they're saying that you could use this for scope-type functions and for SDR-type functions and lots of different things. Single generator, spectrum analyzer, a lot of stuff. And basically, the ultimate goal being that it's flexible and that you could buy it and, you know, reconfigure it for whatever you needed to use. And that alone is very, very interesting. I mean, I think ultimately it comes down to the analog front end that's going to matter a lot. I mean, like you've done on your teardowns, you know, scopes are effectively big analogs, fancy front ends.

**Dave Jones:** It's all about the analog front end. That determines the entire performance of the product.

**Chris Gammell:** I think we can all agree that analog is probably the most important thing in the world, right, Dave? Right. Yes. Nothing to say about that amazing, you know, mixed SOC behind it with two A9 cores and FPGA's and stuff.

**Dave Jones:** Exactly, which is phenomenal bleeding-edge technology. And it all comes down to how well do the bloody FETs work in the front end. Yeah.

**Chris Gammell:** Well, you know, you're not going to get around it, I'll tell you that much. Right. You can measure noise all you want, but it's not going to tell you much. So yeah, this is a, it's a cool video. I mean, it's a cool, cool little product and suggest that people check it out. It's, let's see, the campaign's got another, oh, they did one of those long campaigns, 50 days to go. So yeah, they've already hit their goal and everything. But like I said, having access to the Zinc without, because I think the Zinc dev board I saw, that Zinc 7000 dev board was like a couple grand when it came out, like three or four grand. Right. Ouch. So now it's actually getting into products. You can actually, you know, this is relatively hackable. They give you some, some breakout headers and stuff too. And, and obviously there is an analog front end and, and, and yeah, so you can, you know, you can get signals in and out and you can play with it and develop your own stuff if you want it to at the end. And that's, that's pretty cool. You know.

**Dave Jones:** Can we go onto a big ass? Yeah, might as well do. Yay. Every week we're going to have a crowdsource campaign. Well, that one was too. But this one's, yeah, this one's 32 million bucks, folks.

**Chris Gammell:** Wait, what about the other Zinc part? I thought we were going to do that first. There's, that was the other thing. Yeah. Oh, I forgot it.

**Dave Jones:** Ah. Hey, we're 48 minutes in and we haven't even mentioned our sponsor.

**Chris Gammell:** Okay. We will in a second. It's the Parallela. That's the other one. That's that, that parallel processing supercomputer thing. That's a hundred bucks. So that's even cheaper than the other, than the, the red pitaya. So that's the other one. Sorry. But we should definitely mention our sponsor.

**Dave Jones:** You can't believe we're going for 49 minutes.

**Chris Gammell:** I know. Just yapping. Ah, yes. So Netburner. Netburner. This is our last show with Netburner for right now. But they have been very generous with us and they have very cool product that we've talked about the past couple of weeks. We have the, the mod kit 52, 418, I think. Or is it? No, sorry. 54, 418.

**Dave Jones:** I've got to complain about their model numbers. It's like, you know, HP model numbers, you know. Where do they get these from?

**Chris Gammell:** That's based on the, the, the part from the, the free scale part that's on board. So that's how they actually correlate that. Of course, of course, they correlate it.

**Dave Jones:** Dope. So. That makes sense. Okay. I, I retract my criticism. Yeah. You see it now? Okay. Yeah.

**Chris Gammell:** So the thing we tried this week actually is the, the application builder, basically. It's a very fast way to get started. You just, we'll post a video to actually show you how you can get started.

**Dave Jones:** It's almost instant.

**Chris Gammell:** Yeah.

**Dave Jones:** It's ridiculously simple.

**Chris Gammell:** Yeah. So you basically, you plug in, you plug in your, your board on the network. You go through, it's just like a simple project setup in Eclipse. They have their own little flow, but basically you just select what you want on board, what you actually want to download to it. You know, like web server, DC. I want a web server.

**Dave Jones:** I want auto updating. I want DHCP. I want all this in my project. And you see, you tick the boxes and you press go and it. Yep. And it just zips it right up to it. And then, you know, it gives you a hello world, you know, and then you just type in your code underneath.

**Chris Gammell:** Yeah. It's crazy. And, and the really cool thing is so like, I was just playing around with just the webpage. There's like an included HTML page that comes in there so you can use for troubleshooting with like the web server and everything. I updated it. I added the amp hour rules to the, the index.html. I hit save. And then the auto update function, because I actually included that in the build, it just zipped it right up to the, you know, over the network completely in the background to me. Um, which, you know, for, for my, my speed of development, you know, that's, that's amazing. Usually that'd be able to two hours later, I'd finally get it uploaded and everything. Yeah. Especially since it's over the network. So, uh, that's, that's really cool. So, uh, people go to netburner.com slash the amp hour and you can get a 20% discount on kits and you can find out more about their programs and, you know, all the, the, the development environment, everything. It's very, very good deal. So check it out.

**Dave Jones:** Definitely check it out. I agree.

**Chris Gammell:** All right. Uh, so where are we going next?

**Dave Jones:** Speaking of ridiculous, uh, Indiegogo campaigns.

**Chris Gammell:** Oh yeah. Yeah, this is interesting.

**Dave Jones:** $32 million. The, the, the Ubuntu Edge. Yeah. It's a phone. It's a smartphone. Yes. It's a, you know, open, whatever. Is it open? Uh, yeah. It's not going to be like open hardware, but it'll be. No, no. Right.

**Chris Gammell:** No.

**Dave Jones:** But it's designed for the software geeks, I think, or something. I don't know. Whatever. Who cares? We won't harp on about it. But it's, they're after 32 million bucks. Right. And they've already raised 7 million bucks and there's 23 days left. They might actually make it.

**Chris Gammell:** They might just do it. I mean, basically it's like, it's like buying a, you know, an off contract phone. That's effectively the price they're asking for. Yeah. And, uh, it's impressive hardware. It's, you know, it's, it's obviously consumer level. So it's a little out of our, our, our round house usually, but, uh, a wheelhouse rather.

**Dave Jones:** But there's a reason why it's on Indiegogo and not on Kickstarter because they don't have a prototype, folks. Yes. They're asking 32 million bucks and it's just some, uh, Photoshop renders. Oh, I didn't know that. Of the final product. I think. Anyway. I don't know. I haven't watched the video. Probably talking out my ass. Yeah.

**Chris Gammell:** Yeah. It does. It does just look like renders, but, uh, it's, uh, it's, I mean, it's a nice looking phone and, but the, yeah, the impressive thing is the, uh, the actual fact that they're asking for so much money. So we'll see.

**Dave Jones:** 32 million bucks. And it's not, you know, I mean, uh, it's not easy to manufacture a high quality phone and not cheap either. Even if you think 32 million bucks might be able to do it. Well, you might be wrong.

**Chris Gammell:** You know, there's so much tooling and everything, you know, it's just, it's just setting up the

**Dave Jones:** factory to, to churn them out. And like, and the thing is a lot of factories won't touch you. Right. They'll go, Oh, you want how many phones? 10,000, even 50,000. They'll just laugh in your face. Right. Because the big manufacturers are boasting. They're selling hundreds of thousands of phones per day. Right.

**Chris Gammell:** You know, it's like, yeah, no, yeah. It's, it's crazy. I mean, well, and people have seen, yeah. I mean, if you look at the videos of just, you know, like Foxconn factories making Apple stuff, I mean, just the scale of it is, is amazing. So it's, uh, yeah.

**Dave Jones:** So I, you know, yeah. Good luck if you expect to get your phone anytime soon. Yeah. Well, yeah, but yeah. Dear, dear, dear. But yeah, I mean, well, you know, that, that's really shooting for the clouds. Right. I mean, that's really going for broke. Like, I can't imagine it getting any, you know, any campaign being any bigger than that. I mean, 32 million bucks to do something that you take for granted is a commodity item. You just walk into your shop and buy. Yeah. Really. I mean, whew. Wow. You know, that's a gutsy campaign.

**Chris Gammell:** There are a lot of people in the world, Dave. I mean, there's a lot of, there's a lot of money out there. So.

**Dave Jones:** Yep. True.

**Chris Gammell:** You know, my favorite, uh, part of my smartphone slash Google glasses.

**Dave Jones:** What's that?

**Chris Gammell:** I was all weekend. I was playing with the, uh, the translate function. So. Oh, right. You tap the side, right? And you say, how do I, this was in like one of the promo videos too, but, uh, how do I say this transistor is broken in Chinese? Right. And it'll actually, it'll actually say it for me and then it'll show it in the little screen. And I realized that this is like the perfect device for going to like markets. Right. And then my friend actually told me today too, he's like, well, you're skipping a, or you should skip a step. That basically I should just get a speaker and then just, I say it into that. Yeah. Yeah. Of course.

**Dave Jones:** And then it speaks it. Yeah. Yeah.

**Chris Gammell:** It just speaks it. Right. That's. And I was thinking, oh yeah, of course I'm going to say it wrong. Right. But like that, that is like the most brilliant application for like actual, like human interaction stuff.

**Dave Jones:** Well, I think you can get apps. Can't, can't you get apps that do that now for your phone? Yeah. I mean, it's Google.

**Chris Gammell:** Right. I mean, that's Google. That's you can do that now for Google. It's just a little more discreet. Okay. But yeah, man, I just never, I never thought of it before. I was just playing with it anyways. And then I started thinking about, you know, like going overseas. Cause you know, that's, that's a, I wouldn't say a fear of mine, but I'm very apprehensive about going overseas. It's a big deal. Yeah. I mean, you know, like language barriers and stuff. Cause I was in Korea for a while and it's just embarrassing when you don't know the language. Exactly.

**Dave Jones:** It's more embarrassing than anything. And it's just, you know, harder to get things done really. Oh, definitely. Yeah. Yeah. Yeah.

**Chris Gammell:** So, you know, like all the people, like, so like, uh, we have this article here, how Ian from, from dangerous prototypes, he just moved to Shenzhen as well. Right. We know a couple of people over there now. And it's like, that would be the first thing I would do. Obviously, you know, you have access to this huge marketplace, but if you don't have someone with you that speaks Mandarin, you're kind of screwed. Right. I mean, like that would, should be the first thing you do when you go over there because otherwise, why are you there?

**Dave Jones:** That's right. Yeah.

**Chris Gammell:** I mean, pointing and grunting only does so much, right? I mean, haggling is an important factor in any marketplace environment. So the fact that, uh, you know, Google might allow me to swear and tell people they're ripping me off, you know? Yeah, right. Screw you.

**Dave Jones:** I can go to the guy to boost down and get half the price, you know? Exactly. Yeah.

**Chris Gammell:** You need, you need, you need, you need like a phrase book, right? Like.

**Dave Jones:** Right. Oh, dearity.

**Chris Gammell:** And then there's always the fear. Do you ever see that, uh, Monty Python skit with John Cleese, the, uh, the tobacconist? Where.

**Dave Jones:** No, I don't think so.

**Chris Gammell:** There's like a prankster that, uh, that, uh, gives him a bogus, a bogus translation book and he starts saying all these, these wrong things in Dutch. Nice. It's very good.

**Dave Jones:** Especially if you understand Dutch.

**Chris Gammell:** Oh, no. Basically he ends up getting punched a couple of times. And they have the little translations on screen and everything. Oh, it's good. Yeah. But, uh, yeah. Love it. So Google's also working on the, so the, and they, they've talked about this as well from a, you know, like a broader perspective, right? I mean, this is a huge data project. You know, the electronics for it is impressive too, just from the, you know, it's mostly a microphone, but then, you know, you gotta, you gotta do DSP on it and stuff like that and actually get, um, you actually have to capture all the phenomes and all that stuff that's language based.

**Dave Jones:** And then you've got to understand the Australian accent.

**Chris Gammell:** Right. Well, good luck with that, buddy. Which doesn't work. Yeah, exactly. It only works for you, Yanks.

**Dave Jones:** Yeah. But then, so I saw an article though. It doesn't work speaking strine. Strine? Strine.

**Chris Gammell:** Yeah, I have no idea what you're saying right now.

**Dave Jones:** Strine, mate. Strine, right.

**Chris Gammell:** I know what it really is. Strine, right. No worries, man.

**Dave Jones:** She'll be right.

**Chris Gammell:** Google's actually working on a, uh, a Babelfish or Babelfish, depending how you say it, basically to have the other, the other side of the, so if Dave is speaking strine to me, uh, it could understand him and then translate it to something that's understandable for me because I'm like, you know, what are you talking about, you crazy Aussie? And, uh, yeah. So it's, it's very exciting. It's, uh...

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** It'd be very useful if I went overseas anymore.

**Chris Gammell:** Right. Of course. Yes. Exactly. We'll get you over here eventually.

**Dave Jones:** Right. Our hour's up. But we're going to soldier on.

**Chris Gammell:** No, we can keep going.

**Dave Jones:** Because we've got a ton of stuff to talk about. Yeah. Yeah.

**Chris Gammell:** And a lot of, a lot of people have been, uh, submitting links too. So thank you for that. That's, uh...

**Dave Jones:** Yeah. Yeah. Thank you very much. Because I'm sure...

**Chris Gammell:** I'll go through at the end of this and actually... I'm hopeful. ...grab one that, uh, people, people added, you know? Right.

**Dave Jones:** Oh, can we do... We've got a shonky product of the week. Shonky product of the week.

**Chris Gammell:** The one that you did add? Is that the one that you were talking about?

**Dave Jones:** Yes. The one, the one thing I did add.

**Chris Gammell:** Go ahead.

**Dave Jones:** It is outbooster.com. The internet speed booster. Somebody sent this. So sorry, I forget who sent it to me. They emailed it to me. And, um, yeah. It's a little dongle thing. You know, it's got ethernet in, ethernet out. No power by the looks of it. Right? So it's just ethernet in, ethernet out. And it speeds up your internet connection. Thank God. Yes, folks. And just look at the website. And it's just, yeah. And, um... Oh, God. And it, apparently, if you leave it in there for 30 days or whatever, it learns all about your internet connection and, you know, learns and adapts and all that sort of stuff. Optimizes. Yes. Optimizes, yes. Yes. Oh, boy. With no, you know, it's just ethernet in, ethernet out, folks.

**Chris Gammell:** Is it really just a pass-through? Is that all it is?

**Dave Jones:** Well, I don't know what's inside, right? But it's obviously not much.

**Chris Gammell:** Yeah. Right?

**Dave Jones:** Because there's... Our technology is exclusive and patent pending. Oh, goodness. Yeah, folks. If this one works, I'm a monkey's uncle.

**Chris Gammell:** His name is Bob.

**Dave Jones:** Well, actually, I'm sure it works. Just like the, you know, the $10,000 speaker cables work. If you spend money on it, you know... Yeah, it'll just be... I bet you it works for you, you know? It'll be all in your mind, right? Yeah, that's right. Oh, boy. Maybe they'll hear the show and they'll send us one. We can do a tear down. Yeah, three samples. I bet you it's potted. I bet you it's potted inside.

**Chris Gammell:** Yeah, probably. Mm-hmm. So, in terms of things that other people have sent in, Daniel Amesberger, he actually sent in a pick-and-place machine he's been working on. This is actually, like, he's calling a DIY...

**Dave Jones:** Not another do-it-yourself. Like, my hat's off to people who work on them, right? They're cool projects just because they, you know, they're robots and they pick-and-place components, right?

**Chris Gammell:** Yeah, but this is a little different, too. It's not like... Because this isn't like... We've seen one where it's like a MakerBot-style frame, right? Where it's just a little tiny thing. This thing's like 80-20 style. Like, this is... This looks pretty beefy. Hang on. I forgot this one open. Okay. Yeah. And so, I asked him about it, you know, like, just asking how much in parts. He said just in parts, it's about $6,000 or $7,000, I think. So, I mean, like, this is... This is...

**Dave Jones:** Jeez, you can buy a used machine for that, almost.

**Chris Gammell:** Yeah. Well, yeah, we were talking to Ryan about it the other week, and basically, I think Ryan said he paid, what, like, $15,000 or $16,000 for that refurb one or something like that. Right. And I don't remember how much it was exactly, but I think it was, like, you know, anywhere from, like, $15,000 to $25,000 for a refurbed, older-conditioned one. Yeah. And, yeah, so $6,000 or $7,000. I mean, like, that's the thing. Like, it's the same in all kind of mechanical things. You know, like, heavy stuff is expensive, right? Because it's just a lot of material there. Exactly. And if you want high-powered, you know, stepper motors or, you know, actuators and stuff like that, like, it's not cheap, right? I mean, like, even Ryan talking about the expensive feeder mechanisms and stuff like that, like, there's just a lot of metal there. You know, it's just a lot of mechanical engineering stuff. So this looks great so far. I mean, honestly, it's a great-looking video.

**Dave Jones:** He agrees with me. He mentions me in the article. He does. The TM220, the $4,000 toy-like pick-and-place machine, as I called it, he is completely with me on that. So there you go. Right. Because it has no vision. It's got, you know, it's just a, yeah, it's pretty dumb pick-and-place. Those ones that you can pick up from China now for a couple of grand. Right. Yeah.

**Chris Gammell:** Right. And the other thing to point out about this, I guess, too, is that, so there's $6,000 or $7,000 in parts, right? But this is low-quantity parts, too. Oh, of course. Of course. This is all wild stuff. Yeah. If he, if he, if Daniel takes this and, you know, starts to commercialize it, you could start to optimize for, you know, bulk buys and stuff like that. So there, there would be, there would be optimization there. But in terms of, like, if he sold it, then, you know, basically whatever you make up in volume pricing, you're probably going to charge that to your customers. And so it's safe to assume probably $6,000 or $7,000 just for the final product if he optimized the manufacturing, you know. Oh, easy. Yeah. So. No, at least.

**Dave Jones:** And he's from Austria, not Australia. Not Australia. And that's what he talks about. He talks about Ryan who, you know, bought the $16,000 used pick-and-place machine. But, of course, you know, yeah, you can get them that cheap if you're in the States. They just toss them away. They're a dime a dozen. All these companies are closing because America's going down the toilet. Blah, blah, blah, blah, blah, blah. Blah, blah, blah, blah, blah. And no worries. And good to see they're building cars again, as we talked about. Yes, that's right.

**Speaker ?:** But, yeah.

**Dave Jones:** Yeah, American manufacturing. Anyway.

**Chris Gammell:** The houses are being built, too, you know.

**Dave Jones:** Oh, what? Isn't there, like, 40,000 abandoned houses in your bankrupt state of Detroit? In my backyard. Sorry. Yeah. In your backyard and in Cleveland, too? Yeah. At least we're not Detroit. Which declared bankruptcy, if people don't know. Yes. The state of, the entire state of Detroit declared bankruptcy. City of Detroit. The city of Detroit. Sorry. It's not a state. Duh. Yeah. Slap out of the head with a wet fish. All right. You're right, though. It is harder to get surplus equipment, you know, in certain parts of the world. Yeah. Like, I wouldn't be able to get one here in Australia.

**Chris Gammell:** Right. It turns out you can't get them in Austria, either. You'd have to just build your own, right? Yeah.

**Dave Jones:** Well, that's right.

**Chris Gammell:** You'd have to sew your own little poncho and strap yourself in with the little poncho thing. Yeah. Oh, people gotta see this picture. It's so awesome.

**Dave Jones:** It's not that funny.

**Chris Gammell:** Oh, come on.

**Dave Jones:** What else are you supposed to do if you're riding a bike in the rain? Of course you put a poncho on, otherwise you get wet.

**Chris Gammell:** It looks like someone climbed into their child's, like, play school tent. There happened to be a tricycle inside. They popped their head out the top. They hopped on the tricycle, and then they started wildly peddling around. Oh, my God. Oh, boy. Oh, goodness. Yeah. All right. At least Sinclair's not in business anymore. I don't feel bad making fun of them.

**Dave Jones:** Oh, no. He's talking about bringing it back. He's talking about he's got a new vision. Yeah, he's got a new vision for the future.

**Chris Gammell:** Well, good luck to him. He can do it.

**Dave Jones:** Sir Clive. Yeah. Maybe we can get him on the show.

**Chris Gammell:** Maybe. Maybe.

**Dave Jones:** Who would like to see that? Hands up. Physical show of hands here. Who would like for us to try and get Sir Clive Sinclair on the show? That'd be awesome.

**Chris Gammell:** Anyone? Bueller?

**Dave Jones:** Anyone? Anyone? Bueller? Hello? Anyone out there? No? I can't see anything out in the class here in the corridor. No? There's no one outside? Waving? No? All right. All right.

**Chris Gammell:** So one last submitted link. This comes from Mike. And basically, he had actually sent us an email. But his folks were digging up a shed. But his folks were digging up a shed. In his backyard, they were digging up the shed. And basically, his dog started chewing on something. And it's a little Bakelite terminal from... So it's a general electric, improved electric coupling from the 20s. Made out of Bakelite. It's really cool. It's like just this little old thing, you know, basically for hooking wires together. But yeah, his dog was gnawing on it. And so he pulled it out and sent us a picture of it.

**Dave Jones:** It's a...

**Chris Gammell:** Awesome.

**Dave Jones:** Yeah. It's a rusted piece of... It's a rusted turd, really. But...

**Chris Gammell:** No, that's the thing. That's not rust. That's Bakelite. The brown part is Bakelite.

**Dave Jones:** Is it?

**Chris Gammell:** I just assumed that was... I thought so, too, at first. But yeah, it's...

**Dave Jones:** Oh, okay.

**Chris Gammell:** It's got like little machine threads and everything, too. Oh, yeah.

**Dave Jones:** Now I... Right. Now I... Okay.

**Chris Gammell:** Yeah, because when you first look at it, you're like, oh, it's just old.

**Dave Jones:** Yeah, well, it's just a... Yeah. It's an old rusted bit of... Yeah.

**Chris Gammell:** Yeah, Bakelite, man. Interesting. That stuff was in everything. Oh, yeah. I got an old radio case made out of Bakelite. Yeah. Standing, that was a bad idea. Yeah. Yeah. Yeah. I probably have some carcinogens in my body now. Yeah. Some more, of course. Well done. Yeah, and that's like the same stuff that Bill and Dave used to have their... When they started up HP, their wives were...

**Dave Jones:** Yeah, they were baking them in their oven, yeah.

**Chris Gammell:** In the oven, yeah. Baking those...

**Dave Jones:** Baking like front panels.

**Chris Gammell:** That is DIY, man. That's cool shit.

**Dave Jones:** I like it.

**Chris Gammell:** Yeah. Any other links that we should point out? I put up a list of analog newsletters. I was looking through those today. Those are always fun. I'll put the link in.

**Dave Jones:** Yeah, because you've got a hard-on for analog. We know.

**Chris Gammell:** Yes. It's my life, man. Google have come out with some Google... It's my mouth until it goes away.

**Dave Jones:** Right. Google have come out with some Google TV dongle thing for $35. It's my box, whoop-dee. No, it's cool. Yeah, it's a cool thing. It's like a little...

**Chris Gammell:** It runs Linux and plugs into TVs and basically allows you to throw your screen up onto a TV. And it's hackable. It's already been hacked, too. That's the other thing.

**Dave Jones:** Oh, right. Has it? Okay.

**Chris Gammell:** Yeah, and it's sold out immediately, so...

**Dave Jones:** But it hooks up to Netflix and all that, which we don't get here. You know, it's like...

**Chris Gammell:** Oh, you don't? Oh, that's too bad.

**Dave Jones:** We don't have Netflix here.

**Chris Gammell:** Yeah, dude. Living on the stage really sucks. Oh, darn. At least we're not, Sydney.

**Dave Jones:** I don't even know what Netflix is. I don't even know how it works, because we just don't have it.

**Chris Gammell:** It's like streaming... It's like what you do with torrents, basically. Yeah, that's right. It's like that, except legal and more instant.

**Dave Jones:** Okay. Yep.

**Chris Gammell:** It's like YouTube, except you pay up front for like nine bucks.

**Dave Jones:** Right. And it comes over the cable, does it? Is that the traditional...

**Chris Gammell:** Well, no, it comes over your internet. It comes over your internet connection.

**Dave Jones:** Oh, it comes over your internet, right. Yeah. But you'd have to have like an unlimited internet plan to... Otherwise, it'd chew up. If you're watching that all day and all night, it'd chew up with bandwidth, wouldn't it? Yeah, we have that here, too.

**Chris Gammell:** So we don't have bandwidth caps here.

**Dave Jones:** Oh, right. Okay. Well, a few other companies do that here, like Telstra, who run the cable here. Yeah. You can watch their content isn't metered. So they have... Of course. You know, all of your regular stuff is metered, but if you watch their paid content, it's not metered. So it doesn't count towards your quota.

**Chris Gammell:** Right. That makes sense.

**Dave Jones:** Yeah, of course. Yep. Yeah. Can't wait for that. Maybe we'll get all sorts of stuff like that when the National Broadband Network...

**Chris Gammell:** Oh, yeah.

**Dave Jones:** ...finally makes it here. And we have fiber into every home like every other bastard keeps pointing out. Thank you very much, people. I always get these tweets. Well, I have 100 meg bits upload and download for 20 bucks a month. What's your problem? You know?

**Chris Gammell:** Where's that? Bite me. Oh, man. Bastards. We're not going to include them anytime soon.

**Dave Jones:** Anyone who's got faster internet than me is a bastard. End of story. Yeah.

**Chris Gammell:** Yeah. There's a soundbite. I guess the last thing I'll mention... I'll mention... So, I mentioned the meetup. We had a meetup in New York that went great. Thanks to everyone who came out to that. We're going to have another meetup at... How many people turned up? That was about 10. Cool. We'll have another one at Open Hardware Summit, probably. Probably Thursday night, somewhere around town. And then... The other thing, though, is Cleveland's going to have meetups because I met up with Martin Lorton, who you know from YouTube, and hopefully everybody knows his videos.

**Dave Jones:** He's a fellow full-time blogger now. He's the only other one doing it full-time. So, both myself and Martin are doing it full-time. So, if you're not watching his channel, please support him. Yeah, he's got some cool... Because supporting people like us helps encourage other people to think that they can do it full-time one day and help encourage them to produce content.

**Chris Gammell:** Definitely.

**Dave Jones:** So, you're not just helping us, you're helping the whole industry.

**Chris Gammell:** He's been doing intro videos, too. He's doing a power supply build. Yeah. He's kind of working up to that, too. And he's got a lot of good stuff. I mean, he was nice enough to mention the Amp Hour and contextual electronics on his Thought for the Day segment, too. So, very cool. And he is a nice chap. We had a beer, or three. And we're going to be doing that regularly in Cleveland. So, if there are any Cleveland listeners, let me know. Ah, right.

**Dave Jones:** That's going to be a regular nerd meetup, is it?

**Chris Gammell:** Yeah. We're thinking just like one Thursday a month, basically. Just kind of parking it at a bar and, you know.

**Dave Jones:** I should do that. I should do a meetup.com theme. Dude, I... And have that as a regular...

**Chris Gammell:** Exactly. And, you know, other people should do that, too, because it's not hard. You know, basically, you know, if people need help getting that set up, we'll definitely announce it on here.

**Dave Jones:** Hmm.

**Chris Gammell:** Because it's sometimes... It's really hard to find other people who are interested in this stuff. Yeah. And when you actually get to sit down and talk to someone about it, man, it feels like it's just so natural and like... Right. You're like, ah, finally, someone freaking... You know, because even like... Yeah. You know, you'll go to work... Like, I'll go to work sometimes. And it's just like... I'll have people who are technically proficient and who I like as people, but it's just like we're just not interested. We don't get as excited about the same things, you know. And when you're sitting with someone like that, you know, and just shooting the breeze and talking about projects and stuff, it's basically like this, me and Dave every week. You know, like we get to just have a chat every week, you know. Shoot the shit. Yeah. Exactly. It's great, you know. And when you can do that in person, it's even better. So Dave's going to fly to Cleveland one of these weeks. Right. Yeah, sure. Hang out with me and Martin.

**Dave Jones:** No worries.

**Chris Gammell:** Yeah. God. Can you imagine flying all the way here, just go to Cleveland? Yeah, a quick 20-hour flight, yeah. Dave Jones, the Midwest tour.

**Dave Jones:** Yeah.

**Chris Gammell:** You know you'd see some sweet car factories. You know that.

**Dave Jones:** Right. What? Abandoned sweet car factories?

**Chris Gammell:** You just wouldn't be able to touch anything. You'd get written up to the union.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** All right. So do you think a meet-up, like just a get-together dinner meet-up is better? Like, because I've always thought, oh, yeah, I'd love to have like a sort of a meet-up in the lab. You know? No, no, no, no. Go. It's not as workable. It's third-party location. Yeah.

**Chris Gammell:** Then you don't have to worry about any of the hosting or anything like that. Yeah. Even if you can't make it, then that's good, too. Yeah. No, because everyone else just turns up and they- Exactly. And that's the power of doing those kind of things. You know? Yeah. It's just- And especially if you have it on the regular day, like the third Thursday of the month or something like that. You know? Right. Yeah, yeah. That's a really good way to do it. And I don't know.

**Dave Jones:** The problem with Sydney is that it's so geographically dispersed. Yeah, you know what, though? Dispersed with an ED. Yeah.

**Chris Gammell:** But for, you know, talking to people about nerdy electronic stuff that you can't get many other places other than like a forum, it's worth the drive, you know? Like that's the thing.

**Dave Jones:** It's worth- Yeah, yeah. Yeah. Maybe I'll do that. Maybe I will- You totally should. Go. Just bugger it. I'll do it even if one person turns up.

**Chris Gammell:** That's the other- Yeah, that's the other good thing. You know? Like it doesn't matter if it's just one person or, you know, if it's- If you actually drink beer, then it's just you.

**Dave Jones:** I'll ask on the forum. I'll ask on the forum to see how many people would be interested in a weekly meet- Nah, just do it, man. And if I can get a couple of people. Just do it. Yeah, but then I got to, you know, it'd be nice to know where people live so that you can choose like a central location kind of thing, you know? No.

**Chris Gammell:** For at least a core group of people. Nope. Just pick it and go. No. That's the thing. Just pick and go. I'm telling you. And, you know, every time I go to a city now, like that's- Right. It's just the way to do it, you know? You just pick a place and if people can make it, they can. If they can't, they can't.

**Dave Jones:** Right.

**Chris Gammell:** And next time, if you can't do it, then yeah, we'll get you next time. You know, like that's the best part about it. So, like I said, if people need help publicizing meetups, let us know.

**Dave Jones:** But you've got to book a private room because if you try and do it in like the middle of a pub and you're all just sitting in a booth and everyone's trying to, you know, if you- No. You get all the babble of all the-

**Chris Gammell:** Yeah. No, in New York it was like, we got a big table basically in the back room of a bar and, you know, we just reserved it. And then you just move around a lot. That's the thing. It's best if you just have a stand-up event.

**Dave Jones:** Right. Wait. Yeah, yeah. Okay.

**Chris Gammell:** Like restaurants don't like that as much, but yeah. Nice. That's the way to do it, man.

**Dave Jones:** I think I might.

**Chris Gammell:** Nerds being social. But then again, I'm not a very social enum.

**Dave Jones:** Yeah, see, I'm not a very social enum. Oh, yes you are. Never have been.

**Chris Gammell:** You'll be fine.

**Dave Jones:** It's the same thing like conferences, you know? Spent my entire entire childhood in my lab on my own, you know? I'm not a social enum. You'll be fine.

**Chris Gammell:** Seriously, it's like you'll get this dose of it once a month and then you go recover, right? That's just how it goes. You know, it's like Maker Faire is like that, you know, like Open Hardware is almost like that. It's like this intense meeting a lot of people, talking about fun stuff, and then you just go, you got it. You got to unwind because if you don't, you'll go crazy.

**Dave Jones:** And I think weekly is too much. You would have it like once a month, right? Once a month, definitely. Once every three weeks or something, yeah.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Hmm.

**Chris Gammell:** Can we end the show now, Dave? Is that okay with you?

**Dave Jones:** Yeah, we can. Oh, why? You got something better to do? Have you got another startup idea to go and do this week?

**Chris Gammell:** Well, I do have some videos to make. Yeah, I got a crap load of videos to make still.

**Dave Jones:** I've done my video today.

**Chris Gammell:** Yes. I know. You're done. What are you going to do all day?

**Dave Jones:** This is, well, I don't know. Well, I was thinking about listing a whole bunch of shit on eBay because I was complaining to my brother-in-law the other day who came to the lab. I was complaining, everything keeps coming into the lab, but nothing ever goes back out. I'm just hoarding stuff, and it's getting ridiculous.

**Chris Gammell:** And my basement's like that. It's like a black hole. You could just give it away.

**Dave Jones:** So that's what I'll probably do, and I've got to finish off my little project that I'm doing for my new segment.

**Chris Gammell:** Which I named.

**Dave Jones:** Which you did name, so I will thank you now if I don't get around to thanking you in the first video. Oh, you better thank me in the video. That better be like the whole first video.

**Chris Gammell:** Let me tell you all about Chris.

**Dave Jones:** The whole first video is just bowing to Chris.

**Chris Gammell:** Let me tell you how much Cleveland is awesome.

**Dave Jones:** Right. That's the price I've got to pay for the names. Yeah. I've got to compliment Cleveland. That's the naming rights, yeah. The EV lab.

**Chris Gammell:** All right, man. Well, I guess we'll... Oh, next week. That's the last announcement. This Dave doesn't even know. We are going to have the entire Spark Funds engineering team on the show next week. What? It's going to be insane. So I'll have a post-up.

**Dave Jones:** Why don't you pass this by me? I know. I don't care.

**Chris Gammell:** How many people are we talking about? Seven engineers on their end. I just sent them all the equipment. Oh, dude.

**Dave Jones:** This is so not going to work.

**Chris Gammell:** It's going to be pandemonium. It's going to be... This is not going to work.

**Dave Jones:** I may as well not show up. I won't even get a word image-wise.

**Chris Gammell:** Yeah, you won't talk much. It's fine. It'll be fun. Believe me. So if people have questions for the Spark Fund engineering team next week, we'll have a post-up to get your questions in. And I'm really glad I remembered. Yeah. So next week, I'm excited, man. It's going to be crazy nuts.

**Dave Jones:** And it's probably going to fail miserably because we've got too many people. I warned you about this.

**Chris Gammell:** I know you did.

**Dave Jones:** I warned you that having more than one guest is... It doesn't work. And we'll see how well it doesn't work next week.

**Chris Gammell:** Yes, that's right.

**Dave Jones:** I can say I told you so.

**Chris Gammell:** Yep. You can tell me then.

**Dave Jones:** Bye.

**Chris Gammell:** See ya. This episode was brought to you by NetBurner. NetBurner allows you to get your embedded network solution up and running quickly so you can get your prototype or your final product out the door faster than any other solution available today. To hear more about the hardware, software, and friendly build environment, and to get a listener discount, go to netburner.com slash theampo.

**Speaker ?:** NetBurner.
