---
episode: 346
title: An Interview with Joe FitzPatrick
url: https://theamphour.com/346-an-interview-with-joe-fitzpatrick/
---

**Joe Fitzpatrick:** This is The Amp Hour Podcast. Released June 4th, 2017. Episode 346. An interview with Joe Fitzpatrick. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Joe Fitzpatrick:** Hi, I'm Joe Fitzpatrick with SecurityHardware.com.

**Joe Fitzpatrick:** Welcome, Joe. We're going to talk a little bit about, well, again, we're going to talk about hardware security. We've had a couple people in the past, and Dimitri recommended you join us, and I'm glad you did. Thank you for joining. Thanks for having me. I'm glad to be here. So could you tell us a little bit about how you got into that whole world and what your background is?

**Joe Fitzpatrick:** So my background was electrical engineering, but very far into the computer engineering and down into the silicon layer. I worked for a tiny CPU manufacturer for about eight years. I did speed path debug of CPUs, and then I moved into hardware security pen testing of desktop and server CPUs. That was lots of fun. But what I really enjoyed, both through college, before that, and since then, is training. So in the past four and a half years, I've been running my own business, securing hardware.com, focused on hardware security training, which turns out to be kind of a niche.

**Joe Fitzpatrick:** Yeah, definitely, definitely. Okay, so when you say pen testing around processors specifically, is that like you're on die, like actually probing silicon, or how does that work?

**Joe Fitzpatrick:** Well, it's all a matter of what is in scope in any given situation. So most of what we did was looking at software-based hardware attacks. So what code can I write that is going to use the internal silicon features, the instruction set, the built-in devices, graphics, anything else, to misbehave and allow me to essentially attack other things in the system?

**Joe Fitzpatrick:** Interesting. Okay. And so you basically had to have all of the – you had to know where all the demons were in the silicon, huh?

**Joe Fitzpatrick:** Yeah. And it's interesting. A lot of people who do security, they think about like layers of abstraction. And, you know, software security is all about like finding the flaws in the abstraction layer. But a lot of software people, a lot of security people, they get to the hardware and they kind of think of this as some sort of like bedrock and firmament that doesn't change. In all reality, hardware is, as we know, like layers upon layers of abstraction that have been built up over the past four years. Right.

**Joe Fitzpatrick:** Right. Yeah. That's – and so are you usually – so where would you usually start with that kind of thing? So would you start like attacking like a driver level kind of software or what would you – where would that usually start with and where would it end up?

**Joe Fitzpatrick:** So when I was doing that, you know, we had full internal perspective on everything. So I would do Verilog code review first before the silicon existed. And then once I found interesting things in that, you know, Verilog makes a lot of assumptions as you synthesize it. So those assumptions turned into my test cases, which sometimes, you know, I could confirm pre-silicon. Sometimes I had to turn those into post-silicon test cases to say, oh, if I set this address this way and run this series of instructions, what will happen?

**Joe Fitzpatrick:** That's – okay. And so did you have to know a lot about like how the Verilog compilers were working and everything then? Or – well, I guess the interpreters or however you say it?

**Joe Fitzpatrick:** Synthesizers. There's a few like very common errors. I mean in software security you have like your common class because I think OWASP has 10 top security issues. When it comes to Verilog, it really comes down to like misassigning and using the wrong variable name and poorly documented case statements. Like once you narrow it down to those two, suddenly you find 90% of your issues.

**Joe Fitzpatrick:** And so why the poor documented case statements?

**Joe Fitzpatrick:** Well, so with Verilog, there's a lot of assumptions that are made. If you make an incomplete case statement, it assumes what you expect to do. And, you know, you might think, oh, well, this branch of this case statement doesn't matter. It should never happen in hardware. I'll put an assertion in there just to check for that. That's great for testing, but assertions aren't synthesized on hardware. Assertions are just there for simulation and testing.

**Joe Fitzpatrick:** And so does that end up like in a state machine then? Like do those errors propagate down to state machines? Is that kind of what it ends up as or what?

**Joe Fitzpatrick:** Essentially. You basically expose things to software that shouldn't be exposed to software.

**Joe Fitzpatrick:** Oh, interesting. Okay. And so that, yeah. Okay. So you're saying that like, so usually a register set will be controlling some lower level hardware. And you're saying that something might pop out of that, that register might have access to that lower level hardware where it shouldn't. Is that kind of right?

**Joe Fitzpatrick:** Exactly. Or you have a situation where the documentation says very clearly, set this bit for mode one, set this bit for mode two. Do not set these bits at the same time. Well, what happens if we set these bits at the same time? Guess what I'm going to do.

**Joe Fitzpatrick:** Don't tell me what to do, document. Exactly. Oh, that's great. Wow.

**Joe Fitzpatrick:** Or another great one, which hopefully I'll anonymize enough. We had one part of the documentation which said, okay, this value is anded with that value. The other documentation for the second value said this value is ored with that value, right? And these two registers were used by two different groups for two different purposes. And both thought their logical combination was correct. Of course, in silicon, only one of those two combinations is going to exist. The question is, which one was it? And who was right?

**Joe Fitzpatrick:** Wow. Okay. Man, that's crazy. So, like, what – so, I guess you'd have to take us kind of where this all exists in the development timeframe, too, because I don't even know. Like, how far is it usually from looking at Verilog on a page to, like, a piece of silicon on your desk? I mean, I guess that kind of matters, too.

**Joe Fitzpatrick:** So, you know, the whole timeline from, like, conception and architecture to silicon, that's sellable, is several years. So, typically, it'd be like, you know, you spend the last year of development looking at the Verilog. And then you get first silicon. And you think, oh, this is great. I have first silicon. I can start doing my hardware tests. Except when you're doing security, your job is to make it not work. And it already doesn't work. So, sometimes it takes three or even six months and multiple steppings before you have a working platform running a working operating system before you can turn around and break it.

**Joe Fitzpatrick:** And so, it's, like, a lot of setting up a thesis of, like, oh, well, I think this will happen. And then you have to, like, really well document it so that future you looks back and is, like, oh, what was I thinking here?

**Joe Fitzpatrick:** Exactly. Well, and then the dilemma of if you have multiple products you're working on, you know, you might find – you might do the pre-silicon for product A and then have to move on to post-silicon for product B before the silicon is ready for product A. So, a lot of context switch.

**Joe Fitzpatrick:** Yeah, yeah. I mean, I think that's the thing that – so, like, you know, having you on here and then, you know, Mike Osman and Dimitri and everybody who's come on, Joe Grant, everybody who's been doing security stuff. I'm going to forget someone now. Colin. Colin, yeah. Yeah. Did I forget anyone? Anyways, I think the thing that – so, like, my perception of it has always been, like, oh, well, it's, like, this thing you do after the fact. You're not really – you know, I never thought about people that were at the companies doing this stuff. But the thing that it's – that way it's changing my mind is, like, this – it's this – not regimented, but this well-controlled – it's, like, it's an avocation, right? I don't know. Like, that's the wrong word. Yeah. But it's, like, it's a well-documented thing that happens.

**Joe Fitzpatrick:** Well, it sounds like that, but I would kind of disagree. There's really a very small handful of people who are doing this type of hardware security and pep testing. There's only a handful of companies that are making silicon that are big enough to actually care about and put effort into security. Well, I meant – sorry.

**Joe Fitzpatrick:** What I should have said is what – this is what – the way I've heard it described to me is how it should be done and hopefully more start doing it. Maybe that's a better way to say it? Yeah, perhaps. Yeah. Yeah. Right. It's just that the industry is – can be done, like, as, like, a studied thing, and I just never thought about it like that. So, that's cool. So, why did these companies that you were working for, why did – were they just big enough that they had hired you, or did you kind of – did you study under other people that were doing this kind of thing as well? How did you get into that piece?

**Joe Fitzpatrick:** I didn't actually come into where I was working from the security side. I came from the product side and built up a really deep familiarity with all the debug features in the products. Got it. That turned into very useful when it came time to, you know, look for people who needed to do the security testing as well. So, the group I worked with was a lot of people who had strong software security backgrounds and a lot of people who had strong product backgrounds. And together, you know, you had the audience of people who had hardware security capability.

