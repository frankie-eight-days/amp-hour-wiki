---
episode: 363
title: An interview with Alvaro and Jen from the URE Podcast
url: https://theamphour.com/363-an-interview-with-alvaro-and-jen-from-the-ure-podcast/
---

**Chris Gammell:** This is the Amp Hour Podcast, released October 15th, 2017. Episode 363, an interview with Alvaro and Jen from the Reverse Engineering Podcast. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Alvaro Prieto:** And I'm Alvaro Prieto from the Unnamed Reverse Engineering Podcast.

**Alvaro And Jen From The Ure:** And I'm Jen, also from the Unnamed Reverse Engineering Podcast.

**Chris Gammell:** Crossover Podcast. Welcome, guys. How you doing? Good.

**Alvaro And Jen From The Ure:** Okay.

**Chris Gammell:** All right. Well, the name. We got to talk about the name to start with. What name? Yeah, exactly. Exactly.

**Alvaro And Jen From The Ure:** Names are hard.

**Chris Gammell:** How long has this show been on the air? I guess we've mentioned at one point, but...

**Alvaro Prieto:** So we have four episodes, but they're very erratic. We started the first one, maybe in August or early August?

**Alvaro And Jen From The Ure:** No, July. Oh, July. Yeah. I think it was July 18th.

**Alvaro Prieto:** Yeah, so we record, then we pretend to edit for a while and eventually put it up. We're still learning.

**Chris Gammell:** Okay. Well, you know, consistency. That's what we always say. That's the only reason the Amp Hour is still around. He says after not posting an episode last week. Yeah. So, well, anyways, welcome. I have taken a list of the show. It's some interesting stuff. And so why reverse engineering? I mean, what about that, you know, piqued your interest in the first place?

**Alvaro Prieto:** I mean, I first... I've always liked taking stuff apart, but what really got me into it was Micah. Micah Scott, when she did her Coaster Rout videos. I don't know if you've seen them.

**Chris Gammell:** Oh, yeah. Yeah. Yeah. That's the CD. That's some of the CD, right?

**Alvaro Prieto:** Yeah, I think it was a Blu-ray player. She was reverse engineering so she could control the laser and do all sorts of stuff. When I saw that, I thought it was the coolest thing. And it kind of got me much more interested in taking a little more in-depth look at that on my own. And that's when I did little quadcopters and that kind of thing. That's how it started. What about you, Jen?

**Alvaro And Jen From The Ure:** Well, I didn't get into quadcopters, but we've been talking for a while in the background about doing reverse engineering and that there just wasn't an easy way for people to learn more about it, particularly because we want to learn more about it. And we know the best way for us to do that is by interviewing a bunch of people who know what the heck they're doing. Or maybe they don't know what they're doing, but they're really good at pretending. So we just kept talking about it for the last year and a half. And then finally, I think sometime over the summer, we just had hit our point where we're like, you know, it's time for us to go do this.

**Chris Gammell:** You got to hit record at some point, right? Yeah. Yeah. That's great. Well, so and Jen had written to me, I had mentioned on the show a couple weeks ago, I was going through like past guests and I was trying to say, I was saying that we really haven't had many consumer electronics people on the show before. And I think that was pretty well, I actually haven't reviewed since, but I think that was pretty well proven. But obviously, I know a lot of people out in the Bay Area, you're both out in the Bay Area, and there's a lot of consumer stuff going on out there. So can you give us kind of a rundown of your backgrounds and what you're allowed to talk about for the, you know, the consumer level electronics stuff?

**Alvaro And Jen From The Ure:** So mostly, I've been a firmware engineer on a lot of different consumer products, and they kind of run the gamut between startups and large companies. So I've worked on, for Movea, when they were still doing mice and keyboards, a bunch of XDSL modems back in the 90s and early 2000s. I even worked on the U-verse set-top box and the Amazon Fire Phone, which is probably my least, probably the product that people least like. May it rest in peace. And then finally, something, I've been working on some sort of denim-based product lately that has been around now, I guess, for about two weeks now. Cool.

**Chris Gammell:** Okay. What about you, Alvaro?

**Alvaro Prieto:** So I started, I guess in college, I did a co-op, and it was a train track control system company, and I was doing firmware.

**Chris Gammell:** But a consumer one, huh? Well. Sorry.

**Alvaro Prieto:** Sorry.

**Chris Gammell:** I'm just imagining something being like, I really need this for my backyard.

**Alvaro Prieto:** Oh, for my back train yard, perhaps. Yeah, right. But that's how I got started in firmware and industry, I guess. And then when I graduated, I went straight to TI, and I was doing firmware there. And then I got recruited by Apple, and I worked there for like three and a bit years. Then I switched over to Satellites, which is also not kind of consumer, but kind of fun at Planet. It used to be Planet Labs, now it's Planet. And then I took five months off, enjoyed my life, and now I'm at a medical device company.

**Chris Gammell:** Very cool. Well, so that's a lot of devices, too. So I guess that kind of leads to the first question is, what is the pace? I mean, so I believe that's what me and Dave were talking about, is that just the development cycles and the pace and stuff like that, and really the stress. So could you give us a comparison of like, so Alvaro, you've done the industrial stuff. Jen, have you done industrial as well?

**Alvaro And Jen From The Ure:** Yeah. Actually, the other thing for the last episode that you guys released, you guys were talking about PC 104. I worked for another PC 104 single board computer company, so I was giggling a lot about you guys talking about system on chip.

**Chris Gammell:** That's always people's reaction, is they're giggling. I don't know if you guys saw Paul, one of the DIY battery Powerwall things, he did a reaction video. He was like laughing and just scalding us. A reaction video to the Empire? Yeah, it was fun, actually. I rather enjoyed it. Paul's out in New Zealand. It was great. Yeah. But yeah, so okay, so you both have industrial experience as well, so give us a compare and contrast. What's the difference in the feel and the working situation like?

**Alvaro And Jen From The Ure:** Well, I guess, at least for me, I have a handful of customers on the industrial side. I just need to deliver to them whatever they are going to do for their final application may actually be consumer-facing, but for the most part it isn't. It's just dealing kind of more one-on-one. One, they're a little bit more tolerant of what they want, and they're just buying in bigger volumes. Whereas consumers, it's death by a thousand complaints. Okay. And it's just a lot more visible when you fail.

**Alvaro Prieto:** Yeah. My consumer electronics is a little more special, I guess, because Apple. So it's a little different.

**Chris Gammell:** Who's this Apple? Who's this Apple I've heard of?

**Alvaro Prieto:** Yeah. It's a small company in the Bay Area. Yeah. But yeah, they don't follow the usual rules of a small consumer electronics company. And I was more in the R&D side of things. So I dealt more with prototypes and that kind of thing, and internal products as well. Okay. But I worked with people from all over.

**Chris Gammell:** So, I mean, but either way, I'm sure that you've talked to or saw the design cycle stuff and people, you know, you're talking to people that are outside of your groups, perhaps. Is it, you know, is it a three-month design cycle? Is it a six-month design cycle? Is it noticeably different from working in an industrial company? Or like, what is that like?

**Alvaro Prieto:** So, I mean, from what I've noticed, industrial, the deadlines are a little more flexible. You know, with consumer electronics, you get a hit. I mean, cell phones are yearly cycles nowadays, right? Sure. But a lot of industrial stuff, it'll just get pushed back. It's like, well, oh, well, that's just what happens, you know? And people are just going to get their whatever device later. Seems to be the case, at least in my experience.

**Alvaro And Jen From The Ure:** There's a little bit of luxury that you have when you're launching a product line that you have a little bit more time. Because once you launch that first product, the iterative ones happen on that yearly cycle, which means you're locked in. You're a lot less likely to take on new risky features. Usually those are already mapped out as you're closing up the launch of the previous product. So, once you're on the cycle, there's just, it's just, you just keep running, running, running, running. And there's just not as much innovation that's happening.

**Chris Gammell:** Got it. Okay. Yeah. So, that makes a lot of sense that it's, especially because the overall, so like I think about the industrial stuff. The stuff I used to work on, I remember I had, I was, I guess both companies that I worked at in the industrial space. I was refreshing product lines that were 30 years old. Right? I mean, like, so, but phones obviously don't do that. At a certain point, they just scrap the whole thing and not start over, but, you know, start from a new code base, a new hardware basis, because the hardware is changing so much too.

