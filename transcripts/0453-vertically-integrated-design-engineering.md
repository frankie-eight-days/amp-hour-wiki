---
episode: 453
title: Vertically Integrated Design Engineering
url: https://theamphour.com/453-vertically-integrated-design-engineering/
---

**Dave Jones:** This is The Amp Hour Podcast. Released August 4th, 2019. Episode 453. Vertically Integrated Design Engineering.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV Blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. What's up, nerd? Hey, welcome back, friend. Thank you very much. It's been a while for us, yeah.

**Dave Jones:** Yeah, it has, yeah. I was thinking about it.

**Chris Gammell:** I was putting some numbers to it. I was like, I think I've sent three boards to be fabricated since Dave has been last on the show. So we have lots to talk about, I'm sure.

**Dave Jones:** Yeah, yeah, yeah. Brag, brag, brag. Brag, brag, brag. Just work, work, work. Are these your personal boards or are these contract jobbies?

**Chris Gammell:** These are all contract thingies. So I can only say limited things about them. Other than I've been doing some RF stuff, and that's been interesting learning. But the thing I wanted to mention to you today, I don't know if you saw my tweet this morning. I was like searching around. I have this new project that I'm looking to do for an event that I have coming up. And I just want to make something like blinky and, you know, distributed. And I want to be able to like control stuff around the room and stuff like that. And so I was like looking on DigiKey looking for like cheapo chips, you know, pretty much. Just like searching by increasing level of cost. I found one on there that's 57 cents per chip in like less than 100 quantity for a Bluetooth with a Cortex-M0 on it. And it's like, what?

**Dave Jones:** I'm looking at it now. There's zero stock though.

**Chris Gammell:** Oh, yeah. Who do you think bought them all? I bought 245 chips. It's right before I tweeted that link. I wasn't going to tweet it without actually buying all the stock. Right, right.

**Dave Jones:** Buy before tweeting. That's right. It's like the, yeah. It's like that, you know, every time the fire alarm goes off, I like tweet before I leave. It's like everyone goes, no, tweet after you leave.

**Chris Gammell:** That's right, right. Yeah. Oh, yeah. So I don't know. Like I think I'm not sure if I'm going to use it for that project because I think I might want to get more distance. But what I want to ask you about is just, you know, so I've got an idea where I want to like have a bunch of things distributed around a room and just blinky stuff really. And so I want to have it like distributed around a room. I want to kind of have a, you know, basically broadcast all these things. And I was wondering how you might do that sort of thing that we can kind of do a joint design where I pick your brain.

**Dave Jones:** Oh, God. Well, you know, I'm not into the RFE. Yeah, it doesn't have to be RFE.

**Chris Gammell:** So my first thought on this was actually doing IR. And so doing like a blasted IR type thing where, you know, so basically doing like that.

**Dave Jones:** Yeah, and it bounces off the walls, bounces off everywhere. Like if you're used to it, you don't have to point your TV remote control at the TV. Exactly. You know, you're pointing at the roof and it bounces around.

**Chris Gammell:** Yeah. So this will be an outdoor event and it'll be, you know, nighttime when I do it.

**Dave Jones:** I think I've seen Sammy. No, outdoor is a fail for infrared, I believe.

**Chris Gammell:** Oh, really? Okay.

**Dave Jones:** Yeah, because there's too much. Don't quote me on that, but there's too much. Yeah. You get swamped.

**Chris Gammell:** Oh, yeah, yeah, yeah. You mean when it's light out. So it'll be dark out. Yeah, yeah. Yeah, yeah. I agree. Yeah. If you have the sun, and I was talking to someone about that too, it's like if the sun's out, yeah, it's just going to bring the whole noise floor up effectively. And then you need a lot more discerning type of things. Right. So I was thinking about that. And then I was thinking like, like how do these garage door transmitter, maybe like dig into that somewhere too.

**Dave Jones:** They're like 470 megahertz or 800 megahertz. One of the, they're specific bands and it varies by country.

**Chris Gammell:** Right, right. But I'm just thinking like, what is the, I'm trying to get like a bomb cost of less than a dollar. So I definitely want to micro on there of some type, you know, just do breathing LED type stuff and, you know, for be able to shut down low power mode, stuff like that. But just thinking like, what are some cheaper ways that I can maybe broadcast these things so they wake up, check if there's a message. If there is, then they do a thing. If not, they go back to sleep. You know, like standard kind of stuff.

**Dave Jones:** But not only cheap, not only cheap, you want easy to implement.

**Chris Gammell:** That's true. Right.

**Dave Jones:** So let's say, okay, you've bought these microchip ultra low power BLE system on a chip package for your 50, 40 cents or whatever it was. Yeah. Right. Right. Then there's programming. It's going to work forever to implement the protocols.

**Chris Gammell:** Yeah.

**Dave Jones:** Like don't ask how long David too has been working on implementing the USB stuff for the micro supply. Right. It's months. Right. Just to get it done properly and talking and, you know, doing everything else. Right.

**Chris Gammell:** So. Right. And there's so many like iterations and so many different use cases and corner cases and stuff like that.

**Dave Jones:** You might, you might want to look at the ant protocol perhaps, but then again, I don't know how easy that is to implement.

**Chris Gammell:** You know, there's like. I was looking at all these transceivers and like getting, getting a transceiver less than a dollar is actually really tough. And so that's why I was thinking like an IR element is really cheap. Maybe just having like a simple.

**Dave Jones:** Yeah. See.

**Chris Gammell:** LC transceiver kind of thing.

**Dave Jones:** That's how I would do it. I would keep it dumb. I wouldn't implement any high level stuff like Bluetooth, you know, like maybe like Ant or anything like that perhaps. I'd just like, like dumb ass broadcast. Is it just, it's just broadcast. Yeah. So these things don't have to transmit back. Right. Okay. Right.

**Chris Gammell:** You know, I thought about some more things that I could do if I, you know, broadcast is definitely one of the main things I want it to do. And I was talking to a friend about it. He's like, you know, Bluetooth's not great about like distance stuff too, right? Especially if you're outdoors, it's going to be humid climate. As the humidity goes up, then the, you know, the RF, the 2.4 gigahertz.

**Dave Jones:** And everyone else has their Bluetooth phone enabled. So it's swamping the, you know.

**Chris Gammell:** Yep.

**Dave Jones:** Yep. Yeah. And so then he's like, yeah, I would seriously blast it with, um, with a dumb ass simple serial protocol. So you can do it in like 10 lines of code.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** You don't have to set up stacks and all that sort of BS and have packets.

**Chris Gammell:** Well, the other crazy thing I was thinking about though, is that at 54 cents, you know, this might be just as cheap just to put this thing on there.

**Dave Jones:** And just as a micro. Right. Not really.

**Chris Gammell:** I don't, please don't write it to everybody. I get it. There are cheaper micros out there, but like 54 cents for a micro is not bad in low quantities. So. Yeah.

**Dave Jones:** It's pretty good. Yeah.

**Chris Gammell:** And somebody would be like, well, you could do a pick 10 and you could, you know, whatever 10, 8 bit or whatever.

**Dave Jones:** Well, interestingly, I am going to do a video on this soon, but you know, the three cent microcontroller that I did the video on those Hadouk ones, right? The, um, you know, that you can buy from LCSC and, um, uh, several or someone or several people have reverse engineered all of that. They've now written their own, uh, some proper C compiler. Well, they've now, you know, uh, used another, like, uh, added a, um, added support in a C compiler for it. Oh, cool. And also they've done their own, they've reverse engineered the programming protocol. And now there's like an open source, uh, programmer board for it as well.

**Chris Gammell:** Wow. That's great.

**Dave Jones:** For the three cent micro. So I want to try it out. Yep. And, um, yeah, it's, it's, it's not the GCC compiler. It's another one. If, you know, if you could rattle off names of some other open source C compilers, I could probably tell you that's it. You know, you know, this one like supports 8051 Z80s. Um, I think it starts with S or something. Anyway, I can't remember, but yeah, it's been, it's been reverse engineered. So I want to build that up and try it. Um, so that's, that's fantastic, right? Open source solution exists for a three cent micro. This is perfect for something like this. You just need a dumb ass serial protocol. So you only need like hundreds of bytes of memory, right? You don't need like, you know, kilobytes of memory. You don't need, you know, 32 K.

**Chris Gammell:** Yeah.

**Dave Jones:** Of flash on it to just, just receive a broadcast, uh, serial protocol and flashing a few LEDs.

**Chris Gammell:** Right. Right. Yeah. And I think it's, it's about like how much time I have and to put into this thing anyways. Um, no, no, of course. Yeah. Yeah. Exactly.

**Dave Jones:** That's why I reckon you'll get stuck down in the software. Oh, totally. Yep.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** Yep. That's why I think you need to prioritize that as the solution rather than.

**Chris Gammell:** Yep. Right. Right.

**Dave Jones:** And focus on, you know, I'd, I'd, I'd rather pay a one buck for the chip and, you know, and have the software just done and working than. Yeah. Right. You know, pay 50 cents for a chip and have to.

