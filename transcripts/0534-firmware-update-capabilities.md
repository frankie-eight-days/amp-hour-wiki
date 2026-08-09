---
episode: 534
title: Firmware Update Capabilities
url: https://theamphour.com/534-firmware-update-capabilities/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released March 14th, 2021. Episode 534. Sponsored by Mauser Electronics. Firmware update capabilities.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. What's up, nerd? Not much here, man. Just, you know, building stuff, writing firmware, stuff that you don't want to talk about usually, so no big deal. Firmware, come on. This is an electronics podcast, isn't it? Firmware's not real electronics. Do you have any electronics that doesn't have firmware on it these days?

**Dave Jones:** I'm curious. Yeah, well, no. That's always in the back of my mind. A recent project I'm thinking about, it's like, oh, can I do this without firmware?

**Chris Gammell:** I think there's benefits to it if you can. But I think about, like, power supplies with, like, you know, like, maybe an input's like a, you know, a potentiometer. There's other downsides to doing that sort of thing. But it's not many things anymore, you know?

**Dave Jones:** No, I know. It's like, you know, it's, yeah, like a new version of the microcurrent. It's like, oh, do I have to put a micro in it? It's like, you know. Yeah. Yeah, it's one of those things. Although, you know, like some auto-ranging stuff I'm thinking about doing, you know, at the moment, it's like, oh, yeah, can I, like, I can do that all in analog-y. It's just like, yeah, I have a bunch of comparators and I have some, you know, logic in there that decides when to switch and where.

**Chris Gammell:** Yeah, but then, you know, then your troubleshooting method is swapping out resistors. Is it right? That is a slow process.

**Dave Jones:** It's, you know, putting in chips and dead bugging them and, you know, oh, yeah. I know, but it's just, it's more elegant. It's more elegant.

**Chris Gammell:** I don't think I agree with that. I don't think I agree.

**Dave Jones:** You don't? No. You think it's more elegant to put in a little 10-cent micro and program it than it is to?

**Chris Gammell:** I mean, well, here's the thing, Dave. When I was working at test equipment companies, they didn't, you know, the auto-ranging was also, you know, it had indicators there. It had protection that was like fast switch stuff, but a lot of the range stuff is all controlled by an old processor anyway. So it's been done like this for a while in that example. Yeah, I know. I know.

**Dave Jones:** Goodness. You know, it's like, no. But still, does it have to be?

**Chris Gammell:** The thing is, you're not bad at writing it either. I mean, you write some Arduino stuff. That's no problem, but it's just, you just don't want to. I think you're out of the habit, right? That's the real thing.

**Dave Jones:** Yeah, it's just, yeah, probably. Yeah, I don't do it all the time. It's just annoying.

**Chris Gammell:** And I do find it's a habit thing. Like when I'm back into it, like I'm back in a cycle right now and I feel good. Like I feel like I know what I'm doing. I've got the latest tool chain going. I've got, you know, or the latest IDE, like all that stuff seems to work. And, you know, that feels good. But then, yeah, you take a break for like a month and just a month even. And it's just like, it all falls out the other side of my head.

**Dave Jones:** Yeah. And it's like, like on some machines here, I don't even have any tool chains installed for that kind of stuff because I haven't touched it since I last nuked my machine or something, you know?

**Chris Gammell:** Yeah. Yeah. I don't know if I told you, I've been playing around with having like a virtual machine. Like a, so I actually pay for VMware now because I was like really good low level connections. Like I used to use VirtualBox and like, eh, I didn't like it. But VMware is great for like low level connection to like a, you know, a USB to UART kind of chip or similar. Like it'll just pass right through, no problem. Yeah. Yeah. Yeah. So basically at that point you can have, you know, like people listening to this right now, the software people, yes, I know there's other things like Docker and all that other stuff. It's like, I don't want that. Not right now. And, but like, but having like continuity between machines, that part's kind of nice. Right. The downside is if they're running Windows and VMware, it's kind of clunky.

**Dave Jones:** Yeah.

**Chris Gammell:** It's doable, but clunky. So. Got it.

**Dave Jones:** I like to keep my development system so simple that it's like, man, even if I have to set it up, like it's just like stock, like I like keeping everything like stock install, you know? So I just download the latest version and just loading my source code and go, you know, there's, there's nothing fancy. It's not setting up everything like David did for the micro supply, where I did that video where it was like, you know, an hour just installing all these different types of software so that you can have this optimized software development environment, which I'm sure is great when you actually get down to it, but.

**Chris Gammell:** Right. But the complexity goes up. And so like more points of failure too.

**Dave Jones:** Yeah. Yeah, exactly. So it's, yeah. I just like using the stock standard stuff and then just, yeah, the source code just runs. It's not dependent on anything else. So. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Well, because I did that 1k video, like my thousand and 24th video was 1k, you know, where I took. Like 20, 20 year old, you know, assembly source code. And I simply installed for a pick. And I simply installed the latest version of, you know, pick, you know, MP lab X or whatever it is. Oh yeah. Right. I simply installed the latest one. And all I did was took that existing source code, cut and pasted. And with no experience in MP lab at all, I actually had that compiled and working with no issues in like five minutes. Like it worked like 20, 25 years later. Like, wow.

**Chris Gammell:** Yeah. That kind of continuity thing for like, especially for like industrial products and things like that, man, it's, it's nice to have for sure.

**Dave Jones:** Yeah. It's absolutely incredible. Like I thought, Oh, no way it's going to work first guy. There's going to be some quirk. And no, no, I just chose the old chip, which they don't even know. They probably don't even sell that particular one anymore or whatever. And it was like, yeah, it just, it just compiled and worked and actually made the binary. And then I used a programmer. I programmed the binary and boom, absolutely incredible. So, yep.

**Chris Gammell:** Yeah. That's great.

**Dave Jones:** Something to be said for keeping things simple like that. So the higher the complexity chain you go up, the more you're dependent on so many, especially if you're running like an RTOS or something like that, you know, you're running and all these, you know, stacks and layers of things and things like that. There's just so many things to break.

**Chris Gammell:** When I'm doing Zephyr stuff and you like do like a poll on the latest thing, it's just like, it's, I mean, I don't know. So you've probably never seen a Zephyr install either though, but like it pulls in all of these different like SDKs from different vendors. Yeah. I can imagine. Yep.

**Dave Jones:** Yeah. Right.

**Chris Gammell:** So it's all these, but basically it's all these packages for like ST and Nordic and like all of the vendors and NXP and all these other ones, you know, all they all have like their latest version of the code and you go and update Zephyr, which like references these. And it's just like, it's just like sitting there scrolling for like minutes and minutes of just pulling down the latest versions. Yeah. Wow. Although I did find out that the, so they, so Zephyr does have like a long-term stable release, just like, like Linux does, like Ubuntu does.

**Dave Jones:** Yep.

**Chris Gammell:** Another one of those is coming out soon too. I haven't, I haven't played with that in the past. I always use kind of the, the standard like main repository, but, but yeah, it's interesting. Like how they're moving to that model.

**Dave Jones:** Got it. Ah, bloody software tools. They just, I mean, well,

**Chris Gammell:** the other thing is you could find someone to work on it again. Right. I mean, you worked with David, of course, and the other stuff, but.

**Dave Jones:** Oh yeah. No, if I wanted to pick it up again. Yeah. I wouldn't do it myself. I just get someone who knows those systems and go, Hey, you know, here it is. Go for it. They'll, they'll, they'll, they'll spend a day or two coming up to speed, you know?

**Chris Gammell:** Right. You become like a project manager at that point, which is, you know, its own set of challenges, but might, might fit better for, for what you're trying to do.

**Dave Jones:** Yeah, exactly. So anyway. Yeah. But it's always in the back of my mind. I can't help it. It's the elegance thing of like, Oh, can I just do this without a micro? It's, you know, I, I, I can't, sue me, sue me. Yep.

**Chris Gammell:** All right. The paperwork is on the way. All right.

**Dave Jones:** We unfortunately have to start off this week with some sad news, which just came out last night that Gary Johnston, you may not know the name, but anyone in Australia, Gary Johnston, founder and CEO of Jaycar, one of our, well, there's only two remaining electronic stores, like ones where you can actually go in and actually buy parts. Right. Right. Yeah. Yeah. He sadly, sadly passed away yesterday. It was only 71, which is not old these days, you know, but yeah. Right. Yeah. Right. Without, yeah.

**Chris Gammell:** Like septagenarians and such or about that's, that's 70, whatever. What's a hundred? Octagenarian, nonagenarian. Decagenarian or something? Centagenarian. Centagenarian. Okay. Yeah. Probably right. Century, right? Yep.

**Dave Jones:** And it's sad because like, I always wanted to interview him and it's like, oh God, I should have taken the opportunity. You know, he called me up a couple of times over the years to discuss stuff. And it's like, oh yeah, I should, you know, arrange a range to go meet him and have an interview. And yep. Never got a chance. Unfortunately.

**Chris Gammell:** Yeah. Is there, maybe there's a stuff that people could watch or like other, other interviews of him online. Yes.

**Dave Jones:** I will link one in. Cole. Okay. Cole von, von Moller. Oh, okay. Did a big interview with him. He released that last year, I think. So he's got some extra footage, which he may actually release, but it's not really related. But yeah, it's not like a 45 minute interview talking about, you know, how he founded the company and all sorts of stuff. So we will link that one in.

