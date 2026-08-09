---
episode: 727
title: Boat Anchor Warehouse
url: https://theamphour.com/727-boat-anchor-warehouse/
---

**Chris Gammell:** This The Amp Hour Podcast. Released July 1st, 2026. Episode 727. Boat Anchor Warehouse.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEVblog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Dave Jones:** What's up, nerd?

**Chris Gammell:** Oh, you know, clanker this, clanker that.

**Dave Jones:** Clanker?

**Chris Gammell:** That's what I call AI LLMs, you know, like the clanker.

**Dave Jones:** Oh, right.

**Dave Jones:** Yeah, can we like try and avoid AI topics? Sure, yeah, we can avoid this. You know, because I've told you about the AI data center they're building in my business park here. Yep. And it's like, you know, I walk right past it, right? And I was just thinking, like I was walking past it last night and I thought, like, and I'm looking, like the generators, the actual diesel backup generators and every, like the cooling units and everything are right there. They're like 50 meters away from me on, you know, this nice little nature park. There's cranking diesel? Is that right? Well, no, because it's not operational yet, but I can see them. They're physically installed, right? And they're right there. You'll be able to smell them soon, too. And I don't see them soundproofing. Well, yeah. And I'm wondering, should I actually, well, the answer is yes. I shouldn't actually go and measure the sound level there at different various parts of the day before they install the data center. So it's like, because like if they turn on those diesel generators, I reckon like that's just going to be nuts for everyone. Like it's literally like a hundred meters from another commercial office building that has like a restaurant there with like an open air, you know, like balcony that people sit on and stuff. And it's like, my God, if that thing starts up, I can't imagine. Because all I hear about is people who live, you know, even kilometers away from data centers. They just got like, they just can't stand the noise. Yeah. Because they're constantly, I have some inside knowledge on this. And yes, they do actually run the data centers from the diesel backups.

**Chris Gammell:** Like continuously. Yeah, yeah, yeah. Yeah. We talked about that last time, the behind the meter, right?

**Dave Jones:** Yes. Yes. That's it behind the meter.

**Chris Gammell:** Yeah. Well, I mean, in a positive light in the clanker realm, I have actually been running local models. And that's been an interesting and enlightening experience. Mostly in like, it really resets your expectations. So like, I have Gemma 4 running on. You're right. Well, so I have also, I have a moderately powerful laptop. I have like the new Strix Halo 395. Nice little laptop. Nice processor. That's like an AMD processor with a integrated graphics card thing, whatever. So it's kind of all there, but it's got the, so like the big thing is, so like, again, these are things I'm learning. Like if you have unified memory, that means you have like a chunk of met RAM, like 32 gigs in my case. And you can say like, oh, I want eight of it to go towards graphics and eight of it to go toward 24 towards system rather, where you could turn that around. You could say 24 times towards graphics and eight towards the system. But then that's pretty tough with like a browser open, like eats through eight gigs pretty fast. What that really means though, is you can, and you can do some dynamic scaling too, but in the case of this, and that's why like a lot of the Apple platforms are popular as well as like high bandwidth shared RAM like that. You can like dynamically allocate it to a, to a model. You can have like, like a model on your computer and then you can just directly talk to it. So I've been running, so I'm able to squeeze in the Gemma four, which is the Google deep mind model. They have a, they have like a two, a four, 12, 26, 31. Those are like the sizes of the parameter models and they can do different things. There's also different quantization layers. Again, levels rather. I'm learning all this stuff. And so basically I found the one that I could like just barely squeeze in there and got the memory configured. And basically though, then I'm just directly interacting with it. And then I point Hermes, which is like a open claw, like a slightly different, slightly different open claw style orchestrator agent at it. And you can basically just use it. Like you would use maybe like a cloud code or similar.

**Dave Jones:** Well, that's what I was going to ask for those who have not done it, including myself, all this local model, you know, stuff, which everyone's crapping on about. Yeah. Like what does it ultimately give you? Does it give you the equivalent to a chat GPT? Does it give you the equivalent to a clawed? I guess it depends on what models you install, right?

**Chris Gammell:** Yeah. I mean, I think it's kind of like, uh, like a, you think about the clawed code, like a desk, the clawed desktop, right? That's like, that's like kind of like the equivalent, like having like a Hermes, right? That's like a, that's a harness. That's like a kind of all the, the niceties around it, you know, like memory and handling all these things. You can use it to code. It can code. Yeah, exactly. Yeah. And like when I talked, when we talked about open claw on here too, I was like having it write some code, but that was not talking to my local computer. That was talking out to open router.

**Dave Jones:** I was going to say, can it actually access the internet or like, right. So you can get it to search for latest stuff and things like that or.

**Chris Gammell:** Exactly. Yeah, exactly. The bigger limitation is just that it's like, so that's when you start thinking about like context windows. Again, people are probably snoozing if they're like, Oh, I just want to hear about frigging resistors, Chris. But you know, context windows really fill up fast, right? Because every time you're sending a message into it, you're actually sending all the messages back into it and that sort of thing. And so you really get to know the limitations pretty quickly. And so that's what I'm learning. It's, it's amazing. It's amazing. Like I posted a thing on my blog about this, but it's just like, it posted something in like in Ukrainian and I was just like, what the hell? Like, did this just glitch out? It's like, no, it was just being cheeky. And it was posting Ukrainian. And then it turns out though, like these models that are running on your computer, really running anywhere. They have different languages baked in. It's just like, Oh, Oh yeah. Okay. It just like knows Spanish and it knows Ukrainian and it knows, it knows how to understand Australians even, which is really the hardest thing.

**Dave Jones:** If I had a need for it, I was thinking about, yeah, trying to muck around with a local model of some description, but you know, I have to have a need before I go waste time on it.

**Chris Gammell:** Yeah. I think that's right. And, you know, and, and what I've, you know, kind of come back around to is just like, so now if you don't want to do it low, you know, like locals, it's first off, it's very, very cool. It's amazing. It's possible, but it's, it's slower. It's power intensive. That's fine. Whatever. But it's just like the expectation. If you're used to like a cloud code or, you know, an open chat GPT desktop or something like, it's just like the speed is so insanely different that like, you really have to change your expectation.

**Dave Jones:** Right. But that's fine for a lot of purposes. You can go and write, go and go and write this code. I am going to lunch and you come back and you know, it's, it's kind of done.

**Chris Gammell:** Or a lot of the things with like open claw Hermes, those things too, as well. It's like, it's all cron jobs, right? So cron is like a scheduler. It's like, that's what I was really doing is like waking up on a schedule and be like, Oh, I should go check the internet for, or this, this thing, you know, like go search for EV blog every Tuesday morning and, you know, put a report together and tell me about it. And like, yeah, that's, it doesn't have to go fast. It just has to be consistent and, and the consistency is its own thing. It's its own hard thing. So.

**Dave Jones:** All right. Can we not talk about AI anymore?

**Chris Gammell:** That's it. That's all the AI stuff. I wanted to call out a new part that I found the CH 224.