**Chris Gammell:** Yeah. You know, that was interesting. Uh, so Mike Harrison was over on embedded FM a couple of weeks ago and, um, you know, they, Mike had pinged them basically saying, Hey, I want to come defend pick, pick parts. And it turned into a good discussion, but it was interesting hearing, you know, the embedded side of things and, you know, Alicia and Chris were talking about like the, well, they're not, you know, they, they're not against it, but they weren't as big of fans of like the, the pick stuff. But then Mike was talking more about the logistical side of where that comes from. And, and like from that, I think it actually was a, it was a good, you know, that was a, it was really just like looking at it from two different sides too. It's not that there is a right answer. It was just that like Mike was looking at very much from the hardware, you know, focus and the manufacturing side of things. Whereas Alicia and Chris were looking much more at like the, you know, really digging into a thing where, because they're usually working on projects that are, you know, have a bigger support team around it and stuff like that too. So it sounds like kind of, kind of a similar, similar argument you're making here.

**Dave Jones:** Oh, it's, no, it's totally different. Mike is absolutely, I haven't listened to the episode, but I know exactly what he's talking about. Mike, Mike is absolutely correct. He's built his ecosystem around the pick parts. That's why if anyone comes to him as a, as a contractor and goes, I need this done. He's not going to dick around. Oh, this, you know, this STM32 micro is a bit better. No, screw it. Just use the pick for everything. Because he's been working on those for a decade. He's a certified pick, you know, person, you know, where the microchip pick program or something.

**Chris Gammell:** Yeah. The approved vendor thing. Yeah. Right.

**Dave Jones:** Yeah. And yeah. Approved vendor. And he knows it back to front. Right. And it's like, you know, he can just roll that out in 10 minutes while you're still dicking around downloading the C compiler for this microcontroller you've chosen.

**Chris Gammell:** Right. And that's a good point. And so I was thinking about that too. It was, you know, so like I was just finding this because I was just literally searching for the cheapest thing. And like, like you're saying, it's, I'm going to have a ton of startup time and whatever else. Usually the right micro is one that you can get up and get running fast. And like Mike, he, you know, so we've talked to him around here a lot before too. It's, it's, you know, he has libraries ready to go. He has stuff ready to go. Sure. Like everything else is just an act. And I am treating this as more of an academic exercise, learning a new process, learning a new thing like that. So, and I might not even use these Bluetooth chips for this specific product, but I mean, at 50 cents a chip too, you gotta, you gotta do it. You know?

**Dave Jones:** We had, we had that problem for the micro supply as well. It was like, oh, which micro do we use? Okay. Well, it's easy to pick, um, no pun intended. It's easy to pick one that you've used before and you're familiar with. Right. And it's like, but no, you know, no, cause we're manufacturing a, you know, a solution. It's got to have, you know, it had to have the right number of LCD drivers that had to have, you know, all sorts of, you know, the right, all sorts of, uh, you know, stuff that had to be right. And we went through various brands. It wasn't just, you know, we're going to pick the one that we're familiar with. Ultimately we did end up with an STM 32, but, uh, yeah. Which you have used before you're saying?

**Chris Gammell:** Is that what you mean?

**Dave Jones:** Sorry?

**Chris Gammell:** Is that mean, cause you, you're saying ultimately we did because you used it before, like it's, it just shook out like that or what do you mean?

**Dave Jones:** No, no, no. It, it, it actually popped out of the, uh, selection matrix as the best part. Oh, okay.

**Chris Gammell:** Yeah.

**Dave Jones:** So, so we, you know, we were brand ag, agnostic on that. And it was like, if microchip popped out, if, you know, some other one, you know, if a TI part popped out or something like that, then fine. Yeah. Um, so be it, we'll use that.

**Chris Gammell:** But on the next project, that's, that's the real key, right? Is like, if you guys, you know, once maker supplies out and it's working right, you spin the next one.

**Dave Jones:** We would use it again. Yeah. We would, yeah, that'd go to the top of our list. Then the, then the selection criteria would be, no, what not, what is the best part? It's like, can we use this part again?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** Right. And that's our first step approach. And if we can use that part again, then, you know, it's almost a certain thumbs up because, you know, you've already used it, you've got experience with it, it's in your bill of materials, you've got the parts and you're probably going to use the same assembler again. So they've got them loaded on the machine. It's like, there's a whole bunch of advantages to go on with the one you've used before. And that's why Martin sticks with pick. Oh yeah. No, it's huge. Yeah. It's huge. But sometimes as a contractor, you, you have to, because they might mandate, oh no, we, we're a TI company. We always use TI. You must use TI. Yes, sir. Thank you, sir. I'll charge you for, you know, I'll charge you a hundred bucks an hour to, you know, learn how to use TI. Right. Exactly. Yeah. Yeah. Yeah. Right.

**Chris Gammell:** I think the best, you know, the, I think that, um, you know, in a best case fit with like contracting and stuff like that, you're finding someone who already is in the space. They already know that part. They're already ready to go because then that's going to just be fewer hours.

**Dave Jones:** Well, if you're looking for a contractor, you generally don't care. Right. It's like you're looking for a contractor because you don't know the difference between a TI and an STM part. You just want someone to do a job. You've got some high, high level specs. Yeah. That's a good point. Actually.

**Chris Gammell:** Do this. I, so I, I was really worried when I started doing consulting stuff that, that someone's going to come to me and be like, yes, here's this great job. You have to do it with Altium Designer. And I'd be like, uh, yeah, I don't, I don't really do that.

**Speaker ?:** Right.

**Chris Gammell:** Um, but yeah, you're, no, you're actually right on that case. I, I, I have yet to find someone yet who they're like, yeah, well, we prefer you to, you know, do this. But if I'm like, I'm not going to charge you for the switch over if I have to do it, that kind of thing. Um, yeah, I think that that, that has been, that's been fine a lot of the time. So you're right.

**Dave Jones:** Well, it's, it's like Mike again, he's a great, cause he's a great case example.

**Chris Gammell:** Yeah.

**Dave Jones:** He's a great niche case example. Um, he, I believe he uses like an, uh, like a circuit maker 2000, which has nothing to do with the new circuit maker. I think he uses like, like this is a real old school program that hasn't been updated for like 15 years or something. He still uses that cause it just works and it does what he wants. I believe. Yeah. I think he, I think, I think he did.

**Chris Gammell:** I think, I think I remember him talking about that. Yeah.

**Dave Jones:** And it's tied into his pick and place machine. He's written scripts to automatically get the start, the bomb out of there and, and program the pick and place. And it's like, yeah, like it's all fully optimized and, and you don't change that. Yeah. Yeah. I think especially when you've got systems in place. Yeah.

**Chris Gammell:** Once you're doing like vertical integration type stuff like that too, it makes a lot of sense. And then, I mean, that's like, so you think about taking stuff to manufacturing too, like you're really optimizing a process and anything that really moves outside of that process. That's a huge, huge change. And that's like an entire project for someone that's in the manufacturing engineering space, right? They're like, okay, well now we're going to move in this new slot to, to just replicate that behavior. And, and it's kind of the same thing with vertical, you know, I guess it's, it's not vertical manufacturing in that case. It's vertical like design engineering almost of like, if you move outside of this process that you're really normal and used to, then there's going to be, there's going to be problems and, you know, issues and stuff like that. And, and really just time. It's just going to take a lot more time.

**Dave Jones:** Sure.

**Chris Gammell:** Yeah.

**Dave Jones:** So yes, my advice, stick to the easiest software solution. Yeah. Okay. And you'll be sweet. Yeah. Yeah. Yeah.

**Chris Gammell:** Well, the other thing I was interested in doing this for, I know like thing I would plan around with, so I've been doing more RF stuff, like I said, and that's been interesting. Um, and I was like, well, I could, I could give a talk on this, which is a terrible idea. Why do I do this? Right. Uh, giving a talk at, uh, at chaos camp in three weeks in Germany.

**Dave Jones:** I'm not a subject that you're not a specialist in.

**Chris Gammell:** Luckily I'm giving it in the talk in English. That'll, that'll be helpful. I don't have to learn German. So that, that helps.

**Dave Jones:** Oh, okay. Right.

**Chris Gammell:** Uh, but yeah, basically it's like, this is a talk about the perspective of coming at, uh, RF from someone who started in the DC world and DC is actually DC and not like, you know, what a spectrum analyzer says is DC and like, oh, well, we started like a megahertz. So we're cool. That's DC, you know? Uh, and, uh, yeah, just kind of my learnings there and hopefully, hopefully that'll be a good talk. We'll see how that goes. Um, but you know, hopefully I'm hoping to kind of give that talk more than once. I've actually submitted it more than one place and maybe I'll actually give a talk a second time at some point. Uh, but if people are going to be at camp as well, I'd love to hang out too. So if you're at chaos camp, which is in Germany in a couple of weeks, uh, in Berlin, uh, please give me a shout and, uh, we can meet up. So that'd be a lot of fun.

**Dave Jones:** Cool. Yeah. That'd be awesome. Is that every year, every two years?

**Chris Gammell:** Every four years, actually.

**Dave Jones:** Oh, four years. Oh, wow. Okay.

**Chris Gammell:** So it goes, um, last year was, uh, that other camp I went to, which was here in the States up in Seattle. That was a tour camp. Um, there's also one called EMF and, uh, that's every other year. And then there's a second camp that's in, I think the Netherlands that's every fourth year. So like, if you want to, you can go to a camp, a hacker camp every year. Uh, it'll just be a different camp. Got it. So this is, this is the one put on by the same people that do chaos communication Congress, which is every year. Uh, which is there. I thought it was. Yeah. Yeah. That's like a real conference. That's like a indoor conference right after Christmas, uh, in Leipzig or somewhere else.

**Dave Jones:** And that's, that's the conference that everyone wants to publish this stuff. Yeah.

