---
episode: 175
title: An Interview With Andrew Witte - Telistic Timepiece Technomania
url: https://theamphour.com/175-an-interview-with-andrew-witte-telistic-timepiece-technomania/
---

**Chris Gammell:** This is the M-Hour Podcast, recorded December 9th, 2013. Episode 175, with guest Andrew Witte. Telistic, timepiece, technomania.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics. And I'm Andrew Witte from Pebble Technology.

**Dave Jones:** Hey, Andrew. I'm being ganged up on again. You're from Case Western, same as Chris.

**Engadget:** I am indeed. I don't know if I ever met Chris there. No, I was hiding in the shadows. Okay.

**Dave Jones:** Were we all? Yes, exactly. Yeah, we're nerds, right? Right, exactly. That's how it really goes. You are, tell us all about where you're from. And who you work for, which is the most important thing, which everyone wants to know.

**Engadget:** Yeah, I'm, well, I'm from the Midwest and all that. I've worked for the past two and a half years at Pebble. It was Impulse before that. And we make smartwatches. You may have heard of us from our Kickstarter project, which was... Tailor project. A year and a half ago. Yeah, a little Kickstarter project.

**Chris Gammell:** Yeah, a little tiny one. But people don't know that, that's a reference to it being the biggest Kickstarter ever, the $10 million Kickstarter project.

**Dave Jones:** Is it still the biggest Kickstarter?

**Engadget:** As of the last time I checked, I know there have been some big ones. It might not be any more, but I believe it is.

**Chris Gammell:** Yeah.

**Dave Jones:** Why do you think that's the case? Is it because this was sort of like one of the first sort of consumer gadgety gear freak kind of projects on there? I don't know.

**Engadget:** It wasn't the first. And we actually reached out to a few that had been on there that were consumer projects, like the Lunatic Watch and the Elevation Dock, which had been a record before us.

**Dave Jones:** But the Lunatic was just a band, wasn't it? It was just a watch band, so it wasn't actually a watch.

**Engadget:** Correct.

**Dave Jones:** Yeah.

**Engadget:** We definitely were able to help build up some hype around sort of Kickstarter becoming more mainstream. And I mean, there was only one chance to do that, and we took it. And that certainly helped.

**Dave Jones:** And what did that involve? What did that hype involve?

**Engadget:** We talked to the press a lot, and even starting out, we arranged an exclusive with Engadget to start the project off. And then, I mean, fortunately, we didn't have to do any really crazy PR management stuff because it was a hot enough story that people were interested. But that helped.

**Dave Jones:** They came to you.

**Engadget:** Yeah.

**Dave Jones:** Right. So did you join Pebble before the Kickstarter campaign?

**Engadget:** Yeah, about a year before the Kickstarter, actually.

**Dave Jones:** Oh, a year before. Right. So tell us who are the founders of the Pebble and why they brought you on board and what was the size of the team and stuff like that. Sure.

**Engadget:** So Eric Mijakovsky is the founder of Pebble. He actually founded the company right out of school. At the time I joined, it was Eric and a part-time industrial designer, mechanical guy, and some interns on the software side. And that was basically it. And so I...

**Dave Jones:** Well, that's still quite reasonable in terms of, you know, a guy straight out of school forming a company.

**Engadget:** Yeah.

**Dave Jones:** Where did the money come from?

**Engadget:** Um... Venture? Well, at the time I joined, yes, because he'd gone through Y Combinator, which is a...

**Dave Jones:** Ah, right. Yep.

**Engadget:** Startup accelerator. You've heard of them. Most... Yep. In the Silicon Valley area, mostly targeted around software startups. But they... It's been increasing lately, but they had been maybe once every six months or a year accepted a hardware startup and Pebble was one.

**Dave Jones:** Right. So you joined about a year before. At what state was the project in at that time?

**Engadget:** Well, Eric had shipped a watch called the Impulse that worked with BlackBerrys, which was a reasonable decision to make back in 2007 or so. The iPhone had just come on the scene, but... Right. But in 2011... But in 2011...

**Dave Jones:** And he did all that himself, did he? Or that was a personal project of his?

**Speaker ?:** Um...

**Engadget:** He'd started it, I think, as a senior design project and then turned it into a company and it had some help. Right. But... But... It wasn't just Eric Solo.

**Dave Jones:** Got it. Hmm. So was that a popular watch?

**Engadget:** It was not all that popular. And the manufacturing runs weren't that big. Right. But even then, we didn't sell out. And that was partly because... I mean, the number one question we got about it was, does it support the iPhone? You're right. And the answer was no. And it didn't even really... One of the reasons I came on board was to make it support Android, which we were barely able to do.

**Speaker ?:** Huh.

**Chris Gammell:** What about... So you said it was a BlackBerry watch to start with?

**Engadget:** BlackBerry compatible, yeah.

**Chris Gammell:** Oh, interesting. I didn't even know... So BlackBerry... Was that still Bluetooth back then as well?

**Engadget:** It was Bluetooth. Hmm. We used open source Bluetooth stack. I forget the name of it. That was originally written as a user mode stack for jailbroken iPhones or something like that.

**Chris Gammell:** Oh, wow.

**Engadget:** And it was running on this really tiny microcontroller, a NXP ARM7 with like 32K of flash and 8K of RAM or 4K of RAM or something ridiculous. Oh, what are you talking about?

**SPEAKER_03:** That's huge. Come on. Well, for a Bluetooth stack.

**Engadget:** Oh, okay. Well, you know. Bluetooth is really a messy, messy protocol with way too much software involved. And so we were able to, like at a very low... Using a very low level portion of the Bluetooth protocol called L2Cap, we were able to communicate with BlackBerrys and BlackBerry apps. But support on Android was limited and iOS non-existent.

**Chris Gammell:** Well, I bet you guys are kicking yourselves for not sticking with BlackBerry these days, right?

**Engadget:** We still get asked when we'll have a work with BlackBerry or Windows Phone.

**Chris Gammell:** Really? Oh, interesting. See, now this is an interesting intersection because, I mean, like the Pebble is such a cool... You know, it's such a, like a... It's a great piece of consumer hardware, right? It's very... You guys are a hardware startup. It's a piece of consumer hardware. It's interesting from the embedded perspective. And yet it's such a... You know, it crosses over into that consumer space where it starts to get insane with, you know, people caring about, oh, what's your phone specs? What are, you know, like specs and all that, you know, all the one-up-a-tree that the big players like Samsung and, you know, all the...

**Engadget:** Yeah, all the stuff that people talk about over on XDA Developers and all that stuff. Exactly. You're right. Exactly.

**Chris Gammell:** Yep, exactly. So, I mean, how has that experience been? Yeah. I mean, what is that like to have to kind of jump into that world?

**Engadget:** Well, it's been interesting for sure. But, I mean, we've tried to keep out of the specs race, right? Like, we don't have a color screen. We don't have a camera. There's no bickering over how many megapixels the camera has because there is no camera. Right. Yet.

**Dave Jones:** Oh, goodness. Let's not go there. Yeah.

**Engadget:** I don't know. I don't know. Someone, one of my colleagues brought in this, like, Casio camera watch from 1997. So, I mean, the idea has been around for a while.

**Chris Gammell:** Yeah.

**Engadget:** But I don't think it's catching on.

**Chris Gammell:** Just waiting for that killer app right after Google Glass. That's the next one.

**Dave Jones:** See, I'm not sure, Andrew, if you've seen my do-it-yourself scientific calculator watch. It was the world's first do-it-yourself. It's hideous. As it says. It's hideous. Yeah. No, it's all right. It uses all off-the-shelf parts. And anyway, at around about the same time, all this sort of smartwatch, well, actually, just before the smartwatch revolution, I thought, oh, yeah, I'd bang in all these features.

**Engadget:** The smartwatch or the...

**Dave Jones:** I don't know the exact timeline, but it was sort of, you know, it was before all of... I think it was before... When was it? I don't know. It was four and a half, five years ago. Like the... What timeline would have that been in? So, four or five years ago. So, like 2009 or something.

**Engadget:** Yeah, that might have been the tail end of Microsoft's SpotWatch stuff. And then there was the MetaWatch that spun out of Fossil.

**Dave Jones:** Okay. Anyway, it was around about that time, you know, I thought, oh, yeah, I'll feature... You know, I was working on my next version. I'll bang all these features in there. It'd have everything, including the kitchen sink, you know. And then, well, all this smartwatch revolution has now happened. And now I'm going, well, geez, there's so many out there. Are there a dime a dozen? No, my next version is going to be just a scientific calculator watch. It's not going to do anything else, damn it. It's not going to have anything else in it. It's just I'm going back. Do one thing and do it right. Oh, that's cool. That's right. Yeah, yeah, yeah. Like the Pebble does, yeah. That's good.

**Speaker ?:** Yeah.

**Engadget:** Well...

**Dave Jones:** That's right.

**Engadget:** Like I said, Bluetooth is really a mess. So, if being a scientific calculator watch means you don't have to deal with Bluetooth, then...

**Dave Jones:** Yeah, exactly. I don't know. And I'll get, like, two years battery life out of it. Sure. I'd see why not. None of this fast processor. The processor will be running at 32 kilohertz, you know, because it doesn't need to go any quicker. And nah, screw everything else. And yeah, it's like a real watch, you know. Well, I'm old school, you know. I want my watch to have, you know, at least a couple of years battery life. Thank you very much. I don't want to have to charge my watch. Goodness. I'm having a hard enough time remembering to charge my mobile. Wow.

**Engadget:** Yeah, that's the dream. So, what's the battery... Right. We try to at least do a little better than a phone. So, you can get a week out of a pebble. But yeah, it's not the same as an analog watch where you can go three years or more.

