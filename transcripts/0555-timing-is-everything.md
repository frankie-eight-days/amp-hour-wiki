---
episode: 555
title: Timing is Everything
url: https://theamphour.com/555-timing-is-everything/
---

**Dave Jones:** This is The Amp Hour Podcast. Released August 30th, 2021. Episode 555. Timing is everything.

**Yankee:** Welcome to the Amp Hour.

**Dave Jones:** I'm Dave Jones from the EEVblog. And I'm Chris Gammell, Contextual Electronics. Happy 555. 555. Dave's wearing... Represent. Yeah, he's got some festive stuff on right now. Welcome. Welcome.

**Yankee:** And thank you for joining us, everyone. Yeah, live event. Yep. Hopefully. I'm just checking because this is going out to EEVblog2 as well. Oh, yeah, there we go. Yep, it's there. It's there. Cool, cool. Great. We're doing it. The internet works.

**Dave Jones:** Mm-hmm. Terrific. One thing in my life that's actually being put together right now. Right. I'm giving everything else. I was just showing right before the show. Well, I'm not going to show it with you. It's a hot mess on the other side of the room here. But it's getting there.

**Yankee:** This is your new lab in your new house. How many square footage? Because it's Yankee land.

**Dave Jones:** It's Yankee land. It's 14 by 15. So whatever that is, a little bit less than 220. 15 by 15 would be 225. So yeah, another 210, I guess.

**Yankee:** Which is the bedroom. And that's large. That's actually pretty large.

**Dave Jones:** This is a bonus room. This is a bonus room. A bonus room. They built it out over the garage. They threw it in. Yeah. It was used as a bedroom in the past.

**Yankee:** Oh, okay. It's not part of the original house.

**Dave Jones:** That's right.

**Yankee:** Yeah. Ah, add-on. Okay. Yeah. Right. Got it.

**Dave Jones:** Yeah, so it's great. If I blow it up, no big deal.

**Yankee:** You're right. The lab burns down. Is there a fire extinguisher in there yet?

**Dave Jones:** Oh, definitely. Yeah. Right. Okay. Cool. One of the first things I'd say, fire extinguisher, label printer, computer, new computer monitor. One of my buddies started using a 4K TV as a monitor. Oh, yeah. Yep. So that's like a, I'm sure you'll find one in the dumpster at some point, right? I mean.

**Yankee:** I've found, yeah, no, I've got a 4K. I've found two 4K TVs in the dumpster. Wow. Wow. Yeah, but they're giant. They're too big for a monitor. They're like 50 or 65 inch, you know. Yeah, this is 50. 50 or 60 inch.

**Dave Jones:** This is, no, this is a 43.

**Yankee:** So I've got a 4K monitor. Here, I've got three monitors and one of them is a 4K monitor. It's 32 inch, but it's just, it's actually too small because if you run everything at the native 4K resolution, all the fonts are too small. Everything, I know you can do font scaling and stuff, but it doesn't work in programs that I use properly.

**Dave Jones:** Yeah, my computer's having trouble keeping up. And I, you know, like when you start to really think about it, like what is, like all the lines it's got to draw and whatever. And like if the GPU isn't set right, whatever, it's just, the computer's just like, no, I can't, I can't keep up. I can't do it. Guys, guys.

**Yankee:** When I was a boy.

**Dave Jones:** That's right. Yeah.

**Yankee:** Well, I used to, I used to work on LCD monitored actual design back in the nineties, back in the early nineties at Key Corp. I was in the flat screen group. I was in the flat screen monitor group.

**Dave Jones:** Yeah.

**Yankee:** Yeah. And I can remember we were working on 800 by 600 monitors back then. And that was kind of like leading edge kind of stuff back then. Yeah. 800 by 600. Yep. And back then when you bought the actual panels themselves, they would not guarantee no dead pixels. You, you had to buy them and they would say, well, you may have up to like three dead pixels or whatever. This was like for commercial LCD monitors. You get what you get guys. Come on. Yeah. Yeah. Exactly. You should be thankful this amazing technology exists. That's right. You peasants.

**Dave Jones:** I just think about it. Like, you know, like it's so part of our lives these days, like, and, you know, as technology progresses too, but when you really think about it, like, you know, each pixel is an LED or each pixel is a, you know, or like when the DLP thing was a thing.

**Yankee:** Is a lighty mid-in element. Yeah. It's a little element. And then there's three of them.

**Dave Jones:** Yeah. Yeah. When DLP was like moving mirrors and like all of these things that are there. And it's just because of over time, it's been built up. It's just, it becomes this normal thing now. And I don't know. Got to stop and smell the technology roses sometimes, Dave. Right.

**Yankee:** Right.

**Dave Jones:** Yeah.

**Yankee:** So we have people joining us from the YouTubes and also technically Facebook as well, but I don't think anyone in the engineering community uses Facebook, do they? I always just got one comment. So yeah, we'll be here. Oh, really? Oh, okay. There you go.

**Dave Jones:** Excellent. So if you have questions, you can ask them. It won't be live, but we'll pull some questions on the stream. Otherwise, we're just going to do our usual thing and just BS the whole time. We're fine with that too.

**Yankee:** Yep. That's good. Oh, I just realized that when the comments, cause we're using StreamYard for those who don't yet know, and that pulls in all the comments from all the different platforms. So we're running on our Amp Hour YouTube channel and the EEVBlog2 channel as well. And I just realized that the comments for both of those just show up as just show up as the one thing. We don't know whether it's coming from EEVBlog2 or the Amp Hour.

**Dave Jones:** Yeah. Yeah.

**Yankee:** 3.55K subscribers on our Amp Hour channel. Why isn't it 5.55K? Well, you know, it's very...

**Dave Jones:** We've only started doing video recently, so that's why I think. We'll see. Yeah.

**Yankee:** Can we start with, what is your first memory of the 555 timer?

**Dave Jones:** Hmm. Well, for me, it's not going to be much. Oh, you're asking the people. Yeah. For me, it's like, you know, like, I mean, so there was the 555 contest. That was a lot of fun back in the day. When was that? That was, I think, 2011.

**Yankee:** Oh, 2011. Jeez. Okay. 10 years ago. Yep. Wow.

**Dave Jones:** Yeah.

**Yankee:** Yeah. That was our first year, right? When we were all excited about the podcast and doing everything. We were doing all sorts of shit.

**Dave Jones:** I mean, the internet was kind of different then, too. Yeah, it was. Like, social media wasn't quite as big. Yeah. And, you know, blogs were still a thing at that point. Yeah, right. You remember blogs. Text blogs. I was, yeah.

**Yankee:** I was doing text blogs.

**Dave Jones:** Yeah, exactly. So, yeah, I mean, that was a lot of fun, though. And some of that stuff's still online. You can still see some of it. You know, the winner, I remember, was a lot of, like, servo action stuff there. And so that was kind of how I got interested in it.

**Yankee:** There we go. Brad, we can put up comments as well. Brad's Guitar Garage. He first learned about the 555 from the Tricky Dick kits. I didn't do the Tricky Dick kits because there wasn't a Tricky Dick store near me. I had to, like, hop on a bus or a train to go to the nearest Tricky Dick store. And so my thing was Tandy. So I had the Tandy kits. I had the Tandy 50-1.

**Dave Jones:** Is that, like, the budget version?

**Yankee:** No, no, no. They were just different things.

**Dave Jones:** Tandy was the Radio Shack of Australia, right?

**Yankee:** Radio Shack, yes. That's right, yeah. That's it. And we started out as Tandy Leather. A lot of people don't know that. Tandy Leather Corporation. It was, yeah, they were in that business. Leather goods, apparently.

**Dave Jones:** That happens a lot of times, though. You know, you look at, like, Japanese corporations that are around for, like, 150 years. Like, what was Toyota to start with? You know, like, that sort of thing. They just, like, if corporations are around long enough, they're going to have a lot of divisions. So leather first, I guess.

**Yankee:** We've got Superhouse TVs in the house.

**Dave Jones:** Yeah, welcome, John. Former guest of the show, John Oxer.

**Yankee:** Absolutely.

**Dave Jones:** Yeah.

**Yankee:** And someone who wants to donate $5.55 per mention to charity. Yes, please. Yes, please. We don't need the money, do we, Chris?

**Dave Jones:** We do not.

**Yankee:** No, no. We've got to, yep. Our patrons provide the money for microphones and stuff to send out and all the miscellaneous costs and stuff.

**Dave Jones:** Yep.

**Yankee:** Yep.

**Dave Jones:** So NE555 on YouTube also mentioned the Forrest Mims book. Forrest was a guest on the show back in the days. You can go back and listen to him as well. That may have been my actual first exposure to it as well. Right. You know, just kind of reading through it and, yeah.

**Yankee:** Yep.

**Dave Jones:** Longtime listeners of the show know I was not a big hobbyist like Dave was.

**Yankee:** I can show you a relic from the archives, which I got from my bunker this morning and I found it. I found it. I believe, I think this is my first memory of the 555 timer. I'm not like, this one rings a bell anyway. So what it is, can we show that full screen, Chris?

**Dave Jones:** Yep. Hold on.

**Yankee:** Yep. 99. It's a bit how you do it. That's pretty good. Yeah. 99 IC projects. I still got it. I still got it. 99 IC projects. It's from 1982.

**Dave Jones:** Uh-huh. So, yeah. With a markup on it. Look at that. $2.80. $2.80.

**Yankee:** I did not get this because, once again, I could only get what my local news agent and my local Tandy store had. My local news agent didn't have the electronics. Well, it had Electronics Australia and whatnot, but it didn't have like the special purpose magazines from this. So I actually got this from my cousin at the time, which is the only person in the world I knew who actually did, like, who actually owned a multimeter. Right? And he actually gave me my first digital multimeter. Huh. And I can remember, I can still remember to this day, it was project number 99, which is the first one I looked at. I have a bizarre long-term memory. And project 99, there it is. There it is. Because, like, I jumped straight to the end. I jumped straight to the end. Smart porch light. There it is.

**Dave Jones:** Screenshot now, folks. Screenshot now.

**Yankee:** And I can remember thinking, what is this magical chip? Oh, this looks so advanced. You know, I wasn't that old. Right? And, yeah, I can remember thinking, oh, that's the Dark Scouts. Right? This must be so advanced. And the 555.

**Dave Jones:** I mean, that was your first project and you were pulling right off Transformers? Is that right? You were just going straight off mains?

**Yankee:** It was like, well, I had the odd experience with mains. Let's put it that way. But, yeah, and then there were others. And then I realized, oh, this one has three of them. This one's got three. This is just. And then I, of course, discovered the 558, right? The quad timer. Yeah. 555 sequential timer. And, yeah, I thought this was absolutely. And I didn't know what the diodes in there did and stuff like that. It was like, yeah, it was. So that was, I believe, that was the first time I ever saw a 555. Because my Tandy kits didn't have a 555 in it. So.

**Dave Jones:** Yeah. So you're saying that was basically like, I believe Max is inferring here is that this was the first. This is Dave's smart doorbell. Smart doorbell.

**Yankee:** I don't know. I know.

**Dave Jones:** It was actually IoT because it was actually, the way he hooked it up, it ended up being like a spark app generator. It flickered the lights in the house. And, you know.

**Yankee:** I can remember that I installed a pressure sensor when I was a kid. I installed a pressure sensor at the doorway to my lab, which was my bedroom. Right. And it was set off an alarm anytime somebody.

**Dave Jones:** Yeah. Classic. Classic.

**Yankee:** Anytime somebody entered my lab. Yep. So that's the, yeah, that was cool. 1980. Yes. 1982. Wow. Could have 1984 at the moment, but anyway. Yeah. Yeah. Maplin. Maplin. Wow. That's European. Okay. To all our European viewers, Maplin. I don't think you guys had Maplin in the US, did you? Pretty sure it's a European thing.

**Dave Jones:** If it was, maybe it was around before I was. Some of these years we're talking about is before I was. Right. Just so we're clear.

**Yankee:** I can remember picking up a Maplin thing from the, the news agent eventually did start carrying like the odd thing, but, but you had to go in there every day, like, well, every week, at least you had to go in there to try and find the new stuff. Like, you know, there was no internet. There was no other way to find out about stuff.

**Dave Jones:** The news agent was the internet.

**Yankee:** The news agent, you had to go into the news agent and you'd go.

**Dave Jones:** He was the packet router as in he brought you packets of magazines.

**Yankee:** Yep. And of course the talking electronics magazine, which I've done the interview with Colin Mitchell, who's the founder of talking electronics magazine. And that one famously didn't have a schedule. So it didn't come out every month. So you had to go into the news agent and just, is it there? Is it there? When it was like, oh man, when it was there, that was like, oh, it's been three months shit. And then suddenly appear, magically appears. Hallelujah. And, uh, oh, Maplin. Whoa, was Mike. Mike's in the house. Maplin was former guest several times. Maplin was UK only. Right. Okay. I thought it was a bit broader than that, but there you go. Maplin shop, Maplin shops. Yes. Cause you could buy all your gear from Maplin mail order. That's, that was right. Good question. What was the first device you made designed that used a triple five that you were paid for? Oh, goodness. Goodness.