**Alvaro Prieto:** Yeah, but I guess the urgency isn't there. If it's a 30-year-old product, if it's made it so far, you don't need it.

**Alvaro And Jen From The Ure:** Oh, no, there's urgency. But I thought there was urgency, especially if you have end of life, going back to sugar board computers. Once that thing goes end of life, there's panic.

**Chris Gammell:** Right. Well, and that's usually the problem, too, is that the product line refresh. Usually people are like, oh, we'll be fine. We'll be fine. They're like, oh, crap, we can't buy the processor anymore, because it's a 68, you know, HC, 68, HC, 08 or whatever it is. 11 something. Yeah. Yeah, whatever it is. Yeah. That horrible design.

**Alvaro And Jen From The Ure:** I hate that one.

**Chris Gammell:** I just did the stuff around it. But, yeah, I mean, either way, they never actually refresh it in time. And the scramble, I suppose, is like you said, Jen, it's just that, you know, hurry up right now. We've got to keep making money. Or else you're just going to cancel the whole thing. So, yeah. That's interesting. So, yeah, the other thing about the timeline stuff, too, it's interesting with the numbers, right? So, if you have 10,000 paying customers paying, you know, $5,000 each, right? Or 10 million customers paying $5 each, right? It could be this. I don't know if that math works out. But whatever. If it's, you know, it's a difference in, it might, the overall money might be the same, but the per unit cost could be radically different, right? So, if you have to hit that mark or else you won't be able to sell it for $5,000 or whatever.

**Alvaro And Jen From The Ure:** You're not going to get your, achieve your economies of scale. Yeah. You know, at some point as your volume goes up, you want to be able to save some amount of money. You should be able to negotiate better prices on all your parts and all the packaging and distribution channels when you get there, when you get to millions of units. Mm-hmm. And that's the nice thing about industrial.

**Alvaro Prieto:** You don't have to worry about a lot of that stuff, right? You can use a slightly more expensive part. You don't have to start a penny pinch. If you're only going to sell 5,000 of these, it's not a huge deal. Mm-hmm. Yeah.

**Alvaro And Jen From The Ure:** I think it depends. But what I remember it being a big deal when we did packaging for some of these single board computers, like, ooh, look, a clamshell for us to ship in. It was a big deal that we went that far.

**Chris Gammell:** Right. Yeah. It's got that extra touch and cost and whatever, right?

**Alvaro Prieto:** There was a whole article about don't try to do what Apple does. I don't know if you remember it, how just getting a white plastic that's actually white, unless you're doing it at some ridiculous scale, it's just not worth it. I'll try to find it and we can put it.

**Chris Gammell:** Was that Ben Einstein, maybe, like the Volt Ball blog?

**Alvaro And Jen From The Ure:** I don't remember.

**Chris Gammell:** I know he writes about Apple a lot. Let's see if I can find it. Yeah.

**Alvaro And Jen From The Ure:** So there's the quality control even around those consumer parts. Mm-hmm. What I was going to comment upon was, so the way that Apple goes about, and I can't speak specifically to what happens internally to Apple, but talking with some of their other vendors for manufacturing stuff to get similar outcomes for different colors of devices, let's say. You end up with just a lot of industrial samples. You have those golden samples that are sitting at the end of each manufacturer line to make sure that each batch that comes out is either acceptable or not before you start putting them on the backs of your product that's going out the door.

**Alvaro Prieto:** Yeah, it is the bold one. Yeah, that's great. That's great. That's a good link to have there. Yeah. No, you can't manufacture that like Apple does.

**Alvaro And Jen From The Ure:** No, they go through a lot of pains to get that done.

**Alvaro Prieto:** Yeah.

**Chris Gammell:** Yeah, right. So both of you are in the firmware side, though. So what does that end up playing out like? So you're talking about hardware. Obviously, we're talking about hardware here. But what does that end up playing out with in terms of the efficiencies that you were talking about? So you said the economies of scale. Obviously, you get better per piece pricing because you're buying so many and stuff like that. But I also assume that you need to really, really cut down the code base to try and get that cheaper part in there, less memory or whatever. So how does that end up impacting the firmware side of things?

**Alvaro And Jen From The Ure:** Elvro, did you want to talk about this? Because otherwise I'll rant for an hour. Oh, go for it.

**Chris Gammell:** All right, here we go. It's the gen show.

**Alvaro And Jen From The Ure:** We'll cut you off. I don't know if I'm going to quite get it to an hour. Okay. So what I'm noticing, at least in consumers, like from the get-go, your hardware team is already picking the smallest part possible. And very rarely is there, unless they're particularly sensitive, they're not necessarily going, hey, do you really need this really big part? Otherwise, we're just going to pick the one with 128 on there and that'll be that. But there's just generally not that much back and forth, at least that I've noticed on the last, I would say, last six or seven companies I've worked at. In addition to that, with the economies of sale, I would say at least from my perspective, I don't know about you, Elvro, but I often end up doing the manufacturing for a lot of my products also. And that all started because I used to be the super junior.

**Alvaro Prieto:** What do you mean by the manufacturing? Like the manufacturing tests?

**Alvaro And Jen From The Ure:** The manufacturing tests, the writing all the scripts that drive the test stations, designing the assembly test stations, knowing what the timing was, figuring out how to get all that information, logging all the information, get up to back end so operations can then look to see where the big fallouts are. So at one point I was driving all of that in a couple of different companies that I've worked at just because when I was earlier in my career, if you were the low person on the totem pole, you got to do all that work. And so now it just continues. Now I just get to do it in China.

**Chris Gammell:** Right. Oh, Jen knows how to do that. That's dangerous. Right.

**Alvaro And Jen From The Ure:** So when I worked for Bia Sport, I was the director of engineering. And even though I was doing some firmware work and some algorithms work, there was no mechanical engineer. So I became the mechanical engineer for the company, in addition to spending a lot of time in China crying and looking at the electronics markets and not being paid.

**Alvaro Prieto:** That's what happened to me at Planet. I was originally going to be doing firmware for manufacturing. Oh, close. Not at the office. I originally was supposed to be writing firmware because there was a firmware team, but I was in the manufacturing team that I was going to do firmware specifically for testing. But I ended up just writing test scripts because there was not enough time for me to just not work on the line and get this special firmware up and running. And after six months, I am now a test engineer. I was doing R&D, just firmware and stuff at Apple. I went to work on satellites. I'm supposed to be writing firmware. And then I'm afraid what's going to happen, the same as Jen, that, oh, you're good at testing stuff. And that's going to be the rest of your life.

**Chris Gammell:** Right. Right. They love to have those people, but they don't pay them that much more. Well, exactly.

**Alvaro Prieto:** It's mostly, I mean, I don't mind doing that, but that's not what I wanted to be doing at the time. That's not what I was told I was going to be doing. Right. Because it's fun to automate stuff and do all that stuff. But I want to write C. I mean, it's cool to learn Python and do all that stuff, but I don't want to become the testing guy. Right.

**Alvaro And Jen From The Ure:** But you know what? You're in a unique position, Alvaro. You know hardware. And even with firmware engineers, a lot of them don't know hardware. They don't understand how a product can break when it's being assembled. Because you're no longer testing the design. You're testing the assembly of that particular unit.

**Alvaro Prieto:** Yeah, exactly. And it's a different mindset. So your firmware might be fine and you have a hardware problem or your hardware's fine, you have a firmware problem. I used to be that person that can go in there and figure out which and then fix it.

**Chris Gammell:** Yeah, the fixer. Yeah, exactly. The fixer is necessary, but it's the hours and the pay.

**Alvaro Prieto:** I wish it was a rotation program or something. Yeah. Because there's these things that nobody likes to do, but they have to be done. Yeah. And imagine that each team does it for one month or something and then nobody suffers too much.

**Chris Gammell:** Right. Well, some of this sounds like it's also big company versus small company type stuff. Not that Planet isn't growing, but like all these companies, you know, like obviously you were Apple, not a small company. And you were able to, you know, I know some people in the testing group there, but it's a very defined role versus a startup where it's like, well, just get this thing out the door and maybe launch it into space or whatever. Yeah, don't do all the things yourself.

**Alvaro Prieto:** Yeah, no, Apple has, you know, everybody is doing their one thing they do best kind of thing, right? Right, right. We didn't have enough people applying it and that's why I ended up on the line because we have to, the rocket's going to launch with or without you.