**Speaker ?:** Yeah.

**Dave Jones:** Right. Was there... How much effort went into power consumption of this thing from the get-go?

**Engadget:** It's one of our biggest concerns, definitely, when I'm speccing parts, when we're doing software design.

**Dave Jones:** Was there any feature trade-off, like going, no, battery life is more important. We're not putting that feature in because that's going to kill the battery life.

**Engadget:** Well, the Impulse, our first product, was actually a color OLED display. Oh, right.

**Dave Jones:** How many hours did you get? Like, hours, not days.

**Engadget:** I mean, even with the display off, there was some other stuff in there that was burning power, and so you only got maybe two days. But definitely, if you wanted the OLED to be on, you're talking hours.

**Dave Jones:** Right. And the pebble gets, what, a week?

**Engadget:** Yeah, a week, five to seven days. Is that with the screen permanently on? With the screen on all the time and updating even once per second.

**Dave Jones:** Because it's an e-ink display, isn't it?

**Engadget:** No, it's not an e-ink display, and there's a lot of confusion there.

**Dave Jones:** Let's talk about the screen technology. Yeah.

**Engadget:** Go for it. So, the screen we're using is, we call it an e-paper screen, and we think that's a pretty good way to sort of describe the characteristics. It's on all the time. It's black and white.

**Dave Jones:** Oh, it's a sharp memory?

**Engadget:** But it's the sharp memory LCD, and I don't know if you've experienced with those.

**Dave Jones:** Yes, I'm going to use that. Yeah, I've got some. I've done a video on it. I'm going to use it in my next watch as well.

**Engadget:** Yeah, it's really cool. And one of the things that's cool about that display is, for a small volume electronics designer, displays seem to be one of the most difficult types of components to source and work with.

**Dave Jones:** Oh, yeah.

**Engadget:** But the sharp display, you don't need an NDA to get the data sheet. You can buy them off Mauser, at least when they're in stock. At least in terms of displays, for a fairly advanced and unique display, it's pretty easy to work with in small volume.

**Dave Jones:** Yep. And what frequency are you actually running it at?

**Engadget:** So the display is pretty unique in that because it's memory in pixel, there's no controller. You talk spy directly to the glass. And everyone who I talk to... Oh, you said you're updating once per second. We can update once per second. We can update, I think, 25 or 30 frames per second. And we do during animations. Right. Oh, interesting. There's no fixed frame rate. It's dynamic because of the fact that it's got this memory. And you can even do partial refreshes and so forth.

**Chris Gammell:** So you said it's called memory in pixel? What is that? Memory in pixel.

**Engadget:** I mean... So they fabricate it using a TFT process, but your standard TFT array just has one transistor per pixel. And so you've got to constantly refresh it because the pixel is a capacitor and there's leakage and so you need to refresh it. Oh, like DRAM. Yeah, kind of like DRAM.

**Chris Gammell:** Yeah.

**Engadget:** A really crappy DRAM, but one you can see. Right. But the Sharp Memory LCD actually has an SRAM cell in each pixel.

**Dave Jones:** So once you set the data to it, it just stays there.

**Engadget:** So once you set the pixel, it stays there. Interesting.

**Dave Jones:** So you don't have to update it. You can put an image on there and then it just requires a static current to keep the... Correct. ...to keep the information there.

**Engadget:** Right. So it needs a one hertz clock because you have to invert the polarity of the voltage on the liquid crystals because liquid crystals don't like a DC bias, but that's a pretty easy requirement to satisfy.

**Dave Jones:** And it's pretty low power too at one hertz.

**Chris Gammell:** Yeah. Did you guys see that video that Ben Krasnow made about LCDs?

**Dave Jones:** Making your own LCD. Yeah. Yeah. That was great. Yeah. Yeah, that was brilliant.

**Engadget:** No, I don't think I saw that one. That sounds good.

**Chris Gammell:** It's... It's... I really had never seen how... I guess I never understood how they work before. Just like the whole... The etching process and everything like that. I mean, with... I'm guessing with this sharp thing, it's an actual, you know, a static... There's like a square pixel or something, right? I mean, it's not like a defined element like old seven segment type LCDs were like, right? Right.

**Engadget:** Well, that's the distinguishing factor of the, you know, a TFT array LCD where you've just got an array of pixels that are square versus... Huh. Like the seven segment LCDs, it's sort of like each segment is a pixel and they have the shape.

**Chris Gammell:** Right. Exactly. Yeah. They're just... Yeah. They're just odd. They're not square. Right. Do you know, like the current... I'm guessing you probably live and breathe this stuff and it sounds like Dave's dealt with as well, so I'm kind of on the outside here, but what kind of like current is it just to hold it on with that one hertz inverting? It's like 10 microamps or something.

**Dave Jones:** Yeah. I thought it was around about five. Yeah. There's a couple of modes. There's a couple of... I think it can be as much as 15 or... Yeah.

**Engadget:** But annoyingly, it's a five volt part and so we actually... Yes. Yeah. We burn more current in the inefficiency of the boost converter than the display actually consumes when it's static.

**Dave Jones:** I know. I've had the same issue I wanted designed in. Of course, you want to run it on a single coin cell. Right. You know, three volts down to 2.7 minimum. Yep. And well, you can't. You've got to have that bloody blasted boost converter.

**Chris Gammell:** You've got to double stack them now, right? Oh, man. Yeah. Yeah.

**Dave Jones:** I know. Yeah. You've got to double stack your battery. So was that... At what design... How did you decide whether or not you went for... I presume it's a single coin cell to power it?

**Engadget:** No, it's a lithium ion polymer pouch cell. So the kind that's like 4.2 volt cutoff and then 3.7 roughly in the flat region.

**Dave Jones:** But did you... So what... How much angst went into the design decision to go for a single cell or a dual cell battery? Because if you went for the dual cell, then you wouldn't be... You could power it without the boost converter.

**Engadget:** We could, but there was really no question in terms of the overall cost and complexity of the battery system. And the fact that...

**Dave Jones:** And then you've got the charging and the management stuff like that.

**Engadget:** You've got charging and charging is a lot harder because you mean you can use a linear charger to charge a one cell battery from USB and you need a step up charger to charge dual cell battery. And the extra mechanical complexity of having two cells means you're wasting more internal volume.

**Dave Jones:** Uh-huh. Yes. It's all a big trade-off. Weight as well. Yeah. Yeah. So from the get-go, you pretty much just went, oh, well, we've got to have a boost converter and we'll... Right. There's more benefits to using a single cell lithium battery.

**Engadget:** So we put in the boost converter. We put in a level translator to be able to talk to the display from our MCU. Oh, yeah. Which is down at 1.8 volts. Right. There's not a... It's a bastard, isn't it? Yeah. Minding a boost converter that is not designed for like double A's and therefore has the input voltage range we need. Mm-hmm. Um, and that is, is efficient at incredibly low loads of five or 10 microamps or whatever the display is. Um, there aren't too many out there. So that was a, I mean, a lot of, a lot of designing something like this comes down to shopping for components. And that was one of the trickier.

**Speaker ?:** Oh, yeah.

**Engadget:** Yeah. That was one of the trickier, um, shopping exercises. Um, it turns out we have, it turns out we have, um, excess output current capacity on that boost. Um, as I suppose you might expect given the low demand of the display.

**Dave Jones:** Yeah, exactly. It's unsurprising.

**Engadget:** And so one of the happier things that happened in the design was that we were able to also use that five-volt rail, um, for the white LEDs.

**Chris Gammell:** Oh, nice. For the backlight. For the backlight. Right. Yep. That's good. You should have, uh, put in like an optional taser or something as well, you know? Optional taser.

**Engadget:** We actually had that request on the forum. A user was concerned that the vibration of the, the vibrating motor would not be strong enough to get his attention. So he wanted a built-in taser.

**Chris Gammell:** Oh, my God. You never know. Those kind of things, they can, they, they can turn it into an even more breakout product.

**SPEAKER_03:** The watch that zaps you awake. That would be terrible.

**Dave Jones:** In my scientific calculator watch, I just, um, I needed five volts for the LCD as well. And five volts for the backlight LED as well. Same as this. And I just, um, I went, oh, bugger it. I'll just, uh, generate a PWM signal on one of the, uh, micro pins and just use that as a doubler. And well, you know, it, it worked. But efficiency. Right, right.

**Engadget:** Now you can't put your micro into the low power modes. Yeah.

**Dave Jones:** Yeah, exactly. But it didn't matter because my LCD was, uh, you know, reasonably high power that I had to switch it off anyway. So I'd stay on for five minutes and switch it off. So it was, it was a different ball game.

**Chris Gammell:** Got it. Did that end up affecting you at all? You know, because it's got a boost converter on there and those, not saying it would be, but it could be a little noisier because, you know, you're slamming current around. Did you have any, um, you know, EMI testing problems at all? Or what, what, what happened when you got to that point?

**Engadget:** No, I mean, EMC is, we're dealing with in the grand scheme of things, such small currents. And the board is so tiny. It's like two by one centimeters or something. So there's inherently any loop on there is going to be tiny. Um, and of course with reasonable layout, it's really, really tiny. Um, and so we, EMC has not really been a challenge for now. Antenna performance has been a challenge, which is a whole nother story, but EMC hasn't been too much of an issue for us. Right.

**Dave Jones:** And what was, how much grief did you go through to pass FCC compliant? What, what sort of compliances did you have to pass to sell this worldwide?