**Dave Jones:** CH 224. That's familiar. Yeah. Is that a, it's a, yeah. Yeah. I thought it was a USB chip, isn't it?

**Chris Gammell:** It is exactly. So it's basically, you know, you, we have all these USB C things that are out there and this is far from the only one that's out there, of course. But for me, it was like, Oh, USB C and USB PD and all these different modes and whatever. I'm like, Oh, I just, I don't know how to do any of it. I don't want to like write the code. And it's like, actually you can just buy a chip that does it.

**Dave Jones:** Uh, of course you buy a chip and they're so good that you don't even have to. Well, I don't know. Is that the same? Is that for this one? But you don't even have to program them anymore. Basically it's a USB power delivery chip that can negotiate USB power delivery on your behalf. And you don't even have to program it. You just hook it up to some dip switches or tie some pins and you get your voltage.

**Chris Gammell:** Exactly. It's like, Oh, we've ever wanted, you know, like it's all that we've ever wanted, but this isn't you.

**Dave Jones:** I'm sure it's, um, I'm sure we talked about it before. I'm sure. Well, we've talked about other USB power delivery chips and you just tie some pins and it negotiates the power for you. Does it automatically negotiate the next one down if it can't do the, well, it's like a request response kind of thing.

**Chris Gammell:** So like it defaults to five volts and then it's like, okay, now I'm like, you change the dip switch. Like you said, you switch it to the, so it's like, uh, I forget what the, there's like a one, two and three, like bit, bit set. And you like turn off. So like one is on by default and that's, you pull that high and that's five volts. Then you pull that, you pull the pin one low and you turn on pin two and that's going to be like nine volts. Okay, fine. It's going to go out and like start querying on the line and doing that negotiation saying, Hey, I want nine volts. And if, if you have a power supply that can't do it, it's just gonna be like, Oh, it can't, it's reporting. It can't do it. And it's not going to give it to you.

**Dave Jones:** How do you, you, uh, sorry, I'm not looking at the data sheet. How do you actually trigger it to do that? I know it'll automatically do it on power on, but then can you trigger it when you change it? If a user manually changes a dip switch or can you, is there a pin that you can trigger it?

**Chris Gammell:** That the dip switches would be like, so these pins one, two, three, it would basically be the, that would be the dip switch. There's also pull-ups of different values there.

**Dave Jones:** Yeah, but after you've negotiated 20 volts, for example, can you then change the dip switch back down to five and it will detect that you've changed the switch and it'll renegotiate?

**Chris Gammell:** That's right. Yep.

**Dave Jones:** Oh, okay, cool. That's all we've ever wanted.

**Chris Gammell:** I know, right? Exactly. And there are like different versions. And so there's an A, a K and a Q and Q is, this is a WCH part. So it's, you know, LCSE and the CH32 V003 folks that are making this, but the Q actually has registers and you can do more like fine grain controls. So PPS is like, you can do like 0.1 volts. Yeah.

**Dave Jones:** I actually reviewed a product recently that did this and you can set it in 0.1 volt.

**Chris Gammell:** Oh yeah. Yeah. The werewolf, right? That was the one you did?

**Dave Jones:** Yes. Yes. The werewolf thing.

**Chris Gammell:** Yeah. Well, Luke was on the show not too, not too long ago.

**Dave Jones:** Yeah. It's cool.

**Chris Gammell:** Yeah.

**Dave Jones:** And I've mentioned it before, like back when we were designing the micro supply, you know, these chips did not exist. Like you had to rule your own and it was, oh my God.

**Chris Gammell:** I think that's what, I think that's what was in my head. Honestly. I think that's what was like rattling around in my brain. I'm like, oh, I remember Dave and David, like the STM 32 and all that stuff.

**Dave Jones:** Yeah. Yeah. Yeah. STM 32 to drive the, oh, and like there were chips that did USB negotiate, USB power delivery negotiation, but you had to program them. They were actually little processes and you had to, you know, like it wasn't just strapping a pin or, you know.

**Chris Gammell:** Well, I remember too, like it was like not a lot of stuff was PD back then as well. Like, I mean, how long ago was this at this point? It was a while, right?

**Dave Jones:** It was early in the power delivery days. Yeah. Yeah. Now it's like, oh, it's just expected. Yeah. Yeah. Yeah. It's crazy. Oh man. I don't think this is the only one that actually does this. Oh no, no, no. I'm sure there's other.

**Chris Gammell:** One of my friends pointed me at like, you know, like a six, the SOT 23-6 or something like that. You know, like it does not take a lot to do these sort of things.

**Dave Jones:** Exactly. But even an SOA it's fine, you know, but if you need something, you know, tinier, then by all means. And I'm sure you can get them as a chip scale package too. You know, if you ask the manufacturer, they'll sell it to you and you can just bond it into your shoe phone PCB or something. Yeah.

**Chris Gammell:** And I think the reason these guys are doing it. So I was looking at the CH32X033 and X035 and that same stuff is built in, right? So basically I think what they did is they probably either binned some parts or they just ripped out the front end. So that was basically a micro plus USB PD negotiation. And so basically it's like a thing about a micro that had this kind of built into it. That's the X033 and X035. So that's what I was looking at initially. And I was like, well, that's a lot more than I want. The chip's more, whatever. And I was like, surely there's something else out there. And so I was like, yeah, of course there is.

**Dave Jones:** I reckon USB power delivery is a huge innovation. It's just so useful for everything. Like being able to go up to, in fact, people think that it stops at 20 volts. It doesn't. It can go up to 48 volts.

**Chris Gammell:** Yeah, it's up to, I think, 140 watts is the new limit for the PED 3.2.

**Dave Jones:** Yeah, it's the new limit or something. But yeah, and it can actually go down to three volts, I think, as well. But most power supplies, even the one Werewolf actually provided me, could not do the full voltage range, right? And their main product is bragging about this. So it's like, yeah, there's so few manufacturers of an actual USB power supply that can actually handle the full range of what the standard is capable of. So, yeah, it's just.

**Chris Gammell:** Yeah, I mean, it's not an easy thing to do. And especially if, like, you think about, like, there's dynamic loads coming, you know, so they're trying to regulate them. But they're also regulating across inductance, across the wire, whatever.

**Dave Jones:** Yeah, designing a power supply that's capable of, you know, three volts to 48 volts at, you know, high efficiency over the full current range is, you know, just sort of, yeah.

**Chris Gammell:** I remember you had one of the early reviews on the USB. So the TS-100 was a non-USB PED. It's not going to go there. The TS-80 was the, was like the first, one of the first ones that was like USB-based, right?

**Dave Jones:** The TS-100 was the first. I think the TS-80 came afterwards. Yeah.

**Chris Gammell:** Yeah, but 100 was not, that was a separate power supply, right? That was not USB, I don't think. Maybe I'm wrong about that.

**Dave Jones:** That is correct. That was not USB, I think. That was a DC barrel jack input. Yeah.

