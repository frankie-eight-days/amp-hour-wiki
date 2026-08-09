---
episode: 493
title: PITA Package
url: https://theamphour.com/493-pita-package/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released May 17, 2020. Episode 493. PETA Package.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. Who's coughing and spluttering, not because of something else, no. Well, the coughing is probably because I can't get water out of my tap right now because there's a fire. There's electrical fire near my building in downtown Chicago. And they shut everything off. The power's still on and the internet's on. So that's good.

**Dave Jones:** Otherwise, yeah, this show could cut out, right? It could. Yeah, maybe. They could decide, oh, look, we have to fix this thing. We're going to have to shut the power off to all of Chicago or something.

**Chris Gammell:** Probably not all of Chicago. No. It was like a... It's a couple of grids. They called it like a vault, like a power vault. I'm actually not sure what it is. Probably like you'd guess it was like storage for something of like the power company.

**Dave Jones:** Well, I would guess it's some sort of underground substation thing. Some sort of maybe. Something like that.

**Chris Gammell:** Yeah, I mean, and there is like a substation right near it as well. There's an actual substation, but it's up the line a little bit. So because it's all near like the train lines and stuff. Yeah. But I guess they're diesel.

**Dave Jones:** To produce that sort of smoke, I'd say it's like big copper enamel wiring from transformers or something like that. Yeah. Because that stuff really, you know, that stuff really smokes when you get it going.

**Chris Gammell:** Yeah, exactly. Exactly.

**Dave Jones:** So yeah, something like that. So I don't think it's like equipment racks or anything like that. I think it's, you know, more probably coppers on fire, you know. Copper and iron. Whatever it is, it's underground and it's fire.

**Chris Gammell:** And those two things do not mix in my mind. So I won't be going anywhere near it. But I'm safe. So yeah, we're good to record at least.

**Dave Jones:** Excellent. All right. Fire. Yeah.

**Chris Gammell:** Yeah. Speaking of things that are fire. Yes. You know, as the kids say these days.

**Dave Jones:** Where's this going?

**Chris Gammell:** I started making videos again, Dave.

**Dave Jones:** Whoa. For your contextual electronics?

**Chris Gammell:** Yeah. I got a new course-ish kind of thing. It's like a follow along. New course-ish. Right.

**Dave Jones:** Is this like a live thing again where people follow like daily or are these batch, you know, you're doing them in and then you're going to release them as a whole course?

**Chris Gammell:** No, this is a daily. Yeah. So it's like making one a day, one every weekday. So yeah, making a new board. It's going to be a more advanced kind of thing. It's a Bluetooth, cellular, a bunch of digital stuff, some power. So basically making like a development platform like I talked about on the show before. I actually mentioned it last week on the consultant show, but decided to record some of it and put it up on the site. So yeah, we'll see how that goes. I'll probably put some stuff like outside of the, you know, the actual course at some point. But right now it's all background info. But because of that, I actually have, I actually got a evaluation board from QuickTel, which I found out is pronounced QuickTel and not Quectel. Q-U-E-C-T-E-L. And yeah, it's pretty cool. It's a little EG91, which is like a cellular module. It can do Cat1. So like 10 megabits per second and stuff like that. So yeah, trying that out, seeing how it goes.

**Dave Jones:** Oh yeah, that's a weird, weird sounded name. It's a company name, isn't it? QuickTel.

**Chris Gammell:** Yeah, I'm sure it's something with Chinese characters that I don't understand, you know. Right. So they're based out of Shanghai. They just went public last year. Oh, okay.

**Dave Jones:** Right. Yeah. Okay. Well, the good thing about that is that you can get the domain name for it. You know, it's not taken. That's right. Yeah. Choosing one of these oddball names that doesn't really, yeah.

**Chris Gammell:** What's crazy about it here, actually, I sent you a photo. The dev board is interesting because, you know, it's a pretty standard dev board. They do a couple of interesting things like for grounding. They obviously shield all the cellular components and stuff like that. So there's like a module that already has a shield built onto it. But then they actually put a shield underneath it as well. And then they have like this huge landing pad for actually for connecting the ground of this plugin module and the board ground because you obviously want a really big ground for antennas and stuff like that for like a reference plane.

**Dave Jones:** Oh, I think I see it. It's like a huge copper pad, right?

**Chris Gammell:** Yeah, exactly. Exactly. Yeah. Yeah. And so that was one thing that was interesting about it. Another thing that's interesting here, I'll send you a link in the Zencaster chat. But another thing that's interesting is the fact I'm not sure if it's interesting or what is this? But so they use DB9 for serial, which is not unusual. But like these days you'd think, you know, it's just then they just send a DB9 to USB cable with it. And it's like, is that cheaper than sending just another USB? Or maybe it's because they want to like make it very clear that it's a debug or, you know, a serial communication port?

**Dave Jones:** Yeah. Because a lot of, and a lot of people love their D9, you know, they're familiar with it. They've got their favorite tool. Yeah, I guess so. Yeah, I guess so. Dude, what, what universe are you living in there?

**Chris Gammell:** At the end of the day, you're plugging, you're plugging USB cable into your computer. So like, yeah, I guess you're saying because people want to use their own DB9 to serial to maybe to USB kind of thing. Yes.

**Dave Jones:** They've already got their own favorite solution for debugging serial. And it's like, and it might've been an old school designer as well. Like a modern school designer, just whack straight into USB, you know, what is this UART rubbish for, you know? And no, no, D9. Yes. Thumbs up.

**Chris Gammell:** I would put pins for the, for the, you know, you could always hook into it, but like. No, no, no. I was wondering if it was awesome because maybe it was like cheaper, you know, maybe like there's enough infrastructure that was cheaper, but it sounds like it's actually maybe not cheaper. It's just more of a preference kind of thing.

**Dave Jones:** It's more of a preference thing. Yeah. I like, obviously a D9 is not cheaper than a pin header, of course.

**Chris Gammell:** Yeah.

**Dave Jones:** Or like a, like a, you know, five way pin header or whatever, but it's, it's the universal standard. It always has been since before you were born.

**Chris Gammell:** I'm sure it was, but I just, I don't usually see it on, I don't see it on dev boards normally. That's what I'm really getting at, I guess.

**Dave Jones:** Always in your lab, always have an old PC with a D9 serial connector on it.

**Chris Gammell:** Very handy. I guess so. Yeah. Yep. That's the reason, that's the, that's the whole reason you do dumpster diving, I do.

**Dave Jones:** Right. Yeah. Yeah. I love, I pull out an old one, especially like a combo mod that's got like modern USB three in it, but it still has a D9 on the back because they're, they're still used in the PC world for like a, a server interface, you know, debugging connection.

**Chris Gammell:** Oh, really? Interesting.

**Dave Jones:** Please correct me if I'm wrong, but I still believe there are a server, you know, modern server, brand new server computers that'll have a D9 on them. Interesting. Yeah.

**Chris Gammell:** Yeah. I've seen pins. So like not all of the cases have a D9 or DB9 connector on the back. Right. So sometimes they'll have pins so you could hook it in, but it's just doing the same thing. Right.

**Dave Jones:** Yeah. Yeah, exactly. But usually if a D9 implies that it's actually an RS-232 interface, so you've got to have the UI, you've got to have the RS-232 level converter chip in there. So you've got to have like a max 232 or some sort of equivalent chip in there to do it. So it's definitely more cost. I mean, you could use the D9 as like a TTL output, but then that defeats the whole purpose. You might as well just have a pinheader because when you see a D9, it implies, aha, RS-232 signal levels. This is not TTL. Right. This is RS-232. So, yeah.

**Chris Gammell:** That's a good point. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** Very different signal in levels. Yeah. Yeah. Right. And I guess it's not, I don't know if this is an isolated one either because those come in isolated, right? Like they can get, they get isolated, some of the 232s.

**Dave Jones:** You can get isolated versions. Well, yeah, you've got a, well, do they have isolated directly on chip?