**Chris Gammell:** Yeah. That's, that's a big one. Yeah. Yeah.

**Dave Jones:** I think there's a fairly high standard for what you actually present there, isn't there?

**Chris Gammell:** More than camp because they put that in my crazy ass talk here, Dave.

**Dave Jones:** Right. Okay. Right. Yeah. But yeah, but you're Chris Gammell from the Amp Hour.

**Chris Gammell:** Yeah. That doesn't matter if the content's not. No. No. Oh, okay.

**Dave Jones:** Name, name doesn't do it. Yeah. That's right. Right. Galitarian.

**Chris Gammell:** Galitarian. All right. All right. But yeah, I'm really looking forward to that. But, uh, so I've been playing around with RF and, um, and that's the other thing I was thinking about is like, you know, doing some antenna design. Uh, I've been looking into getting a VNA and so that's been in some interesting stuff. Yep. Um, looking at some of the low cost options. Uh, Shariar, who's been on the show before. He has a, uh, a couple of good, I mean, he has a bunch of videos about really high end stuff, but, um, so low end stuff too. There's one called, uh, I can't remember it now. Feng? No. Good something?

**Dave Jones:** I, I do know the name of it. Yep. Yep. Yep. There's a couple of low end, uh, by low end, are you talking the couple of thousand dollar one or the couple of hundred dollar one? Yeah.

**Chris Gammell:** This is the $2,000 one. Um, right. Yeah. There is one that's like the mini VNA is like, uh.

**Dave Jones:** We, we, we, we, we talked about this like a couple of months back. Oh, did we? I'm sure we did. Oh, okay. Yeah. I'm sure we did.

**Chris Gammell:** Okay. All right. Uh, yeah. So looking into that kind of thing and just building up equipment stores and learning stuff and, oh, you know, I probably did it when I was talking about the book that I was reading, the, uh, the microwave engineering book. Um, and so reading more stuff and actually, oh, there was an interesting thing. I, uh, I downloaded a book about there's a Kindle book about, um, RF layout and I was going to ask you about it. And if you've ever done anything like that.

**Dave Jones:** I have done limited RF layout. Yes. Okay. So not, yeah, not real high end stuff.

**Chris Gammell:** Got it. So like, well, what did that like look like when you were, so basically someone came to you and said, Hey, just do it like this, do it like that. You know, here's kind of the guidelines or, or what did that look like for you?

**Dave Jones:** Oh, it was, it wasn't hugely difficult because it wasn't like microwave stuff.

**Chris Gammell:** Okay.

**Dave Jones:** It was like for, you know, the four, 600 meg range.

**Chris Gammell:** Okay.

**Dave Jones:** So it wasn't really a big deal. I've done like a discreet, uh, transistor RF amp and stuff like that. Oh, really? Yeah. You don't really have to take any, you know, you just make sure all your loops are tight and everything. And you don't really have to care too much about, you know, um, uh, major details like you do, like laying out like, uh, you know, a DDR memory and stuff like that, all those controlled impedance traces with the ridiculously fast, uh, you know, edges and timing requirements and everything. That's much more challenging than doing your, just your generic RF.

**Chris Gammell:** And you just, you mean that's because like, if you get like a 500 megahertz clock signal with, with fast edges, you could be up in the many, many gigahertz.

**Dave Jones:** Up in the gigs, you're up in the microwave range. Yeah. Okay. Okay. Bingo. And, and just, you know, timing and skew requirements and stuff like that. Whereas, you know, RF transmission, you're not, you know, skewing against anything else. Right. There's nothing, you know, there's no timing requirements in there.

**Chris Gammell:** Oh, that's interesting. So it's, yeah. Can you, can you explain a little bit more? I mean, so you just mean that like, because all of this, like, so if you have like a 16 bit bus, they have to get there at the same time. Is that what you kind of mean?

**Dave Jones:** They all have to get there at the same time. That's why you have to use the serpentine traces, which is those wiggly, snaky traces that go around. So not only do your data pairs have to be the same length. So, you know, so all it, so if it's an eight bit database, D zero to D eight, all have to be the same length. And if because, and because when you round it on the board, they're not, they all have to go around different bend radiuses and things like that. Yeah. Right. One of them is going to be, the one on one side where it curves towards is going to be shorter than the one on the outside. It's like going around a track. Yeah. Like being in a race track, right? A track. Yeah. It's being a race track, right? You have to stagger those, you know, start points.

**Chris Gammell:** I would know this because I'm a very fast person and I, I used to run indoor track.

**Dave Jones:** Right. Ah, there you go.

**Chris Gammell:** I was always on the outside.

**Dave Jones:** Oh, right. Yeah. Yeah. Thinking that.

**Speaker ?:** All right.

**Chris Gammell:** I did not, I did not get the, the good starting positions, if you know what I mean, you know?

**Dave Jones:** Exactly. And no, PCB layout's exactly the same. When, when you like, cause the chip is, of course. PCB layout is exactly the same.

**Chris Gammell:** Chris is not good at it.

**Dave Jones:** So they're all starting at the same spot and then you've got a curved track. Yeah. And they're all, and if they end at the same spot, cause they've got to terminate another chip with a flat edge, bingo. Yeah. They're all, so that's why you'll see the wiggly traces. But then not only that, do you have to get the, each one, the, the skew, what it's called actually between each one is the same, the same length. You've got to match those lengths, but then you've got the, they're often a differential pair, right? If you're doing differential pairs, right? So you're doing an LVDS, you know, differential pair or something.

**Chris Gammell:** Yep.

**Dave Jones:** Then you, uh, then those ones have to be matched as well. Right. Yeah. So you've got, you know, like this snake and all around the place, you can have one that's slightly longer than the other. So not only is there a differential length problem, but there's a cross pair length problem as well. And, you know, and, and that becomes a lot harder and they're all transmission lines and stuff like that. Whereas if you're doing an RF transmitter, everything's really just a tight loop, right? You've got your transmit, like you've got your discrete transistors transmitted or these days it's almost, it's almost always just a, just a module. That's why if you go look at the PCB layout for a, uh, for like a wifi module or something, it's nothing. It's a chip with a couple of passive parts around it stitched down to ground. It's got a big ass ground plane on the bottom of it. And then a single trace, which will be controlled, uh, impedance. So like, you know, he only got like one trace going out to the little patch antenna on the board, right? It's a trivial layout. Anyone can do a wifi board layout. Yeah.

**Chris Gammell:** Yeah. My thing was always, uh, keep, keep that, uh, the distance to the UFL connector, which is that little like plugin. Oh yeah. If people don't know what that is, it's like that little one where you see a lot of like antennas plug into that. That little, it's like a little nub. Tiny press on coax. Yeah, exactly. Yeah. Yeah. My thing was always just like, if I can get that as short as possible, I'm usually safe. Yeah. Right. Yeah.

**Dave Jones:** And yeah, so it's not, you know, it's not difficult at all unless you're at the bleeding edge of something like, uh, you know, Sharia would be with his, you know, 50 gig.

**Chris Gammell:** I was looking at your Twitter page earlier today too, to see what we'd be talking about. And like, and you have that big, the picture of the spectrum. That's a mistake. The spectrum. Yeah, of course. Uh, but the spectrum analyzer picture that you have as your, as your background image is another one where like you have the different filters that are built into the PCB and stuff like that. Yeah, exactly. So that's some much more advanced stuff that I would not be doing.

**Dave Jones:** Open up a spectrum analyzer and take a look at that. And yeah, there's some art in that. Yeah.

**Chris Gammell:** Yeah. And you've done tons of tear downs and stuff.

**Dave Jones:** Then you've got to use your controlled impedance, you know, Rogers material and whatnot. Right. Right. And, uh, yep. Can't just get it manufactured at your local, you know, two cent prototype house. Yeah, that's right. Expant. Right. Two cent. Two dollar. Two dollar prototype. You know, dirty, can't get it made at dirty PCB. That's right. Yeah.

**Chris Gammell:** I mean, it's not. I mean, like that, that's when like the PCB is like a significant portion of the actual design as well. You know, like that's the. Right. It's not just routing from here to there. It's no, no, no. This is, this, this PCB is the component.

**Dave Jones:** Yes. Yeah. PCB is the component. Yeah. That's it. Yeah. So yeah. Anyway. So yeah. But it's not a big deal these days unless you're doing something like, yeah, actually designing a high end spectrum analyzer or something. It's usually just a single chip solution. You put a ground plane under it and whack. Yeah. You know, you stitch everything down the ground and you know.

**Chris Gammell:** I just actually posted today too. The TI has an older app note, app note 058, which we'll link in here. They also have like a range of just antenna shapes and sizes and stuff like that. And it's got some background info too. So that's kind of nice, a nice resource. So it's nice to have. Found it's helpful. I'm basically collecting info now. You know, I mean. Right. Yes. Got it. What can I pass off as my own with very, very small attribution links in the bottom of my presentation?

**Dave Jones:** How do you store it all? Do you put the, do you down, physically download the PDF and put it in the project subdirectory under documents? Or what do you do? For that, yeah. That was the go back in the day when I was a boy. Yeah.

**Chris Gammell:** I've been doing that for projects lately because I do a lot of, a lot of GitHub stuff. But, you know, for stuff like this, where this is more of a resource kind of thing. So like an app note like this, I would put this in like my Evernote. I do Evernote for storage. And then it actually, the nice thing about that is it's actually stored on my phone. So if I'm like bored on the train, I can actually look at the PDF and stuff like that. What do you do? You actually do the local storage?

