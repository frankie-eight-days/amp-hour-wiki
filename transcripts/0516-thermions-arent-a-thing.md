---
episode: 516
title: Thermions Aren't A Thing
url: https://theamphour.com/516-thermions-arent-a-thing/
---

**Dave Jones:** This is The Amp Hour Podcast. Released November 8th, 2020. Episode 516. Thermions aren't a thing.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics. What's up, nerd?

**Chris Gammell:** Oh, you know, some stuff in the US.

**Dave Jones:** Don't know what you're talking about. No idea. I know.

**Chris Gammell:** Yeah.

**Dave Jones:** Yeah.

**Chris Gammell:** It's almost over.

**Dave Jones:** We'll see. Excellent. All right. Let's talk some electronics, shall we?

**Chris Gammell:** Yeah, exactly. Exactly. I have been diving into work to try and distract myself. And luckily, yeah, it's been bountiful. So lots of work to do. Yep. I don't know if I've mentioned on the show before, but I've been working on Nordic parts a bunch. Maybe I've mentioned it a little bit.

**Dave Jones:** I'm sure you've mentioned it.

**Chris Gammell:** Yeah. So I do have one. I have a Nordic part on the ABC board, which is that board I made for the course. And that's the cellular board. Yep. But then I've been working on it a little bit otherwise for one other project and then a client project and whatever else. What's interesting is I finally got the Bluetooth bootloading to work.

**Dave Jones:** Yep.

**Chris Gammell:** Have you ever done that? Do you do that with the meter? I have your meter here, but I don't know if it loads from or over the Bluetooth.

**Dave Jones:** No, it doesn't. No. We deliberately didn't do that because it was exceedingly hard, they said, to do anything over the Bluetooth like that. So, yep. Oh, okay. Unfortunately. Oh, yes. It was originally, yes. We wanted to load the firmware over the Bluetooth and also upload from the SD card as well from the Bluetooth. And you could have actually almost tied those two together, but it was, yeah, they just deemed it no. It was like it's not worth our effort. It's not worth our time investment in that.

**Chris Gammell:** I would actually say it is worth it. So, like, I have been shocked at how interesting it is to have, like, to have that capability now because now I can, like, ship off firmware to someone and it's literally like, hey, open this app, upload it. You're good to go. It blinks a little bit and then it's like.

**Dave Jones:** Yeah, but we already had an SD card in the product. No doubt. Yeah, no, no, no. SD card firmware uploading.

**Chris Gammell:** I'm not questioning the practice. I'm just saying that, like.

**Dave Jones:** Oh, no, of course. There's benefits.

**Chris Gammell:** I have found it to be very interesting. Yes. It's, like, very different for me because, like, you know, people that do regular software updates things and, like, have bootloader chains that are very well known, like, they're like, yeah, of course you do that. But, like, for me, it's just it's very different. I think the big downside is that it it just takes up a lot more memory, you know, so, like.

**Dave Jones:** Oh, yeah, it does.

**Chris Gammell:** Yeah. Yeah, so it's, like, I've got, like, the 512k part and, like, a bunch of that. So, I think, like, maybe, like, 60k of that is the actual, like, Bluetooth, like, soft device is the Nordic part. And then, you know, and then you have to have pretty much, like, double the rest of that. So, like, basically, like, I have, like, 440, I think, available, 440k available. You can only really build it into, like, 220. You only get about 200k for your actual program then.

**Dave Jones:** All right.

**Chris Gammell:** Luckily, I write very simple programs.

**Dave Jones:** Jeez, when I was a boy. I have to link you my 1k video of what you can do in 1k, you know.

**Chris Gammell:** Yeah.

**Dave Jones:** You remember the 1k contest, you know?

**Chris Gammell:** Yeah, exactly. Yeah. Yeah.

**Dave Jones:** And it's, but the thing is, a lot of parts, I don't know about the Nordic ones, a lot of parts will only have a limited, they'll have, like, a separate segregated section, a safe area of bootloader memory, and that will be limited. It might be, you know, 2k or something like that, you know. It might be a limited, like, you can't just extend it to.

**Chris Gammell:** For the bootloader itself, you mean?

**Dave Jones:** Yeah.

**Chris Gammell:** Oh, yeah. Yeah. The bootloader is, like, at the top of the memory stack.

**Dave Jones:** Oh, so you're saying don't put the Bluetooth routines in the, no, but it has to be in the bootloader. So it's fully protected. So even if you goof it up completely, it's still, you can still recover via the Bluetooth. So it's all got to be in that protected memory space.

**Chris Gammell:** You mean the actual Bluetooth capability? Yes.

**Dave Jones:** Yes. The Bluetooth.

**Chris Gammell:** No, it's like, yeah, no, the Bluetooth stuff is, like, weird. So, like, Nordic does it where it's, it's like a binary, basically. And, I mean, they're all binaries. But, like, but basically it's like, there's an API to this, like, this just chunk of memory. And, like, you just basically have to, like, preserve part of your flash and part of your RAM. And it's just going to run out of there. And people who know more about this stuff are just laughing at me right now. That's fine. Yeah, right. Of course. But basically that's, that's kind of, like, the, the bottom part. So that's, like, basically, like, 0x0 to, like, 0x2600 or 26,000. And so, like, that's basically just what the soft device is. And it's, like, basically every function that's in, that you might want to use on the Bluetooth side of things, it's in there. And then the bootloader is actually at the very, very top of the memory. So, like, whatever the, you know.

**Dave Jones:** Yeah, but both of those have to be, both of those have to be protected memory spaces. Otherwise, you're going to come and gut's up.

**Chris Gammell:** Yes, that's right. Yeah, I agree.

**Dave Jones:** And, well, that's what I'm saying. Some processors only have that a small amount of protected memory space. Oh, I see. So, like, you would not be able to fit Bluetooth in there.

**Chris Gammell:** Got it. Yeah. Yeah, and that is, it is a big Bluetooth thingy in there. Like, that soft device is.

**Dave Jones:** Oh, yeah. It's a large, yeah, it's a large build. Yeah.

**Chris Gammell:** Because it's basically, like, it's all or nothing. You basically use all, you know, you put in everything in the kitchen sink that Nordic offers you or nothing. Yeah, right. And so, I'm still getting my head around it. But, like, in the Zephyr stuff that I've been doing, it's, like, I think it's more selective on the build. Because the idea is, like, I think they didn't want people to mess it up during the build. But I think they also didn't want to show their source code in the old way of doing things for Nordic. But, like, now I think there's actually, like, the whole stack is in there and available. And, like, you can selectively build what's in there. So, you could shrink it down if you needed less stuff.

**Dave Jones:** Okay. I think. Got it.

**Chris Gammell:** So, yeah. It's interesting, though. And so, like, but now, basically, I just, yeah, I have to, like, package up the firmware that I make then is, like, basically just offset. So, it starts at the beginning of, basically, at the end. Sorry. It starts at the end of the Bluetooth memory area. And then it just runs like a normal program. So, it's super cool. Firmware, Dave. Who knew?

**Dave Jones:** One of the reasons, also, that we didn't do it in the multimeter is because we, ours wasn't a Bluetooth chipset. It was Bluetooth LE, which is actually quite a different beast. Bluetooth LE is much harder and much more inflexible, much less flexible than normal Bluetooth. So, yeah. Just beware. Like, Bluetooth LE does not support serial ports over Bluetooth, for example. You know, you've got to cludge it. If you want to do that, you really have to cludge it.

**Chris Gammell:** Yeah. I don't know about that yet, but that is a.

**Dave Jones:** You don't want to know. It's awful.

**Chris Gammell:** Yeah. Yeah. You're saying because it's, like, low power and it would not be able to stream stuff back. Is that kind of the thinking?

**Dave Jones:** Yeah. And it's, yeah, it's designed to be, yeah, ultra low power. Like, Bluetooth is pretty low power, right? But Bluetooth LE is, you know, yet another level down.