**Engadget:** FCC and CE are the big ones. Yep. Um, and obviously the requirements are a little bit different. Um, for us that all sort of gets abstracted away. Um, we have our, we have our manufacturing partner kind of run the show there. And obviously we tell them what certifications we need to get, but they just engage a testing lab. We send it off, we give the, talk to the testing lab and give them whatever software they need for getting it in the special modes where the radio is off or transmitting a carrier wave on what such and such channel or whatever. And then they do the testing and get a binder and it's all pretty. That's awesome.

**Dave Jones:** And it passed and you, and you didn't have to re-spin anything?

**Engadget:** Um, not for compliance. No, we didn't. So we, we lucked out there.

**Chris Gammell:** That's great. First shot and done. That's, that's, that's the dream, right?

**Engadget:** I mean, I wish I could say that about the antenna performance. Yeah. So what, what compliance we did. Okay.

**Chris Gammell:** What's up with the antenna? Because if people don't know the blue, the, it does have Bluetooth on there. Are there, are there any other RF modes? I didn't think there was anything else.

**Engadget:** No, it's just Bluetooth. And I mean, a simple RF is definitely good in terms of size and battery life.

**Chris Gammell:** Yeah. Yeah. Right.

**Engadget:** But we started, um, we used a pre-certified, um, Bluetooth module that already had an FCC cert so that we just, we would just need to get the part B, which is the thing that any device has to have. And then the part C, I believe, which is the, if you're an intentional emitter, um, which you are, which we are, then we were able to, we are. So the, the theory went, we'd be able to use the modular certification of this module that we were using. But to use the modular certification, you need to use one of the pre-approved antennas and the manufacturer of our module had approved, um, a couple different ceramic chip antennas.

**Dave Jones:** Did you have any issue with, um, you know, absorption by the person's wrist and things like that? And the orientation? Yes.

**Speaker ?:** So here's the thing.

**Engadget:** So we've got this little ceramic antenna. It's designed to perform on such and such a size of board because it needs, it needs a ground plane. Yeah. Um, and we didn't have that. And we've got, we've got wrapped around the outside of the watch. There's this flexible circuit, which has basically connection for all the buttons. Um, you've got the display on the front, which there's a bunch of layers in the display, but for our, for 2.4 gigahertz, it's basically a sheet of metal.

**Chris Gammell:** Yeah.

**Engadget:** Um, and then you've got the person's arm, which is like a bucket of water. It's hugely absorbent at 2.4 gigahertz. Um, like that's the reason they use 2.4 gigahertz for microwave ovens, right? Is that like water is hugely absorbent at that frequency. Um, so you're basically in this cage and the ceramic antenna performance was really poor. And, um, we went through a few iterations of that and worked with the antenna manufacturer. And then we said, you know what? We need to just do our own antenna design. And, um, we didn't, we didn't, we didn't do it ourselves. We had an outside office actually do the design.

**Chris Gammell:** That's business, man. That's business.

**Engadget:** That's how it works. Yeah. Um, but we ended up doing a printed antenna. Um, it's actually on that flexible circuit board. And then there's like a little pogo pin or something that makes contact from the main board to the, where the antenna is on the flex board. Wow. Sweet. And it works decently well. It's, I mean, it's still in terms of, um, there's like a 10 dB loss or something on the antenna, which is really not what it's, yeah, it's not great, but it, it works pretty well. And people are reporting, you know, 30 meters of, of Bluetooth range, which is pretty good.

**Dave Jones:** Because it's really just designed to couple to your phone. Right.

**Engadget:** And so if you're wearing the watch and you're carrying your phone in your pocket.

**Dave Jones:** Yeah.

**Engadget:** Yeah. It's fine. And we can even back down the transmit power.

**Dave Jones:** Even if your phone's in your back pocket and your watch is swinging your arm. You're doing a pull up. Yeah.

**Engadget:** So when we're testing the performance, like you do all the lab testing and you get the antenna characterization and you make sure it's your radiation patterns look good and so forth. Um, but then you do real world testing too. And you do range. But one of the important ones is cross body. So you've got the phone in the back pocket and the watch out in front of you, making sure that the performance is still good.

**Chris Gammell:** With the meat shield in between. Exactly.

**Dave Jones:** Now, does the watch periodically ping the phone or vice, the app or vice versa so that you, so it can tell you it's out of range?

**Engadget:** Yes. So at the application layer, that's a fairly slow period. Right. But at the lower layers of Bluetooth, um, there's some more frequent exchange going on.

**Dave Jones:** Right. So, so the watch knows it's out of range. Does it tell it and show you on the screen going, Oh, I'm, I'm out of range.

**Engadget:** On the phone screen. Yes. On the pebble screen. Um, no, but in, um, the, the latest version of the SDK, we've made that available as an API to some app developers so they can make an app that tells you whether you're connected to your.

**Speaker ?:** Huh.

**Chris Gammell:** Well, that's an interesting, uh, that's an interesting route as well. I'd like to talk about is, is the SDK. Cause you, you mentioned for the show that you guys are getting ready to launch the next version of it or, but even, even just having one out there already, I'm, I'm interested in kind of that dynamic between, you know, you're the hardware maker, you're got this product with like firmware ready to go. And then you got people screaming at you to upgrade it and they want to develop apps. And you're building a platform at this point. What, what is that experience like as a hardware designer?

**Engadget:** Well, I mean, at the level of choosing hardware, it's mostly about, okay, how much memory, how much CPU performance do we need? What else do we need to, in order to, you know, enable it to be a platform? And one of the decisions we made that you might think is a little bit contrary to being a platform for third party software is choosing a microcontroller as opposed to, um, like an ARM Cortex A microprocessor, um, as the platform. That's a power thing, man. It's a power thing.

**Chris Gammell:** Yeah.

**Engadget:** Um, fortunately those all have, um, memory protection units. So we can use that. I mean, it's not the same as virtual memory, but we can use that to sort of sandbox the third party apps.

**Chris Gammell:** So what, I, can you explain that to dumb analog guy here? And of course any of our dumb analog listeners as well. We don't want to forget them. Okay.

**Engadget:** Um, so there is a device, a peripheral device in the microcontroller that we can turn on. It's called the memory protection unit. And basically, um, it sits on the memory bus and it throws an interrupt, um, whenever you access an address outside of a certain range or group of ranges. Um, and then the interrupt handler, which is kernel code, um, can deal with that basically by killing the offending, uh, app, which in our, we're using a free RTOS. So, um, apps run in a free RTOS task that's configured to have sort of low privilege and the memory protection unit turned on and we can kill that task if things go haywire.

**Chris Gammell:** Huh? So does that mean that your, your developers, you have, do you have two different levels of developers, some writing apps directly for the pebble and then some writing like, like phone side applications? Yeah.

**Engadget:** So that's another thing we offer is just the ability to, especially on Android where you have the intent system on Android, um, but also with iOS, um, the ability to just make a phone app that interacts with the pebble. Um, so some people do that, but obviously the big, really compelling thing is to write native apps for the pebble.

**Chris Gammell:** Yeah. That sounds really different though, too, because I mean, I, like, like you said, it's not quite an app market, or at least it's different than how I think of app stuff, because I think of, you know, large marketplaces where people are writing high level programs and stuff like that. But, you know, you guys have like a firmware market. That's actually really different than anything I've ever heard of before. That's, that's kind of.

**Engadget:** Well, we like to compare the device in terms of the horsepower and graphics and so forth to, um, like the original Macintosh. I mean, even down to them both having 128k of RAM. Um, it's a nice, neat comparison. Uh, or the early PDAs, Palm and Newton and that stuff.

**Chris Gammell:** Well, it would just be great if I could get like someone in the actual Android app development market not to be like, yeah, I'm going to use all your phone's memory. So, you know, it'll, it'll come back in a couple of minutes. Don't worry about it. If you get, if you get like three or four developers, like thinking about memory management and stuff, I'm happy. Yeah.

**Dave Jones:** Now with the, um, campaign, you originally asked for a hundred thousand goal and that was, I don't know what a, you know, a couple of thousand watches, maybe something like that. You ended up getting a thousand, right? Yeah. Nice round number. You ended up getting 10 million bucks and, uh, selling like, well, having 60,000 or so, uh, backers wanting watches or more, I think. Um, how did that change your game plan from, you know, because there's a whole different, there's a whole different game plan from going for manufacturing a thousand watches, which you can almost, you know, do, you know, almost by hand, um, to doing 60 odd thousand.

**Engadget:** Right. So we had actually originally the game plan to sort of go into full mass production and go overseas and so forth. Okay. Um, back when we were trying to raise venture capital. Um, and when that fell through and we went on Kickstarter, we said, you know what? We don't have to do that. We think that we could pull off, um, local at home manufacturing, not literally in our garage,

**Dave Jones:** but we, um, we had a, we had a prototype shop that we worked with, um, here in California.

**Engadget:** Um, we still like them. We still use them for prototyping stuff, but we thought that, okay, we can, we can pull off manufacturing a thousand of these things locally. But of course, when the Kickstarter blew up, um, we said, no, that's not going to cut it anymore. And so we, we had met, um, Dragon Innovation. I think you had Scott on the show earlier. Yes, we did. He was great. And we called them back up and said, Hey, we're going to need you guys to help us out with, with overseas manufacturing.

**Chris Gammell:** Hey, we got this bucket of money now. Right. Help. We can afford you now. Right, exactly. And we need some help. That's what buckets of money are great for, actually. Yeah. Making things happen.

**Engadget:** Yeah. I mean, the product had been designed around, um, mass manufacturing upfront. And I, that's one of the things that can break your Kickstarter if you're not expecting it. And there's also, we managed to raise enough money that we avoided this sort of zone of pain that a lot of Kickstarter projects get into where you can't build them in the garage anymore, but you're not really interesting for a contract manufacturer.

