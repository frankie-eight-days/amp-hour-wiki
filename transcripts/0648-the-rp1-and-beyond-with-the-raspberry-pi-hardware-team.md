---
episode: 648
title: The RP1 and beyond with the Raspberry Pi Hardware team
url: https://theamphour.com/648-the-rp1-and-beyond-with-the-raspberry-pi-hardware-team/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released October 22nd, 2023. Episode 648. The RP1 and beyond with the Raspberry Pi Harper team. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**James Adams:** Hi, I'm James Adams, CTO, Hardware at Raspberry Pi.

**Liam Fraser:** Hi, I'm Liam Fraser, a mix of software and hardware engineering at Raspberry Pi. Awesome.

**Chris Gammell:** Welcome back and congrats on the new silicon. That's what we're going to be talking about today. The RP1 silicon was just released. And we're going to do a little recap on last time you guys are here. You were here back in 2021. And we'd love to get an update and hear about all the new things that are happening.

**James Adams:** That's right. Well, thanks for having us back, Chris. Glad to be here. Yeah, let's have a wander through what Raspberry Pi has been doing, I guess, on chip and product side, if you want to talk about that. So where would you like to start?

**Chris Gammell:** Well, I think one of the things that has come out as part of this is just that the RP2040 wasn't the initial target, right? You guys were driving towards this recently. The RP1 is one for a reason, right? It was the first thing you guys started working on, right?

**James Adams:** Yeah. So I guess the naming sounds confusing. But actually, yeah, RP1 is the first. It's called RP1 because it's the first Raspberry Pi silicon that we started. We've got RP2, which is RP2040. And RP3, which is our chip that goes on the 02. So yeah, that's just the order that we started the chip programs. I guess the genesis of RP1 was back in 2015. And we knew that we have this natural architecture of a main processor on the Raspberry Pi and then some kind of IO controller. So back in the early days, that's the LAN 9512 on the very early boards. And then four, which is basically USB to USB, sorry, a USB 2 to a USB 2 hub and Ethernet, 10100 originally. So we kind of wanted to improve on that really. And most people from Raspberry Pi are from a chip design background. And the thought was that we would like to improve on that offering. So back when we started this, we had USB 2, right? We had LAN 9512. Yeah. Yeah. Well, we also, on the Brawcom chips, we had these MIPI channels spare. So we had CSI and DSI. So these could do multi-gigabits of bandwidth, primarily for camera and display. But the initial thought was, well, could we repurpose these channels to actually transport data and do an IO chip by plugging it to those? So this is before we kind of came up with the revelation that, well, actually, we should do a standards-based thing and adopt PTI Express. The original idea was to do something funky with these spare interfaces. And so we started the team in a kind of conservative way, as we do at Raspberry Pi Engineering. So we had three people that we knew from our chip design days who had gone off to do a startup and the startup was running out of money. And so we employed them as contractors to kind of scope out how could we do this? Can we start looking at costing it? Can we start looking at where we get the IP? And so really, we started a chip design team really absolutely from scratch. So we had no one. Then we had three people as contractors. And gradually, as we built the specification, we started to find the IP. We started to build the more detailed specification on how are we really going to do this? We did some software work on, well, is it feasible to reuse these channels as data channels? And yeah, it kind of grew from there. And eventually, we were quite committed. So we pulled those guys on as full-time employees and started employing more ASIC guys. And so now we've got a reasonable-sized team. I think it's still a very small team by ASIC design standards.

**Chris Gammell:** Right. Yeah. Intel laughs at your... Absolutely. We have more interns than you guys have. Yeah, pretty much. Right.

**James Adams:** But we do, you know, we employ people who are a lot of people who've done this for a long time, right? So they really know what they're doing. Yeah. And we're lucky to, because we were in the space before, we knew the good people to go and pull on. And it's taken a little bit of time, but we've managed to recruit a superstar team. And, you know, it's paid off, right? We do manage to do quite a lot with a small team. And I guess it kind of speaks to why RP1 took so long, actually, is that it's a complicated chip. We kind of went through this cycle of deciding on one sort of architecture. And then we did actually have a test chip with these MIPI channels in, and it did actually work. But it kind of missed the boat. It was late. And that's largely just the kind of, you know, the effort to build it. It just took longer than we expected. You know, you're trying to bring up a whole team from scratch. And once we'd, I think we basically taped up, as we taped out that first test chip, we really, we'd already decided, okay, we're going to switch this to PCI Express. Because it has all these advantages. You can plug it into standards-based system. We can plug it into, even before we had, because at this point, we knew the new Broadcom processes upcoming would have PCI Express. And so we could see the future. And we knew we could, even if we didn't have those yet, we could plug it into an x86 PC and do early development work, which is what we did.

**Chris Gammell:** So does that mean on the, on the, so you mentioned like the MIPI and CSI DSI. You said those are kind of like extra channels that were on that, whatever the generation of the Raspberry Pi was. Is that right?

**James Adams:** Yeah, so this is, this is the first, very first. 2035 actually had, has two camera two display. And we only ever exposed one of each. Oh, interesting. On the original boards. Now, the compute module subsequently exposed all of them, but we kind of had two spare rights. So that, that was, that was the idea. Okay.

**Chris Gammell:** Okay. So those were, those were meant as, I thought, I, I, I, I, when I heard you saying, I thought you meant that they were kind of just spare general, general purpose type things. And then they were kind of repurposed as camera and display, but it was, it was a camera and display. Yeah.

**James Adams:** They're quite specifically camera and display. So you had to jump through hoops and decide, well, how on earth do we, we fake this thing to look like a camera and display, but actually just pump general purpose data through it. Yeah. So it was a bit, it was a bit hairy and a bit crazy and it did work, but yeah.

**Chris Gammell:** I mean, that sounds like a lot of, I mean, like I've repurposed, you know, general, you know, like other GPIO or weird, weird peripherals, you know, use what you got. Sometimes you're just kind of pin limited. And in the case of Silicon, there's really no, there's no rework in that sort of thing. So that, that makes a lot of sense. Before we go into the RP one, I'd love to get a update. So like, like we mentioned at the beginning of this, we talked about two and a half years ago. It was mid pandemic. The RP2040 was the only thing that was really, I mean, it was one of the only chips that was available out there. I think it's seen a lot of success. What do you guys, what's, what's the status of it? Where, where do you see it? Where do you see it out in the world and how's it been going?

**James Adams:** Who's going to answer that one?

**Liam Fraser:** Liam, did you want to? Yeah, sure. I mean, I know we've got a lot of industrial customers using RP2040, but I think in particular, the thing that's really done RP2040 well is the, you know, the SDK. We spent so long on that. The MicroPython support out the box. You know, I, and then also Pico W, like, you know, I wanted to add wifi to some fan thing that I had lying around the other day. It was some noisy, uh, plinth heater thing. And I took that out, put some Noctua fans in and hooked up Pico W to it. And it literally is, you know, 10 minutes of MicroPython to, I can now talk to this thing over wifi and, uh, change the speed of the fans. So, uh, yeah, and actually it would be nice to touch on, uh, so the thing that RP2040 allowed us to do during the development to sort of bring RP1 back in a little bit. The first version of RP1, uh, that we started when we had the small chip team, all the RTL was written by hand and RP2040 is actually the chip that we use to develop our sort of scripting our tools on. Because I don't, I don't know when we started RP2040, but you know, it would be at least sort of three years or four years before, before release. And, and the idea was, you know, this is a reasonably small project and it will allow us to sort of prove out, prove out this kind of stuff and then sort of port it back in a, in a way to, to RP1. So sort of between the first version of RP1 and doing RP2040, then the sort of second version of RP1 was using all the scripting stuff that we developed on, on RP2040. And a lot of the RP2040 stuff was, you know, reusing RP1 components, but in a bit more scriptable way. So a lot of the groundwork had been done.

**Chris Gammell:** And the scripting in that case, the scripting refers to like boot code and that sort of thing, or where, where is the scripting involved?