**Chris Gammell:** Yeah, yeah. I think. Yeah. But, I mean, I was on Amazon the other day talking to someone. You can buy, like, a, you know, $40, you know, I think it's a clone of a clone of a clone sort of thing. Like, they're just so cheap these days.

**Dave Jones:** I've got, like, four different types of them sitting here. The bloody manufacturers just keep sending them to me. They're, they're. Oh, yeah. Yeah. Yeah. I'm just, like, going, well, no, I'm not just going to review yet another, you know. Yeah, right. What is the differentiation here? It's like, yeah. Yeah. Yep. That's crazy. Anyway.

**Chris Gammell:** You should see which one can start, like, a campfire first with a USB battery pack.

**Dave Jones:** Yeah.

**Chris Gammell:** Well, then you can, like, you know, if you were going on vacation, you're going camping with the family, it's like, all right, now it's a business trip, Dave.

**Dave Jones:** Right, yeah.

**Chris Gammell:** Write that off.

**Dave Jones:** Dude, when you're a YouTuber, everything's a business trip. Everything's content.

**Chris Gammell:** I'm telling you. Everything's content. Everything's content.

**Dave Jones:** Simply set up a YouTube channel and set up a business title that YouTube channel and you can claim everything.

**Chris Gammell:** That's right. Next up, you've got to become, like, a food critic or, like, a travel blogger, right? Right. Yeah, yeah. Yeah. You did the restaurants for free. That's the real, that's the move, you know.

**Dave Jones:** Yep. But you just go, oh, we're just discussing business, you know. It's like, yeah.

**Chris Gammell:** All right. Well, not only are you discussing business, then, of course, the restaurants, like, also, like, well, we want you to have a good review. Oh, boy. What a time we live in. What a time we live in. Yeah.

**Dave Jones:** All right. Can I send you, I want your reaction. You don't know about this, I don't think, because you don't follow me. You don't use X anymore, so you would never have seen it. I don't. All right. Here we go. Check out your chat. I want your wholesome reaction to this. It's a video on X, but I'll link you to a web page after this. I just want your reaction to this.

**Chris Gammell:** Oh, my gosh. This is a production log. PlayStation 2 making steady progress. Looks like they are doing cardboard versions of the entire thing, like a miniature.

**Dave Jones:** Yes. It's a cardboard. It's a paper artist. Who is manufacturing tiny letters on top of SMD capacitors. And then he builds like an entire PlayStation. Let me link you in. His website.

**Chris Gammell:** I mean, this is art, Dave. This is beautiful.

**Dave Jones:** Well, I'm kind of into art.

**Chris Gammell:** I didn't know this.

**Dave Jones:** I'm a paid modern artist.

**Chris Gammell:** You're going to have to qualify that one, please.

**Dave Jones:** I have sold a modern art piece that I created. You weren't aware of this?

**Chris Gammell:** You might have to remind me. How about that?

**Dave Jones:** Well, I found a printer in the dumpster, as I do, you know. Sure. And I was using it for years. And all of a sudden, it started to fail. And it started to produce all these, like the toner was just going wacko all over the page. Right? And so we'll try to print a map of one of Sagan's board games or whatever he had. And then it came out, like we tried to print it on a big A3. It's a big A3, you know, full color printer. And it produced these amazing color patterns on it. So I thought, uh-huh. I'm going to say, it looked like a modern, you know, when they sell, you know, a blue square, you know, just some squiggles on a wall for $20 million. Of course. Right, right, right. And they just give it some bullshit description of modern art, right? It's all bullshit. But I decided, right, I'm going to write up a wanky description on this. And I'm going to whack it on eBay as an original modern art piece. I signed it and everything. Numbered it.

**Chris Gammell:** And so this is not Dave Jones, the YouTuber, selling art. This is just random artist 1234?

**Dave Jones:** Oh, no, no, no. This is me. I sold it on my eBay page. And somebody bought it for a couple hundred bucks. Wow. And I sent it to them. And I wrote this wanky description for it of what it meant and, you know, everything. So I'm officially an actual sold modern artist.

**Chris Gammell:** There you go. Yep. All you need is a dealer now, you know, like those art dealers. That's a very tight-knit community. So, yeah.

**Dave Jones:** That's it. Anyway, look. Oh, no, yes. I sent you the webpage.

**Chris Gammell:** This is gorgeous.

**Dave Jones:** Look at this dude.

**Chris Gammell:** Yeah.

**Dave Jones:** Look at this dude. The artist's name, if I get a prayer, he's a Japanese artist, Manabu Kasaka. Manabu Kasaka. And he actually creates one-to-one scale replicas of everyday objects. But they're mostly like retro radios, retro, you know, gizmos. Like there's a Walkman. There's like a PlayStation, you know, and like a Wii console. Like a...

**Chris Gammell:** Yeah. Or Super Nintendo. Yeah. Yeah. I mean, like he's doing even like the wavy PCB traces. Yeah.

**Dave Jones:** Yeah. And he does all the individual letters on the components. He cuts them all out by hand, dude. This is... I want to commission this guy to like make a piece for me.

**Chris Gammell:** I mean, what would you ask him for? What would you...

**Dave Jones:** I don't know yet. I maybe like... I don't know. Make me a flip.

**Chris Gammell:** I think his magnum opus would be like the inside of like a tech scope or something, you know? Like an old tech scope.

**Dave Jones:** Oh, yes.

**Chris Gammell:** Yes. Yeah.

**Dave Jones:** Yes.

**Chris Gammell:** Like have like replaceable card slots or something, you know? I mean, this work is fantastic though. This is very, very good. I'm glad you're impressed. Yep. I'm just so impressed with people that have that like level of meticulousness generally. Yes. You know? Like I just... I don't have it. I don't know how to do it.

**Dave Jones:** Spend hundreds of hours on one piece, you know? Yeah. It's like, it's just... Yeah. Yeah. It's phenomenal. Anyway.

**Chris Gammell:** Yeah, we'll link on that stuff.

**Dave Jones:** We'll definitely link it in down below. You've got to check it out. Your mind will be blown. It's just... Yeah. That's really good. If you don't follow me on X where I've posted it. All created out of paper. And it's good because it's in our genre, right? It's in... I know.

**Chris Gammell:** Yeah, yeah, yeah. It counts.

**Dave Jones:** We could talk about it here. I know. It's like little individual pots, like, you know, and wires. It just makes them all out of paper. Oh, gears and cogs for printers and speakers and... Oh.

**Chris Gammell:** Closest I get, Dave, is 0201s. I finally... I mean, I think I talked about this last time. I've been, you know, slowly making my way and finally got this thing programmed. It actually is a Bluetooth device. There was not any certainty of that. It does light up. I'm driving the buzzer at the wrong current, unfortunately. So it's like a not very loud buzzer. But, you know, it's so tiny. You know, and I'm also like in the depths of like, as you're programming, you're like, oh, that pin was not able to do what I thought it was able to do. So I'm slowly learning that sort of thing. I have some Rev 2 changes, you know. Okay. But it worked, huh? Yeah, it's mostly working. I got the... I have it like set up. I have like an accelerometer on board and I have like 16 LEDs. Like there's an outer ring of 12 to be like a clock. And the inner ring is like around the accelerometer. There's like four there. So like outer ring is kind of like a coarse leveling thing. Inner ring is like a fine leveling thing. And then when it actually is level, then it lights up all 16. Nice. The way this thing is set up is like I need to... There's actually two boards. There's like a sandwich. And I think the next step is, you know, so if I do a Rev B, it would be like to make a flat flex, like a rigid flex. And I've never actually done that. Have you done that before?

