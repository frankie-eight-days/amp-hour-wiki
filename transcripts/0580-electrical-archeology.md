---
episode: 580
title: Electrical Archeology
url: https://theamphour.com/580-electrical-archeology/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released March 6th, 2022. Episode 580. Electrical Archaeology.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** I found a part which you cannot find a replacement for. I've challenged the engineering community to find a replacement. I just released a video before this, so you would not seen it.

**Chris Gammell:** Is this like a riddle? It's like, you know, all of human knowledge. A part of my heart.

**Dave Jones:** What?

**Chris Gammell:** I don't know.

**Dave Jones:** Is that a reference to something? Am I missing? No, no, no.

**Chris Gammell:** I'm just saying. It just sounds like the riddle, you know, like that. No human could replace this one part.

**Dave Jones:** Oh, right. Okay. Yeah. Anyway, yeah.

**Chris Gammell:** What is it?

**Dave Jones:** It's a lowly MOSFET. It's a lowly MOSFET. But I contend that there is only one manufacturer of said lowly MOSFET.

**Chris Gammell:** You got a link for me.

**Dave Jones:** Oh, yeah, probably. Hang on. Here we go. Is it that one? No, it's this one. This makes great. Hang on. 43. It's a 4303. And if you Google for 4303, this is why I did a one hour of it.

**Chris Gammell:** That's not a very easily found number or part rather.

**Dave Jones:** Okay. And here we go. You've got it now in your Google thing. All right. It is.

**Chris Gammell:** Sino Power Semi. Yep. Okay. SM. So is SM the...

**Dave Jones:** SM is their prefix. Yeah. It's their prefix.

**Speaker ?:** Got it.

**Dave Jones:** Now, if you watch my video, there is. You can actually find that equivalent part number if you search LCSC. So if you go into LCSC, which is kind of like the Asian DigiKey Mouser equivalent, they're probably...

**Chris Gammell:** Yeah, it's the one tied to JLC. And they basically expose some of the parts only available in the Chinese. We talked about them before, for sure. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** Yep. Heaps.

**Dave Jones:** Is there anyone else in Asia that's like trying to do the DigiKey Mouser thing?

**Chris Gammell:** It's interesting. So yes, I think so. But not... I don't think they get the same exposure. So I remember like... Right. Well, and not the same... You know, they're putting some work in. You know, they put in some work for translation and just exposure and the data management is not a small thing either. I remember like looking at 21IC and that's kind of like also like a social site. I think it was 21IC.cn. Oh, right. One of those. Yeah. Yeah. But it was kind of just like a link dump kind of thing.

**Dave Jones:** One of those. It's like an Asian chat forum or something, is it? It's like a... Yeah. Yeah.

**Chris Gammell:** It looked like a... It kind of looked like... Remember how we used to complain about the Element 14 like Jive?

**Dave Jones:** The Element 14 community.

**Chris Gammell:** It kind of looked like that, but like with a lot of Chinese characters on it.

**Dave Jones:** Right. Got it. It probably used the same application, but a different language set.

**Chris Gammell:** It was bad in either case, let's be honest. Yeah. Right. There's a long throwback for, you know, listeners. Oh, yeah. That was... It was probably episode one of the Amp Hour complaining about it.

**Dave Jones:** Back then, Ben Heck was still doing the Ben Heck show, you know. That's right.

**Speaker ?:** Yeah.

**Dave Jones:** Anyway, I sent you another data sheet to the only equivalent like part number I could find. So this is an APM 4303. And this is from another company you've never heard of, which is VB Semi. And these are both Taiwanese companies. So Sinopower and VB Semi. I don't know. I actually haven't been to the VB Semi website, but Sinopower, all they make is MOSFETs. That's it. Oh, cool. Right? Interesting. So anyway, this stemmed from the Aputure Amaran LED light of mine that failed. I did a repair video on that. So this is like a spinoff video from that. And all of the MOSFETs in there are all of the Sinopower brand. So obviously, the design engineer or the purchasing person there just loves the, you know, Sinopower. Right? Well, it also could have been, you know, it depends where they are, but like... They're a Chinese... Well, it's made in China. I don't know if they're a Taiwanese company, but if they're a Taiwanese company, then yeah, I can totally understand.

**Chris Gammell:** But I'm guessing some of our listening audiences, you know, worked on a design, prototype something with, you know, a locally available chip. And then they basically go to like a DFM process. And part of that is just like a cost down and people in the local ecosystem. So maybe you have a CM and the CM's like, hey, we want to replace them with all these much lower cost chips. You do an eval and you're like, yeah, that's great. Look how much cheaper that is. Holy crap. Yep. Awesome.

**Dave Jones:** And they do... Yeah. Like South Korea, for example, like my 121 GW multimeter is made in South Korea. Right? And they go to extraordinary lengths to find parts made in South Korea. They're almost obsessed with it. Right? And they'll go, I didn't... Like, we need to change this part because this one, we just found one.

**Chris Gammell:** Is it because of imports or because of...

**Dave Jones:** It's a... I don't know. Is it a nationalism thing? Is it a... It could be. Yeah. Yeah. National security thing. I... You know, is it a culture thing? I don't know. Right? But yeah, they just... Yeah, they go to extraordinary lengths. You wouldn't believe... Like a lot of people don't realize how huge the semiconductor... Industry is there. And there's all these ones... Like when, you know, Asia, we're talking about, you know, Taiwan, China, that kind of thing. But there's South Korea. They have their own industry and their own semiconductor makers as well that make all these, you know, obscure, you know, semiconductors and stuff. And it's just something we don't know about yet. You know, it's a whole industry out there. So yes, if you buy a South Korean product, it likely uses a whole bunch of South Korean parts you haven't heard of. So... Yeah. Hmm. Or South Korean manufactured equivalent parts. Anyway, in this case, this MOSFET, right? This Sino Power Jobby, it sounds pretty ordinary, right? It's a 30 volt P channel 17 amp SO8 MOSFET, right? What's the big deal? Like 30 volts is like probably the biggest category for SMD MOSFETs, like in the biggest generic category in terms of voltage range. 17 amps is like it's high, but it's nothing, you know, out of the ordinary. And it's, there's nothing special about it except that it's got ESD protection built in. So if you have a look at this internal schematic, there's some ESD protection. There's an eight kilovolt gate protection. And that's the thing. And that's the thing I spent a one hour video trying to find a replacement for this. And if you have a look at the other one I sent you, the VB Semi that has the exact same part number, 4303. It does not have the ESD protection built in, right? So it's a very different part.

**Chris Gammell:** Is it possible that it's just not documented?

**Dave Jones:** Because I just, I always wondered about these sort of things. Yeah.

**Chris Gammell:** I was just like, I kind of just assume that every input to a chip these days has ESD on it, right? Otherwise.

**Dave Jones:** Not on individual MOSFETs, no. That's the thing. You have to get a specific ESD variant. And a lot of the, all the major manufacturers, they will have like an ESD, like a dash E or a dash ESD or something like that. But you can't just order any part with a dash E on the end, right? It doesn't work like that. They only make like less than a handful of parts that have built in ESD protection. And a lot of them are multi, like dual. They're a dual or they're a quad MOSFET designed for logic level input protection and stuff like that, you know? So, yeah.

**Chris Gammell:** Interesting. So then what about the application circuit as well? So like, what is this going into that you think it, did you back calculate what you think that was required for?

**Dave Jones:** Yes, because it goes into a plug-in battery. There's two batteries on the back of this which have exposed pins. So Joe Average, who's taking out the battery, can scuff their feet and touch these pins. But interestingly, the MOSFET nearest to it is also a P-channel with almost the same specs but doesn't have the ESD protection built in. So this design actually uses almost identical MOSFET, again, from Sino Power. It's almost identical specs except it doesn't have ESD protection and that's even closer to the battery terminals. So I don't, I like, I'd love to see the schematic. I don't just, yeah, I do not do it.

**Chris Gammell:** It does make you wonder though, like if, you know, like you had said, right? So maybe the purchasing agent just likes this part or like I said, it's like super cheap or whatever. And it fits all the specs but maybe it has this extra feature like ESD protection diodes. Yep. And it doesn't, you know, you test it, it doesn't impact anything. No, no problem. Of course. But then it gets out in the field and. Right. So, so in full disclosure, I've seen some of the analysis videos of some of the Keith Leaguer I used to work on. And people say, people maybe I'm talking to right now, they say, oh, well, it probably does this and this. I'm like, no, no, no, that's not it. And it's like, but it's, you know, there's like this institutional knowledge inside the company, which I should be clear. I did not come up with. I was just privy to it. I did not actually, you know, I was not making up any of this, you know, any of this design decisions. I was just, I was able to see the schematics. I was able to see all the decisions making internally. And it's like, but it does, when you then analyze it from outside, it's almost like an, it's like an electronic archaeology type of thing. You know, it's like, oh, this culture may have decided the ESD diodes were important on the MOSFET here, but not here. They must have worshipped the ESD gods. You know, it's just like, all right, well, but like, how are we going to know unless, unless we have. Exactly.