**Liam Fraser:** So it's any sort of common components of the chip. So we've got a small team, RP1, for example, certainly the later versions, you know, there's probably like 20 different clocks on there. There's, you know, 50 odd GPIOs. The bus fabric's got like 90 different connections on it. And all of those things, we basically just stamp out several instances of the same thing, all configured in sort of, you know, in a scripting language. And it really, and this stuff also spits out, you know, your software headers, your documentation, all this kind of stuff.

**Chris Gammell:** All the things that I assume is just magically working, but it's actually under the hood, it's very non-trivial, I'm guessing.

**Liam Fraser:** Yeah, yeah, well, we're still developing it. And yeah, it's, you know, it's a sort of evolving thing as we decide we need new features. But yeah, that's how we're able to do quite a lot with a small team.

**James Adams:** Yeah, I think it's driven by sort of us old hands, basically just being sick of all the typing required to stitch blocks of IP together in chips, right? Yeah. And every ASIC company has some form of scripting of doing this, but I don't know how many years ago it was, Liam, we sort of sat down and said, hey, we need to do some scripting because it's just such a pain to put all this stuff together. And what Liam and Terry and the guys have produced is just like way above what I've ever seen in terms of its ability to, you can basically describe what the chip looks like in a high level kind of language. And it literally goes and builds everything. That's cool. It reduces a ton of work and obviously reduces errors and bugs and it builds all the GPIO and the clocks and all these kind of things kind of out of sort of reusable basic components.

**Chris Gammell:** It's starting to sound like FPJs, almost like halfway to FPJs.

**James Adams:** Kind of. I mean, there's still quite a lot of fettling of each chip, right? I think probably, well, Liam, again, Liam is the expert because he's basically put this together. So you can correct me if I'm wrong, but I think every time we do a chip, we do evolve it a bit. And then that is part of the chip build process, right? And then the next chip probably needs a little bit of customization, but it vastly reduces the amount of work. And if you just want to, say, change a port on the bus or something and do something fairly trivial, it's five minutes work and a recompile rather than hacking a whole bunch of files to pull buses up and down the structure of the chip and all this kind of thing. So it's like, we do try and, I think there's a general kind of approach that we have to engineering is where we, we, we're always slightly under-resourced. So it kind of drives people to try and find ways to-

**Speaker ?:** The hunger.

**Chris Gammell:** It's the hunger.

**James Adams:** Yeah, it's kind of like keep everyone hungry and it kind of drives people to find innovation. So we like, we really like to find this way, ways of working smarter, not harder. And I think this is one of the really nice ways that we've managed to do this on the chip design side.

**Chris Gammell:** How does it get exposed then to something like MicroPython or, you know, other frameworks that are using this then? Is it like, does that call APIs that are then calling these scripts or like how much, how much is exposed to the, the software dummies like me?

**Liam Fraser:** So the, the scripts aren't actually, what, what the scripts are doing is effectively writing out Verilog, which, which describes the, you know, which is the harder description language, which describes the chip. So by the time you're running software.

**Chris Gammell:** Oh, okay. So this is, oh, this is all pre, pre Silicon being made. Oh, I see. Oh, wow. Okay. Oh, okay. I thought this was then configuration of the clock. So you were saying, so when you said like the 50 clocks and all these GPIOs and the fabric and stuff like that, this is to make a 2040 or example, like a 2041, right? If you were going to go from a 2040 to 2041, you would change the configuration file, rerun the scripts. And then you have like a new part. Is that, is that kind of the idea?

**Liam Fraser:** Yeah. Yeah. Wow.

**Chris Gammell:** And all that you got to do is just hand over some money to your, your fab and presto change it. What's the hard part? You know, like what, what's taking so long, right? Yeah.

**Liam Fraser:** Yeah. Unfortunately, you've still got to test the output of what the script makes.

**James Adams:** So yeah, this, this chip design is kind of like 20% design and then 80% test. Actually, I think that's probably a lot of projects, right?

**Chris Gammell:** Except at the beginning when you're planning, you're like, oh, test will be like, what? Like 30% overall. Right. And it's like, no, that's not how that works.

**James Adams:** Yeah. I mean, even with the tests, we have automated stuff to help with this as well. So it's not all bad news.

**Chris Gammell:** Hmm. So then, I mean, I don't dare to ask, uh, you know, what are the long-term plans, but what are the long-term plans? Like, I mean, so you have three Silicon pieces now that are, you know, released and public and stuff like that. But like, is there kind of like a overarching, like things that your team is trying to solve otherwise? I mean, because I don't see many blocks that are on Raspberry Pi-ified on an actual Raspberry Pi, right? You guys have captured a lot of, aside from the actual, the Broadcom chip, you know, you're doing a bunch of the other stuff that's on the board. So what's next?

**James Adams:** Well, I mean, we have a chip team, so we're definitely doing more chip stuff.

**Chris Gammell:** Mm-hmm.

**James Adams:** I think it's been mentioned before that, you know, it's likely we'll have new generations of microcontroller on the way at some point. I don't think that's a particular secret, because, hey, we've done one.

**Chris Gammell:** Because that's just how micro team works. Yeah. I mean, like, I want to see the new model here.

**James Adams:** They'll crank out more chips, and I'm sure we'll do a spin of RP1.

**Chris Gammell:** Yeah.

**James Adams:** You know, it's still a small team. So people have asked, you know, are you going to do your own main SoC? I think we probably even touched, we even touched on this, I think, in the RP2040 discussion. I've certainly, people have asked, and it's kind of like, that's a different order of magnitude problem. That, totally.

**Chris Gammell:** Yeah.

**James Adams:** You know, I think what we've done with RP1 is make it easier to make the big chip, like at Brawcom, because they don't have to faff with adding all the analog Raspberry Pi stuff to it, right? And when I say analog, I mean the kind of like, the sort of medium speed stuff like USB, GPIO, all this kind of stuff. In general, they don't really want to, they kind of want to build chips that are a bit more generic, and we want very specific Raspberry Pi things. So it makes a lot of sense for us to put our specific Raspberry Pi things in a separate bit of silicon, which we can control. And then, you know, it just makes life a lot easier. And of course, we can use it, right?

**Chris Gammell:** Giving up duties, right? It's just who does what they do best, right?

**James Adams:** That's right. So on Pi 5, you know, we work with Brawcom to, on 2712, but it is a, you know, it is, it isn't just our chip, right? So it's, it's, we can kind of like work with them to add the features we want. And then we work with Dialog Renegas to do the power management chip. And that kind of thing works well, right? You have to have a much, much bigger team to start attacking those kind of things. And then, and then you've got three chips. Then you've got the main SEC, the South Bridges and microcontrollers. And it's like, oh my God. And then you've got to keep going with all those. That's just, that's just an immense amount of work, right? So we kind of like to attack the things where we can make a big difference. Hopefully that answers the question without kind of revealing.

**Chris Gammell:** Yeah, no, no. I think that's, you know, that's good for me. I'm not sure if you revealed too much, but.

**James Adams:** In some ways, a lot of the time we don't quite know. We do experiments. We do, we have different ideas and, you know, and actually the team right now are quite focused on just like spinning up production of RP1, for example, and software on Pi 5. Yeah. And so, you know, it's, it's sort of a little bit of a lull in terms of really getting cracked into any new stuff.

**Chris Gammell:** Yeah. That makes sense. So on, on the 2040 specifically, I mean, I feel like that the PIOs have been a very interesting adopted thing. I think there's been a lot of people that are interested in using that sort of thing. I mean, are you seeing other, other use cases around the stuff that's in there or just kind of more as a general purpose chip, maybe other, other ecosystems as well. Like I know Zephyr just pulled in 2040 as well. I was excited about that.

**James Adams:** I didn't see that one. Oh yeah.

**Chris Gammell:** Yeah. It's community support, but yeah.

**James Adams:** Yeah. Yeah. Very good. I don't know. Liam, did you want to answer that one?

**Liam Fraser:** I can, I can give an answer as well. Yeah. I'm just trying to think what projects I've seen recently using, using PIO. I actually saw someone who managed to root a Starlink satellite terminal using RP2040. Yeah. Yeah. And also, you know, it's, it's been, it's been sort of stretched to its limits in many ways with the DVI stuff and like the not HDMI video output that it can do. Yeah. Yeah. But yeah. James, do you want to, do you want to chip in?