**Chris Gammell:** What is the, what's the status of J-car these days in Australia? I mean, are they still, still kicking?

**Dave Jones:** Yeah. Yeah. I've got my, I go down to my local J-car store when I need, you know, a transistor or a chip or something that I need or some parts, something like that. Yeah. I still go down there and they still sell the parts. Of course, they've got the farty novelty gadgets and everything else. That's how they actually make a living. Right. And, you know, and the flashy lead displays and all that sort of stuff. But yeah, they, they still have all the, all the little trays behind the counter and you can go in and you can get your 4,000 series CMOS chip, you know.

**Chris Gammell:** And it's probably the same ones that were on sale when you were a kid too. Yeah. Yeah.

**Dave Jones:** Exactly. Yeah. The same stock. That's it.

**Chris Gammell:** Might as well still work. Yeah. I mean, that is, that is nice to have. I mean, it's, it's tough to keep that business alive, you know, like, well, obviously we talked about fries two weeks ago, right? Fries is gone now. Yeah. Yeah. They're gone.

**Dave Jones:** Yeah.

**Chris Gammell:** So my micro center is probably my only real thing that I have.

**Dave Jones:** So did, did fries actually have individual chips? I can't remember.

**Chris Gammell:** They had like, I think some blister pack style stuff. Right.

**Dave Jones:** I thought they might've.

**Chris Gammell:** Yeah. It only would have been, it wasn't like, like Radio Shack was where there's drawers. I think it would have been more like, so if an Adafruit or a SparkFun was selling like a loose chip, you could probably get it like that. So definitely harder to get and definitely pricey. Yep. You know, when you're in a bind, that's what you need. So yeah, whatever.

**Dave Jones:** Anyway, Carl put on Twitter and I retweeted it. It was like Gary Johnson famously said, while blood is coursing through my veins, I will, you will still find a one meg resistor on the shelves at Jcar. It's like, you know, so yeah, I, hopefully that doesn't end with his passing. So yeah, I hope it doesn't change, but it's amazing. Even a small country like this, we have two Jcar and Altronics. Yeah. Yeah. You can go into actually Altronics is technically better because they do more surface mount stuff as well. You can actually go in there and buy like surface mount parts in like, you know, 10 per icon of tape. So yeah, you can actually get surface mount stuff off the shelf. So, but then again, yeah, well, of course we've got RS components and Farnell, of course. I still call them Farnell.

**Chris Gammell:** Yeah. I think it all comes down to, to, to density, population density. Right. So I think living in Sydney probably helps. And then also the fact that like, because Australia's, you know, a limited size, there's probably a pretty realistic conversation internally about like growth. And then they didn't get out over their skis and like, you know, do the Radio Shack thing where they have 4,000 stores and they tried to grow like a, you know, a large conglomerate does. Yeah. And it's like, oh, then when things go south, it's like, they have nothing to support that huge, that huge overhead they have. So yeah, Jcar probably just was doing a little bit, a little bit more conservatively and that's what helps them stick around.

**Dave Jones:** So yeah. They've only got like 10 stores. Oh, they, yeah. Like they had small like network dealers where, where if you were like a repair shop or something, you could be like a Jcar satellite dealer or whatever the term was where you could order stuff, you could order stuff in and, you know, do it. But yeah, that was before the internet and then the internet came along and well. Yeah. Yep. So.

**Chris Gammell:** Wait, what happened next, Dave?

**Dave Jones:** What happened next? Anyway, but yeah, it's, it's always handy, but I, I have always wondered why they still do it. It's, it's because guys like Gary Johnston was still in charge and they said, yeah, I don't care. I want, I want all these. I don't care about the profits.

**Chris Gammell:** I care about the experience. Yeah.

**Dave Jones:** You can go in and you can buy your 10 K pot. You know, they go in there and they have the drawers. You can ferret through all the drawers. There's all the connectors, all in the little drawers that you can pull out and walk, you know? Yeah. Yeah. Yeah. It's great. So handy. But yeah, no, you can't make a business doing that. It's why they have to sell everything else. So that's right.

**Chris Gammell:** Yeah.

**Dave Jones:** Still.

**Speaker ?:** Yeah.

**Chris Gammell:** But they're, they're still around versus a radio shock, which is not.

**Dave Jones:** They're still around. They're doing great. They sponsor football teams here and they do, you know? Yeah. Yeah. They're, they're, you know, fairly big because like Jaycar is the, like people know they've done branding fairly well, you know? And especially by sponsoring, you know, football teams. Cause here in Australia, like, you know, football's a big, huge thing. And it's like, yeah.

**Chris Gammell:** Australian rules football. Yeah.

**Dave Jones:** Well, that league actually.

**Chris Gammell:** Oh, whatever. Yeah.

**Dave Jones:** Whatever.

**Chris Gammell:** Come on.

**Dave Jones:** Anyway.

**Chris Gammell:** Hey, hey, hey. If anyone's going to bastardize the name football, it's Americans stealing it from the Europeans. Okay.

**Dave Jones:** Oh boy.

**Chris Gammell:** Yeah.

**Dave Jones:** And yeah. So they've, they've, they've done well. So people who, you know, like Tandy had that name and then Dick Smith had that name. Dick Smith gave up parts like early two thousands, probably something like that. That's the last time they, you know, they, they stopped selling parts. They were taken over by the, well, well, the suits finally came to the conclusion that nah, this is bullshit. You know?

**Chris Gammell:** I always felt like they were, they were closer to a, like a radio shack. I guess Tandy as well. Right.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. Tandy radio shack. And it was, it was Tandy here. Of course, there was no radio shack name. Uh, and yeah, it was like, and you get the little blister packs and stuff like that from, from Tandy, but they stopped that. Oh, probably the nineties, you know, something. Oh no, probably into the two thousands as well. Maybe. But yeah, once, once those two, once those ended, then people knew, you know, like, cause Joe average might need, you know, the connectors broken on their widget. Thing. And Joe average might have a soldering iron at home or something, you know, or they go, Oh, okay. I, yeah. Like it's really expensive.

**Chris Gammell:** Better hope it's a 2.5 diameter, a barrel jack. Yeah. Yeah, exactly.

**Dave Jones:** They go in there and buy their 2.5 mil barrel jack and they, you know, yeah. And they actually repair their own thing. So it's, that's been the go-to place.

**Chris Gammell:** Hard to keep a business going over time, but yeah. Yeah. I get it. Yeah.

**Dave Jones:** I don't know how our tronics still do it. Cause they've technically got a much better range than Jaycar yet. They're not known, but they've only got like, there's one store here in Sydney and there's like one store in every major capital city. So there's only like five stores Australia wide or something.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** There's not that many, but still, you know, I don't, they don't have the same branding as Jaycar do. So yeah. Fascinating. Anyway, rip Gary Johnston.

**Chris Gammell:** Yeah. So it's too bad.

**Dave Jones:** Yeah. Let's hope they keep it up.

**Chris Gammell:** Well, speaking of companies that are no longer around, I mean, obviously Jaycar is, but we were talking about the other ones. Who's, who's gone tits up this week. MIPS. MIPS actually it's the opposite. They're, they're back from the dead. So MIPS is the, they make the core that was in like a bunch of microchip stuff. Right.

**Dave Jones:** Right. Yes. Yes. Yeah. The Pika 32 is based on the MIPS architecture. They famously chose the MIPS architecture over the ARM architecture. Right. Right.

**Chris Gammell:** So the news this week is that MIPS is now risk five. Guess who's back. Back again. Yeah. Right. Yeah. I don't quite understand this. I mean, I think there must be some kind of business behind it. And now they're basically like, well, we can't, we can't develop the technology any further on the MIPS side of things. Yep. And the official statement says, we're developing a new industry leading standards, eighth generation architecture, which we will be basing on the open source risk five processor standard, the ISA in this case.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. That's weird, huh?

**Dave Jones:** But ironically, risk five, risk five or risk V? We did this argument.

**Chris Gammell:** We've done this every time. Yeah. It's five. Yeah. It's risk five.

**Dave Jones:** Risk five is based on MIPS.

**Chris Gammell:** Nope.

**Dave Jones:** So apparently it's a, it came and they, you know, that's where it came from apparently. Or that's what they were trying to do better. They were trying to do a better MIPS. So apparently that's, I'm sure. Are you sure? Yeah. I'm pretty sure. Pretty sure.

**Chris Gammell:** So, I mean, the ISA is not, I mean, so like, remember the risk five is the instruction set architecture. Yes. And so.

**Dave Jones:** Reduced instruction set. That's what risk stands for. Risk is reduced instruction set.

**Chris Gammell:** Sorry. What did I say? I said risk instruction set. I don't remember what I said. Yeah.

**Dave Jones:** Anyway. Yeah. Yeah.

**Chris Gammell:** Yeah. It's interesting that it's like, this is especially coming out of the bankruptcy piece. So I don't know. It's. Yeah. We'll see how that goes.

**Dave Jones:** They, you know, there's still money to be, when there's money to be had still, they'll just spin and re-pivot and the CEO, the, the original MIPS CEO is still there or something, isn't he? Or something like that. And they're, yeah, they're doing what a risk five now. So, okay. But under the MIPS branding.