**Dave Jones:** Yeah, you've got to know the design decisions. Maybe this, the schematic alone isn't enough. Like there may be this other knowledge insight, like they've been bitten before. Right. Or something. And they were just covering their ass on this design. But then like, it's, it's almost the identical MOSFET. And there's probably like what a couple of cents difference, maybe between the one that has the ESD and the one that doesn't, you know, okay. I've worked on, on designs where we were like, you know, a few cents made a diff, made a huge difference. But like, why you wouldn't just like, like if you already decided, okay, I need the ESD part in that part of my circuit because reasons. Then why wouldn't you just like bomb consolidate right across the design? Yeah, double it. Right? Just because. Right? So yeah, it's a slight, in fact, the one that's replacing is a slightly lower rated MOSFET. So it's like, oh, maybe, maybe they are saving a few, you know, maybe they're saving 10 cents. I don't know. And maybe that does make a difference. But yeah, I just thought it was odd.

**Chris Gammell:** What's really crazy is like, I mean, this thing is busted, right? This part was busted. Oh, yeah, yeah. What if the ESD diodes caused it, Dave? What if it caused it?

**Dave Jones:** No, they usually don't cause a direct. I know, of course.

**Chris Gammell:** Yep.

**Dave Jones:** Anyway.

**Chris Gammell:** Yeah. There you go. So are you going to try and get these parts or are you going to just try and say, screw it and get it close enough? Oh, no. You have not watched my video. I have not, no.

**Dave Jones:** I salvaged, I dumpster dived and salvaged an old laptop and I stole a MOSFET out of that. I stole a generic MOSFET out of that and God damn it, it works. Just fine. So I actually, yeah, yeah. So I salvaged the part because I did not have, like I've got MOSFET kits here, right? And sure enough, I do not have the P channel ones are relatively rare compared to the N channels, right? So I've got some P channels, but I don't have any P channel SO8s in my kit. So I could have bodged in like a DPAC or something.

**Chris Gammell:** Yeah. SO8 with the three pin source and the one pin gate and like all that.

**Dave Jones:** The three pin source and the four pin drain and the one gate. Yep. Yep. Standard SO8 package. Non-thermal.

**Chris Gammell:** I do prefer this configuration. I feel like, I feel like these are super easy to like figure out, you know, maybe not figure out, but when I'm designing in something like this that has multi-terminal and I want to get a lot of current through whatever, like, you know, there's those big thick packs that have like the heat sink capability to the, you know, the copper plane or whatever. Yeah, there's a big deep pack. Give me this thing.

**Dave Jones:** I know. I know. I love my little SO8 MOSFETs. They're really nice, you know? And, and the good thing about them and another, I think somebody might've asked this in one of the comments maybe is why you would use an SO8 instead of like a DPAC or something like that. You know, one of the, like the power packages, why would you use this? One of the reasons is like, it's just nice from that point of view, but as you mentioned, like just from a designer.

**Chris Gammell:** I think desoldering is easier, honestly. And desoldering is it.

**Dave Jones:** And we're, and handling, we're just used to SO8s. Like we use SO8s everywhere because we use them for op amps and digital, you know, like we just use SO packages, right?

**Chris Gammell:** I mean, this is cranking some current, but well, I guess 10, up to 10 amps.

**Dave Jones:** Well, 17 amps is pretty decent, you know, but that's its maximum. You wouldn't be operating this thing at, you know, at that sort of, yeah, current. But anyway, one of the other advantages I mentioned to the commenter is that is you can route traces under these suckers, right? Oh, yeah. Whereas if you've got a power package, no, it's taking up square area of your board, right? Because it's got that big thermal pad you've got to lay down and you can't put traces under that, right? So if you don't need the power, like if you don't really care about the power, then you would use an SO8. You wouldn't use a DPAC or something like that because you just free up more room to route traces under the device.

**Chris Gammell:** Yeah. And sometimes you just don't have a choice, right? Your purchasing agent says you have to use this part and you're like, okay, well,

**Dave Jones:** yeah, maybe. Yeah. Because they're using it elsewhere in the organization or something like that, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** But yeah, no. And that could mean the difference between a two-layer board and a four-layer board or a four-layer board and a six-layer board or something like that. That's a good point. Right? That could be the threshold difference. I've worked on designs where, oh, God, no. I'm at my last handful of traces and no, damn it, this is just not going to work, right? I'm going to have to go to an extra layer just because, you know, geez, I wish this was a different package. So I could have, you know, got this bus under there or something. I don't know. So, yeah. Oh, it's just nightmare. Anyway.

**Chris Gammell:** I've been looking at P-channel MOSFETs myself for actually looking at, so I really like the ideal diode packages that are out there. They're insanely expensive, you know? And they're meant for like cars and for basically when you're diode oring things together, you could use an ideal diode. It's not a real thing. It's a, you know, it's a marketing term.

**Dave Jones:** Yeah, yeah.

**Chris Gammell:** Basically, it's a P-channel FET and some control logic around it. And then you don't have a drop basically when you're trying to or two supplies together. Awesome. And I've seen, I've started doing a little bit of like preliminary like simulation and stuff like that. It's probably more finicky than I actually want. But let me tell you, if I had designed something in previously with an ideal diode, not only would it be, you know, four extra dollars in the bomb for however many people put on there. Yeah, right. They are pure unobtainium right now. And it's just like, it's the only choice I have if I don't want to drop, if I don't want to drop that, you know, 0.2 volts and up for a shock.

**Dave Jones:** So is it a single manufacturer? Are you locked into a single manufacturer or they're at least, is there at least some choice in the same package pin out?

**Chris Gammell:** There's some choice. I think it also depends like how fancy they get. So like some of them are like, you know, it's the response time and, you know, maybe there's multiples in a package, that sort of thing. So like LT has a very good one. TI has got one. I think OnSemi has one. But they're just, they're nowhere. They're, they are ghost, ghost parts right now. Right. Got it. And, you know, like you look at the actual like ideal diode circuit and it's like, oh, it is just like a couple of NPNs and a P channel MOSFET and some resistors. Asterix, you know? Yeah, right. Right. So we'll see how that works in practice over temperature. And so what you're really buying though is, you know, what I've gotten used to buying and maybe now reversing course on is like, you're buying someone testing that and, you know,

**Dave Jones:** And you're buying package convenience as well. Yeah, exactly. And you're buying bomb convenience. You're there's, it's a single reel on your pick and place machine instead of four reels.

**Chris Gammell:** It's the TV dinner of, of the part of the part world, you know, it's just like, you just peel back the foil and it's there and then ready to eat, you know, it's just, it's all good to go. So, you know, I will update on my, uh, on my escapades soon, sooner or later. I'm thinking, I don't know if you've ever used those sorts of things before, but sometimes you just can't give up the 0.2 volts.

**Dave Jones:** No, it's yeah. Yeah. Yeah. Sometimes you have to go for the obscure oddball part and it's, yeah, it, it absolutely bugs you, but like, you know, like, no, I can't design in 20 things around like, like actually do a, a discrete solution for it. You know, if you find like an only one solution for it, then, you know, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. That's a good thing. But then again, I've, I've very rarely been involved in extremely high volume stuff. So, yeah. You know, right. Right. Yep.

**Chris Gammell:** I feel like that's a kind of a thing where I've had, I've had co-ops working for me before, like, you know, younger engineers working with me and they're like, I have this one part. It's the only part in the world that will possibly ever work with us. I'm like, you may need a result. We may need to go back and look at your assumptions and your requirements and that part's $8. So no, we're not using it. I'm sorry. That is not going to work for us here. Yeah. But usually that is a good indicator. If you're getting down to like the, that one part that keeps popping up on DigiKey or Mouser. Yeah. You might want to be looking at your requirements again.

**Dave Jones:** But then again, yeah. I've often worked in the extreme opposite end where what that, that chips a hundred dollars. So what?

**Chris Gammell:** You know? Sure. Sure. Sure. Sure.

**Dave Jones:** No big deal.

**Chris Gammell:** Yeah. But that's, that's like, you know, if you're saying that about like, you know, undersea ADC or whatever you were doing for that in that case, that's a lot different than like, this is a power converter. Yeah, exactly. I need a five volt rail. It's like, okay. How, how many amps? Oh, you know, a thousand amps.

**Dave Jones:** Oh boy. Yeah.

**Chris Gammell:** Yep. What have we got on the list this week? Not, not much. I got to say. Not much at all.