**Chris Gammell:** Yeah. Yeah. So, I'm still learning a lot with it, to be honest. Yep. But I'm very excited about it. It's cool stuff. And like I said, the ability to, like, just kind of push updates is real nice.

**Speaker ?:** So.

**Dave Jones:** Right. So, yes, my pro tip there is don't use Bluetooth LE unless you absolutely have to use normal Bluetooth.

**Chris Gammell:** Oh, I don't agree with that.

**Dave Jones:** No, trust me. Yeah. Yes. It's a long, hard, expensive lesson learned. I can assure you. Bluetooth LE.

**Chris Gammell:** You guys used a module or you used a chip?

**Dave Jones:** Yeah. Yeah. We used a module. It was the 112. What is it? The BLE 112? Am I right? Jeez. I can't remember. It's. Okay. It's scarring. Silicon Labs. Okay. Yes. That's the Silicon Labs BLE 112.

**Chris Gammell:** The latest. Oh, it's Bluetooth 5. It says. I think. Okay.

**Dave Jones:** But that's. Anyway, it's. Yeah.

**Chris Gammell:** So, you guys just using. You were talking to it over another. From another micro though, right? So, like you have like. Oh, yes. STM 32 on board. And then you just kind of throw. Yes, that's right. Throw serial commands to this thing?

**Dave Jones:** Yep.

**Chris Gammell:** Okay.

**Dave Jones:** But, well, no. It wasn't that easy. Because as I said. Well, yeah. It sounds like it was not easy. Yeah. Bluetooth LE does not support proper serial implementation. We thought it did. And that's why we spent a huge amount of time, money, and effort. Trying to get it working. And it's a real kludge in the end. Yeah. You can get it to do it. But, geez. You know. Yeah. It's just not as easy as it is on normal Bluetooth. Got it. Yep. Yeah.

**Chris Gammell:** Isn't it crazy when some of those. So, like. You know. At the. You know. Now. Thinking about it now. You know that like. You would go back and tell yourself like. Oh. Well. Look a little closer. At that serial side of things. That's really going to be important. Right?

**Dave Jones:** We just took it for granted.

**Chris Gammell:** Well. But, I mean. That happens all the time in designs. And like some things. It's fine. Right? It's like. Oh. It's a software fix. Or. Oh. Change a resistor. Or. You know. Yeah. But some things are just. Yep. Man. They're. They're like. So. Fundamental. To like. The. The. Architecture of your design. It's just like. Oh. That's going to change everything. You know.

**Dave Jones:** Exactly.

**Chris Gammell:** So. Yeah.

**Dave Jones:** Yep. Beware. It's a. The other thing is. You know. USB power delivery. You've heard me crap on about that before. Of course. You know. You think that's easy. No. It's not. It's a nightmare. It's an absolute design nightmare.

**Chris Gammell:** I have to feel that's getting better though. Like. There's more chipsets that are out there for now. Right?

**Dave Jones:** It. It. It. It probably is. Yeah. Yeah. And. And once again. There's the. That large stack problem. Yes. You know. ST. Offer a. You know. A Bluetooth. Offer a power delivery system. But it's like. Dave. It's all the same. But it's like a couple of hundred K. Or something. Right? And it's like all or nothing. You've got to use the whole lot.

**Chris Gammell:** Hundred K dollars? Or. Or. No.

**Dave Jones:** As in a hundred K of memory. Just for implementing. You know. It's. It's insane. Right? It's just. Yeah. It's just crazy. So you can't use a small simple micro. To do your USB power delivery. You know.

**Chris Gammell:** Yeah.

**Dave Jones:** It's just. Yeah.

**Chris Gammell:** I think that's. That's one thing I've been thinking about too. Is just like the. So I think that. Being a later adopter. As. Is my goal in life. You. You get benefits of like. You know. So as. Dye shrinks happen. Or as firmware gets more. You know. Like the. Bluetooth. I think the soft device that I'm using. Is like the version 7. 7.0. Or 7.1. Or something like that. Is like very. Very. Very. Mature. At least in terms of the. The Nordic stuff. And it's like. I'm benefiting from all of the. Heartache that happened. And heartburn. That happened from. People that were using the. 1.0. Standard. And I've heard people complaining about it. But now it's just gotten so mature. It's like. Oh yeah. It's just a thing now. And like. And it was still hard for me. But. But me as a solo engineer. I can actually implement it. Versus. Meeting a team of like. Six people. And like. You know. Long nights in the lab. To try and get this thing working. I think maybe with the power delivery stuff too. It's like. More chipsets are coming out. And so it's going to get easier. To do that sort of thing. But it's just a. It's just a matter of. Maybe buying a more integrated part. Or you know. Re-evaluating. Like you know. Like it becomes a system design problem. And like. You are not. You know. For the stuff you work on. You're not going to go back. And rip everything up. But someone who's starting a new design. Might benefit from the. The new chipset. And just. Leapfrog a little bit in that way. You know.

**Dave Jones:** Yep. Agreed. Sucks.

**Chris Gammell:** Yeah. Electronics.

**Dave Jones:** Can we talk about something vastly simpler. And to me. Vastly more exciting.

**Chris Gammell:** Okay.

**Dave Jones:** I just discovered this. Sorry. I don't have the name of the person. Who alerted me to these things. But. It's probably going to be today's video. That I. Shoot. If I get off my ass. And do it. These are very exciting. I'm so super excited about this. And. I'm a total nerd. Because it's a.

**Chris Gammell:** Burying the lead folks. Burying the lead. Burying the lead.

**Dave Jones:** It's a thermal jumper.

**Chris Gammell:** There it is.

**Dave Jones:** What is a thermal jumper? I hear you say. Yes. It's a. Apparently these are fairly new. Hence why I've never heard of them before. Like. The person who sent it to me said. He did a bit of research. And said. Yeah. It looks like they've only come in. Come out in the last year or something. They're available from. At least two manufacturers. Vishay. And a company I've never heard of. Called. American Technical Ceramics. ATC.

**Chris Gammell:** Yeah. That's. That's. That's not a great name.

**Dave Jones:** ATC. But it's the engineer's choice. That's their. They've. They've stolen the tick single.

**Chris Gammell:** A name that only an engineer could love. How about that?

**Dave Jones:** I'll send you the. Send you the linky to the ATC one. Because you won't have that. So there you go.

**Chris Gammell:** Okay.

**Dave Jones:** What these are. Right. I've done a video. Which we'll have to link in. On. Doing thermal design. Use. For SMD parts. Right. And it's actually. Surprisingly. Tricky. And hard. Right. If you want to get heat. Out of. Surface mount part. Well. Let's look at through hole parts. Right. If you've got your TO220 package. Right. Obviously. People have been doing this for 50 years. Right.

**Chris Gammell:** Better screw that sucker down to a heat sink. Right.

**Dave Jones:** Screw that sucker down to a heat sink. With some thermal paste. Right. No worries. Right. Love it on. Right. But try. To get heat. Out of a. Modern. You know. SMD. Power transistor. Right. In a. You know. Whatever your favorite SMD. Package is. Right. And. Or try and get it out of. A. Motor driver chip. With a big thermal. You know. Pad. On the bottom. And stuff like that. Now. You might think. Oh. Okay. No. You just tie it to the ground plane. Well. A lot of these. Have to be isolated. Right. A lot of these things are. They're not connected to the ground. So you can't just connect it to the ground plane. And you might think. Oh. Well. I can just via stitch it. Down to a big. You know. PCB. Mounted. You know. Thermal pad. And then maybe put one of those. Surface. Mount heat sinks on top. Right. Have a floating pad. Effectively. Yeah. A floating pad. But. Hey. Bingo. You've just killed. Your PCB layout. Room. Right. Or. Or you need to go to a six layer board. Because you've already got four layers. Two for your power. One. Power ground. And two. Routing layers. And then what. You want to add another two. Just for. A heat sink. Okay. But. You know. It's going to cost you more. It might be cheaper to go to one of those. SMD. One of those pick and place. SMD heat sinks. That you can. Put down. Right. They're available in various. Scenarios. And stuff like that. But. The whole idea is. When you go to SMD. Right. You want to do everything SMD. Right. Right. That is the holy grail. And you don't want to say. Oh. Let's mix some through hole parts in there. And. Oh. I'll use a big. To 220. Because I need to screw it into my heat sink. Right. No. You want everything pick and place.