**Dave Jones:** Oh, I remember recommending one. Yeah. For something. Recommend. And Paul Reiko. Paul Reiko from, uh, EDN started like cussing me out for being, I think it was Paul. And, uh, he's just saying, why, why are you doing this, uh, with a five, five, five? You know, like, uh, don't use that. Use, uh, some other timer chip that he was recommending. I don't know.

**Yankee:** Oh, no, bugger off. No, triple five all the way. I can remember that I used it in this, this was a paid gig by my, my, my cousin, not the same one. He gave me the magazine. Another one. He was a tow truck driver and he wanted a, uh, and he, and he wanted a, a doodad box that converted, uh, 24 volts down to, cause that was what was used on the truck or whatever, down to 12 volt converter multi-channel that would drive all the lights. And he gave me the custom connectors. It was like a trailer adapter or whatever, you know, so multi-channel 24 volts into multi output, and then it had to flash, um, some lights as well. So I used a triple five in that to flash one of the, like it had a, a mode on it that you could switch in a triple five timer. So I use that. That was, that was my first paid gig. I don't know. I was maybe 13 something, 12, 13, something like that, you know? So, yep, that was a pay. I think he gave, I think it was like, oh, I was dumb back then. I didn't think about making a profit from this. I just like charged in parts or whatever. And he said, you know, it cost me like 30 bucks in parts or something. And he, you know, and he said, I'll give us, you know, 30 or 35 bucks. I know. Exactly. I was just happy to do it. You know, I was thrilled that somebody gave me a job to do. Yeah.

**Yankee:** Yeah. And he said, nah, he's, he's 50 or whatever, or a hundred, even a hundred. I can't remember what it was. And I went, oh shit, you can make money. You can make money from doing electronics. Holy crap. So excellent question. Thank you. W4 World by web. Raker. Oh, Tony Rob's here as well. Everyone's here. Everyone's here. Yeah. Do I know, do we know any books with just triple five timer circuits? Obviously I've shown one that had, I don't, yes, there's a triple five cookbook.

**Dave Jones:** Yeah. That's not the men's one.

**Yankee:** I'm sure there's a, because they were big back in the day before the internet, you had cookbooks, which had all like building block. Yeah. There's an IC timer cookbook. First edition. Walter Jung. Walter Jung. Is he from LT?

**Dave Jones:** Analog devices. I believe.

**Yankee:** Analog devices. Analog devices. That's it. Yeah. IC timer cookbook. Yeah. Walter G. Jung. Let's get a date on that. Howard W. Sams. 1978.

**Dave Jones:** Yeah.

**Yankee:** And it was copyright 1977. Yeah. There you go.

**Dave Jones:** Yeah. I mean, people might know Walt too from the Op Amp Applications Handbook. That's one that we've definitely talked about on here before. Oh yeah.

**Yankee:** That's great. I've got the printed version of that. You can, I think you can just download it as a PDF. Can you?

**Dave Jones:** I think so. Yeah. Yeah. Yeah.

**Yankee:** I think so. It's great. It's great. Yeah.

**Dave Jones:** There's another book from ADI.

**Yankee:** I think I went to see him live as well. I think he toured here. Oh yeah. And that's where I got it from. I went to one of his lectures. Or is it the other Walter? There's two Walters. There's two Walters at AD and they both write applications books. And I think, yeah, I might be mixing them up. So.

**Dave Jones:** Okay. Yeah. Did you see that analog devices, Maxim is now officially analog devices. We're down another one, Dave. We've lost another chip company.

**Yankee:** Is that latest breaking news?

**Dave Jones:** It's not breaking. No, I mean, this has been in the thing for a while.

**Yankee:** Oh, right. Maybe we covered it or something, did we?

**Dave Jones:** I'm sure we have, but it's, it like is official though. So it's like, so like. It's too big.

**Yankee:** Yeah. No, that's scary, isn't it? Yeah. Big brother is watching. Nah, let's go.

**Dave Jones:** I think what we'll start seeing is the same kind of thing. Like how linear's just kind of been disappearing, you know, just slowly, but surely just kind of no longer linear tech. It's all just analog devices. Everything's analog.

**Yankee:** I've got to throw in the joke. You couldn't buy Maxim anyway. So it's not a loss. Yeah. Right. Right. Right. 1990s jokes. Sorry for those who don't get it. It was, yeah. Maxim were famous. Did, yeah, this was probably before your time again, Chris. Did you get the Maxim data books? Like they used to release like six monthly data books of new chips actually released in the last six months. And the six monthly release books were this thick, right? Just the chips they released in the six months or whatever. And it was like, and that lasted for like four years or something before they finally just went, no, we're just producing too many freaking chip variants. And they were like, you know, everyone was amazed at all these chips that Maxim were pouring out. You know, you had their one for every task, but you couldn't get them. You can get great samples. They're the best sample service in the business, but geez, you know. Ti make a CMOS 555 in a 1.4 BGA. I wonder who uses these. I don't know, because they probably cost a ton more than an SO8, than a generic jelly bean SO8, right?

**Dave Jones:** I just saw Jeremy Hong, who's been on the show at one of the camp shows that I did, like one of the ones where I was remote. Yep. So Jeremy, he just posted a photo of him. There's like a blinky challenge for like 0201s or smaller, maybe 01005s and the BGA chip. And so it's like getting to blinky, but with ultra tiny parts. Right. Yeah, yeah. It's intense. Yeah, yeah. It's really intense.

**Yankee:** You're not allowed to enter unless you own a microscope, you know. Yeah. It's like, yeah. Although back when I was a boy, before I had these things, these are only fairly recent, the glasses. Yeah. I could do that sort of thing without a microscope. But now, no, no chance.

**Dave Jones:** We're all getting older folks. We're all getting older.

**Yankee:** David Ramsey was into Maplin IC catalogs. Fanboy. Oh, boy. Just a random technical question here from Little Tear. Why doesn't exist multimeters with rechargeable batteries? Because, because, because I think I've mentioned this in a video where I did a video on why they use 9 volt batteries in multimeters. And it's on my EVBog2 channel, maybe or something.

**Dave Jones:** Well, so are we right now. So.

**Yankee:** Anyway, the reason that they don't do it is our safety and compliance requirements. Because if you have a rechargeable battery in there, you need to recharge it somehow, right? Which means that you might recharge it via like a USB port or something like that. And if you do that, well, you've broken the case isolation. You've got an external metal part. And then that needs to be safely, that needs to be galvanically isolated from the ground terminal on the multimeter. Otherwise, it won't be able to pass the, pass the various requirements for safety that multimeters have to meet. Or they don't have to if you've got a, you know, Chinese thing that doesn't meet any requirements at all. And you just buy, you know, it's some no-name brand thing. You know, you don't have to. You can sell a multimeter. There's nothing illegal about selling a multimeter that doesn't meet various CAT specs or whatever. Yeah, if it does, and then you send it to a reputable agency to have it verified, then it won't pass. Because it has to meet these. Tektronix, back in the old day, they don't sell it anymore. But Tektronix did a rechargeable multimeter because it had an OLED display on it. And it chewed through the batteries in like nine hours or something. It was horrible, right? It was a great multimeter, super fast. I did a review on it way back in 2009. And the way it recharged its battery is that it used the actual jacks itself. So it repurposed the jacks to, so you put, I think it was into the amps jack or something. So if you put, so if you fed the charger into the amps jack, it had reverse charged the battery. It was, it was neat, right? But that's the only way that way that they could do it. So that's why multimeters don't have rechargeable batteries. You can do it, but it's like.

**Dave Jones:** I feel like the other thing is the, is the pricing, right? So a lot of the multimeters are not set up for pricing. Yeah, pricing as well. You know, at that point, why not just pop the back open and do that sort of thing?

**Yankee:** No, and if you go, if you want the USB port to recharge it, then you've got to have the isolated DC to DC converter. That increases your bomb cost no end. And, you know, it's just, it just gets really messy.

**Dave Jones:** Yeah, I mean, because these days you could just as easily, you could do like, you know, Qi charging or some kind of inductive charging, right? On a pad. But why do that?

**Yankee:** Yeah, yeah. Yes, yes, you could. You, you would have to do an inductive charging. I thought about doing that as a video. I thought about actually getting a multimeter and turn it into a rechargeable multimeter by having a Qi charging coil in it. I don't know.

**Dave Jones:** You should probably make like a ultrasound base beam forming kind of thing and find it anywhere. Maybe for, maybe for sometime in April. Geez, you could do that. Maybe sometime in April.

**Yankee:** Geez, you could get seed funding for that. And you can get, you know, you can get 20 million bucks from Mark Cuban.

**Dave Jones:** We're doing all the hits here today, folks. We're doing all the hits.

**Yankee:** You beam. I'm just waiting for the chip printer to come up. Somebody hasn't trolled us in the comments yet. Why not? Why not?

**Dave Jones:** Actually, on the, on the subject of, oh, oh, I was thinking about the, the Qi charging idea, actually. And just thinking about like why you wouldn't even have that as well. Oh, there you go. Good. Yep. Yeah. The Qi charging and why. Yeah. I mean, just thinking about like, like noise variability too. Oh, that's what it was. I was thinking about like a nine volts versus like a, you know, like just doing a single or double cell. Like why not just do that? But then you have the possibility of, you know, you might need to boost it up and then you're. You do. You have that, that potential, potential of noise kind of seeping in. So.

**Yankee:** Yes. And something like the diode test range. If you only power it with two AAA or AA cells or whatever, then you've only got three volts max terminal voltage. And unless you boost that, you know, your, your low voltage is going to be like 2.1 volts or something like that, where it cuts out. And that's where you, like, you can't even turn on leads. Right. And that's your maximum diode test voltage. And, and then you don't get the full capacity of the batteries. And that's why a lot of batteries, that's why a lot of multi use, multi meters use three cells because it gives you, you know, the four and a half volts, which then drops out at like three volts. And you're at least getting down to one volt per cell using most of the capacity whilst still giving you the diode test range and other things required, the operational voltage required. So yeah. Yeah. Big trade-off.

**Dave Jones:** On the, on the noise thing for rails today, I was, I was finishing up a design and at the last minute I had like a ground pour, it was just a two layer board, but I had a ground pour kind of everywhere for a three volt rail that I was working on. And I, I decided to just rip it out. It didn't seem like a good idea. I don't know if you have any thoughts on ground pour or starting at ground pours, power plane pours or not on a, on a two layer board. So I ended up just routing the three, the three volt rail.

**Yankee:** You do it just because I don't like wasting copper, you know, like I don't like having the copper edge off, you know, it's like, I don't know, there's something offensive about it. It's got to fall out.

**Dave Jones:** It's got to fall out in the solution, right? Yeah.

**Speaker ?:** Yeah.

**Yankee:** Like, you know, I've made giant boards like this and like, I went for various reasons, didn't have a ground plane on it or whatever. And you realize that there's only a few, you know, like the actual area of the thin traces on there is nothing. So like 99% of the copper is being itched away and it's just, I don't know, something offensive about that. I just don't like it.

**Dave Jones:** Not a fan. Not a fan. Yeah.

**Yankee:** Very environmentally unfriendly and I'm a bit of an environmentalist. I just find it, you know.

**Dave Jones:** Oh yeah. Yeah. You know, like we're etching PCBs that are thrown out eventually, but we're environmentalists. Right.

**Yankee:** Exactly. Yeah. Screw it if it gets in, in the way of our hobby. Right. Right. Yep. I draw the line. Yeah. If it gets in the way, no. Oh, what we need is a gold plated NE555 special edition. Would you, I would, hell yes. I would buy that. Oh, oh, you know, I've talked about this before. I've been thinking about minting an EEV blog coin, like an actual real coin, you know, with a Dave head on it just for kicks and it's, you know, one dollary do or something, you know, like just like, it'd be silver. Of course, if you minted like a gold one, it'd be like 2000 bucks worth, you know, it'd be quite expensive. But yeah. Anyway, gold plated. I don't know. Yeah. You could have a, like a solid, I'm thinking like of a solid gold cast triple five timer chip. That'd be so cool. You could certainly do it.

**Dave Jones:** It's possible. Or you could buy a normal one and just spray paint it.

**Yankee:** Yeah.

**Dave Jones:** Yeah.

**Yankee:** Well, no, no, you could actually, no, you can't do real gold plating. You know, you can't just, no, no, no, no, no, no.

**Dave Jones:** There's nothing to throw around like that. I bought a house.

**Yankee:** Yeah. Right. Right. Yep. Challenge coin. Yes. I said, that's a very Yankee thing. The challenge coin. It's a Yankee.

**Dave Jones:** Yeah. It's a military tradition.

**Yankee:** Yeah. Yeah. It's a military tradition. Yeah.