**Chris Gammell:** I can actually give an example if you guys would like, I, I, we're, we are doing video here. Obviously people won't see the one I'm showing here, but a board that I've, I've talked about publicly, I put a Pico onto like a display board and we use the PIO. We, Mike Stish, past guest and my coworker, he basically borrowed an I squared C listener, right? And that was a really good PIO thing. It's just sitting there cranking on I squared C incoming messages. And so it's an I squared C slave. And then we process the incoming messages. It's perfect application of that, of the PIO from my perspective.

**James Adams:** Yeah. We are seeing a lot more customers being as they, cause I think a lot of people originally didn't really understand what it was. And it's still a little bit of a hard thing to get your head around to. You'd have to do a bit of work to understand it, but everyone who's put the effort in and then sort of realized what it is. They're like, Oh, Oh my God, this is really useful. And we are now seeing a lot of interest in, in this stuff and a lot of cool, cool things. I think the more people use it, the more they like it. It's one of those, one of those things it's, it's a new feature. So most people will ignore it until, until they see something cool. And then they're like, Oh, what is that then?

**Chris Gammell:** Yeah. Yeah. I remember with the BeagleBone as well, like BeagleBone had kind of like that same, like software defined, like Silicon, you know, it's high speed processing of GPIO and similar, right? Like that, it felt very similar to me, but on the RP2040 is a lot easier to use because it's not like its own compiled. I mean, it's not a whole nother processor basically.

**James Adams:** Yeah. I think we, the, the idea was always to make it as okay. So I guess the design goal really was to be able to do real, real cycle by cycle, do lots of stuff every cycle. Cause you can attack this kind of problem with, I don't know, just use a general purpose CPU, like another M zero plus that can bit bash. But what you get with PIO is something much smaller. There's actually much more capable of doing things, you know, every cycle, a lot of things, every cycle. So it, although it's a bit, you've got to wrap your head around the, the instruction encoding and how the thing, how the machine actually works. It's, it's much better for that kind of thing. I don't know, Liam, if you've got any more.

**Liam Fraser:** Yeah. There's a, there's a guy on Twitter whose name I can't remember, but he's had PIO talking to like fiber transceivers. So, you know, doing ethernet over, over fiber. And I think, you know, just being able to talk to arbitrary things and, and shift data to them, you know, as quickly as they require, especially with a clock that's, you know, for that kind of bulk data transfer stuff, it is, it is really helpful. And the, and the display kind of application is, is really an extension of that. And also someone did make a PIO logic analyzer that works with like some open source logic analyzers software. Was that Kumar Abhishek?

**Chris Gammell:** I saw him. I can't remember what the software's called. I saw Kumar's giving a talk at, at, at Supercon. I was looking at all the Supercon talks that are coming up, but it's going to be there by chance. Superconfident? I'm not.

**James Adams:** I'm not sure. I'm not sure. I'm not sure if anyone from Pi is.

**Chris Gammell:** Maybe. Yeah. I'm sure that the 2040 will be prominently, prominently featured around, around the Supercon. Yeah. My favorite places.

**Liam Fraser:** But yeah, it just hoovers up whatever pins you configure and puts the data over USB so you can see it in like a logic analyzer. It's really nice.

**Chris Gammell:** That's cool. Yeah. That's, that's another, yeah. Another good example of something that's just like kind of sitting there crunching on inputs, outputs, that sort of thing. It's good. Good use case. I, you know, I think that's the kind of thing too, where it's like you guys said, it's, you don't know you need it until you do. And so I'm sure some of the, the coolest applications are still to come, which is great. And yeah, I mean, to talk a little bit about the, the sourcing side of things too, like, how do you guys keep it? Was it just like the timing was perfect? I mean, like, I mean, we talked about it and then it was just, I think it was like, you know, we talked in 2021, February, 2021, and like things got so, so bad in 21 into 22. And you guys were just like, we got tons of chips. So I just kept seeing them everywhere.

**James Adams:** Yeah. I mean, to be fair, we, I think we underestimated how bad it would get actually. And obviously, you know, Raspberry Pis, the big, the big Pis, right. Well, have been hard to come by. However, that is massively improving now and will continue to improve. But for RP2040, so we, we kind of bought a lot of wafers upfront anyway. And actually because we're a kind of a small player, you know, we don't build that much silicon. We could get offers on little bits of wafers here and there that we could take up. Whereas someone like, I don't know, a Qualcomm or a big guy, they have like a wafer allocation and that just got trimmed. And it's like, they can't, you know, if they get an extra three wafers, it really doesn't matter to them. You know, they're not in that game. Whereas for us, you know, there's 20,000 chips of wafer. If some, if, if we get offered, oh, you know, we've got a few wafers spared, you, do you want them? We're like, oh yeah, we'll have them. So actually the kind of just the scale and the fact that we actually did actually pre-buy a fair quantity. Yeah. Meant that we, you know, we had some good stock.

**Chris Gammell:** Could you explain that interaction? So like, James, are you the one that actually like, do you talk to the fabs? Like how does that conversation go? Like when you have three wafers, right? Or like, is it just like you have like, you get an email?

**James Adams:** So we actually, we actually buy our wafers through iMEC, which is an aggregator. And all we did, when you get to a certain scale, then you can talk to TSMC directly. But you know, those guys are managing a bunch of customers. And I think it's also true that TSMC occasionally have a few, a few spare here and there. Someone maybe deallocates or decommit something. Yeah. And it's usually small numbers. And basically, you know, we, we just get sort of an offer here and there. And it's usually for a reasonable number. And so we could take them. And it's probably more.

**Chris Gammell:** And when you say that we get a wafer, right? You don't, you mean there's a raw wafer available, raw piece of silicon. And then all of the process has already been defined. So they're like, we already know how to make this. We're just going to be able to run it through the line. Is that, is that kind of a...

**Speaker ?:** Yeah.

**James Adams:** So TSMC, TSMC have our mask. They can make our chips and they have various fabs. And each fab can do so many wafer starts a month. They call it wafer starts. Yep. And, you know, those wafer starts will have been booked. Like, you know, NVIDIA will book so much, so many, so many wafers a month because they make zillions of chips and Qualcomm, Qualcomm, all these guys. And that's all allocated and managed. And in normal times, there's enough supply and demand and that's all well balanced. And what happened in the chip shortages, you know, people kind of didn't expect the demand for silicon to actually increase. In fact, they expected to decrease. And then because it's a bit like oil, I think, because there's quite a tight supply demand, it's always managed fairly tightly. All of a sudden, when it gets out of sync, it really gets out of sync. And so the bigger silicon guys, they just kind of had to take a bit of a haircut on the quantity that would be allocated. But people like iMEC, who are an aggregator, who manage kind of multiple smaller accounts, they maybe still have like 100 customers. And one customer says, OK, I don't need these, you know, 10 wafers. Because, yeah, I just, maybe I can't get silicon for my other project. And therefore, I don't need it. So there tends to be a small number of wafers floating around occasionally like this, right? And because we're in the loop, we could sort of, you know, we just ask, you know, we'd said to iMEC, if you have spare, give us a shout. And we could pick up some of the stock. And yeah, again, because RP2040 is a very small chip. It's very economical with silicon. A few wafers goes a long way for us.

**Chris Gammell:** Yeah, 20,000 per wafers. There's, yeah, that's pretty crazy. I used to, so I used to work on, at Samsung in the 2006, the 8, and I was doing memory. And so they were, you know, not huge chips, but they weren't sized down yet. And they were much bigger than that. So like much fewer per wafer, that sort of thing. And it's also like 300 millimeter, right?

**James Adams:** Yes. Yeah. Yeah. So I think we're about, we sort of say headline two square mil. I think we're just a bit bigger than two square millimeters. But yeah, you still got a lot of diaper, a good diaper wafer. Right. Right.

**Chris Gammell:** And then it's like, in terms of like yield, it's high enough that it's like, you just, you don't worry about it, that sort of thing. Like it's, it's dialed in enough.