**Dave Jones:** I am often project based. So yeah, I'll be doing like local storage of, in a documents folder. Like, yeah, when I start a project, the first thing I do is actually create a subdirectory, you know, project name. And then it'll have, you know, CAD. Like, you know, it'll have ECAD. Then it'll have MCAD for the mechanical stuff. It'll have documents. It'll have test. It'll have, you know, pro code. So whatnot. Yeah. So yeah.

**Chris Gammell:** I like that too. And I think that's nice too. Like some people don't like that because then when you start getting into the code side of things, you know, like the unbroken chain of commits.

**Dave Jones:** You have to go, oh, where's that? You have to remember where that old code was. Yeah.

**Chris Gammell:** Well, I meant too.

**Dave Jones:** I want to reuse that code. Right. It's like, oh, yeah, I know I've written that routine for that I squared C controller before I rolled my own. Where is it? Oh, I've got to remember which project I did that on.

**Chris Gammell:** I see. Yeah.

**Dave Jones:** You know, so it's like. Yeah.

**Chris Gammell:** I mean, versus like a library, like high level thing where you're. Yeah.

**Dave Jones:** Yeah. Whereas I, you know, but being the one man band that I am, that's how it works. Whereas if you're a dedicated firmware person, right. Yeah. You're going to do it totally differently.

**Chris Gammell:** Yeah. Right. You're going to write like high level libraries. You'll have different systems in place. And you'll implement them.

**Dave Jones:** Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. You, you, you would have, you know, go to libraries that you reuse all the time. Yep. Yep. You know, and stuff like that. So. Yeah. Yeah. Yeah. But no, I just don't do it. You know, it's, I'm, if I'm designed a project, it's, I'm, I'm doing everything. Right. Yeah. Right. So it's like. Well, you're dead. Yeah, exactly. So it's all under the one, you know, it's all under the one subdirectory.

**Chris Gammell:** You guys, you guys doing that revision, revision control thing yet?

**Dave Jones:** No. Yeah. We do it on bloody Dropbox. Yeah. Oh, that's right. That's right. You do that. Effectively. Yeah.

**Chris Gammell:** Hey, look, that's better than nothing. That's better than nothing. I've, I've been saying that for a while. That's good. Yep. Cool, man. Well, how's, how's the, how's the design progressing? It sounds like you guys are in the throes of a firmware hell still.

**Dave Jones:** Oh, it, it, it is the biggest firmware project we've ever done.

**Chris Gammell:** I believe a shamozzle. Is that the word?

**Dave Jones:** It's a shamozzle. Yeah. Now, if you want to do USB, right. Okay. Look, I'll, I'll, I'll, hang on. I'll, I'll pull up the chat log. I was chatting with David who, who actually works from home now. Uh, now, basically he's been working at home for the last, uh, few months. It's, it's just, it's just easier for him, you know.

**Chris Gammell:** I mean, yeah, Sydney traffic is not to be trifled with.

**Dave Jones:** Yeah. No, there's no reason to be here, you know, and he's just moved again. Like there's just, yeah, there's, there's no reason to come in anyway. Um, here we go. Here we go. Hang on. Let me have a look. Here's the update for today. Uh, CDC and HID devices are being recognized by windows. Their protocol isn't implemented only the initialization is, but that's a big step. Uh, language and string descriptors we're working on. So we've got, uh, all these different modes, CDC, HID. Uh, there's another one, HID class, uh, virtual comports. Yep. Um, they have, uh, uh, we're talking about descriptors, composite class devices. You know, you've got to get all this stuff right.

**Chris Gammell:** Yeah.

**Dave Jones:** So yes, but we're also using HID and storage HID for driverless use. Right, right. So you want to be able to actually drop, drop the font there for updates. And, and cause we're, we're going to be pushing our firmware over the, uh, serial port. And the problem is this is isolated, right? So, so what we've got is we've got, right? This is, you know, this is complicated.

**Chris Gammell:** You guys are doing isolated power off the USB.

**Dave Jones:** And then we're doing isolated power off the USB, right? So we've got a processor, a USB processor on the primary side of the transformer, right? So this is where you plug the USB port into your computer or your phone or, or your whatnot, right? So that handles all the, uh, the, the power delivery system. Right. Which I can talk about in a minute. That's another can of worms we've spent months on. Right. So, so that microcontroller has its own firmware, of course. It's got to, uh, handle all of that, um, all of the power delivery stuff. So it's got to negotiate all the power. And then it's, so then we have to have the ability to firmware update that. And then we go over a, an isolated optical serial link.

**Chris Gammell:** Right.

**Dave Jones:** Right. So a serial link to the main processor on the isolated side of it. And we want to be able to update the firmware on that via, over the optical serial link via the second, via the primary side processor. Right. We want to update that secondary side processors firmware via the primary, you know. Right.

**Chris Gammell:** So you've got to put it in a special mode and then actually dump.

**Dave Jones:** You've got to put it in a special mode and it's got to do that. And it's got to do, we're doing VCP and CDC and HID modes and all these sorts of stuff. It's like, it's just nuts. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** And I think we mentioned the other week that we, uh, had to, uh, the other week, months ago that we, that we had to change processes on that. Yeah. Right. Right. We, we, we had to change our USB chip on the primary side because it ran out of memory and couldn't do stuff that the manufacturer claimed. We started using it. We designed the board. We put it on there, built prototypes, started, you know, it was kind of, sort of working. And then we realized, nah, it couldn't do what, what the manufacturer said. It could do all this sort of stuff. And their example code didn't work. And, you know, so we had to go, nah, let's just abandon that. And we had to, you know, re-spin and we had to redo the whole thing, start from scratch. Yeah.

**Chris Gammell:** That's nuts.

**Dave Jones:** With a new processor.

**Chris Gammell:** Well, then USB has its own, uh, you know, so there's got its own like pitfalls and like, like, uh.

**Dave Jones:** Oh, if, if, if, if you want to do it right, if you just implemented a simple, like. You know, serial, you know, USB, serial, virtual serial. You grab a chip. You order something. It's easy. With all the drivers. Right, yeah.

**Chris Gammell:** Like the, uh, CP2102 or the.

**Dave Jones:** Or something like that. Yeah. It's trivial. But no, we, we, we have to do a ton of stuff. So we have to. And then you've got to make it easy and driverless for the user. Right, right. To install. You know, you don't want to be writing your own drivers and stuff like that on the PC. That's right. Yeah.

**Chris Gammell:** Because then you have to like distribute a software package and a actual update and stuff like that. Yeah. Yeah, yeah. So there's a, um, there's a talk that happened at Teardown, um, uh, last month that was really, really good about USB and like, like actually like peering into what the data packets look like. Um.

**Dave Jones:** Oh, that's the thing. David, I, we finally found a use for my USB protocol analyzer, right? Yeah, yeah, yeah. I've got the high end USB protocol analyzer. Yep. And, you know, I've never had really a project to use it on. And David says that what he's doing would be impossible without this USB serial packet.

**Chris Gammell:** Right.

**Dave Jones:** Analyzer. And he found a bug in it that, um, yeah, he has to go back to the manufacturer and goes, look, it, you know, I think this is a bug and I can't continue my work unless this bug is fixed. Yeah, yeah. It's like, you know, how much you rely on those serial, uh, on those, uh, USB debugging tools. Yeah. Because if it doesn't work, you just throw your hands up and go, I don't know. Right, exactly.

**Chris Gammell:** You just keep plugging it in, unplugging it, plugging it in, unplug it, unplug it. Yeah. Yeah, so, so Kate and Michaela gave this.

**Dave Jones:** You cannot just, you cannot just use your scope and put it on the USB lines. That's right. And expect to be able to see anything useful. That's right. It doesn't work. Right.

**Chris Gammell:** Yeah, so Kate, Kate and Michaela gave this really, really good talk about this. Um, uh, it's basically an open source USB tool, low cost. Like it's actually like some of it's software based. So if other people are doing USB things, like it was a really, really good talk. Um, so I'll link that into, uh, but like, yeah, I mean, like, what do you do when USB goes wrong? Like, I think they, one of the examples they gave was like, there was like a reset packet that was maybe not even reset. It was like one of the earliest packets that was happening and it wasn't working, you know? And, and like thinking about like peering into that, like other than seeing, is there activity on the USB bus? Other than that, like, what am I going to do? I'm going to be like, well, I guess I'll just try and solder this thing down again and see if it's just a bad solder joint. You know, like that's effectively the level. Right. It's effectively like operating without a scope. Clutching a straw. Yeah, exactly. I mean, like, it's, it's just, it's just, it's called cargo, cargo cult type stuff where I'm just, you know, trying this, trying that, holding the tongue out at the wrong angle, you know, like. Yeah. Yeah. So it's really, I'm really glad there's, there's tools that are coming out for that kind of thing. Cause whoo. Yeah. I think it'll just make it more accessible.

**Dave Jones:** And like, and, and for those who, who know the USB, I'm sure they're going to correct us, but David's saying, oh, the HID returns just one end point, but CDC requires three end point. It's bananas.

**Chris Gammell:** Yeah. I don't know.