**Dave Jones:** Uh, so you haven't got quite enough money to go elsewhere and you end up being screwed. Yeah. You're in a world of hurt.

**Engadget:** Yeah. So we, we got lucky there to be able to just bypass that.

**Chris Gammell:** Speaking of world of hurt, uh, so I take it that means that you also worked in a, a ticket to China with your, uh, you got a complimentary flight to China. Is that, is that correct?

**Engadget:** Um, as part of the process, 10 or 12 tickets to China, way too many. It's fun the first two or three times and then it just becomes a drag. Yeah. But trying to do it without going over there and just totally hands off. No, that's impossible. I wouldn't want to do a, try and do a project that way.

**Dave Jones:** Even, even for simple things, it's, it's just not possible. It just blows up in your face every time. Yeah.

**Chris Gammell:** So, uh, I, I, I remember people were all up in arms about that. Like, Oh, my watch is late, but I remember seeing it. I think we even talked about it on the show. We're like, there's, I mean, that is a ton of watches, right? I mean, especially from, from starting from scratch. I mean, so what, what were some of the challenges you had when you were, when you were getting started up over there?

**Dave Jones:** Well, first of all, how late were you? Well, in terms of you, the absolute first one you shipped out.

**Engadget:** So the date, um, that we promised on the Kickstarter was September. Um, and the first unit out the door was, um, mid January. So in terms of lateness of Kickstarter, I mean, we missed Christmas and we were really beating ourselves up over having missed Christmas, but there was really no way we could have shipped everyone's unit before Christmas. Right.

**Chris Gammell:** Right. Plus they bought them in like what? March the year before or something like that. It's like, it's not like people thought it was going to be a Christmas present. Did they?

**Engadget:** I think some people did and I, I feel for them, but in terms of lateness of Kickstarter projects, three or four months is not that bad, but was disappointing.

**Dave Jones:** No, it's not that bad.

**Engadget:** What was disappointing was how long it took us to, um, sort of ramp up the manufacturing line and get to a full production capacity and be able to ship all 85,000 units that got bought in Kickstarter. That took a number of months after January.

**Dave Jones:** So how long in total from the end of the campaign to the first shipment?

**Engadget:** From the end of the campaign, end of campaign ended in June.

**Dave Jones:** June. Right.

**Engadget:** And the first shipment was in January. So six months.

**Dave Jones:** Six months. Okay. Well, that's still not too bad. I was going to say, for those who don't know.

**Chris Gammell:** I'm a non-consumer and that seems like, wow. It's like industrial. That'd be like, oh, okay, well, here's your bonus.

**Dave Jones:** Well, see, that's the thing with the modern consumer world. People are used to the buy it now button on eBay, right? Or, or Amazon, you know, buy it now. It's in stock. This, you know, waiting six months for, or 12 months. So some of them are two years behind. They take to finally ship. I mean, it's a different world. Right.

**Engadget:** I mean, even some of the components that are in Pebble, you've got lead time of three or four months. And so like we placed orders right for, for components for production quantities right after the Kickstarter ended. And I mean, you're like, do we really want to lock in the design that soon? Well, we have to, because that's what the lead times are.

**Chris Gammell:** At least this little part right here.

**Engadget:** I think there was even a photo in one of the Kickstarter updates of Eric signing a PO for a million dollars for the screens or something. Oh, wow. Nice.

**Dave Jones:** I'll have to dig that out. Yeah. And link that in.

**Engadget:** Yeah.

**SPEAKER_03:** Wow.

**Dave Jones:** Well, I'm about to do a Kickstarter this month from a project in which I'm reintroducing, but I've had to buy because some of my parts are hard to get and long lead time if I don't buy them now. So I've had to commit to like, you know, I just paid 4,200 bucks for a reel of bloody components because if I don't get them, I'll be screwed and won't be able to, to, to fulfill the campaign. So I've got to make those decisions and spend money before I even start. Yeah. Yeah. Because, you know, I don't want to do a Kickstarter campaign and then promise, oh, sorry, I'll deliver in four or five months time. You know, I don't like that just from, you know, I want to do it now.

**Engadget:** Yeah, certainly if it's feasible to deliver sooner, then why not? Everyone, that's good for everyone. Yeah, of course. Less hanging over your head and the buyers get it sooner.

**Dave Jones:** That's, that's the thing. And I don't want to deal with the, the complaints and the requests for updates. How did you have to deal with that? Not personally, but as a company we did.

**Engadget:** And it's, um, Sarah, um, who at the time, uh, was our sort of our sole customer support person. Oh my gosh. Personally, personally answered. Um, I think 50,000 emails over the course of like three months.

**SPEAKER_03:** That's, let's take a moment of silence for, was it Sarah you said? Yes.

**Engadget:** That is, that is admirable and terrifying.

**Dave Jones:** Uh-huh.

**Engadget:** It really is. And our support team, now that we're shipping and we have actual like technical support issues, that's, um, right. One of the faster growing areas of the company.

**Dave Jones:** Yep.

**Engadget:** Man.

**Dave Jones:** Oh, that is, that is painful because, uh, everyone thinks, oh, look, I'll just, you know, and, and the emails always start with, oh, look, I don't want to, you know, waste your time, but, oh, quick. Can you just give me a quick update? And, you know, and it's like, because people think, oh, nobody else will do it. You know, I'll be the only one. No.

**Engadget:** And Dave, you probably know, you'd probably know better than I, but is the Kickstarter kind of built in private messaging system still really awful in terms of the user interface? I remember it being like 10 messages per page and there was no way to navigate between the pages.

**Chris Gammell:** Oh, man.

**Dave Jones:** As a, as a, uh, producer, I haven't used a Kickstarter yet because it's only just arrived in Australia. Okay. I've used the Australian version possible, um, which was, yeah. I mean, my campaign that I ran on there broke the possible system. It just, you know, they just couldn't handle it. It didn't work. Um, so they, they had to fix it all up and yeah, it's not good. I've heard Kickstarter is not that great either for interaction. The backend is pretty bare bones.

**Chris Gammell:** All people care about is the money up front, right?

**Dave Jones:** Well, how, how hard was it just to extract, uh, people's shipping information? For example. I mean, for me, when I ran my campaign for my rulers on possible, that was the number one thing. And that's what broke in the system. I couldn't extract all everyone's mailing addresses in a usable format.

**Engadget:** Well, Kickstarter didn't even have a mailing address feature. They had this one, like you had one time you could send out a poll. That's what they called it. A poll to all your backers and have them submit information. And we said, you know, we aren't even going to do that. We just, we just built actually a web application to manage all this because we would have had thousands of people like requesting to change their address. And okay, if you've got a thousand backers, you can deal with manually changing people's addresses. But for us, like that wasn't even feasible. So we built a web app to just let people put in all their information.

**Chris Gammell:** That's kind of nice too. Cause then it kind of is built in your, your starting of your community then as well. Right. It's like the people that are going to be developers and stuff like that. So exactly.

**Dave Jones:** Well, I do, I do hope that's been fixed. Cause I'm about to use Kickstarter and give it a try.

**Engadget:** Yeah. The last project I backed, I just backed the, um, the laser cut catapult thing. Uh, that ended a couple of weeks ago. Um, so that's the most recent thing I've backed on Kickstarter. Uh, and it did, they did add actual shipping address fields.

**Dave Jones:** Right. Ooh. Okay. I might think twice. Maybe I'll go back to possible. At least it's, uh, they've ironed out all the issues with my last campaign. So maybe I should stick with that. Yeah. At least I know it works, right? It's a known quantity.

**Engadget:** Kickstarter is a hype machine.

**Dave Jones:** It's a hype machine. Yes. That's it. Uh, and, um, before, uh, what do you think about the changes that they made? I think it wasn't a result of your campaign, but the result of, um, they would never say so, but yeah, but there were a couple of projects, um, uh, that pushed them over the edge to where now you can't start a Kickstarter campaign unless you have a real prototype you can show. Right.

**Engadget:** So the Lockatron guys, which they're good friends of, of ours, um, just down the road. Um, they were sort of the first Kickstarter campaign to get rejected under the new rules. Although Kickstarter told them it was actually the old rules. Um, apparently you can't put home improvement devices on Kickstarter. Um, really?

**Dave Jones:** Why is that?

**Engadget:** I don't know. I, I really don't know. But anyway, they, they, I guess like some sort of like super insulation or something. Right.

**Dave Jones:** Um, free energy thing or, you know, yeah. Right.

**Engadget:** But anyway, they, um, rather than going on Indiegogo or something like that, they made this thing called self-starter where they just use their own website to, um, get pre-authorizations on, on, um, Amazon payments, which is the payment back end that Kickstarter uses. Um, and they had success with that, although they had another source of funding. And so they were able to defer actually collecting the money until shipping, which probably helped bolster people's confidence to do something that wasn't one of the established crowdfunding sites.

**Dave Jones:** Yeah, that makes sense because it's all a trust thing, right? If, you know, some unknown person, you know, pops up with their campaign, it's well, well, you know, how do I trust these guys? But most people don't seem to care. I mean, I've seen campaigns that have gone. Right.

**Engadget:** And Kickstarter is pretty hands off to themselves. Like, I mean, theoretically they're there to resolve issues, but they're pretty hands off.

**Chris Gammell:** You thought 50,000 emails was bad, right? Yeah. Imagine how many Kickstarter get. Yeah. Oh, that's, that's messy. Oh, speaking about funding. Have you guys, have you guys picked up any other funding since? I thought I remember seeing some. We did.

**Engadget:** We raised a $15 million venture capital round, um, this spring. Wow. That's impressive.