**Chris Gammell:** Yeah. So. Yeah. What's, what's interesting about the, so like taking this on, I think one, one thing you would gain, you would gain from this is basically all the compiler support that's already there for risk five stuff. Like, and I'm just continually surprised by this. I was just. Well, it's not that MIPS didn't have, have it. Right. But it's, it's a JSON, right? So if you had a bunch of tools built for risk five, because all these people are building out tool chains that support it or similar. Right. Yeah. And then MIPS requires another because they have a different instruction set. It's like, even though it might be branded MIPS, it's like, then could start to use the tools that are out there. So compilers and similar things that, that basically have the same instructions at the lowest level.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** So I feel like this could be a money saving, you know, like just thinking about how, how these companies are approaching risk five stuff. It's like, it's a money saving thing, if nothing else. Right. Okay. It's, you know, there's a standardization piece, but then from a business perspective, it's, I'm excited about it. If people are coming in and they're like, yeah, we're going to standardize because it's cheaper. And it's like, great. Fine with me. You know, I think that that's, that helps to build instead of like these vertically integrated companies, it starts to build more like crossover type stuff.

**Dave Jones:** Right. Now, the interesting thing about this is people might think, oh, what happens to the, what happens to the microchip, uh, pick 32 that's based on the MIPS architecture. Oh, like, cause I'm going to, no, I'm sure they're fine. I mean, I might actually, uh, contact microchip and see what the, see what the deal is. Maybe we can get a, maybe we can get them on the show.

**Chris Gammell:** Cool. That'd be great.

**Dave Jones:** Yeah. And you know, Steve, uh, Zangy butchering that last name, I'm sure. Give Steve, Steve a shout. Yep. And, uh, see what, yeah. See what their future is and stuff like that. Obviously they would have, you know, a company like that would not have been dumb enough to sign an agreement that was reliant upon MIPS staying solvent. Right. It was like, we're licensing your architecture. We want it forever. Here's the money. Bugger off. If you guys go under, that's your business. We don't care. We're still making our MIPS chips. It's like. Yeah.

**Chris Gammell:** I felt like MIPS was closest to ARM. I mean, I'm, I'm sure I'm wrong about this stuff, but like in terms of like the business model, in terms of licensing and generating IP that was being used elsewhere. Yeah. They weren't, they weren't building MIPS processors or anything like that. It's just the architecture.

**Dave Jones:** You could not buy a MIPS chip that I'm aware of.

**Chris Gammell:** Well, there's some tie in with MIPS. I thought it was a name conflation, but when Forrest Mims was on the show, he mentioned something about MIPS. Did he? Yeah. Really? I'm looking at it. Wow. There was something. It may have been just a conflation of the names, but I thought, I thought there was something there.

**Dave Jones:** Okay.

**Chris Gammell:** Oh no. MITS. Oh, MITS.

**Dave Jones:** MITS. Yes. The, yes. That, uh, Ed. What's his name? Sadly, he's no longer with us either. He designed the. Ed Roberts. Ed Roberts. Yes. Ed Roberts. That's right. MITS.

**Chris Gammell:** Yeah. I totally knew that the whole time, everyone. I just wanted to do a call back to the Forrest Mims show because we had Forrest on the show.

**Dave Jones:** That's why I was surprised. That's like Forrest MIPS and, uh, Forrest Mims and MIPS. That didn't make sense. MITS. Yes. Yeah. MITS.

**Chris Gammell:** You know, there's just so many, there's only so many acronyms you can have. Yes. And we're talking about Radio Shack too. So Forrest was in my head, I'm sure.

**Chris Gammell:** You know. No, MITS.

**Dave Jones:** MITS stood for, um, something instrumentation and telemetry systems.

**Chris Gammell:** Mike. That's right. Micro instrumentation and telemetry systems.

**Dave Jones:** Micro instrumentation, telemetry systems. Yes. MITS. Yeah. Good memory. Yes. Yeah. Yeah. Well, I know my computer history. That's all tied in with the Altair and, you know, the whole thing. And, and technically Bill Gates was not an employee of MITS, whereas Paul Allen, co-founder of Microsoft, he, he technically was an employee of MITS at the time. So, but Bill Gates, yeah, he was never actually employed by MITS. So back in the early Microsoft days, because yeah, they, they basically moved to Albuquerque to be next door to MITS because that was their one big customer.

**Chris Gammell:** It was like, was that the, was that the one that you were, were you refurbing an Altair recently or was that a different computer?

**Dave Jones:** No, not, not an Altair. No.

**Chris Gammell:** What were you refurbing?

**Dave Jones:** Uh, I was, was I refurbing something?

**Chris Gammell:** You did something with like a display on some like old computer.

**Dave Jones:** Oh, that was an old, uh, compact portable. Is that the one you're talking about?

**Chris Gammell:** Oh yeah, probably. Yeah. Yeah. Yeah.

**Dave Jones:** I've got, still got that on my bench. Yeah. No, that's good. That's an IBM compatible thing.

**Chris Gammell:** Oh, got it. Okay.

**Dave Jones:** Yep.

**Chris Gammell:** So it was like later, later. We're talking mid. Got it.

**Dave Jones:** Early to mid eighties. Not, uh, yeah. Mid seventies. Yeah. But yeah. Yeah. A lot of people don't know that. Is that Microsoft?

**Chris Gammell:** Dave, come on, man. You're, you're all pre you're, you're in pre Chris era here. Right.

**Dave Jones:** Yeah. I know. Yeah. Yeah. You weren't even born when, uh, Microsoft moved their head headquarters to Albuquerque, which is, which was next to a strip joint. I do believe. Oh, really? Yeah. Yeah. Yeah. So yeah, there's many books on the history of, of all of this stuff, which is great. Yeah. So, yeah.

**Chris Gammell:** Yeah. It's crazy thinking about that stuff too. Like people in, you know, those crossroads of like technology, whatever too, it's not like they were like thinking it was going to, you know, they knew it was exciting and this big thing, but they didn't know that they were going to like make. Oh no. History books about that kind of stuff too.

**Dave Jones:** They were just doing cool stuff. They were just nerds doing cool stuff, you know?

**Chris Gammell:** Yeah, exactly.

**Dave Jones:** Yeah.

**Chris Gammell:** Nerds hanging out.

**Dave Jones:** And they, and they followed where the action was. It was like when the action was in a Silicon Valley, you know, before it was even coined Silicon Valley, that's where you went. If the action was in Albuquerque with, uh, mitts and the Altair, that's where you went. You know, it's like, yeah. So you just follow the, uh, nerdery.

**Chris Gammell:** Yeah. I wonder where the nerdery is these days. I, I, I have to, I have to imagine I'm not, I don't have my finger on the pulse of it. I think these days, at least in the U S everybody's at home. So there's also that.

**Dave Jones:** Well, here, well, can we float this? Can we float our opinions on this? What is the future of Silicon Valley?

**Chris Gammell:** Well, no one's ever come up with this before. No, nor, nor, nor where will be the next Silicon Valley? I've never seen any headlines that say that.

**Dave Jones:** It's like a bit, it's I like, it can't go back to the way it was, you know, like.

**Chris Gammell:** You mean a post post COVID?

**Dave Jones:** Sorry.

**Chris Gammell:** I said like a fruit orchard. Like it started out as.

**Dave Jones:** Right. No, it's like where like, if, if your company wasn't there, you did not exist. Whereas now that's not really, you know, that's not really the case. I mean, you've got rocket labs. They're in New Zealand, you know, launching rockets in bloody New Zealand and they don't have to be in near SpaceX in bloody California to make it happen.

**Chris Gammell:** Right. Yeah. I think, I think that there is a general distribution of technology. I think there's that sort of thing, but I, I push back against the notion that people are going to stop doing the office thing.

**Dave Jones:** Oh, then they're not going to stop doing it, but will company, will new startups fill the compelling need? Like if you're a startup in the U S you simply went to Silicon Valley. If you're a tech startup, right. You wanted your presence to be in Silicon Valley. But is, is that, is that now the case?

**Chris Gammell:** Is that still San Francisco too? Right. I mean like, yeah, I mean there's. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Right. I don't know. I think, I think it all comes down to like talent bases, right? Really? You know, people think about the geography a lot more than the talent base though. Like talent and then money, right? That's the two things that I think about. And I don't think Sand Hill road is going anywhere. That's where like all the VCs are. Right. You know, there's, there's more money out there, you know, well money's so cheap these days that it's like, okay, there's tons of investment capital everywhere, but it's like, but that's still where a lot of the tech stuff happens. That's where like, if you want to really get frothy, like valuation craziness, I think that you still have to at least visit there. Right. Whether or not you have to like, yeah. Plop down a, you know, uh, and, and actually, yeah.

**Dave Jones:** An expensive rented office there with wanky furniture.

**Chris Gammell:** Yeah. Right. But I, I think there's a lot of talent in the area still. I just think that.

**Dave Jones:** Oh, of course.