**Dave Jones:** So CDC is easily the most complicated and expects he'll get notifications from the HID tomorrow, which I think is today. And, you know, and, and, and then he's saying, look, I can do this, the, the dirty way or the proper way. And it's like, and I'm like, and he's going, which one he's asking me, which one do you want me to do? Like, I can have something up and running quicker if I do it the dirty way, but we might get caught down the track where he'd have to rewrite the whole thing. And this would be after it's actually, you know, we've shipped out units and it's actually delivered to customers and whatnot. And I'm going, no, Murphy will bite us in the ass. Just, you know, spend the extra days, you know, we've already spent, you know, six months working on like various, you know, power delivery stuff and various USB stuff just on the software side of things.

**Chris Gammell:** Yep. Yep.

**Dave Jones:** It was like, I, I, I never expected it to be this, like, if I knew it was this much work from the get go, like I thought, you know, I thought that we'd just use a USB capable chip and the drivers would just work and, you know, like everything would be hunky dory. It's like a week's work or something, you know, it's like, like it should just like use the example code and it should just all work. But no, it's, if you want to do it properly.

**Chris Gammell:** Right.

**Dave Jones:** And I realized that you're, you're aware of those portable soldering irons, those, you know, little USB powered. Yeah.

**Chris Gammell:** Like the TS100.

**Dave Jones:** The TS100 and the TS80. Yep. Yep. I found out why, why the TS80, which I love. It's, it's better than the TS100. It's better than the TS100 fanboys go wild. Yeah, right. It's right. It's right. It's really nice, but you can only power it from quick charge.

**Chris Gammell:** Yeah, that's right. Yeah.

**Dave Jones:** PAX, right. They use the quick charge standard. You can't power them from the much more popular and widespread power delivery PD standard ports. Right. Why? Because David's trying to implement PD and it is enormously complicated. Yeah. It's a shit show. If you want to do it properly, right, you know, if you want to implement, that's why they just use the quick charge thing. It was quick and easy. Right. It was quick and dirty. It just worked. They just plugged in the chip and it probably just, you know, used default code and it probably just worked. Yep. And, but power delivery is a much more complicated beast. So that's why they, that's why it doesn't support that. And, and, and it makes sense. Why, why support the lesser known and almost dwindling standard only when, when you're not supporting the most popular and biggest and most widespread one that's, that's actually dominating because of the engineering work involved.

**Chris Gammell:** Wait, so which one's actually dominating?

**Dave Jones:** The, the power delivery standard. That, that is the standard. Oh, okay. Whereas the, whereas the quick charge is a specific Motorola. I think it came, it's a Motorola thing. Got it. Okay. Right. So my, my old, my, you know, so they, they developed it. A couple of other manufacturers kind of, sort of picked it up. Got it. You know, it was kind of, maybe it was like an open standard or something.

**Chris Gammell:** I was going to say like, is this all based on like reference designs and what's actually available? Like, like, like, you know how like every Bluetooth speaker is the exact same reference design, you know, is it like that kind of thing?

**Speaker ?:** Yeah, yeah.

**Dave Jones:** That's probably what they did. That's probably what they did for the Hick charge. And that's how they got their solder and iron. And that's what they, but they, you know, but it only supports a small number of these packs, these battery packs.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. And that's what, you know, so, so, so just because they didn't want to do the engineering work, they've actually completely crippled their product into a tiny niche market.

**Chris Gammell:** Or, or Dave, you know, you sell a thing that can only work on quick charge and then you sell that for real cheap. You sell the quick charge battery pack for a lot of money. You sell it. Yeah. You know, it's sneaky like that. It's sneaky like that. Oh man.

**Dave Jones:** We'll, we'll sell custom battery packs with the micro supply. That's right. That's right. Yep. You know. Anyway.

**Chris Gammell:** The one, the one is a loss leader. It's a loss leader.

**Dave Jones:** Right. Yep. It's just, yeah. Like the printers and the ink cartridges, right?

**Chris Gammell:** Exactly. Yep.

**Dave Jones:** Right. Yep. He's a free printer.

**Chris Gammell:** Yeah. Yeah. Remember that was happening? Yeah.

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** I never. Still is. Yeah. I guess so. I don't.

**Dave Jones:** I was at my post office the other day. I was waiting in line at the checkout and, you know, I don't know if the post offices in the US are the same, but they basically, you know, they, they're like a little shopping.

**Chris Gammell:** And yeah, they're trying to make margin on the other stuff.

**Dave Jones:** Yeah. Yeah. Yeah. You know, so as you're standing in the line, they've got all these things next to you and you just, oh yeah, I'll pick one of those. Often they've got real good bargains there. Anyway, it was like, yeah. And, and they had like laser printers, you know, it was like, yeah, they had like, yeah, they have like two of them. It's not like they have hundreds of, you know, they have like two per store or something. And yeah, they'll have cameras. They'll have, you know, phones. You can, oh yeah, I need a phone. You know, I'll just buy it at the post. Check out. That's different than here. Yeah.

**Chris Gammell:** That's different than here.

**Dave Jones:** Oh, okay. Right. Okay. Anyway. So they, and there it is. Laser printer, 30 bucks.

**Chris Gammell:** 30 bucks. Australian. Oh my God.

**Dave Jones:** Right. That is like how much you, that's, that's like $20 US.

**Chris Gammell:** Yeah. Yeah. That's nuts. Right. I mean, that's like.

**Dave Jones:** Retail at the, at the post office. Post office. Right.

**Chris Gammell:** So that 20 bucks is pretty much going to the post office. At least. At least. Pretty much. 10 to $15 of that is going to the post office.

**Dave Jones:** It's just like, come on. It's insane.

**Chris Gammell:** Oh. That's nuts.

**Dave Jones:** Yeah. It was free. Like it was like in terms of a printer, it was practically free. That's great. Yeah. Nuts. Anyway. Yeah. Cool.

**Chris Gammell:** All right. So should we go on the list now? We have been on the list.

**Dave Jones:** Oh, I'm giving a talk. I'm giving a talk.

**Chris Gammell:** Where are you giving a talk?

**Dave Jones:** Yeah. I'm giving a talk. I'm giving a talk at a school.

**Chris Gammell:** Yeah.

**Dave Jones:** I was invited to give a talk on renewable energy.

**Chris Gammell:** Oh. You're going to talk about solar roadways, huh?

**Dave Jones:** I asked this on the forum. I asked this on the forum. And like half the people said, yeah, they've got to know about it. They need to know about critical thinking. Yeah. And the other half said, no, don't tell them anything negative. These kids need to be supported and live in their safe space. Well, they didn't say safe space. But, you know, they need to, you know, they need to only be encouraged. I think inspired.

**Chris Gammell:** Inspired is the word, Dave. Yes. Inspired.

**Dave Jones:** So, yeah, inspired. So, guess which option I'm taking.

**Chris Gammell:** Of course you're going to take the first option. Yeah. We did it.

**Dave Jones:** But, no, you know, like 90% of my talk will be inspiring, you know, and the rest will be, well, just sometimes, you know, don't be so open-minded that your brains fall out. Yeah. That's good. Right. Yeah. Yeah. And I do actually have a slide with the Carl Sagan quote. That's great. That Carl Sagan quote. Yeah. That's a good one.

**Chris Gammell:** When are you doing this?

**Dave Jones:** I'm doing it Monday. Nice. So, after this, straight after this, I've got to finish off my slide because it's Friday here. So, I've got to finish off my slide so that I can send it to the teacher there, the headteacher, so that they can not really approve it, but just like, hey, this is what I'm, you know. You know, is this sort of, is this what you want?

**Chris Gammell:** Right.

**Dave Jones:** You know, kind of thing. That's great. That's great, man. Yeah.

**Chris Gammell:** I'm not giving any talks this weekend, but I'm actually, I'm headed to Vegas tomorrow, which is, you know, in August. In the States, great time to go to Vegas, of course. It's 110 degrees Fahrenheit. Right. Or 42 degrees C. Got it. And whatever the number is.

**Dave Jones:** Well, it's not peak, though. If you went a month, month and a half ago, it would have been peak.

**Chris Gammell:** It's pretty bad. Oh, no. It's pretty bad.

**Dave Jones:** In July? No, no, no. Okay. Yeah. Yep. It's just coming off peak.

**Chris Gammell:** It's pretty, it's a dumb time to be there. But anyway. But there's a big security conference there at Black Hat. And I'm helping past guest Joe Fitz with his workshop. He's giving a workshop for four days, two different workshops in each day. We're doing hardware hacking and reverse engineering for people who have never done hardware before. And it's very exciting to see how this is going to go. There's going to be milling machines, 3D printing, actual like, you know, then just some of the standard like, you know, having logic analyzers and spy bus and, you know, actually like decoding stuff. But this is actually like making stuff, like making a PCB, making a 3D printed thing, making jigs and doing it in a conference room at Black Hat. It's going to be, it's going to be very interesting to see how it all goes. And I'm really excited. And, and actually speaking of. Is this going to be recorded? No, no, no, no. This is like one of those paid trainings. So this is a, yeah, this is.

**Dave Jones:** Oh, oh, oh, it's a paid. Yeah, yeah, yeah.

**Chris Gammell:** So like, and that's, that's like a big thing. So like a lot, you know, I'm still really not confused, but I'm interested in it. Like the security industry, man, there is just so much, like, there's such a strong culture around training and it's really impressive. But it's also like, like, these are not cheap trainings. These are like the standard corporate trainings that are like thousands of dollars.

**Dave Jones:** Oh, yeah. They're thousands.

**Chris Gammell:** And they fill up, you know, and then, then there's a, and Black Hat's like a conference that costs a couple thousand dollars to go to. It's just like a standard industry style conference.