**Dave Jones:** Come on. Well, you know, I've been busy, Dave. Well, I'll tell you what I've been trying to do. I've been trying. That's great. Because once again, it's to do with this bloody light, right? There's lots of spinoff things because this thing killed my batteries, right? Because the MOSFET was shorted, right? So it deep discharged the batteries as, as I was actually plugging in and they're giving out zero volts now, right? They're, they're an eight point. So they're an eight volt dual cell lithium ion, you know, Sony battery thing.

**Chris Gammell:** Sure.

**Dave Jones:** And they're giving out precisely zero volts. And the reason they're giving out precisely zero volts is not because it's entirely discharged. It's because the built-in circuit protection, there's almost certainly built-in circuit protection that has kicked in and actually disabled the cells. Now, whether that's an electronic MOSFET-y fuse type thing, or whether that, that is an actual like fuse inside that's actually now, you know, gone and there's no way to do it. So, you know, quite a few people in the comments said, why can't you rejuvenate the battery? So that's what I'm trying to do at the moment. So I'm up to day three and I'm currently staring at it and I've got 8.4 volts going into it and only three milliamps. It hasn't changed at all. So the whole idea is that the cells inside are under the lockout voltage, the under voltage lockout voltage of the protection circuit. So if the cells drop under, you know, two volts per cell or something like that, you know, it varies. Right. But let's just say two volts or something per cell. Then the absolute, then the low voltage under lock protection kicks in and totally disables those cells. So they cannot go to zero. And the, and the theory is, is that if you trickle charge them at a couple of milliamps by that, I mean, you just put your regular eight volts across. Well, in this particular case, eight volts across the two cell battery and you leave it there for a long time.

**Chris Gammell:** Don't just up it to 10 volts. No, no, no, no, no. That's bad news. Yeah.

**Dave Jones:** So, uh, you can, uh, yeah. If you don't know a, a lithium ion battery is charged at 4.2 volts. Right. And it's got to be pretty precise. Right. Yes. Right. It's got to be within like half a percent or something. Right. It's, it's pretty close. Right.

**Chris Gammell:** I feel like that's always the, that's the other thing too, though, is it's, that's the, that's the trickle, trickle voltage. Right. Or is that right? That's only, that's as you, as your volt, as your current drops.

**Dave Jones:** That's the constant voltage charge rate because there's, there's dual modes. There's a constant voltage charge mode and then there's constant current after that, that tapers off. So it's a dual stage charging system. So yeah, this is constant voltage. So I've got it there and it's drawing three milliamps, right? So there's three milliamps going into something. Right. And the, and then the theory is, is that, is that part of that something, of course, will be the protection circuit, but hopefully.

**Chris Gammell:** Kirchhoff says, well, where is this going?

**Dave Jones:** We just don't know because it's a black box, unfortunately, unless it's an ultrasonically welded black box. So we don't know. Yeah. Right. Right. So I can't just take it apart and have a squeeze.

**Chris Gammell:** With magical fire bags inside. Yeah.

**Dave Jones:** So yeah, hopefully like there's a bit of charge going into the cells. And the whole idea is that if you leave it on there for a couple of days, you will trickle charge these cells. And eventually, because they're not actually completely destroyed cells, they will actually charge up above the under voltage lockout. And then boom, the, the, it'll turn back on and you've rejuvenated and, and you've recovered the cell and Bob's your uncle. Right.

**Chris Gammell:** But you're taking bets on this.

**Dave Jones:** No, I think this has a permanent, I think I'm going to have to get out the, uh, Dremel.

**Chris Gammell:** These are going to recycle, recycling. Yeah.

**Dave Jones:** After I get the Dremel in there and take off the, yeah, actually have a look inside and you can actually take them apart. See, if you can take them apart easily and you've got access to the individual cells, then you can rejuvenate and charge the individual cells. And then, you know, hopefully the under voltage lockout comes back up. But a lot of these have like permanent E fuses and stuff, you know, like permanent fuses in them that, and if they blow, well, you know, yeah. So yeah. So it's not working yet. So everyone who wanted me to do that, well, I'm doing it, but it's not, you know, what

**Chris Gammell:** you should do is take the battery outside and try, you know, 8.5 volts, 8.6. See what happens.

**Dave Jones:** Roll them dice, Dave. Did, did you see the slow-mo guys video? They, they just did one.

**Chris Gammell:** Oh no. Blowing up capacitors.

**Dave Jones:** They finally blew up capacitors.

**Chris Gammell:** Oh, very nice. It's pretty glorious.

**Dave Jones:** It's pretty glorious. Like, cause they, they've got, they've got the real shit, you know, they've got the

**Chris Gammell:** good stuff.

**Speaker ?:** Right.

**Chris Gammell:** Yeah. But like, I don't know, some caps are catastrophic and some are just kind of like, I'm done.

**Dave Jones:** Yeah. Yeah. But they vent. Yeah. Yeah. If you have the ones with the vent, then they're just going to vent out the top. That's, that's their job, you know, so they don't explode, but you do get some spectacular footage of, you know, the venting out and stuff.

**Chris Gammell:** Got it.

**Dave Jones:** Yeah. Yeah. It's just like, and they've got one where they angle, like they had a water filled balloon and then they shot the capacitor at the water filled balloon. And it looks like a plant, like what would happen, like when an S asteroid would impact a planet. And you can see the ripples in like the water going across the planet, so to speak. Oh, it's just, it's, it's pretty glorious footage. They got absolutely fantastic. 180,000 frames a second.

**Chris Gammell:** And then, yeah, those guys are, yep. Yeah. It's pretty good. I haven't blown up a cap in a while.

**Dave Jones:** Yeah. No, I, yeah. I did a slow-mo video way back in the old days, you know, video 50 or something. I don't know, but yeah, that was fun. But yeah, you know, it's a bit, uh, cliche, isn't it? It's a bit like old hat cliche to blow up caps, you know?

**Chris Gammell:** I mean, it's, it's fine. I just mean like, I, I've done it by accident. That's the only time I've ever done it.

**Dave Jones:** Right. Okay.

**Chris Gammell:** And, uh, and that hasn't happened in a while. So I think that means I'm not working on high voltage stuff very often these days.

**Dave Jones:** Well, it doesn't have to be high voltage. You just have to stick it in backwards, you know? Sure. Sure. Yeah. Isn't hard. Yeah. In fact, it doesn't take much at all. People think, oh, you've got to put 240 volts across them. No. If you just get a 16 volt cap and you put 20 volts across it, it'll just, the, uh, pressure will build up inside and inside and it'll just keep building and building and building. Of course you've got to have like a high current power supply, you know, that helps a lot too. Got it. Yeah. Yeah. Yeah. But, uh, uh, yeah, it's, but then again, small caps, you don't need much in the way of power to heat up the electrolyte inside and then boil it. And then all the pressure builds up and then, you know, boom ski. Yep. And just the cloud of plume that went everywhere. Oh God. It's just, you know, and that blowing capacitor smell. Oh, yep. Magic. Love it. Anyway. Yeah. Yeah. My battery's just sitting here doing nothing, not getting into it or getting out of it. Yeah. Yep. Yep. It's boring. Got to call it quits. Quite disappointed. Everyone got me all excited, hoping I can rejuvenate the battery. And it's like, nah, never works. Bloody Murphy. Anyway. All right. Uh, floating solar farms. I know you wanted to talk about floating solar farms. Was it you who put it on here?

**Chris Gammell:** Uh, I did. When was that? Oh yeah. That was a while ago. That was like, we didn't talk about that though, huh?

**Dave Jones:** No, no, we didn't talk about that. Yeah. Kind of. Yeah.

**Chris Gammell:** Interesting idea.

**Dave Jones:** It is, but I can show you what happens. If, if you haven't seen what happens.

**Chris Gammell:** Oh, I think you did mention. Oh, there's further down. No, there's a further down video.

**Dave Jones:** Oh, is that article? Oh, right.

**Chris Gammell:** Yeah. In Japan.

**Dave Jones:** Oh, right. Okay. Oh yeah. Oh, I haven't watched that. Oh. Oh, magic smoke. Oh, oh, oh.

**Chris Gammell:** So anyways, floating solar farms. The idea is that if you're on top of a reservoir, you basically much like, was that a Veritasium video as well about like the black balls in the LA reservoir to like help shade the water? So you just cut down on.

**Dave Jones:** 96 million black balls. Yeah. That's right. Yeah. Yeah. Yeah.

**Chris Gammell:** Shade balls. Yeah. And, uh, and so that you shade the water, you also can get some cooling effects on the solar panels. You know, there's ups and downs and, you know, there's people.

**Dave Jones:** Unfortunately, there's two problems with putting solar panels on water is a things tend to move when they float. But just saying, you know, you can have them like crash into each other.

**Chris Gammell:** Sure.

**Dave Jones:** Yeah. Which is what's obviously happened here.

**Chris Gammell:** Yeah. Like during a windstorm or whatever. Yeah.