**Chris Gammell:** Right, exactly.

**Alvaro Prieto:** You better test these things and get them on there.

**Chris Gammell:** So going back to what Jen said about the processor selection. So that sounds common, right? I mean, the decoupled hardware versus firmware decision, obviously that's not a great thing to do because, you know, like, I mean, not that you had the firmware pre-written anyways, you know, so they're kind of just guessing on how much firmware is going in there. But so how did that, how did that end up playing out then? So you've got a fixed amount of memory on the processor. You've got, you know, you've got these constraints that you had no input on, fine, whatever. But then you also have a time constraint of a deliver time. So how does that end up playing out in terms of, is it like, are you allowed to, I mean, do features actually get cut out?

**Alvaro And Jen From The Ure:** Can you repeat your question again?

**Chris Gammell:** Sure. Sure. So, so the firm, the firmware is the, the, actually, I don't know what the question was.

**Alvaro And Jen From The Ure:** You were going down the road. It was like, hey, they didn't converse with you. So what happens when?

**Chris Gammell:** Shit sucks, don't it? Yeah. Yeah. That's, that's like the, that was, that's the synopsis. Shit sucks, don't it? I feel like this is turning into a therapy session. It's more like, here's your circuit Morton of this processor.

**Alvaro And Jen From The Ure:** So I'm just going to comment on it. So at least, and I think, you know, maybe, I think you, I think you've had other guests that have come on here and they remember there was a time period when the firmware engineer and the hardware engineer were the same person. There wasn't really a separate team. And now.

**Chris Gammell:** And that happens with small teams as well, right? I mean, that's another thing that happens, right? Yes and no.

**Alvaro And Jen From The Ure:** It's, it's not nearly as common as it once was. And yeah, you know, at least, at least the, when I talk with older hardware engineers, they remember writing firmware. That is not necessarily the converse.

**Alvaro Prieto:** Yeah, but a lot of times you look at that firmware and you want to cry.

**Alvaro And Jen From The Ure:** Yes, that is also true. That'll bring us to a different separate rant. But to go back to your question, and this also ties in with cycling through different job positions is that it's hard for you to understand as a R&D engineer necessarily what customer's experience is going to be unless you actually put yourself in that position or how to understand or how to design for manufacturability unless you're put in that position, unless you have to like basically dog food your poop effectively.

**Alvaro Prieto:** Well, that's why I like this rotation thing is like if you've been in the manufacturing test area, next time you're designing a product, you're going to put in all those features. It's what they call design for testing or testability or whatever. And I'm sure it's the same for your customers, right? And once, if you're using the product, you're going to kind of know what you want it to do in the first place. Right.

**Chris Gammell:** You're at least going to weep when you can't find the USB port and you're going to be like, oh, I should tell them where the USB port is or whatever it is, right? Some kind of, some kind of empathy in design.

**Alvaro And Jen From The Ure:** Yeah, I think it's kind of bordering along that.

**Chris Gammell:** Someone did a talk on that.

**Alvaro And Jen From The Ure:** Yeah, wasn't that covered by another podcast?

**Chris Gammell:** The test engineer for the customer or whoever. Sure. Yeah. Who was it?

**Alvaro And Jen From The Ure:** Yeah.

**Alvaro Prieto:** Embedded? Yeah. Someone else? I think it was Chris Vick.

**Alvaro And Jen From The Ure:** Yeah, I think it was.

**Alvaro Prieto:** Oh, cool. Empathy driven design or something.

**Alvaro And Jen From The Ure:** I think he came back twice, didn't he?

**Alvaro Prieto:** Yeah. Oh, he's a regular. Yeah.

**Alvaro And Jen From The Ure:** Now he is. Yeah.

**Alvaro Prieto:** Okay.

**Chris Gammell:** So where are we going with all this stuff? It's your show. I don't know.

**Alvaro And Jen From The Ure:** So I think you were trying to get me to throw hardware engineers under the bus. No, I mean, not trying to get me to throw them under the bus. You were talking about how, like, hey, something's already been pre-chosen for you. And now you got to figure out, like, how you're going to make it work. And then there's this deadline that's looming over you. And it's a hard deadline. Well, the first thing I want to comment upon is that it's not a hard deadline. And I would say for a lot of products out there, there really isn't a hard deadline.

**Alvaro Prieto:** They'll tell you it is. The product managers are going to be like, no, it has to be done by this date or else. Or else what? And it never gets done. Well, they just say, you know. It's like, no, we have to do this. We have to do this.

**Alvaro And Jen From The Ure:** You've had really nice product managers. I remember my first product manager would just regularly threaten my job if I didn't get something done by tonight. Oh, really? That's another topic. I feel like we're getting down a therapeutic route. But anyway, so a lot of times what ends up happening is, at least on the last few projects I've been on, it wasn't the firmware that was late. It was the mobile app that was late, and they were the ones that were struggling to get things done.

**Chris Gammell:** Yeah.

**Alvaro And Jen From The Ure:** So it's just kind of like you just pass.

**Chris Gammell:** I'm not trying to throw anyone under a bus. I'm just trying to get to, you know, so the baseline question was, how is consumer different, right? And so we've kind of talked about the volume stuff. Obviously, that plays out. I've been asking about the firmware stuff because I think, you know, that would be different. Obviously, I don't have as much firmware experience in general. But, yeah, just kind of, I guess the baseline question is, how is consumer different?

**Alvaro Prieto:** Well, one thing for a consumer that you might do that you might not, well, but one thing you might do with super high volumes that you might not do for a few hundred devices is you might have to get the parts pre-programmed, right? So you have to have your firmware ready ahead of time because it might be too small to have a programming header on there or at least put a bootloader on it, right? That's something that with the bigger equipment, you can have your connector or that kind of stuff and then program it right before it goes out. Whereas a lot of the high volume stuff, you just want the chips pre-programmed or program the factory before it goes out.

**Alvaro And Jen From The Ure:** So I can put this in perspective of all our favorite products, which we'll just put under the general header of Internet of Poop. And this day and age, the product never stops developing. It is always being updated. It's always being improved. So instead of thinking that you have to meet a deadline with all the features ready to go, you have to think about your firmware getting to a certain minimal viable product. And I think you guys talked at some point about lean startups and Steve Blank.

**Chris Gammell:** We've had Eric on the show, yeah.

**Alvaro And Jen From The Ure:** And I've met Steve Blank and that whole group of people. But today, more and more organizations, whether they're hardware, mobile, wherever, they're running less waterfall and more iterative. And the way that IoT is set up, this works really well. So you just need to make sure that my gold master, which gets flashed into a product three to four months ahead of when we actually have the product land in someone's hands, can boot up, connect to the backend server somehow, and get updated with all the newest, latest, and greatest features that day zero. And make sure that is solid.

**Chris Gammell:** Right.

**Alvaro And Jen From The Ure:** That's all I have to do.

**Chris Gammell:** And just like, don't brick itself, right? Yes. That's the main thing?

**Alvaro And Jen From The Ure:** Yes.

**Alvaro Prieto:** Yeah, you need a solid bootloader. If you screw that one up.

**Alvaro And Jen From The Ure:** I need a solid bootloader. And depending on what happens, I need a solid app.

**Chris Gammell:** Oh, okay. Because sometimes it gets delivered through the Wi-Fi app to the app and then app through Bluetooth to the device or something like that.

**Alvaro And Jen From The Ure:** But the, oh, I was talking about the app on the firmware itself. But yeah, the mobile app, I guess. But the mobile app doesn't need to be ready until literally the hour before launch. And I've worked for companies where it was done literally the hour before launch.

**Chris Gammell:** That's terrifying.

**Alvaro And Jen From The Ure:** Somehow made it up on the Google Play store. Somehow made it up on the iTunes store just literally in time. And right after that, we all got drunk and passed out.

**Chris Gammell:** Support requests be damned. Yeah. Yeah, no, that is interesting how that changes the dynamic of the development cycle then because of those consistent updates.

**Alvaro Prieto:** I don't like it. It makes us lazy.

**Chris Gammell:** Really? Okay.

**Alvaro Prieto:** Well, because now your product doesn't have to be finished, right? Like John said, you need your minimum features. You might have promised all these other things. And then you ship your product. But then, okay, you have the idea, oh, I'm going to implement all these other features. But they always start pulling resources or they tell you to start working the next thing. And people start half-assing things. And it just...