**Chris Gammell:** How much could it possibly cost. To just have some hand placed. You know. Hand soldered. And or wave soldered things.

**Dave Jones:** It's just. Yeah. It's going to be vastly easier. Cheaper. And simpler. To have everything SMD. Ink. But. As I said. You've got the problem. With getting heat out of SMD parts. So. Ta-da. These new magic thermal jumpers. They look like resistors. Or surface mount resistors. Available in different packages. Big fat wide ones. By the way. By the way. People argue over whether width. Or length. Is better. When it comes to thermal. I'm telling you. Width. You want width. Okay. Because it's. I mean. Wouldn't it just be.

**Chris Gammell:** The same. Surface area or no? It's not. No. No. No. No. No.

**Dave Jones:** Because it's got a longer path. It's got a longer path. So you want a wider. Shorter path. Than a long. Even if it's the same surface area. Because. Pause. If you do the electrical analogy.

**Chris Gammell:** Yeah. I guess. If you take that to extremes. Right. Well. Yeah. If you like. If you had like a really long wire. That would be much worse. Like instead of.

**Dave Jones:** Extra resistance. Which in this case. Translates into the thermal equivalent. Which is extra. Thermal conductance. Right. So you get a higher thermal resistance. Right. So more power dissipated. No. You want a fatter. Wider. Shorter. Part. Anyway. There's surface mount parts. You can just. You know. Pick and place. They come on a reel. You can buy them on a reel. They just pick and place. And they drop down.

**Chris Gammell:** They look like resistors. Honestly.

**Dave Jones:** They look like resistors. Yeah. But they're actually. They're made of. What's the. Hang on. I'll get you what they're made of. In a sec.

**Chris Gammell:** AIN. Is that it? Thermally conductive. AIN substrate. I don't know what that means.

**Dave Jones:** It's an aluminium nitride. Substrate material. Oh.

**Speaker ?:** Got it.

**Dave Jones:** Oh. That's an L.

**Chris Gammell:** Okay. A-L-N. Yes. Lowercase L. Gets you every time.

**Dave Jones:** Right. So they're made out of aluminium nitride. And they're thermally conductive. But they're. The beautiful thing is. Is that they're electrically isolated. Right. So that you can. Like literally put these right next to your. The heat. The pad. That you want to get out. Say you've got a big thermal SMD package. You can put this right next to it. And bingo. It's a low. Thermal. Conductivity path. Through to. Then. You can get it out to. A ground. So then you can connect it to your ground plane. Right. Because you've already got. You know. Usually you're going for a four layer board. These days. For any sort of like. Complicated design. So you've already got that big ground and power plane in there. You can use that. As your heat sink. And that's what's so exciting about these things. But it's got to be electrically isolated. So that's what these things do.

**Chris Gammell:** You still want to send it to your heat sink. You're sorry. You're still going to send it to your ground plane. You want to use all the copper. But you don't want to send the electrons. You're saying.

**Dave Jones:** That's right. You don't want to send the electrons. You want to send the heat.

**Chris Gammell:** You want to send your thermions.

**Dave Jones:** Your thermions. Thermions. I'm sure that's a legitimate physics word.

**Chris Gammell:** Yeah. Sure.

**Dave Jones:** Thermions. If not.

**Chris Gammell:** It is now.

**Dave Jones:** And the other thing is. Is that they're very low capacitance. We're talking like. You know. Yeah. 0.1 puff. Or something like that. Which is important. If you've got like high switching stuff. Right. So if you've got big switching power transistors. Right. Operating at. You know. A meg. Or something like that. You don't want high capacitive parts. Coupled onto there either. Yeah. So that can be a big. That can be a big deal. So. Yeah.

**Chris Gammell:** I'm very excited about these things. Can you try and paint a picture. Of what this looks like though. So like. Okay. So. So like.

**Dave Jones:** What picture of what it looks like.

**Chris Gammell:** Yeah. So like. Okay. So you're going. No. I get that. That actually. There's like a thermal picture. I meant. Like. So. You have like. A thing that looks like a. 0603 resistor. Or equivalent. Right. That is. Directly touching another component. On one of the leads. Is that the idea. Yeah. Or is it just. Touching an area. Like an isolated area. And then taking that. To the ground plane.

**Dave Jones:** The whole idea. Is that. Let's say you wanted to get heat. Out of an SMD resistor. Right. Let's say you had a. You know. A power resistor. Or something. You wanted to get heat out of it.

**Chris Gammell:** So like a sense resistor. Of like a motor driver. Okay.

**Dave Jones:** Yes. A current sense resistor. Or something. You know. At maximum current. You design it. And it might be a one. One watt. Power dissipation. Right. Sure. You know. A big. Big ass power resistor. Right.

**Chris Gammell:** And it's got a. It's got a thermal coefficient. And that might change the resistance. And yada yada yada.

**Dave Jones:** Yep. So what. So what you want to do. Is actually. Here's where you have to change the footprint. Well you don't have to. But you know. Anyway. So you extend the footprint out. So that. The footprint of the resistor. So that. Then you. Connect. The thermal. The thermal resistor. Right. Let's call it the. Well no. The thermal jumper. Sorry. You connect the thermal jumper. Directly to the pad. Of the resistor. Right. So you essentially. Sold them both. Onto the same pad. You know. You can use separate pads. And then join them. With a gigantic. Thick track. Right. But it. And then. It's going to suck. All of the. Thermions. Out of the. I love that word. Out of. Out of the resistor. And you could do it on both sides. You could do it on both. Yeah. Yeah.

**Chris Gammell:** That's what I was really wondering. So. So it would. So like. When I. I guess that's the. The thing that I was confused about. Because. When you think about like. So say. We're using that same like a nice big. Sense resistor. 0.01 ohms. And it's still dumping a ton of heat. Or something like that. Normally if you're going to heat sink that. You would. Make a physical contact. With the heat sink. And then maybe some thermal paste. And then. That is the conductor. Like through the actual package. Of the resistor. It sounds like now. It's drawing it through the pads though.

**Dave Jones:** It's got. It's got to go through the pad. Yeah. Whether or not that is. A regular component pad. Or whether or not it's a power pad. On the bottom of the chip. Or. Yeah.

**Chris Gammell:** So it could be like a maybe a small. So say that the. The. Sense resistor had an actual mounting element. To a thermal pad. That's not. Tied to a big. Much bigger ground plane. Yeah. It might have that as. So this would maybe be the bridge. From that small thermal pad.

**Dave Jones:** That's right.

**Chris Gammell:** Where it's just contacting. The package of it. Versus. Yeah. Okay. All right. So that's. That's where. That's where I was getting confused. Yeah. But that's. Yeah. That's. That's super cool.

**Dave Jones:** Obviously. This is not as good as going directly via. Vias down to your ground. If you've got a big thermal pad. Right. And you want to go down to your ground plate. This is where you need isolation. Right. If you need. You know. Yeah. This is the key part about this product. Is it's isolated.

**Chris Gammell:** Yeah. And what's the. Is it like super high voltage too? I don't know.

**Dave Jones:** Oh. I'm not sure about the standoff voltage. That'll. That'll depend on the package.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh yeah. No. 1.5. 1.5 kV. AC RMS. Oh yeah. I guess you're right.

**Chris Gammell:** That would. That would depend on the. Like the creepage and clearance then. Yeah. Of this. Of this specific part. Right.

**Dave Jones:** Yeah. But the actual part itself. Is 1.5 kilovolts. So.

**Chris Gammell:** Or would it be the breakdown of the material internally?

**Dave Jones:** I don't know. It just says. The. No. This is the dielectric. So that's internal. That's by definition. The internal. So it says greater than 1.5 kilovolts.