**Chris Gammell:** I'm looking at the, the converter chip now that you point that out and it is pretty, pretty wide body, but I don't know if it's wide enough to be isolated. Oh, I don't think it's isolated.

**Dave Jones:** It's probably just a max 232 or equivalent. It should have 232 in the part number somewhere. I would be guessing.

**Chris Gammell:** My old eyes, Dave, they're not, they're not. Yep. They're not.

**Dave Jones:** Yeah. They don't. Yeah.

**Chris Gammell:** Join the club. Got to get the old cell phone light out here. You know?

**Dave Jones:** Yep. The old Mark one eyeball just doesn't do it anymore. Huh?

**Chris Gammell:** That's right. That's right.

**Dave Jones:** Yep. I've got a Mark two eyeball. I've got my glasses now. So yeah.

**Chris Gammell:** You have glasses? Is this new? No, you've had glasses.

**Dave Jones:** I've had glasses for years now. Okay. It's, I use it in most of my videos now.

**Chris Gammell:** Oh yeah. I guess when you're like streaming and stuff like that, right? Yeah. Oh yeah. Yeah.

**Dave Jones:** Or if I'm doing a, you know, a video talking head screen capture thing. Yeah. I'm usually using my glasses to read the monitor. I don't need them, but my optometrist says I wear them. Wear them. So yeah, I wear them for looking at monitors now and everything else. Yeah.

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** So yes, it'll be less straight. Otherwise my eyes strain too much and that'll just make them worse. And, you know, they'll deteriorate quicker or whatever. I don't know.

**Chris Gammell:** Time marches on, Dave. Time marches on.

**Dave Jones:** Exactly.

**Chris Gammell:** And the cat's in the cradle with the silver spoon. Oh boy.

**Dave Jones:** Yep. Yep. Sad. All right. What have we got for today's show?

**Chris Gammell:** You did a stream or not a stream. You did a talking head video and you've been playing with the Padauk three cent micro contribution.

**Dave Jones:** Yes. I'm back to the Padauk three cent micro. And remind me of a segue. We can probably do a chip of the week segue with that.

**Chris Gammell:** Okay. Cool. Cool. Yeah. So that first video is you making the actual programmer, right? Or looking at all the parts you'd already made.

**Dave Jones:** I've had these parts forever and I've been meaning to assemble it. And I thought I was originally going to do like a live stream of just me assembling the board.

**Chris Gammell:** You like, like a live thing.

**Dave Jones:** Just assembling the board and then just do one video of like, oh, here's using this new thing. And I thought, no, I thought maybe there's need for a sort of like a multi-part tutorial out there of how to take any GitHub project, really any GitHub hardware project. So if you go, oh, I want that widget, but nobody sells it, right? Nobody sells the kit. Nobody sells a made up one or whatever. And I need that little widget. How do you take, how do you go into the GitHub, take the PCB and schematic and the bomb and everything and actually get it manufactured and then test it and install all the drivers? And it's, yeah. And of course it turned out I was right. So I thought, oh, maybe this will make a multi-part tutorial because things will go wrong and you learn when things go wrong. You know, oh, look, I installed this driver and it didn't work. Okay. Why? Let's troubleshoot it. And there were lots of stuff like that. So yeah. So it turned into a five-part video series of like each one's like half an hour or something like that. So, you know, but that's the amount of effort that is required to get something like this, you know, built and up and running if you aren't familiar with it. So it's basically you, you sitting beside me actually doing this thing, you know, actually getting it all up and working.

**Chris Gammell:** So where did you get this idea from? Some kind of like project-based education, Dave. It's so innovative.

**Dave Jones:** So innovative. I've been doing it for years.

**Chris Gammell:** I think there's a, it's a, it's a different experience, right? Of like, it's a slower kind of thing. People have to be patient through it and you don't get as much of like the, you don't, you don't get much of the summary.

**Dave Jones:** No. And I expect the views to be low. It's not like a great Scott, it's not like a five or seven minute great Scott video of here's how to use your Paduk microcontroller in five minutes, you know, where everything goes right and everything's, you know, everything's perfect and polished and yeah, it's no, this is for those who want to see the entire process warts and all kind of thing.

**Chris Gammell:** So there's one thing Dave has is warts. Yep.

**Dave Jones:** Exactly. Oh, it's not quite, it's, it's edited. So it's not like, you know, if it was live, it'd be, you know, there'd be a lot of, you know, it's a bit better than doing it live. Yeah. There'd be a lot more warts. But anyway, anyway, in the spoiler alert, spoiler alert, turn off now, mute your podcast now. If you don't want to hear the, what happens in the final video.

**Chris Gammell:** Do you want to know? I'm, I'm, I'm muting. I don't know. Yeah. Go ahead. Go ahead.

**Dave Jones:** Is that.

**Chris Gammell:** Did it all work out in the end, Dave? And, and we all learned something today.

**Dave Jones:** Well, the chip worked like you can see it. First thing in the video is that like, like I powered it, you know, I've, I've spent the last four videos building this thing up, programming my chip and I finally get it to program. And then I go to put it on my breadboard and it's a UART, right? It's supposed to spit out hello world from a, you know, from a software UART, a, you know, an IO, because it doesn't have a hardware UART in it for three cents, right?

**Chris Gammell:** Yeah, it's just a bit of titling, yeah.

**Dave Jones:** Bang. Yeah. And it's, and, and I get data on the screen and I get data on my scope and yay, winner, winner, chicken dinner. Right. And then I start looking at it and I'm going, that's not a UART signal. That's like a clock thing. And then when I went to go in and touch it, the signal started to change as, as my hand got closer to it. And so this, this packet, this data packet is actually changing length as my hand gets closer to it. It's like spooky action at a distance.

**Chris Gammell:** Huh?

**Dave Jones:** This is Einstein stuff, right?

**Chris Gammell:** That's nice. I mean, there's electromagnetics involved, I suppose, but that's about as much as we're going to give you.

**Dave Jones:** No, no. It's all, it's a capacitance, sunny boy. It's capacitance. And yeah. So obviously it's what's happening because it's a UART driven program. Sorry. It's an interrupt driven program. Right. So I think what's happening is the chip was obviously programmed incorrectly somehow. Now. And it was, I still don't know. I still haven't solved it.

**Chris Gammell:** Someone did this. Who did this? Come on.

**Dave Jones:** And it, one of the inputs, cause all the inputs were floating, right? Cause this was just supposed to have a single output. So none of the pins are tied anywhere. Right. So obviously I believe it because if, if, if you see anything change when you move your hand towards it, then you can be pretty certain that you've got a floating input somewhere. Right. That that's actually capacitively coupling like 50 Hertz from your, that's picked up from your body and stuff like that. Right. So it's, so it was interrupting. It was probably restart interrupting this damn thing all the time. And it was just, and it was spitting out this random clock thing as my hand got closer. It was really bizarre. Anyway, you have to watch the video. I still haven't solved it.

**Chris Gammell:** Oh, I thought there actually was a resolution.

**Dave Jones:** Oh, well, no, there is a happy ending. Cause I do, I tried another example program that did work. Right. So apparently this program was, it was not written for the actual chip I had. So there's obviously some sort of subtle variation in there. Something's wrong. So you have to really, I tried to rewrite it. I tried to like go into the instructions, you know, like, and actually almost rewrite the entire thing, but it still didn't work properly. So yeah, I don't know. I'm sure some people solve it and get it working. But anyway, yes, I was able to blink a lead, you know, like.

**Chris Gammell:** Okay. That's, that's a good start. I mean, like what, what are you hoping to use this for in general? Like, or I guess more broadly.

**Dave Jones:** Absolutely nothing. It's just for interest sake. Although I did, I thought maybe, oh, look, wouldn't it be cool to have like a, get this gigantic panel with like 10,000 microcontrollers, like the world's, you know, biggest distributed computing cluster or something. It's got like 10,000 micros on one big panel, you know, it'd cost you more to program the pick and place machine to do it than it would for the actual micros and the board, you know?