**James Adams:** Pretty much. Yeah. I think the small die on a, on a well, well known mature process, like TSMC40 yields very well. So yeah, we just package them up. We don't test the wafer. We just package them up and then we throw away the dead ones. I think we're kind of like, you know, 95, 96% yield, something like that.

**Chris Gammell:** Yeah. And yeah, there's benefits of being not on leading edge node too. That's, that's pretty interesting.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. Huh. What does it take to get, so you said like a hundred people are at iMac, right? How big do you have to be to get to that point? I mean, like.

**James Adams:** iMac helps startups, right? So that's, that's kind of what they do. They aggregate because big guys like TSMC, they don't want to, they don't want to talk to the really small guys because there's so many of them and they can't, right? They're, they're big. So they talk to someone like iMac, which aggregates all these chip, these smaller chip companies. And originally they helped us with a lot of the chip stuff. As we've got bigger, we've gradually sort of done more and more of it ourselves, but they also buy the wafers for you. Yeah. If you see, if you see what I mean. Yeah. Yeah. Like cashflow type of stuff. Yeah. It's kind of like an, I guess, ASIC incubator type.

**Chris Gammell:** Just distributor kind of thing almost.

**James Adams:** Yeah. Yeah. Pretty much. So that, you know, they were, they, they helped us bootstrap into the chip world. As almost any chip startup will do, they'll, they'll go to one of these incubators. Imex probably the, I think they're the biggest one and most well known. And they kind of help, help you, help you get going and yeah. Help supply your wafers. Even if you only need a few, they can provide that kind of, that kind of service where you couldn't just go and talk to TSMC.

**Liam Fraser:** And I guess the other nice thing is as well, we didn't have to decide how to allocate our wafers because we only had one, you know, we only had RP2040. So we didn't have to divide up a smaller number. That's right. Yeah.

**Chris Gammell:** Oh, you mean like if, if you were making the RP1 at the same time and then those had a lot of demand. Exactly. We'd have to pick. High five. Yeah. Right. Yeah. Yeah. And that does sound, yeah. Like I think about the companies that had like a TI that had like automotive, like breathing down their neck. It's like Chris Gammell is not getting any chips. Like I am buying from the bottom of the bottom of the barrel. Like I'm, I'm just the last in line. So it's fine. Right. I mean, like that's how it goes.

**James Adams:** I mean, it's really great that we could supply people with silicon in a, you know, a really probably the worst silicon shortage. I think anyone has ever seen it in the industry. So we have our commercial guy has been in the industry basically forever and it's the worst he's ever seen. I think if you go and talk to the really seasoned guys who've been here for a long time, yeah, no one's ever seen anything like that. But, you know, on the flip side, we're now aware that this kind of stuff can happen. And I think people are, you know, the fact that they're aware of that kind of risk is useful.

**Chris Gammell:** Oh, sure. Until, until the people retire and then, then it all happens again. Right.

**Speaker ?:** Yeah.

**James Adams:** Yeah. Hopefully we're kind of done with that. I'm sure there'll be other, other things at some point in the future, but you know, that was a really bad, that was a really bad situation. Oh yeah.

**Chris Gammell:** Yeah. Yes. My buddy who's in purchasing has told me stories that I, I just, that are somewhat unbelievable, but.

**James Adams:** I think everyone on both sides, purchasing and supply have just had a really tough couple of years. So. Yeah. Yeah. Yeah.

**Chris Gammell:** Hopefully we get a break just to chill out. That's great. So, okay. So let's, let's go a little bit back into RP one now. So you, you had the 2040, you've learned all these things. You had the scripting, you have the, the learning from PIO and similar kinds of things. And now you're putting in kind of, you already had some stuff in there, but now you're putting in kind of a higher speed, higher complexity things like ethernet, like USB three, things like that. One question I had about that, you mentioned you started in 2015. Does IP get old? Like, do you have like a new version that you update to? So like, if you buy an IP block in 2015, there's probably a better IP block in 2022, right. Or whenever you update it. So like, how much does it change from one generation to the next?

**Liam Fraser:** I can answer that. It really depends on sort of IP to IP. I think the IP vendors always recommend that when you do a tape out, you sort of pick the latest version of the IP.

**Chris Gammell:** It's like a package update. It's like a, you do like an NPN, NPM update and then you get the newest USB three. Yeah.

**Liam Fraser:** Well, once, obviously once we've sort of verified it, then, then we have to freeze the design and, and we won't, you know, once it's gone to TSMC, we won't, we won't be changing it unless it's a sort of a different version of the chip. But yeah, it's, you know, IP that you buy in still has bugs and they will sort of issue, you know, notifications of, of, of bugs. And then it's up to you to decide whether you want to take the bug fix or not. But yeah, some, sometimes we, we take a version change and nothing's changed. And sometimes you take a version change, do a diff and the whole thing's been rewritten. So it's a, you know, and, and if that does happen, then you're kind of like, oh, do we, do we want to take this, this new version? Because we're not sure.

**Chris Gammell:** Got it. And so, and you're saying diffs as well. So is it being delivered as Verilog? I mean, or is it, is it actually more piled down to.

**Liam Fraser:** So, so it tends to get delivered as Verilog and then we check all of our stuff into Git. So that allows us to, you know, diff it and see, see what the difference is. And yeah, every, you know, when we tape out a chip, we like tag releases of everything. So we know exactly what we've, what we've got. And the chip itself knows its chip ID, sort of its Git hash as it was taped out. So you can always go back and see what you made.

**Chris Gammell:** Positively software-y. Yeah. I mean, like, I know it happens in software, but it still like feels weird to me like that, to like hear it like that, you know, like, of course it's all software, but like, yeah. Yeah. In my head, I'm like, well, no, someone's like moving this transistor from A to B, right? It's like, no, that's not how it works. Yeah.

**James Adams:** Oh, we have a little tiny bit of that. Maybe not the transistor level, but when you get to the fettling of the chip before you kick it out the door, the physical design guys, often what we call, who we call the backend guys, you know, they are looking at the wires. They're looking at the physical transistors and the, and the different blocks and moving them slightly and connecting wires and things. So there's a bit of that, uh, looking at the ESD structures and, you know, there's quite a bit of hand fettling at the end for sure.

**Chris Gammell:** Yeah.

**James Adams:** Cause you've got to kind of broadly tell the tools, you know, where does, where does this stuff go as well? You know, how's the layout going to be? Where are all the pins? Right. Yeah. Kind of placing all the blocks. Yeah. Silicon, Silicon auto routers, right? Well, I mean, yeah, most of it is right.

**Chris Gammell:** Yeah.

**James Adams:** Placing route. Yeah. Totally. Describe the chip in Verilog, which is a sort of a higher level description language, and then compile it down into gates and then pull the gates into the, into the box in the chip. And then the, basically the tool kind of goes and goes and puts them in, in places and routes them. But then when you get to the, when you get to kind of the edges of the box, then you do have to do a bit more manual work.

**Chris Gammell:** Right. Yep. Yep. I guess I always think about like, obviously there's a lot of high value IP that's in there. Right. So like not cheap things, right. You guys are dealing with IP that's expensive because it was very expensive to manufacture and stuff like that. Is there any interesting process around that? Like in my mind, I think of like, like a golden USB key that has walked through the door with, with, you know, with monks in robes. But it, or is it just like literally like, oh, here's, we'll add you to the Git repo.

**Liam Fraser:** Oh, I can probably talk about this as well. Uh, so I also, well, uh, one of my many hats, uh, raspberry pie is sysadmin. So I, uh, when I first started, I sort of, uh, had a sysadmin background and then I've ended up doing a lot of other stuff as well. So we keep all of our servers on for ASIC on site. Cool. Yeah. Partially. So we know where they are and partially because we need a fair amount of compute. So, uh, I think each, each server's got like 40 calls, 80 threads, you know, 5, 12 gig of RAM. And there's like six of those and that, that kind of performance in AWS. It's a lot cheaper to buy the physical thing and plug it in.

**Chris Gammell:** Yep.

**Liam Fraser:** Yeah. So we know, you know, where our servers are, it's all encrypted. You know, you need an SH key to get onto it, all that kind of stuff.

**Chris Gammell:** Yeah.