**Joe Fitzpatrick:** Interesting. Okay. So, you said you got more into the training side of things. How have you seen things change? I mean, you've been doing training, you said, for five plus years? Yeah.

**Joe Fitzpatrick:** So, I started out training, and what we were doing is training all the people who were doing hardware validation. So, like, oh, does this interface work? Does, you know, memory accesses work? Do, you know, drive accesses work? Convincing them, like, okay, if you find something interesting, could you please recognize whether it has security implications and just flag that for us? Because when you're dealing with a giant, you know, product, a giant silicon product, you have hundreds upon hundreds upon hundreds, maybe thousands or more bugs. Some of them have security implication. Some of them don't. So, I trained hundreds of people who were doing functional validation on how to recognize a security bug. And I really enjoyed that and wanted to do more. And the timing all worked out well. That's what I decided to do when I left.

**Joe Fitzpatrick:** I see. Okay. So, you're doing internal training, you're saying?

**Joe Fitzpatrick:** Yeah. So, I was doing internal training, and that flipped into external training. But then I look at external, and I can't, you know, really – there's not a huge audience for silicon security.

**Joe Fitzpatrick:** Yeah.

**Joe Fitzpatrick:** There is a huge audience for embedded systems and now IoT and everything else. So, you know. You don't say. Wait. Wait. So, there have been problems with security and IoT? That's weird. People keep telling me about them. I haven't found any yet. Wow. Okay. I see opportunities, not problems.

**Joe Fitzpatrick:** Nice. So, how do things change then? So, now you're on the outside, right? So, you don't have access to register sets or, you know, hidden stuff. So, how does that end up changing things for you?

**Joe Fitzpatrick:** Well, so, what's really interesting is, you know, one of the things that frustrated me when I was working on CPUs is I'm dealing with, like, deep down in the middle of the silicon, barely documented or accessible to the outside world things. And there are security issues there, and they get found and fixed. But there's this whole world of embedded systems and low-hanging fruit and everything else that is, I should say, perhaps saying it's easier is not the best way to put it, but it's easier, right?

**Joe Fitzpatrick:** I like low-hanging fruit. That's good. I mean, like, yeah.

**Joe Fitzpatrick:** You go and you open up any, you know, off-the-shelf consumer electronics device, and there's a dozen things that will pop out and say, oh, this is interesting, this is interesting, this is interesting. Can I get firmware? Can I get, you know, JTAG or, you know, debugger control? Yep. Those are things that are very accessible to a wide range of people. They're actually really inexpensive to do these days. And, you know, in the past five years of doing trainings and working with a lot of consumer off-the-shelf products, I've seen an actual improvement in the security of these things, which is great.

**Joe Fitzpatrick:** Oh, that is great. Yeah. So, and, I mean, the thing that I always hear about with the security stuff, too, because I'm obviously on the outside of all this whole world. But the thing that I always hear is that, like, it's always the weakest link is still always people. So, like, you're saying, like, someone just hung the firmware out on the Internet, and it's like, okay, I'm going to go deconstruct this. Or someone didn't obscure the pads, or even if they did, they didn't do it well, that kind of stuff, right? I mean, like, all these things are very human-based errors where the silicon is a much deeper level.

**Joe Fitzpatrick:** Yeah. So, when you look at, like, the big picture, you know, I decide that there's some IoT device that I want to hack, right? I can look at it from the software perspective, right? I can, you know, go put it on my network and start doing network fuzzing, like throwing random input at it. I can do it from a purely network perspective and try and do something remote, you know, try and find these devices, you know, shared publicly on the Internet somewhere. I can do a physical approach where I open the device up and I look for debug headers and stuff, and I try and, you know, extract firmware from flash chips. Or I can do a deeper, like, silicon-level attack where, you know, I might use, like, a chip whisperer that Colin makes or some other attack to do a side channel attack or invasive decapping. Oh, yeah. Every one of those has a very different cost and time required and skill set required. And whichever one is easier is really where people are going to go. Yeah. So, I mean, I talk about in class, like, oh, here's eight ways to go dump firmware. But then what's the easiest way to get the firmware? You just go to the vendor's website and download it. Yep.

**Joe Fitzpatrick:** Yeah. That's true. Yeah. And that actually, okay, I remembered another name. Sammy was on the show, too. Oh, yeah. He talks about that stuff all the time where he's just like, yeah, I just did it with an Arduino. It's like, who cares? I'm just doing it. I'm getting it done. Whatever. I'm just throwing bits of this thing or doing whatever it takes. And, you know, those kind of methods, too, where it is. It's just you have this toolbox of ways to get into something and whatever wrench fits, right, or whatever socket set fits.

**Joe Fitzpatrick:** Exactly. And what's really interesting to me is when you're building a product, you need to make something that's got a certain level of reliability and repeatability. And, you know, you have to be able to manufacture it. So, you have a lot of parameters. So, what you're going to do in a shipping product is a much smaller subset of what you can do when you're just trying to get it to work once. So, you know, you can bit bang a protocol with an Arduino and have it work, you know, one in ten times, and that's a valid attack. But if you're shipping a product and it only works one in ten times, then that doesn't really work. That's not. Well, that product's probably not shipping. Hopefully not shipping.

**Joe Fitzpatrick:** Yeah. Yeah, that's very true. That's interesting. So, how does this end up? What kind of form does this take then? I mean, when you're – so, now you're out in the world. You're teaching classes. What are people, like, using this for or looking to learn? Is it, like, people that are building products and looking to secure them or is it something else?

**Joe Fitzpatrick:** There's – that was my interest at first. My focus is the product side. My background is the product side. So, I was looking to talk to the people who are designing products and get some security mindset in their work. What it turns out is there's a lot of people who are, you know, pen testers who work for security consultancies. And they're the ones who are doing the web-based pen tests, the software pen tests, and now are doing IoT pen tests. And they need the skill set to touch the hardware. What's interesting is I've had a lot of conversations recently and trying to tune what I'm doing in class. And people get, you know, contracted to do a pen test on an IoT device. And they say, we only want a software pen test. Like, well, why do you only want a software pen test? Well, because the hardware is hard. It's inside a case. We use screws that they can't get the bit for. Yeah. Yeah. And so, part of that is...

**Joe Fitzpatrick:** You know what you should do with that? You should just, like, you should have, like, a standard response where you just fire up a Dremel. Like, you know what that sound is?

**Joe Fitzpatrick:** Well, and that's the thing is giving people the stock responses to these excuses for why hardware is out of scope. And one question I often pose is, okay, I understand hardware is out of scope. You don't want to talk about physical attacks because you think that your hardware is expensive, hard to get, or going to be physically secured. What about the fact that I can buy one of these off the shelf, open it up, extract the firmware, and then I can do full, you know, reverse engineering of the firmware and figure out my software attack, figure out my network attack. Right. That's where I think the compelling reason to put hardware in scope is.

**Joe Fitzpatrick:** That's good. Yeah, no, that's really good. I mean, because you're right. I mean, like, people think that it's, like, this captive thing. Like, firmware is not something that's, you know, not accessible, right? It's like, yeah, it's only as safe as you're... As someone is not tenacious, right? Yeah. If they're tenacious, they're going to get it.

**Joe Fitzpatrick:** I talk at a lot of security conferences, and sometimes I get there and I speak and give a presentation, and then I get questions. And the questions often, like, point out to me, like, sometimes I'm worried I'm just basically getting up there and spouting out EE-101. And actually, I am. I'm up there spouting out EE-101, like, connect a wire, and we get signal. Like, that's it. But then the questions show me, like, wow, like, when you have a software background and you have a security background, the software is... The hardware is, like, a black box to you. And getting up there and getting people to understand, like, it's not a black box. There are ways in. There are nuances. There's lower layers. There's abstractions. That's really powerful. It's kind of like, you know, within the security community, everybody talks about, oh, you know, we're just, you know, the echo chamber. We keep going to conferences, and we have security people talking to security people, telling everybody how bad security is. We need security people going to, you know, development conferences and hardware conferences talking about security. And it's kind of the reverse of that. Like, I'm the hardware guy that goes to the security conference and says, hey, look, all these assumptions you made. Here's how they're perhaps invalid. Wait, you were about to say you're dumb, weren't you? No, no, I was not. All you guys, you're dumb. So, that's the other thing I say. I'm doing training for now because I want to teach all these smart security people how to, like, understand hardware. Because in five years, when all the smart people start doing it, I'm outclassed. Like, some of this stuff that these guys do is amazing.