**Chris Gammell:** What is the, what is the programming mechanism for it though? Is it like a, are there like programmed pins on it or can it load over? Is there a bootloader for you or how does that work?

**Dave Jones:** Oh, it's a, no, it's like a pick kind of system. It's like a higher voltage thing. So that's why the programmer board needs like a higher, like a 12 volt voltage, you know, DC to DC boost converter. So you've got to like hit it with like, I think it's six volts and 12 volts. So you've got to like put it up to six volts and then that, that pulls out the ID from the chip or something. Anyway, somebody's reverse engineered. They, they, they had to reverse engineer this.

**Chris Gammell:** Got it. Got it.

**Dave Jones:** To be, because I, I actually asked PDUK if they would, they would release the programming information for it. And they said, no, sorry, it's proprietary. So everyone on the EV blog forum went, well, screw that. We're going to reverse engineer this thing. Now they've completely reverse engineered it. There's even, it's even emulated. You can actually get a, you can get the PDUK micro architecture and whack it in an FPGA. Fantastic.

**Chris Gammell:** I would love to know as these things are being designed into things too, that, I mean, like, I guess that's what I'm really wondering about is like the, the application level of like what people are using super tiny micros for in general, just because they're super cheap, super tiny. I generally, I'm interested in that of like, you know, is it just one-off functions or are they trying to squeeze more stuff into it? I mean.

**Dave Jones:** Well, there'll be, there'll be those who are doing it for the fun, right? Yeah. For those who there'll be those doing it for the fun. And a lot of comments on the video were like, well, what's the point of this? This is useless for a hobbyist. Yes, of course it is. You know, there's, if you're building a one-off or 10 of, or even a hundred of units, right? It doesn't matter whether or not you pay three cents for a micro or 30 cents or even $3 for a micro, right? It doesn't really, especially for a one-off, it doesn't matter. Right? So you may as well use your more, you know, your more refined, you know, your, your picks and your AVRs and whatnot. Right?

**Chris Gammell:** Yeah. STM 32s or whatever. I mean, if, yeah, if you have the money for it, right. I mean, I guess it always comes down to like, if you have the dollars for it, you could just throw an STM 32 on it or whatever. Really? Yeah.

**Dave Jones:** But even STM 32s are a 50 cents or a dollar.

**Chris Gammell:** Yeah. No, exactly. Exactly. I'm just saying that. So it's like, you know. It has to be something high volume enough. It's got to be something high volume enough.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** You've got to be using like multiple ones on your design or something, you know, squeezing every cent out of your design. So, yeah. But it's just interesting. A lot of people are interested in this thing. Just from the, just purely because it's a challenge and it is three cents, you know, it's crazy.

**Chris Gammell:** Yeah. So I think that, that kind of gets people's imagination kind of running wild of like, oh, I could do anything with this. And then it's, you know, the reality is of course something less. And when you really are going to spend that kind of time on it, it's like, yeah, maybe you aren't going to use it for everything, but I think it does. It's a, it's a great mental exercise. And for some people, they actually will use it for products or, or whatever's out there. So yeah. I would love to hear about it. If people, if people, if people have a list or something like that, I would love to see a list of what it goes into eventually.

**Dave Jones:** Yep. Oh, segue. I almost forgot. Yeah. Three cent microcontroller. Well, a spoiler alert, I'm probably going to do a video on this to actually test it out, see if it's any good. What about a one cent voltage regulator? There's a jelly bean part that everyone's going to use, right?

**Chris Gammell:** Adjustable or fixed?

**Dave Jones:** This one is fixed. You can all get it in like, you know, different voltage grades. So five volts, 3.3, 1.8, et cetera. But they're one cent, right? Yeah. So everyone uses a voltage regulator in almost every design. It's almost universal, right?

**Chris Gammell:** Yeah. Well, that's kind of a broad statement though. I mean, like. Oh, but come on, right? It's. But they're different. Well, it's different based on like what the needs of the circuit are though. You know what I mean? Like it's not like. Yeah, of course. I know.

**Dave Jones:** You might need a low noise voltage, but most of the time.

**Chris Gammell:** There is, there is no universal.

**Dave Jones:** Yeah. But most of the time. Oh no, there is. Come on. Come on. A standard triple one seven.

**Chris Gammell:** Okay. So what's, what is the one, what's the one cent one? Like how much, how much current output can we get? Get out of this.

**Dave Jones:** 300 milliamps.

**Chris Gammell:** Okay. Yeah. Then that's fine. Right. I mean, I just mean that like when you have starting to have higher current needs.

**Dave Jones:** Oh, well, okay. If you have higher current, you're going to need a higher current regulator, but most people are going to be running like a 3.3 volt microcontroller. So then they're powering it from USB or they're doing with it. And so this need a jelly bean 3.3 volt voltage regulator, right? Yep.

**Chris Gammell:** Yep. Yep. Yep. Yeah. I agree.

**Dave Jones:** And you can get them for one cent.

**Chris Gammell:** Okay.

**Dave Jones:** Which is absolutely amazing from different companies. There's multiple companies, but the generic part number that I've got is the 6206. The one I've actually got in front of me is the SSP 6206. But I'm looking, there's actually cheaper ones on LCSC.

**Chris Gammell:** I was going to say, is this just you browsing through like sorting by cheapest to most expensive? Oh, I'm sorting by cheapest.

**Dave Jones:** Yeah. I'm sorting by cheapest. So the cheapest one looks to be the XC6202.

**Chris Gammell:** Yeah. I guess the power, the linear regular thing doesn't really inspire much creativity in my mind, at least. Maybe it's out there, but you know, like it feels like the programmability makes it something special for the 3 cent microcontroller. You know what I mean?

**Dave Jones:** Right. Yeah. No, no, of course. But because most people aren't going to be using a 3 cent microcontroller, right? But everyone is going to be, eventually you're going to use a voltage regulator, right?

**Chris Gammell:** That's right. Yes. That is correct. Yes.

**Dave Jones:** Right. And do you, okay. Do you, why, why, why would you pay 30 cents for one?

**Chris Gammell:** Right. Would you pay 30 cents for this ship? Oh, I would. Would you pay 10 cents for this ship? Oh yeah, I would. Would you be willing to pay only one cent for this ship? Yeah. I'd love that. Anyways. Sorry.

**Chris Gammell:** And the first 50 callers get a free set.

**Dave Jones:** Exactly. Yep.

**Chris Gammell:** Yep. Exactly.

**Dave Jones:** Oh boy. Anyway. What? Out of curiosity. I'm just searching DigiKey right now. What is the cheapest LDO you can get? What's the cheapest regulator you can get? Let's have a look. Unit price. What? Let's go.

**Chris Gammell:** While you're doing that, I want to bring up as well that there is a new, I'm trying to find it while we're doing this too. I should have had it up before, but there's a new FPGA maker on the scene as well that has like a $2 FPGA. A single quantity $2 FPGA, which is kind of crazy.

**Dave Jones:** Yeah. But tell us the package, son.

**Chris Gammell:** No, no. That's what I need to. That's where the trick comes in, Dave. Yeah.

**Dave Jones:** Welcome to Dave and Chris Google. Anyway, while you're looking for that, the cheapest name brand voltage regulator looks to be $0.05 or $0.04, but that's in a TO92 package. So let's not go there. It's a microchip one, which is actually an old Micrel one, but then there's an OnSemi one. Yeah. $0.05, $0.05. $0.06. So the ones I'm talking about are five times cheaper. And these are thousand of quantities too. And they're a little pain in the ass package. Look at it. I'll show you this. Oh man, this is just, this is some evil shit. Look, let me, oh, just no, no, no, no, no, no. I don't even know what package that is.

**Chris Gammell:** Four dots, the four dots of salt. Oh yeah. Those are nice. I've actually, I've seen this one before.

**Dave Jones:** With a power pad on the bottom. With a power pad on the bottom.

**Chris Gammell:** What do they even call that package?

**Chris Gammell:** To give an audio picture, it's like a diamond in the middle, which is like the, it's like in the diamond shape because it's not square with the, the pad, the, the, the, it's like a square package, but it's a, it's a four pin XDFN.