**Chris Gammell:** Right. And then I guess if you're not getting enough of the baseline features in there, then it's like this self-fulfilling prophecy of like, oh, well, we're pushing this thing to market. It's not completely done. And then, oh, people don't seem to like it as much because they're, you know, it's not...

**Alvaro Prieto:** It's more about people getting lazy about testing and making sure everything works because when you can just send another update and fix it, why spend all this time testing it to make sure it works in the first place? That's what you should do. But if you don't have to, it's like, oh, if there's a bug, we'll fix it later. It's a poor experience.

**Alvaro And Jen From The Ure:** Okay. Well, think about it this way. If the first thing I do when I start on a project is I make sure I have the capability of OTAing my device, then what I've enabled is I can send product out to a lot of different people internally and have a very limited alpha test. And then they get all the updates as we push them out. And I can get feedback, consistent feedback. And that's what we did. That's great, yeah. That's the first thing I did when I worked at BIA was make sure that we could do OTA because what was happening before is we'd have all these alpha testers and they would just physically send back the device to us. We'd put a new image on it and we'd send it back out to them. And that's really time consuming.

**Alvaro Prieto:** I think that's great. It's just when the customer is the one that's having to update constantly, right? When it's internally in testing, that's the best way to do it. But when you can update everyone's devices after they've bought them and it's easy, people start getting lazy. That's the only thing I'm saying. It's not that.

**Chris Gammell:** Also, I should cut in here. The OTA means over the air, right? Yeah. Over the air update. That's for a wireless device.

**Alvaro Prieto:** Yeah.

**Chris Gammell:** Right. Just like on your phone. You've got to watch out for those.

**Alvaro And Jen From The Ure:** Yeah, because if you look in like the Google Play Store and I'm assuming iTunes, like any other release notes, it never says, hey, new and improved features. Most of the time it just says with bug fixes.

**Alvaro Prieto:** Yeah. Right. Well, there's a good one. Someone said fix a few bugs and introduced a bunch more. Just being honest.

**Alvaro And Jen From The Ure:** The honesty app.

**Chris Gammell:** Nice. So how does this end up playing together then with the hardware? Because obviously you both have your hands-on hardware as well. I mean, most firmware engineers do have that hardware, you know, the need to be near it anyways. So how does that end up playing out? Especially, you know, like you're talking about, these things that can't – obviously hardware cannot be updated in the field. There's no OTA for hardware. Thank God. So how does that end up playing out in terms of consumer versus industrial versus, you know, delivery time, stuff like that?

**Alvaro Prieto:** I think for all of them, one of the things that also happens is the hardware engineers also get lazy because like, oh, we can fix it in firmware. Or that's just – I don't like that. Where we don't have to test it as much. We'll do a patch in firmware and hopefully work around it. I guess. But this is –

**Alvaro And Jen From The Ure:** I mean, I can tell you how I've dealt with it on other projects. And it's primarily that your P0, maybe you have a bunch of different processors or different architectures that you're trying to work through with different concepts. And you just kind of put them on this frankenboard together just to see whether you can answer all the different questions that you have about what the product can and cannot do. And from there, you just basically, you know, trim out all the excess or, you know, based on whatever the feedback is from your testing and go forward. On the other side of it, you know, you have your marketing and product management teams who should be working to narrow down like a bunch of different things. Like, hey, do we want five LEDs? Is three okay? Do we need an accelerometer? Do we need like a rubber ducky on it? Do people care? Who knows? And they should at least be willing to go, hey, if we just have these things, will we be able to – you know, if we want to add this on later, will we be able to do this with the hardware as it stands now? And that's usually when some have – it's kind of a top-down, bottom-up approach where you kind of meet in the middle and go, okay, this will get us to X amount of value later on if we decide to go down that value. So as long as you have like enough – as long as you have enough like features on the hardware that the software can craft into something interesting and compelling, then that's usually enough that the marketing team can then go, okay, we're going to start with this first round of features and then we'll just keep adding and brainstorming more and more and more as they're going through – leading up to launch. And then those that don't quite make it but they still want, they'll just put into sustaining releases. And that's mostly what marketing has been trying to do. And what's interesting is that you want your app to be really cool. You want your IoT device to be really cool out of the box. But then in order to keep people using your watch or your IoT rubber ducky or whatever, you need to keep putting in compelling new features every few months to keep them using it. And so that's a lot of the marketing strategy that they've been using.

**Chris Gammell:** Oh, interesting. Like a magical – like kind of a magical feeling to it like, oh, what can this thing do today? Is that kind of the idea?

**Alvaro And Jen From The Ure:** Yeah, it's – you know, the whole idea is you've got to make it sticky. So they're just going to give you just enough the first time to like make you happy. And then you'll start – it'll wear off and then they'll come up with the next release. And it'll give you something new that's supposed to, you know, renew that sticky factor. Sticky being not physically sticky but want to keep touching it.

**Speaker ?:** You're Pokemon.

**Alvaro And Jen From The Ure:** Yeah, yeah, yeah.

**Chris Gammell:** Dopamine-driven development.

**Alvaro And Jen From The Ure:** So I think that's one of the parts that we don't think about on the hardware side so much is marketing. Like why isn't this feature in here now? It's ready to go. It's because they're trying to hold off to make sure that the product's still compelling. If you kind of drop all your load all at once at the beginning, you know, it wears off fast. I'm going to keep some mystery. Got it.

**Chris Gammell:** So what about dealing with the actual volume piece? So you mentioned the OTA stuff and that I'm sure plays into this as well. But, you know, some of these things that you've discussed are going out into the world in literally millions of volume. So how does that play out with, you know, how that impacts your work? But then also the, you know, do you have access to – are you programming parts that are not commercially available to someone like, you know, some schlub like me? Is it like even custom silicon that's so leading edge that you then have to end up troubleshooting it and stuff like that?

**Alvaro Prieto:** I mean, in the big companies, you usually – you might not get – you will get some custom silicon. But usually it's just the cutting edge silicon. So it's not yet available, but it will be.

**Chris Gammell:** Like early release kind of stuff?

**Alvaro Prieto:** Yeah, early release, especially for the big companies. Or even once you save big numbers, they give you the parts early. And you're dealing with incomplete documentation. The errata is not quite there. There might be silicon bugs. So it's a little bit more of a challenge to get stuff up and running. But that's kind of the price you pay for using it early.

**Alvaro And Jen From The Ure:** I've definitely been on both sides of the table for this part, both being like, hey, here's some new silicon to use. And you're like, hey, how do I – you know, what's wrong with this thing? And I've definitely been on the other side where I'm the salesperson or the FAE involved that had to break the news. Like, hey, so –

**Chris Gammell:** We found something.

**Alvaro And Jen From The Ure:** We found something. It's going to be a six-month lag.

**Chris Gammell:** We found a silicon lump.

**Alvaro And Jen From The Ure:** There's peanut butter all over the silicon.

**Alvaro Prieto:** Sometimes the errata was a customer – you know, a customer would find this bug and then come back to us. And we're like, oh, we better document this, I guess.

**Chris Gammell:** That's really real. You found it. Yeah. You found the golden bug. You win. Working silicon eventually.

**Alvaro Prieto:** Yes. Well, it's usually documented, not working silicon.

**Chris Gammell:** Got it. Got it. Yep, yep, yep. Don't use that spy bus. Use this spy bus.

**Alvaro Prieto:** Yeah, or turn off the spy bus and turn it back on whenever it happens.

**Alvaro And Jen From The Ure:** Have you tried turning it on and off again?

**Alvaro Prieto:** I currently use parts like that.

**Alvaro And Jen From The Ure:** I think there was something in the STMicro recently that I – like about a year ago that had that problem. It would just suddenly just like give up the ghost. And you're like, oh, yeah, just reboot it and you'll be fine. I'm like, what the hell?

**Alvaro Prieto:** Oops. Oops. So when you're dealing with volume, you start dealing with those a lot more. And then also you start – as far as testing, when you test locally, you only have maybe hundreds of units, thousands at most. Once you go into the field, you have millions. If it's a problem that happens, one million, if you have 100 million, this problem is going to start popping up. So as far as firmware, getting crash logs back is super helpful but very rarely available. Possible. Available. But also just with the hardware and testing, just your tolerances on your things, you start seeing weird stuff that happens once in a while. And those things are hard to track down.