**Liam Fraser:** Yeah. That makes sense. And everyone logs into them. So, uh, so, you know, you, you can't like copy stuff to your laptop, that, that kind of thing. Ah, yeah. And then also our backups are in a known, you know, with a known company and a known data center. So we sort of know, know where all the stuff is, uh, and yeah, try and, uh, try and control access to it. Got it. And pretty tightly. Yeah.

**Chris Gammell:** I wouldn't call that paranoid, but that's like responsible. Like it's just not, it's not super webby. Right. I mean, that's, that's kind of interesting because you, I would kind of imagine AWS and Azure and all the, the big processors, they love to talk about like instant compute availability, but, but they do love to charge for it too. Don't they? Oh yeah. It's like, okay guys. Well, there is some, there is some crossover point where it's like, no, no, no, we'll just we'll buy our own computers. Thank you very much. You know? Yeah. That makes a lot of sense. Yeah. That's cool. Okay. Yeah. That's great. So, but no, but no golden keys and monks and stuff like that. Huh? I mean, you guys are in Cambridge too. So I just imagine all the pomp and circumstance that the university has.

**James Adams:** That's just when we go to the, we just go to the pub and enjoy that. Yeah. Yeah. We just, as Liam says, you know, actually one of the things, our IT is quite simple. It's basically a bunch of encrypted disk and servers that we keep on site and backup encrypted to a known site. It's actually not particularly complicated and that's, that's nice because it's easy to monitor. And yeah, if you, yeah, you have to be a known good Raspberry Pi employee to get an SHH key. Yeah. That's good. To work on this stuff.

**Chris Gammell:** Yeah. I think, I think it kind of comes, comes back to that idea of like, it is software, right? You guys are working in software to make this very complex end result. And so many software things apply, right? Like you're saying SSH keys and all that, like it, it all makes sense. It is, you know, an IT organization type of thing. So like, yeah, it makes a lot of sense. It's, it's interesting. Yeah. Cool. So then what does it take to, so you, you buy the IP for the USB and the ethernet type. Like I, I, I guess I don't have a good feeling for like, so maybe, maybe this, if, if, if Chris was going to go start a chip tomorrow and I had gobs and bunny and maybe I hire some smart folks like you to come and sit in my IT center, which you guys are peering into my, my office right now, but let's pretend this is an actual legit operation. I could go out and buy IP for modern ethernet controllers, modern USB controllers. Is that, that the idea? Yeah.

**James Adams:** Yep. So we, I mean, there's no secret. Cause I think most of us in the day, we buy a lot of stuff from Synopsys, for example. Okay. Sure. And they supply the IT, sorry, the IP, you know, you've got to pay them money and support money and they, they'd sort of deliver it to you. Got to keep it secret as we've talked about. And then it comes with a manual of how to use it. You know, usually with a lot of pages that you have to read through and it sort of tells you how you, how to hook it up. Right. So things like USB, you buy the controller, which is the digital bit, which is written in Verilog usually. And the FI, which is this, the SIRDES, the high speed SIRDES, you know, the analog bit, we call it the analog bit. So it's because the high speed analog. Similar for the, you know, the MIPI CSI DSI cameras and USB, that's basically the model. I guess ethernet's a bit different because it's, it's kind of a digital only thing. And then you just buy some fast IO pads to, to run the RGMI. That's kind of, yeah, that's kind of it. And then what we do is, I mean, we design some little bits ourselves, but broadly, for something like RP1, it's stitching it all together. But there is a lot of work still in the, in the stitching, the cloths for each thing. Totally. The control, the GPIO, you know, all of that kind of stuff. I mean, maybe Liam could speak a bit more about that.

**Liam Fraser:** Yeah. And I actually wanted to touch on prototyping for FPG, on FPGAs as well. So like James said, this sort of chip version, what we call the ASIC version. So there'll be a controller and then the ASIC version will be like the controller and the PHY. So the analog side, but then you'll also have a sort of FPGA version, which is the controller. And then that will expose the sort of PHY interface on a bunch of signals that will come out of the FPGA. Okay. So for RP1, we used a pro FPGA system. So that's, it sort of has loads of daughter cards. So you can get a daughter card, which has an ethernet PHY on it and an ethernet jack, or one that has like USB three ports on it, et cetera, et cetera. So it allows us to test the controller with, with a real PHY and know that we've got at least that side, right. The ASIC PHY, you just have to simulate and then trust that, you know, if they've got it right and you'll find out if you've got it right when the chip comes back.

**Chris Gammell:** Yeah.

**Liam Fraser:** I think the, you can never run the FPGAs at like full speed. So I think the RP1 system clock is probably 200 megahertz and then on FPGA it will be, I don't know, 30 or something like that, but it's still enough. You can still run small bits fast, which is enough to run like the high speed interface of the USB three of the ethernet quickly. And also FPGA is a great for software prototyping because you can attach debugger. You can, you know, all, all that kind of stuff. Whereas simulations are very, very slow and you get, you know, sort of one millisecond will be one millisecond of SIM time might take, you know, five minutes, 10 minutes, depends on how big the design is, but it takes a long time.

**Chris Gammell:** And I always remember like looking, my FPGA knowledge is very 2004. So please excuse that. But I just remember like looking at the, the logic outputs basically from a simulator and just being like, it's useful. I know it's telling me stuff that is or isn't working, but it's just like, it's not, it doesn't feel real. You know, it doesn't feel like it's a, you know, it is, it is like, it's telling me important things, but it doesn't feel real. I know it's feels over real.

**James Adams:** I mean, on the digital logic side, simulators are perfectly accurate pretty much. Yeah. As Liam says, when you've got things like high speed fires, you can only kind of approximate that, and then you take these big Xilinx FPGAs and you compile your design onto one of those, run it slower, but at least then you have real digits, real IOs twiddling, talking to chips that are kind of fire emulation. And then you can actually plug real USB threes in. So we, you know, we had RP one on FPGA plugged into a, an Intel box over PCI express and had, you know, USB in a camera and a display kind of running in prototype. This is before we'd actually taped the chip out. Right. But it's basically running exactly, pretty much exactly as the chip would run.

**Chris Gammell:** Do you guys have any photos of that setup? I love those like old, like the, did you ever see the original like iPhone, like all on one huge board thing? I haven't seen that, but I can imagine. Yeah. It was just all dev boards, basically all, it was like a, it was like a full panel of a PCB and they just kind of shoved everything together. Like I love those old prototype photos. I think they're so fun.

**James Adams:** We must have some somewhere.

**Liam Fraser:** Yeah. I'm sure I've got some.

**Chris Gammell:** Someone's phone probably. Yeah.

**James Adams:** Trouble is this stuff takes a long time to, you know, how many, really a long time ago we took those pictures. I'm sure I've got some somewhere as well.

**Chris Gammell:** Yeah. Yeah. Google photos is how I do it. I just search for electronics and then Google photos. Like this is probably electronics. And I'm like, oh yeah, 2015. Sorry if I find my old stuff. I really like that. You guys have the, so like I'm looking, I'm looking at the data sheet right now and it says like each SSI. So this is for spy. Each SSI controller is based on a configuration of the synopsis DW APB SSI IP version 4.0.2. A, right? Like that's, that's great. That's like almost like traceable back to like the actual IP. Not that it really matters, but like, is there any concern about like, well, someone could just replicate this whole design? Is that, is that like of concern or not really?

**James Adams:** It's a good question. I mean, I think it would be hard to really replicate it exactly, but you know, you could with a, with a, with a design team and enough money and enough time. But I guess by the time you've done that, we'd probably be onto gen two or something. Yeah. I mean, you know, it's kind of like, you know, you could go build an Intel processor if you really wanted to with enough time and money. How much is it worth?

**Chris Gammell:** I think it also like, it kind of sidesteps the whole, like the value prop of something like the, you know, obviously your company and the RP 2040 is this finished thing that gets delivered to me. The user is like, is that it's done and it's tested. Like all of the other stuff that goes into it is the, like the software and, you know, the putting it all together, the, the optimizations that you're doing around this stuff. And yeah, there, you know, there is legitimate like competition out there. So I'm just getting curious about that. I think you guys probably have more scale than maybe some upstart might have, despite you also being upstarts, you know, it's all relative scale, right? You versus NVIDIA. It's like, oh, they're like, oh, okay. Ant, ant of a company, right? But, but like at one point NVIDIA was an ant of a company too, right? So like, that's the.