**Dave Jones:** That means you guys aren't calling the shots anymore. No, that's not necessarily the case.

**Chris Gammell:** No, that's not necessarily the case, right? Not necessarily the case. Did you have to, did you have to go on like those, uh, I've only heard stories about that whole funding dance, the dog and pony show. Did you have to go along with that also?

**Engadget:** I've heard some stories too, but I did not. I'm an engineer.

**SPEAKER_03:** I didn't have to do that.

**Chris Gammell:** Sweet. Excellent. Yeah. Excellent. I know this is backtracking a little bit. I wanted to ask you about, uh, China a little bit more because, you know, you mentioned the, the, the part reels, like the 40, the four months rather of, of lead time and stuff like that. And I think that actually what it kind of fell in that one, there was that one period where there was lead times went, went to like 28 weeks for a lot of parts. I remember it was really crazy.

**Dave Jones:** It was 40 back in the day. Yeah. If you were, if you were doing stuff back in the early nineties, 40 weeks was a typical lead time.

**Chris Gammell:** This is not the nineties I'm talking about, David. It was recently.

**Dave Jones:** There was, there was, there was a lead time thing. When I was a boy. Yeah.

**Engadget:** I mean, it varies based on class of components too. Um, we haven't really had any lead time scares. Um, I mean, there's been a few close calls. Um, and some of our lead times do get to be fairly high. Um, you know, four months. Plus, but yeah. Um, which is what, 16, 18 weeks, but yeah. Yeah. Um, never to the point where we've had really, um, a supply chain issue shut down the line, which is, that's, that's pretty good. We've been lucky there.

**Dave Jones:** That means your planning's pretty good. Yeah.

**Chris Gammell:** Yeah. I think it was Zach, um, Smith Hoken. Um, I think he was talking about it and maybe other people have as well where, you know, we always talk about like, you know, you're designing prototypes over the world. And you even mentioned that, you know, you can get that sharp display off a Mauser, but then you go over to China and there's just like all these no label parts or, you know, you can get the parts, but they're not necessarily easy to get them. Genuine. Yeah. Well, not even genuine. Yeah. There is that too. But even, even in the best case scenario that, you know, it's just like the, the supply chain is set up differently than, you know, a, a distributor in the state side, you know, like an arrow or an Avnet or something. Yeah.

**Engadget:** So we actually work with Avnet. Um, and they, we buy from Avnet and get take delivery in Hong Kong or something like that. Um, and for some of the, for some of the components and then some, um, our manufacturer sources directly and they've got their own supply chain, especially for like resistors and capacitors. Yeah. They've just got their approved vendors or whatever.

**Chris Gammell:** Yeah. I always wonder about where that, where that balance point is, you know, because there's always going to be like, like if you design in like some specific TI part, right. So you probably could get something similar, but then you got to play the data sheet game and do all the, the revalidation of components and stuff like that. And I just imagine that would be a really difficult thing if you aren't just living there. I mean, right. I mean, it sounds like you were living there for a little while, but close to it.

**Engadget:** Yeah. Um, but yeah, we specify for, especially for Silicon, but other components as well, exactly what they are, what the manufacturer should be. Um, and some of them we actually then just buy from Avnet or from the manufacturer and give them to our factory.

**Chris Gammell:** Gotcha. Okay. So that's, yeah, that is, that's kind of what I was wondering about is that the ones you really care about, you, you, you take, you take extra care to get them there.

**Dave Jones:** Whereas I, you know, an 0603 10k resistor, you just let the factory, you know, source that for as much as possible.

**Dave Jones:** Right.

**Engadget:** Like I want at least telling, tell me what your approved vendor list is. Give me the data sheets for all of them. So I know roughly what's going into the product. Yeah. But ultimately it doesn't really matter if it meets your specs, it's probably good enough.

**Chris Gammell:** At a certain point, the stuff's just going to stop working if it's not right. So you always got that going. Well, it's digital.

**Engadget:** And like, and during pre-production, I mean, we say, okay, if you're good, you've got three resistor vendors, you know, build a third of the units with each. I mean, it's not perfect. It's not, it's not perfect science, but.

**Chris Gammell:** No, it's manufacturing. Yeah, exactly. What about, what about the test side of things? I mean, I mentioned the, you know, catching it in tests, but how extensive is your test set up and did you have any involvement in that?

**Engadget:** We did have involvement. So it's for such a tiny board. Pretty much, we have to rely on functional tests a lot and say, you know, we're not testing every node. We just go, okay, if everything works, then it's good. So we do, we do a test step after SMT and the code is burned on. Actually, I think it's at part at the same workstation where they, where they flash the firmware. They do some testing and make sure all the voltage rails are good and make sure that the buttons and everything works. And then as part of the, the factory firmware image, there's some stuff to do a self-test test of the memory and the accelerometer and all this other stuff that's self-testable.

**Dave Jones:** And that's still at the bare board level?

**Engadget:** That's still at the bare board level. And then there's some more tests sort of along the way as it's assembled into a complete watch and to make sure that you're like Bluetooth performance. So, I mean, the antenna is not part of the bare board. So after the antenna is assembled, then they, they put it in an RF test chamber and, and measure the output power and make sure that's where it should be. And they, even the waterproofing of the physical unit, they test for every unit to make sure it doesn't leak.

**Dave Jones:** Oh, every unit is actually pressure tested.

**Engadget:** So initially when we're ramping up the line, they actually pressure test it underwater. Um, and then to increase throughput, once they're pretty confident in the process, they actually use a pressurized air test. So at least you don't, aren't getting the units wet.

**Chris Gammell:** We had, we had 10 failures. So we'll be by the hair dryer.

**Dave Jones:** Are there any plans to, you know, because once you're, you build up confidence in your manufacturing, um, you know, chain there, is there any, uh, chance of removing some of those tests and optimizing things? Because look, you know, you've, we've made a hundred thousand watches and we've had, you know, only 0.0001% fire at this step. So you can sort of eliminate that step as there, to save time and right.

**Engadget:** I mean, there's some stuff that you do during pre-production that you wouldn't even do once production starts like x-raying every board, right? You mean you wouldn't do that? Of course.

**Dave Jones:** Right. Yeah.

**Engadget:** Um, but even with, uh, with Bluetooth, right? So we, we do an RF test, um, at the board level, and then we do an RF test, um, on finished goods and the Agilent test that runs that box. It's like a Bluetooth test or in a box or something. It's like $40,000. So there's a lot of capital costs associated with doing that test.

**Dave Jones:** All right.

**Engadget:** Yep. And so we said, okay, if the pass rate's looking pretty good, why not just drop the one at the bare board stage and just rely on the finished goods test?

**Dave Jones:** Because that's, you know, that's a very common thing to do, to optimize that is to look at your continually look at your production, uh, yields and, and figure out where you can optimize stuff. Yeah, definitely. Yeah.

**Chris Gammell:** Everything goes to the bottom line cost eventually. Right. That cost hurts too. It feels like, I mean, I know, I always know that like, okay, I get it. It's good that like my boards work, but it's like, come on, they're doing so good. Just turned on the test a little bit. And that's when it bites you. Yeah. So this has been, I mean, you guys are making a lot of watches. I guess the question, actually, so one of the questions we had on Reddit and actually a question I always have about this because, you know, Dave talks about his watches as well. Um, how do you, like, do people still wear watches? Like, I, I just use my. I love my watch, dude. I know. I'm just saying in general, like I know fashion. I don't understand fashion and like functionally, a lot of people are used to it from, uh, you know, just having watches.

**Dave Jones:** Yeah. I, I feel naked if I go out without my watch.

**Engadget:** I definitely had a phase, um, in my younger days when I was like that. And then I, I gave up wearing watches for a while, a year, I really not too long before I started, um, working on watches. And of course now it's an occupational hazard. Well, I wear a watch every weekday. I don't always wear my pillow on weekends to be completely honest.

**SPEAKER_03:** Um, you get home, pour yourself a drink, take off the watch. No, it's not like hanging on the wall.

**Engadget:** Charge it. Oh my God. No, that's only once a week. That's right. Only once a week, Dave. Right. I went through a lot of blood, sweat and tears to make it. So you only had to charge it once a week. That's right. Once a week.

**Chris Gammell:** You have like a little ritual every week. You're like, all right, this is it. This is, this is my hard work manifest.

**Engadget:** But in terms of people seem to want electronics and alternative form factors, and that includes wearable. And for us, it's about what are people going to adopt now and not some super futuristic thing that they're going to sort of think they want, but not actually wear because it makes them look too nerdy. And my Google Glass is right next to me.

**Dave Jones:** I heard you say that. For me, it's about having the right tool for the job. Right. Right. The optimized tool for checking the time and doing a stopwatch and looking at what day of the week is it? You know, what's the date? Nothing beats a watch. Right. Right. Having to whip out your phone is just stupid. Same with a calculator. Right. My office is littered with physical calculators. I have them, you know, one calculator every square meter, right, of my office space so that I don't, I can just reach for it. I don't have to use a stupid Windows thing. I don't have to get out my phone and call up the calculator app and that sort of crap. Right. They're non-optimized.

**Chris Gammell:** Your TI-83 emulator on your Android cell phone. Yeah, exactly.

**Dave Jones:** You know, my Casio or HP emulator. I don't want that garbage.

**Chris Gammell:** Right.

**Dave Jones:** It's just, no, the right tool for the job because it's optimized. It's like a solar power. The battery never runs out for 20 years. Right. It's always there. I know it's instant on, ready to go. My watch is there. All I'm going to do is twist my wrist and bang. You know, there it is.