**Chris Gammell:** Yeah. Because it's some voltage. Every. Yeah. Everything starts to. Oh yeah. Break down. Right. I mean. So. Everything breaks down.

**Dave Jones:** Given enough voltage.

**Chris Gammell:** Yeah.

**Dave Jones:** Oh by the way. The term thermion is real. By the way. Is it? Oh. Yes. Yes. Yes. Thermion. It just occurred to me. Thermionic emission. Is a thing. It's a. You know. It's like a. Yeah. It's like a valve thing. You know. Thermionic emission. It's like elements. Sure. Anyway. So yeah. We absolutely butchered that.

**Chris Gammell:** Well. We need a new. We need a new word then. But I still like thermion. All right. Yeah. Have I ever mentioned. The hot air rises and heat sinks. By Tony Cordybon. Is it a book? It's a book. It's a book. Sorry.

**Dave Jones:** I love the title. That's just. Yeah. It's. It's actually a really.

**Chris Gammell:** It's like really cheeky. Like the whole book is written really cheeky.

**Dave Jones:** I see. Is it about heat sinks? Because if it's. It is. Yeah. It's. It's about.

**Chris Gammell:** Yeah. It's basically. You know. Like the front page is like. The front of the. The cover of the book is just like. A picture of a thermograph. Drawn on a napkin with coffee and stuff. And yeah. Oh. Nice. Like it's very. What's it called? It's totally like a story. The whole thing. So it's very narrative. In that way. Oh. That sounds great.

**Dave Jones:** I might get that. Yeah.

**Chris Gammell:** Yeah. You might. You'd probably like it. Yes. It's a good book.

**Dave Jones:** Unlike the usual self-help recommendations you give each week. You know. Oh.

**Chris Gammell:** Sorry. I thought you were going to say. Unlike the usual. Equation based books that are usually covering this topic. You know what Dave. Whatever. Those also have stories.

**Dave Jones:** No. Just based on the title. I know it's going to be good. You know. Yeah. Yeah. So. Yeah.

**Chris Gammell:** You're judging a book by its cover. Cover. Absolutely. Absolutely. Oh. And then. Sorry. The subtitle is. Everything you know about cooling electronics is wrong. So it's very. Very targeted. Yep. Anyways. Yeah. That's a good one.

**Dave Jones:** That sounds great.

**Chris Gammell:** Yeah.

**Dave Jones:** Yep. Let's get that. All right. Maybe I can do a book review.

**Chris Gammell:** Oh boy. That'd be a first.

**Dave Jones:** Yeah. I don't know. Technically it's not. I used to do book reviews back in the back.

**Chris Gammell:** Okay. Art of electronics doesn't count Dave. Art of electronics doesn't count.

**Dave Jones:** No. I used to do a book. I used to do book reviews when I first started my channel. Yep. Yep. Used to be. I had multiple segments in the one video and one of them was a book review. So. Yeah. Anyway.

**Chris Gammell:** The good old days.

**Dave Jones:** Anyway. I love these thermal jumpers. It's like. I am just losing count of the number of designs I can think of over the years where this would have come in so handy.

**Chris Gammell:** Yeah.

**Dave Jones:** Really. Somebody's going to jump in the comments and go. Oh yeah. They've been around for a decade. Exactly. But. Holy crap. You know. I just learned about them and I think they're the duck's guts. So. And the price. Tell us the price son. Because I know you want to. The. In thousand of. Quantity. Hang on. Just let me enter it into the digi keys here. Thousand of quantity. About 36 cents a pop.

**Chris Gammell:** Well that's not bad.

**Dave Jones:** A thousand quantity.

**Chris Gammell:** Yeah.

**Dave Jones:** It's okay. You know. I mean.

**Chris Gammell:** You're probably going to do not many of these. Right. Unless you're having a huge board. In which case. Or like a huge amount of heat in your board. But. Well.

**Dave Jones:** Yeah. As I said. Just use one big fat wide one.

**Chris Gammell:** Yeah.

**Dave Jones:** You know. Or they. They. They jump up to 55 cents for the big fatties.

**Chris Gammell:** Okay. So. You know. What is your. What is your. What's like one of your examples. That you. You could think of.

**Dave Jones:** Oh. Getting out of. Uh. Like a. Well. A power. Any power transistor design. Where I've had to. Uh. In low profile stuff. Where normally you would. Uh. Sort of. Like have a. Um. A. A. A thermal pad. On. On top of the chip. For example. Right. You would have a thermal pad. On top of the chip. And then you'd have a heat sink. Wedged on top of that. Or you'd have the case. Wedged on top of that. Right. So. You know. Usually like a metal case. Or whatever.

**Chris Gammell:** Yeah. Like a piece of metal. Just coming down. And like.

**Dave Jones:** Yeah.

**Chris Gammell:** Clamping it.

**Dave Jones:** But of course. Getting. Heat out of your chip. Via. The. Through the plastic case. Is pretty poor. Because you know. The thermal conductivity of plastic. Is not great. Right. So it's. You know. So you want to get it out. And then. From the pads. Right. A lot of it comes out. If. If you've got chips. That's coming out via the bond wires. Because they're metal bond wires. Right. And they. So the dye heats up. The metal bond wires heat up. The pads heat up. Right. Everything heats up. So. It's. And if you've got power. Power resistors. For example. Yeah. It's like. I've. I've had to. You know. I've done many times. Where I've had to put like. Little. Sort of like. Mini PCB heat sinks. Like just large thermal pads.

**Chris Gammell:** Got it.

**Dave Jones:** Hooked onto. Hooked onto my power resistors. Just to. Just to get the power. You know. Just to keep the temperature down. Right.

**Chris Gammell:** And then you wouldn't have. And then you're just dependent on radiation. Instead of like. You don't have any like. Active cooling or anything like that. Right.

**Dave Jones:** No. No. It's a radiative. You know. Thing. Usually. Unless you've got heat out the other way. I've even done designs where. We've actually. Hermetically sealed packages. Where we. Oh yeah. Actually inject them with a gas. So then the. A high thermally conductive gas. Which then gets the heat out to the outside can. And stuff like that. You know. Cool. So yeah. That's you know. That's very expensive. Very specialized. You know. Small quantity. Stuff used in the military. Things. But yeah. It happens. You know. When you need that specific requirement. Then you go to town to do it. Right. Doesn't matter how much it costs. Right. Yeah. Each package has to be. Hermetically sealed. Filled with gas. Then sealed. Then tested. Then gas tested. That it doesn't leak. And you know. Has to be qualified. That it can survive. Shock and vibration. Without leaking. Without the gas leaking out. Because if the gas leaks out. Then your thermal conductivity. Goes to buggery. And the. And the circuitry just. Cooks itself. You know. Because it can't get the heat out. Right. And it's just. Yeah. It's nightmare. But. But there. As I said. Like having that isolated thermal. Those large thermal pads. It kills your. PCB layout. You know. It's just really annoying. Yeah.

**Chris Gammell:** It's like a. Keyboard zone at that point. Right. I mean. You just got to go around it. Yeah.

**Dave Jones:** Yeah. It's just got to go around it. It ruins your. You know. Your layout density. And. To be able to put in one of these small parts. And then just. And get it isolated. Down to your ground plane. Wow. You know. Ground or power. It doesn't matter.

**Chris Gammell:** Yeah. Right.

**Dave Jones:** Wow. You know. Although. Like. Internal ground planes. Aren't the best heat sinks. Right. Not exactly the most efficient. Because they're wedged between. Right. Fiberglass. Which is not exactly. Thermally conducted. Right.

**Dave Jones:** Yeah.

**Dave Jones:** And. But in the military side of things. There's many advanced. Manufacturing technologies. In PCB design. Which a lot of people don't know about. Because you won't get it. From your JLCs. Your PCB waves. That's right. Yeah. Right. You know.

**Chris Gammell:** All those. Right. Right. You're also going to be paying for it. Because that's. Yeah. Yeah.