**Alvaro And Jen From The Ure:** That's just all money. So half the time when you're evaluating these types of risks, you're looking at the likelihood versus the cost. And then anytime customer service is involved, it's super costly.

**Chris Gammell:** Oh, yeah. Okay. Yep.

**Alvaro Prieto:** Yeah, but you have capacitor cracking that's causing some current leaks or you're having just the microcontroller doing weird stuff. I mean, I'm trying to think of specific examples without – Yeah, without giving it all away. Without giving stuff away.

**Alvaro And Jen From The Ure:** What was going on in Apple that capacitors were cracking? I never said those. Actually, don't answer that.

**Chris Gammell:** Yeah. So what about other – so that's interesting from – like you're saying, like the testing stuff, obviously there's just a lot of units out there. But what about other – dealing with high volume kind of things of – like does that change deployment then? So from a firmware perspective, from a hardware perspective, do you get called when you have lot differences? And so you have – I guess that's kind of the tolerances thing you're talking about.

**Alvaro Prieto:** Well, if there's analog components and you have to do calibration, it's easy to do with a few units. But if you want to scale that, it becomes an issue. Also, just firmware updates, right? Firmware update for 1,000 devices is different from a million devices. If you screw it up, you can't just give everyone a bad firmware update. So you have to do staging, right? You have to give like 0.1% of the units, you know, start seeding the new firmware image. Wait. Okay. They didn't break. Okay. Give it to 1%, 10%. So you have to be a lot more careful with your updates.

**Chris Gammell:** And this is specifically using OTA type over-the-air updates and stuff?

**Alvaro Prieto:** Yeah. So this is remote firmware updates. You have to be really careful. And then there's a whole security aspect too, which is just a whole other podcast. But you don't want someone else to do the firmware update for you. Oh, right.

**Chris Gammell:** Yeah, no, that's a good point. That's a really good point. I mean –

**Alvaro Prieto:** If it's connected.

**Alvaro And Jen From The Ure:** So, you know, you're talking about like, hey, we get some early access to silicon or we get this. But for the most part, a lot of consumer is not very forward-thinking. It's not very R&D-centric at all. It's just repackaging stuff that they're getting from another vendor. And it's really the vendors that are absorbing all that R&D cost for you.

**Alvaro Prieto:** App notes and stuff like that, yeah. Yeah. Yeah. If you look at a lot of consumer routers and stuff, it's just the networking chips reference circuit repackaged. And that also happens with software, which is an issue because people just take the example code, put in the web server, and accept that if you look at the example code, it has all these warnings that say, this is – do not use in production. This does not have security kind of enabled because it makes it more complicated. So it's an example. They want to sell you this device. So it'll make it easier to test. But if you want to do it securely, you've got to go through a lot more hoops. But people just say, oh, it works. Copy and paste the vendor code. It works. And now you have tons and tons of insecure devices out there.

**Alvaro And Jen From The Ure:** It's even worse than that. Maybe you've worked with some vendors that had competent software people that would tell you, hey, warning, you need to do some other stuff. A lot of the stuff that I've gotten from vendors has been – is completely unstable and doesn't work and has its own set of bugs that you need to figure out and work through. And quite frankly, a lot of these schedules for the products are so tight that you may never get to them. You may never even find them before they go onto the field.

**Alvaro Prieto:** And then you turn it off back on.

**Alvaro And Jen From The Ure:** I think that's a lot of the issues that – I was going to say there's a certain mobile chip manufacturer that has a lot of issues, but they've left the mobile game. I think you guys can probably figure that one out. They don't understand things like shared memory coherency.

**Chris Gammell:** Well, I guess they left the game, so that's good. No, that's an interesting picture of the industry, though, too. I mean, so that is kind of the image I had of just the time constraints, stuff like that. I think a lot of people are using reference designs, application notes, things like that in their designs. But what it comes back to is, is it verified? Is it tested? And then how much impact can it have? Because like you're saying, there could be millions of units out in the world.

**Alvaro Prieto:** Well, you say verified and tested. If it works on my desk, it might not work at a different temperature, different humidity, different battery levels. Oh, right. Making – Different salt fog conditions. Yeah, making volume stuff is hard, especially when it's consumer electronics. For industrial equipment, you know – you have a pretty good idea how they're going to use it. But consumers are notoriously good at using things for all sorts of things you never imagined. So –

**Chris Gammell:** Right. Yeah, none of my industrial products have ever been dropped in the toilet. So – and then they get mad at me, right?

**Alvaro Prieto:** Because why would you not make it waterproof? I mean, it's clearly your fault.

**Chris Gammell:** Yeah, of course. Right, right. Of course.

**Alvaro And Jen From The Ure:** I didn't know that I could use the set-top box to open beer, but –

**Chris Gammell:** Wait, you're saying I couldn't go heli-skiing with this? What? Yeah, that is a wide range. So, well, I mean, we're talking about a lot of products are in the field, not a lot of timelines, but tell me about how – how does this stuff get handed off then? So, DVT, PVT, all that stuff, right? So, like, going to, like, from R&D engineering or, you know, just design engineering to a manufacturing facility or a manufacturing setup, what do you have to do in order to get that right?

**Alvaro Prieto:** I mean, I was fortunate enough not to have to do that in most cases. But from what I've observed, I mean, usually, again, you start building small and start growing, right? So, the first builds is going to be the design engineers for the CM. You know, you get your boards. Do they work? That kind of stuff. Once you start scaling, you need to get more Pippo involved because you don't have enough – like, the designers are just a handful. You can't have them in China 24-7 just making sure everything gets built. They do get sent, you know, to the factory to make sure it goes. But then you start training other people to, you know, understand the product and be able to respond to any problems that happen. And until you start ramping up, now you're building thousands. Now you're building 100,000. And it's kind of – it's all in stages, I guess. And, you know, eventually the design team is, you know, you step back. They might start working the next thing. Now, product gets shipped. You start getting field failures. And then those usually go back to the design folks. Or you'll have a team kind of triage for common issues. But then the really tricky ones go back to the design folks.

**Alvaro And Jen From The Ure:** One, it depends on if you're using a contract manufacturer and what exactly they're handling for you. So, you may be starting with your request for proposals from them. And you may have them just handle all of the manufacturing, like, including deciding what the test plan is. And you may have a hand in deciding or signing off on the acceptance criteria. Or they may also be doing the BSP for you for that particular chipset. They may be doing some of the design work for you. These days they –

**Alvaro Prieto:** Board support package.

**Alvaro And Jen From The Ure:** Oh, yeah. Board support package, BSP. They may be doing a lot of stuff for you as a CM. But it also depends on your volumes, what they – if they already kind of have a product in their, you know, in-house that's – already kind of fits the bill for what you want to do. So, it's great if you are just a snazzy biz dev guy who just wants to – who doesn't have any engineers and you just want them to go off and build it for you. They can handle everything for you. If you have engineers and you want to do something that doesn't quite fit the bill for what they already have, then it's – it falls a lot more in line with what you're talking about, Alvaro.

**Alvaro Prieto:** Isn't that what Dave's doing for his new meter? Just having people build it?

**Chris Gammell:** Yeah, in Korea, yeah, they're an existing DMM manufacturer that are doing custom design for him that he did. So, yep.

**Alvaro Prieto:** Yeah. So, I mean, there's – you can do everything from hands off to all hands on deck.

**Chris Gammell:** Got it. And so, there's no rhyme or reason across products you guys have worked on.

**Alvaro Prieto:** I think when you're big enough, you know, you have all the resources and expertise to do it yourself. But when you're starting out, it's, you know, better – I think it's better to let the experts do it kind of thing, right? Some people try to do it themselves. I mean, you've had – I remember Salia, right? They brought in manufacturing in-house. But it was a bit too much initially, and then they had to go back to CM. So, it really depends on the product and what's required.

**Chris Gammell:** Has it been mostly China for the work? I mean, that's, I guess, another common thing with consumers thinking, well, you know, I always get frustrated when the – when, you know, you listen to, like, startup talks about hardware stuff. And they're like, well, of course you're going to go to China. And it's like, well, no, not necessarily. But if you're a consumer, then, yeah, you probably are going to, right?