**Dave Jones:** Rigid flex, yeah.

**Chris Gammell:** Yeah. I mean like so what are the inputs to that that is different? Like it's just like a different drawing layer and stuff like that? Because I don't...

**Dave Jones:** You can have it. Well, I don't... I haven't done it since they sort of like, you know, these newfangled online, you know, upload your Gerbers and they, you know, do it and they 3D model it for you. And they, you know, do all the bells and whistles. You could basically do it as any way you wanted to, as long as it was clear to the manufacturer that, yep, you'll do it as a separate mechanical layer, for example. And you would, you know, just use worded instructions saying, yeah, this is the flex part, this is the rigid part, and you'd have arrows and, you know, stuff pointing and things like that.

**Chris Gammell:** I just figured it's like one of the... So like if I do like a six-layer board that there's like some laminate, like seventh layer, seventh and eighth layer, I suppose, in there, that is the flex, right? I mean, like it just gets sandwiched in there.

**Dave Jones:** Yes. And you could call those, you could label those layers, you know, the flex layer and stuff like that. Yeah. And it's usually like they know what they're doing, right? You know, if they have any questions whatsoever, they'll come back to you and, you know, ask. But I don't know if there's any like standardized way to do it with, you know, your JLCs and your PCB ways and whatnot these days. I don't know if there's any. I haven't done one using them.

**Chris Gammell:** Yeah, that's great. If only one PCB sales rep would try and contact me on LinkedIn or otherwise, I just never hear from them. Oh, we did.

**Dave Jones:** That's the sarcasm to take to go. Yeah.

**Chris Gammell:** I think I'd probably reject four or five a day. I mean, it's just like there's so many people out there, you know.

**Dave Jones:** I don't get that many. I get very few these days. Even they're caught in my Gmail spam folder automatically, which I rarely ever check because it's just like.

**Chris Gammell:** I mean, this is mostly LinkedIn, just so you know. I mean, LinkedIn is where it all happens.

**Dave Jones:** The hell are you doing? And what? What the hell are you doing on LinkedIn, dude?

**Chris Gammell:** I don't spend a lot of time there, but I do, you know, I use it as like a network site, but you also get emails about people that are trying to do outreach. And sometimes there are some very valuable people that do outreach on there. For instance, you don't actually know this, but the show that we published last week, which is today, I talked to Massimo on LinkedIn first, and then he agreed to be on the show, and we talked all about Arduino, and like that was great. So he's on there, you know.

**Dave Jones:** Occasionally I'll get people, like I'll get an email saying, you have received a message on LinkedIn, and it's from somebody, you know, fairly prominent. And I go, oh, okay, right. Yeah, exactly. So like that, right. Yeah, but there are people who use it as a social media, and everyone, like everyone I talk to goes, oh, God, I hate LinkedIn. God, I hate LinkedIn. I don't know anyone who goes, oh, I love LinkedIn. Oh, oh, it's just so good. I can't spend 10 hours a day on LinkedIn. It's like. Yeah.

**Chris Gammell:** I think that if you do think that, and you don't like that part of your life, if you want to cut that out, because the thing is, you know, much like on X, there's a algorithm that's like there to, it's, you know, their job is to keep you there, right? That's what they want to do.

**Dave Jones:** Yeah, yeah, yeah, of course.

**Chris Gammell:** If you don't like that, they actually do have a chronological option. And when you start doing chronological, all things get better, because it's just like, oh, no new content. I guess I'll just go back to doing anything else in my life. You know?

**Dave Jones:** It's a, yeah, it's the same thing with X slash Twitter. It's like people complain about it, and they go, you're using the for you tab, aren't you? And they go, what's that? Yeah, don't do that. And they go, oh, just click the following tab, and you only get posts from people you follow.

**Chris Gammell:** Yeah, yeah. Yes.

**Dave Jones:** It's not rocket science. Yeah. You know?

**Chris Gammell:** I think across, across the social ecosystems. Yeah, yeah. That's the only way to operate these days.

**Dave Jones:** Oh, yeah. Yeah, they're all the same. Yeah.

**Chris Gammell:** Yeah, like I had a friend who was like new to Reddit somehow, and he's like, yeah, it's, I don't like it at all. And I was like, well, yeah, you got to really like winnow down the default channels. So you got to get out of the, like the, where all the knuckleheads are, and then like find your spaces. And then, and then it's, it's great. I mean, it's super addictive then, you know?

**Dave Jones:** Yes. Yes. Or, you know, you go to the wiring harness. Yeah, exactly. Reddit, and you'll just get pictures of wiring harnesses or something, you know? It's like, yeah.

**Speaker ?:** Right. Yeah.

**Dave Jones:** Oh, boy. Anyway, we spoke about, before about vintage components made out of paper. Well, here's some vintage. I just sent you a link. Go, go check it out. A prominent, one of the big old school testing measurement companies at Maxervice. Their name is or was Maxervice. In Melbourne, in Victoria, bring your own machete. Australians will get that joke. Thank you. And, uh, yes, they're, um, well, they're not shutting down. They got bored out. Um, cause the original owner is ill or something like that. Hope he's doing well, but yeah, it's all shutting down. And they're like a warehouse of old boat anchor.

**Chris Gammell:** Oh yeah.

**Dave Jones:** You know, test gear. There's some photos on there.

**Chris Gammell:** I see some photos. Yep. Yep. Yep. Yep.

**Dave Jones:** Like there's just rows and rows and rows of floor to ceiling warehouse of test equipment. And it kind of looks like a mess as like, there's some shelves that are very orderly and there's parts of it that are just like, you know, it seems like a junkyard, you know?

**Chris Gammell:** Yeah. We don't have an equivalent. There's a, there's a car collector site called bring a trailer, which I love. Like, first off, that's just like bring a trailer.com. Like what a brilliant name. We don't have like a, you know, whatever the, uh, it was like boat anchors away or something like that. We should, they make a site name, you know, like, you know, it's not going to work, but that's kind of the point, right? It's like everybody's selling their old project down there and their old test gear. And yeah, it's just, it's kind of like EV block forms like that.

**Dave Jones:** Yeah, exactly. But I'm, I'm afraid. That almost all of this is going to end up as e-waste. I, I guarantee it, you know? Oh yeah. Yeah. Most like, no, there's so much stuff, dude. There's thousands and thousands of items. You can't sell these onesies, right? You're, you're either going to have to sell them by the pallet load or they're going to have to go to the e-waste. Like there's no way you can sell these onesies and twosies. And there's a few people on the EV blog forum who were in Melbourne and they have gone through and they got, you know, thousands of dollars worth of stuff. So they've probably picked the eyes out of the good stuff,