**Dave Jones:** You can get high thermally conductive graphites. Embedded into your PCB material. You can get thermal. Thermal water channels. Embedded into your PCB material. Oh wow. Thermal pipes. You know. Like actual. Not just. Like you can get water pipes. Embedded into your PCBs. You can get just. Copper. Copper conductors. Like big copper rods. Embedded into the.

**Chris Gammell:** Oh. Like they do for like. Like PC heat sinks. And stuff like that. Like just. Pure copper. Like on top of a. Intel chip kind of thing.

**Dave Jones:** Yes. Yeah. And that. But that'll be embedded. Into your PCB structure. And then you'll have these large copper tabs. Coming out the side. And then you could mount those. On to large external heat sinks. And there's all sorts of advanced technology. Like that. And you have to. And if you have to ask the price. You can't afford it.

**Chris Gammell:** That's right.

**Dave Jones:** You know. But. But these things are. These are real design requirements. In the industry. Right. That's why these technologies exist. Because there's. And this is just another. Neat little part. You know. It's not for everyone. As I said. If you've just got. If you can actually connect through to ground. Well. You just put vias down to ground. Right. No big deal. But if it has to be isolated. Wow. Sorry. I'm very excited.

**Chris Gammell:** Yeah. No. It's great. I mean. Are you doing any. Is this. Are you doing power designs these days? I just. I'm not.

**Dave Jones:** This is not for a current design. No. I got it.

**Chris Gammell:** Yeah.

**Dave Jones:** No. I'm. I'm not doing a current design. Where. Oh. Well. No. Technically. The micro supply. Cause. I'd be sure. Yeah. That's what I was thinking. Which will. Yeah. Which will link in. One of them was. Yeah. Trying to get. We. We designed a heat sink. Like a customized heat sink. I've done a video on that customized. Yeah. Heat sink. And that had to be thermally isolated. You know. And it's like. Yeah.

**Chris Gammell:** Yeah. I can imagine from like a. You know. A safety perspective as well. You know. It's good to be isolated. That kind of thing. So. Yeah.

**Dave Jones:** Oh. Yes. Of course. Yeah. Even. Even if you could. Electrically connect it through to a heat sink. You may not want to.

**Chris Gammell:** Right. Yeah.

**Dave Jones:** Because it may be a high voltage. Like. You know. If you're in a. High voltage power amplifier or something. You don't want the heat sink. To be tied to high voltage. You know. If you've got a big switching. You know. A big. Switching. You know. High voltage. Main side. Switcher. Or something like that. You know. You don't. You may not want all the heat sinks to be live.

**Chris Gammell:** You know. Yeah. I. Speaking of high voltage. And things that I want to be near. I did end up watching those videos. We talked about last time. The 345 kilovolt. And the 34.5 kilovolt. Yeah. My God. Like. That is. It's a different world. That is something. It is totally a different. I'm like. Yeah. Yeah. I think the. The interesting thing to me about it was. Was. You know. You're watching it. So. If people don't remember. I'll link these videos back in again. So. Basically. It was a substation. This guy walking around. Just. Explaining what everything is. And. What's interesting about it. Is. He's. He's talking through all these things. And I'm like. Oh. Transformer. You know. Like. Yeah. Yeah. Relay effectively. You know. It's like all of these things. That have these very. Very common analogs. And I'm like. Oh. Yeah. I understand those. But these things are just monstrous. They're so big. No.

**Dave Jones:** You do not understand these. You do not understand how they. You think you know how a relay works. Well. I'm no. I understand the concept.

**Chris Gammell:** Yeah. Yeah. Maybe. How about this. I understand the block diagram. Maybe. Yeah. Of course. Yeah. But like. Yeah. The actual implementation. Like. A transformer that looks like that. Is nothing. Like. I've ever seen. I mean. It's just.

**Dave Jones:** No. Because it's. It's filled with oil. Because it needs to. You know. It's like. Yeah.

**Chris Gammell:** Yeah. Nothing I'm doing is filled with oil. Yeah. Maybe me. After like a plate of fries. That I eat or something. And you're like. I'm filled with oil. But that's about it.

**Dave Jones:** A lot of people ask. Like. You know. Where. Where. Where are jobs. In the industry. And stuff like that. Power. Big industry power. I'm. You know. That is. Because it's not sexy. Right.

**Chris Gammell:** Yeah. That was the other interesting thing. That was. So that was. That was tied to a. That was tied to a. Turbines. Wind turbines. Right. So that was like a substation for wind turbines.

**Dave Jones:** Oh. Yes. Right. And it's just. There's so much call for people knowledgeable in. You know. Really high energy. High power. Stuff. You'll never be out of a job. Like. And they pay. You know. Serious money. Right.

**Chris Gammell:** And the young engineers. They just go through them like. You know. Like matchsticks. So. You know. They just burn up right away. So. They're always looking for new ones. You got to keep filling that funnel. You know. So that when. Billy. Billy crossed the wires again. You're going to need a new intern.

**Dave Jones:** Oh. I. I. I don't want to. Definitely. I'm not going to search for it and link it in. But. I watched this video of this guy that was train surfing in India.

**Chris Gammell:** Oh. God. No.

**Dave Jones:** Yeah. No. Somebody filmed the whole thing. And he stood up. And. Yeah. You can guess the rest. My God. Oh. Thank you. It's. No.

**Chris Gammell:** Yeah. I mean the internet's full of that kind of crap. I don't need that. I don't need that stuff. Yeah.

**Dave Jones:** It's. Yeah. You do not want to watch it.

**Chris Gammell:** Yeah.

**Dave Jones:** Of what happened. I am interested in like the.

**Chris Gammell:** You know. It's a power delivery in terms of like. You know. It's a grid. Grid modernization in general. Right. I mean like the U.S. Is. Has some parts that are good. But like so much of it is just. There's so many. Old areas. And like. Like. NIMBYism. You know. You know that term. I'm sure you do in Australia. Right.

**Dave Jones:** NIMBYism.

**Chris Gammell:** Yeah. So it's an acronym for not in my backyard. So NIMBYism is basically like. People who like buy expensive properties. And like. Don't change anything. Don't let anyone. Yeah. Yeah. Yeah. Right. So it's like. That's a NIMBY.

**Dave Jones:** Don't build a nuclear reactor in my neighborhood. Well. Yeah. There's that. Build anywhere else. Just don't build it. But like.

**Chris Gammell:** It could even be like. Don't upgrade. Don't upgrade infrastructure near me. Because I don't want you to change my sight lines out in the backyard. Right. Yeah. Like that kind of thing too. And like. That's problematic. So that's kind of a problem. But there are some areas that are modern. But like. There's. Man. Certain. Like the. The logistics of doing that. Have got to be insane. You know. We. I don't even know. Who would get on the show. If people have suggestions on who we would get on the show. And or if they know people. That would be very. Very interesting. Because that is. Yep. So far afield from anything I've ever done with.

**Dave Jones:** I tried to do that. Because. Yeah. Just down the road from me here. Like literally. I could probably walk there. Right. Is. Is the main. Control headquarters. For the. Eastern Australia. Energy grid.

**Chris Gammell:** Yeah.

**Dave Jones:** Right. It's the main. It's the main HQ. Where they control. And I said. Hey. You know. I've got a big engineering channel. Can I come in? I've got a camera. Yeah. I've got a camera. And they went. New.

**Speaker ?:** Yeah.

**Dave Jones:** Even though. I looked on their YouTube channel. And they just let a whole bunch of students. Into film. In like. A month before.

**Dave Jones:** TikTok. And you know. Yeah.

**Chris Gammell:** Dave. You should have done some dancing. And then you could have gotten in. Right.

**Dave Jones:** Okay. Anyway. Yeah. Yeah. That's. I mean.

**Chris Gammell:** I think there are some like security risks there. And I get that. But. Yeah. I don't know how they would. I. I. You know that really.

**Dave Jones:** Gave them the opportunity to. Actually vet the footage. Before I actually released it. And they went. No. No. Just. That's too bad. Flat out. No.

**Chris Gammell:** Yeah.

**Dave Jones:** And they had a whole media department. Oh yeah. Like I talked to the person. The head of the media outreach department. And they said no. It's like. Well. What are you employed for?