**Joe Fitzpatrick:** Yeah. No, I know. And that's just, like, the stuff that they keep trying and, you know. And the mindset, too. I mean, like, it really is that tenacity that consistently impresses me of, like, well, this didn't work, so I tried this. I didn't try this, so I tried this. You know? Like, it's great. I mean, like, that is really admirable. Uh-huh.

**Joe Fitzpatrick:** Well, and, like, another example is one of the projects I worked on, one of the first ones I did was Slot Screamer as part of the NSA playset. It's a PCI Express device based off of an off-the-shelf chip that you can program to do DMA accesses. So you can stick this card in a system, and barring any other protections, you can go and read the contents of memory and modify the contents of memory. And you can use this to, like, bypass lock screens, modify kernels in memory, all that stuff. Wow. Okay. So what I did is I just did the basics. Like, I plugged it in. I had the proof of concept. You could read and write memory, and I had one example. And I thought, like, okay, that's cool. And it's really interesting because just this past year, another guy, he built a whole software suite behind this. So he's got this thing where you plug it in a system, and you run his software, and it goes and, like, opens up shells. It gives you file access. It does all this stuff. And all that is a layer of software built upon a piece of hardware. And it's just really neat to see this.

**Joe Fitzpatrick:** Yeah. Right. And it does it just, like, automatically. It's, like, I mean, that's, like, some movie stuff right there, right? Where it's, like, they plug it. I always remember the one where it's, like, you plug it in, and it's, like, running through the door codes. It's, like, okay, come on. Like, you know, like, that one always bugs me. But, like, that kind of thing where it's just running all these, it's just trying all these things, right?

**Joe Fitzpatrick:** Yeah. So the demo I had is, you know, you plug it in. And actually, at that point in time, Macs didn't have a couple protections they have now. So you plug in a Thunderbolt cable, right? And you just have it sit there, and it scrolls through, and it reads through your memory until it finds the code that checks your password, right? Wow. And it patches it, and then you walk up, and you bang, bang, bang, bang, bang, a bunch of stuff, and hit enter. Doesn't matter what happens, because it always passes, and it always removes the lock screen, and you're logged into the computer.

**Joe Fitzpatrick:** Oh, my God.

**Joe Fitzpatrick:** Luckily, they've put some countermeasures in place about that on Macs, at least.

**Joe Fitzpatrick:** They have done that since, or they?

**Joe Fitzpatrick:** Yeah, they've done that since. Mac 10.8.2 and later.

**Joe Fitzpatrick:** Yeah, update your software, folks. Yeah. Wow. So, well, I guess that's a good question, too, because I think when Mike was on last time, he was talking about his behavior in hotel rooms, but he unplugs everything from the walls and turns the TVs away. And, well, you posted that great picture of the mirror on Twitter yesterday. Okay. So, how do you view security now? I mean, what is your feeling about it all?

**Joe Fitzpatrick:** Well, it's funny. I have kind of a fatalist approach to it, right? We've got such huge stacks of software that are sitting on such huge stacks of hardware, and a lot of them are very poorly tested and stressed. So, what it comes down to is, you know, you've got all these, you know, ODA vulnerabilities, this, like, you know, leaks and drops of exploits. You've also got all the things that have been sitting there unpatched. You've got all these devices that are on, you know, ancient nulls that have vulnerabilities. So, really, like, and then you've got social engineering on top of that, like, the guy who showed up and pretends to be, you know, the guy from Amazon Prime delivering something some guy sent you, right? And, oh, I'm just going to plug this into my computer because he sent me a microphone to talk on the show. Who knows? This may have happened an hour ago. Who knows what this device is or, like, what extra firmware is on there? So, what it comes down to is there's so many issues, right? You have, like, basic security sanitation, like, you know, the whole password thing and don't trust random devices. And that protects you from the bulk of, like, the undirected attacks. But if someone wants to get on your computer and someone wants to get something you're doing, like, there's just so many paths to do that that, you know, if you're targeted, it's only a matter of time before the persistence pays off. Got it. Got it.

**Joe Fitzpatrick:** So, don't – So, you don't, like, avoid, like, network services or anything like that? Obviously, we're talking on one right now. Yeah, no. You're hooked into the internet. I'm on the internet.

**Joe Fitzpatrick:** I did turn off my VPN so that we would have lower latency on this call. But, you know. Oh, thank you. That's very nice of you. No problem. Yeah.

**Joe Fitzpatrick:** Yeah. Yeah. And, I mean, VPN – I mean, I think that – well, obviously, the internet is back kind of with the net neutrality stuff. That's kind of coming back up again and it's ridiculous. But that's – you know, a lot of people are talking about VPNs again and just general security stuff. So, you're just saying you're always through a VPN. You're always doing that kind of stuff. Yeah.

**Joe Fitzpatrick:** And, you know, I kind of feel like I need to have a slightly higher bar than the average person. But, you know, I avoid plugging in random USB devices that I get handed at conferences. Smart. Smart.

**Joe Fitzpatrick:** Yep.

**Joe Fitzpatrick:** You haven't, like, concreted your USB ports or anything like that? No, I haven't. And, you know, there's pros and cons to that. Like, paranoia versus usability.

**Joe Fitzpatrick:** Yeah. I wonder if the – do you think USB-C with all, like, the negotiation that has to happen between devices, do you think that'll actually improve things? Just because it's not, like, direct – Not at all. No?

**Joe Fitzpatrick:** Okay. Not at all. It is – so, basically, what we've got with USB-C, and I've done quite a bit of poking at it. Every device you plug into USB-C now needs to be smart. Any cable that you plug in that does anything beyond basic USB has essentially a microcontroller in it. Right? Right. So, I've actually got a USB-C to VGA adapter that I've been messing with. Okay. And, you know, I'm like, okay, so how does this work? I open it up, and I know USB-C can output DisplayPort. And on this little device is a DisplayPort to VGA buffer chip. Okay, that makes sense. There's also a USB power delivery chip and a USB microcontroller. And I'm like, oh, okay. So, let's plug it in and see what I can do. Oh, it turns out direct firmware update is available on this USB microcontroller. I can dump the firmware off of this device. I can flash new firmware to it.

**Joe Fitzpatrick:** Oh, God.

**Joe Fitzpatrick:** So, the way it works is it connects via USB 2 and says, oh, I'm a display adapter. Right? There's a little negotiation that happens and spits out DisplayPort. Okay, that USB microcontroller is sitting on USB. And now I can read and write the firmware for it. So, my theoretical attack that I have yet to implement because I have not had enough time to sit down and do it is, okay, can I make this USB-C to VGA adapter also appear as a keyboard that hits the forward and backward keys while you're presenting? So, you know, it just keeps changing your slide for you.

**Joe Fitzpatrick:** You just go around and you're like offering it to presenters like, oh, you got USB, you got one of those new Macs, you need one of these converters here? Yeah. Uh-huh. Oh, my God.

**Joe Fitzpatrick:** So, here's the dilemma, right? From usability, you've got this universal port and universal cable and a universal adapter. So, you don't have to worry about what you're hooking up. But at the same time, you have no way of knowing what you're hooking up. Right?

**Joe Fitzpatrick:** Yeah, yeah.

**Joe Fitzpatrick:** I look at a device. It's a box. It's got a USB-C cable. Is it a display adapter? Is there extra stuff inside? I have no way of knowing without like truly taking it apart.

**Joe Fitzpatrick:** So, like there would be – so, people listening might have a notion to build a product that basically intercepts the signal of what it's saying it is before you let it through or something. Like having like a – I mean, it would be a man in the middle, but it's like more like a monitor in the middle of like, you know, like what is this thing saying it is? And then is this okay or not okay? Is that like something that might work?

**Joe Fitzpatrick:** Yeah, like a USB firewall essentially.