**Dave Jones:** Yeah. It's weird. The security industry kind of adopted that too. I think it's mostly because of the, uh, the drinking culture aspect of it. Okay. Yeah. Do you know how that goes or no?

**Yankee:** Yeah. Yeah. You spoke. Yes. If you're at a pub, is it, what's it called over there in the, in Yankee land? It's a pub here. Is it a bar? Yeah. A bar. Bar. Yeah. So, so if you're at a bar in the U S and, uh, and somebody wax down their challenge coin, they don't have to pay for their drinks or something. Or no, if you can't present your coin, if somebody lays down the coin and you can't present yours, you, you have to pay for their beer. So that's. Among other things. It's not just. Among other things. Yeah.

**Dave Jones:** But that is one popular use case. And that's why I think the security industry got into that. Yes.

**Yankee:** Mikey, Mikey's very right. Yes. They do in for very high volumes. They not on the prototype. Most people don't do high volume stuff. So they'll never know little tidbits like this, that yes, high volumes, they will charge more for less copper because they have to etch it away. And it takes longer in the process as well.

**Dave Jones:** Sure.

**Yankee:** And, and they have to go through their vault. You know, it's, it's not like they don't.

**Dave Jones:** They got a spreadsheet somewhere, right? Yes.

**Yankee:** And yeah, they've got to refill their chemical etchant every time it gets saturated with the copper. Like you can't just, like, it doesn't just magically last forever. They've got to refresh their copper. You know, once it's saturated with X amount of copper in there, they've got to, yeah, they've got to refresh it and that costs money. You know, shock, horror, chemicals. But you don't know that if you're small to medium volume. But yeah, on the high volume stuff, absolutely. That's why single sided boards are still a thing, right? Single, you open any modern TV. See, or any modern consumer appliance, single sided PCB for the power supply, because it's cheaper. It's like they save 10 cents or something on the board. It's cheaper. So, yep. You betcha. Actually, it's probably even more than 10 cents. You know, it's like probably a dollar or something. You know, if you can save that cost. Yeah. Why not? We should have a fab run an EV log chip. Well, you can do that nowadays. Can't you? There's that's right. Yeah.

**Dave Jones:** The program. Yeah. Mad Ven is running a class and they'll teach you how to do it. And then I think they're doing a run. There's the Google shuttle run thing. There's the we had Mohammed Kasaman from eFabless and they're working with open lane. I mean, I should get some of these things. So, yeah, there is there are many, many more opportunities to do chips these days than there had been. And there's also classes on top of it. So if you're interested in that stuff, definitely check out Mad Ven's class. It's supposed to be really great. So go check that out.

**Yankee:** Yep. I don't know about how they recover or what they do with that copper. Yeah. Because copper is worth money. Right.

**Dave Jones:** Sure. I think it's got a fall out of solution or something. Right.

**Yankee:** Yeah. I'm sure you can. Yep. Something happens. Right. I don't know if anyone knows. Magic happens. If anyone actually works in a PCB fab. We have, we now have an actual PCB fab here in Australia. A bare board PCB fab. Because sorry for you, New Zealanders, we always steal your stuff. But Circuit Labs in New Zealand is now in Australia. They got bought out. And as part of the deal, they moved to here. They moved here. So I'm not sure where or whatever, because, you know, it was during the whole COVID things. I don't know what's going on. But yeah. Yeah. Circuit Labs, they've announced that they moved to Australia. So, yeah. Cool. So once all that's up and running, I haven't been notified yet, but I think it's still in process. But, yep. One fab in our entire country that you can get bare boards. But, well, no, technically there's two. But the other one, Lintec, I think. Lintec, they only make like really ultra high end 50 layer boards. Like, you know, you can't go to them. You wouldn't go to them for just, you know, I don't think they won't get out of bed for anything under a thousand bucks. Right. Yeah. So it's like. I feel like a lot of these countries too.

**Dave Jones:** Like, you know, Australia is not alone in having a defense industry. And I think that a lot of countries want to have in-country capabilities so that they can lock down secrets, whatever.

**Yankee:** Yes, they do. That's the only reason Lintec still exists here is the military contracts. Yeah. I guarantee it. Because we used them and they, when I was working on that sort of stuff and yeah, we would pay thousands of dollars for one board. Like that's nothing. Yeah, exactly. That was nothing. Yeah.

**Dave Jones:** And it's going to, it's going to price you out. I mean, if you're like, oh, I'm going to support locally, like it's a great thought, but it's probably from a practical, practical perspective, probably not going to do it. So.

**Yankee:** Yep.

**Dave Jones:** Yeah. Actually the same thing happened with a DOD here. So, uh, they just announced in, uh, the U S the DOD is picked Intel and it's like, all right, well, you had like two or three choices. Yeah, exactly. Maybe it's like Intel or microchip or I think that's about it. Like, what else is making chips in the U S anymore?

**Yankee:** It depends on what, you know, node they want to do. Depends on what.

**Dave Jones:** Yeah, exactly. I think, but you know, they're talking about like leading edge type stuff as well. So it's basically, you know, Intel or TSMC. Those are pretty much your choices. And so, uh, yeah, so that's, uh, those are the choices there.

**Yankee:** Yep. Any chance of doing a Amp Hour with Rod Elliott? Yes, I certainly could.

**Dave Jones:** I don't know who Rod Elliott is. Sorry.

**Yankee:** My audio guru here in Australia. I've done a video interview with him at a trade show and yeah, he's one of the, uh, yep. He's webpage. If you want anything analog, anything audio. Wow. He's, uh, go to Elliott Sound Products. Elliott Sound Products website. Sound AU. Oh, is it, is he changed it? I think he might've, he might've changed it. I'm posting a link. Can we post links here? Yep, we can. There you go. Well, we should be able to because we're the host. So yes. And that has, he, he has like the best in-depth projects. Like just absolutely stunning. And, and audio tutorials and stuff like that. There's just incredible. Absolutely incredible. Yes. Yeah. Rod actually contacted me. Oh, it was actually pre-COVID that, um, yeah, we should probably do something together. And yeah, yeah. I was like going to go over there and interview him like in his, um, in his, like we're maybe going to do like a, maybe a whiteboard thing or something like that, perhaps. Yeah. Something like that. Cause he's here in Sydney somewhere.

**Dave Jones:** Yeah.

**Yankee:** So, yep. Yeah. We can have him on the Amp Hour for sure. I'll tee that one up after this. But yeah, no, it's just crazy. He's got a crazy amount of, uh, projects in there all with like theory of operation and everything. Like, you know, it's not just, oh, here's a schematic and a PCB. No, he like goes in depth on everything. It's just, yeah, absolutely amazing. So yeah. Highly, highly regarded website.

**Dave Jones:** Speaking of in depth and educational stuff, we do have some sad news. Uh, past guest of the show.

**Yankee:** Oh yes.

**Dave Jones:** Henry Ott passed away a couple of days ago. Oh, a while ago rather. Sorry. In May.

**Yankee:** Henry Ott.

**Dave Jones:** Yeah. So someone had found us and posted this on the subreddit. Thank you for that. But, uh, yeah, Henry, uh, Henry. He is a wonderful, uh, EMC expert. And so I definitely recommend people go and check that out. Not only, you know, he's got some stuff on his website that you can go and check out, whatever. We also had an interview with him. And so, yeah, that's sad to hear. I mean.

**Yankee:** It is 36. That puts him at, uh, 86.

**Dave Jones:** Yep.

**Yankee:** Yep. Yep. Yeah. That's a pretty good innings.

**Dave Jones:** Sure. Sure. Yep.

**Yankee:** Well done, Henry. Legend.

**Dave Jones:** Yeah. Total legend. Yep.

**Yankee:** Highly recommend his book.

**Dave Jones:** Yeah. And we were talking about that a little bit last time about like, uh, some signal integrity stuff as well.

**Yankee:** AVE. I'll try and get AVE on the amp hour. What do you think?

**Dave Jones:** I don't think we're going to get any video. We'll just get some hands.

**Yankee:** I don't, yeah. I don't think we'll understand what he's saying either. We'll need a translator on that. Why do so many people prefer the inaccurate reproduction of tubes and colored sound in general? It's the warm fuzzies. People like the warm fuzzies, you know? So, I don't know. If, if that's what you like, fine. Just don't try and sell it as, you know, like absolute perfection. Well, you know, you can sell it as, as what it sounds like, but don't, you know, the, the audio full stuff. The good thing is, is that the tubes and colored stuff, they're like the, the audio files make no, even the audio files don't try and say, well, tubes are the most purest sound. No. You know, even, even they admit that that's bullshit. You know, they go, no, it's got distortion and that's how I like it. And that's, you know, how it should be. Damn it. When you're playing LPs or whatever, you know, that's, yeah, that's fine.

**Dave Jones:** Yeah. We did have, uh, someone was doing a preamp for a phono preamp on here. Uh, I'll look them up, but, uh, but he talked about that cause he was doing, he was doing simulation and basically reproduction using an STM 32 DSP.

**Yankee:** Yeah. All right.

**Dave Jones:** And so, uh, yeah.

**Yankee:** Sacrilege.

**Dave Jones:** Yeah. I mean, that's what the interesting thing is like when you have, now you're selling into a crowd that wants, you know, all these crunchy sounds or whatever is Shannon parks, um, from parks audio. Uh, and so, uh, you know, when you're selling into this, this crowd, it's like you're, you have a bunch of preconceived notions as well. And then it's like, well, when you start to do a side-by-side comparison and maybe you can offer a cheaper, better option, you know, it's, there's room and this is where audio usually falls off for me. I'm just like, oh, okay. That's, that's not for me. I don't think that's going to be a, uh,

**Yankee:** no, I, my audio care factor is pretty low. Although I do take care with what studio monitors I use for the flat, but I want like perfect flatness, you know, and stuff like that. But I know like it should be replaying my videos on, uh, or actually editing my videos on, you know, Yamaha NS 10s or whatever, you know, that sound sort of dodgy. People don't know this, that these are, that these recording studios, right? They, they use Yamaha NS 10 monitors, which have been around since the bloody sixties or something. And these are shit speakers. These are like really these NS 10 speakers. They are like, as far as studio monitors go, they're actually completely and utterly shit. They're not flat. They're like horrible. Like, you know, they have no advanced technology in them to give you a flat response or whatever. But the reason that they use them in all the recording studios around the world is because it's the de facto standard and it's, and it's closer to what like the, like the home user would use. You know, you could have, you know, $50,000 studio monitor speakers, perfectly flat engineered to, you know, for your particular space and studio. So it's absolutely perfect. And if you mix your audio using that, then often it can sound shit on people's earbuds and stuff like that or people's, you know, little boom box or whatever, you know, so, or home stereo. So they often have shittier speakers. The single cone audio tones are one of them. The audio tone make, make, make these little cubes and they're just a single wide range speaker, right? And they're often used in studios as well to give you like a more like down to earth, what this thing will sound like on users gear. And that's what they have to mix for. You can't just use these perfect sounding studio monitors. It doesn't work. Yeah. So yeah. Yep. Yamaha NS 10s. Uh oh. Plus one for Mrs. EV blog and Mrs. Gamble. They want guests on the amp hour. Oh boy.

**Dave Jones:** That's not happening guys.

**Yankee:** Yeah. I don't think that's happening. I don't know. What's Mrs. EV blog going to talk about environmental science. She's an environmental scientist. She could talk all day about, you know, sewage systems, I guess. So we can do an entire episode on sewage or water quality or something. Yep. Yes. The NS 10s originally sold us hi-fi, but they didn't sell well. And then they became the somebody in some studio in the US. I can't remember exactly which one first used them. And then, you know, back in the 60s or something. And then they, you know, when other people came around to the studio, whoa, what speakers are you using? They sound really, you know, you know, smoking their joints as you did in the 60s or whatever. Saying, oh, that sounds trippy. So everyone ended up getting the NS 10s in every studio around the world. So yeah, there you go. All right. Ah, yes. That's the difference between mixing and mastering. Mastering is all about what it will sound like for the end user. Yes. Yes. It's a multi-step process in the studio, apparently. Aura tone. Thank you. Aura tone, not audio tone. I was, yep. Aura tone. The little cube things. You can, like, you can still buy them used for like a thousand bucks or something, you know, because they don't make them anymore. So they're highly sought after. Congrats on the triple five show. Started a learn program in AVR about a month ago. And this newbie and this PCB shaker is my first project. I'm finishing the schematic right now. Excellent. I hope it doesn't work. I genuinely hope it doesn't work and you have to troubleshoot it. Seriously. Seriously. I've done, you know, I'm sure Chris would agree. Would you not, Chris? The best way to learn is to troubleshoot. Yeah. Is when things, if things work first time. Yeah. Okay.

**Dave Jones:** You've learned how to solder and, you know. Let's get some, let's get some guardrails in place though. Right. Okay. Right. Yeah. Before we get abuse and hate mail. I just, well, no, no, no. I actually, I just, I, I treated myself to a, reducing a board spin today. So I had a, I had this case here. Oh yes.