**Dave Jones:** Yeah. A windstorm, you know, waves, you know, get up or whatever. Fixed position. Yeah. No, it is not, you know, anchored into the ground with big, you know, metal stakes into the ground. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** So yeah, you tend to have a problem. You can come a gutter that way. And I sent you a link. Oh no, that wasn't the one covered in. No, I didn't send you the one covered in. I like moss. Oh, bird poo actually. Because we get big lakes, right? You get lots of aquatic birds. Avian. Yes. Spectators. What are the words for water bird, you know, waterfowl, water aquatic, water aquatic birds or whatever. Yeah. They tend to love to poop on these things and yeah.

**Chris Gammell:** Yeah. They're all perches, right? I mean, that's what it's all. Yeah. They're all perches. You got to like do some kind of bird dispersal methods and stuff like that.

**Dave Jones:** And it's just, no, it's just, it is not a fundamentally good idea. I can understand why they're doing it because the water helps to cool the, to keep the panels cool and stuff like that. And well, the, you're just wasting that land area and you're not wasting, but you, you know, that land area is otherwise, you know, not being used for anything else apart from the water. So it makes sense, but yeah, nah. One of the good uses I've seen is the water canals. I think this was in India, I think, and they've covered their water canals with solar panels. And that's great because that stops water evaporating. It stops the sun hitting. These are big concrete channels, right? Which, you know, huge water, right? But they don't use pipes because I don't know, they're more expensive. I don't know. Anyway, these big, huge, big quarter canal things and they, and they aren't very wide. They're only like four or five meters wide or something. So you can put, you know, the structure of the solar panels over them and you can anchor them into the ground either side and they cover the trenches and, and it helps shade them. So you don't get the water evaporating from the trenches and you get your solar power and it, because it's not like a lake or anything, you don't get your water birdie, fowly things pooping all over. Generally. It's great.

**Chris Gammell:** So my friend is, uh, is an, like in a group for a city, major U S city, and he's did exactly that in the U S as well. And like, yeah, I saw there was one in the U S which state is that?

**Dave Jones:** Uh, there's not, there is a state in the U S which are trying.

**Chris Gammell:** I don't know if I can blow him in for what it is. So it's a, it's a major city in the U S, but yeah, he did that same thing. And then they were, because it was like a public works project too. They were able to like, just donate, you know, they were doing it just to shade the water and then they were able to, uh, donate the power to like low income families too, which

**Dave Jones:** was like, Oh, well, that's okay. That's yeah. It's cool. It's awesome. Yeah. Love it. So, but yeah, nah, the, the floating panels on the water, that's more trouble than it's worth. I don't yet. People have yet. Countries have done these on massive scale. They've done them on massive scale.

**Chris Gammell:** I think this one was, wasn't a reservoir as well. It wasn't like a, it wasn't a natural waterway. It wasn't like a lake or something. No, but even still like reservoirs kind of become these natural, you know, man-made lakes effectively. So there's also that.

**Dave Jones:** Yeah. And it seems a very popular thing to do, but yeah, quite a few of them seem to have come with guts in a big way.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** They just all crashed together and there's photos of, you know, you know, like thousands of panels.

**Chris Gammell:** Most, uh, Hackaday-y comments I had read in a while. There's a lot of angry people. So, you know, if you want to get back to the, the throwback to the grumpy, the grumpy old ways on Hackaday.

**Dave Jones:** Oh yeah. Okay. Come on.

**Chris Gammell:** Yeah. Just the usual stuff. No, no need here. No, no need here.

**Dave Jones:** Yeah. But what is the gist of the comments?

**Chris Gammell:** Oh.

**Dave Jones:** Are there any solar roadways comments?

**Chris Gammell:** You're also, no, no, no. No, it's more about, uh, like the sun is still blowing, you know, like because there, there are fish in these reservoirs as well. It's hurting that natural, you know, all that sort of stuff.

**Dave Jones:** So, oh, okay. Right.

**Chris Gammell:** It's always going to be a balance of like, you know, unless you're putting solar, like in the middle of the desert and I guess desert ecosystems also have, you know, uh, life out there, but yeah, there's always going to be some kind of environmental impact from, from putting a thing out there that's disrupting the natural flow of things.

**Dave Jones:** Well, there's this famous Elon Musk thing about, you know, we can power the entire United States with, you know, 10 square kilometers or something of solar panels. And, uh, the, uh, common sense, uh, skeptic did a video running the numbers on that, which was a really good video. Actually, if you're interested in the numbers behind that in, in that, yeah, he wasn't quite on the money, but you know, like, yeah, technically in theory, you can power like an entire country with, you know, just like a small, relatively small amount of solar panels. So if you ignore the whole storage thing, right. Let, let, you know, just ignore that thing for a minute. It's like, it doesn't work because transmission.

**Chris Gammell:** Yeah. They're doing like amount of sunlight hitting, hitting the ground. Right.

**Dave Jones:** Yeah. And well, no, and no, it's, it's, it's the transmission thing. Right. You can't just whack it. Yeah, sure. Oh, I live in Australia here. We could just have, you know, a big solar farm in the middle of the country that powers the entire country. No worries. Right. Yeah. We'll try and transport the energy that far. It's just, it just, you know, it's just dumb. So, yeah, it's a complete non-starter to think that you can, you know, like just use one big central source and that's it. That's why, you know, yeah, it just doesn't work. And it's got nothing to do with solar. It's the same thing with nuclear, with anything else. Right. Molten salt, you know, anything. Right. Geothermal stuff. It's like, yeah, Australia's got tons of geothermal, but it's in the middle. It's in the middle of places where people don't live. So, you know, you've got to, you've got to transport the energy. So, yep.

**Chris Gammell:** Grid stuff. Grid stuff's above my pay grade, man. Right. Way above my pay grade.

**Dave Jones:** But it's something you can run the numbers on though. It isn't above your pay grade. You can simply run the numbers. You know, you mean like that?

**Chris Gammell:** I meant the actual design and, you know, that sort of thing.

**Dave Jones:** Oh, the grid infrastructure and stuff like that. Yeah, thinking through actually how you build all that stuff out. Yeah.

**Chris Gammell:** Grid level projects and just the voltages.

**Dave Jones:** We should actually try and get somebody on who is like in charge of like designing like a countrywide grid or something like that. Someone who knows the ins and outs.

**Chris Gammell:** How could you even have, like, is there one person? Does the buck stop somewhere? You know?

**Dave Jones:** Right, right. I don't know.

**Chris Gammell:** Because there's so many pieces of it, right? There's people that are like installing towers. There's all the people that are manufacturing on the various pieces. But like someone at some Vogon planning office in the middle of Beetlejuice 6 or wherever it is, you know, like that, the plans are in the basement there.

**Dave Jones:** You need to talk to the operators. Remember when we went to the, here in Australia, we went to the Canberra Deep Space Tracking Complex, right?

**Chris Gammell:** Yeah, yeah.

**Dave Jones:** And we talked to NASCOM 1 on Twitter. And he's great to follow, by the way. He's awesome.

**Chris Gammell:** Richard, right?

**Dave Jones:** Richard, yes. He's one of the operators, right? And like, and I've done video, like I've done videos and he just knows everything. The people who operate the systems know everything. So all you got to do is talk to an operator, I reckon. Right? Yeah.

**Chris Gammell:** Yeah. I don't know who that, who would that be for a power, you know? Yeah.

**Dave Jones:** Well, I've got one down the street here, which operates the entire East Coast of Australia. But I tried to get in and talk to them and they wouldn't let me. Basterds.

**Chris Gammell:** Oh, you mean there's an office. You don't have a contact. You need a contact.

**Dave Jones:** Oh, no, no. I don't. Yeah. I need an actual technical person there who, you know, there's going to be someone who knows how it all works.

**Chris Gammell:** Hundreds or thousands of people listening right now that could reach out. And actually, if we have a, if anyone's emailed us in the past, I don't know, three months, our feedback email has been broken. Apparently, we got ourselves under some blacklists.

**Dave Jones:** Yeah, that's right.

**Chris Gammell:** So we have not gotten your emails. It probably bounced back to you. We're sorry about that. Yep. It should work now. All it took was me changing the IP address of our entire web infrastructure here.

**Dave Jones:** Because we're on some spam list somewhere. Yeah. Because we're hardcore spammers here at the EV. Yeah, Cialis.

**Chris Gammell:** Yep. Cialis.

**Dave Jones:** So, yeah.

**Chris Gammell:** I feel like that joke goes on deaf ears these days, too. Like, you know, like, the kids growing up these days, did they get the same kind of spam that we do? Like, spam is just, like, so much less of an issue than it used to be. You know?

**Dave Jones:** Oh, I never had. Once I switched to Gmail, my spam problem just completely vanished.

**Chris Gammell:** I know. But, like, you had the before, right? We all got the before. Yeah, yeah, yeah. And people that are younger that are just like, yeah, I've had a Gmail address since I was in, like, middle school. And it's just like.