**Joe Fitzpatrick:** Yeah, that's a great name for it. There you go. Yeah. Product idea.

**Joe Fitzpatrick:** So, I know there's USB proxy, the project that Dominic Spill did on the Beagle on Black, which I don't know what state that project's in, but it's only USB 2.0. But that kind of idea like, oh, you know, we have USB. We plug it through this thing. Let's look at the traffic. Let's filter the traffic or let's inject the traffic, you know, like. Yeah.

**Joe Fitzpatrick:** Right, right. And yeah, that was one used for testing and they were trying to do – Dominic works with Mike too, right?

**Joe Fitzpatrick:** Yeah, yeah.

**Joe Fitzpatrick:** Yeah, and they're trying to do like a USB protocol analyzer at some point, right?

**Joe Fitzpatrick:** Oh, yeah. Daiso. That's kind of an interesting project. I was just talking the other night with Jared Boone about it and wanting it to happen, but like it's just a very complicated and advanced project that requires a lot more time than any of us have.

**Joe Fitzpatrick:** Yeah. Well, you know, you guys get conferences and trainings to do, so people keep paying the bills that way, so that helps, right? Yeah. Nothing to sneeze at. Man, that is crazy about the USB-C though. Like I didn't even think about that because, I mean, you could also like – couldn't you plug in and say like I'm a mass storage device as well and I have the script to auto run or whatever? I mean not that auto runs always work, but.

**Joe Fitzpatrick:** So, I mean, you can basically have a situation where you walk up and you have USB-C and you plug in this cable that's coming from the monitor, right? And your display shows up on the screen. You're like, oh, okay. Oh, and you're also charging over that as well. So, okay, I have my laptop. I plugged one cable in, I see display and I'm charging. Oh, it also has a network adapter in there, so I'm directly connected to the network. Like, okay, that's cool. Oh, it's also a keyboard. Interesting. Oh, it's also a mass storage device. So, like you have one cable. You don't know what's on the other side until you plug it in. And suddenly you have connected all these standard IO ports on a PC to another piece of hardware.

**Joe Fitzpatrick:** I'm already getting like a little anxious, I gotta say. Maybe I shouldn't have gotten this one after all. Like, I'm really excited about USB-C. Don't get me wrong. Like, I think it's awesome in general, but now I'm like, oh, maybe not.

**Joe Fitzpatrick:** No, and I think it's great too. And I have an XPS 13, which I got like as soon as it was announced, which is one of the first ones that had Thunderbolt 3. So, it's on all the USB-C stuff plus PCI Express over it as well.

**Joe Fitzpatrick:** Oh, Jesus. So, there's no, is there any like in-between layer there? Like, what do you usually use that for?

**Joe Fitzpatrick:** Testing and playing with things.

**Joe Fitzpatrick:** So, why is PCI Express on that bus though? Like, what are they expected?

**Joe Fitzpatrick:** So, basically, USB and Thunderbolt kind of have converged into USB-C or Thunderbolt 3. So, it's the same connector, similar protocol, hardware layers. And it just means that, you know, there's one fewer adapter in the world, one fewer cable in the world. Well, that's not true because there's specific USB-C Thunderbolt cables that don't necessarily work the same as others. But, you know, it's a good idea, right? You're converging. You're going to have fewer cables, except it's not there yet, right? You actually, I think Apple has a great like list of all the different versions of the USB-C cables they have. Some of them do USB. Some of them do USB-C with DisplayPort. Some of them do Thunderbolt 3. Like, it's not easy.

**Joe Fitzpatrick:** Wait, don't some of the cables have to be like, not certified, but do they have like little ID chips in some of the cables too? Yep.

**Joe Fitzpatrick:** So, there's chip in the cable that identifies the cable. It identifies the way that the cable can maintain the power that you're asking to draw through it.

**Joe Fitzpatrick:** Yeah, right. Yeah. So. Yeah, because we had Jason Surundel on. Yeah, yeah. He was talking about some of that stuff.

**Joe Fitzpatrick:** I got his USB Type-C, you know, power delivery breakout boards to do some cool stuff. And I liked his toaster oven that makes cookies off of USB-C. Oh, yeah.

**Joe Fitzpatrick:** Yeah, I think it's fun. Oh, man. That is, okay. Wow. Welcome to the future, huh? Yeah. Well, so what else is scaring you these days? I guess these always turn into fear-mongering shows a little bit, but, you know, it's also like this kind of healthy, because it's like you guys are doing this because it's kind of clear and present danger type stuff. It's like, well, no, we should be thinking about this because it's out there, right?

**Joe Fitzpatrick:** What scares me?

**Joe Fitzpatrick:** I don't know. Well, I guess maybe I should ask about, you mentioned NSA Playset. I mean, you said, is that still going on? What's the deal with that?

**Joe Fitzpatrick:** Yeah, so the NSA Playset popped up after the whole Ant Catalog article that got published like three years ago, four years ago now. And so several of us all, you know, basically branded our hacks that year as NSA Playset, right? These are reimaginations or similar devices to what the catalog had, but we're going to do them with open source hardware and do them cheap, which is cool. On the one hand, the Ant Catalog was several years old at the time. Right. Yeah, they're on the next model. So we're, you know, we're mimicking the last gen. But yeah, it was neat because I guess the way I present it is before 2012, right? Our mindset of like, what is a hardware implant? An implant is kind of the intelligence term for like malicious software you put on a system. So the hardware implant is like a malicious piece of hardware you plug in somewhere. Our mindset was like, oh, what's what is a hardware implant? Okay, so basically mod chips for games and drive chips for game consoles was the extent of our public knowledge of what these things were. And then suddenly we see all these leaked documents and pictures of like, oh, we have a USB cable that also has a hub and a radio in it. Oh, we have a device we plug into the JTAG port on a motherboard and it persists malware. So it really changed my perspective on a lot of these things. And being a hardware person, what it also showed me is so first off, these things are real. There are people doing this stuff. A government agency is doing this, you know, a nation state doing this. But also it was neat for me is because all of these devices basically were hardware devices you plug in to give software privilege and then go away. Right. My mindset is always.

**Joe Fitzpatrick:** The hardware goes away or the software goes away?

**Joe Fitzpatrick:** It just doesn't do anything else. Right. My mindset was always like, oh, if I have hardware access, I can do everything. Right.

**Joe Fitzpatrick:** I'm a hardware guy.

**Joe Fitzpatrick:** That's how I think.

**Joe Fitzpatrick:** Right. You're thinking about a wire that's persisting and you keep pushing bits through what you're saying.

**Joe Fitzpatrick:** But the way these things were all designed is like, oh, here's a hardware device. It's going to sit on the bus and it's going to give root access to someone and then it's going to be doing nothing else because you've got root access. Why would you need to do anything else in hardware when you've got a root shell remotely?

**Joe Fitzpatrick:** Right. Exactly. And it's better because then it's not, it's harder to find. Right. Because that one time you have to actually be there right when it happens or else you don't detect it. It just looks like a dumb USB stick or whatever. Right.

**Joe Fitzpatrick:** Well, and then, and think about the number of people who look inside computers these days. Right. How many people would look inside their computer and notice if there's an extra board soldered on somewhere and think something of it. That's true. Yeah. Oh my God. Maybe people who listen to your podcast would, would not, you know, be concerned about that. But like the vast majority of people, like the thought of even opening a case is, is unfathomable. So opening it.

**Joe Fitzpatrick:** Yeah. Mostly for dust for me. It's just, you know, it would, it would hit my nostrils pretty hard, but yeah. But yeah, no, you're right. I mean, like you're saying like, you're saying like the, uh, now the Amazon Prime guy is, it's not the Amazon Prime guy showing up. It's, uh, it's one of those, uh, God, the Best Buy repair people, right? Yeah. And they're coming to fix your computer, but at the same time there, there's a new board in there and yeah, whatever. Oh, we made it faster. Yeah. It's an upgrade. Yeah. Right. Aftermarket upgrade. That's right. Wow. So, okay. So that changed your, your viewing of it. So does that mean that it changed, uh, the kind of stuff you were developing or testing for? Or how, how do you, how do you test for that then? Isn't it just like, well, open up your computers.