**Yankee:** You mentioned this on Twitter. Yeah.

**Dave Jones:** I tweeted about this. Yeah. So I, I, for some reason the, you know, they get these like, these catch things. They're like, I guess they're like separators. Oh yeah. Yeah.

**Yankee:** No, you, they're put in, uh, PCBs vertically. They're, they're, you'll find that they're 1.6 mil wide. So PCB, that's a standard PCB thickness that fits in vertical. Yeah. Oh, that's great.

**Dave Jones:** That's really good to know. I always wondered. Cause like, yeah, uh, it's actually really frustrating the, um, you know, if you don't find the right files and what you have to do is they just give you like the pure, you know, you can go and get the drawing right for the actual outline. You get the DXF.

**Yankee:** Yep.

**Dave Jones:** And then, uh, and then you have to basically, I take it into like fusion.

**Yankee:** You've got to import it into it. If you use Altium that can, you know, you can import it and it does 3d CAD checking.

**Dave Jones:** Will it actually shrink it? So that's the thing. So it'll, it'll import the outline here, but I don't want the outline. I want a little bit less. I want an offset of that outline. And so that's what I'm usually doing is I'm taking it down by a millimeter or so. Oh, okay.

**Yankee:** You shrink it. Okay. No, you don't want to definitely fit. Right. Okay. No, I don't. Somebody in the comments, please let us know. I don't know. Maybe the Latium at latest Altium might have this, but I doubt it. Is that yes. Bring in that and say, right. It would be nice to just have like a macro. There should be a board fit option and it, and it just cuts it down by half a millimeter. Yeah.

**Dave Jones:** Half a millimeter or a millimeter. Like I do a millimeter just to really be sure, but like, yeah.

**Yankee:** That's a great feature. Yeah.

**Dave Jones:** Yeah. I do that in fusion, but then there's, you know, always some weirdness there and you get to re-export it, whatever. It looks like Mike's saying that some of, uh, Hammond's data sheets re-export. You know, these days, especially for this case, I, uh, this one, I don't know. I forget who's making this thing. Bund? Bud. Bud Industries. Uh, you can buy this on a, uh, on Amazon too. So like I found it on like four different distributor sites and Amazon. And Amazon. Can you tell I've been burned much recently, Dave? Can you tell that I'm feeling the pain of the shortage? Uh, so yeah. Yeah. So, and yeah, so Wiley's asking about the offset. That is what I did here. So if you're using a DXF for the outline, you could import it to another CAD tool and offset it. That is what I did. So I imported it into fusion. I don't use, I don't use fusion electronics. I use KiCAD. People that are new here, I guess, wouldn't know that. But, uh, um, so then I re-exported it.

**Yankee:** Ted obsessed with key CAD. Yeah. Key CAD, not KiCAD. Key CAD.

**Dave Jones:** Yeah.

**Yankee:** Yeah. So yeah. Your new house has noise problems, Chris. It does. Yeah.

**Dave Jones:** We've got a couple of, you know what it really is. It's just, you're not used to the, you don't hear all of the noise that used to be at the old place. And now like anything that comes through, it's like, oh, what's that? You know?

**Yankee:** You need some sound. Is that because the window's open or is that just coming through the walls?

**Dave Jones:** And that's just, yeah. You know, it's just not a condo building anymore. I used to be like up on a top floor of the condo. So now it's, I'm right at, right at the loud, loud butt heads, uh, level.

**Yankee:** Yeah. But you're in the middle of suburbia though. You know?

**Dave Jones:** Some loud butt heads drive through suburbia pretty fast.

**Yankee:** With their F-150 pickup, right? And their gun rack on the back.

**Dave Jones:** It's actually the same guy. And I think it's actually a Camaro, you know, like the Camaro type. Okay. Yeah.

**Yankee:** Someone lives on your street. Okay.

**Dave Jones:** Mm-hmm. Yeah. Speaking of cars, my buddy bought a Chevy Bolt, uh, not a Volt.

**Yankee:** Oh, the recall. The recall. Well, he doesn't own it anymore. It's been recalled.

**Dave Jones:** Well, he does though. I mean, that's not a...

**Yankee:** Well, he's got to send it back. Yeah.

**Dave Jones:** Yeah. Well, you know, you really recall in that case is just a, uh, I think it's a take it in. You know, it's like a free service kind of thing. Yeah.

**Yankee:** Yeah. Yeah.

**Dave Jones:** It's not like a, it's not like a trade-in for a new car thing.

**Yankee:** No. So are they swapping the whole pack or is it some sort of sell?

**Dave Jones:** I think it's a whole pack.

**Yankee:** It's a whole pack. I think so. Yeah. That's what I believe.

**Dave Jones:** I didn't get all the details. So yeah.

**Yankee:** Yep. That's what's going to happen to mine. I'm waiting for the, uh, recall notice. I do believe all the Ioniq cars sold here and around the world. I think all of them around the world have been recalled as well.

**Dave Jones:** Do you think that car manufacturers have like insurance for this sort of thing? Like I carry insurance for like, if I make a mistake as a design engineer, it's been

**Yankee:** paid for by LG. Oh really? LG is paying for it or 70% of it or something. Wow. I think in the case of the high Hyundai recall, I think LG are paying 70% or something of the recall cost.

**Dave Jones:** Because it's the battery specifically. It's not like a charging circuit.

**Yankee:** It's, it's the battery. No, no, no. It's not the charging circuit. It's, it's, it's the cells, but like, there's only like eight of them. Around the world that have actually caught on fire, but still like, you know, a lot of people like to make the claim that, oh, petrol, more petrol cars catch on fire. Yeah. But they're usually the old ones. They're almost always the old ones. I know there is a recent case where, is it Ford? Oh, somebody knew some new car, some model of new car, ice car, internal combustion engine car is actually blowing up, is actually catching on fire at a similar rate to EVs or something. But yeah, that's the thing with EVs. This is happening to new cars, like brand new cars, just sitting there doing nothing. You know, whereas the internal combustion engine cars, usually it's not going to catch on fire if it's just sitting there, right? Doing nothing. It's just sitting in your garage, right? Yeah. You know, that's why they catch on fire on the road or whatever. That's how it usually happens. So, and then they're usually old cars that it happens to. So it's not an equivalent thing. So I hate seeing that comparison. I really do. I think it is more of a problem with EVs. You know, when you've got that much energy density, these things, you know, people think, oh, we can, you know, battery technology will magically increase the capacity of batteries tenfold. Hello, McFly. Well, A, that would have more energy density than TNT, I think. Like seriously, like where the current lithium battery technology is on the edge of being an explosive. Like there's so much energy in per square unit volume that you can't just increase it ten times. It's just, it's not going to happen. Right? So you need to change the entire technology to make it non-exothermic or non, but still the energy's in X square volume. I mean, it's, it's, it's going to continue to be a problem. So unfortunately, yes, you cannot beat the laws of physics, Captain. Energy density per square meter.

**Dave Jones:** Right, right. Well, I mean, gasoline is very dense, but it's also not as, it's very well understood now, I think as well. I think that's another thing.

**Yankee:** Yes, it's very well. Yeah. Yeah. Yeah. And it's easier to handle and contain a physical liquid than it is to, you know, batteries are complex. The manufacturing batteries is complex. And if any small thing goes wrong, you know, you've got X amount of square area to go wrong in a cell. Because if you have a puncture through or whatever, you know, if you have some manufacturing defect or whatever, then, you know, yep. It's a big problem. I think the Tesla battery fire in Melbourne is out. Well, I assume it is. I assume it's out. I've done a video on that. Oh, I hadn't heard about that. Yeah. You didn't hear about that?

**Dave Jones:** No.

**Yankee:** Oh, I've done a video on it. The Tesla Morable fire. It's one of Tesla's, it's a big farm. It's a giant Tesla battery farm. The biggest in the Southern Hemisphere. It caught on fire.

**Dave Jones:** This isn't the one that was meant to like supplant or supplement the grid, was it?

**Yankee:** Yes. Yes.

**Dave Jones:** Oh. That sat on fire. I remember when that went out. I remember when they were like so proud of themselves for like spinning up this thing that like. Yeah.

**Yankee:** Yeah.

**Dave Jones:** When they couldn't fix the power for a while.

**Yankee:** Well, they, they did. This is the second giant one here. This is the, the first one's still working fine. It's paid for itself and it's doing great. But the second one they installed here, which is even bigger. Yeah. Caught on fire. Oops.

**Dave Jones:** Yeah. Yep.

**Yankee:** Yep. And they had just started, they had just turned it on and started charging it. It was like four hours after they started charging it and it caught on fire. So, oops. Yep.

**Dave Jones:** Yeah.

**Yankee:** Someone's going to pay for that.

**Dave Jones:** So Simon asked if we've watched physics girls, a hydrogen series. I love physics girls channel. She has a fantastic channel. I haven't, I have not gotten to the hydrogen series yet. I've seen.

**Yankee:** I've, I've seen parts of her video on the hydrogen series. I think some people are criticizing her for that because it's sponsored. I think, you know, cause they like, or whatever. I think, I think don't quote me, but yeah, they like, she spent like a week driving around the country in this hydrogen car, which they, you know, gave it to use.

**Dave Jones:** So I don't really understand the logistics of it all because it's like.

**Yankee:** Oh no, it's, it's never going to work. I did it. Like, this is another prediction. I'm sure I've made on the amp hour before, and I'm sure I'll be correct. Hydrogen cars will not be a thing. Okay. They just know there's nothing going for it. It might work in some niche for trucks or something, maybe, but no, it won't work mainstream because it doesn't solve anything, right? If you have to go to the gas station for you Yanks, right? Petrol. Petrol station here. Petrol. If you, or servo, if you have to go to the servo to fill up your hydrogen powered car, what's the, what's the advantage? The advantage of, as an EV owner, I can tell you what the advantage of EVs is. I never have to go anywhere to charge it. I come home at the end of the day and I just plug it into the power, the trickle charge PowerPoint and it recharges overnight during, you know, and, and covers, unless you're like a traveling salesperson and you're doing 500 miles a day or something, then it'd be different.

**Dave Jones:** But the, the downside of that is the, uh, the, I think people like immediately jump to the, to the long haul type stuff, right. And, and the logistics of that.

**Yankee:** Oh yeah, they, they immediately criticize that. And then they immediately say, well, I live in a unit and I can't, I don't even have a car space. Well, okay. Well, EVs currently aren't a thing for you then currently, right. Unless the infrastructure is in place, but like hydrogen. Yes, they are talking about this and they have trialed them. These hydrogen storage tanks at home, right. But really, do you want to have a hydrogen storage tank strapped to the side of your house and then have the hydrogen man come around every week and re and re for every month and refill your hydrogen tank on the side of your house from the big hydrogen tanker trunk? Bullshit. Right. It's like, oh no, you can actually produce it, but then you, you know how much energy you need to actually produce hydrogen.

**Dave Jones:** It's like, yeah, I feel like the storage is still the big part there is to like, you know, you need to like super cool storage to.

**Yankee:** Cold story. It's like, and a super high pressure storage. It's like, come on. No, it's not going to be a thing. EVs, everyone, like everyone who has a house has the ability and to park their car in their house has the ability to charge their car up without any new infrastructure. Plug it into the PowerPoint. No, there's just no contest. It's not going to, I can safely say hydrogen powered cars are going to be a complete and epic failure.

**Dave Jones:** Yeah. I mean, well, they've been talking about fuel cells for a while already. So yeah.

**Yankee:** Yeah. It's, it's not going to happen. Another day of prediction.

**Dave Jones:** I can tell you this. My next car is an EV and, uh, you know, I am not an early adopter.

**Dave Jones:** Right. Yeah. I have a garage now.

**Yankee:** I should have got one a long time ago, but you know, but then I ended up getting one for almost free. The government paid for it. You know.

**Dave Jones:** There you go.

**Yankee:** Well, government, me, the taxpayer paid for it. Yeah.

**Dave Jones:** So it's a loop back. It's a loop back. Yeah.

**Yankee:** Oh, someone says propane or winter bunker fuel deliveries are kind of used to it.

**Dave Jones:** Yeah, that's true. I mean, like there is infrastructure. So like, you know, I, I used to have family that was living out in the boonies and, you know, yes, you don't, you don't have natural gas being piped to your house and electricity is still super expensive for as a heating solution. And so you'd have propane being delivered by truck and then you have like just a tank sitting outside. However, those tanks were mostly inert. I mean, they're just big metal tanks and you're just like, you turn on the valve and it comes in the house and whatever. There's no like, I mean, maybe there's monitoring for flow rate, but it's not like there's nothing fancy about that. Whereas I imagine hydrogen there would.

**Speaker ?:** Yeah.