**Dave Jones:** Oh, so you can't, so it's, so there's not just like a free, you can't just rock up to Black Hat.

**Chris Gammell:** No, that's, there's a, so then like, I think B-Sides is lower cost, but then DEF CON is right after as well. So it's like a bunch of conferences kind of happening all at once in Vegas. They're all security focused, but then, you know, I go to hang out with the hardware people. Yep. Um, but I'm really excited because, uh, MG is going to be there. And if you remember MG, he's the one who was doing the, we talked about him on the show. He was doing the milling of the, uh, uh, the solder mask. Remember that it was like a, a milled board, but it had solder mask on it. Oh, yes. Right. So he's helping with the workshop as well. And I'm going to pick his brain about, about, uh, how the hell he was doing that. So really excited about that. And, uh, yeah. And then I'll be at DEF CON for a day as well. You know, that's like the badge life stuff. And, uh, so again, if people are out, out and about love to, love to hang out. Um, yeah, it should be, should be a good time. Inside, of course, not, not outside. Cool. So, yeah. Uh, yeah. So teaching hardware. We'll see how that goes.

**Dave Jones:** We just don't have the same stuff here.

**Chris Gammell:** Yeah. Well, you know, like something like that could, I mean, you could do that at the, so like the Linux conf is coming up in, in January, right? That's the one that, uh.

**Dave Jones:** It, it is. Um, I think it's down in Tasmania. Oh, is it really?

**Chris Gammell:** Okay. Cool.

**Dave Jones:** I don't know. Yeah. Yeah. I think, yeah. It's there, but I don't think it's ever been in, I can't remember the last time it was in Sydney. I've certainly, certainly haven't gone to it.

**Chris Gammell:** That's like one of the biggest ones though, I think.

**Dave Jones:** Yeah. I'm not sure if there's a hardware aspect to it this time. I had a look a couple of weeks back at the website and I couldn't really see anything.

**Chris Gammell:** I thought John Oxer helped do like, like Linux conference stuff.

**Dave Jones:** Yeah, I know. That's what I thought as well. But anyway. All right.

**Chris Gammell:** I'll, I'll take a look. I'll take a look. I'm looking for somewhere to go in the cold depths of the winter. So maybe that would be a good time to come visit, you know? Right. You know, you know, business travel, Dave, business travel. Of course. Of course. I think it would be one of the mini confs on there too. So we'll see how it goes. But there was a bunch of stuff. I thought down in Australia that you guys were doing some, I keep seeing RISC-V stuff pop up all over the place. I thought it was at Linux conf. Maybe it was something else. Maybe that was actually just Tim Ansell at there doing that last year or something. But I keep seeing RISC-V pop up everywhere, including Alibaba.

**Dave Jones:** Yeah. What the? Yeah.

**Chris Gammell:** That's interesting. So basically.

**Dave Jones:** They have a chip group.

**Chris Gammell:** Yeah. I'm not sure. We couldn't, we were looking at this article earlier. We couldn't really figure out why. I guess it's some of it's, I guess Alibaba has server division. So there is that. They kind of operate like an AWS. Oh, of course. Yeah.

**Dave Jones:** Like Amazon roll their own servers and stuff. And Google and Microsoft all make their own servers. Yeah. They also like design and build their own.

**Chris Gammell:** But Microsoft isn't, so like Facebook has servers, Google has servers, everybody else. Most of them are not yet doing their own chips, I don't think. I think that's maybe on the path. And maybe that's what RISC-V is going to kind of do more of. But it seems like in China right now, because of like all the ridiculousness with the tariffs and stuff. The government. Yeah.

**Dave Jones:** Huawei banning and all that sort of crap.

**Chris Gammell:** Well, and then arms stepping away too. It's like, okay, so now like what are their real choices in terms of chips? It's interesting if it's going to drive, if it's going to drive China just be like, all right, we're just going to do our own thing. Who cares? You know, like they are very, not as resource constrained, you know, as they used to be.

**Dave Jones:** So China's going to be like the Soviet Union of the, you know, 70s and 80s. They were just doing all their own chips. Like they'll just copy it. Like Soviets had their own industry, right? Sure. They weren't using Intel chips. They were like, right? Right, right, right. I think less of a global thing anyways. They couldn't even buy like TI, TTL chips, right? They couldn't even buy like just generic off-the-shelf TTL chips. So they have their own generic brand TTL chips. Oh, okay. Right, right. If you open up any Russian bit of kit, it's like, yep, that's a 7474 flip-flop, right? But it's not from any of the manufacturers you've ever heard of, right? It's all Russian.

**Dave Jones:** Interesting.

**Dave Jones:** They've got their own part numbers. They've got their own manufacturers. They roll their own silicon and they copy it, you know, often. Yeah. Yeah. But yeah, it's like they had their own insular complete industry.

**Chris Gammell:** Right, right.

**Dave Jones:** It's like completely cut off from the rest of the world.

**Chris Gammell:** I can't help but think that's not a – I mean, obviously, I don't think this is a good idea anyways.

**Dave Jones:** No, it's a bad idea.

**Chris Gammell:** It seems like it's just a step backwards too because then it's like people that would have been – I know. I like the idea of an open ecosystem, of course, with RISC-V stuff. I think that's great, right? And if this maybe pushes that forward a little bit, maybe that's an unintended consequence that's kind of nice. But like ultimately, I would think that there would just be more drive, like just more money in the system. Like if Intel knows that they can make another billion dollars, they're going to keep pushing themselves internally in order to like to push out that next node or that next chip or whatever. Same thing with ARM and, you know, at TSMC and everybody else, right? It's just like money is the driver of economic growth. Usually the ones that are leading the pack anyways are going to continue to push forward to that next thing. And if now everybody is going insular and it's like, oh, well, we're just going to do our own thing now and we'll take a step back. And it just seems like that's going to slow everything down.

**Dave Jones:** It's going to ultimately fail. It's just done. But, you know, politics.

**Chris Gammell:** Politics, yes. Realities of the situation.

**Dave Jones:** It's getting in the way. Like, you know, now all the rage is in the political circles is let's ban encryption or let's put backdoors into every encryption thing. It's like, no. It doesn't work like that, you dumb asses. It's like, come on. It's like, yes, the famous Australian prime minister came out and said the laws of mathematics are very commendable, but Australian law comes first.

**Chris Gammell:** Jesus.

**Dave Jones:** You dumb ass. Our prime minister actually said that. Wow. Uttered those immortal words. Wow. The laws of mathematics are commendable. But it's trumped by Australian law. So if we tell you to put a backdoor into an encryption system, you have to do it even though it's not technically possible. Jesus.

**Chris Gammell:** Yeah.

**Dave Jones:** That's the level of dumbness we're dealing with when you reach the political level. Yep. Anyway. Yeah.

**Chris Gammell:** You know, I've been watching. So I watch a lot of these. So I get the Jetix Smart Brief. That's one that I get. And then I also get Woodstock Wire. Those are like two newsletters that I'll often use to seed the subreddit with stories and stuff like that. And it's interesting because I've seen a couple stories lately. And, you know, it's not trend making at all. It's just like, you know, my ears kind of perk up or I guess my eyes in this case. And I've seen a couple like higher profile like manufacturers, like contract manufacturers have started to shift operations and started to move stuff around. And when Scott Miller was on the show two weeks ago too, he was talking about that as well. You know, just that like industry isn't going to wait around for whatever. It's just they're going to go and try and find the best deal because they have to make their margins. And it's like it's I'm just going to I'm interested. I'd love to hear from people, you know, like leave a comment if you're if you're seeing similar things just because it's hard to tell. Right. No, no company's going to be like we're moving all of our operations. We had to shut down. You know, like not everybody's going to announce that unless they're a public company. So I'd love to just hear, you know, boots on the ground kind of information from listeners. It's like they're like, oh, yeah, well, you know, we're not traveling to China anymore. We're moving stuff to Vietnam or whatever's happening. I'd be I'd be interested to hear from people.

**Dave Jones:** So you want a bunch of people to leak stuff to the Ampera.

**Chris Gammell:** That's right. That's right. We're the yeah, we're the we're the new source, Dave. I mean, I'm just personally curious. I mean, like it doesn't seem like, you know, from a high level, it doesn't seem like much has changed other than like, yeah, I pay tariffs now. And it's like that sucks. But I'm on a very small level.

**Dave Jones:** The whole tariff thing, like people just shrug their shoulders and and carried on, didn't they? That really didn't.

**Chris Gammell:** Well, at the level I'm at, yes. Caused a big ruckus, did it? But like I'm not buying enough stuff from China for it to matter. Well, of course. Yeah. So I think that, you know, that could have.

**Dave Jones:** So I'm sure there's companies that have gone under because of the tariff. Yeah.

**Chris Gammell:** I think that I think that it could really, really impact some people if you're on a thinner margin.

**Dave Jones:** But I certainly haven't heard. It's not like, you know, everyone's complained on the forum about the tariff. It was like.