**Joe Fitzpatrick:** Good question. Um, how do you test? I haven't solved that problem.

**Joe Fitzpatrick:** Okay.

**Joe Fitzpatrick:** What it did, what it did for me though, is it made me realize that, um, you know, I didn't have to put all the effort into making this like hardware device that goes and, you know, pops root shells and deletes this and reprograms that. I just needed to have the hardware device that, you know, converted hardware to root shell and then software people would like understand the implications and the value of that. So again, my focus is training. I do like all my side projects and research, present those at conferences and, you know, hopefully, um, get people to think about hardware security a little bit more. Um, but yeah, so like, I don't need to, you know, do anything other than pop a root shell and then it's a software problem. It's someone else's problem. Right. Right.

**Joe Fitzpatrick:** And when you say pop a root shell, you also mean like, so it's connected to something else so that they could get to it. Right.

**Joe Fitzpatrick:** Yeah. Yeah. So, so an example is, you know, I mentioned the PCI Express one. The other one, um, is like JTAG, right? We all know what JTAG is. You hook it up, you get debug control over a CPU. Um, it's, it's more complicated for a software person to understand JTAG than it is to like understand like a serial console. But, uh, you know, if, if I can use JTAG and I have a little, uh, device, like basically an Arduino that runs, uh, through a JTAG, uh, through a, an X, an SVF, a serial vector format file, which is a series of JTAG commands, right? I plug that into a system and either hit play or have it timed to like play back a series of JTAG commands after a certain amount of time. And that series of JTAG commands could modify memory to change a root password. It could, um, I have one example where I have a PLC, right? A programmable logic controller that, you know, is used to switch on and off like dams or, you know, other industrial machine equipment.

**Joe Fitzpatrick:** Right, right, right.

**Joe Fitzpatrick:** And it's got these little plugs on the front where you can put like upgrade modules in. So you can give like ethernet connectivity or a USB connectivity to this thing. But if you pop that out and you look inside from the opening, you can see a 10 pin arm JTAG header. So what I did is I, I made a little device, I plugged a little Arduino in it and I had a script so when I plug that in, it gets power from the connector. It turns on, it waits five seconds, it halts the CPU and writes to a GPIO to turn off your output. Right. And so like, that's, that's the extent of a proof of concept I need at this point to show like, this is an issue.

**Speaker ?:** Right.

**Joe Fitzpatrick:** This warrants more investigation at the very least. Yeah. Yeah, no, that's true. And, and I think that, uh, so I used to work in industrial stuff and I talked to a couple of people where they were like, you know, they talk about all the, cause there was all these articles about hacking, blah, blah, blah. Like, like network connected power plants that didn't need to be, which of course, but like they always talked about it. Like, look, yes, those things are a problem, but like, if you really want to get at that thing, there's no security. Right. You know, there was no like physical security. There was no one, there was no gate. You know what I mean? Like it was like, yeah. So it's more about just having knowledge of the thing as well. I, so how, how do you deal with that? So like, okay, so you know, you know that there's a thing where you could go plug into, there may be a JTAG port there, but then how do you figure out that there might be devices to play with? You need like full access to the system to go and then say, well, when I do this, this turns on, or when I do that, this turns off. Is that kind of how you have to probe around or what?

**Joe Fitzpatrick:** Oh, so you're saying like, how, how would I, how would I adapt that to a real system?

**Joe Fitzpatrick:** Like an actual, yeah, well like, so once you have access to the JTAG port, I suppose, I mean, I know that you can, you have the chain and it'll identify devices, but then even still, what is your method for then going and saying, okay, well, I know this is, you know, a micro that's controlling a motor. Uh huh. Uh, you have to go like dump the firmware and like analyze it then, or what's the next step then?

**Joe Fitzpatrick:** Well, so from the PLC perspective, um, you know, I had a test system that I think I got off a digi-key, right? Um, I was able to open it up. I know exactly what CPU is inside. I can assume anything, the same model is going to have the same CPU, um, and the same base firmware. I didn't actually poke at the firmware at all. I mean, I just did the, the bare minimum of like, I have JTAG control. I can control GPIOs, right? I can reverse engineer the board and see where the GPIOs are connected to know what outputs of the PLC they're connected to. Um, so what I would have to do is, you know, let's say I, I go on a, a tour of like a dam or a power plant, you know, just look around and see what things are connected to. I'm not saying that I could figure it all out, but theoretically, you know. Right, right.

**Joe Fitzpatrick:** But then you might also be able to buy like a, like a board from a scrap house, like, right? Or something like that. And actually have access to like a labeled pin header or something. Right.

**Joe Fitzpatrick:** And, and it's, it's interesting you mentioned that because on a tangent, like, uh, there's been a bit of poking around at medical devices lately, right? Oh yeah. Yeah.

**Joe Fitzpatrick:** And so those things never change because of the, uh, yeah, the regulations.

**Joe Fitzpatrick:** So, you know, someone goes and they get a, you know, medical infusion pump and they take it apart and they find lots of vulnerabilities that are remotely exploitable. Okay. That's great. Now they go have the like discussion with the vendor. Right. And in my mind, the vendor should be like, Hey, thanks for doing this. You know, how do we, how do we fix this? How do we make it harder? Um, instead the vendor is like, well, where'd you get that device? Well, here's the problem. The problem is you got that device. If you didn't have that device, you wouldn't know the stuff.

**Joe Fitzpatrick:** You mean this device that you sell to people for a lot of money?

**Joe Fitzpatrick:** You sell it to hospitals and hospitals are supposed to like physically protect it or whatever, but you know, you can still buy these things on eBay. So it's very interesting that their concern, their mindset of hardware security is physical security still.

**Joe Fitzpatrick:** Right. Right. Or economic security in a way, right? Of like, Oh, well, this is not accessible to the public. So it's not a problem, but it's like, yeah, the, the places that are buying these high end pieces of equipment are often high value targets anyways. Right.

**Joe Fitzpatrick:** Yeah. Yeah. And, and, you know, I mean, what we're talking about what, you know, uh, researchers who publish everything they do, uh, uh, or most of what they do, uh, approach it, you know, like I'm not going to go into a hospital and steal an infusion pump and hack it and talk about it, but if someone wanted to, like, it's pretty easy to walk into a hospital and walk out with something.

**Joe Fitzpatrick:** Right. Exactly. Well, I guess that is, I mean, that's what it all comes down to, right? It's like, okay, will this happen? Probably not. But could this happen? Yeah. And, and, and that's, and, and then it's about like, who, whose responsibility is it that it doesn't happen? Right.

**Joe Fitzpatrick:** Well, will it happen perhaps at some point? Why doesn't it happen? Because no one's trying and no one is motivated and no one wants to cause. Because hopefully people aren't a-holes, right? Yeah, exactly. And I think that's the. However, history has proven there's a lot of a-holes out there. Yeah.

**Speaker ?:** Yeah.

**Joe Fitzpatrick:** So as a security measure, we should just make the whole world, uh, a-hole free, right?

**Joe Fitzpatrick:** Well, unfortunately that is sometimes the, uh, yeah, well.

**Joe Fitzpatrick:** Yeah. Well, tangent, different, different, different subject matter. Different, different podcast probably.

**Joe Fitzpatrick:** Uh, I, so I always do wonder how that conversation goes, right? So, so someone goes to a hardware manufacturer like that and says, or, or, you know, is publishing about this stuff. I, I agree with it. I think that it's, it's important, but if I'm being honest, Joe, uh, it, it always kind of sounds like blackmail to me a little bit. I know it's not, but like, you know, it's like, oh, well, this is, this is not secure. Uh, you should fix this. If it's, there's always like this, this thing at the, like, it's almost like this hanging sentence of like, and I can fix it for you. You know what I mean? Like, it's not, is that part of the culture or how does that work?