**Chris Gammell:** I guess, but, Oh, so this is already like post, this is post picked over.

**Dave Jones:** I think this is post or semi or during the pick out.

**Chris Gammell:** This is not beginning of the ham radio swap meet. This is end of the swap meet.

**Dave Jones:** And yeah, it's got, you know, just all old vintage HP, you know, tech stuff.

**Chris Gammell:** And it's just like, yeah, I mean,

**Dave Jones:** this is fantastic.

**Chris Gammell:** This is what, uh, Greg Charvat, when he was back on the show, you know, like this is like his, his dream of like, just, he wants to go fix stuff. So you just go pick it up and, or Tom Lee as well. I, you know, I caught up with Tom relatively recently as well. Yeah. Tom likes doing that sort of thing. Yeah.

**Dave Jones:** Yeah. It's great. Yeah. It appeals to a certain crowd and like to go down there and have a look, but you know, I'd have to like buy a flight to Melbourne and get a rental car. And then if I picked anything up, how do you get it back? Cause they weigh like, you know, 30 kilos a pop. So, you know, it's like, I'd never make enough money back on the views. No,

**Chris Gammell:** you wouldn't. But here's, here's the move. You, you go, you go to buy a trailer.com or whatever the Australian equivalent is. You go and buy a camper project. You buy a caravan. You put that in storage for six years and you say, you know, the next time this comes up, I'll have my caravan project and that'll be ready to go. And I'll take that. I'll drive that down to Melbourne. And that's how you also, that's how you layer this stuff on, right? So you're going to have a caravan to go pick up test gear in another state. And that's how it all works. Yeah. Yeah.

**Dave Jones:** So I can bring a trailer and fill up my already overcrowded.

**Chris Gammell:** Thanks. Well, but then the caravan also becomes storage. Don't forget that.

**Dave Jones:** Yeah. Yeah. Exactly. Find a parking space for it. Yeah. Need to hire a parking space just to keep the.

**Chris Gammell:** Of course. Yeah. You should really get a garage. I mean, you should get like a, like a, you know, like temperature controlled. Yeah. Safe.

**Dave Jones:** Oh yeah. Right. And to do that, we'll have to sell our house and buy a new one on a big property somewhere that has, you know, giant shed or where I can build this giant climate control.

**Chris Gammell:** Yeah, exactly. You know, like a 20 foot tall garage door to get. Yeah. Yeah. You get your Winnebago in there.

**Dave Jones:** Yep. Yep.

**Chris Gammell:** I, I stooped so low that I went on Facebook marketplace the other day, Dave, because I was trying to sell something and someone's selling a schoolie, a schoolie, a schoolie. Yeah. It's when you convert a school bus into a living. Oh no.

**Dave Jones:** A schoolie here is schoolies week where at the end of their high school, everyone goes out for schoolies week. That's the only reason. Yeah.

**Chris Gammell:** Yeah. Sure. Yeah. Got it. Yeah.

**Dave Jones:** We don't have school buses. No, we don't, we don't have the school bus culture that you guys do.

**Chris Gammell:** Got it. Got it. Yeah.

**Dave Jones:** Yeah. They hold zero nostalgic value for anyone here.

**Chris Gammell:** Yeah. That's smart. Yeah. I mean, the schoolies are like huge diesel engines, you know? Yeah. Yeah. Not, not the best time to be buying one of those.

**Dave Jones:** Well, you can do an EV conversion.

**Chris Gammell:** Yeah. I catch, I catch those on the YouTubes sometimes. Yeah. The conversions.

**Dave Jones:** People converting them over. Yep.

**Chris Gammell:** Yeah. Pretty cool. You'd probably need a lot of batteries for a school buses are not small in the States. No,

**Dave Jones:** for hauling that, all that weight around. Yeah, exactly.

**Chris Gammell:** All those, all those chunky kids. Yeah. Yeah.

**Speaker ?:** Oh,

**Dave Jones:** you wouldn't know what happened to my bloody EV, right? Did I talk about this? It got actually recalled.

**Chris Gammell:** Oh no. Wow.

**Dave Jones:** My Hyundai 2020 EV got recalled last month. Right. And it said, oh, it can just spontaneously explode due to a software error.

**Chris Gammell:** Oh boy.

**Dave Jones:** So I thought, well, that's probably not good.

**Chris Gammell:** I will listen to this one. Yeah. Okay.

**Dave Jones:** So there aren't, as far as I know, there are no technical details on how the software can cause the battery to short out and explode.

**Chris Gammell:** So that's the problem actually, is that they don't, they don't know how it works. So they just, you know,

**Dave Jones:** sometimes it just blows up. There's too much code in there. There's half a million lines of code and they don't know how it works. Wow. Well, that was the problem with the Toyota accelerator pedal thing. Wasn't it? It was, there was just so much code in there. They had no idea how it actually worked.

**Chris Gammell:** I don't remember. I mean, I remember past guest of the show, Jack Gansel talking about it a bunch, but Gansel.

**Dave Jones:** Yes. He was on the, he was an expert witness or something for it. I think. Yeah. Yeah. And it was just, yeah, it was nuts. They just had no idea how it worked. It was like millions of lines of code in there and it was just nuts. Anyway. So yeah, apparently my EV could just spontaneously short out the battery and explode, which is not optimal. So I sent it back for the service recall and sent it back for the recall. And also a regular service hadn't serviced it for ages. So they updated the software because the fix was a software update. Darn it.

**Chris Gammell:** You'd hope they put new batteries in, you know?

**Dave Jones:** Right. Yeah. Yeah. That'd be nice. Please give me a whole new pack.

**Chris Gammell:** Yeah. Yeah. Yeah.

**Dave Jones:** And you can upgrade the capacity while you're at it. Yeah. That'd be nice.

**Chris Gammell:** Yeah. Right. Right.

**Dave Jones:** Anyway. So I got, I got it back and I turned it on. And the first thing I noticed was click, click. I'm trying to make a relay noise. I can't really make it. Yeah.

**Chris Gammell:** Yeah. Yeah. Yeah. Yeah.

**Dave Jones:** But it sounds like a relay contactor and it's like going off and on, off and on in sort of a semi repetitive pattern for about 15, 20 seconds. And I'm going, am I going crazy? What the hell's going on?

**Chris Gammell:** It's like, are they trying to blow me up?

**Dave Jones:** I, yeah, I don't know yet. And it, and it still does that. Like the, the car can drive. So I can turn it. As soon as I turn it on, I can, because it's, you know, there's no engine to start up. You can immediately start driving. I can start driving. And the relay click, this contactor clicking is still going. And it goes on for like 15, 20 seconds. And it's quite loud. Every time I start up the bloody car.

**Chris Gammell:** Hmm.