**Chris Gammell:** I'm media. Yeah. Right.

**Dave Jones:** I don't understand why they have a job.

**Chris Gammell:** We talked to. Teletype operators. And also. Weekly periodicals. People really seem to like those. Pamphlet writers.

**Dave Jones:** Right. I'm sure they'd talk to Silicon Chip. You know. If they wanted to write an article. Oh well. Yeah. I mean.

**Chris Gammell:** Come on. Yeah. Silicon Chip. Anyway.

**Dave Jones:** Yeah. I tweeted it. Because there's. There's wire. There's fires in California again. Right. And the grid went down.

**Chris Gammell:** Right. Yeah. So that's. Like a brownout. So some of that is. They actually take down the grid. I think is a preparatory thing.

**Dave Jones:** They do. Andrew.

**Dave Jones:** maybe a government thing and they said oh you know it's due to one of the reasons why it's going down the grid's going down is lack of maintenance and i responded would go like and and everyone's going how do we fix this how do we fix this i'm going well hello i don't even need to answer like issues are caused by a lack of maintenance how do we fix it oh yeah i was like i thought there's

**Chris Gammell:** some punchline here other than the obvious one is the punchline yes it's maintenance is the answer right it is the problem and the answer yes yeah no it's it's true i mean it's because you've

**Dave Jones:** you've seen that helicopter footage right of the guys who actually clean the wires oh that stuff oh my god yeah oh that's that's insane i'd love to do that just once oh my god no wouldn't like so dave's

**Chris Gammell:** talking about is basically it's a bunch of chainsaws that dangle down from a uh a helicopter not chainsaws they're like rotating blades i mean like it looks like it's just a death machine really and it just comes through and it just buzzes no no no no no no they're they're they're very cool

**Dave Jones:** as well like they actually trim back uh you know trees that are going to overgrow the power lines and stuff no i'm talking about the people who maintain the lines they get they jump they crawl out like a helicopter comes right up next to the line they use a big stick to actually ground the you know or to uh equate to the equalize the equalize the helicopter to the you know three to the 500 half a million volt line and then they crawl out of the helicopter onto the line they put a harness on and they and they go along cleaning the inspecting and maintaining the lines i wow yeah like yep like it's a piece of wire you wouldn't think it'd need maintenance but yeah

**Chris Gammell:** it does i mean it's super high tensile and like yeah i mean yeah it's crazy yeah yeah you would want to do that really i mean is this like your adrenaline junkie thing oh yeah it'd be a yeah

**Dave Jones:** totally yeah i'd love to do a helicopter drop onto a power line that'd be fantastic okay well that's uh

**Chris Gammell:** the so for taking a tally here that's one person in the current conversation that would like to do that

**Dave Jones:** i'm sure it'd take a month of training just to get approval to you know it's not something that you could just do you know you'd have to take months and months of courses to you know and to even be

**Chris Gammell:** allowed to do it yeah have you ever heard that really bad country some people love it sorry but there's a i am the lineman for the county no oh yeah yeah i think oh man that's been like on playlist for me lately it's like so like maybe it's john denver or something like that but i don't know right yeah yeah it's it's real i'm not my not my shtick but uh it's funny that there's like

**Dave Jones:** it's like popular culture around it too i guess you know like right you know uh uh anyway that's job of the week yeah sure sure that's no it's a serious no seriously job of the week power big

**Chris Gammell:** industrial yeah power electric transmission i always had a lot of trouble with i i was uh what was i watching the other day maybe it was on the i think it maybe was on that that set of videos but it's talking about like delta and y configurations and stuff like that yeah it's made more sense over time but i just had like flashbacks to like the fundamentals of engineering exam oh yeah yeah

**Dave Jones:** they love asking about that stuff like you know we had to yeah you had to learn all that right you had to learn your delta y configurations and how to uh you know do the calculations to transform between delta and y and all that sort of stuff and it's like yeah i've never used it well yeah exactly i mean

**Chris Gammell:** people in the power industry of course do but like yeah of course it's it's bread and butter you know it's pretty rare when i'm not you know plugging something in that's not coming you know

**Dave Jones:** in the shape of a usb plug you know no as soon as you get to three phase i'm actually confused you

**Chris Gammell:** know like yeah what you know it's like right right right and it's all around us though you know like

**Dave Jones:** it's got to be so yeah of course yeah i just you know if you don't work on that stuff it's you know it's away dc even even ac you know like yeah that's a bit confusing you know dc right right right

**Chris Gammell:** exactly yes yeah like i said usb plugs good for me thanks right yeah uh well just sort of scale difference too i mean like we're a bunch of wusses well yeah i mean yeah there's that but like just the scale difference of like 345 kilovolts and you know it's just like megawatts of power and all that stuff and then like and then i'm working on stuff on my bench that like if i scuff my feet too much and i don't put on what's why don't put on my uh you know my my wristband uh you know i pop it yeah it's it's gonzo you know so yeah yeah speaking of bench uh how did the uh the move end up i guess

**Dave Jones:** we're we didn't get updated and it's still not complete because there were there were a couple of last minute boxes that came out that i had to clear out like at the last minute and they went and they went here i've yet to sort them so there's still a few boxes on the ground but i got my under bench storage yeah i saw that you know yep um you know it cost a pretty penny but i i for those who don't know like i you've no doubt seen i keep most things in tubs right yeah but but tubs are annoying because they've got lids and they stack on top of each other so to get something you know and murphy's law said mercy's law of tubs means that the thing you want is right at the back and right at the bottom tub right so you're gonna take them all out and you got it yeah right so it's annoying so i thought no for like everyday use stuff that i just need to pull like test leads and stuff right that i need little adapter things and other little gadgets that i need to like pull out every day i wanted a nice shelf in open trays that i just pull out the tray and there it is right yeah it's just no taking off lids no doing anything it's just you know so i custom designed these uh flat pack storage units with these tubs and uh yeah very nice nice it look nice yeah but i haven't saw them yet so yeah well i mean

**Chris Gammell:** that's the thing like when you get when you when you like that's that's like a weekend thing yeah when you pick up on that right you gotta like you know put on a put on a movie in the background and like

**Dave Jones:** you know just you gotta put a podcast on in the background and you know it's one of those i don't want to do it during like productive daylight hours kind of thing you know during work hours that's kind of like a yeah nighttime or a weekend kind of thing no i was so i was in the exact same

**Chris Gammell:** spot pretty well not the exact same spot obviously the scale was much different but like i just moved all my stuff from from my desk at mhub because i'm just going down to like just the you know the

**Dave Jones:** shared area so you're not at mhub anymore you're gone ski well i like i can go in but i don't like

**Chris Gammell:** have all my stuff there anymore right at home now and so you don't actually so you're not paying for a workbench there anymore yeah i'm not paying for like a permanent bench but i'm still like paying to

**Dave Jones:** access equipment and stuff oh you're paying for the regular access the regular access right that's

**Chris Gammell:** right right yeah not non-vip i can't actually yeah it used to be 24 7 access now i have to go in during working hours oh yuck oh really okay yeah there you go yeah so i had to make similar decisions and just i think the the forcing function was the same thing it was like oh well end of the month got to go move all my stuff home and uh yeah right and refactor then and uh yeah i i started my

**Dave Jones:** move like three months ago i thought oh you know i better start now and it was still a last minute scramble yeah it was literally 11th hour stuff like i was gonna dump a whole bunch of stuff and then people turned up at like with hours to spare you know but before it was going to be tossed and i didn't toss anything really everything was everything was taken so yeah yeah that's always

**Chris Gammell:** a tough thing too like the sorting process and just like the oh the some days the some days of it you know i just luckily i had i've had some stuff laying around long enough i'm like oh stuff that was like cluttering up my bench in cleveland i think i think it's time yeah right yeah yeah you're right how many years ago was cleveland you know yeah that was uh four and a half years ago so yeah oh that's that all okay yeah yeah but the the big thing on for me is like i think some of it is also just like mentally like i'm like oh chris it's okay to leave some some space unused it will get used eventually