**Joe Fitzpatrick:** Well, I mean, there's part of that. Like there, there's a situations where, you know, someone targets a software, a product, whatever, and find something and then goes and reports it to them and says, I'm going to disclose in 90 days or, you know, next week. Um, and the company that receives that, um, perhaps they've never thought about security. Perhaps it's a mom and pop business or one, one person show. Right. And they're like, yeah, I'm, I don't make any money on this. Like I'm, I'm like doing a Kickstarter or something. Uh, and you're telling me that I need to spend X number of dollars for you or a third party to do a security analysis. Like, yeah, that, that does look a lot like blackmail. On the flip side of that, um, actually I've had this conversation the past two days regarding, uh, the, uh, case in Oregon where there's a, uh, someone who is being fined for calling himself an engineer, right? Oh yeah. Yeah.

**Joe Fitzpatrick:** We talked about that a little bit. Yep. I think we were supposed to maybe, but yeah.

**Joe Fitzpatrick:** When you're a professional engineer, right, you've got obligations. You, you need to, uh, think about health and safety and all that stuff. And, you know, if you're a professional engineer designing a bridge and you skip those things, you're liable.

**Joe Fitzpatrick:** If you sign off without being, uh, certified, right? Whatever.

**Joe Fitzpatrick:** But if you are an IOT, you know, home automation device developer and your thing uses unencrypted wifi to control the lock on your door, um, I kind of think there's, there's a similar realm of, of, uh, you know, uh, responsibility there. Um, so, so, you know, I, I'm not totally answering that. Like, yeah, it does. It does look a lot like blackmail, but at the same time, like, you know, the, the, we can also go down the tangent of like our vulnerabilities, free speech, right? Right. You know, I find this vulnerability, I can choose to sit on it. I can choose to report it to the vendor and give it to them for free. I can choose to report it to the vendor and threaten to, you know, publish it. I can sell it to, you know, uh, uh, on the, the gray or black or whatever market you might want to call it. Um, there's a lot of choices and there are better choices now than there were just a few years ago. We've got a couple of companies that, um, do bug bounties, like administer bug bounties and we'll actually help you, you know, communicate with a vendor to fix things. Um, but yeah, it's, it's all, all very different.

**Joe Fitzpatrick:** Um, no, no, I think that that's a good, that's a great example though about the lock, I think. Right. Cause like, okay. So then it raises a million dollars. It's out there. So do people are, do people deserve to know that it's a vulnerability, right? Maybe there's no economic, uh, bent. It's just like a true concern because you were interested in the product and you were looking into it. It's like, I don't know. I, I, I prefer to know that, you know?

**Joe Fitzpatrick:** And here's another aspect of it. Um, basically if, if anybody finds a vulnerability, right? Uh, an issue in software, um, you can have this assumption that someone else should be able to find it too. Right. So if I find out that this IOT door lock is trivially explainable, right? I can only assume that there's someone else doing the same thing and that someone else may or may not be willing to tell the vendor, may not be willing to, you know, publish it, may or may not be willing to, you know, use it illegally.

**Joe Fitzpatrick:** They might just be willing to walk into someone's house and make themselves a sandwich, right? And yeah. Sandwich. That sounds good. Security sandwich. Yeah. Yeah. That's a man. That is. Yeah. It's, it's like, uh, I'm sure that there's, uh, lots of conference talks about ethics in this kind of realm, right?

**Joe Fitzpatrick:** Unfortunately, not very many.

**Joe Fitzpatrick:** Really? Yeah. Oh, that's interesting.

**Joe Fitzpatrick:** Um, there's a lot of, uh, bars had kind of conversations about it. Um, but yeah, there are, there are some, but not the majority of conference discussions. Um, but yeah, there, there are debates on the ethics of it. There are the, the bug bounty companies, bug crowd, um, or one and others, you know, they really have ironed out the, uh, the ethics of that field pretty well. Um, so.

**Joe Fitzpatrick:** Well, that's great. I mean, that's, it seems like there's some people thinking about it. That's a, that's a great start. Right. So.

**Joe Fitzpatrick:** Yeah. And there's also, uh, uh, there's a, there's an ISO standard on like vulnerability disclosure, which is pretty cool. Um, really?

**Joe Fitzpatrick:** Do you know the number?

**Joe Fitzpatrick:** I do not know the number, but Katie Mazzaris knows. Okay.

**Joe Fitzpatrick:** I'll, I'll look that up on a disclosure. That's, that's a cool idea though. I mean, I think that especially like, I mean, obviously there's so much stuff about autos these days too. I saw something about like, um, how was it? Uh, can bus hacking recently. And they were like messing around with the radio via laptop. And I mean, that's limited hopefully, but yeah, there's some, there's some real implications there. You know, like it's, it's scary stuff sometimes it could be, it could get out there pretty fast.

**Joe Fitzpatrick:** Well, and yeah, that's, there, there's been people hacking on automobiles for a decade now. Um, but what was really interesting about the whole Jeep case is there was a string of issues all tied together that basically allowed you to do a lot of bad things to a vehicle. Um, and you know, when you, when you just report it, then the vendor's like, oh, whatever, you know, we'll, we'll do an update. We'll do a recall and flash the firmware when the next time they bring it into for service. But when you go and like have a video of someone like getting pulled over on the side of the road because their engine cut, suddenly everybody's getting USB drives to do it immediately. Um, so, you know, I, again, is that blackmail? You could argue. Yeah, it is. Is that in the best interest of the safety of people? Probably.

**Joe Fitzpatrick:** I'll tell you what, I would probably, if, if it wasn't fixed, I would probably cancel the next Uber that showed up was the Jeep. Uh, yeah, you know, like that's kind of what it comes. You're right though. At a certain point, like the only thing you have left is like kind of public opinion and yeah, it's interesting. Well, uh, speaking of conferences, you seem like you're, it seems like we're kind of ramping up conference season, uh, and you've been doing a lot of training. So what's your, what's your next, what are you kind of moving towards on trainings and everything?

**Joe Fitzpatrick:** Well, so next week or the week after next, I'm headed to recon and I'm going to help Dimitri with his class on, uh, um, hardware reverse engineering and tooling, um, using, uh, FPGAs. Um, and then black hat, I've got a couple of classes, uh, focused on embedded systems and kind of integrating, uh, that into a hardware pen test. But the big thing that's coming up is myself, Dimitri, um, Colin O'Flynn and Joe Grand are all working together to have like a, a big hardware hacking training event in San Francisco in November.

**Joe Fitzpatrick:** Uh, what's it, what's it called?

**Joe Fitzpatrick:** Uh, uh, hardware security dot training.

**Joe Fitzpatrick:** Uh, editor's note, uh, that was hardware security dot training. Just had to cut in here.

**Joe Fitzpatrick:** Pretty straightforward URL. Um, so I'll be teaching my classes on embedded systems. Uh, Dimitri will be doing his on using PGAs for tooling. Joe Grand has his on basics of, uh, logic analyzers, soldering, and, uh, identifying systems. And Colin has his class on side channel attacks. Um, so hopefully there'll be something for everyone there. Well, everyone who's interested in hardware security, at least.

**Joe Fitzpatrick:** Is that like, uh, they're all kind of concurrent? They're all, uh, you can only take one or is it like you kind of take them all?

**Joe Fitzpatrick:** Uh, uh, Dimitri uses a four day. The rest are all two day classes. So you could compare up a couple of them. Um, the other thing we're, we're looking at doing is we're going to try and get some speakers to come in during lunchtime. Um, so not only would you get some training, you'll get a little bit of, uh, you know, new stuff coming from people who do hardware stuff, hardware security.

**Joe Fitzpatrick:** That's great. That's, um, and that's going to be in San Francisco. What, what dates in November?

**Joe Fitzpatrick:** San Francisco, November 6th through 9th. Great. It's a Monday through Thursday. That's great. And you know, it's, it's like the hardware, hardware security conference without the conference.

**Joe Fitzpatrick:** All the conference activities will be held at the bar after, after, after hours, right? That's cool. That's a really good, that's really good. So, uh, so people, okay, so people who are listening, uh, who may have heard other shows are looking to get more into this. What, what is your usual go-to for like, you know, how do you usually recommend people start getting into this stuff? You know, maybe with training, but even otherwise or at home?