**Dave Jones:** So it's an XDFN exposed pad. So what, what the pad in the middle does nothing? Is it not connected?

**Chris Gammell:** You got to heat sink it.

**Dave Jones:** No, but it says it's a four pin. It doesn't say it's a five pin. So there's four on the outside and there's, no, no, no, no, no. This is wrong.

**Chris Gammell:** Well, I'm trying to find the, uh, the dimensions of this thing too now.

**Dave Jones:** No, the pad in the middle is not, it looks like it's not connected. Although it's available in a SOC 23.5. This by the way, is the NCP 115 for those playing along at home. And it's available in a SOC 23.5, all this weird ass XDFN package, which is the cheaper one. So you can't get the SOC 23.5 for that price. You have to get this pain in the ass.

**Chris Gammell:** It's a one millimeter by one millimeter. That's the, uh, that's the total package size. Yeah.

**Dave Jones:** Oh no, no, no, no.

**Chris Gammell:** The pin, the pin, the pins that are actually the actual conductive pins are like these weird corner pads and it looks like they're 0.24 by point. Oh, it gives a different size pad size, but 0.24 by 0.26.

**Dave Jones:** Yeah.

**Chris Gammell:** Those are fun, but you know what? It doesn't take up much space. So that's nice. No, no.

**Dave Jones:** That's the whole point. And that's why it's cheap because they used in mobile phones and whatnot, you know?

**Chris Gammell:** Yeah. You know, that came up again. Uh, there's, there's a video we posted to the subreddit this week. He does the flip displays. There we go. Carl Bouget, Bouget, uh, Carl, he, he did a, um, he did a bunch of PCB based motor driver or motors as well. So he did this for Hackaday prize and he has a bunch of cool videos about PC, PCB motors, basically. So he puts the, uh, the coils into the PCB and then he drives, he drives motion with, uh, by driving current through them and stuff like that. So he has a product where he was doing the same kind of thing where he's basically, he's got a PCB, he's got a flex PCB with a coil in it and he drives current through it with motor drivers, but he found a new chip for it instead of, instead of using a, uh, an actual H bridge, which was like one of the TID RV parts. He switched to a, uh, a haptic, uh, driver, like the, the phone buzzer thing. He's basically, you know, the thing that drives your buzzer on your phone. Yeah. But I'm watching the video now. Anything like that. Yeah. Anything like that, where you can get, you can harvest something off a phone. You're going to be super tiny, but you also, you're going to get super cheap stuff out of it. So that's kind of nice. Right. And so he kind of goes through how the, uh, you know, the differences between an H bridge and this, and this specific driver part and any tests and stuff. It's, it's cool video. I liked it.

**Dave Jones:** Anyway, I hereby deem that the XD FN four package wins the pain in the ass package of the week. That should be a new segment. Seriously. One millimeter by one millimeter with it. Oh, bloody. No.

**Chris Gammell:** Yeah. Wrong. I've been getting more comfortable. So I've been doing a lot of, I think I have a, I have an eight pin, I have a six pin BGA on a recent board. I have an eight pin X on something like that. Or is that what this was? I don't know what the part, part names are, but much, much tinier than I've been used to. But I, did I tell you about my new micro microscope setup? I tweeted about that.

**Dave Jones:** Uh, you, I thought, yeah, you tweeted about, I saw the photo. It's a big long zoom lens. Yeah.

**Chris Gammell:** So it's got like, it's like a telescopic lens and then it's got like a four 40 megapixel sensor on it. And then I just hooked it up to an HDMI meter or HDMI screen kind of in line with what I'm doing. You know, people pointed out right, rightfully so it's not, it's not a microscope. It's not, you know, it's obviously not stereoscopic. So I don't get depth perception, but for me, it's just been super helpful just to get to the detail levels that I need to. And I like that it's like out of my workspace. So it's actually, it's actually, as it's shown, it's mounted out of my, um.

**Dave Jones:** Oh yeah. The working distance is like 400 millimeters or something. Right. It's huge.

**Chris Gammell:** Exactly. Yeah. It's, it's really nice for that stuff. And it's a video by volt log. So he had, uh, recommended it actually as a add on to like a low cost. Um, it's like a trinocular microscope. Yeah. And then I, but then at the end he's like, yeah, you can, yeah. Stereo microscope with like the, with the port for doing HDMI capture too. And, uh, and at the end he's like, yeah, you can just buy it by itself by yourself. And it's like $95 I think shipped. So like that was awesome. So yeah. Yeah. Yeah.

**Dave Jones:** I was doing that. Like I, I love my Tugano. I love my Tugano microscope for like zooming in and stuff, you know, it's got a huge working distance zooming in. Yeah. It's got 30 times optical zoom. It's, you know, it's absolutely phenomenal, but I hate soldering under it with a, you know, HDMI monitor. Yeah. No, it just, cause you don't get the depth perception and stuff like that, but it's the best thing I have for video capture. Right. I can't use my.

**Chris Gammell:** What would you prefer for, for, for soldering?

**Dave Jones:** I would use my Mantis, which is a stereoscopic, uh, stereoscopic hood. Um, Oh, sorry.

**Chris Gammell:** I was getting those confused. I was getting those confused. The Mantis is one like the heads up display you're saying. And then you would have the.

**Dave Jones:** The Mantis is the heads up, heads up one. Yeah. Heads up analog. Got it. Got it. You know, real lenses and mirrors and shit. So yeah. And that one does have a camera built in, but it's so crap. It is like, it can't even take a decent photo, let alone video. It's just, you know, and, and the optical quality of the Mantis, if you've ever looked through one is, is, is phenomenal. That's why they're super expensive, you know? So I've got this phenomenal optical microscope and I can't get with a, with the factory built in camera. And I, I don't even know why they even sell it with the camera built in. It is, you know, it's absolutely useless. So I do have other stereo microscopes here and I do actually have technically a lens capture attachment for it. So maybe I should look at, yeah, but it doesn't have a big working distance, you know, doesn't have a big, uh, yeah. Optical working distance. So if I want, you know, a large optical working distance, um, well, well the Mantis isn't that huge a working distance, but it's good enough. So yeah, but it only like, yeah, I do have a times 10 lens for it, but that's too much. And then it gets too close and stuff like that. So I usually only sold it with a times four or times eight, if I need to zoom in. Um, and my, my normal zoom level would be four.

**Chris Gammell:** Uh, yep. I think the, the thing with the, uh, the, for me, for me, at least it's like being able to get hot air under there too, is like important. Like, so like soldering. Yeah, of course you need that, but being able to get like the hot air pencil under there and like not damage anything. That's another thing that's like super critical for me to be able to, to, you know, just to manipulate things and move them around. Cause I keep stupidly designing in tiny switch mode supplies and all these crazy ass packages they keep coming out with like, Ooh, new part. I'll try this bad idea. Bad idea. Yeah.

**Dave Jones:** Oh, what's the world coming to the world's going to shit. I'm telling you Mars.

**Chris Gammell:** Oh, that's what, that's what made you notice. That's what made you notice Davis was the microscopes. It wasn't anything else.

**Dave Jones:** Oh boy.

**Chris Gammell:** Anyway, 2020.

**Dave Jones:** Playing the last package of the week. Yeah.

**Chris Gammell:** Okay. I can't find this FPGA thing. It was somewhere on the consulting form. I can't find it for the life of me. So I don't know what the hell it is. Yeah. It's some new, there's new, the new FPGA out there. I'll try and find it for next, next time. So we'll see how it goes.

**Dave Jones:** Speaking of soldering, another segue. Yeah. I did a recent video on a, um, the soldering fume extractor. What, what sort of stuff did, what fume extractor are you using at the moment or nothing?

**Chris Gammell:** Yeah. My lungs, unfortunately. Sucking up like a man.

**Dave Jones:** Yeah. Right. Put air on your chest. Yeah. Right. Yeah. Okay. Yeah. Right.