**Engadget:** Yeah. We think it's the right form factor for the job and it's a form factor that a lot of people are used to and maybe not everyone is currently wearing the watch, but we think it's a form factor that a lot of people like.

**Speaker ?:** Huh.

**Chris Gammell:** All right. Well, I guess. Watches are popular. Who would have thought? I know. I know. Yeah. There's entire, yeah. I get it. Yeah. So, do you have any, like, I know Waz is a big watch fanatic. Is he like one of your big fans? I know Chris Anderson who's been on the show. I think he's a Pebble fan. He's a huge fan. Yeah.

**Engadget:** Waz, I don't know. I think he's got one.

**Chris Gammell:** All right. That's a good start.

**Speaker ?:** I don't know.

**Engadget:** I don't hang out with Waz, so I don't know.

**Chris Gammell:** Not yet. You don't hang out with him yet.

**Dave Jones:** But he's too busy wearing his valve. Oh, yeah. Nixie tube. That's right. With the big two-digit display, you know.

**Chris Gammell:** There you go. There's a power-saving device for you, Andrew. Is put Nixie tube display. Yeah. Nixie tubes. Yeah, that's it. You thought a boost converter to five volts was bad. Try 300 volts. Yeah. Enjoy that.

**Dave Jones:** So, do you have any idea how many watches you've sold all up? Because they're selling in department stores now, aren't they, or something?

**Engadget:** Yeah, we are. Like that? Which is awesome. Ballpark? Yeah, so we're online.

**Dave Jones:** It's obviously in the hundreds of thousands now.

**Engadget:** We announced a number, and maybe, I don't know, maybe I'll look it up, and we can go back to this at the end of the show. I don't want to announce a number that's different from the most recent one we already said.

**Chris Gammell:** Well, what's the most recent? Sorry about that. I don't even know what that is. So, maybe whatever the public number is, is probably the safest number for us to say here. Yeah.

**Dave Jones:** Well, we know it was 80,000 from the campaign. Yeah, at least 80,000. Yeah, right. So, it's got to be double that, at least. Yeah, if it's under 200,000.

**SPEAKER_03:** 275,000.

**Dave Jones:** That was a couple months ago. That's a lot of watches. Yeah. There you go. So, people do like watches, then.

**Chris Gammell:** It is definitive, folks.

**Dave Jones:** Have there been any hardware changes in that time, or did you sort of nail it and sort of stuck with it?

**Engadget:** Not really substantive ones. But we did switch away from using the CAN Bluetooth module to sort of putting the equivalent circuit directly on our own board, and that was a pretty big cost savings.

**Dave Jones:** And then you had to get it certified yourself. Right.

**Engadget:** So, well, we had to recertify it because we'd already, because we designed our own antenna, we had to go through our own certification process already anyway.

**Dave Jones:** And that was worth it from just a cost point of view? Definitely. Yeah. Cost point of view.

**Engadget:** And lead time.

**Chris Gammell:** So, what do you think, Dave? Should we go to the Reddit questions eventually now? Reddit questions. Reddit questions. I think some of these actually were covered. Yeah, I think a lot of them were. So, maybe what are some of your favorite applications you've seen on there? Because, I mean, that is one of the things that we mentioned here, and that is a big thing about it, is that people can put their own applications on there. Have you seen any that are particularly, you know, stand out to you that are kind of favorites?

**Engadget:** I actually like, and this is a bit of a cop-out because we ship it with the unit, but I like the RunCaper one. I use it for cycling because I don't run, but you start your cycling activity on your phone and then it automatically on the Pebble actually brings up the interface and shows you your speed and elapsed time on the Pebble interface. That's nice.

**Dave Jones:** And that uses the GPS because that's a normal app for your phone, isn't it?

**Engadget:** Right, but I don't have one of those fancy bike mounts for my phone, so.

**Dave Jones:** Right, so it's just a convenient wrist mount, yeah.

**Chris Gammell:** Right, and you don't want $600 jiggling around on your bike as you go over bumps.

**Dave Jones:** That's it. You can just leave it in your backpack and it tracks the, you know, and it can track in there and transmits to your watch. That's the way to do it.

**Engadget:** Yeah, that's cool. And there's some cool stuff that people are doing with, like, home automation and remote controls. Yeah. Hooking it up to their lights or thermostat or whatever.

**Chris Gammell:** Smart house stuff and, yeah, all that sort of jazz. So it doesn't have any kind of, like, microphone input or anything like that, though, right? So there's no, like, Dick Tracy kind of functionality or anything like that? No.

**Engadget:** I mean, it's a common thing that you hand it to someone. It's a smart watch and can I talk into it? No, but we're not. You can talk about it. We think that adds too much. No, just push the bloody button. We think that adds too much complexity.

**Chris Gammell:** Yeah.

**Engadget:** It does.

**Chris Gammell:** No, it does. And especially from battery, right? I mean, like, that is, like, the central thesis here is needs to last for days. Yeah. And, like, I think about that, too, with, like, you know, oh, it'd be nice if it does media type stuff as well and, you know, like, all that other stuff. But it's, like, then it will not last for days. Right.

**Engadget:** There's the crowd that wants it to be an MP3 player and then it won't last for days.

**Chris Gammell:** Exactly. Well, that's, like, that Samsung one. Was it Samsung? The one that, like, the Galaxy S4 was giving away with it. Yeah. And that thing was a spectacular flop as far as I've read about, at least. But that was a lot of that functionality that you were talking about with, like, the bright screen, the bright color screen. And I think it does. It's got a camera.

**Engadget:** It's got voice. It's got, I think there's three microphones on that thing. They do all the same, like, spatial noise cancellation stuff that phones have. Really? It's literally a phone just crammed down into a watch. Yeah.

**Dave Jones:** Yeah. Feature creep. How, how, you've obviously been following other watches on the market. How crap are these ones you buy on eBay and deal extreme and stuff like that? I mean, they're a dime a dozen. Everyone's churning out a smart watch.

**Engadget:** Hey, I've got one that's literally a dual SIM feature phone in the form factor of a watch.

**SPEAKER_03:** Wait, what's dual SIM? What does that mean?

**Engadget:** It means that you can put it on two cell networks at the same time.

**Dave Jones:** Same time. What? Why would you write that? Oh, it's very convenient when you're trying to, you know, you've got work and personal ones. Right. Or if you're traveling.

**Engadget:** Or in China, which is the domestic market, the calling rates vary a lot based on who you're calling and what network you're on. So a lot of people want to be on two different networks.

**Chris Gammell:** Do you have to, like, wear, like, a battery pack, though?

**Engadget:** No, the battery life of this thing is, like, four hours. Yeah. Okay.

**Dave Jones:** Yeah, exactly. It's shit, right? It's unusable. And that's four hours when you buy it, if you're lucky. And then the battery in it's so crap and sourced from the absolute, you know, cesspit of Shenzhen. The one hungiest of one hung low, Dave. Exactly. The worst alleyway in Shenzhen. And, you know, this thing's just got toxic chemicals in it, you know. It's not a real battery and it lasts a week, you know, like, before the battery actually dies completely and you can't recharge it.

**Engadget:** So, Dave, I take it you've encountered a few of these watches. Do you have a favorite?

**Dave Jones:** No, I just know that they're totally shit. All these products that are just, you know, me too, built down to a price. And, you know, when you can buy a watch like this for, you know, 20 bucks delivered or something, you know, it's just bullshit. You know it's bullshit. You know it can't have a quality battery in it. You know it can't have, you know, quality parts in it. It's just, you know, it's just not possible. I don't know. Sometimes you do.

**Engadget:** What was that, the phone that Bunny found a few months ago that was, like, $8 or something?

**Chris Gammell:** Oh, yeah. I know what you're talking about.

**Dave Jones:** Yeah, but it's a one-off. You can't buy it anymore. It was like a...

**Speaker ?:** Right.

**Engadget:** It was like they bought up some stock of cheap old components and they manufactured them into phones, but that stock is gone. Right.

**Dave Jones:** Yeah, exactly. You know, you can't buy it next month. It's just, it's crazy. These things are built down to a price and they're just usually garbage. That's my experience. It's not just watches I'm talking about. It's other products as well, you know. Watch is just another fad, you know, that they've caught on to and, oh, yeah, look, you know, they can sell a million of them on eBay. Right.

**Chris Gammell:** And, Andrea, are you guys seeing pricing power now that you, I mean, like, obviously you have the name, right? I mean, Pebble is a very strong brand, I think, right now. And, obviously, you guys have a lot of attention from the Kickstarter and then your venture stuff. I mean, does that change your dynamic with, like, a vendor, like a chip vendor then?

**Engadget:** I don't have to drive to the sales meetings anymore.

**SPEAKER_03:** That's a good measure.

**Engadget:** Yeah. Do you get bought lunch? Yeah.

**Dave Jones:** They come visit us. Yeah. Right. Yeah, that's a good measure. And chouch your lunch. Yeah. Yeah. That's it.

**Chris Gammell:** Okay. Yeah, that's, I mean, that's good. Because, I mean, you guys are into the, I mean, you said 275 right now. Yeah. You know, that's a lot of watches. But that means that, you know, then projections are going to put you into millions and stuff like that as well. Yes.

**Engadget:** It does change the relationship you have with the suppliers. Yeah. Yeah. In terms of what you get access to, technology and.

**Chris Gammell:** Oh, yeah. You get early access then and stuff like that. Yeah. And I bet you've signed tons of NDAs.

**Engadget:** More than I can count.

**Chris Gammell:** Yeah. Oh, man.