**Dave Jones:** Right. And it basically handles most of it for you. Yeah. Yeah. Almost all of it. Except in the last six months, it just went completely to shit. And all my good email was getting spammed. And, but that, I just tweeted yesterday that that seems to be fixed now. Somebody fixed it. Somebody realized. And they, I don't know, they reverted to the previous code.

**Chris Gammell:** They don't, oh, they give us or something. And, like, yeah. Yeah, that's what it is. They just reverse the changes. Get reset dash dash hard. Yeah, right.

**Dave Jones:** And, like, yeah.

**Chris Gammell:** I mean, the email system is weird, man. It is just, I had to dig into it more than I ever wanted to. And I'm very bad at it. But, man, like, the way that, like, email servers talk to one another, it is, it is a pile of spaghetti. Right. It is. Anyways, our email works. And if you happen to be working in or around or you know people in the power grid field, we'd love to talk to them. We want to interview them. Yeah, that'd be great. We have people listening, we think. So if you're listening to this and you're like, yeah, I know somebody, shoot us a note, please.

**Dave Jones:** So what do we, what are we looking out of that? It's like, why are grids designed the way they do? You know, how. Why are grids? How close do you need the power stations? Like, you know, how, like.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. All sorts of stuff. I'm sure there's a million trade-offs.

**Chris Gammell:** I would be interested, like, how much of a slice do they see as well, right? Like, is, so if someone's working in a, so like I used to work for ABB, right? And I worked in the part that, like, designed the controller that went into the power plant.

**Dave Jones:** For those who don't know, ABB, Alan, they're a controls company.

**Chris Gammell:** They might see a Brown Bavari. Yes, there are. Yes. This is actually Bailey, formerly Bailey controls. That's where I used to work. And that was before I joined the supply frame crowd. And, and like, so I was working on stuff that went into power plants.

**Dave Jones:** Yep.

**Chris Gammell:** And. Okay. But like, there was no notion of like the actual output power. You know, I never saw anything above five volts, you know? Right. Right. It was like logic level and like temperature sensing and like stuff that's just like around. And even then I didn't even, you know, I wasn't there long enough to like see it all the way through. So like.

**Dave Jones:** Right.

**Chris Gammell:** That's like one small piece of a very large complicated system. And that's still in the power plant. And then, then it gets stepped up and stepped up and stepped up and over these transmission lines and step down and step down. And like, there's all these, and it's somewhere there's like control nodes that are actually like rerouting stuff and bringing on new capabilities as needed. Yep. I don't know. It seems like we're just way out of, I'm way out of my element. I'll at least say so. Yeah. Yep. So that's some of the questions that it would just be.

**Dave Jones:** It's a great thing to get into, I think. I think it's, we've mentioned this before. Yeah.

**Chris Gammell:** Yeah. When they talk about smart grid, what do you, what's the smart part?

**Dave Jones:** Well, I suspect the smart part might, might be doing away with their job. Might be the smart part. Maybe. Doing away with the operator, you know? So it's like.

**Chris Gammell:** Every time I hear about, you know, smart grid's brought up a lot in like the IoT system. Space, which I'm now adjacent to and in. And it's always like, well, the power company is going to send you, you know, over your Wi-Fi. They're going to send you a, you know, a packet that says, oh, now it's, you know, power's cheap now. So turn on your stuff. And then it's going to control like at the.

**Dave Jones:** Yeah. Charge your electric card. At the junction box. Right now. And then no, stop. Right. Quickly. You know?

**Chris Gammell:** Yeah.

**Dave Jones:** I don't care if you have to go somewhere tomorrow. No, we're going to cut off your EV charger.

**Chris Gammell:** It's probably going to be very inconvenient for people, but you know, you might get a little cost reduction.

**Speaker ?:** Yeah.

**Dave Jones:** Well, somebody emailed me the other day. I can't remember exact details, but it was something along the lines of, I think you're in Australia. They were talking. They were trying to tell me that there was a government thing where the utilities, the energy utilities could now shut off your power. Like they can, they can remotely shut off your power via smart meter. And I don't think that's actually possible. I don't think, you know, why, why, why would anyone? Well, I guess, you know, there's people dumb enough to install these wifi light bulbs. Right. So I guess there's people dumb enough to install a remotely connected thing that lets the, that lets the authorities disconnect your power.

**Chris Gammell:** Well, I think that if it was your meter though, usually you don't have, you don't have, you don't have control of it though. At your, at your meter. That's like usually owned by the, it's owned by the power company. Right. It's like, you get everything past the meter, but because they're charging you for the power, they get everything to the meter. And they own the meter and that's usually like for billing and things like that.

**Dave Jones:** Yeah, but they can like switch. That's right. They were saying they could switch off your solar. They could remotely switch off your solar system. It's like, I don't know anyone who's got a, a, a solar inverter system installed that can be remotely switched off by the energy authority. Like if you're dumb enough to install one of those things, then. Yeah. Right. Why would you just like not install that part? Yeah. Yeah, exactly. Just not install.

**Chris Gammell:** Oh, you know what? I don't have my wifi password. So I guess I can't hook into your control system. Mighty. Yeah.

**Dave Jones:** But they, they seem to think that this was a thing and I went, I don't think so. I've, I've never heard of it. So if you've heard of it, I don't know, leave it in the comments, please.

**Chris Gammell:** But yeah. Yeah. Yeah. Well, what is the incentive there too?

**Dave Jones:** Like, oh, the incentive is, is, is to control the grid. Solar is a big, in particular is a big problem because we've got a massive, so we've got one of the largest solar uptakes here in the world. Like something like 40% of houses in this country have solar on them. Right. And that causes problems on the grid. It means they can't manage the grid. It's pumping too much power into the grid at certain times of the day. And, and the voltages go way above, you know, it risks the voltages going above the compliant level and, you know, all sorts of things. So they, you know, it's, it's really becoming an actual problem. So yeah. Anyway.

**Chris Gammell:** Yeah. And it's too bad. Like, like, like there's not like micro storage, like, you know, micro in quotes. Right. But like on a neighborhood level. Right. Cause it would be nice if they're like, all right, we're not going to turn off your solar, but now you're feeding. So your solar is feeding, you know, the sun is shining very bright. You're feeding your neighbors.

**Dave Jones:** Everybody's trading with your neighbors. Yeah.

**Chris Gammell:** Well, you're feeding your neighbors, but then like, if there's still too much, like then you should be able to like, just feed it into like a micro storage down the street instead of all the way back at the, at the power station.

**Dave Jones:** Yep. Exactly. Exactly. And then, and then you avoid all the transmission losses and everything else if you do everything locally. So somebody asked me like, you know, does my EV, right. Cause I've got now a smart EV charger that only charges my EV when the sun shines. Right. So I can guarantee that all the solar power that I'm generating and action, all the energy that goes into my car comes from the solar panels. And they're going, Oh, but you can't guarantee that because how do you know? Like it's just coming from the grid, but no, it's actually not. It's coming from the panels because it's, it's all done before the metering. It's all done before the metering. And I can physically see that there's no energy coming in from the grid.

**Chris Gammell:** Yeah. Right. Right. Right. That's one thing. It's very good at tracking, right? It's like, it knows which way the power's flowing. Yes. It knows.

**Dave Jones:** I can physically see. I've got an else, I can, I can got a display that shows me that the energy going in and out of the grid. And I can see that. No, nothing's being exported to the grid. It's all going into my car. It's all being dumped. It's all being handled locally. So if you could do that at a street level, that'd be, you know, that'd be fantastic.

**Chris Gammell:** Yeah. So, you know, one thing I've been thinking about, so we had some ice storms and now that I live in North Carolina, everybody freaked the F out. They were just like, quarter inch of snow. We're shutting down everything. The government shut down. The schools are shut down. It's all shutting down. And they were, it was, nobody went anywhere. It was crazy. But, you know, I was like, okay, well, my power might shut off. And that, that sucks. Cause that's, you know, like I've got the electric water heater now and just a lot more electricity in my life than I used to when I lived in the wintry North.

**Dave Jones:** Yep.

**Chris Gammell:** What I was wondering though, is like, I do not have solar here and I don't really hear about any like localized battery solutions, like home battery solutions. Usually I hear about them to capture like solar, but you don't ever really hear about them in terms of just as a, as a grid backup. Yeah. Grid backup.

**Dave Jones:** As a grid thing where you can, yes, just charge them up during the day at cheap power rates and use them at night when it's expensive and stuff like that. And that helps balance the grid and, you know, et cetera, et cetera. Right.

**Chris Gammell:** And like, I guess, I mean, a car, unless your car obviously would very much work in that way, but I do not have one of those. And the math would probably work out to just get one of those if, if that was the case and it could feed back into my, into my house when the power goes out. But like, right. I was just, I was thinking about like, have you heard about that sort of thing? Is that a, is that a thing or no? The, uh, what just having battery for. Yeah. Like just buying a power wall or just having a, you know, a DMI system.