**Chris Gammell:** No, it's stupid. It's, um, yeah, I don't use, um, you know, I had one of those, just the cheapo, you know, molded black plastic with the fan in the back and like a, but you have one that looks like, uh, like a, like a elephant trunk almost. Right.

**Dave Jones:** Yes. It's a big snaky thing, which, so it sits under your desk and I got this new big snake, you know, yeah, the big snaky nozzle thing comes up over the bench. Um, and you put it straight over your work and it works well. But the problem is, I think it's even like, I got the low noise model. It's still not low noise enough, you know? Uh, so it's frustrating.

**Chris Gammell:** I have been noticing as I like, you know, do a lot of video calls. Everyone's doing video calls these days, but like, you know, my hot air pencils left on. Oh, that's loud. My VNA is on. That's loud. Everything's got a fan. Everything generates heat.

**Dave Jones:** It's like, yeah.

**Chris Gammell:** So, you know, noisy stuff. What are you going to do?

**Dave Jones:** Yep. I don't know.

**Chris Gammell:** Invent the quiet fan.

**Dave Jones:** You know, well, I, I, I do have, like, I modify one of my pace ones to put a quiet fan in it. You know, I had this, uh, 240 volt, you know, mains fan in it. And it was like, sounded like a, you know, a, um, sound like a jet fighter starting up.

**Chris Gammell:** Yeah.

**Dave Jones:** And, uh, so I modified it with like a really silent PC fan, you know, and it's great. It's really silent, but it doesn't suck much. So yeah, I want my, I want my fume extractors to suck. Yeah. And, uh, yeah. So you have to get it like really close. You've got to get it like right up in there to sort of, you know, you've got to be right next to the damn thing. And most board, you know, which is okay if you're working on a tiny little board, maybe, but you know, if you're working on anything larger, it's just hopeless. It just like, cause your board is too far. And so the fume extractor has got to be on the other side of your board. So anyway, yep. Yep. So you need these, these snaky arm ones are great.

**Chris Gammell:** Get like a big fan to just blow it across the entire desk and then have like some cold, you know, big collection mechanism. Well, that's the other thing you can do.

**Dave Jones:** I've actually done a video on that too. Yeah. You can just modify it. Just get a regular PC fan and stick a battery on it or with a boost converter and bingo, you've got a little fan to just blow it out of your face at least. Which is a fine solution if you've got like, you know, open windows and open doors and stuff like that.

**Chris Gammell:** But right.

**Dave Jones:** If you're in a yard.

**Chris Gammell:** Or if you're doing air filtering other ways in your place.

**Dave Jones:** If you're doing other, yeah, exactly. I could use my other big air filter in a, in my little soldering room.

**Chris Gammell:** But yeah.

**Dave Jones:** Anyway, fumes. When I was a boy. Yep.

**Chris Gammell:** I mean, yeah. Suck them right up. I'm trying to, you know, I've switched to lead free, but yeah, the, the, the flux is still not great. So, and that's usually what's kicking off a lot of the fumes.

**Dave Jones:** You do realize there's no lead fumes in there. You do realize lead fumes aren't a thing. Right.

**Chris Gammell:** Right. Right. Exactly.

**Dave Jones:** It's, it's the same rosin flux that you suck it up regardless of whether you use lead or lead free. Right. Exactly. Makes absolutely no difference.

**Chris Gammell:** Yep.

**Dave Jones:** Anyway.

**Chris Gammell:** Did we mention on the show? So I had mentioned on the show about Alvaro at one point making a storage system. Did I mention that?

**Dave Jones:** Storage system. Yes, you did. Yeah. You mentioned it the other week. And I did. Okay. I wasn't sure when that video came out. Yeah. Yeah. It's a lot of effort, you know, individually bagging things up, making barcode, printing barcode labels for your database. And there's, you know, there's some reasons, you know, some people would, some people would get great advantage from doing this, but most people wouldn't. So. Yeah.

**Chris Gammell:** I think it, it depends on the type of work you're doing for sure. If you're doing like, so like for me, uh, I've been doing project based work, right. Just for different clients. Yes. And it's, as long as I have the parts for the build, it's like I put all the box parts in a box and they stay there and I labeled the box and that's fine. It becomes a storage nightmare, of course. And then the problem is like when the projects, you know, moves on to the next rev or whatever, then it's like, okay, now what do I do with all these parts? So that's when I think this kind of thing comes in, uh, because then I'm like rooting through the box when it's, it's not, uh, when I, you know, like the next rev needs a part and I'm out of it or whatever. But, um, yeah.

**Dave Jones:** But sometimes it's often just easier, cheaper and saves time just to simply, regardless of whether or not you've got the parts, just order your entire bomb from your DigiKey or your mouse or your LCS or whoever you happen to use. And it all just comes and they're all bagged and they're all labeled and they're all ready to go. And yeah, you know, it's just, it's just easier. Yeah. Yeah. It's kind of, you know, it's wasteful and it's, you know, stuff like that, but it's like, you just can't like, there's always going to be parts that you can't use. So what are you going to do? Like, sure. You can check your database. If you've got this system. Oh, I know I have X number of those parts. So then you don't have to, uh, do it or whatever. But as I showed in my, uh, recent video, my first in this multi-part series video of how to upload a bomb to your DigiKey and your mouse as your component supplies, you can just upload your Excel bomb. Right. And bingo, you can, you know, it, it takes like a few minutes and it'd take longer to search your database and figure out manually what parts you have and then actually remove them from your bomb. Cause you're almost going to have to, you know, almost certainly going to have to order something from your component supplier. Right. You won't have everything.

**Chris Gammell:** Well, and I think that's the thing is like, if you, if you have enough iteration, then you might. Right. But yeah, I think that's the point.

**Dave Jones:** If you're doing subtle variations on the same project every time for 10 different clients, you know, then yeah, yeah, of course. But yeah, as I said, very few people are going to be in that position though. It's just like having your own pick and place machine. It's going to be useless for all, but a very select few people who have that particular requirement.

**Chris Gammell:** Yeah. And almost, I wonder if that crosses over too, cause then you'd have like the, it'd be beneficial to have the same parts again and again and again. And it would change your design mindset too. Right. We wouldn't be looking at, we wouldn't be looking at any one millimeter by one millimeter. No, no, no. Like cheapest parts. The cheaper thing in that case, especially if it's low volume is just to use what you got. So yeah, of course. That's the reason to do that kind of thing. Yep.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** And then, and then the size and shape and everything of your board is, is actually dictated by the parts you've got, you know? So. Exactly. Yep. And unless you're designing like a new smartwatch or something, no, you're not going to be, you know, using this pain in the ass one millimeter by one millimeter package. Yep. Yep. Yep. Yeah. Ah, boy. Anyway.

**Chris Gammell:** Yep.

**Dave Jones:** What else we got?

**Chris Gammell:** Oh, not much on the list. I, uh, I almost electrocuted myself the other day. That was fun.

**Dave Jones:** Excellent. Well done.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** But you've just got that wimpy 110 volt rubbish in the U S.

**Chris Gammell:** This was a isolated transformer that can do a kilowatt. So, um, it was more.

**Dave Jones:** Yeah. It, yeah, it has a, yeah, but it's still only 110 volt, right?

**Chris Gammell:** I mean, no, it was a DC bus voltage that was generated and stuff like that. Anyways, it was a bad, it was bad. Uh, it, it was floating much, much above, much more above chassis than I thought it was. And, um, and, uh, I, I went to go measure with the scope and, uh, and scope scones or chassis scope, scope, scope, scope, scope.

**Dave Jones:** It's there. I swear on, on this audio link, it sounded like a scope. That's like a scope. That's gone up in smoke. It's a scope. Yeah.