**Chris Gammell:** You know, I, I think the interesting thing will be, okay. So all these, all this migration has been happening because of COVID and that's going to drive some of the, at least the short-term effects. I think, you know, people buying houses more in the suburbs or just out in the wilderness. You know, um, I've been watching people, um, Caleb craft from make, he, uh, he actually just posted a video about his, uh, using his, uh, star link and he was like in rural Missouri. Right. So it's like, you know, like, so people like Caleb can get much better connectivity than kind of being more further out. So I think there will be more normalized, um, remote work, but I think from like a headquarters standpoint, I think, I think it'll all continue to continue to coalesce because I think that if people are chasing young talent, young talent still wants to be where other young people are and that cities. And so it's just going to keep doing that. Maybe it'll distribute a little bit more into other big cities, but I don't think, I don't think that it'll appreciably go away.

**Dave Jones:** I don't think it'll be the showstopper it once was, if you really don't want to have an office in Silicon Valley, you don't have to be successful. It's like, right.

**Chris Gammell:** You might, you might be still flying into, you know, San Jose airport to go visit some of the money bags, but like, I don't know.

**Dave Jones:** Well, they're all moving to Texas now, aren't they?

**Chris Gammell:** Everyone's in Texas, you know? Yeah. Yeah. Texas. Yeah. I think, uh, Silicon Valley is, it's a terribly laid out area too. Like it's beautiful. Like the weather is amazing there, right? It's like, yeah, yeah.

**Dave Jones:** Yeah. It's great.

**Chris Gammell:** Really nice weather and like Sunnyvale and stuff. But, but it's just like, it's like concrete city. I mean, like, it's just like, you have to drive a lot of places. Maybe I just didn't visit the right places. Don't kill me if, if you live there and you love it, but.

**Dave Jones:** Yeah. No, that's the impression I got. Yeah.

**Chris Gammell:** It's, it's not a city to me. It's like, it's, you know, San Jose is a city, but like Silicon Valley is just like so sprawling that it's like, you know, it's, it's not quite suburbs because it's so built up, but it's not a city. It's not, you can't live there without a, you can live there with like a train and a bike maybe, but like, but like cars are kind of the, the, the name of the game. It feels like. Got it. This and more on the Dave and Chris lifestyle podcast. Here in the amp hour, we're interested in sponsors that help us educate our listeners. Today. Today, we're talking again with Paul Gulotta from Mauser Electronics. He's going to discuss wide band gap semiconductors. And I asked him about how they're different from other semiconductors.

**Chris Gammell:** Traditionally, people have used silicon, but silicon has a band gap in the low ones. What we're really talking about today is wide band gap products that have been developed that have a band gap in the neighborhood of three to four electron volts. And so some ones that are very typical that are being employed today include silicon carbide, also called SIC, S-I-C, and gallium nitride, also called GAN, G-A-N. So let's just say we're, we have three times as much electron volts available to us. What that means physically when it comes down to what's happening with electronics is that they're able to achieve higher switching frequencies so they can be turned on faster, on and off faster. And anytime we can increase the switching frequencies, we're going to be able to operate everything that we're doing downstream in the design at higher speeds.

**Chris Gammell:** So we're driving higher frequencies, but why does that matter? What are the applications of these new types of semiconductors?

**Chris Gammell:** An important one that's really driving a lot of the train is automotive. Everybody's trying to store electronic energy in the car. So that's a huge renewable energies, things like solar and wind and those types of things. Those require power inverters, things to change what's coming in and get it into an electrical format as well as energy storage. But there's also things like 5G that's coming on to give us increased capabilities in terms of how connected everything is, how fast they're operating and wide band gap helps that. Specifically, in something like 5G, one of the technologies that's underpinning that is a thing called massive multiple input, multiple output. That's often called MIMO, M-I-M-O. And this type of technology will be enabled by wide band gap technologies. You can also use these products in industrial. Since these parts and these technologies and these products do that more efficiently, these help industry be more efficient to produce things for lower energy costs and the like.

**Chris Gammell:** The higher band gap allows for higher switching frequencies, but it took me a second to understand that this would actually make for lower switching losses in converters and similar. Paul explains it more.

**Chris Gammell:** We can only make silicon turn on and off so fast before a bunch of residual effects essentially compromise its performance and make it more difficult for us to achieve the necessary switching frequency. Another thing that also happens with that is even if we do lots of external things to silicon to make it perform at its best, in order to do that, we have to add a variety of products, things like capacitors and other various things to optimize that. And that takes up size and it takes up additional costs and complexities just because you have to do all this optimization to try to make the silicon do its very best. With wide band gap, you get to use less components. And so that simplifies everything.

**Chris Gammell:** To learn more about wide band gap semiconductors and how you can use them in your designs, check out the Mauser Electronics application page on the topic. You can go to theamphour.com slash band gap to get a direct link to that page and learn more. That's theamphour.com slash band gap. And now back to the show.

**Dave Jones:** Speaking of changes, a friend and guest of the show, Lewis Rossman. Oh yeah. Has just announced he released a video last night. But surprise of absolutely no one is that he's now changing. He's basically changing his full-time job.

**Chris Gammell:** Oh yeah?

**Dave Jones:** Pretty much. Yeah. He's announced that. Paraphrasing. But yeah, we'll link in his video. You can go to his announcement video. It's like, here's my change in life. This is what I'm doing as a full-time job. Now he's going to spend the next two years. Now, if you don't know, real estate. Lewis Rossman, of course, does his repair videos, right? He's got his repair shop in New York and he does his famous repair videos. He does his famous real estate rants. He does, you know, all sorts of, you know, business rant videos. Very popular, right? And so he's decided, nope, not doing that anymore. What is more important? What's more worthy of my time? I'm going to spend the next two years fighting for the right to repair. Ah, okay. Thing, right?

**Chris Gammell:** He's taking that full-time thing.

**Dave Jones:** He's taking that on full-time. That's going to be his focus. I don't think he said he's going to stop, like, doing videos on other stuff, but it might just be an occasional hobby thing or something, as it always has been. That's great. No, he's going to focus on that full-time.

**Chris Gammell:** Yeah, no, I think that mission in life is great. What's interesting about the right to repair stuff is, like, I kind of feel like the biggest impact you could have is to go and, like, lobby the EU. Because, like, if the EU does something, it just becomes, like, tentacles everywhere. Yeah, like the USB standard stuff. Like, man, you know, people complained about that at first, but, like, I love it. I, man, I am so not sick of having, do you remember, like, every phone having, like, just a separate charger standard? It was so bad.

**Dave Jones:** Yes, I know. Oh, it was, yeah, I know. It was a nightmare.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. And now it's all USB. Well, now it's like, well, there's, you know, is it USB-C? Is it USB-C or is it USB micro? You know?

**Chris Gammell:** I don't care. Yeah, exactly. It's one or the other. Yeah, yeah, exactly. You know, and then Apple has their own thing still. I don't know how they get away with that, but, like, the, yeah, just that, that kind of, like, driving standardization. Like, you know, people can have all kind of political views of whether or not that's good or not, but, man, coalescing around cheaper hardware is, that is my politics.

**Dave Jones:** No, I just had to ferret around yesterday for a plug, a suitable matching plug pack for my old Canon camcorder. Yeah, yeah, yeah. Oh, it's like, oh, God. Yeah. Yeah.

**Chris Gammell:** Yeah. It sucks.

**Dave Jones:** Yep. No, they couldn't just use a standard DC barrel jack. It was this little mini barrel jack thing, and it was like, you know, some oddball voltage or something.

**Chris Gammell:** Yeah, it's like a 0.5 millimeter inner diameter or something crazy.

**Dave Jones:** So, yeah, something like that, right? Yeah. And, ah, it's a pain in the ass. So, anyway, yeah, so that's a good focus because he doesn't want, right, because at the moment, right to repair is, like, kind of like his name's associated with that. And he said he's got so much baggage that he doesn't want to damage the movement because people don't want to, you know, dig up all this stuff on him because he's said a lot of controversial, you know, in quote marks, right? Yeah. Controversial. It wouldn't be hard to pull up a controversial quote from Lewis Rossman. Let's put it that way. Yeah, I think that's right. And, yeah, and, you know, and so he wants to now, like, I don't know the mechanisms of it behind it, but apparently there's some money in play now behind it. There's been money put behind it, and he wants to make it more formal so it's beyond him. He wants to make it like a big formal movement kind of thing. Yeah. That's great. And although he'd be driving it, this would be his full-time job and commitment, he doesn't want it to be focused around him as a personality anymore.

**Chris Gammell:** Yeah. So, yeah. Yeah, and I think you have to make it an idea instead of a person, right? Yes, yes. That's true of any movement, I think.

**Dave Jones:** That's it. So, yeah, yeah, it's great.

**Chris Gammell:** I mean, how do you feel about the whole right to repair thing? I mean, like, obviously we had Lewis on the show twice now.

**Dave Jones:** And we had him one dedicated to the right to repair episode that was very popular. We'll link that one in because he goes through a lot of the stuff. Yeah, yeah. And, yeah, I think it's, no, we should damn well demand this of all of our products. You should be able to have a schematic. There was an argument on his recent video. It's like, schematics or die. You know, it's like, you know, if you don't provide me the schematics, forget it. You are not. I don't care what other token steps you take towards right to repair. It's like, well, you don't give me the schematic. Screw you, right? We are not going to promote or endorse you as being repair friendly. Yeah. It's like.

**Chris Gammell:** Yeah, that is the line in the sand.