**James Adams:** That's true. I mean, you know, we do like to make this stuff open, right? Because, you know, it's just where we can, we like to, right? It's, you know, we can't open up more than, for example, in the controllers, what the synopsis will let us, for example, and we can't open certain things from the Broadcom stuff because it's Broadcom IP, but where we have our own IP, most of the time we really like to, to make it open. Yeah. People, people do kind of like, I think unreasonably say, oh, Raspberry Pi, they say they're open, but they're not open because yeah, the Broadcom thing, there's still, you know, there's still stuff there that we can't see and et cetera, et cetera. But over the years, we have really tried hard to make the platform more open. If you look at the firmware now, the, the firmware blobs really reduced down to just kind of some clocks and power stuff, you know, all the GPU stuff is, is open. You know, we're doing our best to push, push openness where we really can. And, you know, more stuff is upstream in the kernel now.

**Chris Gammell:** I'm sure in the 13 years of the amp hour, we have also complained about that at some point. And, but like at a certain point, you know, any layer of abstraction eventually runs into some kind of opaqueness, right? I think so. Yeah. Through the stack, right? It's just like, I don't know how Silicon, you know, I don't ultimately know what the process node is. Like I'm not going to get access to that, even if I have all of the transistor layout, whatever. And like the truth is at a certain point, it's just like performative, some of the openness, right? So doing the best you can and you're making good over, over, over strides overall.

**James Adams:** I think where it is actually valuable to people, then we'll always try and do it right. I mean, you know, making stuff on RP1 open, what's the value in that? Well, I mean, you know, we provide drivers for it and stuff, but at least you can now go and have a look inside this chip. And if you've got some weird, weird thing going on, maybe you can go and then hack on it and have a look. And if you want to do something funky with it, yep, off you go. You've got some data there and it'll be interesting to see what people do do with it. Yeah. Competition. There's always competition. I think we just like to, yeah, it's a balance, right? We don't ever really withhold stuff. Philosophically, we don't really want to withhold stuff for that kind of reason. If you see what I mean?

**Chris Gammell:** Right. Sometimes the IP agreement, so it's very big to know contract, I'm sure.

**James Adams:** Well, yeah, it's mostly just IP agreements. We can't release this stuff because it's not our stuff to release. But anyway, hopefully, yeah, RP1. And the documentation is not quite finished. I don't know if you've noticed, but yeah, it says draft all over it and we're still writing it. But it has got a lot of good information in there now, but we're sort of still fettling it. Just the whole Raspberry Pi release thing, there's just such a huge amount of work, peripherals, the documentation. You know, so we're, you know, the usual thing where we're kind of like peddling really fast

**Chris Gammell:** still to get it all going. I remember from the last time you guys were here too, just like the scale and the, I remember you talking about the cost of things and just like some of the design decisions that came around, like the Pico, I think it was. And just like, do we put a, there was some like button that you didn't have a certain button on there or you didn't have a header on there or something that was like a cost savings.

**Liam Fraser:** The run pin probably. What was it? The run pin probably.

**Chris Gammell:** The run pin. Yeah. Yeah. Yeah.

**James Adams:** People put on a reset button. I think that's so unreasonable.

**Chris Gammell:** Get a wire, folks.

**James Adams:** I think what you need to realize when you build these products, there's sort of a certain low, there's a low level of fixed costs that you can't really, you know, it's not a linear scale, right? It starts from a certain fixed costs that you can never get away from. So when you build these really low cost products, if you want them to be still good quality, like they, Picos have a hundred percent test, you know, they're built at Sony, they're built to a very high standard, that stuff, even though the materials going into it and the number of components is kind of, you know, it's not a lot, there's still that kind of fixed cost. And when you're trying to build a $4 product, you know, you really, you really have to engineer out as much cost as you possibly can. And yeah, people complain about like, why didn't the Pico have USB-C? That's a common one. Well, actually, USB-C connectors are twice the price of the micro USB. And, you know, that makes a difference, actually. And also, you know, we buy a lot of micro USB connectors. We had the supply there.

**Chris Gammell:** I think because you guys probably can't say it, I can say it. The right answer is, shut up, it's $4, right?

**James Adams:** Pretty much, right? Yeah.

**Chris Gammell:** I mean, like, people will always ask for more, no matter what price you are. You could offer it to them at 99 cents, they say, why is it at 98 cents, right? I mean, like...

**James Adams:** I get it, right? I think we all get it. It's like, as an engineer, especially, you're like, oh, God, if only they'd just done that, it would be just so awesome. And it's like, yeah, but we couldn't. Like, we did think about it, but kind of just didn't. You know, we've always got to make these trade-offs. And that is engineering in a nutshell, right? You're always making costs, you know, time. All this stuff is all a trade-off. And so, yeah, hopefully, you know, maybe in the future, USB-C gets cheaper.

**Chris Gammell:** So instead of optimizing that next thing, we went and just worked on the new thing to also optimize that for you, folks. Exactly, yeah.

**James Adams:** But so, you know, we kind of take some of the feedback. You know, we take the feedback, right? We listen to people. But we also, you know, we have to build this stuff and make it work.

**Chris Gammell:** I know we're much into the recording here now, but like the RP1 that lives on the Raspberry Pi 5, what is it for? I guess we probably should have led with that. It's a companionship to the Broadcom part that's on there that does all the Linux lifting, right? But what is the RP1 kind of generally meant for?

**James Adams:** Ooh, who wants to have a go at that? What is it for? I think we kind of already, we sort of spoke about it. It's too, what's the best way to answer this?

**Chris Gammell:** You had said, how about this? You said the word Southbridge.

**James Adams:** Yeah.

**Chris Gammell:** And that's like a term from like the Intel stuff, I think.

**James Adams:** Yeah.

**Chris Gammell:** I never really understood what that is. So maybe what is a Southbridge?

**James Adams:** So that's kind of the IO hub, right? So in past times, your IO hub would live off your processor, right? And that was called a Southbridge. And you had Northbridge, which tended to be the sort of cache and memory system, which that was the first thing that got kind of subsumed into these all-in-one these days, Intel and AMD processors. And so Southbridge was the kind of IO hub. Northbridge was the memory controller and cache. So yeah, it's a Southbridge. It's the natural evolution of the kind of architecture of the Pi, I think, really. It's taking the Pi-ness and putting it into a chip that is kind of stable. It's well-engineered. It's just the stuff we need. It takes the load off designing the main processor. And as you shift nodes down, as you go down from, you know, 2711 on Pi-4 is a 28 nanometer chip. 2712 on Pi-5 is 16 nanometer. The analog side, so there's all the PHYs, the USB 3 PHYs, the PCI Express, all this kind of stuff doesn't scale very well when you go down the small nodes, right? And as you go down the nodes, the silicon gets more expensive. So you've got kind of two wins there. One is you've got a stable thing that you've farmed out all this development work and you know it just works. And then you've also got the fact that you're not putting a USB PHY on this chip that's still the same size as it was on 28, but now your silicon's twice the price, for example. So it has a kind of a double benefit. And I guess people are re-realizing this. I'm not sure if it's complete revelation, but basically this is what chiplets are, right? So we kind of got a chiplet here. This is basically it, right? So we've done a chiplet architecture. We've used PCI Express, which is a standard. I mean, I think chiplets now, they're coming up with lower, you know, different standards, similar kind of serial standards, but, you know, lower power and designed to put these things next to each other on a chip substrate. But it's basically a chiplet architecture and done for the kind of the similar reasons, right?

**Chris Gammell:** I also think about the amount that I've abused Raspberry Pi pins in the past, you know, 5-volt tolerance, 3-volt tolerance, and just like, you know, you're moving down to 16 nanometers. Like, what is the core voltage on a 16 nanometer process? Like 0.9 volts?