**Chris Gammell:** That's actually, that's about right. Actually. Yeah. Yeah. No. And, uh, yeah. So the, uh, the, uh, things are chassis, chassis grounded. And, uh, kabam. Uh, I basically, I vaporized a wire. Uh, so that was fun. Yep. Yeah. It was, it was my, my little bit of welding for the day, I guess. And, uh, scattered some, some carbon all over the place. It was actually kind of interesting. Um, so, uh, one of the forum members, he actually reviewed a super, super low cost handheld scope. I wasn't really expecting much out of it. And I mean, it's not that great. It's, you know, like low cost, um, displays and stuff like that. But, uh, for that kind of thing of where it's a floating scope then, right. You're not chassis, you're not tied to chassis. You don't need an isolation transformer or anything like that on your scope. Then you, uh, you can, you can do stuff like that. So I don't know. I just thought it was pretty cool. I'll send you a link.

**Dave Jones:** Oh yeah. No, that's why I have a portable scope. It just, you know, it's not. Yeah, exactly.

**Chris Gammell:** Right. When you're doing like, like, uh, high, high voltage stuff and things are spread out.

**Dave Jones:** But I've got high voltage probes as well. You know, I've got high voltage differential pros, which aren't isolated by the way. I've done a whole video tear down and actually reverse engineering of a high voltage probe video. Oh yeah. And, um, yeah, people just assume that these high voltage probes are isolated. They aren't. They just use a crap ton of resistance in series so that, you know, the current, so that, yeah, it's, you know, they just use these high voltage strings and they, yep. Basically a four meg resistor in each, uh, line. And, and then, and then you have a, a, a, a resistor voltage divider and that's how it does it, you know?

**Chris Gammell:** Yeah.

**Dave Jones:** And it doesn't blow stuff up because well, it's eight meg, you know? That's right. Yeah. There's not much current you can do unless it arcs over, but that's why they put multiple resistors in series on the string because you can't get a one kilovolt resistor. Well, you can, but they're special, right? So you just get a 12, you just put four or five 1206 resistors, which are about 200 volts a pop. You know, you put four or five of those in series and bingo, you've got yourself a do it yourself high voltage resistor and that's how they do it. So yeah. Way to get it done. These, these high voltage probes. Yeah. They're not isolated. So, and they don't have to be. So, which is great.

**Chris Gammell:** That's awesome.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah. So for a hundred bucks, interesting. I'm not sure if I'll get one, but the, uh, you know, it's a cool review of a low cost, low cost handheld. Cause usually the handheld ones are, uh, I don't know what, how much yours was, but the ones I've seen are pretty pricey.

**Dave Jones:** Oh, mine was like 50 bucks or something.

**Chris Gammell:** Oh, really?

**Dave Jones:** Well, no, I've, I've got a, like a high end one, but I've also done video reviews of cheap ones. So I've got a, you know, yeah. Like one of them's like 50 bucks or something.

**Chris Gammell:** Got it. Yeah. Yeah. Yeah.

**Dave Jones:** Super cheap. And it's got like 20 meg bandwidth, you know, it's like, yep. Which is good enough, but it kind of, you know, it's, they're really built down on price.

**Dave Jones:** Right. Yeah. Exactly. For a reason. Yep.

**Chris Gammell:** So, um, how goes the, uh, speaking of test equipment, how goes the, uh, how goes the micro supply?

**Dave Jones:** I will, I will get back onto it. I'm going to do a summary video of like state of the nation where it's at.

**Chris Gammell:** Okay. Okay. Yeah.

**Dave Jones:** People will see it.

**Chris Gammell:** Okay. So that's good.

**Dave Jones:** Yep. I just, you know, it's just me at the moment. So that's right. That's right.

**Chris Gammell:** Back to, you know, back to just Dave. Back to just Dave.

**Dave Jones:** Yep. I've got lots of, uh, yeah. I, and I've got other, uh, products, which I've got, got to evaluate as well. I've got an issue with my micro current that I've got to, uh, solve. Cause that's not for sale at the moment. A lot of people keep asking. There's an issue there that needs to be solved. And, uh, and I've got a couple of new products that I need to evaluate, um, for sale, you know, things like that. So, yep.

**Chris Gammell:** Great.

**Dave Jones:** Cause you know, I've got to stay in business, you know, I've got to flog stuff for a living. Yeah. Yeah. This YouTube gig still doesn't really pay the bills. So after a decade, right. Got to flog stuff. Yep. Yep. Now, well, yeah. So speaking of sucks up a lot of my time. Yeah.

**Chris Gammell:** Speaking of, uh, sorry, going back to, uh, uh, soldering rather. Um, uh, I've been doing a bunch of tiny mods because of tiny mistakes. Um, and, uh, yeah, uh, you know,

**Dave Jones:** And stuff like that.

**Chris Gammell:** Yeah. Well, more like, uh, forgot to assign pins or got the wrong pins on a QFN part. And so I've been doing enamel wire jumpers and all that kind of fun stuff. Um, yeah, but it's, um, you know, I've been using my share of flux and, um, and I was asking over on the consulting forum and I thought maybe I'd ask you or two of like, what are you usually doing for like cleaning up boards? Like, are you, uh, you just going straight with isopropyl or what, what do you, what are you doing these days? If you're, I mean, do you ever use ultrasonic or anything like that?

**Dave Jones:** No, I don't use ultrasonic. I've got various, uh, flux removers. Um, like I've got a local chemtronics Australian brand flux for me. I've got heavy duty flux remover and, you know, which isn't just IPA. It's not IPA. It's got, uh, you know, tetra, cause a hydrazine or something in it. Yeah, exactly.

**Chris Gammell:** There's always, yeah, like some kind of benzene ring in there to make you asphyxiate. Yeah.

**Dave Jones:** I can actually go and get it and I can read you the, I can read you the, uh, I mean, that might be interesting.

**Chris Gammell:** Yeah. Yeah. Yeah. So this bodge. Hang on. Hang on. I'll be back. I'll talk about the bodge. Yeah. Okay. Yeah. We'll see how that goes. Uh, yeah. So this bodge was a bunch of enamel wire, which I had never done before. I actually, I will put a link in. Um, I had an enamel wire, you know, 30 wire, 30 gauge, three, 30 AWG, but I had never like, uh, I never actually used it before. I, and, um, I was looking at like how to strip it. And there's a article on Hackaday about just burning off the ends, which, you know, people were using enamel wire, like, yeah, duh, no joke. But yeah, it's pretty easy. You just basically put some soldering solder on the end of your song and you put the wire to it and just burns the enamel right off. So yeah, a new, a new way to, uh, solder stuff on there. Yeah. Don't breathe. I've not used a lot of magnet wire in the past. So yeah.

**Dave Jones:** Anyway, ultra flux remover, unfortunately, um, it's non-corrosive, low toxicity. It's a chem tools, cleanium ultra flux remover, but it doesn't actually tell you the, um, ingredients. So I guess you'd have to read the MSDS for the material safety data sheet.

**Chris Gammell:** Oh, I guess.

**Dave Jones:** Yeah. It doesn't actually, doesn't tell you what's in it, but, um, yeah, it's not just, um, isopropyl. So yeah. Right. Anyway. Okay.

**Chris Gammell:** Yeah. Cause I know I, my, um, I have, uh, what's it called? Uh, not shellac, but the conformal coating stuff. And that's another one where it's like, you look at a conformal coating, uh, spray container and it's, it's, it's nasty. It's, it's real nasty.

**Dave Jones:** Yeah. Oh yeah. That's, that's horrible stuff. You need like a fume hood or you need to simply put it outside somewhere while that stuff. Yeah, exactly. Yeah.

**Chris Gammell:** Don't want to, don't want to concentrate it, treat that anywhere. Okay. So you're just using flux remover and, and isopropyl.

**Dave Jones:** I just use flux remover and then I might use an isopropyl thing, you know, to clean it all up. But yeah, no, generally, yeah. Heavy duty flux removers are good. Ooh. Ingredients. Here we go. Here we go. I've got the ingredients. Hang on. Light hydro treated petroleum naphtha. Propylene glycol. Closely related to napalm.

**Speaker ?:** Yeah.

**Dave Jones:** Love the smell of napalm in the morning. Propylene glycol monomethyl ether and isopropanol.

**Chris Gammell:** Oh, okay.