**Dave Jones:** you know yeah oh boy yep all right let's get onto our list can we talk about this because it's a it's one of these things that you know is like i'm glad the service is available but then again i don't kind of understand where it fits into the scheme of things it's very niche anyway i know what he's going to talk about here yeah yeah exactly spark fun a la carte they call it um a la carte and it's a dave your french is impeccable here's the blurb at the point and click your way to a fully populated custom printed circuit board from spark fun click here to get started now it's like um so they will actually design your board for you yep am i right because it's sort of kind of kind of sorter

**Chris Gammell:** yeah yeah so there's another so like basically it's a they have all of their stuff as modules in yeah you know a cat pro i think they use eagle still and basically i think it's like you're kind of you're using it's almost like a like a selector it's like a pulldown program effectively and like there's yeah right however many branching options there are it's it is a it is a reasonable amount of things that can be hooked from one to another and basically you're selecting all of the things that can be selected and then it's going to auto place those and off you go so basically it's like kind of you know spark fun obviously sells a lot of great modules they're kind of small breakouts for chips and things like that the way i kind of think about it is like they they have these boards and they're just kind of putting them all onto one board for you and yeah that's that's kind of the

**Dave Jones:** main thing yeah i it's somebody mentioned this it's kind of like for somebody who designs a gadget for burning man and they don't really know anything about electronics and but they need like 20 of them and they don't want to hand wire 20 of them and that's kind of the market for it and that's about the only market for it perhaps you know i'm exaggerating there a tad but it's not a big

**Chris Gammell:** market yeah i think it's it's all low you know it's all low frequency low power signals right so like from that side of things it's yeah it's stuff that would be just as good if you did wire it point to point or through a breadboard or whatever like it's not like you're you know i don't think any of the modules are going to be anything high speed other than you know maybe you know i know one of the modules you can put on there is like a esp so like yeah that's got rf subsections on on the chipset or on the module but that's not that's not dependent on how it's laid out yep can you like

**Dave Jones:** define the size of the board the footprint because like this is not a really a fully custom pcb design service they are not going to design a fit to envelope pcb for your you know fancy looking you know smart watch for kickstarter or something right this is that's not what this is right i agree yeah

**Chris Gammell:** i think that yeah you have to go to a a consultant a real pcb designer to do this and it's what is it 995 or something yeah half off for the first year i think or the end of the year so but yeah that's so

**Dave Jones:** it sounds as to some that sounds cheap to people who know about this sort of stuff yeah if you hire a professional pcb designer 995 bucks is cheap right but to others it might seem oh so expensive

**Chris Gammell:** you know yeah i think i think if you took so i think it really comes down to like activation energy right so like if someone is used to buying from spark fund and they're buying modules and they like it they're able to hook things up and they're like oh look an option to just move forward and like you said build 20 of a thing and like building 20 hand-wired prototypes is not trivial that's you know like a lot of things go wrong with that yeah so like from that perspective that's great and i think that that's actually a great use case for the service i think if if that same person knew a little bit more about what they were what the potential output was you know they would just easily be like i'm using these six modules from spark fund they'd go on upwork or similar and be like hey can you take these files and push them on a board with this form factor and like it would probably be about the cost of this but then you know spark fund's going to make this board for them too so

**Dave Jones:** like there are benefits to this is that included in the cost is making the board included in the

**Chris Gammell:** cost or no i mean it's just the layout this is just i think the board the board might be i don't know if there's a flat charge for the board that might be included because boards are dirt cheap these days yeah exactly and i think i think there's so there's a price when you go through the the actual menus there's like prices on each module and it's a little bit less i think than the actual module itself that it would buy so i'm i'm not completely sure on that i've only gone i've gone

**Dave Jones:** through it like once so yeah i haven't got i haven't even gone through it so yeah it's where it's

**Chris Gammell:** worth going through it i think it's interesting all right what someone brings up in the uh the subreddit comments is something that my friend yours had told me about it recently but uh gumsticks has a very advanced module it's called geppetto so geppetto.gumsticks.com is like a competitor i guess but so i had heard about this because they already have like raspberry pi 4 c the cm4 like we talked about i think two weeks ago the uh the module and then we talked about it last week with jay as well and it's like basically breakout boards for something like this and it's kind of reconfigurable it's got some 3d elements to it and like basically you you see everything like this is a much much more uh advanced version of the same kind of idea so if you're building stuff and you're not using raspberry or sorry you're not using uh spark fund things then this might be a good option too so if you're in that builder section of things of course chris is going to going to it suggests that you should learn ki cad you know that would obviously be the best solution but you know that's yep whatever uh and that is i think the best solution but that's that's that's actually pretty big some people just

**Dave Jones:** don't want to like it costs you more than a thousand if your time's valuable cost you more than a thousand dollars to learn how to use ki cad right just in time right i'm i'm actually going through this now i've i've selected my controller you're allowed to select one controller like an atmel or or whatever it is uh then you're allowed to select components i've selected a couple of switches and things and other modules and then you can select connectors and you know it's it's pretty limited i mean it's you know i've only got a couple of types of connectors i'm trying not to judge it too much

**Chris Gammell:** right now you know what i mean like it's it's it's a new service yeah yeah it's a new service and they

**Dave Jones:** can add things later you know you know if you had a thousand different types of connectors you go oh

**Chris Gammell:** okay this is getting serious right and i think one of the things that they're offering here is a you know there's a limited uh ecosystem anyways right it's people that are like deep in the spark fund side of things and yeah yeah so probably not our not most of our audience but maybe but no most of our

**Dave Jones:** audience wouldn't it would be interesting wouldn't have need for this yeah because they'd actually design their own but yeah yeah no i'm i'm sure there's a niche for it but it's not yeah it's it's not magic there was a quite a bit of hoopla oh look get a custom pcb design for 995 bucks it's like

**Chris Gammell:** not really kind of even if if you found someone like in a you know lower cost country that is doing it for

**Dave Jones:** 50 50 bucks that's like 20 hours you can lay out your board for 50 bucks yeah sorry 50 bucks an hour i meant sorry oh i had 50 bucks an hour yeah like 50 bucks an hour like you know like and there's some

**Chris Gammell:** places that'll that's you know going wage and that's great and like good engineers that'll do that sort of thing and it's like all right that's 20 hours like i you could get a pretty good design in 20 hours i think so but again it's that activation energy are you going to go and source that person yourself deal with it what if it goes wrong whereas this is a probably a known thing yep so but a lot

**Dave Jones:** of people don't know how much time and effort goes into producing a real top quality complicated pcb for a real product that requires fit to envelope design and stuff like that you know i've i've worked a month on a pcb right and it's not because i'm slow it's because there's a multitude of one component

**Chris Gammell:** a day folks that's all he'll do it's like he's like no no i'm taking my coffee break i'm taking my 15

**Dave Jones:** anyway yeah news did it did straight off the teletype from the new york times in their new york times font oh can we can we like yawn it's like somebody's buying somebody but i don't know i don't know what

**Chris Gammell:** you're talking about here yet so i'm getting there this is pretty big amd oh that agrees to buy

**Dave Jones:** xilinx for 35 billion dollars in stock boring is there anyone left i know right by i mean who bought um the out altera um the yeah who the hell bought out altera intel intel that's it yeah intel intel bought altera you may have heard of them amd yeah i just you know and now amd buys xilinx of course

**Chris Gammell:** you know yeah yeah pepsi pepsi battles coke xilinx battles altera you know like yeah and um intel battles amd it's like yeah okay rc cola is over in the corner just crying just crying who bought arm rc cola you know no i'll say no no idea about rc cola royal crown no uh that is uh softbank had bought arm previously and then that's right and then they sold it recently to nvidia nvidia that's

**Dave Jones:** it nvidia yeah that's right it's just i can't keep up we we haven't been able to keep up for the last

**Chris Gammell:** decade let's admit yeah i mean these i think you're right though it is kind of it's big fish eating bigger fish well not bigger fish eating big fish because all the small fish have already been eaten