**Dave Jones:** Yeah. Especially like, like, and that again, that's in the country, right? There's like setback requirements too of like, oh, your, your tank is not going to be right next to your house. It's not attached to your house. If you really want to be making like changes like this, you know, you'd start to have like, like on the side of the house, you know, I think about the density of Dave's neighborhood and it's like, you're not just blowing up your house anymore. You're blowing up your neighbor's house. Yeah. Yeah. Yeah. So, uh, yeah. Energy.

**Yankee:** No, that's why I'm actually, you know, I'm considering home storage, right? I'm just trying to work out the numbers and stuff like that. I'm actually considering not to use lithium ion storage because it's exothermic, right? I don't like, and like, you know, having the idea of having this strapped to the side of my house or inside the house or whatever is like, you know, I know the odds of it happening, but the fact that it can happen kind of like goes, well, no, why don't I use like a flow battery? Why don't I choose like a flow battery or some other technology that's not going to blow up, you know, that's not going to catch on fire and burn down my house, you know? That's good. But then again, I've already got the EV in my garage. So if that catches on fire, you know, it's the fire alarms going off, right?

**Dave Jones:** I guess the first thing is to have a really good connected, connected fire alarm or something, right? Or just a, do you have a connected smoke alarm?

**Yankee:** We don't have a connected fire alarm. No, we've got independent alarm, you know, just like, yeah. Standalone. Standalone type. Yep. BPB. Yep. Yeah. Yep. So we do have one in the garage, so that'll go off. And I'd like to think if in the middle of the night, the fire alarm in the garage went off, we'd probably hear it. Or at least she would hear it. I probably wouldn't, but you know.

**Dave Jones:** A past guest of the show, I won't say who it was, but a past guest of the show had doorbell footage. He had like a Nest camera. Oh, yeah, right. On his doorbell. And he has footage of his, the batteries he was charging in his garage burned down his entire garage. He had internal, he had internal footage and he had external footage and you just saw the whole thing about. Oh, yeah. It's rough. Yep. It's rough. Yep.

**Yankee:** You know, it's, you know, it's.

**Dave Jones:** But it's also, it was also safe, right? I mean, like that was the other thing. Like, so he had this footage and also, you know, like he was, his family was safe, all that was important. So, yeah.

**Yankee:** Yes. Lifepo. Living. Polymer.

**Dave Jones:** Lifepo. Lifepo. Yes.

**Yankee:** Yeah. You can get those for home storage as well. And the, yes, they are not exothermic. So I do believe they are safer. Yep.

**Dave Jones:** Yeah.

**Yankee:** Yep. There's an Australian company that does flow batteries though. So I don't know. I might.

**Dave Jones:** What is a flow battery? I don't know what that is.

**Yankee:** A flow battery is a chemical. It's like a pumped chemical system, hence flow. You've got to have a flow of chemicals. Oh my God. I can't remember the exact chemicals now, but anyway.

**Dave Jones:** I hear chemicals are bad and I shouldn't eat them or be around them. So if you could just make me feel safer about chemicals.

**Yankee:** All right.

**Dave Jones:** There's chemicals in my water.

**Yankee:** I don't think they're, no, I don't think they're acidic or anything. I think if they actually leaked out, it's not. They're not solid state.

**Dave Jones:** They're not sodium or anything crazy like that. It's probably like a wet cell. Yeah.

**Yankee:** Yeah. Red flow zinc bromide. I thought it was bromide. I knew that. I like, and I thought, no, well, is it? Yeah. Actually bromide's a fire retardant. So bromide is a chemical, I believe it's a chemical fire retardant. So it literally can't catch on fire. Like I think, don't quote me on that, but yeah.

**Dave Jones:** Yeah.

**Yankee:** Yeah.

**Dave Jones:** I actually, I had asked you about, I think maybe on the show, but we talked about it otherwise too. And I did talk to my buddy who's a solar salesperson. And one of my childhood friends is a solar salesperson. And he took a look at my new place. He's like, no, there's a, don't do it. I think we talked about that sun tool. The sun. Yes.

**Yankee:** Yeah. The Google, there's a Google sun. It only works in the U S but yeah, it'll map how much energy square area your roof is and tell you how much your solar energy and it'll show shading for trees. Shading of trees. Cause it has sort of like a 3d model. Sun tracker. Something like that. Sun. I don't know. You did send me to link. Yeah. But yeah. And no, I've seen the roof of your house. And once I, I immediately saw that and went, no, don't even bother installing solar. Yeah. It's like, nah, you've, you've got like 10 angled things.

**Dave Jones:** Yeah. When my buddy said, well, my buddy said, he's like, he's like, well, Chris, that's right. He's like, Chris, uh, solar panels are square. And your roof is triangular.

**Yankee:** Your roof's got like 10 triangles on it.

**Dave Jones:** Pentagrams or something like that. Something like that. And not so much.

**Yankee:** You could put a couple on there, but like, no, I had a three kilowatt system with 12 panels. Obviously 12 would be more now because they're on 250 Watts, but even that is not nearly enough to power my house. So it's like, no, you've got to have like 20 plus panels or something before you even start getting serious for solar. So.

**Dave Jones:** Someone corrected us after we were talking about this. It was a couple of shows ago. We were talking about this. Of course I dig.

**Yankee:** We're always wrong.

**Dave Jones:** Yeah. Well, no, no, they were correcting that, not correcting. They were, they were clarifying. Cause you had said, Mrs. EEV blog runs the air con. Yep. And I was thinking about it and I was really confused. I think it was on Twitter. And do you call the heater as well? Is that also the air con? If it's like heating or cooling?

**Yankee:** Yes. It's that was very confusing to me. Yeah. Yeah.

**Dave Jones:** Cause I was like, it's winter there. Yeah. Yeah. That makes so much more sense. It's still the air con.

**Yankee:** No, we don't have, yeah. We, we don't have the same heating solutions that you guys did. And there's no, almost practically no house in Australia that has, you know, they're all heat pumps, right? Yeah. Heat pumps through the walls of the apartment building or something.

**Yankee:** You have heat pumps. We have HVAC. Sorry. Yes.

**Dave Jones:** So I have, right. Forced air, central HVAC kind of thing. So it's like.

**Yankee:** No, we just have a reverse cycle air con that heats up.

**Dave Jones:** Yeah.

**Yankee:** So we still, that's why we still call it an air con, you know? Yeah.

**Dave Jones:** I mean, air conditioner. It makes sense. It's just, that's the only way that we talk about the cooling system here. So that's what.

**Yankee:** Although having said that in some mountains regions, they do have like central gas heating. So you'll have like floor vents and it'll be a central gas hot heating, central gas heating thing or something. But no, in most of Australia, no, it's, it gets pretty warm here. So no, heating's not a thing here generally.

**Dave Jones:** Yeah. Wiley was asking if I live in a dome because I said I had a very oddly shaped roof.

**Yankee:** Like a buckyball. Buckyballs are all the rage in the eight. Was it the eighties? The seventies. When they discovered, when they discovered the buckyball, it was all, I was going to revolutionize everything. Buckyballs was going to revolutionize our entire lives.

**Dave Jones:** Buckingham, Buckington Fuller? No, something Fuller, right? I don't know. Yeah. He had a house actually from my old place in Ohio. There was actually one of his early creations. Is it Buckingham something? I thought it was, I know it was Bucky. So Buckingham, I thought. But, but yeah, he did like the, the house of the future. And yeah, people are going to go nuts about this.

**Yankee:** That was Buckminster.

**Dave Jones:** That's it. Buckingham. How do I not know that Buckminster Fuller? Yeah.

**Yankee:** So I've, I've done a video on looking through old books beyond 2000. They were called books one, two, and three. It was a TV show in the eighties. What life would be like beyond 2000. And I've done a video looking through those books and it's just hilarious to see like some of the things that we thought we're going to actually predict and you know, that, that we're going to be big and it's like, yeah.

**Dave Jones:** Hey man, they got the video phone right. They got the video phone right.

**Yankee:** Nobody, nobody predicted the smartphone. Absolutely nobody.

**Dave Jones:** No, there was that. I mean, well.

**Yankee:** No, not, not as it is. No. Not as it is. You're right. You're right. No. No.

**Dave Jones:** Yeah. I mean, uh, I think the closest would be Star Trek right with the communicator, right? You know, like the flip up. Yeah. Maybe.

**Yankee:** I don't know, but, uh, I'm sure I'm trying to find the video to link it in, but it's not there.

**Dave Jones:** Uh, what video? Oh yeah. Of the 2000s? Has the future. Yeah.

**Yankee:** It's because I didn't put beyond 2000 in the title. Has the future arrived yet? Part one. So here we go. I will link it for those playing along at home. Cause we do have people playing along at home today. Nikola Tesla. Oh, Tesla fan boy in the house. Predicted the smartphone. Yeah. Okay. No, the, the greatest, the greatest prediction ever. And it wasn't even a prediction. It was a demo. It's called the mother of all demos. Look it up. The mother of all Douglas Englehart. Englehart, Englehart. Douglas Englehart. I think the mother of all demos.

**Dave Jones:** But what year was it?

**Yankee:** Uh, 60s.

**Dave Jones:** Okay.

**Yankee:** Uh, Douglas Englehart, mother of all demos. Don't Englehart. No, no, it's Englehart. Yes, I was right. The mother of all demos. Look it up. Check it. Google the mother of all. Anyway, what he, don't quote me on this, but what he demonstrated, he actually physically, this was technology they'll demonstrate in the 60s. He demonstrated graphical user interfaces on a computer, hypertext, right? So hypertext markup language, basically. Teleconferencing, like as in Zoom calls. They, they, they actually did this live in the 60s as a demo. The mouse, they, they actually demoed the mouse.

**Dave Jones:** This is, this is Xerox parked then, right? That was.

**Yankee:** This is Xerox parked. Douglas Englehart at the Xerox parked. I've seen that before. It's the mother of.

**Dave Jones:** That image came up on Twitter the other day too. And like the mouse too. It looks, it's, it's rough. Yeah. But yeah, yeah. It's rough as guts. But you're right.

**Yankee:** All this, all this stuff that's modern, that we use all of like word, word processing and like, you know, gooey interfaces and the whole, you know, email, everything. This was all done in a demo on the 60s called the mother of all demos.

**Dave Jones:** What's interesting. So I was, I was having a chat with my buddies about this the other day too. Just thinking about like, as an electronics designer, the other type of things that we do these days. And like, and so like if you're in the 60s and you're like, well, you know, you're going to look up your own things. And then be like, well, but I have a research assistant or you're going to type up your own things on your, on your computer, right? You're going to have a word processing. Well, but I have a secretary or, you know, like you're going to, you're going to have a graphical user interface so you can interact with your computer. It's like, yeah, but I could sit in a meeting with someone. And it's just like how compressed everything has gotten in terms of like just the work labor force and stuff like that. We were really complaining about like all of the things that we had to do and all the tasks were out there and just kind of like the efficiency gains that happened. And, you know, they happened because technology plus also expectations and bottom lines, whatever. But like, that's when it's really crazy. I feel like, like having that kind of vision upfront while, you know, like while you're in and amongst all of these other things, all of these other norm, normal things that are happening around you, right? He was making that prediction when his secretary was typing something up and is, you know, like all of these things that were happening, you know, it's just that that's when it gets really hard when you're inside a system like that, it's really hard to break out and do the prediction of the future stuff. But to be fair, also Xerox was making some of that future stuff anyways, right? They were inventing it.

**Yankee:** Yeah, it was absolutely incredible, but it didn't go anywhere for 20, 30 years. You know, it's just like they demoed all this. They actually had it working and it was a thing. It's just wasn't, wasn't commercially viable, unfortunately. So, yep. Oh, he passed away in 2013 at the age of 88. There you go. Douglas Engelbart. Yep. Legend. Mother of all demos. I have no idea what that means. Anyone? Bueller. Bueller. Chris is frozen. Oh, stream's frozen. Chris is frozen. Am I still live, everyone? Can anyone hear me? Let's have a look. You are still live? Yes, I'm still live. Okay. Thank you. Yeah, John Oxer says I'm still live. Yep. Yep. You're fine. Yep. I'm good. And no. Yep. Chris has left the chat. All right. So I'm going to have to anchor this one. No whackers. Audio is good. No drops. Yep. Chris, he's obviously got a dodgy internet connection to his new home. I told him that was the number one requirement. For the new home. I'm still live. I have my suspicions. Yep. I may be dead. You never know. I could be a sim bot. So anyway. Back to questions. Because we don't have anything planned for the show. So, you know. We're just doing. Oh, we're way past our amp hour anyway. But who cares? And it's not like I have a real day job to go back to. But if you do want to know. I am actually working on a reverse engineering video at the moment. So, which is reverse engineering. The Mixig DP1007 probe. So, and. Dave. Can you explain your role at Altium? Altium produces software. But why was there hardware design? In-house, real world software testing. Are they still partly based in Australia? Good question. Ian. How long? It might take another hour to do this. Right. I joined Altium in. Oh, boy. I've been away from Altium for 10 years. I was there for four, I think. So, yeah. 2009, was it? No. No. I left in. No. I left in 2011. I left in 2011. So, 2007. 2007. I joined Altium. And, yes. They started up a hardware group. Because, in fact. The first person they hired. Was my former colleague. At SirCell. At Tally's. Slash SirCell. That I was working at the time. And Steve Howell. And so they got. He was the first hire. For the hardware group. And then the second hire. They practically poached. Everyone from Tally's. Slash Altium. Okay. The second hire. Was my mate Jeff Engel. And he was also. From SirCell. Tally's. At the time. Oh, Chris is back. All right. I'll continue. He's back. Is that. No, no. Please go. Dodgy house. You've got there. Dodgy internet connection.