**Dave Jones:** Like I asked on one of the EV forums and they said, Oh, maybe it's an air conditioning thing. And aha, they had actually touched the air con system. They gave it one of these chemical flushes, you know, to get the bacteria out and all that sort of stuff. You know, they upsold me on that, but I thought, you know, yeah, yeah, it's probably worth it. Right. Cause they are a kind of a breeding ground for bacteria and crap like that. And the car was starting to smell a bit. So I thought, yeah, you know, we'll give it a bacterial flush. And, um,

**Chris Gammell:** you need sons, Dave, that's, that's a different problem.

**Dave Jones:** So what I can determine is that it's not the air con system.

**Chris Gammell:** Okay.

**Dave Jones:** Um, doing it is some relay under the passenger side of the dash. And unless I tack, take off the entire dash apart, I don't know what relay or contact or whatever it is, is, is making this noise. And I don't know whether or not to take it back. Cause it's a pain in the ass to take it back. Like, you know, I've got to take it back and they've got to have it for the whole day. And then I've got to walk back to the office and then I've got to, you know, go back and pick up the car. And it's like, you know, it's a pain in the ass.

**Chris Gammell:** So the whole dance. Yeah. Yeah.

**Dave Jones:** I don't know. At this stage, I haven't bothered. Should I, or should I just bloody leave it? I don't know.

**Chris Gammell:** I think, you know, I think you should make this into content, Dave, you could, you could make it a, you can make it a video.

**Dave Jones:** I can make it a video to see what they said. You know,

**Chris Gammell:** I think this is, maybe this is the beginning of you. You know, what is the, the, this, this is the click and the click and clack, you know, there you go. So,

**Dave Jones:** well, well, I can almost guarantee I'm 95% sure I'll take it back and it'll be a complete waste of my time. And they'll go, Oh no, that's normal. That's part of the software upgrade.

**Chris Gammell:** Yeah. That sounds great.

**Dave Jones:** Totally waste of all. They'll go, we have no idea, but everything's confirmed safe. And, you know, you just suck it up, buttercup.

**Chris Gammell:** I mean, as you were saying this, I was, I was thinking like, I don't actually know, like I knew where the fuse panel was on my old, actually on my, my gas-based car. I know where it is in there. I don't actually know where the fuse panel is on my EV. I think it's under the hood. Mine's got more than one.

**Dave Jones:** They, they, they usually more than one. Usually they'll have the 12 volt extensory, like a, maybe like a, a sort of like a minor one under your driver's side, you know, steering wheel.

**Chris Gammell:** Yeah. That's what I, that's the place I usually think of it.

**Dave Jones:** A secondary, a secondary, larger one. Yeah. Um,

**Chris Gammell:** in the blade, the blade style ones. Do you guys use those too? The blade style ones?

**Dave Jones:** Yeah. Yeah.

**Chris Gammell:** I think what I would say is I would just start yanking those. And then when they stop, then you'll know at least what circuit it is. Right?

**Dave Jones:** Then I'll know what it is.

**Chris Gammell:** Yeah. Great. Okay.

**Dave Jones:** Yeah.

**Chris Gammell:** Troubleshooting mode, you know, just switch into it, man.

**Dave Jones:** Anyway, we're talking about, uh, chip of the week before. Um, I think did. Yeah. No, I did this video two weeks ago so that we have not had a video. We have not recorded a video since then. Have you seen my video on the Texas instruments? How they screwed up the NA double five three, two. I have. That went sort of like virally.

**Chris Gammell:** I have seen that.

**Dave Jones:** A lot of people had seen it.

**Chris Gammell:** Yeah.

**Dave Jones:** And it was like, Jesus.

**Chris Gammell:** You know, that's, I don't know if you know this, Dave, that's actually what you want.

**Dave Jones:** Yes, I know, but it happens so rarely that, and it happens on ones I don't expect. Happens on videos. I don't, I did not expect that one to go sort of, you know, virally. And I, and I think it got written up on Hackaday as well. And, you know, other things and well, it wasn't just that it got written.

**Chris Gammell:** Well, why don't you, why don't you give a quick recap for the people? Right.

**Dave Jones:** Um, TI Texas instruments have changed the process node and, and the design of the classic NA double five, three, two audio op amp, right? This is the jelly bean audio op amp. It's like advertise, you know, if you buy any high end audio file product, though, they'll boast about having any double five, three twos in there because like it's the audio op, amp people trust, right? It's 40 years old, right? It's, you know, well,

**Chris Gammell:** yeah, I guess jelly, jelly bean doesn't usually say like high end. No,

**Dave Jones:** it's not the highest end op amp, but we'll get into that. Um, no, it's a bit, it's a pretty D it was a great audio op amp for its day. Right. Um, and it's still very good these days. Like who needs 0.0008%, you know, harmonic distortion, you know, homeopathic quantities of distortion,

**Chris Gammell:** you know, homeopathy.

**Dave Jones:** It's like you dilute that. It's so small. It's unmeasurable. It's like, you know, um, anyway, it's, it's a, you know, it's a decent audio op amp. It's not up there with the super duper high end, but it's a, but people still advertise it because people trust it. Right. It is the go-to audio op amp. Anyway, they, they changed the process node and they changed the design, right? They went to a smaller process node and there's a change note on the, uh, they, when semiconductor, large semiconductor companies like this change a, a, a design, either they change the fab or they change the design, you know, the functionality changes, the spec changes, they will release a design change note, right? For that part. And then that automatically goes out to your digi keys and your mouses. So if you've bought the part from digi key or mouser before, for example, you'll get an email saying, aha, there's a change notification for this chip, you know, please read and blah, blah, blah. Right. That's all part of this.

**Chris Gammell:** So yeah. Yeah. I get a lot more of the obsolete notices, unfortunately, than the, uh, yeah,

**Dave Jones:** yeah, you get the obsolete notices, but you can also get these part change notifications, right? Or if you buy it through your authorized rep or whatever, you know, your local TI rep, their job, one of their jobs is to notify, keep you on your database and notify you if you've bought that chip before, there's any change notifications, they should contact you. Right. That's all. That's why you pay extra from buying through them instead of the, you know, instead of the black market or eBay or something like that. So anyway, so this change notification, it says, you know, yes, look, we moved it to this foundry, right? We moved it from this, um, like they actual named the actual foundry, which made they name, name the process node and all the technical, you know, stuff that you'd be familiar with having worked at a fab. Right. And yes, we, we're using now, I, you know, this nanometer process or whatever, and we've changed the fab, but then they will summarize it and say, there are no, basically this does not impact the design or the specs at all.

**Chris Gammell:** All's well that ends well.

**Dave Jones:** And then you go in and you read the data sheet. Well, they've increased the bandwidth, which is fine, but they've lowered the slew rate.

**Chris Gammell:** Yeah.

**Dave Jones:** That's not good. If you rely on the slew rate from nine volts per microsecond to five, and the, uh, the, uh, human body model has changed. For those who aren't aware, the human body model is the, um, static sensitivity of the inputs, right? How much voltage surge, how much static surge can the inputs take without actually blowing up? They've halved that from 2000 volts to a thousand volts. Yeah. That's a bummer. That's a bummer if your design relies on that. Yeah. Right. But the most egregious change is they've changed the maximum supply voltage from 22 volts to 18 volts. Yeah.