**Alvaro Prieto:** So, half of mine hasn't been because, like, medical devices, usually you're close by. Satellites we did in the basement. In the basement. Well, not in the basement. On the first floor in San Francisco. Oh, yeah, you should have seen it.

**Alvaro And Jen From The Ure:** Wow.

**Alvaro Prieto:** Yeah. And – You can hear people's footsteps above you and, like, dust falls.

**Alvaro And Jen From The Ure:** What kind of rickety halt-and-catch-fire place were you working at?

**Alvaro Prieto:** Well, it was just planet office. But eventually, you know, they installed a clean room and everything. But right after I started, we had kind of pieces of plastic on the ceiling so that the dust from people walking above wouldn't, you know, get the satellites there.

**Chris Gammell:** Right. Well, I guess satellites are ITAR-controlled anyways, right? So, that's – Yeah. Yeah, that's a different thing. What about you, Jen?

**Alvaro And Jen From The Ure:** So, when I started doing manufacturing in the mumble-mumble 90s, it was actually – it was actually up in Fremont, California. And there still are lots of manufacturing houses in Fremont, California. I even worked for one of them very briefly. So, all those little – you know, when you're up in SF, they have those little dots that can tell whether a parking space is open or not? They used to manufacture all of those. And I think that manufacturing house is still around. But during that time period, consumer electronics were enormous, physically enormous. But with the miniaturization, the requirement is – you know, the skill required hasn't really caught up with the places here. So, they can handle small volumes out here. They can't handle extraordinarily large volumes. You could go to Mexico. I think Ensenada is like one big manufacturing hub. Yeah, they used to be pretty big. Or you can go to China. Yeah, the other thing that you – yeah, the other place that you need to evaluate – or not place, but the other thing that you need to evaluate is what are you trying to achieve? Different manufacturing houses have different capabilities. And, you know, obviously you have Flex and Foxconn as being the most visible ones worldwide. But they each have their own specialties. And it's not always obvious to most people when they're trying to find somebody, especially if it's the first time they're manufacturing something, that – how to navigate and find the right CM for what they're trying to do. For startups in particular, there's a number of smaller manufacturing houses that will kind of give you an internship, I don't know, like a prize. And they'll invest in what they think are promising startups. And they will give you kind of free work. They will work on your project for X number of iterations to kind of, you know, help and invest. But they're also kind of looking at it from their angle, like, hey, if this takes off, we can, you know, really make a lot of money here.

**Alvaro Prieto:** There's also the volume factor, right? In China, they make the components for the thing you're building right next to the thing you're building or, you know, nearby. So if you have to scale and you have to build, you know, a few million more this week, you couldn't do that in the U.S. You can't just go to DigiKey and overnight, you know, 10 million whatever components. But if you're near the factory of those, you could just drive down the road and get them kind of thing. Or they'll ramp it up. That's one case, right?

**Alvaro And Jen From The Ure:** I would say generally speaking, that's true. I think you've had, like, Bunny and some other people talk about the nuance there, which is, yes, they can have quick access to other people. That doesn't mean that those other people are bringing quality. It also may mean that there's some additional cost to get it there in a certain time. So just getting something from Hong Kong back into China is its own particular pain.

**Chris Gammell:** Well, you were both talking about firmware delivery to different devices and stuff like that. And if you start varying, you know, product, you know, from one run to the next, it's going to, you know, you're going to have other issues that you have to track and stuff like that.

**Alvaro And Jen From The Ure:** Yeah, there's very clear incremental changes you're trying to do build to build. Early on, it's really focusing on being able to validate the design, the engineering design. And then it moves more towards validating the process of building the product itself. And then sometimes, actually, more often than not, I'm noticing it kind of gets all smooshed together. So you're kind of doing two things at once, whether you should be or not.

**Chris Gammell:** I want to ask one more thing about kind of the volume manufacturing stuff. And then I'd like to touch on a little bit more reverse engineering. But so I've seen some of Alvaro's stuff out in the wild. I own one of the Amazon Fireboxes that Jen mentioned. Obviously, you've both seen, you know, successes and failures. What is, so I guess that's another thing that I don't, no one has ever talked about the product that I've worked on in the past. You know what I mean? Maybe, maybe Dave has talked about test equipment that I've helped on, but that doesn't really count. So what is that like then?

**Alvaro Prieto:** I mean, that's pretty, I mean, I worked on very, very early prototypes for some of the Apple stuff that I've seen out there. And it's cool now that it exists. I can tell people like, ooh, I worked on that, you know. And it's, I don't know, it feels better. Working on stuff in secret is, that's rough. Because, well, for me, I'm a total nerd. I love telling people about the stuff I make because I love, I love making it, right? So, so once I'm able to say, hey, you know, I worked on that. It really, I don't want to say validates, but, but it encouraged me to do more.

**Chris Gammell:** And Jen, what about you? Because you have, you have that comparison specifically for the Amazon phone, which didn't really hit the mark. And then the Amazon Fire, which I think, or the Fire TV stuff, I think is, I mean, that's one of my favorite devices.

**Alvaro And Jen From The Ure:** Actually, I really like the Fire TV. So I think the thing is like when I was working on more industrial or networking equipment or call center equipment, it was difficult for people to, to, to understand what exactly I do. I'm like, I just, I make the hardware go. I make the lights blink and they, it still doesn't, it doesn't sound very impressive at all.

**Chris Gammell:** Doesn't, doesn't register with them.

**Alvaro And Jen From The Ure:** It doesn't register. It doesn't resonate with them at all. But being able to go like, hey, you know, I work, you know, point, you know, walk into someone's house and go, oh yeah, I worked on that. You know, every time the, the picture scales to the right resolution, that's me. Or the fact that you can talk into your microphone on the, the Fire TV remote, um, and it records your voice. Um, I, you know, I can talk about that and that's really cool that people just can really understand like, oh, you did that.

**Chris Gammell:** Yeah.

**Alvaro And Jen From The Ure:** It just makes me seem like, oh, I'm not just some dorky engineer. I mean, I know I'm a dorky engineer, but it, but it, it means that people kind of can understand what I'm doing.

**Chris Gammell:** Right.

**Alvaro And Jen From The Ure:** But it's a lot of work to get people to see it though. That's the problem. Yep.

**Chris Gammell:** Right. Yeah. It's a different set of challenges, stuff like that.

**Alvaro Prieto:** Explaining firmware to people is hard.

**Chris Gammell:** Well, I mean, I don't, I mean, I, I tell people that I work on electronics. I'm not, I'm not like, well, if you look at resistor one here, um, you know, it's not like.

**Alvaro Prieto:** I did that. Well, I tell people I write firmware.

**Chris Gammell:** Yeah.

**Alvaro Prieto:** And they're like, what's firmware? It's like, oh, it's like a software for microcontrollers. What's a microcontroller?

**Chris Gammell:** No, no, that's, I would never, why would you ever dive that deep? Like just treat everyone like you're talking to your grandmother. No way, man. Ah. They ask because they're confused, not because they care. No offense. I mean, I care. Uh, but like. Some people care, Chris. Some people care, but they're, they're the people that already know what you do. You know what I mean? Like, I don't know.

**Alvaro Prieto:** They might care, but they don't know yet.

**Chris Gammell:** If you go to a cocktail party, if you go to a cocktail party and they're like, what's a microcontroller? If you went to a cocktail party and someone asked what's a microcontroller, they'd just be nice.

**Alvaro And Jen From The Ure:** Chris, you're going to the wrong cocktail parties. I don't know why you didn't move out here. Yeah. I don't know why you stayed in Chicago.

**Chris Gammell:** I actually had to give this speech yesterday. Well, that's actually, okay. So I did think of another question too. So interestingly, so Jen, you mentioned a lot of companies. Alvaro mentioned a couple of companies as well. So then what's the job market like for in consumer? I mean, obviously you do have to live in the Bay Area. Well, that helps if you want to have a lot of opportunities. You don't have to. It helps.

**Alvaro Prieto:** But it certainly helps. I mean, there's lots of jobs here right now.

**Chris Gammell:** So the hoppability, you know, that word I just made up, the hoppability between jobs. I mean, is it like the software craziness where people are, recruiters are calling and, you know, ringing your phone off the hook? What's that like?

**Alvaro Prieto:** Most of the firmware engineers I know are happy or they're working somewhere, so they're not actively looking. And the recruiters, at least where I have worked, are always desperate for firmware engineers. So I don't think there's enough.