**Chris Gammell:** Yeah. Yeah. Right. I mean, like that's the thing. Like some people, I mean, it depends on what scale you're at. And if you're, if I think about like the engineers that I know that are like lower level, most of them are not going to be impacted. Right. It's like, yeah. Okay. Like I'm shipping stuff in the States. It's less than $800. I don't have to pay tariff. That's fine. Right. That's, that's most of the people that I know doing stuff. If you're doing like low scale manufacturing in the States, like, okay. Yeah. You're going to start dealing with stuff. But you know, sometimes you're just like, well, what I'm going to do is switch over to a CM overseas. No, I'm not going to do that. But then if you're like at a medium or a large level, right, to where it actually would have really, really insignificant cost impacts, you're probably not allowed to talk about your work publicly, you know, like. Yeah. Yeah. And until the amp hour comment section where we don't ask for an email or we don't, you don't have to use your real name, but you know, please don't lie, you know, but yeah, I mean, like I'm just generally curious about it. So, and that's the thing, I think it's one of those things where it's, if it, if it is happening in the background, it's going to, you know, we're going to find out from just contacts and hearing about it and maybe a couple of small stories here and there. I don't think it's going to be like, because people want to make waves on the political side of things, they're going to be like, ah, whatever, you know, it's a, it's a thing. But I'm, I'm curious if it actually is having impact. And I think there might be. So we'll see. Okay. Uh, on the risk five things, uh, there is also a link that we have on the subreddit risk five from scratch, uh, which is interesting. Uh, basically, uh, you could do everything, right? So you can do tool chain setup and all the way through to like getting, I think this is on the code side of things. Um, but, but pretty interesting to actually get it up and running. And, uh, you know, like I said, I think, I think I'm really bullish on risk five in general. I think it's, you know, there's going to be some circumstance.

**Dave Jones:** I hadn't noticed. Right. I know.

**Chris Gammell:** I know. Circumstantial things that are coming through. I actually, I went on a podcast and I talked about it, uh, with, uh, I was, I was on a 3M podcast and I, I, I brought that up as the thing that I'm most looking forward to is, uh, is open tool chains and risk five. So, um, uh, yeah.

**Dave Jones:** Yeah, no, it's, it's very impressive. And like, even I, as I mentioned earlier in the show, I got excited when that three cent microcontroller, now there's a tool chain. Yeah, exactly. Right. Like where, whereas before you had to use this sort of like custom quirky single executable downloaded from the manufacturers, some weird, it wasn't even, you know, proper ANSI C, it was like quasi C. Yeah, right. And it was kind of, you know, like C-ish. And, uh, and, and you had to buy their program, right? Right. Right. You know, you couldn't like, yeah. And there was just like no information on it. Now it's like, yeah, everyone's reverse engineered that. And apparently it works. So, you know, it's great. So now it opens up, opens that up to greater number of people. It's fantastic.

**Chris Gammell:** You know, one thing on the three cent micro and then also the tariff stuff too. I, I went to go with order from LCSC today. I was like really excited about it because I had an order one with their, their partner PCB house and they stopped doing that. Did you know that?

**Dave Jones:** Oh, what, what, what, they stopped doing the boards?

**Chris Gammell:** They stopped, no, they stopped. So JLC still does boards and LCSC does, still does parts, but it used to be you could buy parts and then. Oh, so you can't bundle them anymore. You can't bundle them anymore. That sucks. Right. Anyways, just from shipping. Yeah. Yeah. Yeah. I've been, oh, that was another thing I was going to talk about is the, uh, I've been doing it where I was really pissed. There was an article that LCSC got some investment from like Sequoia, China and stuff like that. And most people don't give a shit about that and that's fine. Um, but the reason I was upset is because they started listing like legit parts on there. You know, I was, I went there cause I wanted to see like, and I would still like to see this. You know, I tweeted about this a couple of weeks ago. I still want to see like, what is the most commoditized footprint out there? I don't care about brands. I care about commodity. I want to be able to, to drop six different parts in the same footprint. And so that I have a little bit of like, you know, continuity between, you know, if, uh, if a chip company makes something and it's like, you can do that if you go back to the seven, four series logic and you're on standard footprint sizes and stuff like that. But you can't, you can't do that with like switching regulators and microcontrollers and stuff like that.

**Dave Jones:** And so I was more, I, Oh, you can.

**Chris Gammell:** Okay. Tell me.

**Dave Jones:** Yeah. There are some switching microcontrollers that are generic jelly bean, but they're not the best solution. They're not the easiest to use. They're not the most efficient, you know, they're blah, blah, blah.

**Chris Gammell:** Right. And I, you know, and I guess some of that I accept like the, the, as you go up in complexity, like, you know, the, even the switching regulators that I'm talking about, usually it's because they're modern parts. They have modern processes. And then they have these crazy ass late late or footprints rather fine, whatever. Um, but like things like switches, I don't care about switches. Like, come on. I, I, I just want like the cheapest switch that I can get that a lot of parts will switch into and that I can keep driving the cost down. And, you know, obviously resistors are, are fine. Uh, LEDs are fine. There's standard, standardized.

**Dave Jones:** Your regular passives, your transistors, your, you know. Right. Or fairly generic jelly bean. But yeah, no, once you get up into your more complicated.

**Chris Gammell:** Even like, even like diodes, you know, like, so like it's just a standard Schottky diode, you know, thinking there's a ton of parts out there, but I want to just know what is, what is the most voluminous part count out there. That's all I really care about. And I just want to drop that footprint down so that I can, honestly, so I can usually go figure it out later too. If I can just put a footprint down, I'm like, oh, SOD 123 is fine. I'll be able to find a part for that. That's great. You know, like I just need these standard, you know, kind of like that thing we were talking about at the top of the show with like, you know, vertically integrated design engineering. It's like, if I just know I'm going to drop a diode and I can definitely find a part for it, great, you know. But if I have to go find one of those, you know, NexFet crazy ass, you know, 16 pin, you know, it's like a monstrosity of copper and polyamide and whatever else is in there, you know. It's like, yeah, it's tougher. So that's why I was going to LCSC and then now it's all like flooded with real parts. That's the end of that story. Sorry.

**Dave Jones:** Oh, what? So LCSC is flooded with real parts. Yeah.

**Chris Gammell:** So like they started like.

**Dave Jones:** Because they used to be mostly like Chinese.

**Chris Gammell:** They called it like Asia brand or something like that. But they were showcasing parts that you usually can only get in China. And that's what the value was to me. Like that's what I care about. But now it's like, oh, well, no, you can buy like a little list like a TI part on there or something like that. I don't think, I don't know if TI is.

**Dave Jones:** Which is fine as long as they're not taking the Asia stuff away.

**Chris Gammell:** And they haven't, but it's just flooding the whole space for me. You know, they want to sell more parts. Fine, whatever. I want to go there.

**Dave Jones:** They want to become a mouser and a digi key. Exactly, exactly. They want to, they can sniff the opportunity. Exactly. And that's fine.

**Chris Gammell:** But I just want to search specifically in the low cost region.

**Dave Jones:** Right. Yeah. Well, can you isolate that as a filter actually on the website when you, like I want Asia only brands?

**Chris Gammell:** I'm not sure actually. Maybe.

**Dave Jones:** Is that, you know?

**Chris Gammell:** But it's still gunking up my, it's gunking up my thing, Dave. I want to.

**Dave Jones:** Anyway, I was going to look at doing that. This is interesting because this three cent microcontroller, right? I was going to do a video where I actually built this thing up and got it working and everything. And I was going to like do, do the community a favor by actually, actually making an online bomb, right? Available at digi key or mouser or LCSC or somebody, right? That just had all the parts. Like, you know how on, how on these websites you can post like a public link to a bomb, right? So that every, so that, you know, if you want to build one of these, you don't have to go in and go, oh, I need this resistor and this transistor and I need this chip. And I, you know, it takes you hours, right? If somebody's already done all that work, you just, you know, just hit the link for that bomb, order all those parts, bang, they come. Right. And I was going to do that with both the parts and the board as well. So I was going to make the board publicly available, like I was going to, because it's open source anyway, right? So I was going to upload it, but, but then people don't have to do the problem of uploading it even, right? Like downloading it from the GitHub or whatever, and then uploading it to their manufacturer. They can just order it. It's already done. So what is the go-to?

**Chris Gammell:** Yeah.

**Dave Jones:** What are the go-to places for making a publicly accessible PCB and bomb list like that? Like what is, you know, mouser and TGK are the obvious ones for the bomb, right?

**Chris Gammell:** I mean, for the PCB, I would, you know, normally when I'm sharing something like this, I would just share a parts, sorry, a GitHub repo. I think that from my perspective, that's what I usually would prefer.

**Dave Jones:** Yeah, but it's no, no, but see, but if you're like a GitHub repo, right, then you've got multiple steps to do it. If somebody just wants their three cent program in micro, right? It's all they want. They have to go to the GitHub, find the board, download the board, find, find the correct Gerber files, make sure they're all okay. Upload them, check them to make sure they've got all the, you know, the uploads done. All right. Make sure they've selected all the correct options on the PCB manufacturing side of things, and then cross their fingers and hope they got it all right. And then press the order button, right? Whereas if it's already, you can do this with the micro supply board, and I can't remember where it is. Somebody uploaded it. Yeah. Because it's open source. Somebody, not micro supply, the micro current board. It's on one of these, you know, public PCB house websites where you can just order one.

**Chris Gammell:** Got it. Yeah.

**Dave Jones:** If you want a blank micro current board, apparently you can just push a button on a website and they'll send you one. Yeah.

**Chris Gammell:** So like Oshpark has like a marketplace like that.

**Dave Jones:** It might be Oshpark. Yeah. It might be. So Oshpark has that.

**Chris Gammell:** I think PCBWay has that now. I think.