**Chris Gammell:** Yep.

**Dave Jones:** And this chip's been around for 40 years. There's a lot of designs that, that relied on the fact that the NE5532 is a maximum 22 volt part, typically used at 18 to 20. But now they're saying the absolute maximum, the absolute maximum is a plus minus 18 volts.

**Chris Gammell:** Yeah. That's not great. It's like, I mean, like, well, most people are using this to plus minus 15. Right. And those never go over. They use regulators. Right. They're not just rectifying off a transformer.

**Dave Jones:** And it's famous. Well, speaking of which, this op amp is famous for being able to drive 800, drive high voltages into 600 ohms loads, which is the traditional audio type load, right? The 600 ohm load. And it's famous for being able to do that. And now they've actually removed all mention of 600 ohm loads in the data sheet. And it's like, aha. And if you go into the schematic, you'll see that they've entirely changed the actual design. The front end transistors are now PNP instead of NPN.

**Chris Gammell:** Yeah. This is like, they let the intern at it or something, huh? Or I don't know.

**Dave Jones:** Yeah. But the worst part is they didn't change the part number.

**Chris Gammell:** And that would have been the right, the right move. Right.

**Dave Jones:** Sure. And it'd be fine if they go any 5532-1 or dash two or something. But no, they kept the part number the same. And they said, trust me, bro. It's, it's good to go. And it's like, yeah, yeah, nah. Anyway, they screwed the pooch. But then, so I found another one, which is the OPA 134, which is an old Burr Brown part. Shout out to all the Burr Brown fanboys that they still brand them Burr Brown because, you know, there's a few old timers who will use it. Anyway, the OPA 134 is, is an actual high end, really super high end audio op amp with homeopathic quantities of distortion, right? Like point 0000008% THD or something. Right. And I looked at the change note for that part. It's an eight pin SOP, right? And the original part had two trim pins on it. We could hook up a trimmer pod to make it even more homeopathic quantities of, you know, offset and stuff. Right. They made a change in that part where they simply removed the trim pins and they didn't change the part number. They literally, literally removed the trim pins. They changed the entire functionality of the part and they didn't change the part number.

**Chris Gammell:** Some engineers are having bad days. Those are bad days.

**Dave Jones:** This is just, no, no,

**Chris Gammell:** this is, this is the thing they don't, I feel like they don't tell you, you know, like if there's young engineers too, like they don't tell you this in school, right? I mean, I don't have a ton of young listeners, but like, you know, this is the kind of thing where like, this is why, this is why I had a job, I suppose, in my first job at Keithley, you know, like, I guess it was my first job, but my job at Keithley was basically dealing with this kind of stuff, you know, coming in, maintaining, maintaining engineering effectively. It's just, yeah. Cause then what are you going to do? Like, Oh, the trim pot's gone. Now. Oh,

**Dave Jones:** the component obsolescence engineer, their job is real. Yeah, exactly.

**Chris Gammell:** Yeah. Yeah. And I think the longer electronics around and the longer, you know, this has some crazy 45 years on a part. It's like, okay, well that there's a lot of residual damage when things change.

**Dave Jones:** And there's another part, the LMH 6518, which is used in the front end of almost every modern scope, right? It's, it's got the differential amplifiers and the, you know, the variable gain amplifier and everything. Right. And it's famously, well, it's designed, it was originally designed to be able to handle 400 Hilly volt offsets, which is what, what you need, right? When you turn the, you can shift the input of your front end on your scope, right? That's a basic functionality. And they changed the design of that chip as well. Without sort of, you know, if you have to read deep in the data sheet, they didn't change the part number and they go, well, it's not quite capable of the 400 millivolt offset anymore. And apparently forum has documented cases of people's scopes being bricked because they had too much front end DC offset. So like, yeah, yeah. Wow. This is not good. Good. Dude.

**Speaker ?:** Yeah.

**Chris Gammell:** It's like the electronics version of in shitification, you know, it's like, uh, usually that refers to internet. That's like a corey doctor term. It's like, uh,

**Dave Jones:** there are lots of comments on the, under that video, the using the word and shitification. There are.

**Chris Gammell:** Okay. I didn't even see those. That's I feel, I feel like I was poaching those now, but I didn't. Oh, there you go. I see it. Yeah. Yeah. It's great. It's a great term. I love that term. Yeah. Yeah. It's great. That was not good. Yeah. That's wild. I, you know, it's interesting too. Cause like, I think that there's a lot of like tribal knowledge. Like, so like, okay. So like there's the, the now what? And it's like, there's always like this tribal knowledge that kind of exists from like, at like the FAE level too. Cause they're going to be like, well, most of our people are either, you know, revalidating their designs and they're just saying, okay, we'll make it work. Or there's this other part. And then they kind of point you in that direction. And that's kind of like the tribal knowledge that like, it's kind of like the shortcut, but I'm not sure that exists. I mean, you know, the forum kind of operates in that, in that way, but it's, it can be tough to find that, that info, you know, like you don't have to go and discover all that stuff yourself, but it does happen.

**Dave Jones:** Exactly. You want to know what else happens? Shit happens. What else happens? We have this shit happens. Our segment shit happens segment. Here you go. I'll link it in. You probably haven't seen it. Cause I just released it last night, a video on my second channel where I went to repair my Lovo Accutron to watch, right? Very nice watch. Right. Very nice brand. Very nice watch. Very accurate. High, high frequency, 262 kilohertz or the second hand on it just sweeps beautifully. It's just gorgeous. Anyway, fantastic watch. Um, so I thought there was something electrically wrong with it. So I started out the repair video thinking, you know, like it, it just wouldn't move. Right. So I went in there and when I went in there under the microscope, if you go to about two minutes, 45 or something in the video,

**Chris Gammell:** yeah,

**Dave Jones:** you'll see me pointing at the drive coil, the giant drive coil in there.

**Chris Gammell:** It looks like it's like delaminated almost. Yeah.

**Dave Jones:** It's been mangled. It's been mangled. Guess who did that?

**Chris Gammell:** You.

**Dave Jones:** Yeah. Some dickhead. Yep. I can only presume I did that when I was last changing the battery. And I like was, you know, it's got one of those coin cell batteries, you know, and sometimes you have to dig them out, you know, it's like, Oh, you scraped across it. And I probably did it with like a metal, you know, a sharp metal thing. And it just happened to dig, you know, like a slipped or something and it must've gone in and just gouged out the coil. And this coil, I've never seen such tiny gauge wire in my life. This thing has to have like 5,000 turns of the tiniest gauge wire you've ever seen in your life.

**Chris Gammell:** Have you ever seen those like automated transformer winding videos too? Like there's so much fun to watch.

**Dave Jones:** Yeah. They're great. Oh, yeah. Yeah. They're hypnotizing. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** And, and there's some people that are just going, Oh, just rewind it, bro. And it's like,

**Chris Gammell:** yeah, right. Okay.

**Dave Jones:** I don't even think I can buy this gauge wire. Yeah.