**Dave Jones:** No, most people I know, um, they buy it because they have the solar and they want to store their excess solar. Here, here in Australia, you've got to have a smart meter to make that viable. Right. So I, I, I don't have a smart meter. I've got a dumb meter. So I, I, so there's no time of day tariff for me. Right. So, so the power during the day costs me the same amount of power at night. If I, if I wanted to take advantage of such a battery system without having, well, it makes no difference if you've got solar or not really. It's, it's, it's doing the same thing. Yeah. Yeah. You, you would have to, I'd have to change over to a smart meter that gives me a different, like a cheaper rate during the day. So that then I could suck in the power from all my neighbor's solar panels. Right. During the day when the power is cheap. And then I reuse that power at night when it's, it's expensive. And that doesn't just help me. It doesn't just help the actual homeowner that also helps the grid. Cause I talked about too much solar on the grid is a real problem for managing the grid. Like they're having a hard time managing all this solar uptake. So if people were installing home battery systems, that, that actually helps. Cause that can absorb that.

**Chris Gammell:** You think that would be like the next, the next level of tariffs or whatever.

**Dave Jones:** I think there's a few, there are a few trials here where they have actually put a street level grid storage. There, there's a few trials going on, but yeah, I'm not aware of anyone like just making the conscious decision to do that. Yeah. And there's no, certainly no government incentives here to, to actually do that. And, and that's not the reason behind it.

**Chris Gammell:** Yeah. And you guys still are not getting the incentives on the cars either, which kind of stinks.

**Dave Jones:** No, no zero. Yeah. So, yep.

**Chris Gammell:** Man, if you watch the, if, you know, I'm sure down under, you know, cause you guys use that term so much. Uh, I'm sure in your part of the world, you guys watch the, uh, the Superbowl, you know, the, uh, the U S football.

**Dave Jones:** We totally watched the Superbowl. Yeah. Yeah. Everybody loves it.

**Chris Gammell:** But what's it? So I did watch some of it. I've watched like a couple of commercials. My, uh, it was on in the background and man, the amount of like, just like, you know, the demographics of the Superbowl, like trucks, you're just, you're going to see a lot of truck commercials. Right. Okay.

**Dave Jones:** Yeah.

**Chris Gammell:** Electric trucks. Like, oh my goodness. Like really? There was a lot, was it? Oh, a lot. Yeah. Yeah. It was, it was very encouraging. Like it was great. I was very happy about that. So bring it on more electric trucks. If you're going to buy trucks, make them electric.

**Dave Jones:** Well, unfortunately you can't buy a Tesla. Can you buy any electric truck in the U S right now? Is there any electric car? Because the, um, Cybertruck has been delayed. The Cybertruck, actually he came out, Musk came out and said, basically, sorry guys, but we can't make it for the price that we promised.

**Chris Gammell:** Oh man.

**Dave Jones:** He didn't exactly say that, but he said, um, like.

**Chris Gammell:** All those, all the stainless steel's going to the, the spaceships. Oh, that's right. The blow up.

**Dave Jones:** It was made out of stainless steel, was it?

**Chris Gammell:** No, I don't know. It looked the same. It looked, you know, that, that's silvery. Yeah. It had the metallic. Yeah.

**Dave Jones:** Yeah. And anyway, yeah.

**Chris Gammell:** He said, uh, cost is a big issue. I think you can buy. I, so the F-150 lightning is, I think available. I don't know if you can buy any cars right now, which is because of the shortage, the ship shortage, but in theory that's available right now. Right. Maybe it's, maybe it's a waiting list. I don't know. I think it's.

**Dave Jones:** Well, he, he also made, well, he basically, his tweet made the bold claim that if we can't do it, as in he means like a low cost EV truck, then nobody can do it.

**Chris Gammell:** That guy is so full of hot air. I'm so sick of the musky. I just need to, I just shut him off. I don't follow him on Twitter. I can't, I can't do it.

**Dave Jones:** But unfortunately everyone does follow him. Right. And that's the thing. He, you know, influences markets, but you know.

**Chris Gammell:** I mean, yes, I see your retweets of him. So yes, I do catch it, but it's, uh, you know, get me off that crazy train as soon as like, like smart guy has a lot of smart people working for him, but man, that guy is bananas. It's just not, I can't, I can't handle him. So. And the hero of worship too. It's just a little, you know, myself included. Right. It's just, it's just a little much. Yep. So. Yep.

**Dave Jones:** But yeah, that's an interesting, like, so you don't, do you know of an EV truck that's actually available from any manufacturer?

**Chris Gammell:** Well, that's what I'm saying. I think that, I think the F-150 Lightning is, but I don't know how to tell. Cause I, I don't know how to buy a car.

**Dave Jones:** Can you actually buy it? Is it a.

**Speaker ?:** Yeah.

**Chris Gammell:** I don't know. Oh, pre, uh, starting spring 2022. So maybe not.

**Dave Jones:** It's not actually. So it's announced, but it's not, it hasn't shipped yet.

**Chris Gammell:** I'm also being targeted by my local Ford dealer. I'm really worried if I know this is Cerritos, California. Nevermind. It's just like, you start searching, you know, like I'm going to get so many ads now. Right. Just like buy a truck. Yep. You know, like when someone searches buy truck in Google, they probably get targeted with ads for the rest of their life. Like, Oh, but you wanted a truck in March of 2022. Surely you still do in 2038, even though the world's on fire.

**Dave Jones:** Yep.

**Chris Gammell:** We can make money off of you. Oh boy. Yep. Yeah. Yeah. So far. I don't know. Uh, there, there are, uh, let's see my, one of my new neighbors, he has a plug in hybrid. That's not a truck though. I think, Oh, it's an SUV. So there's a lot of SUVs that are out now that are hybrids or hybrids. Hybrids are me.

**Dave Jones:** Hybrids are me.

**Chris Gammell:** It's better than nothing. Dave. I try. I try. You know how much I drive per week? It's a, it's a, it's a crazy week when Chris drives to the grocery store and back. I'm clocking in at less than like 500 miles a year, you know? Right. Okay.

**Dave Jones:** Just, just wait until the kids go to school, you know? Yeah, I know.

**Chris Gammell:** I know. I know. Yeah. That'll, that'll change things. That'll change things. Oh boy.

**Dave Jones:** Yeah. Well, that, that's the same for us. Almost all of our running around as the kids, you know? Yeah, totally.

**Chris Gammell:** And I mean, you know, I'm sure by, uh, I'm sure by the time my daughter is grown up, uh, you know, I'll just put her in a self-driving Uber, right? That'll just help me. Right.

**Dave Jones:** Yeah, sure. Yeah.

**Chris Gammell:** Just, just, just poking the bear here, folks.

**Dave Jones:** Should we make, should we update our predictions on full self-driving?

**Chris Gammell:** Oh yeah. It's not looking good.

**Dave Jones:** It's just, it's shit house. No, it's still getting better. Yeah, I know. I know.

**Chris Gammell:** I think the vision stuff is getting better. I just, you know, like the.

**Dave Jones:** Yeah. No.

**Chris Gammell:** One thing I think about with all this stuff is, I don't know if you've looked at like the hiring market. It is so incredibly hard to hire people. Like, and just, you know, especially at the, like the high end. So like, you know, I know people in the hardware and firmware space and I'm trying to hire people in that space. And like, it's just, there's a lot of roles there, but then you like zoom out a little bit and you go on like, you know, you go on the hacker news who's hiring page. So I don't know if you knew this is a, have you ever seen this thing or not? I haven't. It's like the first of the month, every month, uh, hacker news has a thread and it's just who's hiring and all of it. And so like, you know, usually it's engineers at a company will post about who they want to work with or, you know, like that they're hiring.

**Dave Jones:** So, you know, and. Oh, so the companies know about this and the companies actually post on their director, like.

**Chris Gammell:** That's right. And like recruiters know about it now too. And it's, you know, there's still like the social. Yeah. But it's, but I think, you know, because it's social and because it can get downloaded if it's super spammy or whatever, it's still okay. And you know, I, hang on.

**Dave Jones:** I like that idea that it can get down. If you're a, if you're a dickhead bloody recruitment agency is just like a bunch of wankers and you get downvoted to into oblivion. Right. I really liked that idea.

**Chris Gammell:** Yeah.

**Dave Jones:** I mean, oh geez. I think we don't have to participate in that just for, just for the kicks.

**Chris Gammell:** How would you participate though? Like you, I mean, you're not hiring. I don't know. I'd be a. Oh, just downvoting.

**Dave Jones:** You could be a user. I could, I could like downvote. Got it. Got it. Yes. That'd be so satisfying. Oh. Oh. Recruitment agency. Yeah. No. People. Obviously our audience know we're not fans of recruitment companies. That's right.