**Alvaro And Jen From The Ure:** Like, I'm interviewing firmware engineers like crazy. And I'll be honest with you, it's hard to find a competent, I don't mean like incredible. I mean competent, solid firmware engineer. And when we can bring somebody in, it's disappointing. It's super disappointing. So that said, if you want to move jobs in Silicon Valley as a firmware engineer, you have a really good opportunity to like just find any number of different jobs because people are so desperate that, you know, you don't have to be an incredible algorithm developer. You don't have to be able to do DSP work. You just need to be able to write string copy.

**Alvaro Prieto:** Well, and a lot of times, you know, you go through not the software engineer interview, but more of a hardware engineer interview, which in Silicon Valley tends to be a little bit more forgiving. Yes. They're pretty vicious with the software engineering interviews here.

**Chris Gammell:** Oh, you just mean in comparison. I thought you meant like compared to elsewhere in the world. So you're saying...

**Alvaro Prieto:** No, no, just in Silicon Valley, the software is even more competitive. They were like, there's tons of candidates, so they really have to filter them out to get the good ones. Got it. So they really pull no punches in those interviews.

**Chris Gammell:** Right. And so it's more like, oh, you know what components are. You've programmed a microcontroller. Welcome to the table at least, right? Yeah, we'll talk to you. Yeah. Okay. No, that's good. I mean, that's good for people to know.

**Alvaro And Jen From The Ure:** Are you saying that I should just become a hardware engineer?

**Alvaro Prieto:** I'm technically a hardware engineer in my current position, but I write firmware. So I started doing PCBs now. That's very interesting. I'm just saying there's other ways.

**Alvaro And Jen From The Ure:** And I've also done PCBs for PC104. Nice.

**Chris Gammell:** What software were you using back then? I was going to say, it probably wasn't KiCad, huh? PC104 was not congruent with KiCad.

**Alvaro And Jen From The Ure:** It was standard ORCAD.

**Alvaro Prieto:** No, they're still using that.

**Alvaro And Jen From The Ure:** Ask me about mouse controls or mouse gestures. Oh, man.

**Alvaro Prieto:** I've heard bad things.

**Alvaro And Jen From The Ure:** Ask me about mouse gestures and mentor graphics.

**Chris Gammell:** Wait, is that the one where you do like an M, a Z? Is that like a Z to zoom? Is that the one?

**Alvaro And Jen From The Ure:** No, you don't do that. You just like do a slash down, slash down. And you zoom in and you go the opposite way, slash up. And then you zoom back.

**Alvaro Prieto:** While you're pressing a key or?

**Alvaro And Jen From The Ure:** I don't think you, no, the button. While you press the mouse button. Well, that's not bad. And then undo is like the, you do a little counterclockwise circle. Shake your computer. I feel like I'm interviewing for a job right now. And all I got for you is I don't know anything about resistors. I knew mouse gestures.

**Chris Gammell:** Well, let's interview based on y'all's interviewing. Amazing. So, so on the unnamed reverse engineering podcast, you know, what, what are the people you've talked to so far? Who's coming up? And then what, what have you learned about reverse engineering so far?

**Alvaro Prieto:** I mean, so we've talked, uh, two episodes has just been us, uh, talking to each other, which I wouldn't recommend. And then there's, there's a lot of giggle.

**Chris Gammell:** You wouldn't recommend talking to one another or you wouldn't recommend listening to those shows?

**Alvaro And Jen From The Ure:** The alternate name for those episodes is GiggleCast, I think.

**Alvaro Prieto:** The first one was for sure. Uh, but the, the, the, we, we talked to, uh, Dimitri Greenberg, which you might know of as the guy who ran Linux on an AVR biker controller. Good Lord.

**Chris Gammell:** Okay.

**Alvaro Prieto:** Um, yeah, that guy. Uh, and he, he's an awesome reverse engineer. Yeah. Really fun. Uh, just, I learned a lot just listening to him and then, uh, you know, ScanLime, Micah, Micah, Elizabeth Scott, uh, you've probably seen, seen some of her stuff on online. Yeah. Uh, that was a ton of fun. And, and again, especially because she was kind of the recent Jen and I started, you know, talking about the podcast. We saw her videos and said, Hey, we should do something like that. Um, and now we're using the podcast just like you guys and everyone else to talk to cool people and learn more about it. Oh yeah. Yeah.

**Alvaro Prieto:** I'm not, I'm not an expert in reverse engineering, but I find it incredibly interesting and useful. So if we're able to, to use this as a way of getting people to, to tell us all sorts of cool stuff, their projects and that kind of stuff, I'll take it.

**Chris Gammell:** So what about other projects that you both have on the, on the horizon then that you're, you're hoping to, to reverse engineer? I mean, I, I know Micah does a bunch of, uh, uh, what was like opcode stuff on the, on the winch bot. Right. It was like checking out.

**Alvaro Prieto:** Yeah. Yeah.

**Alvaro Prieto:** That she had the controller on the, on the pan tilt or the gimbal controller, I guess she had to reverse engineer the firmware for that. So she could make it do whatever she wanted.

**Chris Gammell:** She wanted, so what are you both doing?

**Alvaro Prieto:** I mean, are you, are you using this in your everyday jobs or are you guys trying to, I have used it in my jobs before, uh, where, uh, we're trying to integrate some, uh, a device with a battery. And when you put a generic battery, it would, it wouldn't work. So, so the, the, the, the fancy batteries had a, um, like a little serial protocol that would authenticate. And so, so, you know, do a bunch of date captures and try to emulate it. Or another time, uh, we had a battery tester that was just some, uh, I don't know if it's generic, but some Chinese, uh, battery tester, uh, for, you know, 186 fifties for, for lithium batteries. And it would just discharge them and charge them, discharge them and charge them and tell you the capacity of them. And this thing would spit out either some binary file or a horrible, horribly formatted Excel file. And I needed more than that. So I, I opened, I opened up their binary file on, uh, on a hex editor and I started looking for patterns. And then I eventually wrote a Python, uh, decoder for their binary files to be able to export it to whatever I needed to be able to, uh, kind of log, log data and, and do stuff with it. So that was a fun little reverse engineering project for work. This is mostly just when you have tools, you don't understand.

**Alvaro And Jen From The Ure:** Just so I'm clear, you, you said you, the, the, the fancy battery you were using basically had some IP protection on it. So it like, was the K cup of batteries.

**Alvaro Prieto:** It was something that, um, that, yeah, the, the, the battery's fancy enough that it had some sort of protection and we needed to power it constantly. This was just for a test project. And so, so if you just connect power to it, it's like, oh, I don't, I don't know what this battery is. And it still worked, but it would put up this display saying, oh, I don't know what this battery is. And we try to remotely operate something. It doesn't quite work when, when there's a dialogue waiting for you to click on it. Right. Yep. So it was mostly an inconvenience thing. We ended up figuring another way around it, but.

**Chris Gammell:** And Jen, what are you doing right now? Are you, have you used this in the past or?

**Alvaro And Jen From The Ure:** What is, um, so it turns out every year I have a birthday and I came upon a birthday card that I had received and it amused me greatly. And it basically, you open it up and the lights come on and then you blow out the lights, quote unquote, and then it plays happy birthday to you. So I want to reverse engineer that greeting card. So, um, I don't know if anyone's seen on my Twitter feed, I've been asking about how to remove this darn epoxy. And I think I may have, yes, there have been offers of acids. John McMaster. And videos traded.

**Alvaro Prieto:** No, John McMaster, who runs the reverse engineering meetup in Mountain View, he, he, he's the ICD capping king of the Bay Area. He has icy pictures, siliconprong.com or .org is his website.

**Alvaro And Jen From The Ure:** And x-rays and yeah.

**Alvaro Prieto:** Yeah. You want to stay away from wherever he's doing it.

**Chris Gammell:** Well, that's like we had, uh, we had Ken on a while ago, two shows ago as well. So he's, he's thinking of that stuff. Yeah.

**Alvaro Prieto:** So, so we've been talking to him as well. Um, cause yeah, he does some fantastic reverse engineering and he's given talks at the, at the meetup, the local meetup.

**Chris Gammell:** Oh, cool. Okay. What is this meetup? So it's a reverse engineering meetup in the Bay Area?