**Dave Jones:** Yes. Anol. Anol. Anol. Not isopropyl. It's got the A-N in there. So, yeah. So it's got a combination of all these, yeah. I mean, Mrs.

**Chris Gammell:** Evie, Mrs. Evie blog's a chemist, right? She could tell you what some of those things are, right?

**Dave Jones:** Yeah. I'm sure she's good. Yeah. Yeah. Oh boy. Yeah. Yeah. Not good. So anyway, that's why I've also got it. Yeah. My fume extractor is not just a fume extractor. It's got a charcoal filter as well, which, which takes out the, you know, the toxic fumes as well. So.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah. Does both. Hmm. Anyway. Yeah. Heavy duty. I've got ultra and heavy duty. Oh yeah. Yeah.

**Chris Gammell:** People were saying on, so one of the reasons that I was asking about it too, is because one of the boards that I'm doing has like, it's a humidity sensor. And so I figured that's got like water ingress, you know, it's like tiny, tiny hole on it. But like, you know, just thinking about like washing, you know, I still like, I still get kind of antsy about just like washing boards, you know, like people like there's like water soluble, even flux and solder and stuff like that. But like, I still, I'm just like water and circuit boards. You don't, you're not supposed to do that, but it's like, yeah, I know. It really can do that stuff.

**Dave Jones:** It requires a leap of faith. Yeah. Yeah.

**Chris Gammell:** You know, and then, yeah, then you could dry it off and heat it up and whatever, but like, I, yeah.

**Dave Jones:** Yeah. I'm not going to use it. If I've got the isopropyl, I'll just use the isopropyl, you know?

**Chris Gammell:** Yeah. Yeah.

**Dave Jones:** It's like, yep. And a brush. It's nice to have a nice conductive, you can get one of the conductive brushes, right? The proper PCB scrubbing conductive brushes. Otherwise they can generate static and, you know, potentially kill your boards.

**Chris Gammell:** Yeah.

**Dave Jones:** And, and, you know, give it a good, good scrub over. Don't just, you know, spray on your isopropyl and just leave it to drip dry. Actually get your scrubbing brush in there and, you know, over it. Yep.

**Chris Gammell:** Yep. Yep. That's a good point. Get the, getting the residue off. It feels like that's the main thing. Cause like sometimes I'll just like be spreading it around and then it's just, it's just like, oh, I made this worse. You know? Depends to the type of.

**Dave Jones:** I hate it when you drip it. Like you, like you spray your isopropyl on your board, you hold it over your bench and then it like drips off and all the gunk, all the flux residue comes off. And then it's like a murky kind of, you know, crap on your bench. You know, it's like. Right.

**Chris Gammell:** Yeah. Yep. Oh, well.

**Dave Jones:** Anyway, what, what do we got left? We got like five minutes left. What do we got?

**Chris Gammell:** Oh, this is, uh, there's a really good video actually just found today. Um, uh, someone designing, you know, it's just kind of like soup to nuts doing a design and I can add STM 32. It's a NRF 24 chip kind of building into like a little, uh, platform instead of just like buying a low cost. You basically built his own and, um, you know, it's good picking out parts. It's good picking out or doing some kind of stuff, um, doing some of the firmware choices and stuff like that. So I really just liked it for, um, kind of doing everything together. Um, so that's a good one.

**Dave Jones:** Yep. Oh, hang on. I've, I've got a really good one. I'll try and find the link. Somebody posted on Twitter. Um, it's an Aussie guy, e-waste Ben. Have you ever seen him? He like scraps boards for, for gold e-waste, right? Cause there's gold in them, their boards, right? Um, and seek your fortune and glory kid in, uh, scrapping PCBs. And so yeah, he's an, he's an Aussie. I believe he's down in Victoria somewhere and he scraps all these boards. So he's got a YouTube channel and an e-waste business. And somebody, you know, uh, somebody on Twitter posted, um, who was it? Who did the, uh, the twisting capacitor thing to get off the surface mount capacitors. Right. Oh God. Yeah. You, you, you tweeted it and then I retweeted it from your tweet or whatever. And yeah, so there's a big to do on there. Some people are saying, you know, and I tweeted, uh, no, that's, you know, like I tweeted the force, you know, it's as if it's painful to watch cause he's. It's painful to watch cause you twist. I've done it myself many times over the years. And it does.

**Chris Gammell:** I mean, getting those. So this is, these are the large aluminum electrolytics, like the, the big can capacitors, not like the old school, like not the old, uh, electrolytics, but these are the silver cans. So people are visualizing it. Someone basically took a pair of, yeah, they took a pair of, uh, wire strippers, used them as pliers and just twisted the damn thing off.

**Dave Jones:** So it's, uh, and just twisted back and forth and it breaks the legs and leaves the legs. And then you can get the cap. So you've got the cap off and then you can get in there if you soldier it on and just scrape the pad, scrape the, uh, the lead off the pad, you know?

**Chris Gammell:** Right.

**Dave Jones:** So it isn't magic. You still have to clean those pads up, you know?

**Chris Gammell:** Right.

**Dave Jones:** So.

**Chris Gammell:** But it actually is really hard to get those unless you have double, unless you have a double, um, soldering iron, it's hard or like soldering iron tweezers. It is actually hard to get those.

**Dave Jones:** No, you get in one side, you lift it up, you bend it and you get to the other side, you lift it up, you heat up one pad and you bend it. It's not rocket science. You, you just need to get access. Uh, access is usually the problem, you know, like other parts are like obscuring the, the thing or whatever. So. Yep.

**Chris Gammell:** Okay.

**Dave Jones:** So this started something else you're saying. Yes. Somebody tweeted, I, I, I, I know e-waste, Ben. I've seen his videos before. And somebody said, that's not how you remove components. You know, this is how you remove components. I'll, I'll get the link. And he, he uses a pneumatic chisel thing. You know, one of those pneumatic chisels that like goes in and out and he's like, um, he's like chiseling off all the parts.

**Chris Gammell:** I was just like, uh, like this is like how they do. Um, this is like how they do, uh, taking out, uh, floor tiles or something like that. Like a jackhammer, but like a, in a chisel.

**Chris Gammell:** Yes. Yeah. Yeah. Yeah. Take it out for. Yes. Like a jackhammer with a little chisel end on it. And this is how he takes connectors off the boards. It's just, it's awesome.

**Dave Jones:** And, and, and horrific and directly disturbing at the same time. I'm trying to find the video, man. It's just, oh man. It's like, yeah, it's.

**Chris Gammell:** Yeah. Oh man. I mean like, and so what is, what are the parts he actually harvests? Is he harvesting the boards themselves or is he getting the parts or.

**Dave Jones:** Uh, not, not usually he harvests the, the connectors and the pins because, because pins and connectors are usually gold plated. They're usually hard gold plated. Right. Especially like your high quality ones and especially the ones in the 1970s. They were using gold. Like it was no tomorrow, you know? And, uh, they were really, you know, 10, 10 micron hard, hard plated.

**Chris Gammell:** Right. Well, the parts were so expensive anyways. Why not just, why not just, why not just plate them with gold anyway?

**Dave Jones:** Exactly. And, uh, yeah, back then, you know, like do I hit 10 micron hard coating now? It's like, oh, like half a bee's dick, you know, hard gold. If you're lucky. It's so, you know, they, they claim it's hard gold, but it's actually, you know, yeah. It's like, yeah. Flash, gold flash. Flashiest gold flash you can get. The thinnest gold flash you can get.

**Chris Gammell:** You get exactly. You get one insertion cycle and that's it. That's all you get.

**Dave Jones:** You get one insertion cycle before the gold went off. Yeah. It's just terrible. Yeah. They just don't make them like they did in the seventies, you know? And, um, anyway, or you really, so he's getting, he's scrapping all these boards. He's getting like these, uh, Cisco router boards worth a hundred thousand dollars each. You know, it's just, oh, it's just.

**Chris Gammell:** The gold is worth that much or the, or the boards are worth that much?