**Joe Fitzpatrick:** Um, well, so I don't have a, I need to come up with a list because I get the question a lot. And basically every, every month or so someone has taken an, like an off the shelf embedded device, taken it apart and done the basic hardware hack on it. And I love reading those because most of the time it's someone who's new to hardware hacking. It's someone who may have pieced together things they found in blogs or other places and applied them, but it's really great to see different people's perspectives and approaches on how they tackle the same problem, um, and what they do with it. So, um, yeah, I should make a list of these blog posts that I've seen. Um, one, one standby is, uh, um, Craig Hafner's dev TTY is zero. He's got a lot of information on, you know, focusing on these embedded devices and taking apart.

**Joe Fitzpatrick:** Um, and so what's, what's the usual goal of that kind of thing of just like, like owning the, owning the, um, the network traffic from it or what's the, what's the ultimate goal for that thing?

**Joe Fitzpatrick:** Um, it depends on who does it, but it seems like it's consistently like, I want to get a device. I want to open it up. I want to understand what it's doing. I want to get firmware off and then use the firmware to figure out how I can make it a software problem.

**Joe Fitzpatrick:** Okay. That's yeah. That's a good way to say it, I guess. Yeah. That's like, uh, so having some kind of control so you can make it do a thing without, without, uh, that it wasn't meant to do. Right. I guess. Right.

**Joe Fitzpatrick:** Yeah. And the kind of things people find, they find like hardwired backdoors. So like, yeah, we took a hardware approach, but we got the firmware and we reverse engineered the firmware, we find this string. And when I go to that, that page on the, on the device, like on the network, it automatically authenticates and logs me in and gives me control over the device. Um, another thing is, you know, devices store keys that let them communicate with a backend. And a lot of times they give too many keys, um, you know, private keys instead of public keys. Um, so all sorts of devices, things like that, you know, uh, figuring out what root passwords are, hard coded passwords, all those things, uh, pop up really quickly once you've got physical access and you can dump the firmware.

**Joe Fitzpatrick:** Right. Yeah. I guess, isn't there like a list of, uh, default passwords for like webcams and all that stuff that's like, there's like just standard passwords for a lot of things that are out there.

**Joe Fitzpatrick:** Yeah. I know. I know. I've heard of that, but I, I, it's not coming to mind immediately. Most of the time I just Google like, you know, model number and find the manual and it tells me the default password. So.

**Joe Fitzpatrick:** Wow. Again, the, uh, the easy, the easy solution is the right solution.

**Joe Fitzpatrick:** Yeah. So like I'm at a hotel and they have like metered internet because apparently some places still do this. And I go to their like in page and it's like, oh, it's a, you know, whatever brand go online, find that brand, you know, find the default password. And sure enough, most of the time it works, you know, really that's, that's the usual approach. Yeah. Okay. And then I go to the front desk and I'm like, oh yeah, thanks for the internet. Oh, by the way, you still using the default password. And the response is usually like, oh yeah, but no one knows that. And yeah, maybe you did, but like, it's not worth the effort, right. To, to fix that.

**Joe Fitzpatrick:** So you get to be, you get to be a superhero on a network just because they're, they're too lazy.

**Joe Fitzpatrick:** Yeah, pretty much. I mean, if you look at it, if you look at the cost benefit, right. Like it's not worth their time and effort, right. Unless someone comes in and maliciously, maliciously takes down all their network or uses all their metered data, it's not going to affect anyone.

**Joe Fitzpatrick:** Yeah. That's a good point. Right. And then, so it's just kind of status quo, like, well, or they don't know how to do it in the first place. Right.

**Joe Fitzpatrick:** Yeah.

**Joe Fitzpatrick:** Wow.

**Joe Fitzpatrick:** Well, and you look at it like, well, I have x-ray vision, so maybe all of you want to start wearing lead clothing and, you know, maybe some people do, but not everyone has x-ray vision. So is it really worth walking around with, you know, a hundred pounds of clothes on? Maybe, maybe you'll just see my nethers. Who knows? Or maybe I'll just close my eyes all the time. Yeah. Wear lead glasses. Right, right. Yeah. Yeah. Actually, that's an interesting one. That was probably not the greatest analogy, but it came to me in a moment. So, yeah, that's what you get.

**Joe Fitzpatrick:** So you had sent me some of, so you do talks all the time as well. Are you like, do you have a bunch of those on YouTube as well? Yeah. Or are they mostly just slides?

**Joe Fitzpatrick:** You know, I have been meaning to index them more thoroughly, but yeah, a lot of conferences will publish them and put the videos online. And the most recent one that I know is online is from Troopers in Heidelberg in March. And before that, there was a couple at Hardware.io in September and Black Hat last year.

**Joe Fitzpatrick:** And what are you usually doing? Is you usually like building a, or you're doing an exploit and then you kind of talk about it? Or is it like you do more general stuff or what?

**Joe Fitzpatrick:** Well, so I found that like I've started to start a lot more projects than I finish, which I know no one else has that problem.

**Joe Fitzpatrick:** No, no. Definitely no one listening to this show. It's unique to me. Yeah. No one you're talking to right now.

**Joe Fitzpatrick:** So what I've kind of done is I've realized, okay, well, even the projects I've not earned into like a fully crafted, you know, end product, I've learned something and I can take a handful of these and put them together and actually get some valuable information out of them. So what I've been presenting on recently and a derivative of this will be presenting at DEF CON this year, along with my co-presenter, Mike Leibowitz. We took a bunch of hardware security modules, right? So like YubiKeys, RSA tokens, and TPMs and kind of looked at them and said, okay, well, what's the threat model that people used when they decided to use these devices? Like, okay, we think our computers own, so we want a YubiKey that's going to be our login authority. Right?

**Joe Fitzpatrick:** And that's like the thing where it like looks up the code over based on time or whatever, network based or whatever.

**Joe Fitzpatrick:** Yeah, you touch it and it gives a one-time password that spits it out on your screen, into your like login box. And it's, you know, it is, it's far more secure than just typing in a password that you remember that you keep in a passwords.txt file on your desktop. Oh, okay. But like, we trust these devices. And if we leave this device out for a few minutes, can we still trust it? It's a good question. And so we kind of went around and poked at different ways of cloning YubiKeys, which we didn't clone a YubiKey, but we made a fake YubiKey from scratch. And with this added feature that when you, when you plug this YubiKey in, it not only shows up as a YubiKey, it also shows up as a keyboard, or sorry, as a mouse. And so when you mouse over our webpage, right, the mouse jiggles and that jiggling exfiltrates the key that's securing everything. Whoa, wait, what?

**Joe Fitzpatrick:** Did you follow? No, no. So wait, you're saying that if I have this thing plugged in and I go to your website, it's going to, it's going to do something?

**Joe Fitzpatrick:** So we took, a YubiKey is a thing, right?

**Joe Fitzpatrick:** Sure. Physical device.

**Joe Fitzpatrick:** Made at one, a device that looks like a YubiKey and acts like a YubiKey and authenticates like YubiKey, right? But when you are not using your mouse, it jiggles the mouse around, right? So it shows up the mouse as well as a YubiKey and it causes the mouse pointer to go up, down, left, right by one pixel, right? When you go to a malicious webpage and you mouse over it, right, the JavaScript on the page is always grabbing the mouse coordinates and it can decode the data that was being sent, right? Oh my God. Does that make sense?

**Joe Fitzpatrick:** Yeah, yeah, yeah. Oh, yeah. Because you're saying like, there's like analytics plugins that do like, where are people putting their mouse, where are all these things happening, right? That's always being captured, right?

**Joe Fitzpatrick:** Yeah, yeah.

**Joe Fitzpatrick:** Okay.

**Joe Fitzpatrick:** So yeah, so basically we have this device that looks like a YubiKey, it's not a YubiKey. It smells like a YubiKey, it's not a YubiKey. But it also leaks out your secret key in the process.

**Speaker ?:** So.

**Joe Fitzpatrick:** Wow. Just kind of undermining, changing the way people implicitly trust their hardware is what the objective is.

**Joe Fitzpatrick:** I mean, Joe, at this point, I don't trust a damn thing. I don't know, I don't even know if I'm talking to you anymore. Like what, is this even a microphone? Like what? Wow. Okay. Yeah. Okay. So what is, so this is the, you sent me one of the talks. Is this like the, there's an RSA token as well? Is that the same thing? Or is this a different talk that you're talking about?