**Alvaro Prieto:** So it's called the Mountain View reverse engineering meetup and they meet once a month. Okay. And like in the back of a barbecue joint.

**Alvaro And Jen From The Ure:** In the Dickies barbecue shack.

**Alvaro Prieto:** It's sketchy, but it's great. Um, no, but something, some great talks happened. They're not recorded. Um, so people are a little more willing to say stuff. Let's just say that you're like, Whoa, what? And, and some really cool, cool stuff they talk about. So, um, yeah, it's, it's a cool resource for people in the Bay Area.

**Chris Gammell:** Well, so it sounds like some of the, uh, the, so, so if I was going to list out some of these things, like, like you're talking about the firmware dumps, that seems like that's a big skill that you need to have. Being able to read the hex files, stuff like that. Uh, knowing like what Joe Grand does, like JTAGulator, you know, finding the JTAG ports and being able to reprogram things. That's a big piece. Are there other skills in there that kind of cross over into the hacking world or what, what else is in there?

**Alvaro Prieto:** I mean, uh, a lot of the skills to use in reverse engineering are also very useful for debugging. Okay. Oh, interesting. Your own product, right? Because, you know, you're trying to see how it works. Uh, you're probing around, you're looking, um, just how stuff is working. And I might be working my own product and stuff's failing, but I might look at it and be like, oh, I remember this time I was doing something like that and go do that. Also, you get to learn from other engineers' work. You might be opening a really fancy piece of equipment that, uh, someone made a long time ago and clearly spend a lot of time designing it. And you get to look at it and kind of take it all in and say, whoa, I never thought of doing stuff this way. Um, or this is really elegant design or, well, this is horrible. How does it even work? Right. So it's just kind of a way to learn as well.

**Speaker ?:** Yeah.

**Chris Gammell:** A physical bug. Why, oh, why, oh, why, oh, why, oh, why?

**Alvaro And Jen From The Ure:** I don't know if there's a physical bug. How old is the electronics that you're opening?

**Alvaro Prieto:** Oh, no, I have gotten some old stuff, but that was just.

**Chris Gammell:** Yeah, I mean, this sounds like, I mean, that's also what Dave, Dave does with the teardowns, stuff like that. People that are doing teardowns. Exactly. Understanding how it all gets put together.

**Alvaro Prieto:** It's just, uh, the teardowns are mostly hardware. We, well, I mean, Ken's reverse engineering hardware stuff. Um, I, I, I'll focus on the firmware. So the Prodox, the quadcopters I did a while back, that, that was just for fun. Like I really had no need to reverse engineer this $30 quadcopter, but I, I saw Skain Lime's video. Um, and I, I wanted to do something of my own in that similar fashion just to teach myself to prove that I could do it. And, uh, I just reverse engineer the radio protocol. So instead of trying to dump the firmware in this case, I tapped the communications between the microcontroller and the radio chip. And just looked at that and then connected my own microcontroller to the radio chip and was able to do it that way. Um, and that just taught me about how this radio works, you know, how, how their, the controller works and all that stuff. So it was fun. Cool.

**Chris Gammell:** That's great.

**Alvaro And Jen From The Ure:** And no one died.

**Chris Gammell:** Right. Yes. This also kind of sounds like, like some of these skills are like the, uh, the stuff that I was blown away with. If people didn't listen to the, the, uh, interview we did with Zach from Zachtronics, um, like the Shenzhen IO game. Like that seems like that's a lot. Like he, his games are also a lot of, a lot of, uh, reverse engineering and, you know, like challenges.

**Alvaro Prieto:** Yeah.

**Chris Gammell:** And I was just incredulous that whole show. I don't understand why he made those. I still don't understand it, but it sounds like that's a good practice. I don't know if either of you have played those.

**Alvaro Prieto:** People like puzzles. I mean, I have a lot of friends who put, drop a puzzle in front of them and it's, you know, they call it nerd sniping, right? They have to solve it. They can't not know it. And that's what a lot of the great reverse engineers do. I mean, they, we interviewed Dimitri.

**Alvaro And Jen From The Ure:** They just keep going. And the only reason. They just keep going.

**Alvaro Prieto:** Well, the only reason he reverse engineered the PSOC was because the data sheet said that the user could not read part of memory. And that's just challenge accepted for him. And, and just because they told him he couldn't do it, he just wanted to prove that he could. And that's as much as little, as little as it takes sometimes.

**Alvaro And Jen From The Ure:** And that's why he also did the, uh, the Dreamcast VRMs. I'm sorry. VMUs.

**Alvaro Prieto:** Yeah. Yeah. Because, you know, can't be done. So like, oh, really? Right. Hold my beer. Hold my beer.

**Alvaro And Jen From The Ure:** I didn't seem like a beer drinker, but yeah, sure.

**Chris Gammell:** It's a turn of phrase. Yeah. Well, that's great. So I'm, well, I'm looking forward to, you know, listen to more of these shows. Uh, where can, where can people find this podcast?

**Alvaro Prieto:** Unnamedre.com? Yes. I think. I don't know. Yes.

**Alvaro And Jen From The Ure:** Not HTTPS.

**Alvaro Prieto:** Yeah. So it's, it's U-N-N-A-M-E-D-R-E.com. Until we find a name. And then you can also on your podcast app, just search for Unnamed Reverse Engineering Podcast. Um, we'll have four episodes. Yeah. We should record some more. Yeah. Um, I'm in the process of moving again.

**Chris Gammell:** So where can people, where can people find you, you both online?

**Alvaro Prieto:** Um, I'm on, uh, my websites, uh, alvarop.com, A-L-V-A-R-O-P.com. And on Twitter, I'm just, uh, my first name and last name, Alvaro Prieto, at Alvaro Prieto.

**Alvaro And Jen From The Ure:** I'm RebelBotJen on Twitter. And you can find me at RebelBot.com. And that's pretty much all, the only places I think you can find me. Unless you find me on the street.

**Chris Gammell:** Okay.

**Alvaro Prieto:** But then they won't know.

**Chris Gammell:** Right. Exactly. Who, who is this mysterious person that's ranting about firmware to me?

**Alvaro Prieto:** Chris doesn't have his Google Glass anymore. Oh, yeah. Yeah.

**Alvaro And Jen From The Ure:** They give me, they give me a dollar. Tell me, go away.

**Alvaro Prieto:** I remember the first time I met, I don't know if it's the first time I met Jen, but, but you had, uh, you had a little 3D printed, uh, uh, camera cover for, for Chris. That's right.

**Chris Gammell:** Yeah.

**Alvaro Prieto:** At the 10D meetup?

**Alvaro And Jen From The Ure:** Yes, I did.

**Chris Gammell:** I still have that.

**Alvaro Prieto:** I was that person.

**Chris Gammell:** Still with the Google Glass. Yep. Yep. It's sitting next to me, underused.

**Alvaro And Jen From The Ure:** Oh.

**Alvaro Prieto:** Oh, they didn't take it away?

**Chris Gammell:** Didn't take what away?

**Alvaro Prieto:** The Google Glass?

**Chris Gammell:** Why would they take it away?

**Alvaro And Jen From The Ure:** They have to find you to take it away, man. I don't know.

**Chris Gammell:** Uh.

**Alvaro And Jen From The Ure:** So, I guess, uh, I guess what he's trying to tell you, Chris, is that someone was supposed to come in the dead of the night and, like, take it away from you. I don't know. Without you knowing. I don't.

**Chris Gammell:** I don't think so. If there's a buyback program, I'm happy. You're happy to sell it? I'm happy to sell it. I'll, you know, I'll take an enterprise version. I don't care. So.

**Alvaro Prieto:** Wait, you're not using it right now. I know.

**Chris Gammell:** Exactly. I mostly just use it at home. It's just a, it's just a casual, you know, just my home, my home, uh, automation thing.

**Alvaro Prieto:** To tell you what's next on your calendar. Right.

**Chris Gammell:** Well, uh, thank you to you both for, uh, being on the show today. I'm looking forward to hearing more about reverse engineering and, uh, I'm, I appreciate the, uh, you know, hearing about commercial electronics in general. I thought it was really, really cool.

**Alvaro Prieto:** Thanks for having us. Thank you.

**Chris Gammell:** Talk to you soon. All right.

**Alvaro Prieto:** Thanks a lot. We'll be right back.