**Dave Jones:** No, no, no, no, no, the actual board. I don't know how much of the gold's worth, but you know, you might get like, you know, 10 bucks worth of gold from each one or something. I don't know. But, um, yeah, it's just. So he's.

**Chris Gammell:** Okay. But they were originally a hundred thousand dollars. You're saying.

**Dave Jones:** Oh yes. The, the board to buy is a hundred thousand dollars. Yes. And he gets all this stuff for free, you know, because people are tossing them out. The e-waste, but, uh, and, and he even salvages like tantalum capacitors. Like. I, I don't know how you recycle tantalum. Interesting. But geez, you know, I, I know tantalum is expensive and it's kind of rare, but you know, it's like. Jeez.

**Chris Gammell:** Oh, he's not really, he's not using the capacitors again. You're saying he's just somehow harvesting the actual, the element.

**Dave Jones:** Oh no, no. He, he, he, he melts these things down to get all the, to get all the raw materials. Melts them down. And it's just unbelievable.

**Chris Gammell:** Yeah. True. Yeah. I always wonder about that with like, you know, e-waste and recycling and stuff like that too. Like is someone doing that at some other point, you know, like.

**Dave Jones:** Oh yes. Harvest them. And they, and they put them in a big fire and they melt it all down and it releases all the time. I don't know where the toxic fumes go probably into the atmosphere or whatever, but you know. Um, yeah. And you know, little dribbles of gold come out. Exactly. Dribbles of other metals come out. So. Yeah.

**Chris Gammell:** Sometimes I think about this Dave and I think about the fact that we're, you know, you know, I'm, I'm not doing anything super high volume, but we are contributing to this. And I kind of have that, uh, that sketch in my head of like.

**Chris Gammell:** Probably. Yeah. I know. I think of that all the time.

**Dave Jones:** You know, it's, we're so wasteful. You know, we were talking about that earlier in the show. We're talking about, oh, just, you know, buy it from DigiKey, right. Buying all the parts, you know. Yep.

**Chris Gammell:** Just buy more parts. Right. Right. Right. Man. Yeah. Yeah. I mean, it's a drop in the bucket compared to like the, uh, the, the broad, like how much stuff's getting made, but like, yeah, it's still sometimes when I think about the element of, of, uh, stuff that's being made, it's like, or like stuff that's being manufactured and there's a lot of, a lot of stuff that ends up in the bin.

**Dave Jones:** Anyway, um, I'm gonna, I'm gonna find this video. So we're ending on a happy note today. I'm going to find this video. You go. Here we go. Here we go. I think I found it. I think I found it. No, no. Hang on. I'm getting there. I'm getting there. Please. I'll, I'll get there by the time we close out the show. Surely.

**Chris Gammell:** All right. This show brought to you by our patrons. And, uh, thank you to all of them. If you didn't know, you can sign up on Patreon today. You get access to our discord channel and you get early access to some content. And, um, we haven't done a meetup yet, but we plan to actually discord just, um, just turned on a thing where all the chat rooms now have video too. So if you go into it, sorry, if you, if you go into the audio chat rooms, they all are enabled with video up to 25 people. So we need to plan to do that at some point and have a, uh, little video conference, meet up with folks. So we'll set that up sometime soon. But if you become a patron today, you support the show and you also get access to the community. So thanks to all our patrons right now and hope other people will become patrons in the future. This message brought to you by Dave, not being able to find you a link.

**Dave Jones:** That was very professional, Chris.

**Chris Gammell:** Dave, do you even, come on, man. Do you even internet?

**Dave Jones:** Do I even internet, bro? I'm pretty poor at internetting. It's, it's all new to me, you know, all this internet thing.

**Chris Gammell:** That's what I was saying, you know? So while Dave's doing this, I guess I'll talk more about stuff. Uh, KiCad has another plugin. That's kind of cool. There's an automatic panelization tool called KiCat, KiKit, KiKit, maybe KiKit. That's probably more likely. And so there's a new tool out there that does panelization. Uh, it does it just, I don't think it does. I think it's just panelization with break tabs, not with V score, but, uh, this actually was pretty tough to do in, uh, in, I mean, you can do it manually. And, uh, Peter, as in Tebski has some videos about that. That's what I used to learn how to do it. Uh, but now there's more plugins and stuff like that because all the other plugins I'd seen in the past had not worked. So pretty cool that there is this new thing there. All right, Dave, check in or should I, should I mention another, another, uh, I got it.

**Chris Gammell:** I got it. I got it. I got it. I got it. I got it. More stuff. I got it.

**Chris Gammell:** Here we go. I got it. You'll love this. You'll love this.

**Dave Jones:** You gotta watch it. Here you go. Be prepared to be horrified.

**Chris Gammell:** Okay. Another thing I will mention is, uh, if you're, if, if you're an Eagle user, there's also a link on this subreddit, uh, Lamora from Ada Fruit, uh, Lady Ada, we did a stream as well. We'll link that in. So she did an Eagle. Uh, she showed how she penalizes her boards too. So that's another good one. When you want to see you make a more manual process. Um, I think Eagle has plugins too, but, um, but it is good to see how to do it. Oh, I've done panelization videos. Yeah. It's got like a million views. Panelization videos. You've definitely done the panelization videos, right? Yeah. Yeah. No, like a million views, whatever. You know, still we do. Just like a million views, whatever. Okay. So I'm watching a video that Dave sent me now. Removing icy chips. Holy crap. Keep on going. He does everything.

**Chris Gammell:** He does the entire board. He's doing it on carpet. He's doing it on carpet.

**Chris Gammell:** All right. I'll watch it more later. Yeah.

**Chris Gammell:** Yeah.

**Chris Gammell:** Yeah. That carpet. Oh my God. I don't have an industrial vacuum cleaner or something.

**Chris Gammell:** It's just horrifying to watch yet. Yet somehow satisfying. Yeah.

**Chris Gammell:** This is great. We'll definitely have this link here. No, no, it's great. That's, that's fantastic. Yeah.

**Chris Gammell:** I'm watching. I can't stop.

**Chris Gammell:** That's actually a great way to take off components too. I mean, like taking off connector sucks, right? It's better. It's better just to, you know, knock, knock the plastic part off, go and then, you know, solder, desolder all the pins and then, uh, this is a pretty, reuse your board. Yeah.

**Chris Gammell:** Oh, it's just, I, I just can't.

**Chris Gammell:** Yeah. You just cannot. I don't think so either.

**Dave Jones:** You have to watch it. You cannot look away. It is just.

**Chris Gammell:** Yeah. Well, these other videos, like 10 most valuable CPUs for gold recovery. Yeah. This is a very specific channel. This is like, this is like even more than I expected. If you want to get gold out of e-waste. Okay, cool.

**Dave Jones:** That's what he does. He, he, he scraps all these components and e-waste and he gets the gold out of, you know, it's, I, it's a lot. It's a hard, messy business for not much return. It's exactly, it's, you know, anyway, it's a business.

**Chris Gammell:** It's works for him.

**Chris Gammell:** Do you think he looks at like Bitcoin miners? He's like, you, you think you're getting riches out of, out of mining? Yeah. Come on. Right. Yeah.

**Dave Jones:** It's a hard, messy business. Yeah. So, yeah. So is this. I mean, there is not much gold. There's like, you know, in a, even in a high end board, there might be, you know, 10 bucks worth of gold and the amount of effort you've got to go to, to, uh, you know, extract that, you know, huge furnace to extract all the gold from, you know, melted away from all the plastic components and everything else. It's just, uh, it's just incredible, incredible amount of work for, yeah, very little, but I guess it'd be satisfying in the end, you know, you end up with this little lump of gold. Right.

**Chris Gammell:** So, yeah, you know, but yeah, anyway, brilliant.

**Dave Jones:** Well, that's it. That's all we have for this week. We'll link that in. Check it out. It'll change your life.

**Chris Gammell:** Definitely.

**Dave Jones:** All right, man. Talk to you next week. Catch you next time.

**Speaker ?:** Bye.