**Chris Gammell:** I don't know anything about watches. Just so we're clear. What, what is this doing? What is this?

**Dave Jones:** Oh, it's the drive coil for the mechanism that makes it spin. You know, a quartz watch will use a coil, like to make it spin, to make the, the cog spin, which then turns the hands, right. It's actually a mechanical one.

**Chris Gammell:** Got it. So it's like,

**Dave Jones:** it's a coil of it's an electromagnetic coil. Yeah. Got it. And it's also glued in there as well. And it's, and it's ultrasonically wire bonded to the PCB. That's how tiny these, you know, and fragile these wires are. They're like little bond wires, you know, die, you know,

**Chris Gammell:** you can even see scrape marks on there. I think, yeah, you can see scrape marks. That sucks. I mean, I know this is not equivalent, but I do have ongoing, like, like scars of shame on my, on one of my build plates from my 3d printer, where I was just like, frustrated and like scraping at it, you know, but now every time I do a print, I'm like, yeah, yeah, that's where I ruined that one. You know,

**Dave Jones:** I still haven't got my 3d printer back up and working. I just, I just don't have the, I don't have the will to take apart the entire head. It's just like, I'm trying to build up the enthusiasm to try and take it all. Yeah.

**Chris Gammell:** You just need a project, man. You just need like a thing where like, you're like, I really need a 3d printer.

**Dave Jones:** Get off my ass and go, right. I got to fix this damn printer. It's like, Oh God, you know, I've already changed the head on. I've already taken it apart, cleaned it out. And you know, but no, the actual, it's all gummed up inside. I think that's the consensus is that all the cogs inside the actual head are all gummed up and I got to get in there. Oh, so yeah. Yep. Bloody 3d printers. Yeah. Do you see that? They banned them. They banned them in, was it New York? Am I wrong on that? Which state? Or was it Ohio?

**Chris Gammell:** Yeah. They were doing like some ghost. I think it was New York. It was like ghost guns and stuff like that. That was.

**Dave Jones:** Yeah. Yeah. And they literally banned 3d printers. Like the actual bill went through. It was passed. I think.

**Chris Gammell:** So I don't really get how they enforce that, but.

**Dave Jones:** Well, they can't. It's just a bullshit rule that they pass, you know, virtue signal into everyone that, you know, Oh, look what we did. And then it just screws it. I think it's,

**Chris Gammell:** it's, it is saying like, there's like gun problems in the States. Like no. Duh. And like, I don't think the ghost guns from 3d, you know, commercial 3d printers.

**Dave Jones:** Ghost guns from 3d printers are the least of your worries. Yeah. Yeah.

**Chris Gammell:** Right.

**Dave Jones:** Right. Right. Right. I don't think that's going to fix the problem, dude. It is not. It is.

**Chris Gammell:** It is endemic. Yeah. Yeah.

**Dave Jones:** Yeah. It's a cultural thing. It's a. Yes. It's way, it's way bigger than the guns. Yeah.

**Chris Gammell:** Way bigger. Way bigger. Yep. Yeah. So yeah. Yeah. I mean, there was like all this stuff with bamboo, all that stuff going down, you know, Jeff's made a video about it. I think Lewis made a video about it, but like, you know, like all the open source kind of the closed nature of it and, and, and bad faith stuff from bamboo. But the thing is they make cheap hardware too. So I think people are going to keep supporting it because of that. You know?

**Dave Jones:** Well, and I, there's lots of, I go once again, you've got to be on X. There's a lot of hate on X dude.

**Chris Gammell:** That's actually why I'm not on X Dave. Well,

**Dave Jones:** a lot of the 3d printer, you know, all the good stuff that's happening is all, it's all on X. And, um, all the 3d printer YouTubers are jumping on the bandwagon. It's like, nope, never buying bamboo again. Nope. Done. Yeah. I think, you know, yep.

**Chris Gammell:** Well, I think that'll play out over time. We'll see.

**Dave Jones:** Yeah. Yeah. Anyway. Ah, boy, we could talk about another, um, Lewis thing. If you're really keen to get into a, uh, lawsuit side of things,

**Chris Gammell:** lawyers, lawyers, you know,

**Dave Jones:** should I, should I talk about battle born batteries?

**Chris Gammell:** Oh, I don't know that one. I have not heard about that one now.

**Speaker ?:** Right.

**Dave Jones:** Anyway. Um, I'll, I'll make it, I'll, I'll send you the link. I'll send you the link.

**Chris Gammell:** Got it. Okay.

**Speaker ?:** Yeah.

**Dave Jones:** So yeah, no, I won't go into it. Basically their batteries are failing and a big YouTuber, um, is being sued by them. Cause he did a battery testing them to their specifications. That was on their data sheet and it failed. They like melted inside. Yeah. It's not good. And like tested multiple batteries and they've all like melted inside. Yeah. They sent them a, you know, cease and desist or something. I don't know, but they're somehow suing them. I don't know the details and then they've changed their data sheet. It's magically vanished. The, that, that's. Yeah. I go. Wonder how that happens. And then mysteriously, the link I sent you, a blog article appeared that no, is this, um, melting down inside seems to be a feature because I'm not a material scientist. I don't know. But anyway, we will link in the, um, very informative blog article down below about how they use plastic. In between two metal contacts on the battery terminals of a giant battery. And somehow that's good.

**Chris Gammell:** But anyway,

**Dave Jones:** they claim it is. So, yep. All right. No problem.

**Chris Gammell:** Good luck. Good luck with that.

**Dave Jones:** Oh boy. Yeah. Everyone's suing everyone these days. Uh, Lewis is suing Samsung. Did you see that?

**Chris Gammell:** I did not know.

**Dave Jones:** Yeah. I, I have not read the full thing. Apparently. Yeah. He bought my Samsung SSD drive and there's something about the warranty and they wouldn't honor his warranty. So he went, Oh, bugger it. I'm suing him. So I don't know the details beyond that, but go Lewis. Oh God. He's, he's in it for the love of the game. Lewis is in it for the love of the game. He's good on him. I love it. Yeah. We'll have to get him back on the show one day. Yeah.

**Chris Gammell:** It'd be good. He's still doing right to pair repair stuff generally too. Right. I mean like that's his.

**Dave Jones:** Yeah. Yeah. That's, that's pretty much. I don't think I've seen him do a repair video for years now. I think he's like, he's, he still owns and runs his repair business that moved from New York to Texas wisely. Um, but, uh, yeah, I haven't seen, I don't think he does repair videos anymore. So yeah, it's all this right to repair. Cause he works for them full time. He works for, uh, Futo, um, basically full time now as an advocate for this right to repair stuff, which is cool. Yep. All right. Is our amp hour up?

**Chris Gammell:** Yeah. I don't know if there's any last things that you wanted to mention.

**Dave Jones:** No, no, I think I covered it all.

**Chris Gammell:** All right.

**Dave Jones:** Catch you next time.

**Chris Gammell:** See you soon.

**Speaker ?:** Bye. Thank you. Thank you.