**Dave Jones:** Yeah. Man, I got fiber. I got fiber that I. My. Well, I'll tell you about that afterwards.

**Yankee:** Yankee fiber. All right.

**Dave Jones:** Anyway.

**Yankee:** So, yeah. So, they joined. So, he was the second one. To join the hardware group. And then. He said. Oh, Dave. You should come over to Altium. You know. And see. We're working on this hardware shit. And, yeah. So, I went to interview at Altium. By Nick. With Nick. Nick Martin. The founder himself. And he liked me. So, I was in like Flynn. And, yeah. So, they poached three people. From. Which was almost the entire hardware. Which, well. At the time. Was the entire hardware group. They poached from. Sir. So, Altium. So, we were all former colleagues. Working on the same stuff. So, we just all moved to Altium. And then we hired a. Faming. Who was. A. Who was our Chinese guy. He was Chinese. Could speak Mandarin. So. Very handy. Trust me. It's very handy. To have someone. Who speaks Mandarin. And can get on. What was the chat thing. At the time. That you chat to. I don't know if it's still a thing. QQ. QQ. Or whatever. Yeah. WeChat. Or whatever. Yeah. Yeah. I think it was QQ. Oh, no. WeChat. Yeah. QQ sounds right. QQ or something. So, he can get in there. And chat to all the. You know. All the distributors. And he handled. You know. He handled. Interfacing. With Chinese suppliers. And manufacturers. And stuff like that. So, that was very handy. To have him on board. And, you know. Just parts sourcing. And things like that. So, that was the four of us. In the hardware group. At Altium. And our job was. Well. Our kind of main role. Was to design. The. Nano board hardware. No. I don't have one here. It's down in my storage bunker. Anyway. The first NB2. The. Nano board. NB2. Here we go.

**Dave Jones:** Show your screen there. If you want.

**Yankee:** No. No. Don't. Don't share my screen. No. I'll just. Oh. Well. Yeah. Okay. You can share my screen. I can share my screen now. So. Nano board NB2. This bad boy here. Are we sharing? Not yet. Not yet. Oh. Hang on. Oh. I have to do it. Do I? Yes.

**Dave Jones:** You do. Yeah. So that I can't just take control of your computer. I thought you could.

**Yankee:** I thought you were in charge. Okay. So if I go like. That. Hang on. No. No.

**Dave Jones:** There it goes.

**Yankee:** No.

**Dave Jones:** No.

**Yankee:** Hello. McFly.

**Dave Jones:** There's a share button at the bottom.

**Yankee:** It's a share button.

**Dave Jones:** The bottom. Oh.

**Yankee:** Right. Oh. Screen share. Yeah. You're right. Yep. Share screen. There we go. There we go.

**Dave Jones:** While Dave's doing that. I can talk about my fiber story. There we go. I had. Yeah. Go on. Too slow. Too slow. Too slow. Too slow. All right. You finish up.

**Yankee:** Too slow.

**Dave Jones:** You finish up.

**Yankee:** Okay. So that can. I can share.

**Dave Jones:** This thing was so ugly. This thing was so, so ugly. Oh. And expensive.

**Yankee:** No. It wasn't. I wouldn't say it was ugly.

**Dave Jones:** I'm telling you right now, Dave. You reckon that's ugly.

**Yankee:** Well, this one was sexier. This was the next generation. Okay.

**Dave Jones:** No, they're all ugly. They're dev boards, but they're ugly. They're ugly dev boards. Sorry. They look nice for dev boards, but they're dev boards and the category is ugly. That's what I'm trying to say.

**Yankee:** At the time. At the time. Okay. They were. At the time, they were the dice cards. Right. Anyway. Right. Anyway. The Natterboard. So it had an FPGA module here. So this thing in the middle, this was an FPGA module. So we designed various FPGA board, you know, different types, different brands and types of FPGA boards. These were the peripheral boards, the PB boards, as we call them. And we designed, you know, dozens and dozens of these to do different things. Like this one up here was an audio. This was an SD, a compact flash back then, compact flash card reader. This one was a USB. Geez. What was that? God, I forget. I don't know. Maybe I designed that. I don't know. And anyway, you had a touch screen. Is that a WISnet chip? And anyway, I had an LCD over here. No, that wasn't around. We're talking the nineties here. So, sorry. Late, late two thousands. And yeah. And I had, you know, audio and VGA output and stuff anyway. And analog to digital converter inputs and stuff like this. Anyway, this was, yeah. Actually, this was the NB2 before the hardware group was the NB1. And that was designed, I believe, by Nick Martin himself, the founder of Altium slash ProTel. Here's the thing.

**Dave Jones:** You get all this stuff. It's all super custom. It's all designed. It's all supposed to be looking cool. And then you get this lime green terminal block. Yeah, I know. I know. Come on. Come on. You couldn't like call a vendor. You couldn't call a vendor and be like, how about black? And they're like, yeah, we've got black. Of course we have black.

**Yankee:** Right. Anyway, there's the NB1.

**Dave Jones:** Well, we're Phoenix contact. So we have to have green. I'm sorry. It has to be the ugliest green you can possibly. Take olive drab. Mix in a little bit of lime, you know, key lime. And then, you know, some vomit on top. And that is the Phoenix green.

**Yankee:** Right. Anyway, there's the NB1. So that was designed by Nick and, I don't know, laid out by who were probably someone who was writing the PCB software at the time. You know, like they didn't have a hardware group back then. And, you know, but they had hobbyists. Like, you know, most of the, you know, probably a lot of the programmers there were actually hobbyists themselves, you know. Anyway, so they laid out that. So anyway, they designed, Nick decided that, oh, yeah, we're going all FPGA. Because this was when Altium decided in 2000, when they went public to, yeah, become a public. Well, no, when was it? I don't know. Any time in the 2000s. They went public, publicly traded company. And then they changed the whole vision of the company. FPGA, he decided FPGA was the future. Everything would have. I mean, see if they could.

**Dave Jones:** I'm just, I'm just throwing shade at other people's comments here. Do it, please.

**Yankee:** Throw out the comments. Yep. And, and. You keep going. You tell your stories. So he decided, right. Because Nick Martin ran everything, right. It was a public company, but no, he iron fist, you know. So famously, the company was like, was pretty much Nick Martin, everyone else. It was a flat structure. It was like, yeah, technically there were managers, but it was like nothing went ahead unless Nick Martin said so. You know, it's like, you know, it's anyway, which can be good and bad. You know, it has its good points and has its bare points. But anyway, yeah, FPGAs was the future. Everything would have FPGAs in it. Microcontrollers, not gone. FPGAs, everything. You know, it was so compelling that FPGAs were going to be the future. He bet the company on it. And, yeah, and it developed actually some really good, Altium has really good FPGA support built in. It's really amazing where you can drag and drop FPGAs in. And they had hardware. They bought various companies.

**Dave Jones:** Who brought this up? Who do I kick out of this chat? Come on, this is great. They got Dave. Anyway. They got Dave on this.

**Yankee:** No, because it's a fascinating story. It's fascinating.

**Dave Jones:** It's fascinating to you. This is a dev board from 10, 15 years ago.

**Yankee:** No, no, but the whole vision of FPGAs is fascinating. They bet the whole, they bet all of Altium on it. Yes, I know.

**Dave Jones:** People can hear many shows about this and how it didn't work out.

**Yankee:** And how it didn't work out. Anyway, I'm going to complete my story, Chris, if I may.

**Dave Jones:** Can you imagine the vision? If this vision came to fruition in the scenario we're currently in, they'd be like, oh, there's an FPGA in everything. And you'd be like, you know what? Everything in the world is shut down because you cannot buy a single goddamn FPGA right now.

**Yankee:** It's the same thing. Yeah. Anyway, he thought it was so compelling that, yeah, they bet the company on it. And it had, they had C to hardware compilers. They bought a company, I can't remember the name, that did C to hardware compilers. And you could just write your C, it'd convert it to VHDL, or Verilog order, and it'd drop it in there. And it was all, it all worked really magically. It wasn't great for like really high-end projects and stuff like that. And it tied into all the vendor tools. So it tied, so yeah, it'd be installed, you know, the Xilinx tools and the Altera tools. And it would all seamlessly pull those in and use those in the background. And it was really cool technology, but it, yeah, it just didn't work. And so a PCB company made the PCB tool optional extra. I'm, I'm, I'm not kidding. This was their marketing at the time. You can go, go look it up. It was turning the world of electronics upside down was their marketing slogan. They had billboards in Silicon Valley, all over Silicon Valley. And it was like, yeah, the whole idea was that you bought, you could buy this board for $4,000, right? It was the world's most, US dollars, I think that was. US, right?

**Dave Jones:** It was a $2,005. Yeah, yeah.

**Yankee:** No, that was a, yeah, whenever, 2011 I left. So it was, yeah, 2009. $2,0010. Yeah, 2010. Roughly $2,010. $4,000 bucks.

**Dave Jones:** Those are, those are, those are post crash dollars. Yeah.

**Yankee:** And you could buy this on DigiKey, right? You could buy this on, we did a deal with DigiKey, right? If you were to put. They had 200 of these in stock at DigiKey. I actually remember the number. Oh, Chris has dropped again. So they had 200 of these NB2 nano boards in stock. So you bought this for $4,000. It came with a license.

**Dave Jones:** $4,000 in.

**Yankee:** You're breaking up, Chris. Your audio is breaking up.

**Dave Jones:** Yeah.

**Yankee:** Is Chris's audio breaking up? Yeah, Chris is breaking up. I think I'm still good to go. Anyway, so $4,000. And the idea was that you got a license to the Altium software, but it didn't include the PCB tool, right? It came with all the FPGA and software and compilers and everything else, right? That because the whole idea was that, oh, why would you need that? You can just design your product using these modules. So the whole idea was that you could plug these modules into your product. You would never have to design a custom PCB again. Or if you did, it'd just be a motherboard that held these modules, right? And we'd develop hundreds of these modules and they'd do everything, right? And also, at the time, they went into modular PCB concepts. So you'd never lay out a full board ever again. It was like your power supply. Here's the mod. Just take it from the library. Drop it in. The actual layout, right? And it was like, so that was the vision of Altium at the time. And it was like so wacky. Like it was never going to work practically. So anyway, this was the $4,000 development board. And basically it didn't sell. I don't think a single person bought one from DigiKey. So I think DigiKey made us buy them all back. Well, they sent them all back. And we had to re... It was like, you know, there were some people who bought them. You know, there were other sales avenues as well. Like some people bought them and stuff. But yeah, it was basically... It was... It priced itself out of the market. So then we developed the NanoBoard 3000. The NanoBoard 3000. Why is my... Normally I've got a thing which pops up. Anyway, NanoBoard 3000, which was... This was $300. So this was like order of magnitude low. I think it was $300. And it was order of magnitude lower cost. And it was compatible with all the same FPGA boards. It was actually... Oh, no. Sorry. Did it... Oh, no, no. It had one built on. I thought you could... Oh, God. I can't remember. It's been a decade now. Anyway, it used the same NanoBoards and everything. And this was $300. And it also came with a license and the software. Once again, with no PCB tool. So it was like... Yeah.

**Dave Jones:** I have expected to be coming back into like just you switching over to solar roadways or... Yeah. What else is on the greatest list? Why not?

**Yankee:** Anyway. So yeah. So in the end it failed and they booted Nick from the company.

**Dave Jones:** That's another good story. Another story for another day. Yeah.

**Dave Jones:** Yeah.

**Yankee:** And yeah. Poor old Nick. Really nice guy. Felt sorry for him. But yeah. He ran out to him as his hobby company. And it was like, you know, and his vision company. It was... Yeah. Even though it was a publicly listed company which was supposed to make a profit. So yeah. Nah. Profit didn't matter. It was like... So nobody bought the $4,000. So I hereby claim to have helped develop the world's most expensive development board. And for... Does anyone know of a more expensive development board than $4,000? I know there are. I know there are FPGA. Like you can ASIC development boards. You can get like 100... In the six digit range. In the hundreds of thousands of dollars that have... They're like huge. They're like this big. And they've got like 50... Like high-end FPGAs that are worth $10,000 per chip. And it's got... And they've got like 50 of them on there. And you can buy them for like half a million dollars or whatever. I think they go up to. I can't remember the name of the brand. Somebody's going to put it in here. The... Any FPGA ultra scale board. Yeah. So they're designed to simulate ASICs before you... You simulate them in an array.