**Dave Jones:** oh boy anyway i don't think i don't think this impacts us i mean i don't use no it doesn't change if you're a xilinx fanboy and you use xilinx every day it's not going to change right anything really unless they get in there and sharpen their pencils and parts get deprecated and oh well yeah yeah i don't but they've got to honor existing contracts you know so it's not like you know you buy you know amd buys xilinx and then xilinx originally had a 10-year contract to supply this part to some military uh vendor it's not like amd can go oh sorry no you you know you buy the baggage that comes with that that's right that's right so yeah i wonder about the emotional toll not

**Chris Gammell:** the emotional toll but like the so like i remember like people talking about emotion of toll of the xilinx fanboys well yeah i mean like so i i remember like i think when i was a key fleet like one of the guys told me like oh it'll always be burr brown to me you know like the ti it may be ti maybe it's

**Dave Jones:** you talking about i don't know someone's talking about that yeah i was a b i was a burr brown fanboy

**Chris Gammell:** yeah of course yeah they're great parts right but like i i never really felt that and then like you know now linear tech is a analog devices company well yeah and like but you know like it's just the thing you know and then you kind of get you know you get attached to it that's really the only i think that's the only thing that really impacts me is like yeah if they start you know like so like altera is sorry uh yeah altera is now intel fpga right so like or altera intel fpga or whatever it

**Dave Jones:** actually yes i don't think did they drop the name entirely or they're in the process of dropping the

**Chris Gammell:** name the i think they're i think they're well on the way to just being intel i mean and if you think about it like it makes sense from a brand perspective of like intel's a pretty pretty strong brand oh yeah

**Dave Jones:** and whatever oh yeah here we go um intel.com oh yeah whatever happened to atmel are they still atmel are they trying to rebrand a microchip parts because that's been a couple of years now hasn't it

**Chris Gammell:** i think so the easy way to do it is you just search on the terms here and so i just search for atmel and microchip.com pops up so there is no atmel.com anymore it's just going to be yeah right it's just you know so like that's that is the modern day equivalent of how are they still

**Dave Jones:** branding you know i mean the part number is going to be the same it's still at

**Chris Gammell:** right and that's usually what survives yeah i mean that's that's how you can tell the old the only thing that's parts like the bq family and the stuff and yeah exactly yeah so all of that

**Dave Jones:** survives so the you know the nat semis and the yeah exactly yeah yeah yeah yeah oh that was lm right that was national semiconductor lm something yes lm yep yeah um yeah i but i think eventually they're

**Chris Gammell:** all just going to get subsumed by the by the the main brand and right corporate silliness

**Dave Jones:** yep oh to be in a big corporation again so if i go under microchip here i'd be surprised to actually see the atmel name now product offerings there's atmel start but that's because i think that's the

**Chris Gammell:** actual tool that's like what comes up but yeah i think it's all it's all becoming one chip it's going to be really interesting david what are we going to talk about about 10 years when it's just like hey did you see the new part from chip company yeah exactly oh it's here we go i've got it it's

**Dave Jones:** just pick an avr there's no mention of atmel it's just oh they're avr parts so there's the pick line and there's the avr line of microchip parts yeah so it's i think that's how they've done it so which is smart of course you have to because that's what people oh it's an avr processor it's the avr architecture it's you know like you can't just suddenly oh go oh it's a pick you know because a pick is a different architecture than avr it's yeah yeah so yep oh boy the worlds are changing my friend oh don't i know it man we've been doing this shit for too long it's like well we haven't yeah it's been a while

**Chris Gammell:** i uh so to give an update on a long ago thing so i i'm going to be working from another location uh in a couple days and uh you remember the portal lab portal lab never really made it off the ground yes yeah you know but i do have uh like a subset of different things i take with me now and like so i have a pretty good setup uh that i take with me that i'm going to be taking with me on this short trip you know it's like jlink programmers and you know the yeah tsa is this for a client thing is this a client yeah it's like an on-site thing i have to do and um but like having like all the measurement equipment it's just kind of all shrunk down and i i just really like that trend and i kind

**Dave Jones:** of hope that yep that continues because are you taking a real scope is there a real scope in there

**Chris Gammell:** or you know well it's gonna be analog discovery but i i really like those so yeah i mean and like

**Dave Jones:** most of the things i'm real scope you know what i meant by real scope yeah i mean yeah there's no

**Chris Gammell:** there's no knobs it's you know no built-in screen or anything like that i think it's uh yeah it's definitely a pc scope and it's low low you know 30 30 megahertz but like for what i do it's it's fine

**Dave Jones:** how would you define a real scope a real scope is one that sits on your bench yeah yeah it's form factor it sits on your bench you know yeah it's a square you know it's a rectangular box and it has a big screen that has knobs and buttons and you know um i i would even go so if oh i don't know if i'd use the word real but like it may be differentiated between bench scope and pc scope you know a bench scope because you can get like bench ones that are you know hardly that are all touchy-feely you know it's like the new tech one right it's all you know it's mostly touchy oh you

**Chris Gammell:** mean it's like touch interface you're saying yeah yeah yeah yeah so there's you know you can get more

**Dave Jones:** of that

**Chris Gammell:** and less knobs i have an interesting like requirement where i actually really like pc scopes and pc based uh microscopes as well it's kind of weird so i use this program called manic time which i don't think i've mentioned in here but i i kind of love it like i'm basically i installed spyware on my computer for myself yeah and it takes a screenshot every 30 seconds now and it tracks like hey are you looking at a browser are you looking at a whatever else and so i use it for consulting obviously to track my time and things like that it's like really really useful to the point where even i could not remember what i had done in a uh in a linux terminal like i'd like been typing commands in and i was able to go back to that day eight days ago and go to the time where it happened and i could see a screenshot of the the code i pulled up or the code i typed in so that was kind of crazy but like but the nice thing is like so now i put my microscope into just like a you know on on one of my screens and then i can actually capture like oh i was working on that board you know board abc on that day and i can actually like see like oh that's what i was doing that day or whatever and so the same thing with like scopes i can go and like capture not not that i need that for capturing traces but just seeing what i'm doing every day everything's kind of like on the screens

**Dave Jones:** it's almost like a proof of work show me that you you know you could go well here's an animation of 30 second screen here's a one-hour animation of 30 second screenshots go for your life oh i i have no

**Chris Gammell:** fear of like ever proving my time like i can totally do that right for everything i do and that's not the reason to do it it's actually it's like really it's really just a great program yeah it's interesting because like that plays into then like having a you know having this kind of microscope versus uh you know there's obviously many better ways to do it but um yeah it's just a it's a nice silver lining i think that's how amp hour dude did you end up listening to the last amp hour or no or is that

**Dave Jones:** still on your no i haven't listened to it yet that'll be a uh i i only put podcasts on yeah that's an

**Chris Gammell:** organizing lab podcast yeah yeah it's a good one uh i i listened back to it just to hear what jay was talking about i definitely it's on my list of you know like i i think i said on the show like my ever-growing list of things to learn but like building my own linux system i'd like to do that within the next year i think that's that's doable yep hold me to it dave okay all right all right well good luck with your uh continuing lab organizational tasks yeah it's good i handed

**Dave Jones:** back my keys the other day so it's oh yeah that's yeah that's yeah that's the right step yeah i'm enjoying saving the money you know i can just i can just feel the cash washing over me now you know

**Chris Gammell:** that i was pissing away before can i borrow like 20 bucks i hear you i hear the flush right now you

**Dave Jones:** know yankee bucks or uh either one's fine yeah all right oh i got 20 aussie bucks here yeah well all right vastly superior to that cotton rubbish that you guys yeah i agree all right all right man

**Dave Jones:** catch you next time you just finished episode 516 of the amp hour courtesy of our patrons join the club at patreon.com slash the amp hour or if money ain't your thing throw us an itunes review we love it all a special thanks today to our corporate sponsor bideo who now sell the pc bite grippy proby goodness for your bench you

**Speaker ?:** you