**Dave Jones:** Yeah, that is the line. That is the bar you have to, minimum bar you have to get over to be able to, you know, say that you're doing something. It's kind of like open hardware. Like, you know, there's a minimum bar that you need to jump over to call yourself open hardware.

**Chris Gammell:** Yep.

**Dave Jones:** Yeah. It's the same, same for right to repair. And I think that's a good baseline having, having the schematic available. But then again, you could argue that the, well, the schematic's useless. Then if you serial number parts, like you actually tie parts into serial numbers so that you can't even salvage a part from another unit and put it in the, and put it in a repair unit, it won't work because it's been serialized. Right. And it's baked into the software and stuff. Oh yeah. We're open. Here's the schematic. Good luck. You know? And it's like, you can't buy the chips because they're customized. Right. Or, or, you know, TI or something. Apple will use a TI charger chip or whatever. Right. And they won't sell it to anyone else except Apple.

**Chris Gammell:** It's like, well, holy crap.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** Yep.

**Dave Jones:** So even if Apple actually released the schematics, if you can't buy the parts or the serialized, well, no, you're screwed. So, you know, there's gotta be some minimum thing there. So.

**Chris Gammell:** Yeah. Yeah. I wish there was some kind of push to do more custom or not custom, sorry. Uh, like standardization on footprints too. Like, you know, like a, like a default fallback footprint that everything had. Now again, this is going to come into that.

**Dave Jones:** No, it's the, it's the utopia. That's never going to happen. There's always going to be reasons why companies want X footprint. You know, there's just, that's, that's why they exist in the first place.

**Chris Gammell:** If we're talking about like things that we want, that's what I want. I know it's not realistic, but that's what I want.

**Dave Jones:** Fair enough. Okay. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Oh, goodness. Anyway. Yes. Yes. The right to repair thing. It needs to be. And unfortunately it's a lot of, uh, it has to, this is one of the things that, well, you can for like put a press public pressure on companies to do it. And those that do it will get actually rewarded with sales. Right. That's the, that's the idea. You shouldn't need government intervention for this sort of thing. The free market should take care of it. You know, you should be able to put enough pressure on companies that, Hey, we won't buy your product unless I can repair it myself. And, and the first company that comes out and says, Hey, look, we, we, we, we released the schematic. Here's the parts, or you can buy them from digi key or whatever, you know?

**Chris Gammell:** Yeah. It could be a differentiator in the marketplace. Right.

**Dave Jones:** So the first company that do that, you can potentially do this without legislation. The market can do it, but ultimately no, you know, companies just aren't that easily convinced.

**Chris Gammell:** Right. Right. There's probably not enough, enough of a push yet, but yeah, I think that's what Lewis will be working on.

**Dave Jones:** Yeah. So you've got to lobby and they've had some wins. They've had some wins in the US and in the EU too, I think. And there's a right to repair thing going on here. So maybe I should investigate that more. Although I'm not in the repair business as such, like, uh, you know, that's actually Lewis's bread and butter, you know? So, but, but still with my audience, maybe I can help out. So never know. Yep. Yeah. That'd be great. But ultimately, yeah, it will require a combination of government. Government legislation, as you were saying, like the EU coming in and mandating that, yes, all new mobile phones must use a USB for charging. None of this, none of this proprietary rubbish anymore, you know? And that, and that got the job done. Right. So yeah, hopefully something, yeah. Similar sort of thing, but it's, it's, it's going to need both. It's going to need both solutions. But yeah. No. See, I don't know. Like if I was a marketing person at these companies, I'd go, look, no, no other companies. Like marketing is doing something nobody else does. Right. Being the first, making a big splash. Right. That can.

**Chris Gammell:** But, but I think internally, if you were like, Hey, I know how to get more, more views or more, more attention. We should give away our IP. And it's like, regardless of whether or not the fact that we believe that a schematic is truly IP.

**Dave Jones:** Yeah.

**Chris Gammell:** It is still IP. Right. I mean, like it's, at least it's perceived as IP internally. I think that's the big thing. So I think that's probably the uphill battle. It's like, your schematic is not that interesting. You know?

**Dave Jones:** That's a t-shirt right there. Your schematic is not that interesting. Yeah. Right. But give it to me.

**Chris Gammell:** Yeah. Right. Right. Yeah. That could be the back.

**Dave Jones:** Yeah. It's like, no, cause there's so much that goes into copying a product. And it's like, it's, it's showing that even if you don't release the schematics, well, China can just, you know, these factories in China can just copy your product anyway. Right. So it's not, you know, eh, it isn't really helping, but. You know, it's, it's not like nobody's talking about actually releasing the original source files and, you know, things like that, or, or, or release, you know, the PCB files to make it trivial for a company to copy. Right. Exactly.

**Chris Gammell:** Yeah. Like what is, what is the real goal of the thing?

**Dave Jones:** Yeah. Well, that's, that's the open source hardware debate as well. It's like, well, how much do you give away? Is a PDF schematic enough? Are the original, you know, like, uh, the original schematic and files, schematic and PCB files. What do you do about the bomb? What do you do about your supplier information? Do you give everyone everywhere, you know, make it a turnkey thing so that anyone can just, you know, turn a key and manufacture your product. It's like, how far do you go? And well, that's up to each individual.

**Chris Gammell:** And you can go and debate all this on April 9th, uh, open source hardware summit is coming up on April 9th. Virtual. I'm sure.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. It's virtual.

**Dave Jones:** Yeah. So if it was here in Australia, it'd be the real deal.

**Chris Gammell:** Yeah. But nobody could get there. We'd be quarantined for two weeks first.

**Dave Jones:** Everyone in Australia could go, you know?

**Chris Gammell:** Oh, okay. Well, you should do one, man. Right. Take advantage. You know, like you could, you can get together. That's I highly recommend it.

**Dave Jones:** I could start up the EV blog meetup again. Yep.

**Chris Gammell:** There you go. Yeah. Yes, you could.

**Dave Jones:** I don't think there's any limits. I could, I could do the EV blog meetup and cram 500 nerds into a room and. Yep. Exactly. With zero masks. Spitting all over each other, you know? Yeah. Yeah. Yeah. Yeah. Yeah. Salivating over all the latest hardware. And there you go. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Possible. Yep.

**Chris Gammell:** Oh boy. Anyway. Yes. Lewis. Cool. Yeah. Yeah. We'll definitely link in that video.

**Dave Jones:** Yep.

**Chris Gammell:** Something you were mentioning with that. I think. Oh, you were mentioning the, the replacing the connector on a thing. And I was thinking about one of my recent designs. I did something that like, I don't usually do on prototypes, but I'm really, really glad I did. And that is, can you, can you guess what I did on my recent prototypes? No. No. I designed in wire to board connectors. Whereas normally I was, it were in the previous revision. I was like soldering wires directly to the, like to just like some pin headers. Yeah. Yeah. Yeah. Man. Let me tell you, that makes such a difference. You know, it's just like. I know. I know.

**Dave Jones:** I know.

**Chris Gammell:** The thing that I always get scared off about though is the custom, the custom. Yeah. Yeah.

**Dave Jones:** The custom assembly. You don't want to have to have a custom little crimping tool to make the little crimpy things and then push them into the connector. What a pain in the ass. Who wants that? Exactly. Just put a hole in the board with a pad. Just wire it on. Be a man. That's right. You know?

**Chris Gammell:** Exactly. Well, I don't know. Yeah. But the, the thing that I figured out is that you can buy pre-crimped cable from distributors now. Well, not now. I'm sure you have been able to for a while. I found it and I'm like, oh, well that's easier. And like, this is like super tiny stuff. And, and yeah, so I just like assemble little cables and I can, you know, do a little, a splice.

**Dave Jones:** Isn't, isn't like seed or somebody doing it now? Who's the company that just announced that they're doing cable assemblies? Somebody tweeted it out that you can, somebody, uh, uh, JLC. I think it was JLC. Wasn't it? They do custom. I don't know. Don't, don't quite. Yeah.

**Chris Gammell:** I mean, dirty prototypes or dirty cable used to do that stuff. And I think seed has a cable service too. And honestly, like, like I think I mentioned on the show before, like, it's not that hard to actually get like cable samples made. It's usually the low volume stuff sucks, but like, you know, go on Ali, Alibaba, find someone who's making something that looks relatively similar and write him an email and be like, Hey, can you change it here, here, and here? And they're like, yeah, of course. Yeah.

**Dave Jones:** Easy peasy lemon squeezy. Yeah.

**Chris Gammell:** You know, but there is overhead for that. So this was more like when you're like still at the prototype stage, you know, buying those pre-crimps is like real great. So yeah. So I've been enjoying, enjoying my, my easy connect and disconnect life.

**Dave Jones:** Cool bananas.

**Chris Gammell:** Yeah. It's so much better. I don't know.

**Dave Jones:** Well, you could always use like 0.1 inch ribbon cable and headers, you know?

**Chris Gammell:** Yeah. So the real thing is like, so like, this is also now I built for building out a test stand for this board that I'm building. And like, so like having these peripherals that are just able to like clip in super easy. So like you think about building out that for, you know, if I want to test 10 boards and I do it with like, say a ribbon cable, like you're talking about now, I've de-soldered that ribbon cable a couple of times and you know, my soldering is just, it's ugly. So, uh, you know, and so it's just a much more reliable, reliable connection. So, all right. You heard it here first folks, connectors more reliable than my soldering.