**Dave Jones:** No. Ultra scale is not necessarily just that. You can buy like an ultra scale for... Oh, well, no. Yeah. Yeah.

**Dave Jones:** You know, that's military using that sort of thing too. So yeah. They're just top end right now. Yeah. Any kind of military... Yeah.

**Yankee:** Anyway, you can... Yeah. There's companies that specialize in these ASIC development boards that have an array of FPGAs. So you can get... You know. So you simulate your ASIC. And it ties into all the ASIC tools, I guess. You know. Software probably costs more than the hardware. And it's... Yeah. And you can simulate your ASIC before you turn that key to, you know, get your mask. That costs a million dollars or whatever. So yeah. Those boards are more expensive, but not mainstream. What does Nick do now? I don't know what Nick does now. I don't know. He sort of dropped off there. He absolutely vanished. Signal Path is in the house. So Dave, have you bought a Wi-Fi router cage yet to protect you by my health?

**Dave Jones:** Just the underwear. Greatest hits, all right? Just the Wi-Fi safe underwear.

**Yankee:** Just the underwear. Yeah. Just the... Just the mesh shielded underwear to protect them.

**Dave Jones:** Me undies is now doing chain mail, you know.

**Speaker ?:** Yeah.

**Yankee:** It reminds me of the scene from Mission... No, not Mission Impossible. 11.

**Dave Jones:** Ocean's 11.

**Yankee:** Ocean's 11. Is it? Yes. Is Ocean's 11 or 12 or whatever? Where he's, you know, covering like this as the EMP goes off. You know, he's like... That's your character. He's pushing the button and he's covering.

**Dave Jones:** Yeah.

**Yankee:** It's great. I always love that scene. Yeah. Yeah. Oh, they're so dodgy. Anyway, if you haven't seen it, watch our video on the EVE Blog 2 channel with Sharia from the Signal Path where we talk about this bullshit. It's great. Oh, and it's an Ampour episode too. That's right. Yep. Yep. But if you want the video version, it's there. It's also available as video on the Ampour.

**Dave Jones:** That's right. 553. Straw poll.

**Yankee:** Can we do a straw poll? Do people like or want to watch a video version of the Ampour? Or should we just stick to audio? Because there are some subtle things that change when we do a video version. It's not as... It probably doesn't sound as good to our podcast because we build up 10,000... What's our current subscriber count, Chris?

**Dave Jones:** Yeah.

**Yankee:** 15,000? Sure. Something like that. That's about right. Yeah. That's about right, I think. And then we built that up on audio podcasts. So most people have just... Who gave Red Bull to Dave? No, this is just my usual self. Anyway. Video is great. Yes. Video. Video. Less distraction while working. Video is good too. Yeah, because there are compromises. Because if we do video, we have to use a tool like this and the audio is not as good. We do believe the audio is not going to be as polished from using StreamYard. And then we sort of... And the interaction's different when we're looking and talking to each other. The interaction sounds different. It'll come across different.

**Dave Jones:** I don't think it actually sounds any different. I listened to both. No? Yeah. You did? Yeah.

**Yankee:** Okay. No, I know ones that I've looked at some we've done and I thought it sounded different.

**Dave Jones:** I think the thing that's different is the... Usually we don't edit the video. So there's no...

**Yankee:** Right.

**Dave Jones:** There's no tightening up of...

**Yankee:** Right. There's no... Right. Okay.

**Dave Jones:** There's ways to make us sound slightly more intelligent. And putting us on camera is not one of them.

**Yankee:** Right. Yeah. Audio is most important. I think of...

**Dave Jones:** Someone had asked earlier on... It was a student question and now I've lost it. Oh, wow. Oh, we run out... The comments disappear past a certain point. So sorry about that. If there was a student who asked a question earlier and I totally missed it and I meant to put it on the screen. So if you...

**Yankee:** Okay. We do have audio recorded separately or we can.

**Dave Jones:** We do.

**Yankee:** But it's just the style of the way we talk, I think. The interaction, I think, is different when you have video. So I think there is some subtle difference there. Chris notwithstanding. He doesn't think so, but I think so.

**Dave Jones:** Dave just isn't comfortable on video. That's what it is, folks.

**Yankee:** Oh, yeah. No. About 2,000. 2,500 videos. I'm just... Yep. Yep. Yeah. Yeah, I think I'm at least 2,500 videos now, by the way. Because I've got like 1,400 official, but I've got like actually 1,700 on my main channel because there's a lot that aren't numbered. And then my second channel has close to 800 or something videos. So... That's crazy, man. Nice. Yep. Nuts.

**Dave Jones:** Next thing you know, Dave's going to start putting cameras up in his house. It'll just be watch Dave live stream his life. That's how we know we've reached the end.

**Yankee:** It was a fleeting thought. It was a fleeting thought when I had my first child. Should we like stream our lives, you know? Like raising the kid, you know? It's like Truman Show style. It's like... No. No. No. No. Not going to happen. You managed to buy David. Saliba managed to buy a LaCroix 9314. Excellent.

**Dave Jones:** How much did you pay for it?

**Yankee:** It's a scope.

**Dave Jones:** Give me a little bit more than that. While you're looking that up, this is the question that was asked. What's more valuable as an undergrad? Internship work experience or work... An internship or work experience in an electronics manufacturer wanting to be a design engineer? So that is the question that was asked before. Are they different things? I mean, I guess internship was probably a longer or shorter time period, right? Than work experience. But I kind of think about internships are work experience, really.

**Yankee:** I don't differentiate. I don't know what the differentiation is.

**Dave Jones:** I think they're talking about like a year, you know, like go and take a year, maybe, and work on like a line. I think, honestly... Oh, okay. It comes down to like how you present it too, right? So like if you could do... If you only had three months to do an internship and you could like get some kind of project out of it that you could talk about in your next interview or that would look really good or be, you know, the thing that's going to be catnip to the future recruiters, then do that, right? Or if you're going to get some kind of valuable experience or get to work with someone really great, you know, like those are all the reasons to do these sort of things. If you're going to go and like be on a, you know, a production line for six months and you're going to be turning a screw, it's like that's not worth it, you know? Even if it's on there, so.

**Yankee:** Well, I guess it depends on your degree, doesn't it?

**Dave Jones:** If you can go work in Shariar's lab, that would be the best thing, yeah.

**Yankee:** What they offer, like some of them will force you to do, like to take a year off, take a year of your degree, will be like all six months or whatever. They'll force you to go work full time. Others will go, no, it's only, you know, part-time work experience or something. Some won't even have it.

**Dave Jones:** Yeah, yeah.

**Yankee:** So it's like, although most, most degrees, most universities, colleges in the Yanks will give you the ability to pause your degree and then, or your diploma or whatever it is you're doing, and then go do a year's work experience and then come back and finish it. So that's always an option. Like even if you're, even if you, the structure of your course doesn't actually force you to do some sort of internship or work experience, then you can still do it. You can just pause. You should just be able to pause. But yeah. Yeah. But often a lot, there are a lot of people who pause and then never go back. That's right. Yeah. So once they get the sniff of the free world. And the money. And being free and free in the real world and shit, I don't have to study. Oh, this is great. And I get paid instead of paying them. It's like, oh, you know. Yep. Yep. Oh, Sharia. Here you go. Here you go. Go and work for Sharia. No, I don't. What is the behemoth Tesla made for the dojo hardware? I have no idea what that is. You, Chris? Tesla behemoth? No? Dojo hardware?

**Dave Jones:** I try not to pay attention to the antics of Tesla these days.

**Yankee:** Right. Yep. I can do the robot. I swear he did that as a troll. I swear. Like, the guy's a master level troll. Like, he just does it just to stir people up and he gets a kick out of it. I'm sure, like, I'm absolutely sure of it. New system for crunchy neural nets. Oh, okay. Right. Yeah. Yeah.

**Dave Jones:** Oh, that was, they released some new silicon. Okay. I know what they're talking about now. Yeah.

**Yankee:** All right. Yeah. Yeah. Yawn. No. I don't really have my, yeah. Same, Chris. You're not really interested in AI. I mean, I'm interested.

**Dave Jones:** There's going to be huge impacts on us. I'm sure. It's just that. Of course. I have no capabilities there. So it's like, what am I going to talk about on here? It's like, yeah. Computers.

**Yankee:** When I was a boy, we didn't have IGBTs at this sort of level, you know?

**Dave Jones:** Yeah.

**Yankee:** Back when I was working on high voltage stuff, it was hard to get a 500 volt transistor. What? You know? It was like.

**Dave Jones:** 4,500 volts?

**Yankee:** Yeah. That's crazy. They're incredible. Wow. They're incredible. They're just insane. Yeah. Yep. Yep. Back when I was doing, you know, five, 600 volt stuff, that was like, the limit was the semiconductors you could get. Sure. Totally.

**Dave Jones:** Like, you know. How big is the trench?

**Yankee:** Yeah.

**Dave Jones:** Actually, so you've mentioned on another, I think one of your streams, you'd mentioned John Edmund, who was, remember the Cree guy? Yes. Yeah. That we had on here. Yeah.

**Yankee:** Cree. Yeah.

**Dave Jones:** You know I'm next to Cree now. That's right. So I live in North Carolina now. Oh. Oh, there they are. They're fabs down here. Yeah.

**Yankee:** Oh, there you go. You can go visit.

**Dave Jones:** Yeah.

**Yankee:** Knock on the door. Yep.

**Dave Jones:** Yeah.

**Yankee:** Yeah.

**Dave Jones:** It's interesting. The types of industry that are down here and stuff like that too. Like the, it's very like medical heavy. So, you know, that's not me. Right. But, yeah. It'll be interesting.

**Yankee:** There's an interesting question.

**Dave Jones:** Yep.

**Yankee:** Don't know if I've got an answer. As the show has grown and as you've grown as an engineer, I kind of plateaued, I think. How have you re-evaluated the tools at your disposal? Well, that's more a question for Chris because he does active development, active product development, whereas I don't do that anymore, really.

**Dave Jones:** Hmm. Yeah. I mean, I guess it depends on the tools. I mean, so like on the firmware, software, tool chain side of things, like that stuff is way better than it used to be, I think. Even just, I was just talking, I was throwing some shade on Twitter the other day about VS Code, right? So like VS Code these days versus like Eclipse. And Eclipse was like, yeah, but we've got millions of downloads. It's like, I don't care. Eclipse is just like, you know, like it's every old IDE is Eclipse-based or whatever. But like just VS Code is like this open source, nice looking, pretty capable IDE that not even, it's just a, you know, it's not even IDE. It's just like a platform that you can build on top of. And like, it's just making development easier, right? And it used to just, I mean, Dave, you deal with it, right? It's just like you get the IDE that you get and then you just work within that, right? Yeah. And so.

**Yankee:** I don't like to change. I like to stick with the same. If I learn an IDE or a CAD tool or any tool, I don't like to change. I still like to use it.

**Dave Jones:** So Dave doesn't reevaluate. I do like doing that. I think.

**Yankee:** Well, I do. Like I'm always sort of looking, but in the end I go like the equation, is it worth it? What value is it going to add? And if it doesn't, if there's not some compelling game changing thing, then I'm not going to change.

**Dave Jones:** Well, I think you got to, you got to actively try new things though, too. You got to like, you know, sample, you got to like, you know, try it, try things out on.

**Yankee:** Well, you can, it depends on if you've got the time and. Right. You know, if you've got the time to do it. I think that's worth it. Right. Yeah.

**Dave Jones:** So that's.

**Yankee:** Some people just, you know, ask, ask Mike, is Mike still in the chat? Like he still uses. Yeah. He mentioned he's using. Old, old, old tools. Right. Because why? Yeah. Why, why, why change? It does his job and he's so busy that, you know, developing projects for clients that he doesn't have. Couldn't care less about.

**Dave Jones:** Well, you know, we should ask, we should ask someone else here. I'm sure. What they think. So let's add Mr. John Oxford to the stream. G'day. Hey, what's up, John? Hey, there we go. Finally checked his DMs. He saw. I know. I'm sorry. That's all right. How you doing, man?

**Chris Gammell:** Really good. How are you? I'm good. Awesome, mate.

**Dave Jones:** Fantastic. So how about, how about you? Have you reevaluated the tools at your disposal, Mr. Smart House? Smart House.

**Chris Gammell:** I am constantly reevaluating, but I never seem to change. Yeah. I find that I get stuck. It's that classic problem.

**Dave Jones:** You just, you just, you keep finding the same answer over and over again. Is that the thing? Yeah.

**Chris Gammell:** Well, it's the classic problem that, you know, both of you talk about all the time where, when you're really familiar with something, the friction of changing to something else has that short-term pain. And overcoming that can be really difficult. So, you know, CAD tools are the classic thing. I use Eagle constantly. And every now and then I will open KeyCAD and play around with it a little bit and just feel out of my depth and nothing is quite what I expect. So I have to, it's going to be a real conscious effort to say, I'm going to take the performance hit for a while to overcome that, to change tools. So that's just what you've got to get through.