**Chris Gammell:** Yeah.

**Dave Jones:** Here at the Ampow.

**Chris Gammell:** Yeah. I mean, like it's always been kind of like that. So I don't know, like people, so people that are in the hardware firmness space, I've been like a lot of newsletters are good about this stuff. So there's like the prepared has a good newsletter. And analog.io is a new newsletter that's out there. Jack Gansel's newsletter. They all have like, you know, job posting areas in there.

**Dave Jones:** Oh, I didn't know Jack's one had.

**Chris Gammell:** Yeah. Jack's has always been free. It's always been like, you know, keep a low word count. It's just like a great way for people that are like, you know, people that are, there are very few marketing executives that are reading Jack Gansel's newsletter. Right. In fact, I've, I'm continuously impressed by like the variety of people that he gets responding to his newsletter because then he'll republish. And if you're not reading his newsletter, I highly recommend it. It's one of my favorites. It's called the Embedded Muse. Well, I'll link it in. But yeah, it's got a job section too. And it's usually pretty low key. You know, it's just like a, yeah, here's the job, you know, come check us out.

**Dave Jones:** Cause usually I would bury it in a random location within the thing each time so that the recruitment agencies, you know, cause they, they're like their eyes would roll over. They start seeing technical articles. Oh, I see. So they, you know, just bury it. Like don't, don't make it easy for them to, you know.

**Chris Gammell:** Got it.

**Dave Jones:** Yeah.

**Chris Gammell:** I mean, well then in that case, a lot of these newsletters too, like there, there's a filtration mechanism that is a human. Right. And so usually when you have marketplace systems like a Hacker News or a, here's an old reference, a monster.com or an indeed.com, monster.com. Remember them, Dave? Remember their Superbowl ads?

**Speaker ?:** No.

**Chris Gammell:** Sorry. No, I know you don't. Right. They were, yeah. That was like the first.com crash. Oh, really? There's how old I am. Yeah. Remember the early 2000s? Yeah. I remember. Yeah. I know you do. You don't remember the Superbowl ads from the early 2000s and the late nineties.

**Dave Jones:** I hate to break it to you, Chris, but there is like, you're not American. I know. There's a whole world out there outside of America. I know, Dave. You know?

**Chris Gammell:** I have to imagine that, you know, when the Aussie rules football is on, there's also expensive ads running against that. Just probably not as expensive.

**Dave Jones:** No, but we don't. Yeah. But we don't like obsess over them. It's like, you know, we don't go, Oh, all the ads are coming on. No, we just go to the freaking Dunny. You know, we don't care about the ads. Right. Yes. Yes. They do pay more.

**Chris Gammell:** It's become this cultural thing. It's this cultural thing.

**Speaker ?:** Yeah.

**Dave Jones:** No, we don't have the cultural thing in regards to ads during a major.

**Chris Gammell:** It's become its own thing, you know? Right. Yeah. I don't, I'm not, you know, forward against it. I would not pay $7 million for 30 seconds of an ad, if you ask me. Yeah. Nor would I put up a QR code. I'm sure you saw that story. Come on. I've seen the story.

**Dave Jones:** One of the crypto sites, they put up a floating barcode or something. Yeah. Yeah. Floating QR code. Yeah. Yeah.

**Chris Gammell:** Yeah. There's some old news. We're now like three weeks past it, but anywho.

**Dave Jones:** You've got a segue, haven't you?

**Chris Gammell:** No, not really. Just there's filtration. I do. On a lot of these sites. I think it's good to, you know, so if people are looking, you know, we're coming out of the, the great resignation or whatever they're calling this, this epoch that we're in. And as people are starting to look. I thought it just started. Maybe. Who knows, man?

**Dave Jones:** All right. Anyway, come on.

**Chris Gammell:** We're living in some weird times.

**Dave Jones:** Dude, you don't know what the segue is. You put it on the list yourself. It's at number one. It's got 11 votes. Google mandates workers go back to Silicon Valley.

**Chris Gammell:** Yeah. Yeah. Okay. Let me start again. All right. So speaking of, speaking of jobs, I bet some Googlers will be looking for some new jobs soon when they're forced to go back into the office. Haha, suckers. Enjoy that in your $600,000 salary.

**Dave Jones:** It just blows up.

**Chris Gammell:** Do you know how much software engineers get paid, Dave? Do you know how much software engineers get paid? It is insane. I know.

**Dave Jones:** It blows my mind. I don't think you could get a $600,000 job here in Australia.

**Chris Gammell:** To be fair, it's not a $600,000 salary, right? Right, right. $180,000 and then like RSUs that are worth- What's an RSU? Stock options. Some type of stock option that- Ah, right. Basically, it's equivalent stock that you can cash in at some point that's worth like a buttload of money.

**Dave Jones:** Is there a threshold for that? Like the share price has to make a, the company has to make a limit? Because I got bloody share options that are, we actually call them share options here in Australia. Oh, okay. And it's like, and they associate it with a price target. So when I was working at Altium, the share price was 10 cents, right?

**Chris Gammell:** Yeah.

**Dave Jones:** It was for five bucks. And then during the tech boom, and then it went down 10 cents because, you know, they didn't want to make a profit. They just didn't want to rent as a hobby business. Anyway, 10 cents. And so we all got these share options. We go, great. And we read it and says, well, the, the share exercise option, it's called the share exercise price is a dollar. So it's only if the share price gets up to a dollar, can you actually like sell them, right? Can you actually buy in?

**Chris Gammell:** Well, you can sell them for loss if you wanted to, if you wanted the stock for some reason.

**Dave Jones:** Oh, it's just, no.

**Chris Gammell:** You may be able to take a write off on that, I guess. I don't know how that would work.

**Dave Jones:** No, I don't even think you can do that. So you can't even get a tax advantage that way. That is not common.

**Chris Gammell:** I have not seen a- Okay.

**Dave Jones:** Well, that's a thing here.

**Chris Gammell:** I think it's because at Altium, it was the, the strike price was set before the drop happened. Right. So that's, that is what happens when the market goes down. No, no. Mostly the time.

**Dave Jones:** No, it wasn't set then. It was set when it was 10 cents.

**Chris Gammell:** Oh, interesting. I've never heard of that before. I'm sure there's a reason for it. I have no idea what it is. Usually though, the RSUs that like a software engineer will get, and I'm sure I'm saying this wrong too. It's, you're going to make a buttload of money on it, right? It's like you, you have some strike price that's much below what the, you know, so if you're a Googler and the share price.

**Dave Jones:** So you can buy them at five bucks, but the current share market price is 10 bucks. So you can buy them instantly at five bucks and then instantly go sell them for 10.

**Chris Gammell:** And the other thing that happens is, so like if usually there's like a vesting plan for that sort of thing. So like a common thing for options generally is like a one year cliff so that you can't, you don't get any of it for the first year. Of course. So if you stay for, you have to stay for one year to get the first 25%. You're right. And then, and then it's scaled. Right. So then if you stay for two years, you get 50% of that grant. If you stay for three, 75, four, all of it.

**Dave Jones:** Apple, Apple back in the day, this is some computer history for you. Apple back in the day used to have these t-shirts. This is when Apple floated on the stock market and it was the biggest float in American history. Right. They, everyone went around with these t-shirts that F, U, I, F, V. These are letters and it's, and it stood for FU, I'm fully vested. And everyone walked around with these t-shirts saying FU, I'm fully vested. Like, you know, it's like, yeah.

**Chris Gammell:** You mean when they were going public? That's what that was.

**Speaker ?:** Sure.

**Dave Jones:** That wasn't on, I'm surprised that wasn't on like Silicon Valley or one of those shows. Yeah.

**Chris Gammell:** Well, there's a rest and vest jokes and stuff like that. That's the same kind of thing. Right. So someone who has, they're waiting for their stuff to become vested. So they just wait it out. Yeah. This is all.

**Dave Jones:** Yep.

**Chris Gammell:** So anyways, a lot of what these salaries are is like these RSUs and you get some every year and then you can just, they're just like this salary add on. But the thing is, so say you were, you know, the $5 strike price and $10, you might be able to sell it for $10 on the first day or, you know, like after the one year mark. Well, stock prices tend to go up too. So like they're worth even more if you hold onto them. Yeah. And so it's just like this paper money that's worth a buttload of money. It's just like, it's, it's insane. And so, yeah. What would be interesting is when all these Googlers have to go back to the office, how much do they like working from home? We'll see. Do they like it? I don't know. $450,000 difference? Maybe.

**Dave Jones:** I, I, but I suspect if they're fully vested, there's a lot of them that are going to go, nah, see ya.

**Chris Gammell:** Yeah. They might just be like, you know, I'm going to do that startup I wanted to work on, you know, or I'm just going to retire for a while or. Yeah. Yeah. Totally. Yeah. Google money. Fang or formerly known as Fang now known as Manga.