**Dave Jones:** Oh boy. Yeah. That's, that's the age old thing in a product design. Um, it goes back before I was born. That was a long time ago. Um, yeah. Do you go for an all connector solution? Do you hardwiring? Like when I'm doing a tear down of a product, I go, oh geez, they've hardwired in these, you know, look, Sony, the bastards. They've like hardwired in these cables, right? They're soldering them in. And how do I get these boards apart? And I've got to unsolder the bloody things just to take the boards out so I can like poke around at them and stuff. It's like, you know, but no, somebody deemed that that was, you know, cost saving or some other, you know, thing that they wanted to do and they weren't going to go, you know, or they will mix them. Like you, you tear down a product and you go, well, this is half board, nice board to board interconnect and half hardwired sold. And it's like, what the hell? Yeah.

**Chris Gammell:** I want to talk to my manufacturing engineer here, you know?

**Dave Jones:** Yeah. Nuts.

**Speaker ?:** Yeah.

**Chris Gammell:** What else should we talk about, Dave?

**Dave Jones:** What would you like to talk about, Chris?

**Chris Gammell:** Let's talk about the listener survey since a listener survey was up on the last episode, 533 with Joel Dunsmore. If you haven't heard that, that is, was a awesome conversation I got to have with him. And yes, we're giving away copies of his book. And so please do fill out our yearly survey. Even if you don't want the book, please fill it out. I may have a goodie or two to throw in that it's not that book as well. Yep. In case you've already got a copy.

**Dave Jones:** Didn't we forget something in last year's survey and you went, oh yeah, we should have added that.

**Chris Gammell:** Yeah. I, I, I had that thought and then I was like, oh, I'm out of time. So next year it is. Yeah. I could not remember what it was.

**Dave Jones:** No, I, I, I don't remember either. Yeah. But I thought I'd float it anyway, because there was something. I'm sure we said it on the show. Yeah. It was like, oh yeah, we definitely did.

**Chris Gammell:** We definitely did. So. Yeah. Oh well.

**Dave Jones:** Oh boy. Yeah. I have to do another survey for my channel. I haven't done one for donkey's years. So all the, I don't know if the data's out of date or what now, you know, has, has my audience changed? I don't know.

**Chris Gammell:** Yeah.

**Dave Jones:** No, no idea. So might've run another one. Hmm. But I can tell you from experience that even if you do the stuff that the audience, that the survey says that everyone wants, people still get upset anyway. It's like.

**Chris Gammell:** Oh yeah. Yeah.

**Dave Jones:** But, but 70% of people said they want this video and it's like, well, no, I don't like it.

**Chris Gammell:** We're going to do our own thing regardless.

**Dave Jones:** Yeah, exactly. It's just, it, you know, it is helpful though.

**Chris Gammell:** Yeah. I mean, we, we love hearing from all of you. I mean, like, that's for sure.

**Dave Jones:** The, uh, free form comment fields are the best. I love scrolling through the. Yeah. Be creative, please. We'd love to hear from you.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Dave's an asshole. It's like, yeah, it's great. Love it.

**Chris Gammell:** Uh, did you see I'm encroaching on your, uh, on your space? I did. I did an unboxing video, Dave.

**Dave Jones:** And I have not seen your unboxing video. I don't do unboxing videos. Really? I know. It's also a teardown. It's also a teardown. Mailbag.

**Chris Gammell:** It's also a teardown. Yeah.

**Dave Jones:** Yeah. What is it?

**Chris Gammell:** It's a dual scope. I mean, it's nothing you haven't seen before. Okay.

**Dave Jones:** No, I've done a dual scope. Yeah.

**Chris Gammell:** Right. Yeah. I got a new one. So mine broke.

**Dave Jones:** Oh, is there a new model?

**Chris Gammell:** Is there? No, no, mine broke.

**Dave Jones:** Oh, okay.

**Chris Gammell:** I had a beta and I broke it. I just, I was, I was rough housing with it. And so Matt sent me a new one. Uh, and, uh, yeah.

**Dave Jones:** You were rough housing with it. What were you, what the, were you throwing it? Is it physical or is it electrical rough housing?

**Chris Gammell:** No, it was physical. I think I'd probably, you know, like something when I was like unplugging the front plate or something like that. So. Right. I don't know what I did, but, uh, yeah. New one works great. And, uh, yeah. Measuring current. Like it's my job. It is my job.

**Dave Jones:** Right. Cool.

**Chris Gammell:** Yeah. I know. And I've been, I've been doing current measurements on my, my cellular board and I'm like, I'm all excited. I got all fired up and I'm like, oh yeah, I'm going to see like, you know, these huge spikes. And then like the current will go down to nothing. Cause I'm using this tiny little processor. Yeah. Yeah. And then I, it's like 20 milliamps, 25 milliamps. And like, like, you know, idle state. I'm like, what, what is going on here?

**Dave Jones:** You're expecting like 25 microamps or something. You got 25 milliamps.

**Chris Gammell:** I was, yeah. Yeah. I was like, oh yeah, it's going to probably like a hundred microamps, you know, like the NRF 52. Yeah. Yeah. Right. Current, whatever. Yeah. And it didn't. Not yet. I have some room to, to optimize still. It turns out I have a, uh, I have an op amp just kind of like turned on and sitting there on one of my plugin boards. And so, uh, yeah, that, that takes some current and you know, the sensors aren't turned off right.

**Dave Jones:** And it's taking tens of milliamps. What is a, one of those bipolar jobbies?

**Chris Gammell:** Yeah. It's a high, high accuracy.

**Dave Jones:** Right. Yep.

**Chris Gammell:** J-fed, I think. Yeah. I don't remember what it's on there. 41, 90 or something.

**Dave Jones:** For, for those playing along at home, you usually can't get high speed and low noise with low power consumption. It's like. Yeah.

**Chris Gammell:** There's a trade off somewhere. Yeah.

**Dave Jones:** Yeah. It's not going to happen.

**Chris Gammell:** Yeah. Why all the boxes are warm when you, you know, turn them all on and it's like, oh, they, they normalize at like 30 C.

**Dave Jones:** Right. Yeah. But it feels nice. It feels like quality. Like it's doing quality electronics in there.

**Chris Gammell:** It's got that warm, crunchy measurement capability, you know?

**Dave Jones:** Oh boy. Yeah. Tubes. We should go back to tubes, you know, filaments that heat up just for the sake of the.

**Chris Gammell:** Well, there, there's a product that, you know, doesn't have any firmware on it, Dave. You could go back to that.

**Dave Jones:** Is there a tube product with firmware?

**Chris Gammell:** Oh, totally. Yeah. So there's a guy at my meetup in Chicago, Keith. Keith, he built this, uh, this cool, like alarm clock that uses tubes as well. You know, it's the display element. Yep. Really, really nice design. It's got like an STM 32.

**Dave Jones:** Oh, he put an STM 32 and it gave me a break. What? Come on.

**Chris Gammell:** That's the problem. What? You can't source it?

**Dave Jones:** I've done a video on my, my clock design. All 4,000 series CMOS. Thank you very much.

**Chris Gammell:** Oh, well, okay. So, I mean, it's not like it's just the clock. Yeah. Okay. All right.

**Dave Jones:** Well, what else does it do? Bloody money. I don't remember. It's been a while.

**Chris Gammell:** Dave, it's been a while since I've seen people.

**Dave Jones:** Oh, right. Okay.

**Chris Gammell:** You know, into a hardware meetup that I get to see other people's work. People should like show up at the next meetup that they have. And they just have like boxes and boxes of, of projects ready to go, you know? Right.

**Dave Jones:** Everyone's been stuck at home. They've had nothing to do but work on projects, you know?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Hmm. How's things there anyway? Are things opening up there again?

**Chris Gammell:** The vaccine is going well. It's, I think like 10% of the, no, sorry. One in four, I saw a statistic. One in four people in the US has had their first vaccine. Right. For some people, they only need one shot with the new Johnson & Johnson. Oh, really? Okay. All right. Uh, yeah. It's still, I actually, I was looking at an article the other day that there's like a New York Times, uh, calculator, you know, you put in like your health conditions, you know, everything that, and then it tells you where you are online. And, uh, I think I had 240 million people ahead of me.

**Dave Jones:** Yeah. Right. Yeah. I'm like, yes, even though I'm old, I'm like, nah, I'm like bottom of the line. Yep.

**Chris Gammell:** Are you guys getting a vaccine or no? You're not going to.

**Dave Jones:** What here?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** It's, it's, it's free if you want it, you can have it, but you're on a waiting list. Like, yeah, I am like they're doing like, yeah, there's this multi-phase rollout thing. And I'm literally in the last, if I, you know, if you go through the check, but I'm literally in the last, you know, thing. It's okay. Like the, the only one less important than me is kids, you know? Right. So, yeah.

**Chris Gammell:** Just really strong immune systems. You mean?

**Dave Jones:** Yeah. Yeah. It's like, no, I have no comorbidities. I'm, you know, not old. Well, you know, in the scheme of things.

**Chris Gammell:** Oldish. Right. Yeah.