**Dave Jones:** And then how, how bold do you get in terms of, you know, oh, look, we're going to, you know, buy a million of this part because we can get a spectacular price point. You know, how often would you commit to, you know, huge volumes above and beyond what you need for, you know, current production and projections and things like that. I know that's maybe.

**Engadget:** One of the things that's happened as we get bigger is that I'm not quite so involved in that side of things anymore. But I don't think we do that.

**Dave Jones:** You have a purchasing department that sort of, right, handles all that sort of stuff. And isn't that a huge burden off your shoulders? Oh, yeah.

**Engadget:** Definitely. You get to sleep now. That's fun. Yes. Yeah. No more, no more 1 a.m. Skype calls. Oh, yeah. All right.

**Chris Gammell:** Those are fun.

**Engadget:** I had a few of those, especially with our battery vendor. All right. We spun a custom battery and there was a lot of back and forth there. Lots of 1 a.m. Skype calls.

**SPEAKER_03:** Nasty. Why does someone choose to do a custom battery, if you're allowed to say? Dude, did you optimize the power for volume?

**Engadget:** Right. We're trying to maximize the volume it occupies.

**Chris Gammell:** Yeah. Okay. Yeah.

**Dave Jones:** The power per volume is everything. Yeah. What hours per volume is, you know. If you can utilize every square millimeter of space inside that watch, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** That's a huge gain.

**Chris Gammell:** Yeah. Does that mean that, so like in the battery game, is custom like a, because I know, it took me a long time to find out about, I think Dave actually told me about like the cells and like how the standard cells are and stuff like that. But does that mean like in custom batteries that it's just a repackaging of standard cells then?

**Engadget:** Well, first of all, for lithium ion polymer, it's a, the manufacturing process is a windup foil. It's kind of like a foil capacitor type construction. Okay. um in i mean obviously the the principle of operation is not like a foil capacitor but the the manufacturing technology is where they like laminate a bunch of films together and they wind it into a coil um and that winding can be done in any number of sizes and so that's what you get to

**Dave Jones:** customize cool and you can even get flexible ones these days yeah these days really amazing thin

**Engadget:** thin flexible fantastic yeah there was another kickstarter there was another kickstarter watch um that's going really thin i think their watch is like 0.8 millimeters thick or something um they built it into a stainless steel bracelet and they're using one of these flexible batteries

**Chris Gammell:** you guys get a lot of my buddy has one of those like super thin like mechanical watches that are like i don't know how much he spent on it but it's like do you guys get a lot of purists that are like oh well if it's not you know like it because watches are back into the you know the mechanical stuff as well do you do you get a lot of that kind of like purists of like oh i'm not touching digital or i mean or i'm not touching it because it doesn't

**Dave Jones:** have a stainless steel band or yeah you know what we do get a lot of is people saying well my watch

**Engadget:** has a solar panel or it has one of those like uh spinning weight rewinding mechanisms yeah i'm wondering if something like that would work for a pedal instead of having to recharge it and unfortunately the power density you get out of those is not high enough uh yeah right

**Chris Gammell:** wait you mean that the pz electrics won't work oh man i saw a pop sci article about that

**Engadget:** i've done a video on that my favorite one is transparent solar panels

**Dave Jones:** right yeah yep so that you can use it over the face so you get a larger surface area so so you don't

**Engadget:** but of course if it's transparent how much light energy is it collecting

**Chris Gammell:** right exactly yeah it's a spray spray on pn junctions right yeah i got one of the world's

**Dave Jones:** most efficient um solar cells and and looked at and measured its uh you know power output for powering a watch you know when i was working on my uh calculator watch and yeah it's just nowhere near the uh near the requirement for you know for charging the battery using the you know the charging you know the inefficiency and the charging circuits and everything else you just can't do it it's just you waste money and that's for a watch stuff yeah and that's for a watch that you know was running on the you know the smell of an oily rag let alone one that only gets a week's yeah battery using a

**Engadget:** general like mcu or um did you find one of the um like hardware implementations of a scientific

**Dave Jones:** calculator oh no because i know those are out there right no i was running off a just just a regular

**Chris Gammell:** low power cpu okay so yep so you're saying that like someone designed it like in logic gates or what

**Engadget:** do you what do you mean yes there are like dedicated scientific calculator chips and certainly four function calculator but i believe scientific calculator and i mean it's not the kind of thing you can buy off digi key i mean they come from you know yep random far east factories and they typically are um what like wire bond chip on board they don't even come in packages exactly but if you go buy a scientific calculator that's what will be inside there like the kind that's underneath

**Chris Gammell:** that black goop that's yeah exactly oh that's awesome and there are and they dedicated segment

**Dave Jones:** display one so it's not like you know you can interface it to a you know a dot matrix uh sharp

**Engadget:** memory lcd or something like that yeah so a lot of times these calculators will be like literally that one chip and a solar panel or battery that's it and a display and a keypad and that's it

**Dave Jones:** oh yeah that's all that's it that's three bucks and it costs they've been that way since 1970s yeah you know they haven't changed so those are the kind of chips then too that have like because i

**Chris Gammell:** remember i think it was someone who had like an old rpn calculator too and they were like telling me how how accurate their calculator was maybe it was dave telling me that as well um what we're like we're like old old calculators actually didn't have accuracy like even because of how the algorithms were in or something like that i'm not sure exactly what i'm talking about here i don't know i sound

**Engadget:** like more of a calculator nerd just then than i actually really am so i don't know okay no fail

**Dave Jones:** chris sorry all right yeah i'm gonna say would you guys run another kickstarter campaign because as you said it's a hype machine and you guys have the brand and people would go you know buy in frenzy a kickstarter frenzy because oh it's pebble they've got a new kickstarter is this something you consider

**Engadget:** or i don't know it's there's obviously pros and cons there but i mean now we have now now we've developed a lot more of the traditional channel like you said we're in bricks and mortar retail and we we have our own online direct sales and now we're in amazon so you could buy one on amazon and now that we have all that developed is kickstarter still the best i don't know right they've gone

**Chris Gammell:** back to the high school football game at that point right then it just becomes a marketing machine

**Dave Jones:** right that like a lot of people just use it for that um technically i you know and and there have

**Engadget:** been some products that have gone back on kickstarter um right sometimes it works sometimes it doesn't

**Dave Jones:** because that's essentially all i'm using it for is like a pre-sales tool really i mean you know i can if i wanted to i could afford the money to you know i don't need it to get the money to run a production run of my latest kit for example but you know it's a nice pre-sales tool so that you know exactly how many people are buying because they put their money up front so yeah i don't know if you're the same level as them though dave sorry no i'm not no i'm not but you know it's no but but you could have done it for a watch like this you know like you know if you do a small run of you know a hundred or a couple hundred watches or something you know you can you know only cost you a few tens of thousands maybe or less you're talking about the scientific calculator oh or just any watch in general kind of thing or any kind of you know product like this you could potentially do it yourself um you you could actually fund it yourself but uh it depends on i guess um what sort of position you're in so but what i'm saying is that there's a there's a bunch of people out there who use the crowdfunding sites as a pre-sales tool you know they they don't actually need the money it's more of a hype and pre-sales thing yeah than it is for genuinely needing the money yeah we were not in that boat but

**Chris Gammell:** a lot of folks do well where are you guys and you're in silicon valley is that right yes so does that have i mean i'm guessing you know your clientele are pretty uh tech savvy does that so that means you guys are probably pretty forward-facing in terms of like the the silicon valley community and stuff like that right i mean like do you see a lot of fans in the area yep fans and emulators and

**Engadget:** certainly we were um part of some of the um very um well i mean very small community of people two or three years ago that were kind of talking about doing hardware startups and how do you do consumer electronics as a startup these days um and of course the amount of activity around that is really um ballooned and we participate we participate in a lot of the meetup groups and presentations and conferences and stuff around that that's good you're gonna be at uh solid con um just like solid con i've heard of solid con um i should try and go to that yeah it's uh no

**Dave Jones:** current plans it's next spring what is it for the uninitiated like me it's an internet of thing it's like o'reilly's internet of things oh ah right i've got right yeah yeah i know the one grown yeah

**Chris Gammell:** well that's the thing i mean they pebble is part of the internet i mean like i'd say more than most right i mean they are a controlled device for many connected other devices that they

**Engadget:** are i mean it maybe it's not the first thing that some people think of when they say internet of things but that is a category that we seem to get we get lumped into and i think it's fair

**Dave Jones:** yeah i think so there's a question on reddit um somebody asked about can you tell us about the pebble watch that was shown in the kickstarter video like was it like the one and only prototype or was it was it hand built um it was one it was one of three um three printed they were 3d printed

**Engadget:** including the lens um so yes you can do 3d uh transparent printing i think it's the sla process and like very painstakingly polished afterward i think i think they cost us about a thousand dollars

**Dave Jones:** each just for the lens oh just for the lens wow yeah all right roi is pretty good though right i mean

**Engadget:** yeah you guys made it back pretty quick um and then we had it we had we had the 3d printed prototype and of course the 3d printed plastics are not very strong and we also did not have the the form factor that the really tiny two by one centimeter circuit board designed um and so we just crammed the display itself into the the 3d printed watch um and then filled the rest of it with i don't know rtv or something to make it more solid and and then we then we tethered it to um the pebble prototype board at that time which was you know a couple inches square or whatever just a general you know two yeah arduino size um and and that was what was in the kickstarter video and so it was so it was sort of really a watch it wasn't some sort of cgi trickery in the video right um but yeah the the we had the circuit board um outside and i think that wired actually um during the campaign had we let them have put some photos uh of that setup so that's out there for viewers who can't quite envision this

**Dave Jones:** there's photos up there on the internet so you can see the 3d printed case warts and all yeah