**Joe Fitzpatrick:** Yeah, yeah. The RSA token. Yep. So that, yeah, the RSA token, we just kind of like said, oh, well, you know, this device spits out a random, not random, a cryptographic six digit number every minute. Like we normally, if someone would try and get the key out of that, but instead, let's just add Bluetooth to the device and read the display and, and broadcast the six digit pin.

**Joe Fitzpatrick:** Yeah. Okay. Yeah. I guess that works too, huh?

**Joe Fitzpatrick:** There's, there's, there's all the matter of like how, how quick can you do it? How, uh, how effective can you pull it off? And like, does the hardware look like it's the original hardware when you're done? Who knows? But yeah, it's all worth, all worth a try, you know, exploring what's possible.

**Joe Fitzpatrick:** Hmm. So what I'm hearing you say is that if we are going to design security devices like YubiKey or something similar, there should, we should have like a, like a squid, like a, or like one of those things when like bank robbers, like rob a bank and then like they open up the, the bag and it spurts ink everywhere. You should have like something like that, like a tamper detective device or something and everything.

**Joe Fitzpatrick:** Well, I think, um, the, the, the call to action that I usually throw at the end is, um, if I'm getting a hardware device from someone, um, I should have a way of authenticating that it's legitimate, right? Yeah. Um, and if you go to, uh, YubiKey's forums, you know, you look on the back, it's, uh, you look at what they say, it's like, oh, well, does it say powered by Yubico on the back? Like, well, I can, I can print that on the back of anything. Um, you know, and they, and they do have a cryptographic way. So there, there is more to it than that. But like any, any device that you have that, you know, you want to trust or you're expected to trust, you should have a way to verify. Um, the other side of it is one of the reasons we've gotten this situation is because hardware vendors don't under, don't understand or don't worry about security implications. So you buy an SOC from a vendor, you put it on a board, you sell the board to an OEM, the OEM puts a badge on it and sells it. And, you know, someone puts software on top and sells that nowhere along the way has anybody expressed any security expectations. So the SOC vendor might think like anybody who has physical access to this SOC can reprogram it. And that's a valid assumption. The problem is they don't pass that along. And, you know, it's the first step in the process is making sure everybody passes along their security expectations, the silicon to the hardware to the products.

**Joe Fitzpatrick:** So what would that look like in a perfect world for you?

**Joe Fitzpatrick:** Well, um, I can't recall the, the router firmware, but basically, you know, the, the vendor of, of silicon says, Hey, you know, we cannot guarantee anything if you have physical access to this device. And then they say that when they sell it to, uh, the, the board developer and the board developers understands that and they build a product and they say to the software team, Hey, by the way, we can't guarantee anything if someone has physical access to this device. And then the software team takes that into consideration and says, Oh, that means that they can get access to anything that's on this device. Um, and considers that when they design the software and market the product.

**Joe Fitzpatrick:** And so, yeah, no, I think you're right. Yeah. I think so. Like they might put like a, I mean, not that it couldn't be bypassed, but it might be like put a light sensor in there. So if the box is opened, it wipes the firmware or something like that.

**Joe Fitzpatrick:** Well, and then that's, that's another path, right? How about hardware countermeasures? Right. Um, and some point in time people say, Oh, we'll put, we'll put, we'll put, uh, you know, a moisture sensor. So we know if you dropped your phone in the water, we're going to put a light sensor. So we know if you opened the case. Um, and if you did that, then we'll void your warranty. Um, but all the cases I've seen of that are mostly companies trying to protect their own IP and their own liability, not protecting users of the device and their data. They're also, in my opinion, expensive and often trivially exploitable as well. Yeah.

**Joe Fitzpatrick:** I mean, I guess you can go in a dark room, right? Yeah.

**Joe Fitzpatrick:** You can open the case in the dark. Yep. Uh, yeah. The, the old, uh, femto cells, the little like grow, uh, uh, cell phone towers. Um, the original one, I think the 18 pad, when you opened up the case, there was wire, like a little plastic cables attached to a bunch of jumpers. And when those jumpers got pulled off, right. If you tried to power it on again, it would like wipe some and, and, you know, set a tamper flag. And it was like three or four jumpers that had a special arrangement. And if you put them on the wrong way, it would also set that tamper flag. So, you know, there's all these tricks that some people have tried, but I don't know that there's many truly effective ones at this point. Yeah.

**Joe Fitzpatrick:** Right. Well, like you, like you said at the top too, though, you said if someone wants to get in your, if someone wants to get in your device, they're going to eventually. So it's kind of more about, it's like a cat and mouse game of what's the most you can do for the reasonable cost that's not, you know, super, you know, you have to be better than any other than the competition, of course, and hopefully you're better than the majority of cases, but at a certain point, someone's going to get in. So what's the most you can do?

**Joe Fitzpatrick:** How much can you expect to make by fully exploiting my system, right? How much, what's the dollar value of the information on my computer or, you know, et cetera, et cetera. That's, that's the, the indicator of how much effort it's worth to exploit you, right? Yep. So if I have, you know, top secret plans for next generation aircraft or something, that's a little different from having, you know, a customer contact list and my email passwords.

**Joe Fitzpatrick:** Yeah. Well, but you're still saying, I mean, it's still important, right? I mean, it's still like something that people should be thinking about. So I guess when I, you know, where do you see the future of hardware security going? Like in general, like with pen testing in general of like, like device testing, everything that's out there, like where, where do you, where, where is the, where's the general direction? Is it, is it happening more? Is it happening less? Is it, is there, is there more needed? What's your opinion there?

**Joe Fitzpatrick:** What I see from the like consumer electronics embedded device realm is in the past five years, suddenly vendors have stopped obviously marking JTAG and UART test points. Um, they've started to, you know, have dead consoles. They've started to disable JTAG on their devices. Um, so there's progress even in the past five years. And so what can I see in like five to 10 years? Um, I see a situation where when I go to the store and I open up a device, right, it's going to be a PCB with one, maybe two pieces of silicon on it. Um, with no test points, no real understanding because, um, so much of the functionality is integrated into a single piece of silicon that anything except for silicon attacks are going to be, uh, very difficult. Um, so from a hardware perspective, I think that's where it's going. I think that the golden, uh, uh, the golden era of hardware hacking on embedded devices is, is going to not last that long. Um, well, that's not true. It's going to, it's going to be a few more years, which is long enough. Um, on top of that, we've also got, uh, software improvements, right? So as software gets better, as, as, uh, coding gets cleaner, um, we're going to have fewer and fewer software issues. And when software is harder to hack, you know, anybody who really wants to get into a system is going to look for the cheapest spot. And that might be hardware. That might be silicon. So it's just a, it's an ever-changing, uh, equilibrium. Uh, what people target is going to change over time. And, uh, we're going to slowly improve the hardware and, uh, probably slowly improve our, our, uh, attack capabilities as well.

**Joe Fitzpatrick:** And at the end of the day, it might end up being just go after the humans anyways, right?

**Joe Fitzpatrick:** Yeah, pretty much, you know, emails and, uh, you know, stuff like that.

**Joe Fitzpatrick:** Yeah. Well, that's great. So, uh, where can people find you at, uh, so you said your next conference is recon, on, uh, but where can people find you online and, and find out about where your next trainings are and everything.

**Joe Fitzpatrick:** So my website is securinghardware.com. I generally do my best to keep my latest trainings and keep, uh, links to all the presentations I've given, um, and videos when they're available on there. Um, and the upcoming group training is hardware security dot training. Um, and that's the, the joint training project between me, Joe Grand, uh, Colin O'Flynn and Dimitri Nadez-Pasov. Oh, and I'm, I'm secure, securely on Twitter.

**Joe Fitzpatrick:** That's great. Uh, yeah. And definitely, uh, you've, you've been sharing some great stuff on there. So, uh, uh, thank you for being on the show today. I really appreciate it. Uh, especially, uh, I know this is the last minute, so, uh, I appreciate your flexibility on that. And, uh, we'll hope to see you at conferences and talk to you soon. No problem. Thanks. Thanks for having me. Have a great day.

**Joe Fitzpatrick:** Bye.

**Speaker ?:** Bye. Bye. Bye.