**Dave Jones:** Yeah. No, I'm not in my seventies, you know, something like that. I think it's mild risk over sixties or something. And then once you get in the same, once you're in your eight, like highest risk is eighties plus, you know, so they're like high priority and stuff like that. But no, if you're like, yeah. Youngish and fit and you know, you don't have any other underlying health issues. No, go to the back of the line, you know? So, which is fair enough, you know?

**Chris Gammell:** Yeah. Yeah. Totally.

**Dave Jones:** Yeah. No, totally. They should roll it out to the vulnerable people first. There's our weekly COVID update on The Amp Hour. Grown. Right. I just don't watch the news anymore. It's like, no. Yeah. I don't, I don't blame you. Yep. Yep. Gave up a long time ago. I think they're about to fly the helicopter on Mars. Aren't they? I think so. Yeah. I mean, I think they're close. Aren't they searching for a spot to drop it, to poop it out the back and then. Is that how it works? I haven't seen how it actually. Yeah. They physically drop it onto the ground and then move away and they poop it out. And yep. And then they stand back a distance. So then they can point the camera at it and they let it go. So yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** That's going to be.

**Chris Gammell:** I didn't realize how long it's been like in development and also like the constraint. I was watching the Veritasium video on it.

**Dave Jones:** Oh, right. Yeah.

**Chris Gammell:** Yeah. It's, uh, it's, I mean, I just like the, the speeds that the rotors have to spin at is like really nuts.

**Dave Jones:** Oh yeah. Cause there's bugger all air there. You know, there's bugger all air there.

**Chris Gammell:** It's like one, one, one hundredth. One hundredth.

**Dave Jones:** I think something of that order. Yeah. Yeah. It's like, yep.

**Chris Gammell:** Pretty crazy.

**Dave Jones:** Two orders less than here. Yeah. That's a, yeah. It's a lot. That's why it has to weigh like a hundred. Doesn't it weigh? Oh, it was away 400 grams or something. Is that the entire? Yeah.

**Chris Gammell:** It's insanely light. And then the other, the, the method of the mounting too, I don't know if you saw that the board was mounted or the boards are mounted rather, but they're actually mounted on the outside of the battery pack. And so the whole thing is like coated in like a, you know, like that gold foil stuff that they use for like radiation shielding, whatever. Yeah. But then the board, all of the control circuitry is mounted on the outside of the battery pack. I think because any residual heat from the battery is then also used to help heat the board up because a lot of the battery power is also using, being used to heat the board up as well, or to like keep things warm enough, you know, like just resistive elements and stuff. So that's the shitty thing about space.

**Dave Jones:** You know, I'm not sure of the temperature variations of where they landed. I'm not sure of the, you know, I don't think they, that wasn't their major concern. I think the science location was their major concern. Cause there are, there are some spots on Mars that can actually get into the 20 degree range, which I don't know what that, that Celsius, none of that Fahrenheit rubbish, but that's like, you know, just normal office temperature. Like the standard office temperature that I'm in now is like 23 or something is standard office temperature. Yeah. And you can get places on Mars that actually get that. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. So you can get, you know, there are some places that, that during the day they do actually get into nice, comfortable temperatures. So technically if you, you could walk outside, if you didn't, there weren't other issues, you could, you know, Yeah.

**Chris Gammell:** If you were going to asphyxiate and get irradiated and, uh, yeah, yeah. Yeah.

**Dave Jones:** Yeah. All sorts of other things then. Yeah. It'd be nice. So. Yep.

**Chris Gammell:** Yeah. It feels like the, the control algorithm on this thing is like really, really complex too, of just like having the dual rotor thing and like, and then how, how it actually like steers and yeah, it's just a lot of, there's a lot of science going into this thing. It feels like. So your odds of it working, of it actually flying. Oh, uh, I honestly didn't think it wouldn't fly. I guess.

**Dave Jones:** No, I, I think there's zero chance unless something goes wrong.

**Chris Gammell:** Like there's actually like hitting something maybe and not being able to recover. No, no.

**Dave Jones:** I, I think it'll fly. I think, you know, they've done their test. You know, these things are easy, fairly easy to calculate, although they're still not sure. Like, you know.

**Chris Gammell:** Yeah. It's a risk risk profile kind of thing or whatever. Right.

**Dave Jones:** But I, I think, no, it's all, I think it will get off the ground. I think this little puppy will go up. Yep.

**Chris Gammell:** Yeah. I mean, and even if they don't know right away, it's going to be, uh, they don't know for a couple of minutes. What is it? 20, 20 minutes. What's the, what's the transmit time?

**Dave Jones:** 12 minute delay or 14 minutes or something. Isn't it the moment? Something like that. Yeah. Yeah. Yep. Oh boy. Anyway, that's going to be very cool.

**Speaker ?:** Yeah.

**Dave Jones:** Oh, all right. What else we got?

**Chris Gammell:** How was your, uh, build your DMM build? Didn't you have a new DMM coming up?

**Dave Jones:** No.

**Chris Gammell:** I thought you were, I thought you were doing a rev on a design or something. No. Or maybe it was just released.

**Dave Jones:** Nope. That's someone else. I mean, I've got, I've got a new multimeter, but there's nothing to do with revs or new boards or anything. No. Sorry.

**Chris Gammell:** Oh, it's just like a new, a new model that's branded or something.

**Dave Jones:** It's a new model that's branded. Yeah. Yes. But that's it. No, sorry. Don't know where you were going with that one.

**Chris Gammell:** Okay.

**Dave Jones:** Yeah. Can we imagine that that was the case? What was your, where were you going?

**Chris Gammell:** She's going to ask how it's going. I mean, honestly, it's just like, uh, yeah. Like what's new with it? Uh, no, sorry. Well, what else, what else are you building these days, Dave? I mean, I, I, I feel like I can only talk about so much stuff, you know, that I'm building because, uh, you know, it's client stuff.

**Dave Jones:** Right. Well, you're building more stuff than me.

**Chris Gammell:** I know.

**Dave Jones:** I know. It's like, yep. I'm just too busy making videos and stuff. Although today I am probably going to shoot an update video on the micro supply. It's like, I'm going to get the box out the box.

**Chris Gammell:** The box that like the project box.

**Dave Jones:** Yep. The, the project box, which contains all the bits and, uh, yeah, I'm going to, uh, do a video.

**Chris Gammell:** You should put on like a, like a hat that makes you look like an archeologist, you know? Yeah. Right.

**Dave Jones:** Make it thematic. People are going to be disappointed. It's like, no, I'm probably not going to do anything with it. It's like, I was going to maybe talk about this in the video. It's the sunken cost fallacy kind of thing. You know, it's like, you know, yeah, it was a great idea 10 years ago. For this USB power supply. Now I'm thinking, it's, it's not going to be that. Like if, if it was app, if it was actually done and all it required was me to send all the files off and some company makes it, then I'd probably just do it for kicks. Right. And then if it doesn't sell, it doesn't sell me. But no, it's like.

**Chris Gammell:** Oh, sorry. I miss, I misheard you. I thought you were saying micro current. You said micro supply.

**Dave Jones:** Mike, Mike, micro supply, the little power supply. Oh, got it. You know, which looks really funky and it's got all custom. Parts in almost everything in its custom.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. But it needs like a new transformer. Like it needs a new custom transformer. It needs proper thermal testing and other stuff. And it needs. It's not at a point where I could just turn a key and actually make some, you know, we were getting fairly close to that. We were going to actually manufacture like 10 or 20 of them and like send out, you know, 10 or 15 of them to various people and actually trial it. So we weren't getting too far off from that, but there was still work required to do that. So, yeah. And it's tough.

**Chris Gammell:** Anytime, like, you know, a project kind of goes sour or quiet or whatever, you know, it's just like that thing happens, you know, I feel like when it happens with like a client project, it's like, oh, well, that sucks. Cause I stopped getting paid for it, you know? But like that happens in business too. But when it's like a personal project project, it's always, you know, it's like that someday like box can just continue to sit there, but it's kind of like a mental weight as well, you know? So it's like, it's almost better to like put it away and be like, nope, this is for sure done. Or yes, I'm going to pick it up on X date.

**Dave Jones:** Yeah. Well, do you have any examples of the sunken cost fallacy where you've continued with something, even though you shouldn't, because you've invested all this time, money and effort and you don't want to see that go to waste. The amp hour. Ha ha. Ha ha.

**Chris Gammell:** No. You know, I was, I was very hesitant to give up the engineering commons when I was, you know, deciding whether or not to come with that. And, you know, I'd put, I think it was like half a year into that. And luckily Jeff kept it going. I was thinking about Jeff the other day. I got to reach out to him, but like, luckily it kept going. So like that made me feel better, but. Right. Okay. So that. It was in a different state at that point too. Right. I mean, like in it. And so I think leaving, leaving a project behind like that is like, yeah, you know, you, but to make it something new to like make, to refresh it or to like make it, to grow it bigger or finish it in your case. Right. That sort of thing. It's like the sunk cost fallacy is like the real cost in the future is the work you still have to do. Right. So that's the, that's what I think is what's out there. And if you're not, you're not interested or willing to do that, then that's like, yeah, then, you know, just put it aside and move on to the next thing or harvest it for another project at some point in the future.