**Chris Gammell:** brilliant then that goes that goes into the uh the history case at the end right yeah

**Dave Jones:** yeah so i still got that of course oh yeah that's great yeah so what um lens are you using now is it like a quartz crystal kind of thing no it's plastic and we had to do that to get it curved to the extent it is yeah oh okay right was there any thought of using like a you know a proper crystal um glass

**Engadget:** lens i mean certainly they're a lot more scratch resistant and so we do what we can there's a coating on the on the lens now but um i mean the design to get it to what it is plastic was pretty much the only material that would work and i mean there's a lot of features on the inside of that too um and to get that sort of seamless top surface you have to have the detailing the mechanical features on the bottom and so really that has to be a plastic part did you and and did you say you

**Chris Gammell:** had your hand in any of the plastics designs at all i mean i guess you uh no i really don't i mean i

**Engadget:** i had to keep up on that back when i was in china a lot and kind of supervising everything because only one of us was over there at a time but um oh tag you're it yeah tag you're it um i hope you're somewhat up on mechanical engineering um i really need to get home and eat a burger um but no that's not really my uh area of expertise well it's good to keep up on that too because if

**Chris Gammell:** you're uh you know when they come to you the next day and like hey guess what you lost about uh you

**Engadget:** know three centimeters on your board um but it's fun like i learned way more about injection molding plastic parts than i ever thought i would want to know um as part of this

**Chris Gammell:** whole process it's awesome isn't it i love it i never want to design a tool but it's like it's so

**Dave Jones:** cool to me so what's your job these days as cto what does that entail a lot of sort of like

**Engadget:** setting the priorities for software development um it's like purgatory yep and i mean so there's that that's sort of the purgatory side the fun side is like i'm still pretty hands-on for electrical engineering i mean we have got me and one other um electrical engineer that's good and so like this project of of re-spinning the board to you know cost down by getting rid of the bluetooth module i mean it doesn't sound exciting but that kept us busy for quite a while yeah yeah yeah um and doing stuff like continuing to characterize the power consumption and like using current probes to understand exactly where power is going in the board i mean obviously before going into production we had a pretty good idea of you know what the design is like in terms of power consumption but that's something where um if we invest even more time in characterizing it we can do even better yeah yeah

**Chris Gammell:** you can start running firmware cross testing and stuff as well yeah put it into this mode see if it

**Engadget:** does and the firmware is a huge huge um contributor as far as what the actual power consumption is i mean i think if everything if everything on the board is powered up the battery life is like four hours or

**Dave Jones:** something yeah yep so did you do like a development internal development version of the hardware that sort of you know broke everything out to test points and current probes shunts build in yes things like

**Engadget:** that we've got that and in fact that's what our software developers still use because it's also got a jtag um right jtag to usb thing right on the board so it's pretty convenient for them right um so we've been through like three divisions of of that but yes we do basically we spin our own development kit

**Dave Jones:** um for internal use that's great right can you do jtag over bluetooth or no is that even a possibility

**Chris Gammell:** like to do debug over bluetooth um i think it's i'd imagine there's so much debugging of bluetooth that'd

**Engadget:** be difficult to yeah i mean a lot of the things that we want to debug are to do with the bluetooth stack and so i don't know how well that would um but for maybe for app developers right because their app is

**Chris Gammell:** sort of running in a sandbox yeah does it uh does it run 4.0 does it do the low energy stuff yes it

**Engadget:** does low energy um right now what's your opinion on that the only application for that right now is um that we use it for is the uh getting the notifications uh from ios 7 ah um it's definitely opening up the market for bluetooth stuff way more than it ever was um with classic bluetooth both on the um the silicon side like there's you know four main vendors of bluetooth classic silicon and there's dozens for for le but also on the consumer product side there's a lot of cool sensors and stuff um out there for btle and on the software development side so i mentioned i think i mentioned very early on it that bluetooth is really a mess software wise and that's mostly applies to classic

**Chris Gammell:** bluetooth um le is quite such a complex beast yeah because it only sends back the that's the one

**Engadget:** thing i know about four well it's like a published subscribe model at the soft in terms of the software

**Chris Gammell:** abstraction yeah right it just sends back everything or sends back some of the things yeah and that's

**Engadget:** why the power also helps right um so my background is automotive and like can and that's actually kind of a similar programmer's abstraction where it's like publish subscribe i've got this set of attributes and i'm gonna dynamically update them and then you watch them huh that's an that's an

**Chris Gammell:** interesting parallel i didn't i didn't know that they kind of map like that that's what uh i guess we should have covered this at the beginning what was the automotive background you stuff you did

**Engadget:** yeah so i mean my professional background was at first pure software like web apps and that kind of enterprise software and that kind of thing and then i went to school for um computer engineering and then i got into firmware um i was working on automotive um like driver assistance um putting cameras in cars to detect surrounding conditions and then warn the driver like you know turn off the high beams if there's a surrounding traffic or whatever um and then i decided that i had had enough of that and wanted to get into consumer electronics and then that's how i ended up at pebble

**Chris Gammell:** that's crazy again man you know i really want to uh you know uh have uh i this this timeline on this project's too long i really like it to be two months instead of two years but you know that's your thing that's that's good uh that's more i'm sure it's very exciting out there that's that is one thing i have to say it's it seems like it's very fast-paced and very um very customer uh you know facing as well yes you get interesting feedback i'm sure being able to talk

**Engadget:** to actual customers is i mean it's huge and in terms of being able to make good products and it's also really fun and in other industries that's something that doesn't happen quite as much i mean i know that obviously in different contexts but i know that for instance in industrial that obviously happens because i mean you're making a product for one customer but right yeah well

**Chris Gammell:** with cars too i mean like you have six million maybe you have six million customers but it's like you're not going to ask all of them you're going to kind of just tell them what they get and then they have choices amongst the marketplace whereas it seems like the thing about automotive is that um

**Engadget:** the timelines are so long and so you're trying to like predict what people are going to want in five years and i mean that was never a problem in the past for automotive but now that they're sort of getting into consumer electronics with infotainment and stuff um it's really tough like who knows what people are going to be doing for consumer electronics in five years and yet that's what the automakers are

**Chris Gammell:** trying to predict right driving their car with a watch obviously i mean that's going to be yeah

**Dave Jones:** because we don't have enough distractions in the car yeah it would just be that's like very bond-esque

**Chris Gammell:** you know that's that's cool what how okay that maybe that should be our final question how soon until we see a pebble on daniel craig's arm in a in a future bond movie is there any chance um

**Engadget:** oh is he gonna say yes no i can't say yes because there's there's uh nothing like that in the works oh oh come on sorry guys that's um but you can control your car with your watch um mercedes announced this a little while ago um they they have a pebble app to unlock your mercedes from your watch

**Chris Gammell:** and that's good that the battery life is long enough that you know if you leave your car in a car park for seven days you know or the battery just dies if you get there but yeah as you're walking

**Dave Jones:** up to it oh shit knew i should have taken the early flight

**Chris Gammell:** well andrew it's uh it's been really awesome i mean i i really appreciate you being so forthcoming with i mean like there's so many details to this stuff it seems like it's been a a crazy journey but you know very well it turned out very well and uh you know thanks i'm happy to share and it's there's

**Engadget:** there's never enough out there about how sort of consumer electronics design actually happens and i know as someone who wanted to get into the industry it's like what actually happens in the electrical engineering department at a consumer like i don't know yeah a lot of panic and coffee yeah

**Dave Jones:** and hotel rooms in china in china right yeah lots of any any thoughts about now that you're a huge well you know you're a decent size company any thoughts about potentially bringing it back home which are quite a few companies are doing oh manufacturing they're yeah manufacturing they're

**Engadget:** on shoring now is my moto x was made in dallas yeah my moto x was too it's tough because the supply chain support just really still isn't there yeah right you can't just walk down the local markets

**Dave Jones:** and pick up a reel because your smt line is stopped because you ran out of that part you know not that you want to be doing that anyway no anyway but still you know but the options there

**Chris Gammell:** exactly yeah or a cup of sugar and a reel of 10ks it's more like okay so we've got this charging

**Engadget:** connector on the side of the watch and it's got these pins that are custom machined and then we get them gold plated and like finding the machining shop and then the gold plating service and like we'd have to be flying all over the u.s to find vendors that could do this stuff whereas in china it's all within like half an hour drive of the factory yeah the final assembly factory you know

**Chris Gammell:** they'll ship you this stuff in the u.s you just got to send them buckets of money like buckets of

**Dave Jones:** money we can only hope all right thank you very much andrew it's been awesome i'm gonna hope for

**Chris Gammell:** the bond movie first i think right yeah that's i don't know that's killer yeah maybe we can see

**Dave Jones:** him wearing a prototype pebble watch because that's where you want to show your prototype first you

**Engadget:** know you've got to get in a famous bond movie yeah that's it good suggestion i'll keep that in mind

**Chris Gammell:** there we go yeah david your marketing department if you can get it yep yes andrew thank thank you again for being on the show it's been really really great sure of course my pleasure all right so people

**Dave Jones:** can find pebble at uh get pebble.com and they can find you on twitter as well they can follow you

**Engadget:** i are you a twitter nerd um not that much i think the last time i tweeted anything was some months ago

**Dave Jones:** but ah right okay well don't follow andrew on twitter then i'm i'm a pretty boring twerp or whatever

**Chris Gammell:** you call a twitter user dave and i call that to each other yeah yeah it's nothing like a good

**Dave Jones:** mindless tweet of what you're having for lunch you know right of course all right thanks andrew thank you catch you later bye later

**SPEAKER_03:** you

**Speaker ?:** you