**Dave Jones:** Okay. What's Manga? Manga.

**Chris Gammell:** Microsoft. Nope. Nope. Microsoft, Apple.

**Dave Jones:** Manga. That would be Microsoft, Apple, Netflix.

**Chris Gammell:** Oh, Microsoft. No, no, no. Cause Fang was never in Microsoft. It should be, but it's not in there. Oh, well. Fang was Facebook, Apple, Amazon, Netflix, and Google.

**Dave Jones:** Who does the M stand for then? In Manga.

**Chris Gammell:** It stands for Facebook now because they've changed the meta.

**Dave Jones:** Oh, meta. Oh, meta. Oh, God.

**Chris Gammell:** And Google became, and actually it's like Google actually became Alphabet. So I don't even think Manga works anymore. It doesn't matter. It's stupid. But Fang is the, if you see Fang with two As, that's usually referring to these large tech companies with large stock grants and people getting paid a lot of money. And if you're listening to me right now and you're thinking, oh, Chris, I hate you. I'm working in these companies. I'm like, well, you know, go cry in your piles of money. Hardware engineers don't get paid like that. I have theories about this too. Okay. One of the things is, I think, so obviously I think the scale difference of like a, you know, hyperscale engineers is what it like Google engineers are called because like, you know, you go work on Google maps and it touches like, you know, you can have a team of 300 people that might serve 5 billion people, you know, in the world or whatever the actual users. And just like the scale difference is like that. Whereas if you or I design a circuit board.

**Dave Jones:** That is called revenue per employee. There's a term for it. Yeah.

**Chris Gammell:** That's it. Yeah. Yeah. Oh, okay. I didn't know that. Yeah.

**Dave Jones:** There's a specific industry term. Yeah.

**Chris Gammell:** Got it. Yeah. And I think, so I think revenue per employee is one thing that's obviously going to impact things.

**Dave Jones:** I think at one stage, the biggest revenue per employee company was Norton. Was Norton. Or was it. Norton. Or was it. Holy crap. That's a throwback. Or was it John McAfee. It might've been McAfee antivirus or something. It was one of those two. I think they were the greatest revenue per employee. It was like $10 million revenue per employee or something. It was enormous. Right. So yeah. So this is a financial metric that's actually used in the industry.

**Chris Gammell:** So yeah, that's one thing. I think another thing is just, you know, how hard is it to get to labor? Right. Especially like super skilled labor. Right. Some of this stuff is very, you know, if you're a DevOps engineer for a hyperscale company like Google, it's like, yeah, okay. There are a finite number of people in the world that can do that kind of thing. And it's high pressure. Okay, fine. But then I have a theory as well. Like the closer you are to the sale of a thing, I think the more you can make. So I think that really goes against hardware engineers. Right.

**Dave Jones:** Potentially.

**Chris Gammell:** Because like you think about like a sales engineer. Right. So someone who's a salesperson.

**Dave Jones:** Yeah, of course.

**Chris Gammell:** You can basically say, hey, I got us another million dollars of business. Yeah. All I want is 3% of that as my bonus. It's like, oh yeah, you got us all that business. Yeah, it's tangible. Right. You can, yeah. Whereas how do you or I as hardware engineers do that sort of thing? It's like, well, I combine, you know, here's a little throwback. I, you know, I reused a MOSFET and I was able to save us 10 cents per board. And so that obviously helped our margin on this one product that we sell out of 20. You know, it's like, oh, okay.

**Dave Jones:** And that's at Altium. How they handled the bonuses at Altium was that everyone would get a fixed percentage. Right. So everyone would get the same amount, but then you would get another 50%. So no, sorry. Half of it, everyone would get the same. And then the other half would be scaled based on your, based on your salary and your role and stuff. Yeah. So it was like, you know, it wasn't pretty good. It was sort of like half, half, half pizza kind of thing.

**Chris Gammell:** You know what? I bet you still didn't touch what the salespeople were getting now. Like salespeople just get crazy.

**Chris Gammell:** No. Yeah. They get crazy bonuses.

**Dave Jones:** No, my, I've also got a theory about this is that, yeah, no, that obviously matters. I know for a fact that that matters. But hardware engineers actually come with a lot more inherent cost to the company because they're actually, they've got to not only spend money on the wages, right? But they've got to spend money on the hardware that they're actually designing a building, right? That could easily double or triple someone's salary, right? Whereas a software engineer, like there is literally, well, there's not, I'm not going to say there's not any other cost because you've got to buy it. Yeah, there's snacks and you've got to buy them pizza and they've got to buy them multiple monitors and, you know, you've got computers and mainframe, right? But that's the same for almost every employee. Whereas hardware engineers have very specific requirements. Like I could tell you how much just our little tiny hardware group spent on prototype PCBs in a year. You'd be shocked, right?

**Chris Gammell:** Give it. Come on. What is it?

**Dave Jones:** No, I'm not going to give it. Come on. I'm not going to give it publicly. Why not? Let's just say that you could hire a couple of employees. This is like 20 years ago. You could hire a couple of hardware engineers for the cost of just prototyping boards, right?

**Chris Gammell:** That's impressive. Right?

**Dave Jones:** Yeah. Okay. It's serious money.

**Chris Gammell:** Junior employees or like senior employees?

**Dave Jones:** Oh, well, yeah, no. You know, but let's just say that you could at least hire one and you could hire an extra engineer for the cost of, you know.

**Chris Gammell:** Sure. All right. All right.

**Dave Jones:** Just simply prototype boards, right?

**Chris Gammell:** Yeah.

**Dave Jones:** That's blank boards. I'm not even talking parts.

**Chris Gammell:** I get it. Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** Not even talking. Yeah.

**Chris Gammell:** Bananas.

**Dave Jones:** Right? It's nuts. So I think that plays a role in it too, but that's to a manager. That's not what?

**Chris Gammell:** Hey, Dave. You remember when we could buy parts? Yeah.

**Dave Jones:** I'm pretty old, you know.

**Chris Gammell:** I don't remember these days. It was just nostalgia. That was nostalgia kicking in, you know, bubblegum tap shoes and all that. Yeah.

**Dave Jones:** Yep. Yep. There you go. So I don't know. Leave it in the comments. Are you like, are you, is your company mandating that you've got to come back to work and you, and are you going to tell them to stick it?

**Chris Gammell:** Yeah.

**Dave Jones:** Because I reckon there's going to be a, quite a surprising percentage of people who will tell them to stick it. So, hmm. Yeah.

**Chris Gammell:** Yeah. I think it will be.

**Dave Jones:** Speaking of the great resignation, there's a video out. Was it a Wendover one or some, one of the major YouTubers just did a video, which I haven't, no, Fusion. Fusion. What's his name?

**Chris Gammell:** No.

**Dave Jones:** His name's Tagago or somebody. Fusion TV. Cold Fusion TV, I think. Just did a video on that, which I haven't watched yet. So, and, and his videos are usually very good in sort of the Wendover productions style.

**Chris Gammell:** Oh, okay. I'd probably like that.

**Dave Jones:** Yeah. Yeah. So I'll link that in. Cold Fusion. Let me, I'll dig it up.

**Chris Gammell:** Yeah. I don't know. I feel like the, the structure for hardware engineers right now too, though, like the ones who are, I don't know, a lot of them are probably already going to the office. Like just thinking about the shared cost of hardware and like labs and stuff like that. I haven't heard about as many hardware engineers going remote as other, you know, like there's still usually some tie back to an office or a manufacturing space or something like that. So I don't think it'll be as big of a step change.

**Dave Jones:** Yeah. Cause you know, at, at any reasonable size company, you're going to have a pretty good lab that you're not going to have at home.

**Chris Gammell:** Right. Exactly. Right. Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah. I'd love to hear from people. We'd love to hear from people generally, especially now that we have an email address that works again. So shoot us an email. So if that doesn't work, the empire at gmail.com also always pretty much works.

**Dave Jones:** Well, it's actually best to leave a comment down below. So rather than email us directly with your thoughts, cause then people, other people can see it and comment on your comment section.

**Chris Gammell:** Who knows? We do. We also have Twitter, Patreon, if you want to be on there.

**Dave Jones:** Yep. Yeah.

**Chris Gammell:** Definitely be on Patreon.

**Dave Jones:** I don't think we ever mentioned that, do we? No.

**Chris Gammell:** Eh, once in a while.

**Speaker ?:** Yeah.

**Dave Jones:** Anyway, that's all we got for this week.

**Chris Gammell:** I quit for this episode.

**Dave Jones:** I quit for this episode. Damn it. We're not going back into the office, Chris. I refuse to go back into The Amp Hour corporate headquarters.

**Chris Gammell:** That's right. Ain't that the truth.

**Dave Jones:** Catch you next time.

**Speaker ?:** We'll see you next week.