**Yankee:** And it's not just changing tools, it's upgrading.

**Dave Jones:** What if I booted him out as soon as he started saying, like, I'm an Eagle user and I just booted him right out of here. I'm like, see you, John, you know.

**Yankee:** Right. I'm going. It's like, no, as somebody who's worked at Altium, I know one of the biggest things that the salespeople kept telling everyone is that like, we can't get these people to like, it was easier to get people to change to Altium than it was to get people to upgrade to the next version of Altium. Like they just wouldn't, they would stick with 99 SE, you know, and they just would not, oh, what's this summer winter bullshit? No, I'm not, I piss off, you know, I'm not upgrading. It's like, no, Altium 20 piss off. I'm happy with, you know, 2016 or whatever. It's like, yeah, they just wouldn't change because they were familiar with all the bugs and quirks and everything and it just worked. And it's a tool to get the job, at the end of the day, it's a tool to get the job done.

**Chris Gammell:** Yeah.

**Yankee:** And if it does the job for you, why change? Yeah.

**Chris Gammell:** Well, this conversation I think started, you were talking about IDEs and software tools. And even after all these years, my preferred editor is Vim. And I just find that I can get around things quickly with it.

**Yankee:** Yeah. Yeah. Yeah.

**Dave Jones:** I feel like that's its own, that's its own brand of crazy, you know? Yeah. True. Especially, but like, you know, you have like a software background too, right? And didn't, didn't you do software for a while? Yeah. About 20 something years. Yeah. Yeah. So that's, yeah. Yeah. Yeah. I mean, that's going to be a common, common thread, I feel like, you know? Yeah. I don't know. I feel like, I feel like when there's a new challenge you have to hit or like a new chipset that comes out or something like that, like, that's what I think about, you know, like, yes, if you're doing the, you know, if you're doing like a power supply layout and it's just, you know, another spin of the same thing over again, then like, yeah, the same tool is going to be the same, the same thing. I just feel like when you're into a new space, you're trying out new applications. You get, sometimes you just gotta, you gotta try out new things.

**Chris Gammell:** Yeah. Well, right now I'm just in the process of getting into a whole new thing on new for me, which is FPG8. And this came up earlier in Dave's rant about Altium. And so for the Open Hardware Minicon, which is going to be on in January, the project we're doing this year is going to be based on Tim Ansell's work with the FOMU, which has got the UP5K FPGA on it. And for those who don't know, it's an FPGA board, which is so small, it goes inside the USB port of a computer. So the actual PCB is like, you know, that big and it's got an FPGA on it. So, um, yeah, we're working with Tim's assistants to put together a project, which is going to be a conference badge with the UP5K on it based on the architecture of the FOMU. And that whole thing is totally new to me because I've never done any FPGA work before. But yeah, getting into a new field is an opportunity to look for the... And that uses Open Toolchain, right? Yeah, it's a whole new toolchain and different things to learn.

**Yankee:** Yeah. Yeah. But it's not changing your...

**Chris Gammell:** No.

**Yankee:** Well, it can add a tool to your arsenal. That's right. But it's not changing your actual bread and butter stuff. And here's an interesting question. Do you think Altium and other EDAs should be worried about KECAD encroaching on their market share? Probably not. It's like as great as KECAD is getting, it's still not a pro-level tool. Like I know there are people who will throw examples at me. Oh, look at this 10-layer boarding KECAD and stuff like that. But unless you've worked in the professional, like the truly high-end professional PCB base, then it doesn't have the tools that you need. So I think it's a significantly long way off from challenging Altium.

**Dave Jones:** Dave's working from old knowledge. And yes, I think his old knowledge is correct. And we'll re-evaluate once this is out. Yeah.

**Yankee:** Yeah. But you've... Chris, you have never been a true high-end professional PCB designer. Oh.

**Chris Gammell:** I'm just going to get the popcorn. That's right. Yeah.

**Yankee:** No, I do, you know, what's the highest-end, you know, sort of stuff? It's, you know.

**Dave Jones:** All right, Dave. We don't need to start slinging mud at 555. Okay.

**Yankee:** Yeah. Yeah. Yeah, right. Chris is still designing with 555s. Yeah. Yeah, right. Right. Yeah. Yeah.

**Yankee:** Shots fired. All right.

**Chris Gammell:** Well, congratulations on episode 555. I just wanted to drop in and say hi. Yeah. Thanks for dropping in, John. Thank you very much. Appreciate it. I'll talk to you both later.

**Yankee:** And maybe when they... If the lockdown's ever end, we'll catch up again.

**Chris Gammell:** Yes, we've got to meet up again in person. And Chris, if I see you again next time, I won't try to kill you with a drone.

**Dave Jones:** Okay. Thanks. I was going to mention. Yeah. Yeah.

**Chris Gammell:** The drone that did that is sitting just on top of that bookcase up there. It's been retired. Yeah.

**Dave Jones:** Yeah. Yeah. It might hit you in the head first now. Maybe.

**Chris Gammell:** Yeah.

**Dave Jones:** Tie that thing down.

**Chris Gammell:** Cool. Okay. See you, John. Cool. Thanks. See you.

**Yankee:** All right. Thanks, John. See you. Hey, that was a surprise guest. I didn't know it was coming on. The pop-in, man. Awesome. You got the pop-in.

**Dave Jones:** Yeah, I've sent out a couple of Twitter DMs and see if others... Right. This is starting to go on a little long here, so I'm getting towards my bedtime. But, yeah.

**Yankee:** Oh, yeah. Yankee land. It's only 1043 a.m. here. Mm-hmm. We don't want to end the amp hour at 555 episodes. I don't know. It'd be fitting end, wouldn't it? I think we should call it quits now, Chris. What do you reckon? Just like, yeah.

**Dave Jones:** Costanza quit while we were ahead.

**Yankee:** A what?

**Dave Jones:** Because, you know, Seinfeld. George Costanza. George Costanza, yeah. He would leave a party before anything happened because he'd be like, one good joke and he's out, you know.

**Yankee:** Oh, right. I don't remember that episode. I've watched probably every one, but I don't actually remember that. Yeah. Okay. It's been a while. Dave Caddy's a real competitor. Yes. Totally. Yeah. Yeah. But no, with the KiCad thing, no, seriously, even if it was a pro level, like even if it had all the pro level features that the pro level tools have, which it doesn't, but even if it did, or even if it could, you know, look, you can use, you can use KiCad for any PCB design you like, regardless of how high end is it. It's just...

**Dave Jones:** Going to do this for a bit. Here we go.

**Yankee:** No, it's shit. I could go back and use a tool from the 80s to do any PCB layout I want. It's just a matter of how efficient it is in terms of being able to do that. Anyway, so it's also the stigma of being a free tool. A lot of companies simply will not switch to it because they expect to have professional paid support available. They just won't buy into a free open source tool. They just won't do it. Simple as that. End of story. You know, regardless of how good it is and how good it gets. Unfortunately.

**Dave Jones:** I'm not going to probably trust you as the temperature of the market, but I'm sure you could post something on.

**Yankee:** Here you go. No, what it requires. I'll tell you what it requires. Okay. It requires a... It's a generational change thing. I do agree with that. So it's a 20-year thing. It requires a whole new generation. That's 20 years worth of engineers to get into the market. And then they bring it into companies. And then it becomes... Once it's a de facto tool within a company, it stays that way. Yes. Right? Yeah. But... No, but even you've talked about basic stuff. Like, you know, they change their file structure and stuff all the time and it breaks things. Does it not?

**Dave Jones:** Between major versions, yeah.

**Yankee:** Can you import a key CAD file from 10 years ago?

**Dave Jones:** Yes.

**Yankee:** Yes, you can. Yes. Mm-hmm. But you've got to import it?

**Dave Jones:** Yeah. Yeah, it's one way. Or something. It's a pull forward. It's not a go backwards.

**Yankee:** Got it.

**Dave Jones:** But you can go and download the old one and try and get that booted if you want to.

**Yankee:** Whereas Altium, you can actually pull in newer versions into older software. Did you know that? Yeah. Exactly. Right there. Right there is a feature key CAD doesn't have. And essential to a professional PCB designer, that's absolutely essential. Right? You know?

**Dave Jones:** This debate is just not that...

**Yankee:** It's just not because you're such a fanboy of key CAD. And look, I love key CAD too.

**Dave Jones:** Yes, I suppose I am a fanboy, but I feel like it's just... You know, like we've talked about many times on here before, it's a religion. Right? That's the way to talk about it. Oh, yes. Yes. It's a religion. It is a religion. Yes. Dave and I pray differently.

**Yankee:** Hey, I've got no loyalty to Altium. Let me tell you that. Right? Yes, I've been using it for... I started out with ProTel. Right? Well, actually, I didn't start out with ProTel. I started out with Kipik. Kipik was the guy's name. It was his last name. Can't remember his first name. Kipik. PCB design. Called PC Breeze. It was Australian software, but PC Breeze. I was actually going to do a video. I just thought about it recently. Going to do a video to see if I can still download that. You can download to Shareware. It used to be Shareware, if you remember Shareware. I remember Shareware.

**Yankee:** It used to be Shareware. And then you can pay, you know, if you actually liked it, you can pay for it. Send it to a PO box. Send it to a check. Send it in your 20 bucks. Yes, send it to check. And send in a money order for those in Australia. You know money orders. You know, so, yep.

**Dave Jones:** Oh, that's nice. Put that up there. Yeah.

**Yankee:** Yeah. I've got to put that up. Yep. So yeah. And I started out with PCB Breeze. You know, I've got no love. You know, I've got a love hate relationship without him. So, you know, it's not like I'm intensely loyal to Altium, but I have been a professional beat and PCB designer and I have worked at the company and I do know the market and I know the customers and I know the, you know, and I know the companies that use these tools. It's like, you know, yeah, it's Dave's right though. There you go. I don't know what I'm right about. It's a generational thing. Things will change in a few years and another tool will come around and start the whole thing over again. Just like Battlestar Galactica universe. Hand me right to the end there, Raker.

**Dave Jones:** All right. I think we're, I think I'm, I got to wrap up here, but.

**Yankee:** Oh, you got to wrap up.

**Dave Jones:** Yes.

**Yankee:** Should I continue? I don't know. I'm kind of on a roll here. Should I continue people or should I call it quits?

**Dave Jones:** I think maybe we, we, you start a new broadcast cause we got to actually package this up as a, as a podcast.

**Yankee:** Oh yeah, we do. Yeah. I better go to. Yeah. Yep. And we'll keep it under two hours cause then the YouTubes will, doesn't have to process it. Yeah. If it's over two hours, it, it, it limits. It only processes the first two hours.

**Dave Jones:** I did not know that.

**Yankee:** Yeah. Hmm.

**Dave Jones:** All right. Well, 555, man. Cool. We made it. Yep. It's basically 11 years. Actually, it's a little bit more than 11 years here.

**Yankee:** So 11 years, geez, get less for murder. Yeah. Yeah.

**Dave Jones:** Literally. Yeah. You said that in the first couple of years. I'm like, well, yeah. Yeah. I know. I know. I know. Like, yeah.

**Yankee:** It's now genuinely you get less for murder. You know, you get less for all sorts of things. Yeah. Yeah.

**Dave Jones:** Well, thanks to everyone who stuck around, who asked questions. We really appreciate that being part of the show. Cool. Yeah. We'll do maybe more of this in the future. Maybe I'll do a little better job of setting it up beforehand so people have the links. Yes. Beforehand. So I appreciate everyone who showed up.

**Yankee:** Although we won't be doing live ones, I don't think.

**Dave Jones:** Yeah. I mean.

**Yankee:** Well, it's like live shows as a show.

**Dave Jones:** Yeah. I mean, this would be the, this would pretty much be the, the extent of it, like a Q&A show once in a while.

**Yankee:** Yeah.

**Dave Jones:** Yeah. This is more people showing up than we've had in the past.

**Yankee:** Because we, we, we do know that most people listen to this as a podcast and a lot of people said they like the one hour. They don't like it when it goes over too much because they are sort of, they design their, you know, their workout or whatever, or their drive to work or whatever around a one hour episode. So it's, you know, yeah. So we are conscious of that. The amp hour keeps going.

**Dave Jones:** They have to circle the block a bunch. Yeah. Exactly.

**Yankee:** They've got to sit outside their house and listen. I've done that before actually. Yeah. Right. Yeah. Yeah. Yeah. I've done it too. Yeah.

**Dave Jones:** I don't think they're doing it for us, but if you do, and you've been in your car for 50 minutes, I'm sorry. Go inside, have a cup of cocoa, and we'll apologize somehow. Cool.

**Yankee:** Anyway, thank you very much for joining us.

**Dave Jones:** See you soon.

**Yankee:** Catch you next time.

**Speaker ?:** Bye. Thank you.