**James Adams:** Yeah, it's like 0.9, 0.95. I think 1-volt absolute max. Yeah. So, yeah, the transistors, yeah, the transistors get smaller. Exactly. They're less stable. Actually, our GPIO pins on RP1 are hardened for ESD as well. So we actually did some custom engineering on those to make them more hardened to ESD strikes. Okay. So, again, it's just another improvement that can kind of help the thing be more robust.

**Chris Gammell:** Right.

**James Adams:** So, yeah, we can add all that kind of good stuff, and we can stop having to put it on the expensive silicon. Yeah. That's interesting.

**Chris Gammell:** You know, I'll just slip this in. Are there any Easter eggs we should know about in the RP1?

**Liam Fraser:** Liam? Well, I think I'm sure it's in the date sheet somewhere. It's definitely on Twitter and on the blog that there's PIOs in there. Ah. But there are, oh, sorry, there's only one PIO. I mean, yeah, you got to do it, right? But it's not accessible over PCI Express. I mean, I think that's sort of key architectural difference between RP1 and RP2040 is that RP2040 has got a really small bus fabric that's designed for, like, low latency. So if you want to go and read a peripheral, that will take one or two clock cycles on RP2040. Whereas because you've got PCI Express and you've got sort of big hungry busmasters like USB and, like, you know, cameras and displays, it's a higher latency but higher throughput fabric. So you might go and want to talk to a PIO or you might want to talk to a UART, let's say. That might take you 10 clock cycles, which is, you know, quite... It's perfectly fine when you're on Linux because it's not that long. Yeah. So RP1, it's not really a microcontroller. It does have some small ARM processes in it to manage it, but it's quite different. So to expose PIO, we effectively need a way for Linux to talk to the small ARM cores in the, like, little microcontrollery management bit to then talk to PIO on its behalf. So it's not quite as simple as just saying there's a PIO at this address. Yeah. Yeah.

**James Adams:** Makes sense. Yeah. And we are working on how to do that nicely so people can use it.

**Liam Fraser:** Yeah.

**James Adams:** So it's coming. I think we're just trying to... Yeah, we just want to make a nice way so that people can use it. Yeah. If we just expose how to hack at it, then we'll probably get 10 different ways and none of them work very well. But try and come up with a nice solution for people to load code into it and run stuff. I mean, actually, it's a good point that Liam brings up is because you're remoting the stuff over PCI Express, even just... Because a lot of people do use Raspberry Pis and bit bang the GPIO from the processor, which is still a relatively high latency thing, even on, like, a Pi 4. But it's much worse on a Pi 5, right? Because you've got this PCI Express bus. You've got to send your messages over before it can go and twiddle the pin. So there will be some cases where people are kind of doing this and it will be worse on Pi 5. Just bit banging an IO and expecting it to... It's sort of for something like WS2810... What are they? 2810B or what are they called? The little... The LEDs. That's right. Yeah. Yeah.

**Chris Gammell:** Those have, like, crazy... It's like... It's like the timing is... Yeah, specific time windows.

**James Adams:** Exactly. Yeah. That kind of just about works on older Pis because, you know, there's... It's generally fast enough. I mean, I still wouldn't recommend it, but people do. But on a Pi 5, that's almost certainly not going to work because your latency is higher to the GPIO and it's also more variable. Because, like, if USB bus traffic or a camera bus traffic gets in there, it's going to... You know, it's much more variable. Right. So, yeah, that is a thing. And, again, the PIO can solve some of these. So, we are going to try and make it usable. But it's coming. It's just not quite revealed yet.

**Chris Gammell:** Okay. That's cool. I mean, honestly, on... You know, when I'm using Raspberry Pis, I'm using other people's software. I'm using... You know, I'm just... I'm using off-the-shelf type of stuff. Again, as a hardware person, if I want to go in two little bits, I'm going down embedded because I mostly know how to do it. And, like, that's just what I know what to do. I feel like one of the challenges is that because Raspberry Pi is so... The Raspberry Pi board, right? The 4, 5, 6, whatever, is so broadly accessible and powerful and, you know, out there. People use it for all kinds of things because they don't know any different. I mean, like, I remember seeing the discussion on the RP2040 when it first came out and people were like, oh, this is never going to run Linux. It's like, no shit. But, you know, that's the context a lot of people come in with. And I was like, that's fine. But I feel like that's also, like, the best case scenario would be when you write to the slash sys, whatever, you know, GPIO. It sends a little message back on the terminal that says, have you heard about the RP2040? Or try MicroPython today. You know, like, C is your friend, you know? So, yeah.

**Liam Fraser:** Yeah.

**Chris Gammell:** The opportunity to educate. Yeah.

**Liam Fraser:** And we have, you know, where people are using standard Linux interfaces for, you know, for GPIO, for cameras, for displays, all that kind of stuff. We have implemented that for, you know, for RP1 and Pi5. You know, when we were sort of prototyping on FPGA, you might have a Linux driver that can, you know, shove a frame out over to a DSI display, for example. But then there's probably a year's work to go from that to I can support any DSI display at any resolution and present it as a video device in video for Linux, you know? And it's the same story for a camera and all that kind of stuff. So there's been...

**Chris Gammell:** And it's all upstream and, like, well-tested. Yeah. Right. Built without errors. And, yeah. I mean, like, there's so many... Like, that's one of the things that I think about, too. Like, you know, I am the piddliest little Linux user of the world. But, like, just the number of people that, like, are involved in the whole thing to make my RetroPie work, right? Like, I love RetroPie. It's so great. But, like, just the number of people in that software value chain that gets down to me so I could play, you know, Zelda. It's just... It's really crazy how many people are there. So it starts with you guys. That's great.

**James Adams:** Yeah. Well, I mean, it's amazing that we can provide the kind of hardware that, you know, allows people to do all this cool stuff as well. So, yeah, it's been a fun 10-plus years, actually.

**Chris Gammell:** 10 years, yeah.

**James Adams:** See how far we've come. Yeah. Yeah. I mean, for me, I wasn't a founder. But I joined, basically, as soon as... It was obvious that it needed some permanent people to sort of run it. But I started in the beginning of 2013. So, yeah, we're... For me, it's over 10 years now. But it's been fun, right? When we started, we didn't... We didn't even have an office. And now we're at, like, 120 sort of people on the trading, sort of on the tech company side, if you like. Yeah. And then another at least 120 on the sort of the charity side. So, it's become quite big. Yeah.

**Chris Gammell:** That's a silicon company right there, right? Yeah. A very small silicon company. Yeah, right, right. Of course. Yeah, yeah, exactly. It's all relative, right? Okay. So, last time, I'm looking at notes from our last show in 2021. I asked about using... I asked on the Raspberry Pi 5 if you said... If you were going to use the 2040 on the Raspberry Pi 5. And you said no, because of cost. So, is RP1 actually a cost-down version? Or is it just because it would be in addition to other things at the time?

**James Adams:** I mean, I'll tell you what. If we had our time again with RP1, we would have put a 2040... Kind of an actual 2040 in it. We've sort of got a proto-ish 2040 type thing. Uh-huh. As you can see, you know, there's a couple of ARM cores and a bit of PIO and some memory. But, yeah, I mean, it would have been really lovely to have had the whole thing synchronized so that we could actually put an RP2040 in it. Got it. But putting a physical one on the board, I mean, you know, it's a 7x7 QFN chip. Where would we put it? What would it do? As we've gone down the generations in Raspberry Pi, we've always tried to hoover up more and more of the function into the main bits of silicon, either the power management chip or the main chip or the I.O. controller now. And so what you see on something like Pi 5 is it's just got those big bits of silicon and a memory, of course, and Wi-Fi. And the rest of it's just kind of like connectors and capacitors and resistors. We've taken away a lot of control, sort of external control silicon type stuff. That's good for two reasons. One is it lowers the cost in general. And it also makes your supply chain a bit simpler. Yeah. So it's kind of a good thing to do. And also, yeah, board space is always actually now really is an issue for us. You know, trying to cram everything onto a credit card is getting trickier and trickier.

**Chris Gammell:** Yeah. Well, that's Eben for choosing that form factor to start with. That's, you know, you just got to give him a hard time, right? Come on, man. Why credit card? Why not like passport sized or whatever?