**Dave Jones:** Yeah. And, and it's not just a hardware that the, it's not just projects that the sunken costs fallacy. It's also in, in, in investment as well. Or you go, Oh, well, you know, I've been buying these shares and I'll put so much money in I don't want to, you know, sell them because, you know, I'm going to, Oh, I'm going to, you know, you have to buy more cause I've already put so much money into it. It's like, you know, yeah. Sometimes you've just got to go, nah, you know, it's, it's done. There's nothing you can do. Yeah. Especially if it doesn't interest you anymore. It's like, you know, so like there's times when I've been super hyped about that. You know, I did a whole, well, two different video series on that. And I was like, yeah, at the time of doing that, I was hyped and everyone goes, well, why don't you keep doing it? It's because, well, you know, it doesn't really interest me that much anymore.

**Chris Gammell:** Yeah.

**Dave Jones:** So unfortunately, yeah, that's just the way it is. But anyway, so the plan is, is to get the hardware out, you know, show people where it is and then let people bitch in the comments that I'm not going to do anything with it. And, um, you know, it'll, it'll get it out of their system. And then, you know, and then I, well, I've already released the source code. I actually released that like a year ago. The source code has been out there a long time. And I don't think I've released the latest schematic though. So I might actually release that. I might just dump it, you know, on the Githubs for those who are interested in such things. And yep, that, that might be that, unfortunately.

**Chris Gammell:** So, Hey, you know, like, uh, if you love something, let it, let it free.

**Dave Jones:** And if it comes back to you, maybe it'll come back to you as a finished product. Maybe I can buy it. Well, no, the thing is like, I've already got one. I've already got a couple of finished products and it works. Right. It's just, so I've got the thing that I wanted basically.

**Dave Jones:** Right. Yeah.

**Chris Gammell:** So you were building it to scratch your own itch. Right. Yeah. Yeah. Yeah.

**Dave Jones:** I was building it to scratch my own itch. Yeah. And, and the itch is scratched. I've already got it and I use it, you know, it's a cute little power supply, but it's not. Yeah. Yeah. The effort to go to actually produce it.

**Chris Gammell:** Yeah. It's not, it's not every, everything you wanted. Right.

**Dave Jones:** It's no, no, it's not, you know, it's, it's, it's, it's evolved over time and it's changed, but it's a, no, it's actually more than what I wanted actually. Cause it's USB power. This is what I originally wanted. This was the original thing is that it took power from a USB input and gave you an adjustable power supply. That was it. That was it. And that's what it does. And it does that with quite a few bells and whistles, you know, it's got a big, nice display on it and a custom keypad and, you know, it's a nice, sexy case and form factor and everything. So it's actually, yeah, it's actually done better than what I, what I originally imagined. Cause mine was just, you know, my original design was like, oh, just a crusty old jiffy box, you know, and. Right. Yeah, exactly. Yeah. Board on top. So I might, I, I'll try and dig out some of my original prototypes from like 12 years. Cause we're, we're, we're talking probably 12 years ago now. Yeah.

**Chris Gammell:** I mean, it was an early, the first one was like an early, uh, set of series on the, on the board.

**Dave Jones:** Yeah. Yeah. I can remember I was still working at Altium at the time and I was working in, was it the old building? No, I was working at the new Altium building. I was working at Altium and Leo Simpson from Silicon Chip magazine came in. And he was dropping by, I don't know, he wanted to see Altium or something. And he knew that I worked there. So he dropped by my, uh, little office, uh, cubicle, my, my, uh, Dilbert cubicle, you know, just chatting away. And I said, oh, by the way, I've been working on this little micro supply thing. Would you be interested in actually publishing this? And I showed him my little prototype and everything. And he thought it was great, you know? So yeah, write up an article, you know, and we'll get it published and blah, blah. So I was, I was actually reasonably close to getting that published too. So, but I sort of changed direction at the last minute or something. And I thought, oh, I'll just wait for this new version. And then, then there was another version on top of that. And then, you know, so it never got published, unfortunately. And there it goes. Yeah.

**Chris Gammell:** It takes on the mind of its own. Right.

**Dave Jones:** Right.

**Chris Gammell:** Yeah. Yeah. That's tough, man. It's tough at the end of things. Anyway. I'm making that decision stuff, I think, you know?

**Dave Jones:** Right. Yeah. It's like, I just, I just don't have the time and the will to get it into a finished product. Like I'm more interested in other stuff than that now. So that's just the way it is. Yeah. Yeah. But then again, if I don't like, I don't want it to just sit there. That's why I want to make a video. I want it showing like, yeah, here it is. The final thing. It got to this. Here's sort of like some old prototypes. Here's how it evolved and blah, blah, blah. And if, and if you want to take it up, well, you know, here's some files. Go for it.

**Chris Gammell:** Cool. That's great. Knock yourself out.

**Dave Jones:** But yeah.

**Chris Gammell:** I think that's, that kind of thing's good. Like a retrospective like that. That's good.

**Dave Jones:** Yep. Last minute. Last minute. Last calls. Nothing else.

**Chris Gammell:** People have been buying the Thermaltronics thing I recommended.

**Dave Jones:** Oh, right. Okay. Yeah.

**Chris Gammell:** That's nice.

**Dave Jones:** Nice.

**Chris Gammell:** What did I see on your bench? What did you have a JBC on your bench?

**Dave Jones:** I've got a JBC and a pace. Yeah. Nice. Although I'm, I'm actually using the pace more than the JBC now.

**Chris Gammell:** Okay.

**Dave Jones:** Yep.

**Speaker ?:** Cool.

**Dave Jones:** Yeah. Need two soldier and irons, by the way. You shouldn't just have one. You need two.

**Chris Gammell:** Yeah. So then you can dual wield and, you know. Exactly.

**Dave Jones:** Flip little chips off and, yep.

**Chris Gammell:** Right. Two. Yep. You should see three. This isn't even my final form.

**Dave Jones:** Can we talk?

**Dave Jones:** about like releasing a new model oh like a new rev yeah the fluke 87 has changed right originally came out in 1988 87 88 as the fluke 87 and then it was the fluke 87 3 and they skipped the two they went to the three and then the fluke 87 5 came out so they've revised it a couple of times but the fluke 87 5 came out in 2004 i believe or even slightly earlier early 2000s so it's getting close to 20 years old they've been selling the exact same model for i could probably predict what

**Chris Gammell:** the answer is which is uh money and uh when when papa dan or her doesn't want to spend any money

**Dave Jones:** to keep making money so people keep buying the old one yeah yeah but but they keep but they do release new models so it's not like they're like as in other multimeters so it's not like they're not working on new designs not like they don't have a design team with money to work on new designs

**Chris Gammell:** there's a reason yeah but why spend it if you're making money on the old one if you can still source

**Dave Jones:** parts and everything else like who cares no i i ultimately made this argument in the end here we go we'll finish it off why not okay is that uh okay let's say they sell a hundred thousand multi fluke 87s a year right it's still a very popular multimeter right it's it's the industry it's as industry standard as you get right everyone compares a multimeter with with with the 87 5 right yeah it's still very popular so let's say they sell a hundred thousand a year well if they release a new new model is everyone who owns an 87 5 going to rush out and buy the new model most likely not right because like they're very expensive for starters right and they just you know unless it's i don't know so radically different which not many people are going to their big customers aren't really going to accept but that's another side argument i bet the yeah the

**Chris Gammell:** big money is coming in from like just people who have it on a standard like a standard list somewhere they're like yeah our standard equipment is 87 5 great the big money comes from government contracts and

**Dave Jones:** military contracts they're the two big things and yeah and it's like okay they designed a new model they're still going to sell a it's not like they're going to suddenly start selling double right it's not going to happen there's not enough small buyers excited you know there's not enough multimeter enthusiasts so excited to spend a thousand bucks right there's no i mean there are collectors but not like that yeah no not enough to matter not enough to matter so they're still going to be selling a hundred thousand a year regardless right i'm making that figure up right but they're still going to be making the same amount regardless of whether or not they release a new model all of your big buyers they're all happy to buy the existing model and they have been for 20 years and they're still happy to buy it so yeah that's one of the reasons not to rock the boat and actually release a new model so yeah anyway there's more to it than that there's more to i am in complete agreements

**Chris Gammell:** agreeance with you but i think we will uh we'll put in the the link to the to the the forum thread

**Dave Jones:** the forum thread yep speculate there yeah excellent no problem they're right debate away cool

**Chris Gammell:** yeah next week we will have sammy from ethnics which is an fbga company on the show so uh as a final reminder please fill out the survey please fill out the survey and be creative be creative in your comments and and creative and kind i don't care about kind okay then be creative i've i've i've got a

**Dave Jones:** dedicated hate mail address and i read it i know because it's just it's just fun yeah people actually send email to my hate mail address just to see if i read it oh like you know they send an email i'm sending this to your hate mail but i just i really love your show and everything i just want to see if you actually read your hate mail i actually reply yep you know yeah so yep love it all right anyway that's it hey dave talk to you soon catch you next time

**Chris Gammell:** love it or hate it that was our show and let's be honest if you got this far you probably didn't hate all of it a reminder that we love our patrons you can become one of them by joining the crowd and the discord channel at patreon.com slash the amp hour we'd also love it if you remember to fill out the survey thanks you

**Speaker ?:** you