**Dave Jones:** Oh, PCBWay have it. Okay. Oshpark. Who was the other one?

**Chris Gammell:** PCBWay and Oshpark are the two that I'm pretty sure does that. And then like. Right. Have a public. I think Seed might do that as well. I'm not sure.

**Dave Jones:** Right. They might. Okay. All right. Yeah. I have to check if LCSC do it because that's where I get my boards from at the moment. I have to check if they have like a make it a public option or something. Don't like PCBWay. Don't one of them like make it public by. Like if you use their low cost service, part of the terms are that you have to make it public or something like that.

**Chris Gammell:** I sure hope not.

**Dave Jones:** I can vaguely remember something like that. I know. It's like. I didn't think so. If you want your boards for $2, you've got to make them public. It's like otherwise they cost, you know, $10 or $20 or something. I don't know. I don't know. Something like that. I don't know. That's its own.

**Chris Gammell:** It's its own little.

**Dave Jones:** Yep. You have to watch out for that.

**Chris Gammell:** A microcosm of craziness. Right. All right. So we're almost done here. I wanted to ask you about your Apollo 11 stuff real quick that you did a shit ton of stuff there. So how was it?

**Dave Jones:** I went down there for four days. Yeah. I spent four days down there talking to the original trackers. I met Andy Thomas, who was the Australian born astronaut who's been on three shuttle missions. That's super cool. And that was, yeah, it was just an awesome time. Yeah. It's absolutely fantastic.

**Chris Gammell:** Awesome. Awesome.

**Dave Jones:** So, yes, you had a question.

**Chris Gammell:** I'm just generally about the experience and stuff like this. So those are all, all those videos are EEV Discover if people haven't seen them.

**Dave Jones:** So most on EEV Discover, some are on EEV blog too. There's one on EEV blog, which, yeah, is like my, like my own summary.

**Chris Gammell:** Yeah. Okay. So that might be a good place to start too. And we'll link all those in too. Anything unexpected about that? I mean, did you, did you kind of see?

**Dave Jones:** Well, I discovered, I had no idea. I had no idea about the ARIA NASA tracking plan.

**Chris Gammell:** Oh yeah, that was cool.

**Dave Jones:** Right? People think that to track the Apollo missions that they only had the three tracking stations, right? Canberra, which we've been to, the Goldstone one in California and the Spanish one. Right? And people think that was it. No, that was only a third of NASA's entire tracking network. They, they had not only a fleet of ships tracking ships, but they also had these tracking aircraft called ARIA that, that actually have this steerable dish in the nose. They converted these 737s. I, I, no, it's anyway, Boeing planes, right? Big planes, yes. Yeah. Anyway, they converted them with this big, like big Snoopy nose on the thing. And, and these dishes could track and they, and they were taking these, um, flying them all around the world so that you can track all of your low earth. Like, like they couldn't like actually talk to the moon, right? They couldn't receive signals from the moon, but you have to track the Apollo aircraft. You have to, uh, spacecraft in earth orbit. Mm, yeah. Right? And the only way that you can't do that with three ground-based tracking stations.

**Chris Gammell:** Right, right.

**Dave Jones:** It doesn't work like that, right? Once it goes over the, the, in fact, a ground-based tracking station can only track an Apollo aircraft in, in earth orbit for like six minutes.

**Speaker ?:** That's right.

**Chris Gammell:** Yeah, I remember one of your videos too, you were talking about this, or maybe it was an older one with Richard talking about, uh, the, the speed of the dish moving, I think it was. And it like, it just can't move fast enough because of the arcs that it's flying through.

**Dave Jones:** It cannot move. It cannot arc. Yeah. It, it, it can't slew fast enough across the sky. So that's why they had to move. Yeah. Uh, the, the big 70 meter dishes are 0.1 and 0.2 degrees per minute. Yeah. Whereas the, whereas the tracking dishes, they can do three or five degrees per minute. Yeah. You know, they're like six or eight times faster and they slew. And, and I met, met the guy who was in charge of the Aria aircraft. He was there. That's super cool. And, and I, and I got him on camera, did an interview. It's fascinating.

**Chris Gammell:** You know, you know what's interesting to me about that is that like, for some reason, all the other stuff they did, of course there was tons of stuff there, but for some reason, like that level of like, like, like logistics and costs and everything else they did, like, yeah, that makes it feel like it's even more expensive for some reason. Like, of course they were spending people on the moon. They were spending so much money, but for some reason that, that's like, oh yeah, now it's, now it's expensive.

**Dave Jones:** No, you have no idea what went, people have no idea, even if you're an Apollo buff, like I am, you have no idea what actually went on at the lower details of stuff you've never heard about it. Just the switching exchanges, right? I was, I was talking to one of the guys there telling the story about how, oh, if it wasn't for me, nobody in the world would have seen those Apollo missions. Cause I was in charge of this one little, uh, line that came out of this telephone exchange in whatnot and I fixed it and, and everyone got to watch it. Right. Nobody knows this story. That's great. Right. And if, and if that one line went down, boom, the whole world wouldn't have seen, you know, the moonwalk. It's like, you know, people think it's just, just the dish and then it's no, there's this whole massive infrastructure of, you know, so many links in the chain. It was phenomenal. And you just don't hear about them because they didn't fail because they worked. That's right.

**Chris Gammell:** And, and, and there was probably redundancy on redundancy on redundancy. But at the same point, sometimes.

**Dave Jones:** Oh no. Some of them weren't. You were, you'd be surprised at the, oh, that the number of links in that chain that were, that if they went down, that was it. There was no redundancy.

**Chris Gammell:** Nice.

**Dave Jones:** For, for certain phases of the mission, for other phases of the mission, but, but for the actual moonwalk as Neil was coming down that ladder, there was, you know, pretty much a no, no redundancy. It was. Yeah.

**Chris Gammell:** Wow.

**Dave Jones:** Yeah. Anyway. Yeah. Crazy. That is crazy. Crazy. So yeah, it was like fascinating stories. And these guys, they, yeah, 50 years later, they can tell you which switch they flicked. Right. That's great. To, to do this thing. Unbelievable memories. Oh, wow. Yeah. It's, it's like it's yesterday for them.

**Chris Gammell:** That's great, man.

**Dave Jones:** It's fantastic. Yeah. So yeah. So yeah. That was four days of just hearing all these stories.

**Chris Gammell:** You're earning out pretty hard.

**Dave Jones:** Most of it, most of them I didn't capture on camera. So, you know. That's good, man.

**Chris Gammell:** I'm glad you got to go down there. Yeah. It's awesome. It was a lot of fun. I saw the, maybe I saw you share it or someone share it, but that Apollo 11 real time too. If people haven't seen that. Yeah. I, I, I shared that. That was fantastic. Yeah. Really cool.

**Dave Jones:** That. Yeah. And I met the, um, I met the, the, one of the producers of the Apollo, of the Apollo 11 movie. And he was one, he wasn't just the producer. He was one of the guys who actually he's, he's actually an archivist. He's not actually a movie producer. He's a, he's a, he's an archivist. So he's the one who got all the audio out of the archives and processed it all like 60 different channels. Like I'm talking, you know, like, like six days worth of 60 different channels of audio that they had to, uh, not only get out of the archives, they had to process, polish it, you know, clean up to make it. Then they had to figure out how it all synced and timestamped and everything else. And sometimes they only had like one little, one little snippet of like, like two seconds in a video where they went, aha, this, this controller in the back corner there said that. So therefore I can sync up. I can use that as a reference point to sync up all this other data over here. And it's like, oh my God, they spent years syncing up all this audio.

**Chris Gammell:** That's great.

**Dave Jones:** Which if you haven't seen the movie, watch Apollo 11. Oh, oh. And you've got to watch it on the big screen. That's the one. Yeah.

**Chris Gammell:** I was like thinking about it. I was like, I've seen Apollo 13. I was like, nope, that's not the movie Dave. That's not the movie Chris. No, no, no. Apollo 11.

**Dave Jones:** You want to know what the best thing about the Apollo 11 movie is? We'll finish with this. The best thing is that there's no commentary.

**Chris Gammell:** Oh really?

**Dave Jones:** There's no commentary. There's no, you know, none of the astronauts talking about their experiences and all that sort of crap. Right? You can get that anywhere else. This is just all an hour or hour and a half or two hours of all archive footage in order. So they start about, I think they start like eight hours before the launch or something. And then it's just, and then they take you through sequentially. And it's like, because they had like 50 different cameras. They found all this original 65 millimeter footage and all the original commentary. So there's no audio and no video in this entire movie that is not, that wasn't actually recorded by the people on the day.

**Chris Gammell:** That's awesome. Yeah.

**Dave Jones:** Yeah. And it feels like you are there, you know, and it's just, yeah, it is absolutely remarkable.

**Chris Gammell:** I might not take you up on the big screen thing, but there is, they're on, they're on rental right now. So I might just go rent it.

**Dave Jones:** No, no.

**Chris Gammell:** I don't know if I can find it on a big screen. I'll see if I can.

**Dave Jones:** Dude, IMAX somewhere. You've got to see it on IMAX. All right.

**Chris Gammell:** All right. I'll try.

**Dave Jones:** Trust me. It'll, trust me. It'll change your life. You'll thank me. All right. Yeah. Cool. Yep.

**Chris Gammell:** All right, man. Well, we'll talk to you soon.

**Dave Jones:** All right. Catch you next time.

**Chris Gammell:** To the moon.