**James Adams:** I did have a prototype of Pi 4, which was three millimeters longer. And yeah, he... Hard no, huh? Basically, yeah. Basically just like poked me until it was the right size again. Didn't let me rest. Yeah. That was just not acceptable. And fair enough, right? We managed to squeeze it back again. Yeah.

**Chris Gammell:** Yeah. I remember. So I saw some of the stuff. I saw some people complaining online, which is like basically like a universal, right? All things complaining, right? But like the... I saw the ports layout change back, but it wasn't anything extreme. It's just like, yeah, you have to buy a new $5 plastic case for this new one. Okay, fine. Right. But it did change back again because of, I'm guessing, the geometry of the layout and stuff like that, right?

**James Adams:** Yeah, pretty much. So we decided on the how the... So it's another... If you look at Pi 5, if you look at the chips on it and you look at the routing, every chip has been co-designed or designed to have the pins and the wires coming out in exactly the right place. I guess the classic, the best example on Pi 5 is the PCI Express bus between RP1 and 2712. There's a big, just a big multi-lane motorway of differential pairs and coupling caps. And if any of those crossed over, you blow up your PCB board tech. Yeah. So each of these things has been designed to be exactly... The pinout has been engineered carefully.

**Chris Gammell:** Another benefit to doing your own silicon, honestly, right? I mean, like...

**James Adams:** Absolutely, right.

**Chris Gammell:** I don't get to do that when I'm just buying off the shelf. I'm like, okay, well, I guess this one goes all the way around here. You know?

**James Adams:** So that whole full stack thing really makes a difference. And yeah, we can get away with a six-layer board exactly the same as the Pi 4, the same PCP tech. It does have blind and buried wires, but it's still a relatively cheap PCB. And the PCB is quite a reasonable part of the cost of the Pi. So, you know, that really makes a difference, that kind of...

**Chris Gammell:** Well, eventually you get the... You do have some benefit of volume. I feel like... Oh, we do. ...the blind and buried. Yeah, that might... You know, eventually they're like, well, we'll give that to you for free, right? You know, you're making enough boards.

**James Adams:** Oh, no, we don't get anything for free. I know. But no, no, no. I mean, you know, we get relatively better pricing because of the volume. But, you know, each of those things is an extra process step and you do pay for it.

**Chris Gammell:** Five cents can impact the end result, right? Everything is cost-based. Yeah, totally. Yeah. Like I asked last time, I'll ask again, where's RISC-V in the Raspberry Pi? If I say, if I walked into the Raspberry Pi office and I said RISC-V, do I get pushed out the door? Or do I get welcomed in with it?

**James Adams:** No, I don't think so. We like RISC-V. I think we keep an eye on it. Yeah. Well, we have a kind of members program. I'm sorry, I forgot exactly what it's called.

**Liam Fraser:** I think it's the RISC-V Foundation, something like that.

**James Adams:** Yeah. Yeah, RISC-V Foundation. Pay our fees to keep an eye on it. I mean, it could be a thing in the future. It's just, you know, maturity of things like ARM. I guess when you're engineering these chips, ARM, and actually RISC-V have helped in this regard, is they've made ARM a bit keener and they've changed some of their processes to make getting their IP a bit easier. So that's nice. But in general, it's very easy to get hold of ARM IP. It works very well. It's well tested. It's well documented. The ARM cores, you know, they have very high performance cores if that's what you want. And, of course, that's what we kind of use. There isn't really any RISC-V equivalent. And then there's the kind of maturity of the software tools. You know, I think in the stack of maturity, x86 is way, way up here. And ARM's had a fair bit of, you know, attention down here. And then RISC-V has kind of got a long way to go, I think.

**Chris Gammell:** Yeah.

**James Adams:** And it's all of those things together just makes ARM more compelling at the moment, right? It's just the right answer. For us guys who have a small team and, you know, we need this stuff, you know, a lot of stuff in the RISC-V world just doesn't exist that we would need.

**Chris Gammell:** Right. I was wondering about that. Like you said, with all of the IP blocks that are, like, listed here, too, like, is it would be, like, you'd have to go and build your own SPI controller IP at that point then?

**James Adams:** That's got, you know, that's an independent thing to RISC-V, so that's not a problem. But it's more the process of calls, right? And then the software tools and debuggers and all of that kind of stack, right? The ecosystem isn't as mature as ARM. And, you know, we kind of, you know, we like ARM. They're a Cambridge company like us. And we have a great relationship with them. So it's just that, really, more than anything. So we're definitely not anti-RISC-V, for sure. We're definitely interested in it. But we also like ARM. Sure. Okay. That makes sense.

**Chris Gammell:** Yeah.

**James Adams:** They build good stuff. Yeah.

**Chris Gammell:** Yeah, that's great. That's great. Anything you'd love the audience to know or things to check out on the new Raspberry Pi 5 or the RP1 when they're looking at the Raspberry Pi 5 that they buy?

**Liam Fraser:** There's your signature hiding on the board somewhere, James.

**James Adams:** Oh, yes. Is that on every board? Is that why? It's under the USB 3 connector, I think. Yes. I think from Pi 4, because it's such a, yeah, I still do the layouts for these. It's become such a big, you know, it's a long-term project, right? Because we're, you know, we're designing these things for a long time because you're doing chips with the pinouts and all the rest of it. So to my mind, this is now kind of a bit of digital art. That's why I like to think about it. And I take a long time to make them look nice. So I just decided I'll just start signing them. And it's hopefully not gratuitous because it's then hidden by the connector. But, yeah, I kind of, like, put a lot of effort into it. So it feels like it might be a good thing to sign.

**Chris Gammell:** That's great. No, I think that is, I think Easter eggs and, you know, signatures and things like that, those are the things, too, where, like, that's just, like, trivia into the future, too. You know, like seeing old signatures under, like, the case of, like, early computers and stuff like that. You know, it's like we have to make our own mythologies, basically. It's fine.

**James Adams:** So I like it. Is there anything else to say about Pi 5? I mean, it's, I think we are, it's the most Raspberry Pi, Raspberry Pi. I think you've kind of already alluded to this, the fact that we've kind of touched every bit of silicon pretty much to make it work. I think it's, you know, kind of just advertising for Raspberry Pi now, but it's a great platform. You know, we enjoy using it internally. Right. Yeah. It's really fast, and it's going to get better as we evolve the software, and, you know, it's early days. So it's just a product we're very proud of.

**Chris Gammell:** Yeah. I was watching Jeff's, Jeff Geerling's review of it, and I was, like, looking at it, I'm like, that, I mean, that could, that could be something you just take with you and just play around with and have, you know, like, the display and the processing and all this stuff. Like, it's not a laptop, of course, right? But it's not, not bad. Definitely better than my old laptops. So, like, I definitely use slower and, like, you know, like, obviously the software is just so ubiquitous and useful. So, yeah.

**James Adams:** Yeah. I mean, if you want to use something like Office 365 or Teams or Google Meet, all this stuff now works really well on the Pi 5, whereas in Pi 4 is kind of a bit hit and miss. Nobody wants to use Teams. In the history of the world, no one has wanted to use Teams. Well, yeah. Sometimes we get forced to do this, but even Teams works very well.

**Chris Gammell:** Yeah, that's, that's interesting. Yeah, and I think that does actually open up other product ideas and, you know, just, like, accessibility to the underlying tech. And it's, like, it's not some bespoke thing. It's, like, an off-the-shelf piece of hardware that you can deploy for lots of different things now. It's great. It's really, really good. And I'm excited to have it. Guys, thanks for coming back on. I look forward to Raspberry Pi 6. So, get started. Get started on the RP, what are you, probably, 4, 5, 6? RP, 4, 5, 6, whatever's up there. And then Raspberry Pi 6. I'm sure there's no shortage of things to do. And, you know, or whatever, the RP, 20, 40, whatever the next thing of that is. Well, we'd love to talk more about that in the future. So, thanks for being here today.

**James Adams:** Been a pleasure. Thank you very much, Chris.

**Chris Gammell:** Thanks for having us. Cheers.

**Speaker ?:** Cheers. administered in administered Thank you.
